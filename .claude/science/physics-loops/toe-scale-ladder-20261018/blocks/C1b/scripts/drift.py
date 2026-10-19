#!/usr/bin/env python3
"""Equilibration drift diagnostic: per measurement chunk (15 min each), P(|W_a|=1), P0, <W^2>, E, S1 at
beta = L/2, L, bmax.  usage: drift.py TAG"""
import sys, glob, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
tag = sys.argv[1]
fs = sorted(glob.glob(os.path.join(HERE, "..", "data", "raw", tag + "_c*.npz")))
for f in fs:
    d = np.load(f)
    m = d["m"]; k = list(d["keys"]); b = d["betas"]
    L = int(tag[1]) if tag[1] != '1' else 10
    line = f"{os.path.basename(f)} nsw_end={int(d['nsw_end'])} trips={int(d['trips'])}:"
    for bb in (L / 2, float(L), b.max()):
        i = int(np.argmin(np.abs(b - bb)))
        W = m[:, i, [k.index('Wx'), k.index('Wy'), k.index('Wz')]]
        p0 = (W == 0).mean(); p1 = (np.abs(W) == 1).mean()
        line += f" | b={b[i]:.3g} P0={p0:.3f} P1={p1:.3f} W2={(W**2).mean():.3f} E={m[:, i, k.index('E')].mean():.2f}"
    print(line)
