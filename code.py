from math import pi, exp
import matplotlib.pyplot as plt
import cmath
from scipy import signal


N = 2048
x = lambda n : exp(-0.5*n**2)

def X(k) :
    sommeR = 0
    sommeI = 0
    for n in range(N) :
        sommeR += (x(n)*cmath.exp(-2j*pi*n*k/N)).real
        sommeI += (x(n)*cmath.exp(-2j*pi*n*k/N)).imag

    sommeR, sommeI = sommeR/N, sommeI/N
    return (sommeR, sommeI)

Lk = [k for k in range(N)]
DFT = [X(k)[0] for k in Lk]
#Phase = [X(k)[1] for k in Lk]

#plt.plot(Lk, DFT, "b*")
#plt.plot(Lk, Phase, "r*")
#plt.show()
