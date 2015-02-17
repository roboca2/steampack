import parameters as param
from calculator import *
from type_checker import *

def construct_tree_step3():
  child_list = []
  #print("\n< SETP 3 >")
  
  if len(param.C_n) > 1:
    #print("case : |C_n| > 1")
    #print("< Node" + str(param.t) + " >\n"+ str(param.Node[param.t-1])+"\n")
    
    for element in param.C_n:
      param.t += 1
      G = gcd_calculator(element)
      new_Node = [ ['index',param.t], [['S'],element], ['G',G], ['leaf',0], ['channel','0 level-'+str(G)+' channels'], [['child'],[]] ]      
      type_checker(new_Node)
      child_list.append(param.t)
      param.Node.append(new_Node)
      param.U.append(new_Node)
      
      #print("< Node" + str(param.t) + " >\n"+ str(param.Node[param.t-1])+"\n")

    param.n_Node[5][1] = child_list
    return 1
  
  else:
    #print("case : |C_n| = 1")
    param.Node[param.n_Node[0][1]-1][3][1]='leaf node'
    #print("current node -> Node" + str(param.n_Node[0][1])+"("+str(param.Node[param.n_Node[0][1]-1][3][1])+")")
    
  #print("\nfinish step3\n")
  return 1