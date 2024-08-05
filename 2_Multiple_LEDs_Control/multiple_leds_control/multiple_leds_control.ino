const int ledPins[] = {13, 12, 11}; // Pins connected to LEDs
const int numLeds = 3; // Number of LEDs

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming character

    // Check if the command is for turning on or off an LED
    if (command >= '0' && command < '0' + numLeds * 2) {
      int ledIndex = (command - '0') / 2; // Determine which LED to control
      int ledState = (command - '0') % 2; // Determine the state (0: off, 1: on)

      digitalWrite(ledPins[ledIndex], ledState); // Set LED state
      Serial.print("LED ");
      Serial.print(ledIndex);
      Serial.println(ledState ? " is ON" : " is OFF");
    }
  }
}
