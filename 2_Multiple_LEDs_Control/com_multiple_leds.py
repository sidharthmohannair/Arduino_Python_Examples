import serial
import serial.tools.list_ports
import time

def list_ports():
    """List all available ports and their descriptions."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print(f"Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
    return ports

def find_arduino_port():
    """Automatically detect the Arduino COM port."""
    ports = list_ports()
    for port in ports:
        # Check for specific identifiers for your Arduino
        if 'Arduino' in port.description or 'FT232R USB UART' in port.description:
            return port.device
    # Check for /dev/ttyUSB0 if it's not detected by description
    for port in ports:
        if '/dev/ttyUSB0' in port.device:
            return port.device
    return None

def communicate_with_arduino(port, baud_rate=9600):
    """Send data to Arduino and control LEDs."""
    try:
        # Open the serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port}")
        time.sleep(2)  # Wait for Arduino to reset

        # Send commands to turn on/off LEDs
        while True:
            command = input("Enter a number from 0 to 5 (0: LED0 off, 1: LED0 on, 2: LED1 off, ...), or 'Q' to quit: ").upper()
            if command == 'Q':
                break
            elif command in ['0', '1', '2', '3', '4', '5']:
                ser.write(command.encode())  # Send command to Arduino
                time.sleep(0.5)  # Wait for the command to be processed
                response = ser.readline().decode().strip()
                print(f"Arduino response: {response}")
            else:
                print("Invalid command. Please enter a number from 0 to 5, or 'Q'.")

        ser.close()
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    arduino_port = find_arduino_port()
    if arduino_port:
        communicate_with_arduino(arduino_port)
    else:
        print("Arduino not found. Please check the connection.")
