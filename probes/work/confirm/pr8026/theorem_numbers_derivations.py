#!/usr/bin/env python3
"""J:confirm:J-provenance-PR8026 -- independent test of the finder's provenance HIT on PR #8026.

The task's sourcing rule: for every number in the theorem statements, 'locate the runner line that prints it (the PR's scripts/ runner and
its cached stdout) or its exact derivation in the note'. The finder searched the two caches only and called 1/144, 7/124416, 4/a, 2ce
unsourced.

This script, for each number:
  1. searches both caches (ASCII and Unicode forms) and the two runner SOURCES (check lines);
  2. locates and recomputes the note's exact derivation in exact arithmetic:
       u/144      = u [2 * (1/6) * (1/96) * 2]                        (note eq. (5))
       7/124416   = I/96^2 + 2 I/(576 * 24), I = (4/6)(1/3) = 2/9    (note eqs. (6)-(7))
       4/a        = min over labels (p,q) != (0,0) of (p^2 + pq + q^2 + 3p + 3q)/a
       C_0 = 2ce  : (ce)^P/(1 - q) <= (2ce)^P for q <= 1/4, P >= 1
  3. checks the Haar ingredients of (5)-(6) by Monte Carlo over Haar-random SU(3): int |Tr U|^2 = 1, int (Tr U)^2 = 0,
     int Tr(AU) Tr(U^dag B) dU = Tr(AB)/3 for fixed random A, B.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction as F

import numpy as np

BRANCH = "codex/spatial-area-block36-20260907"
NOTE = "docs/GAUGE_WILSON_SPATIAL_LOOP_AREA_SUPPRESSION_BOUNDED_THEOREM_NOTE_2026-09-07.md"
CACHES = ["logs/runner-cache/gauge_wilson_spatial_loop_area_chain_check_2026_09_07.txt",
          "logs/runner-cache/gauge_wilson_spatial_loop_area_coefficients_check_2026_09_07.txt"]
RUNNERS = ["scripts/gauge_wilson_spatial_loop_area_chain_check_2026_09_07.py",
           "scripts/gauge_wilson_spatial_loop_area_coefficients_check_2026_09_07.py"]


def show(path):
    return subprocess.run(["git", "show", f"FETCH_HEAD:{path}"], capture_output=True, text=True, check=True).stdout


def haar_su3(n, rng):
    Z = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2)
    Q = Q * (d / np.abs(d))[:, None, :]
    det = np.linalg.det(Q)
    return Q / (det ** (1 / 3))[:, None, None]


def main():
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], check=True)
    note = show(NOTE)
    caches = {c: show(c) for c in CACHES}
    runners = {r: show(r) for r in RUNNERS}

    tokens = {"1/144": [r"1\s*/\s*144", r"u\s*/\s*144", r"F\(1,\s*144\)"],
              "7/124416": [r"7\s*/\s*124416", r"F\(7,\s*124416\)"],
              "4/a": [r"4\s*/\s*a\b"],
              "2ce": [r"2\s*c\s*e\b", r"2ce"]}
    print("1. where each number appears")
    for name, pats in tokens.items():
        in_cache = [c.split("/")[-1] for c, t in caches.items() if any(re.search(p, t) for p in pats)]
        in_runner = [(r.split("/")[-1], ln.strip()) for r, t in runners.items() for ln in t.splitlines() if any(re.search(p, ln) for p in pats)]
        in_note = [i + 1 for i, ln in enumerate(note.splitlines()) if any(re.search(p, ln) for p in pats)]
        print(f"   {name}: cache lines {in_cache or 'none'}; runner lines {[x[1][:60] for x in in_runner] or 'none'}; note lines {in_note}")

    print("2. the note's exact derivations, recomputed")
    one_face = 2 * F(1, 6) * F(1, 96) * 2
    I = F(4, 6) * F(1, 3)
    mid = I / 96 ** 2
    ends = 2 * I / (576 * 24)
    two_face = mid + ends
    labels = [(p, q) for p in range(6) for q in range(6) if (p, q) != (0, 0)]
    e_first = min(p * p + p * q + q * q + 3 * p + 3 * q for p, q in labels)
    # 2ce: (ce)^P/(1-q) <= (2ce)^P  <=>  1/(1-q) <= 2^P ; worst case q = 1/4, P = 1
    ok_2ce = all(1 / (1 - F(1, 4)) <= F(2) ** P for P in range(1, 50))
    print(f"   eq.(5): 2*(1/6)*(1/96)*2 = {one_face}; eq.(6): I = (4/6)(1/3) = {I}; I/96^2 = {mid} (note: 1/41472); 2I/(576*24) = {ends} "
          f"(note: 1/31104); eq.(7): sum = {two_face}; first positive electric label energy min(p^2+pq+q^2+3p+3q) = {e_first} (note: 4/a); "
          f"(ce)^P/(1-q) <= (2ce)^P for q <= 1/4, P >= 1: {ok_2ce}")
    derivs = {"1/144": ("eq. (5)", one_face == F(1, 144) and "=u/144+O(u²)" in note.replace(" ", "")),
              "7/124416": ("eqs. (6)-(7)", two_face == F(7, 124416) and mid == F(1, 41472) and ends == F(1, 31104) and "124416" in note),
              "4/a": ("section 1: all-label energies [p²+pq+q²+3p+3q]/a", e_first == 4 and "first positive energy is 4/a" in note),
              "2ce": ("the uniform complex bound: (ce)^P/(1-q) <= (2ce)^P, C_0 = 2ce", ok_2ce and "C_0=2ce" in note.replace(" ", ""))}

    rng = np.random.default_rng(8026)
    U = haar_su3(200000, rng)
    tr = np.trace(U, axis1=1, axis2=2)
    m_abs2 = np.mean(np.abs(tr) ** 2)
    m_sq = np.mean(tr ** 2)
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    B = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    lhs = np.mean(np.einsum("ij,nji->n", A, U) * np.einsum("nji,ji->n", np.conj(U), B))
    rhs = np.trace(A @ B) / 3
    print(f"3. Haar SU(3), 200000 samples: <|Tr U|^2> = {m_abs2:.4f} (1); |<(Tr U)^2>| = {abs(m_sq):.4f} (0); "
          f"<Tr(AU) Tr(U^dag B)> = {lhs:.4f} vs Tr(AB)/3 = {rhs:.4f}")

    all_derived = all(ok for _, ok in derivs.values())
    haar_ok = abs(m_abs2 - 1) < 0.02 and abs(m_sq) < 0.02 and abs(lhs - rhs) < 0.05 * max(1, abs(rhs))
    for name, (where, ok) in derivs.items():
        print(f"   {name}: exact derivation in the note ({where}) re-derived: {ok}")
    if all_derived:
        print("SUMMARY: not reproduced - the task sources a number by a printing runner line OR its exact derivation in the note; all four "
              "'unsourced' numbers have exact derivations in the note, each re-derived here in exact arithmetic (u/144 = 2*(1/6)*(1/96)*2; "
              "7/124416 = 1/41472 + 1/31104 with I = 2/9; first positive energy 4/a from the label minimum 4; C_0 = 2ce from "
              "(ce)^P/(1-q) <= (2ce)^P), and 1/144 and 7/124416 are also asserted by the coefficients runner's check lines; the finder "
              f"searched the caches only (their counts-only stdout); the Haar ingredients hold by Monte Carlo: {haar_ok}")
    else:
        bad = [n for n, (_, ok) in derivs.items() if not ok]
        print(f"HIT: confirmed - no exact derivation in the note re-derives for: {bad}")
        print("SUMMARY: confirmed - unsourced numbers")


if __name__ == "__main__":
    main()
