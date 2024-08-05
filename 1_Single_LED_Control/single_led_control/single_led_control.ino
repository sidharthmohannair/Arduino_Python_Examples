const int ledPin = 13; // Pin connected to LED (usually pin 13 for built-in LED)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming character

    if (command == 'H') {
      digitalWrite(ledPin, HIGH); // Turn the LED on
      Serial.println("LED is ON");
    } else if (command == 'L') {
      digitalWrite(ledPin, LOW); // Turn the LED off
      Serial.println("LED is OFF");
    }
  }
}
