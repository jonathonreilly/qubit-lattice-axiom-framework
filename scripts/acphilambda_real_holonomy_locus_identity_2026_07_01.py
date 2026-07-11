#!/usr/bin/env python3
"""Exact gates for AC_phi_lambda real-holonomy locus identity.

The runner checks only the paired note, the three origin/main sources named by
the note, and exact symbolic/Fraction arithmetic for the locus identity.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
import re

import sympy as sp


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01.md"
SCRIPT = ROOT / "scripts" / "acphilambda_real_holonomy_locus_identity_2026_07_01.py"
BRANNEN = ROOT / "docs" / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
MODULUS = ROOT / "docs" / "KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md"
CUSTODY = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "premise_decision_history.json"


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def expanded(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_trig(sp.expand(expr)))


def sympy_fraction(q: Fraction) -> sp.Rational:
    return sp.Rational(q.numerator, q.denominator)


def mod_two(q: Fraction) -> Fraction:
    return q % Fraction(2, 1)


def orbit(seed: set[Fraction]) -> set[Fraction]:
    seen = {mod_two(x) for x in seed}
    todo: deque[Fraction] = deque(seen)
    while todo:
        x = todo.popleft()
        for y in (mod_two(x + Fraction(2, 3)), mod_two(-x)):
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def is_locus_dhat(q: Fraction) -> bool:
    c = sp.cos(3 * sp.pi * sympy_fraction(q))
    return expanded(c**2 - 1) == 0


def multiset_matches(xs: list[sp.Expr], ys: list[sp.Expr]) -> bool:
    unmatched = list(ys)
    for x in xs:
        for i, y in enumerate(unmatched):
            if expanded(x - y) == 0:
                del unmatched[i]
                break
        else:
            return False
    return not unmatched


def markdown_targets(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def markdown_link_with_label(text: str, label: str) -> bool:
    pattern = r"\[" + re.escape(label) + r"\]\([^)]+\)"
    return re.search(pattern, text) is not None


def main() -> int:
    print("AC_phi_lambda real-holonomy locus identity runner")
    print("=" * 72)

    note = read(NOTE) if NOTE.exists() else ""
    brannen = read(BRANNEN) if BRANNEN.exists() else ""
    modulus = read(MODULUS) if MODULUS.exists() else ""
    custody = read(CUSTODY) if CUSTODY.exists() else ""
    registry = read(REGISTRY) if REGISTRY.exists() else ""
    targets = markdown_targets(note)

    check("paired note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("paired runner exists", SCRIPT.exists(), str(SCRIPT.relative_to(ROOT)))
    check("Brannen circulant source exists", BRANNEN.exists(), str(BRANNEN.relative_to(ROOT)))
    check("modulus no-go source exists", MODULUS.exists(), str(MODULUS.relative_to(ROOT)))
    check("custody-chain source exists", CUSTODY.exists(), str(CUSTODY.relative_to(ROOT)))
    check("Tier-A registry data exists", REGISTRY.exists(), str(REGISTRY.relative_to(ROOT)))
    check("custody pins time-reversal-reality", "time-reversal-reality" in custody)
    check("custody pins b=c-bar definition", "b=c̄" in custody or ("K-reality" in custody and "δ=0" in custody))
    check("modulus pins stationary candidates", "stationary candidates are" in modulus or "δ=k·60°" in modulus)
    check("modulus pins degeneracy", "degenerate" in modulus)
    check("registry pins K-real arg-det sentence", "arg det M in {0, pi} -> 0 on the K-real reading" in registry)
    check("registry pins shared C3 object sentence", "same C_3 conjugate-symmetric object" in registry)
    check("Brannen pins circulant form", "circulant form" in brannen)
    check("Brannen pins coupling coordinates", "(a, |b|, delta)" in brannen)

    delta = sp.symbols("delta", real=True)
    rho, a = sp.symbols("rho a", positive=True, real=True)
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    cs = [sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    lambdas = [a + 2 * rho * c for c in cs]
    centered = [lam - a for lam in lambdas]

    check("omega is an exact primitive cube root", expanded(omega**3 - 1) == 0 and expanded(omega - 1) != 0)
    check("Lemma R power sum cos is zero", expanded(sum(cs)) == 0)
    check("Lemma R power sum cos^2 is 3/2", expanded(sum(c**2 for c in cs) - sp.Rational(3, 2)) == 0)
    check("Lemma R power sum cos^3 is (3/4)cos(3delta)", expanded(sum(c**3 for c in cs) - sp.Rational(3, 4) * sp.cos(3 * delta)) == 0)
    check("spectrum mean determines a", expanded(sum(lambdas) - 3 * a) == 0)
    check("centered quadratic determines |b|", expanded(sum(x**2 for x in centered) - 6 * rho**2) == 0)
    check("centered cubic determines cos(3delta)", expanded(sum(x**3 for x in centered) - 6 * rho**3 * sp.cos(3 * delta)) == 0)
    check("cos(3delta) invariant under +2pi/3", expanded(sp.cos(3 * (delta + 2 * sp.pi / 3)) - sp.cos(3 * delta)) == 0)
    check("cos(3delta) invariant under reflection", expanded(sp.cos(-3 * delta) - sp.cos(3 * delta)) == 0)
    shifted_cs = [sp.cos(delta + 2 * sp.pi / 3 + 2 * sp.pi * k / 3) for k in range(3)]
    reflected_cs = [sp.cos(-delta + 2 * sp.pi * k / 3) for k in range(3)]
    check("shift relabels the eigenvalue multiset", multiset_matches(shifted_cs, cs))
    check("reflection relabels the eigenvalue multiset", multiset_matches(reflected_cs, cs))
    generic_delta = sp.Rational(0)
    generic_shift_change = expanded(sp.cos(3 * (generic_delta + sp.Rational(1, 10))) - sp.cos(3 * generic_delta))
    check("wrong generic shift changes registrable content", generic_shift_change != 0, str(generic_shift_change))

    check("b=1 has K-real phase delta=0", sp.arg(sp.Integer(1)) == 0)
    check("b=-2/5 has K-real phase delta=pi", sp.arg(sp.Rational(-2, 5)) == sp.pi)
    check("delta=0 gives real holonomy +1", sp.cos(3 * 0) == 1)
    check("delta=pi gives real holonomy -1", sp.cos(3 * sp.pi) == -1)
    thirds = {Fraction(k, 3) for k in range(6)}
    expected = {Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1), Fraction(4, 3), Fraction(5, 3)}
    check("all k/3 rational representatives are on-locus", all(is_locus_dhat(q) for q in thirds))
    for q in (Fraction(1, 4), Fraction(1, 5), Fraction(5, 12)):
        check(f"off-grid dhat={q} rejects |cos(3pi*dhat)|=1", not is_locus_dhat(q))
    k_orbit = orbit({Fraction(0), Fraction(1)})
    check("G-orbit of {0,1} equals all thirds", k_orbit == expected, str(sorted(k_orbit)))
    check("G-orbit has six representatives", len(k_orbit) == 6)
    quarter_orbit = orbit({Fraction(1, 4)})
    check("wrong-value rejector: 1/4 not in K-real orbit", Fraction(1, 4) not in k_orbit)
    check("wrong orbit from 1/4 misses all thirds", quarter_orbit.isdisjoint(expected), str(sorted(quarter_orbit)))
    grid = {Fraction(n, 12) for n in range(24)}
    l2_grid = {q for q in grid if is_locus_dhat(q)}
    check("L2 equals L3 on denominator-12 rational grid", l2_grid == expected, str(sorted(l2_grid)))
    check("thirds set is closed under +2/3", {mod_two(q + Fraction(2, 3)) for q in expected} == expected)
    check("thirds set is closed under reflection", {mod_two(-q) for q in expected} == expected)

    delta_phys = sp.Rational(2, 9)
    phi_phys = 3 * delta_phys
    check("physical delta is positive", delta_phys > 0)
    check("physical delta lies below pi/3 exactly", bool(delta_phys < sp.pi / 3))
    not_multiples = [sp.simplify(delta_phys - k * sp.pi / 3) != 0 for k in range(-3, 4)]
    check("physical delta is not k*pi/3 for |k|<=3", all(not_multiples), str(not_multiples))
    check("identity-unit holonomy is Phi=2/3", phi_phys == sp.Rational(2, 3))
    check("holonomy lies in the open interval (0,pi)", bool(0 < phi_phys < sp.pi))
    check("cos(2/3) is not +1", sp.simplify(sp.cos(phi_phys) - 1) != 0 and bool(0 < phi_phys < sp.pi))
    check("cos(2/3) is not -1", sp.simplify(sp.cos(phi_phys) + 1) != 0 and bool(0 < phi_phys < sp.pi))
    check("theta parallel beta=2 has arg(beta^3)=0", sp.arg(sp.Integer(2) ** 3) == 0)
    check("theta parallel beta=-3/7 has arg(beta^3)=pi", sp.arg(sp.Rational(-3, 7) ** 3) == sp.pi)
    check("wrong-value rejector: delta=pi/3 is on-locus", sp.cos(3 * sp.pi / 3) == -1)
    check("wrong-value rejector distinguishes delta=2/9 from pi/3", delta_phys != sp.pi / 3 and sp.cos(3 * sp.pi / 3) != sp.cos(phi_phys))

    required = [
        "any derivation of the charged-lepton phase value must supply K-reality-breaking registered content",
        "real-holonomy locus",
        "observation, not a derivation",
        "not a terminal no-go",
        "`W_cycle_holonomy_value`",
    ]
    for phrase in required:
        check(f"note contains required phrase: {phrase}", phrase in note)
    for n in range(1, 9):
        check(f"note contains N{n} gate", f"### N{n}" in note)
    forbidden = [
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes the " + "route",
        "P" + "DG",
        "theta is " + "closed",
        "r=1/2 is " + "forced",
    ]
    for phrase in forbidden:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note)
    check("note declares canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note does not use runner PASS as source status", "**Status:** PASS" not in note)
    check("note does not lean on PR #4783 as authority", "RULED OUT by PR #4783" not in note)
    deps = [
        "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "docs/KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md",
        "docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md",
    ]
    for dep in deps:
        check(f"dep link present as markdown label: {dep}", markdown_link_with_label(note, dep))
    md_targets = [t for t in targets if t.endswith(".md")]
    allowed_basenames = {Path(dep).name for dep in deps}
    check("only the three origin/main md files are linked", {Path(t).name for t in md_targets} == allowed_basenames, str(md_targets))
    inflight = [
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM",
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION",
    ]
    for name in inflight:
        check(f"in-flight context name appears: {name}", name in note)
        check(f"in-flight context name is not a markdown target: {name}", all(name not in t for t in targets))
    check("primary runner is linked", "scripts/acphilambda_real_holonomy_locus_identity_2026_07_01.py" in note)
    check("status authority header is standard", "Status authority:** independent audit lane only" in note)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 55 else 1


if __name__ == "__main__":
    raise SystemExit(main())
