import parameters as param
import math

def allocate_step3():
  #print("V_n["+ str(param.n_Node[0][1]) + "] : " +str(param.V_n[param.n_Node[0][1]]))
  param.tree_allocate_log = param.init_list[:]
  channel_num =0.0
  k_machines = ""

  
  for types in param.V_n[param.n_Node[0][1]]:
    #print("current type : "+str(types))
    #print("N["+str(types)+"] : " + str(param.N[types]))
    #print("T["+str(types)+"] : " + str(param.T[types]))
    #print("G["+str(param.n_Node[0][1])+"] : " + str(param.n_Node[2][1]))
    
    channel_num = param.N[types] * param.n_Node[2][1]
    channel_num /= param.T[types]
    channel_num = math.ceil(channel_num)
    # calculate (N_k * G_n) / T_k -> and math.ceil()

    param.log += "Allocate "+str(channel_num)+" level-"+str(param.n_Node[2][1])+" subchannels to type "+str(types)+" machines\n\n"
    param.log += str(param.N[types])+" level-"+str(param.T[types])+" subchannels and allocate them to "+str(param.N[types])+" type "+str(types)+" machines\n\n\n"

    
    #print(str(param.N[types])+" level-"+str(param.T[types])+" subchannels and allocate them to "+str(param.N[types])+" type "+str(types)+" machines")
    
  param.tree_allocate_log.append(param.log)
 
