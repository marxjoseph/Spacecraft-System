import RPi.GPIO as GPIO
from gpiozero import AngularServo, Button
from RPLCD.gpio import CharLCD
from time import sleep

# Servo
servo = AngularServo(
    18,
    min_angle=-45,
    max_angle=45,
    min_pulse_width=1/1000,
    max_pulse_width=2/1000
)

# Button
button = Button(17)

# LCD
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2,
    pin_rs=25,
    pin_e=24,
    pins_data=[23, 22, 27, 4]
)

# Starting position
servo.angle = 0

# Starting LCD message
lcd.clear()
lcd.write_string("SPACECRAFT")
lcd.cursor_pos = (1, 0)
lcd.write_string("STATUS: READY")

try:
    while True:

        if button.is_pressed:

            # LCD says actuator is working
            lcd.clear()
            lcd.write_string("SPACECRAFT")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("ACTUATING...")

            # Move servo
            servo.angle = 45
            sleep(1)

            servo.angle = -45
            sleep(1)

            servo.angle = 0
            sleep(1)

            # Return to ready
            lcd.clear()
            lcd.write_string("SPACECRAFT")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("STATUS: READY")

            button.wait_for_release()

        sleep(0.05)

finally:
    servo.detach()
    lcd.clear()
    GPIO.cleanup()
