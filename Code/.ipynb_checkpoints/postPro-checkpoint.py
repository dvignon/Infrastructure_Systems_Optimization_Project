import csv
def postPro(results):
    """
    This function creates saves the results into a specified format and filename
    
    INPUTS: 
    results: The result output from the Pyomo model
    _format: Desired format for the file
    filename: Desired name for the file
    
    OUTPUTS:
    None

    """
    #
    # Collect the data
    #
    vars = set()
    data = {}
    f = {}
    for i in range(len(results.solution)):
        data[i] = {}
        for var in results.solution[i].variable:
            vars.add(var)
            data[i][var] = results.solution[i].variable[var]['Value']
            
        f[i] = results.solution[i].objective['obj']['Value']
    #
    # Write a CSV file, with one row per solution.
    # The first column is the function value, the remaining
    # columns are the values of nonzero variables.
    #
    rows = []
    vars = list(vars)
    vars.sort()
    rows.append(['obj']+vars)
    for i in range(len(results.solution)):
        row = [f[i]]
        for var in vars:
            row.append( data[i].get(var,None) )
            rows.append(row)
            
    print("Creating results file results.csv")
    writer = csv.writer(open('results.csv', 'wb'))
