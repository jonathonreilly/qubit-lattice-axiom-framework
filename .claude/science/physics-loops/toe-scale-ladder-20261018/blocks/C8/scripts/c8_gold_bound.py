#!/usr/bin/env python3
"""Review fix check: |rho g| = E |g|/|x| <= E <= pi for the M1 vertex at b_gold (any theta), sampled."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c8_core as cc
P = F = 0
rng = np.random.default_rng(3)
for th in (0.0, 0.05, 0.2):
    W = cc.Walk('gold', theta=th)
    k = np.vstack([rng.uniform(-np.pi, np.pi, (200000, 3)), np.array([np.pi, 0, 0]) + 1e-3*rng.normal(size=(20000, 3))])
    u, x = W.sym(k)
    m = np.max(cc.rho_u(u)*np.linalg.norm(x[:, 2:], axis=1))
    ok = m <= np.pi + 1e-12
    P += ok; F += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [numerical] gold theta={th}: max |rho g| over 220k samples (incl. near X) = {m:.6f} <= pi")
print(f"TOTAL: PASS={P} FAIL={F}")
