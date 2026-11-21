#!/usr/bin/env python3
"""lane976 analysis: applies the pre-set criteria of library/gap-escape-opus.md Section 3 to logs/*.npz.
Usage: python3 -I ana976.py <logs dir>. Written by Claude Opus 5.5 for row 976. GUIDE only."""
import glob, json, os, re, sys
import numpy as np

D = sys.argv[1]
KS = [1, 2, 3, 4, 8, 16, 30, 45]


def load(pattern):
    runs = []
    for f in sorted(glob.glob(os.path.join(D, pattern))):
        z = np.load(f)
        runs.append({k: z[k] for k in ("sxy", "sxz", "syz", "O", "D")} | {"file": os.path.basename(f)})
    return runs


def frac_stats(per_seed, n_eff):
    v = np.array(per_seed, dtype=float)
    m = float(v.mean())
    se = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else float("nan")
    ub = 3.0 / n_eff if m == 0.0 else None
    return m, se, ub


def analyse(runs, s0, tol_rel=0.10, mode="xy"):
    """mode xy: in A' iff s_k >= (1 - tol) s0; mode vac: |s_k - s0| <= tol s0."""
    T = runs[0]["sxy"].shape[1] - 1
    O1bar = float(np.mean(np.concatenate([r["O"][:, 1] for r in runs])))
    n_eff = len(runs) * 4
    out = {"n_seeds": len(runs), "n_conf": int(sum(r["sxy"].shape[0] for r in runs)), "O1bar": O1bar, "k": {}}
    for k in KS:
        if k > T:
            continue
        fA, fAp, s, o, d = [], [], [], [], []
        for r in runs:
            sk = r["sxy"][:, k]
            inAp = sk >= (1 - tol_rel) * s0 if mode == "xy" else np.abs(sk - s0) <= tol_rel * s0
            inA = inAp & (r["O"][:, k] > O1bar / 2)
            fA.append(inA.mean()); fAp.append(inAp.mean())
            s.append(sk.mean()); o.append(r["O"][:, k].mean()); d.append(r["D"][:, k].mean())
        mA, seA, ubA = frac_stats(fA, n_eff)
        mAp, seAp, ubAp = frac_stats(fAp, n_eff)
        out["k"][k] = {"f_A": mA, "se_A": seA, "ub95_A": ubA, "f_Ap": mAp, "se_Ap": seAp, "ub95_Ap": ubAp,
                       "s": float(np.mean(s)), "se_s": float(np.std(s, ddof=1) / np.sqrt(len(s))) if len(s) > 1 else None,
                       "O": float(np.mean(o)), "D": float(np.mean(d)),
                       "smax": float(max(r["sxy"][:, k].max() for r in runs)), "smin": float(min(r["sxy"][:, k].min() for r in runs)),
                       "sxz": float(np.mean([r["sxz"][:, k].mean() for r in runs])),
                       "syz": float(np.mean([r["syz"][:, k].mean() for r in runs]))}
    return out


res = {}
names = set()
for f in glob.glob(os.path.join(D, "xy_b*_L*_T*_*_s*.npz")):
    m = re.match(r"xy_b([\d.]+)_L(\d+)_T(\d+)_(cold|hot)_s\d+\.npz", os.path.basename(f))
    names.add(m.groups())
for (b, L, T, st) in sorted(names):
    runs = load(f"xy_b{b}_L{L}_T{T}_{st}_s*.npz")
    res[f"xy b{b} L{L} T{T} {st}"] = analyse(runs, 2.0)
for f in sorted(glob.glob(os.path.join(D, "vac_b*_L8.npy"))):
    b = re.match(r"vac_b([\d.]+)_L8\.npy", os.path.basename(f)).group(1)
    uv = np.load(f)
    # xy action of the frozen vacuum slice = s_0 of every vac run (slice 0 is frozen)
    runs = load(f"vac_b{b}_L8_T*_cold_s*.npz")
    if runs:
        s0 = float(runs[0]["sxy"][0, 0])
        r = analyse(runs, s0, mode="vac"); r["s0"] = s0
        res[f"vac b{b} L8"] = r
for f in sorted(glob.glob(os.path.join(D, "xyT_b*_L8_T*_cold_s11.npz"))):
    m = re.match(r"xyT_b([\d.]+)_L8_T(\d+)_cold_s11\.npz", os.path.basename(f))
    runs = load(os.path.basename(f))
    r = runs[0]
    T = r["sxy"].shape[1] - 1
    res[f"buffer b{m.group(1)} L8 T{T}"] = {k: float(r["sxy"][:, k].mean()) for k in KS if k <= T}
json.dump(res, open(os.path.join(D, "ana976.json"), "w"), indent=1)

for key, r in res.items():
    if key.startswith("buffer"):
        print(key, " ".join(f"s{k}={v:.4f}" for k, v in r.items()))
        continue
    print(f"{key}: seeds {r['n_seeds']} conf {r['n_conf']} O1bar {r['O1bar']:.4f}" + (f" s0 {r['s0']:.4f}" if "s0" in r else ""))
    for k, v in r["k"].items():
        ub = f" ub95 {v['ub95_Ap']:.3f}" if v["ub95_Ap"] is not None else ""
        print(f"   k={k:2d} s={v['s']:.4f}+-{(v['se_s'] or 0):.4f} sxz={v['sxz']:.4f} syz={v['syz']:.4f} O={v['O']:.4f} D={v['D']:.4f}"
              f" smax={v['smax']:.3f} fA={v['f_A']:.3f}+-{v['se_A']:.3f} fA'={v['f_Ap']:.3f}+-{v['se_Ap']:.3f}{ub}")
