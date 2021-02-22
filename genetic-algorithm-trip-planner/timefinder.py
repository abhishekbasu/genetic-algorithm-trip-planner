# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

'''
def TIMEFINDER(mainlist, timesecs, onode, dnode):
	invalid = 1
	gotvalue = 0
	t1 = 0
	t2 = 99999999
	minstorage = 99999999
	minindexstorage = 1	
	for i in range(0,499):
			for j in range(0, len(mainlist[i])):
				gotvalue = 0
				if(mainlist[i][j][0] == onode  and timesecs <= mainlist[i][j][1]):
					if(mainlist[i][j][1] <= minstorage):
						for s in range(0, len(mainlist[i])):
							if(mainlist[i][s][0] == dnode and mainlist[i][s][1] >= mainlist[i][j][1]):
								t2 = mainlist[i][s][1]
								minstorage = mainlist[i][j][1]
								t1 = minstorage
								minindexstorage = i
								invalid = 0
								gotvalue = 1
								break
				if(gotvalue == 1): break
	if(invalid == 1): #if no values are found
		t1 = 0
		t2 = 99999999
	return(t1,t2)
'''
def INDEXFINDER(mainlist, timesecs, onode):
	invalid = 1
	minstorage = 99999999
	minindexstorage = 99999999
	minstorage1 = 99999999
	minindexstorage1 = 99999999
	for i in range(0,499):
			for j in range(0, len(mainlist[i])):
				if(mainlist[i][j][0] == onode  and timesecs <= mainlist[i][j][1] and mainlist[i][j][1] <= minstorage):
					minindexstorage1 = minindexstorage
					minstorage1 = minstorage
					minstorage = mainlist[i][j][1]
					minindexstorage = i
	return(minindexstorage,minstorage, minindexstorage1,minstorage1)


def TIMEFINDER(mainlist, timesecs, onode, dnode):
	notfound=1
	minindexstorage,minstorage, minindexstorage1,minstorage1 = INDEXFINDER(mainlist,timesecs,onode)
	if(minindexstorage>=9999):
		return(0,99999999)
	for j in range(0,len(mainlist[minindexstorage])):
		if(mainlist[minindexstorage][j][0]==dnode):
			t2=mainlist[minindexstorage][j][1]
			t1=minstorage
			if(t2-t1<0):
				notfound = 1
			else:
				notfound = 0
		if(notfound==1):
			if(minindexstorage1>=9999):
				return(0,99999999)
			if(mainlist[minindexstorage1][j][0]==dnode):
				t2=mainlist[minindexstorage1][j][1]
				t1=minstorage1
				if(t2-t1<0):
					notfound = 1
				else:
					notfound = 0
	if(notfound == 1): #if no values are found
		t1 = 0
		t2 = 99999999
	return(t1,t2)