# dummer Rover.py
from picozero import Robot, Button, pico_led
from time import sleep

rover = Robot(left=(18,19), right=(20,21))
button = Button(0)

def button_toggle():
    pico_led.toggle()        
        

button.when_pressed = button_toggle

while 1:
    if pico_led.value:
        rover.forward(t=3, wait=True)
    if pico_led.value:
        rover.left(t=0.65, wait=True)
        sleep(1)
    else:
        sleep(.5)