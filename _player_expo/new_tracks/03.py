import datetime
import time
import re
import RPi.GPIO as GPIO

relayPin = [14, 16, 8, 7, 12]
stateRelayPin = [False, False, False, False, False]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(relayPin, GPIO.OUT)

start_time = datetime.datetime.now()
file = open("t02.txt", 'r')
extract_number = "\\d+"
lineCount = 0
score = [['btn_0', 'on', '11486\n'], ['btn_1', 'on', '11667\n'], ['btn_2', 'on', '11687\n'], ['btn_0', 'off', '11869\n'], ['btn_3', 'on', '12020\n'], ['btn_1', 'off', '12181\n'], ['btn_2', 'off', '12473\n'], ['btn_2', 'on', '13107\n'], ['btn_2', 'off', '13328\n'], ['btn_1', 'on', '13569\n'], ['btn_3', 'off', '13761\n'], ['btn_1', 'off', '14253\n'], ['btn_0', 'on', '14756\n'], ['btn_0', 'off', '15420\n'], ['btn_0', 'on', '15651\n'], ['btn_1', 'on', '15762\n'], ['btn_2', 'on', '15873\n'], ['btn_0', 'off', '16014\n'], ['btn_1', 'off', '16316\n'], ['btn_2', 'off', '17391\n'], ['btn_3', 'on', '18135\n'], ['btn_3', 'off', '18668\n'], ['btn_0', 'on', '23884\n'], ['btn_1', 'on', '24095\n'], ['btn_0', 'off', '24276\n'], ['btn_2', 'on', '24428\n'], ['btn_1', 'off', '24609\n'], ['btn_3', 'on', '24860\n'], ['btn_2', 'off', '25162\n'], ['btn_4', 'on', '25484\n'], ['btn_3', 'off', '25565\n'], ['btn_4', 'off', '26741\n'], ['btn_4', 'on', '28098\n'], ['btn_3', 'on', '28651\n'], ['btn_4', 'off', '28751\n'], ['btn_3', 'off', '30089\n'], ['btn_0', 'on', '32059\n'], ['btn_1', 'on', '32310\n'], ['btn_0', 'off', '32451\n'], ['btn_2', 'on', '32653\n'], ['btn_1', 'off', '32954\n'], ['btn_3', 'on', '33457\n'], ['btn_2', 'off', '33497\n'], ['btn_4', 'on', '33608\n'], ['btn_3', 'off', '33870\n'], ['btn_4', 'off', '35267\n'], ['btn_4', 'on', '36112\n'], ['btn_3', 'on', '36273\n'], ['btn_4', 'off', '36384\n'], ['btn_2', 'on', '36474\n'], ['btn_3', 'off', '36616\n'], ['btn_2', 'off', '37922\n'], ['btn_4', 'on', '39943\n'], ['btn_3', 'on', '40084\n'], ['btn_1', 'on', '40274\n'], ['btn_2', 'on', '40426\n'], ['btn_4', 'off', '40567\n'], ['btn_0', 'on', '40628\n'], ['btn_3', 'off', '41051\n'], ['btn_1', 'off', '41372\n'], ['btn_2', 'off', '41714\n'], ['btn_0', 'off', '42870\n'], ['btn_0', 'on', '43131\n'], ['btn_1', 'on', '43383\n'], ['btn_0', 'off', '43524\n'], ['btn_1', 'off', '43896\n'], ['btn_1', 'on', '44219\n'], ['btn_2', 'on', '44369\n'], ['btn_3', 'on', '44551\n'], ['btn_1', 'off', '44823\n'], ['btn_2', 'off', '45195\n'], ['btn_3', 'off', '45486\n'], ['btn_3', 'on', '45748\n'], ['btn_2', 'on', '46693\n'], ['btn_3', 'off', '46955\n'], ['btn_2', 'off', '47840\n'], ['btn_0', 'on', '48201\n'], ['btn_1', 'on', '48382\n'], ['btn_2', 'on', '48473\n'], ['btn_0', 'off', '48504\n'], ['btn_1', 'off', '48665\n'], ['btn_2', 'off', '49650\n'], ['btn_2', 'on', '49671\n'], ['btn_2', 'off', '49691\n'], ['btn_2', 'on', '50244\n'], ['btn_3', 'on', '50526\n'], ['btn_3', 'off', '51028\n'], ['btn_2', 'off', '51059\n'], ['btn_4', 'on', '52236\n'], ['btn_4', 'off', '52718\n'], ['btn_3', 'on', '52749\n'], ['btn_3', 'off', '52960\n'], ['btn_1', 'on', '53725\n'], ['btn_1', 'off', '54388\n'], ['btn_0', 'on', '55956\n'], ['btn_1', 'on', '56167\n'], ['btn_0', 'off', '56308\n'], ['btn_2', 'on', '56379\n'], ['btn_1', 'off', '56631\n'], ['btn_2', 'off', '58339\n'], ['btn_0', 'on', '60831\n'], ['btn_1', 'on', '61023\n'], ['btn_0', 'off', '61164\n'], ['btn_2', 'on', '61314\n'], ['btn_1', 'off', '61516\n'], ['btn_2', 'off', '62320\n'], ['btn_1', 'on', '64722\n'], ['btn_2', 'on', '64914\n'], ['btn_3', 'on', '65064\n'], ['btn_1', 'off', '65105\n'], ['btn_4', 'on', '65316\n'], ['btn_2', 'off', '65438\n'], ['btn_3', 'off', '65499\n'], ['btn_1', 'on', '66634\n'], ['btn_4', 'off', '66684\n'], ['btn_3', 'on', '68011\n'], ['btn_3', 'off', '68364\n'], ['btn_2', 'on', '68987\n'], ['btn_1', 'off', '69219\n'], ['btn_3', 'on', '69721\n'], ['btn_2', 'off', '69953\n'], ['btn_3', 'off', '70325\n'], ['btn_3', 'on', '70556\n'], ['btn_3', 'off', '71632\n'], ['btn_0', 'on', '73340\n'], ['btn_1', 'on', '73561\n'], ['btn_0', 'off', '73703\n'], ['btn_2', 'on', '73763\n'], ['btn_3', 'on', '74036\n'], ['btn_1', 'off', '74086\n'], ['btn_2', 'off', '74981\n'], ['btn_3', 'off', '76317\n'], ['btn_4', 'on', '77072\n'], ['btn_3', 'on', '77303\n'], ['btn_4', 'off', '77564\n'], ['btn_4', 'on', '77837\n'], ['btn_3', 'off', '77907\n'], ['btn_4', 'off', '78792\n'], ['btn_4', 'on', '79053\n'], ['btn_1', 'on', '79456\n'], ['btn_1', 'off', '80099\n'], ['btn_4', 'off', '80150\n'], ['btn_1', 'on', '80352\n'], ['btn_4', 'on', '80642\n'], ['btn_1', 'off', '81045\n'], ['btn_4', 'off', '81056\n'], ['btn_4', 'on', '81509\n'], ['btn_3', 'on', '81920\n'], ['btn_2', 'on', '82302\n'], ['btn_1', 'on', '82454\n'], ['btn_0', 'on', '82786\n'], ['btn_4', 'off', '83048\n'], ['btn_1', 'off', '83812\n'], ['btn_2', 'off', '84154\n'], ['btn_3', 'off', '84486\n'], ['btn_0', 'off', '85038\n'], ['btn_4', 'on', '85311\n'], ['btn_1', 'on', '85833\n'], ['btn_3', 'on', '86156\n'], ['btn_1', 'off', '86778\n'], ['btn_3', 'off', '87231\n'], ['btn_4', 'off', '87865']]

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
         GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==1:
      if c=='n':
         print(str(relayPin[n])+" : on")
         GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==2:
      if c=='n':
         print(str(relayPin[n])+" : on")
         GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False
   elif n==3:
      if c=='n':
         print(str(relayPin[n])+" : on")
         GPIO.output(relayPin[n], True)
         stateRelayPin[n] = True
      elif c=='f':
         print(str(relayPin[n])+" : off")
         GPIO.output(relayPin[n], False)
         stateRelayPin[n] = False

while findMillis()<=95765:
   if findMillis() == float(score[lineCount][2]) :
      tpitch = re.findall(extract_number, score[lineCount][0])
      pitch = int(tpitch[0])
      if stateRelayPin[pitch]!=1:
         GoFan(pitch, lastChar(score[lineCount][1]))
      elif stateRelayPin[pitch]!=0:
         GoFan(pitch, lastChar(score[lineCount][1]))
      lineCount +=1