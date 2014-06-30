#include <Servo.h>
/*
 'Facebook Flagger' (Bean Notifications)
 Release r1-0
 by Colin Karpfinger, Punch Through Design LLC
 Released under MIT license. See LICENSE for details.
 */
#define TWITTER_SERVO_PIN 1
#define FACEBOOK_SERVO_PIN 0
#define TWITTER_SERVO_NOTIFY_POSITION 43
#define FACEBOOK_SERVO_NOTIFY_POSITION 43

Servo twitterServo;
Servo facebookServo;
int twitter_pos=0;
int facebook_pos=0;

void setup() 
{
  // initialize serial communication at 57600 bits per second:
  Serial.begin(57600);
  Serial.setTimeout(25); 
}

void loop() 
{
  char buffer[64];
  size_t readLength = 64;
  uint8_t length = 0;  
  length = Serial.readBytes(buffer, readLength);    
  
  if (length>0)
  {  
    for (int i=0; i<length; i++){
      if (buffer[i]=='T'){
        twitterServo.attach(TWITTER_SERVO_PIN);
        delay(100);
        twitterServo.write(TWITTER_SERVO_NOTIFY_POSITION-20);
        delay(500);
        twitterServo.write(TWITTER_SERVO_NOTIFY_POSITION+20);
        delay(200);
        twitterServo.write(TWITTER_SERVO_NOTIFY_POSITION);
        delay(200);
        twitterServo.detach();    //detach so motor turns off and doesn't make buzzing sound.
      }
      else if (buffer[i]=='F'){
        facebookServo.attach(FACEBOOK_SERVO_PIN);
        delay(100);
        facebookServo.write(FACEBOOK_SERVO_NOTIFY_POSITION-20);
        delay(500);
        facebookServo.write(FACEBOOK_SERVO_NOTIFY_POSITION+20);
        delay(200);
        facebookServo.write(FACEBOOK_SERVO_NOTIFY_POSITION);
        delay(200);
        facebookServo.detach();    //detach so motor turns off and doesn't make buzzing sound.
      }
    }
  }
  Bean.sleep(10000);            //sleep for 10 seconds to conserve battery
}
