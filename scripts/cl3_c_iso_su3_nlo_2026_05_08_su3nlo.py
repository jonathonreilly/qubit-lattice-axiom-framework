"""Finite SU(3) single-plaquette fit and supplied-scenario diagnostics.

The cited RESULTS.md and SU3_NLO_DERIVATION.md artifacts are absent.
Wilson coefficients are supplied hypotheses compared with finite quadrature,
not a verified analytic derivation. Hamilton-limit values and transfer rules
are historical scenario inputs, not validated error bounds. Existing numerical
operands, fit thresholds, output keys and CLI remain unchanged. Original source:
f24d17d97d372df977476e4a69674577f31af575:scripts/cl3_c_iso_su3_nlo_2026_05_08_su3nlo.py
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np


# ---------- SU(3) heat-kernel single-plaquette ---------- #


def P_HK_SU3(s_t: float) -> float:
    """SU(3) heat-kernel single-plaquette ``<P>_HK = 1 - exp(-(4/3) s_t)``.

    Derivation: HK kernel is rho(U;s) = sum_R d_R chi_R(U) exp(-s C_2(R)),
    with C_2((1,0)) = 4/3 (fundamental rep of SU(3)). By orthonormality:
    <chi_R(U)>_HK = d_R exp(-s C_2(R)). Hence:

        <Re tr U>_HK = (1/2)(<chi_(1,0)> + <chi_(0,1)>) = 3 exp(-s 4/3).

    Therefore <P>_HK = 1 - <Re tr U>/3 = 1 - exp(-(4/3) s).
    """
    return 1.0 - math.exp(-(4.0 / 3.0) * s_t)


def P_HK_SU3_series(s_t: float, order: int = 4) -> float:
    """Truncated series of ``P_HK_SU(3)(s_t)`` for cross-check."""
    coefs = [
        0.0,                          # constant
        4.0 / 3.0,                    # s_t
        -8.0 / 9.0,                   # s_t^2 = -(4/3)^2/2
        +32.0 / 81.0,                 # s_t^3 = +(4/3)^3/6
        -32.0 / 243.0,                # s_t^4 = -(4/3)^4/24
    ][: order + 1]
    return sum(c * s_t ** i for i, c in enumerate(coefs))


# ---------- SU(3) Wilson single-plaquette via Weyl integration ---------- #


def P_W_SU3_numerical(beta_W: float, ngauss: int = 100) -> float:
    """SU(3) Wilson single-plaquette ``<P>_W = 1 - <(1/3) Re tr U>_W``.

    Weyl integration over the SU(3) Cartan torus, with adaptive range
    truncation for large beta_W where the integrand is sharply peaked
    at U = I.

    Parameters
    ----------
    beta_W : float
        Wilson coupling = 2 N_c / g^2 in the isotropic case, or
        beta_tau = 2 N_c xi / g^2 in the anisotropic Hamilton-limit case.
    ngauss : int
        Resolution parameter (per-axis); total grid has 4*ngauss^2 points.

    Returns
    -------
    P_W : float
        Wilson single-plaquette expectation.
    """
    sigma = math.sqrt(3.0 / beta_W)
    # Truncate to 10*sigma for large beta_W (covers ~exp(-50) tail).
    rmax = min(math.pi, 10.0 * sigma)
    n = ngauss * 4
    grid = np.linspace(-rmax, rmax, n, endpoint=False) + rmax / n
    h = 2 * rmax / n
    T1, T2 = np.meshgrid(grid, grid, indexing='ij')
    T3 = -T1 - T2
    V2 = (
        16.0
        * np.sin((T1 - T2) / 2) ** 2
        * np.sin((T2 - T3) / 2) ** 2
        * np.sin((T3 - T1) / 2) ** 2
    )
    Re_tr_U = np.cos(T1) + np.cos(T2) + np.cos(T3)
    A = (beta_W / 3.0) * (Re_tr_U - 3.0)
    A_max = float(A.max())
    w = V2 * np.exp(A - A_max)
    Z = float(w.sum() * h * h)
    avg_RetrU = float((Re_tr_U * w).sum() * h * h / Z)
    return 1.0 - avg_RetrU / 3.0


def P_W_SU3_analytic_NLO(s_t: float, order: int = 3) -> float:
    """Supplied Wilson-series coefficients, not a recovered analytic derivation. The historical c_3=-4.33 fit is preserved as a numerical scenario."""
    LO = (4.0 / 3.0) * s_t
    NLO = -(s_t ** 2) / 9.0
    if order == 1:
        return LO
    if order == 2:
        return LO + NLO
    # NNLO from numerical extraction
    c_3 = -4.33  # asymptotic fit value (units of 1/beta^3)
    NNLO = (c_3 * s_t ** 3) / 27.0
    return LO + NLO + NNLO


# ---------- Self-test: derivation cross-check ---------- #


def derivation_self_test(verbose: bool = True) -> dict:
    """Finite numerical fit comparison with supplied NLO coefficient; not a proof.

    Plot (P_W*beta - 4)*beta vs 1/beta. Asymptotic intercept = c_2 = -1
    (the NLO coefficient). Fit slope to extract c_3.
    """
    if verbose:
        print("\n" + "=" * 70)
        print("SELF-TEST: finite fit versus supplied SU(3) NLO coefficient")
        print("=" * 70)

    betas = [12, 24, 48, 96, 192, 384, 768, 1500, 3000]
    rows = []
    for b in betas:
        P_W = P_W_SU3_numerical(b, ngauss=100)
        nlo_form = (P_W * b - 4) * b   # should -> -1 = c_2
        rows.append({"beta": b, "P_W": P_W, "nlo_form": nlo_form})
        if verbose:
            print(f"  beta={b:>6}  <P>_W = {P_W:.7f}  (P_W*beta-4)*beta = {nlo_form:+.5f}")

    # Asymptotic c_2: take largest beta value
    c_2_inferred = rows[-1]["nlo_form"]

    # Fit y = c_2 + c_3/beta + c_4/beta^2 with large-beta values
    betas_arr = np.array([r["beta"] for r in rows], dtype=float)
    y = np.array([r["nlo_form"] for r in rows])
    mask = betas_arr > 50
    A_mat = np.column_stack([
        np.ones(mask.sum()),
        1.0 / betas_arr[mask],
        1.0 / betas_arr[mask] ** 2,
    ])
    coefs, *_ = np.linalg.lstsq(A_mat, y[mask], rcond=None)
    c_2_fit, c_3_fit, c_4_fit = coefs.tolist()

    if verbose:
        print(f"\n  Fit: y = c_2 + c_3/beta + c_4/beta^2")
        print(f"    c_2 = {c_2_fit:+.5f}  (supplied target: -1)")
        print(f"    c_3 = {c_3_fit:+.5f}")
        print(f"    c_4 = {c_4_fit:+.5f}")

    # Verify analytic LO
    P_W_LO = 4.0 / betas[-1]
    P_W_num = rows[-1]["P_W"]
    rel_err_LO = abs(P_W_LO - P_W_num) / P_W_num if P_W_num > 0 else 0
    if verbose:
        print(f"\n  At beta={betas[-1]}: <P>_W = {P_W_num:.7f}, LO {4.0/betas[-1]:.7f}  (rel err {rel_err_LO:.2%})")

    # Pass if c_2 is close to -1 (within tolerance)
    pass_self_test = abs(c_2_fit + 1.0) < 0.01
    if verbose:
        print(f"\n  PASS = {pass_self_test}")

    return {
        "rows": rows,
        "c_2_inferred": c_2_inferred,
        "c_2_fit": c_2_fit,
        "c_3_fit": c_3_fit,
        "c_4_fit": c_4_fit,
        "pass": bool(pass_self_test),
    }


# ---------- Path A: SU(3) C-iso analytic comparison ---------- #


def path_a_analytic(verbose: bool = True) -> dict:
    """Path A: SU(3) NLO analytic <P>_W vs <P>_HK across multiple xi values."""
    if verbose:
        print("\n" + "=" * 70)
        print("PATH A: SU(3) single-plaquette numerical/supplied-series comparison")
        print("=" * 70)
        print("  At g^2 = 1; s_t = g^2 / (2 xi) = 1/(2 xi);  beta_W = 3/s_t")
        print()
        header = (
            f"  {'xi':>5} {'s_t':>10} {'beta_W':>10} {'<P>_HK':>10} "
            f"{'<P>_W (num)':>14} {'<P>_W (NLO)':>13} {'(W-HK)':>11} {'rel_shift':>10}"
        )
        print(header)
        print("  " + "-" * (len(header) - 2))

    rows = []
    for xi in [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]:
        s_t = 1.0 / (2.0 * xi)
        beta_W = 3.0 / s_t
        P_HK = P_HK_SU3(s_t)
        P_W_num = P_W_SU3_numerical(beta_W, ngauss=100) if beta_W < 5000 else None
        P_W_ana_NLO = P_W_SU3_analytic_NLO(s_t, order=2)
        if P_W_num is None:
            # Use analytic at very small s_t (large beta_W)
            P_W_num = P_W_ana_NLO
        diff = P_W_num - P_HK
        rel = diff / P_HK if P_HK > 1e-12 else 0.0
        rows.append({
            "xi": xi,
            "s_t": s_t,
            "beta_W": beta_W,
            "P_HK": P_HK,
            "P_W_num": P_W_num,
            "P_W_NLO_analytic": P_W_ana_NLO,
            "abs_diff": diff,
            "rel_shift": rel,
        })
        if verbose:
            print(
                f"  {xi:>5.1f} {s_t:>10.5f} {beta_W:>10.3f} {P_HK:>10.5f} "
                f"{P_W_num:>14.7f} {P_W_ana_NLO:>13.7f} {diff:>+11.5f} {rel:>+10.3%}"
            )

    # Extract LO and NLO of rel_shift via polynomial fit (no constant)
    s_arr = np.array([r["s_t"] for r in rows])
    rel_arr = np.array([r["rel_shift"] for r in rows])
    mask = (s_arr < 0.3) & (rel_arr > 0)  # use small-s_t for clean fit
    s_fit = s_arr[mask]
    rel_fit = rel_arr[mask]

    if verbose:
        print()
        print(f"  Polynomial fit of rel_shift(s_t) for s_t < 0.3 (no constant):")

    fit_results = []
    for k in [1, 2, 3]:
        if len(s_fit) > k:
            V = np.column_stack([s_fit ** i for i in range(1, k + 1)])
            coefs, *_ = np.linalg.lstsq(V, rel_fit, rcond=None)
            fit_results.append({"order": k, "coefs": coefs.tolist()})
            if verbose:
                a_str = ", ".join(f"a_{i+1}={c:+.5f}" for i, c in enumerate(coefs))
                print(f"    Order {k}: {a_str}")

    if verbose:
        print()
        print(f"  Conditional LO of rel_shift_SU(3): 7/12 = {7/12:.6f}")
        print(f"  (vs SU(2) proxy: 1/4 = {1/4:.6f}; ratio SU(3)/SU(2) = {(7/12)/(1/4):.2f})")

    return {
        "rows": rows,
        "fit_results": fit_results,
        "analytic_LO_rel_shift_coefficient": 7.0 / 12.0,
        "su2_proxy_LO_rel_shift_coefficient": 1.0 / 4.0,
        "ratio_SU3_over_SU2": (7.0 / 12.0) / (1.0 / 4.0),
    }


# ---------- Path B: Hamilton-limit absolute shift ---------- #


def path_b_absolute_shift(P_KS_inf: float, P_KS_inf_err: float,
                           verbose: bool = True) -> dict:
    """Conditional arithmetic using supplied P_KS and an assumed single-to-multiplaquette transfer rule. Historical extrapolation provenance is unavailable. No physical error bound is established."""
    if verbose:
        print("\n" + "=" * 70)
        print("PATH B: assumed transfer-rule scenario on supplied <P>_KS")
        print("=" * 70)
        print(f"  Supplied historical scenario input: <P>_KS = {P_KS_inf} ± {P_KS_inf_err}")
        print(f"  (old extrapolation attribution is unverified; see corrected source note)")
        print()
        print(f"  {'xi':>5} {'s_t':>10} {'rel(LO)':>10} {'rel(num)':>10} "
              f"{'abs_shift':>12} {'<P>_KS bound':>14}")
        print("  " + "-" * 72)

    rows = []
    for xi in [1, 2, 4, 8, 16, 32, 64]:
        s_t = 1.0 / (2.0 * xi)
        beta_W = 3.0 / s_t
        rel_LO = (7.0 / 12.0) * s_t
        if beta_W < 5000:
            P_W_num = P_W_SU3_numerical(beta_W, ngauss=100)
            P_HK = P_HK_SU3(s_t)
            rel_num = (P_W_num - P_HK) / P_HK
        else:
            rel_num = rel_LO
        # Absolute shift on <P>_KS: rel_shift propagates as an additive bias.
        abs_shift = rel_num * P_KS_inf
        # KS-Hamilton-corrected estimate: <P>_KS_corr = <P>_KS_anisotropic / (1 + rel_shift)
        # Treating this as an interval for a physical value is an unproved additional assumption.
        rows.append({
            "xi": xi,
            "s_t": s_t,
            "rel_LO": rel_LO,
            "rel_num": rel_num,
            "abs_shift": abs_shift,
        })
        if verbose:
            print(f"  {xi:>5d} {s_t:>10.5f} {rel_LO:>10.4%} {rel_num:>10.4%} "
                  f"{abs_shift:>+12.6f} {P_KS_inf:>14.4f} ± {abs(abs_shift):.4f}")

    # ε_witness target = 3e-4 absolute. Find xi at which abs_shift drops below.
    target = 3e-4
    cross_xi = None
    for r in rows:
        if abs(r["abs_shift"]) < target:
            cross_xi = r["xi"]
            break

    if verbose:
        print()
        print(f"  ε_witness target absolute shift: {target}")
        if cross_xi is not None:
            print(f"  → C-iso shift falls below ε_witness at xi >= {cross_xi}")
        else:
            print(f"  → C-iso shift above ε_witness for all xi tested (max xi = 64)")
            # Project: rel_LO = (7/12)*(1/(2 xi)) = 7/(24 xi).
            # abs_shift = rel * P_KS = (7/(24 xi)) * 0.4410 = 0.1287/xi.
            # 0.1287/xi < 3e-4 -> xi > 429. So we'd need xi ~ 430 to hit ε_witness.
            xi_required = (7.0 / 24.0) * P_KS_inf / target
            print(f"  → Conditional scenario projection: xi ≈ {xi_required:.0f} required to drop C-iso below ε_witness.")

    return {
        "rows": rows,
        "P_KS_inf": P_KS_inf,
        "P_KS_inf_err": P_KS_inf_err,
        "epsilon_witness_target": target,
        "xi_below_target": cross_xi,
        "xi_projected_for_target": (7.0 / 24.0) * P_KS_inf / target,
    }


# ---------- Path C: combined error budget ---------- #


def path_c_error_budget(path_b_result: dict, verbose: bool = True) -> dict:
    """Quadratic combination of supplied historical statistical, volume and transfer terms. This is scenario arithmetic, not a validated Hamilton-limit uncertainty."""
    if verbose:
        print("\n" + "=" * 70)
        print("PATH C: supplied-scenario quadratic error combination")
        print("=" * 70)

    eps_stat = 0.0002       # PR #685 statistical
    eps_vol = 0.0006        # PR #685 volume
    P_KS = path_b_result["P_KS_inf"]

    print(f"  ε_stat (supplied historical value)        = {eps_stat:.4f}")
    print(f"  ε_vol  (supplied historical value) = {eps_vol:.4f}")
    print()
    print(f"  ε_C-iso (assumed transfer scenario):")

    rows = []
    for r in path_b_result["rows"]:
        xi = r["xi"]
        eps_ciso = abs(r["abs_shift"])
        # Combine in quadrature
        eps_total = math.sqrt(eps_stat ** 2 + eps_vol ** 2 + eps_ciso ** 2)
        # Dominant contribution
        if eps_ciso > eps_stat and eps_ciso > eps_vol:
            dominant = "C-iso"
        elif eps_vol > eps_stat:
            dominant = "vol"
        else:
            dominant = "stat"
        rows.append({
            "xi": xi,
            "eps_ciso": eps_ciso,
            "eps_total": eps_total,
            "dominant": dominant,
        })
        if verbose:
            print(f"    xi={xi:>3d}: ε_C-iso = {eps_ciso:.5f}  ε_total = {eps_total:.5f}  ({dominant} dominates)")

    # Where does ε_total reach ε_witness?
    target = 3e-4
    if verbose:
        print()
        print(f"  Target ε_witness ~ {target} absolute.")
        target_reached = None
        for r in rows:
            if r["eps_total"] < target:
                target_reached = r["xi"]
                break
        if target_reached is not None:
            print(f"  → ε_witness reached at xi = {target_reached} via SU(3) NLO C-iso.")
        else:
            # Project xi needed: eps_ciso = 0.1287/xi (LO formula)
            # Total: eps_total = sqrt(eps_stat^2 + eps_vol^2 + (0.1287/xi)^2)
            # Solve eps_total^2 = (3e-4)^2:
            # eps_stat^2 + eps_vol^2 = 4e-8 + 3.6e-7 = 4e-7
            # (3e-4)^2 = 9e-8
            # We need eps_stat^2 + eps_vol^2 < (3e-4)^2 first.
            # Currently eps_stat^2 + eps_vol^2 = 4e-7 = (6.3e-4)^2 > (3e-4)^2.
            # So even with eps_ciso = 0, ε_total > 3e-4.
            stat_vol_sq = eps_stat ** 2 + eps_vol ** 2
            print(f"  → ε_stat^2 + ε_vol^2 = {stat_vol_sq:.2e} = ({math.sqrt(stat_vol_sq):.4e})^2")
            if stat_vol_sq > target ** 2:
                print(f"  → ε_total cannot reach ε_witness with current stat+vol; need to tighten those first.")
            else:
                print(f"  → C-iso needs further reduction (xi > 64 or analytic to higher order).")

    return {
        "eps_stat": eps_stat,
        "eps_vol": eps_vol,
        "P_KS_inf": P_KS,
        "rows": rows,
    }


# ---------- Driver ---------- #


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["self_test", "path_a", "path_b", "path_c", "all"],
                        default="all")
    parser.add_argument("--out_dir", type=str,
                        default="outputs/action_first_principles_2026_05_08/c_iso_su3_nlo_closure")
    parser.add_argument("--P_KS_inf", type=float, default=0.4410)
    parser.add_argument("--P_KS_err", type=float, default=0.0006)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {
        "args": vars(args),
        "version": "c-iso-su3-nlo-2026-05-08",
        "module": "cl3_c_iso_su3_nlo_2026_05_08_su3nlo",
    }

    print(f"\n=== SU(3) finite diagnostics; physical closure open ===")
    print(f"Date: 2026-05-08  |  Workspace: {args.out_dir}")
    print(f"Supplied historical scenario input: <P>_KS = {args.P_KS_inf} ± {args.P_KS_err}\n")

    print("Scope: numerical fit only; missing analytic proof and physical transfer remain open.")
    t0 = time.time()

    if args.mode in ("self_test", "all"):
        results["self_test"] = derivation_self_test(verbose=True)

    if args.mode in ("path_a", "all"):
        results["path_a"] = path_a_analytic(verbose=True)

    if args.mode in ("path_b", "all"):
        results["path_b"] = path_b_absolute_shift(
            P_KS_inf=args.P_KS_inf, P_KS_inf_err=args.P_KS_err, verbose=True
        )

    if args.mode in ("path_c", "all"):
        # Need path_b result
        if "path_b" not in results:
            results["path_b"] = path_b_absolute_shift(
                P_KS_inf=args.P_KS_inf, P_KS_inf_err=args.P_KS_err, verbose=False
            )
        results["path_c"] = path_c_error_budget(results["path_b"], verbose=True)

    results["wall_time_s"] = time.time() - t0

    # Final summary
    print("\n" + "=" * 70)
    print("CONDITIONAL DIAGNOSTIC SUMMARY")
    print("=" * 70)
    if "path_a" in results:
        print(f"Path A (supplied SU(3) NLO hypothesis):")
        print(f"  rel_shift_SU(3)(s_t) = (7/12) s_t + O(s_t^2) ≈ 0.5833 s_t")
        print(f"  vs SU(2) proxy used in PR #685: rel_shift = (1/4) s_t = 0.25 s_t")
        print(f"  Ratio SU(3)/SU(2) = 7/3 ≈ 2.33  (C-iso is LARGER than prior estimate)")
    if "path_b" in results:
        print(f"\nPath B (absolute shift on <P>_KS = {args.P_KS_inf}):")
        for r in results["path_b"]["rows"]:
            if r["xi"] in [4, 16, 32, 64]:
                print(f"  xi={r['xi']:>3d}: |Δ<P>| = {abs(r['abs_shift']):.5f} ({r['rel_num']:.3%} relative)")
    if "path_c" in results:
        print(f"\nPath C (supplied-scenario error arithmetic):")
        for r in results["path_c"]["rows"]:
            if r["xi"] in [4, 16, 32, 64]:
                print(f"  xi={r['xi']:>3d}: ε_total = {r['eps_total']:.5f}  ({r['dominant']} dominates)")

    print(f"\nWall time: {results['wall_time_s']:.1f} s")

    # Save
    out_path = out_dir / f"results_mode-{args.mode}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2,
                  default=lambda o: float(o) if isinstance(o, np.generic) else str(o))
    print(f"Saved: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
