import matplotlib.pyplot as plt 
import numpy as np 
import math 

eta = 1
K = 4
maxepoch = 1000
lamda = 1
Emax = 0.01

x = np.matrix('-1 -1 -1 -1; 0 0 1 1,3; 0 1 0 1')
d = np.matrix('0 1 1 0; 1 0 1 1')
E = np.zeros(maxepoch, 1)

v1 = np.zeros(3, K+1)
v2 = np.zeros(3, K+1)
w1 = np.zeros(3, K+1)
w2 = np.zeros(3, K+1)

v1  #some random initial value
v2 #some random initial value
w1 #some random initial value
w2 #some random initial value


print(d)
print(x)


# for i in maxepoch:
#     for 



#hidden layer

delta_h1 = (delta_o1*w1(2,k)+delta_o2*w2(2,k))*lamda*z1*(1-z1)
delta_h1 = (delta_o1*w1(3,k)+delta_o2*w2(3,k))*lamda*z1*(1-z2)

v1(:,k+1)=v1(:,k)+eta*delta_h1*x(:,k)
v2(:,k+1)=v2(:,k)+eta*delta_h2*x(:,k)

E(i)=E(i) +0.5*((d(1,k)-y1)^2 + ((d(2,k)-y2)^2))

end

if E(i) < Emax
    flag = i;
    break;

else 
    v1(:,1) = v1


#wtf is this?














































# x = np.linspace(-10, 10, 100) 
# z = 1/(1 + np.exp(-x)) 
  
# plt.plot(x, z) 
# plt.xlabel("x") 
# plt.ylabel("Sigmoid(X)") 
  
# plt.show() 



