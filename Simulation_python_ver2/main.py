import parameters as param
from initialize import *
from tree_constructor import *


param.Node = [ [ ['index',1], [['S'],[8,12,24,32]], ['G',4], ['leaf',0], ['channel','0-level 4 channels'], ['child',0] ] ]
# initial value.

tree_constructor()
print("tree construct!")


