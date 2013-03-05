#!/usr/bin/python
import subprocess
import os 
import sys 
import settings 
import music21 
import threading
from collections import deque

def playStream(s):
   sp = music21.midi.realtime.StreamPlayer(s)
   sp.play()

def playNote(n):
   s = music21.stream.Stream()
   s.append(n)
   playStream(s)

def record(score, recLogFilename):
   settings.printDebug(recLogFilename)
   period = 1; # in ms
   print("[INFO] Remember to turn on SHMConfig for the touchpad. See README for detail.")
   cmd = ['synclient',  '-m' , str(period)]
   settings.printDebug(cmd)
   p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
   print('[INFO] Press Ctrl+c to cut off the current phrase.')
   noteIter = iter(score)
   recLogLines = ['time\t y\t z\t f\t w\t l\t r\t u\t d\t m\t multi\n']
   prevFingerCount= 0
   while True:
      try:
         line  = p.stdout.readline()
         settings.printDebug(line),
         sys.stdout.flush()

         if len(line.split()) != 12:
            settings.printDebug('Not a data line format. Skipped.'),
            continue;

         (time, x, y, z, f, w, l, r, u, d, m, multi) = line.split();
         fingerCount = int(f)

         if fingerCount > prevFingerCount:
            #Note on event
            settings.printDebug("Note ON")
            try:
               note = noteIter.next()
            except StopIteration:
               print('[ERROR]: Your recording is longer than the score. Force cut.')
               break
               #raise Exception('[ERROR]: Your recording is longer than the score. Stopped')
            t = threading.Thread(target=playNote, args=(note,))
            t.start()
            #playNote(note)

         recLogLines.append(line)
         prevFingerCount = fingerCount

      except KeyboardInterrupt:
         print('[INFO] Current phrase is cut by user')
         break 

   p.kill()
   with open(recLogFilename, 'w') as f:
      f.writelines(recLogLines)

