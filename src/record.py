#!/usr/bin/python
import subprocess
import os 
import process
import settings 
import music21 
#infname = './test.mp3';
#outfname = './test.txt';
def playStream(s):
   sp = music21.midi.realtime.StreamPlayer(s)
   sp.play()
def record(recLogFilename):
   period = 1; # in ms
   print("[INFO] Remember to turn on SHMConfig for the touchpad. See README for detail.")
   cmd = ['synclient',  '-m' , str(period)];
   settings.printDebug(cmd)
   key = 'r';
   while (key != ''):
      with open(recLogFilename, 'w') as outfile:
         p = subprocess.Popen(cmd, stdout = outfile);
      key = raw_input('Press ENTER to continue, "r"-Enter to restart.');
      settings.printDebug(key)
      p.kill();

#def annotate(): #deprecated
#   #outPath = '../records/';
#   period = 1; # in ms
#   cmd = ['synclient',  '-m' , str(period)];
##cmd = ['synclient']; 
#   if DEBUG: print(cmd);
#   fileNo = 0;
#   key = '';
#   while (key != 'q'):
#
#      #outfname = outPath + 'record_' + str(fileNo) + '.txt';
#      with open(outfname, 'w') as outfile:
#         p = subprocess.Popen(cmd, stdout = outfile);
#      key = raw_input('Press ENTER to end current recording and continue. Press q-Enter to quit.');
#      if DEBUG: print(key);
#      p.kill();
#      fileNo+=1;
#      #if (key == 'q'):
      #   os.remove(outfname);
         

#if (key == ')
#subprocess.call(['mplayer', infname]);
#   process.process(outPath)
#if __name__ == '__main__':
#   annotate();
