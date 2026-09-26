#!/usr/bin/env python3
"""Exact checks: every clock profile a relabelling forces the whole momentum constraint, and no positive inertia can be
added to the member - within block 112's lattice bracket of the member's lapse constraints (flat strain, the term linear in
canonical momentum, symmetric face timing), block 124's kinetic family, block 144's drifting relabellings and block 54's walk
with block 139's staggered mass, all as landed on main: the relabelling fields xi(M, N) of block 112 span every bond field, while
a uniform lapse gives only gradients; a cubic-only kinetic term takes the bracket out of the relabellings' span for every kinetic
ratio; the closing line (gamma = 0, beta = -alpha) is indefinite on uniform strains, so no nonzero positive semidefinite
kinetic term lies on it; the walker sea's adiabatic inertia on uniform strains is positive semidefinite and nonzero, with no
dilation part at mu = 0 and its own ratio beta/alpha in (-1, 0); on the walker's side, with the lapse coupled to
block 135's e' and block 136's momentum placement, the bracket closes with block 112's xi exactly when one lapse is uniform
(K/(4 alpha) = 1), and for general lapse pairs only through second order in their wave numbers (the supervisor's own
derivation; not adopted).

B (T1): delta lapses at a bond's ends give that bond alone; the bracket equals that bond's relabelling; a uniform lapse gives gradients.
C (T2): block 112's bracket with a cubic-only kinetic term misses the relabellings' span for every ratio.
D (T3): the kinetic family on uniform strains; the closing line is indefinite; positive semidefinite forms on it vanish.
E (T4): the sea's adiabatic inertia on uniform strains: the matrix elements with and without the staggered mass; positivity;
       the dilation at mu = 0; the average over the axis permutations; the member plus the sea is off the closing line.
H (T5): the walker's side: one lapse uniform (exact, with a control); delta lapses two steps apart; no c at rational points;
       the defect's third-order form for every k and all directions; no finite-range placement closes it (the extreme-hop witness).
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_every_clock_profile_a_relabelling_forces_the_whole_momentum_constraint_and_no_positive_inertia_can_be_added_to_the_member_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "one_corner_timing": "B",
    "uniform_lapse_taken_as_every": "B",
    "cubic_only_term_ignored": "C",
    "closing_trace_sign_flipped": "D",
    "inertia_sign_flipped": "E",
    "permutation_average_forged": "E",
    "walker_first_order_c_forged": "H",
    "delta_lapses_adjacent": "H",
    "third_order_form_forged": "H",
    "placement_extremes_adjacent": "H",
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
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


F = Fraction
ZERO = F(0)
PAIRS = ((0, 1), (0, 2), (1, 2))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the clocks, the lengths, the kinetic term, the walk and its sea are supplied; the memo does not define a time metric)")


# ============================================================================================ lattice helpers (block 112's placement)
def unit(j):
    return tuple(1 if k == j else 0 for k in range(3))


def torus(side):
    sites = list(product(range(side), repeat=3))

    def sh(x, v, s=1):
        return tuple((x[k] + s * v[k]) % side for k in range(3))
    return sites, sh


def lapse_bracket(sites, sh, n, m, a_diag, a_face, c, timing):
    """Momentum coefficients of B[N, M] = sum over strains of dR1[N]/dh times dkin[M]/dP, as in block 112 (landed), with the
    diagonal kinetic block a_diag = alpha + gamma and the faces a_face = alpha (gamma the cubic-only term)."""
    coef = {}
    for x in sites:
        second = [n[sh(x, unit(i))] - 2 * n[x] + n[sh(x, unit(i), -1)] for i in range(3)]
        grads = [-sum(second, ZERO) + second[j] for j in range(3)]
        total = sum(grads, ZERO)
        for j in range(3):
            coef[("d", x, j)] = m[x] / (2 * a_diag) * (grads[j] - c * total)
    for y in sites:
        for (i, j) in PAIRS:
            corners = {"four": [y, sh(y, unit(i)), sh(y, unit(j)), sh(sh(y, unit(i)), unit(j))], "one": [y]}[timing]
            mean = sum((m[z] for z in corners), ZERO) / len(corners)
            mixed = n[y] - n[sh(y, unit(i))] - n[sh(y, unit(j))] + n[sh(sh(y, unit(i)), unit(j))]
            coef[("f", y, (i, j))] = mean / (4 * a_face) * 2 * mixed
    return coef


def relabelling(sites, sh, xi):
    """Momentum coefficients of G[xi] = sum P.(d_i xi_j + d_j xi_i), xi_j on the bond from x to x + e_j (block 112)."""
    coef = {}
    for x in sites:
        for j in range(3):
            coef[("d", x, j)] = 2 * (xi[(x, j)] - xi[(sh(x, unit(j), -1), j)])
    for y in sites:
        for (i, j) in PAIRS:
            coef[("f", y, (i, j))] = xi[(sh(y, unit(i)), j)] - xi[(y, j)] + xi[(sh(y, unit(j)), i)] - xi[(y, i)]
    return coef


def closing_field(sites, sh, n, m, alpha, kk):
    return {(x, j): kk / (4 * alpha) * (n[sh(x, unit(j))] * m[x] - n[x] * m[sh(x, unit(j))]) for x in sites for j in range(3)}


def bracket(sites, sh, n, m, a_diag, a_face, kk, c, timing="four"):
    b1 = lapse_bracket(sites, sh, n, m, a_diag, a_face, c, timing)
    b2 = lapse_bracket(sites, sh, m, n, a_diag, a_face, c, timing)
    return {k: kk * (b1[k] - b2[k]) for k in b1}


def rank_of(rows):
    rows = [list(r) for r in rows]
    rank, col = 0, 0
    ncols = len(rows[0]) if rows else 0
    while rank < len(rows) and col < ncols:
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [v / pv for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [a - fac * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
        col += 1
    return rank


def delta(sites, at):
    return {x: (F(1) if x == at else ZERO) for x in sites}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    alpha, kk = F(3, 7), F(5, 11)
    sites, sh = torus(3)
    bonds = [(x, j) for x in sites for j in range(3)]
    fields, single, brackets_ok = [], True, True
    timing = "one" if mut("one_corner_timing") else "four"
    for (x, j) in bonds:
        m, n = delta(sites, x), delta(sites, sh(x, unit(j)))
        xi = closing_field(sites, sh, n, m, alpha, kk)
        support = [b for b in bonds if xi[b] != 0]
        single = single and support == [(x, j)] and xi[(x, j)] == kk / (4 * alpha)
        fields.append([xi[b] for b in bonds])
        if (x, j) in bonds[:12]:
            lin = bracket(sites, sh, n, m, alpha, alpha, kk, F(1, 2), timing)
            g = relabelling(sites, sh, xi)
            brackets_ok = brackets_ok and all(lin[k] == g[k] for k in lin)
    full = rank_of(fields)
    checks.check("B1", single and full == len(bonds),
                 f"on the 3^3 torus, lapses M = delta at x and N = delta at x + e_j give block 112's xi(M, N) = K/(4 alpha) on that bond alone, for all {len(bonds)} bonds: the xi(M, N) span every bond field (rank {full})")
    checks.check("B2", brackets_ok,
                 "for twelve of these pairs, block 112's bracket {C[N], C[M]} (the term linear in momenta at flat strain, beta = -alpha, faces timed by the mean of their four corners) is exactly the relabelling generator of that single bond")
    one = {x: F(1) for x in sites}
    grads = []
    for y in sites:
        xi = closing_field(sites, sh, one, delta(sites, y), alpha, kk)
        grads.append([xi[b] for b in bonds])
    r_uniform = rank_of(grads)
    gvals = {b: F((3 * b[0][0] + 5 * b[0][1] + 7 * b[0][2] + 11 * b[1]) % 13 - 6, 5) for b in bonds}
    mvals = {x: F((2 * x[0] + x[1] * x[2] + 1) % 7 - 3, 3) for x in sites}
    xi_u = closing_field(sites, sh, one, mvals, alpha, kk)
    lhs = sum((xi_u[b] * gvals[b] for b in bonds), ZERO)
    div = {x: sum((gvals[(x, j)] - gvals[(sh(x, unit(j), -1), j)] for j in range(3)), ZERO) for x in sites}
    rhs = kk / (4 * alpha) * sum((mvals[x] * div[x] for x in sites), ZERO)
    claimed = len(bonds) if mut("uniform_lapse_taken_as_every") else len(sites) - 1
    checks.check("B3", r_uniform == claimed and lhs == rhs,
                 f"with a uniform lapse N = 1, xi(M, 1) = -(K/(4 alpha)) times the forward difference of M: over all M these span only the gradients (rank {r_uniform} = sites - 1), and G[xi(M, 1)] = (K/(4 alpha)) sum_x M_x (backward divergence of the constraint)(x) exactly")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    alpha, kk = F(3, 7), F(5, 11)
    sites, sh = torus(3)
    n, m = delta(sites, (0, 0, 0)), delta(sites, (1, 0, 0))
    keys = sorted(bracket(sites, sh, n, m, alpha, alpha, kk, F(1, 2)))
    cols = []
    for x in sites:
        for j in range(3):
            xi = {(z, l): (F(1) if (z, l) == (x, j) else ZERO) for z in sites for l in range(3)}
            g = relabelling(sites, sh, xi)
            cols.append([g[k] for k in keys])
    base = rank_of(cols)
    b0 = bracket(sites, sh, n, m, alpha, alpha, kk, F(1, 2))
    control = rank_of(cols + [[b0[k] for k in keys]]) == base
    misses = []
    for gam in (F(1, 5), F(-1, 7), F(2, 3)):
        a_diag = alpha if mut("cubic_only_term_ignored") else alpha + gam
        bz = bracket(sites, sh, n, m, a_diag, alpha, kk, ZERO)
        bo = bracket(sites, sh, n, m, a_diag, alpha, kk, F(1))
        misses.append(rank_of(cols + [[bz[k] for k in keys], [bo[k] - bz[k] for k in keys]]) - base)
    checks.check("C1", control, "control: with no cubic-only term, at c = 1/2 the bracket for lapses at 0 and e1 lies in the span of the relabellings (block 112)")
    checks.check("C2", misses == [2, 2, 2],
                 f"with a cubic-only kinetic term gamma sum hdot_ii^2 (diagonal block alpha + gamma, faces alpha), gamma = 1/5, -1/7, 2/3: the bracket is affine in c = beta/(alpha + gamma + 3 beta) and the whole line misses the relabellings' span (rank {base} -> {base} + {misses}); no kinetic ratio closes the algebra unless gamma = 0")


# ============================================================================================ family D
AL, BE, GA = sp.symbols("alpha beta gamma", real=True)
VA = sp.eye(3)
VE = sp.diag(1, -1, 0)
VT = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])


def kinetic(v, a, b, g):
    return a * (v * v).trace() + b * v.trace() ** 2 + g * sum(v[i, i] ** 2 for i in range(3))


def family_d(checks: Checks) -> None:
    vals = [sp.expand(kinetic(v, AL, BE, GA)) for v in (VA, VE, VT)]
    checks.check("D1", vals == [sp.expand(3 * AL + 9 * BE + 3 * GA), sp.expand(2 * AL + 2 * GA), 2 * AL],
                 "block 124's kinetic family with a cubic-only term, alpha tr(v^2) + beta (tr v)^2 + gamma sum v_ii^2, takes 3 alpha + 9 beta + 3 gamma, 2 alpha + 2 gamma and 2 alpha on the dilation, the E strain diag(1, -1, 0) and the T strain (e1 e2 + e2 e1)")
    bsign = 1 if mut("closing_trace_sign_flipped") else -1
    line = [sp.expand(x.subs({BE: bsign * AL, GA: 0})) for x in vals]
    lam = sp.Symbol("lambda", real=True)
    a_s, e_s, t_s = sp.symbols("a_A a_E a_T", nonnegative=True)
    sols = sp.solve([lam * line[0] / AL - a_s, lam * line[1] / AL - e_s, lam * line[2] / AL - t_s], [lam, a_s, e_s], dict=True)
    # on the line: a_A = lam * (value on A)/alpha must be >= 0 and a_T = lam * (value on T)/alpha >= 0; opposite signs force lam = 0
    opposite = sp.sign(line[0].subs(AL, 1)) * sp.sign(line[2].subs(AL, 1)) == -1
    checks.check("D2", line[2] == 2 * AL and opposite and len(sols) == 1,
                 f"the closing line gamma = 0, beta = -alpha takes {line[0]}, {line[1]}, {line[2]} on (A, E, T): opposite signs on the dilation and the T strain, so a positive semidefinite kinetic term lies on the line only if it vanishes on both, hence on all three")


# ============================================================================================ family E
s1, s2, s3, a1, a2, a3 = sp.symbols("s1 s2 s3 a1 a2 a3", real=True)
MU = sp.Symbol("mu", nonnegative=True)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def sdot(v):
    return v[0] * SX + v[1] * SY + v[2] * SZ


def family_e(checks: Checks) -> None:
    svec = [s1, s2, s3]
    avec = [a1, a2, a3]
    S2 = s1 ** 2 + s2 ** 2 + s3 ** 2
    # (E1) two bands: |<+|sigma.a|->|^2 = tr(P+ X P- X) = |a|^2 - (a.s)^2/|s|^2; the frame (1 + h)^(-1/2) = 1 - h/2 + O(h^2)
    pp = (sp.eye(2) + sdot(svec) / sp.sqrt(S2)) / 2
    pm = (sp.eye(2) - sdot(svec) / sp.sqrt(S2)) / 2
    x2 = sdot(avec)
    two = sp.simplify((pp * x2 * pm * x2).trace() - (a1 ** 2 + a2 ** 2 + a3 ** 2 - (a1 * s1 + a2 * s2 + a3 * s3) ** 2 / S2)) == 0
    eps = sp.Symbol("eps")
    hm = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j)}{max(i, j)}"))
    e1 = sp.eye(3) - eps * hm / 2
    frame = all(sp.expand(sp.expand(e1 * e1 * (sp.eye(3) + eps * hm) - sp.eye(3))[i, j]).coeff(eps, 1) == 0 for i in range(3) for j in range(3))
    checks.check("E1", two and frame,
                 "for the walk's plane-wave block sigma.s, |<+|sigma.a|->|^2 = |a|^2 - (a.s)^2/|s|^2; the frame (1 + h)^(-1/2) is 1 - h/2 at first order, so a uniform strain rate v enters as -(1/2) sigma.(v s)")
    # (E2) with the staggered mass: the block on (k, k + (pi, pi, pi)) is tau_z (x) sigma.s + mu tau_x, and the strain enters as -(1/2) tau_z (x) sigma.a
    tz = sp.Matrix([[1, 0], [0, -1]])
    tx = sp.Matrix([[0, 1], [1, 0]])
    h4 = sp.kronecker_product(tz, sdot(svec)) + MU * sp.kronecker_product(tx, sp.eye(2))
    x4 = -sp.kronecker_product(tz, sdot(avec)) / 2
    en = sp.sqrt(S2 + MU ** 2)
    p4p = (sp.eye(4) + h4 / en) / 2
    p4m = (sp.eye(4) - h4 / en) / 2
    cross = [s2 * a3 - s3 * a2, s3 * a1 - s1 * a3, s1 * a2 - s2 * a1]
    target = ((cross[0] ** 2 + cross[1] ** 2 + cross[2] ** 2) + MU ** 2 * (a1 ** 2 + a2 ** 2 + a3 ** 2)) / (2 * (S2 + MU ** 2))
    four = sp.simplify(sp.expand((p4p * x4 * p4m * x4).trace()) - target) == 0
    h2ok = sp.simplify(sp.expand(h4 * h4) - (S2 + MU ** 2) * sp.eye(4)) == sp.zeros(4, 4)
    checks.check("E2", four and h2ok,
                 "with the staggered mass the block squares to (|s|^2 + mu^2) and the summed matrix elements are tr(P+ X P- X) = (|s x a|^2 + mu^2 |a|^2)/(2(|s|^2 + mu^2)): the sea's adiabatic inertia per site is M(v) = <(|s x v s|^2 + mu^2 |v s|^2)/(|s|^2 + mu^2)^(5/2)>/16, a sum of nonnegative terms")
    # (E3) the three strains: the dilation has |s x s| = 0; the T strain's integrand is positive where s1^2 + s2^2 > 0
    sv = sp.Matrix(svec)

    def cross2(v):
        w = v * sv
        c = sv.cross(w)
        return sp.expand((c.T * c)[0])
    sign = -1 if mut("inertia_sign_flipped") else 1
    cA, cE, cT = cross2(VA), cross2(VE), sign * cross2(VT)
    tform = sp.expand((s1 ** 2 - s2 ** 2) ** 2 + (s1 ** 2 + s2 ** 2) * s3 ** 2)
    eform = sp.expand(4 * s1 ** 2 * s2 ** 2 + (s1 ** 2 + s2 ** 2) * s3 ** 2)
    pos_point = cT.subs({s1: 1, s2: 0, s3: 0}) > 0
    checks.check("E3", cA == 0 and sp.expand(cT - tform) == 0 and sp.expand(cE - eform) == 0 and pos_point,
                 "|s x v s|^2 is 0 on the dilation (so at mu = 0 the sea's inertia has no dilation part), (s1^2 - s2^2)^2 + (s1^2 + s2^2) s3^2 on the T strain (positive at s = (1, 0, 0), so the inertia is nonzero for every mu) and 4 s1^2 s2^2 + (s1^2 + s2^2) s3^2 on the E strain")
    # (E4) at mu = 0: mu_E - 3 mu_T, averaged over the axis permutations (which keep the zone and |s|), is -sum (s_i^2 - s_j^2)^2 / |s|^5
    d = sp.expand(eform - 3 * tform)
    sym = sp.expand(sum(d.subs({s1: p[0], s2: p[1], s3: p[2]}, simultaneous=True) for p in permutations([s1, s2, s3])) / 6)
    weight = sp.Rational(1, 2) if mut("permutation_average_forged") else 1
    target_sym = -weight * ((s1 ** 2 - s2 ** 2) ** 2 + (s1 ** 2 - s3 ** 2) ** 2 + (s2 ** 2 - s3 ** 2) ** 2)
    neg_point = sym.subs({s1: 1, s2: 0, s3: 0}) < 0
    checks.check("E4", sp.expand(sym - target_sym) == 0 and neg_point,
                 "averaged over the six axis permutations, the E strain's integrand minus three times the T strain's is -[(s1^2 - s2^2)^2 + (s1^2 - s3^2)^2 + (s2^2 - s3^2)^2] <= 0, and -2 at s = (1, 0, 0): so at mu = 0, mu_E < 3 mu_T")
    # (E5) the sea's own numbers at mu = 0, and the member plus the sea
    me, mt, kk = sp.symbols("mu_E mu_T K")
    vals = [kinetic(v, AL, BE, GA) for v in (VA, VE, VT)]
    sol = sp.solve([vals[0], vals[1] - me / 2, vals[2] - mt / 2], [AL, BE, GA], dict=True)[0]
    ratio_ok = sp.simplify(sol[BE] / sol[AL] + me / (3 * mt)) == 0
    tot_a, tot_b, tot_g = kk / 4 + sol[AL], -kk / 4 + sol[BE], sol[GA]
    on_line = sp.solve([tot_g, tot_b + tot_a], [me, mt], dict=True)
    off = on_line == [{me: 0, mt: 0}]
    checks.check("E5", ratio_ok and off,
                 "at mu = 0 the sea's inertia, read in the member's family, has alpha = mu_T/4, gamma = (mu_E - mu_T)/4, beta = -mu_E/12: ratio beta/alpha = -mu_E/(3 mu_T), in (-1, 0) by E4; added to the member at alpha = K/4, beta = -alpha, the total lies on the closing line only if mu_T = 0, which E3 excludes")


# ============================================================================================ family H
# T5: the walker's side. One-walker operators between plane waves <k + Q| . |k>, in exact Gaussian rationals at rational angles.
def gz(re, im=0):
    return (Fraction(re), Fraction(im))


GZ, G1 = gz(0), gz(1)


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)


def m2(a, b, c, d):
    return [[a, b], [c, d]]


def madd2(A, B):
    return [[gadd(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]


def msub2(A, B):
    return [[gsub(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]


def mmul2(A, B):
    return [[gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def msc2(z, A):
    return [[gmul(z, A[i][j]) for j in range(2)] for i in range(2)]


def mz2():
    return m2(GZ, GZ, GZ, GZ)


def ent2(A):
    return [A[0][0], A[0][1], A[1][0], A[1][1]]


PAULI = [m2(GZ, G1, G1, GZ), m2(GZ, gz(0, -1), gz(0, 1), GZ), m2(G1, GZ, GZ, gz(-1))]


def a_add(a, b):                                  # angles by exact (cos, sin)
    return (a[0] * b[0] - a[1] * b[1], a[1] * b[0] + a[0] * b[1])


def a_neg(a):
    return (a[0], -a[1])


def v_add(u, v):
    return [a_add(x, y) for x, y in zip(u, v)]


def h_walk(k):
    out = mz2()
    for a in range(3):
        out = madd2(out, msc2(gz(k[a][1]), PAULI[a]))
    return out


def cos_prod(q, skip=None):
    out = Fraction(1)
    for a in range(3):
        if a != skip:
            out *= q[a][0]
    return out


def h_lapse(kout, kin, q, smear=True):            # <kin + q| (1/2){N~, H} |kin>, N = e^{iqx}, N~ = C1 C2 C3 N (or N itself)
    w = cos_prod(q) if smear else Fraction(1)
    return msc2(gz(w / 2), madd2(h_walk(kout), h_walk(kin)))


def p_parts(k, Q, j):                             # block 136's placements: P''_j and the curl-carrying Q_j, as plane-wave symbols
    kq = v_add(k, Q)
    phi = gmul(gadd(G1, a_neg(Q[j])), gz(Fraction(1, 2) * cos_prod(Q, skip=j)))
    two_step = (k[j][1] * k[j][0] + kq[j][1] * kq[j][0]) / 2
    ppp = msc2(gmul(phi, gz(two_step)), m2(G1, GZ, GZ, G1))
    pref = gmul(gz(Fraction(1, 4) * cos_prod(Q)), gadd(a_neg(kq[j]), k[j]))
    qq = msc2(pref, madd2(mmul2(PAULI[j], h_walk(k)), mmul2(h_walk(kq), PAULI[j])))
    return ppp, qq


def p_b(k, Q, j):
    ppp, qq = p_parts(k, Q, j)
    return msc2(gz(Fraction(1, 2)), madd2(ppp, qq))


def walker_bracket(k, q1, q2):                    # X = <k + Q| -i[H_M, H_N] |k>, M = e^{i q1 x}, N = e^{i q2 x}
    k1, k2, k12 = v_add(k, q1), v_add(k, q2), v_add(v_add(k, q1), q2)
    mn = mmul2(h_lapse(k12, k2, q1), h_lapse(k2, k, q2))
    nm = mmul2(h_lapse(k12, k1, q2), h_lapse(k1, k, q1))
    return msc2(gz(0, -1), msub2(mn, nm))


def relabel_side(k, q1, q2):                      # Y = <k + Q| sum xi(N, M).P^B |k> at c = 1, xi_j = e^{iQx}(e^{i q2_j} - e^{i q1_j})
    Q = v_add(q1, q2)
    out = mz2()
    for j in range(3):
        out = madd2(out, msc2(gsub(q2[j], q1[j]), p_b(k, Q, j)))
    return out


def common_ratio(X, Y):
    rs = set()
    for x, y in zip(ent2(X), ent2(Y)):
        if y == GZ:
            if x != GZ:
                return None
            continue
        rs.add(gdiv(x, y))
    return rs.pop() if len(rs) == 1 else None


TRIPLES_H = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]


def rat_angle(i, sgn=1):
    a, b, c = TRIPLES_H[i % len(TRIPLES_H)]
    return (Fraction(a, c), Fraction(sgn * b, c))


def family_h(checks: Checks) -> None:
    # H1: one lapse uniform (M = 1, N = e^{iqx}): X = -Y exactly, i.e. block 112's G[xi] with K/(4 alpha) = 1; curl part orthogonal
    target = gz(-2) if mut("walker_first_order_c_forged") else gz(-1)
    first, curl, plain, n = True, True, True, 0
    for ik in product(range(3), repeat=3):
        for iq in product(range(3), repeat=3):
            k = [rat_angle(ik[0]), rat_angle(ik[1] + 1, -1), rat_angle(ik[2] + 2)]
            q = [rat_angle(iq[0] + 3), rat_angle(iq[1] + 4, -1), rat_angle(iq[2] + 5)]
            kq = v_add(k, q)
            hn = h_lapse(kq, k, q)
            X1 = msc2(gz(0, -1), msub2(mmul2(h_walk(kq), hn), mmul2(hn, h_walk(k))))
            hp = h_lapse(kq, k, q, smear=False)
            X1p = msc2(gz(0, -1), msub2(mmul2(h_walk(kq), hp), mmul2(hp, h_walk(k))))
            Y1, cu = mz2(), mz2()
            for j in range(3):
                w = gsub(q[j], G1)
                Y1 = madd2(Y1, msc2(w, p_b(k, q, j)))
                ppp, qq = p_parts(k, q, j)
                cu = madd2(cu, msc2(w, msub2(qq, ppp)))
            first = first and common_ratio(X1, Y1) == target
            curl = curl and all(z == GZ for z in ent2(cu))
            plain = plain and common_ratio(X1p, Y1) == gz(-1 / cos_prod(q))
            n += 1
    checks.check("H1", first and curl and plain and n == 729,
                 "T5(a): with one lapse uniform the walker's bracket is block 112's G[xi] exactly with K/(4 alpha) = 1 (X = -Y at 729 rational (k, q)); the curl-carrying part is orthogonal to gradients; control: with e in place of e' the ratio is -1/prod cos q_a, not constant")
    # H2: delta lapses two steps apart along an axis: xi = 0 on every bond, the bracket is not zero (position space, exact)
    def smear8(site):
        return {tuple(site[a] + d[a] for a in range(3)): Fraction(1, 8) for d in product((-1, 1), repeat=3)}

    def hops(x):
        out = []
        for a in range(3):
            for sgn in (1, -1):
                y = tuple(x[b] + (sgn if b == a else 0) for b in range(3))
                out.append((y, msc2(gdiv(gz(sgn), gz(0, 2)), PAULI[a])))
        return out

    def smeared_op(w):
        op = {}
        for x, wx in w.items():
            for y, mat in hops(x):
                op[(x, y)] = madd2(op.get((x, y), mz2()), msc2(gz(wx / 2), mat))
                back = [mm for (yy, mm) in hops(y) if yy == x][0]
                op[(y, x)] = madd2(op.get((y, x), mz2()), msc2(gz(wx / 2), back))
        return op

    def op_mul(A, B):
        rows = {}
        for (y, z), mat in B.items():
            rows.setdefault(y, []).append((z, mat))
        out = {}
        for (x, y), mat in A.items():
            for z, m2_ in rows.get(y, []):
                out[(x, z)] = madd2(out.get((x, z), mz2()), mmul2(mat, m2_))
        return out
    u = (0, 0, 0)
    v = (1, 0, 0) if mut("delta_lapses_adjacent") else (2, 0, 0)
    HM, HNd = smeared_op(smear8(u)), smeared_op(smear8(v))
    ab, ba = op_mul(HM, HNd), op_mul(HNd, HM)
    comm = {key: msub2(ab.get(key, mz2()), ba.get(key, mz2())) for key in set(ab) | set(ba)}
    nonzero = [key for key, mat in comm.items() if any(z != GZ for z in ent2(mat))]
    Mf, Nf = {u: 1}, {v: 1}

    def shift(x, a):
        return tuple(x[b] + (1 if b == a else 0) for b in range(3))
    xi_zero = all(Nf.get(shift(x, a), 0) * Mf.get(x, 0) - Nf.get(x, 0) * Mf.get(shift(x, a), 0) == 0
                  for a in range(3) for x in product(range(-2, 4), repeat=3))
    checks.check("H2", xi_zero and len(nonzero) == 16,
                 f"T5(b): delta lapses at u and u + 2e_1 give xi = 0 on every bond, but [H_M, H_N] has {len(nonzero)} nonzero two-by-two entries: exact closure fails for every c")
    # H3: generic rational (k, q1, q2): no single c; along an axis with MN = 1 the ratio is -(1/2) cos^2 q (1 + cos q)
    none_count, m = 0, 0
    for ik in product(range(2), repeat=3):
        for s in range(4):
            k = [rat_angle(ik[0]), rat_angle(ik[1] + 1, -1), rat_angle(ik[2] + 2)]
            q1 = [rat_angle(s + 3), rat_angle(s + 4, -1), rat_angle(s + 5)]
            q2 = [rat_angle(s + 1, -1), rat_angle(s + 2), rat_angle(s)]
            none_count += common_ratio(walker_bracket(k, q1, q2), relabel_side(k, q1, q2)) is None
            m += 1
    axis = []
    for cq, sq in ((Fraction(3, 5), Fraction(4, 5)), (Fraction(5, 13), Fraction(12, 13))):
        q1 = [(cq, -sq), (Fraction(1), Fraction(0)), (Fraction(1), Fraction(0))]
        q2 = [(cq, sq), (Fraction(1), Fraction(0)), (Fraction(1), Fraction(0))]
        k = [rat_angle(0), rat_angle(1), rat_angle(2)]
        axis.append(common_ratio(walker_bracket(k, q1, q2), relabel_side(k, q1, q2)) == gz(-Fraction(1, 2) * cq * cq * (1 + cq)))
    checks.check("H3", none_count == m == 32 and all(axis),
                 "T5(b): at 32 rational (k, q1, q2) no single c gives X = c Y entrywise; along an axis with M = e^{-iqx}, N = e^{iqx} the ratio is -(1/2) cos^2 q (1 + cos q) (at cos q = 3/5 and 5/13), which is -1 only as q -> 0")
    # H4: the defect is third order, for every k and all directions: q1 = t u, q2 = t v, sin k_a -> S_a, cos k_a -> C_a
    t = sp.Symbol("t")
    Ss, Cs = sp.symbols("S1:4"), sp.symbols("C1:4")
    U, V = sp.symbols("u1:4"), sp.symbols("v1:4")
    order = 4

    def tr_t(x):
        x = sp.expand(x)
        return sum(x.coeff(t, n) * t ** n for n in range(order))
    SIGS = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

    def mt(A):
        return A.applyfunc(tr_t)

    def sa(a, b):
        return (tr_t(a[0] * b[0] - a[1] * b[1]), tr_t(a[1] * b[0] + a[0] * b[1]))

    def sv(x, y):
        return [sa(p, r) for p, r in zip(x, y)]

    def sH(k):
        return sum((SIGS[a] * k[a][1] for a in range(3)), sp.zeros(2, 2))

    def scp(q, skip=None):
        out = sp.Integer(1)
        for a in range(3):
            if a != skip:
                out = tr_t(out * q[a][0])
        return out

    def sHN(ko, ki, q):
        return mt(scp(q) * (sH(ko) + sH(ki)) / 2)

    def spB(k, Q, j):
        kq = sv(k, Q)
        phi = tr_t((1 + Q[j][0] - sp.I * Q[j][1]) / 2 * scp(Q, skip=j))
        ppp = tr_t(phi * (k[j][1] * k[j][0] + kq[j][1] * kq[j][0]) / 2) * sp.eye(2)
        pref = tr_t(scp(Q) * (kq[j][0] - sp.I * kq[j][1] + k[j][0] + sp.I * k[j][1]) / 4)
        qq = mt(pref * (SIGS[j] * sH(k) + sH(kq) * SIGS[j]))
        return mt((ppp + qq) / 2)
    k = [(Cs[a], Ss[a]) for a in range(3)]
    q1 = [(1 - (t * x) ** 2 / 2, t * x - (t * x) ** 3 / 6) for x in U]
    q2 = [(1 - (t * x) ** 2 / 2, t * x - (t * x) ** 3 / 6) for x in V]
    k1, k2, k12 = sv(k, q1), sv(k, q2), sv(sv(k, q1), q2)
    X = mt(-sp.I * (mt(sHN(k12, k2, q1) * sHN(k2, k, q2)) - mt(sHN(k12, k1, q2) * sHN(k1, k, q1))))
    Q = sv(q1, q2)
    Y = sp.zeros(2, 2)
    for j in range(3):
        Y += mt(tr_t((q2[j][0] + sp.I * q2[j][1]) - (q1[j][0] + sp.I * q1[j][1])) * spB(k, Q, j))
    D = mt(X + Y)
    circle = [Cs[a] ** 2 + Ss[a] ** 2 - 1 for a in range(3)]
    gens = list(Cs) + list(Ss)

    def mod_c(x):
        x = sp.expand(x)
        return 0 if x == 0 else sp.reduced(x, circle, *gens)[1]
    low = all(mod_c(D[i, j].coeff(t, n)) == 0 for n in (0, 1, 2) for i in range(2) for j in range(2))
    five = 4 if mut("third_order_form_forged") else 5
    udv = sum(U[a] * V[a] for a in range(3))
    form = sp.I / 4 * sum(Cs[j] * Ss[j] * (U[j] - V[j]) * (4 * udv + (five - 4) * U[j] * V[j]) for j in range(3))
    third = all(sp.expand(mod_c(D[i, j].coeff(t, 3) - (form if i == j else 0))) == 0 for i in range(2) for j in range(2))
    lead_x = any(mod_c(X[i, j].coeff(t, 1)) != 0 for i in range(2) for j in range(2))
    checks.check("H4", low and third and lead_x,
                 "T5(c): with q1 = t u, q2 = t v, for every k and all directions (symbolic; modulo cos^2 + sin^2 = 1), X + Y vanishes at orders t^0, t^1, t^2, while X itself starts at t^1; at t^3 it is (i/4) sum_j sin k_j cos k_j (u_j - v_j)(4 u.v + u_j v_j) times the identity: the walker's momentum density against a bilinear of third order in the lapses' wave numbers")
    # H5: no finite-range placement closes it. For the body-diagonal placement, the extreme hop sites in a generic direction give a
    # non-adjacent pair whose commutator has the single-path element W(a_h, a')^dag W(b_h, b'); time reversal makes every block a real
    # quaternion, so such products vanish only with a factor; sets invariant under the proper rotations never have extremes one step apart.
    def e_site_op(x):
        out = {}
        for a in range(3):
            for sgn in (1, -1):
                y = tuple(x[b] + (sgn if b == a else 0) for b in range(3))
                hop = msc2(gdiv(gz(sgn), gz(0, 2)), PAULI[a])                 # H(x, y) = sgn sigma_a/(2i)
                back = [[(hop[j][i][0], -hop[j][i][1]) for j in range(2)] for i in range(2)]
                out[(x, y)] = madd2(out.get((x, y), mz2()), msc2(gz(Fraction(1, 2)), hop))
                out[(y, x)] = madd2(out.get((y, x), mz2()), msc2(gz(Fraction(1, 2)), back))
        return out

    E0 = {}
    for d in product((-1, 1), repeat=3):
        for key, mat in e_site_op(d).items():
            E0[key] = madd2(E0.get(key, mz2()), msc2(gz(Fraction(1, 8)), mat))
    E0 = {key: mat for key, mat in E0.items() if any(z != GZ for z in ent2(mat))}
    hop_sites = {s for (r, c) in E0 if r != c for s in (r, c)}
    nvec = (Fraction(1), Fraction(1, 10), Fraction(1, 100))

    def phi(x):
        return sum(p * q for p, q in zip(nvec, x))
    a_h, b_h = max(hop_sites, key=phi), min(hop_sites, key=phi)
    tv = tuple(p - q for p, q in zip(a_h, b_h))
    if mut("placement_extremes_adjacent"):
        tv = (1, 0, 0)
    Et = {(tuple(p + q for p, q in zip(r, tv)), tuple(p + q for p, q in zip(c, tv))): mat for (r, c), mat in E0.items()}
    ab, ba = op_mul(E0, Et), op_mul(Et, E0)
    elements, single = 0, True
    for (r, ap), mat_a in E0.items():
        if r != a_h or ap == a_h:
            continue
        for (r2, bp), mat_b in E0.items():
            if r2 != b_h or bp == b_h:
                continue
            key = (ap, tuple(p + q for p, q in zip(tv, bp)))
            got = msub2(ab.get(key, mz2()), ba.get(key, mz2()))
            dag_a = [[(mat_a[j][i][0], -mat_a[j][i][1]) for j in range(2)] for i in range(2)]
            want = mmul2(dag_a, mat_b)
            single = single and got == want and any(z != GZ for z in ent2(want))
            elements += 1
    units = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    witness = single and elements > 0 and tv not in units and tv != (0, 0, 0)
    # time reversal i sigma_y K: sigma_y W* sigma_y = W iff W = [[p, q], [-q*, p*]], a real quaternion; then W^dag W = (|p|^2 + |q|^2) 1
    pr, pi_, qr, qi = sp.symbols("pr pi qr qi", real=True)
    rr = sp.symbols("r0:8", real=True)
    Wg = sp.Matrix([[rr[0] + sp.I * rr[1], rr[2] + sp.I * rr[3]], [rr[4] + sp.I * rr[5], rr[6] + sp.I * rr[7]]])
    sy_ = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    cond = sy_ * Wg.conjugate() * sy_ - Wg
    eqs = [sp.re(z) for z in cond] + [sp.im(z) for z in cond]
    sol = sp.solve(eqs, list(rr), dict=True)
    quat = len(sol) == 1 and sp.Matrix(8, 1, [sol[0].get(x, x) for x in rr]).free_symbols <= set(rr) and len(sp.Matrix(8, 1, [sol[0].get(x, x) for x in rr]).free_symbols) == 4
    Wq = sp.Matrix([[pr + sp.I * pi_, qr + sp.I * qi], [-(qr - sp.I * qi), pr - sp.I * pi_]])
    tr_fix = sp.simplify(sy_ * Wq.conjugate() * sy_ - Wq) == sp.zeros(2, 2)
    normq = sp.simplify(Wq.H * Wq - (pr ** 2 + pi_ ** 2 + qr ** 2 + qi ** 2) * sp.eye(2)) == sp.zeros(2, 2)

    def is_quaternion(mat):
        return mat[0][0] == (mat[1][1][0], -mat[1][1][1]) and mat[0][1] == (-mat[1][0][0], mat[1][0][1])
    e_quat = all(is_quaternion(mat) for mat in E0.values())
    # proper rotations: sets invariant under them never have extremes one step apart (every orbit in [-3, 3]^3, with and without 0)
    rots = []
    for perm in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            mrot = [[sg[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]
            if sp.Matrix(mrot).det() == 1:
                rots.append(mrot)
    orbits = []
    for x in product(range(-3, 4), repeat=3):
        if x == (0, 0, 0):
            continue
        orb = frozenset(tuple(sum(mrot[i][j] * x[j] for j in range(3)) for i in range(3)) for mrot in rots)
        if orb not in orbits:
            orbits.append(orb)
    adjacent = 0
    for orb in orbits:
        for s_ in (set(orb), set(orb) | {(0, 0, 0)}):
            hi, lo = max(s_, key=phi), min(s_, key=phi)
            adjacent += tuple(p - q for p, q in zip(hi, lo)) in units
    checks.check("H5", witness and quat and tr_fix and normq and e_quat and len(rots) == 24 and adjacent == 0,
                 f"T5(d): for the body-diagonal placement the extreme hop sites in the direction (1, 1/10, 1/100) are {a_h} and {b_h}; for the non-adjacent pair u, u + {tv} the commutator element is the single-path product W(a_h, a')^dag W(b_h, b') != 0; time reversal forces every block to a real quaternion (a 4-dimensional solution space, W^dag W = |W|^2), so such products vanish only with a factor; over every proper-rotation orbit in [-3, 3]^3 the extremes are never one step apart")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 112, 124, 135, 136, 139 and 144 as landed on main (the walk and its staggered mass, the member's lattice bracket of lapse constraints, its kinetic family and its drifting relabellings, and the walker's placements of energy and momentum); it reports what the member's clock algebra implies for two reading questions; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Lemaitre", "Lemaître", "Robertson", "Hubble", "Kasner", "Heckmann", "Schucking", "Schücking", "Bianchi", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt", "Inglis", "Zener", "Sakharov", "Leibniz", "Cauchy", "Hesse", "Boulware", "Wald", "Gambini", "Pullin", "Bahr", "Dittrich")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
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
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - delta lapses at a bond's two ends give that bond alone; block 112's bracket for twelve such pairs",
    "per_site: executed - the uniform lapse gives only gradients (rank sites - 1) and the divergence identity",
    "per_mode: executed - the cubic-only kinetic term: the bracket's line in c misses the relabellings' span on the 3^3 torus",
    "per_block: executed - the sea's adiabatic inertia on uniform strains: two- and four-band matrix elements, positivity, the permutation average; the walker's bracket: one lapse uniform, delta lapses two steps apart, the third-order defect, the extreme-hop witness against every local placement",
    "lattice_wide: block 112's scope (flat strain, the term linear in canonical momentum, symmetric face timing); uniform strains for the sea",
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
    family_h(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: block 112's relabelling fields span every bond field while a uniform lapse gives only gradients, so if every clock profile is a relabelling the whole momentum constraint is forced; a cubic-only kinetic term breaks the closure for every ratio; the closing line is indefinite on uniform strains and the walker sea's adiabatic inertia is positive and nonzero, so the member plus that inertia is off the line; the walker bracket closes with block 112 xi exactly only when one lapse is uniform, and otherwise through second order in the lapse wave numbers; no finite-range placement with the rotations and time reversal closes it; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
