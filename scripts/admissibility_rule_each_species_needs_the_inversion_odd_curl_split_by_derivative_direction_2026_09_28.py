#!/usr/bin/env python3
"""Exact checks: which lattice placements of block 158's inversion-odd curl term (1/8) eps.C serve each of the walk's eight species
(harvest of probe HIT #9367, a Claude Opus worker, refereed by Claude Sonnet). (T1) Species A (corner of {0, pi}^3, D = diag cos A,
s = det D, rho = sD) sees a frame E as rho E rho (block 70, landed), and s eps.C[rho E rho] = sum_d D_d X_d with
X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j the part of eps.C = sum_d X_d whose derivative is along axis d; its comparator completion needs the
coin scalar N_A = (1/8) sum_d D_d X_d. (T2) A symmetric hop by displacement m reaches species A with the sign prod_d D_d^(m_d mod 2), a
site term unchanged; the eight sign patterns are the characters of {+-1}^3, so a coin-scalar placement serves all eight species iff its
long-wave weight is X_d/8 on the displacements odd along axis d alone and zero on every other parity class. (T3) With weight (1/8) eps.C,
a site term or face-diagonal hops serve k = 0 only and the body diagonal serves k = 0 and (pi,pi,pi); any placement on even-degree
classes gives a corner and its antipode the same scalar while N changes sign, so it serves both only where N_A = 0. (T4) On the lengths'
frame e = 1 + eta every X_d vanishes at first order, but the lengths' connection gives block 161's links the per-axis scalars
L_j = (1/4) eps_jab omega_jab with omega_jab = d_b eta_aj - d_a eta_jb, nonzero for the jet d_3 eta_12 = 1: they hand the six mixed
species a spurious first-order scalar (-1 at (pi,0,0)).

A (premises): landed block 70's exchange rule and its frame row.
B (T1): the species map of eps.C, symbolic with a rational frame and 27 generic derivatives.
C (T2): the sign rule for hops on a (4,6,4) torus with random integer weights.
D (T2): the characters and the unique serving placement.
E (T3): the alternatives and the even-degree obstruction.
F (T4): first order on the lengths' frame; block 161's links.
Exact (sympy, integers). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_EACH_SPECIES_NEEDS_THE_INVERSION_ODD_CURL_SPLIT_BY_DERIVATIVE_DIRECTION_ONLY_PER_AXIS_HOPS_CARRYING_EACH_AXIS_PART_SERVE_ALL_EIGHT_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_each_species_needs_the_inversion_odd_curl_split_by_derivative_direction_only_per_axis_hops_carrying_each_axis_part_serve_all_eight_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED70 = (
    "`U_nT_aU_n = D_aT_a`",
    "| frame `E` | `s_n H[ρ_nEρ_n]` |",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "species_map_forged": "B",
    "sign_rule_forged": "C",
    "characters_forged": "D",
    "alternative_forged": "E",
    "links_forged": "F",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
CORNERS = list(itertools.product((0, 1), repeat=3))
LC = lambda a, b, c: sp.LeviCivita(a, b, c)


def eps_c(E, dE):
    """block 158's eps.C = eps_abc E^i_b E^j_c (d_i e^a_j - d_j e^a_i); E[b][i] = E^i_b, dE[i][a][j] = d_i e^a_j"""
    tot = sp.Integer(0)
    for a, b, c, i, j in itertools.product(range(3), repeat=5):
        l = LC(a, b, c)
        if l == 0:
            continue
        tot += l * E[b][i] * E[c][j] * (dE[i][a][j] - dE[j][a][i])
    return sp.expand(tot)


def x_part(E, dE, d):
    """X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j"""
    tot = sp.Integer(0)
    for a, b, c, j in itertools.product(range(3), repeat=4):
        l = LC(a, b, c)
        if l == 0:
            continue
        tot += 2 * l * E[b][d] * E[c][j] * dE[d][a][j]
    return sp.expand(tot)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t70 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(normalize_text(n) in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility or site privileged; Admissibility is not a dynamics axiom (the walk, its frame and the curl term are supplied)")
    q = list(LANDED70)
    if mut("landed_quote_forged"):
        q[1] = "| frame `E` | `s_n H[D_nED_n]` |"
    checks.check("A3", all(x in t70 for x in q), "landed block 70: the site-sign map multiplies a hop along a by D_a, and species n sees a frame E as rho_n E rho_n")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    rng = random.Random(9367)
    dsym = [[[sp.Symbol(f"d{i}{a}{j}") for j in range(3)] for a in range(3)] for i in range(3)]
    ok_split = True
    ok_map = True
    for trial in range(3):
        while True:
            e = sp.Matrix(3, 3, lambda r, c: sp.Rational(rng.randint(-5, 5), rng.randint(1, 4)) + (2 if r == c else 0))
            if e.det() != 0:
                break
        Einv = e.inv()
        # E^i_b: the frame is the inverse co-frame; E[b][i] with e^a_j E^j_b = delta
        E = [[Einv[i, b] for i in range(3)] for b in range(3)]
        ec = eps_c(E, dsym)
        xs = [x_part(E, dsym, d) for d in range(3)]
        ok_split = ok_split and sp.expand(ec - sum(xs)) == 0
        for A in CORNERS:
            D = [(-1) ** n for n in A]
            s = D[0] * D[1] * D[2]
            rho = [s * x for x in D]
            # species frame rho E rho; its co-frame rho e rho; derivatives transform the same way (rho constant)
            E2 = [[rho[b] * E[b][i] * rho[i] for i in range(3)] for b in range(3)]
            d2 = [[[rho[a] * dsym[i][a][j] * rho[j] for j in range(3)] for a in range(3)] for i in range(3)]
            lhs = sp.expand((1 if mut("species_map_forged") else s) * eps_c(E2, d2))
            rhs = sp.expand(sum(D[d] * xs[d] for d in range(3)))
            ok_map = ok_map and lhs == rhs
    checks.check("B1", ok_split, "eps.C = X_1 + X_2 + X_3 with X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j, for three rational frames and 27 generic derivatives")
    checks.check("B2", ok_map, "for every one of the eight species, s eps.C[rho E rho] = sum_d D_d X_d: the species' comparator completion needs the coin scalar N_A = (1/8) sum_d cos(A_d) X_d")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    rng = random.Random(29)
    Ls = (4, 6, 4)
    sites = list(itertools.product(*[range(L) for L in Ls]))
    idx = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    disps = [(1, 0, 0), (0, 1, 0), (1, 1, 0), (1, -1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (-1, 2, 0), (1, 2, 3), (0, 0, 2)]
    ok = True
    for m in disps:
        w = {x: rng.randint(-9, 9) for x in sites}
        H = sp.zeros(n, n)
        for x in sites:
            y = tuple((x[a] + m[a]) % Ls[a] for a in range(3))
            H[idx[x], idx[y]] += w[x]
            H[idx[y], idx[x]] += w[x]
        for A in CORNERS:
            U = sp.diag(*[(-1) ** sum(A[a] * x[a] for a in range(3)) for x in sites])
            sign = 1
            for a in range(3):
                sign *= ((-1) ** A[a]) ** (m[a] % 2)
            if mut("sign_rule_forged") and m == (1, 1, 0):
                sign = 1
            ok = ok and (U * H * U - sign * H) == sp.zeros(n, n)
    V = sp.diag(*[rng.randint(-9, 9) for _ in sites])
    U = sp.diag(*[(-1) ** (x[0] + x[2]) for x in sites])
    ok = ok and U * V * U == V
    checks.check("C1", ok, "on a (4,6,4) torus with random integer weights, a symmetric hop by m (ten displacements, including two-step and three-axis ones) is multiplied by prod_d D_d^(m_d mod 2) under every species' site-sign map; a site term is unchanged")


# ============================================================================================ family D (T2)
def family_d(checks: Checks) -> None:
    X = sp.symbols("X1:4")
    chi = sp.Matrix(8, 8, lambda i, j: sp.prod([((-1) ** CORNERS[i][d]) ** CORNERS[j][d] for d in range(3)]))
    ok_orth = chi * chi.T == 8 * sp.eye(8)
    w = sp.symbols("w0:8")
    eqs = []
    for i, A in enumerate(CORNERS):
        D = [(-1) ** n for n in A]
        p = sum(w[j] * sp.prod([D[d] ** CORNERS[j][d] for d in range(3)]) for j in range(8))
        N = sp.Rational(1, 8) * sum(D[d] * X[d] for d in range(3))
        eqs.append(sp.expand(p - N))
    sol = sp.solve(eqs, w, dict=True)
    want = {w[j]: (X[[d for d in range(3) if CORNERS[j][d] == 1][0]] / 8 if sum(CORNERS[j]) == 1 else 0) for j in range(8)}
    if mut("characters_forged"):
        want[w[0]] = sp.Rational(1, 8) * sum(X)
    ok_sol = len(sol) == 1 and all(sp.simplify(sol[0][k] - v) == 0 for k, v in want.items())
    checks.check("D1", ok_orth and ok_sol, "the eight sign patterns are orthogonal characters (chi chi^T = 8 I); the only class weights serving all eight species are X_d/8 on the class odd along axis d alone and zero on the site, face-diagonal and body-diagonal classes")


# ============================================================================================ family E (T3)
def family_e(checks: Checks) -> None:
    X = sp.symbols("X1:4")
    tot = sum(X) / 8
    served = {}
    for name, cls in (("site", [(0, 0, 0)]), ("face diagonals", [(1, 1, 0), (1, 0, 1), (0, 1, 1)]), ("body diagonal", [(1, 1, 1)])):
        corners = []
        for A in CORNERS:
            D = [(-1) ** n for n in A]
            p = sum(sp.prod([D[d] ** c[d] for d in range(3)]) for c in cls) * tot / len(cls)
            N = sp.Rational(1, 8) * sum(D[d] * X[d] for d in range(3))
            if sp.expand(p - N) == 0:
                corners.append(A)
        served[name] = corners
    want = {"site": [(0, 0, 0)], "face diagonals": [(0, 0, 0)], "body diagonal": [(0, 0, 0), (1, 1, 1)]}
    if mut("alternative_forged"):
        want["site"] = [(0, 0, 0), (1, 1, 1)]
    ok_tab = served == want
    # even-degree classes: the scalar at a corner and at its antipode agree, while the needed scalar changes sign
    w = sp.symbols("v0:8")
    ok_even = True
    for A in CORNERS:
        D = [(-1) ** n for n in A]
        Dm = [-x for x in D]
        pe = lambda DD: sum(w[j] * sp.prod([DD[d] ** CORNERS[j][d] for d in range(3)]) for j in range(8) if sum(CORNERS[j]) % 2 == 0)
        ok_even = ok_even and sp.expand(pe(D) - pe(Dm)) == 0
        need = lambda DD: sum(DD[d] * X[d] for d in range(3))
        ok_even = ok_even and sp.expand(need(D) + need(Dm)) == 0
    checks.check("E1", ok_tab and ok_even, f"with weight (1/8) eps.C: {served}; and any placement on the even-degree classes (site, face diagonals) gives a corner and its antipode the same scalar while N_A changes sign, so it serves both only where N_A = 0")


# ============================================================================================ family F (T4)
def family_f(checks: Checks) -> None:
    # first order on e = 1 + eta, eta symmetric: generic first derivatives d_i eta_aj symmetric in (a, j)
    de = [[[sp.Symbol(f"h{i}{min(a, j)}{max(a, j)}") for j in range(3)] for a in range(3)] for i in range(3)]
    Eid = [[1 if i == b else 0 for i in range(3)] for b in range(3)]
    xs = [x_part(Eid, de, d) for d in range(3)]
    ok_x = all(x == 0 for x in xs)
    # the lengths' connection at first order: omega_jab = e^a_k(d_j E^k_b + Gamma^k_jl E^l_b), g = 1 + 2 eta
    t = sp.Symbol("t")
    om = [[[sp.Integer(0)] * 3 for _ in range(3)] for _ in range(3)]
    for j, a, b in itertools.product(range(3), repeat=3):
        dE = -de[j][a][b]  # d_j E^a_b at first order (E = 1 - eta)
        gam = de[j][a][b] + de[b][a][j] - de[a][j][b]  # Gamma^a_jb at first order for g = 1 + 2 eta
        om[j][a][b] = sp.expand(dE + gam)
    ok_om = all(sp.expand(om[j][a][b] - (de[b][a][j] - de[a][j][b])) == 0 for j, a, b in itertools.product(range(3), repeat=3))
    # block 161's link along j: a_{j,c} = (1/2) eps_cab omega_jab; its scalar (1/2) E^j . a_j = (1/2) a_{j,j} at first order
    L = [sp.expand(sp.Rational(1, 2) * sp.Rational(1, 2) * sum(LC(j, a, b) * om[j][a][b] for a in range(3) for b in range(3))) for j in range(3)]
    sub = {s_: 0 for s_ in set().union(*[x.free_symbols for x in L])}
    jet = dict(sub)
    jet[sp.Symbol("h201")] = 1  # d_3 eta_12 = 1 (zero-based: derivative index 2, pair (0, 1))
    Lj = [x.subs(jet) for x in L]
    if mut("links_forged"):
        Lj = [0, 0, 0]
    sums = sp.expand(sum(L))
    D = [-1, 1, 1]  # species (pi, 0, 0)
    spur = sum(D[d] * Lj[d] for d in range(3))
    ok = ok_x and ok_om and Lj == [sp.Rational(1, 2), -sp.Rational(1, 2), 0] and sums == 0 and spur == -1
    checks.check("F1", ok, f"on the lengths' frame e = 1 + eta: every X_d vanishes at first order (so every species needs zero), the lengths' connection is omega_jab = d_b eta_aj - d_a eta_jb, block 161's per-axis link scalars sum to zero but for the jet d_3 eta_12 = 1 are {Lj}; species (pi,0,0) receives {spur} at first order, a spurious scalar")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the mixed species."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Berry", "Zak", "Hellmann", "Feynman",
                   "Walsh", "Hadamard", "Ivanenko", "Kogut", "Susskind")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Walsh) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the split of eps.C by derivative direction; the species map of eps.C for all eight species",
    "per_site: executed - the sign rule for ten displacements on a (4,6,4) torus",
    "per_mode: executed - the character argument and the unique serving placement",
    "per_block: executed - the alternatives with weight (1/8) eps.C; the even-degree obstruction; first order on the lengths' frame and block 161's links",
    "lattice_wide: checked and not executed - the range-1 realisation's error (floating point in the probe, about l^-2); coin-valued placements; placements with staggered weights; relabelling consistency for the six mixed species",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: each species needs (1/8) sum_d cos(A_d) X_d; only per-axis hops carrying X_d/8 serve all eight; with weight (1/8) eps.C the site term and face diagonals serve k = 0 only, the body diagonal k = 0 and (pi,pi,pi); block 161's links give the six mixed species a spurious first-order scalar; a harvest of probe #9367, refereed by Claude Sonnet 5 (same family); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
