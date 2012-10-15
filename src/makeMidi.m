filePath= '../records/record_0.txt.processed.csv';
%TODO read score
nmat = noEnvelopAnalysis(filePath)
apply2Score(nmat, score);
