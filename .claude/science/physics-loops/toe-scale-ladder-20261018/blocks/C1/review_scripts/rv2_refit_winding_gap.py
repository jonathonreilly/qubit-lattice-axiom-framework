#!/usr/bin/env python3
"""Reviewer check R2: refit the winding gap dE(L) from the numbers TABULATED in NOTE.md section 5.1 (typed in by
hand from the NOTE, not read from the block's json), with own weighted least squares (closed-form normal equations,
no scipy curve_fit), and audit the verdict arithmetic.

Checks (PASS = the NOTE's number is reproduced within rounding):
  - every fit row of NOTE section 5.2 (parameters, errors, chi2);
  - repo [EXT] refit (section 5.5);
  - the sigma 2-sigma upper bound "sigma <~ 0.04 g";
  - the 0.9/0.7/0.9 sigma ΔE comparisons and the 3.2 sigma E(W=0, L=8) disagreement.
Info: chi2 p-values, sensitivity fits (drop L=4; drop L=12), projection-rule audit, the T=16 version of the
L=8 disagreement, per-plaquette energies against the repo.
"""
import numpy as np
from math import erf, sqrt
from scipy.stats import chi2 as chi2dist

RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""), flush=True)


def wls(X, y, s):
    W = 1 / s ** 2
    A = X.T @ (W[:, None] * X)
    b = X.T @ (W * y)
    cov = np.linalg.inv(A)
    p = cov @ b
    r = (y - X @ p) / s
    return p, np.sqrt(np.diag(cov)), float((r ** 2).sum()), len(y) - len(p)


MODELS = {
    "C": lambda L: np.c_[1 / L],
    "S": lambda L: np.c_[1 / L, L],
    "Str": lambda L: np.c_[L],
    "Q": lambda L: np.c_[1 / L ** 2],
    "K": lambda L: np.c_[np.ones_like(L)],
}

# NOTE section 5.1 (V=0)
T2L = {4: (0.676, 0.063), 6: (0.440, 0.102), 8: (0.161, 0.120), 10: (0.092, 0.301), 12: (0.655, 0.353)}
TMAX = {4: (0.676, 0.063), 6: (0.440, 0.102), 8: (0.322, 0.169), 10: (0.158, 0.385), 12: (0.655, 0.353)}
REPO = {4: (0.7315, 0.0084), 6: (0.3699, 0.0198), 8: (0.1685, 0.0443)}
V05 = {4: (0.185, 0.038), 6: (0.238, 0.080), 8: (-0.038, 0.154)}
V09 = {4: (0.068, 0.010), 6: (-0.014, 0.024), 8: (-0.124, 0.043)}

# NOTE section 5.2 / 5.5 claimed values: (first param, err, [sigma, err], chi2)
CLAIM = {
    "T2L": {"C": (2.62, 0.23, None, 3.9), "S": (None, None, (-0.010, 0.015), 3.4), "Str": (None, None, None, 54.5),
            "Q": (None, None, None, 4.4), "K": (None, None, None, 17.9)},
    "TMAX": {"C": (2.70, 0.23, None, 1.6), "S": (None, None, (0.007, 0.018), 1.4), "Str": (None, None, None, 36.7),
             "Q": (None, None, None, 5.2), "K": (None, None, None, 7.8)},
    "REPO": {"C": (None, None, None, 51), "Q": (None, None, None, 5.1), "S": (None, None, (-0.034, 0.005), 0.07)},
}


def arr(d, keep=None):
    Ls = np.array(sorted(k for k in d if keep is None or k in keep), float)
    return Ls, np.array([d[int(L)][0] for L in Ls]), np.array([d[int(L)][1] for L in Ls])


def close(a, b, tol):
    return abs(a - b) <= tol


fits = {}
for name, d in (("T2L", T2L), ("TMAX", TMAX), ("REPO", REPO), ("V05", V05), ("V09", V09)):
    L, y, s = arr(d)
    print(f"--- {name}: L={L.astype(int).tolist()}")
    fits[name] = {}
    for m, f in MODELS.items():
        p, e, c2, dof = wls(f(L), y, s)
        pv = 1 - chi2dist.cdf(c2, dof) if dof > 0 else float("nan")
        fits[name][m] = (p, e, c2, dof)
        print(f"   {m:3s} p={np.round(p, 4).tolist()} err={np.round(e, 4).tolist()} chi2={c2:.2f}/{dof}  p-value={pv:.3g}")
        if name in CLAIM and m in CLAIM[name]:
            a, ae, sg, c2c = CLAIM[name][m]
            ok = close(c2, c2c, 0.06 if c2c < 10 else 0.6)
            if a is not None:
                ok &= close(p[0], a, 0.006) and close(e[0], ae, 0.006)
            if sg is not None:
                ok &= close(p[1], sg[0], 0.0006) and close(e[1], sg[1], 0.0006)
            check(f"NOTE fit reproduced: {name} model {m}", ok, f"own {np.round(p,4).tolist()}+-{np.round(e,4).tolist()} chi2 {c2:.2f} vs NOTE {CLAIM[name][m]}")

# sigma bound
for name in ("T2L", "TMAX"):
    p, e, _, _ = fits[name]["S"]
    print(f"[INFO] {name}: sigma 2-sigma upper bound = {p[1] + 2 * e[1]:.4f}; 2-sigma lower bound {p[1] - 2 * e[1]:.4f}")
ub = max(fits[n]["S"][0][1] + 2 * fits[n]["S"][1][1] for n in ("T2L", "TMAX"))
check("NOTE 'sigma <~ 0.04 g (2 sigma)' is the max of the two 2-sigma upper bounds", close(ub, 0.04, 0.005), f"{ub:.4f}")

# sensitivity
for name, d in (("T2L", T2L), ("TMAX", TMAX)):
    for keep, lab in (({6, 8, 10, 12}, "drop L=4"), ({4, 6, 8, 10}, "drop L=12"), ({4, 6, 8}, "L=4..8 only")):
        L, y, s = arr(d, keep)
        out = []
        for m in ("C", "S", "Str", "Q"):
            p, e, c2, dof = wls(MODELS[m](L), y, s)
            out.append(f"{m}: p={np.round(p,4).tolist()}+-{np.round(e,4).tolist()} chi2 {c2:.2f}/{dof}")
        print(f"[INFO] sensitivity {name} {lab}: " + " | ".join(out))

# combined: block T-max L=4..12 with repo replacing L=4,6,8 (repo more precise) -- info only
L = np.array([4, 6, 8, 10, 12.]); y = np.array([REPO[4][0], REPO[6][0], REPO[8][0], TMAX[10][0], TMAX[12][0]])
s = np.array([REPO[4][1], REPO[6][1], REPO[8][1], TMAX[10][1], TMAX[12][1]])
for m in ("C", "S", "Q"):
    p, e, c2, dof = wls(MODELS[m](L), y, s)
    print(f"[INFO] repo L=4..8 + block L=10,12 (T max): {m} p={np.round(p,4).tolist()}+-{np.round(e,4).tolist()} chi2 {c2:.2f}/{dof}")

# comparisons with repo
for Lv, (b, be) in ((4, TMAX[4]), (6, TMAX[6]), (8, TMAX[8])):
    r, re_ = REPO[Lv]
    print(f"[INFO] dE L={Lv}: block {b}({be}) vs repo {r}({re_}): {(b - r) / np.hypot(be, re_):+.2f} sigma")
z32 = (-443.3635 - (-443.828)) / np.hypot(0.0311, 0.140)
z16 = (-443.3635 - (-443.734)) / np.hypot(0.0311, 0.077)
check("NOTE 3.2 sigma for E(W=0,L=8): repo -443.3635(311) vs block T=32 -443.828(140)", close(z32, 3.2, 0.06), f"{z32:.2f} sigma")
print(f"[INFO] same comparison against block T=16 -443.734(77): {z16:.2f} sigma (NOT quoted in NOTE); "
      f"size of the disagreement 0.37-0.46 exceeds dE(L=8) itself (0.16-0.32)")
for Lv, rep, blk in ((4, (-56.2820, 0.0069), (-56.253, 0.045)), (6, (-187.4349, 0.0145), (-187.455, 0.076)),
                     (8, (-443.3635, 0.0311), (-443.828, 0.140))):
    z = (rep[0] - blk[0]) / np.hypot(rep[1], blk[1])
    npl = 3 * Lv ** 3
    print(f"[INFO] E(W=0) L={Lv}: repo {rep[0]} block {blk[0]}: {z:+.2f} sigma; per plaquette repo {rep[0]/npl:.5f} block {blk[0]/npl:.5f}")

# projection-rule audit from the per-chain table (W=0 energies, other T values the NOTE table does not show)
npl4, npl6 = 192, 648
e16 = np.array([-0.29335, -0.29319, -0.29320]) * npl4
se16 = np.array([0.00025, 0.00026, 0.00026]) * npl4
m16 = e16.mean(); s16 = max(e16.std(ddof=1) / sqrt(3), np.sqrt((se16 ** 2).sum()) / 3)
print(f"[INFO] projection audit W=0 L=4: T=8 -56.253(45) vs T=16 {m16:.3f}({s16:.3f}): {(m16 + 56.253) / np.hypot(0.045, s16):+.2f} sigma")
e18, s18 = -0.28901 * npl6, 0.00011 * npl6
print(f"[INFO] projection audit W=0 L=6: T=12 -187.455(76) vs T=18 (1 chain) {e18:.3f}({s18:.3f}): {(e18 + 187.455) / np.hypot(0.076, s18):+.2f} sigma "
      f"(E_mix must DEcrease with T in expectation)")
print("[INFO] W=1 energies exist at a single T for L=4, 6, 12: the dE projection rule is testable only at L=8, 10")

# V=0.9 negative dE significance
for Lv, (v, e) in V09.items():
    print(f"[INFO] V=0.9 L={Lv}: dE/sigma = {v / e:+.2f}")
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
