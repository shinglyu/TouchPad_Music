import music21
import os.path
import collections
import glob
import argparse

import settings
import scoreList 

#outputDir = settings.defaultOutputDir
#outputDir = "../scoreQuarantine/"

#useCorpus = True #False: use real file
useCorpus = False#False: use real file

if useCorpus:
   scoreNameList = scoreList.corpusNameList
else: #use real file
   scoreNameList = scoreList.quarantine2List

def isPureMonophonic(m21Score):
   #settings.printDebug(any(map(lambda n:n.isChord,m21Score.flat.notes)))
   #print(map(lambda n:n.isChord, m21Score.flat.notes))
   if (any(map(lambda n:n.isChord, m21Score.flat.notes))):
      return False;
   return True
   #offsets = map(lambda n:n.offset, m21Score.flat.notes)
   #count = collections.Counter(offsets)
   #hasOverlapNotes = any(map(lambda c:c>1, count))
   #return hasOverlapNotes

def main(path):
   for scoreName in sorted(glob.glob(path)):
      try:
         if useCorpus:
            s = music21.corpus.parse(scoreName)
         else:
            s = music21.converter.parse(scoreName)

         if isPureMonophonic(s):
            tag = "mono"
         #add simple poly
         else:
            tag = "poly at "
            for n in filter(lambda n:n.isChord, s.flat.notes):
               tag = tag + "measure " + str(n.measureNumber) + ":"
               tag = tag + str(n.offset) + " "
         print("* " + scoreName + "\t" + tag)

      #except IOError:
      #   pass
      except (ValueError, AttributeError) as e:
         print("* " + scoreName+ "\tERROR")
         print(e)
         pass
            


if __name__ == "__main__":

   parser = argparse.ArgumentParser()
   parser.add_argument("path", #nargs="1" , 
                       help="Path of score files. e.g. '../scores/*.xml'",
                       #default=config.config["defaultGenScore"]
                      )
   args = parser.parse_args()

   main(args.path)
