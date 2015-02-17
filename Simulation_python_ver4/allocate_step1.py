import parameters as param

def allocate_step1():
  if param.U == []:
  # if U = null, finish the algorithm  
    #print("finish step1 : U == None, finish the algorithm")
    return -1

  param.n_Node = param.U[0]
  #print("n_Node :"+str(param.n_Node[3]))
  del param.U[0]
  # pick arbitrarily a node n and remove it from U

  if param.n_Node[3][1] == 'leaf node':
    #print("case : n_Node is leaf node -> go to step3")
    return 3
  # if n_Node is leaf node -> go to step 3
  else:
    #print("case : n_Node is non-leaf node -> go to step2")
    return 2
  # if n_Node is non-leaf node -> go to step 2
