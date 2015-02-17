import parameters as param

def print_log(types):
  line = 1
  print("< Tree based allocate algorithm >\n")
  print("R_tree : " + str(param.R_tree)+"\n")
  for tree_based_allocate in param.tree_allocate_log:
    print(tree_based_allocate+"\n")
    
  print("\n< Raw allocate >\n")
  print("R_raw : " + str(param.R_raw)+"\n")
  for raw_allocate in param.raw_allocate_log:
    print(raw_allocate+"\n")
    if line%2 == 0:
      print()
    line += 1

  print("< Lower Bound >\nR_low : " + str(param.R_low))
  print("\n")
