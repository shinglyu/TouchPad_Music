recordPath = '../records/';
midiPath = '../midi/'
DEBUG = True;
def getRecName(filename):
   return recordPath + filename + '.txt';
def getProcessedName(filename):
   return recordPath + filename + '.txt.processed.csv';
def getMidiName(filename):
   return midiPath + filename + '.mid';

