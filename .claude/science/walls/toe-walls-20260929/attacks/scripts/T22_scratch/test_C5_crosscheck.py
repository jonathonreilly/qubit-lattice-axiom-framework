import numpy as np, scipy.linalg as sl
from test_C3_winding import *
coef = fourier_coeffs(); M = hop_matrices(coef); Qs = build_Q_nz(M)
def argdet_scipy(Q):
    lu, piv = sl.lu_factor(Q)
    d = np.diag(lu)
    perm_sign = (-1)**np.sum(piv != np.arange(len(piv)))
    return np.angle(perm_sign*np.prod(d/np.abs(d)))
def argdet_eig(Q):
    ev = np.linalg.eigvals(Q)
    return np.angle(np.prod(ev/np.abs(ev)))
for kz in (0.0, 0.3, 1.7):
    Q = sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())
    print(f"kz={kz}: arg det via slogdet {np.angle(np.linalg.slogdet(Q)[0]):+.6f}  via LU {argdet_scipy(Q):+.6f}  via eigvals {argdet_eig(Q):+.6f}")
# winding using the scipy LU route, nk=1600
nk = 1600
ks = 2*np.pi*np.arange(nk+1)/nk
ang = np.array([argdet_scipy(sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())) for kz in ks])
un = np.unwrap(ang)
print("tails tick winding (scipy LU route):", (un[-1]-un[0])/(2*np.pi), " max step", np.abs(np.diff(un)).max())
# per-node bookkeeping: count of eigenphases of the polar factor within 0.35 of 0 and pi at kz values, for the record
def polar_phases(kz):
    Q = sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())
    u, s, vh = np.linalg.svd(Q); V = u@vh
    return np.angle(np.linalg.eigvals(V))  # eigenphase = -epsilon
for kz in (0.0, np.pi/2, np.pi):
    ph = polar_phases(kz)
    print(f"kz={kz:.3f}: states with |phase|<0.35: {(np.abs(ph)<0.35).sum()},  within 0.35 of pi: {(np.abs(np.abs(ph)-np.pi)<0.35).sum()}")
