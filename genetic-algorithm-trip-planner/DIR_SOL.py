# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from adjcheck import *
def DIR_SOL(adjdictionary, originnode, destinationnode):
    import itertools
    chromset2 = [0]
    nodeid=originnode
    counter=0
    for j in range (0,(len(adjdictionary[nodeid-1]))):
      if int(adjdictionary[nodeid-1][j][1]) == destinationnode:
        mode = int(adjdictionary[nodeid-1][j][0])
        chromset2.append([originnode,mode,destinationnode,0,0,0,0,0,0,-3]) #total length is 10 now
        counter=counter+1
    del chromset2[0]
    if counter>0:
        return (1, chromset2)
    else:
        return (0, 9999)
