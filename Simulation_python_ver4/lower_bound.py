import parameters as param

def lower_bound():
  param.R_low = 0.0
  
  #print("N : " + str(param.N))
  #print("T : " + str(param.T))
  
  for types in range(1,param.K+1):
    #print("N : " + str(param.N[types]))
    #print("T : " + str(param.T[types]))
    param.R_low += param.N[types] / param.T[types]
  
