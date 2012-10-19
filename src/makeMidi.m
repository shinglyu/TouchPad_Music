addpath('../lib/miditoolbox')
addpath('../lib/midirw_java')
csvFilePath= '../records/record_0.txt.processed.csv';
midiFilePath='../midi/mahler_phrase001_score.mid';
outMidiFilePath=[midiFilePath(1:end-4) '.human.mid'];
score = readmidi_java(midiFilePath);%no mex version
%TODO read score
nmat = noEnvelopAnalysis(csvFilePath);
outScore = apply2score(nmat, score);
if (~isempty(outScore))
   writemidi_seconds(outScore, outMidiFilePath);%no mex version
end

