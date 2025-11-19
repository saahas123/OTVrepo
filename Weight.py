from machine import ADC, Pin
import time

# ADC pin (replace with your actual pin)
fsr_adc = ADC(Pin(32))
fsr_adc.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V

# Fixed resistor in voltage divider (Ohms)
R_FIXED = 10000  # 10kΩ, adjust if needed

def read_fsr_series():
    adc = fsr_adc.read()  # 0-4095
    voltage = adc / 4095 * 3.3  # convert ADC value to volts
    
    if voltage == 0:
        fsr_res = float('inf')
    else:
        fsr_res = R_FIXED * (3.3 / voltage - 1)  # total resistance of both FSRs in series
    
    return adc, fsr_res



