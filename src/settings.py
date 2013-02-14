import os

recordPath = '../records/';
scorePath = '../score/'
defaultScoreFilename =  scorePath + 'test2.score.mid'
defaultOutputFilename=  recordPath + 'test2.perf.mid'
#DEBUG = False;
DEBUG = True;
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
