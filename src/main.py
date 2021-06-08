#

from machine import Pin
import utime
x = 0  # control variable
y = 0  # control variabel
steps = 0  # steps counter
voltas = 1
speed = 2  # regulates the speed(the lower the faster)
time_open_s = 5
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
    global steps
    global steps_gone
    global t

    utime.sleep_ms(500)

    for j in range(int(steps-steps_gone)):
        spin(CLOCK)
        steps_gone += 1
        if steps_gone == steps:
            return None

        if button_right.value() == 0 or button_left.value() == 0:
            utime.sleep_ms(500)
            return None

    return None


t = 0
button_right = Pin(22, Pin.IN, Pin.PULL_UP)
button_left = Pin(19, Pin.IN, Pin.PULL_UP)
red_led = Pin(5, Pin.IN, Pin.PULL_UP)
yellow_led = Pin(9, Pin.IN, Pin.PULL_UP)
green_led = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    while x == 0:
        y = 0
        if button_left.value() == 0:  # when left button pressed opens the gate fully
            y = 1
            utime.sleep_ms(500)  # small delay to start spinning
            for j in range(int(voltas*509)):
                spin(A_CLOCK)
                steps += 1
                if button_left.value() == 0:  # if left button pressed stops
                    break

        x = 1

        while button_right.value() == 0:        # while the right button is pressed it opens
            y = 1
            spin(A_CLOCK)
            steps += 1
            if button_right.value() == 1:
                x = 1  # when released changes state
    while x == 1:
        y = 0
        t = utime.time()
        while steps != steps_gone:
            y = 1
            utime.sleep_ms(500)

            if button_right.value() == 0 or button_left.value() == 0:
                utime.sleep_ms(500)
                stop_go()
                t = utime.time()

            if utime.time()-t == time_open_s:
                stop_go()
                t = utime.time()

        x = 0
        steps = 0
        steps_gone = 0

# https://components101.com/motors/28byj-48-stepper-motor
