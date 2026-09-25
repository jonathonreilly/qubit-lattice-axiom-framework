#!/usr/bin/env python3
"""Exact checks for the conditional source note.
For the explicitly supplied continuum quadratic action, positive K and alpha, conserved sources and nonzero spatial momentum: the generic nonzero-frequency exchange formula requires omega² different from p². The static clock formula is separate. With supplied spinless point-body stress and a conservative near-zone prescription, the displayed order-v² velocity-dependent interaction gives W=1 through the first weak-binding order using tensor virial averages. No finite response at the wave pole, nonlinear completion, lattice result or physical gravity identification is established.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS_THAT_GIVE_PULL_BOUND_PAIRS_WEIGHT_ONE_ALONG_EVERY_AXIS_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_members_pull_carries_the_velocity_terms_that_give_pull_bound_pairs_weight_one_along_every_axis_at_first_order_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "curvature_second_order_forged": "B",
    "shift_coupling_sign_flipped": "C",
    "alpha_off_the_books": "C",
    "drift_residual_forged": "C",
    "retardation_dropped": "D",
    "static_pull_taken_for_the_member": "E",
    "boost_half_dropped": "E",
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


Fr = Fraction
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its shift, its kinetic term, the source link and the bodies are supplied; the memo does not define a time metric)")


# ============================================================================================ plane waves
EL = sp.Symbol("E")
FIELD_NAMES = ("h11", "h12", "h13", "h22", "h23", "h33", "u", "N1", "N2", "N3")


def plane_wave(names):
    a = {nm: sp.Symbol("a_" + nm) for nm in names}
    b = {nm: sp.Symbol("b_" + nm) for nm in names}
    return a, b, {nm: a[nm] * EL + b[nm] / EL for nm in names}


def make_d(kvec):
    def d(f, j):
        return sp.expand(sp.I * kvec[j] * EL * sp.diff(f, EL))
    return d


def make_dt(w):
    def dt(f):
        return sp.expand(-sp.I * w * EL * sp.diff(f, EL))
    return dt


def average(expr):
    return sp.expand(sp.expand(expr).coeff(EL, 0))


def lengths(F):
    return sp.Matrix(3, 3, lambda i, j: F["h%d%d" % (min(i, j) + 1, max(i, j) + 1)])


def member_curvature(h, d, forged=False):
    """R1 and R2 of blocks 62 and 101, in position-space form (derivatives by d)."""
    trh = h.trace()
    r1 = sum(d(d(h[i, j], i), j) for i in range(3) for j in range(3)) - sum(d(d(trh, i), i) for i in range(3))
    q = sp.Rational(1, 5) if forged else QUARTER
    r2 = (-q * sum(d(h[i, j], l) ** 2 for i in range(3) for j in range(3) for l in range(3))
          + HALF * sum(sum(d(h[i, l], i) for i in range(3)) * sum(d(h[j, l], j) for j in range(3)) for l in range(3))
          - HALF * sum(sum(d(h[i, j], i) for i in range(3)) * d(trh, j) for j in range(3))
          + QUARTER * sum(d(trh, l) ** 2 for l in range(3)))
    return sp.expand(r1), sp.expand(r2)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    kz, w, eps = sp.symbols("k omega epsilon")
    kvec = (0, 0, kz)
    d, dt = make_d(kvec), make_dt(w)
    a, b, F = plane_wave(FIELD_NAMES)
    h = lengths(F)
    u = F["u"]
    shift = [F["N1"], F["N2"], F["N3"]]

    def trunc(e, order=2):
        e = sp.expand(e)
        return sp.expand(sum(e.coeff(eps, j) * eps ** j for j in range(order + 1)))

    g = sp.eye(3) + eps * h
    ginv = (sp.eye(3) - eps * h + eps ** 2 * h * h).applyfunc(sp.expand)
    sqrtg = sp.expand(1 + HALF * eps * h.trace() + eps ** 2 * (sp.Rational(1, 8) * h.trace() ** 2 - QUARTER * (h * h).trace()))
    dg = [[[d(g[i, j], l) for l in range(3)] for j in range(3)] for i in range(3)]
    gam = [[[trunc(HALF * sum(ginv[m, l] * (dg[l][i][j] + dg[l][j][i] - dg[i][j][l]) for l in range(3))) for j in range(3)] for i in range(3)] for m in range(3)]

    def ricci(i, j):
        return trunc(sum(d(gam[m][i][j], m) - d(gam[m][i][m], j)
                         + sum(gam[m][m][l] * gam[l][i][j] - gam[m][j][l] * gam[l][i][m] for l in range(3)) for m in range(3)))

    ric = [[ricci(i, j) for j in range(3)] for i in range(3)]
    scal = trunc(sum(ginv[i, j] * ric[i][j] for i in range(3) for j in range(3)))
    dens = trunc(sqrtg * scal)
    r1, r2 = member_curvature(h, d, forged=mut("curvature_second_order_forged"))
    checks.check("B1", sp.expand(scal.coeff(eps, 1) - r1) == 0 and sp.expand(dens.coeff(eps, 1) - r1) == 0,
                 "the first-order curvature of the lengths delta + h is R1 = d_i d_j h_ij - lap tr h, exactly")
    checks.check("B2", average(dens.coeff(eps, 2) - r2) == 0,
                 "the second-order part of sqrt(gamma) R minus the member's R2 averages to zero on every plane wave (wave vector along an axis; both are rotation-invariant contractions): the actions agree")
    hd = sp.Matrix(3, 3, lambda i, j: dt(h[i, j]) - d(shift[j], i) - d(shift[i], j))
    k1 = hd / 2
    comparator = (sum(k1[i, j] ** 2 for i in range(3) for j in range(3)) - sum(k1[i, i] for i in range(3)) ** 2
                  + u * scal.coeff(eps, 1) + dens.coeff(eps, 2))
    ah, bh = sp.symbols("alphahat betahat")
    member = ah * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + bh * sum(hd[i, i] for i in range(3)) ** 2 + u * r1 + r2
    diff = average(member - comparator)
    amps = [a[nm] for nm in FIELD_NAMES] + [b[nm] for nm in FIELD_NAMES]
    coeffs = [c for c in sp.Poly(diff, *amps).coeffs()] if diff != 0 else []
    sol = sp.solve(coeffs, [ah, bh], dict=True) if coeffs else [{}]
    unique = len(sol) == 1 and sol[0] == {ah: QUARTER, bh: -QUARTER}
    at_books = average(member.subs({ah: QUARTER, bh: -QUARTER}) - comparator) == 0
    checks.check("B3", unique and at_books,
                 "with K_ij = (1/2) Hdot_ij at first order, the member per unit K equals the comparator's second-order lapse-and-shift density on every plane wave iff alpha = K/4 and beta = -alpha")


# ============================================================================================ family C
def member_matrix(alpha, K, p, w, with_shift):
    kvec = (0, 0, p)
    d, dt = make_d(kvec), make_dt(w)
    a, b, F = plane_wave(FIELD_NAMES)
    h = lengths(F)
    u = F["u"]
    shift = [F["N1"], F["N2"], F["N3"]] if with_shift else [0, 0, 0]
    hd = sp.Matrix(3, 3, lambda i, j: dt(h[i, j]) - d(shift[j], i) - d(shift[i], j))
    r1, r2 = member_curvature(h, d)
    lag = alpha * (sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) - sum(hd[i, i] for i in range(3)) ** 2) + K * (u * r1 + r2)
    lav = average(lag)
    names = [nm for nm in FIELD_NAMES if with_shift or not nm.startswith("N")]
    mat = sp.Matrix(len(names), len(names), lambda r, c: sp.diff(lav, b[names[r]], a[names[c]]))
    return mat, names


def kept_books_source(prefix, p, w):
    th = {}
    for (i, j) in ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)):
        th[(i, j)] = th[(j, i)] = sp.Symbol("%s%d%d" % (prefix, i + 1, j + 1))
    mom = [p * th[(i, 2)] / w for i in range(3)]
    e = p * mom[2] / w
    return e, mom, th


def coupling(names, e, mom, th, sign=1):
    vec = []
    for nm in names:
        if nm == "u":
            vec.append(-e)
        elif nm.startswith("N"):
            vec.append(sign * mom[int(nm[1]) - 1])
        else:
            i, j = int(nm[1]) - 1, int(nm[2]) - 1
            vec.append(th[(i, j)] if i != j else HALF * th[(i, j)])
    return sp.Matrix(vec)


def exchange(alpha, K, p, w, with_shift, sign=1):
    mat, names = member_matrix(alpha, K, p, w, with_shift)
    e2, m2, t2 = kept_books_source("T", p, w)
    e1, m1, t1 = kept_books_source("S", p, w)
    j2 = coupling(names, e2, m2, t2, sign)
    j1 = coupling(names, e1, m1, t1, sign)
    try:
        sol, params = mat.gauss_jordan_solve(-j2)
    except ValueError:
        return mat, None, None
    pairing = sp.simplify(sp.expand((j1.T * sol)[0]))
    if pairing.free_symbols & set(params):
        return mat, None, None
    tt = e1 * e2 - 2 * sum(m1[i] * m2[i] for i in range(3)) + sum(t1[(i, j)] * t2[(i, j)] for i in range(3) for j in range(3))
    tr1 = -e1 + sum(t1[(i, i)] for i in range(3))
    tr2 = -e2 + sum(t2[(i, i)] for i in range(3))
    expected = (tt - HALF * tr1 * tr2) / (2 * K * (p ** 2 - w ** 2))
    return mat, pairing, expected


def family_c(checks: Checks) -> None:
    p, w = sp.symbols("p omega", positive=True)
    K, al = sp.symbols("K alpha", positive=True)
    books_alpha = K / 3 if mut("alpha_off_the_books") else K / 4
    sign = -1 if mut("shift_coupling_sign_flipped") else 1
    mat, pairing, expected = exchange(books_alpha, K, p, w, True, sign)
    ok1 = (pairing is not None and sp.simplify(pairing - expected) == 0 and mat.rank() == 6
           and sp.simplify(mat - mat.H) == sp.zeros(*mat.shape))
    checks.check("C1", ok1, "with the shift at alpha = K/4: the plane-wave matrix is hermitian of rank 6 of 10 (four relabellings); every conserved source away from p=0 and omega**2=p**2 has a solution, and a second source feels (1/(2K)) [T'.T - (1/2) T' T] / (p^2 - omega^2), free of the relabellings")
    mat0, pairing0, expected0 = exchange(K / 4, K, p, w, False)
    ok2 = pairing0 is not None and sp.simplify(pairing0 - expected0) == 0 and mat0.rank() == 6
    checks.check("C2", ok2, "without the shift at alpha = K/4: rank 6 of 7, and the same exchange at nonzero frequency away from the wave pole (omega**2 != p**2, p != 0)")
    blocked = True
    for with_shift in (True, False):
        for alpha in (K / 3, K / 5, 2 * K):
            blocked = blocked and exchange(alpha, K, p, w, with_shift)[1] is None
    e2, m2, t2 = kept_books_source("T", p, w)
    obstruction_ok = True
    for with_shift in (True, False):
        mat_g, names = member_matrix(al, K, p, w, with_shift)
        j2 = coupling(names, e2, m2, t2)
        conds = [sp.simplify((v.T * j2)[0]) for v in mat_g.T.nullspace()]
        conds = [c for c in conds if c != 0]
        if len(conds) != 1:
            obstruction_ok = False
            continue
        ratio = sp.simplify(conds[0] / ((K - 4 * al) * e2 / (4 * al)))
        obstruction_ok = obstruction_ok and ratio != 0 and not ratio.free_symbols
    checks.check("C3", blocked and obstruction_ok, "at alpha = K/3, K/5 and 2K, with or without the shift, a source that keeps the books has no solution; at general alpha the one condition is (K - 4 alpha) e / (4 alpha) = 0")
    mat_s, names = member_matrix(K / 4, K, p, 0, True)
    e0 = sp.Symbol("e0")
    j0 = sp.Matrix([-e0 if nm == "u" else 0 for nm in names])
    sol, params = mat_s.gauss_jordan_solve(-j0)
    clock = sp.simplify(sol[names.index("u")])
    checks.check("C4", clock == -e0 / (4 * K * p ** 2), "static content: the clock is u = -e/(4 K p^2), block 101's law at unit rate")
    mat_n, names_n = member_matrix(K / 4, K, p, w, False)
    mat_n0, _ = member_matrix(K / 4, K, p, 0, False)
    xi = sp.symbols("xi1:4")
    kv = (0, 0, p)
    drift = {"u": 0}
    for (i, j) in ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)):
        drift["h%d%d" % (i + 1, j + 1)] = sp.I * (kv[i] * xi[j] + kv[j] * xi[i])
    vec = sp.Matrix([drift[nm] for nm in names_n])
    kin = sp.simplify((mat_n - mat_n0) / w ** 2)
    iu = names_n.index("u")
    only_h = all(kin[iu, c] == 0 and kin[c, iu] == 0 for c in range(len(names_n))) and not kin.free_symbols & {w}
    static_zero = sp.simplify(mat_n0 * vec) == sp.zeros(len(names_n), 1)
    hdot = sp.Matrix(3, 3, lambda i, j: sp.I * (kv[i] * xi[j] + kv[j] * xi[i]))
    residual = [sp.expand(K * sum(sp.I * kv[i] * (hdot[i, j] - (hdot.trace() if i == j else 0)) for i in range(3))) for j in range(3)]
    if mut("drift_residual_forged"):
        claimed = [0, 0, 0]
    else:
        claimed = [-K * p ** 2 * xi[0], -K * p ** 2 * xi[1], 0]
    residual_ok = all(sp.expand(residual[j] - claimed[j]) == 0 for j in range(3)) and residual[0] != 0
    shifted = sp.Matrix(3, 3, lambda i, j: hdot[i, j] - sp.I * (kv[i] * xi[j] + kv[j] * xi[i]))
    checks.check("C5", only_h and static_zero and residual_ok and shifted == sp.zeros(3, 3),
                 "without the shift: time enters only through the lengths' second derivatives, and the static part annihilates a relabelling, so h = t (d xi + (d xi)^T), u = 0 solves the source-free member; its momentum-constraint residual is -K p^2 xi_perp (nonzero across the wave vector); with the shift N = xi it is a pure relabelling")
    t, x, y, z = sp.symbols("t x y z")
    X = (x, y, z)
    xif = [sp.Function("xi%d" % i)(x, y, z) for i in range(3)]
    thf = [[sp.Function("Th%d%d" % (min(i, j), max(i, j)))(t, x, y, z) for j in range(3)] for i in range(3)]
    pf = [sp.Function("P%d" % i)(t, x, y, z) for i in range(3)]
    hdr = [[t * (sp.diff(xif[j], X[i]) + sp.diff(xif[i], X[j])) for j in range(3)] for i in range(3)]
    lhs = HALF * sum(thf[i][j] * hdr[i][j] for i in range(3) for j in range(3))
    xp = sum(xif[j] * pf[j] for j in range(3))
    rhs = sp.diff(t * xp, t) - xp + sum(sp.diff(t * sum(thf[i][j] * xif[j] for j in range(3)), X[i]) for i in range(3))
    books = {sp.Derivative(pf[j], t): -sum(sp.diff(thf[i][j], X[i]) for i in range(3)) for j in range(3)}
    checks.check("C6", sp.expand((lhs - rhs).subs(books)) == 0,
                 "content that keeps its books couples to the drifting lengths as -xi.P plus total derivatives: (1/2) Theta.h = d/dt(t xi.P) - xi.P + d_i(t Theta_ij xi_j)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    lam = sp.Symbol("lambda")
    m1, m2, K, r = sp.symbols("m1 m2 K r", positive=True)
    v1 = sp.Matrix(sp.symbols("v1x v1y v1z"))
    v2 = sp.Matrix(sp.symbols("v2x v2y v2z"))
    n = sp.Matrix(sp.symbols("nx ny nz"))
    eta = sp.diag(-1, 1, 1, 1)

    def body(m, v):
        gam = 1 / sp.sqrt(1 - lam ** 2 * v.dot(v))
        vm = [1] + list(lam * v)
        return sp.Matrix(4, 4, lambda i, j: m * gam * vm[i] * vm[j])

    t1m, t2m = body(m1, v1), body(m2, v2)
    tt = sum(t1m[i, j] * t2m[k, l] * eta[i, k] * eta[j, l] for i in range(4) for j in range(4) for k in range(4) for l in range(4))
    trace = lambda tm: sum(eta[i, i] * tm[i, i] for i in range(4))
    comb = sp.expand(sp.series(tt - HALF * trace(t1m) * trace(t2m), lam, 0, 3).removeO())
    target = sp.expand(m1 * m2 * HALF * (1 + sp.Rational(3, 2) * lam ** 2 * (v1.dot(v1) + v2.dot(v2)) - 4 * lam ** 2 * v1.dot(v2)))
    checks.check("D1", sp.expand(comb - target) == 0, "point bodies: T1.T2 - (1/2) T1 T2 = (m1 m2 / 2) [1 + (3/2)(v1^2 + v2^2) - 4 v1.v2] through order v^2")
    P2, W2 = sp.symbols("P2 W2", positive=True)
    xs, ys, zs = sp.symbols("x y z", real=True)
    rr = sp.sqrt(xs ** 2 + ys ** 2 + zs ** 2)
    lap = lambda f: sp.diff(f, xs, 2) + sp.diff(f, ys, 2) + sp.diff(f, zs, 2)
    series_ok = sp.simplify(1 / (P2 - W2) - (1 / P2 + W2 / P2 ** 2 + W2 ** 2 / (P2 ** 2 * (P2 - W2)))) == 0
    checks.check("D2", series_ok and sp.simplify(lap(rr) - 2 / rr) == 0 and sp.simplify(lap(1 / rr)) == 0,
                 "1/(p^2 - w^2) = 1/p^2 + w^2/p^4 + w^4/(p^4 (p^2 - w^2)) exactly; lap r = 2/r and lap(1/r) = 0 off the origin, so 1/p^4 is -r/(8 pi) where 1/p^2 is 1/(4 pi r)")
    ta, tb = sp.symbols("t1 t2")
    x1 = sp.Matrix([sp.Function("x1%s" % c)(ta) for c in "xyz"])
    x2 = sp.Matrix([sp.Function("x2%s" % c)(tb) for c in "xyz"])
    dist = sp.sqrt((x1 - x2).dot(x1 - x2))
    u1, u2 = x1.diff(ta), x2.diff(tb)
    nn = (x1 - x2) / dist
    mixed = sp.diff(dist, ta, tb)
    checks.check("D3", sp.simplify(mixed + (u1.dot(u2) - nn.dot(u1) * nn.dot(u2)) / dist) == 0,
                 "d/dt1 d/dt2 |x1(t1) - x2(t2)| = -[v1.v2 - (n.v1)(n.v2)] / r")
    inst = comb.subs(lam, 1) / (2 * K) / (4 * sp.pi * r)
    mixed_pt = -(v1.dot(v2) - n.dot(v1) * n.dot(v2)) / r
    ret = 0 if mut("retardation_dropped") else (m1 * m2 * HALF) / (2 * K) * (-1 / (8 * sp.pi)) * mixed_pt
    expected = m1 * m2 / (16 * sp.pi * K * r) * (1 + sp.Rational(3, 2) * (v1.dot(v1) + v2.dot(v2)) - sp.Rational(7, 2) * v1.dot(v2) - HALF * n.dot(v1) * n.dot(v2))
    checks.check("D4", sp.simplify(sp.expand(inst + ret - expected)) == 0,
                 "the pull between two slow bodies: (m1 m2 / (16 pi K r)) [1 + (3/2)(v1^2 + v2^2) - (7/2) v1.v2 - (1/2)(n.v1)(n.v2)]")


# ============================================================================================ family E
def weight_minus_one(a, b, c, u_avg, up_avg, mass):
    return ((1 + 2 * (2 * a + b)) * u_avg + (1 + 2 * c) * up_avg) / mass


def family_e(checks: Checks) -> None:
    m1, m2, k, r = sp.symbols("m1 m2 k r", positive=True)
    A, B, C = sp.symbols("a b c")
    M = m1 + m2
    mu = m1 * m2 / M
    P = sp.Matrix(sp.symbols("P1:4"))
    q = sp.Matrix(sp.symbols("q1:4"))
    n = sp.Matrix(sp.symbols("n1:4"))
    p1 = m1 / M * P + q
    p2 = m2 / M * P - q
    h1 = (-p1.dot(p1) ** 2 / (8 * m1 ** 3) - p2.dot(p2) ** 2 / (8 * m2 ** 3)
          - k / r * (A * (p1.dot(p1) / m1 ** 2 + p2.dot(p2) / m2 ** 2) + B * p1.dot(p2) / (m1 * m2) + C * n.dot(p1) * n.dot(p2) / (m1 * m2)))
    s = sp.Symbol("s")
    coef = sp.expand(h1.subs({P[i]: s * P[i] for i in range(3)}, simultaneous=True)).coeff(s, 2)
    pn2 = P.dot(P)
    T = q.dot(q) / (2 * mu)
    TP = P.dot(q) ** 2 / (2 * mu * pn2)
    U = -k / r
    UP = -k * n.dot(P) ** 2 / (r * pn2)
    target = pn2 / (2 * M) * (-(T + 2 * TP) / M + 2 / M * ((2 * A + B) * U + C * UP))
    checks.check("E1", sp.simplify(coef - target) == 0,
                 "first-order Legendre transform: the P^2 part of the corrections is (P^2/(2M)) {-(T + 2 T_P)/M + (2/M)[(2a + b) U + c U_P]}")
    x = sp.Matrix(sp.symbols("x1:4"))
    e = sp.Matrix(sp.symbols("e1:4"))
    rn = sp.sqrt(x.dot(x))
    h0 = q.dot(q) / (2 * mu) - k / rn

    def bracket(f, g):
        return sum(sp.diff(f, x[i]) * sp.diff(g, q[i]) - sp.diff(f, q[i]) * sp.diff(g, x[i]) for i in range(3))

    lhs = bracket(2 * x.dot(e) * q.dot(e), h0)
    rhs = 2 * q.dot(e) ** 2 / mu - 2 * k * x.dot(e) ** 2 / rn ** 3
    checks.check("E2", sp.simplify(lhs - rhs) == 0,
                 "tensor virial bracket: {2 (e.x)(e.q), H0} = 2 (e.q)^2 / mu - 2k (e.x)^2 / r^3, whose average vanishes in a bound state: 2 <T_P> = -<U_P>")
    ua, upa, ta_, tpa = sp.symbols("Uavg UPavg Tavg TPavg")
    pre = (ua - 2 * tpa + 2 * (2 * A + B) * ua + 2 * C * upa) / M
    post = sp.expand(pre.subs(tpa, -upa / 2))
    formula_ok = sp.simplify(post - weight_minus_one(A, B, C, ua, upa, M)) == 0
    member = {A: sp.Rational(3, 2), B: -sp.Rational(7, 2), C: -HALF}
    if mut("static_pull_taken_for_the_member"):
        member = {A: 0, B: 0, C: 0}
    member_ok = sp.simplify(post.subs(member)) == 0
    static_ok = sp.simplify(post.subs({A: 0, B: 0, C: 0}) - (ua + upa) / M) == 0
    mm = sp.Symbol("m", positive=True)
    line = sp.simplify(pre.subs({A: 0, B: 0, C: 0, upa: ua, tpa: ta_, m1: mm, m2: mm}) - (ua / (2 * mm) - ta_ / mm)) == 0
    both = sp.solve([1 + 2 * (2 * A + B), 1 + 2 * C], [B, C], dict=True)
    iff_ok = len(both) == 1 and both[0] == {B: -HALF - 2 * A, C: -HALF}
    checks.check("E3", formula_ok and member_ok and static_ok and line and iff_ok,
                 "W = 1 + [(1 + 2(2a + b))<U> + (1 + 2c)<U_P>]/M; one along every axis iff 2a + b = -1/2 and c = -1/2; the member's pull (3/2, -7/2, -1/2) gives W = 1; the clock's pull alone gives 1 + (<U> + <U_P>)/M, and on a line with equal masses 1 + <U>/(2m) - <T>/m")
    lam = sp.Symbol("lambda")
    y1 = sp.Matrix(sp.symbols("y1:4"))
    y2 = sp.Matrix(sp.symbols("z1:4"))
    w1 = sp.Matrix(sp.symbols("u1:4"))
    w2 = sp.Matrix(sp.symbols("w1:4"))
    f1 = sp.Matrix(sp.symbols("f1:4"))
    f2 = sp.Matrix(sp.symbols("g1:4"))
    tt = sp.Symbol("t")
    E = sp.Matrix(sp.symbols("E1:4"))
    dd = y1 - y2
    rr = sp.sqrt(dd.dot(dd))
    nn = dd / rr
    lag = (sum(m * (-1 + v.dot(v) / 2 + v.dot(v) ** 2 / 8) for m, v in ((m1, w1), (m2, w2)))
           + k / rr * (1 + A * (w1.dot(w1) + w2.dot(w2)) + B * w1.dot(w2) + C * nn.dot(w1) * nn.dot(w2)))
    dy1 = -E * tt + w1 * E.dot(y1)
    dy2 = -E * tt + w2 * E.dot(y2)
    dw1 = -E + f1 * E.dot(y1) + w1 * E.dot(w1)
    dw2 = -E + f2 * E.dot(y2) + w2 * E.dot(w2)
    dlag = sum(sp.diff(lag, y1[i]) * dy1[i] + sp.diff(lag, y2[i]) * dy2[i] + sp.diff(lag, w1[i]) * dw1[i] + sp.diff(lag, w2[i]) * dw2[i] for i in range(3))
    F = sum(m * (-E.dot(y) + v.dot(v) / 2 * E.dot(y)) for m, y, v in ((m1, y1, w1), (m2, y2, w2))) + k / rr * E.dot(y1 + y2) / 2

    def ddt(f):
        return (sum(sp.diff(f, y1[i]) * w1[i] + sp.diff(f, y2[i]) * w2[i] + sp.diff(f, w1[i]) * f1[i] + sp.diff(f, w2[i]) * f2[i] for i in range(3))
                + sp.diff(f, tt))

    rem = dlag - ddt(F)
    sub = {}
    for i in range(3):
        sub.update({w1[i]: lam * w1[i], w2[i]: lam * w2[i], f1[i]: lam ** 2 * f1[i], f2[i]: lam ** 2 * f2[i]})
    sub[k] = lam ** 2 * k
    remb = sp.expand(rem.subs(sub, simultaneous=True))
    low = sum(remb.coeff(lam, j) * lam ** j for j in range(4))
    half = 0 if mut("boost_half_dropped") else HALF
    expected = -lam ** 3 * k / rr * ((2 * A + B + half) * E.dot(w1 + w2) + (C + half) * nn.dot(E) * nn.dot(w1 + w2))
    checks.check("E4", sp.simplify(sp.expand(low - expected)) == 0,
                 "long-wave boost dx_a = -eps t + v_a (eps.x_a): the Lagrangian changes by dF/dt - (k/r)[(2a + b + 1/2) eps.(v1 + v2) + (c + 1/2)(n.eps)(n.(v1 + v2))] through third order (v ~ k^(1/2) ~ lambda)")
    rows = []
    for coeffs in ((Fr(3, 2), Fr(-7, 2), Fr(-1, 2)), (Fr(0), Fr(0), Fr(0))):
        a_, b_, c_ = coeffs
        rows.append([weight_minus_one(a_, b_, c_, Fr(1), s_, Fr(1)) for s_ in (Fr(0), Fr(1, 2), Fr(1, 3))])
    checks.check("E5", rows[0] == [Fr(0), Fr(0), Fr(0)] and rows[1] == [Fr(1), Fr(3, 2), Fr(4, 3)],
                 "in units of <U>/M: a circular orbit across and in its plane, and an isotropic state: the member's pull gives 0, 0, 0; the clock's pull alone gives 1, 3/2, 4/3 (W below one)")


# ============================================================================================ family F
FENCES = (
    "This note studies the expressly supplied model and only the conditional scope recorded in its claim_scope and Landing review boundary; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record", "Landing review boundary", "Dependencies")
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
    "per_element: executed - the member's curvature terms against the second-order curvature of the lengths delta + h on every plane wave, and the kinetic normalization alpha = K/4 as the only match",
    "per_site: executed - the member's plane-wave equations with and without the shift, solved exactly for every source that keeps the books, at nonzero frequency away from the wave pole (omega**2 != p**2, p != 0); the static clock law",
    "per_mode: executed - the one obstruction (K - 4 alpha) e / (4 alpha) at any other alpha, with and without the shift; the drifting relabellings without the shift",
    "per_block: executed - the pull between two slow bodies to order v^2; the weight of a bound pair from the P^2 coefficient and the tensor virial bracket; the boost remainder through third order",
    "lattice_wide: long wavelength; first order in 1/K; slow compact bodies in point form; spin couplings and the member's cubic order not supplied",
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
    print('scope: For the explicitly supplied continuum quadratic action, positive K and alpha, conserved sources and nonzero spatial momentum: the generic nonzero-frequency exchange formula requires omega² different from p². The static clock formula is separate. With supplied spinless point-body stress and a conservative near-zone prescription, the displayed order-v² velocity-dependent interaction gives W=1 through the first weak-binding order using tensor virial averages. No finite response at the wave pole, nonlinear completion, lattice result or physical gravity identification is established.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
