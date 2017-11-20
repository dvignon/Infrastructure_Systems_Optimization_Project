def flowBalRule(model,d,M,i,k):
    """
        This function defines the flow balance constraints for the TAP.

        INPUTS: 
        model: Pyomo model (Concrete or Abstract)
        d: Numpy array where d[i,j] is the demand between node i and node j. d[i,i] = 0
        M: Sparse node incidence matrix M

        OUTPUTS: 
        Rule or expression for flow balance constraints


    """
    return (sum(M[i,a]*model.fk[a,k] for a in model.links )-d[i,k]==0.0)
    #return (sum(M[i,a]*f[a,k] for a in model.links )-d[i,k]==0.0 for i in model.nodes for k in model.od)
    #return (M[i,:].dot(model.f[:,k])-d[i,k]==0.0)
