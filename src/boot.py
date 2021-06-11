# ligh signal of booting up
from machine import Pin
import utime

x = 0

red_led = Pin(5, Pin.OUT)
yellow_led = Pin(9, Pin.OUT)
green_led = Pin(10, Pin.OUT)

red_led.value(True)
utime.sleep_ms(500)
yellow_led.value(True)
utime.sleep_ms(500)
red_led.value(False)
green_led.value(True)
utime.sleep_ms(500)
yellow_led.value(False)
utime.sleep_ms(500)
green_led.value(False)
utime.sleep_ms(500)
red_led.value(True)
yellow_led.value(True)
green_led.value(True)
utime.sleep_ms(500)
while x < 5:  # x has to be odd
    red_led.value(not red_led.value())
    yellow_led.value(not yellow_led.value())
    green_led.value(not green_led.value())
    x += 1
    utime.sleep_ms(500)
red_led.value(True)
