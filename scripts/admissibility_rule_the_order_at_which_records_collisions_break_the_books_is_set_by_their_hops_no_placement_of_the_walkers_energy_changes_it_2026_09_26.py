#!/usr/bin/env python3
"""Exact checks: the order at which records' collisions break the books is set by their hops; no placement of the walker's
energy changes it - within block 54's walk and blocks 135, 136 and 143 as landed, with blocks 150 and 152 as pushed: for every
finite-range placement of the walker's energy, the total energy current's band-diagonal is the band's energy times its velocity
(for the walk, the two-step momentum in both bands), so the member's momentum at zero transfer is fixed; for walks
h = sum_a sigma_a f(k_a) with one light cone and hops of range R, the momentum equals the offset near every corner through
order N - 1 with N <= R + 2, N = 3 for neighbour hops (the supervisor's own derivation; not adopted).

B (placements): the continuity symbol at first order in the transfer; the symmetric placement, one with an added divergence of a
       hermitian family, and the number density; band-diagonals in both bands; a placement change [h, F] has zero band-diagonal.
D (hop range): exact power-series solves for R = 1..5 (largest N = 3, 3, 5, 5, 7); the matrix-of-powers lemma for m <= 6.
E (the range-three walk): its product form, zeros, speed bound and fifth-order momentum; the fifth-order sum on the shell family.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_ORDER_AT_WHICH_RECORDS_COLLISIONS_BREAK_THE_BOOKS_IS_SET_BY_THEIR_HOPS_NO_PLACEMENT_OF_THE_WALKERS_ENERGY_CHANGES_IT_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_order_at_which_records_collisions_break_the_books_is_set_by_their_hops_no_placement_of_the_walkers_energy_changes_it_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "divergence_not_closed": "B",
    "largest_order_forged": "D",
    "power_lemma_equation_dropped": "D",
    "stencil_coefficient_forged": "E",
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
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIG = (SX, SY, SZ)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its placements and one record per site are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
K = sp.symbols("k1:4", real=True)
Q = sp.symbols("q1:4", real=True)
KP = tuple(K[i] + Q[i] for i in range(3))
ZERO_Q = {Q[0]: 0, Q[1]: 0, Q[2]: 0}


def h_of(kk):
    return sum((SIG[a] * sp.sin(kk[a]) for a in range(3)), sp.zeros(2))


def hop_blocks():
    """Real-space blocks <y|H|z> of the walk whose symbol, in the convention below, is sum_a sigma_a sin k_a."""
    blocks = {}
    for a in range(3):
        e = tuple(1 if i == a else 0 for i in range(3))
        me = tuple(-v for v in e)
        blocks[e] = blocks.get(e, sp.zeros(2)) - SIG[a] / (2 * sp.I)
        blocks[me] = blocks.get(me, sp.zeros(2)) + SIG[a] / (2 * sp.I)
    return blocks


HOPS = hop_blocks()


def h_el(y, z):
    d = tuple(y[i] - z[i] for i in range(3))
    return HOPS.get(d, sp.zeros(2))


def symbol(family0):
    """Symbol A(k + q, k) of the family A_x = T_x A_0 T_x^dag from the blocks of A_0."""
    tot = sp.zeros(2)
    for (y, z), m in family0.items():
        tot += sp.exp(-sp.I * sum(KP[i] * y[i] for i in range(3))) * sp.exp(sp.I * sum(K[i] * z[i] for i in range(3))) * m
    return tot


def near_sites():
    return [(a, b, c) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2)]


def total_current(e_sym, j):
    """First order in q_j of i(h(k+q) e - e h(k)) = -sum_j (1 - e^{-i q_j}) J_j gives J_j(k, k)."""
    lhs = sp.I * (h_of(KP) * e_sym - e_sym * h_of(K))
    c1 = sp.diff(lhs, Q[j]).subs(ZERO_Q)
    return c1 / (-sp.I)


def band_diag(M):
    eps = sp.sqrt(sum(sp.sin(x) ** 2 for x in K))
    out = []
    for s in (1, -1):
        P = (sp.eye(2) + s * h_of(K) / eps) / 2
        val = sp.expand((P * M * P).trace())
        out.append(sp.simplify(sp.simplify(val.rewrite(sp.exp)).rewrite(sp.sin)))
    return out


def family_b(checks: Checks) -> None:
    o = (0, 0, 0)
    e0 = {}
    for y in near_sites():
        for z in near_sites():
            m = sp.zeros(2)
            if y == o:
                m += h_el(o, z) / 2
            if z == o:
                m += h_el(y, o) / 2
            if m != sp.zeros(2):
                e0[(y, z)] = m
    # the number density Pi_0 and its current: the velocity
    n0 = {(o, o): sp.eye(2)}
    ok1 = True
    for j in range(3):
        v = band_diag(total_current(symbol(n0), j))
        E = band_diag(total_current(symbol(e0), j))
        eps2 = sum(sp.sin(x) ** 2 for x in K)
        dE = sp.diff(sp.sqrt(eps2), K[j])
        vel_ok = sp.simplify(v[0] + dE) == 0 and sp.simplify(v[1] - dE) == 0
        target = -sp.sin(K[j]) * sp.cos(K[j])
        en_ok = all(sp.simplify(sp.expand_trig(x - target)) == 0 for x in E)
        ok1 = ok1 and vel_ok and en_ok
    at0 = (symbol(e0).subs(ZERO_Q) - h_of(K)).applyfunc(lambda t: sp.simplify(t.rewrite(sp.exp)))
    checks.check("B1", ok1 and at0 == sp.zeros(2), "symmetric placement e_0 = (Pi_0 H + H Pi_0)/2: its symbol at zero transfer is h(k); the number current's band-diagonal (the velocity) is -dE_b/dk_j in each band, and the energy current's is -sin k_j cos k_j in both bands, E_b times the velocity")
    # add the divergence of a hermitian family G_x: D_0 = G_0 - G_{-e_1}, G_0 = sigma_z Pi_0 H Pi_{e_2} + h.c.
    e2 = (0, 1, 0)
    G0 = {(o, e2): SZ * h_el(o, e2)}
    G0[(e2, o)] = G0[(o, e2)].H
    eD = dict(e0)
    for (y, z), mm in G0.items():
        eD[(y, z)] = eD.get((y, z), sp.zeros(2)) + mm
        if not mut("divergence_not_closed"):
            ys = tuple(y[i] - (1 if i == 0 else 0) for i in range(3))
            zs = tuple(z[i] - (1 if i == 0 else 0) for i in range(3))
            eD[(ys, zs)] = eD.get((ys, zs), sp.zeros(2)) - mm
    sD = symbol(eD)
    sum_ok = (sD.subs(ZERO_Q) - h_of(K)).applyfunc(lambda t: sp.simplify(t.rewrite(sp.exp))) == sp.zeros(2)
    differs = (sD - symbol(e0)).applyfunc(lambda t: sp.simplify(t.rewrite(sp.exp))) != sp.zeros(2)
    ok2 = sum_ok and differs
    for j in range(3):
        if not ok2:
            break
        E = band_diag(total_current(sD, j))
        target = -sp.sin(K[j]) * sp.cos(K[j])
        ok2 = ok2 and all(sp.simplify(sp.expand_trig(x - target)) == 0 for x in E)
    checks.check("B2", ok2, "a different placement (the symmetric one plus the divergence of the hermitian family sigma_z Pi_0 H Pi_{e_2} + h.c.): it still sums to H, its symbol differs, and its total current has the same band-diagonal -sin k_j cos k_j in both bands")
    F = sp.Matrix(2, 2, sp.symbols("f0:4"))
    comm = h_of(K) * F - F * h_of(K)
    zero_diag = all(sp.simplify(x) == 0 for x in band_diag(comm))
    checks.check("B3", zero_diag, "a placement change enters the total current as [h, F] for a 2 x 2 symbol F, and [h, F] has zero diagonal in both bands (block 143 T2, re-checked for a general F)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    d = sp.Symbol("d")
    expected = {1: 3, 2: 3, 3: 5, 4: 5, 5: 7}
    if mut("largest_order_forged"):
        expected[3] = 7
    found = {}
    odd_unique = True
    even_vanish = True
    for R in range(1, 6):
        c = sp.symbols(f"c1:{R + 1}")
        f = sum(c[n - 1] * sp.sin(n * d) for n in range(1, R + 1))
        best, sols = None, None
        for N in range(3, 2 * R + 6, 2):
            eqs = []
            for A in (0, sp.pi):
                g = sp.series(f.subs(d, A + d) * sp.diff(f, d).subs(d, A + d), d, 0, N).removeO()
                poly = sp.Poly(sp.expand(g), d)
                for m in range(N):
                    eqs.append(sp.expand(poly.coeff_monomial(d ** m) - (1 if m == 1 else 0)))
            sol = sp.solve(eqs, c, dict=True)
            if sol:
                best, sols = N, sol
            else:
                break
        found[R] = best
        # classify: solutions with odd harmonics only are unique up to sign; the others vanish at pi/2
        odd_sols = [s for s in sols if all(s.get(c[n - 1], 0) == 0 for n in range(2, R + 1, 2))]
        other = [s for s in sols if s not in odd_sols]
        odd_unique = odd_unique and len(odd_sols) == 2 and all(s[c[0]] != 0 for s in odd_sols)
        for s in other:
            val = f.subs(s).subs(d, sp.pi / 2)
            even_vanish = even_vanish and sp.simplify(val) == 0
    checks.check("D1", found == expected and odd_unique and even_vanish,
                 f"exact power-series solves for f an odd trigonometric polynomial of degree R with f f'(A + d) = d + O(d^N) at both corners: the largest N for R = 1..5 is {[found[R] for R in range(1, 6)]} = [3, 3, 5, 5, 7]; the odd-harmonic solutions are unique up to sign, and every other solution vanishes at pi/2 (a cone off the corners)")
    ok = True
    for m in range(1, 7):
        xs = [sp.Integer((2 * j + 1) ** 2) for j in range(m)]
        rows = [[1] * m] + [[x ** l for x in xs] for l in range(1, m + 1)]
        rhs = [1] + [0] * m
        if mut("power_lemma_equation_dropped"):
            rows, rhs = rows[:-1], rhs[:-1]
        A = sp.Matrix(rows)
        Ab = A.row_join(sp.Matrix(rhs))
        ok = ok and Ab.rank() > A.rank()
        # the even-harmonic and vanishing variants: m unknowns, m homogeneous equations l = 0..m-1 have only the zero solution
        H = sp.Matrix([[x ** l for x in xs] for l in range(m)])
        ok = ok and H.det() != 0
    checks.check("D2", ok, "the matrix-of-powers lemma for m <= 6 with x_j = (2j + 1)^2: sum_j b_j = 1 and sum_j b_j x_j^l = 0 for l = 1..m have no solution, and the homogeneous square system is invertible: an odd stencil of degree 2m - 1 matches d at best through d^(2m-1), and a nonzero one has a Taylor term of order at most 2m - 1")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    k, d, c = sp.symbols("k d c", real=True)
    c3 = -sp.Rational(1, 12) if mut("stencil_coefficient_forged") else -sp.Rational(1, 24)
    f = sp.Rational(9, 8) * sp.sin(k) + c3 * sp.sin(3 * k)
    prod_form = sp.simplify(sp.expand_trig(f - sp.sin(k) * (1 + sp.sin(k) ** 2 / 6))) == 0
    fp = sp.expand_trig(sp.diff(f, k))
    speed = sp.expand(fp.subs(sp.cos(k), c)) if fp.has(sp.cos(k)) else fp
    speed_poly = sp.expand(sp.Rational(3, 2) * c - c ** 3 / 2)
    speed_ok = sp.simplify(fp - (sp.Rational(3, 2) * sp.cos(k) - sp.cos(k) ** 3 / 2)) == 0
    bound_ok = sp.expand(1 - speed_poly ** 2 - (1 - c ** 2) ** 2 * (4 - c ** 2) / 4) == 0
    fifth = True
    for A in (0, sp.pi):
        g = sp.series(f.subs(k, A + d) * sp.diff(f, k).subs(k, A + d), d, 0, 7).removeO()
        fifth = fifth and sp.expand(g - (d - sp.Rational(9, 20) * d ** 5)) == 0
    checks.check("E1", prod_form and speed_ok and bound_ok and fifth,
                 "the range-three walk f = (9/8) sin k - (1/24) sin 3k = sin k (1 + sin^2 k / 6): zeros only where sin k = 0; f' = (3 cos k - cos^3 k)/2 with 1 - f'^2 = (1 - c^2)^2 (4 - c^2)/4 >= 0; f f'(A + d) = d - (9/20) d^5 + O(d^7) at both corners")
    p, x = sp.symbols("p x", real=True)
    s5 = (p / 2 + x) ** 5 + (p / 2 - x) ** 5
    form_ok = sp.expand(s5 - (p ** 5 / 16 + sp.Rational(5, 2) * p ** 3 * x ** 2 + 5 * p * x ** 4)) == 0
    v0 = s5.subs({p: 1, x: 0})
    v1 = s5.subs({p: 1, x: sp.Rational(1, 2)})
    checks.check("E2", form_ok and v0 != v1, f"along block 152's family d1 = (p/2 + x, y, 0), d2 = (p/2 - x, -y, 0) the fifth-order sum is p^5/16 + (5/2) p^3 x^2 + 5 p x^4, not constant on the leading-order shell ({v0} at x = 0 against {v1} at x = 1/2, p = 1)")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 135, 136 and 143 as landed on main (the walk, the energy placement, the momentum that keeps the books, and the band-diagonal of a placement change), with blocks 150 and 152 as pushed; it reports what sets the order at which records' collisions break the books; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at R = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Hellmann", "Feynman", "Vandermonde", "Taylor", "Fourier", "Bloch", "Schwarz", "Liouville",
                   "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Green", "Pauli", "Hamilton", "Wigner", "Riemann", "Hilbert", "Schur", "Fermi", "Peierls", "Kato", "Koszul")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T3 — the hops set the order", "## Theorem T3 — the hops set the order (after Vandermonde)", 1)
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
    "per_element: executed - the continuity symbol at first order in the transfer, for the energy and the number density",
    "per_site: executed - the symmetric placement and one with an added divergence of a hermitian family, symbolically",
    "per_mode: executed - band-diagonals in both bands; a general placement change [h, F] has zero band-diagonal",
    "per_block: executed - exact power-series solves for hop ranges R = 1..5; the matrix-of-powers lemma for m <= 6; the range-three walk",
    "lattice_wide: checked and not executed - every placement and every R by proof; the collision law from block 152 (pushed)",
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
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: block 54's walk; every finite-range energy placement gives the band's energy times its velocity at zero transfer, so no placement changes the records' collision order; for walks h = sum sigma_a f(k_a) with one light cone and hop range R the order is at most R + 2, three for neighbour hops; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
