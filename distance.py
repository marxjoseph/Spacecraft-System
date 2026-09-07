from gpiozero import AngularServo, Button
from time import sleep

servo = AngularServo(
    18,
    min_angle=-45,
    max_angle=45,
    min_pulse_width=1/1000,
    max_pulse_width=2/1000
)

button = Button(17)

servo.angle = 0

try:
    while True:
        if button.is_pressed:
            print("BUTTON PRESSED - ACTUATING")

            servo.angle = 45
            sleep(1)

            servo.angle = -45
            sleep(1)

            servo.angle = 0
            sleep(1)

            button.wait_for_release()

        sleep(0.05)

finally:
    servo.detach()
