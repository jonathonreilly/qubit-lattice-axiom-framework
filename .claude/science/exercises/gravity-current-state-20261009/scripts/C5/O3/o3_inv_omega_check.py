import numpy as np
from numpy.polynomial.legendre import leggauss
for n in [32, 64, 96, 128]:
    x, w = leggauss(n); k = 0.5*np.pi*(x+1); wk = 0.5*w; C = np.cos(k)
    tot = 0.0
    for a in range(n):
        S = 6-2*(C[a]+C[:,None]+C[None,:])
        tot += wk[a]*np.sum(wk[:,None]*wk[None,:]/np.sqrt(S))
    print("n=%3d  <1/omega_0> = %.6f" % (n, tot))
