import numpy as np
import matplotlib.pyplot as plt

lamb=np.linspace(0.1,150,500)

def dist(x,l):
    return 1.0/l * np.exp(-x/l)

def dist_int(x,l):
    return -np.exp(-x/l)

def p_lamda(l):
    if(l<100):
        return 1
    if(l>100):
        return 0

def p_dat_lam(x,l):
    N=dist_int(20.0,l)-dist_int(1.0,l)
    return dist(x,l)/N

prob=np.ones(500)
x=np.array([1.2,2.5,2.8,5.0])
for i in range(500):

    for j in range(4):
        prob[i]=prob[i]*p_dat_lam(x[j],lamb[i])
    prob[i]=prob[i]*p_lamda(lamb[i])

plt.plot(np.log10(lamb),prob)
plt.xlabel("$log_{10}{\lambda}$")
plt.ylabel("Probabilidad")
plt.show()
