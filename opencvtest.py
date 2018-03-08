from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import datetime
import RPi.GPIO as IO

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args = vars(ap.parse_args())

redLower = (0, 70, 50)
redUpper = (2, 255, 255)
##redLower = (100,150,0)
##redUpper = (140,255,255)
##redLower = (5, 0, 50)
##redUpper = (10, 150, 200)

pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# otherwise, grab a reference to the video file
else:
    camera = cv2.VideoCapture(args["video"])
(grabbed, frame) = camera.read()
#frame = imutils.resize(frame, width=800)

height, width, channels = frame.shape

# meshW is number of grid in x direction and meshH is number of grid in H direction
meshW = 3
meshH = 3

IO.setmode(IO.BOARD)

def inflate(pin,onOff):
    IO.output(pin,onOff)
    
def deflate(pin,onOff):
    IO.output(pin,onOff)

#width and height of every cell in grid
meshUWidth = width // meshW
meshUHeight = height // meshH
onPinList = [7, 5, 12, 15, 19, 21, 23, 26, 31, 33, 35, 38]
offPinList = [8, 3, 11, 16, 18, 22, 24, 29, 32, 40, 36, 37]
for pin in onPinList + offPinList:
    IO.setup(pin, IO.OUT)

onPinDict = {}
offPinDict = {}

onOffDict = {}

gridOnDict = {"00" : [21,23,12], "01" : [18,21,5], "02": [15,18,7],
              "10" : [33,21,23], "11" : [31,18,21], "12" : [26,15,18],
              "20" : [38,33], "21" : [35,38,31], "22" : [35,26]}

for pin in onPinList:
    onPinDict[pin] = [False,datetime.datetime.now()]
for pin in offPinList:
    offPinDict[pin] = [False,datetime.datetime.now()]
for i,j in zip(onPinList,offPinList):
    onOffDict[i] = j

print (onOffDict)

while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
##    frame = imutils.resize(frame, width=800)
    
    for i in range(meshW -1):
        cv2.line(frame,(meshUWidth * (i+1),0),(meshUWidth * (i+1), meshUHeight * 3),(255,0,0),2)
        
    for i in range(meshH -1):
        cv2.line(frame,(0,meshUHeight * (i+1)),(meshUWidth * 3, meshUHeight * (i+1)),(255,0,0),2)
    
    

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hsv, redLower, redUpper)
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    centroids = []
    # only proceed if at least one contour was found
    toDeflate = []
    toInflate = []
    if len(cnts) > 0:
        for c in cnts:
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 0.2:
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                centroids.append(center)
                cv2.circle(frame, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        detectMatrix = [[0]*meshH for i in range(meshW)]

        for w in range(meshW):
            for h in range(meshH):
                minX = w * meshUWidth
                maxX = minX + meshUWidth
                minY = h * meshUHeight
                maxY = minY + meshUHeight
                check = [(c[0] >= minX and c[0] <= maxX) and (c[1] >=minY and c[1] <= maxY) for c in centroids]

                if any(check):
                    cv2.circle(frame, ((minX + maxX)/2, (minY + maxY)/2),5, (0,255,0),-1)
                    detectMatrix[h][w] = 1
        
        
        for i,row in enumerate(detectMatrix):
            for j,cell in enumerate(row):
                if cell == 1:
                    toInflatePins = gridOnDict[str(i)+str(j)]
                    for pin in toInflatePins:
                        if pin not in toInflate:
                            toInflate.append(pin)
        print toInflate
        
    for pin in onPinList:
        pinStatus = onPinDict[pin]
        if pin in toInflate:      
            delta = datetime.datetime.now() - pinStatus[1]
            if pinStatus[0] == False:
                onPinDict[pin][0] = True
                onPinDict[pin][1] = datetime.datetime.now()
                inflate(pin,False)
        else:
            delta = datetime.datetime.now() - pinStatus[1]
            if pinStatus[0] == True and delta.seconds >5:
                onPinDict[pin][0] = False
                onPinDict[pin][1] = datetime.datetime.now()
                inflate(pin,True)
                toDeflatePin = onOffDict[pin]
                if toDeflatePin not in toDeflate:
                    toDeflate.append(toDeflatePin)
    for pin in toDeflate:
        defDelta = datetime.datetime.now() - offPinDict[pin][1]
        if offPinDict[pin][0] == False and defDelta.seconds > 10:
            offPinDict[pin][0] = True
            offPinDict[pin][1] = datetime.datetime.now()
            inflate(pin,False)
        
    for pin in offPinList:
        delta = datetime.datetime.now() - offPinDict[pin][1]
        if offPinDict[pin][0] == True and delta.seconds > 10:
            offPinDict[pin][0] = False
            offPinDict[pin][1] = datetime.datetime.now()
            inflate(pin,True)
    pts.appendleft(center)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        for pin in offPinList + onPinList:
            inflate(pin,True)
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()