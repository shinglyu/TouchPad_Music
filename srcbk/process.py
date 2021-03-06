#!/usr/bin/python
DEBUG = True;
#DEBUG = False;
import os
import fnmatch 
import settings 
#import Queue
import subprocess 
#infname = './test.mp3';
#outfname = './test.txt'; 
def preProcess(filename):
   #listfname = './list.txt';
   #with open(listfname, 'r') as listf:
   #   for filename in listf: 
      #for filename in os.listdir(path): 
         #filename = filename.strip('\n');
         #if not fnmatch.fnmatch(filename, '*.txt'): continue;
         #filename = path + filename;
         recName = settings.getRecName(filename);
         if DEBUG: print(recName);
         with open(recName, 'r') as tapFile:
            #recName_noext = os.path.splitext(recName)[0];
            #outFilename = filename + '.processed.csv'
            outFilename = settings.getProcessedName(filename);

            with open(outFilename, 'w') as outFile:
               for line in tapFile: 
                  if DEBUG: print(line.split());
                  if len(line.split()) == 17: (time, x, y, z, f, w, l, r, u, d, m, multi, gl, gm, gr, gdx, gdy) = line.split(); 
                  elif len(line.split()) == 12:
                     (time, x, y, z, f, w, l, r, u, d, m, multi) = line.split();
                  else:
                     print('unknown line format');
                     continue;
                  if (time == 'time'): continue;
                  else:
                     outFile.write(time+ ',' + z + ',' + f + '\n');

                     #tList.add(time);
                     #zList.add(z);
               #polt(tList, zList);

def getRecLength(filename):
   recFile = settings.getProcessedName(filename);
   with open(recFile, 'r') as rec:
      #noteQueue = Queue.Queue();
      noteStack = [];
      length = 0;
      prevMulti = 0;
      for line in rec:
         if settings.DEBUG: print(line.strip().split(','))
         (time, z, multiStr) = line.strip().split(',');
         multi = int(multiStr)
         if (multi - prevMulti > 0):
            noteStack.append(time);
            if (settings.DEBUG):print(len(noteStack));
         elif (multi - prevMulti < 0):
            noteStack.pop();
            if (settings.DEBUG):print(len(noteStack));
            length += 1;
         prevMulti = multi;
   return length;

def makeMidi(filename):
   #cmd = ['bash', './makeMidi.sh'];
   cmd = ['/usr/local/MATLAB/R2010b/bin/matlab', '-nosplash', '-nodesktop', '-nodisplay', '-r', 'makeMidi(\'{fname}\'); quit;'.format(fname = filename)];
   if settings.DEBUG: print(cmd)
   p = subprocess.Popen(cmd);

if __name__ == '__main__':
   preProcess('../records/');
