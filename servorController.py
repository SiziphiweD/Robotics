from pyfirmata import Arduino, util
import time

# Specify the correct port where Arduino is connected
board = Arduino('COM6')  # For Windows
# board = Arduino('/dev/ttyUSB0')  # For Linux/Mac

# Start the iterator thread
it = util.Iterator(board)
it.start()

# Define pin 13 (built-in servor) as output
servo_pin = board.get_pin('d:13:o')  # d: digital, 13: pin number, o: output

# Function to set servo angle
def set_servo_angle(angle):
    # Convert angle to pulse width (0-180 degrees to 0-180)
    pulse_width = angle / 180.0 * 1.8 + 0.5
    servo_pin.write(pulse_width * 10)  # PyFirmata uses pulse width in microseconds

# Sweep the servo back and forth
try:
    while True:
        for angle in range(0, 180, 1):
            set_servo_angle(angle)
            time.sleep(0.01)  # Delay to allow servo to reach the position
        for angle in range(180, 0, -1):
            set_servo_angle(angle)
            time.sleep(0.01)
except KeyboardInterrupt:
    # Stop the servo when the script is interrupted
    servo_pin.write(0)  # Set to 0 or a neutral position
    board.exit()  # Close the connection to the board