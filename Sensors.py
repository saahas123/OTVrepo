from machine import Pin, time_pulse_us
import time

TRIG1 = Pin(2, Pin.OUT)
ECHO1 = Pin(3, Pin.IN)

# --- Sensor 2 Pins ---
TRIG2 = Pin(4, Pin.OUT)
ECHO2 = Pin(5, Pin.IN)
def get_distance(trig, echo):
    # Send a 10µs pulse
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Measure the time for the echo
    duration = time_pulse_us(echo, 1, 30000)  # timeout 30ms

    # Calculate distance (speed of sound = 34300 cm/s)
    distance = (duration / 2) * 0.0343
    return distance


# --- Functions for each sensor ---
def getUltra1():
    return get_distance(TRIG1, ECHO1)

def getUltra2():
    return get_distance(TRIG2, ECHO2)

