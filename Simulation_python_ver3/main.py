import parameters as param
from resource_allocator import *
from tree_constructor import *
from set_params import *

import math 
types = [8,12,24,32]
type_num = 4

set_params(types,1)    
print("I : " + str(param.I))
print("N_" +str(1) +": " +str(param.N[1]))
  
param.Node = [ [ ['index',1], [['S'],[8,12,24,32]], ['G',4], ['leaf',0], ['channel','0-level 4 channels'], ['child',0] ] ]
# initial value.

done = tree_constructor()

if done != 1:
  print("\n\nC4ONSTRUCT ERROR!\n")



print("===========================\n f = " + str(param.f))
resource_allocator()
