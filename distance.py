import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

try:
    while True:
        # Send 10us trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for ECHO to go HIGH
        timeout = time.time() + 0.1
        while GPIO.input(ECHO) == 0:
            if time.time() > timeout:
                print("No ECHO signal")
                break

        pulse_start = time.time()

        # Wait for ECHO to go LOW
        timeout = time.time() + 0.1
        while GPIO.input(ECHO) == 1:
            if time.time() > timeout:
                print("ECHO stuck HIGH")
                break

        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 34300 / 2

        print(f"Distance: {distance:.1f} cm")

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
