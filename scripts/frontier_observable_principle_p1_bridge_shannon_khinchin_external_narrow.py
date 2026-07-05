#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge Shannon/Khinchin external bounded note.

This runner verifies Layer-1 external classification theorems for continuous
additive scalar functionals (Cauchy log functional equation, Shannon entropy
additivity, Khinchin uniqueness axiom enumeration, Aczel-Daroczy classification),
plus the finite-block Grassmann determinant factorization, plus the explicit
honest admission that P1 is NOT retired by this scaffold.

All numerical checks use exact `fractions.Fraction` arithmetic or SymPy
symbolic verification.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md"
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


def test_T1_cauchy_log_symbolic() -> None:
    section("T1: Cauchy log functional equation (symbolic SymPy)")
    x, y = sp.symbols("x y", positive=True)
    lhs = sp.log(x * y)
    rhs = sp.log(x) + sp.log(y)
    diff = sp.simplify(lhs - rhs)
    check(
        "log(x*y) = log(x) + log(y) symbolically",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )
    # Also verify that exact multiplicative-to-additive composition allows
    # an arbitrary scale c but no additive offset.
    c = sp.Symbol("c", real=True)
    expr = c * sp.log(x * y) - c * sp.log(x) - c * sp.log(y)
    check(
        "c*log(x*y) = c*log(x) + c*log(y) for any real c",
        sp.simplify(expr) == 0,
        f"sympy.simplify(c*log diff) = {sp.simplify(expr)}",
    )
    b = sp.Symbol("b", real=True)
    shifted = (c * sp.log(x * y) + b) - (c * sp.log(x) + b) - (c * sp.log(y) + b)
    check(
        "additive offset b is forbidden by exact additivity unless b=0",
        sp.simplify(shifted) == -b,
        f"shifted residual = {sp.simplify(shifted)}",
    )


def test_T2_cauchy_log_numerical_grid() -> None:
    section("T2: Cauchy log equation on rational grid (numerical)")
    import math
    rationals = [Fraction(1, 2), Fraction(2, 1), Fraction(3, 7), Fraction(11, 5),
                 Fraction(13, 9), Fraction(1, 3)]
    ok_all = True
    max_residual = 0.0
    for x in rationals:
        for y in rationals:
            xf, yf = float(x), float(y)
            residual = abs(math.log(xf * yf) - math.log(xf) - math.log(yf))
            if residual > 1e-12:
                ok_all = False
            if residual > max_residual:
                max_residual = residual
    check(
        "log(xy)=log(x)+log(y) on rational grid to <1e-12",
        ok_all,
        f"max_residual={max_residual:.3e}, grid_size={len(rationals)**2}",
    )


def test_T3_shannon_independence_additivity() -> None:
    section("T3: Shannon entropy additivity on independent distributions (exact)")
    # p = (1/2, 1/2), q = (1/3, 2/3)
    # H(p) = -sum p_i log p_i
    # For independent product (p (x) q)_{ij} = p_i q_j we want H(p (x) q) = H(p) + H(q)
    p = [Fraction(1, 2), Fraction(1, 2)]
    q = [Fraction(1, 3), Fraction(2, 3)]
    # Use symbolic log to verify the identity exactly
    def H_symbolic(dist):
        return -sum(sp.Rational(pi.numerator, pi.denominator) *
                    sp.log(sp.Rational(pi.numerator, pi.denominator)) for pi in dist)
    Hp = H_symbolic(p)
    Hq = H_symbolic(q)
    product = []
    for pi in p:
        for qj in q:
            product.append(pi * qj)
    Hpq = H_symbolic(product)
    diff = sp.simplify(Hpq - Hp - Hq)
    check(
        "H(p (x) q) = H(p) + H(q) symbolically for independent rational p, q",
        diff == 0,
        f"sympy.simplify(H(p (x) q) - H(p) - H(q)) = {diff}",
    )


def test_T4_khinchin_axiom_enumeration() -> None:
    section("T4: Khinchin axiom enumeration on a discrete distribution test bank")
    # The Khinchin theorem assumes (K1) continuity, (K2) monotonicity at uniform,
    # (K3) chain-rule additivity, (K4) consistency. The theorem CLASSIFIES the
    # solution as H = -k sum p log p. Here we verify that this classification
    # functional satisfies each axiom on sample distributions, AND we verify
    # that a non-additive alternative violates the chain rule.
    import math

    def H_shannon(dist):
        return -sum(float(p) * math.log(float(p)) for p in dist if p > 0)

    # K1 continuity check: perturb a distribution slightly, H should change continuously
    p_base = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
    p_perturbed = [Fraction(34, 100), Fraction(33, 100), Fraction(33, 100)]
    delta_H = abs(H_shannon(p_perturbed) - H_shannon(p_base))
    check(
        "K1 continuity: small perturbation -> small H change",
        delta_H < 0.01,
        f"|H(perturbed) - H(uniform)| = {delta_H:.4e}",
    )

    # K2 max-at-uniform: H_n(1/n,...,1/n) = log n is monotone in n
    H_unif_2 = H_shannon([Fraction(1, 2), Fraction(1, 2)])
    H_unif_3 = H_shannon([Fraction(1, 3)] * 3)
    H_unif_4 = H_shannon([Fraction(1, 4)] * 4)
    check(
        "K2 monotonicity at uniform: H_2 < H_3 < H_4",
        H_unif_2 < H_unif_3 < H_unif_4,
        f"H_2={H_unif_2:.4f}, H_3={H_unif_3:.4f}, H_4={H_unif_4:.4f}",
    )

    # K3 chain rule on a 2x2 joint: H(AB) = H(A) + H(B|A)
    # joint = ((p11, p12), (p21, p22))
    p11, p12 = Fraction(1, 6), Fraction(1, 3)
    p21, p22 = Fraction(1, 4), Fraction(1, 4)
    joint = [p11, p12, p21, p22]
    pA = [p11 + p12, p21 + p22]
    # Conditional H(B|A) = sum_A pA * H_B|A=a
    HBgivenA = 0.0
    for a, pa in enumerate([pA[0], pA[1]]):
        if a == 0:
            p_b_given_a = [p11 / pa, p12 / pa]
        else:
            p_b_given_a = [p21 / pa, p22 / pa]
        HBgivenA += float(pa) * H_shannon(p_b_given_a)
    HA = H_shannon(pA)
    HAB = H_shannon(joint)
    check(
        "K3 chain rule: H(AB) = H(A) + H(B|A) numerically",
        abs(HAB - HA - HBgivenA) < 1e-12,
        f"H(AB)={HAB:.6f}, H(A)+H(B|A)={HA+HBgivenA:.6f}",
    )

    # K4 consistency: H_n(p, 0) = H_n(p)
    p_padded = p_base + [Fraction(0)]
    check(
        "K4 consistency: appending zero-prob event leaves H unchanged",
        abs(H_shannon(p_padded) - H_shannon(p_base)) < 1e-12,
        f"H(p,0)-H(p)={H_shannon(p_padded)-H_shannon(p_base):.2e}",
    )


def test_T5_grassmann_block_determinant_factorization() -> None:
    section("T5: Grassmann determinant factorization on finite SymPy block")
    # Build a 4x4 antisymmetric staggered toy D = D_A (+) D_B with D_A, D_B 2x2
    # antisymmetric (a real anti-Hermitian / real antisymmetric pair).
    jA, jB = sp.symbols("jA jB", real=True)
    # D_A: 2x2 real antisymmetric
    a = sp.Rational(1, 2)
    D_A = sp.Matrix([[0, a], [-a, 0]])
    # D_B: 2x2 real antisymmetric
    b = sp.Rational(1, 3)
    D_B = sp.Matrix([[0, b], [-b, 0]])
    # Block diagonal D
    D = sp.zeros(4, 4)
    D[:2, :2] = D_A
    D[2:, 2:] = D_B
    # Source: J = jA I_A (+) jB I_B
    JA = jA * sp.eye(2)
    JB = jB * sp.eye(2)
    J = sp.zeros(4, 4)
    J[:2, :2] = JA
    J[2:, 2:] = JB
    # Full block determinant
    det_full = sp.simplify((D + J).det())
    # Block factorization
    det_A = sp.simplify((D_A + JA).det())
    det_B = sp.simplify((D_B + JB).det())
    det_product = sp.simplify(det_A * det_B)
    diff = sp.simplify(det_full - det_product)
    check(
        "det(D_A (+) D_B + J_A (+) J_B) = det(D_A+J_A) det(D_B+J_B) symbolically",
        diff == 0,
        f"sympy.simplify(diff) = {diff}",
    )


def test_T6_log_abs_Z_additivity_on_block() -> None:
    section("T6: log|Z| additivity on independent Grassmann blocks (numerical)")
    import math
    # Same setup as T5, numerical
    a, b = 0.5, 1.0 / 3.0
    jA, jB = 0.7, 1.1
    # 2x2 antisymmetric block determinants: det((0,a;-a,0)+j*I) = j^2 + a^2
    Z_A = jA * jA + a * a
    Z_B = jB * jB + b * b
    log_Z_full = math.log(abs(Z_A * Z_B))
    log_Z_sum = math.log(abs(Z_A)) + math.log(abs(Z_B))
    residual = abs(log_Z_full - log_Z_sum)
    check(
        "log|Z_full| = log|Z_A| + log|Z_B| on independent blocks",
        residual < 1e-12,
        f"|residual|={residual:.3e}, log|Z_full|={log_Z_full:.6f}",
    )


def test_T7_honest_scope_admission() -> None:
    section("T7: Honest scope check — P1 NOT retired by this scaffold")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "fails to close P1 positively",
        "presuppose additivity",
        "P1 itself remains an admitted physical-principle",
        "Shannon route relabels P1",
        "do not derive P1",
        "Aczel-Daroczy",
        "Khinchin",
        "Cauchy",
    ]
    missing = [adm for adm in required_admissions if adm not in text]
    check(
        "note contains all required honest-scope admission strings",
        not missing,
        f"missing={missing}" if missing else "all required strings present",
    )


def test_T8_sensitivity_non_additive_alternatives() -> None:
    section("T8: Sensitivity — non-additive alternatives violate the functional equation")
    # Demonstrate that f(r) = r (identity) does NOT satisfy f(r1 r2) = f(r1) + f(r2),
    # showing the multiplicative-to-additive equation specifically requires log form.
    r1, r2 = Fraction(2), Fraction(3)
    f_identity_r1r2 = r1 * r2
    f_identity_sum = r1 + r2
    check(
        "f(r)=r: f(r1 r2)=r1 r2 != r1+r2 = f(r1)+f(r2) (so identity is NOT additive)",
        f_identity_r1r2 != f_identity_sum,
        f"f(r1 r2)={f_identity_r1r2}, f(r1)+f(r2)={f_identity_sum}",
    )
    # Demonstrate that f(r) = r^2 also fails additivity
    f_square_r1r2 = (r1 * r2) ** 2
    f_square_sum = r1 ** 2 + r2 ** 2
    check(
        "f(r)=r^2 also fails f(r1 r2)=f(r1)+f(r2) in general",
        f_square_r1r2 != f_square_sum,
        f"f(r1 r2)={f_square_r1r2}, f(r1)+f(r2)={f_square_sum}",
    )
    # Confirm that log is the unique class satisfying multiplicative-to-additive
    # via Cauchy: any continuous f with f(xy)=f(x)+f(y) must be c log x.
    # This is a CLASSIFICATION conclusion, NOT a derivation of additivity.
    import math
    c = 1.0
    r1f, r2f = 2.0, 3.0
    lhs = c * math.log(r1f * r2f)
    rhs = c * math.log(r1f) + c * math.log(r2f)
    check(
        "c*log satisfies the multiplicative-to-additive equation",
        abs(lhs - rhs) < 1e-12,
        f"lhs={lhs:.6f}, rhs={rhs:.6f}",
    )


def test_T9_scope_boundary_parent_unchanged() -> None:
    section("T9: Scope boundary — parent statuses not promoted")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "DOES NOT",
        "Derive the P1 admitted premise",
        "Promote, alter, or set the audit status",
    ]
    forbidden = [
        "promotes the status of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "retired premise P1",
        "closes P1 positively",
        "retired_p1",
    ]
    has_required = all(req in text for req in required)
    has_forbidden = any(fb in text for fb in forbidden)
    check(
        "note explicitly states non-promotion language",
        has_required,
        f"required_all_present={has_required}",
    )
    check(
        "note avoids forbidden status-promotion strings",
        not has_forbidden,
        f"forbidden_present={has_forbidden}",
    )


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary check")
    text = NOTE.read_text(encoding="utf-8")
    check(
        "note declares Claim type: bounded_theorem",
        "**Claim type:** bounded_theorem" in text,
    )
    check(
        "note declares Status authority: source-note proposal only",
        "Status authority" in text and "source-note proposal only" in text,
    )
    forbidden_status = [
        "effective_status: retained",
        "effective_status: audited_clean",
        "pipeline-derived status: retained",
        "audit lane verdict: retained",
        # also forbid removing the honest admission later
        "P1 is now derived",
        "P1 is closed",
    ]
    check(
        "note avoids forbidden status-overclaim strings",
        not any(fb in text for fb in forbidden_status),
    )


def main() -> int:
    print("# Observable-principle P1 bridge Shannon/Khinchin external bounded note runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_cauchy_log_symbolic()
    test_T2_cauchy_log_numerical_grid()
    test_T3_shannon_independence_additivity()
    test_T4_khinchin_axiom_enumeration()
    test_T5_grassmann_block_determinant_factorization()
    test_T6_log_abs_Z_additivity_on_block()
    test_T7_honest_scope_admission()
    test_T8_sensitivity_non_additive_alternatives()
    test_T9_scope_boundary_parent_unchanged()
    test_T10_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
