import parameters as param

def initialize():
 
  param.T_parent1 = param.init_list[:]
  param.T_parent2 = param.init_list[:]
  
  param.t_parent = param.init_list[:]
  param.t_parent1 = param.init_list[:]
  param.t_parent2 = param.init_list[:]

  for key, value in param.PQ.items():
    param.PQ[key] = 0
  
  param.Pj_star = param.init_int
  param.Qj_star = param.init_int
  param.gcd = param.init_int


#print(param.T_parent1)
#print(param.T_parent2)

#print(param.t_parent)
#print(param.t_parent1)
#print(param.t_parent2)

#print(param.PQ)
#print(param.Pj_star)
#print(param.Qj_star)
#print(param.gcd)
