#include <SimpleDHT.h>
#include<Servo.h>


int pinDHT11 =7;
SimpleDHT11 dht11(pinDHT11);

void setup() {
  Serial.begin(9600);
   
 
}

void loop() {
 
   int amm=analogRead(A0);
  int am=map(amm,0,1023,0,100);
  Serial.print("Ammonia ");
  Serial.print(am);
  Serial.print("%");
    
  // start working...

  
  // read without samples.
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    Serial.print("Read DHT11 failed, err="); Serial.print(SimpleDHTErrCode(err));
    Serial.print(","); Serial.println(SimpleDHTErrDuration(err)); delay(1000);
    return;
  }
  
  Serial.print("       Temperature:  ");
  Serial.print((int)temperature); Serial.print(" C "); Serial.print("  ");
    Serial.print("Humidity:  ");
  Serial.print((int)humidity);  
  Serial.println("");
  int a=temperature;

  // DHT11 sampling rate is 1HZ.
  delay(1500);
}