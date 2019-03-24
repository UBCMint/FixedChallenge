void setup() {
  Serial.begin(9600);
}

void loop() {
  
  int pA0 = analogRead(A0);
  int pA1 = 0;
  int pA2 = 0;
  int pA3 = 0;
  
  // Converts pin readings to string in csv format
  String data = String(pA0) + ',' + String(pA1) +  ',' + String(pA2) +  ',' + String(pA3);

  // Print data to serial in string format, to be split in python
  Serial.println(data);
  delay(2);
}
