from enes100 import enes100
import time

# Initialize connection to the ENES100 Vision System
enes100.begin("theDropouts", "MATERIALS", 522, 1120)

# Confirm connection
while not enes100.is_connected():
    print("Waiting for connection to Vision System...")
    time.sleep(1)

print("Connected to Vision System!")

# Main loop
while True:
    if enes100.is_visible:  # Boolean, not a function
        print("Marker visible!")
        print("X =", enes100.x)
        print("Y =", enes100.y)
        print("Theta =", enes100.theta)
    else:
        print("Marker not visible.")
    
    time.sleep(1)
