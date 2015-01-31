import parameters as param

def construct_tree_step1():
  if param.U == []:
  # if U = null, finish the algorithm  
    print("finish step1 : U == None, finish the algorithm")
    return -1
  
  param.n_Node = param.U[0]
  del param.U[0]
  # pick arbitrarily a node n and remove it from U
  
  param.T_parent = param.n_Node[1]
  param.T_parent = param.T_parent[1]
  # T_parent = S_n
  
  param.C_n = []
  # initialize C_n
  print("\n< STEP 1 >")
  print("n_Node : " + str(param.n_Node[0]))
  print("T_parent : " + str(param.T_parent))
  print("C_n : " + str(param.C_n) + "\n")
  print("finish step1 : U != None\n")
  return 2
  # go to step 2
