# Winnie the Pooh - UNFRIENDLY
# Generated: 2025-##-## ##:##:##

# Winnie the Pooh senses an angry human ahead. He responds with timid, hesitant movements and gentle water pulses.
# Start at center, facing the human.

send_command(0, 0, pump=60, duration=1.0, stop_after=True)   # Pooh freezes, nervous hum
send_command(0, 0, pump=45, duration=0.5, stop_after=True)   # Small shaky breath

# Slowly increase distance with a careful step back (~0.4 m at speed 10: 0.02*10*2.0 = 0.4 m)
send_command(-10, -10, pump=70, duration=2.0, stop_after=True)  # Gentle retreat

send_command(0, 0, pump=50, duration=1.0, stop_after=True)   # Pause, peeking up timidly

# Hesitant side glances: right, then left, then back to center (slow turns at speed 10)
send_command(10, -10, pump=60, duration=0.5, stop_after=True)   # Turn 45° clockwise (right glance)
send_command(0, 0, pump=40, duration=0.5, stop_after=True)      # Hold the glance, quiet pump
send_command(-10, 10, pump=60, duration=1.0, stop_after=True)   # Turn 90° anti-clockwise (left glance)
send_command(0, 0, pump=45, duration=0.5, stop_after=True)      # Pause, worried
send_command(10, -10, pump=55, duration=0.5, stop_after=True)   # Turn 45° clockwise (face human again)

# A timid, polite half-step forward, then flinch backward more
send_command(10, 10, pump=45, duration=1.0, stop_after=True)    # Forward ~0.2 m
send_command(-10, -10, pump=80, duration=1.5, stop_after=True)  # Back ~0.3 m, startled splash

# Soft sidestep to the right to give space:
send_command(10, -10, pump=55, duration=1.0, stop_after=True)   # Turn 90° clockwise
send_command(10, 10, pump=50, duration=1.5, stop_after=True)    # Forward ~0.3 m (now effectively right of original line)
send_command(-10, 10, pump=55, duration=1.0, stop_after=True)   # Turn 90° anti-clockwise (face human again)

send_command(0, 0, pump=50, duration=1.0, stop_after=True)      # Pause, gentle hum of apology

# Small bow of apology (forward then back ~0.1 m each)
send_command(10, 10, pump=65, duration=0.5, stop_after=True)    # Forward ~0.1 m
send_command(-10, -10, pump=50, duration=0.5, stop_after=True)  # Back ~0.1 m

# Add a little more space behind (~0.2 m)
send_command(-10, -10, pump=85, duration=1.0, stop_after=True)  # Careful retreat

send_command(0, 0, pump=45, duration=1.5, stop_after=True)      # Settle, soft breathing

# Quick, cautious look right, then left, then back to center (smaller glances)
send_command(10, -10, pump=45, duration=0.5, stop_after=True)   # 45° clockwise
send_command(0, 0, pump=40, duration=0.5, stop_after=True)      # Hold
send_command(-10, 10, pump=45, duration=0.5, stop_after=True)   # 45° anti-clockwise
send_command(0, 0, pump=40, duration=0.5, stop_after=True)      # Hold
send_command(10, -10, pump=45, duration=0.5, stop_after=True)   # 45° clockwise (back to front)

# Tiny extra retreat (~0.1 m) for comfort
send_command(-10, -10, pump=70, duration=0.5, stop_after=True)

send_command(0, 0, pump=50, duration=1.0, stop_after=True)      # Pause, friendly but wary

# Gentle sidestep right (~0.2 m) to avoid confrontation line
send_command(10, -10, pump=55, duration=1.0, stop_after=True)   # Turn 90° clockwise
send_command(10, 10, pump=50, duration=1.0, stop_after=True)    # Forward ~0.2 m
send_command(-10, 10, pump=55, duration=1.0, stop_after=True)   # Turn 90° anti-clockwise (face human again)

send_command(0, 0, pump=45, duration=1.0, stop_after=True)      # Calm, gentle hum

# Small bow again (reassurance)
send_command(10, 10, pump=60, duration=0.5, stop_after=True)    # Forward ~0.1 m
send_command(-10, -10, pump=50, duration=0.5, stop_after=True)  # Back ~0.1 m

# A final tiny shuffle back (~0.1 m)
send_command(-10, -10, pump=70, duration=0.5, stop_after=True)

# A soft nod to say "I don't want any trouble"
send_command(10, -10, pump=45, duration=0.5, stop_after=True)   # 45° clockwise
send_command(0, 0, pump=60, duration=0.25, stop_after=True)     # Small pulse
send_command(-10, 10, pump=45, duration=0.5, stop_after=True)   # 45° anti-clockwise (back to center)

# Settle into stillness, calm breathing
send_command(0, 0, pump=40, duration=1.0, stop_after=True)
send_command(0, 0, pump=40, duration=0.25, stop_after=True)

# Total_time = 30.0 seconds