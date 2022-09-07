# Helligkeit einer ext. LED sinusförmige Helligkeit
from time import sleep
from picozero import LED
from math import sin, radians

led = LED(15) # GPIO 15

while True:
    for i in range(360):
        angle = radians(i)
        led.brightness = 0.5 + 0.5 * sin(angle)
        sleep(0.01)