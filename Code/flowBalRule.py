def flowBalRule(model, d, M)
"""
    This function defines the flow balance constraints for the TAP.
    
    INPUTS: 
    model: Pyomo model (Concrete or Abstract)
    d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
    M: Sparse node incidence matrix M
    
    OUTPUTS: 
    Rule or expression for flow balance constraints
    
    
"""
    # return (sum(M[i,a]*f[a,k] for a in model.links )-d[i,k]== 0.0 for i in model.nodes for k in model.od)
    L=M.shape(1)
    return (M.dot(f[:,k])-d[:,k]== np.zero(L) for k in model.od)