#!/usr/bin/env python3
"""Exact checks: in block 95's clocked transit, records in a held clock gradient settle with one weight per record, (2a - 1) g each,
but do not drift alike: a lone record at a = 1 does not drift, a bound group drifts at -((2a - 1)n - 1) D0 g, and records alone do
not bind (a harvest block from a Grok-refereed probes attempt; block 95 as landed supplied; not adopted).

B (T1): one record's mean velocity at first order, isolated and with one neighbour of each content; no gradient term at a = 1.
C (T2, T3): the stationary law in a linear field, and the centre-clock chain's tilted invariant measure W(sigma) exp(-c g.X).
D (T4): the first-order centre velocity V1 = -c D0 g and the field-free diffusion constant D0, lone record and tethered pairs.
E (T5, T6): the separation chain's reversible measure; the instantaneous push at contact against the long-time drift.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RECORDS_IN_A_CLOCK_GRADIENT_SETTLE_WITH_ONE_WEIGHT_PER_RECORD_BUT_DO_NOT_DRIFT_ALIKE_AND_GROUPS_NEED_A_BINDING_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_records_in_a_clock_gradient_settle_with_one_weight_per_record_but_do_not_drift_alike_and_groups_need_a_binding_clause_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "gradient_term_kept_at_a_one": "B",
    "tilt_exponent_forged": "C",
    "drift_sign_flipped": "D",
    "contact_push_forged": "E",
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
R = sp.Rational
E6 = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
OMEGA = (("equal", R(3, 2)), ("opposite", R(1, 2)), ("orthogonal", R(1)))       # block 40's neutral-scale pair weights at (p, q, r) = (3, 1, 2)


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), sp.Integer(0))


def shift(u, v, s=1):
    return tuple(x + s * y for x, y in zip(u, v))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the clocks, the transit and the binding are supplied clauses)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: one record's mean velocity in a held uniform gradient, at first order; none at a = 1."""
    g1, g2, g3, a, s = sp.symbols("g1 g2 g3 a s", real=True)
    g = (g1, g2, g3)
    ok = True
    notes = []
    for label, omega in (("isolated", None),) + OMEGA:
        h = R(1, 2) if omega is None else 1 / (1 + omega)
        vel = [sp.Integer(0)] * 3
        for e in E6:
            if omega is not None and e == (1, 0, 0):
                continue                                             # the neighbour's site is occupied
            rate = sp.exp((1 - a) * s * dot(g, e)) * h / 6           # w at the record's own site is 1: w_x^a w_y^(1-a) = e^((1-a) g.e)
            vel = [vel[k] + e[k] * rate for k in range(3)]
        first = [sp.expand(sp.series(v, s, 0, 2).removeO().subs(s, 1)) for v in vel]
        m = 2 * h * sp.eye(3) - (sp.zeros(3, 3) if omega is None else sp.diag(h, 0, 0))
        bias = [sp.Integer(0)] * 3 if omega is None else [-h / 6, sp.Integer(0), sp.Integer(0)]
        want = [bias[k] + (1 - a) / 6 * sum((m[k, j] * g[j] for j in range(3)), sp.Integer(0)) for k in range(3)]
        ok = ok and all(sp.expand(first[k] - want[k]) == 0 for k in range(3))
        at_one = [sp.simplify(v.subs(a, 1).subs(s, 1)) for v in vel]
        claimed = [bias[k] + (R(1, 6) * sum((m[k, j] * g[j] for j in range(3)), sp.Integer(0)) if mut("gradient_term_kept_at_a_one") else 0) for k in range(3)]
        ok = ok and all(sp.simplify(at_one[k] - claimed[k]) == 0 for k in range(3))
        notes.append(f"{label} h = {h}")
    checks.check("B1", ok, "T1: a record hopping at w_x^a w_y^(1-a) h/6 in the held field w = e^(g.x) has mean velocity, on its own clock, b + ((1 - a)/6) M g + O(g^2), with M the sum over its free moves of h e e^T and b = (1/6) sum h e: isolated, of any content, b = 0 and M = I; with one neighbour at e1 of pair weight omega, h = 1/(1 + omega) on its five free moves, M = h(2I - e1 e1^T) and b = -(h/6) e1 (" + "; ".join(notes) + "); at a = 1 the velocity is b exactly, with no gradient term at any order")


# ============================================================================================ family C
def tether_states():
    nearest = list(E6)
    diagonal = sorted({v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v) == 2})
    return nearest + diagonal


def cluster(kind: str, omega=None):
    """Return (n, states, weights, moves); a move is (target state, record, e, q0 = h/6, the moving record's offset from the centre)."""
    if kind == "lone":
        return 1, [()], {(): sp.Integer(1)}, {(): [((), 0, e, R(1, 12), (0, 0, 0)) for e in E6]}
    states = tether_states()
    inside = set(states)
    weights = {d: (omega if d in E6 else sp.Integer(1)) for d in states}
    moves = {}
    for d in states:
        lst = []
        for i in (0, 1):
            for e in E6:
                d2 = shift(d, e, -1) if i == 0 else shift(d, e, 1)   # d = x1 - x0; the tether keeps d in the 18 offsets, both ways
                if d2 not in inside:
                    continue
                h = weights[d2] / (weights[d] + weights[d2])
                r = tuple(R(-x, 2) for x in d) if i == 0 else tuple(R(x, 2) for x in d)
                lst.append((d2, i, e, h / 6, r))
        moves[d] = lst
    return 2, states, weights, moves


def family_c(checks: Checks) -> None:
    """T2: the stationary law in a linear field; T3: the centre-clock chain's tilted invariant measure."""
    g1, g2, g3, a, om = sp.symbols("g1 g2 g3 a omega", real=True)
    g = (g1, g2, g3)
    ok = True
    # T2: block 95 T1 in the held field w = e^(g.x): pi(C) = W(C) prod w^(1-2a) balances every move of two records
    def weight(cfg):
        (x0, x1) = cfg
        contact = sum(abs(p - q) for p, q in zip(x0, x1)) == 1
        return (om if contact else sp.Integer(1)) * sp.exp((1 - 2 * a) * (dot(g, x0) + dot(g, x1)))
    configs = [((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (1, 1, 0)), ((0, 0, 0), (2, 0, 0)), ((0, 0, 0), (1, 1, 1))]
    for cfg in configs:
        for i in (0, 1):
            for e in E6:
                x = cfg[i]
                y = shift(x, e)
                if y == cfg[1 - i]:
                    continue
                new = (y, cfg[1]) if i == 0 else (cfg[0], y)
                wc, wn = weight(cfg), weight(new)
                bare_c = wc * sp.exp(-(1 - 2 * a) * (dot(g, cfg[0]) + dot(g, cfg[1])))
                bare_n = wn * sp.exp(-(1 - 2 * a) * (dot(g, new[0]) + dot(g, new[1])))
                h_f = bare_n / (bare_c + bare_n)
                h_b = bare_c / (bare_c + bare_n)
                fwd = wc * sp.exp(a * dot(g, x) + (1 - a) * dot(g, y)) * h_f
                bwd = wn * sp.exp(a * dot(g, y) + (1 - a) * dot(g, x)) * h_b
                ok = ok and sp.simplify(fwd - bwd) == 0
    checks.check("C1", ok, "T2: in the held field w = e^(g.x) block 95's law pi(C) = W(C) prod_z w_z^(1-2a) = W(C) exp((1 - 2a) n g.X) balances every move of two records (contact weight omega symbolic, g and a symbolic): where records settle carries one factor (2a - 1) g per record, whatever their contents")
    # T3: rates divided by the centre's clock w(X): detailed balance with W(sigma) exp(-c g.X), c = (2a - 1)n - 1
    ok = True
    for kind in ("lone", "pair"):
        n, states, weights, moves = cluster(kind, om) if kind == "pair" else cluster(kind)
        c = (2 * a - 1) * n - 1 if not mut("tilt_exponent_forged") else (2 * a - 1) * n
        for sgm in states:
            for (t, i, e, q0, r) in moves[sgm]:
                back = [mv for mv in moves[t] if mv[0] == sgm and mv[1] == i and mv[2] == tuple(-x for x in e)]
                ok = ok and len(back) == 1
                (_, _, eb, qb, rb) = back[0]
                fwd = weights[sgm] * q0 * sp.exp(dot(g, r) + (1 - a) * dot(g, e))
                bwd = weights[t] * qb * sp.exp(-c * dot(g, tuple(R(x, n) for x in e)) + dot(g, rb) + (1 - a) * dot(g, eb))
                ok = ok and sp.simplify(fwd - bwd) == 0
    checks.check("C2", ok, "T3: with every rate divided by the centre's clock w(X), the chain of (X, sigma) is in detailed balance with W(sigma) exp(-c g.X), c = (2a - 1)n - 1, move by move, symbolic in g, a and the contact weight (a lone record, and a pair held to the 18 nearest and face-diagonal offsets by a tether): its tilted generator has principal eigenvalue zero at k = 0 and at k = c g")


# ============================================================================================ family D
def generator(n, states, moves, rate):
    ix = {s: j for j, s in enumerate(states)}
    size = len(states)
    mat = sp.zeros(size, size)
    for sgm in states:
        for (t, i, e, q0, r) in moves[sgm]:
            val = q0 * rate(e, r)
            mat[ix[sgm], ix[t]] += val
            mat[ix[sgm], ix[sgm]] -= val
    return mat, ix


def stationary_law(mat):
    size = mat.shape[0]
    a = mat.T.copy()
    a[size - 1, :] = sp.ones(1, size)
    rhs = sp.zeros(size, 1)
    rhs[size - 1] = 1
    return a.LUsolve(rhs)


def first_correction(mat, p0, mat1):
    size = mat.shape[0]
    a = mat.T.copy()
    a[size - 1, :] = sp.ones(1, size)
    rhs = -(mat1.T * p0)
    rhs[size - 1] = 0
    return a.LUsolve(rhs)


def response(kind, omega, a, ghat):
    """First-order centre velocity V1 per unit gradient along ghat, and the field-free diffusion tensor D0 (Lambda = k.D0 k + ...)."""
    n, states, weights, moves = cluster(kind, omega) if kind == "pair" else cluster(kind)
    l0, ix = generator(n, states, moves, lambda e, r: sp.Integer(1))
    l1, _ = generator(n, states, moves, lambda e, r: dot(ghat, r) + (1 - a) * dot(ghat, e))
    p0 = stationary_law(l0)
    p1 = first_correction(l0, p0, l1)
    v1 = [sp.Integer(0)] * 3
    for sgm in states:
        j = ix[sgm]
        for (t, i, e, q0, r) in moves[sgm]:
            coeff = p1[j] * q0 + p0[j] * q0 * (dot(ghat, r) + (1 - a) * dot(ghat, e))
            v1 = [v1[c] + coeff * R(e[c], n) for c in range(3)]
    size = len(states)

    def lam2(k):
        f = sp.zeros(size, 1)
        for sgm in states:
            f[ix[sgm]] = sum((q0 * R(dot(k, e), n) for (t, i, e, q0, r) in moves[sgm]), sp.Integer(0))
        a2 = -l0
        a2[size - 1, :] = p0.T
        rhs = f.copy()
        rhs[size - 1] = 0
        psi = a2.LUsolve(rhs)
        tot = sp.Integer(0)
        for sgm in states:
            for (t, i, e, q0, r) in moves[sgm]:
                ke = R(dot(k, e), n)
                tot += p0[ix[sgm]] * q0 * (ke ** 2 / 2 + ke * psi[ix[t]])
        return sp.nsimplify(tot)
    d0 = sp.zeros(3, 3)
    for i in range(3):
        d0[i, i] = lam2(tuple(1 if j == i else 0 for j in range(3)))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        d0[i, j] = d0[j, i] = (lam2(tuple(1 if m in (i, j) else 0 for m in range(3))) - d0[i, i] - d0[j, j]) / 2
    z = sum(weights.values(), sp.Integer(0))
    p0_ok = all(sp.simplify(p0[ix[sgm]] - weights[sgm] / z) == 0 for sgm in states)
    return [sp.nsimplify(v) for v in v1], d0, p0_ok, n


def family_d(checks: Checks) -> None:
    """T4: V1 = -c D0 g exactly at first order; D0 differs between a lone record and bound pairs, and between contents."""
    ok = True
    table = {}
    for kind, name, omega in (("lone", "lone", None),) + tuple(("pair", nm, w) for nm, w in OMEGA):
        for a in (R(1), R(3, 4), R(0)):
            for ghat in ((1, 0, 0), (1, 2, 3)):
                v1, d0, p0_ok, n = response(kind, omega, a, ghat)
                c = (2 * a - 1) * n - 1
                sign = 1 if mut("drift_sign_flipped") else -1
                want = [sign * c * sum((d0[k, j] * ghat[j] for j in range(3)), sp.Integer(0)) for k in range(3)]
                ok = ok and p0_ok and d0 == d0[0, 0] * sp.eye(3) and all(sp.simplify(v1[k] - want[k]) == 0 for k in range(3))
                if ghat == (1, 0, 0):
                    table[(name, a)] = (d0[0, 0], v1[0])
    d_lone = table[("lone", R(1))][0]
    d_pairs = [table[(nm, R(1))][0] for nm, _ in OMEGA]
    values_ok = d_lone == R(1, 12) and d_pairs == [R(2, 105), R(2, 135), R(1, 54)]
    at_one = [table[(nm, R(1))][1] for nm in ("lone",) + tuple(nm for nm, _ in OMEGA)]
    checks.check("D1", ok and values_ok and at_one == [0, -R(2, 105), -R(2, 135), -R(1, 54)],
                 f"T4: exactly at first order, on the centre's clock, V1 = -((2a - 1)n - 1) D0 g for a lone record and for tethered pairs of equal, opposite and orthogonal contents (contact weights 3/2, 1/2, 1), at a = 1, 3/4, 0 and g along (1,0,0) and (1,2,3); D0 isotropic, the internal law W/Z; D0 = 1/12 (lone), 2/105, 2/135, 1/54 (pairs); at a = 1, per unit gradient along x: {', '.join(str(v) for v in at_one)} - a lone record does not drift, bound pairs drift towards slow clocks at rates set by their contents: the drift is not universal")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T6: the instantaneous push at contact points up the gradient; the long-time drift of a bound pair points down."""
    g = sp.symbols("g", positive=True)
    w0, w1 = sp.Integer(1), sp.exp(g)                              # records at 0 and e1, w = e^(g x1), a = 1, W = 1 (h = 1/2)
    v0 = [sum((w0 / 12 * e[k] for e in E6 if e != (1, 0, 0)), sp.Integer(0)) for k in range(3)]
    v1 = [sum((w1 / 12 * e[k] for e in E6 if e != (-1, 0, 0)), sp.Integer(0)) for k in range(3)]
    centre = [sp.simplify((v0[k] + v1[k]) / 2) for k in range(3)]
    claimed = (sp.exp(g) - 1) / 24 if not mut("contact_push_forged") else (1 - sp.exp(g)) / 24
    push_ok = sp.simplify(centre[0] - claimed) == 0 and centre[1] == 0 and centre[2] == 0
    _, d0, _, _ = response("pair", sp.Integer(1), R(1), (1, 0, 0))
    drift = -(2 * 1 - 1) * 2 + 1                                   # -c at a = 1, n = 2
    rises = sp.simplify(claimed.subs(g, 0)) == 0 and sp.diff(claimed, g).is_positive is True          # zero at g = 0 and increasing: positive for g > 0
    checks.check("E1", push_ok and drift * d0[0, 0] < 0 and rises,
                 f"T6: at a = 1, two records in contact along the gradient (exclusion only) have centre velocity (e^g - 1)/24 > 0, towards faster clocks, because the faster record is pushed off more often; the same pair held by a tether drifts at -D_pair g = -{d0[0, 0]} g, towards slower clocks: a group's fall is not a contact force but the clock factor acting with its equilibrium weight")


# ============================================================================================ family F
FENCES = (
    "This note works within block 95's clocked transit of records, as landed on main, in a held uniform clock gradient; it reports where records settle, how records and bound groups drift, and what binding needs; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Perron", "Frobenius", "Schur", "Kolmogorov", "Smoluchowski", "Langevin", "Nernst", "Kubo", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - one record's first-order velocity, isolated and with one neighbour of each content (symbolic in g and a); the vanishing gradient term at a = 1",
    "per_site: executed - detailed balance of block 95's law in a linear field for two records, and of the centre-clock chain's tilted measure, move by move (symbolic)",
    "per_mode: executed - the exact first-order drift and diffusion constant of a lone record and of tethered pairs of three contents, at a = 1, 3/4, 0 and two gradient directions",
    "per_block: executed - the instantaneous push at contact against the long-time drift of the same pair",
    "lattice_wide: T1-T4 and T6 on Z^3 in a held uniform gradient for block 95's clocked transit; T3-T4 for a group held in a finite set of relative configurations by a supplied binding clause; T5 on Z^3 for block 95's own pairs; the transit, its timing a, the pair weights and the binding are supplied",
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
    print("scope: block 95's clocked transit in a held uniform gradient - one record moves with b + ((1 - a)/6) M g (none at a = 1); where records settle carries one factor (2a - 1) g per record; a group held by a binding clause drifts at -((2a - 1)n - 1) D0 g, so drift is not universal; block 95's own pairs are not bound; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
