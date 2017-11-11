def objRule(model,param,d):
    """
    This function defines the obejctive function for the TAP
    
    INPUTS: 
    model: the Pyomo model instance (Concrete or Abstract)
    param: a dictionary of the parameters for the model
    d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
    
    OUTPUTS:
    Objective function expression (Concrete or Abstract)
    """