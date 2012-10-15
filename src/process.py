#!/usr/bin/python
#DEBUG = True;
DEBUG = False;
import os
#infname = './test.mp3';
#outfname = './test.txt';
def process(path):
   #listfname = './list.txt';
   #with open(listfname, 'r') as listf:
   #   for filename in listf: 
      for filename in os.listdir(path): 
         #filename = filename.strip('\n');
         filename = path + filename;
         if DEBUG: print(filename);
         with open(filename, 'r') as tapFile:
            #filename_noext = os.path.splitext(filename)[0];
            outFilename = filename + '.processed.csv'

            with open(outFilename, 'w') as outFile:
               for line in tapFile: 
                  if DEBUG: print(line.split());
                  if len(line.split()) == 17:
                     (time, x, y, z, f, w, l, r, u, d, m, multi, gl, gm, gr, gdx, gdy) = line.split();
                  elif len(line.split()) == 12:
                     (time, x, y, z, f, w, l, r, u, d, m, multi) = line.split();
                  else:
                     print('unknown line format');
                  if (time == 'time'): continue;
                  else:
                     outFile.write(time+ ',' + z + ',' + f + '\n');

                     #tList.add(time);
                     #zList.add(z);
               #polt(tList, zList);

if __name__ == '__main__':
   process('../records/');