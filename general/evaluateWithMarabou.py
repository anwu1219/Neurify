import sys
import warnings
import numpy as np

sys.path.append("/home/haozewu/Projects/TargetAttack/Marabou")

from maraboupy import Marabou

nnet_file_name = sys.argv[1]
try:
    inputs = [list(map(float,sys.argv[2:]))]
except:
    with open(sys.argv[2], 'r') as in_file:
        for line in in_file.readlines():
            inputs = [np.array(list(map(float,line.split(",")[:-1])))/255]


print("Num inputs:", len(inputs[0]))
net1 = Marabou.read_nnet(nnet_file_name)
y = net1.evaluate(inputs)
print(y)
