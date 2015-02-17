import parameters as param
from set_params import *
from tree_based_algorithm import *
from resource_allocator import *
from lower_bound import *
from print_log import *
from initialize import *
from save_data import *
from graph import *


for types in range(1,param.K+1):
  param.tree_based_channels = param.init_list[:]
  param.raw_channels = param.init_list[:]
  param.lower_channels = param.init_list[:]
  
  for machine in param.machines:
    print("current machine number : "+str(machine) + "\n")
    init_all()
    set_params([8,12,24,32],types,machine)
    # parameter setting
    
    param.I[types] = machine
    # setting machine number
    
    tree_based_algorithm()
    # calculate R_tree -> by tree based allocation algorithm

    lower_bound()
    # calculate R_low -> by lower bound algorithm

    raw_resource_allocator()
    # calculate R_raw -> by raw algorithm

    temp_data()
    # save data, data will be use when drawing graph
    
    print_log(types)
    # print results
    
  save_data(types)
  channel_graph(types)
delay_graph()


  
