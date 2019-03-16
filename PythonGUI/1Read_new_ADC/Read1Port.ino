//This example shows how to use the Extended ADC Shield for a variety of analog inputs

#include <ExtendedADCShield.h>
#include <SPI.h>

//float data[200];
//Initialize the ADC Shield with default pins and 16-bit ADC (LTC1859)
ExtendedADCShield extendedADCShield(16);

float ch0, ch1, ch2m3, ch4, ch5, ch7m6;
float zeropzero = 0.0;

void setup() {
  Serial.begin(250000);
  //SPI.begin must be called here on Due only
  SPI.begin();
  //Throw out first read (junk data) and configure input 0 as single ended bipolar -5 to +5V
  extendedADCShield.analogReadConfigNext(0, SINGLE_ENDED, BIPOLAR, RANGE10V);
}


void loop() {
  //Read input 0, set up input 1 as single ended unipoloar 0 to 5V
  ch0 =  extendedADCShield.analogReadConfigNext(0, SINGLE_ENDED, BIPOLAR, RANGE10V);
  
  //Print results with 5 decimal places of precision 
  String data = String(ch0) + ',' + String(zeropzero) +  ',' + String(zeropzero) +  ',' + String(zeropzero);

  // Print data to serial in string format, to be split in python
  Serial.println(data); 
  
}  
  
