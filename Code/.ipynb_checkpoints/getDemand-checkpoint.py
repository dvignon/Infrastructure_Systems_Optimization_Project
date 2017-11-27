import pandas as pd
import numpy as np
from scipy import sparse
def getDemand(filename, L): 
    """This function returns the demand for each O-D pair in the TAP problem
    
    INPUTS:
    filename: String which the represents the name of the file from which the demand is read
    
    OUTPUTS:
    d: N-by-K Scipy sparse array where d[:,k] is the demand vector for OD pair k and where each row corresponds to a node
    """
    
    #Here we open the file
    f  = open(filename, "r")
         
    #Parse through the file line by line
    for line in f.readlines():
    #Get the number of O_D pairs and creates a matrix for these O-D pairs
        if "<NUMBER OF ZONES>" in line: 
            n_OD = int(line.split(">")[1])
            D = np.zeros([n_OD,n_OD])
            OD_pair = []
        #Check number of Origin
        elif "Origin" in line:
            #print(line.replace(" ","\t").split("\t"))
            #index_i=int(line.replace(" ","\t").split("\t")[1])
            index_i=int(line.split("\t")[1])
        #Fills row for Origin index_i
        else:
            index_j =line.replace(";",":").split(":")
            for k in range(0,len(index_j)-2,2):
                j = int(index_j[k].replace(" ",""))-1
                D[index_i-1,j]=float(index_j[k+1].replace(" ",""))
                if (index_i != j+1):
                    OD_pair.append((index_i,j+1))
            
    
    #form d matrix
    J = []
    I = []
    V = []
    for k in range(len(OD_pair)):
        i = OD_pair[k][0]-1
        j = OD_pair[k][1]-1
        I.append(i)
        I.append(j)
        J.append(k)
        J.append(k)
        V.append(D[i,j])
        V.append(-D[i,j])
        
       
    d = sparse.coo_matrix((V,(I,J)),shape =(L,len(OD_pair)))
    d = sparse.csc_matrix(d)
    
    return d, OD_pair
        
         