from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.off()
    print ("The light is switched OFF")
    sleep(300.0)