#!/usr/bin/env python3
"""Exact checks: under one record per site a collision changes the records' two-step momentum only at third order in their
offsets from the cones - within block 54's walk and block 78's one record per site (two records, no added interaction), with
blocks 140 and 143 as landed: near a corner of the zone a record's two-step momentum depends only on its offset from that corner;
crystal momentum keeps the offsets' sum exactly in every collision when the offsets are below pi/4, so the pair's two-step
momentum changes only at third order; for antisymmetric pairs the hard core scatters through a rank-one T-matrix, so every
incoming state on a shell scatters alike and the change is nonzero for almost every incoming state (block 143 T1), exactly
third order (the supervisor's own derivation; not adopted).

B (kinematics): the corner identity and the series; the offsets' sum in every corner channel.
C (the contact collision): the compression's resolvent (rank-one T-matrix); the loss rate for a rank-one kernel.
D (the order): the cubic of the offsets is not constant on the massless shell (an explicit family and two exact points).
E (the contact weight): the singlet's weight in a band pair; near one corner an antisymmetric pair meets any interaction only
       through the singlet at leading order.
Exact rational, Gaussian-rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp
from sympy import QQ_I
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "cubic_coefficient_forged": "B",
    "addition_law_forged": "B",
    "rank_one_numerator_forged": "C",
    "cubic_form_forged": "D",
    "singlet_weight_forged": "E",
    "triplet_kernel_forged": "E",
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
SX, SY, SZ = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])


def dm(matrix):
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I)


def eye(n):
    return DomainMatrix.eye(n, QQ_I)


def scal(z, n):
    return eye(n) * QQ_I.from_sympy(sp.sympify(z))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk and one record per site are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    d = sp.Symbol("delta", real=True)
    corner = all(sp.simplify(sp.sin(A + d) * sp.cos(A + d) - sp.sin(d) * sp.cos(d)) == 0 for A in (0, sp.pi))
    cubic = -sp.Rational(1, 3) if mut("cubic_coefficient_forged") else -sp.Rational(2, 3)
    series = sp.series(sp.sin(d) * sp.cos(d), d, 0, 7).removeO()
    series_ok = sp.expand(series - (d + cubic * d ** 3 + sp.Rational(2, 15) * d ** 5)) == 0
    checks.check("B1", corner and series_ok, "at a corner A in {0, pi}, sin(A + delta) cos(A + delta) = sin(delta) cos(delta) = delta - (2/3) delta^3 + (2/15) delta^5 + ...: odd in delta, so no second-order term")
    # offsets' sums s, s' in (-1/2, 1/2) (units of pi), corners A, B, A', B' in {0, 1}: congruence mod 2 forces s = s'
    grid = [Fr(k, 12) for k in range(-5, 6)]
    ok, seen = True, 0
    for A, B, A2, B2 in product((0, 1), repeat=4):
        for s in grid:
            for s2 in grid:
                diff = (A + B + s) - (A2 + B2 + s2)
                if diff.denominator == 1 and diff.numerator % 2 == 0:
                    ok = ok and s == s2
                    seen += 1
    checks.check("B2", ok and seen > 0, f"crystal momentum: with offset sums in (-pi/2, pi/2) and corners in {{0, pi}}, every congruence mod 2 pi on a rational grid ({seen} cases over all corner channels) has equal offset sums: the sum is conserved exactly in every channel")
    # (d) subadditivity of eps at exact points whose sines and cosines are rational (the circle's rational points form a group)
    base = [(Fr(0), Fr(1)), (Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17)), (Fr(20, 29), Fr(21, 29))]
    angles = []
    for (sn, cs) in base:
        for (a1, a2) in ((sn, cs), (-sn, cs), (sn, -cs), (-sn, -cs)):
            if (a1, a2) not in angles:
                angles.append((a1, a2))

    def add_angle(u, v):
        (s1, c1), (s2, c2) = u, v
        if mut("addition_law_forged"):
            return (s1 * c2 + 2 * c1 * s2, c1 * c2 - s1 * s2)
        return (s1 * c2 + c1 * s2, c1 * c2 - s1 * s2)

    def eps2(kv):
        return sum(c[0] ** 2 for c in kv)

    def le_sum(x2, y2, z2):
        # sqrt(x2) <= sqrt(y2) + sqrt(z2), exactly, for nonnegative rationals
        lhs = x2 - y2 - z2
        return lhs <= 0 or lhs * lhs <= 4 * y2 * z2

    sub_ok, n_pts = True, 0
    for i in range(0, len(angles), 3):
        for j in range(1, len(angles), 4):
            for l in range(2, len(angles), 5):
                a = (angles[i], angles[j], angles[l])
                b = (angles[j], angles[l], angles[i])
                ab = tuple(add_angle(a[t], b[t]) for t in range(3))
                sub_ok = sub_ok and le_sum(eps2(ab), eps2(a), eps2(b))
                n_pts += 1
    quarter = sp.sin(sp.pi / 4) ** 2 == sp.Rational(1, 2)
    checks.check("B3", sub_ok and quarter and n_pts > 0, f"the dispersion eps(k) = (sum_a sin^2 k_a)^(1/2) is subadditive, eps(a + b) <= eps(a) + eps(b), at {n_pts} exact point pairs with rational sines and cosines; with sin^2(pi/4) = 1/2, a pair of energy below sqrt(2)/2 keeps every offset below pi/4, and a band pair (+, -) has energy at most eps(K) <= eps(k1) + eps(k2)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    n = 6
    h = sp.Matrix(n, n, lambda i, j: sp.Rational((i + 1) * (j + 2) % 5 - 2, 3) + (sp.Rational(i - j, 7) * sp.I if i != j else 0))
    h0 = dm((h + h.H) / 2)
    c = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), 0, 0])
    cD, cT = dm(c), dm(c.T)
    P = eye(n) - cD * cT
    z = sp.Rational(1, 3) + sp.I * sp.Rational(2, 5)
    R0 = (h0 - scal(z, n)).inv()
    gcc = (cT * R0 * cD).to_list()[0][0]
    if mut("rank_one_numerator_forged"):
        G = R0 - R0 * cD * cT * (QQ_I.one / gcc)
    else:
        G = R0 - R0 * cD * cT * R0 * (QQ_I.one / gcc)
    ok1 = P * ((P * h0 * P - scal(z, n)) * G) * P == P and G * cD == dm(sp.zeros(n, 1)) and cT * G == dm(sp.zeros(1, n))
    checks.check("C1", ok1, "the compression to the complement of a removed unit vector c has resolvent G = R0 - R0|c><c|R0/<c|R0|c> (exact, a six-state model): the hard core scatters through the rank-one T-matrix |c><c|/G_cc")
    w = [Fr(1, 9), Fr(2, 9), Fr(1, 3), Fr(1, 6), Fr(1, 18)]
    gs = [Fr(1, 2), Fr(-1, 3), Fr(1, 4), Fr(2, 5), Fr(-1, 7)]
    gc2 = Fr(4, 9) + Fr(1, 25)                                   # |G_cc|^2 for G_cc = 2/3 - i/5
    gbar = sum((a * b for a, b in zip(w, gs)), Fr(0)) / sum(w, Fr(0))
    ok2 = all(sum((w[q] * w[j] / gc2 * (gs[j] - gs[q]) for j in range(5)), Fr(0)) == w[q] / gc2 * sum(w, Fr(0)) * (gbar - gs[q]) for q in range(5))
    checks.check("C2", ok2, "for a rank-one kernel <q'|c><c|q>/G_cc the rate-weighted change of g from q is |<c|q>|^2 rho_c (gbar - g(q))/|G_cc|^2, with gbar the contact-weighted mean: the same outgoing distribution for every incoming state (exact on a five-state shell)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    p, x, y = sp.symbols("p x y", real=True)
    d1 = (p / 2 + x, y, sp.Integer(0))
    d2 = (p / 2 - x, -y, sp.Integer(0))
    cubes = sp.expand(sum(a ** 3 for a in d1) + sum(a ** 3 for a in d2))
    coef = 2 if mut("cubic_form_forged") else 3
    form_ok = sp.expand(cubes - (p ** 3 / 4 + coef * p * x ** 2)) == 0
    E = sp.Rational(5, 2)
    pts = ({p: 1, x: sp.Rational(5, 4), y: 0}, {p: 1, x: 0, y: sp.sqrt(21) / 4})

    def norm(v, s):
        return sp.sqrt(sum(a.subs(s) ** 2 for a in v))
    on_shell = all(sp.simplify(norm(d1, s) + norm(d2, s) - E) == 0 for s in pts)
    vals = [cubes.subs(s) for s in pts]
    checks.check("D1", form_ok and on_shell and vals[0] != vals[1],
                 f"on the massless shell |d1| + |d2| = E with total offset (p, 0, 0) the cubic of the offsets is p^3/4 + 3 p x^2 along d1 = (p/2 + x, y, 0), d2 = (p/2 - x, -y, 0): at E = 5/2, p = 1 it is {vals[0]} at (5/4, 0) and {vals[1]} at (0, sqrt 21/4), so the third-order change is not constant on the shell")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    n1 = sp.symbols("a1:4", real=True)
    n2 = sp.symbols("b1:4", real=True)

    def proj(nv, s):
        return (sp.eye(2) + s * (nv[0] * SX + nv[1] * SY + nv[2] * SZ)) / 2
    sing = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
    sign = -1 if mut("singlet_weight_forged") else 1
    ok = True
    for s1 in (1, -1):
        for s2 in (1, -1):
            val = sp.expand((sing.H * sp.kronecker_product(proj(n1, s1), proj(n2, s2)) * sing)[0, 0])
            target = (1 - sign * s1 * s2 * sum(a * b for a, b in zip(n1, n2))) / 4
            ok = ok and sp.expand(val - target) == 0
    checks.check("E1", ok, "the singlet's weight in the band pair (s1, s2) with spinor directions n1, n2 is (1 - s1 s2 n1.n2)/4, positive except where n1.n2 = s1 s2, a null set of the shell")
    # E2: antisymmetrization at q = 0: (u - SWAP u)/2 = P_s u, P_s the singlet projector; so an antisymmetric pair's plane wave on a
    # finite set of relative positions is, at leading order, (sum_r |r>) (x) P_s u(q), and any operator there acts through <s|u>
    SW = sp.Matrix(4, 4, lambda i2, j2: 1 if (i2 // 2 == j2 % 2 and i2 % 2 == j2 // 2) else 0)
    s_vec = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
    Ps = s_vec * s_vec.H
    if mut("singlet_weight_forged"):
        Ps = Ps + sp.diag(1, 0, 0, 0)
    anti_ok = sp.simplify((sp.eye(4) - SW) / 2 - Ps) == sp.zeros(4, 4)
    uu = sp.Matrix(sp.symbols("w0:4"))
    Tloc = sp.Matrix(3, 3, sp.symbols("t0:9"))                     # any operator on three relative positions, in the singlet sector
    ones = sp.Matrix([1, 1, 1])
    lead = (sp.kronecker_product(ones, Ps * uu)).H * sp.kronecker_product(Tloc, Ps) * sp.kronecker_product(ones, Ps * uu)
    tau = (ones.T * Tloc * ones)[0, 0]
    rank_one = sp.expand(lead[0, 0] - (uu.H * s_vec)[0, 0] * tau * (s_vec.H * uu)[0, 0]) == 0
    checks.check("E2", anti_ok and rank_one,
                 "T4: (1 - SWAP)/2 is the singlet projector, so at leading order an antisymmetric pair's plane wave on a finite set of relative positions is (sum_r |r>) (x) P_s u, and any operator there gives the on-shell form <u'|s> tau <s|u>: the hard core's coin structure, whatever the interaction")
    # E3: both exchange signs at leading order near one corner: the kernels, their angular means, and the triplet's irreducibility
    tt = sp.Symbol("t", real=True)
    c_ = (1 - tt ** 2) / (1 + tt ** 2)

    def up_vec(tv):
        return sp.Matrix([1, tv]) / sp.sqrt(1 + tv ** 2)

    def dn_vec(tv):
        return sp.Matrix([-tv, 1]) / sp.sqrt(1 + tv ** 2)
    P_t = (sp.eye(4) + SW) / 2
    u0 = sp.kronecker_product(up_vec(0), dn_vec(0))
    ut = sp.kronecker_product(up_vec(tt), dn_vec(tt))
    amp_t = (ut.H * P_t * u0)[0, 0]
    amp_s = (ut.H * Ps * u0)[0, 0]
    w_t = sp.simplify(sp.expand(amp_t * sp.conjugate(amp_t)))
    w_s = sp.simplify(sp.expand(amp_s * sp.conjugate(amp_s)))
    cc = sp.Symbol("c")
    wt_form = cc / 4 if mut("triplet_kernel_forged") else cc ** 2 / 4
    kernels_ok = sp.simplify(w_t - wt_form.subs(cc, c_)) == 0 and sp.simplify(w_s - sp.Rational(1, 4)) == 0

    def mean_c2(w):
        return sp.integrate(w * cc ** 2, (cc, -1, 1)) / sp.integrate(w, (cc, -1, 1))
    means_ok = mean_c2(cc ** 2 / 4) == sp.Rational(3, 5) and mean_c2(sp.Rational(1, 4)) == sp.Rational(1, 3)
    Uz = (sp.eye(2) - sp.I * SZ) / sp.sqrt(2)
    Ux = (sp.eye(2) - sp.I * SX) / sp.sqrt(2)
    trip = sp.Matrix.hstack(sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 1, 0]) / sp.sqrt(2), sp.Matrix([0, 0, 0, 1]))
    Xm = sp.Matrix(3, 3, sp.symbols("x0:9"))
    eqs = []
    for U in (Uz, Ux):
        Rm = sp.simplify(trip.H * sp.kronecker_product(U, U) * trip)
        eqs += list(sp.expand(Xm * Rm - Rm * Xm))
    sol = sp.solve(eqs, list(Xm), dict=True)
    irreducible = len(sol) == 1 and len(Xm.subs(sol[0]).free_symbols) == 1 and Xm.subs(sol[0]) == Xm.subs(sol[0])[0, 0] * sp.eye(3)
    checks.check("E3", kernels_ok and means_ok and irreducible,
                 "both exchange signs at leading order near one corner: the singlet kernel is 1/4 and the triplet kernel c^2/4 (c the cosine of the scattering angle), with angular means <c^2> = 1/3 and 3/5, both below one; the coincident triplet is irreducible under the quarter turns (its commutant is the scalars), so the hard core and any symmetric interaction act on it as a multiple of the identity")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 78, 140 and 143 as landed on main (the walk, one record per site, the two-step momentum and the shell geometry); it reports at which order in the records' offsets from the corners of the zone a collision changes their two-step momentum; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein",
                   "Schwarz", "Liouville", "Morse", "Fredholm", "Sylvester", "Paley", "Wiener", "Riesz", "Fatou", "Poussin", "Hardy", "Cauchy", "Borel", "Hölder", "Holder",
                   "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Fourier", "Taylor", "Green", "Pauli", "Hamilton", "Wigner", "Bloch", "Schrodinger", "Riemann", "Hilbert", "Schur", "Fermi", "Peierls")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 — the change is third order in the offsets", "## Theorem T1 — the change is third order in the offsets (after Einstein)", 1)
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
    "per_element: executed - the corner identity sin(A + d) cos(A + d) = sin d cos d and the series to fifth order",
    "per_site: executed - the offsets' sum in every corner channel on a rational grid (congruence mod 2 pi forces equality)",
    "per_mode: executed - the compression's resolvent (rank-one T-matrix) and the rank-one loss formula, exactly",
    "per_block: executed - the cubic of the offsets on the massless shell (a family and two exact points); the singlet's band weight",
    "lattice_wide: checked and not executed - the null-set statements on lattice shells rest on block 143 T1 and analyticity, proved in the note",
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
    print("scope: two records of the walk under one record per site, no added interaction; near the corners a collision changes the pair two-step momentum only at third order in the offsets, in every corner channel; for antisymmetric pairs the rank-one hard core makes every incoming state on a shell scatter alike and the change nonzero for almost every incoming state, exactly third order; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
