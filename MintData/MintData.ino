// Pin assignments
// Analog input channels
#define ch1 A0
#define ch2
#define ch3
#define ch4

//double data, val;
float data, val;
void setup() {
  // Analog pin assignment (read 4 channels)
  pinMode(ch1, INPUT);

  Serial.begin(230400); //230400, 115200
  delay(1000);
  Serial.setTimeout(5); //try this 50, 100
  setupMATLAB(); 
}

void loop() {
  // Collect analog channel data
  val = analogRead(ch1);
  data = val*(5.0/1023.0);
  //data = 2.5; //dummy value
  /*data2 = 5;
  data3 = 6;
  data4 = 1;*/
 //Serial.println(data);
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
   //int val = Serial.read();
   /*if (val == 'x')
   {
     Serial.println(time);
   } 
    
   delay(10);
   */
   //if (val == 'y')
   //{
     Serial.println(data);
   //} 

   delay(10);
  }
}

