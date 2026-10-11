"""Operator-level check (V3 method) of the 2D free-p common zero (s2_zero_d2_M1.0.npy): mixed range-4 non-separable symbol.
Stencil for term (n,m): i sin(n kx)cos(m ky) = 1/4 [e^{i(n,m)k} + e^{i(n,-m)k} - e^{i(-n,m)k} - e^{i(-n,-m)k}]."""
import numpy as np, sys, time
from s2_operator_check import build
from v3_free_scalar_seagull_copy import comm_matrix, bulk_kernels, symbol, e0, hess
from s2_core import terms, quad_forms, kg_vac
a = np.load('s2_zero_d2_M1.0.npy'); tl = terms(2, 4)
sten = {}
for coef, (n, m) in zip(a, tl):
    if abs(coef) < 1e-14: continue
    for sx in (1, -1):
        for sy in ((1, -1) if m else (1,)):
            w = sx*coef*(0.25 if m else 0.5)
            sten[(sx*n, sy*m)] = sten.get((sx*n, sy*m), 0.0) + w
t0 = time.time()
for M in [1.0, 0.3]:
    Qf = quad_forms(2, 256, tl, lambda K: kg_vac(K, M))
    for ch in ['E', 'T2']:
        N = 40; L = 96
        H, K, idx, n = build(2, N, M, ch, sten)
        T1 = comm_matrix(K, H, n); T2 = comm_matrix(K, T1, n)
        kH, _ = bulk_kernels(H, idx, N, 2, n, 2); k1, e1 = bulk_kernels(T1, idx, N, 2, n, 6); k2, e2 = bulk_kernels(T2, idx, N, 2, n, 11)
        S0, _ = symbol(kH, L, 2); S1, _ = symbol(k1, L, 2); S2, _ = symbol(k2, L, 2)
        para = hess(lambda e: e0(S0 + e*S1)[0], 0.01); full = hess(lambda e: e0(S0 + e*S1 + 0.5*e*e*S2)[0], 0.01)
        print(f"M={M} {ch:2s}: transl.err T1 {e1:.1e} T2 {e2:.1e} | operator para {para:+.6e} full {full:+.6e} | Jacobian form {a@Qf[ch]@a:+.6e}  "
              f"[sin k flow: {Qf[ch][tl.index((1,0)),tl.index((1,0))]:+.4e}]  ({time.time()-t0:.0f}s)")
        sys.stdout.flush()
