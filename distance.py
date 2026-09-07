from gpiozero import AngularServo, Button
from time import sleep

# -------------------------
# SERVO
# -------------------------
servo = AngularServo(
    18,
    min_angle=-45,
    max_angle=45,
    min_pulse_width=1/1000,
    max_pulse_width=2/1000
)

# -------------------------
# BUTTON
# -------------------------
button = Button(17)

# -------------------------
# FUEL
# -------------------------
fuel = 100
valve_open = False

# Start in nominal state
servo.angle = 0

print("SPACECRAFT FUEL SYSTEM")
print("STATUS: NOMINAL")

try:
    while True:

        if button.is_pressed:

            if not valve_open:
                # Open fuel valve
                valve_open = True
                servo.angle = 45

                print("FUEL:", fuel, "%")
                print("VALVE: OPEN")

                # Simulate fuel consumption
                fuel -= 1

            else:
                # Close fuel valve
                valve_open = False
                servo.angle = 0

                print("FUEL:", fuel, "%")
                print("VALVE: CLOSED")

            # Wait for button release
            button.wait_for_release()

        sleep(0.05)

finally:
    servo.detach()
