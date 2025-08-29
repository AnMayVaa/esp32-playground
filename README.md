# ESP32 & MicroPython Playground

![ESP32 Banner](https://www.esp32s.com/wp-content/uploads/2025/06/home-banner-4-1750433333.jpg) 

## 📖 About This Repository

Welcome to my personal playground for embedded systems! This repository serves as a living document of my learning journey with the **ESP32 microcontroller** and **MicroPython**. Here, you'll find a collection of hands-on projects, each designed to explore a specific piece of hardware, a programming concept, or a real-world application.

The goal is to move from fundamental concepts like hardware drivers to more complex integrations involving sensors and connectivity. Each project is self-contained and includes the necessary code and wiring instructions to be reproduced.

---

## 🚀 Technology Stack

This repository primarily utilizes the following technologies:

-   **Microcontroller:** `ESP32`
-   **Programming Language:** `MicroPython`
-   **IDE:** `Thonny`
-   **Key Components Explored:**
    -   `MAX7219` 8x8 LED Matrix Displays
    -   `HC-SR04` Ultrasonic Distance Sensor

---

## 🔧 Projects Showcase

Here is a summary of the projects currently in this repository. Click on a project name to see its detailed README, code, and wiring diagram.

| Preview | Project | Description | Components Used | Status |
| :---: | :--- | :--- | :--- | :---: |
| ![Counter GIF Preview](https://github.com/AnMayVaa/esp32-playground/blob/main/images/01-01.jpg?raw=true) | **[01 - Vertical Counter](./01-4-in-1-led-matrix-counter/)** | A digital counter displayed vertically on a 4-in-1 (8x32) LED matrix. A great exercise in custom display rendering. | `ESP32`, `MAX7219` | ✅ Complete |
| ![Distance Meter GIF Preview](https://github.com/AnMayVaa/esp32-playground/blob/main/images/02-01.jpg?raw=true) | **[02 - Distance Meter](./02-ultrasonic-distance-meter/)** | A real-time distance measuring tool using an ultrasonic sensor, with the output shown on the vertical LED matrix. | `ESP32`, `MAX7219`, `HC-SR04` | ✅ Complete |
| *... (My next project below!)* | ***Coming Soon*** | | | 🚧 In Progress |

---

## 🛠️ General Setup & Requirements

To run any of the projects in this repository, you will generally need the following:

1.  **Hardware**: An ESP32 development board and the specific components listed in each project's README.
2.  **Firmware**: The latest stable version of [MicroPython for ESP32](https://micropython.org/download/esp32/).
3.  **IDE**: [Thonny IDE](https://thonny.org/) is highly recommended as it has excellent built-in support for MicroPython on the ESP32.

---

## 🌱 Future Goals

This repository is an ongoing project. I plan to explore more advanced topics in the future, such as:
-   [ ] Wi-Fi and Bluetooth connectivity
-   [ ] Communicating with web services and APIs
-   [ ] Using protocols like MQTT for IoT
-   [ ] Interfacing with I2C sensors (e.g., temperature, humidity)
-   [ ] Exploring sleep modes for battery-powered projects

## 👋 Contact & Acknowledgements

Feel free to explore the projects! If you have any questions or suggestions, please open an issue in this repository.

Happy coding!
