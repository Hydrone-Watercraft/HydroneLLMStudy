# Eeyore - UNFRIENDLY
# Generated: 2025-##-## ##:##:##

# Eeyore notices an angry, unfriendly human. He freezes, trembles, and slowly retreats with hesitant motions.
# Start at pool center, facing the human.

send_command(0, 0, pump=70, duration=2.0)  # Startled freeze with a worried plume
send_command(0, 0, pump=30, duration=1.0)  # Brief quiet stillness (pump off)
send_command(0, 0, pump=80, duration=1.0)  # A shakier burst—nervous

send_command(-10, -10, pump=70, duration=2.0)  # Slow, cautious retreat backward (~0.4 m)

send_command(10, -10, pump=50, duration=0.5)  # Turn slightly away (clockwise ~45°)
send_command(15, 10, pump=60, duration=2.0)   # Hesitant sidestep arc forward, trying not to offend (~0.5 m)

send_command(0, 0, pump=85, duration=1.5)  # Trembling pause—“Oh well…”
send_command(0, 0, pump=40, duration=0.5)  # Softer sigh

send_command(10, 10, pump=50, duration=0.5)   # Small apologetic nod forward (~0.1 m)
send_command(-10, -10, pump=60, duration=0.5) # And back again (~0.1 m)

send_command(10, -10, pump=50, duration=0.5)  # Another small turn away (clockwise ~45°, now facing right/east)
send_command(10, 10, pump=70, duration=1.5)   # Quiet drift away to the side (~0.3 m)

# Shivery, timid quivers—tiny back-and-forth motions
send_command(10, 10, pump=60, duration=0.3)   # forward ~0.06 m
send_command(-10, -10, pump=75, duration=0.3) # back ~0.06 m
send_command(10, 10, pump=60, duration=0.3)
send_command(-10, -10, pump=75, duration=0.3)
send_command(10, 10, pump=60, duration=0.3)
send_command(-10, -10, pump=75, duration=0.3)

send_command(0, 0, pump=75, duration=1.2)  # Quiet, worried stillness

send_command(-10, 10, pump=50, duration=1.0)  # Slow look back toward the human (anti-clockwise 90°, facing forward again)
send_command(10, 10, pump=45, duration=0.6)   # Tentative tiny step forward (~0.12 m), unsure
send_command(0, 0, pump=80, duration=0.9)     # Gulp… another tremble

send_command(-15, -15, pump=80, duration=3.0) # Deeper retreat (~0.9 m), staying cautious

send_command(10, 10, pump=50, duration=0.5)   # Regains a little space forward (~0.1 m)
send_command(0, 0, pump=60, duration=1.0)     # Settles

send_command(10, -10, pump=50, duration=1.0)  # Slow, uncertain half-look away (clockwise 90°)
send_command(-10, 10, pump=50, duration=1.0)  # Then back again (anti-clockwise 90°)

send_command(0, 0, pump=65, duration=1.5)     # Low, steady plume—resigned Eeyore sigh

# Final gentle sway—still afraid, but polite
send_command(10, 10, pump=55, duration=1.0)   # forward ~0.2 m
send_command(-10, -10, pump=60, duration=1.0) # back ~0.2 m
send_command(0, 0, pump=30, duration=1.0)     # quiet stillness (pump off)

# Total_time = 2.0+1.0+1.0 + 2.0 + 0.5+2.0 + 1.5+0.5 + 0.5+0.5 + 0.5+1.5
#            + 0.3+0.3+0.3+0.3+0.3+0.3 + 1.2 + 1.0+0.6+0.9 + 3.0 + 0.5+1.0
#            + 1.0+1.0 + 1.5 + 1.0+1.0 + 1.0
#            = 30.0 seconds