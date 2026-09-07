from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=13, trigger=12)

while True:
    print(sensor.distance * 100, "cm")
    sleep(1)