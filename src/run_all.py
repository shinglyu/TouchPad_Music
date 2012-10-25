#!/usr/bin/python
import os
import fnmatch 
import midi 
import record 
import process 
import settings 
import music21
for filename in os.listdir(settings.midiPath): 
   if not fnmatch.fnmatch(filename, '*.mid'): continue;
   if fnmatch.fnmatch(filename, 'test.mid'): continue;
   if settings.DEBUG: print(filename)

   score = midi.readMidi(settings.getMidiName(filename));
   recLen = 0;
   scoreLen = len(score.flat.getElementsByClass(music21.note.Note))
   while(recLen != scoreLen):
      midi.play(score);
      record.record(filename);
      process.preProcess(filename);
      recLen = process.getRecLength(filename);
      if(recLen != scoreLen):
         print('Record length {recLen} is not equal to score length {scLen}, please redo the recording.'.format(recLen = recLen, scLen = scoreLen) );
   process.makeMidi(filename);



   #process(filename)



