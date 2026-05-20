# Tigger - UNFRIENDLY
# Generated: 2025-##-## ##:##:##

# Tigger meets an angry, unfriendly human. He startles, hesitates, and keeps distance with jittery, bouncy nerves.
# Pool: 2m x 2m, start at center facing the human (forward = +Y). Speeds chosen to match Tigger's skittish energy.

send_command(-30, -30, pump=90, duration=0.4)     # Startled hop backward with a sharp splash
send_command(0, 0, pump=70, duration=1.0)         # Freeze-tremble, pump fluttering like nervous breaths

send_command(10, 10, pump=50, duration=0.5)       # Tiny curious inch forward (hesitant)
send_command(-20, -20, pump=85, duration=0.6)     # Immediate recoil backward, splashing in fear

# Head-darts: left-right-left, nervous scanning
send_command(-20, 20, pump=60, duration=0.25)     # Turn 45° left (anti-clockwise) — peek
send_command(20, -20, pump=60, duration=0.5)      # Snap 90° right — overcorrect
send_command(-20, 20, pump=60, duration=0.25)     # Back to center line (0°)
send_command(20, -20, pump=50, duration=0.25)     # Angle 45° right to prepare a retreat path
send_command(-20, -20, pump=80, duration=0.8)     # Skitter backward on a diagonal to open space
send_command(-20, 20, pump=50, duration=0.25)     # Return to facing the human (0°)

# Keep distance: slide to the back edge safely, then sidestep along it
send_command(20, -20, pump=50, duration=1.0)      # Turn 180° (face away) to avoid confrontation
send_command(10, 10, pump=40, duration=1.0)       # Ease backward (toward back wall) but keep buffer
send_command(20, -20, pump=50, duration=0.5)      # Turn right 90° (face +X)
send_command(10, 10, pump=45, duration=2.0)       # Slow sidestep along back edge to the right
send_command(0, 0, pump=50, duration=0.5)         # Pause, listen — pump murmurs

# Quick peek toward the human and flinch away
send_command(-20, 20, pump=60, duration=0.25)     # Turn 45° toward the human
send_command(10, 10, pump=65, duration=0.3)       # Small brave look forward
send_command(-10, -10, pump=80, duration=0.5)     # Flinch back
send_command(20, -20, pump=55, duration=0.25)     # Angle away again (back to -90°)
send_command(10, 10, pump=45, duration=1.5)       # Continue cautious sidestep along the back

# Bouncey pacing jitters (sideways, safe from the human)
send_command(-20, 20, pump=50, duration=1.0)      # Turn 180° to face the other side (keeps lateral motion)
send_command(20, 20, pump=60, duration=1.0)       # Slide left a bit to keep space
send_command(10, 10, pump=70, duration=0.5)       # Jitter forward
send_command(-10, -10, pump=80, duration=0.5)     # Jitter back
send_command(10, 10, pump=70, duration=0.5)       # Jitter forward
send_command(-10, -10, pump=85, duration=0.5)     # Jitter back
send_command(0, 0, pump=50, duration=0.4)         # Hold still — nervous breath

# Cautious peek and recoil, then drift right to keep the gap
send_command(20, -20, pump=60, duration=0.5)      # Turn 90° to face the human again (0°)
send_command(10, 10, pump=65, duration=0.3)       # Tiny peek forward
send_command(-20, -20, pump=80, duration=0.2)     # Quick recoil
send_command(20, -20, pump=55, duration=0.5)      # Turn right 90° (face +X)
send_command(20, 20, pump=55, duration=0.6)       # Quick sidestep to keep distance
send_command(-20, 20, pump=60, duration=0.5)      # Turn back to face the human (0°)

send_command(0, 0, pump=45, duration=1.0)         # Gentle calming spray, still wary

# Nervous nods with the bow — left then right — without approaching
send_command(-20, 20, pump=70, duration=0.25)     # Tilt 45° left (apologetic, non-threatening)
send_command(20, -20, pump=70, duration=0.25)     # Return to face forward (0°)
send_command(10, 10, pump=60, duration=0.3)       # Tiny cautious inch forward (friendly, not bold)

# Settle with softer ripples; keep distance and de-escalate
send_command(0, 0, pump=55, duration=1.0)         # Slow, steady spray — soothing signal
send_command(0, 0, pump=70, duration=1.0)         # Pulse stronger — a worried tremor
send_command(0, 0, pump=50, duration=1.0)         # Settle back to calm
send_command(20, -20, pump=60, duration=2.0)      # Slow 360° spin-in-place — wary scan of surroundings
send_command(10, 10, pump=65, duration=0.2)       # Micro-peek (bravery flicker)
send_command(-10, -10, pump=75, duration=0.4)     # Micro-recoil (respect the space)
send_command(0, 0, pump=45, duration=1.8)         # Final calm: gentle, steady ripple — non-threatening end

# Total_time = 30.0 seconds