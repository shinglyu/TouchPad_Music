import music21
import os.path
import collections

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
   if (any(map(lambda n:n.isChord,m21Score.flat.notes))):
      return False;
   offsets = map(lambda n:n.offset, m21Score.flat.notes)
   count = collections.Counter(offsets)
   hasOverlapNotes = any(map(lambda c:c>1, count))
   return hasOverlapNotes

for scoreName in scoreNameList:
   try:
      if useCorpus:
         s = music21.corpus.parse(scoreName)
      else:
         s = music21.converter.parse(scoreName)
      if isPureMonophonic(s):
         print('cp ' + scoreName + ' ../scoreQuarantine3/')
         
   except (ValueError, AttributeError):
      print('[ERROR] '+ scoreName+ ' has error.')
      pass


