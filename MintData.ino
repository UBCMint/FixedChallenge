// Pin assignments
// Analog input channels
#define ch1 A0
#define ch2
#define ch3
#define ch4

void setup() {
  // put your setup code here, to run once:
  // analog pin assignment (read 4 channels)

  pinMode(ch1, INPUT);

  Serial.begin(9600); 
  setupMATLAB(); 
}

void loop() {
  // put your main code here, to run repeatedly:
  // Collect analog channel data
  analogRead(ch1);
 
  sendToMATLAB(); 
}

void setupMATLAB() {
  Serial.println("setup in MATLAB testing");

  while (! Serial);

//handshake with matlab

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
   if (val == 'x')
   {
     Serial.println(xyPosition[0]);
   } 
    
   delay(10);
   
   if (val == 'y')
   {
     Serial.println(xyPosition[1]);
   } 

   delay(10);
  }
}

