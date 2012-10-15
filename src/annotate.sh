#!/bin/sh
infname="./test.mp3"
outfname="./test.txt"

synclient -m 1 > $outfname &
mplayer -slave -input file=./mplayerCmd $outfname 
