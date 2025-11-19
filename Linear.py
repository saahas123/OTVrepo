from machine import Pin, PWM
import time

# --- PIN SETUP ---
IN1 = Pin(17, Pin.OUT)      # direction pin 1
IN2 = Pin(16, Pin.OUT)      # direction pin 2
ENA = PWM(Pin(5))          # enable pin (PWM)
ENA.freq(1000)              # 1 kHz PWM

# --- HELPER FUNCTIONS ---
def stop():
    IN1.value(0)
    IN2.value(0)
    ENA.duty_u16(0)

def extend(speed=65535):
    IN1.value(1)
    IN2.value(0)
    ENA.duty_u16(speed)

def retract(speed=65535):
    IN1.value(0)
    IN2.value(1)
    ENA.duty_u16(speed)



