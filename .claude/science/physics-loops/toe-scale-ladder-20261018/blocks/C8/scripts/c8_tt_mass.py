#!/usr/bin/env python3
"""C8 diagnostic: the q -> 0 (q^0) part of the TT response for coupling M1, bubble + contact,
compared with the covariant expectation -rho_vac/2 (from E = rho_vac int sqrt(gamma), sqrt(gamma) =
1 - h:h/4 + O(h^3) for TT). A mismatch is an induced TT 'mass' term (diffeomorphism breaking at q^0).
Contact (M1, e = 1 - h/2 + 3h^2/8 at link midpoints): -(3/2) t lambda^2, t = (1/3) int rho g.g/|x|.
All quantities per unit volume per lambda^2, lattice units (tau = a = 1)."""
import os, sys, functools, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c8_core as cc
print = functools.partial(print, flush=True)
PASS = FAIL = 0
def check(name, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(f"{'PASS' if ok else 'FAIL'} [numerical] {name}")
res = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'c8_results.json')))
for walk in ('bstar', 'iso'):
    W = cc.Walk(walk)
    out = []
    for N in (96, 160):
        g1 = -np.pi + 2*np.pi*(np.arange(N) + 0.5)/N
        KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
        K = np.stack([KX.ravel(), KY.ravel(), KZ.ravel()], 1)
        rv = tt = 0.0
        for i in range(0, K.shape[0], 1 << 16):
            u, x = W.sym(K[i:i+1 << 16] if False else K[i:i+(1 << 16)])
            rv += np.sum(-2*cc.Efun(u)); nx = np.linalg.norm(x, axis=1)
            tt += np.sum(cc.rho_u(u)*np.sum(x[:, 2:]**2, 1)/nx)/3
        out.append((rv/N**3, tt/N**3))
    (rv, tt), (rv2, tt2) = out[1], out[0]
    for chan in ('zA', 'zB', 'dA'):
        e = [v for v in res.values() if v['walk'] == walk and v['theta'] == 0 and v['coupling'] == 'M1' and v['chan'] == chan and v['N'] == 96 and v['kap'] == 1.0][0]
        mTT = -e['I0'] - 1.5*tt
        print(f"{walk} {chan}: rho_vac = {rv:.8f} (N=96: {rv2:.8f}); t = {tt:.8f}; bubble q^0 = {-e['I0']:.8f}; "
              f"total q^0 TT coefficient = {mTT:.6f}; covariant expectation -rho_vac/2 = {-rv/2:.6f}; mismatch = {mTT + rv/2:.6f}")
    check(f'{walk}: vacuum energy density and contact integral converged (N=96 vs 160, rel < 1e-4)', abs(rv - rv2) < 1e-4*abs(rv) and abs(tt - tt2) < 1e-4*abs(tt))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
