from math import pi, exp
import matplotlib.pyplot as plt
import cmath
from scipy import signal
from numpy.fft import fft

N = 2048
x = lambda n : exp(-0.5*(n/7)**2)

def X(k) :
    sommeR = 0
    sommeI = 0
    for n in range(N) :
        sommeR += (x(n)*cmath.exp(-2j*pi*n*k/N)).real
        sommeI += (x(n)*cmath.exp(-2j*pi*n*k/N)).imag

    sommeR, sommeI = sommeR/N, sommeI/N
    return (sommeR, sommeI)



Lk = [k for k in range(N)]
Lx = [x(n) for n in Lk]
DFT = fft(Lx)

#Phase = [X(k)[1] for k in Lk]

#plt.plot(Lk, Lx, "b-")
#plt.plot(Lk, Phase, "r-")
#plt.show()
