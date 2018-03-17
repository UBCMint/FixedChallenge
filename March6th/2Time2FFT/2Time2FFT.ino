// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // reads inputs sequentially
  int sensorA0 = analogRead(A0);
  int sensorA1 = analogRead(A1);
  //int sensorA2 = analogRead(A2);
  //int sensorA3 = analogRead(A4);
  //int sensorA2 = sensorA0*2;
  //int sensorA3 = sensorA1*0.5;

  // prints input sequentially
  // to be read and plotted separately
  Serial.println(sensorA0);
  delay(2);
  Serial.println(sensorA1);
  delay(2);
  //Serial.println(sensorA2);
  //delay(2);
  //Serial.println(sensorA3);
  //delay(2);        // delay in between reads for stability
}
