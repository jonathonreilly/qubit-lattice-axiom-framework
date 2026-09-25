#!/usr/bin/env python3
"""Exact checks: one record per site - pairs bound as neighbours have half the walker's speed squared on a line and never its
speed in every direction: two records of block 54's walk under block 78's compression, bound by a supplied neighbour possibility
shift (a hermitian term on the pair's two coins when they are adjacent), move on a line with exactly E = V + sin^2(K/2)/V (equal
coins), so c^2 = 1/2 for every binding; in space, at strong binding, the pair's second-order generator for keeping its bond is
5/2 - (1/2) cos K_a sigma_a sigma_a - sum_(b != a) cos K_b sigma_b sigma_b (exclusion halves the along-bond term), and for every
rotation-covariant possibility shift the sum over the three axes of a bound pair's weight matrix is at most 3/2, against 3 for a
free record (the supervisor's own derivation; blocks 54 and 78 as landed; block 115 placed; not adopted).

B (T1): the line, exact for every binding.
C (T2): the same-bond law at strong binding; exclusion halves the along-bond term.
D (T3): every covariant possibility shift; no bound pair has weight one along all three axes.
E (T4): controls - a free record, no exclusion, contact pairs, the timed term.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_PAIRS_BOUND_AS_NEIGHBOURS_HAVE_HALF_THE_WALKERS_SPEED_SQUARED_ON_A_LINE_AND_NEVER_ITS_SPEED_IN_EVERY_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_record_per_site_pairs_bound_as_neighbours_have_half_the_walkers_speed_squared_on_a_line_and_never_its_speed_in_every_direction_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "line_speed_forged": "B",
    "same_bond_unhalved": "C",
    "fermion_rolling_forged": "D",
    "axis_sum_forged": "D",
    "control_exclusion_injected": "E",
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, one record per site, the neighbour possibility shift and any timing of it are supplied; the memo does not define a time metric)")
# ============================================================================================ two records bound as neighbours, relative coordinate at total wave vector K
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
ID2 = sp.eye(2)
PAULI3 = (SX, SY, SZ)
PAULI1 = (SZ,)
KS = sp.symbols("K1 K2 K3", real=True)
TT = sp.symbols("t", real=True)
CC, SS = sp.symbols("c s", positive=True)
UU = sp.symbols("u")


def kr(a, b):
    return sp.kronecker_product(a, b)


SWAP4 = sp.Matrix(4, 4, lambda i, j: 1 if (i // 2 == j % 2 and i % 2 == j // 2) else 0)
UP = sp.Matrix([1, 0])
DN = sp.Matrix([0, 1])
SING = (kr(UP, DN) - kr(DN, UP)) / sp.sqrt(2)
TRIP = ((kr(UP, UP) - kr(DN, DN)) / sp.sqrt(2), sp.I * (kr(UP, UP) + kr(DN, DN)) / sp.sqrt(2), (kr(UP, DN) + kr(DN, UP)) / sp.sqrt(2))


def hop(a, sgn, pauli, K=KS):
    """<r|H2|r + sgn e_a> for two records of block 54's walk at total wave vector K (record 1's coin first)."""
    ph = sp.exp(sp.I * K[a] / 2)
    if sgn > 0:
        return (kr(pauli[a], ID2) * ph - kr(ID2, pauli[a]) / ph) / (2 * sp.I)
    return (-kr(pauli[a], ID2) / ph + kr(ID2, pauli[a]) * ph) / (2 * sp.I)


def bonds(dim):
    out = []
    for a in range(dim):
        e = [0] * dim
        e[a] = 1
        out.append(tuple(e))
        out.append(tuple(-x for x in e))
    return out


def hops_into(r2, pauli, K=KS):
    dim = len(r2)
    for a in range(dim):
        for sgn in (1, -1):
            rp = tuple(r2[i] - (sgn if i == a else 0) for i in range(dim))
            yield rp, hop(a, sgn, pauli, K)


def second_order(r1, r2, pauli, excl, bound, K=KS):
    """sum over intermediate positions r' (not in the bound set; not coincidence under exclusion) of <r1|H2|r'><r'|H2|r2>."""
    dim = len(r1)
    zero = tuple([0] * dim)
    tot = sp.zeros(4, 4)
    for rp, m2 in hops_into(r2, pauli, K):
        if rp in bound or (excl and rp == zero):
            continue
        for r1p, m1 in hops_into(rp, pauli, K):
            if r1p == r1:
                tot += m1 * m2
    return tot


def rewrite_trig(m):
    return m.applyfunc(lambda z: sp.simplify(sp.expand(sp.expand_complex(sp.expand(z).rewrite(sp.cos)))))


def sym_lambda(sign, excl):
    """the bound manifold's second-order generator on Z^3, exchange-symmetrised: blocks over the three positive bonds."""
    bd = set(bonds(3))
    pos = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    rows = []
    for ea in pos:
        row = []
        for eb in pos:
            meb = tuple(-x for x in eb)
            row.append(second_order(ea, eb, PAULI3, excl, bd) + second_order(ea, meb, PAULI3, excl, bd) * sign * SWAP4)
        rows.append(row)
    return sp.Matrix(sp.BlockMatrix(rows))


def red(z):
    z = sp.expand(z)
    z = z.subs(sp.conjugate(UU), 1 / UU).subs(sp.conjugate(CC), CC).subs(sp.conjugate(SS), SS)
    z = sp.expand(z).subs(SS ** 2, 1 - CC ** 2)
    return sp.simplify(z)


def hc(m):
    return m.T.applyfunc(sp.conjugate)


def restrict(lam, per_bond):
    cols = []
    for a in range(3):
        for v in per_bond(a):
            w = sp.zeros(12, 1)
            w[4 * a:4 * a + 4, 0] = v
            cols.append(w)
    b = sp.Matrix.hstack(*cols)
    return hc(b) * lam * b


def rest_levels(m0, blocks=None):
    """rest eigenspaces; blocks = list of index lists of rest-decoupled blocks with a known value (value, idx) or None."""
    out = []
    if blocks is None:
        for val, mult, vecs in m0.eigenvects():
            out.append((sp.simplify(val), [v.applyfunc(sp.simplify) for v in sp.GramSchmidt(vecs, True)]))
        return out
    n = m0.shape[0]
    for val, idx in blocks:
        if val is not None:
            out.append((val, [sp.eye(n)[:, i] for i in idx]))
            continue
        sub = m0.extract(idx, idx)
        for v2, mult, vecs in sub.eigenvects():
            full = []
            for v in sp.GramSchmidt(vecs, True):
                w = sp.zeros(n, 1)
                for k, i in enumerate(idx):
                    w[i] = v[k]
                full.append(w)
            out.append((sp.simplify(v2), full))
    return out


def weight_matrices(mr, levels, direction):
    """the K^2 form on each rest level along a direction: W = 2 (P L2 P + P L1 R L1 P) / |n|^2; also returns the first-order blocks."""
    mt = mr.subs({KS[i]: TT * direction[i] for i in range(3)})
    m1 = mt.diff(TT).subs(TT, 0).applyfunc(red)
    m2 = (mt.diff(TT, 2).subs(TT, 0) / 2).applyfunc(red)
    n2 = sum(x * x for x in direction)
    n = mr.shape[0]
    out = []
    for lam, vs in levels:
        q = sp.Matrix.hstack(*vs)
        first = (hc(q) * m1 * q).applyfunc(red)
        r = sp.zeros(n, n)
        for lam2, vs2 in levels:
            if sp.simplify(lam2 - lam) == 0:
                continue
            q2 = sp.Matrix.hstack(*vs2)
            r += q2 * hc(q2) / (lam - lam2)
        w = (2 * (hc(q) * m2 * q + hc(q) * m1 * r * m1 * q) / n2).applyfunc(red)
        out.append((lam, first, w))
    return out


def axis_sums(mr, levels):
    """per rest level: the first-order blocks vanish along every axis, and the sum over the three axes of the weight matrix."""
    tot = None
    first_zero = True
    for d in range(3):
        e = [0, 0, 0]
        e[d] = 1
        res = weight_matrices(mr, levels, tuple(e))
        if tot is None:
            tot = [w for (_, _, w) in res]
        else:
            tot = [tot[i] + res[i][2] for i in range(len(res))]
        first_zero = first_zero and all(f == sp.zeros(*f.shape) for (_, f, _) in res)
    return first_zero, [(levels[i][0], tot[i].applyfunc(red)) for i in range(len(levels))]


def scalar_of(m):
    """m is a multiple of the identity: return the multiple, else None."""
    v = m[0, 0]
    if (m - v * sp.eye(m.shape[0])).applyfunc(red) == sp.zeros(*m.shape):
        return red(v)
    return None


def ray(a):
    return CC * SING + UU * SS * TRIP[a]


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: on the line, under one record per site, a pair bound as neighbours has E = V + b^2/V exactly."""
    V = sp.symbols("V", nonzero=True, real=True)
    K = sp.symbols("K", real=True)
    z, E, r = sp.symbols("z E r")
    ok = True
    # relative generator on the line (walkers sigma_z D), coins (s1, s2) = eigenvalues of sigma_z
    rel = {}
    for s1 in (1, -1):
        for s2 in (1, -1):
            ap = (s1 * sp.exp(sp.I * K / 2) - s2 * sp.exp(-sp.I * K / 2)) / (2 * sp.I)   # coefficient of phi(r + 1)
            am = (-s1 * sp.exp(-sp.I * K / 2) + s2 * sp.exp(sp.I * K / 2)) / (2 * sp.I)  # coefficient of phi(r - 1)
            rel[(s1, s2)] = (sp.simplify(sp.expand_complex(ap)), sp.simplify(sp.expand_complex(am)))
    b_co = sp.sin(K / 2)
    ok = ok and sp.simplify(rel[(1, 1)][0] - b_co) == 0 and sp.simplify(rel[(1, 1)][1] - b_co) == 0
    ok = ok and sp.simplify(rel[(1, -1)][0] + sp.I * sp.cos(K / 2)) == 0 and sp.simplify(rel[(1, -1)][1] - sp.I * sp.cos(K / 2)) == 0
    # the half-line r >= 1 with phi(0) = 0 (exclusion), V at r = 1: phi(r) = z^(r-1), z = b/V, E = V + b^2/V
    bb = sp.symbols("b", positive=True)
    zz = bb / V
    EE = V + bb ** 2 / V
    ok = ok and sp.simplify(EE - (bb * zz + V)) == 0                    # r = 1: E phi(1) = b phi(2) + b phi(0) + V phi(1), phi(0) = 0
    ok = ok and sp.simplify(EE - bb * (zz + 1 / zz)) == 0               # r >= 2: E = b (z + 1/z)
    # the counter-moving coins: phi(r) = i^r chi(r) turns i cos(K/2) (-phi(r+1) + phi(r-1)) ... into cos(K/2)(chi(r+1) + chi(r-1))
    chi = sp.Function("chi")
    lhs = (rel[(1, -1)][0] * sp.I ** (r + 1) * chi(r + 1) + rel[(1, -1)][1] * sp.I ** (r - 1) * chi(r - 1)) / sp.I ** r
    ok = ok and sp.simplify(sp.expand(lhs - sp.cos(K / 2) * (chi(r + 1) + chi(r - 1)))) == 0
    e_co = V + sp.sin(K / 2) ** 2 / V
    e_ct = V + sp.cos(K / 2) ** 2 / V
    c2_co = sp.simplify(sp.diff(e_co ** 2 / 2, K, 2).subs(K, 0))
    c2_ct = sp.simplify(sp.diff(e_ct ** 2 / 2, K, 2).subs(K, 0))
    target_co = sp.Rational(1, 2) if not mut("line_speed_forged") else sp.Integer(1)
    ok = ok and sp.simplify(c2_co - target_co) == 0 and sp.simplify(c2_ct - (-sp.Rational(1, 2) - 1 / (2 * V ** 2))) == 0
    # without exclusion: the even channel phi(0) = x: x = 2b/E, E = b(z + x) + V, E = b(z + 1/z); series E = V + 3 b^2/V + O(b^4)
    e2, e4 = sp.symbols("e2 e4")
    Es = V + e2 * bb ** 2 + e4 * bb ** 4
    xs = 2 * bb / Es
    zs = bb / (V + bb * xs)          # from b/z = b x + V
    resid = sp.series(Es - bb * zs - bb / zs, bb, 0, 5).removeO()
    sol = sp.solve([sp.expand(resid).coeff(bb, 2), sp.expand(resid).coeff(bb, 4)], [e2, e4], dict=True)
    ok_even = len(sol) == 1 and sp.simplify(sol[0][e2] - 3 / V) == 0
    c2_even = sp.simplify(sp.diff((V + 3 * sp.sin(K / 2) ** 2 / V) ** 2 / 2, K, 2).subs(K, 0))
    ok_even = ok_even and c2_even == sp.Rational(3, 2)
    checks.check("B1", ok and ok_even,
                 "T1: on the line (walkers sigma_z D), under one record per site and for either exchange sign, a pair of equal coins bound as neighbours by V has exactly E = V + sin^2(K/2)/V (the half-line wave z^(r-1), z = sin(K/2)/V), so c^2 = d^2(E^2/2)/dK^2 at rest is 1/2 for every V: half the walker's; opposite coins have E = V + cos^2(K/2)/V exactly, c^2 = -1/2 - 1/(2V^2), inverted; without exclusion the even channel reaches coincidence and E = V + 3 b^2/V + O(b^4), c^2 = 3/2")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the same-bond law at strong binding, in three dimensions and on the line."""
    bd3 = set(bonds(3))
    excl = not mut("same_bond_unhalved")
    ok = True
    for a in range(3):
        e = [0, 0, 0]
        e[a] = 1
        ea = tuple(e)
        mea = tuple(-x for x in e)
        blk = rewrite_trig(second_order(ea, ea, PAULI3, excl, bd3))
        law = sp.Rational(5, 2) * sp.eye(4) - sp.cos(KS[a]) * kr(PAULI3[a], PAULI3[a]) / 2 - sum((sp.cos(KS[b]) * kr(PAULI3[b], PAULI3[b]) for b in range(3) if b != a), sp.zeros(4, 4))
        ok = ok and rewrite_trig(blk - law) == sp.zeros(4, 4)
        ok = ok and second_order(ea, mea, PAULI3, True, bd3) == sp.zeros(4, 4)
    blk1 = rewrite_trig(second_order((1,), (1,), PAULI1, True, set(bonds(1)), K=(KS[0],)))
    law1 = sp.eye(4) / 2 - sp.cos(KS[0]) * kr(SZ, SZ) / 2
    ok1 = rewrite_trig(blk1 - law1) == sp.zeros(4, 4)
    # on the line the law is exact: equal coins sigma_z x sigma_z = 1 give 1/2 - cos(K)/2 = sin^2(K/2), the T1 energy's b^2
    ok1 = ok1 and sp.simplify(sp.Rational(1, 2) - sp.cos(KS[0]) / 2 - sp.sin(KS[0] / 2) ** 2) == 0
    # bipartite: every bond position has odd coordinate sum and each step changes it by one, so no odd return (next order is g^-3)
    ok_par = all(sum(r) % 2 == 1 for r in bonds(3))
    checks.check("C1", ok and ok1 and ok_par,
                 "T2: for any coins on the bond e_a, the strongly bound pair's second-order generator for keeping its bond is exactly 5/2 - (1/2) cos K_a sigma_a sigma_a - sum_{b != a} cos K_b sigma_b sigma_b in three dimensions (1/2 - (1/2) cos K sigma_z sigma_z on the line, where it is T1 exactly); exclusion halves the term along the bond (the rear record cannot step first) and removes any two-step link between the bond's ends; E = g m0 + Lambda/(g m0) + O(g^-3), since no odd path returns to a bond")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: every rotation-covariant possibility shift; no bound pair has weight one along all three axes."""
    # (a) the commutant of the bond's stabiliser: C4 about the bond, and a half-turn across it followed by exchange
    u4 = (sp.eye(2) - sp.I * SZ) / sp.sqrt(2)
    c4 = kr(u4, u4)
    h2 = kr(-sp.I * SX, -sp.I * SX)
    xs = sp.symbols("x0:16", real=True)
    basis16 = []
    for i in range(4):
        for j in range(4):
            basis16.append(kr((ID2, SX, SY, SZ)[i], (ID2, SX, SY, SZ)[j]))
    m = sum((xs[k] * basis16[k] for k in range(16)), sp.zeros(4, 4))
    eqs = []
    for g in (c4, SWAP4 * h2):
        d = (g * m - m * g).applyfunc(sp.expand)
        for z in d:
            eqs += [sp.re(z), sp.im(z)]
    sol = sp.linsolve([sp.expand(e) for e in eqs if e != 0], xs)
    free = set()
    for tup in sol:
        for z in tup:
            free |= z.free_symbols
    pm = TRIP[0] * hc(TRIP[0]) + TRIP[1] * hc(TRIP[1])
    gens = (pm, SING * hc(SING), TRIP[2] * hc(TRIP[2]), SING * hc(TRIP[2]) + TRIP[2] * hc(SING), sp.I * (SING * hc(TRIP[2]) - TRIP[2] * hc(SING)))
    ok_comm = len(free) == 5 and all(((g * x - x * g).applyfunc(sp.simplify) == sp.zeros(4, 4)) for x in gens for g in (c4, SWAP4 * h2))
    # (b)-(e) the ground spaces: a ray in the zero-spin plane, the spin +-1 plane, and the accidental unions
    lam_f = sym_lambda(-1, True)
    lam_b = sym_lambda(1, True)
    results = {}
    ok_first = True
    # pure ray, symbolic mixing c = cos(theta) and phase u
    for nm, lam in (("f", lam_f), ("b", lam_b)):
        mr = restrict(lam, lambda a: [ray(a)])
        m0 = mr.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}).applyfunc(red)
        ok_first = ok_first and (m0 - (4 * CC ** 2 + 1) * sp.eye(3)).applyfunc(red) == sp.zeros(3, 3)
        fz, sums = axis_sums(mr, [(4 * CC ** 2 + 1, [sp.eye(3)[:, i] for i in range(3)])])
        ok_first = ok_first and fz
        results[("ray", nm)] = [scalar_of(w) for (_, w) in sums]
        if nm == "f":
            diag = sp.diag(*[sp.Rational(5, 2) + sp.cos(KS[a]) / 2 + (2 * CC ** 2 - 1) * sum(sp.cos(KS[b]) for b in range(3) if b != a) for a in range(3)])
            ok_ray_f = rewrite_trig(mr.applyfunc(red) - diag).applyfunc(red) == sp.zeros(3, 3)
            if mut("fermion_rolling_forged"):
                ok_ray_f = not ok_ray_f
    # the spin +-1 plane
    for nm, lam in (("f", lam_f), ("b", lam_b)):
        mr = restrict(lam, lambda a: [TRIP[b] for b in range(3) if b != a])
        m0 = mr.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}).applyfunc(red)
        fz, sums = axis_sums(mr, rest_levels(m0))
        ok_first = ok_first and fz
        results[("pm", nm)] = [(v, scalar_of(w)) for (v, w) in sums]
    # the zero-spin plane (both rays), the coin-blind shift (all four), and the ray with the spin +-1 plane (symbolic mixing)
    for nm, lam in (("f", lam_f), ("b", lam_b)):
        for key, per in (("plane0", lambda a: [SING, TRIP[a]]), ("all", lambda a: [SING] + list(TRIP))):
            mr = restrict(lam, per)
            m0 = mr.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}).applyfunc(red)
            fz, sums = axis_sums(mr, rest_levels(m0))
            ok_first = ok_first and fz
            results[(key, nm)] = [(v, scalar_of(w)) for (v, w) in sums]
        mr = restrict(lam, lambda a: [ray(a)] + [TRIP[b] for b in range(3) if b != a])
        m0 = mr.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}).applyfunc(red)
        blocks = [(None, [1, 2, 4, 5, 7, 8]), (4 * CC ** 2 + 1, [0, 3, 6])]
        fz, sums = axis_sums(mr, rest_levels(m0, blocks))
        ok_first = ok_first and fz
        results[("union", nm)] = [(v, scalar_of(w)) for (v, w) in sums]
    # the two coincidences of the union, where the ray's level meets a spin +-1 level: fermions c^2 = 3/4, bosons c^2 = 1/4
    spectra = {}
    for nm, lam, c2v in (("f", lam_f, sp.Rational(3, 4)), ("b", lam_b, sp.Rational(1, 4))):
        mr = restrict(lam, lambda a: [ray(a)] + [TRIP[b] for b in range(3) if b != a]).subs({CC: sp.sqrt(c2v), SS: sp.sqrt(1 - c2v), UU: 1})
        m0 = mr.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}).applyfunc(sp.simplify)
        fz, sums = axis_sums(mr, rest_levels(m0))
        ok_first = ok_first and fz
        results[("coincide", nm)] = [(v, scalar_of(w)) for (v, w) in sums]
        spectra[nm] = [(sp.simplify(v), {sp.nsimplify(k2): m2 for k2, m2 in w.eigenvals().items()}) for (v, w) in sums]
    mu = CC ** 2
    expect = {
        ("ray", "f"): [(3 - 8 * mu) / 2], ("ray", "b"): [(3 - 8 * mu) / 2],
    }
    ok_vals = all(sp.simplify(results[k][0] - expect[k][0]) == 0 for k in expect)
    want_pm = {"f": {0: sp.Rational(3, 2), 4: -sp.Rational(1, 2)}, "b": {2: sp.Rational(1, 2)}}
    ok_vals = ok_vals and all(dict((sp.simplify(v), w) for v, w in results[("pm", nm)]) == want_pm[nm] for nm in ("f", "b"))
    # every per-level axis sum is a single number (a multiple of the identity on the level), except at the fermions' coincidence,
    # where the merged level keeps its two values -3/4 and -1/2; every value is at most 3/2 for c^2 in [0, 1]
    allsums = [results[("ray", "f")][0], results[("ray", "b")][0]]
    for key in ("pm", "plane0", "all", "union", "coincide"):
        for nm in ("f", "b"):
            allsums += [w for (_, w) in results[(key, nm)] if w is not None]
    nonscalar = [(key, nm, v) for key in ("pm", "plane0", "all", "union", "coincide") for nm in ("f", "b") for (v, w) in results[(key, nm)] if w is None]
    ok_scalar = nonscalar == [("coincide", "f", 4)] and dict(spectra["f"]).get(4) == {-sp.Rational(3, 4): 3, -sp.Rational(1, 2): 3}
    allsums += [sp.Rational(-3, 4), sp.Rational(-1, 2)]
    bound = sp.Rational(3, 2)
    if mut("axis_sum_forged"):
        bound = sp.Rational(1, 2)
    ok_bound = True
    for w in allsums:
        gap = sp.factor(sp.simplify(bound - w))
        if gap.free_symbols:
            num, den = sp.fraction(sp.together(gap))
            pn = sp.Poly(sp.expand(num), CC)
            pd = sp.Poly(sp.expand(den), CC)
            ok_bound = ok_bound and all(cf >= 0 for cf in pn.coeffs()) and all(cf >= 0 for cf in pd.coeffs())
        else:
            ok_bound = ok_bound and gap >= 0
    top = max((w.subs(CC, 0) if hasattr(w, "free_symbols") and w.free_symbols else w) for w in allsums)
    checks.check("D1", ok_comm and ok_first and ok_ray_f and ok_vals and ok_scalar and ok_bound and top == sp.Rational(3, 2),
                 "T3: a possibility shift on a bond that is covariant under the bond's rotations and the records' exchange is mu_pm (spin +-1 along the bond) plus any hermitian form on the zero-spin plane {S, t_a} (five real numbers); at strong binding its bound pairs live on one of: a ray cos(theta) S + e^(i phi) sin(theta) t_a, the spin +-1 plane, or an accidental union; fermion pairs on a ray never roll and have E^2 = g^2 m0^2 + 2(5/2 + (1/2) cos K_a + (2 cos^2(theta) - 1) sum_(b != a) cos K_b), weight -1/2 along the bond and 1 - 2 cos^2(theta) across; on every rest level of every case the sum over the three axes of the weight matrix is one number, (3 - 8 cos^2(theta))/2 on a ray, 3/2 or -1/2 (spin +-1 plane, fermions), 1/2 (bosons), and in the accidental unions rational functions of cos^2(theta) (two values, -3/4 and -1/2, on the one level where a ray meets a spin +-1 level of the same kind), never above 3/2, which the pairs with zero spin along the bond reach: no bound pair has weight one along all three axes, which needs 3")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: controls - a free record, the pair without exclusion, contact pairs, and the timed neighbour term."""
    k = sp.symbols("k1:4", real=True)
    eps2 = sum(sp.sin(x) ** 2 for x in k)
    ok_free = all(sp.simplify(sp.diff(eps2 / 2, k[d], 2) - sp.cos(2 * k[d])) == 0 for d in range(3))
    ok_free = ok_free and sum(sp.diff(eps2 / 2, k[d], 2).subs({x: 0 for x in k}) for d in range(3)) == 3
    bd3 = set(bonds(3))
    excl = mut("control_exclusion_injected")
    blk = rewrite_trig(second_order((1, 0, 0), (1, 0, 0), PAULI3, excl, bd3))
    law = 3 * sp.eye(4) - sum((sp.cos(KS[b]) * kr(PAULI3[b], PAULI3[b]) for b in range(3)), sp.zeros(4, 4))
    ok_noex = rewrite_trig(blk - law) == sp.zeros(4, 4)
    ok_noex = ok_noex and second_order((1, 0, 0), (-1, 0, 0), PAULI3, excl, bd3) != sp.zeros(4, 4)
    # contact pairs (block 115, no exclusion): the bound set is coincidence; exchange acts on the coins alone there
    blkc = rewrite_trig(second_order((0, 0, 0), (0, 0, 0), PAULI3, False, {(0, 0, 0)}))
    ok_ct = rewrite_trig(blkc - law) == sp.zeros(4, 4)
    wts = []
    for v in (SING,) + TRIP:
        wts.append([sp.simplify((hc(v) * kr(PAULI3[b], PAULI3[b]) * v)[0]) for b in range(3)])
    ok_ct = ok_ct and wts[0] == [-1, -1, -1] and all(wts[1 + a][a] == -1 and sum(wts[1 + a]) == 1 for a in range(3))
    # the neighbour term timed like the hops keeps the clock's scaling (block 115 T5's identity, for a bond)
    lam_, x1, x2 = sp.symbols("lambda x1 x2", positive=True)
    w = lambda x: lam_ ** (2 * x)
    hop_t = sp.sqrt(w(x1) * w(x1 + 1))
    bond_t = sp.sqrt(w(x1) * w(x2))
    ok_timed = sp.simplify(hop_t.subs(x1, x1 + 1) / hop_t - lam_ ** 2) == 0 and sp.simplify(bond_t.subs({x1: x1 + 1, x2: x2 + 1}, simultaneous=True) / bond_t - lam_ ** 2) == 0
    checks.check("E1", ok_free and ok_noex and ok_ct and ok_timed,
                 "T4: a free record has d^2(eps^2/2)/dk_d^2 = cos 2k_d, one along each axis at rest (sum 3); without exclusion the same-bond law is 3 - sum_b cos K_b sigma_b sigma_b (the along-bond term not halved) and the bond's ends are linked through coincidence; contact pairs (block 115) have the same law at coincidence, so their axis weights are the coin correlations: -1, -1, -1 for the singlet, and -1 along a, +1 across for t_a (sum 1); the neighbour term timed by sqrt(w(x1) w(x2)) scales like the hops under a joint translation")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with a supplied neighbour possibility shift and block 115 placed; it reports how pairs bound by that shift move, on a line and in space; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
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
    "per_element: executed - the line's bound pair exactly (the half-line wave for both coin alignments and every V) and the same-bond law as a symbolic operator identity in K on Z^3 and on the line",
    "per_site: executed - every bond position and every intermediate position of the second-order generator; exclusion's removed step; the odd coordinate sum of every bond position",
    "per_mode: executed - the commutant of the bond's rotations and exchange (five real numbers) and every ground space it allows: a ray with symbolic mixing and phase, the spin +-1 plane, the zero-spin plane, the coin-blind shift, the union with symbolic mixing and its two coincidences",
    "per_block: executed - the weight matrices along each axis on every rest level, their first-order blocks and their sum over the axes; the controls (a free record, no exclusion, contact pairs, the timed term)",
    "lattice_wide: two records; strong binding at leading order in 1/g in three dimensions (exact for every binding on the line); moderate binding, the staggered mass, pushes, non-covariant shifts and more records not treated",
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
    print("scope: one record per site - pairs bound as neighbours have c^2 = 1/2 on a line for every binding, and in space, at strong binding, no rotation-covariant possibility shift gives a bound pair weight one along all three axes (the axis sum is at most 3/2, against 3); supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
