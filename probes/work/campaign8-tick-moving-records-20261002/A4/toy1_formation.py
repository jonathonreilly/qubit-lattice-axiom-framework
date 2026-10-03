"""Toy 1: formation rules, with and without (unbiased, g=0) moves, 2D periodic L x L.

usage: python3 toy1_formation.py RULE MOVES(0/1) [L] [T]
Outputs a compact summary line + saves h(t), E(t) to npz.
"""
import sys, time
import numpy as np
from t1lib import tick

rule = sys.argv[1]
moves = bool(int(sys.argv[2]))
L = int(sys.argv[3]) if len(sys.argv) > 3 else 128
T = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
params = dict(p=0.05, k=1, beta=1.0, m=1)
rng = np.random.default_rng(12345)
rho0 = 0.2
occ = rng.random((L, L)) < rho0
N = L * L
h = np.empty(T + 1)
E = np.zeros(T)
F = np.zeros(T)
M = np.zeros(T)
h[0] = 1 - occ.mean()
last = np.full((L, L), -1, dtype=np.int32)
count = np.zeros((L, L), dtype=np.int32)
expg = np.exp(0.0 * np.arange(5))
t0 = time.time()
for t in range(T):
    occ, out, form = tick(occ, 0.0, rule, rng, params, moves=moves, expg=expg)
    ev = out.astype(np.int32) + form.astype(np.int32)
    count += ev
    last[ev > 0] = t
    M[t] = out.sum() / N
    F[t] = form.sum() / N
    E[t] = M[t] + F[t]
    h[t + 1] = 1 - occ.mean()
el = time.time() - t0
recent = (last >= T - 500).mean()
# late-time log-log slope of h between T/4 and T
i1, i2 = T // 4, T
hl = h[i1:i2 + 1]
if hl[-1] > 0 and hl[0] > 0:
    slope = np.polyfit(np.log(np.arange(i1, i2 + 1)), np.log(np.maximum(hl, 1e-12)), 1)[0]
    rate = -np.polyfit(np.arange(i1, i2 + 1), np.log(np.maximum(hl, 1e-12)), 1)[0]
else:
    slope = rate = np.nan
cps = [10, 100, 500, 1000, 2000]
print(f"rule={rule:10s} moves={int(moves)} L={L} T={T} time={el:.1f}s")
print("  h(t):    " + "  ".join(f"t={c}:{h[c]:.5f}" for c in cps if c <= T))
print("  E(t):    " + "  ".join(f"t={c}:{E[c-1]:.5f}" for c in cps if c <= T))
print(f"  cum events/site={count.mean():.3f}  cum formations/site={F.sum():.4f} (<= 1-rho0 = {1-rho0:.2f} bound)  "
      f"frac sites with event in last 500 ticks={recent:.4f}  late loglog slope={slope:.3f}  late exp rate={rate:.5f}")
np.savez(f"toy1_{rule}_m{int(moves)}.npz", h=h, E=E, F=F, M=M, count=count)
