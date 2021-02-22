# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# File separator
# Purpose is to generate csv files for each busid

import csv

def DATAINPUT(filename):
    inputFile = open(filename,"r")
    dictmain = {}
    i=0
    for line in inputFile:
        d=str.strip(line)
        k=d.split(",")
        reqlength= int(k[1])
        dictmain[str(k[0])+" "+str(k[1])+" "+str(k[2])]=(str(k[3]))
    inputFile.close()
    return dictmain

def DATAOUTPUT(dictionaryfile):
	for keys in dictionaryfile:
		writer = csv.writer(open(("TF"+str(keys).split(" ")[0]+".csv"), 'a'))
		writer.writerow([keys.split(" ")[1],keys.split(" ")[2],dictionaryfile[keys]])

dictmain=DATAINPUT("tripstops_day1.csv")
print dictmain
DATAOUTPUT(dictmain)