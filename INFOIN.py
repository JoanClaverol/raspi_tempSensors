import RPi.GPIO as GPIO # import libraries
GPIO.setmode(GPIO.BCM) # escull si el tipo de GPIO es board o BCM
GPIO.setup(4,GPIO.IN) # assignan el GPIO 4 que sera d entrada
try: # intenta la seguent accio
    while True: # loop infinit
        input_value = GPIO.input(4) # el port de entrada se't guarda  en el valor input
        print(input_value) 
finally:
    GPIO.cleanup() # si no funciona, stop el try