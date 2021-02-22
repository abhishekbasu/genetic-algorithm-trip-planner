# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from schedulecheck import *
def VALIDCHECK(chromset, start):  #dependencies: DATAINPUT -> needs the file dictmain    
    hours, minutes=start.split(":")
    stime=(int(hours)*3600)+(int(minutes)*60)
    first_stime = stime
    ftime=stime
    for j in range(0,len(chromset)):
        if (chromset[j][-1]==0):
            chromset[j].append(9999)
        if (chromset[j][-1]>0):
            continue
        else:
            wtime=0 #total waiting time
            ttime=0
            for k in range(0,-chromset[j][-1]-1,2): # look through each odd node- busstop
                fromnode = chromset[j][k]
                tonode = chromset[j][k+2]
                mode = chromset[j][k+1]
                waittime, traveltime, stime = SCHEDULECHECK(mode,stime,fromnode,tonode)
                if(stime<0):
                    ttime=999999999999
                    break
                else:
                    wtime+=waittime
                    ttime+=traveltime
            chromset[j].append(stime-first_stime)
    return chromset