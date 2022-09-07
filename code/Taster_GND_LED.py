# Bei Knopfdruck Board-LED umschalten
from picozero import Button, pico_led
from time import sleep

pico_led.off()
button = Button(0) #GPIO 0

def button_toggle():
    pico_led.toggle()

button.when_pressed = button_toggle

while True:
    sleep(0.2)