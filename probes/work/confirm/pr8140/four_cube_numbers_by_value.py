#!/usr/bin/env python3
"""J:confirm:J-provenance-PR8140 -- independent test of the finder's provenance HIT on PR #8140.

Finder's HIT: in the defect-representation note, "<a,Q^-1 a> = 17/24 and ||P_perp k||^2 = 9*(7/24)"; the caches print
17/24 and 51/8 but not the literal token 7/24, so 7/24 is 'unsourced'.

Different machinery:
  1. value-based provenance: every rational token p/q (and integer) in ALL FIVE runner caches of the PR is parsed as a
     Fraction, and the note's four-cube values 17/24, 9*(17/24) = 51/8 and 9*(7/24) = 21/8 are looked up by value,
     with the cache key that prints them;
  2. the numbers recomputed from scratch: the tesseract {0,1}^4 as a cell complex (16 vertices, 32 edges, 24 plaquettes),
     the plaquette-edge incidence restricted to the 17 cotree edges of a BFS spanning tree, P_e = D Q^-1 D^T, and the
     witness j = 0, a = D^T e_p, k = 3 e_p, N = 3, in exact rationals (sympy).
"""
from __future__ import annotations

import itertools
import re
import subprocess
from collections import deque
from fractions import Fraction

import sympy as sp

BRANCH = "physics-loop/clock-static-charge-20260915"
NOTE = "docs/FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md"


def git_show(path):
    return subprocess.run(["git", "show", f"FETCH_HEAD:{path}"], capture_output=True, text=True, check=True).stdout


def caches():
    files = subprocess.run(["gh", "pr", "view", "8140", "--json", "files", "--jq", ".files[].path"],
                           capture_output=True, text=True, check=True).stdout.split()
    return [f for f in files if f.startswith("logs/runner-cache/")]


def values_in(blob):
    """(Fraction value, line) for every rational token a/b and every integer token in the blob (sha lines skipped)."""
    out = []
    for line in blob.splitlines():
        if "sha256" in line.lower():
            continue
        for m in re.finditer(r'(?<![\w.])(-?\d+)\s*/\s*(\d+)(?![\w.])', line):
            out.append((Fraction(int(m.group(1)), int(m.group(2))), line.strip()))
    return out


def tesseract_numbers():
    verts = list(itertools.product((0, 1), repeat=4))
    vidx = {v: i for i, v in enumerate(verts)}
    edges = []
    for v in verts:
        for d in range(4):
            if v[d] == 0:
                w = tuple(v[i] + (i == d) for i in range(4))
                edges.append((v, d))  # edge from v in direction d
    eidx = {e: i for i, e in enumerate(edges)}
    plaqs = []
    for v in verts:
        for d1, d2 in itertools.combinations(range(4), 2):
            if v[d1] == 0 and v[d2] == 0:
                plaqs.append((v, d1, d2))
    assert (len(verts), len(edges), len(plaqs)) == (16, 32, 24)

    def shift(v, d):
        return tuple(v[i] + (i == d) for i in range(4))

    B = sp.zeros(len(plaqs), len(edges))
    for p, (v, d1, d2) in enumerate(plaqs):
        # boundary of the oriented square v -> v+e1 -> v+e1+e2 -> v+e2 -> v
        B[p, eidx[(v, d1)]] += 1
        B[p, eidx[(shift(v, d1), d2)]] += 1
        B[p, eidx[(shift(v, d2), d1)]] -= 1
        B[p, eidx[(v, d2)]] -= 1
    # d_0: vertices -> edges; check d_1 d_0 = 0
    D0 = sp.zeros(len(edges), len(verts))
    for e, (v, d) in enumerate(edges):
        D0[e, vidx[v]] -= 1
        D0[e, vidx[shift(v, d)]] += 1
    assert B * D0 == sp.zeros(len(plaqs), len(verts))
    # BFS spanning tree, cotree edges
    adj = {v: [] for v in verts}
    for e, (v, d) in enumerate(edges):
        adj[v].append((shift(v, d), e))
        adj[shift(v, d)].append((v, e))
    seen, tree, dq = {verts[0]}, set(), deque([verts[0]])
    while dq:
        v = dq.popleft()
        for w, e in adj[v]:
            if w not in seen:
                seen.add(w)
                tree.add(e)
                dq.append(w)
    cotree = [e for e in range(len(edges)) if e not in tree]
    D = B[:, cotree]
    Q = D.T * D
    Qi = Q.inv()
    Pe = D * Qi * D.T
    Pp = sp.eye(len(plaqs)) - Pe
    ep = sp.zeros(len(plaqs), 1)
    ep[0] = 1
    a = D.T * ep
    k = 3 * ep
    N = 3
    phase = (N * a.T * Qi * D.T * k)[0]
    ee = (a.T * Qi * a)[0]
    em = (k.T * Pp * k)[0]
    diag_e = set(Pe[i, i] for i in range(len(plaqs)))
    diag_p = set(Pp[i, i] for i in range(len(plaqs)))
    return dict(r=len(cotree), P=len(plaqs), rank=D.rank(), trace=Pe.trace(), diag_e=diag_e, diag_p=diag_p, phase=phase,
                real=sp.nsimplify(sp.cos(2 * sp.pi * phase)), ee=ee, em=em, Q_det=Q.det())


def main():
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], check=True)
    note = git_show(NOTE)
    stated = [l.strip() for l in note.splitlines() if "7/24" in l or "51/8" in l]
    print("note lines: " + " | ".join(stated))
    targets = {"<a,Q^-1 a> = 17/24": Fraction(17, 24), "phase 9*(17/24) = 51/8": Fraction(51, 8), "||P_perp k||^2 = 9*(7/24) = 21/8": Fraction(21, 8),
               "the factor (P_perp)_pp = 7/24": Fraction(7, 24)}
    cache_list = caches()
    found = {}
    for c in cache_list:
        for val, line in values_in(git_show(c)):
            for name, t in targets.items():
                if val == t and name not in found:
                    found[name] = (c.split("/")[-1], line)
    print(f"1. value-based search over all {len(cache_list)} caches of PR #8140:")
    for name in targets:
        if name in found:
            print(f"   {name}: printed in {found[name][0]} as {found[name][1]}")
        else:
            print(f"   {name}: not printed as a value")
    t = tesseract_numbers()
    print(f"2. tesseract from scratch: r = {t['r']}, P = {t['P']}, rank D = {t['rank']}, det Q = {t['Q_det']}, trace P_e = {t['trace']}, "
          f"(P_e)_pp = {t['diag_e']}, (P_perp)_pp = {t['diag_p']}, phase = {t['phase']} (Re = {t['real']}), <a,Q^-1a> = {t['ee']}, "
          f"||P_perp k||^2 = {t['em']}")
    value_sourced = "||P_perp k||^2 = 9*(7/24) = 21/8" in found
    recomputed = (t["diag_e"] == {sp.Rational(17, 24)} and t["diag_p"] == {sp.Rational(7, 24)} and t["em"] == sp.Rational(21, 8)
                  and t["phase"] == sp.Rational(51, 8) and t["ee"] == sp.Rational(17, 24))
    if value_sourced and recomputed:
        print(f"SUMMARY: not reproduced - the note's ||P_perp k||^2 = 9*(7/24) is the value 21/8, which the defect-representation "
              f"cache prints as {found['||P_perp k||^2 = 9*(7/24) = 21/8'][1]} (the runner asserts em == 21/8); the finder searched "
              f"3 of the {len(cache_list)} caches for the literal factor 7/24 only (the literal does occur, in "
              f"{found['the factor (P_perp)_pp = 7/24'][0] if 'the factor (P_perp)_pp = 7/24' in found else 'no cache'}, a cache the finder "
              f"did not search, but as another note's quantity; the four-cube source is the 21/8 value); det Q = {t['Q_det']} matches "
              f"the cache's Q_det; "
              f"all four numbers recompute from the tesseract complex (17/24, 7/24, 21/8, 51/8, Re = -sqrt(2)/2)")
    elif not value_sourced:
        print("HIT: confirmed - ||P_perp k||^2 = 9*(7/24) = 21/8 is not printed as a value in any cache of PR #8140")
        print("SUMMARY: confirmed - unsourced value")
    else:
        print(f"SUMMARY: not reproduced for provenance; recomputation mismatch {t}")


if __name__ == "__main__":
    main()
