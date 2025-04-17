#perceptron neural network

import numpy as np


w = np.matrix('-0.1; 0.2; -0.3')
n = 1
E = 0
epoch = 100
current_epoch = 0

d = [1, 0, 1, 1]

x  = np.array([[-1, 0, 0], [-1, 0, 1], [-1, 1, 0], [-1, 1, 1]])


matA = np.matrix('1; 2; 3')
matB = np.matrix('1 2 3')


def step(self , input):
    if input > 0:
        return 1
    else:
        return 0
    







# while current_epoch < epoch:
    
#     while i < len(x):
#         x1 = x[i]
#         i += 1
#     #forward propagation
#     net = w*x[current_epoch]
#     y = step(net)
#     #update weightss
#     w_new = w_init + n*(d[0] - y)*x1
#     #calc error
#     E = E + 0.5*(d[0] - y)**2

#     if E == 0:
#         break
#     current_epoch += 1
    

print(len(x))


