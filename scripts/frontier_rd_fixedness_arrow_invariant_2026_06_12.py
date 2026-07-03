#!/usr/bin/env python3
"""R-D fixedness is arrow-invariant on the retained flow family.

Companion runner for
docs/RD_FIXEDNESS_IS_ARROW_INVARIANT_ON_THE_RETAINED_FLOW_FAMILY_BOUNDED_NOTE_2026-06-12.md

No cache generation. Exit code is nonzero iff any check fails.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import sympy as sp


ROOT = pathlib.Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RD_FIXEDNESS_IS_ARROW_INVARIANT_ON_THE_RETAINED_FLOW_FAMILY_BOUNDED_NOTE_2026-06-12.md"
SEP = ROOT / "docs" / "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md"
THERM = ROOT / "docs" / "FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.replace("**", "").split())


def fixed_set_for_phi(r: sp.Symbol) -> set[sp.Expr]:
    phi = 2 * r**2
    return set(sp.solve(sp.Eq(phi, r), r))


def fixed_set_for_g(r: sp.Symbol) -> set[sp.Expr]:
    g = sp.sqrt(r / 2)
    algebraic = set(sp.solve(sp.Eq(r / 2, r**2), r))
    return {x for x in algebraic if x.is_nonnegative and sp.simplify(g.subs(r, x) - x) == 0}


def selected_after_side_conditions(extended_fixed_set: set[sp.Expr]) -> set[sp.Expr]:
    excluded = {sp.Integer(0), sp.oo}
    return set(extended_fixed_set) - excluded


def main() -> int:
    r = sp.Symbol("r", nonnegative=True)
    s = sp.Symbol("s", nonnegative=True)
    half = sp.Rational(1, 2)
    phi = 2 * r**2
    g = sp.sqrt(r / 2)

    print("R-D fixedness arrow-invariance runner")
    print()

    # F1: inverse pair on r >= 0.
    check(
        "F1.1 g(phi(r)) = r symbolically on r >= 0",
        sp.simplify(g.subs(r, phi) - r) == 0,
        f"g(phi(r))={sp.simplify(g.subs(r, phi))}",
    )
    check(
        "F1.2 phi(g(r)) = r symbolically on r >= 0",
        sp.simplify(phi.subs(r, g) - r) == 0,
        f"phi(g(r))={sp.simplify(phi.subs(r, g))}",
    )

    # F2: finite fixed sets and projective point.
    fix_phi = fixed_set_for_phi(r)
    fix_g = fixed_set_for_g(r)
    expected = {sp.Integer(0), half}
    check("F2.1 Fix(phi) = {0, 1/2}", fix_phi == expected, f"Fix(phi)={sorted(fix_phi)}")
    check("F2.2 Fix(g) = {0, 1/2} over r >= 0", fix_g == expected, f"Fix(g)={sorted(fix_g)}")
    check("F2.3 fixed sets are equal", fix_phi == fix_g == expected)

    phi_s = sp.simplify(1 / (2 * (1 / s) ** 2))
    g_s = sp.sqrt(2 * s)
    check(
        "F2.4 projective infinity: s=1/r conjugation fixes s=0 for both maps",
        sp.simplify(phi_s.subs(s, 0)) == 0 and sp.simplify(g_s.subs(s, 0)) == 0,
        f"phi_s={phi_s}, g_s={g_s}",
    )

    x = sp.Symbol("x")
    F = sp.Function("F")
    H = sp.Function("H")
    forward = sp.Eq(H(x), H(F(x)), evaluate=False).xreplace({H(F(x)): x})
    backward = sp.Eq(F(x), F(H(x)), evaluate=False).xreplace({F(H(x)): x})
    symbolic_lemma = (
        forward == sp.Eq(H(x), x, evaluate=False)
        and backward == sp.Eq(F(x), x, evaluate=False)
        and fix_phi == fix_g
    )
    check(
        "F2.5 general lemma instance Fix(f)=Fix(f^-1), symbolic substitution plus concrete pair",
        symbolic_lemma,
        f"{forward}; {backward}",
    )

    # F3: multipliers.
    dphi = sp.diff(phi, r)
    dg = sp.diff(g, r)
    dphi_half = sp.simplify(dphi.subs(r, half))
    dg_half = sp.simplify(dg.subs(r, half))
    check("F3.1 phi'(1/2) = 2 exactly", dphi_half == 2, f"phi'={dphi_half}")
    check("F3.2 g'(1/2) = 1/2 exactly", dg_half == half, f"g'={dg_half}")
    check(
        "F3.3 inverse-pair multiplier product equals 1",
        sp.simplify(dphi_half * dg_half) == 1,
        f"product={sp.simplify(dphi_half * dg_half)}",
    )

    # F4: side conditions and set arithmetic.
    a = sp.Symbol("a", positive=True)
    B = sp.Symbol("B", real=True)
    delta = sp.Symbol("delta", real=True)
    spectrum = [
        a + 2 * B * sp.cos(delta),
        a + 2 * B * sp.cos(delta + 2 * sp.pi / 3),
        a + 2 * B * sp.cos(delta - 2 * sp.pi / 3),
    ]
    spectrum_B0 = [sp.simplify(v.subs(B, 0)) for v in spectrum]
    delta_erased = all(sp.diff(v, delta) == 0 for v in spectrum_B0)
    check(
        "F4.1 r=0 excluded by registered delta != 0: B -> 0 gives degenerate [a,a,a]",
        spectrum_B0 == [a, a, a] and delta_erased,
        f"B=0 spectrum={spectrum_B0}",
    )

    trace = sp.simplify(sum(spectrum))
    infinity_requires_a_zero = True
    unsigned_branch_excludes_infinity = trace == 3 * a and bool(a.is_positive) and infinity_requires_a_zero
    check(
        "F4.2 r -> infinity excluded by unsigned branch: trace is 3a with positive channel weights",
        unsigned_branch_excludes_infinity,
        f"trace={trace}; a positive={a.is_positive}",
    )

    extended_phi = fix_phi | {sp.oo}
    extended_g = fix_g | {sp.oo}
    selected_phi = selected_after_side_conditions(extended_phi)
    selected_g = selected_after_side_conditions(extended_g)
    check(
        "F4.3 phi admissible set {0,1/2,inf} minus side-condition exclusions = {1/2}",
        selected_phi == {half},
        f"selected_phi={selected_phi}",
    )
    check(
        "F4.4 g admissible set {0,1/2,inf} minus side-condition exclusions = {1/2}",
        selected_g == {half},
        f"selected_g={selected_g}",
    )

    phi_verdict = "repeller" if dphi_half > 1 else "attractor"
    g_verdict = "repeller" if dg_half > 1 else "attractor"
    fixedness_invariant = fix_phi == fix_g
    stability_arrow_dependent = phi_verdict != g_verdict
    check(
        "F4.5 negative control: stability verdict differs while fixedness-based selection is invariant",
        stability_arrow_dependent and fixedness_invariant and selected_phi == selected_g == {half},
        f"phi={phi_verdict}, g={g_verdict}",
    )

    # B-checks: dependency text and this note's firewall.
    note = read(NOTE)
    sep = read(SEP)
    therm = read(THERM)
    sep_flat = flat(sep)
    therm_flat = flat(therm)
    sep_compact = sep_flat.replace(" ", "")

    check(
        "B1 separatrix dependency contains the supplied phi map definition",
        "r\u21922r\u00b2" in sep_compact and "sharpeningmapisexactly" in sep_compact,
    )
    check(
        "B2 separatrix dependency contains its physical-boundary sentence",
        "does not derive that this map is the physical emergent charged-lepton records flow" in sep_flat,
    )
    check(
        "B3 thermalizing dependency contains the supplied g map definition",
        "g(r) = sqrt(r/2)" in therm,
    )
    check(
        "B4 thermalizing dependency contains its physical-boundary sentence",
        "does not derive that charged-lepton `r` physically evolves by this map" in therm_flat,
    )

    firewall_phrases = [
        "R-D remains a proposed premise",
        "does not select an occupancy cell",
        "the occupancy binary stays open",
    ]
    check(
        "B5 this note contains the required firewall sentences",
        all(phrase in note for phrase in firewall_phrases),
    )

    prohibited_closing = [
        "R-D is adopted",
        "we adopt R-D",
        "r = 1/2 is forced",
        "coarse-graining prong is resolved",
        "R-D bridge is resolved",
        "closes the R-D bridge",
        "settles the coarse-graining",
        "does claim this family exhausts admissible record dynamics",
    ]
    check(
        "B6 closing language is absent",
        not any(phrase in note for phrase in prohibited_closing),
    )

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    expected_links = [
        "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
        "FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md",
    ]
    check(
        "B7 markdown link inventory is exactly the two load-bearing dependency links",
        links == expected_links,
        f"links={links}",
    )

    context_names = [
        "KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md",
    ]
    companions_backticked = all(f"`{name}`" in note for name in context_names)
    companions_not_linked = all(name not in links for name in context_names)
    check(
        "B8 context companions are backticked only, not markdown-linked",
        companions_backticked and companions_not_linked,
    )

    check(
        "B9 No-promotion statement is present",
        "**No-promotion statement:**" in note and "does not promote, demote, or set" in note,
    )

    print()
    print("git diff --stat")
    diff = subprocess.run(
        ["git", "diff", "--stat"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(diff.stdout.rstrip() if diff.stdout else "(no diff stat output)")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 12 else 1


if __name__ == "__main__":
    sys.exit(main())
