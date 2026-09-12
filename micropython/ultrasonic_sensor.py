"""MicroPython HC-SR04 ultrasonic distance example."""

from machine import Pin, time_pulse_us
from time import sleep_us, sleep

TRIGGER = Pin(5, Pin.OUT)
ECHO = Pin(18, Pin.IN)


def read_distance_cm() -> float:
    TRIGGER.value(0)
    sleep_us(2)
    TRIGGER.value(1)
    sleep_us(10)
    TRIGGER.value(0)

    duration = time_pulse_us(ECHO, 1, 30000)
    if duration < 0:
        return -1.0
    return (duration * 0.0343) / 2


while True:
    distance = read_distance_cm()
    print("distance_cm=", round(distance, 2))
    sleep(0.5)
