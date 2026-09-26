#!/usr/bin/env python3
"""Exact checks: moving records at the neutral scale have no long-range order at low density, and long-range order at large
beta and high density - within block 126's static vacancy law as landed (block 39 T5's law with vacancies, block 40's neutral
scale), two-valued menu: at c0 = 1/cosh(beta) the kernel is 1 + t sigma sigma'; for z < 1/320 the contents correlate only inside
occupied clusters, which are dominated by independent occupation at density 64 z; the law is reflection positive through planes
of sites, and given the chessboard estimate and a torus separation lemma the pattern polynomial bounds the contour sum (a harvest
of probe #9260, line-checked by the supervisor; not refereed by another model family; not adopted).

B (the neutral kernel): c0 e^(beta s s') = 1 + tanh(beta) s s'.
C (reflection positivity): on the 4 x 2 torus with the pair on the side of two joined twice, for every configuration of the two
       fixed planes the weight matrix over the two mirror columns is symmetric and rank one, for the neutral kernel and a general one.
D (low density): the occupation bound by basis certificates; cluster decoupling; the path sum; an exact 2 x 2 x 2 torus check.
E (chessboard ratios): all 3^8 cube patterns; the dissemination weights on the 4^3 torus; the ratio bound; the pattern polynomial.
H (the contour sum): the series; the counts of self-avoiding paths and of *-connected sets; the explicit region.
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
    "docs/ADMISSIBILITY_RULE_MOVING_RECORDS_AT_THE_NEUTRAL_SCALE_HAVE_NO_LONG_RANGE_ORDER_AT_LOW_DENSITY_AND_LONG_RANGE_ORDER_AT_LARGE_BETA_AND_HIGH_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_moving_records_at_the_neutral_scale_have_no_long_range_order_at_low_density_and_long_range_order_at_large_beta_and_high_density_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "neutral_kernel_forged": "B",
    "mirror_bond_dropped": "C",
    "occupation_cap_forged": "D",
    "bad_pattern_count_forged": "E",
    "animal_bound_forged": "H",
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


def torus_bonds(dims):
    """One bond per site and direction; on a side of two the pair is joined twice."""
    sites = list(product(*[range(n) for n in dims]))
    bonds = []
    for s in sites:
        for a in range(len(dims)):
            u = tuple((s[i] + (1 if i == a else 0)) % dims[i] for i in range(len(dims)))
            bonds.append((s, u))
    return sites, bonds


def weight(conf, sites, bonds, z, kern):
    w = Fr(1)
    for s in sites:
        if conf[s] != 0:
            w *= z
    for (a, c) in bonds:
        w *= kern(conf[a], conf[c])
    return w


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the law with vacancies, its weights and the menu are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    b = sp.Symbol("beta", positive=True)
    t = sp.tanh(b)
    scale = 1 / sp.cosh(2 * b) if mut("neutral_kernel_forged") else 1 / sp.cosh(b)
    kern = all(sp.simplify((scale * sp.exp(b * s) - (1 + t * s)).rewrite(sp.exp)) == 0 for s in (1, -1))
    checks.check("B1", kern, "at the neutral scale c0 = 1/cosh(beta), c0 e^(beta s s') = 1 + tanh(beta) s s' for s s' = +-1; with an empty end the kernel is 1, so with vacancies it is 1 + t sigma sigma', sigma = n s in {-1, 0, 1}")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    dims = (4, 2)
    sites, bonds = torus_bonds(dims)
    if mut("mirror_bond_dropped"):
        bonds = [bd for bd in bonds if bd != ((0, 0), (1, 0))]
    planes = [(0, 0), (0, 1), (2, 0), (2, 1)]
    col1, col3 = [(1, 0), (1, 1)], [(3, 0), (3, 1)]
    states = list(product((-1, 0, 1), repeat=2))
    cases = [
        ("neutral t = 1/2, z = 3", Fr(3), lambda u, v: Fr(1) if u == 0 or v == 0 else 1 + Fr(1, 2) * u * v),
        ("general c e^(beta) = 3, c e^(-beta) = 1/5, z = 1/7", Fr(1, 7), lambda u, v: Fr(1) if u == 0 or v == 0 else (Fr(3) if u == v else Fr(1, 5))),
    ]
    ok = True
    for _, z, kern in cases:
        for pc in product((-1, 0, 1), repeat=4):
            base = dict(zip(planes, pc))
            mat = []
            for a in states:
                row = []
                for c in states:
                    conf = dict(base)
                    conf.update(zip(col1, a))
                    conf.update(zip(col3, c))
                    row.append(weight(conf, sites, bonds, z, kern))
                mat.append(row)
            m = sp.Matrix(mat)
            ok = ok and m == m.T and m.rank() == 1 and all(m[i, i] > 0 for i in range(len(states)))
    checks.check("C1", ok, "reflection through the plane of sites x = 0 (also fixing x = 2) on the 4 x 2 torus with the pair on the side of two joined twice: for all 81 configurations of the fixed planes, the weight matrix over the two mirror columns (9 x 9) is symmetric and rank one with a positive diagonal, for the neutral kernel and for a general c, beta, z; so E[F theta(F)] is a sum of squares (exact)")


# ============================================================================================ family D
def bernstein_nonneg(poly, var, deg):
    p = sp.Poly(sp.expand(poly), var)
    a = [p.coeff_monomial(var ** i) for i in range(deg + 1)]
    coef = [sum(sp.binomial(j, i) / sp.binomial(deg, i) * a[i] for i in range(j + 1)) for j in range(deg + 1)]
    return all(c >= 0 for c in coef)


def family_d(checks: Checks) -> None:
    tt = sp.Symbol("t")
    cap = 32 if mut("occupation_cap_forged") else 64
    occ_ok = True
    for k in range(7):
        for l in range(7 - k):
            S = (1 + tt) ** k * (1 - tt) ** l + (1 - tt) ** k * (1 + tt) ** l
            occ_ok = occ_ok and bernstein_nonneg((1 + tt) ** 6 + (1 - tt) ** 6 - S, tt, 6)
    occ_ok = occ_ok and bernstein_nonneg(cap - (1 + tt) ** 6 - (1 - tt) ** 6, tt, 6)
    checks.check("D1", occ_ok, f"for every k + l <= 6 occupied neighbour ends, S = (1+t)^k (1-t)^l + (1-t)^k (1+t)^l <= (1+t)^6 + (1-t)^6 <= {cap} on [0, 1] (nonnegative basis coefficients): P(x occupied | rest) = zS/(1 + zS) <= 64 z")

    def corr(adj, i, j, tv):
        num = Fr(0)
        den = Fr(0)
        n = 1 + max(max(e) for e in adj)
        for cfg in product((-1, 1), repeat=n):
            w = Fr(1)
            for (a, c) in adj:
                w *= 1 + tv * cfg[a] * cfg[c]
            den += w
            num += w * cfg[i] * cfg[j]
        return num / den
    dec = corr([(0, 1), (2, 3)], 0, 3, Fr(1, 3)) == 0 and corr([(0, 1), (2, 3)], 0, 1, Fr(1, 3)) == Fr(1, 3)
    p = sp.Symbol("p", positive=True)
    nn = 12
    partial = sum(6 * 5 ** (k - 1) * p ** (k + 1) for k in range(1, nn + 1))
    path_sum = sp.expand((1 - 5 * p) * partial - 6 * p ** 2 * (1 - (5 * p) ** nn)) == 0
    checks.check("D2", dec and path_sum, "given the occupied set, contents decouple across clusters (<s0 s3> = 0 across two clusters, <s0 s1> = t inside one); the path sum p + sum_n 6 5^(n-1) p^(n+1) = p + 6 p^2/(1 - 5p) for p < 1/5")

    # the whole statement on the 2 x 2 x 2 torus (bonds joined twice), exactly
    sites, bonds = torus_bonds((2, 2, 2))
    o = (0, 0, 0)
    ok = True
    for z, t in ((Fr(1, 400), Fr(9, 10)), (Fr(1, 330), Fr(1, 2))):
        kern = (lambda tv: (lambda u, v: 1 + tv * u * v))(t)
        Z = Fr(0)
        S = Fr(0)
        for cfg in product((-1, 0, 1), repeat=len(sites)):
            conf = dict(zip(sites, cfg))
            w = weight(conf, sites, bonds, z, kern)
            Z += w
            S += w * conf[o] * sum(conf.values())
        pv = 64 * z
        ok = ok and S / Z <= pv + 6 * pv ** 2 / (1 - 5 * pv)
    checks.check("D3", ok, "on the 2 x 2 x 2 torus with the pairs joined twice, exactly at (z, t) = (1/400, 9/10) and (1/330, 1/2): sum_x <sigma_0 sigma_x> <= p + 6p^2/(1 - 5p), p = 64 z")


# ============================================================================================ family E
def family_e(checks: Checks):
    cube = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    edges = [(u, v) for u in cube for v in cube if u < v and sum(abs(p1 - p2) for p1, p2 in zip(u, v)) == 1]
    A, U = sp.symbols("A U", positive=True)
    points = ((Fr(1, 3), Fr(5)), (Fr(9, 10), Fr(1, 7)))
    poly = sp.Integer(0)
    nbad = 0
    ratio_ok = True
    for tau in product((-1, 0, 1), repeat=8):
        pat = dict(zip(cube, tau))
        V = sum(1 for s in tau if s == 0)
        m = sum(1 for (u, v) in edges if pat[u] * pat[v] == -1)
        k = sum(1 for (u, v) in edges if pat[u] == 0 or pat[v] == 0)
        for t0, z0 in points:
            # each cube edge occurs twice per 2 x 2 x 2 cell of the disseminated configuration
            w_direct = z0 ** (8 - V)
            for (u, v) in edges:
                w_direct *= (1 + t0 * pat[u] * pat[v]) ** 2
            w_formula = z0 ** (8 - V) * (1 - t0) ** (2 * m) * (1 + t0) ** (2 * (12 - m - k))
            w_plus = z0 ** 8 * (1 + t0) ** 24
            # the eighth power of A^V U^m is z^(-V) ((1 - t)/(1 + t))^(2m)
            ratio_ok = ratio_ok and w_direct == w_formula and w_direct / w_plus <= z0 ** (-V) * ((1 - t0) / (1 + t0)) ** (2 * m)
        good = all(s == 1 for s in tau) or all(s == -1 for s in tau)
        if mut("bad_pattern_count_forged") and all(s == 0 for s in tau):
            good = True
        if good:
            continue
        nbad += 1
        poly += A ** V * U ** m
    L = 4
    tor, tbonds = torus_bonds((L, L, L))
    diss_ok = True
    t0, z0 = Fr(1, 3), Fr(5)
    kern0 = lambda u, v: 1 + t0 * u * v
    for tau in [(1,) * 8, (1, 1, 1, 1, 1, 1, 1, -1), (0, 1, -1, 1, 0, 0, 1, -1), (1, -1, -1, 1, -1, 1, 1, -1), (0, 0, 0, 0, 0, 0, 0, 1)]:
        pat = dict(zip(cube, tau))
        conf = {s: pat[(s[0] % 2, s[1] % 2, s[2] % 2)] for s in tor}
        V = sum(1 for s in tau if s == 0)
        m = sum(1 for (u, v) in edges if pat[u] * pat[v] == -1)
        k = sum(1 for (u, v) in edges if pat[u] == 0 or pat[v] == 0)
        w_cell = z0 ** (8 - V) * (1 - t0) ** (2 * m) * (1 + t0) ** (2 * (12 - m - k))
        diss_ok = diss_ok and weight(conf, tor, tbonds, z0, kern0) == w_cell ** (len(tor) // 8)
    P = sp.Poly(poly, A, U)
    lead_ok = (P.coeff_monomial(A) == 16 and P.coeff_monomial(U ** 3) == 16 and P.coeff_monomial(A * U ** 2) == 48
               and P.coeff_monomial(A ** 2) == 56 and P.coeff_monomial(U ** 4) == 30 and all(c > 0 for c in P.coeffs()))
    checks.check("E1", ratio_ok and diss_ok, "for all 3^8 cube patterns at (t, z) = (1/3, 5) and (9/10, 1/7): the cell weight is z^(8-V) (1 - t)^(2m) (1 + t)^(2(12-m-k)) (V empty sites, m opposite edges, k edges at an empty site) and w_tau/w_+ <= z^(-V) ((1 - t)/(1 + t))^(2m), the eighth power of A^V U^m; the 2-periodic dissemination on the 4^3 torus has weight w_tau^(N/8) exactly (five patterns)")
    checks.check("E2", nbad == 6559 and lead_ok and len(P.terms()) == 42,
                 f"all 3^8 patterns of the 2 x 2 x 2 cube: {nbad} bad ones; the pattern polynomial P(A, U) = 16A + 16U^3 + 48AU^2 + 56A^2 + 30U^4 + ... has 42 terms, all with positive coefficients (so it grows with A and U)")
    return poly, A, U


# ============================================================================================ family H
def family_h(checks: Checks, poly, A, U) -> None:
    x = sp.Symbol("x")
    nn = 12
    partial = sum(k * x ** (k - 1) for k in range(1, nn + 1))
    series = sp.expand((1 - x) ** 2 * partial - (1 - (nn + 1) * x ** nn + nn * x ** (nn + 1))) == 0
    eps = poly.subs({A: sp.Rational(1, 10 ** 5), U: sp.Rational(1, 100)})
    bound = 1 - 2 * (2 * eps + 2 * eps / (1 - 676 * eps) ** 2)
    checks.check("H1", series and eps <= sp.Rational(1, 2704) and bound > sp.Rational(998, 1000),
                 "sum_n n x^(n-1) = 1/(1 - x)^2, so the contour sum is 2 eps/(1 - 676 eps)^2; at A = 10^-5, U = 10^-2 (z >= 10^40, 1 - tanh(beta) <= 10^-8) eps <= 1/2704 and 1 - 2[2 eps + 2 eps/(1 - 676 eps)^2] > 998/1000")
    steps = [d for d in product((-1, 0, 1), repeat=3) if sum(abs(c) for c in d) == 1]
    star = [d for d in product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]

    def add(a, b):
        return tuple(p + q for p, q in zip(a, b))
    o = (0, 0, 0)
    walks = [[o]]
    saw_ok = True
    for n in range(1, 6):
        walks = [w + [add(w[-1], d)] for w in walks for d in steps if add(w[-1], d) not in w]
        saw_ok = saw_ok and len(walks) <= 6 * 5 ** (n - 1)
    level = {frozenset([o])}
    animal_ok = True
    for n in range(2, 4):
        grown = set()
        for S in level:
            for s in S:
                for d in star:
                    u = add(s, d)
                    if u not in S:
                        grown.add(S | {u})
        level = grown
        cap = 26 ** (n - 1) if mut("animal_bound_forged") else 26 ** (2 * (n - 1))
        animal_ok = animal_ok and len(level) <= cap
    checks.check("H2", saw_ok and animal_ok, "counts on Z^3: self-avoiding paths of n <= 5 steps number at most 6 5^(n-1); *-connected sets of n <= 3 cubes through a given cube number at most 26^(2(n-1)) = 676^(n-1) (there are 26 and 711)")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 39, 40 and 126 as landed on main (the law with vacancies, its neutral scale and the static vacancy law's open question); it reports whether that law has long-range order at the neutral scale for the two-valued menu; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at z = 1/320."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Ising", "Peierls", "Fröhlich", "Frohlich", "Israel", "Lieb", "Simon", "Biskup", "Deuschel", "Pisztora", "Timár", "Timar",
                   "Bernstein", "Griffiths", "Dobrushin", "Holley", "Liggett", "Schwarz", "Liouville", "Fourier", "Taylor", "Green", "Pauli", "Hamilton", "Gauss", "Einstein", "Planck",
                   "Euler", "Laplace", "Poisson", "Cauchy", "Riemann", "Hilbert", "Schur", "Fermi", "Bloch", "Wigner", "Legendre", "Rodrigues", "Spencer")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 — no long-range order at low density", "## Theorem T1 — no long-range order at low density (after Peierls)", 1)
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
    "per_element: executed - the neutral kernel c0 e^(beta s s') = 1 + t s s' symbolically",
    "per_site: executed - the occupation bound for every neighbourhood of k + l <= 6 occupied ends, by basis certificates",
    "per_mode: executed - cluster decoupling, the path sum, and the exact 2 x 2 x 2 torus check of the low-density bound",
    "per_block: executed - reflection positivity on the 4 x 2 torus for every plane configuration; all 3^8 cube patterns; dissemination weights on the 4^3 torus",
    "lattice_wide: checked and not executed - every even torus by proof; T2 given the chessboard estimate and the torus separation lemma (premises A1, A2)",
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
    poly, A, U = family_e(checks)
    family_h(checks, poly, A, U)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: block 126's static vacancy law, two-valued menu, at the neutral scale; no long-range order for z < 1/320 at every beta (exact); long-range order at large beta and high density given the chessboard estimate and the torus separation lemma; harvest of probe #9260, line-checked by the supervisor, unrefereed by another family; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
