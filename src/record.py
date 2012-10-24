#!/usr/bin/python
DEBUG = False;
import subprocess
import os 
import process
import settings 
#infname = './test.mp3';
#outfname = './test.txt';
def record(filename):
   #outPath = '../records/';
   period = 1; # in ms
   cmd = ['synclient',  '-m' , str(period)];
#cmd = ['synclient']; 
   if DEBUG: print(cmd);
   key = 'r';
   while (key == 'r' or key == 'R'):
      #outfname = outPath + filename + '.txt';
      outfname = settings.getRecName(filename);
      with open(outfname, 'w') as outfile:
         p = subprocess.Popen(cmd, stdout = outfile);
      key = raw_input('Press ENTER to continue. Press "R"-Enter to restart.');
      if DEBUG: print(key);
      p.kill();
      #if (key == 'q'):
      #   os.remove(outfname);

def annotate(): #deprecated
   #outPath = '../records/';
   period = 1; # in ms
   cmd = ['synclient',  '-m' , str(period)];
#cmd = ['synclient']; 
   if DEBUG: print(cmd);
   fileNo = 0;
   key = '';
   while (key != 'q'):

      #outfname = outPath + 'record_' + str(fileNo) + '.txt';
      with open(outfname, 'w') as outfile:
         p = subprocess.Popen(cmd, stdout = outfile);
      key = raw_input('Press ENTER to end current recording and continue. Press q-Enter to quit.');
      if DEBUG: print(key);
      p.kill();
      fileNo+=1;
      #if (key == 'q'):
      #   os.remove(outfname);
         

#if (key == ')
#subprocess.call(['mplayer', infname]);
   process.process(outPath)
if __name__ == '__main__':
   annotate();
