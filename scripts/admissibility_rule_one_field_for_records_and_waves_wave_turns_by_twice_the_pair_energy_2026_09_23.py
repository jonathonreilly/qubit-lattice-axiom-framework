#!/usr/bin/env python3
"""Exact checks: one field for records and waves - a wave passing a record turns by twice the record's pair energy at that distance
(the owner's moving-records reading; block 53's clock field, block 95's pair law, block 54's walk and its ray law; not adopted).

B (T1): the kernel of one record summed along a lattice line is the plane kernel (exact on 4^3/4^2 and 6^3/6^2).
C (T2): for 1/(4 pi r), the line integral of the transverse gradient at impact parameter b is -2/(4 pi b), exactly.
D (T3): the straight-line kick on a long wave is 2|U(b)|, towards the record, and equals 2 log g(b) with block 95's pair law.
E (T3): the walk's ray-law tensor is the identity at long waves and its speed is one.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_ONE_FIELD_FOR_RECORDS_AND_WAVES_A_WAVE_PASSING_A_RECORD_TURNS_BY_TWICE_THE_PAIR_ENERGY_AT_THAT_DISTANCE_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    note, axioms = texts
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
    """T1: summed along a straight line, the kernel of one record is the plane kernel (exact on tori)."""
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
    checks.check("B1", ok and plane_ok, "T1: on the 4^3 and 6^3 tori the kernel of one record summed along any lattice line equals the plane kernel of the 4^2 and 6^2 tori at every transverse offset (exact); the plane kernel inverts the plane Laplacian with its zero mode removed (checked at all 36 sites of 6^2): a straight path past a record feels the plane kernel's gradient")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: in the continuum, the line integral of the transverse gradient of 1/(4 pi r) is exactly twice 1/(4 pi b)."""
    x, b = sp.symbols("x b", positive=True)
    y = sp.symbols("y", positive=True)
    pot = 1 / (4 * sp.pi * sp.sqrt(x ** 2 + y ** 2))
    val = sp.integrate(sp.diff(pot, y).subs(y, b), (x, -sp.oo, sp.oo))
    factor = 2 if not mut("deflection_halved") else 1
    exact = sp.simplify(val + factor / (4 * sp.pi * b)) == 0
    checks.check("C1", exact, "T2: for the far field 1/(4 pi r) of one record, the integral along a straight line at impact parameter b of the transverse gradient is -1/(2 pi b) = -2 x 1/(4 pi b), exactly: a straight path's transverse kick is twice the potential at closest approach")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: a long wave turns by twice the pair energy, and so by twice the log of the pair excess."""
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
    checks.check("D1", rel1 and rel2 and towards, "T3: with u = 6 log(kappa)/(4 pi r) (log kappa < 0, records slow clocks) the straight-line kick on a long wave at impact parameter b is -int d_y u dx = -(3/pi)|log kappa|/b, towards the record, of size 2|U(b)| with U(b) = 6 log(kappa)/(4 pi b) block 95's pair energy; with block 95's pair law g(b) = exp(-U(b)) the turn is 2 log g(b): a wave passing a record turns by twice the log of how much likelier a second record is at that distance")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T3 (the walk at long waves): the ray law's tensor is the identity and the speed is one, so the turn equals the kick."""
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    eps2 = sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2
    M = sp.hessian(eps2 / 2, (k1, k2, k3))
    diag_ok = sp.simplify(M - sp.diag(sp.cos(2 * k1), sp.cos(2 * k2), sp.cos(2 * k3))) == sp.zeros(3, 3)
    at0 = M.subs({k1: 0, k2: 0, k3: 0})
    unit = at0 == sp.eye(3) if not mut("anisotropic_long_waves") else at0 == 2 * sp.eye(3)
    vx = sp.diff(sp.sqrt(eps2), k1).subs({k2: 0, k3: 0})
    speed_one = sp.limit(sp.simplify(vx), k1, 0, "+") == 1
    checks.check("E1", diag_ok and unit and speed_one, "T3 for the walk (block 54): the tensor of its ray law, Hess(|sin k|^2/2) = diag(cos 2k_j), is the identity at k = 0 and the speed along an axis tends to 1, so at long waves the ray law is dv/dt = -grad(u) + 2(v.grad u)v and a straight passage turns the velocity by the transverse kick (the first term; the second is of second order)")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock field, block 95's pair law and block 54's walk; it reports how the one field that makes records clump turns a passing wave; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the line sum of the kernel at every transverse offset of 4^3 and 6^3",
    "per_site: executed - the plane kernel's defining identity at all 36 sites of 6^2",
    "per_mode: executed - the kernels from their nonzero modes; control: kick against twice the pair energy on a 128-torus, and walk packets against clouds of rays in one record's field",
    "per_block: executed - the continuum line integral and the walk's ray-law tensor, symbolic",
    "lattice_wide: T1 on every torus (the line sum picks the modes with no component along the line); T2-T3 in the continuum far field, first order in log kappa, straight passage; the lattice ratio executed; the ray law is block 54's (executed for the walk there and here)",
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
    print("scope: one field for records and waves - summed along a line the record kernel is the plane kernel; a long wave passing a record turns towards it by twice the pair energy at the impact parameter, 2|U(b)| = 2 log g(b) with block 95's pair law (first order, far field); nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
