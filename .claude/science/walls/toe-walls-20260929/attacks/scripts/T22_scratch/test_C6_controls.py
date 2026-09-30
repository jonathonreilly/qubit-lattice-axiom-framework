import numpy as np, scipy.linalg as sl
from test_C3_winding import *
from test_C5_crosscheck import argdet_scipy
I2_ = np.eye(2, dtype=complex)
# control 2: ordered tick polynomial, straight-line dressing, det winding at fine k_z grid
N = 8; k = 2*np.pi*np.arange(N)/N
kx, ky, kz_ = np.meshgrid(k, k, k, indexing='ij')
def Sj(q, j): return np.cos(q)[..., None, None]*I2_ - 1j*np.sin(q)[..., None, None]*sig[j]
U = np.einsum('...ab,...bc,...cd->...ad', Sj(kx,0), Sj(ky,1), Sj(kz_,2))
Mo = {}
for nx in range(-1,2):
    for ny in range(-1,2):
        for nz in range(-1,2):
            ph = np.exp(-1j*(nx*kx + ny*ky + nz*kz_))
            Mo[(nx,ny,nz)] = np.einsum('xyz,xyzab->ab', ph, U)/N**3
Qs = build_Q_nz(Mo)
nk = 800; ks = 2*np.pi*np.arange(nk+1)/nk
ang = np.array([argdet_scipy(sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())) for kz in ks])
un = np.unwrap(ang)
print("control 2 (ordered tick polynomial, straight-line dressing): winding", (un[-1]-un[0])/(2*np.pi), " max step", np.abs(np.diff(un)).max())
# control 1: exact product of dressed conditional shifts
Sx = shift_op(0); Sy = shift_op(1)
ang = np.array([argdet_scipy(Sx @ Sy @ Sz_kz(kz)) for kz in ks[::20]])
un = np.unwrap(ang)
print("control 1 (exact ordered tick): winding", (un[-1]-un[0])/(2*np.pi), " max step", np.abs(np.diff(un)).max())
