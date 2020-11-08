import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER=16 #pin 16 set as trigger
GPIO_ECHO=18 #pin 18 set as ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER,False)
time.sleep(0.5)
while True:
    GPIO.output(GPIO_TRIGGER,True) #trigger pulse sent
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    while GPIO.input(GPIO_ECHO)==0: #echo recieved
        start=time.time()
    while GPIO.input(GPIO_ECHO)==1:
        stop=time.time()
    elapsed=stop-start #Time taken calculated
    distance=34300*elapsed/2 #sonic speed = 34300 cm/s
    print"distance:%.1f"%distance    

    
