#!/usr/bin/env python3
"""Fits of the electric-winding gap dE(L) = E0(W=1) - E0(W=0) (mixed estimator, T = 2L) at each V:
  (C) Coulomb only:      dE = A / L
  (S) string + Coulomb:  dE = A / L + sigma * L
Weighted least squares; reports sigma with error and chi2. Writes data/winding_fit.json."""
import json, os
import numpy as np

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
rows = json.load(open(os.path.join(base, "data", "winding_gap.json")))
out = {}
for V in sorted({r["V"] for r in rows}):
    rs = sorted([r for r in rows if r["V"] == V and abs(r["T"] - 2 * r["L"]) < 1e-9], key=lambda r: r["L"])
    if len(rs) < 2:
        continue
    L = np.array([r["L"] for r in rs], float)
    y = np.array([r["dE"][0] for r in rs])
    s = np.array([r["dE"][1] for r in rs])
    w = 1 / s ** 2
    # Coulomb only
    X1 = (1 / L)[:, None]
    A1 = np.linalg.solve((X1 * w[:, None]).T @ X1, (X1 * w[:, None]).T @ y)
    chi1 = float((((y - X1 @ A1) / s) ** 2).sum())
    res = {"L": L.tolist(), "dE": y.tolist(), "err": s.tolist(),
           "coulomb_A": float(A1[0]), "coulomb_A_err": float(np.sqrt(1 / (w / L ** 2).sum())), "coulomb_chi2": chi1, "dof_c": len(L) - 1}
    if len(rs) >= 3:
        X2 = np.stack([1 / L, L], axis=1)
        M = (X2 * w[:, None]).T @ X2
        cov = np.linalg.inv(M)
        p = cov @ (X2 * w[:, None]).T @ y
        chi2 = float((((y - X2 @ p) / s) ** 2).sum())
        res.update({"A": float(p[0]), "A_err": float(np.sqrt(cov[0, 0])), "sigma": float(p[1]), "sigma_err": float(np.sqrt(cov[1, 1])),
                    "chi2": chi2, "dof": len(L) - 2})
    # pure string fit for comparison
    X3 = L[:, None]
    p3 = np.linalg.solve((X3 * w[:, None]).T @ X3, (X3 * w[:, None]).T @ y)
    res["string_only_sigma"] = float(p3[0])
    res["string_only_chi2"] = float((((y - X3 @ p3) / s) ** 2).sum())
    out[str(V)] = res
    print(V, json.dumps(res))
json.dump(out, open(os.path.join(base, "data", "winding_fit.json"), "w"), indent=1)
