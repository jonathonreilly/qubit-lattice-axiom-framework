#!/usr/bin/env python3
"""Exact checks: at the neutral scale on the sphere menu, moving records have no long-range order for
z < z1(beta) = (1 - e^(-2 beta))^2/(144 beta^2), which falls only as beta^-2 (the supervisor's own derivation, unrefereed).
Block 126's law with vacancies as landed; the occupied set is a gas of connected clusters whose weight is z^|A| times the
contents' integral; at the neutral scale a spanning tree integrates to 1, and each extra bond costs at most c0 e^beta.

A (premises): landed block 126's menus, scales and kernel; the axioms.
B (T1): the tree integral is 1 at the neutral scale; c0 e^beta = 2 beta/(1 - e^(-2 beta)); extra bonds |E(A)| - |A| + 1 <= 2|A| + 1.
C (T2): exact site-animal counts on Z^3 through n = 6 against 36^(n-1); the series sum; on a ring of six with the two-valued
   neutral kernel, the probability that a connected set is the origin's cluster never exceeds its weight (full enumeration).
D (T3): the region z1(beta): its limit 1/36 as beta -> 0, beta^2 z1 -> 1/144, and z1 (4 F_6) ~ (4/27) beta^3 against block 168.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ON_THE_SPHERE_AT_THE_NEUTRAL_SCALE_MOVING_RECORDS_HAVE_NO_LONG_RANGE_ORDER_BELOW_A_DENSITY_FALLING_ONLY_AS_BETA_TO_MINUS_TWO_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_LONG_RANGE_ORDER_ABOVE_THE_NEUTRAL_SCALE_AND_NO_FULL_BOUND_AT_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_only_as_beta_to_minus_two_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    "`c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued)",
    "The sphere menu has `s ∈ S²` with the uniform measure",
    "`B(s, s') = c e^{βs·s'}`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "tree_integral_forged": "B",
    "animal_bound_forged": "C",
    "region_limit_forged": "D",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
beta, r, th = sp.symbols("beta r theta", positive=True)
STEPS3 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def animals(nmax: int):
    """connected site sets of Z^3 containing the origin, by size (exact enumeration by growth)"""
    origin = (0, 0, 0)
    levels = [set(), {frozenset([origin])}]
    for n in range(2, nmax + 1):
        nxt = set()
        for A in levels[-1]:
            for x in A:
                for e in STEPS3:
                    y = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
                    if y not in A:
                        nxt.add(A | {y})
        levels.append(nxt)
    return levels


def edges_in(A) -> int:
    return sum(1 for x in A for e in STEPS3[::2] if (x[0] + e[0], x[1] + e[1], x[2] + e[2]) in A)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the law with vacancies, its weights and the menus are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[0] = "`c₀(γ) = γ/cosh γ` (sphere) or `1/cosh γ` (two-valued)"
    checks.check("A3", all(n in landed for n in needles), "landed block 126: c0(gamma) = gamma/sinh gamma (sphere); the sphere menu with the uniform measure; B(s, s') = c e^(beta s.s')")


# ============================================================================================ family B (T1)
def family_b(checks: Checks, levels) -> None:
    c0 = beta / sp.sinh(beta)
    leaf = sp.integrate(sp.exp(beta * sp.cos(th)) * sp.sin(th), (th, 0, sp.pi)) / 2
    target = 1 if not mut("tree_integral_forged") else 2
    ok1 = sp.simplify((c0 * leaf - target).rewrite(sp.exp)) == 0
    ok1 = ok1 and sp.simplify((c0 * sp.exp(beta) - 2 * beta / (1 - sp.exp(-2 * beta))).rewrite(sp.exp)) == 0
    checks.check("B1", ok1, "at the neutral scale c0 = beta/sinh beta a leaf integrates out: c0 <e^(beta s.s')> = 1 for any unit s', so a spanning tree's bonds integrate to exactly 1; each other bond is at most c0 e^beta = 2 beta/(1 - e^(-2 beta))")
    worst = max((edges_in(A) - len(A) + 1) - (2 * len(A) + 1) for n in range(1, len(levels)) for A in levels[n])
    checks.check("B2", worst <= 0, f"an induced connected set A of Z^3 has |E(A)| <= 3|A| bonds (degree 6), so at most 2|A| + 1 bonds lie off a spanning tree (checked on every set through n = {len(levels) - 1}; worst excess {worst})")


# ============================================================================================ family C (T2)
def family_c(checks: Checks, levels) -> None:
    counts = [len(levels[n]) for n in range(1, len(levels))]
    bound = (lambda n: 36 ** (n - 1)) if not mut("animal_bound_forged") else (lambda n: 6 ** (n - 1))
    ok1 = counts == [1, 6, 45, 344, 2670, 20886][:len(counts)] and all(c <= bound(n) for n, c in enumerate(counts, start=1))
    xx = sp.Symbol("x")
    ok1 = ok1 and all(sp.expand((1 - xx) ** 2 * sum(n * xx ** (n - 1) for n in range(1, N + 1)) - (1 - (N + 1) * xx ** N + N * xx ** (N + 1))) == 0 for N in range(1, 11))
    checks.check("C1", ok1, f"connected site sets of Z^3 containing the origin: {counts} for n = 1..{len(counts)}, within 36^(n-1) (a spanning tree's closed walk of 2(n-1) steps determines the set); (1 - x)^2 sum_(n <= N) n x^(n-1) = 1 - (N+1) x^N + N x^(N+1), so sum_n n 36^(n-1) zeta^n = zeta/(1 - 36 zeta)^2 for 36 zeta < 1")
    # C2: on a ring of six with the two-valued neutral kernel 1 + t s s' (t = 1/2) and z = 1/3, the origin's cluster A has
    # P(cluster of 0 = A) <= w(A) = z^|A| sum_contents prod_(bonds in A)(1 + t s s')
    V, t, z = 6, Fr(1, 2), Fr(1, 3)
    states = [None, 1, -1]
    Zsum = Fr(0)
    Pcl: dict = {}

    def weight(cfg):
        w = Fr(1)
        for x in range(V):
            if cfg[x] is not None:
                w *= z
        for x in range(V):
            y = (x + 1) % V
            if cfg[x] is not None and cfg[y] is not None:
                w *= 1 + t * cfg[x] * cfg[y]
        return w

    def cluster0(cfg):
        if cfg[0] is None:
            return None
        A = {0}
        for d_ in (1, -1):
            x = 0
            while True:
                x = (x + d_) % V
                if cfg[x] is None or x in A:
                    break
                A.add(x)
        return frozenset(A)

    for cfg in itertools.product(states, repeat=V):
        w = weight(cfg)
        Zsum += w
        A = cluster0(cfg)
        if A is not None:
            Pcl[A] = Pcl.get(A, Fr(0)) + w
    ok2 = True
    for A, pw in Pcl.items():
        As = sorted(A)
        wA = Fr(0)
        for contents in itertools.product((1, -1), repeat=len(As)):
            cfg = {x: s for x, s in zip(As, contents)}
            wa = z ** len(As)
            for x in As:
                y = (x + 1) % V
                if y in cfg:
                    wa *= 1 + t * cfg[x] * cfg[y]
            wA += wa
        ok2 = ok2 and pw / Zsum <= wA
    checks.check("C2", ok2 and len(Pcl) > 0, f"the cluster gas: on a ring of six, two-valued neutral kernel (t = 1/2, z = 1/3, full enumeration of 3^6 configurations), every connected set A containing the origin has P(A is the origin's cluster) <= w(A) ({len(Pcl)} sets)")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    c0e = 2 * beta / (1 - sp.exp(-2 * beta))
    z1 = 1 / (36 * c0e ** 2)
    ok = sp.simplify(z1 - (1 - sp.exp(-2 * beta)) ** 2 / (144 * beta ** 2)) == 0
    want0 = sp.Rational(1, 36) if not mut("region_limit_forged") else sp.Rational(1, 4)
    ok = ok and sp.limit(z1, beta, 0) == want0 and sp.limit(beta ** 2 * z1, beta, sp.oo) == sp.Rational(1, 144)
    F6 = (beta / sp.sinh(beta)) ** 6 * sp.sinh(6 * beta) / (6 * beta)
    ratio = sp.limit(((z1 * 4 * F6) / beta ** 3).rewrite(sp.exp), beta, sp.oo)
    ok = ok and ratio == sp.Rational(4, 27)
    checks.check("D1", ok, "z1(beta) = 1/(36 (c0 e^beta)^2) = (1 - e^(-2 beta))^2/(144 beta^2): 1/36 as beta -> 0 and ~ 1/(144 beta^2) as beta -> oo; against block 168's 1/(4 F_6) the ratio z1 (4 F_6) is ~ (4/27) beta^3, so the new region is larger at large beta")


# ============================================================================================ family F
FENCES = (
    "This note works within block 126 as landed on main (the law with vacancies, its sphere menu and its neutral scale) and places block 168 (a pushed branch); it reports a density below which moving records on the sphere at the neutral scale have no long-range order; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at z1(beta)."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Kotecký", "Preiss",
                   "Mayer", "Peierls", "Ising", "Heisenberg", "Ruelle", "Dobrushin", "Harris")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Peierls) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
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
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the leaf integral and the largest bond weight at the neutral scale",
    "per_site: executed - the bound on bonds off a spanning tree for every connected set through n = 6",
    "per_mode: executed - exact site-animal counts through n = 6 against 36^(n-1); the series sum",
    "per_block: executed - the cluster-gas inequality by full enumeration on a ring of six; the region's limits and its ratio to block 168's",
    "lattice_wide: checked and not executed - the window between low and high density; the sphere at high density",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    levels = animals(6)
    family_a(checks, texts)
    family_b(checks, levels)
    family_c(checks, levels)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 126's law with vacancies on the sphere at the neutral scale: the occupied clusters form a gas with weights at most c0 e^beta (z (c0 e^beta)^2)^|A|, so no long-range order for z < (1 - e^(-2 beta))^2/(144 beta^2); the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
