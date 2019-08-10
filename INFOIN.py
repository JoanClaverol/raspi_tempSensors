import RPIO.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
try:
    while True:
	input_value = GPIO.input(14)
	print input_value
finally:
    GPIO.cleanup()