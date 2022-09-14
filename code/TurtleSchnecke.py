# Python Picozero Turtle
from picozero import Robot, Button, pico_led
from time import sleep

rover = Robot(left=(18,19), right=(20,21))
button = Button(0)

def button_toggle():
    pico_led.toggle()
        

button.when_pressed = button_toggle

stp  = 1.0     # Seitenlänge Quadrat
ts90 = 0.882   # Zeit für 90° Drehung, sehr hardwareabhängig!

def turn(winkel):
    if pico_led.value:
        if winkel>0.0:
            rover.left(t=ts90/90.0*winkel, wait=True)
        else:
            rover.right(t=ts90/90.0*abs(winkel), wait=True)            
    else:
        sleep(1)

def fwd(strecke):
    if pico_led.value:
        rover.forward(t=strecke/10.0, wait=True)
    else:
        sleep(1)
    
while not(pico_led.value):
    print(".")
    sleep(1)

# "Schnecke" aus Quadraten wie im Video
while 1:
    fwd(1+stp)
    sleep(0.1)
    turn(90)
    sleep(0.1)
    fwd(1+stp)
    sleep(0.1)
    turn(90)
    sleep(0.1)
    fwd(1+stp)
    sleep(0.1)
    turn(90)
    sleep(0.1)
    fwd(1+stp)
    sleep(0.1)
    turn(80)
    sleep(0.1)
    #turn(45)
    stp=stp*1.07