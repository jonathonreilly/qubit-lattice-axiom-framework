#!/usr/bin/env python3
"""Review-safe k-dependence rerun with a fixed N window.

This script is a hardened follow-up to ``k_dependence_ceiling.py``.
It keeps the same N window for every k, requires the same complete seed
set across the whole k x N grid, and reports uncertainty using:

1. per-seed power-law slopes
2. bootstrap confidence intervals on the mean slope

The goal is to decide whether the earlier alpha(k) variation survives
once the fit window is fixed and the seed-level spread is exposed.

PASS/FAIL block at the end of main() verifies:
  - the canonical-window seed_alpha + bootstrap CIs for all 7 k values
    match the frozen values quoted in K_DEPENDENCE_REVIEW_SAFE_NOTE.md
  - a second N=[40,60,80] window produces materially different seed_alpha
    values, backing the note's "fit-window-sensitive" interpretation
"""

from __future__ import annotations

import argparse
import math
import os
import random
import sys
from dataclasses import dataclass
from typing import Iterable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.k_dependence_ceiling import pur_min_single_k


_PASS = 0
_FAIL = 0
_FAILED_LABELS: list[str] = []


def _check_close(label: str, computed: float, expected: float, tol: float) -> bool:
    global _PASS, _FAIL
    ok = math.isfinite(computed) and abs(computed - expected) <= tol
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}: computed={computed:+.4f} expected={expected:+.4f} tol={tol:.1e}")
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED_LABELS.append(label)
    return ok


def _check_sign(label: str, computed: float, expected_sign: int) -> bool:
    global _PASS, _FAIL
    s = 0 if computed == 0 else (1 if computed > 0 else -1)
    ok = s == expected_sign
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}: computed={computed:+.4f} expected sign={expected_sign:+d}")
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED_LABELS.append(label)
    return ok


@dataclass
class FitResult:
    alpha: float
    intercept: float
    r2: float


def fit_power_law(ns: Iterable[int], ys: Iterable[float]) -> FitResult | None:
    xs = [math.log(n) for n in ns]
    zs = [math.log(y) for y in ys if y > 0]
    if len(xs) != len(zs) or len(xs) < 3:
        return None
    n = len(xs)
    mx = sum(xs) / n
    my = sum(zs) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (z - my) for x, z in zip(xs, zs))
    syy = sum((z - my) ** 2 for z in zs)
    if sxx <= 0 or syy <= 0:
        return None
    alpha = sxy / sxx
    intercept = my - alpha * mx
    r2 = (sxy ** 2) / (sxx * syy)
    return FitResult(alpha=alpha, intercept=intercept, r2=r2)


def bootstrap_mean(values: list[float], n_samples: int, rng: random.Random) -> tuple[float, float, float]:
    if not values:
        return math.nan, math.nan, math.nan
    if len(values) == 1:
        v = values[0]
        return v, v, v
    draws = []
    for _ in range(n_samples):
        sample = [values[rng.randrange(len(values))] for _ in values]
        draws.append(sum(sample) / len(sample))
    draws.sort()
    lo = draws[max(0, int(0.025 * (len(draws) - 1)))]
    hi = draws[min(len(draws) - 1, int(0.975 * (len(draws) - 1)))]
    mean = sum(values) / len(values)
    return mean, lo, hi


def fmt_prob(v: float) -> str:
    return f"{v:.4f}"


def _run_window(
    n_list: list[int],
    k_values: list[float],
    seeds: list[int],
    bootstrap_samples: int,
    rng: random.Random,
) -> dict[float, dict[str, float | int]]:
    """Build the seed x k x N table and reduce to per-k summary stats.

    Returns dict keyed by k with fields: n_ok, mean_alpha, se, boot_lo,
    boot_hi, pooled_alpha, pooled_r2. Missing fits get math.nan.
    """
    table: dict[float, dict[int, dict[int, float]]] = {}
    complete_seeds = set(seeds)

    for k in k_values:
        table[k] = {}
        for seed in seeds:
            per_n: dict[int, float] = {}
            ok = True
            for nl in n_list:
                v = pur_min_single_k(nl, k, seed)
                if v is None or not math.isfinite(v) or v >= 1.0:
                    ok = False
                    break
                per_n[nl] = max(1e-15, 1.0 - v)
            if ok and len(per_n) == len(n_list):
                table[k][seed] = per_n
            else:
                complete_seeds.discard(seed)

    complete_seeds_sorted = sorted(complete_seeds)
    summary: dict[float, dict[str, float | int]] = {}

    for k in k_values:
        seed_alphas: list[float] = []
        pooled_curve: dict[int, list[float]] = {nl: [] for nl in n_list}
        for seed in complete_seeds_sorted:
            per_n = table.get(k, {}).get(seed)
            if not per_n:
                continue
            fit = fit_power_law(n_list, [per_n[nl] for nl in n_list])
            if fit is not None:
                seed_alphas.append(fit.alpha)
                for nl in n_list:
                    pooled_curve[nl].append(per_n[nl])

        pooled_vals = [sum(pooled_curve[nl]) / len(pooled_curve[nl]) for nl in n_list if pooled_curve[nl]]
        pooled_fit = fit_power_law([nl for nl in n_list if pooled_curve[nl]], pooled_vals)

        if seed_alphas:
            mean_alpha = sum(seed_alphas) / len(seed_alphas)
            if len(seed_alphas) > 1:
                var = sum((a - mean_alpha) ** 2 for a in seed_alphas) / (len(seed_alphas) - 1)
                se = math.sqrt(var / len(seed_alphas))
            else:
                se = 0.0
            _, boot_lo, boot_hi = bootstrap_mean(seed_alphas, bootstrap_samples, rng)
            summary[k] = {
                "n_ok": len(seed_alphas),
                "mean_alpha": mean_alpha,
                "se": se,
                "boot_lo": boot_lo,
                "boot_hi": boot_hi,
                "pooled_alpha": pooled_fit.alpha if pooled_fit else math.nan,
                "pooled_r2": pooled_fit.r2 if pooled_fit else math.nan,
            }
        else:
            summary[k] = {
                "n_ok": 0,
                "mean_alpha": math.nan,
                "se": math.nan,
                "boot_lo": math.nan,
                "boot_hi": math.nan,
                "pooled_alpha": math.nan,
                "pooled_r2": math.nan,
            }
    return summary


def _print_table(n_list: list[int], k_values: list[float], summary: dict[float, dict[str, float | int]]) -> None:
    header = (
        f"{'k':>5s}  {'n_ok':>4s}  {'seed_alpha':>11s}  {'SE':>7s}  "
        f"{'boot95%':>17s}  {'pooled_alpha':>13s}  {'pooled_R2':>9s}"
    )
    print(header)
    print("-" * len(header))
    for k in k_values:
        s = summary[k]
        if s["n_ok"] == 0:
            print(f"{k:5.1f}  {0:4d}  {'FAIL':>11s}  {'FAIL':>7s}  {'FAIL':>17s}  {'FAIL':>13s}  {'FAIL':>9s}")
            continue
        boot_str = f"[{s['boot_lo']:+.3f}, {s['boot_hi']:+.3f}]"
        pooled_alpha = f"{s['pooled_alpha']:+.3f}" if math.isfinite(s["pooled_alpha"]) else "N/A"
        pooled_r2 = f"{s['pooled_r2']:.3f}" if math.isfinite(s["pooled_r2"]) else "N/A"
        print(
            f"{k:5.1f}  {int(s['n_ok']):4d}  {s['mean_alpha']:+11.3f}  {s['se']:7.3f}  "
            f"{boot_str:>17s}  {pooled_alpha:>13s}  {pooled_r2:>9s}"
        )


# Frozen seed_alpha + bootstrap CI per k from K_DEPENDENCE_REVIEW_SAFE_NOTE.md
# (canonical window [25,30,40,60,80], 16 seeds, bootstrap rng=Random(12345),
# 2000 samples). This assert block makes those quoted values reproducible.
_FROZEN_CANONICAL = {
    1.0:  {"mean_alpha": -3.931, "boot_lo": -5.674, "boot_hi": -2.255, "pooled_alpha": -1.846},
    2.0:  {"mean_alpha": -2.881, "boot_lo": -4.784, "boot_hi": -1.094, "pooled_alpha": -0.636},
    3.0:  {"mean_alpha": -2.286, "boot_lo": -4.036, "boot_hi": -0.528, "pooled_alpha": -0.316},
    5.0:  {"mean_alpha": -3.322, "boot_lo": -5.745, "boot_hi": -0.920, "pooled_alpha": -1.800},
    7.0:  {"mean_alpha": -2.827, "boot_lo": -5.306, "boot_hi": -0.198, "pooled_alpha": -0.655},
    10.0: {"mean_alpha": -3.813, "boot_lo": -6.389, "boot_hi": -1.242, "pooled_alpha": -2.518},
    15.0: {"mean_alpha": -2.773, "boot_lo": -5.307, "boot_hi": -0.455, "pooled_alpha": -1.236},
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-list", nargs="+", type=int, default=[25, 30, 40, 60, 80])
    parser.add_argument("--n-seeds", type=int, default=16)
    parser.add_argument("--k-values", nargs="+", type=float, default=[1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0])
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip the PASS/FAIL validation block (frozen-value asserts + window comparison).",
    )
    args = parser.parse_args()

    seeds = [s * 7 + 3 for s in range(args.n_seeds)]
    n_list = list(args.n_list)
    k_values = list(args.k_values)
    rng = random.Random(12345)

    print("=" * 92)
    print("K-DEPENDENCE REVIEW-SAFE RERUN")
    print("  fixed N window across k, shared seed set, per-seed slopes + bootstrap CI")
    print(f"  N window = {n_list}")
    print(f"  seeds = {args.n_seeds}, bootstrap samples = {args.bootstrap_samples}")
    print("=" * 92)
    print()

    summary_canonical = _run_window(n_list, k_values, seeds, args.bootstrap_samples, rng)
    complete = min(int(s["n_ok"]) for s in summary_canonical.values())
    print(f"Complete shared seeds across all k and N: {complete} / {len(seeds)}")
    print()
    _print_table(n_list, k_values, summary_canonical)

    print()
    print("Interpretation guide:")
    print("  - seed_alpha: mean of per-seed slope fits on the fixed N window")
    print("  - boot95%: bootstrap CI on the mean seed_alpha")
    print("  - pooled_alpha: fit to the mean curve, shown only as a diagnostic")
    print()
    print("Review-safe rule:")
    print("  If the bootstrapped intervals overlap heavily across k, the old alpha(k)")
    print("  story was mostly a fit-window artifact. If they separate cleanly, the k")
    print("  dependence survives on a fixed window.")

    if args.skip_validation:
        return
    if (
        n_list != [25, 30, 40, 60, 80]
        or args.n_seeds != 16
        or args.bootstrap_samples != 2000
        or k_values != [1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0]
    ):
        print()
        print("[VALIDATION SKIPPED: non-canonical args; frozen values only apply to defaults]")
        return

    print()
    print("=" * 92)
    print("VALIDATION (frozen-value asserts vs K_DEPENDENCE_REVIEW_SAFE_NOTE.md)")
    print("=" * 92)
    for k in k_values:
        s = summary_canonical[k]
        fz = _FROZEN_CANONICAL[k]
        _check_close(f"k={k:>4.1f} mean_alpha", s["mean_alpha"], fz["mean_alpha"], 0.01)
        _check_close(f"k={k:>4.1f} boot_lo", s["boot_lo"], fz["boot_lo"], 0.05)
        _check_close(f"k={k:>4.1f} boot_hi", s["boot_hi"], fz["boot_hi"], 0.05)
        _check_close(f"k={k:>4.1f} pooled_alpha", s["pooled_alpha"], fz["pooled_alpha"], 0.01)

    print()
    print("=" * 92)
    print("WINDOW-COMPARISON (closes the 'fit-window-sensitive' claim)")
    print("  Re-run with the smaller late-N window [40, 60, 80] and check that")
    print("  the seed_alpha values shift materially vs the canonical window.")
    print("=" * 92)
    rng2 = random.Random(12345)
    alt_n_list = [40, 60, 80]
    summary_alt = _run_window(alt_n_list, k_values, seeds, args.bootstrap_samples, rng2)
    print(f"  N window = {alt_n_list}")
    print()
    _print_table(alt_n_list, k_values, summary_alt)

    print()
    diffs = []
    for k in k_values:
        d = summary_canonical[k]["mean_alpha"] - summary_alt[k]["mean_alpha"]
        diffs.append(d)
        print(f"  k={k:>4.1f}: canonical seed_alpha={summary_canonical[k]['mean_alpha']:+.3f}  "
              f"alt seed_alpha={summary_alt[k]['mean_alpha']:+.3f}  diff={d:+.3f}")
    max_abs_diff = max(abs(d) for d in diffs)
    print()
    _check_sign(
        "window comparison: at least one |Δseed_alpha| > 0.3 (fit-window sensitivity)",
        max_abs_diff - 0.3,
        +1,
    )

    print()
    print("=" * 92)
    if _FAIL == 0:
        print(f"K_DEPENDENCE_FIXED_WINDOW_REVIEW: PASS={_PASS}  FAIL=0")
    else:
        print(f"K_DEPENDENCE_FIXED_WINDOW_REVIEW: PASS={_PASS}  FAIL={_FAIL}")
        print("Failed checks:")
        for lbl in _FAILED_LABELS:
            print(f"  - {lbl}")
    print("=" * 92)
    sys.exit(0 if _FAIL == 0 else 1)


if __name__ == "__main__":
    main()
