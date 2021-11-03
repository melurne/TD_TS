from math import pi, exp
import matplotlib.pyplot as plt
import cmath
from scipy import signal
from numpy.fft import fft
import numpy as np

N = 1024
f1, f2 = 50, 200
A1, A2 = 1, 5
x = lambda n,f : np.sin(2*pi*(n/N)*f)


Lk = [k for k in range(N+1)]
Lx = [A1*x(n, f1) + A2*x(n, f2) for n in Lk]
DFT = fft(Lx)
DFT = [np.abs(a/N) for a in DFT]
#Phase = [X(k)[1] for k in Lk]

plt.plot(Lk, DFT, "b-")
#plt.plot(Lk, Lx, "r-")
plt.show()
