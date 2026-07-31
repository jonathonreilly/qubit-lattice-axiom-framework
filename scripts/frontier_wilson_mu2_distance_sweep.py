#!/usr/bin/env python3
"""Finite parameter sweep for a supplied one-component directed-hopping model.

The historical filenames use Wilson/Newton terminology.  This runner does not
derive those physical identifications: every coefficient and observable is
dimensionless and formal.  It sweeps the operator-shift coefficient while
holding the open cubic graph and source coupling fixed, fits the magnitude of
the shared-minus-self separation-curvature proxy, and then executes a separate
finite two-coefficient centroid-proxy diagnostic.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

from dataclasses import dataclass

import numpy as np

import frontier_newton_both_masses as both_masses
import frontier_wilson_two_body_open as base


AUDIT_INPUT_PATHS = (
    "scripts/frontier_newton_both_masses.py",
    "scripts/frontier_wilson_two_body_open.py",
)

OPERATOR_SHIFT_VALUES = (0.22, 0.05, 0.01, 0.005, 0.001)
SIDES = (11, 13, 15)
SOURCE_COUPLING = 5.0
SEPARATIONS = (3, 4, 5, 6)


@dataclass
class FitSummary:
    operator_shift: float
    alpha: float
    r2: float
    n_clean: int
    n_negative: int
    n_total: int
    min_snr: float


def power_law_fit(xs, ys):
    lx = np.log(np.asarray(xs, dtype=float))
    ly = np.log(np.asarray(ys, dtype=float))
    slope, intercept = np.polyfit(lx, ly, 1)
    fit = slope * lx + intercept
    ss_res = float(np.sum((ly - fit) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return slope, intercept, r2


def collect_rows(operator_shift: float):
    rows = []
    for side in SIDES:
        for separation in SEPARATIONS:
            if separation >= side - 2:
                continue
            row = base.run_config(
                side, SOURCE_COUPLING, operator_shift, separation
            )
            mean = row["a_mutual_early_mean"]
            signal = (
                "NEGATIVE"
                if mean < -1e-6
                else ("POSITIVE" if mean > 1e-6 else "NEAR_ZERO")
            )
            quality = (
                "STABLE"
                if row["snr"] > 2.0
                else ("MARGINAL" if row["snr"] > 1.0 else "NOISY")
            )
            amp = abs(row["a_mutual_early_mean"])
            rows.append(
                {
                    "side": side,
                    "separation": separation,
                    "amp": amp,
                    "snr": row["snr"],
                    "signal": signal,
                    "quality": quality,
                    "row": row,
                }
            )
    return rows


def summarize_operator_shift(operator_shift: float, rows):
    clean = [
        (r["separation"], r["amp"])
        for r in rows
        if r["signal"] == "NEGATIVE" and r["quality"] == "STABLE"
    ]
    n_negative = sum(r["signal"] == "NEGATIVE" for r in rows)
    min_snr = min(r["snr"] for r in rows)
    if len(clean) < 2:
        return FitSummary(
            operator_shift=operator_shift,
            alpha=float("nan"),
            r2=float("nan"),
            n_clean=len(clean),
            n_negative=n_negative,
            n_total=len(rows),
            min_snr=min_snr,
        )
    alpha, _, r2 = power_law_fit([d for d, _ in clean], [amp for _, amp in clean])
    return FitSummary(
        operator_shift=operator_shift,
        alpha=float(alpha),
        r2=float(r2),
        n_clean=len(clean),
        n_negative=n_negative,
        n_total=len(rows),
        min_snr=min_snr,
    )


def main():
    print("=" * 92)
    print("ONE-COMPONENT DIRECTED-HOPPING FINITE PARAMETER SWEEP")
    print("=" * 92)
    print(
        f"dimensionless graph: sides={SIDES}, source_coupling={SOURCE_COUPLING}, "
        f"separations={SEPARATIONS}"
    )
    print(f"Packet width fixed at base SIGMA={base.SIGMA}")
    print(f"operator-shift sweep={OPERATOR_SHIFT_VALUES}")
    print()

    summaries: list[FitSummary] = []
    print(
        "row legend: r shift side separation curvature_proxy SNR sign quality; "
        "N=NEGATIVE S=STABLE"
    )
    for operator_shift in OPERATOR_SHIFT_VALUES:
        rows = collect_rows(operator_shift)
        for item in rows:
            print(
                f"r {operator_shift:g} {item['side']} {item['separation']} "
                f"{item['row']['a_mutual_early_mean']:+.6e} {item['snr']:.2f} "
                f"{item['signal'][0]} {item['quality'][0]}"
            )
        summary = summarize_operator_shift(operator_shift, rows)
        summaries.append(summary)
        if np.isfinite(summary.alpha):
            print(
                f"shift={summary.operator_shift:>7g}: alpha={summary.alpha:+.3f} "
                f"R^2={summary.r2:.4f} "
                f"negative={summary.n_negative}/{summary.n_total} "
                f"stable={summary.n_clean}/{summary.n_total} "
                f"min_SNR={summary.min_snr:.2f}"
            )
        else:
            print(
                f"  fit: insufficient stable negative rows "
                f"(stable={summary.n_clean}/{summary.n_total})"
            )

    print("=" * 92)
    print("EXECUTABLE CERTIFICATE")
    print("=" * 92)
    expected_alpha = (-3.315, -2.392, -1.992, -1.927, -1.871)
    expected_r2 = (0.9960, 0.9978, 0.9984, 0.9985, 0.9986)
    checks = {
        "C1 five declared operator-shift fits are finite": len(summaries) == 5
        and all(np.isfinite(s.alpha) and np.isfinite(s.r2) for s in summaries),
        "C2 all 60 sampled separation-curvature proxies are negative": all(
            s.n_negative == s.n_total == 12 for s in summaries
        ),
        "C3 all 60 sampled rows satisfy the declared stability threshold": all(
            s.n_clean == s.n_total == 12 for s in summaries
        ),
        "C4 fitted exponents soften strictly across the declared grid": all(
            left.alpha < right.alpha for left, right in zip(summaries, summaries[1:])
        ),
        "C5 displayed exponents reproduce the source table": all(
            round(s.alpha, 3) == target for s, target in zip(summaries, expected_alpha)
        ),
        "C6 displayed R^2 values reproduce the source table": all(
            round(s.r2, 4) == target for s, target in zip(summaries, expected_r2)
        ),
    }
    for label, passed in checks.items():
        print(f"[{('PASS' if passed else 'FAIL')}] {label}")
    n_pass = sum(checks.values())
    n_fail = len(checks) - n_pass
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    if n_fail:
        raise SystemExit(1)

    print()
    print("=" * 92)
    print("SEPARATELY SCOPED TWO-COEFFICIENT CENTROID CERTIFICATE")
    print("=" * 92)
    both_masses.main(compact=True)


if __name__ == "__main__":
    main()
