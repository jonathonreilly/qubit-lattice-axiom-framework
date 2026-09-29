#!/usr/bin/env python3
"""J:attack-d:PR9351 -- QUANTIFIER SCOPE of the global spectral indexing of the square microscopic spectral certificate note.

Claim (note, "Exact reduction and global spectral indexing"): "Fix integer spin S >= 1, K, delta > 0 ... For physical trial energy E put lam = x^2 E/delta ... Require lam < 1 and (1 - lam)(2 - lam) > 4x.
Since 0 <= d_m <= 1 the entire eliminated Q block is positive ... Consequently the negative index of F(E) is the number of microscopic eigenvalues strictly below E in this fixed matter/charge sector."
The quantifier is over every integer S >= 1, every K, delta > 0 (so every x = delta/(K S(S+1)), not only x < 1/4) and every admissible E. The note's certificates test it only at the first seven levels of six cases. This script executes it
over the whole admissible interval E < E* (E* = the edge of {lam < 1, R_m(E) > 0 for all m}) for 8 spins x 8 couplings (x from 1e-5 up to 150), against the eigenvalues of the explicit full microscopic matrix (built here from the
parent's definitions: states, Gauss law, hop amplitudes sqrt(1 - E(E - 1)/C), C_S = 4 on W = 0), including test energies within 1e-7 (relative) of every eigenvalue below E*, and a control outside the admissible interval.
Floating point (labelled). Prints SUMMARY: and, only if the identity fails inside the admissible interval, HIT:.
"""
import itertools
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
from scipy.linalg import eigh, eigvalsh_tridiagonal

T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def full_matrix(S, K, delta):
    """H = delta eps^-4 [W + eps T + eps^2 C_S], eps^2 = x; two positive records on the 4-cycle A = {0,2}, B = {1,3}; C_S = 4 on W = 0 and 0 elsewhere (parent's definition, evaluated)."""
    C = S * (S + 1); x = delta / (K * C)
    edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    states = []
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for n in range(-S, S + 1):
            E = (n, q[0] - 1 - n, -q[1] - n, q[2] - 1 + q[1] + n)
            if all(-S <= e <= S for e in E):
                states.append((q, E))
    idx = {s: i for i, s in enumerate(states)}
    H = np.zeros((len(states), len(states)))
    for i, (q, E) in enumerate(states):
        W = sum(1 - q[a] for a in (0, 2))
        H[i, i] += delta / x ** 2 * W + (delta / x ** 2 * x * 4.0 if W == 0 else 0.0)
        for k, (a, b) in enumerate(edges):
            if q[a] == 1 and q[b] == 0:
                a2 = 1 - E[k] * (E[k] - 1) / C
                if a2 > 1e-14:
                    q2 = list(q); q2[a] = 0; q2[b] = 1; E2 = list(E); E2[k] -= 1
                    j = idx[(tuple(q2), tuple(E2))]
                    t = -delta / x ** 1.5 * np.sqrt(a2)
                    H[i, j] += t; H[j, i] += t
    return H, x


def reduced(E, S, K, delta):
    """The negative index of F(E) of the note (tridiagonal in n), or None outside the admissible set (lam >= 1 or some R_m <= 0)."""
    C = S * (S + 1); x = delta / (K * C); lam = x * x * E / delta
    m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
    R = (1 - lam) * (2 - lam) - 4 * x * dm
    if not (lam < 1 and R.min() > 0):
        return None
    n = np.arange(-S, S + 1)
    dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam)
    q = 4 * delta * dm ** 2 / R
    dg[m + S] -= q; dg[m + S + 1] -= q
    return int((eigvalsh_tridiagonal(dg, -q) < 0).sum())


def edge(S, K, delta):
    lo, hi = -1e3 * (1 + delta), 0.0
    C = S * (S + 1); x = delta / (K * C)
    top = delta / x ** 2 * (1 - 1e-12)
    if reduced(top, S, K, delta) is not None:
        return top
    lo = -10.0 * (1 + delta) * C
    if reduced(lo, S, K, delta) is None:
        return None
    hi = top
    for _ in range(200):
        mid = (lo + hi) / 2
        if reduced(mid, S, K, delta) is None:
            hi = mid
        else:
            lo = mid
    return lo


def run():
    K = 1.0
    Ss = (1, 2, 3, 5, 8, 13, 21, 34) if "--dry" not in sys.argv else (2, 5)
    ratios = (0.01, 0.1, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0) if "--dry" not in sys.argv else (0.1, 10.0)
    tested = bad = 0; first = None; cases = 0; near = 0; nodomain = []; xs = []
    for S in Ss:
        for r in ratios:
            delta = r * K
            H, x = full_matrix(S, K, delta)
            ev = eigh(H, eigvals_only=True)
            Es = edge(S, K, delta)
            xs.append(x)
            if Es is None:
                nodomain.append((S, r, x)); continue
            cases += 1
            scale = max(1.0, abs(ev[ev < Es]).max() if (ev < Es).any() else 1.0)
            pts = list(np.linspace(min(ev.min() - 3, Es - 1), Es, 260, endpoint=False)) + [Es - (Es - ev.min() + 3) * t for t in np.logspace(-9, -2, 40)]
            for e in ev[ev < Es]:
                for eps in (1e-7, 1e-6, 1e-4):
                    pts += [e - eps * scale, e + eps * scale]
            for E in pts:
                if E >= Es:
                    continue
                cf = reduced(E, S, K, delta)
                if cf is None:
                    continue
                d = np.min(np.abs(ev - E))
                if d < 2e-8 * scale:
                    continue
                ce = int((ev < E).sum()); tested += 1
                if abs(E - ev[np.argmin(np.abs(ev - E))]) < 2e-4 * scale:
                    near += 1
                if cf != ce:
                    bad += 1
                    if first is None:
                        first = (S, r, x, E, cf, ce)
    check(f"(Q1) over the whole admissible interval E < E* the negative index of F(E) equals the number of eigenvalues of the full matrix below E: {cases} (S, delta/K) cases with a nonempty interval "
          f"(x from {min(xs):.1e} to {max(xs):.1f}), {tested} test energies ({near} within 2e-4 of an eigenvalue), FLOATING POINT", bad == 0,
          f"{bad} mismatches" + (f"; first at S = {first[0]}, delta/K = {first[1]}, x = {first[2]:.3g}, E = {first[3]:.6g}: index {first[4]} vs count {first[5]}" if first else "")
          + f"; cases with an empty admissible interval (x too large for any real E): {len(nodomain)}; {time.time() - T0:.0f} s")
    if bad:
        FIRED.append(f"the count identity fails inside the admissible interval (S = {first[0]}, delta/K = {first[1]}, x = {first[2]:.3g}, E = {first[3]:.6g}: {first[4]} vs {first[5]})")
    # domain of the first-order operator and the low levels: the six cases' first seven levels are admissible
    okd = True; parts = []
    for delta, S in ((1.0, 20), (15803623 / 500000, 20), (1.0, 50), (15803623 / 500000, 50)):
        H, x = full_matrix(S, K, delta)
        ev = eigh(H, eigvals_only=True, subset_by_index=(0, 6))
        adm = all(reduced(e + s * 1e-9, S, K, delta) is not None for e in ev for s in (-1, 1))
        okd &= adm; parts.append(f"delta {delta:.6g} S {S}: E_0..E_6 admissible {adm}, x = {x:.4f}")
    check("(Q2) the seven levels of the note's certificates (and their +-1e-9 endpoints) lie inside the admissible interval (S = 20, 50, both delta)", okd, "; ".join(parts))
    if not okd:
        FIRED.append("a certificate endpoint lies outside the admissible interval")
    # control: just above the edge the criterion (R_m > 0) fails and F is not defined; and with R_m <= 0 forced, the index is not the count (the conditions are needed)
    S, delta = 5, 3.0
    H, x = full_matrix(S, K, delta); ev = eigh(H, eigvals_only=True)
    Es = edge(S, K, delta)
    C = S * (S + 1)

    def index_forced(E):
        lam = x * x * E / delta; m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
        R = (1 - lam) * (2 - lam) - 4 * x * dm
        n = np.arange(-S, S + 1)
        dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam); q = 4 * delta * dm ** 2 / R
        dg[m + S] -= q; dg[m + S + 1] -= q
        return int((eigvalsh_tridiagonal(dg, -q) < 0).sum())
    Eabove = Es + 0.4 * (delta / x ** 2 - Es) if Es < delta / x ** 2 else Es * 1.0001
    ctrl = reduced(Eabove, S, K, delta) is None and index_forced(Eabove) != int((ev < Eabove).sum())
    check("(control) outside the admissible interval the criterion R_m > 0 fails and the formal index differs from the eigenvalue count (S = 5, delta = 3): the conditions are needed and the test can fail", ctrl,
          f"E* = {Es:.4g}; at E = {Eabove:.4g}: formal index {index_forced(Eabove)}, eigenvalues below {int((ev < Eabove).sum())}")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: SCOPE FAILS: " + FIRED[0])
        print("HIT: PR #9351 quantifier scope: " + "; ".join(FIRED))
        sys.exit(1)
    print("SUMMARY: pattern has no purchase on the indexing claim: inside the whole admissible interval, for every tested integer spin S = 1..34 and every coupling ratio delta/K = 0.01..300 (x up to " + f"{max(xs):.0f}" + "), the negative index of F(E) equals "
          "the number of eigenvalues of the explicit full matrix strictly below E; the note's admissibility conditions are exactly what makes it hold (control), and the certificates' endpoints are admissible")


if __name__ == "__main__":
    run()
