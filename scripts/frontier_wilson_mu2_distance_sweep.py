#!/usr/bin/env python3
"""
Wilson open-lattice distance-law sweep versus screening mass.

Goal:
  test whether the steep open-lattice Wilson distance exponent is primarily a
  screening-mass artifact by sweeping mu^2 while keeping the rest of the open
  surface fixed, then execute the separately scoped finite both-masses
  centroid certificate cited by the companion note.

Protocol:
  - open 3D Wilson lattice
  - SHARED vs SELF_ONLY only
  - same packet width, same G, same side set, same separations
  - fit |a_mut| ~ d^alpha on clean attractive rows
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

MU2_VALUES = (0.22, 0.05, 0.01, 0.005, 0.001)
SIDES = (11, 13, 15)
G_VAL = 5.0
DISTANCES = (3, 4, 5, 6)


@dataclass
class FitSummary:
    mu2: float
    alpha: float
    r2: float
    n_clean: int
    n_attractive: int
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


def collect_rows(mu2: float):
    rows = []
    for side in SIDES:
        for d in DISTANCES:
            if d >= side - 2:
                continue
            row = base.run_config(side, G_VAL, mu2, d)
            signal, quality = base.label(row["a_mutual_early_mean"], row["snr"])
            amp = abs(row["a_mutual_early_mean"])
            rows.append(
                {
                    "side": side,
                    "d": d,
                    "amp": amp,
                    "snr": row["snr"],
                    "signal": signal,
                    "quality": quality,
                    "row": row,
                }
            )
    return rows


def summarize_mu2(mu2: float, rows):
    clean = [(r["d"], r["amp"]) for r in rows if r["signal"] == "ATTRACT" and r["quality"] == "CLEAN"]
    n_attractive = sum(r["signal"] == "ATTRACT" for r in rows)
    min_snr = min(r["snr"] for r in rows)
    if len(clean) < 2:
        return FitSummary(
            mu2=mu2,
            alpha=float("nan"),
            r2=float("nan"),
            n_clean=len(clean),
            n_attractive=n_attractive,
            n_total=len(rows),
            min_snr=min_snr,
        )
    alpha, _, r2 = power_law_fit([d for d, _ in clean], [amp for _, amp in clean])
    return FitSummary(
        mu2=mu2,
        alpha=float(alpha),
        r2=float(r2),
        n_clean=len(clean),
        n_attractive=n_attractive,
        n_total=len(rows),
        min_snr=min_snr,
    )


def main():
    print("=" * 92)
    print("WILSON OPEN-LATTICE DISTANCE-LAW SWEEP VS MU^2")
    print("=" * 92)
    print(f"Surface: sides={SIDES}, G={G_VAL}, separations={DISTANCES}")
    print(f"Packet width fixed at base SIGMA={base.SIGMA}")
    print(f"mu^2 sweep={MU2_VALUES}")
    print()

    summaries: list[FitSummary] = []
    print("row legend: r mu2 side d a_mut SNR signal quality; A=ATTRACT C=CLEAN")
    for mu2 in MU2_VALUES:
        rows = collect_rows(mu2)
        for item in rows:
            print(
                f"r {mu2:g} {item['side']} {item['d']} "
                f"{item['row']['a_mutual_early_mean']:+.6e} {item['snr']:.2f} "
                f"{item['signal'][0]} {item['quality'][0]}"
            )
        summary = summarize_mu2(mu2, rows)
        summaries.append(summary)
        if np.isfinite(summary.alpha):
            print(
                f"mu^2={summary.mu2:>7g}: alpha={summary.alpha:+.3f} "
                f"R^2={summary.r2:.4f} "
                f"attractive={summary.n_attractive}/{summary.n_total} "
                f"clean={summary.n_clean}/{summary.n_total} "
                f"min_SNR={summary.min_snr:.2f}"
            )
        else:
            print(
                f"  fit: insufficient clean attractive rows "
                f"(clean={summary.n_clean}/{summary.n_total})"
            )

    print("=" * 92)
    print("EXECUTABLE CERTIFICATE")
    print("=" * 92)
    expected_alpha = (-3.315, -2.392, -1.992, -1.927, -1.871)
    expected_r2 = (0.9960, 0.9978, 0.9984, 0.9985, 0.9986)
    checks = {
        "C1 five declared mu^2 fits are finite": len(summaries) == 5
        and all(np.isfinite(s.alpha) and np.isfinite(s.r2) for s in summaries),
        "C2 all 60 sampled rows are attractive": all(
            s.n_attractive == s.n_total == 12 for s in summaries
        ),
        "C3 all 60 sampled rows are clean": all(
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
    print("SEPARATELY SCOPED BOTH-MASSES CENTROID CERTIFICATE")
    print("=" * 92)
    both_masses.main(compact=True)


if __name__ == "__main__":
    main()
