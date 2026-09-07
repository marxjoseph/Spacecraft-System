from gpiozero import AngularServo
from time import sleep

servo = AngularServo(
    18,
    min_angle=-45,
    max_angle=45,
    min_pulse_width=1/1000,
    max_pulse_width=2/1000
)

try:
    while True:
        servo.angle = -45
        sleep(1)

        servo.angle = 45
        sleep(1)

finally:
    servo.detach()
