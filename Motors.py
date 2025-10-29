from machine import Pin, PWM
from enes100 import enes100
enes100.begin("dropouts", "Material", )

# --- Left Motors (Channel A) ---
in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)
ena = PWM(Pin(4))
ena.freq(1000)

# --- Right Motors (Channel B) ---
in3 = Pin(5, Pin.OUT)
in4 = Pin(6, Pin.OUT)
enb = PWM(Pin(7))
enb.freq(1000)
def left_forward(speed):
    in1.value(1)
    in2.value(0)
    ena.duty_u16(int(speed * 65535 / 100))

def left_backward(speed):
    in1.value(0)
    in2.value(1)
    ena.duty_u16(int(speed * 65535 / 100))

def right_forward(speed):
    in3.value(1)
    in4.value(0)
    enb.duty_u16(int(speed * 65535 / 100))

def right_backward(speed):
    in3.value(0)
    in4.value(1)
    enb.duty_u16(int(speed * 65535 / 100))

def stop_all():
    in1.value(0); in2.value(0); ena.duty_u16(0)
    in3.value(0); in4.value(0); enb.duty_u16(0)
    
def move_forward(speed):
    left_forward(speed)
    right_forward(speed)


def turnLeft(target_angle, tolerance=0.05):
    """Turn left until within tolerance of target_angle."""
    print(f"Turning left to {target_angle}°")
    current_angle = enes100.theta()
    left_backward(30)
    right_forward(30)
    while abs(current_angle - target_angle) > tolerance:
        
        current_angle = enes100.theta()
        print(f"Current angle: {current_angle}")

    stop_all()
    print("Turn left complete!\n")


def turnRight(target_angle, tolerance=0.05):
    """Turn right until within tolerance of target_angle."""
    print(f"Turning right to {target_angle}°")
    current_angle = enes100.theta()
        left_forward(30)
        right_backward(30)
    while abs(current_angle - target_angle) > tolerance:
        
        current_angle = enes100.theta()
        print(f"Current angle: {current_angle}")

    stop_all()
    print("Turn right complete!\n")


