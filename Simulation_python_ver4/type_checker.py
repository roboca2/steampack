import parameters as param

def type_checker(n_Node):
  types = []
  for key, value in param.T.items():
    for period in n_Node[1][1]:
      if period == value:
        types.append(key)

  param.V_n[n_Node[0][1]] = types
    
  
def type_checker2(n_Node):
  types = []
  for key, value in param.T.items():
    for period in n_Node[1][1]:
      if period == value:
        types.append(key)

  return types
