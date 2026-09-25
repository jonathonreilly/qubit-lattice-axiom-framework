#!/usr/bin/env python3
"""Exact checks: exact books need records that never scatter or bind, and nothing local keeps them under one record per site - for two records of block 54's walk with any finite-range
interaction (on block 78's one-record-per-site space or the full space), the total two-step momentum at total wave vector K is
g_a = sin K_a cos 2q_a and varies along the collision shells in the plane and in space (nonzero shell derivative at a
Pythagorean point for all four band pairs); a one-body placement adds nothing within a band; on the line every shell is two
points with one value of g; one record per site removes one coincident state (antisymmetric) or three (symmetric), which
couple to the continuum; the perturbation determinant vanishes at a removed state. These are the exact inputs of the note's
theorems that a kept energy current makes the pair transparent and that a transparent pair removes and binds nothing (the supervisor's own derivation; blocks 54 and 78 as landed; blocks 136, 137 and 140 placed; not adopted).

B (T1): the collision shells.
C (T2): placements within a band.
D (T4): the line's shells.
E (T4, T5): the removed coincident states; the determinant at a removed state.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_NOTHING_LOCAL_KEEPS_THEM_UNDER_ONE_RECORD_PER_SITE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "shell_point_forged": "B",
    "placement_band_diagonal_forged": "C",
    "line_shell_forged": "D",
    "removed_count_forged": "E",
    "determinant_zero_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, one record per site, the interaction and the placements are supplied; the memo does not define a time metric)")
# ============================================================================================ two records at total wave vector K: kinematics of the collision shells
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)
# Pythagorean angles: (sin, cos) rational
PYTH = ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(20, 29), Fr(21, 29)), (Fr(8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25)), (Fr(9, 41), Fr(40, 41)))


def s_add(a, b):
    return a[0] * b[1] + a[1] * b[0]


def s_sub(a, b):
    return a[0] * b[1] - a[1] * b[0]


def minor_is_nonzero(dim, rec1, rec2):
    """dg_1 ^ dE on the (q_1, q_2) plane at k1 = K/2 + q = rec1, k2 = K/2 - q = rec2 (angles given by rational (sin, cos)):
    g_1 = sin K_1 cos 2q_1 gives dg_1/dq_1 = -2 sin(K_1) sin(2 q_1) = -2 sin(a_1 + b_1) sin(a_1 - b_1); dE/dq_2 =
    s1 sin(2 a_2)/(2 eps(k1)) - s2 sin(2 b_2)/(2 eps(k2)), nonzero for every band pair when the squares of its two terms differ."""
    a, b = rec1[:dim], rec2[:dim]
    dg = -2 * s_add(a[0], b[0]) * s_sub(a[0], b[0])
    e1 = sum(x[0] ** 2 for x in a)
    e2 = sum(x[0] ** 2 for x in b)
    s2a = 2 * a[1][0] * a[1][1]
    s2b = 2 * b[1][0] * b[1][1]
    squares_differ = s2a ** 2 * e2 != s2b ** 2 * e1
    return dg != 0 and e1 != 0 and e2 != 0 and squares_differ, dg, (s2a ** 2 * e2, s2b ** 2 * e1)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the total two-step momentum varies along the collision shells in the plane and in space."""
    ok_form = True
    for dim in (2, 3):
        K = sp.symbols("K1:%d" % (dim + 1), real=True)
        q = sp.symbols("q1:%d" % (dim + 1), real=True)
        for a in range(dim):
            ga = (sp.sin(2 * (K[a] / 2 + q[a])) + sp.sin(2 * (K[a] / 2 - q[a]))) / 2
            ok_form = ok_form and sp.simplify(sp.expand_trig(ga - sp.sin(K[a]) * sp.cos(2 * q[a]))) == 0
    rec1 = (PYTH[0], PYTH[1], PYTH[2])
    rec2 = (PYTH[3], PYTH[4], PYTH[5])
    if mut("shell_point_forged"):
        rec2 = rec1
    res = [minor_is_nonzero(dim, rec1, rec2) for dim in (2, 3)]
    ok_pts = all(r[0] for r in res)
    checks.check("B1", ok_form and ok_pts,
                 "T1: the total two-step momentum of two records at total wave vector K and relative q is g_a = sin K_a cos 2q_a in every band (symbolic, Z^2 and Z^3); at the point k1 = K/2 + q, k2 = K/2 - q with Pythagorean angles the shell derivative dg_1 ^ dE on (q_1, q_2) is nonzero for all four band pairs in both dimensions (dg_1/dq_1 = %s, squares %s vs %s and %s vs %s differ), so g is not constant on the shell there; being analytic, it is non-constant on every shell component for almost every K and E" % (res[0][1], res[0][2][0], res[0][2][1], res[1][2][0], res[1][2][1]))


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: a one-body placement adds nothing to the current within a band; the free current is coin-scalar."""
    k = sp.symbols("k1:4", real=True)
    f0, f1, f2, f3 = sp.symbols("f0:4", real=True)
    h = sum((sp.sin(k[a]) * PAULI[a] for a in range(3)), sp.zeros(2, 2))
    eps = sp.sqrt(sum(sp.sin(x) ** 2 for x in k))
    f = f0 * sp.eye(2) + f1 * SX + f2 * SY + f3 * SZ
    comm = sp.I * (h * f - f * h)
    if mut("placement_band_diagonal_forged"):
        comm = comm + f1 * sp.eye(2)
    ok = True
    for s in (1, -1):
        proj = (sp.eye(2) + s * h / eps) / 2
        ok = ok and sp.simplify((proj * comm).trace()) == 0
    # the free record's current is its two-step momentum, sin(k)cos(k) per axis, a multiple of the identity on the coins
    P = [sp.sin(k[a]) * sp.cos(k[a]) * sp.eye(2) for a in range(3)]
    ok = ok and all((h * Pa - Pa * h).applyfunc(sp.simplify) == sp.zeros(2, 2) for Pa in P)
    checks.check("C1", ok,
                 "T2: for any translation-invariant one-body placement f(k) = f0 + f.sigma, the change i[h(k), f(k)] of one record's current has zero trace against each band projector (1 +- h/eps)/2 (symbolic on Z^3): within a band a placement adds nothing to the current; the free record's current is its two-step momentum sin k cos k, a multiple of the identity on the coins that commutes with h(k)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T4 (the line): every collision shell on the line is a pair of points on which g is constant."""
    K, q, q0 = sp.symbols("K q q0", real=True)
    g = sp.sin(K) * sp.cos(2 * q)
    ok = True
    # equal coins: E = sin(K/2 + q) + sin(K/2 - q) = 2 sin(K/2) cos q; shell {q0, -q0}
    E_eq = sp.sin(K / 2 + q) + sp.sin(K / 2 - q)
    ok = ok and sp.simplify(sp.expand_trig(E_eq - 2 * sp.sin(K / 2) * sp.cos(q))) == 0
    ok = ok and sp.simplify(E_eq.subs(q, q0) - E_eq.subs(q, -q0)) == 0 and sp.simplify(g.subs(q, q0) - g.subs(q, -q0)) == 0
    # opposite coins: E = sin(K/2 + q) - sin(K/2 - q) = 2 cos(K/2) sin q; shell {q0, pi - q0}
    E_op = sp.sin(K / 2 + q) - sp.sin(K / 2 - q)
    ok = ok and sp.simplify(sp.expand_trig(E_op - 2 * sp.cos(K / 2) * sp.sin(q))) == 0
    other = sp.pi - q0
    if mut("line_shell_forged"):
        other = sp.pi / 2 - q0
    ok = ok and sp.simplify(E_op.subs(q, q0) - E_op.subs(q, other)) == 0 and sp.simplify(g.subs(q, q0) - g.subs(q, other)) == 0
    checks.check("D1", ok,
                 "T4: on the line (walkers sigma_z D) the collision shells are pairs of points: equal coins have E = 2 sin(K/2) cos q, shell {q0, -q0}; opposite coins have E = 2 cos(K/2) sin q, shell {q0, pi - q0}; on both g = sin K cos 2q takes one value, so a kept current puts no condition on the line's collisions (as block 137 found: the line keeps its books under one record per site)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Controls: the coincident states one record per site removes, per total wave vector and exchange sign."""
    up = sp.Matrix([1, 0])
    dn = sp.Matrix([0, 1])
    basis = [sp.kronecker_product(x, y) for x in (up, dn) for y in (up, dn)]
    swap = sp.Matrix(4, 4, lambda i, j: 1 if (i // 2 == j % 2 and i % 2 == j // 2) else 0)
    # at coincidence exchange acts on the coins alone: antisymmetric pairs keep the coin-antisymmetric states there
    anti = (sp.eye(4) - swap) / 2
    sym = (sp.eye(4) + swap) / 2
    r_f, r_b = anti.rank(), sym.rank()
    if mut("removed_count_forged"):
        r_f = 2
    # the singlet's overlap with a band pair (s1, s2) at directions n1, n2: (1 - s1 s2 n1.n2)/4
    n1 = sp.Matrix([Fr(3, 5), Fr(4, 5), 0])
    n2 = sp.Matrix([0, Fr(5, 13), Fr(12, 13)])
    S = (basis[1] - basis[2]) / sp.sqrt(2)
    ok_ov = True
    for s1 in (1, -1):
        for s2 in (1, -1):
            p1 = (sp.eye(2) + s1 * sum((n1[a] * PAULI[a] for a in range(3)), sp.zeros(2, 2))) / 2
            p2 = (sp.eye(2) + s2 * sum((n2[a] * PAULI[a] for a in range(3)), sp.zeros(2, 2))) / 2
            ov = sp.simplify((S.T * sp.kronecker_product(p1, p2) * S)[0])
            ok_ov = ok_ov and ov == (1 - s1 * s2 * (n1.T * n2)[0]) / 4 and ov != 0
    checks.check("E1", r_f == 1 and r_b == 3 and ok_ov,
                 "controls: one record per site removes, at every total wave vector, the coincident coin states - one (the singlet) for antisymmetric pairs, three for symmetric pairs; the singlet overlaps every band pair, (1 - s1 s2 n1.n2)/4 != 0 at the test directions, so the removed state couples to the continuum and exclusion scatters, as block 137's lost current requires")
    family_e2(checks)


def family_e2(checks: Checks) -> None:
    """T5, step 1 illustrated: the perturbation determinant vanishes at the removed state's energy."""
    z, lam = sp.symbols("z lambda")
    b = sp.Rational(1, 3)
    R = 3
    n = 2 * R + 1
    h0 = sp.zeros(n, n)
    for i in range(n - 1):
        h0[i, i + 1] = b
        h0[i + 1, i] = b
    c = R                      # the coincident relative position r = 0
    P = sp.eye(n)
    P[c, c] = 0
    Q = sp.eye(n) - P
    h2 = P * h0 * P + lam * Q
    A = h2 - h0
    delta = sp.simplify((sp.eye(n) + A * (h0 - z * sp.eye(n)).inv()).det())
    ratio = sp.simplify((h2 - z * sp.eye(n)).det() / (h0 - z * sp.eye(n)).det())
    at = lam if not mut("determinant_zero_forged") else lam + 1
    ok = sp.simplify(delta - ratio) == 0 and sp.simplify(ratio.subs(z, at)) == 0
    checks.check("E2", ok,
                 "T5 (step 1 illustrated): on the line's relative problem truncated to %d positions with the coincident state removed and placed at lambda, the perturbation determinant det(1 + (h'' - h0)(h0 - z)^-1) equals det(h'' - z)/det(h0 - z) symbolically in z and vanishes at z = lambda: a removed state is a zero of the determinant, which transparency would force to be identically one" % n)


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 136, 137 and 140 placed; it reports that no local interaction keeps two records' books under one record per site in two or three dimensions; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the closed form g_a = sin K_a cos 2q_a of the total two-step momentum, symbolically on Z^2 and Z^3",
    "per_site: executed - the shell derivative dg_1 ^ dE at a Pythagorean point for all four band pairs, by rational comparison",
    "per_mode: executed - the placement lemma for any one-body term f0 + f.sigma, symbolically on Z^3",
    "per_block: executed - the line's two-point shells with one value of g; the coincident states removed and their overlap with every band pair; the perturbation determinant on a truncation vanishing at the removed state",
    "lattice_wide: two records; finite-range interactions; almost every total wave vector; the scattering and analytic steps are named standard imports; assumption (A') at one wave vector is named, supported by a floating-point search, not certified",
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
    print("scope: exact books need records that never scatter or bind - a kept total energy current makes two interacting records transparent in the plane and in space, and a transparent pair removes and binds nothing (under the named assumption at one wave vector), so nothing local keeps the books under one record per site; on a line no condition arises; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
