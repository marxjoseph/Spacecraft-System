import RPi.GPIO as GPIO
from gpiozero import AngularServo, Button
from RPLCD.gpio import CharLCD
from time import sleep

# Servo: GPIO18
servo = AngularServo(
    18,
    min_angle=-45,
    max_angle=45,
    min_pulse_width=1/1000,
    max_pulse_width=2/1000
)

# Button: GPIO17
button = Button(17, pull_up=True)

# LCD1602 pins
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2,
    pin_rs=25,
    pin_e=24,
    pins_data=[23, 22, 27, 4]
)

# Start servo in the neutral position
servo.angle = 0

# Show initial spacecraft status
lcd.clear()
lcd.write_string("SPACECRAFT")
lcd.cursor_pos = (1, 0)
lcd.write_string("STATUS: READY")

try:
    while True:
        # Check if the button was pressed
        if button.is_pressed:

            # Show actuator status
            lcd.clear()
            lcd.write_string("SPACECRAFT")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("ACTUATING...")

            # Move actuator to each position
            servo.angle = 45
            sleep(1)

            servo.angle = -45
            sleep(1)

            # Return actuator to neutral
            servo.angle = 0
            sleep(1)

            # Return to ready state
            lcd.clear()
            lcd.write_string("SPACECRAFT")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("STATUS: READY")

            sleep(0.5)

        sleep(0.05)

finally:
    # Clean up when the program stops
    servo.detach()
    lcd.clear()
    GPIO.cleanup()
