# Project 01: Vertical Counter on 4-in-1 LED Matrix

This project is a simple digital counter that displays numbers from 0 to 9999 on a 4-in-1 MAX7219 dot matrix display. The display is oriented vertically, creating an 8x32 pixel canvas.

The main purpose of this project is to demonstrate the control of cascaded MAX7219 modules and how to create custom text rendering functions to handle a rotated (vertical) display orientation.

![_Your_GIF_or_Image_Here_](https://github.com/AnMayVaa/esp32-playground/blob/main/images/01-01.jpg?raw=true)

## Features

-   Displays a counter that increments every second.
-   Supports numbers up to 4 digits (0-9999).
-   Renders text vertically on a 4-in-1 (8x32) MAX7219 display.
-   Automatically centers the number on the display.
-   Written in MicroPython for the ESP32.

## Hardware Required

-   1 x ESP32 Development Board
-   1 x MAX7219 4-in-1 Dot Matrix Module (8x32)
-   5 x Jumper Wires
-   1 x Micro-USB Cable for power and programming
-   (Optional) Breadboard

## Wiring Diagram

Connect the ESP32 to the **INPUT** side of the MAX7219 module as follows:

| MAX7219 Module Pin | ESP32 Pin | Notes                |
| :----------------- | :-------- | :------------------- |
| `VCC`              | `5V` / `Vin` | Power (5 Volts)      |
| `GND`              | `GND`     | Common Ground        |
| `DIN`              | `GPIO 19` | Data In (MOSI)       |
| `CS`               | `GPIO 5`  | Chip Select (SS)     |
| `CLK`              | `GPIO 18` | Clock (SCK)          |

## Software & Setup

1.  **Firmware**: Your ESP32 must be flashed with MicroPython firmware.
2.  **IDE**: This project is developed using [Thonny IDE](https://thonny.org/), which is great for beginners.
3.  **Library File**: This project requires the `max7219.py` library.
4.  **Upload Files**: Using Thonny, upload the following two files to the root directory of your ESP32 device:
    -   `main.py` (This project's code)
    -   `max7219.py` (The display driver library)

## How to Run

1.  Connect all the hardware according to the wiring diagram.
2.  Connect your ESP32 to your computer via USB.
3.  Open Thonny and connect to your ESP32's interpreter.
4.  Ensure both `main.py` and `max7219.py` are on the device.
5.  Run the `main.py` script from Thonny, or simply reset the ESP32 board. The counter should start automatically.
