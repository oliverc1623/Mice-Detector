    #include <Servo.h>

    // Servos to be used
    Servo servo1;
    int pos = 0;    // variable to store the servo position 

    void setup()
    {
      // This is using pin 9 (change accordingly)
      servo1.attach(9);  // attaches the servo on pin 9 to the servo object 
      // initialize the serial port
      Serial.begin(9600);
      servo1.write(130); //initial servo position
    }

    int angle;

    void loop()
    {  
      // wait for the servo angle
      if(Serial.available() > 0)
      {
        angle = Serial.read();
        servo1.write(angle);
        delay(1000);
        
      }
    }
