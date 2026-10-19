#!/usr/bin/env python3
"""Production analysis against the criteria pre-declared in WORKLOG.md (01:32 and 03:35 entries).
usage: analyze_prod.py L1 L2 ...  -> prints report, writes data/summary_prod.json"""
import os, sys, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from analyze import load, derived

NB = 20
DISCARD = 0.2


def bins(x, nb=NB):
    n = len(x) // nb
    return x[: n * nb].reshape((nb, n) + x.shape[1:]).mean(1)


def jack(binned_fn, arrays):
    """arrays: list of (nb, ...) binned arrays; binned_fn maps means -> scalar. jackknife mean/error."""
    nb = arrays[0].shape[0]
    full = binned_fn(*[a.mean(0) for a in arrays])
    js = []
    for i in range(nb):
        m = [np.delete(a, i, axis=0).mean(0) for a in arrays]
        js.append(binned_fn(*m))
    js = np.array(js)
    return full, np.sqrt((nb - 1) / nb * ((js - js.mean()) ** 2).sum())


def run_est(tag, bsel):
    d = load(tag)
    if d is None:
        return None
    m = d["m"][int(DISCARD * len(d["m"])):]
    der = derived(m, d["keys"])
    betas = list(np.round(d["betas"], 6))
    out = {"tag": tag, "trips": d["trips"], "nmeas": len(m), "nsw": d["nsw"], "swap_min": float(d["swap"].min()),
           "beta": {}}
    for b in bsel:
        if round(b, 6) not in betas:
            continue
        i = betas.index(round(b, 6))
        r = {}
        for q in ("E", "W2", "Nc", "S1", "S2", "P0", "P1"):
            if q not in der:
                continue
            bb = bins(der[q][:, i])
            r[q] = (float(bb.mean()), float(bb.std(ddof=1) / np.sqrt(NB)))
        P0b = bins(der["P0"][:, i])
        P1b = bins(der["P1"][:, i])

        def dF(p0, p1, b=b):
            if p1 <= 0:
                return np.nan
            return -np.log(p1 / (2 * p0)) / b

        r["dF1"] = tuple(float(x) for x in jack(dF, [P0b, P1b]))
        r["n_W_nonzero_frac"] = float((der["P0"][:, i] < 1).mean())
        out["beta"][float(b)] = r
    return out


def combine(runs, b, q):
    vals = [(r["beta"][b][q][0], r["beta"][b][q][1]) for r in runs if b in r["beta"] and q in r["beta"][b]]
    if not vals:
        return None
    mu = np.array([v[0] for v in vals])
    se = np.array([v[1] for v in vals])
    m = mu.mean()
    e_b = np.sqrt((se ** 2).sum()) / len(mu)
    e_s = mu.std(ddof=1) / np.sqrt(len(mu)) if len(mu) > 1 else 0.0
    return float(m), float(max(e_b, e_s)), vals


def main():
    Ls = [int(x) for x in sys.argv[1:]]
    res = {}
    for L in Ls:
        bsel = [L / 2, float(L), 8.0]
        seeds = [int(x) for x in os.environ.get("SEEDS", "1,2,3,4").split(",")]
        runs = [r for r in (run_est(f"L{L}_s{s}", bsel) for s in seeds) if r is not None]
        if not runs:
            continue
        res[L] = {"runs": runs, "comb": {}}
        print(f"=== L={L}: runs " + ", ".join(f"{r['tag']}(trips={r['trips']}, nmeas={r['nmeas']}, sw={r['nsw']}, minswap={r['swap_min']:.2f})" for r in runs))
        for b in sorted(set(bsel)):
            if not all(b in r["beta"] for r in runs):
                continue
            res[L]["comb"][b] = {}
            line = f"  beta={b:g}:"
            for q in ("E", "W2", "P1", "dF1", "S1", "S2", "Nc"):
                c = combine(runs, b, q)
                if c is None:
                    continue
                res[L]["comb"][b][q] = c[:2]
                per = " / ".join(f"{v[0]:.5g}({v[1]:.2g})" for v in c[2])
                line += f"\n     {q:4s} = {c[0]:.6g} +- {c[1]:.2g}   [per run: {per}]"
                if len(c[2]) >= 2:
                    (a, ea), (bb_, eb) = c[2][0], c[2][1]
                    z = (a - bb_) / np.sqrt(ea ** 2 + eb ** 2) if ea + eb > 0 else 0
                    line += f"  start-diff z={z:+.2f}"
            print(line)
    json.dump({str(k): v for k, v in res.items()}, open(os.path.join(HERE, "..", "data", "summary_prod.json"), "w"),
              indent=1, default=float)
    # criteria
    print("\n=== criteria (beta = L) ===")
    pts = []
    for L in Ls:
        if L in res and float(L) in res[L]["comb"]:
            c = res[L]["comb"][float(L)]
            eq_trips = all(r["trips"] >= 10 for r in res[L]["runs"])
            print(f"L={L}: K=<W^2>={c['W2'][0]:.4g}+-{c['W2'][1]:.2g}  dF1={c['dF1'][0]:.4g}+-{c['dF1'][1]:.2g}  "
                  f"a=L*dF1={L * c['dF1'][0]:.4g}+-{L * c['dF1'][1]:.2g}  S1={c['S1'][0]:.4g}+-{c['S1'][1]:.2g}  trips>=10: {eq_trips}")
            pts.append((L, L * c["dF1"][0], L * c["dF1"][1], c["W2"][0], c["W2"][1], c["S1"][0], c["S1"][1]))
    if len(pts) >= 2:
        P = np.array(pts)
        x, y, e = P[:, 0], P[:, 1], P[:, 2]
        w = 1 / e ** 2
        A = np.vstack([np.ones_like(x), x]).T
        cov = np.linalg.inv(A.T @ (A * w[:, None]))
        coef = cov @ (A.T @ (w * y))
        chi2 = float((((A @ coef) - y) ** 2 * w).sum())
        print(f"fit a(L) = a0 + s L: a0={coef[0]:.4g}+-{np.sqrt(cov[0, 0]):.2g}  s={coef[1]:.4g}+-{np.sqrt(cov[1, 1]):.2g}  chi2={chi2:.2f}/{len(x) - 2}")
        L1, L2 = P[-2, 0], P[-1, 0]
        S1a, S1b, e1, e2 = P[-2, 5], P[-1, 5], P[-2, 6], P[-1, 6]
        p = np.log(S1a / S1b) / np.log(L2 / L1)
        ep = np.sqrt((e1 / S1a) ** 2 + (e2 / S1b) ** 2) / np.log(L2 / L1)
        print(f"S_T exponent p from L={L1:g},{L2:g}: p={p:.3f}+-{ep:.3f}")
        print(f"K ratio K(L={L2:g})/K(L={L1:g}) = {P[-1, 3] / P[-2, 3]:.3f}")


if __name__ == "__main__":
    main()
