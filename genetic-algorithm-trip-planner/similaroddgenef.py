# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def SIMILARODDGENEF(chromosome1, chromosome2):
    SIMILARODDGENE=[0]
    for i in range(2, -chromosome1[-2]-1,2):
        for j in range(2, -chromosome2[-2]-1,2):
            if(chromosome1[i]==chromosome2[j]):
                SIMILARODDGENE[0]+=1
                SIMILARODDGENE.append((i,j))
    return SIMILARODDGENE