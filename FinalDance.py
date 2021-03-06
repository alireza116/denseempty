import time
import RPi.GPIO as GPIO

#we set up the mode of the raspberry pi
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

onPinList = [7, 5, 12, 15, 19, 21, 23, 26, 31, 40, 35, 38]
offPinList = [8, 3, 11, 16, 18, 22, 24, 29, 32, 33, 36, 37]
allPins = onPinList + offPinList

for i in allPins:
    GPIO.setup(i, GPIO.OUT)



aIn = 7
aOut = 8
bIn = 5
bOut = 3
cIn = 12
cOut = 11
dIn = 15
dOut = 16
eIn = 19 
eOut = 18
fIn = 21
fOut = 22
gIn = 23
gOut = 24
hIn = 26
hOut = 29
iIn = 31
iOut = 32

jIn = 40
jOut = 33

kIn = 35 
kOut = 36
lIn = 38
lOut = 37

# init list with pin numbers

#the list of all inflate and deflate pins
def turnAllOff():
    for i in allPins:
        GPIO.output(i,True)

def AllOnAndOff():
    GPIO.output(onPinList,False)
    time.sleep(5)
    GPIO.output(onPinList,True)

    GPIO.output(offPinList,False)
    time.sleep(15)
    GPIO.output(offPinList,True)
    
def oneByOne(secondsWait):
    for i in range(len(onPinList)):
        GPIO.output(onPinList[i],False)
        time.sleep(secondsWait)
        GPIO.output(onPinList[i],True)
        GPIO.output(offPinList[i],False)
        time.sleep(secondsWait)
        GPIO.output(offPinList[i],True)

def allOnOff(secondsWait):
    for i in onPinList:
        GPIO.output(i,False)
    # here we wait for sevon seconds
    time.sleep(secondsWait)
    for i in onPinList:
        GPIO.output(i, True)

    for i in offPinList:
        GPIO.output(i,False)
    time.sleep(secondsWait)
    for i in offPinList:
        GPIO.output(i,True)
#setup all of of the pins as GPIO.out so this tells the raspberry pi to activates the relays

##
## SETTING UP DONE

##oneByOne(10)
##allOnOff(5)
              


#start dance with ripple effect
        
"""
GPIO.output(aIn,False)
time.sleep(3)

GPIO.output(bIn,False)
time.sleep(3)

GPIO.output(bIn,False)
time.sleep(3)






"""

#part 1
#intro walk through on diagonal 
GPIO.output(cIn,False)
GPIO.output(bIn,False)
time.sleep(4)
GPIO.output(bIn,True)
GPIO.output(cIn,True)

GPIO.output(cOut,False)
GPIO.output(bOut,False)
time.sleep(2)
GPIO.output(eIn,False)
GPIO.output(fIn,False)
time.sleep(4)

GPIO.output(eIn,True)
GPIO.output(fIn,True)
GPIO.output(bOut,True)
GPIO.output(cOut,True)


GPIO.output(eOut,False)
GPIO.output(fOut,False)
time.sleep(2)



#part 2
#corner expression 
GPIO.output(hIn,False)
GPIO.output(iIn,False)
GPIO.output(kIn,False)

time.sleep(4)

GPIO.output(eOut,True)
GPIO.output(fOut,True)

time.sleep(12)

GPIO.output(hIn,True)
GPIO.output(iIn,True)
GPIO.output(kIn,True)

GPIO.output(offPinList,False)
time.sleep(12)             #all deflating for 16 sec
GPIO.output(offPinList,True) #all deflating for 16 sec


#part 3
#dancing around E and I in central zone
GPIO.output(eIn,False)
time.sleep(8)
GPIO.output(iIn,False)
time.sleep(8)
GPIO.output(eIn,True)
GPIO.output(iIn,True)

GPIO.output(iOut,False)
GPIO.output(eOut,False)




#part 4
# walking to opposite corner 
#A,D,H
#B,E,I
#F,J
#b,c,g

GPIO.output(aOut,False)
GPIO.output(dOut,False)
GPIO.output(hOut,False)
time.sleep(4)
GPIO.output(bOut,False)
time.sleep(4)
GPIO.output(aOut,True)
GPIO.output(dOut,True)
GPIO.output(hOut,True)
GPIO.output(bOut,True)
GPIO.output(eOut,True)
GPIO.output(iOut,True)
GPIO.output(fOut,False)
time.sleep(4)
GPIO.output(fOut,True)


#part 5
#outter ring inflate 

GPIO.output(gIn,False)
time.sleep(4)
GPIO.output(cIn,False)
time.sleep(4)
GPIO.output(bIn,False)
time.sleep(4)
GPIO.output(aIn,False)
time.sleep(4)
GPIO.output(dIn,False)
time.sleep(4)
GPIO.output(hIn,False)
time.sleep(4)
GPIO.output(kIn,False)
time.sleep(4)
GPIO.output(lIn,False)
time.sleep(4)
GPIO.output(jIn,False)
time.sleep(12)


#part 6
#outer ring deflate

GPIO.output(jIn,True)
GPIO.output(jOut,False)
time.sleep(6)

GPIO.output(lIn,True)
GPIO.output(lOut,False)
time.sleep(6)

GPIO.output(jOut,True) #turn off j deflater

GPIO.output(kIn,True)
GPIO.output(kOut,False)
time.sleep(6)



GPIO.output(hIn,True)
GPIO.output(hOut,False)
time.sleep(6)

GPIO.output(lOut,True) #turn output fans off after 3 
GPIO.output(kOut,True)
GPIO.output(hOut,True)

GPIO.output(dIn,True)
GPIO.output(dOut,False)
time.sleep(6)

GPIO.output(aIn,True)
GPIO.output(aOut,False)
time.sleep(6)

GPIO.output(bIn,True)
GPIO.output(bOut,False)
time.sleep(6)

GPIO.output(dOut,True) #turn output fans off after 3 
GPIO.output(aOut,True)
GPIO.output(bOut,True)

GPIO.output(cIn,True)
GPIO.output(cOut,False)
time.sleep(6)

GPIO.output(gIn,True)
GPIO.output(gOut,False)
time.sleep(12)

GPIO.output(cOut,True) #turn output fans off after 3 
GPIO.output(gOut,True)


#ending deflate
GPIO.output(offPinList,False)
time.sleep(8)
GPIO.output(offPinList,True)


GPIO.output(onPinList,True)
GPIO.output(offPinList,True)






