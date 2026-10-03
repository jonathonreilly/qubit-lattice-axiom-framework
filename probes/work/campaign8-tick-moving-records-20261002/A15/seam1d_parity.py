#!/usr/bin/env python3
"""A15: 1D seam rules with the other seam parity (seam bond even: s odd), and R at full swap vs the exact 2/9."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from seam1d import run
for rule in ('H', 'K', 'P', 'Smu', 'R'):
    for th, K0 in ((np.pi / 2, np.pi / 2), (np.pi / 4, 2.742)):
        tr, rf, nr, mj, T, pur, vg = run(rule, th, K0, 'A', N=522, s=261)
        print("s odd: rule %-3s theta=%.3f K0=%.3f: trans %.6f refl %.6f maxjump %d purity %.3f" % (rule, th, K0, tr, rf, mj, pur))
print("exact absorbing-chain value for R at full swap: 2/9 = %.6f" % (2 / 9))
