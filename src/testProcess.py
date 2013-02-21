#!/usr/bin/python
import process
import settings 

def exist(filename):
   try:
      with open(filename) as f: pass;
   except IOError as e:
      assert True, e;

filename = 'test.mid'

process.preProcess(filename);
exist(settings.getProcessedName(filename));

recLen = process.getRecLength(filename)
print(recLen)
assert(27 == recLen)

process.makeMidi(filename);
exist(settings.getMidiName(filename));

