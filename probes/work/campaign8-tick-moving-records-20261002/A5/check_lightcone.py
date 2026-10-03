#!/usr/bin/env python3
"""Lane T check B: strict light cone of the ticked step vs tails of continuous change.

(a) Dirac step on a ring: amplitude is exactly 0 outside |x - x0| <= t (and on the wrong checkerboard parity).
(b) Continuous change with a time-independent nearest-neighbour generator H = (i/2)(T - T^dag) (H(k) = sin k, max speed 1):
    <d|exp(-iHt)|0> = J_d(t) (Bessel), nonzero beyond d = t. Dense expm vs scipy.special.jv.
(c) Massive continuous lattice Dirac H(k) = sin k sz + m sx: tail beyond the front (FFT, fine grid).
(d) Effective generator of the step, H_eff = i log U (principal branch): its real-space kernel has
    exponential tails for m > 0 (rate arccosh(1/cos m)) and 1/r tails for m = 0 (no local generator).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.linalg import expm
from scipy.special import jv

print("== (a) Dirac step, ring N=1001, start |x0,R>, t=200")
N, t = 1001, 200
for m in (0.0, 0.3, 1.0):
    R = np.zeros(N, complex)
    L = np.zeros(N, complex)
    x0 = N // 2
    R[x0] = 1.0
    c, s = np.cos(m), np.sin(m)
    for _ in range(t):
        R = np.roll(R, 1)
        L = np.roll(L, -1)
        R, L = c * R - 1j * s * L, -1j * s * R + c * L
    x = np.arange(N) - x0
    amp = np.sqrt(np.abs(R) ** 2 + np.abs(L) ** 2)
    outside = np.abs(x) > t
    wrongpar = (np.abs(x) <= t) & ((x - t) % 2 != 0)
    print("   m=%.1f  max|amp| outside cone = %r   max|amp| on wrong parity = %r   |amp| at x=+t: %.3e (cos^(t-1) m * ... )   norm=%.15f" % (
        m, float(amp[outside].max()), float(amp[wrongpar].max()), amp[x == t][0], np.sum(amp ** 2)))

print("\n== (b) continuous change, H = (i/2)(T - T^dag) on an open chain of 801 sites, t=100")
Nc, tc = 801, 100.0
H = np.zeros((Nc, Nc), complex)
for j in range(Nc - 1):
    # T|j> = |j+1>:  H = (i/2)(T - T^dag)
    H[j + 1, j] += 0.5j
    H[j, j + 1] += -0.5j
psi0 = np.zeros(Nc, complex)
j0 = Nc // 2
psi0[j0] = 1.0
psit = expm(-1j * tc * H) @ psi0
for d in (90, 100, 105, 110, 120, 130, 150):
    a_num = abs(psit[j0 + d])
    a_bes = abs(jv(d, tc))
    print("   d=%3d  |amp| expm=%.3e   |J_d(t)|=%.3e" % (d, a_num, a_bes))

print("\n== (c) massive continuous lattice Dirac, H(k)=sin k sz + m sx, m=0.3, t=100, FFT grid 2^15")
Nk = 2 ** 15
k = 2 * np.pi * np.fft.fftfreq(Nk)
m = 0.3
E = np.sqrt(np.sin(k) ** 2 + m ** 2)
# exp(-iHt) = cos(Et) - i sin(Et) (H/E)
ct, st = np.cos(E * tc), np.sin(E * tc) / E
# start in R at x=0: column (1,0)
gR = ct - 1j * st * np.sin(k)
gL = -1j * st * m
# position amplitude: psi(x) = (1/Nk) sum_k e^{ikx} g(k)
pR = np.fft.ifft(gR)
pL = np.fft.ifft(gL)
amp = np.sqrt(np.abs(pR) ** 2 + np.abs(pL) ** 2)
for d in (100, 105, 110, 120, 130):
    print("   d=%3d  |amp|=%.3e" % (d, max(amp[d], amp[-d])))

print("\n== (d) effective generator H_eff = i log U of the step: real-space kernel |h(r)| (Frobenius)")
Nk = 2 ** 14
k = 2 * np.pi * np.fft.fftfreq(Nk)
for m in (0.0, 0.3, 0.8):
    c, s = np.cos(m), np.sin(m)
    U = np.zeros((Nk, 2, 2), complex)
    U[:, 0, 0] = c * np.exp(-1j * k)
    U[:, 0, 1] = -1j * s * np.exp(1j * k)
    U[:, 1, 0] = -1j * s * np.exp(-1j * k)
    U[:, 1, 1] = c * np.exp(1j * k)
    lam, V = np.linalg.eig(U)
    w = -np.angle(lam)  # principal branch in (-pi, pi]
    Vi = np.linalg.inv(V)
    Heff = np.einsum('kij,kj,kjl->kil', V, w, Vi)
    h = np.fft.ifft(Heff, axis=0)
    hn = np.sqrt(np.sum(np.abs(h) ** 2, axis=(1, 2)))
    rs = (5, 10, 20, 40, 80)
    vals = [hn[r] for r in rs]
    msg = "   m=%.1f  " % m + "  ".join("|h(%d)|=%.2e" % (r, v) for r, v in zip(rs, vals))
    if m > 0:
        kap = np.arccosh(1 / np.cos(m))
        rate = -np.log(hn[40] / hn[20]) / 20
        msg += "\n          fitted decay rate (r=20..40) = %.4f  vs arccosh(1/cos m) = %.4f" % (rate, kap)
    else:
        msg += "\n          r*|h(r)| at r=5,10,20,40,80: " + ", ".join("%.4f" % (r * v) for r, v in zip(rs, vals)) + "  (sqrt2=1.4142 -> 1/r tails)"
    print(msg)
