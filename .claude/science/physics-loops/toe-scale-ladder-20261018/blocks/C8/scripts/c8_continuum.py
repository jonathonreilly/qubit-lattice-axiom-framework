#!/usr/bin/env python3
"""C8 continuum reference with the same observable and the same (minimal) coupling:
massless continuum Dirac H = alpha.p, static TT bubble, sharp cutoff |k_mid| < Lambda on the
midpoint loop momentum. By homogeneity F2(r n) = F2(n)/r, so
  c_G^sharp = -(Lambda^2 / (4 (2pi)^3)) int dOmega F2(n)    (c = 1, one Dirac fermion).
Also compares with the proper-time heat-kernel value Lambda^2/(96 pi^2) (c8_exact E3).
This is a scheme comparison only: a sharp spatial cutoff is not a covariant regulator.
"""
from __future__ import annotations

import os
import sys
import functools

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c8_core as cc

print = functools.partial(print, flush=True)
PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [numerical] {name}")


class ContDirac:
    """Mock 'walk' whose generator is exactly H = alpha.k for |k| < pi:
    u = 1 - cos|k| so that E = arccos(1-u) = |k|; x = (0, 0, khat sin|k|); rho g = k."""
    s = 1.0

    def sym(self, k, deriv=False):
        r = np.linalg.norm(k, axis=1)
        u = 2*np.sin(r/2)**2
        x = np.zeros((k.shape[0], 5))
        x[:, 2:] = k*(np.sin(r)/r)[:, None]
        return u, x


C = ContDirac()
xm, wm = np.polynomial.legendre.leggauss(40)
nph = 80
ph = 2*np.pi*np.arange(nph)/nph
MU, PH = np.meshgrid(xm, ph, indexing='ij')
W = (wm[:, None]*np.full(nph, 2*np.pi/nph)[None, :]).ravel()
st = np.sqrt(1 - MU**2)
nhat = np.stack([(st*np.cos(PH)).ravel(), (st*np.sin(PH)).ravel(), MU.ravel()], 1)
vals = {}
for pol in ('A', 'B'):
    qh, eps = cc.tt_eps('z', pol)
    out = []
    for r in (0.2, 0.1):
        _, F2, _ = cc.F2val(C, 'M1', eps, qh, r*nhat)
        out.append(np.sum(W*F2*r))
    vals[pol] = out
    print(f"  pol {pol}: int dOmega F2(n) = {out[0]:.12f} (r=0.2), {out[1]:.12f} (r=0.1)")
    check(f'continuum pol {pol}: homogeneity F2(r n) = F2(n)/r (r = 0.2 vs 0.1, rel 1e-8)', abs(out[0] - out[1]) < 1e-8*abs(out[0]))
check('continuum: both TT polarisations give the same angular integral (isotropy, rel 1e-8)',
      abs(vals['A'][1] - vals['B'][1]) < 1e-8*abs(vals['A'][1]))
J = vals['A'][1]
kG = -J/(4*(2*np.pi)**3)          # c_G^sharp = kG * Lambda^2
hk = 1/(96*np.pi**2)
print(f"  sharp spatial cutoff: c_G = {kG:.10f} Lambda^2 = Lambda^2/({1/kG:.6f})")
print(f"  proper-time heat kernel: c_G = {hk:.10f} Lambda^2 = Lambda^2/(96 pi^2) = Lambda^2/{96*np.pi**2:.6f}")
print(f"  ratio sharp/heat-kernel = {kG/hk:.10f};  (sharp)*(pi^2) = {kG*np.pi**2:.10f}")
check('continuum sharp-cutoff c_G > 0 (same sign as the heat kernel)', kG > 0)
print(f"RESULT kG_sharp {kG:.15e}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
