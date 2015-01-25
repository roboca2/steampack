import itertools
def combination(input_list, k): 
  for print_combinations in itertools.combinations(input_list,k):
    print(print_combinations)

input_str = input("Insert list (each numbers are separated by space) :") 
input_list = input_str.split(' ')

k_str = input("How many do you want to choose?(only integer) ") 
k = int(k_str)
  
combination(input_list, k)
