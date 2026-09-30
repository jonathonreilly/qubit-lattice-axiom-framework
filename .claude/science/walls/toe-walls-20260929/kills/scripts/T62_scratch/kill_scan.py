"""Kill-check T62: (a) verify window_counts against brute force; (b) scan ALL 64 count-threshold rules containing 0
(A subset of {0..6}) on periodic Z^3, random order, creation-only; report density, hole density, s, Fano(w=12).
Uses the attacker's own frozen_state / var_curve."""
import sys, itertools, numpy as np
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T62_scratch")
from t62_variance import frozen_state, var_curve, window_counts, slope

# (a) brute-force check of window_counts
rng = np.random.default_rng(1)
occ = (rng.random((10, 10, 10)) < 0.4).astype(np.int8)
for w in (1, 2, 3, 5):
    S = window_counts(occ, w)
    B = np.zeros((10, 10, 10), dtype=np.int64)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                B[i, j, k] = sum(occ[(i+a) % 10, (j+b) % 10, (k+c) % 10] for a in range(w) for b in range(w) for c in range(w))
    print("window_counts w=%d equals brute force:" % w, bool((S == B).all()))

# (b) scan
L = int(sys.argv[1]) if len(sys.argv) > 1 else 48
ws = list(range(1, 17))
print("\nL=%d, 2 seeds; all A subset of {0..6} with 0 in A (else the empty box stays empty)" % L)
print("%-20s %8s %10s %8s %8s %6s" % ("A", "density", "holedens", "s(4..16)", "Fano16", "elig"))
rows = []
for r in range(0, 7):
    for rest in itertools.combinations(range(1, 7), r):
        A = [0] + list(rest)
        ss = []; fs = []; ds = []; el = 0
        for sd in range(2):
            rng = np.random.default_rng(2000 + sd)
            o, ne, ns = frozen_state(L, A, rng)
            el += ne
            vc = var_curve(o, ws)
            V = vc[:, 0]; M = vc[:, 1]
            ds.append(o.mean())
            if V[3] <= 0 or V.min() <= 0:
                ss.append(np.nan); fs.append(np.nan); continue
            ss.append(slope(ws, V)); fs.append(V[15] / (M[15] if o.mean() <= 0.5 else (16**3 - M[15])))
        rows.append((A, np.mean(ds), np.nanmean(ss), np.nanmean(fs), el))
        print("%-20s %8.4f %10.5f %8.3f %8.3f %6d" % (A, np.mean(ds), 1-np.mean(ds), np.nanmean(ss), np.nanmean(fs), el))
good = [r for r in rows if not np.isnan(r[2]) and r[2] < 2.7]
print("\nrules with s < 2.7:", [(r[0], round(r[1],4), round(r[2],3)) for r in good])
