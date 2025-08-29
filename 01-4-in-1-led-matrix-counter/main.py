#
# ESP32 MicroPython Project: 4-in-1 Vertical Counter
#
# This script runs a counter from 0 to 9999 and displays the number
# vertically on a 4-in-1 MAX7219 8x8 LED matrix display.
# The display is treated as a single 8x32 pixel canvas.
#

# --- Library Imports ---
import machine
from machine import Pin, SPI  # For hardware control (GPIO pins, SPI bus)
import max7219                # The custom library for the MAX7219 driver
import time                   # For creating delays (e.g., time.sleep())
import framebuf               # For creating in-memory framebuffers, used for font rendering

# --- Hardware Setup ---

# Initialize the SPI (Serial Peripheral Interface) bus.
# This is the communication protocol used to send data to the MAX7219 chip.
# SPI(1) selects one of the ESP32's hardware SPI peripherals.
# sck=Pin(18): Serial Clock pin.
# mosi=Pin(19): Master Out Slave In pin (also known as DIN or Data In).
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(19))

# Initialize the CS (Chip Select) pin. This pin tells the MAX7219 when to listen for data.
cs = Pin(5, Pin.OUT)

# Create the display object from our max7219 library.
# IMPORTANT: num=4 tells the library that we have four 8x8 modules daisy-chained together.
display = max7219.Matrix8x8(spi, cs, num=4)

# Set the brightness of the display (valid range is 0 to 15).
display.brightness(5)

# --- Display Helper Functions for Vertical Orientation ---

def pixel_rotated(x, y, color):
    """
    Draws a single pixel on the physical 8x32 vertical display.
    This function translates our desired vertical coordinates (x, y) into the
    horizontal coordinates that the underlying library expects.
    - x: our horizontal position (0-7)
    - y: our vertical position (0-31)
    - color: 1 for ON, 0 for OFF
    """
    # Check if the coordinates are within our virtual 8x32 canvas.
    if not (0 <= x < 8 and 0 <= y < 32):
        return  # Do nothing if the pixel is out of bounds.

    # This is the core 90-degree clockwise rotation logic.
    # The library sees the display as a 32x8 horizontal canvas.
    # Our vertical 'y' becomes the library's horizontal 'x'.
    # Our horizontal 'x' becomes the library's vertical 'y' (but inverted).
    library_x = y
    library_y = 7 - x
    
    # Call the library's original pixel function with the translated coordinates.
    display.pixel(library_x, library_y, color)

def text_rotated(text, x, y, color):
    """
    Draws a string of text vertically on the display.
    It works by rendering each character to a temporary 8x8 buffer
    and then copying the pixels one by one to their final rotated position.
    """
    # 1. Create a temporary 8x8 framebuffer in memory. This will act as a
    #    small canvas to draw one character at a time.
    char_buffer = bytearray(8)  # An 8x8 monochrome display needs 8 bytes of memory.
    fb = framebuf.FrameBuffer(char_buffer, 8, 8, framebuf.MONO_HLSB)

    # Iterate through each character in the input string.
    for char_index, char_code in enumerate(text):
        # Calculate the vertical starting position ('y' offset) for the current character.
        # Each character is 8 pixels tall.
        char_start_y = y + char_index * 8

        # 2. Render the character onto our temporary framebuffer.
        fb.fill(0)  # Clear the temporary buffer.
        fb.text(char_code, 0, 0, 1) # Draw the character at position (0,0) in the buffer.

        # 3. Scan the temporary buffer and copy each lit pixel to the main display.
        for char_x in range(8):
            for char_y in range(8):
                # If the pixel at (char_x, char_y) in our buffer is ON...
                if fb.pixel(char_x, char_y) == 1:
                    # ...then draw that pixel on the main display at the
                    # correct rotated and offset position.
                    pixel_rotated(x + char_x, char_start_y + char_y, color)

# --- Main Program Loop ---
print("Running Counter Project on 4-in-1 Vertical Display (8x32)")

# Initialize the counter.
count = 0

while True:
    # Convert the current count number to a string for display.
    text_to_display = str(count)
    print("Displaying:", text_to_display)

    # Clear the entire display buffer before drawing new content.
    display.fill(0)

    # --- Vertical Centering Logic ---
    # Calculate the total height of the text in pixels (each character is 8 pixels tall).
    text_height = len(text_to_display) * 8
    # Calculate the starting 'y' position to center the text on the 32-pixel tall display.
    start_y = (32 - text_height) // 2

    # Draw the centered text onto the display buffer.
    text_rotated(text_to_display, 0, start_y, 1)
    
    # Push the contents of the display buffer to the physical LED matrix.
    # This makes the drawing visible.
    display.show()
    
    # Wait for 1 second before the next update.
    time.sleep(1)

    # Increment the counter.
    count += 1
    # If the counter exceeds 9999, reset it back to 0.
    if count > 9999:
        count = 0