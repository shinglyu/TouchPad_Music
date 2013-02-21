import simplejson
import music21

def findScoreInfo(score, infoClass): #infoClass can be TImeSignature or other

def split(splitRecFilename, origScoreFilename):
   with open(splitRecFilename, 'r') as f:
      splitRec = simplejson.load(f)
   origScore = music21.converter.parse(origScoreFilename)

   for offsetSegment in splitRec:
      minOffset = min(offsetSegment)
      maxOffset = max(offsetSegment)
      scoreSegment = (origScore.flat.notes
                      .getElementsByOffset(minOffset, maxOffset))
      #get TimeSignature and key
      #prepent TimeSig and Key to scoreSegment, not the init offset 
      #save the scoreSegment to xml

   #refactor this to recursion or something because we need counter
      
      
