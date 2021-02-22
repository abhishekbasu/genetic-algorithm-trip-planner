# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import random
def ADJCHECK(datamatrix, nodeid):
    i = 1
    while (i==1):
    	if(datamatrix[nodeid-1][0][0]==0):
    		return 9999,9999
        if((len(datamatrix[nodeid-1])-1)==0):
        	return int(datamatrix[nodeid-1][0][1]),int(datamatrix[nodeid-1][0][0])
        rdom = random.randrange(0,(len(datamatrix[nodeid-1])-1))
        rnode = int(datamatrix[nodeid-1][rdom][1])
        rmode = int(datamatrix[nodeid-1][rdom][0])
        i=0
    if (rnode==0 or rmode==0):
    	return 9999,9999
    return rnode, rmode