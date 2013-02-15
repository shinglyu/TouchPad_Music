#!/usr/bin/python
import subprocess
import os 
import sys 
import settings 
import music21 
from collections import deque
#infname = './test.mp3';
#outfname = './test.txt';
def playStream(s):
   sp = music21.midi.realtime.StreamPlayer(s)
   sp.play()

def playNote(n):
   s = music21.stream.Stream()
   s.append(n)
   playStream(s)

def record(score, recLogFilename):
   period = 1; # in ms
   print("[INFO] Remember to turn on SHMConfig for the touchpad. See README for detail.")
   cmd = ['synclient',  '-m' , str(period)]
   settings.printDebug(cmd)
   p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
   print('[INFO] Press Ctrl+c to stop recording the current phrase.')
   noteIter = iter(score)
   queue = deque() #enqueue from right, dequeue from left
   perf = []
   prevParsedLine = {'time': 0, 'pressure': 0, 'fingerCount': 0}
   while True:
      try:
         line  = p.stdout.readline()
         settings.printDebug(line)
         sys.stdout.flush()

         #if len(line.split()) == 17: 
            #(time, x, y, z, f, w, l, r, u, d, m, multi, gl, gm, gr, gdx, gdy) = line.split(); 
         if len(line.split()) != 12:
            print('[WARN] Unknown line format. Skipped.');
            continue;

         (time, x, y, z, f, w, l, r, u, d, m, multi) = line.split();
         parsedLine = {'time': float(time), 'pressure': int(z), 'fingerCount': int(f)}
         #recLog.append({'time': float(time), 'pressure': int(z), 'fingerCount': int(f)})

         if parsedLine['fingerCount'] > prevParsedLine['fingerCount']:
            #Note on event
            try:
               note = noteIter.next()
            except StopIteration:
               print('[ERROR]: Your recording is longer than the score. Stopped')
               break
               #raise Exception('[ERROR]: Your recording is longer than the score. Stopped')
            playNote(note)
            queue.append({'onset':parsedLine['time'], 
                          'velocity': parsedLine['pressure'],
                          'pitch': note.pitch,
                          'duration': None
                          })
            #noteon
            settings.printDebug(queue)
         elif parsedLine['fingerCount'] < prevParsedLine['fingerCount']:
            #note off event
            note = queue.popleft()
            settings.printDebug(queue)
            note['duration'] = parsedLine['time'] - note['onset'] 
            perf.append(note)
         prevParsedLine = parsedLine

      except KeyboardInterrupt:
         print('[INFO] Current phrase is cut by user')
         break 

   p.kill()
   return perf

