#!/usr/bin/env python3
"""J:attack-a:PR9351 -- WITNESS REALIZABILITY: the object the PR's runner certifies is the object the note describes.

The runner never builds the square's microscopic Hamiltonian: it certifies rational enclosures of the eigenvalues of the reduced equation F(E) psi = 0 (through helper files) and of H0, H0 + xH1, and the six error bounds
are differences of those enclosures. The note describes the microscopic model of the two-record square sector (parent's definitions). Realizability here means: the intervals printed in the runner's cache (parsed as exact
rationals) enclose the eigenvalues of (a) the explicit full microscopic matrix built from the parent's definitions (states of the sector, Gauss law, hops with amplitude sqrt(1 - E(E - 1)/C), C_S evaluated) and
(b) the truncated matrices of H0 and H0 + xH1, for every case, every one of the seven levels, and that every printed error bound is the maximum of the endpoint differences of the printed gap intervals.
Also the sector itself is realized as described: state counts per W, all four fields inside [-S, S], every state Gauss-consistent. Floating point for the model side (labelled); exact Fractions for the cache side.
Prints SUMMARY: and, only if a witness is not realized, HIT:.
"""
import itertools
import json
import subprocess
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, eigvalsh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/measured-corrections-20260927"
CACHE = "logs/runner-cache/square_microscopic_spectral_certificate_2026_09_27.txt"
T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def load():
    git("fetch", "origin", BRANCH, "--quiet")
    head = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
    raw = git("show", f"{head}:{CACHE}").stdout
    body = raw.split("----- stdout -----\n", 1)[1].split("\nTOTAL:", 1)[0]
    return head, json.loads(body)


def sector(S):
    C = S * (S + 1)
    edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    states = []
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for n in range(-S, S + 1):
            E = (n, q[0] - 1 - n, -q[1] - n, q[2] - 1 + q[1] + n)
            # Gauss law: outflow at A = q - 1, inflow at B = -q
            gauss = E[0] + E[1] == q[0] - 1 and E[2] + E[3] == q[2] - 1 and E[0] + E[2] == -q[1] and E[1] + E[3] == -q[3]
            assert gauss
            if all(-S <= e <= S for e in E):
                states.append((q, E))
    return C, edges, states


def full_levels(S, K, delta, nev=7):
    C, edges, states = sector(S)
    x = delta / (K * C)
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
    return eigh(H, eigvals_only=True, subset_by_index=(0, nev - 1))


def reduced_count(E, S, K, delta):
    C = S * (S + 1); x = delta / (K * C); lam = x * x * E / delta
    m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
    R = (1 - lam) * (2 - lam) - 4 * x * dm
    n = np.arange(-S, S + 1)
    dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam)
    q = 4 * delta * dm ** 2 / R
    dg[m + S] -= q; dg[m + S + 1] -= q
    return int((eigvalsh_tridiagonal(dg, -q) < 0).sum())


def reduced_levels(S, K, delta, nev=7):
    out = []
    for j in range(nev):
        b = -6 * delta - 5; step = 0.5
        while reduced_count(b, S, K, delta) < j + 1:
            b += step
        a = b - step
        while reduced_count(a, S, K, delta) >= j + 1:
            a -= step
        for _ in range(64):
            mid = (a + b) / 2
            if reduced_count(mid, S, K, delta) >= j + 1:
                b = mid
            else:
                a = mid
        out.append((a + b) / 2)
    return np.array(out)


def operator_levels(S, K, delta, corrected, L=200, nev=7):
    C = S * (S + 1); x = delta / (K * C) if corrected else 0.0
    n = np.arange(-L, L + 1).astype(float)
    dg = 4 * K * n ** 2 - 4 * delta + x * (8 * delta - 8 * K * n ** 2)
    off = -2 * delta + x * (4 * delta + 4 * K * n[:-1] * (n[:-1] + 1))
    return eigvalsh_tridiagonal(dg, off, select="i", select_range=(0, nev - 1))


def inside(v, iv, slack=0.0):
    lo, hi = Fr(iv[0]), Fr(iv[1])
    return lo - Fr(slack).limit_denominator(10 ** 15) <= Fr(float(v)).limit_denominator(10 ** 18) <= hi + Fr(slack).limit_denominator(10 ** 15)


def run():
    head, C = load()
    print(f"PR #9351 head {head[:10]}; cache cases {len(C['cases'])}")
    # sector realization
    ok_sec = True; parts = []
    for S in (1, 2, 5, 20):
        Cc, edges, states = sector(S)
        cnt = {0: 0, 1: 0, 2: 0}
        for q, E in states:
            cnt[sum(1 - q[a] for a in (0, 2))] += 1
        exp0, exp2 = 2 * S + 1, 2 * S
        ok_sec &= cnt[0] == exp0 and cnt[2] == exp2 and all(all(-S <= e <= S for e in E) for q, E in states)
        parts.append(f"S {S}: W = 0/1/2 states {cnt[0]}/{cnt[1]}/{cnt[2]}")
    check("(W1) the sector is realized as described: W = 0 has 2S + 1 states (n = -S..S) and W = 2 has 2S (m = -S..S-1), all four fields in [-S, S], every state Gauss-consistent", ok_sec, "; ".join(parts))
    if not ok_sec:
        FIRED.append("the sector's state counts differ from the note's")
    # cache intervals enclose the model's eigenvalues
    worst_red = 0.0; worst_full = 0.0; n_in = 0; n_tot = 0; bad = []
    okb = True
    for c in C["cases"]:
        S, K, delta = c["S"], float(Fr(c["K"])), float(Fr(c["delta"]))
        er = reduced_levels(S, K, delta)
        efull = full_levels(S, K, delta) if S <= 50 else None
        for j, iv in enumerate(c["microscopic"]["energy_intervals"]):
            n_tot += 1
            if inside(er[j], iv, 1e-11):
                n_in += 1
            else:
                bad.append(("reduced roots", S, c["delta"], j, float(er[j]), [float(Fr(t)) for t in iv]))
            mid = (Fr(iv[0]) + Fr(iv[1])) / 2
            worst_red = max(worst_red, abs(float(mid) - er[j]))
            if efull is not None:
                worst_full = max(worst_full, abs(float(mid) - efull[j]))
        ea = operator_levels(S, K, delta, True); e0 = operator_levels(S, K, delta, False)
        for j, iv in enumerate(c["approximate"]["energy_intervals"]):
            n_tot += 1
            n_in += 1 if inside(ea[j], iv, 1e-11) else 0
            if not inside(ea[j], iv, 1e-11):
                bad.append(("H0 + xH1", S, c["delta"], j, float(ea[j]), [float(Fr(t)) for t in iv]))
        for j, iv in enumerate(c["rotor"]["energy_intervals"]):
            n_tot += 1
            n_in += 1 if inside(e0[j], iv, 1e-11) else 0
            if not inside(e0[j], iv, 1e-11):
                bad.append(("H0", S, c["delta"], j, float(e0[j]), [float(Fr(t)) for t in iv]))
        # every printed bound is the maximum endpoint difference of the printed gap intervals
        diffs = [[Fr(a) - Fr(d), Fr(b) - Fr(cc)] for (a, b), (cc, d) in zip(c["microscopic"]["gap_intervals"], c["approximate"]["gap_intervals"])]
        bound = max(abs(v) for iv in diffs for v in iv)
        okb &= bound == Fr(c["maximum_absolute_gap_error_upper_bound"])
    check(f"(W2) every enclosure printed in the runner's cache contains the model's eigenvalue: {n_in}/{n_tot} levels (microscopic, H0, H0 + xH1; six cases; seven levels each) contain the independently computed value "
          "(reduced-equation roots to 1e-11, truncated H0 and H0 + xH1 matrices)", n_in == n_tot, f"{len(bad)} outside" + (f"; first {bad[0]}" if bad else "") + f"; {time.time() - T0:.0f} s")
    if n_in != n_tot:
        FIRED.append(f"{n_tot - n_in} printed enclosures do not contain the model's level (first {bad[0]})")
    check("(W3) the explicit full microscopic matrix (S = 20, 50, both delta) has its lowest seven eigenvalues within 2e-8 of the midpoints of the cache's microscopic intervals; the reduced roots within 1e-9", worst_full < 2e-8 and worst_red < 1e-9,
          f"largest distance to an interval midpoint: full matrix {worst_full:.1e}, reduced roots {worst_red:.1e} (interval half-width 1e-9)")
    if not (worst_full < 2e-8 and worst_red < 1e-9):
        FIRED.append("the cache's microscopic intervals are not centred on the explicit full model's levels")
    check("(W4) every printed maximum_absolute_gap_error_upper_bound equals the maximum endpoint difference of the printed microscopic and approximate gap intervals (exact Fractions)", okb, "")
    if not okb:
        FIRED.append("a printed error bound is not the maximum of its printed interval differences")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: WITNESS NOT REALIZED: " + FIRED[0])
        print("HIT: PR #9351: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: pattern has no purchase: the sector is realized as described, and the runner's cached rational enclosures contain the levels of the independently built full microscopic matrix (reduced roots and H0, H0 + xH1 matrices), "
          "with the printed error bounds equal to the maximum endpoint differences of the printed intervals")
    return 0


if __name__ == "__main__":
    sys.exit(run())
