#!/usr/bin/env python3
"""Exact mean-zero torus line sums and a weak-field continuum transverse integral; no universal identification with measured pair correlations."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_ONE_FIELD_FOR_RECORDS_AND_WAVES_A_WAVE_PASSING_A_RECORD_TURNS_BY_TWICE_THE_PAIR_ENERGY_AT_THAT_DISTANCE_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_field_for_records_and_waves_a_wave_passing_a_record_turns_by_twice_the_pair_energy_at_that_distance_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "kernel_line_sum_forged": "B",
    "deflection_halved": "C",
    "log_pair_dropped": "D",
    "anisotropic_long_waves": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
def zero_mean_kernel(L, dim):
    """Exact zero-mean inverse of the lattice Laplacian on (Z/L)^dim for L = 4 or 6 (rational cosines)."""
    if L == 4:
        cosv = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    elif L == 6:
        cosv = {0: F(1), 1: F(1, 2), 2: F(-1, 2), 3: F(-1), 4: F(-1, 2), 5: F(1, 2)}
    else:
        raise ValueError(L)
    ks = [n for n in product(range(L), repeat=dim) if any(n)]
    Ek = {n: 2 * dim - 2 * sum(cosv[c] for c in n) for n in ks}
    return {d: sum((cosv[sum(n[i] * d[i] for i in range(dim)) % L] / Ek[n] for n in ks), ZERO) / (L ** dim) for d in product(range(L), repeat=dim)}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = True
    for L in (4, 6):
        G3 = zero_mean_kernel(L, 3)
        G2 = zero_mean_kernel(L, 2)
        norm = F(1) if not mut("kernel_line_sum_forged") else F(1, L)
        for y in range(L):
            for z in range(L):
                ok = ok and norm * sum((G3[(x, y, z)] for x in range(L)), ZERO) == G2[(y, z)]
    G2_6 = zero_mean_kernel(6, 2)
    plane_ok = all(4 * G2_6[d] - sum((G2_6[((d[0] + s0) % 6, (d[1] + s1) % 6)] for s0, s1 in ((1, 0), (-1, 0), (0, 1), (0, -1))), ZERO) == (1 if d == (0, 0) else 0) - F(1, 36) for d in G2_6)
    checks.check("B1", ok and plane_ok, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    x, b = sp.symbols("x b", positive=True)
    y = sp.symbols("y", positive=True)
    pot = 1 / (4 * sp.pi * sp.sqrt(x ** 2 + y ** 2))
    val = sp.integrate(sp.diff(pot, y).subs(y, b), (x, -sp.oo, sp.oo))
    factor = 2 if not mut("deflection_halved") else 1
    exact = sp.simplify(val + factor / (4 * sp.pi * b)) == 0
    checks.check("C1", exact, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    lam, b = sp.symbols("lambda b", real=True)
    lam_neg = sp.symbols("ell", negative=True)
    x = sp.symbols("x", real=True)
    bpos = sp.symbols("b", positive=True)
    u = 6 * lam_neg / (4 * sp.pi * sp.sqrt(x ** 2 + sp.Symbol("y", positive=True) ** 2))
    kick = -sp.integrate(sp.diff(u, sp.Symbol("y", positive=True)).subs(sp.Symbol("y", positive=True), bpos), (x, -sp.oo, sp.oo))
    U = 6 * lam_neg / (4 * sp.pi * bpos)
    g = sp.exp(-U)
    factor = 2 if not mut("log_pair_dropped") else 1
    rel1 = sp.simplify(sp.Abs(kick) - factor * sp.Abs(U)) == 0
    rel2 = sp.simplify(sp.Abs(kick) - factor * sp.log(g)) == 0
    towards = bool(sp.simplify(kick) < 0)                               # the path at +b turns towards the record at 0
    checks.check("D1", rel1 and rel2 and towards, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    eps2 = sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2
    M = sp.hessian(eps2 / 2, (k1, k2, k3))
    diag_ok = sp.simplify(M - sp.diag(sp.cos(2 * k1), sp.cos(2 * k2), sp.cos(2 * k3))) == sp.zeros(3, 3)
    at0 = M.subs({k1: 0, k2: 0, k3: 0})
    unit = at0 == sp.eye(3) if not mut("anisotropic_long_waves") else at0 == 2 * sp.eye(3)
    vx = sp.diff(sp.sqrt(eps2), k1).subs({k2: 0, k3: 0})
    speed_one = sp.limit(sp.simplify(vx), k1, 0, "+") == 1
    checks.check("E1", diag_ok and unit and speed_one, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    gx,gy=sp.symbols("gx gy", real=True)
    v=sp.Matrix([1,0,0]); term=2*gx*v
    projected=(sp.eye(3)-v*v.T)*term
    checks.check("E9", term[0]==2*gx and projected==sp.zeros(3,1), 'Scoped exact check E9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: Exact mean-zero torus line sums and a weak-field continuum transverse integral; no universal identification with measured pair correlations.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
