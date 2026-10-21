#!/usr/bin/env python3
"""Extended winding-gap fits (added at resumption). Reads data/winding_gap.json (written by analyze.py).
For V=0 it uses, for each L, the LARGEST projection time T available (T=2L unless a longer run exists), and also
reports the T=2L-only set. Models (weighted LSQ):
  pre-declared (WORKLOG 20:27): (C) A/L ; (S) A/L + sigma L ; (Str) sigma L only
  post hoc, labelled as such:   (Q) B/L^2 ; (K) constant c
Also refits the repo's guided-projector winding splittings (logs/runner-cache, ring_model_electric_coupling_..._2026_09_25)
as an external comparison (different algorithm and code; guide-dependent). Writes data/winding_fit2.json and prints."""
import json, os
import numpy as np

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
rows = json.load(open(os.path.join(base, "data", "winding_gap.json")))


def wls(L, y, s, cols):
    X = np.stack([c(L) for c in cols], axis=1)
    w = 1 / s ** 2
    M = (X * w[:, None]).T @ X
    cov = np.linalg.inv(M)
    p = cov @ (X * w[:, None]).T @ y
    chi2 = float((((y - X @ p) / s) ** 2).sum())
    return p.tolist(), np.sqrt(np.diag(cov)).tolist(), chi2, len(L) - len(cols)


MODELS = {"C: A/L": [lambda L: 1 / L], "S: A/L + sigma L": [lambda L: 1 / L, lambda L: L], "Str: sigma L": [lambda L: L],
          "Q (post hoc): B/L^2": [lambda L: 1 / L ** 2], "K (post hoc): const": [lambda L: 0 * L + 1]}


def fitall(L, y, s, tag):
    out = {"L": L.tolist(), "dE": y.tolist(), "err": s.tolist(), "fits": {}}
    print(f"--- {tag}: " + ", ".join(f"L={int(l)}: {a:.3f}({b:.3f})" for l, a, b in zip(L, y, s)))
    for name, cols in MODELS.items():
        if len(L) <= len(cols):
            continue
        p, e, chi2, dof = wls(L, y, s, cols)
        out["fits"][name] = {"p": p, "err": e, "chi2": chi2, "dof": dof}
        print(f"  {name:22s} p = " + ", ".join(f"{a:.4f}({b:.4f})" for a, b in zip(p, e)) + f"  chi2 = {chi2:.2f}/{dof}")
    return out


res = {}
for V in sorted({r["V"] for r in rows}):
    rs = [r for r in rows if r["V"] == V]
    Ls = sorted({r["L"] for r in rs})
    for mode in ("T=2L", "largest T"):
        sel = []
        for L in Ls:
            c = [r for r in rs if r["L"] == L and (abs(r["T"] - 2 * L) < 1e-9 if mode == "T=2L" else True)]
            if c:
                sel.append(max(c, key=lambda r: r["T"]))
        if len(sel) < 2:
            continue
        L = np.array([r["L"] for r in sel], float)
        y = np.array([r["dE"][0] for r in sel])
        s = np.array([r["dE"][1] for r in sel])
        tag = f"V={V} {mode} (T used: {[r['T'] for r in sel]})"
        res[tag] = fitall(L, y, s, tag)

# external comparison: repo guided projector (q=1 = one reversed line = our W=1), copied from the runner cache stdout
ext = {"L": [4, 6, 8], "dE": [0.7315, 0.3699, 0.1685], "err": [0.0084, 0.0198, 0.0443]}
res["repo guided projector V=0 (external, guide-dependent)"] = fitall(np.array(ext["L"], float), np.array(ext["dE"]),
                                                                     np.array(ext["err"]), "repo guided projector V=0")
json.dump(res, open(os.path.join(base, "data", "winding_fit2.json"), "w"), indent=1)
