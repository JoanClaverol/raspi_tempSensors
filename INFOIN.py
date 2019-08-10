import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
try:
    while True:
        input_value = GPIO.input(4)
        print(input_value)
finally:
    GPIO.cleanup()