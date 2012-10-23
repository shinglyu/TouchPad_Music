#!/usr/bin/python
import os
import fnmatch 
import testReadMidi 
midiPath = '../midi/'
recordPath = '../record/'
for filename in os.listdir(midiPath): 
   if not fnmatch.fnmatch(filename, '*.mid'): continue;
   print(filename)
   score = testReadMidi.readMidi(midiPath+filename);
   testReadMidi.playNRecord(score);
   #record(filename);
   #process(filename)



