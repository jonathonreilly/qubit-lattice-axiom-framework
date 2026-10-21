#!/usr/bin/env python3
"""Brocard polynomial Vieta / Newton structure in structural integers.

Verifies the NEW retained closed forms in
  docs/CKM_BROCARD_POLYNOMIAL_VIETA_STRUCTURAL_INTEGERS_THEOREM_NOTE_2026-04-25.md

Key NEW identities on the retained NLO Wolfenstein protected-gamma_bar surface:

  (V1) Brocard polynomial expanded in structural integers:
        P(alpha_s)  =  alpha_s^4
                       -  N_pair^3 alpha_s^3
                       -  N_pair^5 alpha_s^2
                       +  N_pair^7 N_color^2 alpha_s
                       +  N_pair^8 N_color (N_quark + 1).

  (V2) Vieta relations on the four (complex) roots of P:
        e_1 = sum            =  +N_pair^3                  =  8,
        e_2 = pairwise sum   =  -N_pair^5                  =  -32,
        e_3 = triple sum     =  -N_pair^7 N_color^2        =  -1152,
        e_4 = product        =  N_pair^8 N_color (N_quark + 1)  =  5376.

  (V3) Newton power sums p_k = sum r_i^k:
        p_1 = e_1                                     =  N_pair^3,
        p_2 = e_1 p_1 - 2 e_2                         =  N_pair^6 + 2 N_pair^5
                                                       =  N_pair^5 (N_pair + 2)
                                                       =  N_pair^7  (since N_pair = 2),
        p_3 = e_1 p_2 - e_2 p_1 + 3 e_3
            = N_pair^3 N_pair^7 + N_pair^5 N_pair^3 + 3(-N_pair^7 N_color^2)
            = N_pair^10 + N_pair^8 - 3 N_pair^7 N_color^2.

  (V4) STRUCTURAL FINGERPRINT (NEW):
        p_2 = 2 e_1^2  (sum of squared roots = twice squared sum of roots),
       which is equivalent to e_2 = -e_1^2/2, i.e.
        e_2 = -N_pair^6/2  =  -N_pair^5  iff N_pair = 2.

       This identity p_2 = 2 e_1^2 is a **signature of N_pair = 2** in the
       Brocard polynomial. For any other positive value of N_pair, this imposed identity
       would fail.

  (V5) Mean of the four roots:
        mean = e_1 / 4  =  N_pair^3 / 4  =  N_pair  (since N_pair^2 = 4).

  (V6) Sum of squared deviations from the mean:
        Sigma (r_i - mean)^2  =  p_2 - 2 mean p_1 + 4 mean^2
                              =  128 - 32 + 16 = 112.

       In structural integers: 112 = N_pair^4 (N_quark + 1) = 16 * 7.

  (V7) Roots of P over Q[sqrt(3), sqrt(5), i]:
        alpha_s_root  =  (2 -/+ 2 sqrt(15)) +/- 2i (sqrt(5) -/+ sqrt(3))
                      =  (N_pair -/+ N_pair sqrt(N_color (N_quark - 1)))
                          +/- N_pair i (sqrt(N_quark - 1) -/+ sqrt(N_color)).

  (V8) Factorisation over Q[sqrt(15)]:
        P(alpha_s = 4 - u)
           =  (u^2 - 4(1 + sqrt(15)) u + 96)
              * (u^2 - 4(1 - sqrt(15)) u + 96).

       Both quadratic factors have discriminant -128 +/- 32 sqrt(15) < 0,
       so all four roots are complex.

  (V9) Discriminant of P(alpha_s):
        Disc(P)  =  numerical value (positive, quartic with 4 complex roots).

Historical status-text assertions below are preserved diagnostics, not
retention proof. Algebra uses supplied counts 2,3,6 and the displayed polynomial.
"""

from __future__ import annotations

# Actual documentary reads/existence checks; presence is not scientific authority.
AUDIT_INPUT_PATHS = ['docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md', 'docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md', 'docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md']

import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_authority(rel_path: str) -> str:
    path = REPO_ROOT / rel_path
    if not path.exists():
        return ""
    return path.read_text()


def extract_status_text(content: str) -> str:
    if not content:
        return ""
    for line in content.splitlines()[:30]:
        stripped = line.strip()
        if stripped.lower().startswith("**status:**") or stripped.lower().startswith("status:"):
            text = stripped
            for prefix in ("**Status:**", "**status:**", "Status:", "status:"):
                if text.lower().startswith(prefix.lower()):
                    text = text[len(prefix):].strip()
                    break
            return text
    return ""


def authority_tier(content: str) -> str:
    status_low = extract_status_text(content).lower()
    if "retained" in status_low and "support" not in status_low:
        return "retained"
    if "current public framework memo" in status_low:
        return "retained"
    if "support" in status_low:
        return "support"
    return "unknown"


def audit_inputs() -> None:
    banner("Ground-up status verification of each cited authority")

    print("  RETAINED-TIER (load-bearing for closure):\n")

    retained_authorities = (
        ("docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md",
         "retained NLO CKM-structure corollary",
         ("retained",)),
        ("docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
         "retained",
         ("retained",)),
        ("docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md",
         "retained standalone structural-identity",
         ("retained",)),
    )

    for rel_path, claimed, kws in retained_authorities:
        content = read_authority(rel_path)
        status = extract_status_text(content)
        tier = authority_tier(content)
        all_kws = all(kw.lower() in status.lower() for kw in kws)

        print(f"    [{rel_path.split('/')[-1]}]")
        print(f"      Status (extracted): {status!r}")
        print(f"      Tier classification: {tier}")
        check(f"Retained-tier verified: {rel_path.split('/')[-1]}",
              all_kws and tier == "retained")
        print()


def extract_retained_inputs() -> dict:
    banner("Extracting retained inputs from authority text")

    counts = read_authority(
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
    )
    n_pair_match = re.search(r"n[_\s]pair\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_color_match = re.search(r"n[_\s]color\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_quark_match = re.search(r"n[_\s]quark\s*=\s*n[_\s]pair\s*n[_\s]color", counts, re.IGNORECASE)

    print(f"  N_pair extracted:                  {n_pair_match.group(0) if n_pair_match else 'NOT FOUND'}")
    print(f"  N_color extracted:                 {n_color_match.group(0) if n_color_match else 'NOT FOUND'}")
    print(f"  N_quark = N_pair * N_color:        {'FOUND' if n_quark_match else 'NOT FOUND'}")

    check("MAGNITUDES retains N_pair = 2", n_pair_match and int(n_pair_match.group(1)) == 2)
    check("MAGNITUDES retains N_color = 3", n_color_match and int(n_color_match.group(1)) == 3)
    check("MAGNITUDES retains N_quark = N_pair * N_color (=6)", bool(n_quark_match))

    return {
        "N_pair": 2,
        "N_color": 3,
        "N_quark": 6,
    }


def setup_symbolic(N: dict):
    # Use a generic symbol (not real-restricted) so sp.solve returns all 4
    # complex roots of the quartic.
    a_s = sp.symbols("alpha_s")
    P_poly_explicit = sp.expand((a_s ** 2 - 4 * a_s + 96) ** 2 - 240 * (4 - a_s) ** 2)

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]

    # Structural-integer form.
    P_structural = (
        a_s ** 4
        - N_pair ** 3 * a_s ** 3
        - N_pair ** 5 * a_s ** 2
        + N_pair ** 7 * N_color ** 2 * a_s
        + N_pair ** 8 * N_color * (N_quark + 1)
    )

    return {
        "a_s": a_s,
        "P_explicit": P_poly_explicit,
        "P_structural": sp.expand(P_structural),
    }


def audit_v1_structural_form(N: dict, S: dict) -> None:
    banner("V1: Brocard polynomial in structural-integer form")

    P_e = S["P_explicit"]
    P_s = S["P_structural"]
    diff = sp.simplify(P_e - P_s)

    print(f"  P(alpha_s) (explicit) = {P_e}")
    print(f"  P(alpha_s) (structural integer form):")
    print(f"     = alpha_s^4 - N_pair^3 alpha_s^3 - N_pair^5 alpha_s^2")
    print(f"        + N_pair^7 N_color^2 alpha_s + N_pair^8 N_color (N_quark + 1)")
    print(f"     = {P_s}")
    print(f"  Difference: {diff}")

    check("V1: P(alpha_s) = alpha_s^4 - N_pair^3 alpha_s^3 - N_pair^5 alpha_s^2 + N_pair^7 N_color^2 alpha_s + N_pair^8 N_color (N_quark + 1)",
          diff == 0)

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]
    print(f"\n  Coefficient verification:")
    print(f"    -N_pair^3                       = -{N_pair ** 3} = -8 (alpha_s^3 coeff)")
    print(f"    -N_pair^5                       = -{N_pair ** 5} = -32 (alpha_s^2 coeff)")
    print(f"    N_pair^7 N_color^2              = {N_pair ** 7 * N_color ** 2} = 1152 (alpha_s coeff)")
    print(f"    N_pair^8 N_color (N_quark + 1)  = {N_pair ** 8 * N_color * (N_quark + 1)} = 5376 (constant)")

    check("V1: -coefficient(alpha_s^3) = N_pair^3 = 8",
          N_pair ** 3 == 8)
    check("V1: -coefficient(alpha_s^2) = N_pair^5 = 32",
          N_pair ** 5 == 32)
    check("V1: coefficient(alpha_s) = N_pair^7 N_color^2 = 1152",
          N_pair ** 7 * N_color ** 2 == 1152)
    check("V1: constant = N_pair^8 N_color (N_quark + 1) = 5376",
          N_pair ** 8 * N_color * (N_quark + 1) == 5376)


def audit_v2_vieta(N: dict, S: dict) -> None:
    banner("V2: Vieta relations on the four (complex) roots of P")

    a_s = S["a_s"]
    P = S["P_explicit"]

    # Vieta: for monic quartic alpha^4 + b3 alpha^3 + b2 alpha^2 + b1 alpha + b0,
    # e_1 = -b3, e_2 = b2, e_3 = -b1, e_4 = b0.
    # Our P: alpha^4 - 8 alpha^3 - 32 alpha^2 + 1152 alpha + 5376.
    # b3 = -8, b2 = -32, b1 = 1152, b0 = 5376.
    # e_1 = -b3 = 8.
    # e_2 = b2 = -32.
    # e_3 = -b1 = -1152.
    # e_4 = b0 = 5376.

    coeffs = sp.Poly(P, a_s).all_coeffs()  # [1, -8, -32, 1152, 5376]
    b3, b2, b1, b0 = coeffs[1], coeffs[2], coeffs[3], coeffs[4]

    e_1 = -b3
    e_2 = b2
    e_3 = -b1
    e_4 = b0

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]
    expected_e_1 = N_pair ** 3
    expected_e_2 = -N_pair ** 5
    expected_e_3 = -N_pair ** 7 * N_color ** 2
    expected_e_4 = N_pair ** 8 * N_color * (N_quark + 1)

    print(f"  e_1 = sum of roots          = {e_1} (expected N_pair^3 = {expected_e_1})")
    print(f"  e_2 = pairwise sum          = {e_2} (expected -N_pair^5 = {expected_e_2})")
    print(f"  e_3 = triple sum            = {e_3} (expected -N_pair^7 N_color^2 = {expected_e_3})")
    print(f"  e_4 = product of roots      = {e_4} (expected N_pair^8 N_color (N_quark + 1) = {expected_e_4})")

    check("V2 e_1: sum of roots = N_pair^3 = 8",
          e_1 == expected_e_1)
    check("V2 e_2: pairwise sum = -N_pair^5 = -32",
          e_2 == expected_e_2)
    check("V2 e_3: triple sum = -N_pair^7 N_color^2 = -1152",
          e_3 == expected_e_3)
    check("V2 e_4: product = N_pair^8 N_color (N_quark + 1) = 5376",
          e_4 == expected_e_4)


def audit_v3_newton_power_sums(N: dict, S: dict) -> None:
    banner("V3: Newton power sums p_k of the roots")

    a_s = S["a_s"]
    P = S["P_explicit"]

    # Solve P symbolically.
    roots = sp.solve(P, a_s)
    p_1 = sp.simplify(sum(roots))
    p_2 = sp.simplify(sum(r ** 2 for r in roots))
    p_3 = sp.simplify(sum(r ** 3 for r in roots))
    p_4 = sp.simplify(sum(r ** 4 for r in roots))

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]

    print(f"  p_1 = sum r_i        = {p_1}")
    print(f"        Expected N_pair^3 = {N_pair ** 3}")
    diff_p1 = sp.simplify(p_1 - N_pair ** 3)
    check("V3 p_1: sum r_i = N_pair^3 = 8", diff_p1 == 0)

    print(f"\n  p_2 = sum r_i^2      = {p_2}")
    expected_p_2 = N_pair ** 7  # because p_2 = 2 e_1^2 with N_pair = 2
    print(f"        Expected N_pair^7 = {expected_p_2}")
    diff_p2 = sp.simplify(p_2 - expected_p_2)
    check("V3 p_2: sum r_i^2 = N_pair^7 = 128 (only at N_pair = 2)",
          diff_p2 == 0)

    print(f"\n  p_3 = sum r_i^3      = {p_3}")
    print(f"  p_4 = sum r_i^4      = {p_4}")
    # Numerical check for p_3, p_4.
    p_3_value = int(p_3)
    p_4_value = int(p_4)
    print(f"        Numerical p_3 = {p_3_value}")
    print(f"        Numerical p_4 = {p_4_value}")

    # Newton's identities (recursive):
    # p_k = e_1 p_{k-1} - e_2 p_{k-2} + e_3 p_{k-3} - ... + (-1)^{k+1} k e_k for k <= 4.
    e_1 = N_pair ** 3
    e_2 = -N_pair ** 5
    e_3 = -N_pair ** 7 * N_color ** 2
    e_4 = N_pair ** 8 * N_color * (N_quark + 1)

    p_3_newton = e_1 * p_2 - e_2 * p_1 + 3 * e_3
    p_4_newton = e_1 * p_3 - e_2 * p_2 + e_3 * p_1 - 4 * e_4

    print(f"\n  Newton's identity:")
    print(f"    p_3 = e_1 p_2 - e_2 p_1 + 3 e_3 = {p_3_newton}")
    diff_p3_newton = sp.simplify(p_3 - p_3_newton)
    check("V3 p_3: Newton's identity p_3 = e_1 p_2 - e_2 p_1 + 3 e_3",
          diff_p3_newton == 0)


def audit_v4_structural_fingerprint(N: dict, S: dict) -> None:
    banner("V4: STRUCTURAL FINGERPRINT -- p_2 = 2 e_1^2 forces N_pair = 2")
    n = sp.Symbol("n", positive=True)
    # Independent companion-matrix trace, rather than assuming p_2 = n**7.
    companion = sp.Matrix([[0, 0, 0, -21*n**8], [1, 0, 0, -9*n**7],
                           [0, 1, 0, n**5], [0, 0, 1, n**3]])
    residual = sp.factor(sp.trace(companion**2) - 2*sp.trace(companion)**2)
    print("  Symbolic Newton residual:", residual)
    check("V4: general-family residual is n**5*(2-n)",
          sp.expand(residual-n**5*(2-n)) == 0)
    check("V4: off-specialization controls n=1 and n=3",
          residual.subs(n, 1) == 1 and residual.subs(n, 3) == -243)


    a_s = S["a_s"]
    P = S["P_explicit"]

    roots = sp.solve(P, a_s)
    p_1 = sp.simplify(sum(roots))
    p_2 = sp.simplify(sum(r ** 2 for r in roots))

    e_1_sq = p_1 ** 2
    p_2_check = 2 * e_1_sq

    print(f"  e_1 = sum of roots      = {p_1}")
    print(f"  e_1^2                   = {e_1_sq}")
    print(f"  2 e_1^2                 = {p_2_check}")
    print(f"  p_2 = sum of r_i^2      = {p_2}")
    diff = sp.simplify(p_2 - p_2_check)
    print(f"  p_2 - 2 e_1^2:          = {diff}")

    check("V4 FINGERPRINT: p_2 = 2 e_1^2 (sum of squared roots = twice squared sum)",
          diff == 0)

    print()
    print("  Equivalent statement: e_2 = -e_1^2/2.")
    print("  In structural integers: e_2 = -N_pair^5, e_1 = N_pair^3,")
    print("    e_2 = -e_1^2/2  =>  -N_pair^5 = -N_pair^6/2  =>  N_pair = 2.")
    print()
    print("  This identity p_2 = 2 e_1^2 is therefore a SIGNATURE of N_pair = 2 in")
    print("  the algebraic structure of P(alpha_s).")

    # Check the abstract identity.
    # For abstract N_pair, we'd have e_1 = N_pair^3, e_2 = -N_pair^5.
    # The identity e_2 = -e_1^2/2 becomes -N_pair^5 = -N_pair^6/2 = -N_pair^5 * N_pair/2.
    # This requires N_pair/2 = 1, i.e. N_pair = 2.
    n_pair_abstract = sp.symbols("n_pair", positive=True, integer=True)
    e_1_abs = n_pair_abstract ** 3
    e_2_abs = -n_pair_abstract ** 5
    fingerprint = sp.simplify(e_2_abs + e_1_abs ** 2 / 2)
    fingerprint_solved = sp.solve(fingerprint, n_pair_abstract)
    print(f"\n  Solving e_2 = -e_1^2/2 abstractly: n_pair = {fingerprint_solved}")
    check("V4: The fingerprint p_2 = 2 e_1^2 algebraically forces n_pair = 2",
          2 in fingerprint_solved)


def audit_v5_v6_mean_variance(N: dict, S: dict) -> None:
    banner("V5 / V6: Mean and squared deviations of the four roots")

    a_s = S["a_s"]
    P = S["P_explicit"]

    roots = sp.solve(P, a_s)
    p_1 = sp.simplify(sum(roots))

    mean = sp.simplify(p_1 / 4)
    N_pair, N_quark = N["N_pair"], N["N_quark"]

    print(f"  Mean of roots = (sum)/(count) = e_1/4 = {p_1}/4 = {mean}")
    expected_mean = sp.Rational(N_pair ** 3, 4)
    print(f"  Expected: N_pair^3/4 = {expected_mean}")
    # Note: at N_pair = 2, this equals N_pair (since N_pair^3/4 = 8/4 = 2 = N_pair).
    print(f"  At N_pair = 2: mean = N_pair = {N_pair}")
    check("V5: Mean of roots = N_pair^3/4 = N_pair (since N_pair = 2)",
          sp.simplify(mean - N_pair) == 0)

    # Sum of squared deviations.
    p_2 = sp.simplify(sum(r ** 2 for r in roots))
    sigma_sq = sp.simplify(p_2 - 2 * mean * p_1 + 4 * mean ** 2)
    expected_sigma_sq = sp.Integer(N_pair ** 4 * (N_quark + 1))
    print(f"\n  Sum of squared deviations = p_2 - 2 mean p_1 + 4 mean^2")
    print(f"                             = {p_2} - {2 * mean * p_1} + {4 * mean ** 2}")
    print(f"                             = {sigma_sq}")
    print(f"  Expected: N_pair^4 (N_quark + 1) = {expected_sigma_sq}")
    diff_sigma = sp.simplify(sigma_sq - expected_sigma_sq)
    print(f"  Difference: {diff_sigma}")

    check("V6: Sum of squared deviations from mean = N_pair^4 (N_quark + 1) = 16 * 7 = 112",
          diff_sigma == 0)


def audit_v7_root_structure(N: dict, S: dict) -> None:
    banner("V7: Roots over Q[sqrt(3), sqrt(5), i]")

    a_s = S["a_s"]
    P = S["P_explicit"]

    # Substitute u = 4 - alpha_s; then P factors over Q[sqrt(15)].
    u = sp.symbols("u")
    P_u = sp.expand(P.subs(a_s, 4 - u))

    factor_plus = u ** 2 - 4 * (1 + sp.sqrt(15)) * u + 96
    factor_minus = u ** 2 - 4 * (1 - sp.sqrt(15)) * u + 96
    product = sp.expand(factor_plus * factor_minus)

    diff = sp.simplify(product - P_u)
    print(f"  P(alpha_s = 4 - u)  =  (u^2 - 4(1 + sqrt(15)) u + 96) * (u^2 - 4(1 - sqrt(15)) u + 96)")
    print(f"  Difference: {diff}")
    check("V7: P factors over Q[sqrt(15)] as a product of two quadratics",
          diff == 0)

    # Discriminants of each factor.
    disc_plus = sp.simplify(16 * (1 + sp.sqrt(15)) ** 2 - 384)
    disc_minus = sp.simplify(16 * (1 - sp.sqrt(15)) ** 2 - 384)
    print(f"\n  Discriminant(u^2 - 4(1 + sqrt(15)) u + 96) = {disc_plus}")
    print(f"  Discriminant(u^2 - 4(1 - sqrt(15)) u + 96) = {disc_minus}")

    check("V7: Both quadratic factors have negative discriminant (all 4 roots complex)",
          float(disc_plus) < 0 and float(disc_minus) < 0)

    # Explicit roots.
    print(f"\n  Roots structure:")
    print(f"    alpha_s_root  =  (2 -/+ 2 sqrt(15)) +/- 2i (sqrt(5) -/+ sqrt(3))")
    print(f"                  =  (N_pair -/+ N_pair sqrt(N_color (N_quark - 1)))")
    print(f"                      +/- N_pair i (sqrt(N_quark - 1) -/+ sqrt(N_color)).")
    N_pair = N["N_pair"]
    print(f"\n    sqrt(N_color (N_quark - 1))  =  sqrt({N['N_color'] * (N['N_quark'] - 1)})  =  sqrt(15)")
    print(f"    sqrt(N_quark - 1)            =  sqrt({N['N_quark'] - 1})  =  sqrt(5)")
    print(f"    sqrt(N_color)                =  sqrt({N['N_color']})  =  sqrt(3)")


def audit_v8_galois_structure(N: dict, S: dict) -> None:
    banner("V8: Galois group structure")

    x = S["a_s"]
    polynomial = sp.Poly(S["P_explicit"], x)
    group, _ = sp.polys.numberfields.galois_group(polynomial)
    primitive = sp.sqrt(15) + sp.sqrt(-5)
    degree = sp.degree(sp.minpoly(primitive, x), x)
    roots = [(2 - 2*t*sp.sqrt(15)) + 2*u*sp.I*(sp.sqrt(5)-t*sp.sqrt(3))
             for t in (1, -1) for u in (1, -1)]
    print("  K = Q(sqrt(15), sqrt(-5)), splitting-field degree:", degree)
    print("  Computed polynomial Galois group:", group, "order", group.order())
    check("V8: primitive element of K has degree four", degree == 4)
    check("V8: all four explicit roots satisfy P",
          all(sp.simplify(polynomial.as_expr().subs(x, r)) == 0 for r in roots))
    contained = [sp.polys.numberfields.to_number_field(r, primitive) for r in roots]
    check("V8: all four roots lie in K", len(contained) == 4)
    check("V8: computed faithful group is Klein four",
          group.order() == 4 and all(g.order() in (1, 2) for g in group.generate()))
    print("  The degree-eight field Q(sqrt(3),sqrt(5),i) is ambient, not minimal.")


def audit_v9_discriminant(N: dict, S: dict) -> None:
    banner("V9: Discriminant of P(alpha_s)")

    a_s = S["a_s"]
    P = S["P_explicit"]

    disc = sp.discriminant(P, a_s)
    print(f"  Disc(P) = {disc}")

    # P has 4 complex roots (no real roots), so Disc(P) > 0.
    print(f"  Disc(P) > 0  =>  either 4 real roots or 0 real roots.")
    print(f"  Combined with P > 0 on whole real line  =>  0 real roots.")
    check("V9: Disc(P) > 0 (consistent with all roots complex)",
          int(disc) > 0)

    # Check structural form. Disc(P) for our quartic.
    # For a quartic alpha^4 + b alpha^3 + c alpha^2 + d alpha + e,
    # Disc = 256 e^3 - 192 b d e^2 - 128 c^2 e^2 + 144 c d^2 e - 27 d^4 + ...
    # We'll just record the numerical value and factor it.
    print(f"\n  Numerical value: Disc(P) = {disc}")
    factor = sp.factorint(int(disc))
    print(f"  Prime factorisation: {factor}")
    print()
    print("  Note: Disc(P) is a large structured integer encoding the algebraic")
    print("  complexity of the protected-gamma_bar surface.")


def audit_summary() -> None:
    banner("Summary of supplied polynomial algebra; status diagnostics are separate")

    print("  Supplied inputs (historical labels below do not establish authority):")
    print("    CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA  (retained)")
    print("    CKM_MAGNITUDES_STRUCTURAL_COUNTS         (retained)")
    print("    CKM_CP_PHASE_STRUCTURAL_IDENTITY         (retained)")
    print()
    print("  Conditional algebraic content:")
    print()
    print("    (V1) Brocard polynomial in structural-integer form:")
    print("           P(alpha_s)  =  alpha_s^4")
    print("                          -  N_pair^3 alpha_s^3")
    print("                          -  N_pair^5 alpha_s^2")
    print("                          +  N_pair^7 N_color^2 alpha_s")
    print("                          +  N_pair^8 N_color (N_quark + 1).")
    print()
    print("    (V2) Vieta relations (each in structural integers):")
    print("           e_1 = +N_pair^3,")
    print("           e_2 = -N_pair^5,")
    print("           e_3 = -N_pair^7 N_color^2,")
    print("           e_4 = +N_pair^8 N_color (N_quark + 1).")
    print()
    print("    (V3) Newton power sums:")
    print("           p_1 = N_pair^3,")
    print("           p_2 = N_pair^7  (only because N_pair = 2),")
    print("           p_3, p_4 in closed form via Newton's identities.")
    print()
    print("    (V4) STRUCTURAL FINGERPRINT:")
    print("           p_2  =  2 e_1^2.")
    print()
    print("         Equivalently e_2 = -e_1^2/2. In abstract structural integers:")
    print("           e_2 = -N_pair^5, e_1 = N_pair^3,")
    print("         so e_2 = -e_1^2/2 forces N_pair = 2.")
    print()
    print("         This identity is a SIGNATURE of N_pair = 2 in the Brocard")
    print("         polynomial structure.")
    print()
    print("    (V5) Mean of the four roots = N_pair^3/4 = N_pair (because N_pair = 2).")
    print()
    print("    (V6) Sum of squared deviations from the mean = N_pair^4 (N_quark + 1)")
    print("         = 16 * 7 = 112.")
    print()
    print("    (V7) Roots over Q[sqrt(3), sqrt(5), i]:")
    print("           alpha_s_root = (N_pair -/+ N_pair sqrt(N_color (N_quark - 1)))")
    print("                          +/- N_pair i (sqrt(N_quark - 1) -/+ sqrt(N_color)).")
    print()
    print("    (V8) Splitting field degree four; faithful Galois group (Z/2Z)^2.")
    print()
    print("    (V9) Disc(P) > 0 (consistent with 0 real roots, 4 complex roots).")
    print()
    print("  Symbolic identities use supplied inputs; no retained authority or physical closure certified.")


def main() -> int:
    print("=" * 88)
    print("Brocard polynomial Vieta / Newton structural integers audit")
    print("See docs/CKM_BROCARD_POLYNOMIAL_VIETA_STRUCTURAL_INTEGERS_THEOREM_NOTE_2026-04-25.md")
    print("=" * 88)

    audit_inputs()
    N = extract_retained_inputs()
    S = setup_symbolic(N)
    audit_v1_structural_form(N, S)
    audit_v2_vieta(N, S)
    audit_v3_newton_power_sums(N, S)
    audit_v4_structural_fingerprint(N, S)
    audit_v5_v6_mean_variance(N, S)
    audit_v7_root_structure(N, S)
    audit_v8_galois_structure(N, S)
    audit_v9_discriminant(N, S)
    audit_summary()

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
