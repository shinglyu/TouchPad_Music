import music21
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("score",  
                    help="Path to score file",
                   )
args = parser.parse_args()

s = music21.converter.parse(args.score)
#s.show('text')
s.show()
#for note in s.flat.notes:
#   print(note.beat)
