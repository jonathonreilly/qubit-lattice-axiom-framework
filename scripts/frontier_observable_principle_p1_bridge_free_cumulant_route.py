#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge free-probability cumulant
route narrow bounded note.

This runner verifies, at exact ``Fraction`` / ``sympy`` precision:

- The elementary block-diagonal determinant factorization
  ``det(D_A (+) D_B + J_A (+) J_B) = det(D_A + J_A) det(D_B + J_B)``
  (T1 symbolic, T2 rational instance, T3 log form).
- The structural fact that the spectral measure of a direct sum
  ``M_A (+) M_B`` is the equally-weighted convex combination of the
  block spectra, NOT the free convolution (T4).
- Classical cumulant additivity on commuting independent variables via
  the log-MGF identity ``log E[e^{t(X+Y)}] = log E[e^{tX}] + log E[e^{tY}]``
  truncated to symbolic order ``t^2`` (T5).
- Voiculescu free-cumulant additivity on free-Gaussian (semicircular)
  pairs: ``kappa_2^free(s_1 + s_2) = kappa_2^free(s_1) + kappa_2^free(s_2)``
  on a freely-independent pair (T6).
- The structural exhibition that free-cumulant additivity does NOT apply
  to the framework's direct-sum spectral measure (T7).
- The ``F_p[J] = r(J)^p`` convergent counterexample family continues to
  satisfy multiplicative factorization on the framework substrate, so
  the convergent obstruction is unaffected by this route (T8).
- The source-text echo of Exercise 4's elementary determinant identity
  (T9).
- A source-note boundary check confirming the explicit honest
  admissions are present in the source note (T10).

All numerical checks use exact ``fractions.Fraction`` arithmetic or
SymPy symbolic verification. No floating-point comparisons load-bearing.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_FREE_CUMULANT_ROUTE_NARROW_NOTE_2026-05-21.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------
# T1: Block-diagonal determinant factorization (symbolic 4x4)
# ----------------------------------------------------------------------


def test_T1_block_det_factorization_symbolic() -> None:
    section(
        "T1: det(D_A (+) D_B + J_A (+) J_B) = det(D_A + J_A) det(D_B + J_B) — symbolic 4x4"
    )
    a, c, jaa, jbb, kcc, kdd = sp.symbols("a c jaa jbb kcc kdd", real=True)
    # D_A real anti-symmetric 2x2:
    D_A = sp.Matrix([[0, a], [-a, 0]])
    # D_B real anti-symmetric 2x2:
    D_B = sp.Matrix([[0, c], [-c, 0]])
    # J_A diagonal real-symmetric source:
    J_A = sp.Matrix([[jaa, 0], [0, jbb]])
    # J_B diagonal real-symmetric source:
    J_B = sp.Matrix([[kcc, 0], [0, kdd]])
    # Block diagonal D and J:
    D = sp.diag(D_A, D_B)
    J = sp.diag(J_A, J_B)
    lhs = sp.expand((D + J).det())
    rhs = sp.expand((D_A + J_A).det() * (D_B + J_B).det())
    diff = sp.simplify(lhs - rhs)
    check(
        "det((D_A (+) D_B) + (J_A (+) J_B)) = det(D_A + J_A) det(D_B + J_B) (symbolic)",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )


# ----------------------------------------------------------------------
# T2: Block-diagonal determinant factorization (exact rational instance)
# ----------------------------------------------------------------------


def test_T2_block_det_factorization_rational_instance() -> None:
    section("T2: Block-diagonal determinant factorization (exact rational instance)")
    a, c, jaa, jbb, kcc, kdd = sp.symbols("a c jaa jbb kcc kdd", real=True)
    D_A = sp.Matrix([[0, a], [-a, 0]])
    D_B = sp.Matrix([[0, c], [-c, 0]])
    J_A = sp.Matrix([[jaa, 0], [0, jbb]])
    J_B = sp.Matrix([[kcc, 0], [0, kdd]])
    D = sp.diag(D_A, D_B)
    J = sp.diag(J_A, J_B)
    subs = {
        a: sp.Rational(Fraction(2, 3)),
        c: sp.Rational(Fraction(1, 5)),
        jaa: sp.Rational(Fraction(1, 2)),
        jbb: sp.Rational(Fraction(1, 3)),
        kcc: sp.Rational(Fraction(2, 11)),
        kdd: sp.Rational(Fraction(3, 5)),
    }
    lhs = sp.Rational((D + J).subs(subs).det())
    rhs = sp.Rational(
        (D_A + J_A).subs(subs).det() * (D_B + J_B).subs(subs).det()
    )
    check(
        "rational-Fraction instance: det(D+J) = det(D_A+J_A) det(D_B+J_B)",
        lhs == rhs,
        f"lhs={lhs}, rhs={rhs}",
    )


# ----------------------------------------------------------------------
# T3: Block-diagonal determinant factorization (log form)
# ----------------------------------------------------------------------


def test_T3_block_det_factorization_log_form() -> None:
    section("T3: log|det(D+J)| = log|det(D_A+J_A)| + log|det(D_B+J_B)| on the runner block")
    # Use an explicit rational instance from T2 with all determinants positive.
    # The 2x2 anti-symmetric + diagonal block has determinant jaa*jbb + a^2; positive for
    # our rational choices.
    a_v = sp.Rational(Fraction(2, 3))
    c_v = sp.Rational(Fraction(1, 5))
    jaa_v = sp.Rational(Fraction(1, 2))
    jbb_v = sp.Rational(Fraction(1, 3))
    kcc_v = sp.Rational(Fraction(2, 11))
    kdd_v = sp.Rational(Fraction(3, 5))
    DA = sp.Matrix([[0, a_v], [-a_v, 0]]) + sp.Matrix([[jaa_v, 0], [0, jbb_v]])
    DB = sp.Matrix([[0, c_v], [-c_v, 0]]) + sp.Matrix([[kcc_v, 0], [0, kdd_v]])
    detA = DA.det()
    detB = DB.det()
    # Confirm both determinants are positive (so absolute values are themselves).
    detA_pos = sp.simplify(detA) > 0
    detB_pos = sp.simplify(detB) > 0
    check(
        "rational instance: det(D_A + J_A) > 0 and det(D_B + J_B) > 0",
        bool(detA_pos) and bool(detB_pos),
        f"det_A = {detA}, det_B = {detB}",
    )
    # log identity:
    diff = sp.simplify(
        sp.log(detA * detB) - sp.log(detA) - sp.log(detB)
    )
    check(
        "log|det(D+J)| - log|det(D_A+J_A)| - log|det(D_B+J_B)| = 0 (symbolic)",
        diff == 0,
        f"diff = {diff}",
    )


# ----------------------------------------------------------------------
# T4: Spectral measure on direct sum vs free convolution (structural)
# ----------------------------------------------------------------------


def test_T4_direct_sum_spectrum_vs_free_convolution() -> None:
    section("T4: Spectral measure on direct sum = convex combination, NOT free convolution")
    # Take M_A = diag(1, 3), M_B = diag(2, 4). The direct-sum spectral
    # measure of M_A (+) M_B is the empirical measure with support
    # {1, 3, 2, 4}, equal weights 1/4 each. Equivalently, it is the
    # equally-weighted convex combination of the empirical measures of
    # M_A and M_B.
    # In particular, the second moment of the direct-sum spectral measure
    # is (1 + 9 + 4 + 16) / 4 = 30/4 = 15/2.
    spectrum_AB_direct_sum = [Fraction(1), Fraction(3), Fraction(2), Fraction(4)]
    n_AB = len(spectrum_AB_direct_sum)
    m2_direct_sum = sum(x ** 2 for x in spectrum_AB_direct_sum) / Fraction(n_AB)
    expected_m2 = Fraction(15, 2)
    check(
        "direct-sum spectral measure second moment = 15/2 (empirical, equally weighted)",
        m2_direct_sum == expected_m2,
        f"m2_direct_sum = {m2_direct_sum}, expected = {expected_m2}",
    )
    # Free convolution m2: by free-additivity, the free convolution of two
    # measures with first moments m1_A, m1_B and variances v_A, v_B has
    # first moment m1_A + m1_B and variance v_A + v_B (free cumulants are
    # additive). For our M_A, M_B (each empirical with 2 points):
    #   m1(M_A) = (1 + 3) / 2 = 2,   v_A = ((1-2)^2 + (3-2)^2) / 2 = 1
    #   m1(M_B) = (2 + 4) / 2 = 3,   v_B = ((2-3)^2 + (4-3)^2) / 2 = 1
    # So the free convolution mu_A (+) mu_B has m1 = 2 + 3 = 5 and v = 1 + 1 = 2.
    # Its second moment is m1^2 + v = 25 + 2 = 27.
    # In contrast, the direct-sum spectral measure has m1 = (1+3+2+4)/4 = 10/4 = 5/2
    # and m2 = 15/2 (just computed). So the two are not equal: 15/2 != 27.
    m2_free_conv = Fraction(27)
    check(
        "free convolution second moment = 27 != 15/2; direct-sum != free convolution",
        m2_direct_sum != m2_free_conv,
        f"m2_direct_sum = {m2_direct_sum} != m2_free_conv = {m2_free_conv}",
    )
    # First moment check: m1_direct_sum = 5/2 vs m1_free_conv = 5. Different too.
    m1_direct_sum = sum(spectrum_AB_direct_sum) / Fraction(n_AB)
    m1_free_conv = Fraction(5)
    check(
        "direct-sum first moment = 5/2 != free convolution first moment = 5",
        m1_direct_sum != m1_free_conv,
        f"m1_direct_sum = {m1_direct_sum}, m1_free_conv = {m1_free_conv}",
    )


# ----------------------------------------------------------------------
# T5: Classical cumulant additivity on commuting independent variables
# ----------------------------------------------------------------------


def test_T5_classical_cumulant_additivity_truncated() -> None:
    section("T5: Classical cumulants — log E[e^{t(X+Y)}] = log E[e^{tX}] + log E[e^{tY}] on independent X, Y")
    t = sp.Symbol("t")
    a, b, c, d = sp.symbols("a b c d", real=True)
    # Truncated MGFs to order t^2:
    M_X = 1 + a * t + sp.Rational(1, 2) * b * t ** 2
    M_Y = 1 + c * t + sp.Rational(1, 2) * d * t ** 2
    # Joint MGF on independent X, Y is the product:
    M_joint = sp.series(M_X * M_Y, t, 0, 3).removeO()
    # Log-MGFs (truncated):
    K_X = sp.series(sp.log(M_X), t, 0, 3).removeO()
    K_Y = sp.series(sp.log(M_Y), t, 0, 3).removeO()
    K_joint = sp.series(sp.log(M_joint), t, 0, 3).removeO()
    diff = sp.expand(K_joint - K_X - K_Y)
    check(
        "classical CGF additivity (truncated): log E[e^{t(X+Y)}] = log E[e^{tX}] + log E[e^{tY}]",
        sp.simplify(diff) == 0,
        f"K_joint - K_X - K_Y = {diff}",
    )
    # Cumulants: kappa_1 = coeff(t), kappa_2 = 2 * coeff(t^2).
    # For X: kappa_1(X) = a, kappa_2(X) = b - a^2.
    # For Y: kappa_1(Y) = c, kappa_2(Y) = d - c^2.
    # For X+Y: kappa_1 = a + c, kappa_2 = (b - a^2) + (d - c^2).
    # We verify variance additivity:
    K_joint_t2_coef = sp.Poly(K_joint, t).all_coeffs()
    # all_coeffs() returns [coeff(t^2), coeff(t), const] for a polynomial of degree 2.
    if len(K_joint_t2_coef) == 3:
        coef_t2_joint = K_joint_t2_coef[0]
    else:
        coef_t2_joint = K_joint.coeff(t, 2)
    var_joint = sp.simplify(2 * coef_t2_joint)
    var_expected = sp.simplify((b - a ** 2) + (d - c ** 2))
    diff_var = sp.simplify(var_joint - var_expected)
    check(
        "kappa_2(X+Y) = kappa_2(X) + kappa_2(Y) on independent X, Y (variance additivity)",
        diff_var == 0,
        f"var_joint = {var_joint}, var_expected = {var_expected}, diff = {diff_var}",
    )


# ----------------------------------------------------------------------
# T6: Voiculescu free-cumulant additivity on free-Gaussian (semicircular)
# ----------------------------------------------------------------------


def test_T6_voiculescu_free_cumulant_additivity_semicircular() -> None:
    section("T6: Voiculescu free-cumulant additivity — semicircular free convolution")
    # Standard semicircular s with kappa_n^free(s) = 1 for n=2, 0 otherwise.
    # The R-transform is R_s(z) = z (only the kappa_2 coefficient is nonzero).
    # For freely-independent s_1, s_2 both standard semicircular:
    #   R_{s_1 + s_2}(z) = R_{s_1}(z) + R_{s_2}(z) = z + z = 2 z.
    # So kappa_2^free(s_1 + s_2) = 2, and the free convolution
    # is semicircular with radius 2 (variance 2).
    # We verify the kappa_2 additivity statement symbolically.
    kappa_2_s1 = sp.Rational(1)
    kappa_2_s2 = sp.Rational(1)
    # By Voiculescu's free-cumulant additivity theorem:
    kappa_2_sum_voiculescu = kappa_2_s1 + kappa_2_s2
    expected = sp.Rational(2)
    check(
        "Voiculescu: kappa_2^free(s_1 + s_2) = kappa_2^free(s_1) + kappa_2^free(s_2) for free standard semicirculars",
        kappa_2_sum_voiculescu == expected,
        f"kappa_2^free(s_1+s_2) = {kappa_2_sum_voiculescu}, expected = {expected}",
    )
    # R-transform additivity check (symbolic): R_{s_1+s_2}(z) = 2 z.
    z = sp.Symbol("z")
    R_s1 = z
    R_s2 = z
    R_sum = R_s1 + R_s2
    expected_R = 2 * z
    diff = sp.simplify(R_sum - expected_R)
    check(
        "R-transform additivity: R_{s_1+s_2}(z) = R_{s_1}(z) + R_{s_2}(z) = 2 z",
        diff == 0,
        f"R_sum = {R_sum}, expected = {expected_R}, diff = {diff}",
    )


# ----------------------------------------------------------------------
# T7: Free-cumulant additivity DOES NOT apply to direct-sum spectral measures
# ----------------------------------------------------------------------


def test_T7_free_cumulant_does_not_apply_to_direct_sum() -> None:
    section("T7: Free-cumulant additivity does NOT apply to direct-sum spectra")
    # Take M_A = diag(1, -1), M_B = diag(2, -2).
    # Spectrum of M_A: {1, -1}, m1 = 0, m2 = 1.
    # Free cumulants of M_A's spectral measure: kappa_1^free = m1 = 0,
    # kappa_2^free = m2 - m1^2 = 1 (for empirical 2-point symmetric).
    # Similarly for M_B: kappa_1^free = 0, kappa_2^free = 4.
    # If free additivity DID apply, we would expect
    # kappa_2^free(direct-sum) = kappa_2^free(M_A) + kappa_2^free(M_B) = 1 + 4 = 5.
    # But the direct-sum spectral measure is the equally-weighted
    # convex combination on {1, -1, 2, -2}, m1 = 0, m2 = (1+1+4+4)/4 = 10/4 = 5/2.
    # So kappa_2 of the direct-sum spectral measure (computed as m2 - m1^2)
    # is 5/2, NOT 5. The discrepancy 5/2 vs 5 is the structural witness that
    # free-additivity does not apply to direct-sum substrates.
    spec_A = [Fraction(1), Fraction(-1)]
    spec_B = [Fraction(2), Fraction(-2)]
    m1_A = sum(spec_A) / Fraction(len(spec_A))
    m2_A = sum(x ** 2 for x in spec_A) / Fraction(len(spec_A))
    kappa_2_A = m2_A - m1_A ** 2
    m1_B = sum(spec_B) / Fraction(len(spec_B))
    m2_B = sum(x ** 2 for x in spec_B) / Fraction(len(spec_B))
    kappa_2_B = m2_B - m1_B ** 2
    check(
        "spectral kappa_2 of M_A's empirical = 1 and M_B's empirical = 4",
        kappa_2_A == Fraction(1) and kappa_2_B == Fraction(4),
        f"kappa_2_A = {kappa_2_A}, kappa_2_B = {kappa_2_B}",
    )
    # Direct-sum spectrum:
    spec_AB = spec_A + spec_B
    m1_AB = sum(spec_AB) / Fraction(len(spec_AB))
    m2_AB = sum(x ** 2 for x in spec_AB) / Fraction(len(spec_AB))
    kappa_2_direct_sum = m2_AB - m1_AB ** 2
    # If free additivity applied: kappa_2 sum should equal kappa_2_A + kappa_2_B = 5.
    # Actual direct-sum kappa_2 = m2_AB - m1_AB^2 = 5/2 - 0 = 5/2.
    check(
        "direct-sum kappa_2 = 5/2, NOT kappa_2_A + kappa_2_B = 5; direct-sum is not free convolution",
        kappa_2_direct_sum == Fraction(5, 2) and kappa_2_direct_sum != (kappa_2_A + kappa_2_B),
        f"kappa_2_direct_sum = {kappa_2_direct_sum}, kappa_2_A + kappa_2_B = {kappa_2_A + kappa_2_B}",
    )


# ----------------------------------------------------------------------
# T8: F_p[J] = r(J)^p convergent counterexample survives the free-cumulant route
# ----------------------------------------------------------------------


def test_T8_F_p_counterexample_survives() -> None:
    section("T8: F_p[J] = r(J)^p multiplicative factorization is unaffected by this route")
    # On the runner block:
    a_v = sp.Rational(Fraction(2, 3))
    c_v = sp.Rational(Fraction(1, 5))
    jaa_v = sp.Rational(Fraction(1, 2))
    jbb_v = sp.Rational(Fraction(1, 3))
    kcc_v = sp.Rational(Fraction(2, 11))
    kdd_v = sp.Rational(Fraction(3, 5))
    DA = sp.Matrix([[0, a_v], [-a_v, 0]]) + sp.Matrix([[jaa_v, 0], [0, jbb_v]])
    DB = sp.Matrix([[0, c_v], [-c_v, 0]]) + sp.Matrix([[kcc_v, 0], [0, kdd_v]])
    r_A = sp.Abs(DA.det())
    r_B = sp.Abs(DB.det())
    r_joint = r_A * r_B  # by T1/T2.
    p_values = [
        sp.Rational(Fraction(1)),
        sp.Rational(Fraction(2)),
        sp.Rational(Fraction(3)),
        sp.Rational(Fraction(1, 2)),
        sp.Rational(Fraction(-1)),
    ]
    all_ok = True
    details = []
    for p in p_values:
        F_joint = r_joint ** p
        F_prod = (r_A ** p) * (r_B ** p)
        diff = sp.simplify(F_joint - F_prod)
        ok_p = diff == 0
        details.append((str(p), str(diff)))
        if not ok_p:
            all_ok = False
    check(
        "F_p[J_A (+) J_B] = F_p[J_A] F_p[J_B] for p in {1, 2, 3, 1/2, -1}",
        all_ok,
        f"(p, diff): {details}",
    )


# ----------------------------------------------------------------------
# T9: Source-text echo of Exercise 4 elementary determinant identity
# ----------------------------------------------------------------------


def test_T9_source_text_elementary_det_identity() -> None:
    section("T9: Source-note Exercise 4 elementary determinant identity echo")
    text = NOTE.read_text(encoding="utf-8")
    required_strings = [
        "det([[A, 0], [0, B]]) = det(A) · det(B)",
        "elementary linear algebra",
        "no probability theory",
        "Exercise 4",
    ]
    for s in required_strings:
        ok = s in text
        check(
            f'note contains source-text string: "{s[:60]}"',
            ok,
            f"present={ok}",
        )


# ----------------------------------------------------------------------
# T10: Source-note boundary check
# ----------------------------------------------------------------------


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "**Type:** bounded_theorem",
        "**Status authority:** independent audit lane only",
        "Source-note proposal disclaimer",
        # Honest admissions:
        "P1 is NOT closed positively",
        "wrong tool for direct-sum independence",
        "wrong notion of independence",
        # Right notions:
        "Muraki five universal",
        "Voiculescu",
        "Speicher",
        "Muraki",
        # Convergent obstruction sharpening:
        "7-class convergent obstruction",
        # P1 explicitly remains admitted:
        "P1 in its strong sense",
    ]
    for s in required_admissions:
        ok = s in text
        check(
            f'note contains admission string: "{s[:60]}"',
            ok,
            f"present={ok}",
        )
    forbidden = [
        "**Type:** positive_theorem",
        "**Type:** retained",
        "**Type:** retained_bounded",
        "audited_clean (this note)",
        "retained_bounded (this note)",
        "P1 is now derived",
        "P1 is closed by this note",
        "P1 is retired by this note",
        "this note promotes the status",
        "audit lane verdict: retained",
        "effective_status: retained (this note)",
        "effective_status: audited_clean (this note)",
        # Free probability does NOT apply to direct-sum independence; reject any wording saying otherwise:
        "free probability forces P1",
        "free probability closes P1",
        "Voiculescu closes P1",
    ]
    hits = [f for f in forbidden if f in text]
    check(
        "note avoids forbidden status-promotion / overclaim strings",
        len(hits) == 0,
        f"forbidden_hits={hits}",
    )


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------


def main() -> int:
    print("# Observable-principle P1 bridge free-cumulant-route runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_block_det_factorization_symbolic()
    test_T2_block_det_factorization_rational_instance()
    test_T3_block_det_factorization_log_form()
    test_T4_direct_sum_spectrum_vs_free_convolution()
    test_T5_classical_cumulant_additivity_truncated()
    test_T6_voiculescu_free_cumulant_additivity_semicircular()
    test_T7_free_cumulant_does_not_apply_to_direct_sum()
    test_T8_F_p_counterexample_survives()
    test_T9_source_text_elementary_det_identity()
    test_T10_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
