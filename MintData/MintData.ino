// Pin assignments
// Analog input channels
#define ch1 A0
#define ch2
#define ch3
#define ch4

double data;

void setup() {
  // Analog pin assignment (read 4 channels)
  //pinMode(ch1, INPUT);

  Serial.begin(9600); 
  setupMATLAB(); 
}

void loop() {
  // Collect analog channel data
  //data = analogRead(ch1);
  data = 2.5; //dummy value
  
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
   /*if (val == 'x')
   {
     Serial.println(time);
   } 
    
   delay(10);
   */
   if (val == 'y')
   {
     Serial.println(data);
   } 

   delay(10);
  }
}

