#!/usr/bin/env python3
"""
Koide Q = 2/3 bridge - conditional-ratio narrowing

Purpose:
  sharpen the remaining Q = 2/3 bridge on the charged-lepton Koide lane.

Review scope:
  - equal cyclic block power and the carrier normalization are supplied;
  - the principal-square-root Brannen envelope and its carrier match are
    supplied on an explicit positive scale and phase domain;
  - physical selection of those premises is outside this runner's scope.

This runner proves a bounded conditional algebraic theorem: under the explicit
carrier, sign, scale, and phase premises printed below, equal cyclic block
power implies the ratio

    P_Q := |b|^2 / a^2 = 1/2

on the C_3-equivariant Hermitian carrier, with the exact conditional chain

  - equal cyclic block power,
  - real-irrep-block democracy,
  - kappa = a^2 / |b|^2 = 2,
  - Brannen c = sqrt(2),
  - Koide Q = 2/3 on the principal-root phase domain.

Honest status:
  this does NOT derive the printed carrier premises and does NOT close the
  physical/source-law bridge. It makes no exhaustiveness claim about unlisted
  arithmetic constructions or physical bridge routes.
"""

from __future__ import annotations

import sys

import sympy as sp


PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    section("Koide Q-bridge conditional-ratio narrowing")
    print()
    print("This runner does not claim physical closure.")
    print("It proves that equal cyclic block power implies the conditional ratio")
    print("P_Q = |b|^2 / a^2 = 1/2 and, on the stated Brannen domain, Q = 2/3.")

    # r0 > 0 is the nondegenerate positive branch needed for a = r0/3 > 0.
    # r1 and r2 remain unrestricted real coordinates.
    r0 = sp.symbols("r0", positive=True)
    r1, r2 = sp.symbols("r1 r2", real=True)
    delta = sp.symbols("delta", real=True)
    c = sp.symbols("c", positive=True)
    v0 = sp.symbols("v0", positive=True)

    section("Premise ledger - conditional theorem domain")
    print("[PREMISE H1] r0 > 0 and r1,r2 are real; hence a = r0/3 > 0.")
    print("[PREMISE H2] E_+ = r0^2/3, E_perp = (r1^2+r2^2)/6,")
    print("             a = r0/3, and |b|^2 = (r1^2+r2^2)/36.")
    print("[PREMISE H3] The principal-root Brannen carrier uses c = 2|b|/a,")
    print("             c > 0, v0 > 0, and delta mod 2pi/3 in [-pi/12,pi/12].")
    print()
    print("H2-H3 are stipulated carrier/domain inputs, not outputs of this runner.")
    print("The theorem derives their exact consequences and leaves physical")
    print("carrier/source-law selection outside its claim.")

    section("Part A - cyclic block power is exactly the Koide selector")
    e_plus = r0**2 / 3
    e_perp = (r1**2 + r2**2) / 6
    selector_gap = sp.expand(6 * (e_plus - e_perp))

    record(
        "A.1 equal cyclic block power is equivalent to 2 r0^2 = r1^2 + r2^2",
        sp.simplify(selector_gap - (2 * r0**2 - r1**2 - r2**2)) == 0,
        f"6(E_+ - E_perp) = {selector_gap}",
    )

    a_map = sp.Rational(1, 3) * r0
    b_sq_map = (r1**2 + r2**2) / 36
    a_sq_map = sp.expand(a_map**2)
    democracy_gap = sp.expand(3 * a_map**2 - 6 * b_sq_map)

    record(
        "A.2 cyclic equal-block-power law maps exactly to 3 a^2 = 6 |b|^2",
        sp.simplify(democracy_gap - (e_plus - e_perp)) == 0,
        "with a = r0/3 and |b|^2 = (r1^2 + r2^2)/36",
    )

    # Solve the equal-power equation for r1^2 and substitute that solution;
    # this derives the locus result rather than assigning a^2 = 2|b|^2.
    equal_power_locus = {r1**2: 2 * r0**2 - r2**2}
    b_sq_on_locus = sp.simplify(b_sq_map.subs(equal_power_locus))
    record(
        "A.3 equal block power derives a^2 = 2 |b|^2",
        sp.simplify(a_sq_map - 2 * b_sq_on_locus) == 0,
        f"on 2 r0^2 = r1^2+r2^2: a^2 = {a_sq_map}, |b|^2 = {b_sq_on_locus}",
    )

    section("Part B - democracy fixes one conditional ratio")
    conditional_ratio = sp.simplify(b_sq_on_locus / a_sq_map)
    kappa = sp.simplify(a_sq_map / b_sq_on_locus)

    record(
        "B.1 real-irrep-block democracy gives |b|^2 / a^2 = 1/2",
        conditional_ratio == sp.Rational(1, 2),
        f"|b|^2 / a^2 = {conditional_ratio}",
    )

    record(
        "B.2 the same democracy law gives kappa = a^2 / |b|^2 = 2",
        kappa == 2,
        f"kappa = {kappa}",
    )

    c_democracy = sp.simplify(2 * sp.sqrt(b_sq_on_locus) / a_map)
    record(
        "B.3 the conditional ratio forces the Brannen prefactor c = sqrt(2)",
        c_democracy == sp.sqrt(2),
        f"c = 2|b|/a = {c_democracy}, using a = r0/3 > 0",
    )

    negative_branch_c = sp.simplify(
        2 * sp.sqrt(sp.Rational(1, 2)) / sp.Integer(-1)
    )
    record(
        "B.4 the a < 0 domain witness gives c = -sqrt(2), so a > 0 is load-bearing",
        negative_branch_c == -sp.sqrt(2) and negative_branch_c != sp.sqrt(2),
        f"a = -1, |b|^2 = 1/2 gives c = {negative_branch_c}",
    )

    section("Part C - Brannen prefactor and Koide ratio")
    envelope = lambda k: 1 + c * sp.cos(delta + 2 * sp.pi * k / 3)
    q_expr = sp.simplify(
        sum(envelope(k) ** 2 for k in range(3))
        / sum(envelope(k) for k in range(3)) ** 2
    )
    q_at_sqrt2 = sp.simplify(q_expr.subs(c, sp.sqrt(2)))

    record(
        "C.1 the Brannen envelope gives Q(c) = 1/3 + c^2/6 independently of delta",
        sp.simplify(q_expr - (sp.Rational(1, 3) + c**2 / 6)) == 0,
        f"Q(c, delta) = {q_expr}",
    )

    sqrt2_bracket = lambda phase, k: sp.simplify(
        1 + sp.sqrt(2) * sp.cos(phase + 2 * sp.pi * k / 3)
    )
    left_boundary = [sqrt2_bracket(-sp.pi / 12, k) for k in range(3)]
    right_boundary = [sqrt2_bracket(sp.pi / 12, k) for k in range(3)]
    outside_witness = [sqrt2_bracket(sp.pi / 3, k) for k in range(3)]

    record(
        "C.2 the principal-root phase-window endpoints are nonnegative",
        all(value.is_nonnegative is True for value in left_boundary + right_boundary)
        and sum(value == 0 for value in left_boundary + right_boundary) == 2,
        f"delta=-pi/12: {left_boundary}; delta=pi/12: {right_boundary}",
    )

    record(
        "C.3 delta = pi/3 is outside the principal-root phase domain",
        any(value.is_negative is True for value in outside_witness),
        f"delta=pi/3 brackets: {outside_witness}",
    )

    record(
        "C.4 c = sqrt(2) gives Q = 2/3 on the stated principal-root domain",
        q_at_sqrt2 == sp.Rational(2, 3) and v0.is_positive is True,
        f"Q(c = sqrt(2)) = {q_at_sqrt2}, v0 > 0",
    )

    section("Part D - scope exclusions (not impossibility claims)")
    print("The exact arithmetic consequences above are conditional on H1-H3.")
    print("The dimension-count and hypercharge coincidences are not theorem inputs.")
    print()
    print("This runner verifies one bounded conditional implication:")
    print("equal cyclic block power => P_Q = 1/2 => Q = 2/3 on the stated domain.")
    print()
    print("Physical selector and source-law identification remain outside scope.")
    print("No claim is made that unlisted routes are exhausted or cannot succeed.")

    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: under H1-H3, equal cyclic block power gives P_Q = 1/2")
        print("and Q = 2/3 on the stated principal-root phase/scale domain.")
        print()
        print("Physical/source-law identification and exhaustiveness over other")
        print("routes are outside scope. Audit verdict and effective status remain")
        print("the independent audit lane's authority.")
        return 0

    print("VERDICT: verification has FAILs.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
