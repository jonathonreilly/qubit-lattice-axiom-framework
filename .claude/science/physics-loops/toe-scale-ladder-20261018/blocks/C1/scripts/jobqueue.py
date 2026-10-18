#!/usr/bin/env python3
"""Sequential job queue: python3 queue.py <jobfile>; each line: L V T nsweep ntherm seed J dtau factor every.
Skips jobs whose data file exists. Logs to logs/queue_<jobfile-stem>.log"""
import os, sys, subprocess, time
here = os.path.dirname(os.path.abspath(__file__))
jobs = [l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
for j in jobs:
    L, V, T, seed = j[0], float(j[1]), float(j[2]), j[5]
    out = os.path.join(here, "..", "data", f"run_L{L}_V{V}_T{T}_s{seed}.npz")
    if os.path.exists(out):
        continue
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(here, "prod.py")] + j, capture_output=True, text=True)
    print(f"[{time.strftime('%H:%M:%S')}] {' '.join(j)} -> rc={r.returncode} {time.time()-t0:.0f}s :: "
          f"{r.stdout.strip()[-400:]} {r.stderr.strip()[-600:]}", flush=True)
