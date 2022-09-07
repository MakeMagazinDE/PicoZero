# Ansicht/Drucken -> Plotter in Thonny
from time import sleep
from picozero import Pot

pot = Pot(0) # ADC0 ! (an Pin 31)

while True:
    print(0.0,pot.value)
    sleep(0.1)
    