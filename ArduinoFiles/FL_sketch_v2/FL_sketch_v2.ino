#include <Servo.h>
 
Servo myservo;  // create servo object to control a servo
 
int pos = 90;    // variable to store the servo position
int integerValue=0;
char incomingByte;

void setup() {
        Serial.begin(9600); 
        myservo.attach(9); //Servo connected to D9
        myservo.write(90); //initial servo position
}
 
void loop() {
 
        // send data only when you receive data:
        if (Serial.available() > 0) {   // something came across serial
          integerValue = 0;         // throw away previous integerValue
          while(1) 
          {            // force into a loop until 'n' is received
            incomingByte = Serial.read();
            if (incomingByte == '\n') break;   // exit the while(1), we're done receiving
            Serial.println(integerValue);
            if (incomingByte == -1) continue;  // if no characters are in the buffer read() returns -1
            integerValue *= 10;  // shift left 1 decimal place
            // convert ASCII to integer, add, and shift left 1 decimal place
            integerValue = ((incomingByte - 48) + integerValue);
           
          }
         Serial.println(integerValue);
         myservo.write(integerValue);
         delay(500);
        }
}

