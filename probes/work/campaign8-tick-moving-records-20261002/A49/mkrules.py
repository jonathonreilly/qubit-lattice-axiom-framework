"""A49 mkrules: collect the lowest-variance rule vectors of the parton (lam'=0) into rules.npz (23-dim, basis order of
anal49) for the forward test: 16-site exact minimizers (S1, S1uS2-complement-free S1inv) and the VMC minimizers at
6^3 / 8^3 (S1, S1inv).  Also prints <H(c)>/site of the parton and of the references at 6^3 for both signs."""
import sys, signal, numpy as np
signal.alarm(120)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal49 import names, SETS, BINV, G, releig, n
res = np.load("anal49_res.npy", allow_pickle=True)[0]
D = np.load("ed16_C.npz")
rules = {}
for w in ("S1", "S1inv"):
    C = D["C_lp0.0"]; G16 = D["G"]
    if w in SETS:
        s = SETS[w]; lam, V = releig(C[np.ix_(s, s)], G16[np.ix_(s, s)]); c = np.zeros(n); c[s] = V[:, 0]
    else:
        B = BINV[w]; lam, V = releig(B.T @ C @ B, B.T @ G16 @ B); c = B @ V[:, 0]
    rules[f"ed16_{w}"] = c / np.sqrt(c @ G @ c)
for (L, spec), r in res.items():
    if spec != "lp:0": continue
    for w in ("S1", "S1inv"):
        if w not in r: continue
        v = r[w][3]
        if w in SETS:
            c = np.zeros(n); c[SETS[w]] = v
        else:
            c = BINV[w] @ v
        rules[f"vmc{L}_{w}"] = c / np.sqrt(c @ G @ c)
for k, c in rules.items():
    print(f"{k:12s}: " + " ".join(f"{nm}:{x:+.3f}" for nm, x in zip(names, c) if abs(x) > 0.02))
np.savez("rules.npz", **rules)
# 16-site exact values in the (fixed) dual-SU(2)-invariant subspaces, all saved states
G16 = D["G"]
print("16-site exact, invariant subspaces (lowest, 2nd):")
for key in [k for k in D.files if k.startswith("C_")]:
    C = D[key]; line = f"  {key[2:]:12s}"
    for w in ("S1inv", "S1uS2inv"):
        B = BINV[w]; lam = releig(B.T @ C @ B, B.T @ G16 @ B)[0]; line += f" | {w}: {lam[0]:.4g}, {lam[1]:.4g}"
    print(line)
# energies per site of the minimizing rules at 6^3 for the parton and the references (invariant combos only)
import glob
from a49lib import pack
for L in (6, 8):
    for lab in (f"vmc{L}_S1inv",):
        if lab not in rules: continue
        c = rules[lab]
        for spec in ("lp:0", "lp:0.1", "neez:0.05", "colz:0.1"):
            fs = sorted(glob.glob(f"s49_{L}_{spec}_*.npy"))
            if not fs: continue
            S = np.concatenate([np.load(f) for f in fs]); E = (S[:, :n].real @ c) / L ** 3
            from a46lib import binerr
            m, e = binerr(E)
            print(f"  L={L} rule {lab}: <H(c)>/site in {spec:10s} = {m:+.5f} +- {e:.5f}")
