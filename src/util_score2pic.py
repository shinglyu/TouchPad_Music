import music21
import os.path
import collections
import glob
import argparse

import settings
import scoreList 


def main(path):
   for scoreName in sorted(glob.glob(path)):
      os.system("musescore " + scoreName + " -o " + scoreName + ".png")

if __name__ == "__main__":

   parser = argparse.ArgumentParser()
   parser.add_argument("path", #nargs="1" , 
                       help="Path of score files. e.g. '../scores/*.xml'",
                       #default=config.config["defaultGenScore"]
                      )
   args = parser.parse_args()

   main(args.path)
