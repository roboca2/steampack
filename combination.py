from random import randint

def combination(input_list, k):
  input_list.sort()
  combination = ""
  combination_list = []
  
  element_list = []
  
  Result = ""
  
  combination_number = 0
  n_factorial = 1
  k_factorial = 1
  nk_factorial = 1
  repeat=0
  
  for number in range(len(input_list)):
    n_factorial = n_factorial*(number+1)
    if number < k:
       k_factorial = k_factorial*(number+1)
    if number < len(input_list) - k:
       nk_factorial = nk_factorial*(number+1)

  combination_number = n_factorial / (k_factorial * nk_factorial)
  
  
  max_num = max(input_list)
  min_num = min(input_list)
  
  while repeat < combination_number:
    choose_k = 0
    rand_pick = ""
    cur_combination = ""
    cur_combination_list = []
    new_combination = ""
    
    while choose_k < k:
      rand_pick = str(randint(int(min_num), int(max_num)))

      if cur_combination.find(rand_pick) == -1:
        cur_combination = cur_combination + rand_pick + "." 
        choose_k = choose_k + 1
        
    cur_combination_list = cur_combination.split(".")
    cur_combination_list.sort()
    del cur_combination_list[0]
    
    

    new_combination = " ".join(cur_combination_list)

    
    if combination.find(new_combination) == -1:
      combination = combination + new_combination + "//"
      repeat = repeat + 1 
    
    combination_list = combination.split("//")
    combination_list.sort()
    del combination_list[0]
    print("I'm not die! please wait....")
  print(combination_list)

input_str = input("Insert list (each numbers are separated by space) :") 
input_list = input_str.split(' ')

k_str = input("How many do you want to choose?(only integer) ") 
k = int(k_str)
  
combination(input_list, k)

