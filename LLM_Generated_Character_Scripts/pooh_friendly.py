# Winnie the Pooh - FRIENDLY
# Generated: 2025-##-## ##:##:##

# Winnie-the-Pooh sees a friendly, kind human. He ambles forward with warm curiosity, hums, splashes gently like sharing honey-joy, and settles close with trust.
# Pool: 2m x 2m, start centered facing the human. Gentle, cozy speeds for Pooh (mostly 12–20). Distances computed from examples (speed 20 ≈ 0.4 m/s).

send_command(20, 20, pump=40, duration=1.0, stop_after=True)   # Soft approach of ~0.4 m (curious but calm)

send_command(0, 0, pump=40, duration=1.0, stop_after=True)     # A comfy pause, Pooh "sniffs" the friendly air

# Curious head tilts (left, right, left) while keeping close
send_command(-20, 20, pump=50, duration=0.25, stop_after=True) # Tilt left ~45°
send_command(20, -20, pump=50, duration=0.5, stop_after=True)  # Tilt right ~90°
send_command(-20, 20, pump=50, duration=0.25, stop_after=True) # Return ~45° to center

# Gentle sway arcs that barely advance, like a shy sidestep around a honey pot
send_command(18, 12, pump=60, duration=0.6, stop_after=True)   # Clockwise arc (~0.18–0.2 m path)
send_command(12, 18, pump=60, duration=0.6, stop_after=True)   # Counterclockwise arc (~0.18–0.2 m path)

# Joyful twirl with a cheerful splash — but not too wild, it's Pooh
send_command(20, -20, pump=100, duration=2.0, stop_after=True) # 360° spin, happy fountain

# Gentle "bounce" of joy (rocking forward-back), staying in place overall
send_command(20, 20, pump=80, duration=0.5, stop_after=True)   # +0.2 m
send_command(-20, -20, pump=60, duration=0.5, stop_after=True) # -0.2 m
send_command(20, 20, pump=80, duration=0.5, stop_after=True)   # +0.2 m
send_command(-20, -20, pump=60, duration=0.5, stop_after=True) # -0.2 m

# Small, trusting step closer, then a tiny bow back
send_command(20, 20, pump=70, duration=0.25, stop_after=True)  # +0.1 m
send_command(-20, -20, pump=50, duration=0.125, stop_after=True) # -0.05 m (a polite nod)

send_command(0, 0, pump=40, duration=2.0, stop_after=True)     # Contented stillness, humming softly

# More curious side-to-side arcs (balanced so he stays near the friendly face)
send_command(18, 12, pump=55, duration=0.6, stop_after=True)   # Arc right
send_command(12, 18, pump=55, duration=0.6, stop_after=True)   # Arc left
send_command(18, 12, pump=55, duration=0.6, stop_after=True)   # Arc right
send_command(12, 18, pump=55, duration=0.6, stop_after=True)   # Arc left

send_command(-20, -20, pump=40, duration=0.25, stop_after=True) # Tiny backward adjust (~0.1 m) to keep safe space
send_command(0, 0, pump=30, duration=0.5, stop_after=True)     # Calm breath

send_command(18, 12, pump=55, duration=0.6, stop_after=True)   # Arc right
send_command(12, 18, pump=55, duration=0.6, stop_after=True)   # Arc left

# Pooh hums and sways — gentle rhythmic tilts with soft fountain
send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Left 45°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(20, -20, pump=60, duration=0.5, stop_after=True)  # Right 90°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Left 45° (centered again)

send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Sway set 2: Left 45°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(20, -20, pump=60, duration=0.5, stop_after=True)  # Right 90°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Left 45° (centered again)

send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Sway set 3: Left 45°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(20, -20, pump=60, duration=0.5, stop_after=True)  # Right 90°
send_command(0, 0, pump=50, duration=0.5, stop_after=True)     # Hum-pulse
send_command(-20, 20, pump=40, duration=0.25, stop_after=True) # Left 45° (centered again)

# Final warm approach and joyful fountain "hello"
send_command(20, 20, pump=80, duration=0.375, stop_after=True) # ~+0.15 m
send_command(0, 0, pump=100, duration=1.0, stop_after=True)    # Big happy splash

send_command(20, -20, pump=90, duration=2.0, stop_after=True)  # Gentle 360° celebratory twirl
send_command(0, 0, pump=40, duration=1.0, stop_after=True)     # Cozy pause, smiling at the friend

# Closing: balanced little strolls that cancel each other, staying near and calm
send_command(12, 18, pump=45, duration=0.7, stop_after=True)   # Arc left
send_command(18, 12, pump=45, duration=0.7, stop_after=True)   # Arc right
send_command(12, 18, pump=45, duration=0.7, stop_after=True)   # Arc left
send_command(18, 12, pump=45, duration=0.7, stop_after=True)   # Arc right

send_command(0, 0, pump=35, duration=1.9, stop_after=True)     # Settled companionship, soft trickle fountain

# Total_time = 30.0 seconds