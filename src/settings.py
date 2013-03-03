import os

recordPath = '../records/';
scorePath = '../score/'
defaultScoreFilename =  scorePath + 'test2.score.mid'
defaultOutputDir =  recordPath 
defaultOutputFormat = '.mid'
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
