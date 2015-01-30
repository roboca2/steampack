import parameters as param
from initialize import *
from construct_tree_step1 import *
from construct_tree_step2 import *
from construct_tree_step3 import *

def tree_constructor():
  step = 1
  
  param.U = param.Node[0:1]
  param.t = 1
  
  while step != -1:
    if step == 1:
     # print("Current step : " + str(step))
      step = construct_tree_step1()
     # print("Next step : " + str(step))
      
    elif step ==2:
     # print("Current step : " + str(step))
      step = construct_tree_step2()
     # print("Next step : " + str(step))
      initialize()

    elif step ==3:
      print("Current step : " + str(step))
      step = construct_tree_step3()
      print("Next step : " + str(step))
      initialize()

    else:
      print("error : step value in tree_contructor module")
      return -1

  return 1
