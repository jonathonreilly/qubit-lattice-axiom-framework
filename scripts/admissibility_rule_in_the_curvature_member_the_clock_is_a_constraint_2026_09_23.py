#!/usr/bin/env python3
"""For an explicit nonzero-mode quadratic action: scalar constraint, two TT frequencies, clock elimination away from a singular kinetic ratio and scoped source-ramp identities."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "relabelling_broken": "B",
    "tt_speed_forged": "C",
    "e_dd_term_dropped": "D",
    "dewitt_ratio_misplaced": "E",
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


# ============================================================================================ helpers (block 62's member and kinetic term)
K, wb, al, be, p = sp.symbols("K wbar alpha beta p", positive=True)
t = sp.symbols("t", real=True)
pv = sp.Matrix(sp.symbols("p1:4", real=True))
Hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j)}{max(i, j)}", real=True))
xi = sp.Matrix(sp.symbols("xi1:4", real=True))


def zero(e):
    return sp.simplify(e) == 0


def R1(h, pp):
    return -((pp.T * h * pp)[0] - pp.dot(pp) * h.trace())


def R2(h, pp, broken=False):
    ph = h * pp
    extra = sp.Integer(0) if not broken else sp.Rational(1, 7) * h[0, 0] * pp.dot(pp)
    return (-sp.Rational(1, 4) * pp.dot(pp) * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
            + sp.Rational(1, 2) * ph.dot(ph) - sp.Rational(1, 2) * (pp.T * h * pp)[0] * h.trace()
            + sp.Rational(1, 4) * pp.dot(pp) * h.trace() ** 2 + extra)


def reduced_equations():
    """Euler-Lagrange expressions at one wave vector along z: L = kinetic + K wbar (u R1 + R2) - e u."""
    e = sp.Function("e")(t)
    u = sp.Function("u")(t)
    ph = sp.Function("phi")(t)
    a_ = sp.Function("a")(t)
    b_ = sp.Function("b")(t)
    xl = sp.Function("xiL")(t)
    cx = sp.Function("cx")(t)
    cy = sp.Function("cy")(t)
    hz = sp.Matrix([[ph + a_, b_, cx], [b_, ph - a_, cy], [cx, cy, 2 * xl]])
    pz = sp.Matrix([0, 0, p])
    hd = hz.diff(t)
    Tkin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
    Lag = Tkin + K * wb * (u * R1(hz, pz) + R2(hz, pz)) - e * u
    EL = {f: sp.expand(sp.diff(sp.diff(Lag, f.diff(t)), t) - sp.diff(Lag, f)) for f in (u, ph, a_, b_, xl)}
    return e, u, ph, a_, b_, xl, EL


def clock_law():
    e, u, ph, a_, b_, xl, EL = reduced_equations()
    phi_sol = e / (2 * K * wb * p ** 2)
    xl_dot = -be * phi_sol.diff(t) / (al + be)
    EPh = EL[ph].subs({xl.diff(t, 2): xl_dot.diff(t), xl.diff(t): xl_dot}).subs(ph, phi_sol).doit()
    return e, sp.solve(sp.Eq(EPh, 0), u)[0]


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    gauge = pv * xi.T + xi * pv.T
    brk = mut("relabelling_broken")
    blind = zero(R1(Hs + gauge, pv) - R1(Hs, pv)) and zero(sp.expand(R2(Hs + gauge, pv, brk) - R2(Hs, pv, brk)))
    phs = sp.symbols("phi", real=True)
    Pp = sp.eye(3) - pv * pv.T / pv.dot(pv)
    scalar = zero(R1(Pp * phs, pv) - 2 * pv.dot(pv) * phs) and zero(R2(Pp * phs, pv) - pv.dot(pv) * phs ** 2 / 2)
    lam, ee = sp.symbols("lam e")
    iso = zero(sp.solve(sp.Eq(K * wb * R1(2 * lam * sp.eye(3), pv), ee), lam)[0] - ee / (4 * K * wb * pv.dot(pv)))
    checks.check("B1", blind and scalar and iso, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    e, u, ph, a_, b_, xl, EL = reduced_equations()
    constraint = zero(EL[u] - (e - 2 * K * wb * p ** 2 * ph))
    speed_factor = 4 if not mut("tt_speed_forged") else 2
    tt = zero(EL[a_] - (speed_factor * al / wb * a_.diff(t, 2) + K * wb * p ** 2 * a_)) and zero(EL[b_] - (4 * al / wb * b_.diff(t, 2) + K * wb * p ** 2 * b_))
    relab = zero(EL[xl] - sp.diff(8 / wb * ((al + be) * xl.diff(t) + be * ph.diff(t)), t))
    checks.check("C1", constraint and tt and relab, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    e, u_sol = clock_law()
    coeff = al * (al + 3 * be) / (K ** 2 * wb ** 3 * (al + be) * p ** 4) if not mut("e_dd_term_dropped") else sp.Integer(0)
    u_claim = -e / (4 * K * wb * p ** 2) + coeff * e.diff(t, 2)
    law = zero(u_sol - u_claim)
    static = zero(u_claim.subs(e.diff(t, 2), 0) + e / (4 * K * wb * p ** 2))
    special = zero(u_claim.subs(be, -al / 3) + e / (4 * K * wb * p ** 2))
    checks.check("D1", law and static and special, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    e, u_sol = clock_law()
    u_claim = -e / (4 * K * wb * p ** 2) + al * (al + 3 * be) * e.diff(t, 2) / (K ** 2 * wb ** 3 * (al + be) * p ** 4)
    tau_r = sp.symbols("tau_r", positive=True)
    De = sp.symbols("Delta_e", real=True)
    s = t / tau_r
    ramp = De * (3 * s ** 2 - 2 * s ** 3)
    du0 = u_claim.subs(e, ramp).doit()
    early = sp.series(du0, t, 0, 2).removeO()
    at_once = zero(early.subs(t, 0) - 6 * al * (al + 3 * be) * De / (K ** 2 * wb ** 3 * (al + be) * p ** 4 * tau_r ** 2))
    after = zero(u_claim.subs(e, De).doit() + De / (4 * K * wb * p ** 2))
    phi_sol = e / (2 * K * wb * p ** 2)
    ratio = -al if not mut("dewitt_ratio_misplaced") else al
    xld = sp.Symbol("xLd")
    forbidden = zero(((al + be) * xld + be * phi_sol.diff(t)).subs(be, ratio) + al * e.diff(t) / (2 * K * wb * p ** 2))
    checks.check("E1", at_once and after and forbidden, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    p,K,w,a=sp.symbols("p K w a",positive=True)
    b=sp.symbols("b",real=True)
    coeff=a*(a+3*b)/(K**2*w**3*(a+b)*p**4)
    s=sp.symbols("s",real=True)
    ramp=10*s**3-15*s**4+6*s**5
    checks.check("E9", sp.diff(ramp,s,2).subs(s,0)==0 and sp.simplify(coeff.subs(b,-a/3))==0, 'Scoped exact check E9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: For an explicit nonzero-mode quadratic action: scalar constraint, two TT frequencies, clock elimination away from a singular kinetic ratio and scoped source-ramp identities.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
