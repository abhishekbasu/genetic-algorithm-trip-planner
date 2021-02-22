# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import random
from similaroddgenef import *
from addrep import *
from validcheck import *
from swapgene import *
def MATING(chromset):
    counter=0
    limit2=1 #Number of times chromosomes are chosen for mating process: number of submating processes
    Pc=0.8 #probability of crossover
    initiallength=len(chromset)
    while(counter<limit2):
        num=random.random()
        if(num>Pc):
            t=0
            chromid1=random.randint(0,initiallength-1) #select a random chromosome 1
            chromid2=random.randint(0,initiallength-1) #select a random chromosome 2
            if(chromid1==chromid2 and t<200): #remove the common chromosome selection error
                chromid2=random.randint(0,initiallength-1)
                t=t+1
            if(t>200): #there may be only 1 chromosome in the set, change the limits on initial solution set
                break
            ################Finding feasible points for crossover###############
            SIMILARODDGENE=SIMILARODDGENEF(chromset[chromid1],chromset[chromid2])
            if(SIMILARODDGENE[0]>0):
                if(SIMILARODDGENE[0]==1):
                    x=SWAPGENE(chromset[chromid1], SIMILARODDGENE[1][0],chromset[chromid2], SIMILARODDGENE[1][1])
                    offspring1 = x[0]
                    offspring2 = x[1]
                    tempchromset= [offspring1,offspring2]
                    tempchromset[0]=ADDREP(tempchromset[0])
                    tempchromset[1]=ADDREP(tempchromset[1])
                    chromset.append(tempchromset[0])
                    chromset.append(tempchromset[1])
                if(SIMILARODDGENE[0]!=1):
                    s= random.randrange(1,len(SIMILARODDGENE)-1)
                    ##############################
                    #Select a random similar gene#
                    ##############################
                    t= SIMILARODDGENE[s]
                    y= t[0]
                    z= t[1]
                    x=SWAPGENE(chromset[chromid1], y,chromset[chromid2], z)
                    offspring1 = x[0]
                    offspring2 = x[1]
                    tempchromset= [offspring1,offspring2]
                    tempchromset[0]=ADDREP(tempchromset[0])
                    tempchromset[1]=ADDREP(tempchromset[1])
                    chromset.append(tempchromset[0])
                    chromset.append(tempchromset[1])
                    ################################
                    ############Elitism#############
                    if(chromset[chromid1][-1]<chromset[chromid2][-1]):
                        del chromset[chromid2]
                    else:    
                        del chromset[chromid2]
                    ################################
                    ################Crossover Ends###############
            counter=counter+1
    return(chromset)