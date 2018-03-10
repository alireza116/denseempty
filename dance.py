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

jIn = 31
jOut = 32
kIn = 35 
kOut = 36
lIn = 38
lOut = 37

# init list with pin numbers

#the list of all inflate and deflate pins
def turnAllOff():
    for i in allPins:
        GPIO.output(i,True)

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
              



#intro walk through on diagonal 
"""GPIO.output(cIn,False)
GPIO.output(bIn,False)
time.sleep(3)
GPIO.output(bIn,True)
GPIO.output(cIn,True)

GPIO.output(cOut,False)
GPIO.output(bOut,False)
time.sleep(10)
GPIO.output(bOut,True)
GPIO.output(cOut,True)"""

#corner expression - first sequence 
"""GPIO.output(hIn,False)
GPIO.output(jIn,False)
GPIO.output(kIn,False)
time.sleep(16)
GPIO.output(hIn,True)
GPIO.output(jIn,True)
GPIO.output(kIn,True)

GPIO.output(offPinList,False)
time.sleep(12)             #all deflating for 16 sec
GPIO.output(offPinList,True) #all deflating for 16 sec"""


#second sequence
"""GPIO.output(eIn,False)
time.sleep(8)
GPIO.output(iIn,False)
time.sleep(8)
GPIO.output(eIn,True)
GPIO.output(iIn,True)

GPIO.output(iOut,False)
GPIO.output(eOut,False)
time.sleep(8)
GPIO.output(iOut,True)
GPIO.output(eOut,True)"""



#third sequence
#A,D,H
#B,E,I
#F,J

#b,c,g

"""GPIO.output(aOut,False)
GPIO.output(dOut,False)
GPIO.output(hOut,False)
time.sleep(4)
GPIO.output(bOut,False)
GPIO.output(eOut,False)
GPIO.output(iOut,False)
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
time.sleep(12)

GPIO.output(gIn,True)
GPIO.output(cIn,True)
GPIO.output(bIn,True)
GPIO.output(aIn,True)
GPIO.output(dIn,True)
GPIO.output(hIn,True)
GPIO.output(kIn,True)
GPIO.output(lIn,True)"""


GPIO.output(offPinList,False)
time.sleep(12)
GPIO.output(offPinList,True)


///turnAllOff()



