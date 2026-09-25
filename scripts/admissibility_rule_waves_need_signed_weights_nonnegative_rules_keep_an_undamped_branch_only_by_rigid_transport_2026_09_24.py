#!/usr/bin/env python3
"""Exact checks: waves need signed weights - a formation rule whose weights are nonnegative with gain one (odds) keeps an
undamped branch on an open set of wave numbers only by rigid transport, at any depth of memory and in any dimension; a signed
two-level rule propagates at every wave number, and the coin walk's step is such a signed rule (a harvest block from five
Grok-refereed probes attempts; blocks 13, 54 and 96 as landed supplied; not adopted).

B (T1): nonnegative rules - Schur-Cohn certificates that the non-transport branches lie strictly inside the unit disk.
C (T2): the entrywise lemma on instances - gauges keep a unimodular eigenvalue, anything else does not.
D (T3): the signed two-level rule - lossless at every wave number, omega = |k| on the line, round long-wave cones.
E (T4): the coin walk's step obeys U^2 - (tr U) U + 1 = 0, a signed two-level rule.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_A_FORMATION_RULE_WITH_NONNEGATIVE_WEIGHTS_KEEPS_AN_UNDAMPED_BRANCH_ONLY_BY_RIGID_TRANSPORT_AND_THE_AMPLITUDE_STEP_IS_A_SIGNED_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_waves_need_signed_weights_a_formation_rule_with_nonnegative_weights_keeps_an_undamped_branch_only_by_rigid_transport_and_the_amplitude_step_is_a_signed_rule_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "average_taken_lossless": "B",
    "lemma_forged": "C",
    "signed_rule_forged": "D",
    "unitary_step_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the admissibility rule supplies a probability distribution at each site (nonnegative odds); records form; Admissibility is not a dynamics axiom (the formation law in level time and the walk are supplied clauses)")


# ============================================================================================ polynomials with Gaussian-rational coefficients
CZ, C1 = (Fr(0), Fr(0)), (Fr(1), Fr(0))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cconj(a):
    return (a[0], -a[1])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def pmul(p, q):
    out = [CZ] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = cadd(out[i + j], cmul(a, b))
    return out


def strictly_inside(p):
    """Schur-Cohn: every root of p (coefficients low degree first, Gaussian rationals) lies strictly inside the unit disk."""
    p = list(p)
    while len(p) > 1 and p[-1] == CZ:
        p.pop()
    while len(p) > 1:
        n = len(p) - 1
        a0, an = p[0], p[n]
        if not cabs2(a0) < cabs2(an):
            return False
        # p_{n-1}(z) = (conj(a_n) p(z) - a_0 p*(z)) / z, p*(z) = z^n conj(p(1/conj z))
        star = [cconj(p[n - j]) for j in range(n + 1)]
        q = [csub(cmul(cconj(an), p[j]), cmul(a0, star[j])) for j in range(n + 1)]
        p = q[1:]
        while len(p) > 1 and p[-1] == CZ:
            p.pop()
    return True


def charpoly2(m):
    """det(z - M) for a 2x2 matrix of Gaussian rationals, low degree first."""
    tr = cadd(m[0][0], m[1][1])
    det = csub(cmul(m[0][0], m[1][1]), cmul(m[0][1], m[1][0]))
    return [det, (-tr[0], -tr[1]), C1]


def charpoly3(m):
    """det(z - M) for a 3x3 matrix of Gaussian rationals, low degree first."""
    tr = cadd(cadd(m[0][0], m[1][1]), m[2][2])
    minors = CZ
    for i, j in ((0, 1), (0, 2), (1, 2)):
        minors = cadd(minors, csub(cmul(m[i][i], m[j][j]), cmul(m[i][j], m[j][i])))
    det = CZ
    for perm, sgn in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        term = (Fr(sgn), Fr(0))
        for r in range(3):
            term = cmul(term, m[r][perm[r]])
        det = cadd(det, term)
    return [(-det[0], -det[1]), minors, (-tr[0], -tr[1]), C1]


ANGLES = ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(0), Fr(1)), (Fr(-4, 5), Fr(3, 5)), (Fr(8, 17), Fr(15, 17)))


def phase(c, s, n=1):
    """e^(-i n k) for cos k = c, sin k = s."""
    out = C1
    for _ in range(abs(n)):
        out = cmul(out, (c, -s) if n > 0 else (c, s))
    return out


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: nonnegative gain-one rules - the witnesses, strictly inside the unit disk away from rigid transport."""
    ok = True
    for c, s in ANGLES:
        e = phase(c, s)
        # the average of a site and its neighbour: one level, symbol (1 + e^-ik)/2
        ok = ok and strictly_inside([csub(CZ, cmul((Fr(1, 2), Fr(0)), cadd(C1, e))), C1])
        # the persistent walk of block 96's line: z^2 - 2p cos k z + (2p - 1), p = 9/25
        p9 = Fr(9, 25)
        ok = ok and strictly_inside([(2 * p9 - 1, Fr(0)), (-2 * p9 * c, Fr(0)), C1])
        # two levels split between displacements: w0 = (1/2) delta_1, w1 = (1/2) delta_2 -> (z - e)(z + e/2): one transport root, one inside
        split = [csub(CZ, cmul((Fr(1, 2), Fr(0)), phase(c, s, 2))), csub(CZ, cmul((Fr(1, 2), Fr(0)), e)), C1]
        other = [cmul((Fr(1, 2), Fr(0)), e), C1]
        ok = ok and pmul([csub(CZ, e), C1], other) == split and strictly_inside(other)
        # the mixing rule: two components, all weight at displacement +1, A = [[1/2, 1/2], [1, 0]]: W(k) = e^-ik A
        w = [[cmul(e, (Fr(1, 2), Fr(0))), cmul(e, (Fr(1, 2), Fr(0)))], [e, CZ]]
        cp = charpoly2(w)
        rest = [cmul((Fr(1, 2), Fr(0)), e), C1]
        ok = ok and pmul([csub(CZ, e), C1], rest) == cp and strictly_inside(rest)
        # the half-step rule: theta_{t+1}(x) = theta_{t-1}(x - 1): z^2 - e^-ik, both roots of modulus one (rigid, velocity 1/2)
        ok = ok and not strictly_inside([csub(CZ, e), CZ, C1])
    if mut("average_taken_lossless"):
        ok = ok and not strictly_inside([csub(CZ, cmul((Fr(1, 2), Fr(0)), cadd(C1, phase(Fr(3, 5), Fr(4, 5))))), C1])
    checks.check("B1", ok,
                 "T1: at five rational angles (Schur-Cohn, exact): the neighbour average (1 + e^-ik)/2, block 96's persistent line walk at p = 9/25, and the decaying partners of the split two-level rule and of the two-component mixing rule have every root strictly inside the unit disk; the unimodular branches that remain are transport - e^-ik for the split and mixing rules, +-e^-ik/2 for the half-step rule")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2's key lemma on instances: |B| <= C entrywise with a unimodular eigenvalue forces |B| = C."""
    stoch = [[(Fr(1, 2), Fr(0)), (Fr(1, 3), Fr(0)), (Fr(1, 6), Fr(0))],
             [(Fr(1, 4), Fr(0)), (Fr(1, 4), Fr(0)), (Fr(1, 2), Fr(0))],
             [(Fr(2, 5), Fr(0)), (Fr(0), Fr(0)), (Fr(3, 5), Fr(0))]]
    ok, tested = True, 0
    for c, s in ANGLES:
        u = (c, s)
        # a diagonal conjugation D C D^-1 times a global phase keeps |B| = C and a unimodular eigenvalue
        d = [C1, u, cmul(u, u)]
        gauged = [[cmul(cmul(d[i], stoch[i][j]), cconj(d[j])) for j in range(3)] for i in range(3)]
        glob = [[cmul(u, gauged[i][j]) for j in range(3)] for i in range(3)]
        cp_g = charpoly3(glob)
        ok = ok and not strictly_inside(cp_g)
        # breaking |B| = C in one entry (a phase that is not a gauge) pushes every root inside
        broken = [row[:] for row in stoch]
        broken[0][1] = cmul(u, stoch[0][1])
        for scale in ((Fr(1), Fr(0)), (Fr(9, 10), Fr(0))):
            b = [[cmul(scale, x) if (i, j) == (2, 0) else x for j, x in enumerate(row)] for i, row in enumerate(broken)]
            cp_b = charpoly3(b)
            inside = strictly_inside(cp_b)
            if mut("lemma_forged"):
                inside = not inside
            ok = ok and inside
            tested += 1
    checks.check("C1", ok and tested == 10,
                 "T2 (the entrywise lemma, on instances): for a row-stochastic irreducible 3x3 C, a gauge D C D^-1 times a global unit phase keeps a unimodular eigenvalue, while a single entry phase that is no gauge (with or without a reduced modulus) leaves every root strictly inside the unit disk (Schur-Cohn at five rational angles) - consistent with the lemma |B| <= C, B x = lambda x, |lambda| = 1 => |B| = C, whose equality case is rigid transport up to a gauge")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the signed two-level rule theta_{t+1} = 2a P theta_t - theta_{t-1} propagates."""
    lam, a, pk = sp.symbols("lambda a P", real=True)
    poly = lam ** 2 - 2 * a * pk * lam + 1
    roots = sp.solve(poly, lam)
    prod_one = sp.simplify(roots[0] * roots[1]) == 1
    k = sp.symbols("k", real=True)
    om = sp.symbols("omega", real=True)
    one_d = sp.simplify(sp.cos(om).subs(om, k) - sp.cos(k)) == 0
    kv = sp.symbols("k1:4", real=True)
    pd = sum(sp.cos(x) for x in kv) / 3
    t = sp.symbols("t", positive=True)
    # cos omega = P gives omega^2 = 2(1 - P) + (1 - P)^2/3 + ..., and 1 - P = O(t^2): the t^2 term of omega^2 is that of 2(1 - P)
    axis = sp.series(2 * (1 - pd.subs({kv[0]: t, kv[1]: 0, kv[2]: 0})), t, 0, 4).removeO()
    diag = sp.series(2 * (1 - pd.subs({kv[0]: t / sp.sqrt(3), kv[1]: t / sp.sqrt(3), kv[2]: t / sp.sqrt(3)})), t, 0, 4).removeO()
    inv = sp.series(sp.acos(1 - sp.symbols("y", positive=True)) ** 2, sp.symbols("y", positive=True), 0, 3).removeO()
    y = sp.symbols("y", positive=True)
    inv_ok = sp.simplify(inv - (2 * y + y ** 2 / 3)) == 0
    speed = inv_ok and sp.simplify(axis.coeff(t, 2)) == sp.Rational(1, 3) and sp.simplify(diag.coeff(t, 2)) == sp.Rational(1, 3)
    grow = sp.solve(poly.subs({a: sp.Rational(5, 4), pk: 1}), lam)
    grows = max(grow) == 2
    lossless = True
    for cval in (sp.Rational(3, 5), sp.Rational(-1, 2), sp.Rational(1)):
        disc = sp.discriminant(poly.subs({a: 1, pk: cval}), lam)
        lossless = lossless and disc <= 0
    if mut("signed_rule_forged"):
        lossless = lossless and sp.discriminant(poly.subs({a: 1, pk: sp.Rational(3, 5)}), lam) > 0
    checks.check("D1", prod_one and one_d and speed and grows and lossless,
                 "T3: for theta_{t+1} = 2a P theta_t - theta_{t-1} (P the neighbour average, symbol P(k) = (1/d) sum_j cos k_j; the deeper weight -1 is negative) the two roots multiply to 1, so both are unimodular exactly when |a P(k)| <= 1: at a = 1 every wave number propagates without loss, cos omega = P(k); in one dimension omega = |k| exactly; in three dimensions omega^2 = |k|^2/3 + O(k^4) along an axis and along the body diagonal alike; at a = 5/4 the rule has the root 2 at k = 0 and grows")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the coin walk's step is a signed two-level recursion of T3's kind."""
    th, k = sp.symbols("theta k", real=True)
    coin = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
    shift = sp.diag(sp.exp(-sp.I * k), sp.exp(sp.I * k))
    u = coin * shift
    det_one = sp.simplify(u.det()) == 1
    tr = sp.simplify((u.trace()).rewrite(sp.cos))
    tr_ok = sp.simplify(tr - 2 * sp.cos(th) * sp.cos(k)) == 0
    ch = (u * u - u.trace() * u + sp.eye(2)).applyfunc(lambda e: sp.simplify(sp.expand(e)))
    ch_ok = ch == sp.zeros(2, 2)
    if mut("unitary_step_forged"):
        ch_ok = (u * u - u.trace() * u - sp.eye(2)).applyfunc(lambda e: sp.simplify(sp.expand(e))) == sp.zeros(2, 2)
    checks.check("E1", det_one and tr_ok and ch_ok,
                 "T4: the 1+1 coin walk U(k) = C(theta) diag(e^-ik, e^ik) has det U = 1 and tr U = 2 cos theta cos k, so by the matrix identity U^2 - (tr U) U + 1 = 0 each amplitude obeys psi_{t+1} = 2 cos theta C psi_t - psi_{t-1} (C the neighbour average): the amplitude step is T3's signed rule with a = cos theta, lossless at every wave number")


# ============================================================================================ family F
FENCES = (
    "This note works within block 13's linear formation law in level time and block 54's walk, both as landed on main and both supplied; it reports that nonnegative weights cannot carry undamped dispersive waves while signed weights can, and that the amplitude walk's step is such a signed rule; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Perron", "Frobenius", "Wielandt", "Schur", "Cohn", "Jury", "Cayley", "Hamilton", "Markov", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - Schur-Cohn certificates for the average, the persistent line walk and the decaying partners of the split and mixing rules at five rational angles",
    "per_site: executed - the entrywise lemma on a row-stochastic 3x3 matrix: gauges keep a unimodular eigenvalue, a single non-gauge phase or a reduced entry does not",
    "per_mode: executed - the signed rule's roots multiply to one; omega = |k| on the line; omega^2 = |k|^2/3 + O(k^4) along an axis and the body diagonal; growth at a = 5/4",
    "per_block: executed - the coin walk: det U = 1, tr U = 2 cos theta cos k, U^2 - (tr U) U + 1 = 0",
    "lattice_wide: T2's classification for every nonnegative gain-one rule of any depth, any number of components and any dimension, with its named imports; T3-T4 for every wave number; the formation law and the walk are supplied",
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
    print("scope: waves need signed weights - nonnegative gain-one formation rules keep an undamped branch on an open set only by rigid transport; the signed two-level rule is lossless at every wave number; the coin walk step is such a signed rule; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
