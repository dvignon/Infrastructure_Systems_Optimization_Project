def costLinkRule(model,param,a):
    """
        This function defines the link flow definitional constraints for the TAP.

        INPUTS: 
        model: Pyomo model (Concrete or Abstract)

        OUTPUTS: 
        Rule or expression for link flow constraints

    """
    return (model.c[a]-(param['t_0'][a]*model.f[a]*(1+ param['beta'][a]/(param['alpha'][a]+1)*(model.f[a]/param['C'][a])**param['alpha'][a]))== 0.0)