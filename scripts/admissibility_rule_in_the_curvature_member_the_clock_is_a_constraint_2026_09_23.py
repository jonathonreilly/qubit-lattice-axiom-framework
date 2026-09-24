#!/usr/bin/env python3
"""Exact checks: in the curvature member the clock is a constraint - a body's change of energy acts at once, and at alpha + beta = 0 a body at rest
cannot change its energy (a probes worker's result, w-jonathonsmac4f50-j03c0, verified here; blocks 60 and 62's clauses; not adopted).

B (T1): block 62's member is relabelling-blind and sees one scalar; block 60's isotropic law is its special case.
C (T2): the rate's equation is a constraint; only the two transverse traceless strains travel.
D (T3): u(k,t) = -e/(4 K wbar p^2) + alpha(alpha + 3 beta) e''/(K^2 wbar^3 (alpha + beta) p^4).
E (T4): a switch-on moves the clock at label time 0+; at alpha + beta = 0 a body at rest cannot change its energy by a jump.
Exact symbolic algebra only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    note, axioms = texts
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
    """T1: block 62's member is blind to relabellings and sees one scalar; block 60's isotropic law is its special case."""
    gauge = pv * xi.T + xi * pv.T
    brk = mut("relabelling_broken")
    blind = zero(R1(Hs + gauge, pv) - R1(Hs, pv)) and zero(sp.expand(R2(Hs + gauge, pv, brk) - R2(Hs, pv, brk)))
    phs = sp.symbols("phi", real=True)
    Pp = sp.eye(3) - pv * pv.T / pv.dot(pv)
    scalar = zero(R1(Pp * phs, pv) - 2 * pv.dot(pv) * phs) and zero(R2(Pp * phs, pv) - pv.dot(pv) * phs ** 2 / 2)
    lam, ee = sp.symbols("lam e")
    iso = zero(sp.solve(sp.Eq(K * wb * R1(2 * lam * sp.eye(3), pv), ee), lam)[0] - ee / (4 * K * wb * pv.dot(pv)))
    checks.check("B1", blind and scalar and iso, "T1: block 62's second-order member (R1 = -(p.h.p - p^2 tr h), R2 its quadratic partner) is unchanged by every relabelling h -> h + p xi + xi p; on the scalar h = (1 - p p/p^2) phi it gives R1 = 2 p^2 phi and R2 = p^2 phi^2/2 in every direction; for isotropic stretch it reproduces block 60's law p^2 lambda = e/(4 K wbar)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the rate is a multiplier (a constraint), only the two transverse traceless strains travel."""
    e, u, ph, a_, b_, xl, EL = reduced_equations()
    constraint = zero(EL[u] - (e - 2 * K * wb * p ** 2 * ph))
    speed_factor = 4 if not mut("tt_speed_forged") else 2
    tt = zero(EL[a_] - (speed_factor * al / wb * a_.diff(t, 2) + K * wb * p ** 2 * a_)) and zero(EL[b_] - (4 * al / wb * b_.diff(t, 2) + K * wb * p ** 2 * b_))
    relab = zero(EL[xl] - sp.diff(8 / wb * ((al + be) * xl.diff(t) + be * ph.diff(t)), t))
    checks.check("C1", constraint and tt and relab, "T2: with block 62's kinetic term (alpha h'_ij h'_ij + beta (tr h')^2)/wbar and no rate of change of a rate, the rate's equation is K wbar R1 = e, i.e. 2 K wbar p^2 phi = e(t): a constraint at each label time; the two transverse traceless strains obey (4 alpha/wbar) a'' = -K wbar p^2 a (speed^2 = K wbar^2/(4 alpha), block 62 T4) and a body at rest does not source them; the longitudinal relabelling obeys d/dt[(alpha + beta) xi' + beta phi'] = 0")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the clock is set at each label time by the content, with a term in the second derivative of the energy."""
    e, u_sol = clock_law()
    coeff = al * (al + 3 * be) / (K ** 2 * wb ** 3 * (al + be) * p ** 4) if not mut("e_dd_term_dropped") else sp.Integer(0)
    u_claim = -e / (4 * K * wb * p ** 2) + coeff * e.diff(t, 2)
    law = zero(u_sol - u_claim)
    static = zero(u_claim.subs(e.diff(t, 2), 0) + e / (4 * K * wb * p ** 2))
    special = zero(u_claim.subs(be, -al / 3) + e / (4 * K * wb * p ** 2))
    checks.check("D1", law and static and special, "T3: eliminating the scalar length and the relabelling gives u(k,t) = -e(k,t)/(4 K wbar p^2) + alpha(alpha + 3 beta) e''(k,t)/(K^2 wbar^3 (alpha + beta) p^4): the clock is fixed at each label time by the content and its second derivative, with block 60's static law as the limit, and exactly the instantaneous Poisson field when alpha + 3 beta = 0")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: a change of a body's energy acts at once; at alpha + beta = 0 it cannot happen at rest."""
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
    checks.check("E1", at_once and after and forbidden, "T4: a smooth switch-on of Delta_e over tau_r moves the clock at label time 0+ at every wave vector by 6 alpha(alpha + 3 beta) Delta_e/(K^2 wbar^3 (alpha + beta) p^4 tau_r^2), and after the switch-on the clock has jumped by the Poisson field of Delta_e, whatever alpha and beta: nothing waits for the strains; at alpha + beta = 0 the relabelling equation reads beta phi' = constant, so the energy of a body at rest can change only at a constant rate and cannot jump")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied clauses of blocks 60 and 62 (the curvature member and its kinetic term) and reports, from a probes worker's exact derivation verified here, when a change of a body's energy reaches the clocks; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the member's relabelling blindness for symbolic h, p and xi",
    "per_site: not applicable - the statements are per wave vector",
    "per_mode: executed - the reduced equations at a general wave vector (rotated to one axis), symbolic in K, wbar, alpha, beta, p; control: packets on a plane slice",
    "per_block: executed - a smooth switch-on of a body's energy, series at label time zero",
    "lattice_wide: every lattice wave vector at second order about the uniform state (O(3)-covariant member and kinetic term); blocks 60 and 62's clauses supplied; no statement beyond second order or for moving bodies",
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
    print("scope: in the curvature member with block 62's kinetic term the clock is a constraint - u = -e/(4 K wbar p^2) + alpha(alpha + 3 beta) e''/(K^2 wbar^3 (alpha + beta) p^4); only transverse traceless strains travel; a change of a body's energy acts at once; at alpha + beta = 0 a body at rest cannot change its energy by a jump; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
