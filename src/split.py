#!/usr/bin/python
import settings 
import argparse 
import simplejson
import music21

#def findScoreInfo(score, infoClass): #infoClass can be TImeSignature or other

def computeTimeSigList(origScore):
   sparseElems= origScore.getElementsByClass(music21.meter.TimeSignature)
   notes = origScore.flat.notes
   if len(sparseElems) == 0:
      #use 4/4 as default, need a smart method to determin
      #or maybe specifiy by command line
      print('[WARN] No time signature found in original score! Default 4/4 used')
      return [music21.meter.TimeSignature('4/4')]*len(notes)
   elif len(sparseElems) == 1:
      return [sparseElems[0]]*len(origScore.flat.notes)
   else:
      elemList = []
      elemIter = iter(sparseElems)
      currElem = elemIter.next()
      nextElem = elemIter.next()
      for note in notes:
         if note.offset > nextElem.offset:
            currElem = nextElem
            try:
               nextElem = elemIter.next()
            except StopIteration:
               pass 
            elemList.append(currElem)
         else:
            elemList.append(currElem)
      return elemList

def writeSegments(, counter = 1): #score needs to be flat
   #TODO

def split(splitRecFilename, origScoreFilename):
   with open(splitRecFilename, 'r') as f:
      splitRec = simplejson.load(f)
   origScore = music21.converter.parse(origScoreFilename)

   timeSigList = computeTimeSigList(origScore)

   settings.printDebug(timeSigList)   

   scoreElemsAll= zip(timeSigList) #may have key etc 

   #TODO: Change this for to writeSegments recursion
   for offsetSegment, scoreElems in zip(splitRec, scoreElemsAll):
      minOffset = min(offsetSegment)
      maxOffset = max(offsetSegment)
      scoreSegment = (origScore.flat.getElementsByOffset(minOffset, maxOffset))

      #currentTimeSig = music21.meter.TimeSignature('4/4')
      for scoreElem in scoreElems:
         scoreSegment.insert(scoreSegment[0].offset, scoreElem)
      scoreMeasures = scoreSegment.makeMeasures()

      scoreMeasures.write('musicxml', outFilename)
      #musicXml = music21.musicxml.toMxObjects.streamToMx(scoreMeasures)
      #musicXmlDoc = music21.musicxml.base.Document(musicXml)
      #k
      #with open(outFilename, 'wb') as f:
         #musicXmlDoc.open(f)
         #musicXmlDoc.write()
         #musicXmlDoc.close()
         
      #musicXml.open(outFilename, 'wb')
      #musicXml.write()
      #musicXml.close()
      #musicXmlDoc = music2.musicxml.base.Document(musicXml)
      print('[INFO] Splitted score saved to ' + outFilename)


      #get TimeSignature and key

      #TODO:key

      #prepent TimeSig and Key to scoreSegment, not the init offset 
      #save the scoreSegment to xml

   #refactor this to recursion or something because we need counter

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("split", 
                       help="Path to split record generated by recordExprPerf.py",
                      )
   parser.add_argument("score",  
                       help="Path to score file",
                      )
   args = parser.parse_args()
   split(args.split, args.score)
