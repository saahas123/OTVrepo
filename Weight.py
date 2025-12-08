from machine import ADC, Pin
import time

# Initialize ADC on pin A0 (or GP26 on Pico)
adc = ADC(Pin(26))   # Change pin number to the correct ADC pin for your board

while True:
    total = 0
    samples = 0
    start = time.ticks_ms()

    # Collect readings for 5 seconds
    while time.ticks_diff(time.ticks_ms(), start) < 5000:
        reading = adc.read_u16()   # 0–65535 on most boards
        total += reading
        samples += 1
        time.sleep_ms(10)          # ~100 samples/sec (optional)

    # Compute average
    average = total / samples

    print("Average reading over 5 seconds:", average)

    time.sleep(1)   # Wait before next cycle
