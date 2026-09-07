from gpiozero import AngularServo
from time import sleep

servo = AngularServo(
    18,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=0.5/1000,
    max_pulse_width=2.5/1000
)

try:
    servo.angle = -45
    sleep(2)

    servo.angle = 0
    sleep(2)

    servo.angle = 45
    sleep(2)

finally:
    servo.detach()
