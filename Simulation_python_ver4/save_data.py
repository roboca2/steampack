import parameters as param

def temp_data():
  param.tree_based_channels.append(param.R_tree)
  param.raw_channels.append(param.R_raw)
  param.lower_channels.append(param.R_low)
  
def save_data(types):
  param.tb_channels.append(param.tree_based_channels)
  param.r_channels.append(param.raw_channels)
  param.l_channels.append(param.lower_channels)
