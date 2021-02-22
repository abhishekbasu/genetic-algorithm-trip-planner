# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pygmaps
def MAPPLOT(path_array):
	mymap = pygmaps.maps(path_array[0][0], path_array[0][1], 14)
	#	
	################# For Origin and Destination ###################
	mymap.addradpoint(path_array[0][0], path_array[0][1], 95, "#00FF00")
	mymap.addradpoint(path_array[len(path_array)-1][0], path_array[len(path_array)-1][1], 95, "#00FF00")
	################################################################
	for i in range(0, len(path_array)):
		mymap.addpoint(path_array[i][0], path_array[i][1], "##00FFFF")
	path = path_array
	mymap.addpath(path,"#FF0000")
	mymap.draw('./mymap.html')