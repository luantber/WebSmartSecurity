void setup() {
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode (2 , INPUT);
  Serial.begin(9600); 
}


void loop() {
  
  if (digitalRead(2) == 1){
        digitalWrite( 13 , HIGH);            
        digitalWrite( 12 , HIGH);
        Serial.println("Movimiento detectado");        
  }
  else{
    digitalWrite( 13 , LOW);  
    digitalWrite( 12 , LOW);
    Serial.println("Sin datos");
  }
}
