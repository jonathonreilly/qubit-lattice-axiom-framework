"""A34 c8: independent check of A36 D7(e) -- does the speed-up of record-timed phases shrink like O(F)?

Own code. Classical gated growth on Z^2 from one seed (A28 gate: a site can form only with a recorded
neighbour, judged at the start of each instant). Schedules:
  G  : one shared tick per cycle; every gate-open empty site forms with chance F at that instant;
  UP : four instants per cycle; a gate-open empty site acts at the instant equal to its number of
       recorded neighbours k (1..4), with chance F (once per cycle per class instant).
Measured: cycles (instants / instants-per-cycle) until some record reaches L-infinity distance R.
ratio = mean cycles(G) / mean cycles(UP)  (> 1: UP faster). A32's 1D renewal argument predicts 1 + O(F).
usage: python3 c8_record_timed_speed.py F NRUNS
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal, sys
import numpy as np
signal.alarm(28)
F = float(sys.argv[1]); NR = int(sys.argv[2]); R = 30
N = 2 * R + 5; c0 = N // 2
rng = np.random.default_rng(int(F * 1e4) + NR)
yy, xx = np.mgrid[0:N, 0:N]
dist = np.maximum(abs(yy - c0), abs(xx - c0))

def kcount(rec):
    k = np.zeros_like(rec, dtype=np.int8)
    k[1:, :] += rec[:-1, :]; k[:-1, :] += rec[1:, :]
    k[:, 1:] += rec[:, :-1]; k[:, :-1] += rec[:, 1:]
    return k

def run(schedule):
    rec = np.zeros((N, N), dtype=np.int8); rec[c0, c0] = 1
    per = 1 if schedule == "G" else 4
    inst = 0
    while True:
        k = kcount(rec)
        if schedule == "G":
            act = (rec == 0) & (k >= 1)
        else:
            act = (rec == 0) & (k == (inst % per) + 1)
        new = act & (rng.random((N, N)) < F)
        rec[new] = 1
        inst += 1
        if new.any() and dist[new.astype(bool)].max() >= R:
            return inst / per

g = np.array([run("G") for _ in range(NR)])
u = np.array([run("UP") for _ in range(NR)])
ratio = g.mean() / u.mean()
err = ratio * np.sqrt((g.std() / g.mean()) ** 2 / NR + (u.std() / u.mean()) ** 2 / NR)
print(f"F={F}: cycles G {g.mean():.1f}, UP {u.mean():.1f}; ratio {ratio:.4f} +- {err:.4f}; excess/F = {(ratio - 1) / F:.3f} +- {err / F:.3f}  ({NR} runs each)")
