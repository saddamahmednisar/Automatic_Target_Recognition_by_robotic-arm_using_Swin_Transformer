#include <Servo.h>

int servoCount = 5;
int servoPins[] = {6,7,3,2,4};  /// pin 7 servo jaw   //pin 6 wrist  //pin 3 Elbow  // pin 4 base 
Servo servos[5];


void setup() {
  Serial.begin(9600);
  
  
  AttachServos();
  
  servos[0].write(10);        ///Wrist     Channel 0 
  servos[1].write(90);         ///Jaws      Channel 1
  servos[2].write(30);        ///elbow  Channel 2
  //servos[3].write(120);        ///shoulder     Channel 3
  servos[4].write(30);        ///Base      Channel 4
  
}

void loop() {
}

void serialEvent() {
  int channel;
  int pos;
  
  channel = Serial.readStringUntil(':').toInt();
  pos = Serial.readString().toInt();
  servos[channel].write(pos);
  Serial.print(channel  );
  Serial.println(pos);
}

void AttachServos() {
  for(int i = 0; i < servoCount; i++) 
  {
    servos[i].attach(servoPins[i]);
  }
 }
