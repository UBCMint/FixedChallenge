void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
}

void loop() {
  char inByte= ' ';
  if(Serial.available()){
    char inByte = Serial.read();
    Serial.println(inByte);
    }
delay(100);
}
