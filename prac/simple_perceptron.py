#perceptron neural network

import numpy as np
import matplotlib.pyplot as plt


w = np.matrix('5; 1; 12')
n = 1   
E = 0
epoch = 1000
epoch_E =[]
current_epoch = 0
i = 0

d = [1, 0, 1, 1]

x  = np.matrix([[-1, 0, 0], [-1, 0, 1], [-1, 1, 0], [-1, 1, 1]])


def step(input):
    if input > 0:
        return 1
    else:
        return 0
    


while current_epoch < epoch:
    
    
    while i < len(x):
        #forward propagation
        net = x[i]*w
        y = step(net)
        #update weights
        w = w + n*(d[i] - y)*x[i].getT()
        #calc error
        E = E + 0.5*(d[i] - y)**2
        print("epoch:", current_epoch, "sample:", i, "weights:", w.getT(), "error:", E)
        epoch_E.append(E)
        i += 1

    if E == 0:
        print("train complete")
        print(w)
        break
    i = 0
    E = 0
    
    
    current_epoch += 1

print(epoch_E)

plt.plot(range(len(epoch_E)), epoch_E, '-')
plt.xlabel("epoch")
plt.ylabel("Error")
plt.show()











