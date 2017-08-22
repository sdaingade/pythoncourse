# -problem3_6.py *- coding: utf-8 -*-

import sys

inputName = sys.argv[1]
outputName = sys.argv[2]

inFile = open(inputName)
outFile = open(outputName, "w")

for line in inFile:
    #print(len(line), line)
    outFile.write(str(len(line.strip("\r\n"))) + "\n")

inFile.close()
outFile.close()

