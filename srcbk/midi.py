from music21 import *
def waitKey():
   raw_input('Press Enter to continue');

def readMidi(filename):
   return converter.parse(filename);

def playStream(s):
      sp = midi.realtime.StreamPlayer(s)
      sp.play()

def playNRecord(s):
   #s.notes.show()
   for n in s.flat.notes:
      print(n)
      sc = stream.Stream();
      sc.append(n)
      #pt = stream.Part()
      #pt.append(n);
      #sc.show()
      sp = midi.realtime.StreamPlayer(sc)
      sp.play(waitKey())
  #for n in s.flat.notes:
  #       n.microtone = keyDetune[n.midi]
  #       sp = midi.realtime.StreamPlayer(b)
  #       sp.play()
  #       ))]
#
#   s.show();
   
   
