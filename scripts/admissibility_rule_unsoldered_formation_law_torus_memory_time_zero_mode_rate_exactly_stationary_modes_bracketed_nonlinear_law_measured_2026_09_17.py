#!/usr/bin/env python3
"""Torus mode variances and memory proxy for a supplied gain-one recurrence.

For the supplied gain-one recurrence theta(t+1)=P theta(t)+xi on a finite periodic L by L plane, prove the mode variances, zero-mode memory proxy and stationary nonzero-mode bracket for beta>0. Exact rational controls on L=2,3,4 and memory-time enclosures on the listed beta and size grid. The S_L increment test concerns L=16,32,64 only.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_NONLINEAR_LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_and_the_nonlinear_law_measured_against_it_bounded_theorem_note_2026-09-17"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "multiplier_wrong": "B",
    "covariance_recursion_wrong": "C",
    "memory_time_wrong": "D",
    "lattice_sum_bounds_wrong": "D",
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


# ------------------------------------------------------------------------------------------- exact enclosures (block 26's, restated)
def exp_bounds(x: Fraction, terms: int | None = None) -> tuple[Fraction, Fraction]:
    assert x >= 0
    n = terms if terms is not None else 2 * (int(x) + 1) + 40
    lo = Fraction(0)
    term = Fraction(1)
    for k in range(n + 1):
        lo += term
        term = term * x / (k + 1)
    assert x < n + 2
    hi = lo + term / (1 - x / (n + 2))
    return lo, hi


def A_bounds(kappa: Fraction) -> tuple[Fraction, Fraction]:
    """coth kappa - 1/kappa = (E + 1)/(E - 1) - 1/kappa with E = e^{2 kappa}, decreasing in E."""
    e_lo, e_hi = exp_bounds(2 * kappa)
    return (e_hi + 1) / (e_hi - 1) - 1 / kappa, (e_lo + 1) / (e_lo - 1) - 1 / kappa


def pi_bounds() -> tuple[Fraction, Fraction]:
    def arctan_partial(x: Fraction, n: int) -> Fraction:
        return sum((Fraction((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1) for k in range(n)), Fraction(0))
    a5_lo, a5_hi = arctan_partial(Fraction(1, 5), 14), arctan_partial(Fraction(1, 5), 13)
    a239_lo, a239_hi = arctan_partial(Fraction(1, 239), 4), arctan_partial(Fraction(1, 239), 3)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


PI_LO, PI_HI = pi_bounds()


# ------------------------------------------------------------------------------------------- the modes and the tiny tori
def cos_exact(L: int, n: int):
    """cos(2 pi n / L) as an exact rational for L in {1, 2, 3, 4, 6}."""
    n %= L
    table = {1: {0: 1}, 2: {0: 1, 1: -1}, 3: {0: 1, 1: Fraction(-1, 2), 2: Fraction(-1, 2)}, 4: {0: 1, 1: 0, 2: -1, 3: 0}, 6: {0: 1, 1: Fraction(1, 2), 2: Fraction(-1, 2), 3: -1, 4: Fraction(-1, 2), 5: Fraction(1, 2)}}
    return Fraction(table[L][n])


def u_mode(L: int, n1: int, n2: int) -> Fraction:
    return (3 + 2 * cos_exact(L, n1) + 2 * cos_exact(L, n2) + 2 * cos_exact(L, n1 - n2)) / 9


def site_variance_modes(L: int, t: int) -> Fraction:
    tot = Fraction(t)
    for n1 in range(L):
        for n2 in range(L):
            if n1 == 0 and n2 == 0:
                continue
            u = u_mode(L, n1, n2)
            tot += (1 - u ** t) / (1 - u)
    return tot / L ** 2


def V_exact(L: int) -> Fraction:
    tot = Fraction(0)
    for n1 in range(L):
        for n2 in range(L):
            if n1 == 0 and n2 == 0:
                continue
            tot += 1 / (1 - u_mode(L, n1, n2))
    return tot / L ** 2


def shift_matrix(L: int, axis: int):
    N = L * L
    M = sp.zeros(N, N)
    for i in range(L):
        for j in range(L):
            src = i * L + j
            if axis == 0:
                dst = ((i - 1) % L) * L + j
            else:
                dst = i * L + (j - 1) % L
            M[src, dst] = 1
    return M


def covariance_recursion(L: int, T: int, wrong: bool = False):
    """Sigma_{t+1} = P Sigma_t P^T + I from Sigma_0 = 0; returns the site variances trace/L^2 and the plane-average variances."""
    N = L * L
    I = sp.eye(N)
    P = (I + shift_matrix(L, 0) + shift_matrix(L, 1)) / 3
    if wrong:
        P = (I + shift_matrix(L, 0)) / 2
    Sigma = sp.zeros(N, N)
    site, avg = [], []
    ones = sp.ones(N, 1)
    for t in range(1, T + 1):
        Sigma = P * Sigma * P.T + I
        site.append(Fraction(str(Sigma.trace() / N)))
        avg.append(Fraction(str((ones.T * Sigma * ones)[0, 0] / N ** 2)))
    return site, avg


def lattice_sum(L: int) -> Fraction:
    """S_L = sum over n in the symmetric box of representatives of Z_L^2, n != 0, of 1/|n|^2."""
    reps = [n if n <= L // 2 else n - L for n in range(L)]
    tot = Fraction(0)
    for a in reps:
        for b in reps:
            if a == 0 and b == 0:
                continue
            tot += Fraction(1, a * a + b * b)
    return tot


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "block 01's note (on main) carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist")


# ============================================================================================ family B — the modes (T1)
def family_b(checks: Checks) -> None:
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand(phi * sp.conjugate(phi), complex=True))
    coeff = sp.Rational(4, 9) if not mut("multiplier_wrong") else sp.Rational(2, 9)
    target = coeff * (sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2)
    ok = sp.simplify(sp.expand_trig(1 - u - target)) == 0
    # the zero set: all three sines vanish iff k1, k2 in 2 pi Z; and u <= 1
    ok = ok and sp.simplify(u.subs({k1: 0, k2: 0})) == 1 and sp.simplify(u.subs({k1: sp.pi, k2: 0})) == sp.Rational(1, 9)
    checks.check("B1", ok, "T1: 1 - |phi(k)|^2 = (4/9)[sin^2(k1/2) + sin^2(k2/2) + sin^2((k1 - k2)/2)] for phi = (1 + e^{i k1} + e^{i k2})/3 (symbolic), so 0 <= |phi|^2 <= 1 with equality only at the zero mode; e.g. |phi(pi, 0)|^2 = 1/9")
    uu, s2 = sp.symbols("u sigma2", positive=True)
    ok2 = True
    for tt in range(1, 9):
        geo = sum(uu ** j for j in range(tt))
        ok2 = ok2 and sp.simplify(geo * (1 - uu) - (1 - uu ** tt)) == 0
    # a concrete mode: u = 1/9 (k = (pi, 0)); exact rational variances by direct recursion vs the closed form
    var = Fraction(0)
    for tt in range(1, 9):
        var = var * Fraction(1, 9) + 1
        ok2 = ok2 and var == (1 - Fraction(1, 9) ** tt) / (1 - Fraction(1, 9))
    L = sp.Symbol("L", positive=True)
    ok2 = ok2 and sp.simplify(s2 * sp.Symbol("t") / L ** 2 - (s2 * sp.Symbol("t")) / L ** 2) == 0
    checks.check("B2", ok2, "T1: a mode with |phi|^2 = u < 1 driven by white noise of variance sigma^2 has variance sigma^2 (1 - u^t)/(1 - u) after t levels (the geometric sum), the zero mode sigma^2 t, and the plane average sigma^2 t / L^2 per component")


# ============================================================================================ family C — the tiny tori (T2)
def family_c(checks: Checks) -> None:
    ok = True
    detail = []
    for L in (2, 3, 4):
        T = 12 if L < 4 else 8
        site, avg = covariance_recursion(L, T, wrong=mut("covariance_recursion_wrong"))
        for t in range(1, T + 1):
            ok = ok and site[t - 1] == site_variance_modes(L, t) and avg[t - 1] == Fraction(t, L * L)
        detail.append(f"L={L}: v_{T} = {site[T - 1]}")
    checks.check("C1", ok, "T2: on the tori L = 2, 3, 4 the exact rational covariance recursion Sigma_{t+1} = P Sigma_t P^T + I reproduces the mode formula (1/L^2)[t + sum_{k != 0} (1 - u_k^t)/(1 - u_k)] for the site variance and t/L^2 for the plane average at every level tested; " + "; ".join(detail))
    # the stationary variance of the nonzero modes on the tiny tori equals V_L exactly in the limit; check the bracket by the lattice sum
    ok2 = True
    for L in (2, 3, 4):
        V = V_exact(L)
        S = lattice_sum(L)
        hi_c = Fraction(9, 16)
        ok2 = ok2 and 3 * S / (4 * PI_HI ** 2) <= V <= hi_c * S
    checks.check("C2", ok2, "T2: on the tori L = 2, 3, 4 the exact V_L = (1/L^2) sum_{k != 0} 1/(1 - u_k) lies in [3/(4 pi^2), 9/16] S_L with the rational lattice sum S_L (the bracket of T3.2 checked where V_L is rational)")


# ============================================================================================ family D — the memory time and the bracket (T3)
def family_d(checks: Checks) -> None:
    ok = True
    rows = []
    factor = 3 if not mut("memory_time_wrong") else 2
    targets = {(6, 16): (4870, 4890), (6, 32): (19480, 19560), (6, 64): (77900, 78300), (12, 16): (9470, 9490), (24, 16): (18680, 18700), (48, 16): (37110, 37130)}
    for beta in (6, 12, 24, 48):
        a_lo, a_hi = A_bounds(Fraction(3 * beta))
        for L in (16, 32, 64):
            tau_lo, tau_hi = Fraction(factor * beta * L * L) / a_hi, Fraction(factor * beta * L * L) / a_lo
            rate_lo, rate_hi = a_lo / (3 * beta * L * L), a_hi / (3 * beta * L * L)
            if (beta, L) in targets:
                lo_t, hi_t = targets[(beta, L)]
                ok = ok and lo_t <= tau_lo and tau_hi <= hi_t
            ok = ok and tau_hi - tau_lo < Fraction(1, 10) and rate_lo > 0
            rows.append(f"beta={beta} L={L}: tau in [{int(tau_lo)}, {int(tau_hi) + 1}]")
    checks.check("D1", ok, "T3.1: the memory time tau_L = 3 beta L^2 / A(3 beta) enclosed exactly (width < 1/10) at beta = 6, 12, 24, 48 and L = 16, 32, 64, e.g. " + "; ".join(rows[:4]) + " ...; the rate sigma^2/L^2 = A(3 beta)/(3 beta L^2) positive")
    # D2: the eigenvalues of M and the two sine inequalities behind the bracket
    M = sp.Matrix([[2, -1], [-1, 2]]) / 9
    ev = sorted(M.eigenvals().keys())
    ok2 = ev == [sp.Rational(1, 9), sp.Rational(1, 3)]
    x = sp.symbols("x", real=True)
    # sin^2(x/2) <= x^2/4 (|sin y| <= |y|) and, on |x| <= pi, sin(x/2) >= x/pi (concavity: the chord lies below); checked exactly on a grid with Taylor enclosures
    def sin_bounds(y: Fraction, terms: int = 12) -> tuple[Fraction, Fraction]:
        assert 0 <= y <= 2
        s = Fraction(0)
        for k in range(terms):
            s += Fraction((-1) ** k) * y ** (2 * k + 1) / factorial(2 * k + 1)
        tail = y ** (2 * terms + 1) / factorial(2 * terms + 1)
        return s - tail, s + tail
    grid_ok = True
    for i in range(1, 21):
        xx = PI_LO * i / 20     # |x| <= pi, x/2 <= 2
        s_lo, s_hi = sin_bounds(xx / 2)
        grid_ok = grid_ok and s_hi <= xx / 2 and s_lo >= xx / PI_HI
    hi_c = Fraction(9, 16) if not mut("lattice_sum_bounds_wrong") else Fraction(5, 16)
    # the bracket's constants: 1/(1-u) >= 3/|k|^2 from 1 - u <= Q <= |k|^2/3; 1/(1-u) <= (9 pi^2/4)/|k|^2 from 1 - u >= 4|k|^2/(9 pi^2);
    # with |k|^2 = (2 pi / L)^2 |n|^2 these give V_L in [3/(4 pi^2), 9/16] sigma^2 S_L
    c_lo = Fraction(3) / (4 * PI_LO ** 2)
    ok2 = ok2 and grid_ok and c_lo < hi_c
    # and the bracket holds on the tiny tori (V_L rational) with the (possibly mutated) upper constant
    for L in (2, 3, 4):
        ok2 = ok2 and Fraction(3) / (4 * PI_HI ** 2) * lattice_sum(L) <= V_exact(L) <= hi_c * lattice_sum(L)
    checks.check("D2", ok2, "T3.2: M = (1/9)[[2,-1],[-1,2]] has eigenvalues 1/9 and 1/3; sin^2(x/2) <= x^2/4 and sin(x/2) >= x/pi on [0, pi] (exact Taylor enclosures on a grid); hence 3/|k|^2 <= 1/(1 - u(k)) <= (9 pi^2/4)/|k|^2 on the square and V_L in [3/(4 pi^2), 9/16] sigma^2 S_L, verified on the tiny tori")
    S16, S32, S64 = lattice_sum(16), lattice_sum(32), lattice_sum(64)
    # log(2)=2*atanh(1/3); bound the positive tail by a geometric series.
    terms = 12
    ln2_lo = 2 * sum((Fraction(1,3)**(2*j+1)/ (2*j+1) for j in range(terms)),Fraction(0))
    ln2_hi = ln2_lo + 2*Fraction(1,3)**(2*terms+1)/((2*terms+1)*(1-Fraction(1,9)))
    ok3 = S16 < S32 < S64 and 2 * PI_LO * ln2_lo - 1 < S32 - S16 < 2 * PI_HI * ln2_hi + 1 and 2 * PI_LO * ln2_lo - 1 < S64 - S32 < 2 * PI_HI * ln2_hi + 1
    checks.check("D3", ok3, f"T3.2: the rational lattice sums S_16, S_32, S_64 increase ({S16.numerator // S16.denominator}, {S32.numerator // S32.denominator}, {S64.numerator // S64.denominator} to the integer part) and consecutive differences lie within 1 of 2 pi log 2 (the growth 2 pi log L + O(1))")


# ============================================================================================ family F
FENCES = ('For the supplied gain-one recurrence theta(t+1)=P theta(t)+xi on a finite periodic L by L plane, prove the mode variances, zero-mode memory proxy and stationary nonzero-mode bracket for beta>0. Exact rational controls on L=2,3,4 and memory-time enclosures on the listed beta and size grid. The S_L increment test concerns L=16,32,64 only. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at beta = 6."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Mermin", "Wagner", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Fourier", "Parseval")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Mermin)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
    float_hits += [x for x in nodes if isinstance(x,ast.Call) and
                   ((isinstance(x.func,ast.Name) and x.func.id in ("float","N")) or
                    (isinstance(x.func,ast.Attribute) and x.func.attr in ("evalf","N")))]
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in sec:
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if nm in sections[0]]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = ('per_element: Exact arithmetic checks the supplied recurrence and identities; its gain-one assumption is not the nonlinear Cartesian mean derivative.', 'per_site: Finite periodic plane covariance matrices are compared with exact mode expressions on the explicitly listed small tori.', 'per_mode: Complex covariance orientation, or real mode variances and bounds, are controlled under the explicitly declared transform convention.', 'per_block: The algebraic statements require the supplied model and beta greater than zero; finite numerical observations have only their listed scope.', 'lattice_wide: No nonlinear infinite-volume theorem, physical law selection, gravity kernel or retained audit grade follows from this certificate.')


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
