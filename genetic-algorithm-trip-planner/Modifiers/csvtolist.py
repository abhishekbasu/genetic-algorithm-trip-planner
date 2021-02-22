# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Find out travel time, waiting time and the arrival time at next stop

def DATATOLIST(filename):
    inputFile = open(filename,"r")
    mainlist = [[(0,0)]]
    for i in range(0,70):
    	mainlist.append([(0,0)])
    #print(mainlist)
    i=0
    for line in inputFile:
        d=str.strip(line)
        k=d.split(",")
       	mainlist[int(k[0])].append((int(k[1]),int(k[2])))
    inputFile.close()
    return (mainlist)


def TIMEFINDER(mainlist, timesecs, onode, dnode):
    x=9999
    y=0
    while (x==9999):
        for i in range(0,70):
            for j in range(0, len(mainlist[i])):
                if(mainlist[i][j][0]==onode and timesecs<mainlist[i][j][1]):
                    x=i
                    t1=mainlist[i][j][1]
    while(y==0):
        for j in range(0, len(mainlist[x])):
            if(mainlist[x][j][0]==dnode):
                t2=mainlist[x][j][1]
                y=1
    return(t1,t2)

def SCHEDULECHECK(busid, startt, onode, dnode):
    mainlist=DATATOLIST("TF"+str(busid)+".csv")
    t1,t2=TIMEFINDER(mainlist, startt, onode, dnode )
    waittime=t1-startt
    traveltime=t2-t1
    newstartt=t2
    return(waittime, traveltime, newstartt)

print(SCHEDULECHECK(1334,64000,3522,3580))
