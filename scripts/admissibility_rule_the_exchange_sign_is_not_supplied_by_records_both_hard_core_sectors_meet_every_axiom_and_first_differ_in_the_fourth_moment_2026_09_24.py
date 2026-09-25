#!/usr/bin/env python3
"""Exact checks: the exchange sign is not supplied by records - the symmetric and antisymmetric hard-core sectors both preserve the specified exclusion and covariance, are closed under the walk and preserve explicitly permutation-invariant observables without proving equal restrictions; they first differ in the fourth
moment, by -8 per plaquette on Z^2 and Z^3; on even rings at order N, equal spectra on specified odd rings; a record's content has no
parity (a harvest block from a Grok-refereed probes attempt; blocks 54 and 78 as landed; not adopted).

B (T1): the two composition rules on the ring of four.
C (T2): the exchange amplitude on Z^2 and Z^3 at orders 2, 3 and 4.
D (T3): rings - order N on even rings, unitary equivalence on odd rings.
E (T4): the grading and the discrete exchange rotation.
Exact arithmetic only (Gaussian integers); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_EXCHANGE_SIGN_IS_NOT_SUPPLIED_BY_RECORDS_BOTH_HARD_CORE_SECTORS_MEET_EVERY_AXIOM_AND_FIRST_DIFFER_IN_THE_FOURTH_MOMENT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "A readout value is determined by record content alone.",
    "The full one-site possibility domain has algebraic presentation",
    "A choice not fixed by the supplied structure remains a named conditional or open dependency.",
)

MUTATION_GATE = {
    "sector_not_closed": "B",
    "plaquette_value_forged": "C",
    "odd_ring_unitary_forged": "D",
    "grading_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: one record per site and permanence (the hard-core space); readout by content alone (readouts commute with the exchange); the one-site domain M_2(C); a choice not fixed by the supplied structure remains a named conditional (the exchange sign)")


# ============================================================================================ Gaussian integers and the walk's hops
def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


ZERO, ONE, IU = (0, 0), (1, 0), (0, 1)
PAULI = (((ZERO, ONE), (ONE, ZERO)), ((ZERO, (0, -1)), ((0, 1), ZERO)), ((ONE, ZERO), (ZERO, (-1, 0))))


def hop_list(dim, axes, ring=None):
    """the moves of 2H = sum_a sigma_a (-i)(T_a - T_a^dagger) for one record: (displacement, coin matrix to apply);
    moving by +e_a carries +i sigma_a, by -e_a carries -i sigma_a."""
    out = []
    for a in axes:
        e = tuple(1 if t == a else 0 for t in range(dim))
        me = tuple(-v for v in e)
        sig = PAULI[a] if ring is None else PAULI[2]
        plus = tuple(tuple(gmul(IU, sig[c][d]) for d in range(2)) for c in range(2))
        minus = tuple(tuple(gmul((0, -1), sig[c][d]) for d in range(2)) for c in range(2))
        out.append((e, plus))
        out.append((me, minus))
    return out


def apply_h2(vec, moves, wrap=None):
    """apply the compressed two-record 2H_2 to a sparse vector over (x, a, y, b) with x != y."""
    out = {}
    for (x, a, y, b), amp in vec.items():
        for rec in (0, 1):
            pos, coin, other = (x, a, y) if rec == 0 else (y, b, x)
            for disp, mat in moves:
                new = tuple(pos[t] + disp[t] for t in range(len(pos)))
                if wrap is not None:
                    new = tuple(v % wrap for v in new)
                if new == other:
                    continue
                for c in range(2):
                    m = mat[c][coin]
                    if m == ZERO:
                        continue
                    key = (new, c, y, b) if rec == 0 else (x, a, new, c)
                    out[key] = gadd(out.get(key, ZERO), gmul(m, amp))
    return {k: v for k, v in out.items() if v != ZERO}


def exchange_amplitude(y, moves, order, dim):
    """sum over coins of <P s | (2H_2)^order | s> for s = (0, a; y, b) on the infinite lattice."""
    o = tuple([0] * dim)
    tot = ZERO
    for a in range(2):
        for b in range(2):
            vec = {(o, a, y, b): ONE}
            for _ in range(order):
                vec = apply_h2(vec, moves)
            tot = gadd(tot, vec.get((y, b, o, a), ZERO))
    return tot


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: two composition rules, both closed, both covariant, both invisible to content readouts."""
    n = 4
    moves = hop_list(1, (0,), ring=True)
    basis = [((x,), a, (y,), b) for x in range(n) for y in range(n) if x != y for a in range(2) for b in range(2)]
    ok_dim = len(basis) == 4 * n * (n - 1)
    ok_comm = True
    for s in basis:
        hs = apply_h2({s: ONE}, moves, wrap=n)
        ps = (s[2], s[3], s[0], s[1])
        hps = apply_h2({ps: ONE}, moves, wrap=n)
        swapped = {(k[2], k[3], k[0], k[1]): v for k, v in hs.items()}
        if mut("sector_not_closed"):
            swapped = {(k[2], k[3], k[0], k[1]): (v if k[0] < k[2] else gmul((-1, 0), v)) for k, v in hs.items()}
        ok_comm = ok_comm and swapped == hps and all(k[0] != k[2] for k in hs)
    herm = True
    for s in basis:
        hs = apply_h2({s: ONE}, moves, wrap=n)
        for t, v in hs.items():
            back = apply_h2({t: ONE}, moves, wrap=n).get(s, ZERO)
            herm = herm and back == (v[0], -v[1])
    sym = {}
    for s in basis:
        k = tuple(sorted([(s[0], s[1]), (s[2], s[3])]))
        sym[k] = sym.get(k, 0) + 1
    ok_sectors = len(sym) == 2 * n * (n - 1) and all(v == 2 for v in sym.values())
    checks.check("B1", ok_dim and ok_comm and herm and ok_sectors,
                 "T1: on block 78's ring of four with its reduced walk, the hard-core two-record space HC (dimension 4n(n-1) = 48) is closed under the compressed generator, which is hermitian and commutes exactly with the exchange P on every basis vector; so the symmetric and antisymmetric parts of HC (each of dimension 2n(n-1)) are two composition rules, each closed under the walk and each with one record per site")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: where the sign shows - the fourth moment, -8 per plaquette."""
    res = {}
    for dim in (2, 3):
        moves = hop_list(dim, tuple(range(dim)))
        seps = [y for y in product(range(-2, 3), repeat=dim) if 0 < sum(abs(v) for v in y) <= 2]
        per_order = {}
        for order in (2, 3, 4):
            per_order[order] = [exchange_amplitude(y, moves, order, dim) for y in seps]
        res[dim] = (seps, per_order)
    ok_low = all(v == ZERO for dim in (2, 3) for order in (2, 3) for v in res[dim][1][order])
    tot2 = (sum(v[0] for v in res[2][1][4]), sum(v[1] for v in res[2][1][4]))
    tot3 = (sum(v[0] for v in res[3][1][4]), sum(v[1] for v in res[3][1][4]))
    want2, want3 = (-128, 0), (-384, 0)
    if mut("plaquette_value_forged"):
        want3 = (-192, 0)
    seps3, amps3 = res[3][0], res[3][1][4]
    per_pair = {}
    for y, v in zip(seps3, amps3):
        kind = "nbr" if sum(abs(t) for t in y) == 1 else ("diag" if max(abs(t) for t in y) == 1 else "line")
        per_pair.setdefault(kind, set()).add(v)
    ok_pairs = per_pair == {"nbr": {(-32, 0)}, "diag": {(-16, 0)}, "line": {(0, 0)}}
    checks.check("C1", ok_low and tot2 == want2 and tot3 == want3 and ok_pairs,
                 "T2: on the infinite lattices Z^2 and Z^3 the coin-summed exchange amplitude <Ps|(2H_2)^k|s> of two records vanishes at orders k = 2, 3 for every separation, and at order 4 sums to -128 per site on Z^2 and -384 per site on Z^3, i.e. tr(P H_2^4) = -8 per plaquette (-8 per site on Z^2, -24 on Z^3); per pair on Z^3 it is -32/16 = -2 for neighbours, -16/16 = -1 on a face diagonal and 0 at distance 2 on a line")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: rings - the sign shows at order N on even rings and never on odd ones."""
    moves = hop_list(1, (0,), ring=True)
    ok_even = True
    want = {4: (128, 0), 6: (-1248, 0), 8: (7680, 0)}
    for n in (4, 6, 8):
        basis = [((x,), a, (y,), b) for x in range(n) for y in range(n) if x != y for a in range(2) for b in range(2)]
        traces = []
        for k in range(1, n + 1):
            tot = ZERO
            for s in basis:
                vec = {s: ONE}
                for _ in range(k):
                    vec = apply_h2(vec, moves, wrap=n)
                tot = gadd(tot, vec.get((s[2], s[3], s[0], s[1]), ZERO))
            traces.append(tot)
        ok_even = ok_even and all(t == ZERO for t in traces[:-1]) and traces[-1] == want[n]
    ok_odd = True
    for n in (5, 7):
        basis = [((x,), a, (y,), b) for x in range(n) for y in range(n) if x != y for a in range(2) for b in range(2)]

        def u_apply(vec, n=n):
            out = {}
            for (x, a, y, b), amp in vec.items():
                sign = 1 if x[0] < y[0] else -1
                sign *= (-1) ** (x[0] + y[0])
                if mut("odd_ring_unitary_forged"):
                    sign = (-1) ** (x[0] + y[0])
                key = (x, 1 - a, y, 1 - b)
                out[key] = gadd(out.get(key, ZERO), gmul((sign, 0), amp))
            return out
        for s in basis:
            lhs = u_apply(apply_h2({s: ONE}, moves, wrap=n))
            rhs = apply_h2(u_apply({s: ONE}), moves, wrap=n)
            ps = (s[2], s[3], s[0], s[1])
            up = u_apply({ps: ONE})
            pu = {(k[2], k[3], k[0], k[1]): v for k, v in u_apply({s: ONE}).items()}
            ok_odd = ok_odd and lhs == rhs and up == {k: gmul((-1, 0), v) for k, v in pu.items()}
    checks.check("D1", ok_even and ok_odd,
                 "T3: on block 78's rings with the reduced walk, tr(P (2H_2)^k) = 0 for k < N and 128, -1248, 7680 at k = N for N = 4, 6, 8 (an exchange must wind); on the odd rings N = 5, 7 the unitary U = (sigma_1 x sigma_1)(G x G) J, with J the sign of the order of the two positions and G = (-1)^x, commutes with the two-record walk and anticommutes with P on every basis vector, so the two sectors are unitarily equivalent and all spectral moments agree; observable and initial-state equivalence is not asserted")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the grading does not reach a record, and the discrete exchange carries no sign."""
    s1, s2, s3 = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    g = sp.Matrix(2, 2, sp.symbols("g0:4"))
    eqs = []
    for s in (s1, s2, s3):
        eqs += list(g * s + s * g)
    lin = sp.solve(eqs, list(g), dict=True)
    ok_lin = lin == [{v: 0 for v in g}] or all(all(val == 0 for val in d.values()) for d in lin)
    mm = sp.Matrix(2, 2, sp.symbols("m0:4"))
    eqs = []
    for s in (s1, s2, s3):
        eqs += list(mm * s.conjugate() + s * mm)
    anti = sp.solve(eqs, list(mm), dict=True)
    ok_anti = len(anti) == 1 and sp.simplify(mm.subs(anti[0]) - mm.subs(anti[0])[0, 1] * sp.I * s2) == sp.zeros(2, 2)
    cc = sp.symbols("cc")
    msq = (cc * s2) * (cc * s2).conjugate()
    ok_sq = sp.simplify(msq + cc * sp.conjugate(cc) * sp.eye(2)) == sp.zeros(2, 2)
    i2 = sp.eye(2)
    gam = sp.kronecker_product(i2, s3)
    es = [sp.kronecker_product(s, s1) for s in (s1, s2, s3)]
    ok_c4 = gam ** 2 == sp.eye(4) and all(gam * e + e * gam == sp.zeros(4, 4) and e ** 2 == sp.eye(4) for e in es)
    omega = es[0] * es[1] * es[2]
    ok_c4 = ok_c4 and omega ** 2 == -sp.eye(4)
    if mut("grading_forged"):
        ok_c4 = ok_c4 and omega ** 2 == sp.eye(4)
    kp = sp.kronecker_product
    maj = [kp(s1, i2, i2), kp(s2, i2, i2), kp(s3, s1, i2), kp(s3, s2, i2), kp(s3, s3, s1), kp(s3, s3, s2)]
    ok_maj = all(m ** 2 == sp.eye(8) for m in maj) and all(maj[i] * maj[j] + maj[j] * maj[i] == sp.zeros(8, 8) for i in range(6) for j in range(i + 1, 6))
    prods = set()
    product_matrices = []
    for mask in range(64):
        pm = sp.eye(8)
        for i in range(6):
            if mask >> i & 1:
                pm = pm * maj[i]
        prods.add(tuple(pm))
        product_matrices.append(pm)
    ok_maj = ok_maj and len(prods) == 64 and all(pm.trace()==0 for pm in product_matrices[1:])
    d = -sp.I * s2
    ok_rot = d * s1 * d.H == -s1 and d * s3 * d.H == -s3 and d * s2 * d.H == s2 and d ** 2 == -sp.eye(2)
    ok_two = kp(d, d) ** 2 == sp.eye(4)
    checks.check("E1", ok_lin and ok_anti and ok_sq and ok_c4 and ok_maj and ok_rot and ok_two,
                 "T4: no linear map of C^2 anticommutes with all three sigma_a except 0, and the antilinear ones are c sigma_2 K, which square to -|c|^2: no involution reversing all three generators acts on C2; a separately demanded complex-linear grading needs at least C4 (Gamma = 1 x sigma_3, e_a = sigma_a x sigma_1, pseudoscalar squaring to -1); two graded presentations compose to Cl(6,0) (six anticommuting square-one generators, 64 trace-orthogonal products), not to M_2(C) x M_2(C); the half-turn about e_2 acts on the coin by D = -i sigma_2 with D^2 = -1 (one record), while D x D squares to +1 on two records, on both sectors alike")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54 and 78 as landed on main (the walk and its reduced ring form; one record per site as an interaction); it reports whether the axioms fix the sign with which two records compose, and where that sign first shows; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Finkelstein", "Rubinstein", "Jordan", "Wigner", "Clifford", "Majorana", "Fermi", "Bose", "Einstein", "Chebyshev", "Kramers", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the compressed two-record generator on every basis vector of the ring of four: closure, hermiticity, commutation with the exchange",
    "per_site: executed - the coin-summed exchange amplitude of every separation up to distance 2 on Z^2 and Z^3 at orders 2, 3 and 4",
    "per_mode: executed - the exchange traces tr(P (2H_2)^k) for k <= N on the rings of 4, 6 and 8",
    "per_block: executed - the odd-ring unitary on every basis vector of the rings of 5 and 7; the grading and the Clifford composite; the discrete exchange rotation",
    "lattice_wide: T1-T4 on the stated lattices and rings; T2 on the infinite lattice by local enumeration; the walk, the compression and the composition supplied; three or more records not treated",
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
    print('scope: Fixed-sector exclusion witness and restricted grading algebra; no general observable indistinguishability. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
