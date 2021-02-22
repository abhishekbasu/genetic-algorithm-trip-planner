# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def DATATOLIST(filename):
    inputFile = open(filename,"r")
    mainlist = [[(0,0)]]
    for i in range(0,499):  #Max Descriptor
        mainlist.append([(0,0)])
    i=0
    for line in inputFile:
        d=str.strip(line)
        k=d.split(",")
        mainlist[int(k[0])].append((int(k[1]),int(k[2])))
    inputFile.close()
    return mainlist