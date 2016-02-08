import sampleLoader
import logging

def checkLengthMatch(sample):
   score = sample['score'].flat.notes
   perf = sample['perf'].flat.notes

   if len(score) == len(perf):
      return True
   else:
      return False

def checkMatch(sample):
   # if not checkLengthMatch(sample): 
   #    return False

   score = sample['score'].flat.notes
   perf = sample['perf'].flat.notes

   noteNo = 0
   for notesPair in zip(score, perf):
      noteNo  = noteNo + 1
      logging.info(str( notesPair[0].offset) +": " + str( notesPair[0].pitch.name) + " == " + str(notesPair[1].pitch.name))
      if notesPair[0].pitchClass != notesPair[1].pitchClass:
         #logging.error("Mismatch at " + str(noteNo))
         raise Exception("Note mismatch at measure " + str(notesPair[0].measureNumber) +", score:" + str( notesPair[0].pitch ) + " != perf:" + str(notesPair[1].pitch))
         return False
   return True

def main():
   raise NotImplementedError


if  __name__ == '__main__':
   main()

