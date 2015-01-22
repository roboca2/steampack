def ant_calculator(term_num):  
  repeat = 0
  ant_seq = "1"
  new_ant = ""
  
  print(ant_seq)
  
  for repeat in range(term_num):
    seq_index = 0
    
    while seq_index < len(ant_seq):
      cur_term = ant_seq[seq_index]
      occurence = 1

      while seq_index+1 < len(ant_seq):
        if cur_term == ant_seq[seq_index+1]:
          occurence = occurence + 1
          seq_index = seq_index + 1
          
        else:
          break
        
      new_ant = new_ant + cur_term + str(occurence)     
      seq_index = seq_index + 1
      
    print(new_ant)
    ant_seq = new_ant
    # now, we need n term' sequence because it is need to calculate n+1 term

    if repeat != term_num-1:
      new_ant = ""
    # it is not last term, initialize new_ant, because reuse

    else:
      return new_ant
    # it is last term, return n term's sequence


term = input("Give me a terms of Ant Sequence that you want : ")
term_num = int(term)
ant_sequence = ""

ant_sequence = ant_calculator(term_num-1)
# it is return to ant_sequence, n term's sequecne

print("=============================================")
print("You want "+ term +" term!")
print("Show you "+ term +" term! ==>> " + ant_sequence)
