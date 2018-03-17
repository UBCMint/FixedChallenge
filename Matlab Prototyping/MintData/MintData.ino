// Pin assignments
// Analog input channels
#define ch1 A0
#define ch2
#define ch3
#define ch4

float data, val;

void setup() {
  // Analog pin assignment (read 4 channels)
  pinMode(A0, INPUT);
  Serial.begin(9600); 
  delay(1000);
  Serial.setTimeout(5); 
  setupMATLAB(); 
}

void loop() {
  // Collect analog channel data
  val = analogRead(A0);
  data = val*(5.0/1023.0);
  sendToMATLAB(); 
}

void setupMATLAB() {
  while (! Serial);
  // Handshake with matlab
  Serial.println('a');
  char a = 'b';
  while (a != 'a')
  {
    a = Serial.read();
  }
}

void sendToMATLAB() {
  if (Serial.available() > 0)
  {
    int val = Serial.read();
    delay(10);
    if (val == 'y')
    {
      Serial.println(data);
    } 
  }
}


