# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def TIMECHECK(datamatrix,start, end):
	    newdatamatrix=[]
	    t=0
	    for i in range(0, len(datamatrix)):
	        if((datamatrix[i][1])>start-50 and (datamatrix[i][1])<end+50):
	            newdatamatrix.append(datamatrix[t])
	            t=t+1
	    return newdatamatrix