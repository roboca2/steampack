import parameters as param
import matplotlib.pyplot as plt
import matplotlib.legend as legend


def channel_graph(types):
  
  tree,=plt.plot(param.machines, param.tb_channels[types-1], 'ro-')
  raw,=plt.plot(param.machines, param.r_channels[types-1], 'g^-')
  lower,=plt.plot(param.machines, param.l_channels[types-1], 'bs-')

  plt.legend([tree, raw, lower],['Tree based allocate algorithm', 'Raw algorithm', 'Lower bound'], loc=1)

  plt.xlabel('number of machines')
  plt.ylabel('number of channels')
  plt.axis([7, 35, 3, 20])
  plt.grid(True)
  plt.show()

def delay_graph():
  y_delay = []
  avg_delay = []
  avg_list = []
  for types, period in param.T.items():
    #print("T["+str(types)+"] : "+str(period))
    avg_delay.append((period+1) / 2)
    #print("avg_delay"+str(avg_delay))

  for repeat in range(len(param.machines)):

    for push in range(len(param.machines)):
      avg_list.append(avg_delay[repeat])
      
    y_delay.append(avg_list)
    avg_list = param.init_list[:]
    
  print(y_delay)

  tree1,=plt.plot(param.machines, y_delay[0], 'rs-')
  raw1,=plt.plot(param.machines, y_delay[0], 'rd-')

  tree2,=plt.plot(param.machines, y_delay[1], 'gs-')
  raw2,=plt.plot(param.machines, y_delay[1], 'gd-')
  
  tree3,=plt.plot(param.machines, y_delay[2], 'bs-')
  raw3,=plt.plot(param.machines, y_delay[2], 'bd-')
  
  tree4,=plt.plot(param.machines, y_delay[3], 'cs-')
  raw4,=plt.plot(param.machines, y_delay[3], 'cd-')
  
  plt.xlabel('number of machines')
  plt.ylabel('average delay [TU]')
  plt.axis([7, 33, 0, 22])
  plt.grid(True)
  plt.show()
