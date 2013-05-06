import music21
import os.path
import argparse

import settings
import scoreList 

#outputDir = settings.defaultOutputDir
outputDir = "../scoreQuarantine20130505/"

#useCorpus = True #False: use real file
useCorpus = False#False: use real file

if useCorpus:
   scoreNameList = scoreList.corpusNameList
else: #use real file
   #scoreNameList = scoreList.scoreFileList
   scoreNameList = scoreList.monoList


for scoreName in scoreNameList:
   try:
      if useCorpus:
         s = music21.corpus.parse(scoreName)
      else:
         s = music21.converter.parse(scoreName)
      sop = s.parts[0]
      #settings.printDebug(os.path.dirname(scoreName))
      #settings.printDebug(os.path.basename(scoreName))
      #settings.printDebug(os.path.splitext(scoreName))
      #settings.printDebug(os.path.split(scoreName))
      #pathElems = os.path.split(scoreName)[:-1]
      if useCorpus:
         pieceName = scoreName
      else:
         pieceName = os.path.basename(scoreName)
      settings.printDebug(pieceName)
      pathWOtitle= os.path.splitext(pieceName)[0]
      workTitle = '.'.join(pathWOtitle.split('/'))
      #workTitle = os.path.splitext(os.path.basename(scoreName))[0]
      
      outFilename = outputDir + workTitle+ '.score.xml'
      sop.write('musicxml', outFilename)
      print('[INFO] '+ outFilename + ' created.')

      #outFilename = outputDir + workTitle+ '.score.mid'
      #sop.write('midi', outFilename)
      #print('[INFO] '+ outFilename + ' created.')
   except (ValueError, AttributeError):
      print('[ERROR] '+ scoreName+ ' conversion FAILED.')
      pass


