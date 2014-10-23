'''
Created on 23 okt. 2014

@author: Jaap
'''
from numpy import *
from measurement import *
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as ani;
from measurement.interpol import linInterpolate2D, linInterpolate1D
from measurement.flread import FileReader
from measurement.meas import MeasureFromFile
from Algoritms import singlePeakAlgoritm

#first load the data from file an example peak is now taken
xvec = linspace(10,50,1000);
gamma = 0.3; #scale factor
x0 = 36; #peak position
#now simulate a lorentzian and plot it for reference
yvec = 1 / (math.pi * gamma * (1 + ((xvec - x0)/gamma)*((xvec - x0)/gamma)));
figure(1);
plot(xvec,yvec);

#start the algoritm
#Take a rough scan of the interesting region completely
xMin = min(xvec); #minimum value of the region of interest
xMax = max(xvec); #maximum value of the region of interest
nPoints = 100; #total points to measure
nRough = 20; #amount of points used for rough estimate
fig, ax = plt.subplots();
line, = ax.plot(xvec,yvec, 'x');
xCur = []; #current measured points x values
yCur = []; #current measured points y value
def animate(i,xCur,yCur):
    xCur, yCur = singlePeakAlgoritm.getNewPoint(xCur,yCur,xvec,yvec,nPoints,nRough);
    line.set_xdata(xCur);
    line.set_ydata(yCur);
    return line;
#animate the measurement protocol in a figure
ani = ani.FuncAnimation(fig, animate, np.arange(0,nPoints), interval = 100, repeat = False, fargs = [xCur,yCur]);
show();
