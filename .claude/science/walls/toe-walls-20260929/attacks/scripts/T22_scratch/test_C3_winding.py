"""Winding of arg det Q(kz) (= arg det V, since Q = V P with P>0), computed with a fine k_z grid and an aliasing guard."""
import numpy as np
from test_C_tails_flux import *

def build_Q_nz(M):
    """Q(kz) = sum_nz e^{i kz nz} Qnz, each Qnz built once (xy hops with Peierls)."""
    D = 2*L*L
    byz = {}
    for (nx,ny,nz), m in M.items():
        byz.setdefault(nz, {})[(nx,ny)] = m
    Qs = {}
    for nz, d in byz.items():
        Q = np.zeros((D, D), complex)
        for x in range(L):
            for y in range(L):
                r = x*L + y
                for (nx,ny), m in d.items():
                    if np.abs(m).max() < 1e-13: continue
                    rp = ((x+nx) % L)*L + ((y+ny) % L)
                    Q[2*r:2*r+2, 2*rp:2*rp+2] += m*np.exp(1j*B*ny*(x + nx/2))
        Qs[nz] = Q
    return Qs

def wind_det(Qs, nk):
    ks = 2*np.pi*np.arange(nk+1)/nk
    ang = np.empty(nk+1)
    for i, kz in enumerate(ks):
        Q = sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())
        sgn, ld = np.linalg.slogdet(Q)
        ang[i] = np.angle(sgn)
    inc = np.diff(np.unwrap(ang))
    un = np.unwrap(ang)
    return (un[-1]-un[0])/(2*np.pi), np.abs(np.diff(un)).max()

if __name__ == "__main__":
    coef = fourier_coeffs(); M = hop_matrices(coef)
    Qs = build_Q_nz(M)
    for nk in (200, 800, 3200):
        w, mx = wind_det(Qs, nk)
        print(f"tails tick: nk={nk:5d}  winding of arg det Q = {w:+.6f}   max phase step = {mx:.3f} (must be < pi)", flush=True)
