import pandas as pd
import numpy as np
from scipy import sparse
def getDemand(filename): 
    """This function returns the demand for each O-D pair in the TAP problem
    
    INPUTS:
    filename: String which the represents the name of the file from which the demand is read
    
    OUTPUTS:
    d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
    """
    
    #Here we open the file
    f  = open(filename, "r")
    
    #Parse through the file line by line
    for line in f.readlines():
    #Get the number of O_D pairs and creates a matrix for these O-D pairs
        if "<NUMBER OF ZONES>" in line: 
            n_origin = int(line.split(">")[1])
            D = np.zeros([n_origin,n_origin])
        #Check number of Origin
        elif "Origin" in line: 
            index_i=int(line.split("\t")[1])
        #Fills row for Origin index_i
        else:
            index_j =line.replace(";",":").split(":") 
            for i in range(0,len(index_j)-2,2):
                D[index_i-1,int(index_j[i].replace(" ",""))-1]=float(index_j[i+1].replace(" ",""))
    
    
    return D