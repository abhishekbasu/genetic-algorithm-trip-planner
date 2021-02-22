# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def PATHRETURN(chromosome, locator):
        inputFile = open(locator,"r")
        dictmain = {}
        i=0
        for line in inputFile:
            d=str.strip(line)
            k=d.split(",")
            dictmain[str(k[0])]=(float(k[1]), float(k[2]))
        inputFile.close()
        path_array=[0]
        for j in range (0, -chromosome[-2]):
            if(j%2==0):
                temp_location = (dictmain[str(chromosome[j])][0],dictmain[str(chromosome[j])][1])
                path_array.append(temp_location)
        del path_array[0]
        return path_array
