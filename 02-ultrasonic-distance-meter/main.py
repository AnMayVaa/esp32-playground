# Import necessary libraries
import machine
from machine import Pin, SPI
import max7219
import time
import framebuf # Used for font rendering

# --- 1. Hardware Setup ---

# --- LED Matrix (SPI) Configuration ---
# Assign SPI pins for communication with the MAX7219 driver.
# SPI(1) is one of the hardware SPI peripherals on the ESP32.
# SCK (Serial Clock): Pin 18
# MOSI (Master Out Slave In) / DIN: Pin 19
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(19))
# CS (Chip Select): Pin 5
cs = Pin(5, Pin.OUT)

# Create the display object.
# IMPORTANT: num=4 tells the library we have four 8x8 modules connected in series.
display = max7219.Matrix8x8(spi, cs, num=4)

# Set the brightness of the display (0=dimmest, 15=brightest).
display.brightness(5)

# --- Ultrasonic Sensor (HC-SR04) Configuration ---
# Assign GPIO pins for the sensor.
trig_pin = Pin(23, Pin.OUT) # Trigger pin sends the sound pulse
echo_pin = Pin(22, Pin.IN)  # Echo pin receives the reflected pulse

# --- 2. Helper Functions ---

def get_distance():
    """
    Measures distance using the HC-SR04 sensor.
    Returns the distance in centimeters (cm).
    """
    # To trigger a measurement, we send a short 10 microsecond pulse.
    trig_pin.value(0)
    time.sleep_us(2)
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    try:
        # Measure the duration of the echo pulse.
        # machine.time_pulse_us() waits for a pulse and returns its duration in microseconds.
        # The timeout (30000 us = 30 ms) prevents the program from getting stuck forever.
        duration = machine.time_pulse_us(echo_pin, 1, 30000)
    except OSError:
        # This error occurs if a pulse is not received within the timeout period
        # (e.g., the object is too far away).
        duration = 0

    # Calculate the distance.
    # Speed of sound is approx. 343 m/s, which is 0.0343 cm/us.
    # We divide by 2 because the sound wave travels to the object and back.
    distance = (duration * 0.0343) / 2
    
    # The HC-SR04 sensor's effective range is up to about 400 cm.
    if distance > 400:
        return 400 # Return a max value if out of range.
        
    return int(distance)

def pixel_rotated(x, y, color):
    """
    Draws a single pixel on the physical 8x32 vertical display.
    It translates our desired vertical coordinates (x, y) into the
    horizontal coordinates that the library expects.
    - x: our horizontal position (0-7)
    - y: our vertical position (0-31)
    """
    # Ensure the pixel is within our 8x32 drawing canvas.
    if not (0 <= x < 8 and 0 <= y < 32):
        return
    
    # Coordinate rotation logic (90 degrees clockwise)
    # The library sees a 32x8 horizontal display.
    library_x = y
    library_y = 7 - x
    display.pixel(library_x, library_y, color)

def text_rotated(text, x, y, color):
    """
    Draws a string of text vertically on the display using the pixel_rotated function.
    """
    # Create a temporary 8x8 framebuffer in memory to render one character at a time.
    char_buffer = bytearray(8)
    fb = framebuf.FrameBuffer(char_buffer, 8, 8, framebuf.MONO_HLSB)

    # Iterate through each character in the input string.
    for char_index, char_code in enumerate(text):
        # Calculate the vertical starting position for the current character.
        char_start_y = y + char_index * 8

        # Render the single character onto the temporary framebuffer.
        fb.fill(0) # Clear the buffer
        fb.text(char_code, 0, 0, 1) # Draw the character

        # Copy the character pixel by pixel from the buffer to the real display.
        for char_x in range(8):
            for char_y in range(8):
                # If the pixel is ON in the buffer...
                if fb.pixel(char_x, char_y) == 1:
                    # ...draw it on the rotated display.
                    pixel_rotated(x + char_x, char_start_y + char_y, color)

# --- 3. Main Program Loop ---
print("Starting Real-time Distance Measurement Project...")

# Display a startup message.
display.fill(0)
# --- CORRECTED CENTERING ---
# Text "RDY" is 3 chars high (3*8 = 24 pixels).
# Start Y = (Total Height - Text Height) / 2 = (32 - 24) / 2 = 4.
text_rotated("RDY", 0, 4, 1) 
display.show()
time.sleep(2)

while True:
    # 1. Get the latest distance reading.
    distance = get_distance()
    
    # 2. Print the value to the Thonny shell for debugging.
    print("Distance:", distance, "cm")

    # 3. Prepare and render the text on the LED display.
    text_to_display = str(distance)
    display.fill(0) # Clear the entire display before drawing new content.

    # Center the number vertically on the 8x32 display.
    text_height = len(text_to_display) * 8
    start_y = (32 - text_height) // 2
    
    # Draw the distance number.
    text_rotated(text_to_display, 0, start_y, 1)
    
    # Update the physical display with the new content from the buffer.
    display.show()

    # 4. Wait for a short period before the next measurement.
    time.sleep(0.2) # 200 milliseconds