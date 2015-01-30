import parameters as param
from fractions import gcd

# input    : set of integer
# output   : None
# function : calculate GCD of set of integer
def gcd_calculator(int_set):
  
  param.gcd = int_set[0]
  
  for integers in int_set: 
    param.gcd = gcd(param.gcd, integers)

  if(param.gcd < 1):
    print("error : gcd is less than 1")
    
  #print("integer set : " + str(int_set))
  #print("GCD of this set : " + str(param.gcd))
  return param.gcd


# input    : a integer
# output   : prime factor of input number
# function : calculate prime factor of input number
def prime_factor(number):
    prime = []
    prime_factor = 2
    
    while prime_factor * prime_factor <= number:
        while (number % prime_factor) == 0:
            prime.append(prime_factor)
            number /= prime_factor
            number = int(number)
        prime_factor += 1
    if number > 1:
       prime.append(number)
    return prime

  
# input    : set of integer
# output   : None
# function : calculate P, Q, Pj_star, Qj_star 
def pq_calculator(int_set):
    prime_factors = int_set[:]
    index = 0
    param.PQ[1] = 1
    
    
    for index in range(len(int_set)):
      prime_factors[index] = prime_factor(int_set[index])

    for prime_list in prime_factors:
      for prime in prime_list:
        param.PQ[prime] = 0
    # initialize PQ dic
    
    for prime_list in prime_factors:
      for prime in prime_list:   
        param.PQ[prime] += 1
    # counting operation.
    
    # key   : prime factor
    # value : occurence
    
    for key, value in param.PQ.items():
      if value > param.Qj_star:      
        param.Pj_star = key
        param.Qj_star = value
    # j_star  = argmax_j qj
    
    # Pj_star : prime factor, its occurence is highest
    # Qj_star : occurence, its value is the highest among all candidates

    
