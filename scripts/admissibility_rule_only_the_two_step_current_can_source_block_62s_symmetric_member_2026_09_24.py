#!/usr/bin/env python3
"""Exact checks: only the two-step current can source block 62's symmetric member - no local placement of the frame's site
response, or of the one-step momentum current, keeps the member's divergence condition on every stationary state; the two-step
current obeys a transposed conservation law and a local averaging onto the bonds makes it exactly compatible (a harvest block
recovering statements deferred when blocks 62-65 landed, from a Grok-refereed probes attempt; blocks 62-64 and 73 as landed
supplied; not adopted).

B (T1): reflection states (exact at 125 sites) and the spans of their q-parts (determinants symbolic in cos theta).
C (T2): the site response - the no-transfer argument and an exact witness.
D (T3): the one-step current - conservation, the no-realisation argument and an exact witness.
E (T4): the two-step current - the transposed law on an exact superposition, and the compatible realisation.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_no_local_placement_of_the_frame_response_or_of_the_one_step_current_keeps_its_divergence_condition_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "site_response_forged": "B",
    "transfer_pairing_forged": "C",
    "current_not_conserved": "D",
    "phi_realisation_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities (the coin); Admissibility is not a dynamics axiom and does not define a time metric (the walk, its currents and the lengths member are supplied clauses)")


# ============================================================================================ the walk and its currents
CZ, C1, CI = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))


def dec(q, n=6):
    """a truncated decimal string of a rational, by integer arithmetic."""
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole = q.numerator // q.denominator
    frac = ((q - whole) * 10 ** n).numerator // ((q - whole) * 10 ** n).denominator
    return f"{sign}{whole}.{str(frac).zfill(n)}"


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cconj(a):
    return (a[0], -a[1])


def cpow(u, n):
    """u^n for a unit Gaussian rational u (so u^-1 = conj u)."""
    if n < 0:
        u, n = cconj(u), -n
    out = C1
    for _ in range(n):
        out = cmul(out, u)
    return out


PAULI = (None, ((CZ, C1), (C1, CZ)), ((CZ, (Fr(0), Fr(-1))), (CI, CZ)), ((C1, CZ), (CZ, (Fr(-1), Fr(0)))))


def mvec(mat, v):
    return (cadd(cmul(mat[0][0], v[0]), cmul(mat[0][1], v[1])), cadd(cmul(mat[1][0], v[0]), cmul(mat[1][1], v[1])))


def inner(u, v):
    return cadd(cmul(cconj(u[0]), v[0]), cmul(cconj(u[1]), v[1]))


def vadd(u, v):
    return (cadd(u[0], v[0]), cadd(u[1], v[1]))


def vscale(c, v):
    return (cmul(c, v[0]), cmul(c, v[1]))


def unit(a, k=1):
    return tuple(k if i == a else 0 for i in range(3))


def plus(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


class Wave:
    """a finite superposition of plane waves: sum_n c_n chi_n e^(i k_n . x), each k_n given by the unit numbers u_a = e^(i k_a)."""

    def __init__(self, parts):
        self.parts = parts
        self.memo = {}

    def __call__(self, x):
        if x not in self.memo:
            out = (CZ, CZ)
            for c, chi, u in self.parts:
                ph = cmul(cmul(cpow(u[0], x[0]), cpow(u[1], x[1])), cpow(u[2], x[2]))
                out = vadd(out, vscale(cmul(c, ph), chi))
            self.memo[x] = out
        return self.memo[x]


def s_op(psi, j, x):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    return vscale((Fr(0), Fr(-1, 2)), vadd(psi(plus(x, unit(j))), vscale((Fr(-1), Fr(0)), psi(plus(x, unit(j, -1))))))


def p_op(psi, j, x):
    """(P_j psi)(x) = (S_j C_j psi)(x) = (psi(x + 2e_j) - psi(x - 2e_j))/(4i), block 73's two-step momentum."""
    return vscale((Fr(0), Fr(-1, 4)), vadd(psi(plus(x, unit(j, 2))), vscale((Fr(-1), Fr(0)), psi(plus(x, unit(j, -2))))))


def h_psi(psi, x):
    out = (CZ, CZ)
    for a in range(3):
        out = vadd(out, mvec(PAULI[a + 1], s_op(psi, a, x)))
    return out


def site_response(psi, a, j, x):
    """block 62's frame response Theta_a^j(x) = Re psi^dag sigma_a (S_j psi)."""
    return inner(psi(x), mvec(PAULI[a + 1], s_op(psi, j, x)))[0]


def bond_current(psi, op, a, j, x):
    """the bond current on x -> x + e_a: (1/2) Re[psi(x+e_a)^dag sigma_a (op_j psi)(x) + (op_j psi)(x+e_a)^dag sigma_a psi(x)]."""
    y = plus(x, unit(a))
    return (inner(psi(y), mvec(PAULI[a + 1], op(psi, j, x)))[0] + inner(op(psi, j, y), mvec(PAULI[a + 1], psi(x)))[0]) / 2


def eigvec(s, energy):
    v = ((s[0], -s[1]), (energy - s[2], Fr(0)))
    if v == (CZ, CZ):
        v = ((energy + s[2], Fr(0)), (s[0], s[1]))
    return v


COS_TH, SIN_TH = Fr(4, 5), Fr(3, 5)


def reflection_state(k2, k3):
    """psi = chi (e^(ik.x) + e^(ik'.x)), k = (pi/2 + theta, k2, k3), k' = (pi/2 - theta, k2, k3); k2, k3 given as (sin, cos)."""
    s = (COS_TH, k2[0], k3[0])
    e2 = s[0] ** 2 + s[1] ** 2 + s[2] ** 2
    energy = Fr(isqrt(e2.numerator), isqrt(e2.denominator))
    chi = eigvec(s, energy)
    u1p, u1m = cmul(CI, (COS_TH, SIN_TH)), cmul(CI, (COS_TH, -SIN_TH))
    u2, u3 = (k2[1], k2[0]), (k3[1], k3[0])
    return Wave([(C1, chi, (u1p, u2, u3)), (C1, chi, (u1m, u2, u3))]), s, energy


def relabelling(xi):
    """block 62's member in site convention: (G xi)_ij(x) = -(d_i xi_j + d_j xi_i)(x), d_a f(x) = f(x + e_a) - f(x)."""
    def comp(j, x):
        return Fr(xi.get(x, (0, 0, 0))[j])

    def h(i, j, x):
        return -((comp(j, plus(x, unit(i))) - comp(j, x)) + (comp(i, plus(x, unit(j))) - comp(i, x)))
    return h


REFLECTION_STATES = (((Fr(3, 5), Fr(4, 5)), (Fr(0), Fr(1))), ((Fr(0), Fr(1)), (Fr(3, 5), Fr(4, 5))), ((Fr(0), Fr(1)), (Fr(0), Fr(1))))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the reflection states and their spans."""
    box = list(product(range(-2, 3), repeat=3))
    ok = True
    for k2, k3 in REFLECTION_STATES:
        psi, s, energy = reflection_state(k2, k3)
        cosk = (None, k2[1], k3[1])
        for x in box:
            p = psi(x)
            ok = ok and h_psi(psi, x) == vscale((energy, Fr(0)), p)
            rho = inner(p, p)[0]
            for a in range(3):
                for j in range(3):
                    want_t = s[a] * s[j] * rho / energy
                    if mut("site_response_forged") and a == j == 0:
                        want_t += Fr(1, 1000)
                    ok = ok and site_response(psi, a, j, x) == want_t
                    cur = bond_current(psi, s_op, a, j, x)
                    ok = ok and cur == (0 if a == 0 else s[a] * s[j] * cosk[a] * rho / energy)
    c = sp.symbols("c")
    rat = sp.Rational
    pts = [(rat(3, 5), rat(4, 5)), (rat(4, 5), rat(3, 5)), (rat(5, 13), rat(12, 13)), (rat(12, 13), rat(5, 13)), (rat(8, 17), rat(15, 17)), (rat(7, 25), rat(24, 25)),
           (rat(-3, 5), rat(4, 5)), (rat(3, 5), rat(-4, 5)), (0, 1)]
    samples = [(pts[0], pts[2]), (pts[1], pts[4]), (pts[3], pts[5]), (pts[6], pts[1]), (pts[7], pts[3]), (pts[2], pts[8])]
    rows_j, rows_t = [], []
    for (s2, c2), (s3, c3) in samples:
        sv, v = (c, s2, s3), (0, s2 * c2, s3 * c3)
        rows_j.append([v[a] * sv[j] for a in (1, 2) for j in range(3)])
        rows_t.append([sv[i] * sv[j] for i in range(3) for j in range(i, 3)])
    det_j, det_t = sp.factor(sp.Matrix(rows_j).det()), sp.factor(sp.Matrix(rows_t).det())
    ok_span = sp.simplify(det_j / c ** 2).is_nonzero and sp.simplify(det_t / c ** 4).is_nonzero and sp.degree(det_j, c) == 2 and sp.degree(det_t, c) == 4
    checks.check("B1", ok,
                 "T1(a): for three reflection states (cos theta = 4/5; s = (4/5, 3/5, 0), (4/5, 0, 3/5), (4/5, 0, 0)) at all 125 sites of [-2,2]^3: H psi = E psi, Theta_a^j = s_a s_j rho/E, J_1^j = 0 and J_a^j = s_a s_j cos k_a rho/E (a = 2, 3), exactly")
    checks.check("B2", ok_span,
                 f"T1(b): at q = (2 theta, 0, 0) the q-parts over six rational (k2, k3) samples span: the J-parts v (x) s have 6x6 determinant {det_j} and the Theta-parts s (x) s (in Sym(3)) {det_t}, nonzero for every cos theta != 0 - the J-parts fill the space where conserved currents at q live, the Theta-parts all of Sym(3)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: no local transfer of the site response keeps block 62's member compatible."""
    psi, s, energy = reflection_state(*REFLECTION_STATES[0])
    region = list(product(range(-3, 3), repeat=3))
    h = relabelling({(0, 0, 0): (1, 0, 0)})
    scale = Fr(-1, 2) if not mut("transfer_pairing_forged") else Fr(0)
    pair = sum((site_response(psi, a, j, x) * scale * h(a, j, x) for x in region for a in range(3) for j in range(3) if h(a, j, x) != 0), Fr(0))
    checks.check("C1", pair == Fr(-1152, 625),
                 f"T2: a transfer P with sym P(0) = -1/2 compatible on every stationary state would need sym(P(q) G(q) w) = 0 on the spans of T1 at every axis q, hence sym P(0) = 0 as q -> 0: a contradiction. Witness: the plain transfer eps = -h/2 on the first reflection state against the relabelling xi = e1 delta_0 pairs to {pair} (not 0)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: no local realisation of the S-current keeps the member compatible."""
    psi, s, energy = reflection_state(*REFLECTION_STATES[0])
    region = list(product(range(-3, 3), repeat=3))
    h = relabelling({(0, 0, 0): (0, 1, 0)})
    pair = sum((bond_current(psi, s_op, a, j, x) * Fr(-1, 2) * h(a, j, x) for x in region for a in range(3) for j in range(3) if h(a, j, x) != 0), Fr(0))
    eta = {(0, 0, 0): 1, (1, 0, 0): 2, (0, -1, 1): -3}
    conserved = all(sum((bond_current(psi, s_op, a, j, x) * (eta.get(plus(x, unit(a)), 0) - eta.get(x, 0)) for x in region for a in range(3)), Fr(0)) == 0 for j in range(3))
    if mut("current_not_conserved"):
        conserved = not conserved
    checks.check("D1", conserved and pair == Fr(-1728, 3125),
                 f"T3: the S-current J is conserved (sum_x J . d eta = 0 for every finitely supported eta, checked for one) but a realisation R with Lambda R(0) = 1 would need R(q) G(q) w in e_c (x) C^3 at every q = t e_c, so R(0) would annihilate every uniform shear: a contradiction. Witness: the plain realisation B = -h/2 on the first reflection state against xi = e2 delta_0 pairs to {pair} (not 0)")


# ============================================================================================ family E
SUPERPOSITION = (
    ((Fr(4, 5), Fr(3, 5)), (Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0))),
    ((Fr(1), Fr(0)), (Fr(4, 5), Fr(3, 5)), (Fr(3, 5), Fr(4, 5))),
    ((Fr(-3, 5), Fr(4, 5)), (Fr(1), Fr(0)), (Fr(4, 5), Fr(3, 5))),
    ((Fr(12, 13), Fr(5, 13)), (Fr(5, 13), Fr(12, 13)), (Fr(1), Fr(0))),
    ((Fr(1), Fr(0)), (Fr(-5, 13), Fr(12, 13)), (Fr(12, 13), Fr(5, 13))),
)
COEFS = ((Fr(1), Fr(2)), (Fr(-3), Fr(1)), (Fr(2), Fr(-1)), (Fr(1), Fr(1)), (Fr(-1), Fr(3)))


def family_e(checks: Checks) -> None:
    """T4: the two-step current - a transposed conservation law and an exactly compatible realisation."""
    parts = []
    for u, c in zip(SUPERPOSITION, COEFS):
        s = (u[0][1], u[1][1], u[2][1])
        parts.append((c, eigvec(s, Fr(1)), u))
    psi = Wave(parts)
    small = list(product(range(-1, 2), repeat=3))
    memo = {}

    def cur(op, a, j, x):
        key = (op is p_op, a, j, x)
        if key not in memo:
            memo[key] = bond_current(psi, op, a, j, x)
        return memo[key]

    def avg(f, l):
        return lambda x: (f(plus(x, unit(l))) + f(plus(x, unit(l, -1)))) / 2

    def transposed(op, a, x):
        tot = Fr(0)
        for j in range(3):
            o1, o2 = [l for l in range(3) if l != j]
            f = (lambda y, j=j: cur(op, a, j, plus(y, unit(j))) - cur(op, a, j, plus(y, unit(j, -1))))
            tot += avg(avg(f, o1), o2)(x)
        return tot
    stationary = all(h_psi(psi, x) == psi(x) for x in small)
    law_k = all(transposed(p_op, a, x) == 0 for a in range(3) for x in small)
    law_j_fails = sum(1 for a in range(3) for x in small if transposed(s_op, a, x) != 0)

    def phi_apply(f, j):
        o1, o2 = [l for l in range(3) if l != j]
        g = avg(avg(f, o1), o2)
        return lambda x: (g(x) + g(plus(x, unit(j, -1)))) / 2
    region = list(product(range(-4, 4), repeat=3))
    pairs_phi, pairs_plain = [], []
    for xi in ({(0, 0, 0): (1, -2, 3), (1, 0, -1): (2, 1, 0)}, {(0, 1, 0): (-1, 0, 2)}, {(0, 0, 0): (0, 0, 1), (-1, 1, 1): (3, -2, 1)}):
        h = relabelling(xi)
        tot_phi = tot_plain = Fr(0)
        for i in range(3):
            for j in range(3):
                hij = (lambda x, i=i, j=j: h(i, j, x))
                bphi = phi_apply(hij, j) if not mut("phi_realisation_forged") else hij
                for x in region:
                    b = bphi(x)
                    if b != 0:
                        tot_phi += cur(p_op, i, j, x) * Fr(-1, 2) * b
                    if hij(x) != 0:
                        tot_plain += cur(p_op, i, j, x) * Fr(-1, 2) * hij(x)
        pairs_phi.append(tot_phi)
        pairs_plain.append(tot_plain)
    checks.check("E1", stationary and law_k and law_j_fails == 81,
                 f"T4(a): on an exact energy-1 superposition of five plane waves with rational sines, sum_j prod_(l != j) C_l [K_a^j(x + e_j) - K_a^j(x - e_j)] = 0 at all 27 sites of [-1,1]^3 for each a (the two-step current's transposed law), while the same combination of the S-current is nonzero at {law_j_fails} of 81")
    checks.check("E2", all(v == 0 for v in pairs_phi) and all(v != 0 for v in pairs_plain),
                 f"T4(b): the realisation B_i^j = -(1/2) phi_j h_ij, phi_j = (1/2)(1 + T_j^-1) prod_(l != j) C_l, pairs the two-step current with every relabelling to exactly 0 (three random relabellings), while the plain B = -h/2 does not ({', '.join(dec(v, 4) for v in pairs_plain)})")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 63, 64 and 73 as landed on main, with the walk in the identity frame at uniform rates; it reports which placements of the walk's currents can source block 62's symmetric member without breaking its divergence condition; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Noether", "Lifshitz", "Bogoliubov", "Cauchy", "Killing", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - H psi = E psi and the closed forms of Theta and J for three reflection states, exactly",
    "per_site: executed - all 125 sites of [-2,2]^3 for the reflection states; all 27 sites of [-1,1]^3 for the transposed law",
    "per_mode: executed - the spans of the q-parts at q = (2 theta, 0, 0) as determinants symbolic in cos theta",
    "per_block: executed - the two witnesses (-1152/625, -1728/3125); conservation of J; the phi-realisation's zero pairing against three relabellings and the plain realisation's nonzero pairing",
    "lattice_wide: T1-T4 on every stationary state of Z^3 and of L^3 tori with 4 | L; the member's solvability at nonzero wave vector rests on block 62 T5 as landed; the q = 0 condition and strict normalisation of the two-step realisation are not treated; the clauses are supplied",
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
    print("scope: which placements of the walk currents can source block 62 symmetric member - no local transfer of the frame site response and no local realisation of the one-step current keeps its divergence condition on every stationary state; the two-step current obeys a transposed law and its phi-realisation is exactly compatible; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
