
# coding: utf-8

# # Problem formulation
# 
# **_Sets_**
# 
# $\mathscr{N}$ = Set of nodes <br>
# $\mathscr{A}$ = Set of links <br>
# $\mathscr{K}$ = Set of O-D pairs <br>
# 
# **_Parameters_**
# 
# $\beta_{ij}$ = Parameter of BPR function, $\forall (i,j) \in \mathscr{A}$ <br>
# $t^0_{ij}$ = Free-flow travel time, $\forall (i,j) \in \mathscr{A}$ <br>
# $\alpha_{ij}$ = Power in BPR function, $\forall (i,j) \in \mathscr{A}$ <br>
# $c_{ij}$ = Capacity of link, $\forall (i,j) \in \mathscr{A}$ <br>
# $d_{ik}$ = Demand for O-D pair $k$ at node $i$, $\forall i,k \in \mathscr{N} \times \mathscr{K}$ <br>
# $M$ = node incidence matrix $(M_{ia})$, $\forall i,a \in \mathscr{N} \times \mathscr{A}$ 
# 
# 
# **_Variables_**
# 
# $f_{ijk}$ = Link flow for O-D pair $k$, $\forall (i,j), k \in \mathscr{A} \times \mathscr{K}$  <br>
# $f_{ij}$ = Total link flow, $\forall (ij) \in \mathscr{A}$
# 
# From now on, we have: $\mathbf{a = (i,j)}$
# 
# **_Objective_**
# 
# 
# **UE**: $\min z = \sum_a t^0_a[f_a + \frac{\beta_a}{\alpha_a + 1} \cdot f_a \cdot (\frac{f_a}{c_a})^{\alpha_a}]$ <br>
# **SO**: $\min z = \sum_a t^0_a[1+\beta_a\cdot (\frac{f_a}{c_a})^{\alpha_a}] \cdot f_a$ 
# 
# **_Constraints_**
# 
# $f_a = \sum_k f_{ak}$, $\forall a \in \mathscr{A}$ -> Definitional constraints on link flow <br>
# $M\cdot(f_{ak}) - (d_{ik}) = 0$, $ \forall k \in \mathscr{K}$ -> Flow balance constraint <br> 
# $f_{ak} \geq 0$, $\forall k \in \mathscr{K}$ -> Non negativity constraints on link flow 
# 

# # Outline
# 
# # 1. Loading and manipulating the data
# For *Anaheim_net*:
# - We need a function that downloads the data and create a list for each of the parameters $\beta$, $t^0$, $\alpha$, $c$
# - We need a function that creates an array **_A_** of tuples for the links using the first two columns. 
# - We need a function that takes **_A_** and creates the (sparse) node incidence matrix **_M_**.
# 
# For *Anaheim_trips*:
# - We need a function that creates the (sparse) vector **_dk_** using the above file. 
# 
# # 2. An abstract Pyomo model
# Here, for this we need: 
# - A definition of each of the model sets and parameters
# - A definition of the model objective function
# - A definition of the model constraint functions 
# 
# # 3. A function for solving the model
# Here, we need a function that will solve take the model and solver options as input and return the solution
# 
# # 4. A function for results post-processing
# Here, we need a function that will output the result to the desired format (if we think the Pyomo ouput is not convenient) and <br>
# a function that will write the results to a specified file format
# 
# **NOTE**: 
# - Having functions here would make it easier for us to build a class later on which will be helpful when we move to the AV case where we will do a lot of evaluations
# - We should create each function in a separate .py file. Though we will probably use Jupyter for testing everything, having a .py file for each function helps make <br>
#     the code modular and eases notebook manipulation

# In[1]:

#Python libraries
from pyomo.environ import *
# Pyomo library for solving a problem
from pyomo.opt import SolverFactory
# Pyomo library for checking the solver statuse 
from pyomo.opt import SolverStatus, TerminationCondition
#panda is a useful data manipulation library
import numpy as np
import pandas as pd
from scipy import sparse
from sys import getsizeof


# In[2]:

#Homemade functions
from getParam import getParam
from getDemand import getDemand
from objRule import objRule
from flowBalRule import flowBalRule
from flowLinkRule import flowLinkRule
from costLinkRule import costLinkRule

filenameNet = "Data/Anaheim/Anaheim_net.tntp"

param,A,M,N,L = getParam(filenameNet)

filenameTrip = "Data/Anaheim/Anaheim_trips.tntp"

d, OD_pair= getDemand(filenameTrip,L)


# # Model definitions

# In[3]:

model=ConcreteModel()

model.links=RangeSet(0,len(A)-1,1) #Set of links
model.od=RangeSet(0,M.shape[1]-1,1) #Set of OD pairs
model.nodes=RangeSet(0,M.shape[0]-1,1) #Set of Nodes
model.f=Var(model.links,within=NonNegativeReals) #set of link flows
model.fk=Var(model.links,model.od,within=NonNegativeReals) #Set link-OD flows
model.c=Var(model.links,within=NonNegativeReals) #Set of link costs


# In[4]:

model.obj = Objective(expr=objRule(model))  #Objective function


# In[ ]:

model.flowBal =  ConstraintList()
for i in model.nodes:
    for k in model.od:
        #model.flowBal.add(flowBalRule(model,d,M,i,k))
        model.flowBal.add(sum(M[i,a]*model.fk[a,k] for a in model.links)-d[i,k]==0.0)


# In[6]:

model.flowLink =  ConstraintList()
model.costLink = ConstraintList()
for a in model.links:
    model.flowLink.add(flowLinkRule(model,a))
    model.costLink.add(costLinkRule(model,param,a))
#model.flowLink = Constraint(model.links, rule=flowLinkRule)


# In[ ]:

model.pprint()


# In[7]:

opt = SolverFactory("ipopt")

#opt.options["mipgap"] = 0.05
#store the results 
results = opt.solve(model)
print(results)


# In[9]:

model.display()

