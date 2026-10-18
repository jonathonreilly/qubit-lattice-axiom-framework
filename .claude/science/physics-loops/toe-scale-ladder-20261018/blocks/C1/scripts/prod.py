#!/usr/bin/env python3
"""Production run: python3 prod.py L V T nsweep ntherm seed [J] [dtau] [every]
Writes data/run_L{L}_V{V}_T{T}_s{seed}.npz (small summary: binned spectra, scalars) and appends a JSON line
to logs/prod.jsonl."""
import os, sys, json, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from driver import run

L, V, T = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
nsweep, ntherm, seed = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
J = int(sys.argv[7]) if len(sys.argv) > 7 else int(T)
dtau = float(sys.argv[8]) if len(sys.argv) > 8 else 0.25
factor = float(sys.argv[9]) if len(sys.argv) > 9 else 1.0
base = os.path.join(os.path.dirname(__file__), "..")
log = open(os.path.join(base, "logs", "prod.jsonl"), "a")
cap = int(max(64, 3 * T + 64))
r = run(L, V, T, nsweep, ntherm, seed, mode=0, J=J, dtau=dtau, factor=factor, cap=cap, log=log)
out = {k: np.asarray(v) for k, v in r.items() if isinstance(v, (np.ndarray, list, tuple, float, int))}
np.savez_compressed(os.path.join(base, "data", f"run_L{L}_V{V}_T{T}_s{seed}.npz"),
                    **{k: (np.asarray(v, dtype=float) if k not in ("stats",) else np.asarray(v)) for k, v in out.items()})
print(f"done L={L} V={V} T={T} seed={seed} time={r['time_total']:.0f}s fails={r['gauss_or_path_failures']} "
      f"valid={r['valid_final']} ST1={r['ST1']} Nf={r['Nf_mid']} Emix={r['Emix']}", flush=True)
