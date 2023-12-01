
void setup() {
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);

}

void loop() {
  if(Serial.available() > 0){
    char data = Serial.read();
    if(data == 'x'){
      digitalWrite(7,HIGH);
      digitalWrite(6,LOW);
    }else if(data == 'n'){
      digitalWrite(7,LOW);
      digitalWrite(6,HIGH);
    }

  }

}
