import music21
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("score",  
                    help="Path to score file",
                   )
args = parser.parse_args()

s = music21.converter.parse(args.score)
#s.show('text')
#s.flat.notes.show('text')
#s.show()
seg = s.flat.getElementsByOffset(11, 18)
seg = seg.notesAndRests
print(seg.lowestOffset)
#for note in seg.flat.notes:
   #print(str(note.beat) + "\t" + str(note.offset) + "\t" + str(note.pitch))

#seg.show()
#refStream = []
#measure = music21.stream.Measure()
#for elem in seg.flat.notesAndRests:
#    if elem.beat == 1.0:
#        refStream.append(measure)
#        measure = music21.stream.Measure()
#        measure.append(elem)
#    measure.append(elem)
#
#refStream.show()
print(" ")
print(-(seg[0].offset))
seg.shiftElements(-(seg[0].offset))
print(seg.lowestOffset)
for note in seg.flat.notes:
   print(str(note.beat) + "\t" + str(note.offset) + "\t" + str(note.pitch))

#r = music21.note.Rest(quarterLength=1)
#seg.insertAndShift(0, r)
#r = music21.note.Rest(quarterLength=1)
#seg.insertAndShift(0, r)
#r = music21.note.Rest(quarterLength=1)
#seg.insertAndShift(0, r)

segRecreated = seg.makeMeasures()
segRecreated.show('text')

for note in segRecreated.flat.notes:
   print(str(note.beat) + "\t" + str(note.offset) + "\t" + str(note.pitch))
