"""Toy 3: leak and evaporation of a single square jam in an empty periodic 2D box (no formation).
usage: python3 toy3_evap.py g s nseeds [L] [T]
Per tick: jam = largest 4-connected cluster (tracked every tick).
Reports (averaged over seeds):
  gross  = detachments per tick: jam records that end the tick outside the jam cluster,
  per_edge = gross / number of jam records with an empty neighbour,
  net    = net loss rate of the jam in the window [T/4, T] (linear fit of jam size),
  ret    = 1 - net/gross (fraction of step-outs that come back),
  N(T)/N0 and the half-life if reached.
"""
import sys, time
import numpy as np
from scipy import ndimage
from t1lib import move_phase, neighbour_count
g = float(sys.argv[1]); s = int(sys.argv[2]); ns = int(sys.argv[3])
L = int(sys.argv[4]) if len(sys.argv) > 4 else 128
T = int(sys.argv[5]) if len(sys.argv) > 5 else 2000
expg = np.exp(g * np.arange(5))
def jam_mask(occ):
    lab, n = ndimage.label(occ)
    if n == 0: return np.zeros_like(occ)
    cnt = np.bincount(lab.ravel()); cnt[0] = 0
    return lab == cnt.argmax()
res = []
t0 = time.time()
for seed in range(ns):
    rng = np.random.default_rng(1000 * s + seed + int(100 * g))
    occ = np.zeros((L, L), bool); c = L // 2 - s // 2
    occ[c:c + s, c:c + s] = True
    N0 = occ.sum(); sizes = []; gross = []; edge = []; half = None
    jam = jam_mask(occ)
    for t in range(1, T + 1):
        nrec = neighbour_count(occ)
        edge.append((jam & (nrec < 4)).sum())
        new, out, arr, wins = move_phase(occ, g, rng, expg)
        # arrivals whose origin was a jam site
        from_jam = np.zeros_like(occ)
        for i, (ax, sg) in enumerate([(a, b) for a in range(2) for b in (1, -1)]):
            from_jam |= wins[i] & np.roll(jam, sg, axis=ax)
        occ = new
        jam = jam_mask(occ)
        gross.append((from_jam & ~jam).sum())   # detachments: jam record ends the tick outside the jam cluster
        sizes.append(jam.sum())
        if half is None and sizes[-1] <= N0 / 2: half = t
    sizes = np.array(sizes); tt = np.arange(1, T + 1)
    w = tt >= T // 4
    net = -np.polyfit(tt[w], sizes[w], 1)[0]
    gr = np.mean(gross[T // 4:]); ed = np.mean(edge[T // 4:])
    res.append((gr, gr / ed, net, sizes[-1] / N0, half if half else np.nan, ed))
r = np.array(res); m = np.nanmean(r, axis=0); sd = np.nanstd(r, axis=0) / np.sqrt(ns)
print(f"g={g} s={s} N0={s*s} seeds={ns}: gross detachments/tick={m[0]:.4f} per edge record={m[1]:.5f} "
      f"net loss/tick={m[2]:.4f}+-{sd[2]:.4f} return frac={1-m[2]/m[0]:.3f} edge recs={m[5]:.1f} N(T)/N0={m[3]:.3f} "
      f"half-life={m[4]:.0f} ({np.isfinite(r[:,4]).sum()}/{ns} reached) [{time.time()-t0:.1f}s]", flush=True)
