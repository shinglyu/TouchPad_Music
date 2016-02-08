#Script to print information about scores, include time signature etc.

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

def getTimeSignature(m21Score):
   #settings.printDebug(any(map(lambda n:n.isChord,m21Score.flat.notes)))
   #print(map(lambda n:n.isChord, m21Score.flat.notes))
   string = ""
   tss = m21Score.flat.getTimeSignatures(returnDefault=False)
   #tss = m21Score.flat.getElementsByClass(music21.meter.TimeSignature)
   if len(tss) == 0:
      return "N/A"
   for ts in tss:
      string += ts.ratioString + " " 
   return string

   #offsets = map(lambda n:n.offset, m21Score.flat.notes)
   #count = collections.Counter(offsets)
   #hasOverlapNotes = any(map(lambda c:c>1, count))
   #return hasOverlapNotes
def removeChords(m21Score):
   outStream = music21.stream.Stream()
   for elem in m21Score.flat:
      try:
         if elem.isChord:
            highest = elem.sortAscending()[-1]
            outStream.append(highest)
         else:
            outStream.append(elem)
      except AttributeError:
         outStream.append(elem)
         pass
   return outStream



def main(path):
   for scoreName in sorted(glob.glob(path)):
      try:
         s = music21.converter.parse(scoreName)

         output = removeChords(s)
         if not isPureMonophonic(output):
            print("Remove chord failed!")
         #tag = ""
         #if isPureMonophonic(s):
            #tag = "mono"
         #add simple poly
         #else:
         #   tag = "poly"
         #print(scoreName + "\t" + getTimeSignature(s) + "\t" + tag + "\n")

      #except IOError:
      #   pass
         outFilename = os.path.dirname(scoreName)+ "/../cleanedScores/"+ os.path.basename(scoreName)
         output.write('musicxml', outFilename)
         print('[INFO] '+ outFilename + ' created.')

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
