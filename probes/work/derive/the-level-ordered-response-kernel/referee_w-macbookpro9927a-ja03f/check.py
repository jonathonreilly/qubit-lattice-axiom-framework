#!/usr/bin/env python3
"""Referee of J:derive:the-level-ordered-response-kernel:a2 (files under w-macbookpro90c72-jf747/, logged with model grok-4.6).

Referee w-macbookpro9927a-ja03f (claude-opus-5-5).  Own code throughout; exact (Fractions, sympy) unless labelled [float].
Objects: P(k) = (1 + sum_j e^{-ik_j})/4 (task); the walk with steps {0, e1, e2, e3} of probability 1/4 each; G = sum_n P^n delta_0;
E(k) = 6 - 2 sum_j cos k_j (block 91); block 91's source enters the rule's argument like one more predecessor.
"""
from __future__ import annotations

import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as Fr

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []
A2 = "probes/work/derive/the-level-ordered-response-kernel/w-macbookpro90c72-jf747/ATTEMPT.md"


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources, verbatim
B90 = ("c3412ce595", "docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_"
       "POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B91 = ("036826ac2e", "docs/ADMISSIBILITY_RULE_A_PINNED_SOURCE_UNDER_LIGHT_CONE_FORMATION_IS_ANSWERED_BY_THE_INVERSE_LATTICE_LAPLACIAN_"
       "WITHIN_A_FACTOR_BETWEEN_M_SQUARED_AND_ONE_BOUNDED_THEOREM_NOTE_2026-09-23.md")
QUOTES = {
    B90: ["The same rule with the past `{0, −e_1, −e_2, −e_3}` (four predecessors: the event lattice in level order)."],
    B91: ["feels an extra pull `h` added to its seven predecessors (weight `e^{β s'·(h_x(s) + h)}`)",
          "`⟨m⟩² / (⟨P_b⟩E(k) + ε⟨m⟩)  ≤  R̂_⊥(k)  ≤  1/E(k)`,  `E(k) = 6 − 2Σ_j cos k_j`.",
          "Its ratios scatter from `0.918` to `1.060`, with a forward–backward asymmetry, and one exceeds the upper bound."],
}
TASK_Q = ["(1 - P)^-1 with P(k) = (1 + sum_j e^{-i k_j})/4", "HIT: (a) exact.",
          "(b) whether the nonlinear law's response can exceed the light-cone law's upper bound 1/E(k) (one executed ratio did)"]
A2_Q = ["`G(x) = (1/3) Σ_{j=1}^3 G(x-e_j)` for `x ≠ 0`.", "It is `G(a,b,c) = (4/3) L!/(a!b!c!) 3^{-L}` for `a,b,c ≥ 0`, `L=a+b+c`.",
        "The symbol `4/(3-Σ e^{-ik_j})` is therefore `8/E`, against the light-cone gain-one kernel `7/E`.",
        "The large-distance Gaussian cross-section is not proved here."]


def family_q() -> None:
    miss = []
    for (sha, path), qs in QUOTES.items():
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{sha[:6]}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:the-level-ordered-response-kernel:a2"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    a2 = open(A2).read()
    miss += [f"a2[{i}]" for i, q in enumerate(A2_Q) if q not in a2]
    check("Q", not miss, f"block 90 (head c3412ce5, PR #8692), block 91 (head 036826ac, PR #8696), the task and a2 quoted verbatim "
          f"({sum(len(v) for v in QUOTES.values()) + len(TASK_Q) + len(A2_Q)} lines){'; missing ' + str(miss) if miss else ''}")


def Gf(x):
    if min(x) < 0:
        return Fr(0)
    L = sum(x)
    return Fr(4, 3) * Fr(math.factorial(L), math.factorial(x[0]) * math.factorial(x[1]) * math.factorial(x[2]) * 3 ** L)


def octant(L):
    return [(a, b, L - a - b) for a in range(L + 1) for b in range(L + 1 - a)]


# ------------------------------------------------------------------------------------------------ R1: the kernel by another route
def family_r1() -> None:
    z1, z2, z3 = sp.symbols("z1 z2 z3")
    s = z1 + z2 + z3
    K = 12
    series = sum(sp.Rational(4, 3) * (s / 3) ** L for L in range(K + 1))
    ok = sp.expand((3 - s) * series - (4 - 4 * (s / 3) ** (K + 1))) == 0             # telescoping: 4/(3 - sum z) = (4/3) sum ((sum z)/3)^L
    poly = sp.Poly(sp.expand(series), z1, z2, z3)
    ok &= all(poly.coeff_monomial(z1 ** a * z2 ** b * z3 ** c) == sp.Rational(Gf((a, b, c)).numerator, Gf((a, b, c)).denominator)
              for L in range(K + 1) for (a, b, c) in octant(L))
    # exact visit counts of the walk: sum_{n <= 80} P^n delta_0, compared with the closed form (remainder < 1e-20 for L <= 6)
    dist = {(0, 0, 0): Fr(1)}
    acc = {}
    for n in range(81):
        for x, p in dist.items():
            acc[x] = acc.get(x, Fr(0)) + p
        new = {}
        for x, p in dist.items():
            for d in ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)):
                y = (x[0] + d[0], x[1] + d[1], x[2] + d[2])
                if sum(y) <= 6:
                    new[y] = new.get(y, Fr(0)) + p / 4
        dist = new
    ok &= all(0 <= Gf(x) - acc.get(x, Fr(0)) < Fr(1, 10 ** 20) for L in range(7) for x in octant(L))
    ok &= all(x in acc for L in range(7) for x in octant(L)) and all(min(x) >= 0 for x in acc)
    check("R1", ok, "S1-S4 follow, by a route of my own: (3 - sum z) sum_L (4/3)(sum z/3)^L = 4 - 4(sum z/3)^(K+1) (K = 12), so "
          "4/(3 - sum e^{-ik}) = 1/(1 - P) has coefficients (4/3) L!/(a!b!c!) 3^-L (all 455 monomials to L = 12); the walk's exact "
          "visit sums to 80 steps meet the closed form within 1e-20 on every site with L <= 6 and never leave the octant")


def family_r2() -> None:
    rec = all((Fr(4, 3) if x == (0, 0, 0) else Fr(0)) + sum(Gf((x[0] - (j == 0), x[1] - (j == 1), x[2] - (j == 2))) for j in range(3)) / 3
              == Gf(x) for L in range(13) for x in octant(L))
    lev = all(sum(Gf(x) for x in octant(L)) == Fr(4, 3) for L in range(13))
    vals = Gf((1, 0, 0)) == Fr(4, 9) and Gf((-1, 0, 0)) == 0
    const = all(Fr(5) == sum(Fr(5) for _ in range(3)) / 3 for _ in range(1))        # h = const solves the homogeneous recursion
    check("R2", rec and lev and vals and const, "S2 needs its support condition and has it: the causal recursion holds through level 12 "
          "(my loop), each level sums to 4/3 (L <= 12), G(1,0,0) = 4/9, G(-1,0,0) = 0; without causality the recursion is not "
          "unique (any constant solves its homogeneous part)")


def family_r3() -> None:
    q = sp.Symbol("q", real=True)
    k = (q, -q, 0)
    E = 6 - 2 * sum(sp.cos(c) for c in k)
    lo = 4 / (3 - sum(sp.exp(-sp.I * c) for c in k))
    lc = 1 / (1 - (1 + 2 * sum(sp.cos(c) for c in k)) / 7)
    ok = sp.simplify(sp.expand_complex(lo - 8 / E)) == 0 and sp.simplify(lc - 7 / E) == 0
    check("R3", ok, "S6 follows: on k = (q,-q,0) the level-ordered symbol 4/(3 - sum e^{-ik}) is 8/E and the light-cone gain-one "
          "kernel (1 - (1 + 2 sum cos)/7)^-1 is 7/E (symbolic)")


# ------------------------------------------------------------------------------------------------ R4: referee side computation, (b)
def family_r4() -> None:
    # zero-temperature rule s' = H/|H|: around the aligned state H = c e_z + v, v transverse, s'_perp = v/c + O(v^2)
    c, v1, v2, t = sp.symbols("c v1 v2 t", positive=True)
    H = sp.Matrix([t * v1, t * v2, c])
    sp_perp = (H / sp.sqrt(H.dot(H)))[0]
    lin = sp.series(sp_perp, t, 0, 2).removeO()
    ok = sp.simplify(lin - t * v1 / c) == 0
    # so the source (entering like one more predecessor, block 91) is answered by (1/c)(1 - P_c)^-1: level-ordered c = 4, light-cone c = 7
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    ks = (k1, k2, k3)
    E = 6 - 2 * sum(sp.cos(x) for x in ks)
    R_lc = (sp.Rational(1, 7) / (1 - (1 + 2 * sum(sp.cos(x) for x in ks)) / 7))
    ok &= sp.simplify(R_lc - 1 / E) == 0                                                   # light-cone at zero temperature = the bound
    A = 3 - sum(sp.cos(x) for x in ks); B = sum(sp.sin(x) for x in ks)
    R_lo = sp.Rational(1, 4) / (1 - (1 + sum(sp.exp(-sp.I * x) for x in ks)) / 4)          # = 1/(3 - sum e^{-ik})
    mod2 = sp.simplify(sp.expand_complex(R_lo * sp.conjugate(R_lo)))
    ok &= sp.simplify(mod2 * E ** 2 - 4 * A ** 2 / (A ** 2 + B ** 2)) == 0                   # |R_lo| E = 2A/sqrt(A^2 + B^2) <= 2
    # [float] scan of the 16^3 torus: max |R_lo| E = 2, reached exactly on sum sin = 0
    L = 16
    mx, mx_off, n_eq = 0.0, 0.0, 0
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        kk = [2 * math.pi * m / L for m in n]
        a = 3 - sum(math.cos(x) for x in kk); b = sum(math.sin(x) for x in kk)
        r = 2 * a / math.hypot(a, b)
        mx = max(mx, r)
        if abs(b) > 1e-9:
            mx_off = max(mx_off, r)
        elif abs(r - 2) < 1e-12:
            n_eq += 1
    ok2 = abs(mx - 2) < 1e-12 and mx_off < 2 - 1e-9
    # position space, zero temperature, infinite lattice: R_lo = G/4; inverse Laplacian drop G_Lap(0) - G_Lap(e) = 1/6 exactly
    Rlo = lambda x: Gf(x) / 4
    fwd = (Rlo((0, 0, 0)) - Rlo((1, 0, 0))) / Fr(1, 6)
    bwd = (Rlo((0, 0, 0)) - Rlo((-1, 0, 0))) / Fr(1, 6)
    ok &= fwd == Fr(4, 3) and bwd == 2
    check("R4", ok and ok2, f"referee side computation for (b), exact: the zero-temperature rule s' = H/|H| answers a source with "
          f"(1/c)(1 - P_c)^-1, so light-cone formation gives exactly 1/E(k) (its window's top) and level-ordered formation "
          f"1/(3 - sum e^(-ik)), with |R| E = 2(3 - sum cos)/|3 - sum e^(-ik)| <= 2, equal to 2 exactly where sum sin k = 0 "
          f"({n_eq} such modes on 16^3, float scan; max elsewhere < 2); in position space its drops at r = 1 are 4/3 (forward) and "
          f"2 (backward) times the inverse Laplacian's 1/6, against the probes' finite-beta 0.918-1.060")


def main() -> int:
    family_q()
    family_r1()
    family_r2()
    family_r3()
    family_r4()
    print("Referee of J:derive:the-level-ordered-response-kernel:a2 - referee w-macbookpro9927a-ja03f (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: fails at step {FAILS[0]} - see the failing check")
        return 1
    print("SUMMARY: every step S1-S6 follows; the kernel repeats attempt a1's (already confirmed) by the causal-recursion route; "
          "the large-distance form and the nonlinear comparison are left open as the attempt says; note that 8/E against 7/E "
          "compares kernels, while in block 91's response units the zero-temperature rules give 2/E against 1/E (R4)")
    print("HIT: confirmed - G = (4/3) L!/(a!b!c!) 3^-L on the forward octant and 0 elsewhere is the unique causal solution, each "
          "level carries 4/3, and the drift-free symbol is 8/E (7/E light-cone); verified by the generating function, exact walk "
          "sums and my own recursion loop to level 12")
    return 0


if __name__ == "__main__":
    sys.exit(main())
