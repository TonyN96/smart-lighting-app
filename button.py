#!/usr/bin/python3

# Script used for changing state of LED using tacticle push button

import light
from gpiozero import Button
from time import sleep

button = Button(22)

while True:
    button.wait_for_press()
    light.light_switch()
    sleep(0.5)