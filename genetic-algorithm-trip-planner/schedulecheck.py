# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

############################################
#Program to open the TF trip time file and
#Find the waiting time, travel time and
#New start time
############################################

from timefinder import *
from datatolist import *
def SCHEDULECHECK(busid, startt, onode, dnode):
    try:
        mainlist = DATATOLIST("TF"+str(busid)+".csv")
        t1,t2 = TIMEFINDER(mainlist, startt, onode, dnode)
        waittime = t1-startt
        traveltime = t2-t1
        newstartt = t2
        return(waittime, traveltime, newstartt)
    except IOError:
        print("IOERROR", str(busid))
        waittime=999999999999
        traveltime=999999999999     
        newstartt=999999999999
        return(waittime, traveltime, newstartt)