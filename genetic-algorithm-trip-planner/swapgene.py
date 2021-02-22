# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def SWAPGENE(chromosome1,i,chromosome2,j):
    orglen1= -chromosome1[-2]
    orglen2= -chromosome2[-2]
    if(i>0 and j>0):
        newchrom1=[0]
        newchrom2=[0]
        k=0
        for t in range(0,i):
            newchrom1.append(chromosome1[t])
            k=k+1
        for t in range(j,orglen2):
            newchrom1.append(chromosome2[t])
            k=k+1
        newlen1=k
        while(k<=9):
            newchrom1.append(0)
            k=k+1
        newchrom1.append(-newlen1)
        k=0
        for t in range(0,j):
            newchrom2.append(chromosome2[t])
            k=k+1
        for t in range(i,orglen1):
            newchrom2.append(chromosome1[t])
            k=k+1
        while(k<=9):
            newchrom2.append(0)
            k=k+1
        newlen2=k
        newchrom2.append(-newlen2)
        del newchrom2[0]
        del newchrom1[0]
        if(len(newchrom1)>10):
            del newchrom1[:]
            newchrom1=[9999,9999,9999,0,0,0,0,0,0,-3]
        if(len(newchrom2)>10):
            del newchrom2[:]
            newchrom2=[9999,9999,9999,0,0,0,0,0,0,-3]
    return newchrom1, newchrom2

