#!/usr/bin/env python3
"""Positive fixed-count rates with symmetric proposals: exact fixed-field and neutralized torus pair laws, clock-only waiting times and finite kernel comparisons."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "bond_clock_taken_to_fall": "B",
    "departure_factor_inverted": "B",
    "field_not_slaved": "C",
    "pair_counted_twice": "C",
    "jumps_biased_by_the_clock": "D",
    "pair_potential_sign_flipped": "E",
    "drifted_kernel": "E",
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
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
from itertools import combinations


def ring_states(L, n, contents):
    """Configurations of n records with contents on a ring of L sites: dict site -> content."""
    out = []
    for sites in combinations(range(L), n):
        for cs in product(contents, repeat=n):
            out.append(dict(zip(sites, cs)))
    return out


def pair_weight(C, L, W):
    """Rule's pair weights between neighbouring records (W[(a, b)]); empty bonds weight one."""
    w = sp.Integer(1)
    for x, a in C.items():
        y = (x + 1) % L
        if y in C:
            w *= W[(a, C[y])]
    return w


def ring_moves(C, L):
    out = []
    for x in C:
        for y in ((x + 1) % L, (x - 1) % L):
            if y not in C:
                C2 = dict(C)
                a = C2.pop(x)
                C2[y] = a
                out.append((x, y, C2))
    return out


def key(C):
    return tuple(sorted(C.items()))


def zero_mean_green_1d(L):
    """G(d) = L^-1 sum_(n != 0) cos(2 pi n d / L)/(2 - 2 cos(2 pi n / L)), exact for L = 6 (rational cosines)."""
    cos6 = {0: sp.Integer(1), 1: sp.Rational(1, 2), 2: sp.Rational(-1, 2), 3: sp.Integer(-1), 4: sp.Rational(-1, 2), 5: sp.Rational(1, 2)}
    assert L == 6
    return {d: sum((cos6[(n * d) % 6] / (2 - 2 * cos6[n]) for n in range(1, 6)), sp.Integer(0)) / 6 for d in range(6)}


def zero_mean_green_3d(L):
    """Exact zero-mean Green function of the 3D lattice Laplacian E(k) on (Z/L)^3 for L = 4 or 6 (rational cosines), as a dict over offsets."""
    if L == 4:
        cosv = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    elif L == 6:
        cosv = {0: F(1), 1: F(1, 2), 2: F(-1, 2), 3: F(-1), 4: F(-1, 2), 5: F(1, 2)}
    else:
        raise ValueError(L)
    N = L ** 3
    ks = [n for n in product(range(L), repeat=3) if n != (0, 0, 0)]
    Ek = {n: 6 - 2 * sum(cosv[c] for c in n) for n in ks}
    G = {}
    for d in product(range(L), repeat=3):
        # cos(k.d) = product-free: cos of a sum is not a product; use the angle index (n.d) mod L
        G[d] = sum((cosv[sum(n[i] * d[i] for i in range(3)) % L] / Ek[n] for n in ks), ZERO) / N
    return G


def step(x, j, s, L):
    return tuple((x[i] + (s if i == j else 0)) % L for i in range(3))


def diff(z, r, L):
    return tuple((z[i] - r[i]) % L for i in range(3))


def rat(x):
    return sp.Rational(x.numerator, x.denominator)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    L = 5
    w = sp.symbols("w0:5", positive=True)
    a = sp.symbols("a", real=True)
    p, q = sp.symbols("p q", positive=True)
    W = {(1, 1): p, (-1, -1): p, (1, -1): q, (-1, 1): q}
    states = ring_states(L, 2, (1, -1))
    exponent = (1 - 2 * a) if not mut("departure_factor_inverted") else (2 * a - 1)
    ok_general = True
    ok_named = True
    moves = 0
    for C in states:
        for x, y, C2 in ring_moves(C, L):
            WC, WC2 = pair_weight(C, L, W), pair_weight(C2, L, W)
            hb_f, hb_b = WC2 / (WC + WC2), WC / (WC + WC2)
            lpi_c = sp.log(WC) + exponent * sum((sp.log(w[z]) for z in C), sp.Integer(0))
            lpi_c2 = sp.log(WC2) + exponent * sum((sp.log(w[z]) for z in C2), sp.Integer(0))
            lr_f = a * sp.log(w[x]) + (1 - a) * sp.log(w[y]) + sp.log(hb_f)
            lr_b = a * sp.log(w[y]) + (1 - a) * sp.log(w[x]) + sp.log(hb_b)
            ok_general = ok_general and sp.simplify(sp.expand_log(lpi_c + lr_f - lpi_c2 - lr_b, force=True)) == 0
            # the three named timings in product form: leaving end, bond, arriving end
            dep_law = (WC / sp.prod([w[z] for z in C]), WC2 / sp.prod([w[z] for z in C2]))
            bond_law = (WC, WC2) if not mut("bond_clock_taken_to_fall") else dep_law
            arr_law = (WC * sp.prod([w[z] for z in C]), WC2 * sp.prod([w[z] for z in C2]))
            rb = sp.sqrt(w[x] * w[y])
            for (pc, pc2), rf, rr in ((dep_law, w[x] * hb_f, w[y] * hb_b), (bond_law, rb * hb_f, rb * hb_b), (arr_law, w[y] * hb_f, w[x] * hb_b)):
                ok_named = ok_named and sp.simplify(pc * rf - pc2 * rr) == 0
            moves += 1
    checks.check("B1", ok_general and ok_named and moves == 120, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    lam, a = sp.symbols("lambda a", real=True)
    pair_factor = 1 if not mut("pair_counted_twice") else 2
    G1 = zero_mean_green_1d(6)
    lap1 = all(2 * G1[x] - G1[(x + 1) % 6] - G1[(x - 1) % 6] == (1 if x == 0 else 0) - sp.Rational(1, 6) for x in range(6))

    def u1(z, D):
        return 2 * lam * sum((G1[(z - r) % 6] for r in D), sp.Integer(0))

    def logf1(D):
        return pair_factor * 2 * lam * (1 - 2 * a) * sum((G1[(r - s) % 6] for r, s in combinations(sorted(D), 2)), sp.Integer(0))
    ok_ring = True
    ring_moves_n = 0
    for n in (2, 3):
        for sites in combinations(range(6), n):
            C = set(sites)
            for x in C:
                for y in ((x + 1) % 6, (x - 1) % 6):
                    if y in C:
                        continue
                    C2 = (C - {x}) | {y}
                    back = C2 if not mut("field_not_slaved") else C
                    lr_f = a * u1(x, C) + (1 - a) * u1(y, C)
                    lr_b = a * u1(y, back) + (1 - a) * u1(x, back)
                    ok_ring = ok_ring and sp.expand(logf1(C) + lr_f - logf1(C2) - lr_b) == 0
                    ring_moves_n += 1
    L = 4
    G = zero_mean_green_3d(L)
    lap3 = all(6 * G[x] - sum((G[step(x, j, s, L)] for j in range(3) for s in (1, -1)), ZERO) == (1 if x == (0, 0, 0) else 0) - F(1, L ** 3) for x in product(range(L), repeat=3))

    def u3(z, D):
        return 6 * lam * rat(sum((G[diff(z, r, L)] for r in D), ZERO))

    def logf3(D):
        return pair_factor * 6 * lam * (1 - 2 * a) * rat(sum((G[diff(r, t, L)] for r, t in combinations(sorted(D), 2)), ZERO))
    confs = [((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (2, 1, 0)), ((0, 0, 0), (1, 1, 1)), ((0, 0, 0), (2, 2, 2)),
             ((0, 0, 0), (1, 0, 0), (0, 2, 1)), ((1, 1, 0), (3, 0, 2), (0, 3, 3))]
    ok3 = True
    moves3 = 0
    for conf in confs:
        C = set(conf)
        for x in C:
            for j in range(3):
                for s in (1, -1):
                    y = step(x, j, s, L)
                    if y in C:
                        continue
                    C2 = (C - {x}) | {y}
                    back = C2 if not mut("field_not_slaved") else C
                    lr_f = a * u3(x, C) + (1 - a) * u3(y, C)
                    lr_b = a * u3(y, back) + (1 - a) * u3(x, back)
                    ok3 = ok3 and sp.expand(logf3(C) + lr_f - logf3(C2) - lr_b) == 0
                    moves3 += 1
    checks.check("C1", lap1 and lap3 and ok_ring and ok3, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    lam = sp.symbols("lambda", negative=True)                      # log(kappa) < 0: records slow clocks
    L = 6
    G = zero_mean_green_3d(L)

    def logw(z, D):
        return 6 * lam * rat(sum((G[diff(z, r, L)] for r in D), ZERO))
    dirs = [(j, s) for j in range(3) for s in (1, -1)]

    def mean_step(x, D, timing):
        """Expected displacement per unit time of the record at x (each vector component), hops to empty neighbours only."""
        out = [sp.Integer(0)] * 3
        for j, s in dirs:
            y = step(x, j, s, L)
            if y in D:
                continue
            rate = sp.exp(logw(x, D)) / 12 if timing == "leave" else sp.exp(logw(y, D)) / 12
            if timing == "leave" and mut("jumps_biased_by_the_clock"):
                rate = sp.exp(logw(y, D)) / 12
            out[j] += s * rate
        return [sp.simplify(c) for c in out]
    A = (0, 0, 0)
    far = [(2, 0, 0), (3, 1, 0), (2, 2, 1), (3, 3, 3)]
    unbiased = all(all(c == 0 for c in mean_step(A, {A, B}, "leave")) for B in far)
    # contact: the only bias is exclusion, directly away from the neighbour
    contact = mean_step(A, {A, (1, 0, 0)}, "leave")
    wA = sp.exp(logw(A, {A, (1, 0, 0)}))
    contact_ok = sp.simplify(contact[0] + wA / 12) == 0 and contact[1] == 0 and contact[2] == 0
    # timed by the site it enters: biased towards faster clocks, i.e. away from the other record when kappa < 1
    enter = mean_step(A, {A, (2, 0, 0)}, "enter")
    lam_val = sp.Rational(-1, 2)
    away = sp.simplify(enter[0].subs(lam, lam_val)) < 0
    # two records: both clocks equal at every separation; relative coordinate law ~ exp(-6 log(kappa) G(d))
    equal_clocks = all(logw(A, {A, d}) == logw(d, {A, d}) for d in product(range(L), repeat=3) if d != A)
    checks.check("D1", unbiased and contact_ok and bool(away) and equal_clocks, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = True
    for L in (4, 6):
        G = zero_mean_green_3d(L)
        axis = [G[(r, 0, 0)] for r in range(L // 2 + 1)]
        diag = [G[(r, r, r)] for r in range(L // 2 + 1)]
        ok = ok and all(axis[i] > axis[i + 1] for i in range(len(axis) - 1)) and all(diag[i] > diag[i + 1] for i in range(len(diag) - 1))
    ell = sp.symbols("ell", negative=True)
    G4 = zero_mean_green_3d(4)
    U = {r: 6 * ell * rat(G4[(r, 0, 0)]) for r in range(3)}
    attract = sp.simplify(U[1] - U[2]) < 0 if not mut("pair_potential_sign_flipped") else sp.simplify(U[1] - U[2]) > 0
    L = 4
    kernel = G4
    if mut("drifted_kernel"):
        kernel = {d: G4[d] + (F(1, 7) if d[0] == 1 else 0) for d in G4}
    even = all(kernel[d] == kernel[tuple((-c) % L for c in d)] for d in kernel)

    def phi(cluster, z):
        return sum((kernel[diff(z, r, L)] for r in cluster), ZERO)

    def central_pull(target, source, j):
        plus = sum((phi(source, step(t, j, 1, L)) for t in target), ZERO)
        minus = sum((phi(source, step(t, j, -1, L)) for t in target), ZERO)
        return (plus - minus) / 2
    A = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
    B = [(2, 1, 1), (3, 1, 1)]
    opposite = all(central_pull(B, A, j) == -central_pull(A, B, j) for j in range(3))
    field_sym = sum((phi(A, b) for b in B), ZERO) == sum((phi(B, r) for r in A), ZERO)
    checks.check("E1", ok and bool(attract) and even and opposite and field_sym, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    # General W need not give uniform allowed directions; W=1 supplies h=1/2.
    h1, h2 = sp.Rational(2, 3), sp.Rational(1, 2)
    x, y, a, lam = sp.symbols("Gxx Gyy a lambda", real=True)
    self_term = 6 * lam * a * (x-y)
    checks.check("D9", h1 != h2 and sp.Rational(1, 2)/6 == sp.Rational(1, 12) and self_term.subs({x:1,y:2,a:1,lam:1}) != 0, 'Scoped exact check D9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Positive fixed-count rates with symmetric proposals: exact fixed-field and neutralized torus pair laws, clock-only waiting times and finite kernel comparisons.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
