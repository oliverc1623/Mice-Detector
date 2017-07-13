#include <Servo.h>
 
Servo myservo;  // create servo object to control a servo
 
int pos = 90;    // variable to store the servo position
int integerValue=0;
char incomingByte;
char readString = '';

void setup() {
        Serial.begin(9600); 
        myservo.attach(9); //Servo connected to D9
        myservo.write(90); //initial servo position
}

void loop(){
         while (!Serial.available()) {} // wait for data to arrive
         while (Serial.available()) // this will be skipped if no data present, leading to          // the code sitting in the delay function below
         {
              delay(30);  //delay to allow buffer to fill 
              if (Serial.available() >0)
            {
            char c = Serial.read();  //gets one byte from serial buffer
            readString += c; //makes the string readString
            }
         }      
}
