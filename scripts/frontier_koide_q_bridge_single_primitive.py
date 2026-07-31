#!/usr/bin/env python3
"""
Koide Q = 2/3 bridge - finite listed-expression comparison

Purpose:
  sharpen the remaining Q = 2/3 bridge on the charged-lepton Koide lane.

Current package status on origin/main:
  - the block-total Frobenius / AM-GM stack proves where the admitted
    functional is extremized;
  - several April 22 support runners add axiom-native reformulations;
  - physical identification is outside this runner's algebraic scope.

This runner proves a conditional algebraic theorem: under the explicit
carrier, sign, representation-dimension, and Yukawa-normalization premises
printed below, four explicitly listed arithmetic / representation-theoretic
expressions share one scalar value:

    P_Q := |b|^2 / a^2 = 1/2

on the C_3-equivariant Hermitian carrier, with the exact consequence chain

  - equal cyclic block power,
  - real-irrep-block democracy,
  - kappa = a^2 / |b|^2 = 2,
  - Brannen c = sqrt(2),
  - Koide Q = 2/3,
  - dim(spinor) / dim(Cl^+(3)) = 1/2,
  - T(T+1) - Y^2 = 1/2 on the charged-lepton Yukawa pair.

Honest status:
  this does NOT derive the printed carrier/face premises and does NOT close the
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
    section("Koide Q-bridge finite listed-expression comparison")
    print()
    print("This runner does not claim physical closure.")
    print("It proves that four explicitly listed arithmetic/representation-theoretic")
    print("expressions share the scalar value P_Q = |b|^2 / a^2 = 1/2.")

    # r0 > 0 is the nondegenerate positive branch needed for a = r0/3 > 0.
    # r1 and r2 remain unrestricted real coordinates.
    r0 = sp.symbols("r0", positive=True)
    r1, r2 = sp.symbols("r1 r2", real=True)
    delta = sp.symbols("delta", real=True)
    c = sp.symbols("c", positive=True)

    section("Premise ledger - conditional theorem domain")
    print("[PREMISE H1] r0 > 0 and r1,r2 are real; hence a = r0/3 > 0.")
    print("[PREMISE H2] E_+ = r0^2/3, E_perp = (r1^2+r2^2)/6,")
    print("             a = r0/3, and |b|^2 = (r1^2+r2^2)/36.")
    print("[PREMISE H3] The Brannen carrier uses c = 2|b|/a and c > 0.")
    print("[PREMISE H4] Dimension-face convention: dim_C(spinor)=2 and")
    print("             dim_R(Cl^+(3))=4.")
    print("[PREMISE H5] PDG-normalized Yukawa-doublet face: T=1/2 and |Y|=1/2.")
    print()
    print("H2-H5 are stipulated carrier/face inputs, not outputs of this runner.")
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

    section("Part B - democracy collapses to one scalar primitive")
    primitive_ratio = sp.simplify(b_sq_on_locus / a_sq_map)
    kappa = sp.simplify(a_sq_map / b_sq_on_locus)

    record(
        "B.1 real-irrep-block democracy gives |b|^2 / a^2 = 1/2",
        primitive_ratio == sp.Rational(1, 2),
        f"|b|^2 / a^2 = {primitive_ratio}",
    )

    record(
        "B.2 the same democracy law gives kappa = a^2 / |b|^2 = 2",
        kappa == 2,
        f"kappa = {kappa}",
    )

    c_democracy = sp.simplify(2 * sp.sqrt(b_sq_on_locus) / a_map)
    record(
        "B.3 the primitive ratio forces the Brannen prefactor c = sqrt(2)",
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

    record(
        "C.2 c = sqrt(2) gives Q = 2/3 identically in the phase delta",
        q_at_sqrt2 == sp.Rational(2, 3),
        f"Q(c = sqrt(2)) = {q_at_sqrt2}",
    )

    section("Part D - representation-theoretic faces hit the same scalar")
    dim_spinor, dim_cl_even = sp.symbols(
        "dim_spinor dim_cl_even", positive=True, integer=True
    )
    t_isospin, y_abs = sp.symbols("T Y_abs", nonnegative=True)
    face_premises = {
        dim_spinor: 2,
        dim_cl_even: 4,
        t_isospin: sp.Rational(1, 2),
        y_abs: sp.Rational(1, 2),
    }
    dim_ratio = sp.simplify((dim_spinor / dim_cl_even).subs(face_premises))
    casimir_diff = sp.simplify(
        (t_isospin * (t_isospin + 1) - y_abs**2).subs(face_premises)
    )
    casimir_sum = sp.simplify(
        (t_isospin * (t_isospin + 1) + y_abs**2).subs(face_premises)
    )
    normalized_casimir_ratio = sp.simplify(casimir_diff / casimir_sum)

    record(
        "D.1 dim(spinor) / dim(Cl^+(3)) = 1/2",
        dim_ratio == sp.Rational(1, 2),
        f"2 / 4 = {dim_ratio}",
    )

    record(
        "D.2 charged-lepton Yukawa Casimir difference T(T+1) - Y^2 = 1/2",
        casimir_diff == sp.Rational(1, 2),
        f"1/2 * 3/2 - (1/2)^2 = {casimir_diff}",
    )

    record(
        "D.3 normalized Yukawa Casimir ratio is 1/2",
        normalized_casimir_ratio == sp.Rational(1, 2),
        "[T(T+1)-Y^2] / [T(T+1)+Y^2] "
        f"= {casimir_diff} / {casimir_sum} = {normalized_casimir_ratio}",
    )

    section("Part E - finite listed-face comparison")
    collapse_values = {
        "|b|^2/a^2": primitive_ratio,
        "dim(spinor)/dim(Cl^+(3))": dim_ratio,
        "T(T+1)-Y^2": casimir_diff,
        "[T(T+1)-Y^2]/[T(T+1)+Y^2]": normalized_casimir_ratio,
    }
    all_half = all(value == sp.Rational(1, 2) for value in collapse_values.values())

    record(
        "E.1 the four listed Q-bridge expressions share P_Q = 1/2",
        all_half and q_at_sqrt2 == sp.Rational(2, 3) and kappa == 2,
        "\n".join(f"{name} = {value}" for name, value in collapse_values.items()),
    )

    section("Part F - scope exclusions (not impossibility claims)")
    print("The exact arithmetic consequences above are conditional on H1-H5.")
    print("In particular, the dimension counts and PDG-normalized Yukawa labels")
    print("are explicit premises rather than outputs of this runner.")
    print()
    print("This runner verifies a finite algebraic comparison of exactly four")
    print("listed expressions, all equal to P_Q = 1/2 under H1-H5.")
    print()
    print("It does NOT derive from retained physics:")
    print("  (1) that the physical selector lives on the admitted normalized")
    print("      second-order reduced carrier, nor")
    print("  (2) that the physical selector is source-free, K = 0, there, nor")
    print("  (3) the readout from Y = I_2 through kappa = 2 to physical")
    print("      Q = 2/3 on the charged-lepton lane.")
    print()
    print("These topics are outside the conditional algebraic theorem checked here.")
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
        print("VERDICT: under H1-H5, the four listed expressions share the value")
        print("P_Q = 1/2 and the H1-H3 consequence chain gives Q = 2/3.")
        print()
        print("Physical/source-law identification and exhaustiveness over other")
        print("routes are outside scope. Audit verdict and effective status remain")
        print("the independent audit lane's authority.")
        return 0

    print("VERDICT: verification has FAILs.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
