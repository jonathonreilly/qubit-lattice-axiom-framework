#!/usr/bin/env python3
"""Scale-axis hierarchy / gauge dimensional-transmutation scoping runner.

Question (owner-authorized exploration). The framework has exactly ONE
dimensionful primitive: the lattice scale a^{-1} = M_Pl
(`scale_reference_primitive`, docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md). The
lattice gauge couplings are O(1) at that scale (bare convention g_bare = 1,
i.e. g_bare^2 = 1, alpha_bare = g_bare^2/(4 pi) = 1/(4 pi) ~ 0.080, so
1/alpha ~ 11-13). Does a framework MARGINAL coupling run from M_Pl and
generate a hierarchically small scale via canonical dimensional
transmutation

    Lambda = M_UV * exp( -2 pi / (b0 * alpha(M_UV)) )                    (DT)

NATURALLY -- an O(1) UV coupling exponentially suppressed to ~10^-17, with
NO tuned relevant parameter? If so this is a genuine derivation of the
hierarchy (a log effect), not a relocation.

HONEST HEADLINE (computed below). With the framework's OWN O(1) coupling
(1/alpha ~ 11), the b3=7 transmutation pole sits at ~10^14-10^15 GeV --
only ~4 orders below M_Pl, NOT ~17. Landing at Lambda_QCD ~ 200 MeV (17
orders) needs 1/alpha(M_Pl) ~ 51; landing at v ~ 246 GeV (16.7 orders)
needs 1/alpha(M_Pl) ~ 43. The physical SM alpha_s run UP from M_Z gives
exactly 1/alpha_s(M_Pl) ~ 52 -- i.e. real QCD transmutes because its
Planck-scale coupling is WEAK (1/alpha~50), whereas the framework's is
~5x STRONGER (1/alpha~11). So: the framework's coupling IS genuinely O(1)
(no tuning to 10^-17), and the MECHANISM (marginal log running, no
relevant operator) structurally avoids the hierarchy problem -- but the
framework's specific O(1) value does NOT, via naive Planck-scale gauge
transmutation, land at either Lambda_QCD or v. The framework's actual
landed Lambda_QCD = 227 MeV comes from a SEPARATE tadpole/CMT chain
(Sommer note), not from this naive (DT) at 1/alpha=11.

This runner introduces NO new axiom, selector, or PDG fit input. It
substitutes the framework's OWN derived 1-loop beta coefficients

    b_3   = (11 N_color - 2 N_quark)/3          = 7     (SU(3)_c, full SM)
    b_3pg = (11 N_color)/3                       = 11    (SU(3)_c, pure gauge)
    b_2   = (11 N_pair - N_color(N_color+1))/3 - 1/6 = 19/6 (SU(2)_L)
    b_QED = (2/3)(N_color + 1)^2                  = 32/3  (U(1)_em catalog form)

  (sources: QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02,
   SU2_WEAK_BETA_COEFFICIENT_*_NOTE, all citing the Peskin-Schroeder
   SU(N) 1-loop formula as a named external admission)

into (DT) with the framework's O(1) UV coupling. All PDG numbers
(Lambda_QCD, v_EW, alpha_s, M_Z) appear ONLY as post-hoc comparators,
never as derivation inputs. Inputs: M_Pl, the framework b0's, the O(1)
coupling.
"""

import math

# ----------------------------------------------------------------------
# Section 0: framework primitives (the ONLY dimensionful / coupling inputs)
# ----------------------------------------------------------------------
M_PL = 1.221e19  # GeV. Scale-reference primitive a^{-1} = M_Pl. NOT derived;
                 # the framework's single dimensionful ruler.

# Framework lattice bare gauge coupling: g_bare = 1 (admitted Wilson
# canonical convention, G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE).
# O(1) -- the central point. alpha_bare = g_bare^2 / (4 pi).
G_BARE_SQ = 1.0
ALPHA_BARE = G_BARE_SQ / (4.0 * math.pi)   # = 1/(4 pi) ~ 0.07958

# Tadpole-improved Planck-scale coupling used by the framework's QCD chain
# (alpha_LM = alpha_bare / u_0, u_0 = <P>^(1/4), <P> = 0.5934).
PLAQUETTE = 0.5934
U0 = PLAQUETTE ** 0.25
ALPHA_LM = ALPHA_BARE / U0                  # ~ 0.0907 (1/alpha ~ 11)

# ----------------------------------------------------------------------
# Section 1: framework-derived 1-loop beta coefficients (PDG convention,
# b0 > 0 <-> asymptotic freedom). Substituted, not introduced.
# ----------------------------------------------------------------------
N_COLOR = 3
N_PAIR = 2          # = C_2(adj SU(2))
N_GEN = 3
N_QUARK_SM = N_GEN * N_PAIR     # = 6 Dirac quark flavors

b3_full = (11 * N_COLOR - 2 * N_QUARK_SM) / 3.0     # = 7
b3_puregauge = (11 * N_COLOR) / 3.0                  # = 11
b2_su2 = (11 * N_PAIR - N_COLOR * (N_COLOR + 1)) / 3.0 - 1.0 / 6.0   # = 19/6
b_qed = (2.0 / 3.0) * (N_COLOR + 1) ** 2             # = 32/3 (catalog form)

# Transmutation (PDG b0>0 convention). AF running:
#   1/alpha(Q) = 1/alpha(M_UV) + (b/2pi) ln(Q/M_UV),  b>0
# IR pole (1/alpha = 0) at:
#   Lambda = M_UV * exp( - 2 pi / (b * alpha(M_UV)) )                   (DT)


def transmutation_scale(M_uv, b0, alpha_uv):
    exponent = -2.0 * math.pi / (b0 * alpha_uv)
    Lambda = M_uv * math.exp(exponent)
    log10_ratio = exponent / math.log(10.0)
    regime = ("asymptotically free -> IR dynamical scale" if b0 > 0
              else "IR-free (UV Landau pole) -> NO IR scale generated")
    return Lambda, log10_ratio, regime


def inv_alpha_to_reach(M_uv, b0, target):
    """1/alpha(M_uv) required so the (DT) pole lands exactly at `target`."""
    L = math.log(target / M_uv)            # negative
    alpha = -2.0 * math.pi / (b0 * L)
    return 1.0 / alpha


def fmt_scale(Lambda):
    if Lambda >= 1.0:
        return f"{Lambda:.4g} GeV"
    return f"{Lambda * 1e3:.4g} MeV"


# ----------------------------------------------------------------------
# Section 2: comparators (POST-HOC ONLY, never derivation inputs)
# ----------------------------------------------------------------------
V_EW = 246.22            # GeV, PDG Higgs VEV (comparator)
LAMBDA_QCD5_PDG = 0.210  # GeV, PDG Lambda_MS-bar^(5) (comparator)
LAMBDA_QCD5_FRAMEWORK = 0.22751  # GeV, framework Sommer-note chain (comparator)
M_Z = 91.1876            # GeV (comparator)
ALPHA_S_MZ = 0.1181      # comparator (also a framework prediction elsewhere)


def banner(title):
    print("=" * 72)
    print(title)
    print("=" * 72)


def main():
    banner("SECTION 0: FRAMEWORK PRIMITIVES (only inputs)")
    print(f"  M_Pl (scale-reference primitive a^-1)   = {M_PL:.4g} GeV")
    print(f"  g_bare^2 (lattice bare, O(1))            = {G_BARE_SQ:.4f}")
    print(f"  alpha_bare = g_bare^2/(4 pi)             = {ALPHA_BARE:.6f}  (1/alpha = {1/ALPHA_BARE:.2f})")
    print(f"  alpha_LM   = alpha_bare/u_0  (u_0={U0:.5f})  = {ALPHA_LM:.6f}  (1/alpha = {1/ALPHA_LM:.2f})")
    print(f"  target depth log10(M_Pl/v_EW)            = {math.log10(M_PL/V_EW):.3f}")
    print(f"  target depth log10(M_Pl/Lambda_QCD)      = {math.log10(M_PL/LAMBDA_QCD5_PDG):.3f}")

    banner("SECTION 1: FRAMEWORK-DERIVED 1-LOOP BETA COEFFICIENTS")
    print(f"  b_3 (SU(3)_c, full SM, N_quark=6)  = {b3_full:.6f}   [= 7]")
    print(f"  b_3 (SU(3)_c, pure gauge)          = {b3_puregauge:.6f}   [= 11]")
    print(f"  b_2 (SU(2)_L)                      = {b2_su2:.6f}   [= 19/6 = 3.1667]")
    print(f"  b_QED (U(1)_em catalog)            = {b_qed:.6f}   [= 32/3 = 10.667]")
    print("  (only SU(3)_c is physically asymptotically free; b_2, b_QED")
    print("   catalog signs are convention/sector artifacts and are shown")
    print("   only to scan the transmutation map, not as physical AF claims.)")

    banner("SECTION 2: GAUGE TRANSMUTATION FROM M_Pl, FRAMEWORK O(1) COUPLING")
    print("  Lambda = M_Pl * exp( -2 pi / (b0 * alpha(M_Pl)) )\n")
    channels = [
        ("SU(3)_c full SM   b3=7",    b3_full,      ALPHA_LM,   "alpha_LM"),
        ("SU(3)_c full SM   b3=7",    b3_full,      ALPHA_BARE, "alpha_bare"),
        ("SU(3)_c pure gauge b3=11",  b3_puregauge, ALPHA_LM,   "alpha_LM"),
        ("SU(2)_L           b2=19/6", b2_su2,       ALPHA_BARE, "alpha_bare"),
        ("U(1)_em catalog   b=32/3",  b_qed,        ALPHA_BARE, "alpha_bare"),
    ]
    results = {}
    for name, b0, a_uv, a_name in channels:
        Lam, lg, regime = transmutation_scale(M_PL, b0, a_uv)
        results[(name, a_name)] = (Lam, lg)
        print(f"  {name:28s} alpha_UV={a_name}={a_uv:.5f}")
        print(f"      exponent -2pi/(b0 a) = {-2*math.pi/(b0*a_uv):.3f}")
        print(f"      Lambda = {fmt_scale(Lam):>16s}   log10(Lambda/M_Pl) = {lg:.2f}")
        print()
    lam_qcd_lm = results[("SU(3)_c full SM   b3=7", "alpha_LM")][0]

    banner("SECTION 3: WHAT UV COUPLING WOULD REACH Lambda_QCD / v? (the honest gap)")
    for tgt_name, tgt in [("Lambda_QCD=210MeV", LAMBDA_QCD5_PDG), ("v_EW=246GeV", V_EW)]:
        need_b3 = inv_alpha_to_reach(M_PL, b3_full, tgt)
        print(f"  target {tgt_name}: with b3=7 need 1/alpha(M_Pl) = {need_b3:.2f}  (alpha = {1/need_b3:.5f})")
    inv_su2_v = inv_alpha_to_reach(M_PL, b2_su2, V_EW)
    print(f"  target v_EW with b2=19/6:  need 1/alpha(M_Pl) = {inv_su2_v:.2f}")
    print()
    print(f"  framework HAS: 1/alpha_LM = {1/ALPHA_LM:.2f},  1/alpha_bare = {1/ALPHA_BARE:.2f}")
    # physical SM benchmark: run alpha_s UP from M_Z to M_Pl with b3=7.
    inv_sm_MPl = 1.0/ALPHA_S_MZ + (b3_full/(2*math.pi))*math.log(M_PL/M_Z)
    print(f"  physical SM check: alpha_s(M_Z)={ALPHA_S_MZ} run UP to M_Pl (b3=7)")
    print(f"      -> 1/alpha_s(M_Pl) = {inv_sm_MPl:.2f}  (alpha = {1/inv_sm_MPl:.5f})")
    print("  => real QCD transmutes 17 orders because its Planck coupling is WEAK")
    print(f"     (1/alpha~52); framework's is ~5x STRONGER (1/alpha~11), so naive")
    print("     (DT) from M_Pl stops ~4 orders down, not 17.")

    banner("SECTION 4: FRAMEWORK'S ACTUAL Lambda_QCD ROUTE (for contrast)")
    print(f"  framework Sommer-chain Lambda^(5)  = {LAMBDA_QCD5_FRAMEWORK*1e3:.1f} MeV (comparator)")
    print(f"  PDG Lambda_MS-bar^(5)              = {LAMBDA_QCD5_PDG*1e3:.0f} MeV (comparator, dev 8.3%)")
    print("  HOW the framework gets 227 MeV: NOT naive (DT) at 1/alpha=11. It")
    print("  starts from alpha_s(v)=0.1033 (tadpole/CMT: alpha_bare/u_0^2) and a")
    print("  hierarchy-formula v, then runs DOWN with 2-loop SM RGE + quark")
    print("  thresholds. The effective coupling at v is what makes Lambda land;")
    print("  the Planck-scale coupling 1/alpha~11 is NOT directly transmuted.")

    banner("SECTION 5: HIERARCHY-PROBLEM STRUCTURE (relevant vs marginal)")
    print("  SM hierarchy problem: m_H^2 is a RELEVANT operator (dim 2),")
    print("  additively renormalized, delta m_H^2 ~ Lambda_UV^2 => tuned to")
    print("  1 part in (M_Pl/v)^2 ~ 10^33.")
    print()
    print("  Framework: NO fundamental scalar mass term in A1(Z^3)+A2(M2(C))+")
    print("  A3(record). Single dimensionful primitive a^-1=M_Pl (a ruler, zero")
    print("  dimensionless content). Any dynamically generated scale via (DT) is")
    print("  a MARGINAL/log effect, Lambda/M_UV = exp(-2pi/(b0 alpha)),")
    print("  radiatively STABLE (no additive quadratic sensitivity), like")
    print("  Lambda_QCD. So the framework STRUCTURALLY LACKS the relevant tuned")
    print("  operator that IS the hierarchy problem. This is a genuine structural")
    print("  feature, not wishful: there is simply no m_H^2 counterterm to tune.")
    print()
    print("  BUT 'no quadratic tuning' != 'v is pinned'. Whether the SPECIFIC")
    print("  value v=246 GeV emerges = whether some marginal coupling's pole")
    print("  lands at 246 GeV. Sec 2-3: with the framework's O(1) coupling the")
    print("  gauge poles land at ~10^14-10^16 GeV, not at v or Lambda_QCD. The")
    print("  landed v-route (v = M_Pl (7/8)^(1/4) alpha_LM^16) is a SEPARATE")
    print("  bounded match (HIERARCHY_FORMULA_HONEST_STATUS, closure open):")
    print("  algebraically exp(-c_eff/alpha_LM) with c_eff=16 alpha_LM")
    print("  ln(1/alpha_LM) ~ 3.48, but c_eff is NOT a coupling-independent")
    print("  group-theory rational, so it is NOT a textbook gauge-transmutation")
    print("  constant (HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING is explicit).")

    banner("SECTION 6: VERDICT INPUTS")
    print(f"  - O(1) UV coupling (not tuned to 10^-17)? YES: 1/alpha ~ 11-13.")
    print(f"  - Marginal/log mechanism, radiatively stable? YES (transmutation).")
    print(f"  - Relevant tuned scalar-mass operator present? NO (framework has none).")
    print(f"  - Framework O(1) coupling transmutes ~17 orders to QCD/EW? NO")
    print(f"      (1/alpha~11 gives ~4 orders -> 10^14 GeV; need 1/alpha~43-51).")
    print(f"  - Any gauge pole lands AT v=246 GeV? NO.")
    print(f"  - Framework's actual 227 MeV from naive Planck (DT)? NO (separate chain).")
    print()
    print("  VERDICT: FRAMEWORK-AVOIDS-HIERARCHY-PROBLEM-BUT-SCALE-NOT-PINNED.")
    print("  The framework has the right STRUCTURE for a natural hierarchy (O(1)")
    print("  marginal coupling, log transmutation, no relevant m_H^2 operator to")
    print("  fine-tune) -- it does NOT relocate the hierarchy into a tuned 10^-17")
    print("  coupling. But its specific O(1) value (1/alpha~11) is ~4-5x too")
    print("  STRONG to transmute the ~17 orders to Lambda_QCD or v by naive")
    print("  Planck-scale gauge running; the SPECIFIC scales v and Lambda_QCD are")
    print("  reached only via separate, still-open bounded chains, not pinned by a")
    print("  clean gauge pole. The transmutation order-of-magnitude actually")
    print("  delivered by the framework's own coupling+b3 is ~10^-4 (M_Pl ->")
    print(f"  ~{fmt_scale(lam_qcd_lm)}), short of the needed ~10^-17 by ~13 decades")
    print("  of coupling strength.")

    # --- machine-checkable structural assertions (no fitted values) ---
    assert abs(b3_full - 7.0) < 1e-12
    assert abs(b3_puregauge - 11.0) < 1e-12
    assert abs(b2_su2 - 19.0/6.0) < 1e-12
    assert abs(b_qed - 32.0/3.0) < 1e-12
    assert abs(ALPHA_BARE - 1.0/(4*math.pi)) < 1e-12
    assert 10.0 < 1/ALPHA_LM < 13.0          # genuinely O(1), 1/alpha ~ 11
    # framework O(1) coupling does NOT reach the QCD scale by naive (DT):
    assert lam_qcd_lm > 1e10                  # stops far above QCD scale
    assert math.log10(lam_qcd_lm / M_PL) > -6 # only ~4 orders down, not ~17
    # reaching Lambda_QCD needs a much WEAKER coupling than the framework has:
    need = inv_alpha_to_reach(M_PL, b3_full, LAMBDA_QCD5_PDG)
    assert need > 3.0 * (1/ALPHA_LM)          # ~5x weaker than framework
    # physical SM benchmark must corroborate the required ~1/50:
    assert 45 < inv_sm_MPl < 60
    print("\nALL STRUCTURAL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
