#!/usr/bin/env python3
"""C8 report: reads logs/c8_results.json (written by c8_lattice.py), forms the error
certificates, the cubic decomposition of the TT stiffness, and the pre-registered checks."""
from __future__ import annotations

import json
import os
import sys
import functools

import numpy as np

print = functools.partial(print, flush=True)
HERE = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(HERE, '..', 'logs', 'c8_results.json')))
PASS = FAIL = 0
kG_sharp = None
try:
    for line in open(os.path.join(HERE, '..', 'logs', 'c8_continuum.log')):
        if line.startswith('RESULT kG_sharp'):
            kG_sharp = float(line.split()[-1])
except OSError:
    pass


def check(name, ok, kind='numerical'):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {name}")


def entries(walk, theta, coupling, chan, chi=np.pi/2, X=None):
    out = [v for v in res.values() if v['walk'] == walk and abs(v['theta'] - theta) < 1e-12 and v['coupling'] == coupling
           and v['chan'] == chan and abs(v['chi'] - chi) < 1e-3 and (X is None or v['X'] == X)]
    return out


def best(walk, theta, coupling, chan, chi=np.pi/2):
    """Value at the reference resolution (N=96, kap=1, inner 24/24/48) and an error certificate =
    max deviation over every other resolution computed (N = 64, 128; kap = 0.7; finer inner rule)."""
    es = entries(walk, theta, coupling, chan, chi)
    if not es:
        return None, None
    ref = [e for e in es if e['N'] == 96 and e['kap'] == 1.0 and e['inner'] == [24, 24, 48]]
    ref = ref[0] if ref else max(es, key=lambda e: e['N'])
    dev = max([abs(e['cG'] - ref['cG']) for e in es if e is not ref] + [0.0])
    return ref['cG'], dev


Q = {'z': np.array([0, 0, 1.0]), 'f': np.array([1, 1, 0.0])/np.sqrt(2), 'd': np.ones(3)/np.sqrt(3),
     'g': np.array([1, 2, 3.0])/np.sqrt(14)}


def cubic(walk, theta, coupling, chi=np.pi/2):
    """Polarisation-summed TT stiffness K(qhat) = A + B sum q^4 + C qx^2 qy^2 qz^2 (the general O_h-invariant
    even polynomial of degree <= 6 on S^2). Fit from z, (110), (111); return A, B, C, iso-average per
    polarisation, errors, and the (1,2,3) prediction test."""
    K, dK = {}, {}
    for d in 'zfdg':
        a, ea = best(walk, theta, coupling, d + 'A', chi); b, eb = best(walk, theta, coupling, d + 'B', chi)
        if a is None or b is None:
            continue
        K[d] = a + b; dK[d] = ea + eb
    if not all(d in K for d in 'zfd'):
        return None
    B = 2*(K['z'] - K['f']); A = K['z'] - B
    C = 27*(K['d'] - A - B/3)
    iso = 0.5*(A + 0.6*B + C/105)
    diso = 0.5*(dK['z']*(1 + 0.4*2) + dK['f']*2*0.4 + dK['d']*27/105)  # crude linear propagation bound
    pred = None
    if 'g' in K:
        q = Q['g']
        pred = (A + B*np.sum(q**4) + C*np.prod(q**2), K['g'], dK['g'])
    return dict(A=A, B=B, C=C, iso=iso, diso=diso + 0.5*(dK['z'] + dK['f'] + dK['d']), pred=pred, K=K)


print("=" * 100)
print("C8 lattice Sakharov coefficient c_G = a^2/(16 pi G_ind) per walk (one IR Dirac fermion), c = 1 units")
print("channels: z = q||(001), f = q||(110), d = q||(111), g = q||(123); A/B = the two TT polarisations")
print("=" * 100)
allpos = True
summary = {}
for walk in ('bstar', 'iso'):
    for cp in ('M1', 'M2', 'M3', 'M4'):
        row = []
        for ch in ('zA', 'zB', 'fA', 'fB', 'dA', 'dB', 'gA', 'gB'):
            v, e = best(walk, 0.0, cp, ch)
            if v is None:
                continue
            row.append(f"{ch} {v:.7e}(+-{e:.0e})")
            allpos &= v > 0
        print(f"{walk:6s} {cp}: " + "  ".join(row))
        cu = cubic(walk, 0.0, cp)
        if cu:
            summary[(walk, cp)] = cu
            print(f"        cubic fit: A={cu['A']:.6e} B={cu['B']:.6e} C={cu['C']:.6e};  isotropic average c_G = {cu['iso']:.7e} (+-{cu['diso']:.0e})")
            spread = (max(cu['K'][d] for d in 'zfd') - min(cu['K'][d] for d in 'zfd'))/(2*cu['iso'])
            print(f"        anisotropy: polarisation-summed K over z,f,d spans {100*spread:.1f}% of 2 c_G^iso")
            if cu['pred']:
                p, k, dk = cu['pred']
                check(f'{walk} {cp}: O_h cubic form fitted on z, (110), (111) predicts the generic (123) direction: '
                      f'pred {p:.8e} vs computed {k:.8e} (rel {abs(p-k)/k:.1e} < 2e-5)', abs(p - k) < 2e-5*k)
    for cp in ('M1',):
        a, ea = best(walk, 0.0, cp, 'dA'); b, eb = best(walk, 0.0, cp, 'dB')
        check(f'{walk} {cp}: (111) TT polarisations degenerate (C3 symmetry), rel {abs(a-b)/a:.1e} < 1e-9', abs(a - b) < 1e-9*a)
    for ch in ('zA', 'zB', 'dA'):
        v, e = best(walk, 0.0, 'M1', ch)
        n = len(entries(walk, 0.0, 'M1', ch))
        check(f'{walk} M1 {ch}: error certificate over {n} resolutions (N=64/96/128, kap=1/0.7, inner 24/36) rel {e/v:.1e} < 1e-5',
              e < 1e-5*v and n >= 5)
check('SIGN (pre-registered, decisive): c_G > 0 in every TT channel, every coupling M1-M4, at b* and b_iso', allpos)

print("-" * 100)
print("Lapse diagnostic (covariance predicts zero O(q^2) lapse stiffness; NOTE Lemma L proves it exactly)")
for walk in ('bstar', 'iso'):
    for cp in ('L1', 'L2'):
        for ch in ('zA', 'dA'):
            es = entries(walk, 0.0, cp, ch)
            if not es:
                continue
            e = es[0]
            print(f"  {walk} {cp} q||{ch[0]}: c_N = {e['cG']:.3e}   (q^0 part {-e['I0']:.3e})")
            check(f'{walk} {cp} q||{ch[0]}: lapse O(q^2) stiffness vanishes (|c_N| < 1e-10)', abs(e['cG']) < 1e-10)

print("-" * 100)
print("Mass dependence (M1, theta = m a) at b*, b_iso; IR stability of the massless value")
for walk in ('bstar', 'iso'):
    for chi in (0.0, np.pi/2):
        for ch in ('zA', 'zB', 'dA'):
            v0, _ = best(walk, 0.0, 'M1', ch)
            vs = [(th, best(walk, th, 'M1', ch, chi)[0]) for th in (0.2, 0.1, 0.05)]
            if any(v is None for _, v in vs):
                continue
            print(f"  {walk} chi={chi:.2f} {ch}: theta=0: {v0:.7e}; " + "; ".join(f"theta={th}: {v:.7e}" for th, v in vs))
            d = [abs(v - v0) for _, v in vs]
            check(f'{walk} chi={chi:.2f} {ch}: c_G(theta) -> c_G(0) monotonically as theta -> 0 (|dev| {d[0]:.1e}, {d[1]:.1e}, {d[2]:.1e})',
                  d[0] > d[1] > d[2] and d[2] < 2e-3*v0)

print("-" * 100)
print("b_gold (massless pi-modes at X; computed at theta > 0 with partition-of-unity balls at Gamma and the three X)")
for th in (0.4, 0.2, 0.1, 0.05):
    row = []
    for ch in ('zA', 'zB', 'fA', 'fB', 'dA', 'dB'):
        v, e = best('gold', th, 'M1', ch)
        if v is not None:
            row.append(f"{ch} {v:.6e}(+-{e:.0e})")
    if row:
        print(f"  theta={th}: " + "  ".join(row))
    cu = cubic('gold', th, 'M1')
    if cu:
        summary[('gold', th)] = cu
        print(f"     isotropic average c_G = {cu['iso']:.6e} (+-{cu['diso']:.0e})")

print("-" * 100)
print("Comparison with the continuum (pre-registered criterion 2)")
hk = 1/(96*np.pi**2)
print(f"  heat kernel (proper time, one Dirac): c_G = (Lambda a)^2/(96 pi^2): Lambda = 1/a -> {hk:.6e}; Lambda = pi/a -> {hk*np.pi**2:.6e}")
if kG_sharp:
    print(f"  same bubble in the continuum, sharp |k| < Lambda: c_G = {kG_sharp:.6e} (Lambda a)^2  [= 13/(840 pi^2) = {13/(840*np.pi**2):.6e}]")
for key, cu in summary.items():
    c = cu['iso']
    lam_eff = np.sqrt(c/hk)
    print(f"  {str(key):18s}: c_G^iso = {c:.6e}; Lambda_eff a (heat-kernel equivalent) = {lam_eff:.4f} = {lam_eff/np.pi:.4f} pi;"
          f"  a/l_P = sqrt(16 pi c_G N_f) = {np.sqrt(16*np.pi*c):.4f} sqrt(N_f)")
for walk in ('bstar', 'iso'):
    c = summary[(walk, 'M1')]['iso']
    r = np.sqrt(c/hk)/np.pi
    check(f'{walk} M1: Lambda_eff/(pi/a) = {r:.3f} lies in the pre-declared "same order" window [0.1, 10]', 0.1 <= r <= 10)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
