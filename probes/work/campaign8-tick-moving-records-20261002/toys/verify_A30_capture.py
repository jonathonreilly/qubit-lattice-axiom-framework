#!/usr/bin/env python3
"""Coordinator's independent check of A30 Q1 (own code).
(a) rate law with surface field eps: A = 2tG sin k/(t^2+eps^2+G^2/4+2t eps cos k+tG sin k), wave packets;
(b) per-tick sure capture (kappa = 1) at k = pi/2: A = x/(1+x/4)^2, x = 2 t tau;
(c) best capture over (k, G) at |eps| = 2t is exactly 2/3 (k = 2pi/3, G = 2 sqrt3 t); |eps| = 1.5t gives 0.80;
(d) the speed-only law A = 2u/(1+u) at G = 2t for a staggered-mass chain (surface on-site -m), upper band."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import expm
t = 1.0
L = 1600; x = np.arange(L)
def A_formula(k, G, eps):
    return 2*t*G*np.sin(k)/(t*t + eps*eps + G*G/4 + 2*t*eps*np.cos(k) + t*G*np.sin(k))
def packet(k, sig=60.0, x0=None):
    x0 = L//2 - 250 if x0 is None else x0
    psi = np.exp(-(x - x0)**2/(4*sig**2) + 1j*k*x); return psi/np.linalg.norm(psi), x0
def H_surface(V, onsite=None):
    H = diags([-t*np.ones(L-1), -t*np.ones(L-1)], [-1, 1], dtype=complex).tolil()
    if onsite is not None:
        for j in range(L): H[j, j] = onsite[j]
    H[L-1, L-1] += V
    return H.tocsc()
print("(a) rate law with surface field eps (surface = site L-1, wall beyond):")
for k, G, eps in ((np.pi/2, 2.0, 0.0), (1.0, 1.3, 0.7), (2.0, 3.0, -1.2), (0.6, 2.0, 2.0), (2*np.pi/3, 2*np.sqrt(3), 2.0)):
    psi, x0 = packet(k)
    Tm = 2*(L-1-x0)/(2*t*np.sin(k))
    out = expm_multiply(-1j*H_surface(eps - 0.5j*G)*Tm, psi)
    print("   k=%.3f G=%.3f eps=%+.2f  captured %.5f  formula %.5f" % (k, G, eps, 1-np.linalg.norm(out)**2, A_formula(k, G, eps)))
print("(b) per-tick sure capture at k = pi/2 (project out the surface site after each tick):")
Lb = 900; xb = np.arange(Lb)
Hb = diags([-t*np.ones(Lb-1), -t*np.ones(Lb-1)], [-1, 1], dtype=complex).tocsc()
for tau in (0.5, 0.25, 0.1, 0.05):
    psi = np.exp(-(xb - 300)**2/(4*40.0**2) + 1j*(np.pi/2)*xb); psi /= np.linalg.norm(psi)
    nt = int(round((2*(Lb-1-300)/(2*t))/tau)) + 400
    cap = 0.0
    for n in range(nt):
        psi = expm_multiply(-1j*Hb*tau, psi)
        cap += abs(psi[-1])**2; psi[-1] = 0.0
    xx = 2*t*tau
    print("   tau=%.2f  captured %.4f  x/(1+x/4)^2 = %.4f" % (tau, cap, xx/(1+xx/4)**2))
print("(c) best capture over k,G for fixed eps (formula scan):")
ks = np.linspace(0.001, np.pi-0.001, 4001); Gs = np.linspace(0.01, 12, 2400)
for eps in (1.5, 2.0):
    K, G = np.meshgrid(ks, Gs); Aa = A_formula(K, G, eps); i = np.unravel_index(np.argmax(Aa), Aa.shape)
    print("   eps=%.1f  max A = %.5f at k=%.4f (2pi/3=%.4f), G=%.4f (2sqrt3=%.4f)" % (eps, Aa[i], K[i], 2*np.pi/3, G[i], 2*np.sqrt(3)))
print("(d) staggered-mass chain, G = 2t, upper band: A vs 2u/(1+u), u = |group velocity|/(2t)")
for m in (0.2, 0.6):
    onsite = m*(-1.0)**x
    # surface site L-1 has on-site m(-1)^(L-1); make L even so surface on-site = -m
    assert (-1.0)**(L-1) == -1.0
    H = H_surface(-0.5j*2.0, onsite)
    for k in (np.pi - 0.5, np.pi - 1.0):   # dE/dk > 0 in the upper band: packet moves toward the surface
        # upper-band Bloch packet: two-site cell, E = +sqrt(m^2 + 4t^2 cos^2 k)
        E = np.sqrt(m*m + 4*t*t*np.cos(k)**2)
        # eigenvector of the 2x2 Bloch block for sites (even, odd) with phase convention psi_j ~ e^{ikj} u_{j mod 2}
        hk = np.array([[m, -t*(1+np.exp(-2j*k))], [-t*(1+np.exp(2j*k)), -m]])  # cell momentum 2k, intracell phase absorbed
        w, V = np.linalg.eigh(hk); u = V[:, np.argmax(w)]
        x0 = L//2 - 250
        env = np.exp(-(x - x0)**2/(4*80.0**2))
        cell = x//2
        psi = env*np.exp(1j*2*k*cell)*np.where(x % 2 == 0, u[0], u[1]); psi /= np.linalg.norm(psi)
        vg = 2*t*t*abs(np.sin(2*k))/E   # dE/dk for E^2 = m^2 + 4t^2cos^2 k, per site
        Tm = (L-1-x0 + 6*80.0)/vg*1.3
        out = expm_multiply(-1j*H*Tm, psi)
        uu = vg/(2*t)
        print("   m=%.1f k=%.1f  captured %.4f  2u/(1+u) = %.4f (u=%.4f)" % (m, k, 1-np.linalg.norm(out)**2, 2*uu/(1+uu), uu))
