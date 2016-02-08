import os

recordPath = '../records/';
scorePath = '../score/'
defaultScoreFilename =  scorePath + 'test2.score.mid'
defaultOutputDir =  recordPath 
defaultOutputFormat = '.mid'
#DEBUG = False;
DEBUG = True;
def getScoreName(scoreFilename):
   scoreName = os.path.basename(scoreFilename)
   scoreName = os.path.splitext(scoreName)[0]
   if os.path.splitext(scoreName)[1] == '.score':
      scoreName = os.path.splitext(scoreName)[0]
   return scoreName

def getRecLogFilename(scoreFilename):
   scoreName = os.path.basename(scoreFilename)
   return recordPath + scoreName + ".log"
#def getProcessedName(filename):
#   return recordPath + filename + '.processed.csv';
#def getMidiName(filename):
#   return midiPath + filename ;

def printDebug(string):
   if DEBUG:
      print("[DEBUG]"),
      print(string)
