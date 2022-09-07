# Ansicht/Drucken -> Plotter in Thonny
# gibt die Tempetarur des RP2040-Chips aus

from time import sleep
from picozero import pico_temp_sensor, pico_led, PWMLED

pico_led.blink()

led=PWMLED(15)
led.pulse()

while True:
    print(0,pico_temp_sensor.temp) # erster Wert nur als "Nullline"
    sleep(0.5)