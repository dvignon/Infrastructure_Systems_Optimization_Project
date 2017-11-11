def getParam(filename):
    """This function returns the parameters for the TAP problem
    
    INPUTS:
    filename: Name of the file from which the parameters for the problem are read.
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
    
    
    return param, A, M
    
    