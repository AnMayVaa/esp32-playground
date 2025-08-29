# Project 02: Ultrasonic Distance Meter with LED Matrix Display

This project creates a real-time digital measuring tape. It uses an HC-SR04 ultrasonic sensor to measure the distance to an object and displays the result in centimeters on the vertical 4-in-1 MAX7219 LED matrix.

This project combines the sensor input with the custom display driver from the previous project.

![_Your_GIF_or_Image_Here_](https://github.com/AnMayVaa/esp32-playground/blob/main/images/02-01.jpg?raw=true)

## Features

-   Measures distance using the HC-SR04 ultrasonic sensor.
-   Displays the distance in centimeters (cm) in real-time.
-   Updates the display approximately 5 times per second.
-   Uses the same 8x32 vertical display setup as Project 01.
-   Written in MicroPython for the ESP32.

## Hardware Required

-   1 x ESP32 Development Board
-   1 x MAX7219 4-in-1 Dot Matrix Module (8x32)
-   1 x HC-SR04 Ultrasonic Sensor
-   ~9 x Jumper Wires
-   1 x Micro-USB Cable for power and programming
-   (Optional) Breadboard

## Wiring Diagram

This project requires connecting both the LED matrix and the ultrasonic sensor. Ensure all components share a common ground (GND).

| Component            | Pin        | ESP32 Pin | Notes                |
| :------------------- | :--------- | :-------- | :------------------- |
| **MAX7219 Module** | `VCC`      | `5V` / `Vin` | Power (5 Volts)      |
|                      | `GND`      | `GND`     | Common Ground        |
|                      | `DIN`      | `GPIO 19` | Data In (MOSI)       |
|                      | `CS`       | `GPIO 5`  | Chip Select (SS)     |
|                      | `CLK`      | `GPIO 18` | Clock (SCK)          |
| **HC-SR04 Sensor** | `VCC`      | `5V` / `Vin` | Power (5 Volts)      |
|                      | `GND`      | `GND`     | Common Ground        |
|                      | `Trig`     | `GPIO 23` | Trigger Pulse Output |
|                      | `Echo`     | `GPIO 22` | Echo Pulse Input     |

## Software & Setup

1.  **Firmware**: Your ESP32 must be flashed with MicroPython firmware.
2.  **IDE**: This project is developed using [Thonny IDE](https://thonny.org/).
3.  **Library File**: This project requires the `max7219.py` library.
4.  **Upload Files**: Using Thonny, upload the following two files to the root directory of your ESP32 device:
    -   `main.py` (This project's code)
    -   `max7219.py` (The display driver library)

## How to Run

1.  Connect all the hardware according to the wiring diagram.
2.  Connect your ESP32 to your computer via USB.
3.  Open Thonny and connect to your ESP32's interpreter.
4.  Ensure both `main.py` and `max7219.py` are on the device.
5.  Run the `main.py` script or reset the board. The display will show "RDY" and then begin displaying the distance.
6.  Place an object in front of the sensor to see the distance change.
