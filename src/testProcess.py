#!/usr/bin/python
import process
print('Hello!')
recLen = process.getRecLength('test')
print(recLen)
assert(7 == recLen)
