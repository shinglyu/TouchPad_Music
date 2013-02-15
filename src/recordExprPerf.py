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
      try:
         print("[INFO] Now playing score. You can start to record anytime by pressing Ctrl+c")
         record.playStream(score); #provide stop button
      except KeyboardInterrupt:
         pass
      print("[INFO] =====Now recording phrase no." + str(counter) + "=====")
      #recLogFilename = settings.getRecLogFilename(args.scoreFilename +'.'+ str(counter))
      recLogFilename = args.outputDir + settings.getScoreName(args.scoreFilename)
      recLogFilename += '.'+ str(counter) + '.log'
      record.record(score, recLogFilename);
      perf = musicGenerator.generatePerf(score, recLogFilename)
      outFilename= args.outputDir + settings.getScoreName(args.scoreFilename)
      outFilename+= '.'+ str(counter) + '.perf' + settings.defaultOutputFormat
      musicGenerator.savePerf2File(perf, outFilename)
      scoreTail= score[len(perf):]
      recordAll(scoreTail, args, counter+1)

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("scoreFilename", nargs="?" , 
                       help="Input score filename",
                       default=settings.defaultScoreFilename
                      )
   parser.add_argument("outputDir", nargs="?" , 
                       help="Expressive output directory",
                       default=settings.defaultOutputDir
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
