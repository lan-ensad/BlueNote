import RPi.GPIO as GPIO 
import re
import time

relayPin = [14, 16, 8, 7, 12]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(relayPin, GPIO.OUT)

##################################################
###     01.txt
#   allpitch = [23, 44, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 65, 66, 68, 70, 71, 73, 75, 76, 80]
#   len = 22
# note1 = [23, 44, 47, 49, 51]
# note2 = [51, 52, 54, 56, 58]
# note3 = [58, 59, 61, 63, 64]
# note4 = [65, 66, 68, 70, 71]
# note5 = [71, 73, 75, 76, 80]
rangeof = [51, 58, 64, 71, 80]
##################################################

##################################################
###     READ FILES
file = open("/home/bluenote/blueNote/_player_expo/01.txt", 'r')
count = 0
extract_number = "\\d+"

def lastChar(s):
    char = s[len(s)-1]
    return char

def goFanGo(n, s):
    if s == 'n':
        GPIO.output(relayPin[n], True)
        print(str(n)+" ON")
    elif s == 'f':
        print(str(n)+" OFF")
        GPIO.output(relayPin[n], False)

def findGoodFan(p):
    if p <= rangeof[0]:
        return 0
    elif p>= rangeof[0] and p<=rangeof[1]:
        return 1
    elif p>= rangeof[1] and p<=rangeof[2]:
        return 2
    elif p>= rangeof[2] and p<=rangeof[3]:
        return 3
    elif p>= rangeof[3]:
        return 4

time.sleep(1)   ##SYNC WITH 01.wav

for line in file:
    count +=1
    x = line.split(" ")

###     DURING NOTES
    tdelay = re.findall(extract_number, x[4])
    delay = int(tdelay[0])

###     PITCH NOTES
    tpitch = re.findall(extract_number, x[2])
    pitch = int(tpitch[0])

###     TRIGGER NOTES
    if delay>=100:
        print(count, end=" ")
        goFanGo(findGoodFan(pitch), lastChar(x[0]))
    else:
        continue

    time.sleep(delay/777)

for x in relayPin:
	GPIO.output(x, False)
