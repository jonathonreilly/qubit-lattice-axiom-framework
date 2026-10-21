#!/usr/bin/env python3
"""Validation of the winding free-energy gap estimators (direct and TI, ti.py with cubic-spline quadrature)
against exact L=2: dF1 = -(1/beta) ln[P1/(2 P0)] from data/exact_L2.json. Rule: |z| <= 3."""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ti
tags = sys.argv[1:]
ex = json.load(open(os.path.join(HERE, "..", "data", "exact_L2.json")))["0.0"]["beta"]
out = ti.main(tags, [0.25, 0.5, 1.0, 2.0, 4.0])
npass = nfail = 0
for b, r in out.items():
    e = ex[str(float(b))]
    x = -np.log(e["P1"] / (2 * e["P0"])) / b
    for k in ("dF1_TI", "dF1_direct"):
        mu, se = r[k]
        z = (mu - x) / se
        ok = abs(z) <= 3
        npass += ok; nfail += (not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] beta={b} {k}: {mu:.5f} +- {se:.5f} exact {x:.5f} z={z:+.2f}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
