import os, signal
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"): os.environ[_v]="1"
signal.alarm(58)
import numpy as np
from scipy.linalg import expm
from walk2d import *
th = 0.3
print("U(K*) massless quasi-energies:", quasi(cycle(KSTAR, th=th)))
dq = 1e-4
sl = []
for ph in np.linspace(0, np.pi, 13):
    K = KSTAR + dq*np.array([np.cos(ph), np.sin(ph)])
    sl.append(np.abs(quasi(cycle(K, th=th)))/dq)
sl = np.array(sl)
print("cone slopes over 13 directions: min %.8f max %.8f ; sin(th) = %.8f" % (sl.min(), sl.max(), np.sin(th)))
for mu, N in ((0.05,1.0),(0.05,0.9),(0.2,0.8)):
    w = quasi(cycle(KSTAR, th=th, mu=mu, N=N))
    print("one-site mass mu=%.2f N=%.2f: rest quasi-energies" % (mu,N), np.round(w,12), " mu*N=%.12f" % (mu*N))
w = quasi(cycle(KSTAR, th=th, dx=0.025))
print("two-site x-mass dx=0.025: rest quasi-energies", np.round(w,12), "(expect +-2dx = 0.05)")
S = expm(-1j*(np.pi/4)*kr(I2,X)); b=0.137
P = expm(-1j*b*kr(X,Z)); R = S@P@S.conj().T
print("|S P S^dag - exp(i b X_x Y_y)| = %.2e" % np.abs(R - expm(1j*b*kr(X,Y))).max())
