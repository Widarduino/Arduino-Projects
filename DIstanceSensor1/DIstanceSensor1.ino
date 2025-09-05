#define trigPin 7
#define echoPin 6
#define MAX_DISTANCE 200

float time;
float timeOut = MAX_DISTANCE * 60;  // in microseconds
int soundVelocity = 340; //m/s



void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin,INPUT);
  Serial.begin(9600);
  delay(100);
  Serial.println("Ping,Time");

}

void loop() {
  
  delay(100);
  Serial.print(getSonar());
  Serial.print(" ");
  time = millis() / 1000.00;
  Serial.print(time);
  Serial.println();


}

float getSonar(){

  unsigned long pingTime;
  float distance;

  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  pingTime = pulseIn(echoPin ,HIGH,timeOut);

  distance = (float)pingTime * soundVelocity / 2 / 10000;   // 2 accounts for time it takes to travel back and 10000 convert s to ms
  return distance;
}
