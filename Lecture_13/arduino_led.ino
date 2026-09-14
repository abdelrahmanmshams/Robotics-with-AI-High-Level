int ledPin = 9;

void setup()
{
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
}

void loop()
{
    if (Serial.available())
    {
        int pwm = Serial.parseInt();

        if (pwm >= 0 && pwm <= 255)
        {
            analogWrite(ledPin, pwm);
        }
    }
}
