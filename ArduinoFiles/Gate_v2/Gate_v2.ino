#include <Servo.h>
 
Servo myservo;  // create servo object to control a servo
 
int pos = 90;    // variable to store the servo position
char incomingByte;

void setup() {
        Serial.begin(9600); 
        myservo.attach(9); //Servo connected to D9
        myservo.write(90); //initial servo position
}

void loop() {
 
        // send data only when you receive data:
        if (Serial.available() > 0) {   // something came across serial
            int integerValue = Serial.parseInt();
            if (integerValue != 0)
              {
              Serial.println(integerValue);
              myservo.write(integerValue);
              }
        }
}
