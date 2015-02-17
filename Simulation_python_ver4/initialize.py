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

def init_all():
  param.U = param.init_list[:]
  param.C_n = param.init_list[:]

  param.L_n.clear()
  param.V_n.clear()
  # key   : types
  # value : (L_n)-list-int, (V_n)-list-int, 

  param.T_parent = param.init_list[:]
  param.T_parent1 = param.init_list[:]
  param.T_parent2 = param.init_list[:]

  param.t_parent = param.init_list[:]
  param.t_parent1 = param.init_list[:]
  param.t_parent2 = param.init_list[:]

  param.Pj_star = 0
  param.Qj_star = 0

  param.PQ.clear()
  # key   : prime_factor
  # value : its occurence
  param.t =0
  param.gcd =0

  param.f.clear()
  param.I.clear()
  param.N.clear()
  #T = {1:2, 2:4, 3:8
  param.T = {1:8, 2:12, 3:24, 4:32}
  # key   : types
  # value : (f)-float, (I)-int, (N)-int, (T)-int
  param.d_max = 4

  param.R_tree = 0
  param.R_raw = 0
  param.R_low = 0.0
  param.K = 4

  param.log = ""
  param.tree_allocate_log = param.init_list[:]
  param.raw_allocate_log = param.init_list[:]

#print(param.T_parent1)
#print(param.T_parent2)

#print(param.t_parent)
#print(param.t_parent1)
#print(param.t_parent2)

#print(param.PQ)
#print(param.Pj_star)
#print(param.Qj_star)
#print(param.gcd)
