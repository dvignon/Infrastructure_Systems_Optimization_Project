import pandas as pd
import numpy as np
from scipy import sparse
def getParam(filename):
    """This function returns the parameters for the TAP problem
    
    INPUTS:
    filename: (relative) Path of the file from which the parameters for the problem are read.
               This is a string
    
    OUTPUTS:
    param: Dictionary with the following
        c: list of link capacities, in the same order as A
        t_0: list of link free flow times
        alpha: list of link "Power" (exponent in BPR function)
        beta: list of link "B" (constant in BPR function) 
    A: list of tuples A[k]=(i,j) where i (j) is the head (tail) of link k
    M: Sparse node incidence matrix M
    """
    #Reading the parameters from the file
   
    param = pd.read_csv(filename, sep = '\t', comment = '<',usecols=['Capacity ', 'Free Flow Time ', 'B', 'Power'])
    
    #Renaming the columns of the file according to our conventions
    param.columns = ['C','t_0','beta','alpha']
    
    #Reading link informations for the file and converting to an array of tuples
    A = pd.read_csv(filename, sep = '\t', comment = '<',usecols=['Init node ', 'Term node '])
    A = list(zip(A['Init node '], A['Term node ']))
    
    #Getting number of nodes(N) and links(L)
    N = max(max(A,key=lambda x:x[0])[0],max(A,key=lambda x:x[1])[1])
    L = len(param)
    
    #Build sparse incidence matrix
    M= np.zeros((N,L))
    for a,b in zip(A,range(len(A))):
        M[a[0]-1,b] = 1;
        M[a[1]-1,b] = -1;

    M = sparse.csr_matrix(M)

    return param, A, M
    
    