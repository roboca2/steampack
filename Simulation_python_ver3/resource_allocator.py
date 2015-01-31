import parameters as param
from calculator import *
import math
from allocate_step1 import *
#from allocate_step2 import *
#from allocate_step3 import *

def resource_allocator():
  step = 1
  f_calculator(1)
  param.R_tree = math.ceil(param.f[1]/param.Node[0][2][1])
  param.U = param.Node[0:1]
  
  
  while step != 1:
    if step == 1:
      print("Current step : " + str(step))
      #step = allocate_step1()
      print("Next step : " + str(step))
      
    elif step ==2:
      print("Current step : " + str(step))
     # step = construct_tree_step2()
      print("Next step : " + str(step))
    

    elif step ==3:
      print("Current step : " + str(step))
     # step = construct_tree_step3()
      print("Next step : " + str(step))
   
    else:
      print("error : step value in resource_allocator module")
      return -1
    
  return 1

