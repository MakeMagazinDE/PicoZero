# LED_puls.py
from picozero import LED
from time import sleep

led = LED(15)

while 1:
    for i in range(0,100):
        led.brightness = i/100.0
        sleep(0.01)   
    for i in range(100,0,-1):
        led.brightness = i/100.0
        sleep(0.01)   
