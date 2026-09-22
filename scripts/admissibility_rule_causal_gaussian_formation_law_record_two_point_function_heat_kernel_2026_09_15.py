#!/usr/bin/env python3
"""Exact checks: the record two-point function of the causal Gaussian formation law in level time.

Scope.  The real Gaussian instance of the nearest-neighbor formation law (v_x = w * sum of the three recorded predecessors + noise
of variance sigma^2; gain g = 3w) in the monotone class on the half-space of Z^3, conditional on level 0.  T1: the directed-path
kernel, checked on a 5x5 transverse torus against the covariance recursion.  T2: the coincidence probabilities P_n of two
directed walks (exact to n = 200) against 1/(36n) <= P_n <= 2/n; the variance series at g = 1 (harmonic growth) and g = 1/2
(bounded); the transverse and downstream decay bounds.  T3: the symbol equals block 09's graph; its expansions; the identity
p_{2n} = C(2n,n)/4^n * P_n for the simple random walk's return probability; the static partial sums bounded, the formation
series unbounded.  T4: the central binomial bounds to n = 400.  T5: the second-order expansion of log f(s.a) for the Born and
exponential overlaps; the literal parent has coefficient -1/6; the separate real fixture has positive gain 1/2; an exact candidate symbol evaluation.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_DIRECTED_GAUSSIAN_PROPAGATOR_OVERLAP_COVARIANCE_GAIN_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_HERMITIAN_GAUSSIAN_INSTANCE_FORMATION_PRECISION_LDL_BOUNDED_THEOREM_NOTE_2026-09-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_directed_gaussian_propagator_overlap_covariance_gain_bounds_bounded_theorem_note_2026-09-15"
BLOCK07_CLAIM_ID = "admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_bounded_theorem_note_2026-09-07"
BLOCK07_FRAGMENT = "1/2` on every edge"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "kernel_formula_wrong": "B",
    "level_sum_not_gain_power": "B",
    "coincidence_bounds_violated": "C",
    "stationary_law_at_g1_claimed": "C",
    "massive_variance_unbounded_claimed": "C",
    "downstream_bound_wrong": "C",
    "symbol_graph_wrong": "D",
    "transverse_expansion_quadratic_claimed": "D",
    "walk_identity_wrong": "D",
    "formation_series_bounded_claimed": "D",
    "binomial_bounds_violated": "E",
    "born_curvature_wrong": "E",
    "block07_gain_wrong": "E",
    "claim_green_function_reproduced": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


F = Fraction


def dec(x: Fraction, n: int = 6) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


# ------------------------------------------------------------------ walks
def coincidence_probabilities(nmax: int):
    """P_n (n = 0..nmax) via the projected lazy walk's counts; also the distribution of the difference walk per n."""
    counts = {(0, 0): 1}
    P = [F(1)]
    dists = [dict(counts)]
    for n in range(1, nmax + 1):
        new: dict = {}
        for (a, b), c in counts.items():
            for da, db in ((0, 0), (1, 0), (0, 1)):
                new[(a + da, b + db)] = new.get((a + da, b + db), 0) + c
        counts = new
        dists.append(counts)
        P.append(F(sum(c * c for c in counts.values()), 9 ** n))
    return P, dists


def displacement_probability(counts: dict, n: int, d: tuple) -> Fraction:
    """P_n(d): probability that the difference of two independent projected walks equals d after n steps."""
    tot = 0
    for (a, b), c in counts.items():
        c2 = counts.get((a - d[0], b - d[1]))
        if c2:
            tot += c * c2
    return F(tot, 9 ** n)


def harmonic(t: int) -> Fraction:
    return sum((F(1, k) for k in range(1, t + 1)), F(0))


def multinomial_square_sum(n: int) -> int:
    return sum((factorial(n) // (factorial(a) * factorial(b) * factorial(n - a - b))) ** 2 for a in range(n + 1) for b in range(n + 1 - a))


def srw_return_count(m: int) -> int:
    """Number of simple-random-walk paths of m steps on Z^3 returning to the origin (direct enumeration over step multisets)."""
    total = 0
    for a1 in range(m // 2 + 1):
        for a2 in range(m // 2 + 1 - a1):
            a3 = m // 2 - a1 - a2
            if 2 * (a1 + a2 + a3) != m:
                continue
            total += factorial(m) // (factorial(a1) ** 2 * factorial(a2) ** 2 * factorial(a3) ** 2)
    return total if m % 2 == 0 else 0


# ------------------------------------------------------------------ torus
def torus_matrices(W: int, w: Fraction):
    sites = [(a, b) for a in range(W) for b in range(W)]
    idx = {s: i for i, s in enumerate(sites)}
    n = W * W
    A = [[F(0)] * n for _ in range(n)]
    for (a, b) in sites:
        for (da, db) in ((0, 0), (1, 0), (0, 1)):
            A[idx[(a, b)]][idx[((a - da) % W, (b - db) % W)]] += w
    return sites, idx, A


def matmul(X, Y):
    n, m, k = len(X), len(Y[0]), len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def transpose(X):
    return [list(r) for r in zip(*X)]


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b07: str) -> None:
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, block 07 on main)")
    checks.check("A2", all(n in normalize_text(axiom_text) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f07 = normalize_text(b07)
    checks.check("A3", BLOCK07_CLAIM_ID in f07 and BLOCK07_FRAGMENT in f07,
                 "block 07's claim id and its real-entry precision fragment (+1/2 on every edge) are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    W, T = 5, 6
    w = F(1, 3)
    sites, idx, A = torus_matrices(W, w)
    n = W * W
    AT = transpose(A)
    C = [[F(0)] * n for _ in range(n)]
    Cs = [C]
    for t in range(1, T + 1):
        C = matmul(matmul(A, C), AT)
        for i in range(n):
            C[i][i] += 1
        Cs.append(C)
    # kernel formula: Cov_t(y, y') = sum_{m=0}^{t-1} sum_z (A^m)[y][z] (A^m)[y'][z]
    Am = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    K = [[F(0)] * n for _ in range(n)]
    for m in range(T):
        K = [[K[i][j] + sum(Am[i][z] * Am[j][z] for z in range(n)) for j in range(n)] for i in range(n)]
        Am = matmul(Am, A)
    if mut("kernel_formula_wrong"):
        K[idx[(2, 3)]][idx[(2, 3)]] += F(1, 7)
    equal = all(Cs[T][i][j] == K[i][j] for i in range(n) for j in range(n))
    checks.check("B1", equal, f"T1: on the 5x5 transverse torus with {T} levels the covariance recursion equals the directed-path kernel formula at every pair of sites (variance at (2,3): {Cs[T][idx[(2, 3)]][idx[(2, 3)]]})")
    # level sums of the kernel = g^n, for g = 1 and g = 1/2
    ok = True
    for g in (F(1), F(1, 2)):
        _, _, Ag = torus_matrices(W, g / 3)
        Am = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
        for m in range(1, 5):
            Am = matmul(Am, Ag)
            s = sum(Am[idx[(2, 3)]])
            if mut("level_sum_not_gain_power"):
                s += F(1, 9)
            ok = ok and s == g ** m
    checks.check("B2", ok, "T1: the level sums of the kernel from a site equal g^n for n = 1..4 at g = 1 and g = 1/2 (a probability kernel at g = 1)")
    report["torus"] = (Cs, idx, A)


# ============================================================================================ family C
NMAX = 200


def family_c(checks: Checks, report: dict) -> None:
    P, dists = coincidence_probabilities(NMAX)
    report["P"] = P
    lo = all(P[n] >= F(1, 36 * n) for n in range(1, NMAX + 1))
    hi = all(P[n] <= F(2, n) for n in range(1, NMAX + 1))
    if mut("coincidence_bounds_violated"):
        hi = all(P[n] <= F(1, 3 * n) for n in range(1, NMAX + 1))
    checks.check("C1", lo and hi and P[0] == 1, "T2(b): 1/(36n) <= P_n <= 2/n for 1 <= n <= 200 (P_0 = 1); n P_n at n = 10, 100, 200: " + ", ".join(dec(n * P[n]) for n in (10, 100, 200)))
    V1 = [F(0)]
    for t in range(1, NMAX + 1):
        V1.append(V1[-1] + P[t - 1])
    H = [harmonic(t) for t in range(NMAX + 1)]
    growth = all(H[t] / 36 <= V1[t] <= 1 + 2 * H[t - 1] for t in range(1, NMAX + 1)) and V1[NMAX] > 3
    if mut("stationary_law_at_g1_claimed"):
        growth = V1[NMAX] < 3
    checks.check("C2", growth, "T2(b): at g = 1 the variance series (sigma^2 = 1) satisfies H_t/36 <= Var_t <= 1 + 2 H_{t-1} for t <= 200, and exceeds 3 at t = 200: " + ", ".join(f"t={t}: {dec(V1[t], 3)}" for t in (10, 50, 100, 200)))
    g = F(1, 2)
    V2 = [F(0)]
    for t in range(1, NMAX + 1):
        V2.append(V2[-1] + g ** (2 * (t - 1)) * P[t - 1])
    bounded = all(V2[t] <= F(4, 3) for t in range(NMAX + 1)) and V2[NMAX] - V2[NMAX // 2] < F(1, 10 ** 20)
    # transverse decay at g = 1/2: Cov(d) = sum_n g^{2n} P_n(d) <= g^{2|d|_inf}/(1-g^2)
    dec_ok = True
    covs = {}
    for m in (1, 2, 3, 4):
        d = (m, 0)
        cov = sum((g ** (2 * n) * displacement_probability(dists[n], n, d) for n in range(NMAX + 1)), F(0))
        covs[m] = cov
        dec_ok = dec_ok and cov <= g ** (2 * m) / (1 - g ** 2)
    if mut("massive_variance_unbounded_claimed"):
        bounded = False
    checks.check("C3", bounded and dec_ok, "T2(a): at g = 1/2 the variance series is <= 4/3 and changes by less than 10^-20 between t = 100 and 200 (" + dec(V2[NMAX]) + "); the equal-level covariance at transverse distance m obeys Cov <= g^{2m}/(1-g^2): " + ", ".join(f"m={m}: {dec(covs[m])}" for m in (1, 2, 3, 4)))
    # downstream bound on the torus at g = 1/2: |Cov(v_t(y), v_{t+s}(y'))| <= g^s sup Var
    W = 5
    sites, idx, A = torus_matrices(W, g / 3)
    n = W * W
    AT = transpose(A)
    C = [[F(0)] * n for _ in range(n)]
    for t in range(6):
        C = matmul(matmul(A, C), AT)
        for i in range(n):
            C[i][i] += 1
    sup_var = max(C[i][i] for i in range(n))
    ok = True
    Cs = C
    for s in range(1, 5):
        Cs = matmul(Cs, AT)  # Cov(v_t, v_{t+s}) = C_t (A^T)^s
        bound = g ** s * sup_var
        if mut("downstream_bound_wrong"):
            bound = g ** (2 * s) * sup_var / 4
        ok = ok and all(abs(Cs[i][j]) <= bound for i in range(n) for j in range(n))
    checks.check("C4", ok, "T2(a): on the torus at g = 1/2 the covariance between level 6 and level 6+s is bounded by g^s times the largest variance for s = 1..4")


# ============================================================================================ family D
def family_d(checks: Checks, report: dict, exact: bool) -> None:
    k1, k2, k3, w_, e, q1, q2 = sp.symbols("k1 k2 k3 w epsilon q1 q2", real=True)
    a = w_ * (sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2) + sp.exp(-sp.I * k3))
    symb = sp.expand_complex(sp.expand((1 - a) * (1 - sp.conjugate(a))))
    target = 1 - 2 * w_ * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) + w_ ** 2 * (3 + 2 * (sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3)))
    if mut("symbol_graph_wrong"):
        target = target + w_ ** 2 * sp.cos(k1 + k2)
    ident = sp.simplify(sp.expand_trig(symb - target)) == 0
    checks.check("D1", ident, "T3(i): |1 - w sum e^{-ik_j}|^2 = 1 - 2w sum cos k_j + w^2 (3 + 2 sum_{i<j} cos(k_i - k_j)): block 09's axial + face-diagonal graph")
    s1 = target.subs(w_, sp.Rational(1, 3))
    level = sp.series(s1.subs({k1: e, k2: e, k3: e}), e, 0, 4).removeO()
    trans = sp.series(s1.subs({k1: e * q1, k2: e * q2, k3: -e * (q1 + q2)}), e, 0, 6).removeO()
    trans_ok = sp.simplify(trans - e ** 4 * (q1 ** 2 + q1 * q2 + q2 ** 2) ** 2 / 9) == 0
    # |k|^4/36 with |k|^2 = e^2 (q1^2 + q2^2 + (q1+q2)^2) = 2 e^2 (q1^2 + q1 q2 + q2^2)
    k4 = (2 * e ** 2 * (q1 ** 2 + q1 * q2 + q2 ** 2)) ** 2 / 36
    if mut("transverse_expansion_quadratic_claimed"):
        trans_ok = sp.simplify(trans - e ** 2 * (q1 ** 2 + q2 ** 2) / 9) == 0
    checks.check("D2", sp.simplify(level - e ** 2) == 0 and trans_ok and sp.simplify(k4 - e ** 4 * (q1 ** 2 + q1 * q2 + q2 ** 2) ** 2 / 9) == 0,
                 "T3(ii): at g = 1 the symbol along (u,u,u) is 2-2cos(u) = u^2 + O(u^4), with leading K^2/9, and on the transverse plane it is |k|^4/36 + O(k^6) (quartic): parabolic")
    ok = True
    for n in range(0, 7):
        lhs = srw_return_count(2 * n)
        rhs = comb(2 * n, n) * multinomial_square_sum(n)
        if mut("walk_identity_wrong"):
            rhs = rhs + (1 if n == 3 else 0)
        ok = ok and lhs == rhs and srw_return_count(2 * n + 1) == 0
    checks.check("D3", ok, "T3(iii): the number of returning simple-random-walk paths of 2n steps equals C(2n,n) * sum_a (n!/a!)^2 for n <= 6 (odd lengths never return): p_{2n} = C(2n,n)/4^n * P_n")
    P = report["P"]
    static = F(1) + sum((F(comb(2 * n, n), 4 ** n) * P[n] for n in range(1, NMAX + 1)), F(0))
    formation = sum((P[n] for n in range(NMAX + 1)), F(0))
    static_ok = static < F(152, 100)
    form_ok = formation > harmonic(NMAX) / 36 and formation > 3
    if mut("formation_series_bounded_claimed"):
        form_ok = formation < 2
    checks.check("D4", static_ok and form_ok, f"T3(iii): the static series 1 + sum_{{n<=200}} C(2n,n)/4^n P_n = {dec(static, 4)} < 152/100 (its sixth is the Green function's diagonal partial sum) while the formation series sum_{{n<=200}} P_n = {dec(formation, 4)} exceeds H_200/36 and 3")
    if exact:
        print("exact P_n at n = 1..6:", ", ".join(str(P[n]) for n in range(1, 7)))
        print("exact static partial sum to n = 200:", dec(static, 12))


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    lo = all(F(comb(2 * n, n), 4 ** n) ** 2 >= F(1, 4 * n) for n in range(1, 401))
    hi = all(F(comb(2 * n, n), 4 ** n) ** 2 <= F(3, 4 * (2 * n + 1)) for n in range(1, 401))
    if mut("binomial_bounds_violated"):
        hi = all(F(comb(2 * n, n), 4 ** n) ** 2 <= F(1, 4 * (2 * n + 1)) for n in range(1, 401))
    checks.check("E1", lo and hi, "T4: 1/(4n) <= (C(2n,n)/4^n)^2 <= 3/(4(2n+1)) for n <= 400: square-root growth in one transverse dimension")
    e, th1, th2, ph1, ph2, beta = sp.symbols("epsilon theta1 theta2 phi1 phi2 beta", real=True, positive=True)

    def unit(u1, u2):
        r = sp.sqrt(u1 ** 2 + u2 ** 2)
        return sp.Matrix([sp.sin(r) * u1 / r, sp.sin(r) * u2 / r, sp.cos(r)])
    dot = sp.simplify((unit(e * th1, e * th2).T * unit(e * ph1, e * ph2))[0])
    quad = (th1 - ph1) ** 2 + (th2 - ph2) ** 2
    born = sp.series(sp.log((1 + dot) / 2), e, 0, 3).removeO()
    expo = sp.series(sp.log(sp.exp(beta * dot)), e, 0, 3).removeO()
    kappa_born = sp.Rational(1, 4)
    if mut("born_curvature_wrong"):
        kappa_born = sp.Rational(1, 2)
    born_ok = sp.simplify(sp.expand(born + kappa_born * e ** 2 * quad)) == 0
    expo_ok = sp.simplify(sp.expand(expo - beta + beta / 2 * e ** 2 * quad)) == 0
    checks.check("E2", born_ok and expo_ok, "T5(b): log f(s.a) = log f(1) - kappa |theta - phi|^2 + O(3) with kappa = f'(1)/(2f(1)): 1/4 for the Born overlap (auxiliary flat Gaussian variance 2/3), beta/2 for e^{beta t}")
    # Literal parent sign. Three-coefficient gain is a comparison, not its finite 2D model.
    Pxx, Pxy = F(3), F(1, 2)
    weight = -Pxy / Pxx
    gain = 3 * weight
    if mut("block07_gain_wrong"):
        gain = -gain
    parent_ok = weight == F(-1, 6) and gain == F(-1, 2) and 2 * weight == F(-1, 3)
    checks.check("E3", parent_ok, "T5(c): literal parent edges +1/2 give coefficient -1/6; sum of three is -1/2, while its 2D monotone two-parent sum is -1/3")
    kk = sp.symbols("kk1 kk2 kk3", real=True)
    six = 3 - 2 * sum(sp.cos(k) for k in kk)
    at0 = six.subs({k: 0 for k in kk})
    u = sp.symbols("u", real=True)
    norm = sp.integrate((1 + u)**3, (u, -1, 1))
    sphere_z = sp.integrate(u * (1 + u)**3, (u, -1, 1)) / norm
    sphere_x2 = sp.integrate((1 - u*u) * (1 + u)**3, (u, -1, 1)) / (2 * norm)
    checks.check("E4", at0 == -3 and (sp.Rational(1, 2) * (6 - 2 * sum(sp.cos(k) for k in kk))).subs({k: 0 for k in kk}) == 0 and sphere_z == sp.Rational(3, 5) and sphere_x2 == sp.Rational(4, 15),
                 "T5: separate sign-reversed 3D real fixture symbol is zero at origin; candidate 3I-sum S symbol is -3 there; actual aligned Born sphere has E[sz]=3/5, E[sx^2]=4/15")


# ============================================================================================ family F
FENCES = (
    "This note computes the directed propagator and accumulated overlap covariance of a supplied real Gaussian recursion; no physical order, rule, gain or sphere fluctuation law is selected.",
    "No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "The tangent Gaussian is auxiliary; broader negative certification is deferred.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "phase transition", "ordered phase exists", "converge", "emergent", "critical point",
    "washes out", "toward the plane", "the trend", "reproduces the Green function", "is the lattice Green function",
)
CLAIM_INJECTIONS = {"claim_green_function_reproduced": "Hence the formation law reproduces the Green function of the gravity lane."}
CLASSICAL_NAMES = ("Fourier", "Parseval", "Plancherel", "Chebyshev", "Jensen", "Cauchy", "Schwarz", "Stirling", "Edwards", "Wilkinson", "Watson", "Toom", "Peierls")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem T2"):
            body = body + " (the Chebyshev bound)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — P_n exactly to n = 200 against the two-sided bounds; the central binomial bounds to n = 400; the walk identity to n = 6",
    "per_site: executed — the covariance recursion against the kernel formula at every pair of sites of a 5x5 torus over six levels",
    "per_mode: executed — the symbol identity with block 09's graph; the level-direction and transverse expansions at g = 1",
    "per_block: executed — the variance series at g = 1 and g = 1/2 to level 200; the static and formation partial sums; the downstream and transverse decay bounds",
    "lattice_wide: analytical identities and bounds, checked in the note, not executed on an infinite lattice; subcritical innovation construction; formal critical symbol; auxiliary tangent Gaussian only; broad negative classification deferred",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    exact = "--exact" in argv
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the causal Gaussian formation law in level time — the directed-path kernel, the gain dichotomy, the symbol and the static/formation walk identity, one transverse dimension, what forces gain one; exact; no Green function claimed")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts[0], texts[1], texts[2])
    family_b(checks, report)
    family_c(checks, report)
    family_d(checks, report, exact)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
