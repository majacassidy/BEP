'''
Created on 21 okt. 2014
measures a point(Gate/Bfield,Bias) and returns that
@author: Jaap
'''
from measurement.interpol import linInterpolate2D
from measurement.flread import FileReader


def MeasureFromFile(x,y,file):
    #read the file
    f = FileReader(file);
    X,Y,Z = f.makeMesh();
    measurement = linInterpolate2D(x, y, X,Y,Z,f.x,f.y);
    return measurement;
    
    