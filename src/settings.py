import os

recordPath = '../records/';
scorePath = '../score/'
defaultScoreFilename =  scorePath + 'test2.score.mid'
defaultOutputDir =  recordPath 
defaultOutputFormatExt = '.xml'
defaultOutputFormatName = 'musicxml'
#DEBUG = False;
DEBUG = True;
def getScoreName(scoreFilename):
   #e.g. ../score/test2.score.mid -> test2
   printDebug("scoreFilename: " + scoreFilename)
   scoreName = os.path.basename(scoreFilename)
   scoreName = os.path.splitext(scoreName)[0]
   #e.g. /test2.score -> test2
   if os.path.splitext(scoreName)[1] == '.score':
      scoreName = os.path.splitext(scoreName)[0]
   if os.path.splitext(scoreName)[1] == '.split':
      scoreName = os.path.splitext(scoreName)[0]
   printDebug("scoreName: " + scoreName)
   return scoreName

def getRecLogFilename(counter, scoreFilename, outputDir):
   #test.score.mid > ../record/test.1.log
      recLogFilename = outputDir + getScoreName(scoreFilename)
      recLogFilename += '.'+ str(counter) + '.log'
      return recLogFilename

def getSplitRecFilename(scoreFilename, outputDir):
   #test.score.mid > ../record/test.split.json
   splitRecFilename= outputDir
   splitRecFilename+= getScoreName(scoreFilename)+'.split.json'
   return splitRecFilename

def getOutFilename(counter, scoreFilename, outputDir):
   #test.score.mid > ../record/test.1.perf.xml
   outFilename= outputDir + getScoreName(scoreFilename)
   outFilename+= '.'+ str(counter) + '.perf' + defaultOutputFormatExt
   return outFilename

def getSplittedScoreFilename(counter, scoreFilename, outputDir):
   #test.score.mid > ../record/test.1.score.xml
   splittedScoreFilename = outputDir + getScoreName(scoreFilename)
   splittedScoreFilename += '.'+ str(counter) + '.score' + defaultOutputFormatExt
   return splittedScoreFilename

#def getRecLogFilename(scoreFilename):
#   scoreName = os.path.basename(scoreFilename)
#   return recordPath + scoreName + ".log"
#def getProcessedName(filename):
#   return recordPath + filename + '.processed.csv';
#def getMidiName(filename):
#   return midiPath + filename ;

def printDebug(string):
   if DEBUG:
      print("[DEBUG]"),
      print(string)
