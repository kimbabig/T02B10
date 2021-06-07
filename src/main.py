#

from machine import Pin
import utime

voltas = 2

In1 = Pin(13, Pin.OUT)
In2 = Pin(12, Pin.OUT)
In3 = Pin(14, Pin.OUT)
In4 = Pin(27, Pin.OUT)
STEP = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [
    0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1]]  # Imputs for the 28BYJ-48 spin

# 509 repeat the process enough to turn ~360 degrees, 1018 ~= 720 and so on
for j in range(int(voltas*509)):
    for i in STEP:
        In1.value(i[0])
        In2.value(i[1])
        In3.value(i[2])
        In4.value(i[3])
        utime.sleep_ms(2)  # regulates the speed(the lower the faster)
In1.value(0)
In2.value(0)
In3.value(0)
In4.value(0)
