int led_pin = 3;
int vibration_pin = A0;

void setup()
{
    pinMode(led_pin, OUTPUT);
    pinMode(vibration_pin, INPUT);
}

bool last_vibration = false;
int led_state = 0;
void loop()
{
    bool vibration = digitalRead(vibration_pin);
    if (last_vibration != vibration)
    {
        if (vibration) {
            led_state = (led_state + 1) % 4;
            analogWrite(led_pin, led_state * 0x3f);
        }
        delay(100);
    }
    last_vibration = vibration;
} 
