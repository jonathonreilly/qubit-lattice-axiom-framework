#!/usr/bin/env python3
"""Finite linked-operator covariance and rotation expansions; a stated four-parameter bond-symbol obstruction and a continuum linear curvature identity."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_THE_WALKS_LINKS_BUILT_FROM_THE_FRAME_CARRY_THE_LENGTHS_CURVATURE_ONLY_AT_PLAQUETTE_REACH_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_walks_links_built_from_the_frame_carry_the_lengths_curvature_only_at_plaquette_reach_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "link_transform_wrong_end": "B",
    "second_order_coefficient_altered": "C",
    "bond_reach_rule_claimed_blind": "D",
    "curvature_sign_flipped": "E",
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
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk, the frame and the links are supplied clauses)")


# ============================================================================================ helpers (ported from the probes worker w-jonathonsmac4f50-jd491)
import random

SIGM = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
ID2 = sp.eye(2)


def vs(v):
    return v[0] * SIGM[0] + v[1] * SIGM[1] + v[2] * SIGM[2]


def su2(q):
    return q[0] * ID2 - sp.I * vs(q[1:])


def cayley(v):
    n2 = sum((x * x for x in v), sp.Integer(0))
    return [(1 - n2) / (1 + n2)] + [2 * x / (1 + n2) for x in v]


def rot_of(U):
    R = sp.zeros(3, 3)
    for b in range(3):
        M = U * SIGM[b] * U.H
        for a in range(3):
            R[a, b] = sp.simplify(sp.expand((M * SIGM[a]).trace() / 2))
    return R


def eq0(M):
    return all(sp.simplify(sp.expand(x)) == 0 for x in M)


def build_H(L, Mf, Vf):
    """H on a ring of L sites along one axis: sum_x (1/2i)[psi_x^+ M V psi_(x+1) - h.c.]."""
    H = sp.zeros(2 * L, 2 * L)
    for x in range(L):
        y = (x + 1) % L
        B = Mf[x] * Vf[x] / (2 * sp.I)
        H[2 * x:2 * x + 2, 2 * y:2 * y + 2] += B
        H[2 * y:2 * y + 2, 2 * x:2 * x + 2] += B.H
    return H


RNG = random.Random(914)


def rq():
    return sp.Rational(RNG.randint(-4, 4), RNG.randint(1, 4))


def rU():
    return su2(cayley([rq(), rq(), rq()]))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    Ux, Uy, V0 = rU(), rU(), rU()
    M0 = vs(sp.Matrix([rq(), rq(), rq()]))
    cov1 = eq0((Ux * M0 * Ux.H) * (Ux * V0 * Uy.H) - Ux * (M0 * V0) * Uy.H)
    Lr = 3
    Us = [rU() for _ in range(Lr)]
    Ms = [vs(sp.Matrix([rq(), rq(), rq()])) for _ in range(Lr)]
    Vs_ = [rU() for _ in range(Lr)]
    Hr = build_H(Lr, Ms, Vs_)
    Ubig = sp.diag(*Us)
    link = (lambda x: Us[x] * Vs_[x] * Us[(x + 1) % Lr].H) if not mut("link_transform_wrong_end") else (lambda x: Us[x] * Vs_[x] * Us[x].H)
    Hr_t = build_H(Lr, [Us[x] * Ms[x] * Us[x].H for x in range(Lr)], [link(x) for x in range(Lr)])
    herm = eq0(Hr - Hr.H)
    cov = eq0(Hr_t - Ubig * Hr * Ubig.H)
    checks.check("B1", cov1 and herm and cov, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    Lr = 3
    Ur = [rU() for _ in range(Lr)]
    H0 = build_H(Lr, [SIGM[0]] * Lr, [ID2] * Lr)
    Hsite = build_H(Lr, [Ur[x] * SIGM[0] * Ur[x].H for x in range(Lr)], [Ur[x] * Ur[(x + 1) % Lr].H for x in range(Lr)])
    exact = eq0(Hsite - sp.diag(*Ur) * H0 * sp.diag(*Ur).H)
    t1 = sp.Matrix(sp.symbols("ta1:4", real=True))
    t2 = sp.Matrix(sp.symbols("tb1:4", real=True))
    ep = sp.symbols("epsilon", real=True)

    def U_series(th, order=3):
        X = -sp.I * ep * vs(th) / 2
        out, term = ID2, ID2
        for n in range(1, order + 1):
            term = term * X / n
            out = out + term
        return out.applyfunc(sp.expand)
    U1, U2 = U_series(t1), U_series(t2)
    first = True
    so = None
    for j in range(3):
        ej = sp.Matrix([1 if i == j else 0 for i in range(3)])
        Mb = (U1 * SIGM[j] * U2.H).applyfunc(sp.expand)
        c1 = Mb.applyfunc(lambda z: z.coeff(ep, 1))
        first = first and eq0(c1 - (vs(((t1 + t2) / 2).cross(ej)) + (sp.I / 2) * (t2[j] - t1[j]) * ID2))
        if j == 0:
            so = Mb.applyfunc(lambda z: z.coeff(ep, 2))
    twist = sp.simplify(sp.expand((SIGM[0] * (U1 * U2.H)).trace() / 2).coeff(ep, 1) - (sp.I / 2) * (t2[0] - t1[0])) == 0
    coef = sp.Rational(1, 8) if not mut("second_order_coefficient_altered") else sp.Rational(1, 4)
    so_claim = (-(t1.dot(t1) + t2.dot(t2)) * coef * SIGM[0] + (vs(t1) * SIGM[0] * vs(t2)) / 4)
    second = eq0(so - so_claim.applyfunc(sp.expand))
    Ef = [sp.Matrix(sp.symbols(f"E{w}1:4", real=True)) for w in ("x", "y")]
    Mb_frame = (U1 * vs(Ef[0]) * U2.H).applyfunc(sp.expand)
    scal = sp.simplify(sp.expand(Mb_frame.trace() / 2).coeff(ep, 1))
    naive = (sp.I / 2) * (t2.dot(Ef[1]) - t1.dot(Ef[0]))
    frame = sp.simplify(scal - (sp.I / 2) * Ef[0].dot(t2 - t1)) == 0 and sp.simplify(naive - scal - (sp.I / 2) * t2.dot(Ef[1] - Ef[0])) == 0
    checks.check("C1", exact and first and twist and second and frame, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    Uh = [rU() for _ in range(2)]
    Rh = [rot_of(u) for u in Uh]
    Sx = sp.Matrix(3, 3, lambda i, j: 0)
    for i in range(3):
        for j in range(i, 3):
            Sx[i, j] = Sx[j, i] = rq() + (3 if i == j else 0)
    f = rU()
    Ma = vs(Rh[0] * Sx[:, 0])
    basis = eq0(Ma * (Uh[0] * f * Uh[1].H) - Uh[0] * (vs(Sx[:, 0]) * f) * Uh[1].H)
    kv = sp.Matrix(sp.symbols("k1:4", real=True))
    xv = sp.Matrix(sp.symbols("x1:4"))
    kap = sp.symbols("kap1:5")
    E = [sp.Matrix([1 if i == a else 0 for i in range(3)]) for a in range(3)]

    def L_bond(a, s):
        ea = E[a]
        se = s * ea
        return kap[0] * ea.cross(se) + kap[1] * se + kap[2] * s.trace() * ea + kap[3] * ea.dot(se) * ea

    def omega_bond(a, s):
        return sp.I * kv[a] * L_bond(a, s)

    def hol(a, b, om):
        return sp.I * kv[a] * om(b) - sp.I * kv[b] * om(a)
    gauge = (sp.I / 2) * (kv * xv.T + xv * kv.T)
    eqs = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        for comp in hol(a, b, lambda c_: omega_bond(c_, gauge)):
            eqs += sp.Poly(sp.expand(comp), *kv, *xv).coeffs()
    sol = sp.solve(eqs, kap, dict=True)
    only_zero = sol == [{kap[0]: 0, kap[1]: 0, kap[2]: 0, kap[3]: 0}]
    if mut("bond_reach_rule_claimed_blind"):
        only_zero = all(sp.expand(e.subs({kap[0]: 1, kap[1]: 0, kap[2]: 0, kap[3]: 0})) == 0 for e in eqs)
    checks.check("D1", basis and only_zero, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    kv = sp.Matrix(sp.symbols("k1:4", real=True))
    xv = sp.Matrix(sp.symbols("x1:4"))
    Ssym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"s{min(i, j)}{max(i, j)}"))
    E = [sp.Matrix([1 if i == a else 0 for i in range(3)]) for a in range(3)]

    def omega_tf(a, s):
        return -(sp.I * kv).cross(s * E[a])

    def hol(a, b, om):
        return sp.I * kv[a] * om(b) - sp.I * kv[b] * om(a)
    gauge = (sp.I / 2) * (kv * xv.T + xv * kv.T)
    blind = all(sp.simplify(x) == 0 for a, b in ((0, 1), (0, 2), (1, 2)) for x in hol(a, b, lambda c_: omega_tf(c_, gauge)))
    H01 = [sp.expand(x) for x in hol(0, 1, lambda c_: omega_tf(c_, Ssym))]
    sgn = 1 if not mut("curvature_sign_flipped") else -1
    Riem = sgn * sp.expand(kv[0] ** 2 * Ssym[1, 1] - 2 * kv[0] * kv[1] * Ssym[0, 1] + kv[1] ** 2 * Ssym[0, 0])
    # the linearized Riemann component R_0101 of g = 1 + 2s, from its definition, in long-wavelength symbols (d -> i k)
    h = 2 * Ssym
    d = lambda i: sp.I * kv[i]
    R0101 = sp.Rational(1, 2) * (d(1) * d(0) * h[0, 1] + d(0) * d(1) * h[1, 0] - d(0) * d(0) * h[1, 1] - d(1) * d(1) * h[0, 0])
    riem_def = sp.simplify(sp.expand(R0101) - sp.expand(kv[0] ** 2 * Ssym[1, 1] - 2 * kv[0] * kv[1] * Ssym[0, 1] + kv[1] ** 2 * Ssym[0, 0])) == 0
    curv = sp.simplify(H01[2] - Riem) == 0 and any(x != 0 for x in H01)
    F = lambda a, b_, d_: sp.I * kv[b_] * Ssym[d_, a] - sp.I * kv[d_] * Ssym[b_, a]
    curls = all(sp.simplify(omega_tf(a, Ssym)[c_] + sum((sp.LeviCivita(c_, b_, d_) * F(a, b_, d_) for b_ in range(3) for d_ in range(3)), sp.Integer(0)) / 2) == 0
                for a in range(3) for c_ in range(3))
    checks.check("E1", blind and curv and riem_def and curls, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    k=sp.Matrix([1,1,0]); x=sp.Matrix([0,0,1])
    s=sp.I*(k*x.T+x*k.T)/2
    om=[-sp.I*k.cross(s[:,a]) for a in range(3)]
    checks.check("E9", any(v!=sp.zeros(3,1) for v in om) and all(sp.simplify(sp.I*k[a]*om[b]-sp.I*k[b]*om[a])==sp.zeros(3,1) for a,b in ((0,1),(0,2),(1,2))), 'Scoped exact check E9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Finite linked-operator covariance and rotation expansions; a stated four-parameter bond-symbol obstruction and a continuum linear curvature identity.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
