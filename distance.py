from gpiozero import Servo
from time import sleep

servo = Servo(18)

try:
    print("0 degrees")
    servo.min()
    sleep(2)

    print("90 degrees")
    servo.mid()
    sleep(2)

    print("180 degrees")
    servo.max()
    sleep(2)

finally:
    servo.detach()
