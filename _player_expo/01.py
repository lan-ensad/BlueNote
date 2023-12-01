import datetime
import time
import re
# import RPi.# GPIO as # GPIO 

relayPin = [14, 16, 8, 7, 12]
stateRelayPin = [False, False, False, False, False]
# GPIO.setwarnings(False)
# GPIO.setmode(# GPIO.BCM) 
# GPIO.setup(relayPin, # GPIO.OUT)

start_time = datetime.datetime.now()
extract_number = "\\d+"
lineCount = 0
score = [['btn_0', 'on', '2472\n'], ['btn_1', 'on', '2674\n'], ['btn_0', 'off', '2814\n'], ['btn_2', 'on', '2905\n'], ['btn_1', 'off', '3086\n'], ['btn_2', 'off', '5268\n'], ['btn_2', 'on', '5328\n'], ['btn_2', 'off', '6012\n'], ['btn_0', 'on', '7649\n'], ['btn_1', 'on', '7962\n'], ['btn_0', 'off', '7982\n'], ['btn_2', 'on', '8686\n'], ['btn_1', 'off', '8736\n'], ['btn_2', 'off', '10898\n'], ['btn_0', 'on', '11501\n'], ['btn_1', 'on', '11742\n'], ['btn_0', 'off', '11933\n'], ['btn_2', 'on', '12014\n'], ['btn_3', 'on', '12376\n'], ['btn_1', 'off', '12497\n'], ['btn_2', 'off', '12929\n'], ['btn_1', 'on', '14045\n'], ['btn_1', 'off', '14950\n'], ['btn_1', 'on', '15212\n'], ['btn_3', 'off', '15433\n'], ['btn_0', 'on', '15714\n'], ['btn_1', 'off', '15745\n'], ['btn_0', 'off', '18981\n'], ['btn_0', 'on', '19816\n'], ['btn_1', 'on', '20017\n'], ['btn_0', 'off', '20078\n'], ['btn_2', 'on', '20219\n'], ['btn_1', 'off', '20359\n'], ['btn_1', 'on', '22651\n'], ['btn_2', 'off', '23083\n'], ['btn_4', 'on', '24300\n'], ['btn_1', 'off', '24421\n'], ['btn_3', 'on', '24572\n'], ['btn_4', 'off', '24793\n'], ['btn_0', 'on', '27849\n'], ['btn_3', 'off', '27889\n'], ['btn_1', 'on', '28141\n'], ['btn_2', 'on', '28362\n'], ['btn_3', 'on', '28564\n'], ['btn_0', 'off', '29338\n'], ['btn_1', 'off', '29860\n'], ['btn_2', 'off', '30423\n'], ['btn_0', 'on', '31991\n'], ['btn_3', 'off', '32011\n'], ['btn_1', 'on', '32193\n'], ['btn_0', 'off', '32304\n'], ['btn_2', 'on', '32354\n'], ['btn_3', 'on', '32606\n'], ['btn_4', 'on', '32908\n'], ['btn_1', 'off', '32919\n'], ['btn_2', 'off', '33140\n'], ['btn_1', 'on', '33985\n'], ['btn_1', 'off', '34557\n'], ['btn_0', 'on', '35924\n'], ['btn_3', 'off', '36055\n'], ['btn_3', 'on', '36106\n'], ['btn_3', 'off', '36146\n'], ['btn_4', 'off', '36147\n'], ['btn_1', 'on', '36268\n'], ['btn_0', 'off', '36540\n'], ['btn_2', 'on', '36691\n'], ['btn_2', 'off', '38440\n'], ['btn_1', 'off', '39173\n'], ['btn_4', 'on', '39736\n'], ['btn_3', 'on', '39948\n'], ['btn_2', 'on', '40330\n'], ['btn_1', 'on', '40552\n'], ['btn_4', 'off', '40643\n'], ['btn_3', 'off', '40935\n'], ['btn_0', 'on', '41266\n'], ['btn_1', 'off', '41729\n'], ['btn_2', 'off', '41739\n'], ['btn_0', 'off', '43086\n'], ['btn_0', 'on', '43307\n'], ['btn_1', 'on', '43700\n'], ['btn_0', 'off', '43951\n'], ['btn_2', 'on', '43952\n'], ['btn_3', 'on', '44203\n'], ['btn_4', 'on', '44505\n'], ['btn_1', 'off', '44536\n'], ['btn_2', 'off', '44607\n'], ['btn_3', 'off', '44708\n'], ['btn_3', 'on', '44758\n'], ['btn_1', 'on', '45582\n'], ['btn_0', 'on', '46346\n'], ['btn_1', 'off', '46448\n'], ['btn_4', 'off', '46518\n'], ['btn_3', 'off', '46558\n'], ['btn_1', 'on', '47383\n'], ['btn_2', 'on', '47715\n'], ['btn_3', 'on', '47906\n'], ['btn_0', 'off', '48319\n'], ['btn_1', 'off', '48329\n'], ['btn_2', 'off', '48340\n'], ['btn_2', 'on', '48350\n'], ['btn_2', 'off', '48361\n'], ['btn_2', 'on', '48371\n'], ['btn_1', 'on', '48794\n'], ['btn_1', 'off', '49537\n'], ['btn_2', 'off', '49547\n'], ['btn_4', 'on', '49759\n'], ['btn_3', 'off', '49860\n'], ['btn_3', 'on', '51066\n'], ['btn_4', 'off', '51228\n'], ['btn_2', 'on', '51378\n'], ['btn_3', 'off', '51620\n'], ['btn_3', 'on', '52002\n'], ['btn_2', 'off', '52053\n'], ['btn_4', 'on', '52204\n'], ['btn_3', 'off', '52265\n'], ['btn_1', 'on', '53652\n'], ['btn_4', 'off', '55350\n'], ['btn_3', 'on', '55883\n'], ['btn_2', 'on', '56216\n'], ['btn_3', 'off', '56406\n'], ['btn_1', 'off', '56487\n'], ['btn_0', 'on', '56749\n'], ['btn_0', 'off', '60618\n'], ['btn_2', 'off', '60628\n'], ['btn_0', 'on', '60840\n'], ['btn_1', 'on', '61072\n'], ['btn_2', 'on', '61263\n'], ['btn_3', 'on', '61564\n'], ['btn_0', 'off', '61846\n'], ['btn_4', 'on', '61977\n'], ['btn_1', 'off', '62611\n'], ['btn_2', 'off', '62982\n'], ['btn_3', 'off', '63767\n'], ['btn_4', 'off', '64491\n'], ['btn_4', 'on', '64803\n'], ['btn_3', 'on', '65085\n'], ['btn_4', 'off', '65427\n'], ['btn_2', 'on', '65457\n'], ['btn_1', 'on', '65729\n'], ['btn_3', 'off', '65749\n'], ['btn_2', 'off', '68101\n'], ['btn_0', 'on', '68663\n'], ['btn_1', 'off', '68715\n'], ['btn_1', 'on', '69217\n'], ['btn_2', 'on', '69559\n'], ['btn_3', 'on', '69841\n'], ['btn_1', 'off', '71620\n'], ['btn_1', 'on', '72012\n'], ['btn_0', 'off', '72254\n'], ['btn_1', 'off', '72756\n'], ['btn_2', 'off', '73159\n'], ['btn_3', 'off', '73411\n'], ['btn_4', 'on', '73652\n'], ['btn_3', 'on', '73924\n'], ['btn_4', 'off', '74085\n'], ['btn_2', 'on', '74206\n'], ['btn_3', 'off', '76025\n'], ['btn_2', 'off', '76699\n'], ['btn_0', 'on', '77111\n'], ['btn_1', 'on', '77352\n'], ['btn_0', 'off', '77604\n'], ['btn_3', 'on', '77745\n'], ['btn_1', 'off', '78650\n'], ['btn_3', 'off', '79665\n'], ['btn_4', 'on', '79876\n'], ['btn_4', 'off', '80490\n'], ['btn_4', 'on', '80792\n'], ['btn_3', 'on', '81004\n'], ['btn_4', 'off', '81185\n'], ['btn_2', 'on', '81296\n'], ['btn_3', 'off', '81506\n'], ['btn_1', 'on', '81558\n'], ['btn_0', 'on', '82010\n'], ['btn_3', 'on', '82302\n'], ['btn_4', 'on', '82553\n'], ['btn_1', 'off', '83679\n'], ['btn_2', 'off', '83719\n'], ['btn_2', 'on', '83800\n'], ['btn_2', 'off', '84344\n'], ['btn_0', 'off', '85580\n'], ['btn_3', 'off', '85922\n'], ['btn_4', 'off', '86907']]

for x in relayPin:
   # GPIO.output(relayPin[i], False)
   print(str(relayPin[x])+" OFF")
   # stateRelayPin[i]=False
   # print(str(i)+" OFF")

def lastChar(s):
    char = s[len(s)-1]
    return char

def findMillis():
   end_time = datetime.datetime.now()
   time_diff = (end_time - start_time)
   execution_time = round((time_diff.total_seconds() * 1000), 0)
   return execution_time

def GoFan(n, c):
   if n ==0:
      if c=='n':
         print(str(relayPin[n])+" : on")
         # GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         # GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==1:
      if c=='n':
         print(str(relayPin[n])+" : on")
         # GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         # GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==2:
      if c=='n':
         print(str(relayPin[n])+" : on")
         # GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         # GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==3:
      if c=='n':
         print(str(relayPin[n])+" : on")
         # GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         # GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False

while findMillis()<=87000:
   # print(findMillis())
   if findMillis() == float(score[lineCount][2]) :
      # print(findMillis())
      tpitch = re.findall(extract_number, score[lineCount][0])
      pitch = int(tpitch[0])
      if stateRelayPin[pitch]!=1:
         GoFan(pitch, lastChar(score[lineCount][1]))
      elif stateRelayPin[pitch]!=0:
         GoFan(pitch, lastChar(score[lineCount][1]))
      else :
         print("???")
      lineCount +=1
      print(lineCount, end=(" "))
      print(findMillis())
   time.sleep(0.0001)

for i in stateRelayPin:
   # GPIO.output(relayPin[i], False)
   stateRelayPin[i]=False
   print(str(i)+" OFF")