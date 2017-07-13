#include <Servo.h>
 
Servo myservo;  // create servo object to control a servo
 
int pos = 90;    // variable to store the servo position
int integerValue=0;
char incomingByte;


void setup() {
    // initialize the digital pin as an output.
    pinMode(ledPin, OUTPUT);     
    pinMode(servopin, OUTPUT);
    
    myServo.attach(9);
    
    Serial.begin (115200);
    Serial.print ("Ready...\n");
}
void loop() {
          digitalWrite(ledPin, HIGH);  // turn LED ON
          
          // While data is sent over serial assign it to the msg
	  while (Serial.available() >= 0){ 
            int msg=Serial.read();

	  }

          digitalWrite(ledPin, HIGH);  // turn LED ON
 
          myServo.write(msg);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
}
