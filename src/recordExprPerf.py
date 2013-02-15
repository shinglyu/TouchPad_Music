#!/usr/bin/python
import os
import argparse
import settings 
import record
import musicGenerator
import music21
def recordAll(score, args, counter = 1): #score needs to be flat
   if len(score) == 0:
      return
   else:
      print("[INFO] Now recording phrase no." + str(counter))
      record.playStream(score); #provide stop button
      recLogFilename = settings.getRecLogFilename(args.scoreFilename +'.'+ str(counter))
      perf = record.record(score, recLogFilename);
      #perf = musicGenerator.generatePerf(score, recLogFilename)
      musicGenerator.savePerf2File(perf, args.outputFilename + '.'+str(counter))
      scoreTail= score[len(perf):]
      recordAll(scoreTail, args, counter+1)

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("scoreFilename", nargs="?" , 
                       help="Input score filename",
                       default=settings.defaultScoreFilename
                      )
   parser.add_argument("outputFilename", nargs="?" , 
                       help="Expressive output filename",
                       default=settings.defaultOutputFilename
                      )
   args = parser.parse_args()

   if settings.DEBUG: print("[DEBUG] Filename: " + args.scoreFilename)
   try:
      score = music21.converter.parse(args.scoreFilename)
   except music21.converter.ConverterException:
      print("[WARN] " + args.scoreFilename+ " is not a score file, skipped.")
      raise

   #recLen = 0;
   #scoreLen = len(score.flat.notes)
   if settings.DEBUG: 
      print("[DEBUG] "), 
      score.flat.show('text')
   recLogFilename = settings.getRecLogFilename(args.scoreFilename)
   notes = score.flat.notes
   recordAll(notes, args = args)


if __name__ == "__main__":
    main()
