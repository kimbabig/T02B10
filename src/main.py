#

from machine import Pin
import utime
x = 0  # control variable
steps = 0  # steps counter
voltas = 1  # number of full turns to fully open
speed = 2  # regulates the speed(the lower the faster)
time_open_s = 5  # time to remain open before closing automatically
steps_gone = 0  # number of steps already closed

In1 = Pin(13, Pin.OUT)  # azul
In2 = Pin(12, Pin.OUT)  # verde
In3 = Pin(14, Pin.OUT)  # amarelo
In4 = Pin(27, Pin.OUT)  # laranja

A_CLOCK = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [
    0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1]]  # Imputs for the 28BYJ-48 spin anticlockwise

CLOCK = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [
    0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]  # Imputs for the 28BYJ-48 spin clockwise


def spin(sentido):  # funtion that makes the 28BYJ-48 spin
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


def stop_go():      # function to control the closing
    global steps
    global steps_gone
    global t

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

red_led = Pin(5, Pin.OUT)
yellow_led = Pin(9, Pin.OUT)
green_led = Pin(10, Pin.OUT)

while True:
    while x == 0:
        if button_left.value() == 0:  # when left button pressed opens the gate fully
            red_led.value(False)
            yellow_led.value(True)
            # small delay to start spinning to avoid double button press detection
            utime.sleep_ms(500)
            for j in range(int(voltas*509)):
                spin(A_CLOCK)
                steps += 1
                if button_left.value() == 0 or button_right.value() == 0:  # if button pressed stops
                    break
            yellow_led.value(False)
            green_led.value(True)
        x = 1

        while button_right.value() == 0:        # while the right button is pressed it opens
            red_led.value(False)
            yellow_led.value(True)
            spin(A_CLOCK)
            steps += 1
            if button_right.value() == 1:
                x = 1  # when released changes state
                yellow_led.value(False)
                green_led.value(True)

    while x == 1:
        t = utime.time()
        while steps != steps_gone:
            utime.sleep_ms(500)
            if button_right.value() == 0 or button_left.value() == 0:
                yellow_led.value(True)
                green_led.value(False)
                utime.sleep_ms(500)
                stop_go()
                yellow_led.value(False)
                if steps != steps_gone:
                    green_led.value(True)
                t = utime.time()

            if utime.time()-t == time_open_s:
                yellow_led.value(True)
                green_led.value(False)
                stop_go()
                yellow_led.value(False)
                if steps != steps_gone:
                    green_led.value(True)
                t = utime.time()

        x = 0
        red_led.value(True)
        steps = 0
        steps_gone = 0

# https://components101.com/motors/28byj-48-stepper-motor
