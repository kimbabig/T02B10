# boot.py - - runs on boot-up
from machine import Pin

red_led = Pin(5, Pin.OUT)
yellow_led = Pin(9, Pin.OUT)
green_led = Pin(10, Pin.OUT)

red_led.value(True)
