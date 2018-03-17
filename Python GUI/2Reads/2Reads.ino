void setup() {
  Serial.begin(9600);
}

void loop() {
  
  //int pA0 = analogRead(A0);
  //int pA1 = analogRead(A1);

  int pA0 = 1;
  int pA1 = 10;
  // Converts pin readings to string in csv format
  String data = String(pA0) + ',' + String(pA1);

  // Print data to serial in string format, to be split in python
  Serial.println(data);
  delay(2);
}
