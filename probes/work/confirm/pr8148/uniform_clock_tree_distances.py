#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8148 - independent test of the finder's HIT on block 14 (PR #8148): 'the stated uniform distances 1/216
(path of 3) and 56059/3369600 (four-leaf star) match neither the TV nor the max-norm of uniform vs static at (3,1,2)'.

Different machinery and a different reading from the finder's:
  * the note is read at its PR branch: R3 and D1-D2 say 'the uniform law differs ... uniform at distance 1/216 on the path and
    56059/3369600 on the star', where 'the uniform law' is the note's clock law lambda = 1 (every unrecorded site at rate 1, so the
    formation order is a uniformly random permutation) - not the uniform distribution on configurations, which is what the finder
    compared;
  * the uniform clock law is computed as the exact average over all n! orders of the sequential (records-only) laws, each order's law
    being w(s)/D_sigma(s) with w the static weight and D_sigma the product of the site normalizers (a representation the finder did
    not use), and the seeded law by exact enumeration of connected growth histories;
  * total variation to the static law, exact rationals.
Prints 'HIT: confirmed - ...' if the note's numbers fail under its own definitions, otherwise 'SUMMARY: not reproduced - ...'.
"""
import itertools
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block14-formation-rate-clause-witness-20260915"
NOTE = "docs/ADMISSIBILITY_RULE_FORMATION_RATE_CLAUSE_WITNESS_NO_COVARIANT_CLOCK_LAW_REACHES_THE_STATIC_LAW_ON_A_PLAQUETTE_BOUNDED_THEOREM_NOTE_2026-09-15.md"
M = range(6)
P, Q, R = 3, 1, 2
W = [[P if a == b else (Q if b == (a ^ 1) else R) for b in M] for a in M]


def show(path):
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def laws(n, edges):
    nb = {i: {j for e in edges for j in e if i in e and j != i} for i in range(n)}
    confs = list(itertools.product(M, repeat=n))
    w = {c: 1 for c in confs}
    for c in confs:
        for a, b in edges:
            w[c] *= W[c[a]][c[b]]
    Z = sum(w.values())
    static = {c: F(w[c], Z) for c in confs}

    def D(order, c):
        seen, d = set(), 1
        for x in order:
            ks = [y for y in nb[x] if y in seen]
            d *= 6 if not ks else sum(_prod(W[s][c[y]] for y in ks) for s in M)
            seen.add(x)
        return d
    orders = list(itertools.permutations(range(n)))
    uniform = {c: sum(F(w[c], D(o, c)) for o in orders) / len(orders) for c in confs}
    # seeded: first site uniform, then uniform over unrecorded sites adjacent to the recorded set
    seeded = {c: F(0) for c in confs}

    def grow(order, prob):
        if len(order) == n:
            for c in confs:
                seeded[c] += prob * F(w[c], D(order, c))
            return
        cand = [x for x in range(n) if x not in order and nb[x] & set(order)]
        for x in cand:
            grow(order + [x], prob / len(cand))
    for x0 in range(n):
        grow([x0], F(1, n))
    return static, uniform, seeded, Z


def _prod(it):
    out = 1
    for v in it:
        out *= v
    return out


def tv(a, b):
    return sum(abs(a[c] - b[c]) for c in a) / 2


def main():
    note = show(NOTE)
    r3 = re.search(r"The uniform law differs[\s\S]{0,700}?`1/216` on the path and `56059/3369600` on the star", note)
    lam = "uniform\n`λ ≡ 1`" in note or "uniform `λ ≡ 1`" in note or re.search(r"uniform\s*`λ ≡ 1`", note) is not None
    tvnote = "exact total variations" in note
    print(f"[note] R3 names 'the uniform law' at distance 1/216 (path) and 56059/3369600 (star): {bool(r3)}; the uniform law is lambda = 1: "
          f"{lam}; distances are total variations: {tvnote}")
    res = {}
    for name, n, edges in (("path", 3, [(0, 1), (1, 2)]), ("star", 5, [(0, i) for i in range(1, 5)])):
        st, un, se, Z = laws(n, edges)
        uni_dist = {c: F(1, 6 ** n) for c in st}
        res[name] = (tv(un, st), tv(se, st), tv(uni_dist, st), Z)
        print(f"[{name}] Z = {Z}; TV(uniform clock law, static) = {res[name][0]}; TV(seeded, static) = {res[name][1]}; "
              f"TV(uniform distribution, static) = {res[name][2]} (the finder's quantity)")
    ok = (bool(r3) and lam and tvnote and res["path"][0] == F(1, 216) and res["star"][0] == F(56059, 3369600)
          and res["path"][1] == 0 and res["star"][1] == 0)
    if ok:
        print("SUMMARY: not reproduced - block 14's D1-D2 hold under the note's definitions: 'the uniform law' is the clock law with "
              "lambda = 1 (a uniformly random formation order), and its total variation to the static law is exactly 1/216 on the path "
              "of 3 and 56059/3369600 on the four-leaf star at (3,1,2), while the seeded law equals the static law on both (R3); the "
              f"finder compared the static law with the uniform distribution on configurations ({res['path'][2]} and {res['star'][2]}), "
              "a different object")
        return 0
    print("HIT: confirmed - the note's R3 distances fail under its own definitions")
    print("SUMMARY: confirmed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
