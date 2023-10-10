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
score = [['btn_4', 'on', '5758\n'], ['btn_4', 'off', '5939\n'], ['btn_3', 'on', '6160\n'], ['btn_2', 'on', '6271\n'], ['btn_3', 'off', '6322\n'], ['btn_2', 'off', '6382\n'], ['btn_1', 'on', '6533\n'], ['btn_1', 'off', '6684\n'], ['btn_0', 'on', '7087\n'], ['btn_0', 'off', '7258\n'], ['btn_0', 'on', '8182\n'], ['btn_0', 'off', '8353\n'], ['btn_1', 'on', '8514\n'], ['btn_1', 'off', '8626\n'], ['btn_4', 'on', '9510\n'], ['btn_3', 'on', '9581\n'], ['btn_4', 'off', '9652\n'], ['btn_3', 'off', '9733\n'], ['btn_2', 'on', '9933\n'], ['btn_2', 'off', '10035\n'], ['btn_1', 'on', '10849\n'], ['btn_1', 'off', '10980\n'], ['btn_0', 'on', '11663\n'], ['btn_1', 'on', '11814\n'], ['btn_2', 'on', '11915\n'], ['btn_0', 'off', '11976\n'], ['btn_3', 'on', '12117\n'], ['btn_2', 'off', '12228\n'], ['btn_1', 'off', '12268\n'], ['btn_3', 'off', '12831\n'], ['btn_3', 'on', '13063\n'], ['btn_1', 'on', '13184\n'], ['btn_3', 'off', '13325\n'], ['btn_1', 'off', '14199\n'], ['btn_1', 'on', '14401\n'], ['btn_2', 'on', '14643\n'], ['btn_2', 'off', '15035\n'], ['btn_2', 'on', '15327\n'], ['btn_1', 'off', '15598\n'], ['btn_0', 'on', '15800\n'], ['btn_2', 'off', '16704\n'], ['btn_0', 'off', '18282\n'], ['btn_0', 'on', '23900\n'], ['btn_1', 'on', '24111\n'], ['btn_2', 'on', '24181\n'], ['btn_0', 'off', '24193\n'], ['btn_1', 'off', '24333\n'], ['btn_3', 'on', '24384\n'], ['btn_2', 'off', '24475\n'], ['btn_1', 'on', '26525\n'], ['btn_3', 'off', '26656\n'], ['btn_1', 'off', '28013\n'], ['btn_2', 'on', '28134\n'], ['btn_3', 'on', '29823\n'], ['btn_3', 'off', '30234\n'], ['btn_2', 'off', '31923\n'], ['btn_0', 'on', '32195\n'], ['btn_1', 'on', '32416\n'], ['btn_2', 'on', '32577\n'], ['btn_0', 'off', '32678\n'], ['btn_3', 'on', '32739\n'], ['btn_1', 'off', '32860\n'], ['btn_2', 'off', '33022\n'], ['btn_4', 'on', '33102\n'], ['btn_3', 'off', '33253\n'], ['btn_4', 'off', '35695\n'], ['btn_4', 'on', '35997\n'], ['btn_3', 'on', '36148\n'], ['btn_4', 'off', '36249\n'], ['btn_2', 'on', '36320\n'], ['btn_1', 'on', '36470\n'], ['btn_3', 'off', '36662\n'], ['btn_0', 'on', '36783\n'], ['btn_1', 'off', '37065\n'], ['btn_1', 'on', '37527\n'], ['btn_0', 'off', '37589\n'], ['btn_2', 'off', '38342\n'], ['btn_1', 'off', '39639\n'], ['btn_0', 'on', '39911\n'], ['btn_1', 'on', '40182\n'], ['btn_1', 'off', '40936\n'], ['btn_0', 'off', '41861\n'], ['btn_4', 'on', '42153\n'], ['btn_3', 'on', '42455\n'], ['btn_1', 'on', '43309\n'], ['btn_4', 'off', '43621\n'], ['btn_3', 'off', '43641\n'], ['btn_1', 'off', '43893\n'], ['btn_1', 'on', '43974\n'], ['btn_2', 'on', '44024\n'], ['btn_3', 'on', '44266\n'], ['btn_1', 'off', '44477\n'], ['btn_4', 'on', '44568\n'], ['btn_2', 'off', '44589\n'], ['btn_3', 'off', '45081\n'], ['btn_4', 'off', '45544\n'], ['btn_4', 'on', '45775\n'], ['btn_3', 'on', '46188\n'], ['btn_3', 'off', '46430\n'], ['btn_4', 'off', '46430\n'], ['btn_4', 'on', '46983\n'], ['btn_3', 'on', '47285\n'], ['btn_2', 'on', '47788\n'], ['btn_4', 'off', '47829\n'], ['btn_3', 'off', '47969\n'], ['btn_1', 'on', '48010\n'], ['btn_2', 'off', '48181\n'], ['btn_1', 'off', '49427\n'], ['btn_0', 'on', '49658\n'], ['btn_1', 'on', '50906\n'], ['btn_1', 'off', '51207\n'], ['btn_0', 'off', '51820\n'], ['btn_0', 'on', '52112\n'], ['btn_1', 'on', '52354\n'], ['btn_1', 'off', '52756\n'], ['btn_0', 'off', '53068\n'], ['btn_0', 'on', '53551\n'], ['btn_0', 'off', '54264\n'], ['btn_2', 'on', '55028\n'], ['btn_3', 'on', '55310\n'], ['btn_3', 'off', '55723\n'], ['btn_2', 'off', '55743\n'], ['btn_2', 'on', '56045\n'], ['btn_3', 'on', '56186\n'], ['btn_4', 'on', '56287\n'], ['btn_3', 'off', '56338\n'], ['btn_2', 'off', '56348\n'], ['btn_2', 'on', '56379\n'], ['btn_2', 'off', '56389\n'], ['btn_4', 'off', '58972\n'], ['btn_1', 'on', '60660\n'], ['btn_2', 'on', '60932\n'], ['btn_3', 'on', '61153\n'], ['btn_1', 'off', '61486\n'], ['btn_2', 'off', '61707\n'], ['btn_3', 'off', '63295\n'], ['btn_0', 'on', '64802\n'], ['btn_1', 'on', '65074\n'], ['btn_0', 'off', '65215\n'], ['btn_2', 'on', '65426\n'], ['btn_1', 'off', '65709\n'], ['btn_3', 'on', '65980\n'], ['btn_2', 'off', '66232\n'], ['btn_3', 'off', '66564\n'], ['btn_1', 'on', '67016\n'], ['btn_4', 'on', '67298\n'], ['btn_4', 'off', '67750\n'], ['btn_1', 'off', '67801\n'], ['btn_1', 'on', '68184\n'], ['btn_0', 'on', '69038\n'], ['btn_1', 'off', '69089\n'], ['btn_0', 'off', '70606\n'], ['btn_4', 'on', '72365\n'], ['btn_4', 'off', '72606\n'], ['btn_3', 'on', '72898\n'], ['btn_3', 'off', '73079\n'], ['btn_2', 'on', '73421\n'], ['btn_3', 'on', '73632\n'], ['btn_2', 'off', '73814\n'], ['btn_4', 'on', '73815\n'], ['btn_3', 'off', '73996\n'], ['btn_4', 'off', '75121\n'], ['btn_0', 'on', '77010\n'], ['btn_1', 'on', '77172\n'], ['btn_2', 'on', '77262\n'], ['btn_0', 'off', '77314\n'], ['btn_1', 'off', '77575\n'], ['btn_3', 'on', '77666\n'], ['btn_2', 'off', '77767\n'], ['btn_3', 'off', '79354\n'], ['btn_1', 'on', '79366\n'], ['btn_1', 'off', '80451\n'], ['btn_4', 'on', '80944\n'], ['btn_3', 'on', '81286\n'], ['btn_4', 'off', '81346\n'], ['btn_2', 'on', '81638\n'], ['btn_3', 'off', '81729\n'], ['btn_1', 'on', '81850\n'], ['btn_0', 'on', '82223\n'], ['btn_3', 'on', '82544\n'], ['btn_4', 'on', '82896\n'], ['btn_1', 'off', '83460\n'], ['btn_2', 'off', '83842\n'], ['btn_3', 'off', '84384\n'], ['btn_1', 'on', '84716\n'], ['btn_2', 'on', '85089\n'], ['btn_0', 'off', '85220\n'], ['btn_3', 'on', '85683\n'], ['btn_4', 'off', '85783\n'], ['btn_3', 'off', '86115\n'], ['btn_2', 'off', '86749\n'], ['btn_1', 'off', '87684\n'], ['btn_0', 'on', '87744\n'], ['btn_4', 'on', '88086\n'], ['btn_0', 'off', '88307\n'], ['btn_4', 'off', '88751\n'], ['btn_4', 'on', '89414\n'], ['btn_4', 'off', '89625\n'], ['btn_3', 'on', '89877\n'], ['btn_3', 'off', '90098\n'], ['btn_2', 'on', '90400\n'], ['btn_2', 'off', '90582\n'], ['btn_1', 'on', '90863\n'], ['btn_1', 'off', '91095\n'], ['btn_0', 'on', '91376\n'], ['btn_0', 'off', '91587']]

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

while findMillis()<=97000:
   if findMillis() == float(score[lineCount][2]) :
      tpitch = re.findall(extract_number, score[lineCount][0])
      pitch = int(tpitch[0])
      if stateRelayPin[pitch]!=1:
         GoFan(pitch, lastChar(score[lineCount][1]))
      elif stateRelayPin[pitch]!=0:
         GoFan(pitch, lastChar(score[lineCount][1]))
      lineCount +=1