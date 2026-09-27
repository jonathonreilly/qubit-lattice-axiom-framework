#!/usr/bin/env python3
"""Exact checks: block 184's stretch rule (pushed; k = k0 + ((l^2 - 1)/2) sin 2k0, u = F^2 with du/dk = sin 2k0) is, with M = 2k,
E = 2k0 and e = 1 - l^2, the relation M = E - e sin E with du/dk = sin E. (T1) The hops of du/dk are b_n = (2/(n e)) J_n(n e) (the
classical series; checked here through order e^7 by exact inversion). (T2) The nearest singularity of E(M) off the real line is the
fold cos E = 1/e, at Im M = kappa = arccosh(1/|e|) - sqrt(1 - e^2); so u is analytic for |Im k| < kappa/2 and its hops of range 2n
decay like exp(-n kappa). (T3) kappa > 0 for 0 < |e| < 1 (every 0 < l^2 < 2 except l = 1, where the reach is finite), kappa depends
only on |e| (a stretch and a compression with the same |1 - l^2| are equally local), kappa = ln(2/|e|) - 1 + O(e^2) near l = 1 and
kappa = s^3/3 + s^5/5 + ... with s = sqrt(1 - e^2) near the ends l -> 0 and l -> sqrt 2, where the decay length diverges. The
supervisor's own derivation, unrefereed. Block 69 as landed; block 184 (pushed) placed and the facts used re-derived.

A (premises): landed block 69; the axioms.
B (T1): the map from block 184's rule; exact inversion of M = E - e sin E through e^7 and the series of (2/(n e)) J_n(n e).
C (T2): the fold: 1 - e cos E = 0 at E = i arccosh(1/e) gives M = i(arccosh(1/e) - sqrt(1 - e^2)); the negative-e case at E = pi + ...
D (T3): positivity and monotonicity of kappa in 1/|e|; the two limits.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_STRETCH_RULES_HOPS_DECAY_EXPONENTIALLY_BELOW_ROOT_TWO_AND_ITS_DECAY_LENGTH_DIVERGES_ONLY_AT_THE_RULES_ENDS_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_stretch_rules_hops_decay_exponentially_below_root_two_and_its_decay_length_diverges_only_at_the_rules_ends_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "series_forged": "B",
    "fold_forged": "C",
    "limit_forged": "D",
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
e = sp.Symbol("e", real=True)
M = sp.Symbol("M", real=True)
L = sp.Symbol("l", positive=True)
k0 = sp.Symbol("k0", real=True)
ORDER = 7


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk and its stretch rule are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = needles[1].replace("do not determine", "determine")
    checks.check("A3", all(n in t69 for n in needles), "landed block 69: the uniform form, and no completion fixed by the leading order")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # the map: 2k = 2k0 - (1 - l^2) sin 2k0 is M = E - e sin E with M = 2k, E = 2k0, e = 1 - l^2; du/dk = sin 2k0 = sin E
    kk = k0 + (L ** 2 - 1) / 2 * sp.sin(2 * k0)
    ok_map = sp.simplify(2 * kk - (2 * k0 - (1 - L ** 2) * sp.sin(2 * k0))) == 0
    # exact inversion by the inversion series: sin E = sin M + sum_m e^m/m! d^{m-1}/dM^{m-1}[sin^m M cos M]
    sinE = sp.sin(M)
    for m in range(1, ORDER + 1):
        sinE += e ** m / sp.factorial(m) * sp.diff(sp.sin(M) ** m * sp.cos(M), M, m - 1)
    sinE = sp.expand(sp.fu(sp.expand(sinE)))
    # compare with sum_n (2/(n e)) J_n(n e) sin(n M), each J_n(n e) as a series in e through e^(ORDER + 1)
    series = 0
    for n in range(1, ORDER + 2):
        jn = sp.series(sp.besselj(n, n * e), e, 0, ORDER + 2).removeO()
        bn = sp.expand(2 * jn / (n * e))
        if mut("series_forged") and n == 2:
            bn = bn * 2
        series += bn * sp.sin(n * M)
    diff = sp.expand(sp.expand_trig(sinE - series))
    # keep only terms through e^ORDER
    diff = sp.series(diff, e, 0, ORDER + 1).removeO() if diff != 0 else 0
    ok_ser = sp.simplify(sp.expand_trig(diff)) == 0
    checks.check("B1", ok_map, "block 184's rule k = k0 + ((l^2 - 1)/2) sin 2k0 is M = E - e sin E with M = 2k, E = 2k0, e = 1 - l^2, and du/dk = sin 2k0 = sin E")
    checks.check("B2", ok_ser, f"exact inversion of M = E - e sin E gives sin E = sum_n (2/(n e)) J_n(n e) sin(n M) through order e^{ORDER}: the hops of du/dk are b_n = (2/(n e)) J_n(n e)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    ep = sp.Symbol("ep", positive=True)
    y = 1 / ep
    Es = sp.I * sp.acosh(y)
    fold = sp.simplify(1 - ep * sp.cos(Es))
    Ms = sp.simplify(sp.expand_complex(Es - ep * sp.sin(Es)))
    want = sp.I * (sp.acosh(1 / ep) - sp.sqrt(1 - ep ** 2))
    if mut("fold_forged"):
        want = sp.I * (sp.acosh(1 / ep) - (1 - ep ** 2))
    okp = fold == 0 and sp.simplify((Ms - want).subs(ep, sp.Rational(1, 2))) == 0 and sp.simplify((Ms - want).subs(ep, sp.Rational(1, 3))) == 0
    # negative e: E = pi + i arccosh(1/|e|) solves 1 - e cos E = 0, and M = pi + i(arccosh(1/|e|) - sqrt(1 - e^2))
    en = -ep
    En = sp.pi + sp.I * sp.acosh(1 / ep)
    foldn = sp.simplify(sp.expand_complex(1 - en * sp.cos(En)))
    Mn = sp.expand_complex(En - en * sp.sin(En))
    okn = foldn == 0 and all(sp.simplify((sp.im(Mn) - (sp.acosh(1 / ep) - sp.sqrt(1 - ep ** 2))).subs(ep, v_)) == 0 for v_ in (sp.Rational(1, 2), sp.Rational(1, 3)))
    checks.check("C1", okp and okn, "the fold 1 - e cos E = 0 lies at E = i arccosh(1/e) (0 < e < 1) or E = pi + i arccosh(1/|e|) (-1 < e < 0), where Im M = kappa = arccosh(1/|e|) - sqrt(1 - e^2): the nearest singularity of E(M), so u is analytic for |Im k| < kappa/2 and its hops of range 2n decay like exp(-n kappa)")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    yv = sp.Symbol("y", positive=True)
    kap = sp.acosh(yv) - sp.sqrt(1 - 1 / yv ** 2)
    dk = sp.simplify(sp.diff(kap, yv))
    ok_mono = sp.simplify(dk - sp.sqrt(yv ** 2 - 1) / yv ** 2) == 0 and sp.simplify(kap.subs(yv, 1)) == 0
    # near the ends: with s = sqrt(1 - e^2), arccosh(1/e) = artanh(s), so kappa = artanh(s) - s = s^3/3 + s^5/5 + ...
    s = sp.Symbol("s", positive=True)
    ok_ends = sp.simplify(sp.acosh(1 / sp.sqrt(1 - s ** 2)) - sp.atanh(s)).subs(s, sp.Rational(1, 2)) == 0 or sp.simplify(sp.cosh(sp.atanh(s)) - 1 / sp.sqrt(1 - s ** 2)) == 0
    ser = sp.series(sp.atanh(s) - s, s, 0, 7).removeO()
    want = s ** 3 / 3 + s ** 5 / 5
    if mut("limit_forged"):
        want = s ** 3 / 2 + s ** 5 / 5
    ok_ser = sp.expand(ser - want) == 0
    # near l = 1: kappa = ln(2/|e|) - 1 + O(e^2)
    ep = sp.Symbol("ep", positive=True)
    # arccosh(1/ep) = ln((1 + sqrt(1 - ep^2))/ep), so kappa - (ln(2/ep) - 1) = ln((1 + sqrt(1 - ep^2))/2) + 1 - sqrt(1 - ep^2) = O(ep^2)
    xx = (1 + sp.sqrt(1 - ep ** 2)) / ep
    ok_log = sp.simplify(sp.radsimp(xx + 1 / xx) - 2 / ep) == 0  # cosh(log x) = 1/ep with x >= 1, so arccosh(1/ep) = log x
    rest = sp.log((1 + sp.sqrt(1 - ep ** 2)) / 2) + 1 - sp.sqrt(1 - ep ** 2)
    near = sp.series(rest, ep, 0, 2).removeO()
    ok_near = ok_log and sp.simplify(near) == 0
    checks.check("D1", ok_mono and ok_ends and ok_ser and ok_near, "kappa(y) = arccosh(y) - sqrt(1 - 1/y^2), y = 1/|e|, vanishes at y = 1 and has derivative sqrt(y^2 - 1)/y^2 > 0: kappa > 0 for 0 < |e| < 1 and depends on |e| only; near l = 1, kappa = ln(2/|e|) - 1 + O(e^2) (finite reach at l = 1); near the ends |e| -> 1 (l -> 0 or sqrt 2), kappa = s^3/3 + s^5/5 + ... with s = sqrt(1 - e^2), so the decay length diverges like 3/s^3")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = sqrt 2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Carlini", "Debye")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Kepler) —", 1)
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
    "per_element: executed - the map from block 184's rule to the inversion relation",
    "per_site: executed - the inversion series through e^7 against the series of (2/(n e)) J_n(n e)",
    "per_mode: executed - the fold's location for both signs of e",
    "per_block: executed - positivity, monotonicity and the two limits of the decay rate",
    "lattice_wide: checked and not executed - the exact decay rates of the walk's own hops F and E (extra branch points where sin^2 k0 + l^2 cos^2 k0 = 0); the asymptotic form of J_n(n e) (named import)",
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
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 184's stretch rule is the inversion relation M = E - e sin E; the hops of its squared energy's slope are (2/(n e)) J_n(n e), decaying like exp(-n kappa) with kappa = arccosh(1/|e|) - sqrt(1 - e^2) > 0 for 0 < l^2 < 2, l != 1; the decay length diverges only at the rule's ends; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
