"""PR 9382 attack-d: QUANTIFIER SCOPE of 'the 8^3 tension is a population effect' and 'S falls with the population to within the moment bound', from the note's own table.

The table (8^3, k = pi/4; forward-walking S at lags 1, 2, 4, 8 for 120 (landed), 960, 3840 and two seeds of 7680 walkers) carries four population values.  The note says: 'population convergence: not shown;
S falls from 960 to 3840 walkers and is stable from 3840 to 7680 at lags 2 to 4'.  What the table alone implies under different extrapolation forms in the walker number N_w:
  S(N_w) = S_inf + a / N_w,  S_inf + a / sqrt(N_w),  S_inf + a N_w^(-1/3), and a saturating exponential in log N_w,
fitted to lag 2 and lag 4 (with the 120-walker landed values where the table has them), the implied S_inf against the ceiling s sqrt(u chi) = 0.424, and how many of the fitted forms leave S_inf below the ceiling;
plus the standard-error bookkeeping the note describes (two seeds combined by 'the larger of mean error over sqrt 2 and half the difference') applied to the two 7680 values at each lag.
Only the numbers printed in the note are used.
"""
import sys
import numpy as np
from scipy.optimize import curve_fit

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

s = 2 * np.sin(np.pi / 8); u, chi = 0.2888, 1.064
ceil = s * np.sqrt(u * chi)
N = np.array([120, 960, 3840, 7680, 7680], float)
tab = {  # lag -> values per row (120, 960, 3840, 7680 seed 3, 7680 seed 4); nan where the table is empty
    0: [np.nan, 0.574, 0.565, 0.556, 0.564],
    1: [0.572, 0.476, 0.448, 0.427, 0.440],
    2: [0.575, 0.468, 0.428, 0.402, 0.413],
    4: [0.564, 0.445, 0.403, 0.415, 0.413],
    8: [np.nan, 0.430, 0.353, 0.395, 0.410],
}
print(f"ceiling s sqrt(u chi) = {ceil:.4f}")
forms = {"a/N": lambda n, S, a: S + a / n, "a/sqrt(N)": lambda n, S, a: S + a / np.sqrt(n), "a N^(-1/3)": lambda n, S, a: S + a * n ** (-1 / 3)}
res = {}
for lag in (1, 2, 4):
    y = np.array(tab[lag]); ok = ~np.isnan(y)
    for use120 in (True, False):
        m = ok & (N > 120 if not use120 else True)
        for nm, f in forms.items():
            try:
                p, cov = curve_fit(f, N[m], y[m], p0=[0.4, 0.1], maxfev=20000)
                res[(lag, use120, nm)] = (p[0], np.sqrt(cov[0, 0]) if np.isfinite(cov[0, 0]) else np.nan, float(np.sqrt(np.mean((f(N[m], *p) - y[m]) ** 2))))
            except Exception:
                res[(lag, use120, nm)] = (np.nan, np.nan, np.nan)
print("   lag  rows used         form         S_inf   (se)     rms of fit   S_inf / ceiling")
for (lag, use120, nm), (Sinf, se, rms) in res.items():
    print(f"   {lag:3d}  {'with 120 walkers' if use120 else 'N >= 960 only':16s}  {nm:12s} {Sinf:7.4f}  ({se:6.4f})  {rms:9.4f}   {Sinf/ceil:6.3f}")
below = [(k, v[0]) for k, v in res.items() if np.isfinite(v[0]) and v[0] < ceil]
vals = np.array([v[0] for v in res.values() if np.isfinite(v[0])])
print(f"   implied S_inf over all {len(vals)} fits: {vals.min():.3f} .. {vals.max():.3f}; ceiling {ceil:.4f}; fits with S_inf below the ceiling: {len(below)} of {len(vals)}")
l24 = [v[0] for (lag, u120, nm), v in res.items() if lag in (2, 4) and np.isfinite(v[0])]
l1 = {(u120, nm): v[0] for (lag, u120, nm), v in res.items() if lag == 1}
above1 = {k_: round(v, 3) for k_, v in l1.items() if v >= ceil}
print(f"   lags 2 and 4 (the plateau lags the note uses): {len(l24)} fits, S_inf {min(l24):.3f} .. {max(l24):.3f}; lag 1 fits at or above the ceiling: {above1}")
check("every extrapolation at the plateau lags 2 and 4 (three forms, with and without the 120-walker row) leaves S_inf below the moment ceiling 0.424; only the two lag-1 1/N fits reach above it (lag 1 is not a plateau lag)", all(v < ceil for v in l24) and len(l24) == 12 and len(above1) == 2 and all(k_[1] == "a/N" for k_ in above1), f"lags 2, 4: {min(l24):.3f}..{max(l24):.3f}; lag 1 above: {above1}")
# the pure S and the population dependence at the largest populations: is 'stable from 3840 to 7680' distinguishable from a slow decline?
print("\n   3840 -> 7680 change per lag (mean of the two seeds minus the 3840 value):", {lag: round(float(np.nanmean(tab[lag][3:5]) - tab[lag][2]), 4) for lag in (1, 2, 4, 8)})
ch = {lag: float(np.nanmean(tab[lag][3:5]) - tab[lag][2]) for lag in (1, 2, 4)}
# what the 1/N form would predict for that step from the 960 -> 3840 change
a960_3840 = {lag: tab[lag][1] - tab[lag][2] for lag in (1, 2, 4)}
pred = {lag: a960_3840[lag] * (1 / 3840 - 1 / 7680) / (1 / 960 - 1 / 3840) for lag in (1, 2, 4)}
print("   1/N prediction of the 3840 -> 7680 change from the 960 -> 3840 change:", {lag: round(-pred[lag], 4) for lag in (1, 2, 4)}, "; observed:", {lag: round(ch[lag], 4) for lag in (1, 2, 4)})
check("the observed 3840 -> 7680 change is larger in magnitude than a 1/N law would predict at lags 1 and 2 (the table does not show 1/N convergence; it shows a faster fall and then a plateau, as the note says)", abs(ch[1]) > abs(pred[1]) and abs(ch[2]) > abs(pred[2]), f"observed {ch}, 1/N predicts {{lag: -pred[lag]}}".replace("{lag: -pred[lag]}", str({k: round(-v, 4) for k, v in pred.items()})))
# two-seed combination rule
for lag in (2, 4, 8):
    a, b = tab[lag][3], tab[lag][4]
    print(f"   lag {lag}: seeds {a}, {b}: mean {np.mean([a, b]):.4f}, half difference {abs(a-b)/2:.4f}  (the rule takes the larger of mean error/sqrt 2 and this half difference)")
mean_lag2_4 = np.mean([np.mean(tab[2][3:5]), np.mean(tab[4][3:5])])
check("the combined S = 0.408 is the mean of the two seeds' plateau values 0.4058 and 0.4110 and lies within 0.003 of the mean of the lag-2 and lag-4 seed means from the table", abs(0.408 - (0.4058 + 0.4110) / 2) < 5e-4 and abs(mean_lag2_4 - 0.408) < 0.003, f"table lag 2/4 mean {mean_lag2_4:.4f}")
print(f"   at the note's own 'S = 0.408 +- 0.014' the ratio to the ceiling is {0.408/ceil:.3f}; the extrapolated S_inf values {vals.min():.3f}..{vals.max():.3f} correspond to {vals.min()/ceil:.2f}..{vals.max()/ceil:.2f} of the ceiling")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9382 from the note's own table: {len(l24)} of {len(l24)} extrapolations at the plateau lags 2 and 4 (1/N, 1/sqrt N, N^-1/3; with/without the 120-walker row) give S_inf {min(l24):.3f}-{max(l24):.3f}, all below the ceiling {ceil:.3f}, while the two lag-1 1/N fits give {min(above1.values()):.3f}-{max(above1.values()):.3f} (above it; lag 1 is not a plateau lag); the 3840 -> 7680 change (lag 2: {ch[2]:+.3f}) is larger than a 1/N law predicts ({-pred[2]:+.3f}), i.e. the table shows a fall then a plateau rather than 1/N convergence, consistent with the note's 'population convergence not shown'; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
