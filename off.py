import time
import RPi.GPIO as GPIO

#we set up the mode of the raspberry pi
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

onPinList = [7, 5, 12, 15, 19, 21, 23, 26, 31, 33, 35, 38]
offPinList = [8, 3, 11, 16, 18, 22, 24, 29, 32, 40, 36, 37]
allPins = onPinList + offPinList

for i in allPins:
    GPIO.setup(i, GPIO.OUT)
    
for i in allPins:
    GPIO.output(i,True)

def turnAllOff():
    for i in allPins:
        GPIO.output(i,True)



turnAllOff() 
        