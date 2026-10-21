#!/usr/bin/env python3
"""Thermodynamic-integration estimator of the winding free-energy gap (declared in WORKLOG 03:40):
  ln[Z_S1/(2 Z_S0)](beta) = ln[P1/(2P0)](beta_min) - int_{beta_min}^{beta} (E_S1 - E_S0) dbeta'
S0 = {W_a = 0}, S1 = {|W_a| = 1}, pooled over a = x,y,z.  dF1(beta) = -(1/beta) ln[Z_S1/(2 Z_S0)].
Errors: delete-one-bin jackknife over 20 time bins (all betas of a run share the bins: PT time).
usage: ti.py TAG [TAG...]  (runs combined: mean, error = max(jackknife-combined, seed scatter))"""
import os, sys, json
import numpy as np
from scipy.interpolate import CubicSpline
QUAD = os.environ.get('TI_QUAD', 'spline')

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from analyze import load

NB = 20
DISCARD = 0.2


def sums(tag):
    d = load(tag)
    m = d["m"][int(DISCARD * len(d["m"])):]
    k = {n: i for i, n in enumerate(d["keys"])}
    E = m[:, :, k["E"]]
    W = m[:, :, [k["Wx"], k["Wy"], k["Wz"]]]
    n = len(m) // NB
    E = E[: n * NB].reshape(NB, n, -1)
    W = W[: n * NB].reshape(NB, n, -1, 3)
    c0 = (W == 0)
    c1 = (np.abs(W) == 1)
    # per bin, per beta: counts and energy sums (pooled over directions)
    S = {"n0": c0.sum(axis=(1, 3)), "n1": c1.sum(axis=(1, 3)),
         "e0": (E[..., None] * c0).sum(axis=(1, 3)), "e1": (E[..., None] * c1).sum(axis=(1, 3)),
         "ntot": np.full((NB, E.shape[2]), 3 * n)}
    return d["betas"], S, d


def estimate(betas, S):
    n0, n1, e0, e1, nt = (S[x].sum(0) for x in ("n0", "n1", "e0", "e1", "ntot"))
    with np.errstate(divide="ignore", invalid="ignore"):
        dE = e1 / n1 - e0 / n0
        lr0 = np.log((n1[0] / nt[0]) / (2 * n0[0] / nt[0]))
    # cumulative trapezoid from beta_min
    if QUAD == "trap" or not np.all(np.isfinite(dE)):
        integ = np.concatenate([[0.0], np.cumsum(0.5 * (dE[1:] + dE[:-1]) * np.diff(betas))])
    else:
        cs = CubicSpline(betas, dE)
        integ = np.array([cs.integrate(betas[0], x) for x in betas])
    lnr = lr0 - integ
    dF = -lnr / betas
    direct = np.full_like(betas, np.nan)
    with np.errstate(divide="ignore", invalid="ignore"):
        direct = -np.log((n1 / nt) / (2 * n0 / nt)) / betas
    return dF, direct, dE


def jack(betas, S):
    full = estimate(betas, S)
    js = []
    for i in range(NB):
        Si = {k: np.delete(v, i, axis=0) for k, v in S.items()}
        js.append(estimate(betas, Si))
    out = []
    for q in range(3):
        J = np.array([j[q] for j in js])
        err = np.sqrt((NB - 1) / NB * np.nansum((J - np.nanmean(J, 0)) ** 2, axis=0))
        out.append((full[q], err))
    return out


def main(tags, report_betas=None):
    per = []
    for t in tags:
        b, S, d = sums(t)
        res = jack(b, S)
        per.append((t, b, res, S, d["trips"]))
    b = per[0][1]
    out = {}
    rb = report_betas if report_betas else b
    for bt in rb:
        i = int(np.argmin(np.abs(b - bt)))
        rows = []
        for t, bb, res, S, trips in per:
            rows.append((res[0][0][i], res[0][1][i], res[1][0][i], res[1][1][i], int(S["n1"][:, i].sum()), trips))
        mu = np.mean([r[0] for r in rows])
        eb = np.sqrt(np.sum([r[1] ** 2 for r in rows])) / len(rows)
        es = np.std([r[0] for r in rows], ddof=1) / np.sqrt(len(rows)) if len(rows) > 1 else 0
        md = np.nanmean([r[2] for r in rows])
        ebd = np.sqrt(np.nansum([r[3] ** 2 for r in rows])) / len(rows)
        esd = np.nanstd([r[2] for r in rows], ddof=1) / np.sqrt(len(rows)) if len(rows) > 1 else 0
        out[float(b[i])] = {"dF1_TI": (float(mu), float(max(eb, es))), "dF1_direct": (float(md), float(max(ebd, esd))),
                            "per_run": rows}
        print(f"beta={b[i]:.4g}: dF1_TI = {mu:.4f} +- {max(eb, es):.4f}   dF1_direct = {md:.4f} +- {max(ebd, esd):.4f}   "
              + " | ".join(f"{t}: TI {r[0]:.4f}({r[1]:.4f}) dir {r[2]:.4f}({r[3]:.4f}) nS1={r[4]} trips={r[5]}"
                           for (t, *_), r in zip(per, rows)))
    return out


if __name__ == "__main__":
    main(sys.argv[1:])
