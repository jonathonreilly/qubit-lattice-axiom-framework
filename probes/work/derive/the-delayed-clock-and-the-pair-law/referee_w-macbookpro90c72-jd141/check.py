#!/usr/bin/env python3
"""Referee of J:derive:the-delayed-clock-and-the-pair-law:a2 (files under w-macbookpro90c72-ja546/, logged with model grok-4.6).

Referee w-macbookpro90c72-jd141 (claude-opus-5-5).  Own code throughout; exact (Fractions, sympy) unless labelled [float].
Model (block 95 P1-P3 with the task's relaxation): a record at x hops to each empty neighbour y at rate w_x^a w_y^(1-a) h/q,
h = W(C')/(W(C)+W(C')), a = 1 (departure timing); du_z/dt = Gamma w_z ((M u)_z + lam (n_z - nbar)), (M u)_z = (1/q) sum_e u_{z+e} - u_z,
lam = log kappa, w = e^u; q = 2 on a ring (block 95: "factor 2 in place of 6"), q = 6 on the cubic torus.
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
A2 = "probes/work/derive/the-delayed-clock-and-the-pair-law/w-macbookpro90c72-ja546/ATTEMPT.md"


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources, verbatim
B95_SHA = "f9b34475df"
B95_NOTE = ("docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_"
            "POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B95_Q = [
    "A move `x → y` runs at the rate `w_x^a w_y^(1−a) · h / 6`, with all rates read in the configuration before the move and `a` a fixed real number.",
    "`a = 1`: the hop is an event of the site the record leaves, so the record \"moves on its own clock\".",
    "with heat-bath factor `h = W(C')/(W(C) + W(C'))`",
    "`W ≡ 1` for records with exclusion only",
    "`π(C) ∝ W(C) exp(6 log κ (1 − 2a) Σ_{{r, s} ⊂ C} G(r − s))`",
    "The zero mode, the unit of rate, is set by the mean of `log w`.",
]
TASK_Q = [
    "departure-timed hopping is in detailed balance with W(C) exp(6 log(kappa) sum_pairs G)",
    "du_z/dt = Gamma w_z ((1/6) sum_e u_(z+e) - u_z + log(kappa)(n_z - nbar))",
    "its effective hop rate (or diffusion constant) in the stationary state of the joint (record, field) process, exactly or to first order in 1/Gamma",
    "is the joint process reversible for any finite Gamma?",
    "HIT: (a) or (b) exact, or an exact proof that no joint law of product form is stationary.",
]
A2_Q = [
    "a record leaves its site toward each neighbor at rate `w_x/d`",
    "No stationary law of product form — a law of the record positions times one deterministic field — exists when `log κ ≠ 0`.",
    "only reparametrizes time",
    "So neither the flat field nor the slaved bump is invariant under the joint process.",
    "The first-order-in-`1/Γ` correction to the two-record separation law is not computed.",
]


def family_q() -> None:
    b95 = subprocess.run(["git", "show", f"{B95_SHA}:{B95_NOTE}"], capture_output=True, text=True).stdout
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:the-delayed-clock-and-the-pair-law:a2"), "")
    a2 = open(A2).read()
    miss = [f"b95[{i}]" for i, s in enumerate(B95_Q) if s not in b95] + [f"task[{i}]" for i, s in enumerate(TASK_Q) if s not in what] \
        + [f"a2[{i}]" for i, s in enumerate(A2_Q) if s not in a2]
    check("Q", not miss, f"{len(B95_Q)} lines of block 95 (head f9b34475, PR #8860), {len(TASK_Q)} of the task, {len(A2_Q)} of a2's "
          f"ATTEMPT.md quoted verbatim{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ Green functions
def ring_G(L: int):
    return [Fr(L * L - 1, 12 * L) - Fr(k * (L - k), 2 * L) for k in range(L)]


def torus4_G():
    cs = [1, 0, -1, 0]                                   # cos(2 pi m / 4)
    sites = list(itertools.product(range(4), repeat=3))
    G = {}
    for k in sites:
        tot = Fr(0)
        for qv in sites:
            if qv != (0, 0, 0):
                tot += Fr(cs[(qv[0] * k[0] + qv[1] * k[1] + qv[2] * k[2]) % 4], sum(2 - 2 * cs[c] for c in qv))
        G[k] = tot / 64
    return G, sites


def shift(k, e):
    return tuple((a + b) % 4 for a, b in zip(k, e))


E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


# ------------------------------------------------------------------------------------------------ R1: a2 step S1
def family_r1() -> None:
    a = sp.Symbol("a", real=True)
    ok = True
    for q in (2, 6):
        wx = sp.Symbol("w_x", positive=True)
        ws = sp.symbols(f"w1:{q + 1}", positive=True)
        rates = [wx ** a * we ** (1 - a) * sp.Rational(1, 2) / q for we in ws]      # one record: no occupied bond, W = 1, h = 1/2
        ok &= all(sp.simplify(r.subs(a, 1) - wx / (2 * q)) == 0 for r in rates)    # a = 1: one number for every neighbour
        tot0 = sum(r.subs(a, 0) for r in rates)
        ok &= sp.simplify(rates[0].subs(a, 0) / tot0 - sp.Rational(1, q)) != 0      # a = 0 would follow the target clock
    check("R1", ok, "S1 follows: with a = 1 (the task's departure timing) and W = 1 (one record has no occupied bond, h = 1/2) the rate "
          "to every neighbour is w_x/(2q) whatever the field, so one record's jump chain is the simple random walk at every Gamma "
          "(q = 2 and 6, symbolic w); a2's rate w_x/d is twice block 95's, harmless for S1")


# ------------------------------------------------------------------------------------------------ R2: a2 step S2
def family_r2() -> None:
    ok = True
    for L in range(3, 13):
        lam = Fr(-1)
        u = [-lam / L * (Fr(z * (L - z)) - Fr(L * L - 1, 6)) for z in range(L)]     # a2's S2 formula
        G = ring_G(L)
        ok &= all(u[z] == 2 * lam * G[z] for z in range(L)) and sum(u) == 0
        ok &= all((u[(z + 1) % L] + u[(z - 1) % L]) / 2 - u[z] + lam * ((1 if z == 0 else 0) - Fr(1, L)) == 0 for z in range(L))
        ok &= u[0] == lam * Fr(L * L - 1, 6 * L)
        if L == 4:
            ok &= u[0] - u[1] == Fr(-3, 4)
    N = 5
    uu = sp.symbols("u0:5", real=True); g, lam = sp.symbols("Gamma lambda", real=True)
    n = [1, 0, 0, 0, 0]
    du = [g * sp.exp(uu[z]) * ((uu[(z + 1) % N] + uu[(z - 1) % N]) / 2 - uu[z] + lam * (n[z] - sp.Rational(1, N))) for z in range(N)]
    inv = sp.simplify(sum(-sp.exp(-uu[z]) * du[z] for z in range(N))) == 0
    # the factor w_z is site dependent: at u = (1,0,0,0), L = 4, lam = -1 the weighted and unweighted velocities are not parallel
    b = [sp.Rational(-7, 4), sp.Rational(3, 4)]                                                       # (Mu + lam(delta - 1/4)) at sites 0, 1
    notpar = sp.simplify(sp.E * b[0] * b[1] - b[1] * b[0]) != 0
    check("R2", ok and inv and notpar, "S2's profile holds exactly (L = 3..12: it is 2 log(kappa) G, mean zero, on-site value "
          "log(kappa)(L^2-1)/(6L); L = 4: u0 - u1 = -3/4); two notes: the relaxation conserves sum_z 1/w_z exactly (symbolic), so the "
          "physical gauge is that invariant, not the mean (the contrast u0 - mean is gauge free); and 'w_z > 0 only reparametrizes "
          "time' is not true of a site-dependent factor (velocities not parallel at u = (1,0,0,0)) - only the zero set is shared")


# ------------------------------------------------------------------------------------------------ R3: a2 step S3
def configs(L, n):
    return [frozenset(c) for c in itertools.combinations(range(L), n)]


def family_r3() -> None:
    lam, g = sp.symbols("lambda Gamma", nonzero=True)
    ok = True
    for L in (4, 5, 6):
        us = sp.symbols(f"v0:{L}", real=True)
        for nrec in (1, 2):
            cs = configs(L, nrec)
            F = {}
            for C in cs:
                F[C] = [g * sp.exp(us[z]) * ((us[(z + 1) % L] + us[(z - 1) % L]) / 2 - us[z] + lam * ((1 if z in C else 0) - sp.Rational(nrec, L)))
                        for z in range(L)]
            for C, D in itertools.combinations(cs, 2):       # F_C - F_D = Gamma lam w (n_C - n_D), never zero: two equilibrium sets never meet
                diff = [sp.expand(F[C][z] - F[D][z] - g * lam * sp.exp(us[z]) * ((z in C) - (z in D))) for z in range(L)]
                ok &= all(v == 0 for v in diff) and C != D
    # a field that is neither flat nor any configuration's equilibrium: S3's text does not treat it
    L, lv = 4, Fr(-1)
    ubar = [Fr(1), Fr(0), Fr(0), Fr(0)]
    G = ring_G(L)
    notflat = len(set(ubar)) > 1
    nonequil = True
    for nrec in (1, 2):
        for C in configs(L, nrec):
            ustar = [2 * lv * sum(G[(z - r) % L] for r in C) for z in range(L)]
            nonequil &= len({ubar[z] - ustar[z] for z in range(L)}) > 1
            drift = [(ubar[(z + 1) % L] + ubar[(z - 1) % L]) / 2 - ubar[z] + lv * ((1 if z in C else 0) - Fr(nrec, L)) for z in range(L)]
            nonequil &= any(v != 0 for v in drift)
    check("R3", ok and notflat and nonequil, "S3 does not cover its own statement: it treats the flat field and the slaved bump "
          "u*(positions), which is not a law of positions times one field, and says nothing of a fixed non-flat field; e.g. u = (1,0,0,0) "
          "on the ring of 4 is neither, and its drift is nonzero for all 10 configurations of 1 and 2 records. Repair (own): F_C - F_D = "
          "Gamma log(kappa) w (n_C - n_D) != 0 for C != D (rings 4-6, symbolic field), so a fixed field is an equilibrium of at most "
          "one configuration; a stationary mu x delta(u - ubar) would sit on one configuration, which the hop rate r0 w_x > 0 empties")


# ------------------------------------------------------------------------------------------------ R4: task (a), not derived by a2
def transient(L, lam, S=150.0, ds=0.01):
    """[float] one record hops x0 = 0 -> x1 = 1 with the field relaxed at x0; returns int_0^oo (w_x1 - w*) ds in s = Gamma t,
    and the largest distance of the final field from the new equilibrium 2 lam G(. - x1) (same invariant level)."""
    G = [float(v) for v in ring_G(L)]
    u = [2 * lam * G[z % L] for z in range(L)]
    wst = math.exp(2 * lam * G[0])

    def f(v):
        return [math.exp(v[z]) * (0.5 * (v[(z + 1) % L] + v[(z - 1) % L]) - v[z] + lam * ((1 if z == 1 else 0) - 1.0 / L)) for z in range(L)]
    J = 0.0
    for _ in range(int(S / ds)):
        k1 = f(u); u2 = [p + 0.5 * ds * r for p, r in zip(u, k1)]
        k2 = f(u2); u3 = [p + 0.5 * ds * r for p, r in zip(u, k2)]
        k3 = f(u3); u4 = [p + ds * r for p, r in zip(u, k3)]
        k4 = f(u4)
        J += ds / 6 * sum(c * (math.exp(v[1]) - wst) for c, v in zip((1, 2, 2, 1), (u, u2, u3, u4)))
        u = [p + ds / 6 * (r1 + 2 * r2 + 2 * r3 + r4) for p, r1, r2, r3, r4 in zip(u, k1, k2, k3, k4)]
    return J, max(abs(u[z] - 2 * lam * G[(z - 1) % L]) for z in range(L))


def family_r4() -> None:
    ok = True
    for L in range(3, 13):
        G = ring_G(L)
        G2 = [sum(G[j] * G[(k - j) % L] for j in range(L)) for k in range(L)]
        ok &= G2[0] - G2[1] == G[0] / 2
        ok &= all(-(Fr(1, 2) * (2 * G[(k + 1) % L] + 2 * G[(k - 1) % L]) - 2 * G[k]) == (1 if k == 0 else 0) - Fr(1, L) for k in range(L))
    Gt, sites = torus4_G()
    ok &= all(6 * Gt[k] - sum(Gt[shift(k, e)] for e in E6) == (1 if k == (0, 0, 0) else 0) - Fr(1, 64) for k in sites)
    g20 = sum(Gt[j] * Gt[j] for j in sites)
    g2e = sum(Gt[j] * Gt[shift(tuple(-c for c in j), (1, 0, 0))] for j in sites)
    ok &= g20 - g2e == Gt[(0, 0, 0)] / 6
    check("R4a", ok, f"referee side computation for task (a), exact ingredients: G2(0) - G2(e) = G(0)/q with G2 = G*G (rings 3-12, q = 2; "
          f"4^3 torus, q = 6, G(0) = {Gt[(0, 0, 0)]}) and (-M)^+ = q G, so after a hop the linearised lag gives int (u_x - u*_x) dt = "
          f"-q log(kappa) G(0)/Gamma at the new site: mean wait (1 - H)/R_inf, H = -q log(kappa) G(0)/(2 Gamma), block 95's r0 = 1/(2q)")
    L = 8
    Jp, ep = transient(L, 0.01)
    Jm, em = transient(L, -0.01)
    Jb, eb = transient(L, -0.5)
    G0 = float(ring_G(L)[0])
    c1 = (Jp - Jm) / 0.02
    okf = abs(c1 / (-2 * G0) - 1) < 1e-3 and max(ep, em, eb) < 1e-8
    check("R4b", okf, f"[float, executed] ring of 8, nonlinear relaxation integrated (RK4, ds = 0.01, s = Gamma t to 150): odd part of "
          f"int (w_x - w*) ds per log kappa = {c1:.5f} vs -q G(0) = {-2 * G0:.5f}; even part {(Jp + Jm) / 2:.1e}; at log kappa = -0.5 the ratio "
          f"is {Jb / (-0.5):.4f} (nonlinear); final field within {max(ep, em, eb):.0e} of the new equilibrium")


# ------------------------------------------------------------------------------------------------ R5: the task text's sign
def family_r5() -> None:
    lam = sp.Symbol("lambda", real=True)
    L = 6
    G = ring_G(L)
    good, bad = True, False
    for C in configs(L, 2):
        for x in C:
            for y in ((x + 1) % L, (x - 1) % L):
                if y in C:
                    continue
                D = (C - {x}) | {y}
                lr_f = 2 * lam * sum(G[(x - r) % L] for r in C)        # a = 1: log of the departure clock, W = 1 so h cancels
                lr_b = 2 * lam * sum(G[(y - r) % L] for r in D)
                pair = lambda S: sum(G[(r - s) % L] for r, s in itertools.combinations(sorted(S), 2))
                good &= sp.expand((-2 * lam * pair(D)) - (-2 * lam * pair(C)) - (lr_f - lr_b)) == 0
                bad |= sp.expand((2 * lam * pair(D)) - (2 * lam * pair(C)) - (lr_f - lr_b)) != 0
    check("R5", good and bad, "task text vs block 95: with a = 1 on the ring of 6 (two records, every move, symbolic log kappa) "
          "detailed balance holds for exp(-2 log(kappa) sum_pairs G) = block 95's (1 - 2a) law, and fails for the task text's "
          "exp(+2 log(kappa) sum_pairs G); a2 uses block 95 only as a comparison (S4), so this does not touch its steps")


def main() -> int:
    family_q()
    family_r1()
    family_r2()
    family_r3()
    family_r4()
    family_r5()
    print("Referee of J:derive:the-delayed-clock-and-the-pair-law:a2 - referee w-macbookpro90c72-jd141 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: referee checks failed at {FAILS[0]}")
        return 1
    print("SUMMARY: fails at step S3 - S3 covers the flat field and the slaved bump (itself not a product law) but no other fixed field; "
          "the narrow claim does hold after a one-line repair (a fixed field is an equilibrium of at most one configuration, R3), but "
          "section 1 weakens the task's product form (records independent of an arbitrary field law) to one deterministic field, "
          "and (a)'s hop rate, (b)'s pair-law correction and reversibility are not derived; the rate does move at order 1/Gamma (R4)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
