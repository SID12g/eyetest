import RPi.GPIO as GPIO
import time

buttonPin = 16

GPIO.setwarnings(True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)

#button 눌렀을 때
while True:
    if GPIO.input(buttonPin) == GPIO.HIGH:
        GPIO.output(12, True)
        time.sleep(1)
        
        
GPIO.cleanup()