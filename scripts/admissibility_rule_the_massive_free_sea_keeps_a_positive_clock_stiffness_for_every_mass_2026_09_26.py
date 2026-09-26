#!/usr/bin/env python3
"""Exact checks: the massive free sea keeps a positive clock stiffness for every mass, and a mass makes a chessboard of clocks
visible (a harvest of probe #9210, confirmed by an other-family referee in #9295). The walk H = sum_a sigma_a S_a with a
staggered mass m eps (eps_x = (-1)^(x+y+z)), clocked as phi (H + m eps) phi (block 77 T3), and the filled sea (block 76):

A (premises): the landed notes of blocks 70, 71, 76 and 77 carry the quoted lines.
B (T1, maps and twins, exact on the 4^3 torus): eps anticommutes with H; every exchange map V_n keeps eps, the even ones
   commute with H + m eps and the odd ones do after eps; eps T (one-site shift after the site sign) is a twin, with density
   e_x[eps T psi; T phi] = -e_{x-e1}[psi; phi] exactly; block 71's on-site twin fails with a mass by 2 m w eps |psi|^2.
C (T2, the sea): M(k)^2 = E^2; P_- M = (M - E)/2, so the filled sea's density is m eps_x - <E>; the projector overlaps
   tr P_a P_b = 1 + ab(s.s' + m^2)/(E E'); the symmetrized second-order weight; the gradient bounds behind the O(|q|^4/m^3)
   remainder.
D (T3, the stiffness and the chessboard): exact zone moments 3/2, 21/8, 81/16; kappa(m) = 1/(8m) - 7/(64 m^3) + 81/(512 m^5)
   - ... for m > sqrt3; exact rational enclosures of kappa(2), kappa(4); a chessboard of clocks: phi_x phi_y = 1 on bonds,
   m w eps = m cosh(a) eps + m sinh(a), first variation N m, second -N m^2 <1/E>.
Exact arithmetic (integers, fractions, sympy); the probe's floating-point families are not used. The runner scans its own
source for floating-point literals.
"""

from __future__ import annotations

import itertools
import math
import random
import re
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_MASSIVE_FREE_SEA_KEEPS_A_POSITIVE_CLOCK_STIFFNESS_FOR_EVERY_MASS_AND_A_MASS_MAKES_A_CHESSBOARD_OF_CLOCKS_VISIBLE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_massive_free_sea_keeps_a_positive_clock_stiffness_for_every_mass_and_a_mass_makes_a_chessboard_of_clocks_visible_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    (2, "Moreover `phi(K+m eps)phi=phi K phi+m w eps`."),
    (2, "Numerical packet and massive-sea experiments are deferred."),
    (3, "The filled negative-level energy is E_-=sum_{lambda<0}lambda of this finite matrix."),
    (3, "At a point where E_- has a Hessian in u, that Hessian annihilates eps."),
    (3, "They are inputs, not derived sea coefficients."),
    (4, "(b) `V_nHV_n = s_nH`, and `V_n(φHφ)V_n = s_n φHφ` for every rate field."),
    (5, "`e_x[A_nψ] = −e_x[ψ]`"),
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "twin_sign_forged": "B",
    "overlap_sign_forged": "C",
    "moment_forged": "D",
    "line_limit_forged": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its mass, its clocks and the sea are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[2] = (3, "The filled negative-level energy is E_+=sum_{lambda>0}lambda of this finite matrix.")
    checks.check("A3", all(nd in texts[i] for i, nd in needles), "landed blocks 70, 71, 76 and 77 carry the quoted lines: the clocked massive walk phi(K + m eps)phi = phi K phi + m w eps; the massive-sea experiments deferred; the filled sea E_- and its Hessian annihilating eps; c and kappa as inputs, not derived; the exchange maps; the twins")


# ============================================================================================ family B (maps and twins on the 4^3 torus, exact)
L = 4
NS = L ** 3
SITES = list(itertools.product(range(L), repeat=3))
IDX = {x: i for i, x in enumerate(SITES)}


def shf(x, a, dd):
    y = list(x)
    y[a] = (y[a] + dd) % L
    return tuple(y)


SIGR = [np.array([[0, 1], [1, 0]]), None, np.array([[1, 0], [0, -1]])]
S2IM = np.array([[0, -1], [1, 0]])                    # sigma_2 = i * S2IM


def zeros():
    return np.zeros((2 * NS, 2 * NS), dtype=np.int64)


def build_k():
    """K = 2H = sum_a sigma_a (T_a - T_a^-1)/i as (real, imaginary) integer matrices."""
    kre, kim = zeros(), zeros()
    for x in SITES:
        i = IDX[x]
        for a in range(3):
            for dd, sgn in ((1, 1), (-1, -1)):
                j = IDX[shf(x, a, dd)]
                if a == 1:
                    kre[2 * i:2 * i + 2, 2 * j:2 * j + 2] += sgn * S2IM
                else:
                    kim[2 * i:2 * i + 2, 2 * j:2 * j + 2] += -sgn * SIGR[a]
    return (kre, kim)


def cmul(A, B):
    return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])


def ceq(A, B):
    return np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1])


def cneg(A):
    return (-A[0], -A[1])


def tmat(a):
    A = zeros()
    for x in SITES:
        A[2 * IDX[x]:2 * IDX[x] + 2, 2 * IDX[shf(x, a, -1)]:2 * IDX[shf(x, a, -1)] + 2] = np.eye(2, dtype=np.int64)
    return (A, zeros())


def vmap(n):
    s = np.array([(-1) ** (n[0] * x[0] + n[1] * x[1] + n[2] * x[2]) for x in SITES])
    D = [(-1) ** v for v in n]
    sgn = D[0] * D[1] * D[2]
    rho = [sgn * dv for dv in D]
    if all(r == 1 for r in rho):
        Rm = (np.eye(2, dtype=np.int64), np.zeros((2, 2), np.int64))
    else:
        ax = rho.index(1)
        Rm = [(SIGR[0], np.zeros((2, 2), np.int64)), (np.zeros((2, 2), np.int64), S2IM), (SIGR[2], np.zeros((2, 2), np.int64))][ax]
    U = np.kron(np.diag(s), np.eye(2, dtype=np.int64))
    return (U @ np.kron(np.eye(NS, dtype=np.int64), Rm[0]), U @ np.kron(np.eye(NS, dtype=np.int64), Rm[1])), sgn


def apply_sigma(a, v):
    (r0, i0), (r1, i1) = v
    if a == 0:
        return ((r1, i1), (r0, i0))
    if a == 1:
        return ((i1, -r1), (-i0, r0))
    return ((r0, i0), (-r1, -i1))


def hw_apply(psi, phi, w, m):
    out = {}
    for x in SITES:
        acc = [[F(0), F(0)], [F(0), F(0)]]
        for a in range(3):
            xp, xm = shf(x, a, 1), shf(x, a, -1)
            vp, vm = apply_sigma(a, psi[xp]), apply_sigma(a, psi[xm])
            for c in range(2):
                re_ = phi[x] * (phi[xp] * vp[c][0] - phi[xm] * vm[c][0])
                im_ = phi[x] * (phi[xp] * vp[c][1] - phi[xm] * vm[c][1])
                acc[c][0] += im_ / 2
                acc[c][1] += -re_ / 2
        e = (-1) ** sum(x)
        for c in range(2):
            acc[c][0] += m * w[x] * e * psi[x][c][0]
            acc[c][1] += m * w[x] * e * psi[x][c][1]
        out[x] = ((acc[0][0], acc[0][1]), (acc[1][0], acc[1][1]))
    return out


def edens(psi, phi, m):
    w = {x: phi[x] * phi[x] for x in SITES}
    hp = hw_apply(psi, phi, w, m)
    return {x: sum(psi[x][c][0] * hp[x][c][0] + psi[x][c][1] * hp[x][c][1] for c in range(2)) for x in SITES}


def family_b(checks: Checks) -> None:
    Kc = build_k()
    epsv = np.array([(-1) ** sum(x) for x in SITES])
    EPS = (np.kron(np.diag(epsv), np.eye(2, dtype=np.int64)), zeros())
    ok1 = ceq(cmul(EPS, Kc), cneg(cmul(Kc, EPS))) and all(not Kc[0][2 * i:2 * i + 2, 2 * i:2 * i + 2].any() and not Kc[1][2 * i:2 * i + 2, 2 * i:2 * i + 2].any() for i in range(NS))
    T0m = tmat(0)
    T0i = (T0m[0].T.copy(), zeros())
    ok1 &= ceq(cmul(cmul(T0m, Kc), T0i), Kc) and ceq(cmul(cmul(T0m, EPS), T0i), cneg(EPS))
    allv = oddsym = True
    for n in itertools.product((0, 1), repeat=3):
        V, sgn = vmap(n)
        allv &= ceq(cmul(cmul(V, Kc), V), Kc if sgn == 1 else cneg(Kc)) and ceq(cmul(cmul(V, EPS), V), EPS)
        if sgn == -1:
            EV = cmul(EPS, V)
            oddsym &= ceq(cmul(cmul(EV, Kc), (EV[0].T.copy(), -EV[1].T.copy())), Kc)
    TW = cmul(EPS, T0m)
    TWi = (TW[0].T.copy(), -TW[1].T.copy())
    twin_op = ceq(cmul(cmul(TW, Kc), TWi), cneg(Kc)) and ceq(cmul(cmul(TW, EPS), TWi), cneg(EPS))
    checks.check("B1", ok1 and allv and oddsym and twin_op, "on the 4^3 torus, exactly: eps anticommutes with H and H has no site-diagonal block; the one-site translation keeps H and flips eps; every exchange map V_n keeps eps, V_n H V_n = s_n H, and for odd n eps V_n commutes with H + m eps; eps T maps H + m eps to -(H + m eps)")
    rnd = random.Random(20260925)

    def gq():
        return (F(rnd.randint(-9, 9), rnd.randint(1, 7)), F(rnd.randint(-9, 9), rnd.randint(1, 7)))
    phi = {x: F(rnd.randint(1, 9), rnd.randint(1, 9)) for x in SITES}
    psi = {x: (gq(), gq()) for x in SITES}
    mm = F(7, 5)
    phiT = {x: phi[shf(x, 0, -1)] for x in SITES}
    chi = {x: tuple(((-1) ** sum(x) * psi[shf(x, 0, -1)][c][0], (-1) ** sum(x) * psi[shf(x, 0, -1)][c][1]) for c in range(2)) for x in SITES}
    e1 = edens(psi, phi, mm)
    e2 = edens(chi, phiT, mm)
    sgn = 1 if mut("twin_sign_forged") else -1
    ok_twin = all(e2[x] == sgn * e1[shf(x, 0, -1)] for x in SITES)

    def theta_eps(ps):
        out = {}
        for x in SITES:
            e = (-1) ** sum(x)
            (r0, i0), (r1, i1) = ps[x]
            c0, c1 = (e * r0, -e * i0), (e * r1, -e * i1)
            out[x] = ((c1[1], -c1[0]), (-c0[1], c0[0]))
        return out
    eA = edens(theta_eps(psi), phi, mm)
    ok71 = all(eA[x] + e1[x] == 2 * mm * phi[x] ** 2 * (-1) ** sum(x) * sum(psi[x][c][0] ** 2 + psi[x][c][1] ** 2 for c in range(2)) for x in SITES) and any(eA[x] + e1[x] != 0 for x in SITES)
    checks.check("B2", ok_twin and ok71, "exact, with a rational rate field, m = 7/5 and a Gaussian-rational state on the 4^3 torus: the twin eps T carries a state in the field phi to one in T phi with e_x[eps T psi; T phi] = -e_{x-e1}[psi; phi] at every site; block 71's on-site twin Theta V_111 fails with a mass: e[A psi] + e[psi] = 2 m w eps |psi|^2, nonzero")


# ============================================================================================ family C (the sea, exact algebra)
def family_c(checks: Checks) -> None:
    m, E, Ep = sp.symbols("m E Ep", positive=True)
    s = sp.symbols("s1:4", real=True)
    t = sp.symbols("t1:4", real=True)
    sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])

    def blk(v):
        Sd = v[0] * sx + v[1] * sy + v[2] * sz
        return sp.Matrix(sp.BlockMatrix([[Sd, m * sp.eye(2)], [m * sp.eye(2), -Sd]]))
    Mk, Mq = blk(s), blk(t)
    sub = {E: sp.sqrt(sum(v ** 2 for v in s) + m ** 2), Ep: sp.sqrt(sum(v ** 2 for v in t) + m ** 2)}
    ok_sq = sp.simplify(Mk * Mk - (sum(v ** 2 for v in s) + m ** 2) * sp.eye(4)) == sp.zeros(4)
    Pm = (sp.eye(4) - Mk / E) / 2
    ok_pm = (Pm * Mk - (Mk - E * sp.eye(4)) / 2).applyfunc(lambda z: sp.simplify(sp.expand(z).subs(sub))) == sp.zeros(4)
    ok_tr = (Mk[0, 2] + Mk[1, 3]) == 2 * m
    checks.check("C1", ok_sq and ok_pm and ok_tr, "in the (k, k+Q) block M(k) = [[s.sigma, m], [m, -s.sigma]]: M^2 = (|s|^2 + m^2) I, so the levels pair at +-E; P_- M = (M - E)/2; the mass block's coin trace is 2m: the filled sea's energy density at uniform clocks is m eps_x - <E>")
    okov = True
    for a_, b_ in ((-1, -1), (-1, 1)):
        Pa = (sp.eye(4) + a_ * Mk / E) / 2
        Pb = (sp.eye(4) + b_ * Mq / Ep) / 2
        trv = sp.expand((Pa * Pb).trace())
        sg = -1 if mut("overlap_sign_forged") else 1
        target = 1 + sg * a_ * b_ * (sum(x * y for x, y in zip(s, t)) + m ** 2) / (E * Ep)
        okov &= sp.simplify(trv - target) == 0
    c = sp.symbols("c", real=True)
    Foo = -sp.Rational(1, 4) * (E + Ep) * (1 + c)
    Fou = lambda Ei, Ej: sp.Rational(1, 2) * Ei * (Ej - Ei) / (Ei + Ej) * (1 - c)
    G = 2 * Foo + Fou(E, Ep) + Fou(Ep, E)
    okG = sp.simplify(G + sp.Rational(1, 2) * ((E + Ep) * (1 + c) + (1 - c) * (E - Ep) ** 2 / (E + Ep))) == 0
    okme = sp.simplify(((-E + Ep) ** 2 / (4 * (-E - Ep)) + (-E + Ep) / 4) - E * (Ep - E) / (2 * (E + Ep))) == 0
    checks.check("C2", okov and okG and okme, "projector overlaps tr P_a(k) P_b(k') = 1 + ab (s.s' + m^2)/(E E'); the first-order element of {u, H}/2 is (lam_i + lam_j)/2 <j|u|i>; the symmetrized second-order weight is G = -(1/2)[(E + E')(1 + n.n') + (1 - n.n')(E - E')^2/(E + E')], whose first part is the held sea's")
    k1, k2, k3 = sp.symbols("k1:4", real=True)
    sv = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3), m])
    En = sp.sqrt(sv[0] ** 2 + sv[1] ** 2 + sv[2] ** 2 + m ** 2)
    nv = sv / En
    dn = nv.diff(k1)
    lhs = sp.simplify((dn.T * dn)[0] - sp.cos(k1) ** 2 * (En ** 2 - sp.sin(k1) ** 2) / En ** 4)
    Sb, Jb = sp.symbols("S J", positive=True)
    beta_val = -Sb / 3
    c0 = 3 * beta_val - m ** 2 * Jb
    ok_held = held_sea_kernel_check() and sp.simplify(c0 + (Sb + m ** 2 * Jb)) == 0
    checks.check("C4", ok_held, "the held sea: expanding E_fix = beta sum_bonds e^((u_x+u_y)/2) + sum_x e^(u_x)(m eps_x - m^2 J) for u = a cos(q.x) gives Pi_fix = 3 beta/4 - m^2 J/4 - (beta/16)|q|^2_lat; with beta = -<|s|^2/E>/3 and J = <1/E>, c0 = 3 beta - m^2 J = -(<|s|^2/E> + m^2 <1/E>) = -<E> and kappa = -beta/4 = <|s|^2/E>/12")
    checks.check("C3", lhs == 0 and sp.simplify(En.diff(k1) - sp.sin(k1) * sp.cos(k1) / En) == 0, "the remainder bounds: |d_j n|^2 = cos^2 k_j (E^2 - sin^2 k_j)/E^4 <= 1/m^2 and d_j E = sin k_j cos k_j / E, so 1 - n.n' <= 3|q|^2/(2m^2), (E - E')^2 <= 3|q|^2, and the free sea's extra term lies in [-9|q|^4/(64|m|^3), 0]")


def held_sea_kernel_check() -> bool:
    """The held sea E_fix[u] = beta sum_bonds e^((u_x + u_y)/2) + sum_x e^(u_x)(m eps_x - m^2 J), expanded to second order in
    u = a cos(q.x) and averaged per site (the eps term averages out for 2q not 0 or Q): a^2 [3 beta/4 - m^2 J/4 - (beta/16)|q|^2_lat]."""
    a, th, beta, J, m = sp.symbols("a theta beta J m", real=True)
    q = sp.symbols("q1:4", real=True)
    per = 0
    for j in range(3):
        per += beta * sp.exp((a * sp.cos(th) + a * sp.cos(th + q[j])) / 2)
    per += sp.exp(a * sp.cos(th)) * (-m ** 2 * J)
    second = sp.series(per, a, 0, 3).removeO().coeff(a, 2)
    avg = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(second)), (th, 0, 2 * sp.pi)) / (2 * sp.pi))
    qlat = sum(2 * (1 - sp.cos(qq)) for qq in q)
    return sp.simplify(avg - (3 * beta / 4 - m ** 2 * J / 4 - beta / 16 * qlat)) == 0


# ============================================================================================ family D (the stiffness and the chessboard)
def smom(n):
    tot = F(0)
    for a in range(n + 1):
        for b in range(n - a + 1):
            c3 = n - a - b
            tot += F(math.factorial(n), math.factorial(a) * math.factorial(b) * math.factorial(c3)) * F(math.comb(2 * a, a), 4 ** a) * F(math.comb(2 * b, b), 4 ** b) * F(math.comb(2 * c3, c3), 4 ** c3)
    return tot


def family_d(checks: Checks) -> None:
    mom = {n: smom(n) for n in range(1, 4)}
    tgt = (F(3, 2), F(23, 8) if mut("moment_forged") else F(21, 8), F(81, 16))
    cj = lambda j: F((-1) ** j * math.comb(2 * j, j), 4 ** j)
    ser = [F(1, 12) * cj(j) * mom[j + 1] for j in range(3)]
    checks.check("D1", (mom[1], mom[2], mom[3]) == tgt and ser == [F(1, 8), F(-7, 64), F(81, 512)], "exact zone moments <|s|^2> = 3/2, <|s|^4> = 21/8, <|s|^6> = 81/16, so for m > sqrt3 kappa(m) = (1/12)<|s|^2/sqrt(|s|^2 + m^2)> = 1/(8m) - 7/(64 m^3) + 81/(512 m^5) - ... (an alternating series whose partial sums bracket it)")

    def enclose(mv, J):
        part = F(0)
        sums = []
        for j in range(J + 1):
            part += F(1, 12) * cj(j) * smom(j + 1) / mv ** (2 * j + 1)
            sums.append(part)
        return min(sums[-1], sums[-2]), max(sums[-1], sums[-2])
    ok_enc = True
    for mv, J in ((F(4), 24), (F(2), 70)):
        lo, hi = enclose(mv, J)
        ok_enc &= hi - lo < F(1, 10 ** 10) and lo > 0
    checks.check("D2", ok_enc, "exact rational enclosures of kappa(2) and kappa(4), each of width below 10^-10 and positive")
    m, aa, ss2 = sp.symbols("m a s2", positive=True)
    Ea = m * sp.sinh(aa) - sp.sqrt(ss2 + m ** 2 * sp.cosh(aa) ** 2)
    ok_var = sp.simplify(Ea.diff(aa).subs(aa, 0) - m) == 0 and sp.simplify(Ea.diff(aa, 2).subs(aa, 0) + m ** 2 / sp.sqrt(ss2 + m ** 2)) == 0
    cc = F(3, 2)
    ch = (cc ** 2 + 1 / cc ** 2) / 2
    shh = (cc ** 2 - 1 / cc ** 2) / 2
    phiC = {x: (cc if (-1) ** sum(x) == 1 else 1 / cc) for x in SITES}
    wC = {x: phiC[x] ** 2 for x in SITES}
    ok_cb = all(phiC[x] * phiC[shf(x, a, 1)] == 1 for x in SITES for a in range(3)) and all(wC[x] * (-1) ** sum(x) == ch * (-1) ** sum(x) + shh for x in SITES)
    checks.check("D3", ok_var and ok_cb, "a chessboard of clocks phi = c^eps: phi_x phi_y = 1 on every bond and m w eps = m cosh(a) eps + m sinh(a) (exact on the 4^3 torus); per mode E(a) = m sinh a - sqrt(|s|^2 + m^2 cosh^2 a), whose first variation is m and second -m^2/E: with a mass the chessboard is not invisible")


# ============================================================================================ family E (T5, the massless sea: harvest of #8716, confirmed by #9321)
def family_e(checks: Checks) -> None:
    import random as _random
    rng = _random.Random(20260923)

    def runit():
        a = F(rng.randint(-9, 9), rng.randint(1, 9))
        b = F(rng.randint(-9, 9), rng.randint(1, 9))
        n = a * a + b * b + 1
        return (2 * a / n, 2 * b / n, (a * a + b * b - 1) / n)
    SIGm = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

    def proj(n, sgn):
        return (sp.eye(2) + sgn * sum((sp.Rational(n[i]) * SIGm[i] for i in range(3)), sp.zeros(2))) / 2
    good = True
    for _ in range(6):
        a, b = runit(), runit()
        trv = sp.simplify((proj(a, 1) * proj(b, -1)).trace())
        good &= trv == sp.Rational(1, 2) * (1 - sum(sp.Rational(a[i]) * sp.Rational(b[i]) for i in range(3)))
    for L in (4, 6):
        cosL = {m: {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}[m] if L == 4 else {0: F(1), 1: F(1, 2), 2: F(-1, 2), 3: F(-1), 4: F(-1, 2), 5: F(1, 2)}[m] for m in range(L)}
        Xs = list(itertools.product(range(L), repeat=3))
        for n in itertools.product(range(L), repeat=3):
            if n == (0, 0, 0):
                continue
            c = {x: cosL[sum(p * q for p, q in zip(n, x)) % L] for x in Xs}
            lin = sum(c[x] + c[tuple((x[i] + (i == a)) % L for i in range(3))] for x in Xs for a in range(3))
            quad = sum((c[x] + c[tuple((x[i] + (i == a)) % L for i in range(3))]) ** 2 for x in Xs for a in range(3))
            mult = 2 if all((2 * m) % L == 0 for m in n) else 1
            good &= lin == 0 and quad == mult * len(Xs) * (3 + sum(cosL[m] for m in n))
    checks.check("E1", good, "massless sea: the coin overlap |<u_+(k')|u_-(k)>|^2 = (1 - n'.n)/2 (rational unit vectors), and on every mode of the 4^3 and 6^3 tori sum_bonds (u_x + u_y) = 0, sum_bonds (u_x + u_y)^2 = eps^2 N (3 + sum_a cos q_a): the held sea's kernel is (beta/8)(3 + sum cos q_a), kappa_held = -beta/4 = I/12 with I = <|sin k|>")
    a_, b_, c_ = sp.symbols("a b c", real=True)
    vec = sp.expand(4 * (a_ ** 2 + b_ ** 2 - 2 * a_ * b_ * c_) - 2 * (1 - c_) * (a_ + b_) ** 2 - 2 * (1 + c_) * (a_ - b_) ** 2) == 0
    vec &= sp.expand(2 - 2 * c_ - (1 - c_ ** 2) - (1 - c_) ** 2) == 0
    qq, r_ = sp.symbols("q r", positive=True)
    r0, Rm = sp.pi * qq / 2, sp.pi * sp.sqrt(3) / 2
    up = sp.integrate(qq * 4 * sp.pi * r_ ** 2, (r_, 0, r0)) + sp.integrate(sp.pi ** 3 * qq ** 4 / (8 * r_ ** 3) * 4 * sp.pi * r_ ** 2, (r_, r0, Rm))
    upper = sp.simplify(up - sp.pi ** 4 * qq ** 4 * (sp.Rational(1, 6) + sp.log(sp.sqrt(3) / qq) / 2)) == 0 and sp.simplify(sp.pi ** 3 * qq ** 4 / (8 * r0 ** 3) - qq) == 0
    dc = F(431, 512) * F(1535, 1536)
    Kc = sp.Rational(dc.numerator, dc.denominator) ** 4 * sp.Rational(23, 24) ** 4 * sp.Rational(32, 1125) * sp.Rational(4, 15) / 8     # C = Kc / pi^2
    low = (1 - F(9, 16) ** 2 / 2 == F(431, 512)) and (1 - F(1, 16) ** 2 / 6 == F(1535, 1536)) and (1 - F(1, 2) ** 2 / 6 == F(23, 24))
    low &= sp.integrate(2 * sp.pi * c_ ** 2 * (1 - c_ ** 2), (c_, 0, 1)) == 4 * sp.pi / 15
    low &= (F(5, 2) ** 3 * F(9, 4) == F(1125, 32)) and Kc * sp.Rational(49, 484) > sp.Rational(4, 100000)       # pi^2 < (22/7)^2 = 484/49
    checks.check("E2", vec and upper and low, "two-sided bounds on the free sea's deficit below the held sea near q = 0: the vector identity 4(a^2 + b^2 - 2abc) - 2(1 - c)(a + b)^2 = 2(1 + c)(a - b)^2; the upper bound -8 dPi <= pi |q|^4 (1/6 + log(sqrt3/|q|)/2) from the cell integral; the lower bound C t^4 log(1/(4t)) <= -8 dPi(t e1) for t <= 1/8 with an exact positive C (> 4/10^5 using pi < 22/7): so dPi/|q|^2 -> 0 and kappa_free = kappa_held = I/12, with a long-ranged |q|^4 log(1/|q|) difference")
    h, q1 = sp.symbols("h q", positive=True)
    Gd = sp.log(1 / sp.cos(h) + sp.tan(h)) - sp.sin(h)
    line = sp.simplify(sp.diff(Gd, h) - sp.sin(h) ** 2 / sp.cos(h)) == 0
    dPi1 = -(sp.cos(q1 / 2) ** 2 / (2 * sp.pi * sp.sin(q1 / 2))) * Gd.subs(h, q1 / 2)
    g1 = 1 / (4 * sp.pi) + dPi1 / (1 - sp.cos(q1))
    lim0 = sp.Rational(1, 4) if mut("line_limit_forged") else sp.Rational(1, 6)
    line &= sp.simplify(sp.series(dPi1, q1, 0, 4).removeO() + q1 ** 2 / (24 * sp.pi)) == 0
    line &= sp.simplify(sp.limit(g1, q1, 0, "+") - lim0 / sp.pi) == 0 and sp.simplify(sp.limit(g1, q1, sp.pi, "-") - 1 / (4 * sp.pi)) == 0
    checks.check("E3", line, "on a line, in closed form: dPi(q) = -(cos^2(q/2)/(2 pi sin(q/2)))[ln(sec + tan)(q/2) - sin(q/2)] = -q^2/(24 pi) + O(q^4), so the free sea is softer by a third there (1/(6 pi) against 1/(4 pi) in g, kappa 1/(3 pi) against 1/(2 pi))")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 55, 70, 71, 76 and 77 as landed on main (the energy density, the exchange maps and twins, the filled sea and the clocked walk with a staggered mass); it reports the massive free sea's density and clock stiffness exactly, and what a mass does to the chessboard of clocks; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at every mass."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Ivanenko", "Belinfante", "Rosenfeld", "Cartan", "Kibble",
                   "Sciama", "Hehl", "Wilson", "Pauli", "Fierz", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton",
                   "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Weyl) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the operator identities of the massive walk on the 4^3 torus (maps, twins, translation), exactly",
    "per_site: executed - the twin's energy density and block 71's on-site twin with a mass, site by site, exactly",
    "per_mode: executed - the (k, k+Q) block algebra, projector overlaps, the second-order weight and the remainder bounds",
    "per_block: executed - the zone moments, the stiffness series and the exact enclosures of kappa(2), kappa(4); the chessboard",
    "lattice_wide: checked and not executed - brute-force diagonalization and torus averages (the probe's floating-point families), the kernel at q = Q, the projected sea",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: the massive free sea of H + m eps with clocks: density m eps_x - <E>; clock stiffness kappa(m) = <|s|^2/sqrt(|s|^2 + m^2)>/12 > 0 for every m; the twin eps T; a mass makes the chessboard of clocks visible; harvest of #9210 (confirmed by #9295); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
