from machine import Pin, PWM
from time import sleep

# --- LEFT SIDE MOTORS (Channel A on H-Bridge) ---
in1 = Pin(13, Pin.OUT)
in2 = Pin(14, Pin.OUT)
ena = PWM(Pin(12))   # enable pin for left motors
ena.freq(1000)

# --- RIGHT SIDE MOTORS (Channel B on H-Bridge) ---
in3 = Pin(25, Pin.OUT)
in4 = Pin(26, Pin.OUT)
enb = PWM(Pin(27))   # enable pin for right motors
enb.freq(1000)



# --- MOTOR CONTROL FUNCTIONS ---
def left_forward(speed):
    """Move both left motors forward"""
    in1.value(1)
    in2.value(0)
    ena.duty_u16(int(speed * 65535 / 100))

def left_backward(speed):
    """Move both left motors backward"""
    in1.value(0)
    in2.value(1)
    ena.duty_u16(int(speed * 65535 / 100))

def right_forward(speed):
    """Move both right motors forward"""
    in3.value(1)
    in4.value(0)
    enb.duty_u16(int(speed * 65535 / 100))

def right_backward(speed):
    """Move both right motors backward"""
    in3.value(0)
    in4.value(1)
    enb.duty_u16(int(speed * 65535 / 100))

def stop_all():
    """Stop all motors"""
    in1.value(0)
    in2.value(0)
    ena.duty_u16(0)
    in3.value(0)
    in4.value(0)
    enb.duty_u16(0)

# --- MOVEMENT COMBINATIONS ---
def move_forward(speed):
    left_forward(speed)
    right_forward(speed)

def move_backward(speed):
    left_backward(speed)
    right_backward(speed)

def turnLeft(speed):
    left_backward(speed)
    right_forward(speed)

def turnRight(speed):
    left_forward(speed)
    right_backward(speed)
    
    

