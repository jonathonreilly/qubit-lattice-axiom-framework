#!/usr/bin/env python3
"""V1 validation: PT QMC at L=2 vs exact full-Gauss-sector thermal averages (data/exact_L2.json, produced by
exact_L2.py by brute-force enumeration + dense diagonalisation; independent of the sampler).
Rule (declared in WORKLOG before running): |QMC - exact| <= 3 sigma, sigma = max(combined binned SE,
seed scatter / sqrt(nseeds)).  usage: validate_L2.py TAG1 TAG2 ... > logs/validate_L2.log"""
import os, sys, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from analyze import estimate

V = sys.argv[1]
tags = sys.argv[2:]
ex = json.load(open(os.path.join(HERE, "..", "data", "exact_L2.json")))[V]["beta"]
per, comb = estimate(tags)
betas = per[0]["betas"]
npass = nfail = 0
for p in per:
    print(f"[INFO] {p['tag']}: n_meas={p['n']} round_trips={p['trips']} min_swap_acc={p['swap'].min():.3f}")
for i, b in enumerate(betas):
    key = str(float(b))
    if key not in ex:
        continue
    for q, eq in (("E", "E"), ("W2", "W2"), ("P0", "P0"), ("Nc", "Nc"), ("S1", "Sq")):
        mu, se = comb[q][0][i], comb[q][1][i]
        e = ex[key][eq]
        z = (mu - e) / se
        ok = abs(z) <= 3
        npass += ok
        nfail += (not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] V={V} beta={b} {q}: QMC {mu:.5f} +- {se:.5f}  exact {e:.5f}  z={z:+.2f}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
