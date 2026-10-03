from machine import Pin, PWM
import time

ena = PWM(Pin(13), freq=30000)
in1 = Pin(26, Pin.OUT)
in2 = Pin(25, Pin.OUT)

in3 = Pin(33, Pin.OUT)
in4 = Pin(32, Pin.OUT)
enb = PWM(Pin(27), freq=30000)


def move_forward(speed):
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)
    ena.duty(speed)
    enb.duty(speed)


def move_backward(speed):
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    ena.duty(speed)
    enb.duty(speed)


def stop_motors():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    ena.duty(0)
    enb.duty(0)
def move_left(speed):
    in1.value(0)
    in2.value(1)
    in3.value(1)
    in4.value(0)
    ena.duty(speed)
    enb.duty(speed)
def move_right(speed):
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    ena.duty(speed)
    enb.duty(speed)


try:
    while True:
        key = input()
        if key == 'w':
            move_forward(700)
        elif key == 's':
            move_backward(700)
        elif key == 'a':
            move_left(700)
        elif key == 'd':
            move_right(700)
        elif key == 'q':
            stop_motors()
except KeyboardInterrupt:
    stop_motors()