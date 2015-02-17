import parameters as param
from calculator import *
from allocate_step1 import *
from allocate_step2 import *
from allocate_step3 import *

def resource_allocator():
  step = 1
  f_calculator(1)
  
  param.R_tree = math.ceil(param.f[1]/param.Node[0][2][1])
  # calculate - equation (4)
  
  #print("f : "+str(param.f))
  #print("f[1]: "+str(param.f[1]))
  #print("G[1]: "+str(param.Node[0][2][1]))
  #print("R_tree: "+str(param.R_tree))
  
  param.U = param.Node[0:1]
  
  
  while step != -1:
    if step == 1:
      #print("Current step : " + str(step))
      step = allocate_step1()
      #print("Next step : " + str(step))
      
    elif step ==2:
      #print("Current step : " + str(step))
      allocate_step2()
      step = 1
      #print("Next step : " + str(step))
    

    elif step ==3:
      #print("Current step : " + str(step))
      allocate_step3()
      step = 1
      #print("Next step : " + str(step))
   
    else:
      print("error : step value in resource_allocator module")
      return -1
    
  return 1


def raw_resource_allocator():
  R_raw = 0
  param.raw_allocate_log = param.init_list[:]
  
  for types in range(1,param.K+1):
    R_raw = math.ceil(param.N[types] / param.T[types])

    param.raw_allocate_log.append("Allocate "+str(R_raw)+" channels to type "+str(types)+" machines")
    param.raw_allocate_log.append(str(param.N[types])+" level-"+str(param.T[types])+" subchannels and allocate them to "+str(param.N[types])+" type "+str(types)+" machines")

    param.R_raw += R_raw



  
