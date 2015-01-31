import parameters as param
import random as ran
from type_checker import *

def set_params(type_list, cur_type):
  
  d_i = 0
  
  for cur in range(len(type_list)):
    param.N[cur] = 0
    param.f[cur] = 0
    
  for cur in range(len(type_list)):
    new_d = param.init_list[:]
    
    if cur+1 == cur_type:
      # current type setting
      print("case : cur == cur_type")
      param.I[cur+1] = param.machines
     
      for i in range(param.I[cur+1]):
        d_i = 4
        #d_i = ran.randint(1,param.d_max)
        param.N[cur+1] += d_i
    
      
    else:
      # otherwise setting initial value
      print("case : cur != cur_type")
      param.I[cur+1] = 20
      param.N[cur+1] = param.I[cur+1]


