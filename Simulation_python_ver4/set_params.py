import parameters as param
import random as ran
from type_checker import *

def set_params(type_list, cur_type,machine):
  param.Node = [ [ ['index',1], [['S'],[8,12,24,32]], ['G',4], ['leaf',0], ['channel','0-level 4 channels'], [['child'],[]] ] ]
  # initial value.
  d_i = 0
  
  for cur in range(1,len(type_list)+1):
    param.N[cur] = 0
    param.f[cur] = 0
    
  for cur in range(1,len(type_list)+1):
    new_d = param.init_list[:]
    
    if cur == cur_type:
      # current type setting
      #print("case : cur == cur_type")
      param.I[cur] = machine
     
      for i in range(param.I[cur]):
        d_i = 4
        #d_i = ran.random()+1
        d_i = ran.randint(1,param.d_max)
        param.N[cur] += d_i
    
      
    else:
      # otherwise setting initial value
      #print("case : cur != cur_type")
      param.I[cur] = 20
      param.N[cur] = param.I[cur]*param.init_d


