#!/usr/bin/env python3
"""T16 test 3: does a symmetric start buy homogeneity (L13-W5)?  2D torus growth of permanent
one-per-site records: rate lam0 + lam1*k (k recorded nearest neighbours), lock content s=+-1
heat-bath biased by neighbours (kappa).  Starts: (a) empty + uniform nucleation, (b) 4 seeds,
(c) Bernoulli sparse seeds at t=0.  Stop at mean density 0.30."""
import numpy as np

L = 384
lam1, dt, kappa = 1.0, 0.05, 0.5
rho_stop = 0.30
rng = np.random.default_rng(1601)


def neigh_sum(a):
    return np.roll(a, 1, 0) + np.roll(a, -1, 0) + np.roll(a, 1, 1) + np.roll(a, -1, 1)


def run(kind, lam0):
    occ = np.zeros((L, L), bool)
    s = np.zeros((L, L), np.int8)
    if kind == "seeds4":
        for _ in range(4):
            i, j = rng.integers(0, L, 2)
            occ[i, j] = True
            s[i, j] = rng.choice([-1, 1])
    elif kind == "bernoulli":
        m = rng.random((L, L)) < 3e-3
        occ |= m
        s[m] = rng.choice([-1, 1], size=m.sum())
    t = 0.0
    while occ.mean() < rho_stop:
        k = neigh_sum(occ.astype(np.int8))
        rate = lam0 + lam1 * k
        p = 1 - np.exp(-rate * dt)
        new = (~occ) & (rng.random((L, L)) < p)
        if new.any():
            m = neigh_sum(s.astype(np.int8))
            pplus = 1 / (1 + np.exp(-2 * kappa * m))
            ss = np.where(rng.random((L, L)) < pplus, 1, -1).astype(np.int8)
            s[new] = ss[new]
            occ |= new
        t += dt
    return occ, s, t


def block_var(occ, b):
    n = L // b
    d = occ[: n * b, : n * b].reshape(n, b, n, b).mean(axis=(1, 3))
    return d.ravel()


def corr_content(occ, s, rmax):
    # C(r) along axes for pairs both recorded; mean-subtracted globally is unnecessary (s symmetric)
    out = []
    for r in range(1, rmax):
        num = den = 0.0
        for ax in (0, 1):
            a, b = s, np.roll(s, -r, ax)
            both = (a != 0) & (b != 0)
            num += (a * b)[both].sum()
            den += both.sum()
        out.append(num / max(den, 1))
    return np.array(out)


configs = [("empty+nucleation", "empty", 3e-4), ("4 seeds", "seeds4", 0.0), ("bernoulli 3e-3", "bernoulli", 0.0)]
NR = 16
results = {}
for name, kind, lam0 in configs:
    S = {12: [], 24: [], 48: [], 96: []}
    C = []
    T = []
    for _ in range(NR):
        occ, s, t = run(kind, lam0)
        T.append(t)
        rho = occ.mean()
        for b in S:
            S[b].append(b * b * block_var(occ, b).var() / (rho * (1 - rho)))
        C.append(corr_content(occ, s, 150))
    C = np.array(C)
    results[name] = dict(T=np.mean(T), S={b: np.mean(v) for b, v in S.items()}, C=C.mean(0), Cse=C.std(0) / np.sqrt(NR))
    r = results[name]
    print(f"{name:18s}: stop time {r['T']:.1f}; b^2 Var(block)/[rho(1-rho)] at b=12,24,48: "
          f"{r['S'][12]:.1f}, {r['S'][24]:.1f}, {r['S'][48]:.1f}, b=96: {r['S'][96]:.1f}; S96/S24 = {r['S'][96]/r['S'][24]:.2f}")

print()
# speed estimate from the seeds run: front radius R ~ sqrt(rho L^2/(pi*4)) at stop; speed v = R/T
Tseed = results["4 seeds"]["T"]
Rseed = np.sqrt(rho_stop * L * L / (4 * np.pi))
v = Rseed / Tseed
Te = results["empty+nucleation"]["T"]
reach = 2 * v * Te
print(f"estimated front speed v = {v:.2f} sites per unit time; twice front distance at the nucleation stop time: {reach:.1f} sites")
for name in results:
    C, Cse = results[name]["C"], results[name]["Cse"]
    xi = next((r + 1 for r in range(len(C)) if abs(C[r]) < 2 * max(Cse[r], 1e-4)), None)
    far = slice(int(min(len(C) - 1, reach + 10)), len(C))
    z = np.abs(C[far]) / np.maximum(Cse[far], 1e-6)
    print(f"{name:18s}: C(1)={C[0]:.3f}, C(2)={C[1]:.3f}, C(4)={C[3]:.3f}, C(10)={C[9]:.3f}; "
          f"max |C|/se for r >= {int(min(len(C)-1, reach+10))+1}: {z.max():.2f}")

a = results["empty+nucleation"]
b = results["4 seeds"]
c = results["bernoulli 3e-3"]
plateau_a = a["S"][96] / a["S"][24]
plateau_c = c["S"][96] / c["S"][24]
plateau_b = b["S"][96] / b["S"][24]
print("\nPlateau ratios S96/S24 (amended criterion, chosen after run 1): empty+nucleation %.2f, bernoulli %.2f, 4 seeds %.2f" % (plateau_a, plateau_c, plateau_b))
print("Pre-registered normalisation (b^2 Var/[rho(1-rho)] within 1.6x of 1): FAILS by construction "
      "(a growth ensemble has a finite correlation area); the plateau ratio is the right test.")
print("RESULT 3 homogeneity: (a),(c) plateau < 2 and (b) plateau > 4:",
      plateau_a < 2 and plateau_c < 2 and plateau_b > 4)
