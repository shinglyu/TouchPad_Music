#!/usr/bin/python
import music21
import settings
sBach = music21.corpus.parse('bach/bwv7.7')
mf = music21.midi.translate.streamToMidiFile(sBach.parts[0])
filename = 'testBach'
mf.open(settings.getMidiName(filename), 'wb')
mf.write()
mf.close()




