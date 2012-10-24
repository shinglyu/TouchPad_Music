#!/usr/bin/python
import os
import fnmatch 
import midi 
import record 
import process 
import settings 
for filename in os.listdir(settings.midiPath): 
   if not fnmatch.fnmatch(filename, '*.mid'): continue;
   if settings.DEBUG: print(filename)

   score = midi.readMidi(settings.midiPath+filename);
   recLen = 0;
   while(recLen != len(score.length)):
      midi.play(score);
      record.record(filename);
      recLen = process.getRecLength(filename);
process.runMatlab();



   #process(filename)



