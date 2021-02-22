# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def ADJMATRIX(filename):
	    inputFile = open(filename,"r")
	    dictmain = {}
	    i=0
	    for line in inputFile:
	        d=str.strip(line)
	        k=d.split(",")
	        for i in range (1, len(k)-1,2):
	            if((k[i] and k[i+1]) is not ""):
	                dictmain.setdefault(k[0],[]).append((k[i],k[i+1]))
	    inputFile.close()
	    datamatrix=[0]*len(dictmain)
	    i=0
	    for i in range (0,len(dictmain)):
	        datamatrix[i]=(dictmain[str(i+1)])
	    return datamatrix