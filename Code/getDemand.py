def getDemand(filename): 
    """This function returns the demand for each O-D pair in the TAP problem
    
    INPUTS:
    filename: String which the represents the name of the file from which the demand is read
    
    OUTPUTS:
    d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
    """
    return d