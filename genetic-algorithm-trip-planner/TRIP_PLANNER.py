# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import timeit
import random
import math
import time as TIME
import multiprocessing
from adjmatrix import *
from chromosome import *
from mating import *
from printresult import *
from validcheck import *
import itertools
from pathreturn import *
from mapplot import *

def CLEANER(chromset):
        if len(chromset)>10:
                chromset=list(chromset for chromset,_ in itertools.groupby(chromset))
                chromset=(sorted(chromset, key=lambda chromset: chromset[-1]))
                if len(chromset)>10:
                        del chromset[10:len(chromset)]
        return chromset

def TRIP_PLANNER(origin, destination, time):
        NumPop=10
        adjmatrixfile=ADJMATRIX("ADJ_final.csv")
        startt = timeit.default_timer() #Timer Start
        #####################################
        initialsolution=CHROMOSOME(adjmatrixfile, NumPop, int(origin), int(destination))
        initialsolution.append([720,1101,244,0,0,0,0,0,0,-3])
        initialsolution=VALIDCHECK(initialsolution, str(time))
        initialsolution=CLEANER(initialsolution)
        print(initialsolution)
        #####################################
        matedsolution=MATING(initialsolution)
        matedsolution=VALIDCHECK(matedsolution, str(time))
        matedsolution=CLEANER(matedsolution)
        #####################################
        for k in range(1,5):
                matedsolution=MATING(matedsolution)
                matedsolution=VALIDCHECK(matedsolution, str(time))
                matedsolution=CLEANER(matedsolution)
        #####################################
        finalsolution=matedsolution
        #####################################
        validity = PRINTRESULT(finalsolution,"stop_dictionary.csv","route_dictionary.csv")
        stopt = timeit.default_timer() #Timer Stop    
        if(validity>=1):
                print ("Time for the solution was = "+str(stopt - startt)+" seconds")
                locator = "locator.csv"
                path_array = PATHRETURN(finalsolution[0], locator)
                MAPPLOT(path_array)
        return validity
counter=0

for i in range(1,2):
        valid=TRIP_PLANNER(720, 244, "13:30")
        if(valid>0):
                counter+=1
print(counter)