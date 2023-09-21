from mido import MidiFile

##################################################
# ###      WRITE MIDI IN FILES
file = open("03.txt", 'w')
mid = MidiFile('03.mid')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
        file.write(str(msg))
        file.write('\n')
##################################################