#define semgPin A0
int semgValue[2] = {0, 1023};

void setup() {
  Serial.begin(115200);
}

void loop() {
  semgValue[0] = analogRead(semgPin);
  Serial.print(semgValue[0]);
  Serial.print(",");
  Serial.println(semgValue[1]);
  delay(10);
}
