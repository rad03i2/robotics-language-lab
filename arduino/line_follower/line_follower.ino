const int LEFT_SENSOR = A0;
const int RIGHT_SENSOR = A1;
const int LEFT_MOTOR_PWM = 5;
const int RIGHT_MOTOR_PWM = 6;

int baseSpeed = 120;
float kp = 0.35;

void setup() {
  pinMode(LEFT_MOTOR_PWM, OUTPUT);
  pinMode(RIGHT_MOTOR_PWM, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int leftValue = analogRead(LEFT_SENSOR);
  int rightValue = analogRead(RIGHT_SENSOR);
  int error = leftValue - rightValue;

  int correction = (int)(kp * error);
  int leftSpeed = constrain(baseSpeed - correction, 0, 255);
  int rightSpeed = constrain(baseSpeed + correction, 0, 255);

  analogWrite(LEFT_MOTOR_PWM, leftSpeed);
  analogWrite(RIGHT_MOTOR_PWM, rightSpeed);

  Serial.print("L=");
  Serial.print(leftValue);
  Serial.print(" R=");
  Serial.print(rightValue);
  Serial.print(" LS=");
  Serial.print(leftSpeed);
  Serial.print(" RS=");
  Serial.println(rightSpeed);

  delay(20);
}
