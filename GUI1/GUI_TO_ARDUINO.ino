byte received = 0;

void Pinconfigure(int x){

  if (x == 10){
    digitalWrite(13,LOW);
  }
  else if(x == 20) {
    digitalWrite(10,LOW);
  }

  else if (x == 11){
    digitalWrite(13,HIGH);
  }

  else if (x == 21){
    digitalWrite(10,HIGH);
  }

}

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);

  pinMode(13,OUTPUT);
  pinMode(10,OUTPUT);


}

void loop() {
  

  if (Serial.available() > 0 ){

    received = Serial.parseInt();
    Serial.println(received);
    
  }


  Pinconfigure(received);
  

  
  

}
