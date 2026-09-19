#!/usr/bin/env python3
"""J:confirm:J-attack-a-PR8155 - independent test of the finder's HIT on block 21 (PR #8155): 'the torus (Z/2LZ)^3 at the stated endpoint
L = 1 does not realize six distinct neighbours (+e_i = -e_i), so it is not the six-neighbour graph the conditionals and C_Lambda row-sum
alpha = 6c are written for'.

Different machinery from the finder (who counted the distinct neighbours of the origin):
  * the definitions are read at the PR branches: block 21 takes 'the torus law mu_L of block 19 on (Z/2LZ)^3' and says it 'has the same
    conditionals'; block 19 defines that law with '3N bonds' and the product over them;
  * the bond list {(x, x + e_i) : x in T, i = 1..3} is built for L = 1..3 and its multiplicities counted;
  * the conditional field at a site is obtained from the log-density by exact symbolic differentiation (sympy) on the L = 1 torus;
  * the influence of one distinct neighbour, the row sum, the walk bounds with multiplicity and the torus sum (1 + alpha)^3 of W5 are
    recomputed exactly on the L = 1 torus.
Prints 'HIT: confirmed - ...' if the six-neighbour structure fails at L = 1 under these definitions, otherwise 'SUMMARY: not reproduced'.
"""
import itertools
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[4]
B21 = "physics-loop/admissibility-induced-law-block21-unsoldered-sphere-static-law-weak-coupling-uniqueness-exponential-decay-20260915"
N21 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_WEAK_COUPLING_ONE_LAW_EXPONENTIAL_DECAY_NO_MASSLESS_CHANNEL_BELOW_ROOT_THREE_"
       "OVER_SIX_BOUNDED_THEOREM_NOTE_2026-09-15.md")
B19 = "physics-loop/admissibility-induced-law-block19-sphere-static-law-goldstone-green-function-channel-20260915"
N19 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_ORDERED_PHASE_TRANSVERSE_CHANNEL_CARRIES_THE_LATTICE_GREEN_FUNCTION_INFRARED_"
       "AND_BOGOLIUBOV_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md")


def show(branch, path):
    r = subprocess.run(["git", "show", f"origin/{branch}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", branch], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"origin/{branch}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def main():
    n21, n19 = show(B21, N21), show(B19, N19)
    same = "The torus law `μ_L` of block 19 on `(Z/2LZ)³`, `N = (2L)³`, has the same conditionals." in n21
    bonds3N = "`3N` bonds" in n19 and "Π_{⟨xy⟩} e^{β s_x·s_y}" in n19
    every = "on the torus `(Z/2LZ)³` for every `L ≥ 1`" in n21
    print(f"[notes] block 21: torus law of block 19 'has the same conditionals': {same}; W5(b) 'for every L >= 1': {every}; block 19: "
          f"'3N bonds', product over bonds: {bonds3N}")

    rows = []
    for L in (1, 2, 3):
        n = 2 * L
        T = list(itertools.product(range(n), repeat=3))
        bonds = [(x, tuple((x[t] + (1 if t == i else 0)) % n for t in range(3))) for x in T for i in range(3)]
        mult = Counter(frozenset(b) for b in bonds)
        slots = Counter()
        for a, b in bonds:
            slots[a] += 1
            slots[b] += 1
        rows.append((L, len(T), len(bonds), len(mult), set(mult.values()), set(slots.values())))
    ok_bonds = rows[0][2] == 3 * rows[0][1] == 24 and rows[0][3] == 12 and rows[0][4] == {2} and rows[0][5] == {6} \
        and all(r[4] == {1} and r[5] == {6} for r in rows[1:])
    print("[bonds] " + "; ".join(f"L = {L}: N = {N}, {nb} bonds = 3N, {nd} distinct pairs, multiplicities {m}, slots per site {s}"
                                   for L, N, nb, nd, m, s in rows))

    # L = 1: conditional field from the log-density
    T = list(itertools.product(range(2), repeat=3))
    beta = sp.symbols("beta", positive=True)
    S = {x: sp.Matrix(sp.symbols(f"s{''.join(map(str, x))}_1:4")) for x in T}
    bonds = [(x, tuple((x[t] + (1 if t == i else 0)) % 2 for t in range(3))) for x in T for i in range(3)]
    logw = sum(beta * (S[a].T * S[b])[0] for a, b in bonds)
    x0 = (0, 0, 0)
    grad = sp.Matrix([sp.diff(logw, v) for v in S[x0]])
    six = sum((S[tuple((x0[t] + (d if t == i else 0)) % 2 for t in range(3))] for i in range(3) for d in (1, -1)), sp.zeros(3, 1))
    distinct = sum((S[tuple((x0[t] + (1 if t == i else 0)) % 2 for t in range(3))] for i in range(3)), sp.zeros(3, 1))
    field_ok = sp.simplify(grad - beta * six) == sp.zeros(3, 1) and sp.simplify(six - 2 * distinct) == sp.zeros(3, 1)
    print(f"[field] L = 1: d log w / d s_0 = beta * (sum over the six slots x +- e_i) = 2 beta * (sum over the three distinct neighbours): {field_ok}")

    # influence and row sum at L = 1, with c = beta/sqrt3 per slot: changing one distinct neighbour moves h by at most 2 * 2 = 4
    c = sp.Symbol("c")
    per_distinct = F(4, 2)          # W1: TV <= (beta/(2 sqrt3)) |dh|, |dh| <= 4 -> 2 * beta/sqrt3 = 2c
    row = 3 * per_distinct
    # walk bounds with multiplicity: C_xy = 2c for distinct neighbours; sum_y (C^k)_0y = (6c)^k and (C^k)_0y = 0 for k < d_T(0, y)
    idx = {x: i for i, x in enumerate(T)}
    Cm = sp.zeros(8, 8)
    for x in T:
        for i in range(3):
            y = tuple((x[t] + (1 if t == i else 0)) % 2 for t in range(3))
            Cm[idx[x], idx[y]] += 2 * c
    walks_ok = True
    Ck = sp.eye(8)
    for k in range(1, 5):
        Ck = Ck * Cm
        walks_ok &= sp.expand(sum(Ck[idx[x0], j] for j in range(8)) - (6 * c) ** k) == 0
        for y in T:
            if k < sum(y):
                walks_ok &= Ck[idx[x0], idx[y]] == 0
    a = sp.Symbol("alpha")
    torus_sum = sum(a ** sum(y) for y in T)
    sum_ok = sp.expand(torus_sum - (1 + a) ** 3) == 0
    print(f"[W2/W5 at L = 1] one distinct neighbour: TV <= {per_distinct} c; row sum {row} c = alpha; walk counts with multiplicity: "
          f"sum_y (C^k)_0y = (6c)^k and (C^k)_0y = 0 below the torus distance for k <= 4: {walks_ok}; sum_x alpha^d_T(0,x) = (1+alpha)^3: {sum_ok}")

    if same and bonds3N and ok_bonds and field_ok and row == 6 and walks_ok and sum_ok:
        print("SUMMARY: not reproduced - block 19's torus law has 3N bonds (x, x + e_i), so at L = 1 each of the 12 edges of (Z/2Z)^3 is "
              "doubled (24 bonds, every site in six bond slots): the conditional field is the sum over the six slots (twice the sum over the "
              "three distinct neighbours, exact derivative of the log-density), one distinct neighbour moves it by up to 4 and has influence "
              "2c, the row sum is 6c = alpha, the walk bounds hold with multiplicity and the torus sum is (1+alpha)^3; W5(b) at L = 1 is the "
              "multigraph statement it is written as. The finder counted distinct neighbours (3) and missed the bond multiplicity")
        return 0
    print("HIT: confirmed - the L = 1 torus does not carry the six-neighbour conditionals under the notes' definitions")
    print("SUMMARY: confirmed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
