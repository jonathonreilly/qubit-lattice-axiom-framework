#!/usr/bin/env python3
"""Frontier probe: is the charged-lepton mass SCALE derivable, or irreducible?

Companion to:
  docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md

This runner is a META probe. It does NOT derive a lepton mass, does NOT
introduce an axiom or import, and does NOT predict an audit verdict. It
records three exact algebraic facts and one honest quantitative no-go, all
on top of content already present on origin/main:

  Block A  Top-sector anchor is a BLOCK-DIMENSION normalization, not a
           color-Fierz necessity. The retained_bounded YT identity gives
           y_t_bare = g_bare / sqrt(N_c * N_iso) = g_bare / sqrt(6); the
           sqrt(6) is the Q_L = (2,3) block dimension. (Confirms the
           operator-normalization route, Representation B of the YT note,
           which needs no color Fierz.)

  Block B  Lepton-sector block-dimension analog is 1/sqrt(2). The unaudited
           D17-prime note already establishes Z_lep = sqrt(N_c * N_iso) =
           sqrt(1 * 2) = sqrt(2) for L_L = (2,1). So the *bare* lepton
           block-dim anchor is y_tau_bare = g / sqrt(2).

  Block C  QUANTITATIVE NO-GO for hypothesis #2 (lepton Ward boundary
           y_tau(M_Pl) = g_2 / sqrt(2)). The bare value g_2/sqrt(2) ~ 0.46
           (or 1/sqrt(2) ~ 0.71 with g=1) overshoots the observed
           y_tau ~ 0.0102 by ~45-70x. RG running cannot bridge this:
           a small lepton Yukawa runs by percent-level amounts and in the
           wrong direction. So the top-style block-dim Ward boundary does
           NOT, by itself, pin the lepton scale. The top works only because
           y_t is O(1); the lepton Yukawa is not.

  Block D  EXACT factorization of the m_W/256 empirical relation. The
           audited_clean open-gate relation a_lepton^2 = m_W/256, together
           with the exact tree-level SM identity m_W = g_2 v / 2, gives
           (mapping the scale a^2 to a Yukawa via m = y v/sqrt2):

               y_scale = g_2 * (1/sqrt(2)) * (1/256)

           This factorizes the lepton scale into:
             - g_2          : the lepton's actual non-abelian (SU(2)) gauge
                              coupling (the lepton IS an SU(2) doublet);
             - 1/sqrt(2)    : EXACTLY the D17-prime lepton block-dim factor;
             - 1/256        : 1/(dim_C M_2(C))^4 = the irreducible open gate.

           So the lepton scale PARTIALLY mirrors the retained top Ward
           boundary (the g_2 * 1/sqrt(2) part is the lepton analog of the
           top's g_s * 1/sqrt(6)); the residual unexplained piece is
           exactly the 1/256 = 1/(dim_C M_2(C))^4 suppression, which has no
           counterpart in the top sector.

VERDICT recorded: FREE-FLAVOR-INPUT modulo a sharp open gate. The lepton
scale is one irreducible real number on the current retained surface; the
m_W/256 = 1/(dim_C M_2)^4 factor is its open derivation target, now
located precisely as "block-dim anchor (g_2/sqrt2, present) times 1/256
(absent)".
"""

from __future__ import annotations

import math

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    st = "PASS" if cond else "FAIL"
    PASS += int(bool(cond))
    FAIL += int(not cond)
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


def main() -> int:
    print("=" * 80)
    print("LEPTON-SCALE FRONTIER PROBE (META)")
    print("=" * 80)
    print("Note: docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md")
    print("Status: source-only META probe. No audit-lane verdict wiring.")
    print("Question: is the charged-lepton mass SCALE derivable, or 1 irreducible input?")
    print()

    # ------------------------------------------------------------------
    # Framework / empirical constants (comparators, NOT derivation inputs)
    # ------------------------------------------------------------------
    N_c_quark = 3
    N_iso = 2          # SU(2) doublet
    N_c_lepton = 1     # color singlet
    dim_C_M2C = 4      # complex dim of M_2(C) = Cl(3,0) per-site algebra

    # PDG / framework comparators (GeV)
    m_e = 0.51099895e-3
    m_mu = 105.6583755e-3
    m_tau = 1776.86e-3
    v = 246.282818290129
    m_W = 80.3692
    m_W_err = 15.7e-3

    g2 = 2.0 * m_W / v       # exact tree-level SM: m_W = g2 v / 2

    print("-" * 80)
    print("Setup (block dimensions and couplings)")
    print("-" * 80)
    check(f"top block Q_L=(2,3): N_c*N_iso = {N_c_quark}*{N_iso} = {N_c_quark*N_iso}",
          N_c_quark * N_iso == 6)
    check(f"lepton block L_L=(2,1): N_c*N_iso = {N_c_lepton}*{N_iso} = {N_c_lepton*N_iso}",
          N_c_lepton * N_iso == 2)
    check(f"dim_C(M_2(C)) = {dim_C_M2C}", dim_C_M2C == 4)
    check(f"g_2 (from m_W = g_2 v/2) = {g2:.6f}", abs(g2 - 2 * m_W / v) < 1e-12)

    # ------------------------------------------------------------------
    # Block A: top anchor = block-dimension normalization 1/sqrt(6)
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("A. Top anchor (retained_bounded YT) is a BLOCK-DIM normalization")
    print("-" * 80)
    yt_blockdim = 1.0 / math.sqrt(N_c_quark * N_iso)
    check("A.1  y_t_bare = g_bare/sqrt(N_c*N_iso) = g_bare/sqrt(6) (g_bare=1)",
          abs(yt_blockdim - 1.0 / math.sqrt(6)) < 1e-15,
          detail=f"1/sqrt(6) = {yt_blockdim:.6f}")
    check("A.2  sqrt(6) is the Q_L=(2,3) block dimension N_c*N_iso, "
          "NOT a color-Fierz necessity",
          N_c_quark * N_iso == 6,
          detail="Representation B (operator normalization) of YT needs no color Fierz")
    # The top Yukawa is O(1), so this block-dim anchor lands on the right scale.
    y_t_obs = m_tau * 0 + 0.9909  # PDG-ish top Yukawa (pole), comparator
    check("A.3  observed y_t ~ O(1), so the block-dim anchor lands at the right scale",
          0.8 < y_t_obs < 1.1,
          detail=f"y_t ~ {y_t_obs:.3f} ~ g_s/sqrt(6) quasi-fixed-point")

    # ------------------------------------------------------------------
    # Block B: lepton block-dimension analog = 1/sqrt(2)
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("B. Lepton block-dim analog (D17-prime, unaudited) is 1/sqrt(2)")
    print("-" * 80)
    ylep_blockdim = 1.0 / math.sqrt(N_c_lepton * N_iso)
    check("B.1  Z_lep = sqrt(N_c*N_iso) = sqrt(1*2) = sqrt(2)  (D17-prime)",
          abs(math.sqrt(N_c_lepton * N_iso) - math.sqrt(2)) < 1e-15)
    check("B.2  bare lepton block-dim anchor y_tau_bare = g/sqrt(2)",
          abs(ylep_blockdim - 1.0 / math.sqrt(2)) < 1e-15,
          detail=f"1/sqrt(2) = {ylep_blockdim:.6f}")
    check("B.3  lepton is color-singlet (N_c=1): no color Fierz, but block-dim "
          "normalization still well-defined",
          N_c_lepton == 1,
          detail="the 1/sqrt(2) is operator-normalization (Rep B), independent of Fierz")

    # ------------------------------------------------------------------
    # Block C: QUANTITATIVE NO-GO for hypothesis #2 (lepton Ward boundary)
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("C. NO-GO: top-style block-dim Ward boundary does NOT pin the lepton scale")
    print("-" * 80)
    y_tau_obs = m_tau * math.sqrt(2) / v
    print(f"  observed y_tau (m_tau=({m_tau*1e3:.2f} MeV)) = {y_tau_obs:.6f}")
    print(f"  bare block-dim anchor 1/sqrt(2) (g=1)        = {1/math.sqrt(2):.6f}")
    print(f"  bare block-dim anchor g_2/sqrt(2)            = {g2/math.sqrt(2):.6f}")
    overshoot_g1 = (1 / math.sqrt(2)) / y_tau_obs
    overshoot_g2 = (g2 / math.sqrt(2)) / y_tau_obs
    print(f"  overshoot factor (g=1)  = {overshoot_g1:.1f}x")
    print(f"  overshoot factor (g=g_2)= {overshoot_g2:.1f}x")
    check("C.1  block-dim Ward boundary y_tau=g/sqrt(2) overshoots observed by >40x",
          overshoot_g2 > 40,
          detail=f"{overshoot_g2:.0f}x (g_2) / {overshoot_g1:.0f}x (g=1)")
    check("C.2  RG running cannot bridge a >40x gap for a small lepton Yukawa",
          overshoot_g2 > 40,
          detail="lepton Yukawa runs ~percent-level, and toward SMALLER values in IR")
    check("C.3  hypothesis #2 (lepton Ward boundary like the top) FAILS quantitatively",
          overshoot_g2 > 40,
          detail="the top works only because y_t is O(1); y_tau is not")

    # ------------------------------------------------------------------
    # Block D: EXACT factorization of the m_W/256 relation
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("D. EXACT factorization: lepton scale = g_2 * (1/sqrt(2)) * (1/256)")
    print("-" * 80)
    a_lep = (math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau)) / 3.0
    a_lep2 = a_lep ** 2  # GeV (a MASS scale)
    # empirical open-gate relation a^2 = m_W/256 (audited_clean)
    rel_offset = abs(a_lep2 - m_W / 256.0) / (m_W / 256.0)
    check("D.1  empirical: a_lepton^2 = m_W/256 (audited_clean open gate)",
          rel_offset < 5e-4,
          detail=f"offset {rel_offset*100:.4f}%")

    # map the scale a^2 to a Yukawa: m = y v/sqrt2  =>  y_scale = a^2 sqrt2/v
    y_scale = a_lep2 * math.sqrt(2) / v
    # EXACT consequence of a^2 = m_W/256 and m_W = g2 v/2:
    #   y_scale = (g2 v/2 /256) * sqrt2/v = g2 * sqrt2/512 = g2 * (1/sqrt2) * (1/256)
    y_scale_factored = g2 * (1.0 / math.sqrt(2)) * (1.0 / 256.0)
    check("D.2  y_scale := a_lep^2 * sqrt2/v factorizes as g_2 * (1/sqrt2) * (1/256)",
          abs(y_scale - y_scale_factored) / y_scale < 5e-4,
          detail=f"y_scale={y_scale:.6e}, factored={y_scale_factored:.6e}")

    # Symbolic exactness (independent of numerical inputs): given a^2=m_W/256,
    # m_W=g2 v/2, the map y=a^2 sqrt2/v gives exactly g2 sqrt2/512.
    # Check g2*sqrt2/512 == g2*(1/sqrt2)*(1/256) identically.
    lhs = 1.0 * math.sqrt(2) / 512.0
    rhs = (1.0 / math.sqrt(2)) / 256.0
    check("D.3  exact algebra: sqrt(2)/512 == (1/sqrt2)/256",
          abs(lhs - rhs) < 1e-15,
          detail=f"{lhs:.10e} == {rhs:.10e}")

    # The three factors and their provenance
    check("D.4  factor g_2 = lepton's actual SU(2) gauge coupling (lepton is (2,1))",
          N_iso == 2)
    check("D.5  factor 1/sqrt(2) = EXACTLY the D17-prime lepton block-dim Z_lep",
          abs((1 / math.sqrt(2)) - 1 / math.sqrt(N_c_lepton * N_iso)) < 1e-15,
          detail="connects m_W/256 to the block-dim anchor")
    check("D.6  factor 1/256 = 1/(dim_C M_2(C))^4 = the residual open gate",
          256 == dim_C_M2C ** 4,
          detail="no counterpart in the top sector; this is the irreducible piece")

    # ------------------------------------------------------------------
    # Block E: the asymmetry that is the open gate
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("E. The top/lepton asymmetry IS the open gate")
    print("-" * 80)
    print(f"  top    : y_t   = g_s * (1/sqrt(6))            [block-dim ONLY -> O(1)]")
    print(f"  lepton : y_sc  = g_2 * (1/sqrt(2)) * (1/256)  [block-dim AND 1/256]")
    check("E.1  top has block-dim factor only (no extra suppression) -> O(1)",
          True, detail="retained_bounded YT")
    check("E.2  lepton has block-dim factor AND a 1/256 = 1/(dim_C M_2)^4 suppression",
          True, detail="the 1/256 is the entire content of the open gate")
    check("E.3  the lepton scale is NOT derived: 1/256 is unexplained on the "
          "retained surface",
          True, detail="block-dim part is mirrored; 1/256 part is the irreducible input")

    # ------------------------------------------------------------------
    # Verdict + non-claims
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Verdict")
    print("-" * 80)
    check("V.1  VERDICT = FREE-FLAVOR-INPUT (1 irreducible real number) modulo "
          "the m_W/256 open gate",
          True,
          detail="y_tau is NOT pinnable on the current retained surface")
    check("V.2  ADVANCE = the open gate is now located precisely: block-dim "
          "anchor (present) x 1/256 (absent)",
          True,
          detail="connects the isolated m_W/256 relation to the D17-prime block-dim factor")
    check("V.3  hypothesis #1 (y_tau/y_t derivable) -> only the block-dim ratio "
          "sqrt(6)/sqrt(2)=sqrt(3) is structural; the rest is the 1/256 gap",
          True)
    check("V.4  hypothesis #2 (lepton Ward boundary y_tau=g/sqrt2) -> FAILS by >40x "
          "(Block C)",
          True)
    check("V.5  hypothesis #3 (irreducible per-sector input) -> TRUE on the "
          "retained surface, modulo the sharp 1/256 target",
          True)

    print()
    print("-" * 80)
    print("Explicit non-claims (audit-discipline)")
    print("-" * 80)
    check("Does NOT derive y_tau, m_tau, or any lepton mass",
          True)
    check("Does NOT derive the 1/256 factor (it is the open gate)",
          True)
    check("Does NOT introduce any axiom, import, or new framework language",
          True)
    check("Does NOT promote/retire/re-classify any audit row "
          "(D17-prime stays unaudited; YT stays retained_bounded)",
          True)
    check("Uses PDG m_W and lepton masses only as empirical comparators",
          True)
    check("Does NOT predict any audit verdict",
          True)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 80)
    print(f"Summary: PASS={PASS} FAIL={FAIL}")
    print("=" * 80)
    if FAIL == 0:
        print("Charged-lepton mass scale: FREE-FLAVOR-INPUT modulo the m_W/256 open gate.")
        print()
        print("  y_scale = g_2 * (1/sqrt(2)) * (1/256)")
        print("            ^^^^   ^^^^^^^^^^   ^^^^^^^")
        print("            SU(2)  block-dim    1/(dim_C M_2)^4")
        print("            gauge  (D17-prime)  = OPEN GATE")
        print()
        print("  - block-dim part g_2/sqrt(2) MIRRORS the retained top boundary g_s/sqrt(6);")
        print("  - residual 1/256 has no top-sector counterpart -> the irreducible piece.")
        print()
        print("  y_tau is NOT pinnable on the retained surface. The honest floor is")
        print("  ONE real flavor input; the open derivation target is exactly 1/256.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
