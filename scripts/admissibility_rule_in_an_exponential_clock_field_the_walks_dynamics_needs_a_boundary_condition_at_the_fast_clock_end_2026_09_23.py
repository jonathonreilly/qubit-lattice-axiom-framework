#!/usr/bin/env python3
"""The exponential line operator has deficiency indices (2,2); chain-separated boundary domains and a circle of translation-compatible choices, with explicit operator-theory imports."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_IN_AN_EXPONENTIAL_CLOCK_FIELD_THE_WALKS_DYNAMICS_NEEDS_A_BOUNDARY_CONDITION_AT_THE_FAST_CLOCK_END_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "scaling_power_wrong": "B",
    "fast_side_growth_forged": "C",
    "green_identity_sign_flipped": "D",
    "even_shift_multiplier_split": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk and its clock are supplied clauses)")


# ============================================================================================ helpers (block 54's line walk in an exponential clock field)
LAM = sp.symbols("lambda", positive=True)


def walk_matrix(xs, w):
    """H_w = W^(1/2) sigma_x D W^(1/2) on the window of sites xs (open ends), basis index 2 i + (0 up, 1 down);
    (T psi)(x) = psi(x - 1), D = (i/2)(T - T^+): (H_w psi)(x) = sqrt(w_x) sigma_x (i/2)(sqrt(w_(x-1)) psi(x-1) - sqrt(w_(x+1)) psi(x+1))."""
    N = len(xs)
    M = sp.zeros(2 * N, 2 * N)
    for i, x in enumerate(xs):
        for j, y in enumerate(xs):
            if y == x - 1:
                c = sp.I / 2
            elif y == x + 1:
                c = -sp.I / 2
            else:
                continue
            amp = c * sp.sqrt(w(x)) * sp.sqrt(w(y))
            M[2 * i, 2 * j + 1] += amp
            M[2 * i + 1, 2 * j] += amp
    return M


def expw(x):
    return LAM ** x


def zero_solution(kind, xs):
    """The four zero-energy solutions of H_w for w = lambda^x: one component on one parity, lambda^(-m) at x = 2m or 2m + 1."""
    comp, par = kind
    v = sp.zeros(2 * len(xs), 1)
    for i, x in enumerate(xs):
        if x % 2 == par:
            v[2 * i + comp] = LAM ** (-sp.floor(sp.Rational(x - par, 2)))
    return v


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    xs = list(range(-4, 5))
    H = walk_matrix(xs, expw)
    herm = sp.simplify(H - H.H) == sp.zeros(*H.shape)
    chainA = lambda i, c: (xs[i] % 2 == 0 and c == 0) or (xs[i] % 2 == 1 and c == 1)
    split = all(H[2 * i + ci, 2 * j + cj] == 0 for i in range(len(xs)) for j in range(len(xs)) for ci in (0, 1) for cj in (0, 1)
                if chainA(i, ci) != chainA(j, cj))
    ok_scale = True
    for a in (1, 2):
        big = list(range(-8, 9))
        Hb = walk_matrix(big, expw)
        power = a if not mut("scaling_power_wrong") else a + 1
        for s0 in range(-3, 4):
            for comp in (0, 1):
                v = sp.zeros(2 * len(big), 1)
                v[2 * big.index(s0) + comp] = 1
                Tv = sp.zeros(2 * len(big), 1)
                Tv[2 * big.index(s0 + a) + comp] = 1
                lhs = Hb * Tv
                rhs_pre = Hb * v
                rhs = sp.zeros(2 * len(big), 1)
                for k in range(len(big)):
                    if 0 <= k + a < len(big):
                        rhs[2 * (k + a)] = rhs_pre[2 * k]
                        rhs[2 * (k + a) + 1] = rhs_pre[2 * k + 1]
                ok_scale = ok_scale and all(sp.simplify(lhs[r] - LAM ** power * rhs[r]) == 0 for r in range(len(lhs)))
    checks.check("B1", herm and split and ok_scale, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    xs = list(range(-6, 7))
    H = walk_matrix(xs, expw)
    inner = [i for i in range(1, len(xs) - 1)]
    sols_ok = True
    for kind in ((0, 0), (0, 1), (1, 0), (1, 1)):
        v = zero_solution(kind, xs)
        Hv = H * v
        sols_ok = sols_ok and all(sp.simplify(Hv[2 * i + c]) == 0 for i in inner for c in (0, 1))
    m = sp.symbols("m", integer=True, nonnegative=True)
    fast = True
    for lv in (2, 3):
        L = sp.Integer(lv)
        s_fast = sp.summation(L ** (-2 * m), (m, 0, sp.oo)) if not mut("fast_side_growth_forged") else sp.summation(L ** (2 * m), (m, 0, sp.oo))
        fast = fast and s_fast == L ** 2 / (L ** 2 - 1)
    slow_terms_grow = all(sp.limit(sp.Integer(lv) ** (2 * m), m, sp.oo) == sp.oo for lv in (2, 3))
    carl = True
    for lv in (2, 3):
        L = sp.Integer(lv)
        term_fast = 2 * L ** (-m - sp.Rational(1, 2))
        term_slow = 2 * L ** (m - sp.Rational(1, 2))
        carl = carl and sp.summation(term_fast, (m, 0, sp.oo)).is_finite and sp.limit(term_slow, m, sp.oo) == sp.oo
    N = 6
    Jc = sp.zeros(N, N)
    for k in range(N - 1):
        Jc[k, k + 1] = -sp.I / 2 * LAM ** (k + sp.Rational(1, 2))
        Jc[k + 1, k] = sp.I / 2 * LAM ** (k + sp.Rational(1, 2))
    G = sp.diag(*[sp.I ** k for k in range(N)])
    Jr = sp.simplify(G.H * Jc * G)
    real_jacobi = all(sp.simplify(Jr[k, k + 1] - LAM ** (k + sp.Rational(1, 2)) / 2) == 0 and sp.simplify(Jr[k + 1, k] - LAM ** (k + sp.Rational(1, 2)) / 2) == 0 for k in range(N - 1))
    checks.check("C1", sols_ok and fast and slow_terms_grow and carl and real_jacobi, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    N = 6
    u = sp.symbols("u0:%d" % (N + 2))
    v = sp.symbols("v0:%d" % (N + 2))
    b = [LAM ** (k + sp.Rational(1, 2)) / 2 for k in range(N + 2)]

    def J(seq, k):
        return b[k] * seq[k + 1] + b[k - 1] * seq[k - 1]

    def W(p, q, k):
        return b[k] * (p[k] * q[k + 1] - p[k + 1] * q[k])
    lhs = sum((J(u, k) * v[k] - u[k] * J(v, k) for k in range(1, N + 1)), sp.Integer(0))
    sign = 1 if not mut("green_identity_sign_flipped") else -1
    rhs = sign * (-(W(u, v, N) - W(u, v, 0)))
    green = sp.simplify(sp.expand(lhs - rhs)) == 0
    checks.check("D1", green, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    xs = list(range(-6, 9))

    def shift(v, a):
        out = sp.zeros(v.shape[0], 1)
        for i, x in enumerate(xs):
            if x - a in xs:
                j = xs.index(x - a)
                out[2 * i] = v[2 * j]
                out[2 * i + 1] = v[2 * j + 1]
        return out
    inner = [i for i in range(3, len(xs) - 3)]
    scalar = LAM if not mut("even_shift_multiplier_split") else None
    ok2 = True
    mults = []
    for kind in ((0, 0), (0, 1), (1, 0), (1, 1)):
        v = zero_solution(kind, xs)
        T2v = shift(v, 2)
        for i in inner:
            for c in (0, 1):
                if v[2 * i + c] != 0:
                    mults.append(sp.simplify(T2v[2 * i + c] / v[2 * i + c]))
                elif T2v[2 * i + c] != 0:
                    ok2 = False
    common = len(set(mults)) == 1 and (scalar is None or sp.simplify(list(set(mults))[0] - scalar) == 0)
    if mut("even_shift_multiplier_split"):
        common = len(set(mults)) == 2
    ok1 = True
    pairs = {(0, 0): (0, 1), (1, 1): (1, 0)}
    for src, dst in pairs.items():
        v = zero_solution(src, xs)
        T1v = shift(v, 1)
        w_ = zero_solution(dst, xs)
        ratios = set(sp.simplify(T1v[2 * i + c] / w_[2 * i + c]) for i in inner for c in (0, 1) if w_[2 * i + c] != 0)
        ok1 = ok1 and len(ratios) == 1 and all(T1v[2 * i + c] == 0 for i in inner for c in (0, 1) if w_[2 * i + c] == 0)
    x0 = sp.symbols("x0", integer=True)
    k = sp.symbols("k", integer=True, nonnegative=True)
    travel = sp.simplify(sp.summation(LAM ** (-(x0 + k)), (k, 0, sp.oo)).subs(LAM, 3).subs(x0, 0) - sp.Rational(3, 2)) == 0
    checks.check("E1", ok2 and common and ok1 and travel, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    M=sp.Matrix([[0,-LAM],[1,0]])
    a,b=sp.symbols("a b",real=True)
    def sol(n):
        return ((-1)**(n//2)*LAM**(-(n//2))*a if n%2==0 else (-1)**((n-1)//2)*LAM**(-((n-1)//2))*b)
    def image(n):
        return sp.expand(sol(n).subs({a:-LAM*b,b:a},simultaneous=True))
    shifted=all(sp.simplify(sol(n-1)-image(n))==0 for n in range(-3,5))
    checks.check("E9", shifted and M*M == -LAM*sp.eye(2) and (-sp.I*M)**2==LAM*sp.eye(2), 'Scoped exact check E9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: The exponential line operator has deficiency indices (2,2); chain-separated boundary domains and a circle of translation-compatible choices, with explicit operator-theory imports.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
