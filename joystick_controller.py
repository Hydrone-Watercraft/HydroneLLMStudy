"""
joystick_controller.py
-----------------------
Controls the Hydrone aquatic robot via a Logitech Extreme 3D Pro joystick.
Discovers the robot on the local network using UDP broadcast, then streams
thruster/pump commands over TCP.

Joystick buttons 6-11 can also trigger pre-generated LLM character scripts
from the LLM_Generated_Character_Scripts/ folder.
"""

import os
import pygame
import asyncio
import json
import socket
import time
import sys

# ---- Joystick Setup ----
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected to: {joystick.get_name()}")

# ---- Button Mapping (Logitech Extreme 3D Pro) ----
BUTTON_TRIGGER = 0   # Full pump on
BUTTON_THUMB   = 1   # Pump off
BUTTON_EXIT    = 2   # Close connection and exit

HAT_INDEX      = 0   # D-pad index

# ---- Network Config ----
PORT            = 5000
DISCOVERY_PORT  = 5001
DISCOVERY_MAGIC = b"HYDRONE_DISCOVERY_V1"
TARGET_NAME     = "atom_s3_1"   # Change to match your device name
DISCOVERY_TIMEOUT = 2.0

# ---- Motion Config ----
LEFT_CORRECTION  = 1     # Multiply left thruster by this to correct hardware asymmetry
DEADZONE         = 0.15  # Ignore joystick axis values below this threshold
MAX_VAL          = 30    # Maximum thruster command value
REFRESH_INTERVAL = 0.2   # Minimum seconds between repeated identical commands

# ---- Button-to-Script Mapping ----
# Maps joystick button index -> script index in the sorted script folder
CHARACTER_BUTTONS = {
    6:  0,  # pooh_friendly
    7:  1,  # pooh_unfriendly
    8:  2,  # tigger_friendly
    9:  3,  # tigger_unfriendly
    10: 4,  # eeyore_friendly
    11: 5,  # eeyore_unfriendly
}

# ================== NETWORK HELPERS ==================

def _guess_broadcast_addrs():
    """Return a list of broadcast addresses to try during UDP discovery."""
    addrs = {"255.255.255.255"}
    try:
        t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        t.connect(("8.8.8.8", 80))
        local_ip = t.getsockname()[0]
        t.close()
        parts = local_ip.split(".")
        if len(parts) == 4:
            addrs.add(".".join(parts[:3] + ["255"]))
    except Exception:
        pass
    return list(addrs)


def discover_atoms(timeout=DISCOVERY_TIMEOUT):
    """Broadcast a discovery packet and collect responding Hydrone devices."""
    found = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.2)

    bcasts = _guess_broadcast_addrs()
    print(f"Sending discovery broadcast to: {bcasts}")

    for bcast in bcasts:
        try:
            s.sendto(DISCOVERY_MAGIC, (bcast, DISCOVERY_PORT))
        except Exception:
            pass

    start = time.time()
    while time.time() - start < timeout:
        try:
            data, addr = s.recvfrom(512)
        except socket.timeout:
            continue
        except Exception:
            continue

        try:
            info = json.loads(data.decode(errors="ignore").strip())
            if isinstance(info, dict) and info.get("ip") and info.get("port") is not None:
                key = info.get("id") or info.get("name") or info.get("ip")
                found[key] = info
        except Exception:
            pass

    s.close()

    if found:
        print(f"Discovery complete: found {len(found)} device(s).")
    else:
        print("Discovery complete: no devices found.")

    return list(found.values())


def pick_target(devices, target_name=TARGET_NAME):
    """Select a device by name, or fall back to the first discovered device."""
    if not devices:
        return None
    if target_name:
        for d in devices:
            if d.get("name") == target_name:
                return d
    return devices[0]


# ================== MOTION HELPERS ==================

def apply_deadzone(v, dz=DEADZONE):
    return 0 if abs(v) < dz else v

def map_val(v, in_min, in_max, out_min, out_max):
    return (v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def significant_change(new, prev):
    """Return True if the new command differs enough from the previous one to send."""
    if abs(new["pump"] - prev.get("pump", -999)) >= 2:
        return True
    if new["left"] != prev.get("left") or new["right"] != prev.get("right"):
        return True
    return False


# ================== DRONE COMMANDS ==================

def send_command(sock, left, right, pump=0, duration=1.0, stop_after=True):
    """Send a timed thruster/pump command, optionally followed by a stop."""
    corrected_left  = int(left  * LEFT_CORRECTION)
    corrected_right = int(right)

    # Zero out sub-threshold values to avoid unintended drift
    corrected_left  = corrected_left  if abs(corrected_left)  >= 1 else 0
    corrected_right = corrected_right if abs(corrected_right) >= 1 else 0

    cmd = {"left": corrected_left, "right": corrected_right, "pump": pump}
    sock.sendall((json.dumps(cmd) + "\n").encode())
    time.sleep(duration)

    if stop_after:
        stop_cmd = {"left": 0, "right": 0, "pump": 0}
        sock.sendall((json.dumps(stop_cmd) + "\n").encode())


def turn_by(sock, angle_deg, turn_speed=30):
    """Send a relative turn command (angle in degrees)."""
    cmd = {"turn": angle_deg, "turn_speed": turn_speed}
    sock.sendall((json.dumps(cmd) + "\n").encode())
    print(f"[PC] Sent turn: {angle_deg} deg at speed {turn_speed}")


# ================== SCRIPT RUNNER ==================

def list_scripts(folder):
    """Return sorted lists of display names and real filenames from the script folder."""
    files      = sorted([f for f in os.listdir(folder) if f.endswith(".py") and "_" in f])
    numbered   = [f"{i + 1}_{files[i]}" for i in range(len(files))]
    return numbered, files


def run_script(filepath, sock):
    """
    Execute a pre-generated LLM motion script.

    NOTE: exec() is intentionally used here to run pre-generated scripts.
    Only run scripts from your own trusted generated folder.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    try:
        exec(
            code,
            {
                "send_command": lambda *a, **k: send_command(sock, *a, **k),
                "turn_by":      lambda *a, **k: turn_by(sock, *a, **k),
            }
        )
    except Exception as e:
        print(f"Error running script {filepath}: {e}")


# ================== JOYSTICK HANDLER ==================

async def joystick_handler(sock):
    prev      = {}
    last_send = 0
    running   = True

    folder = "LLM_Generated_Character_Scripts"
    numbered_scripts, real_scripts = list_scripts(folder)

    while running:
        pygame.event.pump()

        # --- Exit ---
        if joystick.get_button(BUTTON_EXIT):
            print("Exit button pressed. Closing connection.")
            running = False
            break

        # --- Character script buttons ---
        for btn, idx in CHARACTER_BUTTONS.items():
            if joystick.get_button(btn) and idx < len(real_scripts):
                display_name = numbered_scripts[idx]
                filepath     = os.path.join(folder, real_scripts[idx])
                print(f"\nRunning: {display_name} (button {btn})\n")
                run_script(filepath, sock)

        # --- D-pad overrides ---
        hat_x, hat_y = joystick.get_hat(HAT_INDEX)
        override = False

        if hat_x == -1:       # rotate left
            left, right = -MAX_VAL, MAX_VAL
            override = True
        elif hat_x == 1:      # rotate right
            left, right = MAX_VAL, -MAX_VAL
            override = True
        elif hat_y == 1:      # forward
            left, right = MAX_VAL, MAX_VAL
            override = True
        elif hat_y == -1:     # backward
            left, right = -MAX_VAL, -MAX_VAL
            override = True
        else:
            # Main joystick axes: axis 2 = forward/back, axis 1 = turn
            fwd  = -apply_deadzone(joystick.get_axis(2))
            turn =  apply_deadzone(joystick.get_axis(1))
            raw_l = -(fwd + turn) * 100
            raw_r =  (fwd - turn) * 100
            left  = int(map_val(raw_l, -100, 100, -MAX_VAL, MAX_VAL))
            right = int(map_val(raw_r, -100, 100, -MAX_VAL, MAX_VAL))

        # --- Pump control ---
        axis_pump = joystick.get_axis(3)
        trigger   = joystick.get_button(BUTTON_TRIGGER)
        thumb     = joystick.get_button(BUTTON_THUMB)

        if trigger:
            pump = 100
        elif thumb:
            pump = 0
        else:
            raw_pump = int(clamp(map_val(axis_pump, -1, 1, 100, 0), 0, 100))
            if raw_pump == 0:
                pump = 0
            elif raw_pump == 1:
                pump = 15
            else:
                pump = int(map_val(raw_pump, 1, 100, 20, 100))

        # --- Send if state changed or refresh interval elapsed ---
        state = {"left": left, "right": right, "pump": pump}
        now   = time.time()

        if significant_change(state, prev) or (now - last_send) > REFRESH_INTERVAL:
            sock.sendall((json.dumps(state) + "\n").encode())
            print(
                f"Hydrone <- left={left:+3d}  right={right:+3d}  pump={pump:3d}"
                f"{'  [D-pad override]' if override else ''}"
            )
            prev      = state
            last_send = now

        await asyncio.sleep(0.01)

    sock.close()
    print("Connection closed.")


# ================== MAIN ==================

async def main():
    while True:
        sock = None
        try:
            devices = discover_atoms()
            if not devices:
                raise RuntimeError("No Hydrone device found via UDP discovery.")

            print("\nDiscovered devices:")
            for d in devices:
                print(f"  name={d.get('name')}  ip={d.get('ip')}  port={d.get('port')}")

            target = pick_target(devices, TARGET_NAME)
            if not target:
                raise RuntimeError(f"Target device '{TARGET_NAME}' not found.")

            ip   = target["ip"]
            port = int(target.get("port", PORT))

            print(f"\nConnecting to {ip}:{port}  (name={target.get('name')}) ...")
            sock = socket.create_connection((ip, port), timeout=5)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            print("Connected.\n")

            await joystick_handler(sock)
            break

        except Exception as e:
            print(f"Error: {e}. Retrying in 1 s ...")
            try:
                if sock:
                    sock.close()
            except Exception:
                pass
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())