"""
Probe X-L1-MSbar — Beta-function source check and incomplete lattice/<P> rescaling.

Authority role
--------------
Source-note proposal -- audit verdict and downstream status set only by
the independent audit lane.

Purpose
=======
Test whether the physical Cl(3) local algebra / Z^3 framework's source content can derive the
3-loop (beta_2) and 4-loop (beta_3) MSbar QCD beta-function coefficients,
and whether the stipulated lattice/<P> rescaling defines such coefficients.

Verdict structure
=================
The probe is an open_gate (bounded diagnostic, mostly negative on full
derivation, with conditional/supplied-formula coefficient checks and
candidate-monomial diagnostics).

Conditional, supplied-formula, and arithmetic checks (PASS expected):
  1. beta_0 = (11 N_color − 2 N_quark)/3 = 7 at N_f=6 (conditional
     upstream re-expression via S1+matter count)
  2. beta_1 = (34/3) C_A^2 − (20/3) C_A T_F N_f − 4 C_F T_F N_f = 26
     at N_f=6 (supplied standard-continuum formula; substitution check)
  3. Candidate Casimir monomials: arithmetic diagnostic only
  4. Candidate quartic-Casimir monomials: arithmetic diagnostic only
  5. <P>_HK_SU(3)(s_t) = 1 - exp(-(4/3) s_t) closed form used as
     stipulated coupling rescaling
  6. The <P> rescaling differs algebraically from the bare coupling; no full
     renormalization scheme or higher beta coefficient is inferred

Open inputs (reported, no derivation):
  7. beta_2 in MSbar: matching/integral data are NOT in current source content;
     the stipulated <P> rescaling defines no beta coefficient
  8. beta_3: same MSbar source gap and incomplete-<P> boundary at 4-loop

Numerical comparators (PASS expected on literature cross-check):
  9. beta_2^MSbar(N_f=6) = -65/2 = -32.5  (Tarasov-Vladimirov-Zharkov 1980)
 10. beta_3^MSbar(N_f=6) ≈ 2472.28  (van Ritbergen et al. 1997)

Forbidden imports respected:
- NO PDG observed values used as derivation input
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO new axioms

References
==========
- Tarasov O.V., Vladimirov A.A., Zharkov A.Yu. (1980), Phys. Lett. B 93, 429.
- Larin S.A., Vermaseren J.A.M. (1993), Phys. Lett. B 303, 334.
- van Ritbergen T., Vermaseren J.A.M., Larin S.A. (1997), Phys. Lett. B 400, 379.
- Czakon M. (2005), Nucl. Phys. B 710, 485.
- Lüscher M., Weisz P. (1995), Nucl. Phys. B 452, 234.
- Christou C., Feo A., Panagopoulos H., Vicari E. (1998),
  Nucl. Phys. B 525, 387 (with erratum).

Source-note authority
=====================
docs/KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md

Usage
=====
    python3 scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction


# ----------------------------------------------------------------------
# PASS/FAIL bookkeeping
# ----------------------------------------------------------------------

class Counter:
    """Simple counter for PASS / FAIL / OPEN outcomes."""

    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.open_inputs = 0
        self.failures: list[str] = []

    def record(self, name: str, ok: bool, detail: str = "") -> None:
        tag = "PASS" if ok else "FAIL"
        if detail:
            print(f"  [{tag}] {name} | {detail}")
        else:
            print(f"  [{tag}] {name}")
        if ok:
            self.passed += 1
        else:
            self.failed += 1
            self.failures.append(name)

    def open_input(self, name: str, detail: str = "") -> None:
        if detail:
            print(f"  [OPEN] {name} | {detail}")
        else:
            print(f"  [OPEN] {name}")
        self.open_inputs += 1

    def summary(self) -> None:
        print()
        print(f"SUMMARY: PASS={self.passed} FAIL={self.failed} OPEN={self.open_inputs}")
        if self.failed:
            print(f"FAILURES: {', '.join(self.failures)}")


# ----------------------------------------------------------------------
# Supplied and cited Casimir context
# ----------------------------------------------------------------------

# SU(3) Casimirs from YT_EW_COLOR_PROJECTION_THEOREM.md (D7) +
# YT_EXACT_SCHUR_NORMAL_FORM_UNIQUENESS_NOTE.md (S1).
N_COLOR = 3
N_PAIR = 2
N_QUARK = N_COLOR * N_PAIR  # = 6 from S1
N_GEN = 3
N_F = N_QUARK  # asymptotic (above all SM thresholds)
C_F = Fraction(N_COLOR ** 2 - 1, 2 * N_COLOR)  # 4/3
C_A = Fraction(N_COLOR)  # 3
T_F = Fraction(1, 2)


# ----------------------------------------------------------------------
# SECTION 1 — CONDITIONAL SOURCE CHECK: beta_0
# ----------------------------------------------------------------------

def section1_beta_0_conditional(c: Counter) -> None:
    """beta_0 = (11 N_color − 2 N_quark)/3 = 7 at N_f=6.

    From SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26
    inline companion form b_3 (QCD): b_3 = (11 N_color − 2 N_quark)/3.
    At upstream N_color=3, N_quark=6: b_3 = (33-12)/3 = 21/3 = 7.

    This coefficient is universal at one loop across suitably normalized
    mass-independent coupling conventions. No coefficient is assigned here
    to the incomplete stipulated <P> prescription.
    """
    print("Section 1 — CONDITIONAL SOURCE CHECK: beta_0 (1-loop) = 7")

    # Direct from S1 + Casimir
    beta_0_S1 = Fraction(11 * N_COLOR - 2 * N_QUARK, 3)
    c.record(
        "beta_0 = (11 N_color − 2 N_quark)/3 from S1",
        beta_0_S1 == Fraction(7),
        f"= (33-12)/3 = {beta_0_S1} (target 7)",
    )

    # Equivalently from Casimir form: beta_0 = (11/3) C_A − (4/3) T_F N_f
    beta_0_casimir = Fraction(11, 3) * C_A - Fraction(4, 3) * T_F * N_F
    c.record(
        "beta_0 = (11/3) C_A − (4/3) T_F N_f from Casimir",
        beta_0_casimir == Fraction(7),
        f"= {Fraction(11,3)}*3 − {Fraction(4,3)}*{T_F}*{N_F} = "
        f"11 − 4 = {beta_0_casimir} (target 7)",
    )

    # Equivalence of the two forms
    c.record(
        "S1 form ≡ Casimir form for beta_0",
        beta_0_S1 == beta_0_casimir,
        f"both = {beta_0_S1}",
    )

    print("    → beta_0 has the cited conditional S1/matter-count re-expression.")


# ----------------------------------------------------------------------
# SECTION 2 — SUPPLIED-FORMULA CHECK: beta_1 (2-loop)
# ----------------------------------------------------------------------

def section2_beta_1_supplied_formula(c: Counter) -> None:
    """beta_1 = (34/3) C_A^2 − (20/3) C_A T_F N_f − 4 C_F T_F N_f at N_f=6.

    Supplied standard-continuum two-loop QCD formula.
    With upstream (C_F=4/3, C_A=3, T_F=1/2, N_f=6):
      term_gauge = (34/3)·9 = 102
      term_mixed = -(20/3)·3·(1/2)·6 = -60
      term_quark = -4·(4/3)·(1/2)·6 = -16
      sum = 102 - 60 - 16 = 26
    """
    print()
    print("Section 2 — SUPPLIED-FORMULA CHECK: beta_1 (2-loop) = 26")

    term_gauge = Fraction(34, 3) * C_A * C_A
    term_mixed = -Fraction(20, 3) * C_A * T_F * N_F
    term_quark = -4 * C_F * T_F * N_F
    beta_1 = term_gauge + term_mixed + term_quark

    c.record(
        "beta_1 gauge term = (34/3) C_A^2 = 102",
        term_gauge == Fraction(102),
        f"(34/3)·9 = {term_gauge}",
    )
    c.record(
        "beta_1 mixed term = -(20/3) C_A T_F N_f = -60",
        term_mixed == Fraction(-60),
        f"-(20/3)·3·(1/2)·6 = {term_mixed}",
    )
    c.record(
        "beta_1 quark term = -4 C_F T_F N_f = -16",
        term_quark == Fraction(-16),
        f"-4·(4/3)·(1/2)·6 = {term_quark}",
    )
    c.record(
        "beta_1 total = 102 - 60 - 16 = 26",
        beta_1 == Fraction(26),
        f"= {beta_1} (target 26)",
    )

    print("    → Substitution reproduces the supplied standard-continuum formula.")
    print("    → Casimirs do not derive the scalar weights 34/3, 20/3, and 4.")


# ----------------------------------------------------------------------
# SECTION 3 — ALGEBRAIC DIAGNOSTIC: candidate Casimir monomials
# ----------------------------------------------------------------------

def section3_three_loop_color_skeleton(c: Counter) -> None:
    """Evaluate a finite candidate list of Casimir monomials.

    This arithmetic does not enumerate Feynman topologies or establish the
    actual nonzero three-loop beta-function basis.
    """
    print()
    print("Section 3 — ALGEBRAIC DIAGNOSTIC: candidate 3-loop Casimir monomials")

    # Nine candidate monomials, evaluated at
    # (C_F=4/3, C_A=3, T_F=1/2, N_f=6).
    candidate_monomials_3loop = [
        ("C_F^3", C_F * C_F * C_F, Fraction(64, 27)),
        ("C_F^2 C_A", C_F * C_F * C_A, Fraction(16, 3)),
        ("C_F C_A^2", C_F * C_A * C_A, Fraction(12, 1)),
        ("C_A^3", C_A * C_A * C_A, Fraction(27, 1)),
        # C_F^2 T_F N_f = (16/9) · (1/2) · 6 = (16/9) · 3 = 16/3
        ("C_F^2 T_F N_f", C_F * C_F * T_F * N_F, Fraction(16, 3)),
        # C_F C_A T_F N_f = (4/3) · 3 · (1/2) · 6 = 12
        ("C_F C_A T_F N_f", C_F * C_A * T_F * N_F, Fraction(12, 1)),
        # C_A^2 T_F N_f = 9 · (1/2) · 6 = 27
        ("C_A^2 T_F N_f", C_A * C_A * T_F * N_F, Fraction(27, 1)),
        # C_F (T_F N_f)^2 = (4/3) · (3)^2 = (4/3) · 9 = 12
        ("C_F (T_F N_f)^2", C_F * (T_F * N_F) ** 2, Fraction(12, 1)),
        # C_A (T_F N_f)^2 = 3 · 9 = 27
        ("C_A (T_F N_f)^2", C_A * (T_F * N_F) ** 2, Fraction(27, 1)),
    ]

    for name, computed, expected in candidate_monomials_3loop:
        c.record(
            f"3-loop candidate monomial '{name}' value at SU(3), N_f=6",
            computed == expected,
            f"= {computed} (target {expected})",
        )

    print("    → Candidate-monomial arithmetic is reproduced.")
    print("    → No exhaustive diagrammatic basis or monomial weights follow.")


# ----------------------------------------------------------------------
# SECTION 4 — ALGEBRAIC DIAGNOSTIC: quartic Casimir values
# ----------------------------------------------------------------------

def section4_four_loop_color_skeleton(c: Counter) -> None:
    """At 4-loop, the Casimir basis extends to include quartic invariants
    d_F^{abcd} d_F^{abcd} / N_R and d_F^{abcd} d_A^{abcd} / N_R for
    SU(3). For the fundamental representation:
      d_F^{abcd} d_F^{abcd} / N_F = 5/36
      d_F^{abcd} d_A^{abcd} / N_F = 5/2
      d_A^{abcd} d_A^{abcd} / N_A = 135/8

    Their values do not establish the actual nonzero four-loop beta basis.
    """
    print()
    print("Section 4 — ALGEBRAIC DIAGNOSTIC: quartic Casimir values")

    # Recompute the SU(N) quartic invariants from their group-theory formulas.
    nc = N_COLOR
    d_FF_over_NF = Fraction(
        (nc ** 2 - 1) * (nc ** 4 - 6 * nc ** 2 + 18),
        96 * nc ** 3,
    )
    d_FA_over_NF = Fraction((nc ** 2 - 1) * (nc ** 2 + 6), 48)
    d_AA_over_NA = Fraction(nc ** 2 * (nc ** 2 + 36), 24)

    c.record(
        "Quartic invariant d_F^abcd d_F^abcd / N_F = 5/36 (SU(3) fundamental)",
        d_FF_over_NF == Fraction(5, 36),
        f"= {d_FF_over_NF}",
    )
    c.record(
        "Quartic invariant d_F^abcd d_A^abcd / N_F = 5/2 (SU(3))",
        d_FA_over_NF == Fraction(5, 2),
        f"= {d_FA_over_NF}",
    )
    c.record(
        "Quartic invariant d_A^abcd d_A^abcd / N_A = 135/8 (SU(3) adjoint)",
        d_AA_over_NA == Fraction(135, 8),
        f"= {d_AA_over_NA}",
    )

    print("    → Quartic-invariant arithmetic is reproduced.")
    print("    → No exhaustive four-loop diagrammatic basis follows.")


# ----------------------------------------------------------------------
# SECTION 5 — CONVENTION DIAGNOSTIC: stipulated <P> rescaling
# ----------------------------------------------------------------------

def section5_p_rescaling(c: Counter) -> None:
    """Evaluate the stipulated <P> rescaling expression:
       <P>_HK_SU(3)(s_t) = 1 - exp(-(4/3) s_t)
    with s_t = g^2 / (2 xi).

    This does not by itself specify a complete renormalization condition.
    """
    print()
    print("Section 5 — CONVENTION DIAGNOSTIC: stipulated <P> rescaling")

    # Verify <P>_HK closed form for representative s_t values
    def P_HK_SU3(s_t: float) -> float:
        return 1.0 - math.exp(-(4.0 / 3.0) * s_t)

    # At s_t = 1/2 (xi=1, g^2=1)
    s_t_test = 0.5
    P_HK = P_HK_SU3(s_t_test)
    P_HK_expected = 1.0 - math.exp(-2.0 / 3.0)
    c.record(
        "<P>_HK_SU(3)(s_t=1/2) = 1 - exp(-2/3) ≈ 0.4866",
        abs(P_HK - P_HK_expected) < 1e-12,
        f"= {P_HK:.6f} (expected {P_HK_expected:.6f})",
    )

    # Taylor expansion at small s_t: <P>_HK = (4/3) s_t - (8/9) s_t^2 + (32/81) s_t^3
    s_t_small = 0.01
    P_HK_small = P_HK_SU3(s_t_small)
    P_HK_taylor = (
        (4.0 / 3.0) * s_t_small
        - (8.0 / 9.0) * s_t_small ** 2
        + (32.0 / 81.0) * s_t_small ** 3
    )
    c.record(
        "<P>_HK Taylor expansion at small s_t agrees with closed form",
        abs(P_HK_small - P_HK_taylor) < 1e-7,
        f"closed = {P_HK_small:.8f}, Taylor = {P_HK_taylor:.8f}",
    )

    # The stipulated rescaling is not a renormalization point or scheme.
    # alpha_<P>(beta) = alpha_bare(beta) / <P>(beta)
    # This is structurally different from
    # alpha_MSbar(mu) = alpha_bare(beta) * Z_MSbar(beta, a*mu)
    print("    → The stipulated <P> expression is evaluated algebraically.")
    print("    → It does not alone define a full renormalization scheme.")


# ----------------------------------------------------------------------
# SECTION 6 — CONVENTION DIAGNOSTIC: <P> rescaling differs from bare coupling
# ----------------------------------------------------------------------

def section6_rescaling_difference(c: Counter) -> None:
    """Verify only that the stipulated <P> rescaling changes alpha_bare."""
    print()
    print("Section 6 — CONVENTION DIAGNOSTIC: <P> rescaling differs from bare coupling")

    # Evaluate the stipulated rescaling at one representative point.
    s_t_canonical = 1.0 / 12.0  # corresponds to xi=6, g^2=1
    P_HK = 1.0 - math.exp(-(4.0 / 3.0) * s_t_canonical)
    P_HK_canonical = P_HK
    # Stipulated algebraic rescaling: alpha_<P>(beta=6) = alpha_bare / <P>
    # alpha_bare = g_bare^2/(4 pi) = 1/(4 pi) [upstream g_bare=1]
    alpha_bare = 1.0 / (4.0 * math.pi)
    alpha_P_rescaled = alpha_bare / P_HK_canonical
    c.record(
        "at beta=6 the stipulated alpha_<P> differs from alpha_bare",
        alpha_P_rescaled != alpha_bare,
        f"alpha_bare = {alpha_bare:.5f}, alpha_<P> = {alpha_P_rescaled:.5f}, "
        f"<P>_HK_canonical = {P_HK_canonical:.5f}",
    )

    print("    → The stipulated <P> rescaling differs algebraically from alpha_bare.")
    print("    → This does not define a full renormalization condition or beta_2.")


# ----------------------------------------------------------------------
# SECTION 7 — OPEN INPUT: MSbar beta_2; incomplete <P> rescaling
# ----------------------------------------------------------------------

def section7_beta_2_open_inputs(c: Counter) -> None:
    """At 3-loop, the occurrence and weights of nine candidate Casimir
    monomials are not determined by their arithmetic values.
    """
    print()
    print("Section 7 — OPEN INPUT: MSbar beta_2; <P> rescaling defines no beta_2")

    candidate_monomial_3loop_names = [
        "c_FFF (C_F^3)",
        "c_FFA (C_F^2 C_A)",
        "c_FAA (C_F C_A^2)",
        "c_AAA (C_A^3)",
        "c_FFn (C_F^2 T_F N_f)",
        "c_FAn (C_F C_A T_F N_f)",
        "c_AAn (C_A^2 T_F N_f)",
        "c_Fnn (C_F (T_F N_f)^2)",
        "c_Ann (C_A (T_F N_f)^2)",
    ]
    for name in candidate_monomial_3loop_names:
        c.open_input(
            f"3-loop candidate monomial occurrence/weight '{name}'",
            "candidate occurrence and weight are not supplied by this arithmetic",
        )

    print("    → Nine candidate-monomial occurrences/weights are NOT framework-derived.")
    print("    → MSbar requires imported matching/integral data.")
    print("    → The stipulated <P> rescaling defines no beta coefficient.")
    print("    → Other schemes defined by finite coupling redefinitions are not excluded.")


# ----------------------------------------------------------------------
# SECTION 8 — OPEN INPUT: MSbar beta_3; incomplete <P> rescaling
# ----------------------------------------------------------------------

def section8_beta_3_open_inputs(c: Counter) -> None:
    """At 4-loop MSbar requires external perturbative data, while the
    incomplete stipulated <P> rescaling defines no beta coefficient. This is
    a source-content/definition gap, not a claim about the complete literature.
    """
    print()
    print("Section 8 — OPEN INPUT: MSbar beta_3; <P> rescaling defines no beta_3")

    candidate_monomial_4loop_names = [
        "c_F^4 (C_F^4)",
        "c_F^3 A (C_F^3 C_A)",
        "c_F^2 A^2 (C_F^2 C_A^2)",
        "c_F A^3 (C_F C_A^3)",
        "c_A^4 (C_A^4)",
        "c_dF dF (d_F^abcd d_F^abcd / N_F)",
        "c_dF dA (d_F^abcd d_A^abcd / N_F)",
        "c_F^3 n (C_F^3 T_F N_f)",
        "c_F^2 A n (C_F^2 C_A T_F N_f)",
        "c_F A^2 n (C_F C_A^2 T_F N_f)",
        "c_A^3 n (C_A^3 T_F N_f)",
        "c_dF dF n (d_F^abcd d_F^abcd N_f / N_F)",
        "c_F^2 n^2 (C_F^2 (T_F N_f)^2)",
        "c_F A n^2 (C_F C_A (T_F N_f)^2)",
        "c_A^2 n^2 (C_A^2 (T_F N_f)^2)",
        "c_F n^3 (C_F (T_F N_f)^3)",
        "c_A n^3 (C_A (T_F N_f)^3)",
    ]
    for name in candidate_monomial_4loop_names:
        c.open_input(
            f"4-loop candidate monomial occurrence/weight '{name}'",
            "candidate occurrence and weight are not supplied by this arithmetic",
        )

    print("    → 17 candidate-monomial occurrences/weights are NOT framework-derived.")
    print("    → The stipulated <P> rescaling defines no beta coefficient.")


# ----------------------------------------------------------------------
# SECTION 9 — NUMERICAL COMPARATOR: MSbar literature values
# ----------------------------------------------------------------------

def section9_msbar_literature_comparator(c: Counter) -> None:
    """Verify the published MSbar values reproduce the standard formulas
    at N_f=6.

    MSbar 3-loop (Tarasov-Vladimirov-Zharkov 1980):
      beta_2^MSbar = 2857/2 − (5033/18) N_f + (325/54) N_f^2

    At N_f=6:
      = 2857/2 − 5033/3 + 650/3
      = 2857/2 − 4383/3
      = 2857/2 − 1461
      = 2857/2 − 2922/2
      = -65/2

    NOTE on sign: some branch prose quoted the absolute value 65/2.
    The standard coefficient formula above gives the signed value
    -65/2 at N_f=6. We verify both the sign and the magnitude.

    These are LITERATURE-COMPARATOR values, not framework derivations.
    """
    print()
    print("Section 9 — NUMERICAL COMPARATOR: MSbar literature values at N_f=6")

    # Tarasov-Vladimirov-Zharkov 1980: beta_2 in MSbar at N_f=6
    # beta_2 = 2857/2 − (5033/18)·N_f + (325/54)·N_f^2
    beta_2_TVZ = (
        Fraction(2857, 2)
        - Fraction(5033, 18) * N_F
        + Fraction(325, 54) * N_F ** 2
    )
    # At N_f=6: 2857/2 − 5033/3 + 650/3 = 2857/2 − 4383/3
    # 4383/3 = 1461; 2857/2 - 1461 = 2857/2 - 2922/2 = -65/2
    beta_2_target = Fraction(-65, 2)
    c.record(
        "MSbar beta_2(N_f=6) = 2857/2 − (5033/18)·6 + (325/54)·36 = -65/2",
        beta_2_TVZ == beta_2_target,
        f"= {beta_2_TVZ} (target {beta_2_target} = {float(beta_2_target):.4f})",
    )

    # User noted absolute value 65/2 = 32.5
    c.record(
        "abs(beta_2^MSbar(N_f=6)) = 65/2 = 32.5 matches user-quoted value",
        abs(beta_2_TVZ) == Fraction(65, 2),
        f"|beta_2| = {abs(beta_2_TVZ)} = {float(abs(beta_2_TVZ))}",
    )

    # van Ritbergen-Vermaseren-Larin 1997: beta_3 in MSbar at N_f=6.
    # The full formula involves zeta_3. Note: there are several
    # normalization conventions in the literature for beta_3;
    # we report the numerical value computed from the published
    # formula in the convention beta(g) = -beta_0 g^3 ... and document
    # the result honestly.
    zeta_3 = 1.2020569031595942853997381  # Apery's constant
    n_f = 6
    beta_3_VVL_numerical = (
        149753.0 / 6.0 + 3564.0 * zeta_3
        - (1078361.0 / 162.0 + 6508.0 * zeta_3 / 27.0) * n_f
        + (50065.0 / 162.0 + 6472.0 * zeta_3 / 81.0) * n_f ** 2
        + 1093.0 / 729.0 * n_f ** 3
    )
    # The literature value at N_f=6 is approximately 2472.28 in this
    # convention. Different literature normalization conventions
    # (factor 4 differences from beta_n absorbed into (16 pi^2)^n) lead
    # to alternate numerical values.
    c.record(
        "MSbar beta_3(N_f=6) numerical value from VVL formula reproduced",
        math.isclose(
            beta_3_VVL_numerical,
            2472.2837425797165,
            rel_tol=0.0,
            abs_tol=1e-9,
        ),
        f"= {beta_3_VVL_numerical:.4f} "
        f"(VVL 1997 formula evaluation; convention beta = -beta_0 g^3 ...)",
    )

    # Keep this comparator tied to the formula and convention above.
    print("    INFO  The numerical beta_3 value is tied to the displayed convention;")
    print("          it is a comparator, not a framework derivation or all-scheme claim.")

    print("    → MSbar values reproduced from published formulas at N_f=6.")
    print("    → These are literature comparators, NOT framework derivations.")


# ----------------------------------------------------------------------
# SECTION 10 — Lattice scheme literature comparator
# ----------------------------------------------------------------------

def section10_lattice_scheme_comparator(c: Counter) -> None:
    """Keep fixed Wilson bare-lattice results distinct from this probe's
    incomplete stipulated <P> prescription.

    Lüscher-Weisz 1995 computes a two-loop bare-to-MSbar relation.
    Christou-Feo-Panagopoulos-Vicari 1998 computes the three-loop
    bare-lattice beta-function coefficient with Wilson fermions and the
    two-loop MSbar-to-bare relation. That fixed Wilson prescription does
    not define the stipulated <P> prescription used here.
    """
    print()
    print("Section 10 — LATTICE SCHEME COMPARATOR: lattice → MSbar matching cited")

    c.open_input(
        "beta_3 for the stipulated lattice/<P> rescaling at N_f=6",
        "undefined until a completed renormalization prescription is supplied",
    )

    print("    → Fixed Wilson bare-lattice perturbative results are cited literature.")
    print("    → They do not complete the stipulated <P> prescription.")
    print("    → No higher coefficient is inferred from this source-content inventory.")


# ----------------------------------------------------------------------
# SECTION 11 — VERDICT SUMMARY
# ----------------------------------------------------------------------

def section11_verdict(c: Counter) -> None:
    """Final verdict on probe X-L1-MSbar."""
    print()
    print("=" * 72)
    print("PROBE X-L1-MSbar VERDICT")
    print("=" * 72)
    print()
    print("Claim type: open_gate (bounded diagnostic, mostly negative on full derivation,")
    print("            with conditional/supplied checks at 1-loop, 2-loop, and")
    print("            candidate-monomial diagnostics)")
    print()
    print("Coefficient checks:")
    print("  ✓ beta_0 = (11 N_color − 2 N_quark)/3 = 7 (conditional re-expression)")
    print("  ✓ beta_1 = (34/3) C_A^2 − (20/3) C_A T_F N_f − 4 C_F T_F N_f = 26")
    print("    (supplied standard-continuum formula; substitution only)")
    print("  ✓ Candidate Casimir-monomial arithmetic reproduced")
    print("  ✓ <P>_HK_SU(3)(s_t) stipulated rescaling reproduced")
    print()
    print("OPEN inputs:")
    print("  ⚠ MSbar beta_2 and beta_3 remain external comparators")
    print("  ⚠ the stipulated <P> rescaling defines no beta_2 or beta_3")
    print()
    print("Net contribution to Lane 1:")
    print("  - Separates beta_0's conditional re-expression from supplied beta_1")
    print("  - Candidate monomial arithmetic supplies no exhaustive loop basis")
    print("  - The stipulated <P> rescaling defines no beta_2 or beta_3")
    print("  - Does NOT change the supplied two-loop bridge")
    print()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main() -> int:
    print("=" * 72)
    print("Probe X-L1-MSbar — MSbar source check and incomplete lattice/<P> rescaling")
    print("Date: 2026-05-10")
    print("Source-note authority:")
    print("  docs/KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md")
    print("=" * 72)
    print()

    counter = Counter()

    section1_beta_0_conditional(counter)
    section2_beta_1_supplied_formula(counter)
    section3_three_loop_color_skeleton(counter)
    section4_four_loop_color_skeleton(counter)
    section5_p_rescaling(counter)
    section6_rescaling_difference(counter)
    section7_beta_2_open_inputs(counter)
    section8_beta_3_open_inputs(counter)
    section9_msbar_literature_comparator(counter)
    section10_lattice_scheme_comparator(counter)
    section11_verdict(counter)

    counter.summary()

    if counter.failed > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
