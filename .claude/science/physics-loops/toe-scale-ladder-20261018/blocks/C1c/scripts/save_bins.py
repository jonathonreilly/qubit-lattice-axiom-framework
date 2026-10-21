#!/usr/bin/env python3
"""Compact 20-bin summaries of raw PT measurement files (to keep data/ < 50 MB): per tag, per beta,
bin means of E, W2, P0, P1, Nc, S1 and the TI sums (n0, n1, e0, e1, ntot). usage: save_bins.py OUT TAG..."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from analyze import load, derived
import ti
out = {}
for t in sys.argv[2:]:
    d = load(t)
    der = derived(d["m"], d["keys"])
    n = len(d["m"]) // 20
    for q, v in der.items():
        out[f"{t}/{q}"] = v[: n * 20].reshape((20, n) + v.shape[1:]).mean(1)
    b, S, _ = ti.sums(t)
    for q, v in S.items():
        out[f"{t}/ti_{q}"] = v
    out[f"{t}/betas"] = d["betas"]
    out[f"{t}/trips"] = d["trips"]
np.savez_compressed(sys.argv[1], **out)
