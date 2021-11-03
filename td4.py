import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
import scipy.signal.windows as win

N = 256
m = 0
f1 = 10
f2 = 10.5
A1 = 1
A2 = 1
T = 2
fe = 64

win_size = 1

#Lt = [t/fe for t in range(T*fe)]
Lt = np.arange(0, 4, 1/fe)
Lsin = [A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t) for t in Lt]
#LsinPadded = [A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t) for t in Lt] + [0 for i in range(m)]

Lf = [t*fe/(N) for t in range(N)]
Lf = np.arange(0, fe, fe/(N))
#LfPadded = [t*fe/(N+m) for t in range(N+m)]
Lfft = fft(Lsin*win.hann(N))
#LfftPadded = fft(LsinPadded)

#plt.subplot(211)
plt.plot(Lf, abs(Lfft/(N)))
plt.xlim(8, 12)



#N = 128

#Lf = [t*fe/(N) for t in range(N)]
#Lf = np.arange(0, fe, fe/(N))
#LfPadded = [t*fe/(N+m) for t in range(N+m)]
#Lfft = fft(Lsin)
#LfftPadded = fft(LsinPadded)


#plt.subplot(212)
#plt.plot(Lf, abs(Lfft/N))
#plt.xlim(8, 12)

plt.show()


