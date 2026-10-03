#!/usr/bin/env python3
"""A18 invariants: redshift factor N as a series in x = M/R_circ (circumferential radius, coordinate-free),
exponential package metric vs Schwarzschild; ISCO of the package metric (supplied toy, comparator GR)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import sympy as sp, mpmath as mp
x, U = sp.symbols("x U", positive=True)
# package: R_circ = r e^{U} with U = M/r  ->  x = U e^{-U};  N = e^{-U}
Ux = sp.series(-sp.LambertW(-x), x, 0, 5).removeO()
print("package: U(x) =", sp.expand(Ux))
print("package: N(x) =", sp.expand(sp.series(sp.exp(-Ux), x, 0, 5).removeO()))
print("GR     : N(x) =", sp.expand(sp.series(sp.sqrt(1 - 2 * x), x, 0, 5).removeO()))
# ISCO for H = N sqrt(1 + N^2 (p_r^2 + L^2/r^2)), N = e^{-1/r}: V(r)^2 = N^2 (1 + N^2 L^2/r^2); dV=d2V=0
mp.mp.dps = 30
def V2(r, L2): return mp.e ** (-2 / r) * (1 + mp.e ** (-2 / r) * L2 / r ** 2)
def eqs(r, L2):
    return [mp.diff(lambda rr: V2(rr, L2), r), mp.diff(lambda rr: V2(rr, L2), r, 2)]
r_isco, L2_isco = mp.findroot(eqs, (5.0, 15.0))
N = mp.e ** (-1 / r_isco)
S = mp.sqrt(1 + N ** 2 * L2_isco / r_isco ** 2)
Om = N ** 3 * mp.sqrt(L2_isco) / (r_isco ** 2 * S)
print("package ISCO: isotropic r = %.6f M, R_circ = %.6f M, M*Omega = %.6f, x=(M Omega)^(2/3) = %.6f, N = %.6f"
      % (r_isco, r_isco * mp.e ** (1 / r_isco), Om, Om ** (mp.mpf(2) / 3), N))
print("GR ISCO: R_circ = 6 M, M*Omega = %.6f, x = 1/6 = %.6f" % (6 ** -1.5, 1 / 6))
