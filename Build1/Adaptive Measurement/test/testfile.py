'''
Created on 20 okt. 2014

@author: Jaap
'''
from numpy import *
from measurement import *
from pylab import *
import matplotlib.pyplot as plt
from measurement.interpol import linInterpolate2D
from measurement.flread import FileReader
from measurement.meas import MeasureFromFile

#try the filereader class
f = FileReader("../Resources/dev2_BGscan_1.dat");
X,Y,Z = f.makeMesh(1,0,6);
#try the measure function
print(MeasureFromFile(-89.2,99.3,"../Resources/dev2_BGscan_1.dat")); 
#try the interpolation function
print(linInterpolate2D(-89.2, 99.3, X, Y, Z, f.x, f.y));

#plot stuff from the file
pcolor(X,Y,Z, cmap=cm.RdBu,vmin=Z.min(),vmax=Z.max());
figure(2);
plot(f.y,Z[:,10]);
show();



'''
with open("../Resources/dev2_BGscan_1.dat",'r') as f:
#loop through all lines except the comments and newlines
    data = [];
    for line in f:
        if((line[0] != '#') & (line[0] != '\n')):
            dataLine = line.split("\t"); # separate the columns in a list
            floatDataLine = []; #create an empty float list
            for dataString in dataLine:
                floatDataLine.append(float(dataString)); #convert to floats
            data.append(floatDataLine); # insert the floats in the main data list
    #Create a numpy array of the data
    numData = array(data);
    #return the requested columns of the data and all if no columns are specified
    print(numData[:,0]);   '''