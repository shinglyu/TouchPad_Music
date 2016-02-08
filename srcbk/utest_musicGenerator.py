from musicGenerator import *
logFilename = '../records/test.mid.4.log'
outFilename = '../records/test.mid.4.log'
recLog = parseRecLog(logFilename)
settings.printDebug(recLog)

perf = generatePerf(logFilename)
savePerf2File(perf, outFilename)




