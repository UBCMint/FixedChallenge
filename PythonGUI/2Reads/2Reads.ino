void setup() {
  Serial.begin(9600);
}

void loop() {
  
  int pA0 = analogRead(A0);

  // Converts pin readings to string in csv format
  String data = String(pA0);

  // Print data to serial in string format, to be split in python
  int32_t currentMillis = millis();
  Serial.print(data);
  Serial.print(",");
  Serial.println(currentMillis);
  
  delay(2);
}
