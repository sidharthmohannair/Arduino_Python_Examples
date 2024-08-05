
# Single LED Control

This example demonstrates how to control a single LED connected to an Arduino using a Python script. The project showcases how serial communication between Arduino and Python can be used to send commands for turning an LED on and off.

## Project Overview

- **Arduino Code:** `single_led_control.ino`
- **Python Script:** `com_single_led.py`
- **Hardware Required:** Arduino board, LED, resistor (220Ω), jumper wires, breadboard.

## Hardware Setup

### Components

1. **Arduino Board**
2. **LED**
3. **Resistor (220Ω)**
4. **Jumper Wires**
5. **Breadboard**

### Circuit Diagram

Here's a basic diagram for connecting an LED to pin 13 on the Arduino:

- Connect the longer leg (anode) of the LED to pin 13 on the Arduino.
- Connect the shorter leg (cathode) of the LED to a resistor.
- Connect the other end of the resistor to the ground (GND) on the Arduino.

![Circuit Diagram](screenshots/circuit_diagram.png)

### Hardware Setup Screenshot

![Hardware Setup](screenshots/hardware_setup.png)

## Software Setup

### 1. Install Required Software

- **Arduino IDE:** [Download Arduino IDE](https://www.arduino.cc/en/software)
- **Python:** Ensure you have Python 3 installed on your system.
- **PySerial Library:** Install PySerial using pip:

  ```bash
  pip install pyserial
  ```

### 2. Upload Arduino Code

1. Open the `single_led_control.ino` file in the Arduino IDE.
2. Connect your Arduino board to your computer via USB.
3. Select the correct board and port in the Arduino IDE.
4. Upload the code to the Arduino board.

### 3. Run the Python Script

1. Open a terminal and navigate to the `1_Single_LED_Control` directory.
2. Run the Python script:

   ```bash
   python3 com_single_led.py
   ```

3. Follow the on-screen prompts to control the LED:

   - Enter `H` to turn on the LED.
   - Enter `L` to turn off the LED.
   - Enter `Q` to quit the program.

### Software Execution GIF

![Execution GIF](gifs/execution.gif)

## Troubleshooting

- **Port Detection:** Ensure the correct COM port is used for the Arduino. The Python script should automatically detect the port.
- **Permissions:** If you encounter permission issues, ensure your user has access to the COM port.
- **LED Connections:** Verify the connections and polarity of the LED.

## Conclusion

This example demonstrates basic serial communication between Arduino and Python for controlling a single LED. This foundation can be expanded to include more complex interactions and control of additional components.

Feel free to explore the other examples in this repository for more advanced projects.

---

### License

This project is licensed under the MIT License.

