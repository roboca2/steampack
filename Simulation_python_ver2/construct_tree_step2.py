import parameters as param
from calculator import *
def construct_tree_step2():
    print("\n< SETP 2 >")
    gcd_calculator(param.T_parent)
    # calculate GCD of T_parent
    print("T_parent : " + str(param.T_parent))
    print("GCD : " + str(param.gcd))
    
    param.t_parent = param.T_parent[0:len(param.T_parent)]
    for element in range(len(param.T_parent)):
        param.t_parent[element] = param.T_parent[element] / param.gcd
        param.t_parent[element] = int(param.t_parent[element])
    # calculate ~T_parent

    pq_calculator(param.t_parent)
    # calculate P(~T_parent) , Q(~T_parent)
    print("PQ : " + str(param.PQ))
    
    if param.Qj_star > 0:
        for period in param.t_parent:
            if period % param.Pj_star == 0:
                param.t_parent1.append(period)
            else:
                param.t_parent2.append(period)
    # calculate Pj_star & Qj_star
     
    param.T_parent1 = param.t_parent1[:]
    for element in range(len(param.T_parent1)):
        param.T_parent1[element] = param.t_parent1[element] * param.gcd
        
    param.T_parent2 = param.t_parent2[:]   
    for element in range(len(param.T_parent2)):
        param.T_parent2[element] = param.t_parent2[element] * param.gcd
    # divide T_parent -> T_parent(1) and T_parent(2) by Pj_star
    
    print("T_parent1 : " + str(param.T_parent1))
    print("T_parent2 : " + str(param.T_parent2))
    
    print("Pj_star : " + str(param.Pj_star))
    print("Qj_star : " + str(param.Qj_star))
    
    print("t_parent1 : " + str(param.t_parent1))
    print("t_parent2 : " + str(param.t_parent2))
    
    if len(param.T_parent1) > 1:
        print("case : |T_parent(1)| > 1")
        
        param.C_n.append(param.T_parent1)
        # T_parent(1) into C_n
        print("C_n : " + str(param.C_n))
        
        param.T_parent = param.T_parent2[:]
        # let T_parent <- T_parent(2)
         
        if param.T_parent == []:
        # T_parent == None
            print("\nfinish step2 : T_parent = None\n")
            return 3
        # go to step 3
        
        else:
        # T_parent != None
            print("new T_parent : " + str(param.T_parent))
            print("\nfinish step2 : T_parent != None\n")
            return 2
        # go to step 2
        
    elif len(param.T_parent1) == 1:
        print("case : |T_parent(1)| == 1")
        
        param.C_n.append(param.T_parent)
        
        # T_parent into C_n
        print("C_n : " + str(param.C_n))
        print("new T_parent : " + str(param.T_parent))
        print("\nfinish step2 : |T_parent(1)| == 1\n")
        return 3
        # go to step 3
