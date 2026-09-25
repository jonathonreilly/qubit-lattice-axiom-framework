#!/usr/bin/env python3
"""Exact checks: under one record per site the a-term's levels are frozen or out of reach - in block 77's family the middle
half filling has N records after half of the zero-level space, the windows above it need more records than sites, and at one record per site
every composition's generator is a constant; the specified compressed hopping norm is bounded by hole number (a harvest block from a Grok-refereed probes attempt;
blocks 77 and 78 as landed; the hard-core compression supplied; not adopted).

B (T1): exact band counts on even tori, the odd contrast, and the stagger identities on 4^3.
C (T2): the full ring under both compositions.
D (T3): the hole bound and the thin window.
E (T4): the sense-weighted moments of the eight corners.
Exact arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_A_TERMS_LEVELS_ARE_FROZEN_OR_OUT_OF_REACH_THE_MIDDLE_LEVEL_IS_ONE_RECORD_PER_SITE_AND_A_FULL_LATTICE_HAS_A_CONSTANT_GENERATOR_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_one_record_per_site_the_a_terms_levels_are_frozen_or_out_of_reach_the_middle_level_is_one_record_per_site_and_a_full_lattice_has_a_constant_generator_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Records form.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "count_forged": "B",
    "full_generator_forged": "C",
    "hole_bound_forged": "D",
    "chiral_moment_forged": "E",
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
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: a site never carries more than one record (the premise of the hard-core compression); records form; Admissibility is not a dynamics axiom (the family, the stagger and the composition are supplied)")


# ============================================================================================ block 77's family on even tori
A0, AA, MM = sp.symbols("a0 a m", real=True)
PARAMS = ((Fraction(1, 3), Fraction(1, 10)), (Fraction(0), Fraction(1, 4)), (Fraction(-2, 5), Fraction(2, 3)))


def sign_r_s_sqrt(r, s, q):
    """exact sign of r + s*sqrt(q) for rationals r, s and q >= 0."""
    if q == 0 or s == 0:
        return (r > 0) - (r < 0)
    t = s * s * q
    if r >= 0 and s > 0:
        return 1
    if r <= 0 and s < 0:
        return -1
    if r > 0:
        return (r * r > t) - (r * r < t)
    return (t > r * r) - (t < r * r)


def trig_tables(ll):
    """exact cos(2 pi n/L) and sin^2(2 pi n/L) for L in {3, 4, 6, 12}."""
    cs, s2 = [], []
    for n in range(ll):
        c = sp.nsimplify(sp.cos(2 * sp.pi * n / ll))
        cs.append(Fraction(int(sp.fraction(c)[0]), int(sp.fraction(c)[1])) if c.is_rational else None)
        s = sp.nsimplify(sp.sin(2 * sp.pi * n / ll) ** 2)
        s2.append(Fraction(int(sp.fraction(s)[0]), int(sp.fraction(s)[1])))
    return cs, s2


def band_signs(ll, a, shift):
    """signs of E - a0 - shift over both bands and all k of the L^3 torus, E - a0 = 2a sum cos k +/- |sin k| (block 77)."""
    cs, s2 = trig_tables(ll)
    out = []
    for n in product(range(ll), repeat=3):
        c = sum(cs[i] for i in n)
        q = sum(s2[i] for i in n)
        r = 2 * a * c - shift
        out.append(sign_r_s_sqrt(r, Fraction(1), q))
        out.append(sign_r_s_sqrt(r, Fraction(-1), q))
    return out


def torus_ops(ll):
    """sparse A = 2a sum C_j + sum sigma_j S_j, the stagger eps and T_1 on the L^3 torus with a two-state coin."""
    idx = {}
    for x in product(range(ll), repeat=3):
        for c in range(2):
            idx[(x, c)] = len(idx)
    dim = len(idx)
    sig = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    amat, eps, t1 = {}, {}, {}
    for x in product(range(ll), repeat=3):
        for c in range(2):
            eps[(idx[(x, c)], idx[(x, c)])] = (-1) ** sum(x)
        for j in range(3):
            y = list(x)
            y[j] = (y[j] + 1) % ll
            y = tuple(y)
            fwd = AA * sp.eye(2) + sig[j] / (2 * sp.I)
            for c in range(2):
                for d in range(2):
                    if fwd[c, d] != 0:
                        k1, k2 = (idx[(x, c)], idx[(y, d)]), (idx[(y, d)], idx[(x, c)])
                        amat[k1] = amat.get(k1, 0) + fwd[c, d]
                        amat[k2] = amat.get(k2, 0) + sp.conjugate(fwd[c, d])
            if j == 0:
                for c in range(2):
                    t1[(idx[(x, c)], idx[(y, c)])] = 1
    return sp.SparseMatrix(dim, dim, amat), sp.SparseMatrix(dim, dim, eps), sp.SparseMatrix(dim, dim, t1)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the a-term's middle level is one record per site; the windows beyond it are more or fewer than N."""
    ok_counts = True
    rows = []
    for ll in (4, 6):
        nn = ll ** 3
        for a0, a in PARAMS:
            sg = band_signs(ll, a, Fraction(0))
            below, zero = sg.count(-1), sg.count(0)
            want = nn - zero // 2
            if mut("count_forged"):
                want = nn - zero
            up = band_signs(ll, a, 2 * a)
            below_up = up.count(-1) + up.count(0)
            dn = band_signs(ll, a, -2 * a)
            below_dn = dn.count(-1)
            ok_counts = ok_counts and zero % 2 == 0 and below == want and below_up >= nn + 6 + zero // 2 and below_dn <= nn - 6 - zero // 2
            rows.append((ll, below, zero))
    odd = band_signs(3, Fraction(1, 10), Fraction(0))
    ok_odd = odd.count(-1) == 26 and odd.count(0) == 0
    amat, eps, t1 = torus_ops(4)
    anti = (eps * amat + amat * eps).is_zero_matrix
    am = amat + MM * eps
    sq = (am * am - amat * amat - MM ** 2 * sp.SparseMatrix(sp.eye(amat.shape[0]))).applyfunc(sp.expand).is_zero_matrix
    xx = eps * t1
    anti2 = (xx * am + am * xx).applyfunc(sp.expand).is_zero_matrix
    no_site = all(amat[i, i] == 0 for i in range(amat.shape[0]))
    checks.check("B1", ok_counts and ok_odd and anti and sq and anti2 and no_site,
                 f"T1: on the 4^3 and 6^3 tori, for (a0, a) = (1/3, 1/10), (0, 1/4), (-2/5, 2/3), exactly N - z/2 one-record states lie below a0 (z = #(E = a0), even), at least N + 6 + z/2 lie at or below a0 + 2a and at most N - 6 - z/2 below a0 - 2a ({rows[:2]} ...); the odd 3^3 torus gives 26 of 54 (even sides are needed); on 4^3 the stagger anticommutes with A (no on-site part), (A + m eps)^2 = A^2 + m^2 and eps T_1 anticommutes with A + m eps, so with m != 0 exactly N states lie below a0 and none within |m| of it")


# ============================================================================================ hard-core many-record generator on a ring
def ring_generator(ll, nrec, a0, a, m, sign):
    """compressed many-record generator of the family's one-axis member a0 + 2a C + sigma_1 S on a ring of ll sites, with
    nrec records at most one per site, each with a two-state coin; sign = -1 (antisymmetric) or +1 (symmetric composition)."""
    fwd = [[a, Fraction(0)], [Fraction(0), a]]
    configs = []
    for occ in combinations(range(ll), nrec):
        for coins in product(range(2), repeat=nrec):
            configs.append((occ, coins))
    index = {cfg: i for i, cfg in enumerate(configs)}
    dim = len(configs)
    mat = {}

    def add(i, j, v):
        if v != (0, 0):
            o = mat.get((i, j), (Fraction(0), Fraction(0)))
            mat[(i, j)] = (o[0] + v[0], o[1] + v[1])
    half_i = (Fraction(0), Fraction(-1, 2))
    for (occ, coins), i in index.items():
        diag = sum(a0 + m * (-1) ** x for x in occ)
        add(i, i, (diag, Fraction(0)))
        for r, x in enumerate(occ):
            for step in (1, -1):
                y = (x + step) % ll
                if y in occ:
                    continue
                passed = sum(1 for z in occ if z != x and (min(x, y) < z < max(x, y)))
                sg = sign ** passed
                for d in range(2):
                    c = coins[r]
                    re = fwd[d][c]
                    im = half_i[1] if d != c else Fraction(0)
                    if step == -1:
                        im = -im
                    rest = [coins[s] for s in range(nrec) if s != r]
                    pos = [z for z in occ if z != x]
                    pairs = sorted(list(zip(pos, rest)) + [(y, d)])
                    j = index[(tuple(p for p, _ in pairs), tuple(q for _, q in pairs))]
                    add(j, i, (sg * re, sg * im))
    return dim, mat


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: at one record per site every composition's generator is the constant N a0."""
    a0, a, m = Fraction(1, 3), Fraction(1, 10), Fraction(1, 3)
    ok = True
    for sign in (-1, 1):
        dim, mat = ring_generator(4, 4, a0, a, m, sign)
        offd = [k for k, v in mat.items() if k[0] != k[1] and v != (0, 0)]
        diag_ok = all(mat.get((i, i), (0, 0)) == (4 * a0, Fraction(0)) for i in range(dim))
        if mut("full_generator_forged"):
            diag_ok = diag_ok and len(offd) > 0
        ok = ok and dim == 16 and not offd and diag_ok
        dim3, mat3 = ring_generator(4, 3, a0, a, m, sign)
        herm = all(mat3.get((j, i), (0, 0)) == (v[0], -v[1]) for (i, j), v in mat3.items())
        moving = any(k[0] != k[1] and v != (0, 0) for k, v in mat3.items())
        ok = ok and herm and moving
    checks.check("C1", ok,
                 "T2: with four records on block 78's ring of four (a0, a, m) = (1/3, 1/10, 1/3), the compressed generator of both compositions (antisymmetric and symmetric) is exactly 4 a0 times the identity on all 16 coin configurations (every hop lands on an occupied site; the stagger sums to zero on an even ring), while with three records it is hermitian and moves the hole")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: near one record per site only holes move, and the window below a0 - 2a is thin for small a."""
    sig = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    colsum = []
    for j in range(3):
        hop = AA * sp.eye(2) + sig[j] / (2 * sp.I)
        colsum.append([sp.simplify(sum(sp.Abs(hop[r, c]) for r in range(2)).subs(AA, sp.Rational(1, 10))) for c in range(2)])
    bound1 = sp.Rational(1, 10) + sp.Rational(1, 2)
    ok_cols = colsum[0] == [bound1, bound1] and colsum[1] == [bound1, bound1] and all(sp.simplify(v - sp.sqrt(sp.Rational(1, 100) + sp.Rational(1, 4))) == 0 for v in colsum[2]) and sp.sqrt(sp.Rational(26, 100)) < bound1
    a0, a, m = Fraction(1, 3), Fraction(1, 10), Fraction(1, 3)
    ok_rows = True
    for nh in (1, 2):
        for sign in (-1, 1):
            dim, mat = ring_generator(6, 6 - nh, a0, a, m, sign)
            herm = all(mat.get((j, i), (0, 0)) == (v[0], -v[1]) for (i, j), v in mat.items())
            rows = [Fraction(0)] * dim
            for (i, j), v in mat.items():
                if i != j:
                    mod2 = v[0] * v[0] + v[1] * v[1]
                    rows[i] += a if mod2 == a * a else Fraction(1, 2)
                    ok_rows = ok_rows and mod2 in (a * a, Fraction(1, 4))
            bound = 2 * (a + Fraction(1, 2)) * nh
            if mut("hole_bound_forged"):
                bound = 2 * a * nh
            ok_rows = ok_rows and herm and max(rows) <= bound
    cs12, s212 = trig_tables(12)
    thin = sum(1 for n in product(range(12), repeat=3) if sum(s212[i] for i in n) < Fraction(9, 25))
    aa = Fraction(1, 20)
    sg_mu = band_signs(6, aa, -4 * aa)
    holes = 216 - sg_mu.count(-1)
    sg0 = band_signs(6, aa, Fraction(0))
    sg6 = band_signs(6, aa, -6 * aa)
    inside = sum(1 for u, v in zip(sg0, sg6) if u == -1 and v == 1)
    ok_thin = thin == 56 and holes <= sg0.count(0) // 2 + inside
    checks.check("D1", ok_cols and ok_rows and ok_thin,
                 f"T3: a hop a 1 +/- sigma_j/(2i) has column sums |a| + 1/2 for sigma_1, sigma_2 and sqrt(a^2 + 1/4) <= |a| + 1/2 for sigma_3, so with N_h holes the moving part has norm at most 6(|a| + 1/2) N_h (two hops per hole on a ring: every row sum at most 2(|a| + 1/2) N_h, exact on the ring of six with one and two holes, both compositions, hermitian); the window |E - a0| < 6a needs |sin k| < 12a: {thin} of the 1728 momenta of 12^3 at a = 1/20, and on 6^3 at mu = a0 - 4a the holes number {holes}, within the bound z/2 + #(a0 - 6a < E < a0) = {sg0.count(0) // 2 + inside}")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the net sense of the corners' levels, moment by moment."""
    s = sp.symbols("s1:4")
    moments = []
    for pw in range(4):
        tot = 0
        for n in product((0, 1), repeat=3):
            chi = (-1) ** sum(n)
            lev = A0 + 2 * AA * (3 - 2 * sum(n))
            tot += chi * lev ** pw
        moments.append(sp.expand(tot))
    want = [0, 0, 0, 384 * AA ** 3]
    if mut("chiral_moment_forged"):
        want[3] = 192 * AA ** 3
    mult = [sum(1 for n in product((0, 1), repeat=3) if sum(n) == k) for k in range(4)]
    checks.check("E1", moments == want and mult == [1, 3, 3, 1],
                 "T4: the eight corners carry levels a0 + 2a(3 - 2|n|) with multiplicities 1:3:3:1 and senses (-1)^|n| (block 77 T1); the sense-weighted moments sum chi_n L_n^p vanish for p = 0, 1, 2 and equal 384 a^3 at p = 3, for every a0: these moments concern free corners only, not interacting excitation content")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 77 and 78 as landed on main, with block 77's supplied family and staggered sign and block 78's hard-core compression extended to many records; it reports where the family's levels sit in record number and what one record per site does there; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Fermi", "Gershgorin", "Nielsen", "Ninomiya", "Hooft", "Chern", "Lifshitz", "Mott", "Hubbard", "Lieb", "Pauli", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the stagger against A, (A + m eps)^2 = A^2 + m^2 and eps T_1 against A + m eps on every basis vector of the 4^3 torus, with symbolic a and m",
    "per_site: executed - the full ring of four under both compositions; the hole-moving generator's hermiticity and row sums on the ring of six with one and two holes",
    "per_mode: executed - exact band counts on 4^3 and 6^3 for three parameter pairs and on the odd 3^3; the thin window on 12^3",
    "per_block: executed - the sense-weighted moments of the eight corners; the hole count against its bound on 6^3",
    "lattice_wide: T1 on even tori (as a density in infinite volume); T2 on every even torus; T3's norm bound on even tori and its window bound for a < 1/12; the family, the stagger and the compression supplied; the interacting gas's senses not treated",
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
    print('scope: Free filling bound and scalar compression; no interacting no-mobile or chiral classification. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
