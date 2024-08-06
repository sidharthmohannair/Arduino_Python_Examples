
# Multiple LEDs Control

This example demonstrates how to control multiple LEDs connected to an Arduino using a Python script. The project illustrates serial communication between Arduino and Python to send commands for turning LEDs on and off individually.

## Project Overview

- **Arduino Code:** `multiple_leds_control.ino`
- **Python Script:** `com_multiple_leds.py`
- **Hardware Required:** Arduino board, 3 LEDs, 3 resistors (220Ω), jumper wires, breadboard.

## Hardware Setup

### Components

1. **Arduino Board**
2. **3 LEDs**
3. **3 Resistors (220Ω)**
4. **Jumper Wires**
5. **Breadboard**

### Circuit Diagram

Here's a diagram showing how to connect three LEDs to pins 13, 12, and 11 on the Arduino:

- **LED 0**: Connect to pin 13.
- **LED 1**: Connect to pin 12.
- **LED 2**: Connect to pin 11.

Each LED should have its anode connected to the respective pin and its cathode connected to a resistor. The other end of each resistor should be connected to the ground (GND).

![Circuit Diagram](/2_Multiple_LEDs_Control/images/circuit_dia.png)

### Hardware Setup Screenshot

![Hardware Setup](/2_Multiple_LEDs_Control/images/circuit.jpg)

## Software Setup

### 1. Install Required Software

- **Arduino IDE:** [Download Arduino IDE](https://www.arduino.cc/en/software)
- **Python:** Ensure you have Python 3 installed on your system.
- **PySerial Library:** Install PySerial using pip:

  ```bash
  pip install pyserial
  ```

### 2. Upload Arduino Code

1. Open the `multiple_leds_control.ino` file in the Arduino IDE.
2. Connect your Arduino board to your computer via USB.
3. Select the correct board and port in the Arduino IDE.
4. Upload the code to the Arduino board.

### 3. Run the Python Script

1. Open a terminal and navigate to the `2_Multiple_LEDs_Control` directory.
2. Run the Python script:

   ```bash
   python3 ccom_multiple_leds.py
   ```

3. Follow the on-screen prompts to control the LEDs:

   Enter a number from 0 to 5 to turn LEDs on or off:

   -  0: **LED 0** off
   -  1: **LED 0** on
   -  2: **LED 1** off
   -  3: **LED 1** on
   -  4: **LED 2** off
   -  5: **LED 2** on
   -  Enter Q to quit the program.

### Software Execution GIF

![Execution GIF](/2_Multiple_LEDs_Control/images/result.gif)

## Troubleshooting

- **Port Detection:** Ensure the correct COM port is used for the Arduino. The Python script should automatically detect the port.
- **Permissions:** If you encounter permission issues, ensure your user has access to the COM port by adding your user to the dialout group.

   ```bash
   sudo usermod -aG dialout $USER
   ```
- **LED Connections:** Verify the connections and polarity of the LED.

## Conclusion

This example demonstrates how to control multiple LEDs using serial communication between Arduino and Python. This approach can be expanded to include more complex interactions and control of additional components.


Feel free to explore the other examples in this repository for more advanced projects.

---

### License

This project is licensed under the [MIT License](/LICENSE).

