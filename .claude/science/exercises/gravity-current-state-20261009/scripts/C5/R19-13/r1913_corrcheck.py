# check the infinite-chain correlators against a large ring (N = 2^18) for M = 0.3, 0.05, 1
import numpy as np
from r1913_lib import chain_corr
for M in (1.0, 0.3, 0.05, 0.01):
    Gx, Gp, e0 = chain_corr(M, 40)
    N = 2**20; k = 2*np.pi*np.arange(N)/N; w = np.sqrt(M*M + 4*np.sin(k/2)**2)
    fx = np.fft.fft(1/(2*w)).real/N; fp = np.fft.fft(w/2).real/N
    print('M=%.2f max|dGx|=%.2e max|dGp|=%.2e  |de0|=%.2e  Gx0=%.6f' % (M, np.abs(Gx-fx[:41]).max(), np.abs(Gp-fp[:41]).max(), abs(e0 - w.mean()/2), Gx[0]))
