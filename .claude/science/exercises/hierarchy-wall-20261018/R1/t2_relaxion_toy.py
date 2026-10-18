"""R1 / T2: relaxion toy with the record count as the scanner.

Records are permanent, so the local record fraction s_i only rises: a native
monotone scanner. mu^2_i = 1 - 2 s_i (Higgs mass^2 in cutoff units).
Unrecorded sites form a record with probability p per tick while mu^2_i > 0;
formation halts where mu^2_i <= 0 (the vev's backreaction stops the scan).
Frozen floor F = <|mu^2|>, <v^2> = <max(0, -mu^2)>.
"""
import numpy as np
from scipy.ndimage import uniform_filter

L = 48
rng = np.random.default_rng(7)


def run(p, R, maxticks=200000):
    r = np.zeros((L, L, L), bool)
    size = 2 * R + 1
    ticks = 0
    while ticks < maxticks:
        s = uniform_filter(r.astype(np.float64), size=size, mode="wrap")
        elig = (~r) & (1.0 - 2.0 * s > 1e-12)
        if not elig.any():
            break
        r |= elig & (rng.random(r.shape) < p)
        ticks += 1
    s = uniform_filter(r.astype(np.float64), size=size, mode="wrap")
    mu2 = 1.0 - 2.0 * s
    return np.mean(np.abs(mu2)), np.mean(np.maximum(0.0, -mu2)), ticks, r.mean()


print(f"lattice {L}^3 periodic; target (v/M)^2 ~ 4e-34")
res = {}
for R in [1, 2, 4, 8]:
    V = (2 * R + 1) ** 3
    for p in [1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001]:
        F, v2, ticks, frac = run(p, R)
        res[(R, p)] = F
        print(f"R={R} V={V:5d} p={p:6.3f}: floor <|mu^2|>={F:.3e} <v^2>={v2:.3e} "
              f"ticks={ticks:6d} record fraction={frac:.4f}")

for R in [1, 2, 4, 8]:
    ps = np.array([0.03, 0.01, 0.003, 0.001])
    Fs = np.array([res[(R, p)] for p in ps])
    sl = np.polyfit(np.log(ps), np.log(Fs), 1)[0]
    print(f"R={R}: d ln F / d ln p over p in [1e-3, 3e-2] = {sl:.3f}")
Vs = np.array([(2 * R + 1) ** 3 for R in [1, 2, 4, 8]])
Fs = np.array([res[(R, 0.001)] for R in [1, 2, 4, 8]])
print(f"p=1e-3: d ln F / d ln V = {np.polyfit(np.log(Vs), np.log(Fs), 1)[0]:.3f}")
print("NATIVE-RELAX-FAIL" if res[(1, 1.0)] >= 0.01 else "NATIVE-RELAX-not-failed")
