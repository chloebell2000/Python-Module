//latching switches

#define BUTTON 2
#define LED_R 9
int oldVal = HIGH;
int newVal;
bool isOn = false;

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(LED_R, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  newVal = digitalRead(BUTTON);
  if(newVal !=oldVal){
    if(newVal ==LOW){
      isOn = !isOn;
    }
  }
  if(isOn){
  digitalWrite(LED_R, HIGH);
  }
  else{
    digitalWrite(LED_R, LOW);
  }
    oldVal = newVal;
    delay(50);
    }
