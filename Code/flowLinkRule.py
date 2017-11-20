def flowLinkRule(model,a):
    """
        This function defines the link flow definitional constraints for the TAP.

        INPUTS: 
        model: Pyomo model (Concrete or Abstract)

        OUTPUTS: 
        Rule or expression for link flow constraints

    """
    return (model.f[a]-sum(model.fk[a,k] for k in model.od )== 0.0)