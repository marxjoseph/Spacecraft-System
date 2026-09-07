import time
from gpiozero import Servo

# Connect the servo signal wire to GPIO 18
# min_pulse_width and max_pulse_width calibrate typical SG90 micro servos
servo = Servo(18, min_pulse_width=0.5 / 1000, max_pulse_width=2.5 / 1000)

try:
  while True:
    print('Moving to 0 degrees')
    servo.min()  # Value is -1
    time.sleep(1)

    print('Moving to 90 degrees')
    servo.mid()  # Value is 0
    time.sleep(1)

    print('Moving to 180 degrees')
    servo.max()  # Value is 1
    time.sleep(1)

    print('Moving to a custom angle (e.g., ~135 degrees)')
    servo.value = 0.5  # Acceptable range is anywhere between -1 and 1
    time.sleep(1)

except KeyboardInterrupt:
  print('\nProgram stopped safely.')
