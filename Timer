#include <LiquidCrystal_I2C.h>

int adcValue;
int ButtonL = 9;
int ButtonR = 6;
int ButtonS = 3;
int Buzzer = 11;
int MaxTime = 180;
int rest;
int Store;
int Timer;

int StoredTime = 0;
int StoredRest = 0;
bool temp;

bool downL = false;
bool downS = false;

int digit1 ;
int digit2 ;
int digit3 ;

unsigned long zero = 0;
bool toggle; 
bool state = true; // rest or work time

LiquidCrystal_I2C lcd(0x27, 16, 2); // sets lcd adress to 0x27 for a 16 by 2 line display

void LCDFlash(bool type) { // function to flash top when time is unselected
      
      unsigned long hold;
      hold = millis();
     
     
        if ((hold - zero) >= 700) {         // this uses the time program has ran for () and the zero variable which is updated every 700ms to toggle between on and off states without affectimg refresh rates
        toggle = !toggle;                  // toggles between "Work" and " " so create flashing effect
        zero = hold;
        }

      if (type){                           // type variable is changed depending if system is in rest or work mode
        
        if (toggle){
        
          lcd.setCursor(0, 0);
          lcd.print("Work"); 
          
          }
      

        else { 
          lcd.setCursor(0, 0);
          lcd.print("    ");
        }
     }
     
     else {
        
        if (toggle){
        
          lcd.setCursor(0, 0);
          lcd.print("Rest"); 
          
          }
      

        else { 
          lcd.setCursor(0, 0);
          lcd.print("    ");
        }
      
      }
   
    }


void setup() {
  


  pinMode(ButtonL, INPUT);                      // initialise button pins
  pinMode(ButtonR, INPUT);
  pinMode(ButtonS, INPUT);
  pinMode(Buzzer, OUTPUT);
  digitalWrite(Buzzer,HIGH);

  if (!i2CAddrTest(0x27)) {                // if lcd is not set to 0x27 it attempts adress 0x3F which is apparently common for certain types of displays
  lcd = LiquidCrystal_I2C(0x3F, 16, 2);
  }

  lcd.init();                           // initialize the screen
  lcd.backlight();                      // turn on lcd light

  }


  void loop() {

    adcValue = analogRead(A0);                                  
    Timer = MaxTime -(map(adcValue,0 , 1023 , 0 ,MaxTime));               // the read analog value is also mapped from 0 - 100       
    
    if (StoredTime == 0 && state){    // no stored time + Work timer
    
      LCDFlash(true);
    
      lcd.setCursor(0, 1);            // writes timer to second line
  
     digit1 = Timer/60;         
     digit2 = ((Timer%60)/10) ;
     digit3 = ((Timer%60) - (digit2*10));

     lcd.print(digit1);
     lcd.print(":");
     lcd.print(digit2);
     lcd.print(digit3);

     lcd.print("                "); // removes overlap that may alter number
     delay(5);
    } 

    else if (StoredRest == 0 && !state){   // no stored time + Rest timer
    
      LCDFlash(false);
    
     lcd.setCursor(0, 1);            // writes timer to second line
  
     digit1 = Timer/60;         
     digit2 = ((Timer%60)/10) ;
     digit3 = ((Timer%60) - (digit2*10));

     lcd.print(digit1);
     lcd.print(":");
     lcd.print(digit2);
     lcd.print(digit3);

     lcd.print("                "); // removes overlap that may alter number
      delay(5);
    }
    
    ////////////////

    if(digitalRead(ButtonR)==LOW){             // Button R switches from rest mode to work mode

      delay(150);                              // delay was added to avoid imediate switching when button is pressed
      
      if (digitalRead(ButtonR)== HIGH){
      state = !state;}

    }

    if(digitalRead(ButtonL) == LOW){    // tests if left button is pressed
      
      downL = true;
      
    } 


    //////////////// storing Time


    if (digitalRead(ButtonS)==LOW){          // save button

      temp = false;
      downS= true;

      if(state){

        StoredTime = Timer;

      }

      else if(!state){

        StoredRest = Timer;
       
      }

    }
    

       if (StoredTime != 0 && state){  // Stored Time + work mode no flashing
      
         lcd.setCursor(0, 0);
          lcd.print("Work");
        
        lcd.setCursor(0, 1);            
  
        digit1 = StoredTime/60;         
        digit2 = ((StoredTime%60)/10) ;
        digit3 = ((StoredTime%60) - (digit2*10));

        lcd.print(digit1);
        lcd.print(":");
        lcd.print(digit2);
        lcd.print(digit3);

        lcd.print("                "); 
        delay(5);
        
      } 

     else if (StoredRest != 0 && !state)  {   // Stored Time + Rest mode no flashing
      lcd.setCursor(0, 0);
          lcd.print("Rest");
        
        lcd.setCursor(0, 1);            
  
        digit1 = StoredRest/60;         
        digit2 = ((StoredRest%60)/10) ;
        digit3 = ((StoredRest%60) - (digit2*10));

        lcd.print(digit1);
        lcd.print(":");
        lcd.print(digit2);
        lcd.print(digit3);

        lcd.print("                "); // removes overlap that may alter number
        delay(5);

    }  
      
      while (downL && StoredTime != 0 && StoredRest != 0 ){    // infinite loop when ButtonL is pressed that alternates between Rest and Work
        
      lcd.setCursor(0, 0);
      lcd.print("Work");
      lcd.print("             ");
      
      Store = StoredTime;

      for (int i = Store ; i > 0 ; i--){
        
        lcd.setCursor(0, 1);            
        digit1 = i/60;         
        digit2 = ((i%60)/10) ;
        digit3 = ((i%60) - (digit2*10));

        lcd.print(digit1);
        lcd.print(":");
        lcd.print(digit2);
        lcd.print(digit3);

        lcd.print("                "); 
        delay(1000);

        if (i <= 4){
          digitalWrite(Buzzer, LOW);
          delay(50);
          digitalWrite(Buzzer, HIGH);
        }

      }

         digitalWrite(Buzzer, LOW);
         delay(400);
         digitalWrite(Buzzer, HIGH);
         
         
         
         
    

      lcd.setCursor(0, 0);
      lcd.print("Rest");
      lcd.print("             ");
      
      rest = StoredRest;

      
      for (int i = rest ; i > 0 ; i--){
        
        lcd.setCursor(0, 1);            
        digit1 = i/60;         
        digit2 = ((i%60)/10) ;
        digit3 = ((i%60) - (digit2*10));

        lcd.print(digit1);
        lcd.print(":");
        lcd.print(digit2);
        lcd.print(digit3);

        lcd.print("                "); 
        delay(1000);

        if (i <= 4){
          digitalWrite(Buzzer, LOW);
          delay(50);
          digitalWrite(Buzzer, HIGH);
        }

      }
      
         digitalWrite(Buzzer, LOW);
         delay(200);
         digitalWrite(Buzzer, HIGH);
         delay(200);
         digitalWrite(Buzzer, LOW);
         delay(200);
         digitalWrite(Buzzer, HIGH);


    }

  }

bool i2CAddrTest(uint8_t addr) {
  Wire.begin();  
  Wire.beginTransmission(addr);                  // this returns true or false if connection can be made at adress used above (line 12)
  
  if (Wire.endTransmission() == 0) {
     return true;
    } 
    return false;
}
