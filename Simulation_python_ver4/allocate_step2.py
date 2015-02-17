import parameters as param
import math

def allocate_step2():
  channel_num = 0
  index = 0
  new_Node = []
  new_S = []
  child_list = []
  
  for child in param.n_Node[5][1]:
    # for each node i -> L_n, allocate
    index = param.n_Node[0][1]
    
    #print("f["+str(child)+"] : " + str(param.f[child]))
    #print("G["+str(index)+"] : " + str(param.Node[index-1][2][1]))
    #print("G["+str(child)+"] : " + str(param.Node[child-1][2][1]))
    
    channel_num = param.f[child] * param.Node[index-1][2][1]
    channel_num /= param.Node[child-1][2][1]
    channel_num = math.ceil(channel_num)
    # calculate (f_i * G_n) / G_i -> and math.ceil()
    
    param.Node[child-1][4][1] = str(channel_num) + ' level-' + str(param.Node[index-1][2][1]) + ' channels'  
    # modify information of node 
    param.U.append(param.Node[child-1])

  return 1
 

