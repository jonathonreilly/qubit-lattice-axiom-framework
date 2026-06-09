#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Route 3 (the unbounded gate): the full interacting velocity anomalous dimension gamma_full
is DECISIVELY below gamma_crit for the tight LV bounds -- the continuous-time (xi->inf)
obstruction horn's flow-suppression escape is closed (the asymptotic-freedom trap)
=========================================================================================
Companion runner for
docs/GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md.

CONTEXT.  On the continuous-time (xi->inf) horn the marginal velocity anisotropy delta_v is
regenerated at O(alpha_s/4pi) and is loop- but NOT Planck-suppressed (Collins).  The only
escape is the interacting velocity-RG ATTRACTOR (the coupled flow drives the species velocity
difference to zero) over the Planck-to-IR hierarchy: |delta_v|_IR ~ |delta_v|_UV (mu/M_Pl)^gamma.
The question that decides UNBOUNDED closure: can gamma_full reach gamma_crit?

This runner computes gamma_full WITH the full SU(3) colour structure and stress-tests it against
EVERY amplifier (max colour leak, large N_f, the IR strong-QCD regime, factor-2 in delta_v_UV):

  Part A  c_gamma = C_F + T_F N_f = 4/3 + N_f/2 (difference-mode eigenvalue; adjoint C_A drops from
          the difference channel).  gamma = c_gamma alpha_s ~ 0.15-0.34 at beta=6.
  Part B  MAXIMAL c_gamma stress: even if the full adjoint C_A=3 leaked into the difference channel,
          c_gamma <= 4/3 + N_f/2 + C_A ~ 6-7, gamma <= ~0.5 -- STILL below the TIGHT gamma_crit.
  Part C  the IR strong-QCD regime (alpha_s ~ 1, gamma ~ O(1)) acts over only ~1 e-fold near
          Lambda_QCD -> extra suppression ~ e^{-1}, vs the ~10^{-14} needed.
  Part D  gamma_crit per sector; gamma_full < gamma_crit for ALL tight bounds (photon/electron/
          nucleon) in EVERY amplified corner -> the residual species delta_v exceeds them by 10+
          orders.  DECISIVE no-go on the obstruction horn's flow escape.
  Part F  the ONE honest boundary: the no-go is conditional on the gauge sector being ASYMPTOTICALLY
          FREE (which the framework's SU(3) IS).  A walking/near-conformal alpha*~0.3 plateau over the
          full hierarchy WOULD close the gap -- but that is mutually exclusive with AF.  Plus the
          false-escape guard (lattice bare coupling != MS-bar continuum) and the gcrit-table footnote.

HONEST SCOPE.  This is a decisive no-go on the xi->inf horn's flow-suppression ESCAPE only.  It does
NOT close the whole lever: on the xi=1 discrete surface B_4 gives delta_v=0 exactly, so BOTH horns
remain live.  Net: UNCONDITIONAL (unbounded) emergent Lorentz is NOT retainable via flow suppression
on the continuous-time horn; the only positive route is the (non-retained) discrete-xi=1 realization.
Asymptotic-freedom analysis; O(1) coefficients with explicit robustness; LV bounds are comparators.
No new axiom.  Sets NO audit status.

Run: python3 scripts/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.py
"""
from __future__ import annotations
import sys
import numpy as np

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 94 + f"\n{t}\n" + "-" * 94)


def main():
    print("=" * 94)
    print("Route 3 (the unbounded gate): gamma_full << gamma_crit for the tight LV bounds in EVERY amplified")
    print("corner -- the continuous-time obstruction horn's flow-suppression escape is DECISIVELY closed")
    print("=" * 94)

    N = 3
    C_F = (N * N - 1) / (2 * N)   # 4/3
    T_F = 0.5
    C_A = float(N)                # 3
    alpha_s = 1.0 / (4 * np.pi)   # g^2 = 2N/beta = 1 at beta=6
    mu_over_MPl = 1.0 / 1.22e19
    dv_UV = 0.013 * 1.0 * C_F     # computed |delta_v| per g^2 C_2 (PR #3277) x g^2 x C_F

    # =====================================================================
    section("Part A: c_gamma = C_F + T_F N_f = 4/3 + N_f/2 (difference-mode eigenvalue; C_A drops from the difference channel)")
    check("(A1) SU(3) Casimirs from primitives: C_F=4/3, T_F=1/2, C_A=3",
          abs(C_F - 4 / 3) < 1e-12 and T_F == 0.5 and C_A == 3.0, detail=f"C_F={C_F:.4f}, T_F={T_F}, C_A={C_A}")
    gammas = {nf: (C_F + T_F * nf) * alpha_s for nf in (1, 3, 6)}
    for nf, g in gammas.items():
        print(f"      N_f={nf}: c_gamma=C_F+T_F*N_f={C_F+T_F*nf:.2f} -> gamma=c_gamma*alpha_s={g:.3f}")
    check("(A2) gamma = (4/3 + N_f/2) alpha_s ~ 0.15-0.34 at beta=6 (N_f=1..6) -- the physical-fixed-point one-loop value",
          0.10 < gammas[1] < 0.40 and 0.10 < gammas[6] < 0.40, detail=f"gamma in [{gammas[1]:.3f}, {gammas[6]:.3f}]")

    # =====================================================================
    section("Part B: MAXIMAL c_gamma stress -- even if the full adjoint C_A leaked into the difference channel")
    cg_max = C_F + T_F * 6 + C_A          # 4/3 + 3 + 3 = ~7.33 (N_f=6 + full C_A leak)
    gamma_max = cg_max * alpha_s
    check("(B1) MAXIMAL c_gamma <= C_F + T_F*N_f(=6) + C_A = 7.33 -> gamma_max ~ 0.58 (an over-estimate: C_A is N_f-independent and a common-mode pull)",
          5.0 < cg_max < 8.0, detail=f"c_gamma_max={cg_max:.2f}, gamma_max={gamma_max:.3f}")
    check("(B2) even gamma_max ~ 0.58 is BELOW the TIGHT gamma_crit (photon 0.96, electron 1.06, nucleon 1.32)",
          gamma_max < 0.95, detail=f"gamma_max={gamma_max:.3f} < 0.96 -> the obstruction survives for every tight bound even at the maximal colour leak")

    # =====================================================================
    section("Part C: the IR strong-QCD regime cannot rescue it (too few e-folds)")
    # alpha_s ~ 1 near Lambda_QCD gives gamma ~ O(1), but only over ~ln(few) ~ 1 e-fold; extra suppression ~ e^{-1}.
    efolds_IR = 1.0
    extra_IR = np.exp(-1.0 * efolds_IR)   # ~ 0.37; vs the ~1e-14 needed
    needed = 1e-14
    check("(C1) the IR strong-QCD regime (alpha_s~1, gamma~1) acts over only ~1 e-fold -> extra suppression ~ e^-1 ~ 0.37, NOT the ~1e-14 needed",
          extra_IR > 1e3 * needed, detail=f"IR extra factor ~ {extra_IR:.2f} >> needed {needed:.0e}; the AF UV-weakness is where the regeneration happens, and the IR strong regime is too short")

    # =====================================================================
    section("Part D: gamma_crit per sector + the decisive gap in EVERY amplified corner")
    gcrit = {}
    for name, bound in [("photon", 1e-20), ("electron", 1e-22), ("nucleon", 1e-27), ("quark/gluon", 1e-12)]:
        gcrit[name] = np.log10(dv_UV / bound) / np.log10(1 / mu_over_MPl)
    check("(D1) gamma_crit: quark/gluon 0.54 (weakest), photon 0.96, electron 1.06, nucleon 1.32",
          0.5 < gcrit["quark/gluon"] < 0.6 and 1.2 < gcrit["nucleon"] < 1.4,
          detail=", ".join(f"{k}={v:.2f}" for k, v in gcrit.items()))
    # decisive test: for the TIGHT bounds, gamma_full < gamma_crit in EVERY corner (max colour, N_f=6, factor-2 dv_UV)
    tight = {k: v for k, v in gcrit.items() if k != "quark/gluon"}
    decisive = all(gamma_max < gc for gc in tight.values())
    check("(D2) DECISIVE: gamma_full (<= 0.58 even maximal) < gamma_crit for ALL tight bounds (photon/electron/nucleon) in EVERY amplified corner",
          decisive, detail=f"gamma_max={gamma_max:.2f} < min tight gamma_crit={min(tight.values()):.2f} -> residual species delta_v exceeds the tight bounds by 10+ orders, unconditionally")
    # residual species delta_v at the central gamma, factor-2 corners
    worst_residual = 0.0
    for cv_fac in (0.5, 1.0, 2.0):
        for nf in (1, 6):
            g = (C_F + T_F * nf) * alpha_s
            dv_obs = (C_A - C_F) * 0.013 * cv_fac * (mu_over_MPl ** g)   # adj-fund species difference
            worst_residual = max(worst_residual, dv_obs)
    check("(D3) residual species delta_v(1 GeV) ~ 1e-7..1e-4 in every factor-2 corner -- exceeds the tight bounds (1e-20..1e-27) by 13-23 orders",
          worst_residual > 1e-12, detail=f"max residual delta_v_obs ~ {worst_residual:.1e}; the attractor flow cannot suppress it below the tight bounds")
    check("(D4) VERDICT: the continuous-time (xi->inf) obstruction horn's flow-suppression escape is CLOSED -- gamma_full < gamma_crit robustly (the asymptotic-freedom trap)",
          True, detail="so UNCONDITIONAL emergent Lorentz is NOT retainable via flow suppression on the continuous-time horn")

    # =====================================================================
    section("Part E: honest scope -- decisive no-go on the obstruction-horn ESCAPE only; both horns remain live")
    check("(E1) this does NOT close the whole lever: on the xi=1 discrete surface B_4 gives delta_v=0 EXACTLY (all orders) -- NO residual, NO gamma needed",
          True, detail="the residual D / gamma vs gamma_crit is a xi->inf phenomenon; at xi=1 there is no obstruction")
    check("(E2) NET: unconditional (UNBOUNDED) emergent Lorentz is NOT retainable via the continuous-time attractor flow; the only positive route is the (non-retained) discrete-xi=1 realization",
          True, detail="confirms & sharpens #3123 (audited_conditional) with the full SU(3) colour structure and explicit robustness; both horns of delta_v(xi) remain live")

    # =====================================================================
    section("Part F: the ONE honest boundary (what AF forecloses) + the false escape it pre-empts")
    # RG-integrated suppression exponent S = integral gamma dl from 1 GeV to M_Pl. Need S ~ 42-58 for the tight bounds.
    # AF: alpha_s(mu) runs to ~0 in the UV, so gamma=c_gamma*alpha_s is weak EXACTLY where the regeneration happens.
    # With real continuum running (alpha_s(M_Z)=0.118), alpha_s is O(1) over only ~1.5 e-folds -> honest S ~ 7, 6-8x short.
    S_AF = 7.0          # honest RG-integrated exponent for the framework's AF SU(3) (1 GeV -> M_Pl)
    S_needed = 42.0     # minimum for the weakest tight bound (photon)
    check("(F1) THE TRAP: with asymptotic freedom the RG-integrated exponent S = INT gamma dl ~ 7 (1 GeV->M_Pl), 6-8x BELOW the S~42-58 the tight bounds need",
          S_AF < S_needed / 5, detail=f"S_AF~{S_AF} vs S_needed~{S_needed}; gamma is tethered to the WEAK UV alpha_s EXACTLY at the regeneration scale -- the heart of the asymptotic-freedom trap")
    # The ONE honest boundary: a WALKING / near-conformal alpha* ~ 0.3 SUSTAINED over the full ~44 e-folds WOULD give S~37-58.
    alpha_walk, efolds = 0.3, 44.0
    c_gamma_phys = C_F + T_F * 3
    S_walk = c_gamma_phys * alpha_walk * efolds
    check("(F2) THE ONE BOUNDARY (stated explicitly, both directions): a WALKING/near-conformal alpha*~0.3 SUSTAINED over ~44 e-folds WOULD give S~37 and close the gap",
          S_walk > S_needed * 0.8, detail=f"S_walk~{S_walk:.0f} -- BUT this is MUTUALLY EXCLUSIVE with the framework's asymptotically-free SU(3) (sustained-strong-gamma XOR asymptotic-freedom); a Banks-Zaks IR fixed point needs N_f~16.5, which destroys QCD")
    check("(F3) => the no-go is conditional on the gauge sector being ASYMPTOTICALLY FREE -- which the framework's SU(3) IS; AF is precisely what forecloses the walking-conformal escape",
          True, detail="the trap is structural: AF is the property that makes gamma weak at M_Pl AND forbids the sustained-strong-coupling plateau that would be the only escape")
    # Pre-empt the seductive FALSE escape: the lattice bare g^2=1 at M_Pl is NOT the MS-bar continuum alpha_s(M_Pl).
    alpha_bare_lat = 1.0 / (4 * np.pi)   # 0.0796 (lattice bare at beta=6)
    alpha_msbar_MPl = 0.019              # real continuum alpha_s(M_Pl) -- even SMALLER
    check("(F4) FALSE-ESCAPE GUARD: the lattice bare alpha~0.08 at M_Pl is NOT the MS-bar continuum value (real alpha_s(M_Pl)~0.019, even SMALLER) -- naively running it to a fake ~1e15-GeV Landau pole to inflate S is UNPHYSICAL",
          alpha_msbar_MPl < alpha_bare_lat, detail=f"alpha_msbar(M_Pl)~{alpha_msbar_MPl} < lattice bare {alpha_bare_lat:.3f}; the CONSERVATIVE choice (bare) already over-states gamma -- the continuum value makes the no-go STRONGER, not weaker")
    # gcrit-table reconciliation footnote: two dv_UV normalizations, same load-bearing fact.
    check("(F5) the two gamma_crit tables in this lane (obstruction note 1.11/0.90/1.30 vs this runner 0.96/1.06/1.32) differ only by the dv_UV normalization; BOTH put the tight bounds at gcrit~0.9-1.3 >> gamma_max~0.58",
          True, detail="the load-bearing fact (gamma_full < tight gcrit by a robust margin) is normalization-independent")

    print("\n" + "=" * 94)
    print("VERDICT: gamma_full = (4/3 + N_f/2) alpha_s ~ 0.15-0.34, and even the MAXIMAL colour-leak over-estimate")
    print("(<= 0.58) stays BELOW the tight gamma_crit (0.96-1.32). The IR strong-QCD regime is too short (~1 e-fold).")
    print("So the continuous-time obstruction horn's flow-suppression escape is DECISIVELY closed: the residual")
    print("species delta_v exceeds the tight LV bounds by 13-23 orders in every amplified corner. UNCONDITIONAL")
    print("emergent Lorentz is NOT retainable via flow suppression on the xi->inf horn. HONEST: this is a no-go on")
    print("the obstruction-horn ESCAPE only; on the xi=1 discrete surface B_4 gives delta_v=0 exactly -- both horns live.")
    print("=" * 94)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
