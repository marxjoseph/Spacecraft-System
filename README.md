# Spacecraft Fuel & Actuator Control System

A small embedded control system built with a **Raspberry Pi 3B** that simulates a spacecraft fuel-valve/actuator control system.

The system uses a physical push button as a spacecraft command input, a servo as the actuator, and an LCD1602 display for real-time system status.

## Features

* Physical button for spacecraft control input
* Servo motor simulating a fuel valve/actuator
* LCD1602 displaying system status
* Raspberry Pi GPIO control
* Simple embedded control sequence
* Python-based implementation

## System Architecture

```text
              ┌─────────────────┐
              │   Push Button   │
              │  Flight Command │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Raspberry Pi   │
              │  3B Controller  │
              └───────┬───┬─────┘
                      │   │
             ┌────────┘   └─────────┐
             ▼                      ▼
      ┌─────────────┐        ┌─────────────┐
      │    Servo    │        │   LCD1602   │
      │  Actuator   │        │  Telemetry  │
      └─────────────┘        └─────────────┘
```

## How It Works

When the system starts, the spacecraft is placed into a **READY** state.

When the push button is pressed:

1. The LCD displays `ACTUATING...`
2. The Raspberry Pi commands the servo to move to one position.
3. The servo moves to the opposite position.
4. The servo returns to its neutral position.
5. The LCD returns to `STATUS: READY`.

The servo movement represents the operation of a spacecraft actuator, such as a simulated fuel-control valve.

## Hardware

* Raspberry Pi 3B
* Servo motor
* LCD1602
* Push button
* Breadboard
* Jumper wires
* Potentiometer for LCD contrast
* Power supply

## GPIO Wiring

### Servo

| Servo  | Raspberry Pi             |
| ------ | ------------------------ |
| Signal | GPIO18 — Physical Pin 12 |
| VCC    | 5V — Physical Pin 2      |
| GND    | GND — Physical Pin 6     |

### Push Button

| Button        | Raspberry Pi             |
| ------------- | ------------------------ |
| One side      | GPIO17 — Physical Pin 11 |
| Opposite side | GND                      |

The button uses the Raspberry Pi's internal pull-up resistor.

### LCD1602

| LCD1602  | Raspberry Pi             |
| -------- | ------------------------ |
| RS       | GPIO25 — Physical Pin 22 |
| E        | GPIO24 — Physical Pin 18 |
| D4       | GPIO23 — Physical Pin 16 |
| D5       | GPIO22 — Physical Pin 15 |
| D6       | GPIO27 — Physical Pin 13 |
| D7       | GPIO4 — Physical Pin 7   |
| VSS      | GND                      |
| VDD      | 5V                       |
| RW       | GND                      |
| LED+ / A | 5V                       |
| LED- / K | GND                      |
| VO       | Potentiometer center pin |

The potentiometer's two outer pins connect to **5V and GND** and control the LCD contrast.

## Software

The project uses:

* Python 3
* GPIO Zero
* RPi.GPIO
* RPLCD

Install the required packages:

```bash
sudo apt update
sudo apt install python3-gpiozero python3-rpi.gpio
sudo pip3 install RPLCD --break-system-packages
```

## Running the Project

Run the main Python program:

```bash
python3 main.py
```

The LCD should display:

```text
SPACECRAFT
STATUS: READY
```

Pressing the button starts the actuator sequence.

## Project Structure

```text
spacecraft-fuel-control/
│
├── main.py
└── README.md
```

## Engineering Concept

This project demonstrates a basic embedded control loop:

```text
Input → Controller → Actuator
           │
           └────→ Telemetry
```

The push button represents a command from a spacecraft control system. The Raspberry Pi processes that input and controls the servo actuator while simultaneously providing system status through the LCD.

Although the project is a simplified simulation, the architecture demonstrates concepts used in larger embedded systems: **digital inputs, actuator control, state-based behavior, GPIO interfaces, and system telemetry**.

## Future Improvements

Possible extensions include:

* Add an actual distance or pressure sensor
* Add ADC-based analog sensor measurements
* Add fault detection
* Add actuator position feedback
* Add multiple operating states
* Log telemetry data
* Add CAN, SPI, or I2C peripherals
* Implement watchdog/error handling
* Add automated hardware-in-the-loop testing
