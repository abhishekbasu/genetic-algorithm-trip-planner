# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from adjcheck import *
from DIR_SOL import *
import itertools


def CHROMOSOME(adjdictionary,numpop, originnode, destinationnode):
        #defining the constants
        limit = 9 #maximum length of chromosome
        counter = 0 #counter to count the number of solutions generated
        chromset = [0]*numpop #total number of solutions
        max_tries = 30 #maximum number of attempts to search a new adjacent node randomly    
        while(counter <= numpop-1):
            ###Initialise a new chromosome###
            chrom = [0]*limit
            previous = originnode
            current = originnode
            chrom[0] = current
            #################################
            checker = 0 #indicates if max_tries condition has been violated
            ###Scan List###
            scan = [0]
            scan[0] = originnode
            ###############
            i=1 #position at the chromosome, 0 is the origin node
            while (current != destinationnode):
                ###Chromosome length condition###
                if(i+2>limit):
                    checker=1
                    break
                #################################
                node=9999
                t=0
                while (t < max_tries):
                    node , mode = ADJCHECK(adjdictionary,previous)
                    if(node not in scan and node is not 0):
                        scan.append(node)
                        break
                    else:
                        t=t+1
                if(t >= max_tries):
                    checker=1
                    break
                current = node
                if (chrom[i-2]==mode):
                    i=i-2
                chrom[i]=(mode)
                chrom[i+1]=(current)
                i=i+2
                previous= node
                if(node==9999 and mode==9999):
                    checker=1
                    break
            del scan[:]
            if (checker==0):
                chrom.append(-i)
                chromset[counter]=(chrom)
                counter=counter+1
        return chromset