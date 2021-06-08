#

from machine import Pin
import utime
x = 0  # control variable
steps_count = 0  # steps counter
voltas = 2
speed = 2  # regulates the speed(the lower the faster)
time_open_s = 10
steps_gone = 0
In1 = Pin(13, Pin.OUT)
In2 = Pin(12, Pin.OUT)
In3 = Pin(14, Pin.OUT)
In4 = Pin(27, Pin.OUT)

A_CLOCK = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [
    0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1]]  # Imputs for the 28BYJ-48 spin anticlockwise

CLOCK = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [
    0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]  # Imputs for the 28BYJ-48 spin clockwise


def spin(sentido):
    for i in sentido:
        In1.value(i[0])
        In2.value(i[1])
        In3.value(i[2])
        In4.value(i[3])
        utime.sleep_ms(speed)
    In1.value(0)
    In2.value(0)
    In3.value(0)
    In4.value(0)


def stop_go():
    if button_right.value() == 0 or button_left.value() == 0:       # c
        for j in range(int(steps_count - steps_gone)):
            spin(CLOCK)
            steps_gone += 1
            if button_right.value() == 0 or button_left.value() == 0:
                stop_go()
        x = 0
        steps_count = 0
    if utime.time()-t == time_open_s:
        for j in range(int(steps_count - steps_gone)):
            spin(CLOCK)
            steps_gone += 1
            if button_right.value() == 0 or button_left.value() == 0:
                stop_go()
        x = 0
        steps_count = 0


"""
# 509 repeat the process enough to turn ~360 degrees, 1018 ~= 720 and so on
for j in range(int(voltas*509)):
    for i in A_CLOCK:
        In1.value(i[0])
        In2.value(i[1])
        In3.value(i[2])
        In4.value(i[3])
        utime.sleep_ms(2)  # regulates the speed(the lower the faster)
In1.value(0)
In2.value(0)
In3.value(0)
In4.value(0)
"""
t = 0
button_right = Pin(22, Pin.IN, Pin.PULL_UP)
button_left = Pin(19, Pin.IN, Pin.PULL_UP)

while True:
    while x == 0:
        steps_gone = 0
        if button_left.value() == 0:  # when left button pressed opens the gate fully
            utime.sleep_ms(500)  # small delay to start spinning
            for j in range(int(voltas*509)):
                spin(A_CLOCK)
                steps += 1
                if button_left.value() == 0:  # if left button pressed stops
                    t = utime.time()
                    break

        x = 1

        while button_right.value() == 0:        # while the right button is pressed it opens
            spin(A_CLOCK)
            steps += 1
            if button_right.value() == 1:
                x = 1  # when released changes state
                t = utime.time()
    while x == 1:
        utime.sleep_ms(500)
        stop_go()

# https://components101.com/motors/28byj-48-stepper-motor
