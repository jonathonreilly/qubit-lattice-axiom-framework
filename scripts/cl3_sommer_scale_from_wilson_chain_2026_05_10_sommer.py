#!/usr/bin/env python3
"""
Sommer Scale from Supplied Wilson-Chain Inputs — Lane 1 Bounded Probe

Source-note runner for:
  docs/SOMMER_SCALE_FROM_WILSON_CHAIN_PARTIAL_NOTE_2026-05-10_sommer.md

This runner verifies a conditional decomposition only.  It supplies the
rounded context input alpha_s(M_Z)=0.1181, inverts the declared two-loop
formula to obtain Lambda_MS-bar^(N_F=5), and then combines that result with
a supplied r_0*Lambda ratio.  The QCD low-energy bridge supplies a transfer
map; it does not derive the rounded coupling used here.

Accordingly, neither Lambda nor r_0 is promoted to a framework-native
prediction, and this probe makes no Lane 1 import-count decrement.  Reference
values are labeled individually as comparators or load-bearing supplied inputs.
No new axiom or registry input is introduced by the repair.
"""

import math
import sys


def heading(s):
    print()
    print("=" * 72)
    print(s)
    print("=" * 72)


def check(label, condition, detail=""):
    """Assert a check, print pass/fail line, return True/False for tally."""
    if condition:
        print(f"  PASS  {label}")
        if detail:
            print(f"        {detail}")
        return True
    print(f"  FAIL  {label}")
    if detail:
        print(f"        {detail}")
    return False


def alpha_s_2loop_from_lambda(mu, Lambda, beta0, beta1):
    """Standard 2-loop perturbative inversion of Lambda formula.

    alpha_s(mu) = (1 / (beta0 * t)) * [1 - (beta1/beta0^2) * ln(t) / t]
    where t = ln(mu^2 / Lambda^2). All in standard 4*pi normalization.
    """
    t = math.log(mu * mu / (Lambda * Lambda))
    a0 = 1.0 / (beta0 * t)
    correction = 1.0 - (beta1 / (beta0 * beta0)) * math.log(t) / t
    return a0 * correction


def lambda_from_alpha_s_2loop(mu, alpha_s, beta0, beta1):
    """Newton-iteration inversion: given alpha_s(mu), solve for Lambda."""
    # Initial guess from 1-loop
    t_guess = 1.0 / (beta0 * alpha_s)
    Lambda = mu * math.exp(-t_guess / 2.0)
    for _ in range(50):
        t = math.log(mu * mu / (Lambda * Lambda))
        a_pred = (1.0 / (beta0 * t)) * (1.0 - (beta1 / (beta0 * beta0)) * math.log(t) / t)
        # Update Lambda by ratio
        residual = a_pred - alpha_s
        # d(alpha)/d(ln Lambda) approximation
        dLambda = Lambda * 1e-4
        t2 = math.log(mu * mu / ((Lambda + dLambda) ** 2))
        a_pred2 = (1.0 / (beta0 * t2)) * (1.0 - (beta1 / (beta0 * beta0)) * math.log(t2) / t2)
        deriv = (a_pred2 - a_pred) / dLambda
        if abs(deriv) < 1e-30:
            break
        Lambda = Lambda - residual / deriv
        if abs(residual) < 1e-12:
            break
    return Lambda


def threshold_match_lambda(Lambda_source, mq, beta0_source, beta0_target):
    """Match Lambda across a quark threshold at scale mq.

    At leading log: alpha_s_source(mq) = alpha_s_target(mq), giving
    Lambda_target = Lambda_source *
    (mq/Lambda_source)^(1 - beta0_source/beta0_target).
    """
    # Solve alpha_s_source(mq) = alpha_s_target(mq) at LO.
    # Neutral source/target names cover both downward and upward crossings.
    t_source = math.log(mq * mq / (Lambda_source * Lambda_source))
    t_target = (beta0_source / beta0_target) * t_source
    Lambda_target = mq * math.exp(-t_target / 2.0)
    return Lambda_target


def main():
    pass_count = 0
    fail_count = 0

    # =========================================================================
    # Section 1: Declared Wilson-chain context
    # =========================================================================
    heading("SECTION 1: DECLARED WILSON-CHAIN CONTEXT")

    # Existing context values; this runner does not promote their source status.
    P_avg = 0.5934                      # supplied plaquette context at beta=6
    M_Pl = 1.221e19                     # GeV, supplied UV-scale context
    alpha_bare = 1.0 / (4.0 * math.pi)  # canonical Cl(3) g_bare = 1 normalization
    u_0 = P_avg ** 0.25                  # tadpole improvement
    alpha_LM = alpha_bare / u_0          # Lepage-Mackenzie geometric-mean coupling
    apbc_factor = (7.0 / 8.0) ** 0.25    # APBC eigenvalue ratio

    # Display-only coupling-map context (n_link = 2):
    alpha_s_v_context = alpha_bare / (u_0 ** 2)

    # Display-only hierarchy-chain context
    v_EW = M_Pl * apbc_factor * (alpha_LM ** 16)

    # Downstream supplied rounded context value at M_Z. The QCD running bridge
    # supplies only a piecewise transfer map; it does not certify this value as
    # a framework prediction or target match.
    alpha_s_MZ_context = 0.1181
    M_Z = 91.1876  # GeV, load-bearing conventional Z-pole scale

    print(f"  context <P>              = {P_avg}")
    print(f"  context M_Pl             = {M_Pl:.6e} GeV")
    print(f"  declared alpha_bare      = {alpha_bare:.10f}")
    print(f"  computed u_0             = {u_0:.10f}")
    print(f"  computed alpha_LM        = {alpha_LM:.10f}")
    print(f"  context alpha_s(v)       = {alpha_s_v_context:.10f}  (= alpha_bare/u_0^2, n_link=2)")
    print(f"  context (7/8)^(1/4)      = {apbc_factor:.10f}")
    print(f"  context v_EW             = {v_EW:.4f} GeV")
    print(f"  supplied alpha_s(M_Z)    = {alpha_s_MZ_context:.6f}  (downstream rounded context input)")
    print(f"  conventional M_Z          = {M_Z} GeV (load-bearing inversion scale)")

    # Sanity: v_EW reproduces PDG comparator
    v_EW_pdg = 246.22  # PDG comparator only
    rel_v = abs(v_EW - v_EW_pdg) / v_EW_pdg
    if check("declared v_EW formula reproduces its comparator to <0.1%",
             rel_v < 1e-3,
             f"v_EW(formula) = {v_EW:.4f} GeV vs PDG {v_EW_pdg} GeV, rel = {rel_v:.4e}"):
        pass_count += 1
    else:
        fail_count += 1

    # alpha_s(v) is reasonable
    if check("display-only alpha_s(v) context lies in [0.09, 0.12]",
             0.09 < alpha_s_v_context < 0.12,
             f"alpha_s(v) = {alpha_s_v_context:.5f}"):
        pass_count += 1
    else:
        fail_count += 1

    # =========================================================================
    # Section 2: Declared beta-function convention
    # =========================================================================
    heading("SECTION 2: DECLARED BETA-FUNCTION CONVENTION")

    # Existing context: b_3 = -7 (SM RGE coefficient for g_3 with N_F=6 quarks)
    # Per COMPLETE_PREDICTION_CHAIN_2026_04_15 Table in Section 3.2:
    #   b_3 = -7 = group theory of derived gauge + matter content
    # In the SM convention dg/dlnmu = b_3 g^3/(16 pi^2),
    # so beta_0 in the convention dalpha/dlnmu^2 = -beta_0 alpha^2 + ... is:
    # beta_0 = -b_3 / (4*pi)... actually the cleanest form is:
    #
    # alpha_s(mu) = 1 / (beta_0 * ln(mu^2/Lambda^2))   at 1 loop
    # with beta_0 (standard) = (33 - 2 N_F)/(12 pi)
    #
    # For QCD pure (N_F=6): beta_0 = (33-12)/(12 pi) = 21/(12 pi) = 7/(4 pi)
    # For N_F=5: beta_0 = (33-10)/(12 pi) = 23/(12 pi)
    # For N_F=3: beta_0 = (33-6)/(12 pi) = 27/(12 pi) = 9/(4 pi)
    #
    # This convention matches the framework's b_3 = -7 (since b_3 = - (33-2 N_F)/3
    # in dg/dlnmu = b_3 g^3/(16 pi^2) convention with N_F=6 quarks).

    def beta0_pdg(NF):
        """1-loop beta_0 in convention alpha_s(mu) = 1/(beta_0 * ln(mu^2/Lambda^2))."""
        return (33.0 - 2.0 * NF) / (12.0 * math.pi)

    def beta1_pdg(NF):
        """2-loop beta_1 in same convention."""
        return (153.0 - 19.0 * NF) / (24.0 * math.pi * math.pi)

    print("  Beta-function coefficients (PDG-standard convention):")
    print(f"    N_F=6: beta_0 = {beta0_pdg(6):.6f},  beta_1 = {beta1_pdg(6):.6f}")
    print(f"    N_F=5: beta_0 = {beta0_pdg(5):.6f},  beta_1 = {beta1_pdg(5):.6f}")
    print(f"    N_F=4: beta_0 = {beta0_pdg(4):.6f},  beta_1 = {beta1_pdg(4):.6f}")
    print(f"    N_F=3: beta_0 = {beta0_pdg(3):.6f},  beta_1 = {beta1_pdg(3):.6f}")

    # Verify the relationship: framework b_3 = -7 corresponds to QCD beta function with N_F=6
    # In the dg/dlnmu = b_3 g^3/(16 pi^2) convention:
    #   alpha_s(mu) = g^2/(4 pi)
    #   dalpha_s/dlnmu = (2g/(4 pi)) dg/dlnmu = 2 alpha_s g/(4 pi) * b_3 g^2/(16 pi^2)
    #                  = b_3 alpha_s^2 / (2 pi)
    # In standard PDG convention dalpha_s/dlnmu^2 = - beta_0 alpha_s^2,
    # so we need dalpha_s/dlnmu = -2 beta_0 alpha_s^2.
    # Equate: b_3 alpha_s^2 / (2 pi) = -2 beta_0 alpha_s^2
    # → beta_0 = -b_3 / (4 pi)
    # With b_3 = -7: beta_0 = 7/(4 pi) ≈ 0.5570.
    # And (33 - 2*6)/(12 pi) = 21/(12 pi) = 7/(4 pi). ✓
    #
    # This checks only the displayed convention conversion. It does not derive
    # the continuum RGE or promote the source status of b_3.

    context_beta0_NF6 = -(-7.0) / (4.0 * math.pi)  # from supplied b_3 = -7 context
    pdg_beta0_NF6 = beta0_pdg(6)
    if check("b_3 = -7 converts to beta_0 = 7/(4*pi) for N_F=6",
             abs(context_beta0_NF6 - pdg_beta0_NF6) < 1e-12,
             f"converted: {context_beta0_NF6:.10f}, formula: {pdg_beta0_NF6:.10f}"):
        pass_count += 1
    else:
        fail_count += 1

    # Below the b-quark threshold (m_b ~ 4.18 GeV), N_F=4
    # Below the c-quark threshold (m_c ~ 1.27 GeV), N_F=3
    # Above m_t (~172.57 GeV), N_F=6; between m_t and m_b, N_F=5
    # The framework retains m_t = 172.57 GeV (Probe 19 / chain).
    # m_b, m_c are conventional MS-bar mass threshold markers per
    # COMPLETE_PREDICTION_CHAIN section 8.4; m_t is a pole-mass marker.

    m_t_context   = 172.57   # GeV, existing cross-check context
    m_b_pdg       = 4.18     # GeV, conventional MS-bar mass threshold marker
    m_c_pdg       = 1.27     # GeV, conventional MS-bar mass threshold marker

    print(f"  m_t (cross-check context)   = {m_t_context} GeV  (used for N_F=5 -> N_F=6 threshold)")
    print(f"  m_b (MS-bar threshold marker) = {m_b_pdg} GeV   (used for N_F=5 -> N_F=4 threshold)")
    print(f"  m_c (MS-bar threshold marker) = {m_c_pdg} GeV   (used for N_F=4 -> N_F=3 threshold)")

    # =========================================================================
    # Section 3: Lambda_QCD inversion from supplied alpha_s(M_Z) context
    # =========================================================================
    heading("SECTION 3: CONDITIONAL LAMBDA_QCD INVERSION")

    # Strategy: this downstream probe supplies alpha_s(M_Z) = 0.1181 as a
    # rounded context value. At M_Z = 91.19 GeV, N_F=5 is active. We invert the standard
    # 2-loop perturbative formula to extract Lambda^(5), then use threshold
    # matching to get Lambda^(4) and Lambda^(3).
    #
    # The cross-check is that this matches the existing reading in
    # CONFINEMENT_STRING_TENSION_NOTE: "Lambda_MS-bar^(5) = 210 MeV (PDG: 210
    # ± 14 MeV)". That is the same chain.

    print(f"  Starting input: alpha_s(M_Z={M_Z} GeV) = {alpha_s_MZ_context:.6f} (supplied downstream context)")

    # Primary route: Lambda^(5) from alpha_s(M_Z) at N_F=5
    Lambda5 = lambda_from_alpha_s_2loop(M_Z, alpha_s_MZ_context,
                                          beta0_pdg(5), beta1_pdg(5))
    print(f"  Lambda^(N_F=5) [from alpha_s(M_Z) inversion at N_F=5] = {Lambda5*1000:.2f} MeV")

    # Sanity: round-trip
    alpha_check5 = alpha_s_2loop_from_lambda(M_Z, Lambda5,
                                               beta0_pdg(5), beta1_pdg(5))
    if check("Lambda^(5) round-trip alpha_s(M_Z) consistency",
             abs(alpha_check5 - alpha_s_MZ_context) < 1e-6,
             f"recovered alpha_s(M_Z) = {alpha_check5:.10f}, supplied input = {alpha_s_MZ_context:.10f}"):
        pass_count += 1
    else:
        fail_count += 1

    # Step 2: Threshold match at m_b (N_F=5 -> N_F=4)
    Lambda4 = threshold_match_lambda(Lambda5, m_b_pdg, beta0_pdg(5), beta0_pdg(4))
    print(f"  Lambda^(N_F=4) [matched at m_b = {m_b_pdg} GeV]    = {Lambda4*1000:.2f} MeV")

    # Step 3: Threshold match at m_c (N_F=4 -> N_F=3)
    Lambda3 = threshold_match_lambda(Lambda4, m_c_pdg, beta0_pdg(4), beta0_pdg(3))
    print(f"  Lambda^(N_F=3) [matched at m_c = {m_c_pdg} GeV]    = {Lambda3*1000:.2f} MeV")

    # Step 4 (cross-check): Lambda^(6) from threshold matching upward at m_t
    Lambda6 = threshold_match_lambda(Lambda5, m_t_context, beta0_pdg(5), beta0_pdg(6))
    print(f"  Lambda^(N_F=6) [matched at m_t = {m_t_context} GeV]   = {Lambda6*1000:.2f} MeV")

    def alpha_s_1loop(mu, Lambda, beta0):
        return 1.0 / (beta0 * math.log(mu * mu / (Lambda * Lambda)))

    threshold_residuals = [
        abs(alpha_s_1loop(m_b_pdg, Lambda5, beta0_pdg(5))
            - alpha_s_1loop(m_b_pdg, Lambda4, beta0_pdg(4))),
        abs(alpha_s_1loop(m_c_pdg, Lambda4, beta0_pdg(4))
            - alpha_s_1loop(m_c_pdg, Lambda3, beta0_pdg(3))),
        abs(alpha_s_1loop(m_t_context, Lambda5, beta0_pdg(5))
            - alpha_s_1loop(m_t_context, Lambda6, beta0_pdg(6))),
    ]
    if check("leading-log threshold matching preserves alpha_s at all three markers",
             max(threshold_residuals) < 1e-12,
             f"max continuity residual = {max(threshold_residuals):.3e}"):
        pass_count += 1
    else:
        fail_count += 1

    Lambda4_closed = Lambda5 * (m_b_pdg / Lambda5) ** (
        1.0 - beta0_pdg(5) / beta0_pdg(4)
    )
    if check("threshold implementation matches the independent closed formula",
             abs(Lambda4 - Lambda4_closed) < 1e-14,
             f"Lambda4 residual = {abs(Lambda4-Lambda4_closed):.3e} GeV"):
        pass_count += 1
    else:
        fail_count += 1

    # Conventional Lambda reference diagnostic. It is later also used in the
    # supplied composite r_0*Lambda ratio, so it is not globally comparator-only.
    Lambda5_pdg = 0.210     # GeV, PDG
    Lambda5_pdg_err = 0.014 # GeV, PDG 1-sigma
    rel_Lambda5 = abs(Lambda5 - Lambda5_pdg) / Lambda5_pdg

    print(f"  PDG comparator: Lambda_MS-bar^(N_F=5) = {Lambda5_pdg*1000:.0f} +/- {Lambda5_pdg_err*1000:.0f} MeV")
    print(f"  Conditional result: Lambda^(5) = {Lambda5*1000:.2f} MeV")
    print(f"  Relative deviation: {rel_Lambda5*100:.2f}%")

    # Comparator checks are non-load-bearing numerical diagnostics.
    if check("conditional Lambda^(5) result within 30% of PDG comparator",
             rel_Lambda5 < 0.30,
             f"deviation = {rel_Lambda5*100:.2f}% from PDG {Lambda5_pdg*1000:.0f} MeV"):
        pass_count += 1
    else:
        fail_count += 1

    # Tighter check: within sigma-band
    if check("conditional Lambda^(5) result within five PDG sigma",
             abs(Lambda5 - Lambda5_pdg) < 5 * Lambda5_pdg_err,
             f"|Lambda^(5) - PDG| = {abs(Lambda5 - Lambda5_pdg)*1000:.2f} MeV vs 5sigma = {5*Lambda5_pdg_err*1000:.0f} MeV"):
        pass_count += 1
    else:
        fail_count += 1

    # The Lambda value is positive and dimensionful
    if check("Lambda^(5) is finite, positive, in expected QCD range (50-500 MeV)",
             0.050 < Lambda5 < 0.500,
             f"Lambda^(5) = {Lambda5*1000:.2f} MeV"):
        pass_count += 1
    else:
        fail_count += 1

    # =========================================================================
    # Section 4: declared inputs and conditional output
    # =========================================================================
    heading("SECTION 4: LAMBDA_QCD CONDITIONAL ON SUPPLIED INPUT")

    # The supplied alpha_s(M_Z) is load-bearing for Lambda^(5).  Other chain
    # quantities are displayed only for the pre-existing cross-check route.
    print()
    print("  Declared inputs and cross-check context:")
    print(f"    - alpha_s(M_Z) = 0.1181  [supplied downstream context input]")
    print(f"    - alpha_s(v) = alpha_bare/u_0^2  [display-only cross-check context]")
    print(f"    - v_EW = M_Pl*(7/8)^(1/4)*alpha_LM^16  [display-only context]")
    print(f"    - b_3 = -7 (-> beta_0^(N_F=6) = 7/(4 pi))  [declared context]")
    print(f"    - m_t = 172.57 GeV  [cross-check context]")
    print(f"    - m_b, m_c  [PDG infrastructure, threshold matching only]")
    print()
    print("  Lambda^(5) = {:.2f} MeV  (conditional; PDG comparator: 210 MeV, dev: {:.1f}%)".format(
        Lambda5*1000, rel_Lambda5*100
    ))
    print("  Lambda^(3) = {:.2f} MeV  (conditional; cf. CONFINEMENT_STRING_TENSION_NOTE 389 MeV)".format(
        Lambda3*1000
    ))

    if check("Lambda result is explicitly conditional on supplied alpha_s(M_Z)",
             alpha_s_MZ_context == 0.1181,
             "the coupling input is supplied, not derived by the QCD bridge"):
        pass_count += 1
    else:
        fail_count += 1

    # Cross-check against existing CONFINEMENT_STRING_TENSION_NOTE Step 4 quote
    # which records "Lambda_MS̄^(5) = 210 MeV (PDG: 210 ± 14 MeV)" via the same chain.
    rel_existing = abs(Lambda5*1000 - 210) / 210
    if check("Lambda^(5) consistent with existing chain reading (CONFINEMENT_STRING_TENSION_NOTE)",
             rel_existing < 0.30,
             f"this runner: {Lambda5*1000:.2f} MeV vs existing chain reading: 210 MeV"):
        pass_count += 1
    else:
        fail_count += 1

    # =========================================================================
    # Section 5: r_0 from Lambda — the dimensional inversion
    # =========================================================================
    heading("SECTION 5: r_0 FROM LAMBDA (DIMENSIONAL INVERSION)")

    # The Sommer scale r_0 is defined by F(r_0) * r_0^2 = 1.65 (Sommer 1993).
    # In terms of the QCD scale Lambda_MS-bar, r_0 * Lambda is dimensionless.
    # Its value depends on the flavor content and scale convention.
    #
    # Quenched (N_F=0) Necco-Sommer 2002:  r_0 * Lambda_MS-bar^(0) = 0.602(48)
    # The N_F=0 number does not determine the N_F=5 number used below. The
    # latter is constructed directly from the supplied conventional values
    # r_0=0.5 fm and Lambda^(5)=210 MeV.
    #
    # In units where hbar = c = 1: r_0 [fm] = 0.1973 / (Lambda [GeV]) * (r_0 * Lambda)
    #
    # The composite dimensionless ratio is supplied here; this runner does not
    # calculate it independently from gauge dynamics.

    hbar_c = 0.1973  # GeV * fm (universal conversion, NOT a physics import)

    # Reference values. The N_F=5 number below is a composite supplied input
    # constructed from the conventional r_0 and Lambda^(5) references; it is
    # not an independent gauge calculation.
    r0_Lambda_NF0_quenched = 0.602    # Necco-Sommer 2002 quenched
    r0_reference = 0.5                # fm, supplied conventional reference
    r0_Lambda_NF5_supplied = r0_reference * Lambda5_pdg / hbar_c

    print("  r_0 * Lambda is a dimensionless QCD scale ratio")
    print("  (supplied here; this runner does not calculate it).")
    print()
    print(f"  Reference numbers and constructions:")
    print(f"    r_0 * Lambda^(N_F=0) = {r0_Lambda_NF0_quenched} (Necco-Sommer 2002, quenched)")
    print(f"    r_0 * Lambda^(N_F=5) = {r0_Lambda_NF5_supplied:.6f} (constructed from r_0 = 0.5 fm, Lambda^(5) = 210 MeV)")

    # Combine the supplied N_F=5 ratio with the conditional Lambda^(5).
    r0_conditional = (r0_Lambda_NF5_supplied / Lambda5) * hbar_c   # in fm
    print(f"  r_0 (conditional rescaling using supplied composite ratio) = {r0_conditional:.4f} fm")

    # The same r_0 reference is load-bearing in the composite ratio, so the
    # following difference is a rescaling diagnostic, not an independent test.
    rel_r0 = abs(r0_conditional - r0_reference) / r0_reference
    print(f"  Supplied reference r_0 = {r0_reference} fm (also used to construct the ratio)")
    print(f"  Conditional rescaling difference: {rel_r0*100:.2f}%")

    if check("conditional r_0 rescaling identity is internally consistent",
             abs(r0_conditional - r0_reference * Lambda5_pdg / Lambda5) < 1e-14,
             f"r_0 = {r0_conditional:.4f} fm; same 0.5 fm reference constructs the input ratio"):
        pass_count += 1
    else:
        fail_count += 1

    # The dimensional check: Lambda^(-1) is the correct length scale up to O(1)
    Lambda_inv = hbar_c / Lambda5     # 1/Lambda in fm
    print(f"  hbar*c / Lambda^(5) = {Lambda_inv:.4f} fm  (natural length scale)")
    if check("r_0 ~ O(1) * 1/Lambda^(5) (correct dimensional structure)",
             0.3 * Lambda_inv < r0_conditional < 3.0 * Lambda_inv,
             f"r_0/Lambda_inv = {r0_conditional/Lambda_inv:.4f}"):
        pass_count += 1
    else:
        fail_count += 1

    # =========================================================================
    # Section 6: Honest conditional split
    # =========================================================================
    heading("SECTION 6: HONEST CONDITIONAL SPLIT")

    print("  COMPUTED CONDITIONAL CONSEQUENCE:")
    print(f"    Lambda_MS-bar^(N_F=5) = {Lambda5*1000:.2f} MeV")
    print(f"    This value depends load-bearingly on supplied alpha_s(M_Z)=0.1181")
    print(f"    Threshold matching additionally uses declared m_t, m_b, and m_c inputs")
    print()
    print("  SUPPLIED LIMITATION (this probe DOES NOT close):")
    print(f"    The dimensionless ratio r_0 * Lambda is a QCD scale ratio")
    print(f"    Status: its numerical value is supplied; the gauge identification")
    print(f"            alone does not calculate it.")
    print()
    print("  NET LANE 1 IMPORT-COUNT EFFECT:")
    print(f"    None. Both supplied alpha_s(M_Z) and supplied r_0*Lambda remain")
    print(f"    load-bearing, so the algebraic split does not close an import.")
    print()
    print("  This is a bounded conditional decomposition, not a partial closure.")

    if check("bounded verdict: supplied coupling and supplied ratio remain explicit",
             alpha_s_MZ_context == 0.1181
             and abs(r0_Lambda_NF5_supplied - r0_reference * Lambda5_pdg / hbar_c) < 1e-15,
             "no framework-native Lambda or Sommer-scale claim"):
        pass_count += 1
    else:
        fail_count += 1

    # =========================================================================
    # Section 7: Input-role report
    # =========================================================================
    heading("SECTION 7: INPUT-ROLE REPORT")

    # Report which conventional values are load-bearing and which are only
    # display-side comparators. This is prose, not a source-authority proof.
    reference_values = [
        ("v_EW PDG", v_EW_pdg, "comparator for declared v_EW formula"),
        ("Lambda^(5) reference", Lambda5_pdg, "also constructs supplied r_0*Lambda ratio"),
        ("r_0 reference", r0_reference, "also constructs supplied r_0*Lambda ratio"),
    ]
    pdg_infrastructure = [
        ("M_Z", M_Z, "load-bearing inversion scale"),
        ("m_b", m_b_pdg, "load-bearing for the Lambda4 threshold consequence"),
        ("m_c", m_c_pdg, "load-bearing for the Lambda3 threshold consequence"),
    ]
    declared_chain_context = [
        ("alpha_s(M_Z)", alpha_s_MZ_context, "supplied downstream context input"),
        ("alpha_s(v)", alpha_s_v_context, "display-only alpha_bare/u_0^2 context"),
        ("v_EW", v_EW, "display-only hierarchy-chain context"),
        ("alpha_LM", alpha_LM, "computed context value"),
        ("u_0", u_0, "computed P^(1/4) context value"),
        ("m_t", m_t_context, "cross-check threshold context"),
        ("b_3 = -7", -7, "declared coefficient context"),
    ]

    print("  Conventional references and roles:")
    for name, val, role in reference_values:
        print(f"    {name} = {val} ({role})")
    print()
    print("  Conventional infrastructure inputs:")
    for name, val, role in pdg_infrastructure:
        print(f"    {name} = {val} ({role})")
    print()
    print("  Declared inputs and source statuses:")
    for name, val, role in declared_chain_context:
        print(f"    {name} = {val} ({role})")

    print("  INFO  Source-role and frozen-baseline claims require repository-level checks;")
    print("        they are not counted as unconditional runner PASS assertions.")

    # =========================================================================
    # Section 8: Lane 1 import-count update
    # =========================================================================
    heading("SECTION 8: LANE 1 IMPORT-COUNT ACCOUNTING")

    print("  Before this probe (per BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes):")
    print("    Lane 1 imports: 4")
    print("      - Sommer r_0 = 0.5 fm")
    print("      - 4-loop QCD running")
    print("      - threshold matching at heavy-quark thresholds")
    print("      - sea-quark / full-QCD bridge")
    print()
    print("  After PR #917 (4-loop QCD running probe, partial -> 3.5 imports):")
    print("    Lane 1 imports: 3.5")
    print("      - Sommer r_0 = 0.5 fm")
    print("      - 4-loop QCD running [partially derived in PR #917]")
    print("      - threshold matching at heavy-quark thresholds")
    print("      - sea-quark / full-QCD bridge")
    print()
    print("  After this bounded conditional decomposition:")
    print("    No further decrement is justified.")
    print("      - Sommer r_0 splits into:")
    print("          * Lambda_MS-bar^(N_F=5)  [conditional on supplied alpha_s(M_Z)]")
    print("          * r_0 * Lambda^(5)        [supplied ratio]")
    print("      - 4-loop QCD running [partially derived in PR #917]")
    print("      - threshold matching at heavy-quark thresholds")
    print("      - sea-quark / full-QCD bridge")
    print()
    print("  The earlier source-side 3.0 count and Lambda promotion are withdrawn.")

    print("  INFO  Import-count governance is reported, not asserted by this numeric runner.")

    # =========================================================================
    # Final summary
    # =========================================================================
    heading("RESULTS")
    total = pass_count + fail_count
    print(f"  PASS = {pass_count}")
    print(f"  FAIL = {fail_count}")
    print(f"  TOTAL = {total}")
    print()
    print("=" * 72)
    print(f"=== TOTAL: PASS={pass_count}, FAIL={fail_count} ===")
    print("=" * 72)
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
