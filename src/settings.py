recordPath = '../records/';
midiPath = '../midi/'
#DEBUG = False;
DEBUG = True;
def getRecName(filename):
   return recordPath + filename + '.txt';
def getProcessedName(filename):
   return recordPath + filename + '.processed.csv';
def getMidiName(filename):
   return midiPath + filename ;

