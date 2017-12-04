def objRule(model,param):
    """
    This function defines the obejctive function for the TAP
    
    INPUTS: 
    model: the Pyomo model instance (Concrete or Abstract)
    param: a dictionary of the parameters for the model
    d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
    
    OUTPUTS:
    Objective function expression (Concrete or Abstract)
    """

    return sum(param['t_0'][a]*model.f[a]*(1+ param['beta'][a]/(param['alpha'][a]+1)*(model.f[a]/param['C'][a])**param['alpha'][a]) for a in model.links)
    #return sum(model.c[a] for a in model.links)