# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def DATAINPUT(filename):
	    inputFile = open(filename,"r")
	    dictmain = {}
	    i=0
	    for line in inputFile:
	        d=str.strip(line)
	        k=d.split(",")
	        reqlength= int(k[1])
	        dictmain[k[0]+k[1]+k[2]]=(k[3])
	    inputFile.close()
	    datamatrix=[0]*len(dictmain)
	    i=0
	    for keys in dictmain:
	        datamatrix[i]=(int(keys), int(dictmain[keys]))
	        i=i+1
	    datamatrix=(sorted(datamatrix, key=lambda datamatrix: datamatrix[1]))
	    return datamatrix