from pyfirmata import Arduino, util
import time

# Specify the correct port where Arduino is connected
board = Arduino('COM6')  # For Windows
# board = Arduino('/dev/ttyUSB0')  # For Linux/Mac

# Start the iterator thread
it = util.Iterator(board)
it.start()

# Define pin 13 (built-in LED) as output
led_pin = board.get_pin('d:13:o')  # d: digital, 13: pin number, o: output

# Blink the LED
while True:
    led_pin.write(1)  # Turn on LED
    time.sleep(1)     # Wait for 1 second
    led_pin.write(0)  # Turn off LED
    time.sleep(1)     # Wait for 1 second
