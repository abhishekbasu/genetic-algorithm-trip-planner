# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

#Finding the time difference

samplesolution=[[12, 1102, 59, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 244, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 720, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 919, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 1513, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 1514, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 1515, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 1516, 1101, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5], [12, 1102, 731, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3]]

sample2= [[244, 1102, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3]]
#start
# Find out travel time, waiting time and the arrival time at next stop

def DATATOLIST(filename):
    inputFile = open(filename,"r")
    mainlist = [[(0,0)]]
    for i in range(0,99):
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
    y=1
    invalid=0
    t1=0
    t2=-9999
    while (x==9999):
        for i in range(0,99):
            for j in range(0, len(mainlist[i])):
                if(mainlist[i][j][0]==onode and timesecs<mainlist[i][j][1]):
                    x=i
                    y=0
                    t1=mainlist[i][j][1]
            if i==98:
            	invalid=1
            	y=1
    if(invalid==1):
    	t1=0
    	t2=-9999
    while(y==0 and invalid==0):
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

#print(SCHEDULECHECK(1334,64000,3522,3580))
#end



def VALIDCHECK(chromset, start):  #dependencies: DATAINPUT -> needs the file dictmain
    
	#get the adequate start time
    hours, minutes=start.split(":")
    stime=(int(hours)*3600)+(int(minutes)*60)
    
    for j in range(0,len(chromset)):
        # declaring the main variables for evaluating each solution
        wtime=0 #total waiting time
        ttime=0
        # looking through a particular solution
        for k in range(0,-chromset[j][-1]-1,2): # look through each odd node- busstop
            fromnode = chromset[j][k]
            tonode = chromset[j][k+2]
            mode = chromset[j][k+1]
            waittime, traveltime, stime=SCHEDULECHECK(mode,stime,fromnode,tonode)
            if(stime<0):
            	ttime=999999999999
            	break
            else:
            	wtime+=waittime
            	ttime+=traveltime
        chromset[j].append(1.0*ttime+1*wtime)
    chromset=(sorted(chromset, key=lambda chromset: chromset[-1]))
    return chromset


finalsolution=VALIDCHECK(samplesolution,"10:30")
print(finalsolution)


