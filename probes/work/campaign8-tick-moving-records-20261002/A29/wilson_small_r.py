#!/usr/bin/env python3
"""A29: growth rate of the traceless-only Wilson patch in continuous time as r -> 0 (does a tiny patch stay unstable?)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools, importlib.util, sys, io, contextlib
import numpy as np
spec = importlib.util.spec_from_file_location("wc", "wilson_continuous.py")
wc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(wc)
grid = np.linspace(-np.pi, np.pi, 17)
for label, Wproj in (("full", np.eye(6)), ("traceless-only", wc.P_tl)):
    for r in (1e-2, 1e-3, 1e-4, 1e-5):
        g_best = 0.0
        for k in itertools.product(grid, repeat=3):
            k = np.array(k)
            w = r * np.sum((2 - 2 * np.cos(k)) ** 2)
            lam = np.linalg.eigvals(wc.M @ (wc.V_of(np.sin(k)) + w * Wproj)).astype(complex)
            g_best = max(g_best, np.abs(np.sqrt(lam).imag).max())
        print(f"{label:15s} r={r:.0e}: max growth {g_best:.4f} per unit time;  growth / r^(1/4) = {g_best / r**0.25:.3f};  growth / r^(1/2) = {g_best / r**0.5:.3f}")
