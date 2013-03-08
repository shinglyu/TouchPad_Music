import music21
import settings 
from collections import deque

def parseRecLog(filename):
   recLog = []
   settings.printDebug(filename)
   with open(filename, 'r') as recLogFile:
      for line in recLogFile: 
         #settings.printDebug(line.split())
         #if len(line.split()) == 17: 
         #   (time, x, y, z, f, w, l, r, u, d, m, multi, gl, gm, gr, gdx, gdy) = line.split(); 
         if len(line.split()) == 12:
            (time, x, y, z, f, w, l, r, u, d, m, multi) = line.split();
            try: 
               recLog.append({'time': float(time), 'pressure': int(z), 'fingerCount': int(f)})
            except ValueError:
               settings.printDebug('Title line, skipped')
               pass
         else:
            settings.printDebug('Not a data line format in ' + filename + ". Skipped.");
            continue;
   return recLog


def generatePerf(score, recLogFilename):
   recLog = parseRecLog(recLogFilename)
   queue = deque() #enqueue from right, dequeue from left
   perf = []
   noteIter = iter(score)
   for prevLine, thisLine in zip(recLog, recLog[1:]):
      if thisLine['fingerCount'] > prevLine['fingerCount']:
         try:
            note = noteIter.next()
         except StopIteration:
            raise Exception('[ERROR]: Your recording is longer than the score. Stopped')
         queue.append({'onset':thisLine['time'], 
                       'velocity': thisLine['pressure'],
                       'pitch': note.pitch,
                       'duration': None
                       })
         settings.printDebug(queue)
      elif thisLine['fingerCount'] < prevLine['fingerCount']:
         note = queue.popleft()
         settings.printDebug(queue)
         note['duration'] = thisLine['time'] - note['onset'] 
         perf.append(note)
   settings.printDebug(perf)
   return perf

def savePerf2File(perf, outFilename):
   tempo = music21.tempo.MetronomeMark(number=60)
   onsetDuraObjs= [tempo.secondsToDuration(n['onset']) for n in perf]
   #for d in onsetDuraObjs:
   #   settings.printDebug(d) 
   onsets = [d.quarterLength for d in onsetDuraObjs ]
   
   durations= [tempo.secondsToDuration(n['duration']) for n in perf]
   velocities= [n['velocity'] for n in perf]
   pitches = [n['pitch'] for n in perf]
   outStream = music21.stream.Stream()
   for onset, duration, vel, pitch in zip(onsets, durations, velocities, pitches):
      note = music21.note.Note()
      note.duration = duration
      note.volume.velocity = vel
      note.pitch = pitch
      settings.printDebug(onset)
      settings.printDebug(note)
      outStream.insert(onset, note)
   settings.printDebug('')
   outStream.write(settings.defaultOutputFormatName, outFilename)
   #if settings.DEBUG: outStream.show('text')
   #midifile = music21.midi.translate.streamToMidiFile(outStream)
   #midifile.open(outFilename, 'wb')
   #midifile.write()
   #midifile.close()
   print('[INFO] Expressive performance saved to ' + outFilename)

   
