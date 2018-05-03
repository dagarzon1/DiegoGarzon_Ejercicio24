import numpy as np
import matplotlib.pyplot as plt

lamb=np.linspace(0.1,100,500)

def dist(x,l):
    return 1.0/l * np.exp(-x/l)

def dist_int(x,l):
    return -np.exp(-x/l)

def p_lamda(l):
    if(l<100):
        return 1/100
    if(l>100):
        return 0

def p_dat_lam(x,l):
    N=dist_int(20.0,l)-dist_int(1.0,l)
    return dist(x,l)/N

prob=np.zeros(500)
x=np.array([1.2,2.5,2.8,5.0])
for i in range(500):

    for j in range(4):
        prob[i]=prob[i]*p_dat_lam(x[j],lamb[i])
    prob[i]=prob[i]*lamb[i]

plt.plot(lamb,prob)
plt.show()
