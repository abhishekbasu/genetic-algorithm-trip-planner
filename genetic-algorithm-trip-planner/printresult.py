# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def PRINTRESULT(chromset, stopdict, routedict): #updated to take care of no id
        inputFile1 = open(stopdict,"r")
        dictmain1 = {}
        i=0
        for line in inputFile1:
            d=str.strip(line)
            k=d.split(",")
            dictmain1[str(k[0])]=(str(k[1]))
        inputFile1.close()
        inputFile2 = open(routedict,"r")
        dictmain2 = {}
        for line in inputFile2:
            d=str.strip(line)
            k=d.split(",")
            dictmain2[str(k[0])]=(str(k[1]))
        inputFile2.close()
        chromset=(sorted(chromset, key=lambda chromset: chromset[-1]))
        #print("From: "+str(dictmain1[str(chromset[0][0])]))
        #print("To: "+str(dictmain1[str(chromset[0][-chromset[0][-2]-1])])) #-1
        t=0
        for i in range (0, len(chromset)): # Iterate across each solution

            if (chromset[i][-1]<5000 and chromset[i][-1]>0):
                ###
                #m, s = divmod(int(chromset[i][7]), 60)
                #h, m = divmod(m, 60)
                #print("Time of start of this trips is = " + "%d:%02d:%02d" % (h, m, s))
                ###
                print("_____________________________________________________")
                for j in range (0, -chromset[i][-2]): # Iterate on each node
                    if(j%2==0):
                        print("Bus Stop >>>" + " " + dictmain1[str(chromset[i][j])]+" "+"("+str(chromset[i][j]))+")"
                    if(j%2 is not 0):
                        print("Take >>>" + " " + dictmain2[str(chromset[i][j])]+" "+"("+str(chromset[i][j]))+")"
                print("_____________________________________________________")
                print("Time Based Cost Function =  "+ str(chromset[i][-1]))
                t=t+1
        return t
