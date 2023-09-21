#!/bin/bash

# Toutes les 9 à 11 minutes soit 540;660s

###     CONST
logs="logs.txt"
pythonfile=/home/bluenote/blueNote/_player_expo/0
wavfile=/home/bluenote/blueNote/_player_expo/0
mindel=540
maxdel=660

sleep 30

###     SCRIPT ROUTINE
while true; do
    ##  GENERATE NUMBERS
    pick=$((1+RANDOM%3))
    tar=$(shuf -i $mindel-$maxdel -n 1)

    ##  MONITORING & LOGS
    lora=$(date "+%Y-%m-%d %H:%M:%S")
    echo morceau $pick'\t'delay$tar
    msglog="$lora || morceau : $pick || delay : $tar"
    echo $msglog >> $logs

    ##  LAUNCH PROGRAMMS
    cvlc --play-and-exit $wavfile$pick.wav &
    PIDS=$!
    python $pythonfile$pick.py &
    PIDP=$!

    ##  WAIT PROGRAMMS ENDS
    wait $PIDS
    wait $PIDP
    echo END

    ##  DELAY
    sleep $tar
done
