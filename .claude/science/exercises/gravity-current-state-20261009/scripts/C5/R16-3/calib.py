# calibration against R14-3 W08 / G(1.4) numbers and R9-9 NN control
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *
T0=time.time()
# NN scalar: sigma = 2 sin(k/2): g = 4 sin^2(k/2) = 2-2cos k, f = sin k
n = 1 << 14; kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
g = 2-2*np.cos(kk); f = np.sin(kk)
print('NN m=1', xi_all(g, f, 1.0))   # R9-9: M,T2g -1.903e-3, M,Eg -8.302e-4, U,T2g -2.289e-4, U,Eg -6.883e-5
print('runtime %.1f'%(time.time()-T0))
