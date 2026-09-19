#!/usr/bin/env python3
"""Referee of J:derive:lightcone-formation:a4 (author w-macbookpro90c72-j89d5, grok-4.6); referee w-jonathonsmac4f50-j8aa7
(claude-opus-5). Independent code (exact Fractions, sympy); nothing from the author's check.py. Disclosure: this referee's model family
refereed attempts a1, a2, a5 and a6 of this problem (all grok).

Path 0 - 1 - 2, six-axis weights (3,1,2), a = +z. pi ~ prod_x Z_x(s) with Z_x = sum_u prod_{y in N(x)} W(u, s_y).
The task's light-cone stencil includes the site: N(x) = {x, x +- 1} on the path; the truncated star omits it.

R1  step 1: C = sigma^2/(1 - phi^2) = 7 sigma^2/(2E(1 - E/14)) with phi = 1 - E/7 (sympy)
R2  the stated conditionals are the truncated star's: P(s0 = a | s1, s2 = a) = 13/72 and P(s0 = a | s1, s2 = +y) = 1/6, and there they do
    not depend on s1 at all (the conditional of s0 is Z(s0, s2)/sum_v Z(v, s2): the sublattices decouple)
R3  for the light-cone stencil (site included) the conditionals are P(s0 = a | s1 = a, s2 = a) = 39/188 and P(s0 = a | s1 = a, s2 = +y) =
    169/866: they still depend on the next-nearest site, so the range-2 conclusion holds for the task's law; the static nearest-neighbour
    conditional is 1/4 whatever s2 is
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


M = range(6)
W = [[3 if a == b else (1 if b == (a ^ 1) else 2) for b in M] for a in M]
A, Y = 4, 2          # +z, +y


def Z(vals):
    tot = 0
    for u in M:
        pr = 1
        for v in vals:
            pr *= W[u][v]
        tot += pr
    return tot


def cond(law, s1, s2):
    w = {v: law(v, s1, s2) for v in M}
    return F(w[A], sum(w.values()))


def main():
    E, s2 = sp.symbols("E sigma2", positive=True)
    phi = 1 - E / 7
    check("R1", sp.simplify(s2 / (1 - phi ** 2) - 7 * s2 / (2 * E * (1 - E / 14))) == 0, "C = 7 sigma^2/(2E(1 - E/14))")

    star = lambda s0, s1, s2: Z([s1]) * Z([s0, s2]) * Z([s1])                  # sites 0, 1, 2 with neighbours only
    cone = lambda s0, s1, s2: Z([s0, s1]) * Z([s0, s1, s2]) * Z([s1, s2])      # site included
    static = lambda s0, s1, s2: W[s0][s1] * W[s1][s2]
    st_a, st_y = cond(star, A, A), cond(star, A, Y)
    indep = all(cond(star, s1, s2x) == cond(star, A, s2x) for s1 in M for s2x in M)
    check("R2", st_a == F(13, 72) and st_y == F(1, 6) and indep, f"truncated star: {st_a} (s2 = +z), {st_y} (s2 = +y); independent of s1 for "
          f"every s1, s2: {indep}")

    lc_a, lc_y = cond(cone, A, A), cond(cone, A, Y)
    stat = {cond(static, A, s2x) for s2x in M}
    check("R3", lc_a == F(39, 188) and lc_y == F(169, 866) and lc_a != lc_y and stat == {F(1, 4)},
          f"light-cone stencil: {lc_a} (s2 = +z), {lc_y} (s2 = +y) - range 2; static nearest-neighbour conditional {stat}")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - lightcone-formation a4: the light-cone Gibbs law pi ~ prod Z(S_x) has a range-2 specification (on the 3-site "
          "path at (3,1,2), P(s0 = +z | s1 = +z) is 39/188 for s2 = +z and 169/866 for s2 = +y, against the static 1/4 for every s2), so "
          "block 19's nearest-neighbour RP/IR does not transfer; C = 7/(2E(1 - E/14)). Correction: the attempt's 13/72 and 1/6 are the "
          "truncated star's values (site omitted), where the conditional of s0 does not depend on s1 at all")
    print("SUMMARY: confirmed with corrected numbers for the light-cone stencil; the range-2 conclusion holds for both stencils")
    return 0


if __name__ == "__main__":
    sys.exit(main())
