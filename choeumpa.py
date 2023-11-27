import RPi.GPIO as GPIO
import time

GPIO.setwarnings(True)

TRIGER = 24
ECHO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(16, GPIO.OUT)

startTime = time.time()

while True:
    GPIO.output(TRIGER, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(TRIGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGER, GPIO.LOW)
    
    while GPIO.input(ECHO) == GPIO.LOW:
        startTime = time.time()
        
    while GPIO.input(ECHO) == GPIO.HIGH:
        endTime = time.time()
        
    period = endTime - startTime
    dist1 = round(period * 1000000/58 , 2)
    dist2 = round(period * 17241, 2)
    
    print("Dist1", dist1, "cm", ", Dist2", dist2, "cm")
    if dist1 < 10 and dist2 <10:
        GPIO.output(16, True)
        time.sleep(1)
    else:
        GPIO.output(16, False)
        time.sleep(1)
        
GPIO.cleanup()
