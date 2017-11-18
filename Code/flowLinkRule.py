def flowLink_Rule(model)
"""
    This function defines the link flow definitional constraints for the TAP.
    
    INPUTS: 
    model: Pyomo model (Concrete or Abstract)
    
    OUTPUTS: 
    Rule or expression for link flow constraints
    
"""
    return (f[a]-sum(f[a,k] for k in model.od )== 0.0 for a in model.links)