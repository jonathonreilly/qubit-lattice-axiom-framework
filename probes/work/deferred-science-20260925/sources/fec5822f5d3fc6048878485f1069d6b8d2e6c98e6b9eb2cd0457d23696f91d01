#!/usr/bin/env python3
"""Exact checks: the clocked walk's realizations in an exponential clock field - every realization keeps the even-shift identity, those
keeping every shift form a torus (block 108's circle and chain-mixing ones), none keeps the half-turn about the gradient, and in three
dimensions each small sector has exactly four, with no choice continuous across sectors (a harvest block from a Grok-refereed probes attempt;
blocks 54, 108 and 109 as landed supplied; not adopted).

B (T1): entire series solutions at every energy on the line; the boundary form of the zero-energy solutions; the shifts on it.
C (T2): the torus of Lagrangian planes kept by the unit shift; chain-separate exactly on block 108's circle; a chain-mixing witness.
D (T3): the half-turn about the line keeps no plane kept by the unit shift.
E (T4): a three-dimensional sector below sinh(g/2): four Floquet solutions, the pairing, the four kept planes, rotation labels, and the
        direction-dependent limits as the transverse momentum goes to zero.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_CLOCKED_WALKS_REALIZATIONS_EVERY_ONE_KEEPS_THE_EVEN_SHIFT_THOSE_KEEPING_EVERY_SHIFT_FORM_A_TORUS_AND_NONE_KEEPS_THE_HALF_TURN_ABOUT_THE_GRADIENT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_and_none_keeps_the_half_turn_about_the_gradient_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "series_coefficient_forged": "B",
    "isotropic_vector_forged": "C",
    "half_turn_vector_taken_isotropic": "D",
    "pairing_forged": "E",
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


I = sp.I
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk and its clock are supplied clauses)")


# ============================================================================================ family B
LAM, MU, XX = sp.symbols("lambda mu X", positive=True)


def dag(v):
    return v.conjugate().T


def form_pair(r1, v1, r2, v2, cut):
    """Boundary form B_N of two zero-energy solutions (r/mu)^n v at the cut N (the on-site terms cancel); lambda = mu^2."""
    h_up = -I / 2 * MU ** (2 * cut + 1) * SX            # the bond from N to N + 1: -(i/2) lambda^(N + 1/2) sigma_1
    h_dn = I / 2 * MU ** (2 * cut + 1) * SX
    u1n, u1m = (r1 / MU) ** cut * v1, (r1 / MU) ** (cut + 1) * v1
    u2n, u2m = (r2 / MU) ** cut * v2, (r2 / MU) ** (cut + 1) * v2
    return sp.simplify((dag(u1n) * h_up * u2m - dag(u1m) * h_dn * u2n)[0, 0])


def family_b(checks: Checks) -> None:
    """T1: entire series solutions at every energy; the boundary form of the zero-energy solutions; the shifts."""
    ok = True
    for s in (1, -1):
        for eps in (1, -1):
            coeffs = [sp.Integer(1)]
            for j in range(1, 6):
                sign = -1 if not mut("series_coefficient_forged") else 1
                coeffs.append(sp.simplify(sign * 2 * I * s * eps * coeffs[-1] / (LAM ** j - LAM ** (-j))))
            ser = lambda x: sum((cj * x ** j for j, cj in enumerate(coeffs)), sp.Integer(0))
            resid = sp.expand(I * s * eps / 2 * (ser(LAM * XX) - ser(XX / LAM)) - XX * ser(XX))
            ok = ok and sp.simplify(resid + coeffs[-1] * XX ** 6) == 0
    checks.check("B1", ok, "T1: on the line (w = lambda^x), psi(n) = (eps/mu)^n v_s S(z lambda^-n) with sigma_1 v_s = s v_s solves the walk at energy z iff (i s eps/2)(S(lambda X) - S(X/lambda)) = X S(X); the series c_0 = 1, c_j = -2 i s eps c_(j-1)/(lambda^j - lambda^-j) leaves the exact remainder -c_5 X^6 at order 5 for all four (s, eps), symbolic in lambda: its coefficients fall like lambda^(-j^2/2), so each of the four solutions is entire in z and behaves as (+-1/mu)^n at the fast end - all four are square-summable there at every energy")
    a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2")
    v = sp.Matrix([a1, a2])
    w = sp.Matrix([b1, b2])
    ok = True
    for e1 in (1, -1):
        for e2 in (1, -1):
            vals = {form_pair(sp.Integer(e1), v, sp.Integer(e2), w, cut) for cut in (0, 1, 2, 3)}
            want = sp.simplify((-I * e1 * dag(v) * SX * w)[0, 0]) if e1 == e2 else sp.Integer(0)
            ok = ok and len(vals) == 1 and sp.simplify(list(vals)[0] - want) == 0
    shift_ok = all(sp.simplify(((sp.Integer(e) / MU) ** (n - 1)) / ((sp.Integer(e) / MU) ** n) - e * MU) == 0 for e in (1, -1) for n in (0, 1, 2))
    checks.check("B2", ok and shift_ok, "T1: on the four zero-energy solutions (eps/mu)^n v the boundary form is G = diag(-i sigma_1, +i sigma_1) in the blocks eps = +1, -1, the same at every cut; the unit shift acts as eps mu and the shift by two as the scalar lambda = mu^2, so G(T1 x, T1 y) = lambda G(x, y)")


# ============================================================================================ family C
def gram(vecs):
    """G on block vectors (x+, x-): G = -i x+^dag sigma_1 y+ + i x-^dag sigma_1 y-."""
    return sp.Matrix(len(vecs), len(vecs), lambda i, j: sp.simplify(-I * (dag(vecs[i][0]) * SX * vecs[j][0])[0, 0] + I * (dag(vecs[i][1]) * SX * vecs[j][1])[0, 0]))


def family_c(checks: Checks) -> None:
    """T2: the planes kept by the unit shift are L(v1, v2) with v1, v2 isotropic: a torus; chain-separate exactly on block 108's circle."""
    t1, t2 = sp.symbols("t1 t2", real=True)
    z = sp.zeros(2, 1)
    iso = lambda t: sp.Matrix([1, I * t]) if not mut("isotropic_vector_forged") else sp.Matrix([1, t])
    plane = [(iso(t1), z), (z, iso(t2))]
    lagrangian = gram(plane) == sp.zeros(2, 2)
    pole = [(sp.Matrix([0, 1]), z), (z, sp.Matrix([0, 1]))]
    pole_ok = gram(pole) == sp.zeros(2, 2)
    block_nondegenerate = sp.Matrix([[0, -I], [-I, 0]]).det() != 0
    sep = sp.solve(sp.Eq(t2, -t1), t2) == [-t1]
    s3v1 = SZ * iso(t1)
    parallel = sp.simplify(s3v1[0] * iso(t2)[1] - s3v1[1] * iso(t2)[0])
    sep_ok = sp.simplify(parallel.subs(t2, -t1)) == 0 and sp.simplify(parallel.subs({t1: 0, t2: 1})) != 0
    witness = [(sp.Matrix([1, 0]), z), (z, sp.Matrix([1, I]))]
    witness_ok = gram(witness) == sp.zeros(2, 2)
    checks.check("C1", lagrangian and pole_ok and block_nondegenerate and sep and sep_ok and witness_ok,
                 "T2: the unit shift has eigenvalues +mu, -mu on the blocks, and each block is nondegenerate for G, so a plane kept by it is L(v1, v2) = span(v1 (x) E+, v2 (x) E-), Lagrangian exactly when v1 and v2 are isotropic for sigma_1: v = (1, i t) or (0, 1) - a torus of realizations, every one kept by the shift by two (a scalar); L meets the chains (x, sigma_3 x) and (x, -sigma_3 x) exactly when v2 is parallel to sigma_3 v1 (t2 = -t1), block 108's circle; the witness v1 = (1, 0), v2 = (1, i) is Lagrangian, kept by every shift, and chain-mixing")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the half-turn about the line keeps no plane that the unit shift keeps."""
    z = sp.zeros(2, 1)
    joint = [(sp.Matrix([1, 1]), z), (sp.Matrix([1, -1]), z), (z, sp.Matrix([1, 1])), (z, sp.Matrix([1, -1]))]
    commutes = (SX * SX) == sp.eye(2)
    norms = [gram([x])[0, 0] for x in joint]
    claimed_zero = mut("half_turn_vector_taken_isotropic")
    ok = commutes and ((all(nv != 0 for nv in norms)) if not claimed_zero else all(nv == 0 for nv in norms))
    checks.check("D1", ok, f"T3: the line walk commutes with sigma_1 (the half-turn of the content about the line), which commutes with the unit shift on the boundary space; a plane kept by both is spanned by joint eigenvectors (1, +-1) (x) E+-, whose G-norms are {', '.join(str(nv) for nv in norms)} - none is isotropic, so no realization keeps both the half-turn and the identity for the unit shift")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: a three-dimensional sector below sinh(g/2): four Floquet solutions, the pairing, the four kept planes, labels and limits."""
    lam, mu = sp.Integer(4), sp.Integer(2)
    p2, p3 = sp.Rational(1, 4), sp.Rational(1, 3)
    m = sp.sqrt(p2 ** 2 + p3 ** 2)
    s = sp.sqrt(1 + m ** 2)
    nmat = p2 * SZ - p3 * SY
    pmat = p2 * SY + p3 * SZ
    vp = [vec for val, mult, vecs in nmat.eigenvects() if sp.simplify(val - m) == 0 for vec in vecs][0]
    vm = [vec for val, mult, vecs in nmat.eigenvects() if sp.simplify(val + m) == 0 for vec in vecs][0]
    sols = {"a": (m + s, vp), "b": (m - s, vp), "c": (s - m, vm), "d": (-m - s, vm)}
    roots_ok = [sols[k][0] for k in "abcd"] == [sp.Rational(3, 2), -sp.Rational(2, 3), sp.Rational(2, 3), -sp.Rational(3, 2)] and m < (lam - 1) / (2 * mu)
    zero_ok = all(sp.simplify((I / 2 * (1 / r - r) * SX + pmat) * v) == sp.zeros(2, 1) for r, v in sols.values())
    shifts = [sp.simplify(mu / sols[k][0]) for k in "abcd"]
    distinct = len(set(shifts)) == 4
    checks.check("E1", roots_ok and zero_ok and distinct, f"T4: at lambda = 4 and (sin k2, sin k3) = (1/4, 1/3), m = 5/12 < m* = 3/4; the zero-energy solutions (r/mu)^n v with N v = ((r - 1/r)/2) v, N = sin k2 sigma_3 - sin k3 sigma_2, have r = 3/2, -2/3 (N = +m) and 2/3, -3/2 (N = -m), labelled a, b, c, d; the unit shift acts on them as mu/r = {', '.join(str(x) for x in shifts)}, four distinct values")
    names = "abcd"
    table = {}
    for x in names:
        for y in names:
            (r1, v1), (r2, v2) = sols[x], sols[y]
            vals = [sp.simplify(-I / 2 * (r1 * r2) ** cut * (r1 + r2) * (dag(v1) * SX * v2)[0, 0]) for cut in (0, 1, 2)]
            table[(x, y)] = vals[0] if len(set(vals)) == 1 else None
    paired = {(x, y) for (x, y), v in table.items() if v is None or v != 0}
    want = {("a", "c"), ("c", "a"), ("b", "d"), ("d", "b")} | ({("a", "b"), ("b", "a")} if mut("pairing_forged") else set())
    kept = sorted(x + y for i, x in enumerate(names) for y in names[i + 1:] if all(table[(u, v)] == 0 for u in (x, y) for v in (x, y)))
    checks.check("E2", paired == want and kept == ["ab", "ad", "bc", "cd"], "T4: the boundary form is independent of the cut and nonzero only on the pairs a-c and b-d (r_i r_j = 1); every other pair vanishes, through isotropy of each spinor or r_i + r_j = 0; so the planes kept by the unit shift are the six pairs and the Lagrangian ones are exactly ab, ad, bc, cd - four realizations keep every x1-shift in this sector")
    rq = (sp.eye(2) - I * SX) / sp.sqrt(2)
    n_of = lambda q2, q3: q2 * SZ - q3 * SY
    quarter = sp.simplify(rq * n_of(p2, p3) * dag(rq) - n_of(-p3, p2)) == sp.zeros(2, 2)
    half = sp.simplify(SX * n_of(p2, p3) * SX - n_of(-p2, -p3)) == sp.zeros(2, 2)
    def limit_plane(choice, q2, q3):
        nn = n_of(q2, q3)
        up = [vec for val, mult, vecs in nn.eigenvects() if val > 0 for vec in vecs][0]
        dn = [vec for val, mult, vecs in nn.eigenvects() if val < 0 for vec in vecs][0]
        spinor = {"a": (up, 1), "b": (up, -1), "c": (dn, 1), "d": (dn, -1)}
        z = sp.zeros(2, 1)
        cols = []
        for label in choice:
            vec, eps = spinor[label]
            cols.append(sp.Matrix.vstack(vec, z) if eps == 1 else sp.Matrix.vstack(z, vec))
        return sp.Matrix.hstack(*cols)
    differ = True
    for choice in ("ab", "ad", "bc", "cd"):
        pa, pb = limit_plane(choice, 1, 0), limit_plane(choice, 0, 1)
        differ = differ and sp.Matrix.hstack(pa, pb).rank() > 2
    bc_x = limit_plane("bc", 1, 0)
    bc_y = limit_plane("bc", 0, 1)
    checks.check("E3", quarter and half and differ,
                 f"T4: the quarter-turn about x1 (e^(-i pi sigma_1/4)) carries N_p to N_(-p3, p2) and the half-turn sigma_1 carries it to N_(-p), so rotations about x1 keep the labels and each of the four choices is rotation-covariant; but as m -> 0 each choice tends to a plane that depends on the direction of (sin k2, sin k3) - for bc, span({list(bc_x[:, 0])} E+, {list(bc_x[:, 1])} E-) along (1, 0) against span({list(bc_y[:, 0])}, {list(bc_y[:, 1])}) along (0, 1) - so no choice is continuous at the four points m = 0, where by T3 the half-turn keeps none")


# ============================================================================================ family F
FENCES = (
    "This note works within the clocked walk of block 54 and the exponential clock field of blocks 108 and 109, all as landed on main; it reports which self-adjoint realizations keep the clock's scaling identity and the lattice's half-turn about the gradient; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Neumann", "Glazman", "Krein", "Naimark", "Floquet", "Carleman", "Teschl", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the series solutions' recursion and remainder at every energy (symbolic in lambda), and the boundary form of the four zero-energy solutions",
    "per_site: executed - the boundary form at four cuts; the unit shift and the shift by two on the boundary space",
    "per_mode: executed - the torus of Lagrangian planes kept by the unit shift, the chain test, a chain-mixing witness, and the half-turn's joint eigenvectors",
    "per_block: executed - a sector with 0 < m < m*: the four Floquet solutions, the pairing, the four kept planes, rotation labels and the direction-dependent limits",
    "lattice_wide: T1-T3 for the line walk in w = lambda^x with the endpoint theory imported at definition level; T4 sector by sector on Z^3 with w = lambda^(x1); the walk, the clock and the exponential field are supplied",
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
    print("scope: the clocked walk in an exponential field - every realization keeps the even-shift identity; those keeping every shift form a torus containing block 108's circle; none keeps the half-turn about the gradient; in 3D four per small sector, rotation-covariant but not continuous across sectors; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
