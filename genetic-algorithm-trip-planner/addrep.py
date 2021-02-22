# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def ADDREP(chromosome1):
    t=0
    limit=9 # <- - - - - - - - - - - - very important
    chromosome1edited=[0]*limit
    for i in range(1, -chromosome1[-2]-3,2):
        if(chromosome1[i]==chromosome1[i+2]): # to find the duplicates
            chromosome1[i]=0
            chromosome1[i+1]=0
    for i in range(0, -chromosome1[-2]):
        if(chromosome1[i]!=0):
            chromosome1edited[t] = chromosome1[i]
            t=t+1
    chromosome1edited.append(-t)
    return chromosome1edited