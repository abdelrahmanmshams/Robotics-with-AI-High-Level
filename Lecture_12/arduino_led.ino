int ledPin = 13;

void setup()
{
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available())
    {
        char data = Serial.read();

        if (data == '1')
        {
            digitalWrite(ledPin, HIGH);
        }
        else if (data == '0')
        {
            digitalWrite(ledPin, LOW);
        }
    }
}
