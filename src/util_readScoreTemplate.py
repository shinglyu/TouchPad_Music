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
print("beat\toffset\tpitch")
for note in s.flat.notes:
   print(str(note.beat) + "\t" + str(note.offset) + "\t" + str(note.pitch))
