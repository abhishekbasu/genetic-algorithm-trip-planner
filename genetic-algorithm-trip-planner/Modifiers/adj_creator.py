# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

#Abhishek Basu
#Jan-31-2015
#CSV

import timeit #to time the algorithm
import csv #to use csv features

maxlength=21 #This correspond to the maximum stagelength globally 
def DATAPROCESSOR(filename):
	data=[]
	with open(filename, 'rU') as csvfile:
		reader= csv.reader(csvfile, delimiter=',')
		for row in reader:
			data.append(row)
    	return(data)

def FILEWRITER(filename,datalist):
	with open(filename, 'wb') as csvfile:
		writer= csv.writer(csvfile, delimiter=',')
		imax=len(datalist)
		for i in range(0,imax):
			for j in range(1, len(datalist[i])):
				if(len(datalist[i][j]) is not 0):
					writer.writerow([datalist[i][j]]+[datalist[i][0]])
			writer.writerow("\n")


#Timing starts
startt = timeit.default_timer()
#Write code here
data=DATAPROCESSOR("routes.csv") #input the file
#print(data)
FILEWRITER("adjj.csv", data)
#Stop code here
stopt = timeit.default_timer()
print ("Time for the solution was",stopt - startt)
# End of program
'''
if (len(row[i+1]) is not 0): #Longest size issue
						print(row[i])
'''