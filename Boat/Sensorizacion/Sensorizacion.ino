#include "Wire.h"
#include "Ultrasonic.h"
#include "I2Cdev.h"
#include "MPU6050.h"

#define RANGER_PIN 2

Ultrasonic ultrasonic (RANGER_PIN);
MPU6050 accelgyro;

int cms;
int16_t ax, ay, az;
int16_t gx, gy, gz;
int16_t mx, my, mz;

void setup () {
    Wire.begin ();
    Serial.begin (9600);
    accelgyro.initialize ();
}

void loop () {

    if (Serial.available () != 0) {

        int option = Serial.read ();
        cms = ultrasonic.MeasureInCentimeters ();
        accelgyro.getMotion9 (&ax, &ay, &az, &gx, &gy, &gz, &mx, &my, &mz);

        switch (option) {

          case 0x30:
            Serial.print (cms);
            Serial.print ("\n");
            break;

          case 0x31:
            Serial.print (ax);
            Serial.print (" ");
            Serial.print (ay);
            Serial.print (" ");
            Serial.print (az);
            Serial.print ("\n");
            break;

          case 0x32:
            Serial.print (gx);
            Serial.print (" ");
            Serial.print (gy);
            Serial.print (" ");
            Serial.print (gz);
            Serial.print ("\n");
            break;

          case 0x33:
            Serial.print (mx);
            Serial.print (" ");
            Serial.print (my);
            Serial.print (" ");
            Serial.print (mz);
            Serial.print ("\n");
            break;
        }
    }
}