from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=13, trigger=12, max_distance=4)

print("Reading distance from sensor...")

try:
    while True:
        print(f"Distance: {sensor.distance * 100:.1f} cm")
        sleep(1)
except KeyboardInterrupt:
    print("Stopped by user.")