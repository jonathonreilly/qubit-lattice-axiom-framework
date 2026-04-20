#!/usr/bin/env python3
"""Search one-body families with hydrogen priority and a hard He+ guardrail."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402
from scripts.atomic_one_body_runtime import benchmark_one_body_candidate  # noqa: E402


def _rank_key(row: dict[str, Any]) -> tuple[float, float, float]:
    return (
        float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
        float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--kinetic-stencils",
        nargs="*",
        default=("five_point", "seven_point"),
    )
    parser.add_argument(
        "--lattice-spacings",
        type=float,
        nargs="*",
        default=(0.8, 2.0 / 3.0),
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=(
            "hard_floor",
            "erf_softcore",
            "exp_softcore",
            "tanh_softcore",
            "gaussian_floor",
        ),
    )
    parser.add_argument(
        "--softening-multipliers",
        type=float,
        nargs="*",
        default=(0.4, 0.5, 0.65, 0.8),
    )
    parser.add_argument(
        "--counterterm-strengths",
        type=float,
        nargs="*",
        default=(-0.2, -0.1, 0.0, 0.1, 0.2),
    )
    parser.add_argument("--max-orbitals", type=int, default=16)
    parser.add_argument("--n-eig", type=int, default=40)
    parser.add_argument("--helium-guard-band", type=float, default=0.02)
    parser.add_argument("--min-hydrogen-improvement", type=float, default=0.01)
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_hydrogen_priority_search.json",
    )
    args = parser.parse_args()

    baseline_payload = read_json(args.baseline_readout_json)
    baseline_metrics = baseline_payload["accuracy_metrics"]
    baseline_hydrogen_error = float(
        baseline_metrics["relative_errors"]["hydrogen_ground"]
    )
    baseline_helium_ion_error = float(
        baseline_metrics["relative_errors"]["helium_ion_ground"]
    )
    baseline_one_body_rms = float(
        baseline_metrics["scores"]["one_body_rms_relative_error"]
    )

    stencils = [str(value) for value in args.kinetic_stencils]
    spacings = [float(value) for value in args.lattice_spacings]
    profiles = [str(value) for value in args.nuclear_profiles]
    multipliers = [float(value) for value in args.softening_multipliers]
    counterterms = [float(value) for value in args.counterterm_strengths]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    total_points = (
        len(stencils) * len(spacings) * len(profiles) * len(multipliers) * len(counterterms)
    )
    current_index = 0
    for kinetic_stencil in stencils:
        for lattice_spacing in spacings:
            for nuclear_profile in profiles:
                for softening_multiplier in multipliers:
                    for counterterm_strength in counterterms:
                        current_index += 1
                        scan_started = time.perf_counter()
                        benchmark = benchmark_one_body_candidate(
                            reference_coupling=1.595,
                            lattice_spacing=float(lattice_spacing),
                            softening_multiplier=float(softening_multiplier),
                            nuclear_profile=str(nuclear_profile),
                            nuclear_counterterm_strength=float(counterterm_strength),
                            kinetic_stencil=str(kinetic_stencil),
                            max_orbitals=int(args.max_orbitals),
                            n_eig=int(args.n_eig),
                        )
                        errors = benchmark["metrics"]["relative_errors"]
                        scores = benchmark["metrics"]["scores"]
                        hydrogen_error = float(errors["hydrogen_ground"])
                        helium_ion_error = float(errors["helium_ion_ground"])
                        hydrogen_improvement = baseline_hydrogen_error - hydrogen_error
                        helium_guardrail = (
                            helium_ion_error
                            <= baseline_helium_ion_error + float(args.helium_guard_band)
                        )
                        hydrogen_priority_pass = (
                            hydrogen_improvement >= float(args.min_hydrogen_improvement)
                        )
                        physically_bound = bool(
                            benchmark["hydrogen_ground_orbital"]["physical_bound"]
                            and benchmark["helium_ion_ground_orbital"]["physical_bound"]
                        )
                        row = dict(benchmark)
                        row["elapsed_seconds"] = round(
                            time.perf_counter() - scan_started,
                            6,
                        )
                        row["guardrails"] = {
                            "hydrogen_priority_pass": hydrogen_priority_pass,
                            "helium_ion_guardrail_pass": helium_guardrail,
                            "physically_bound": physically_bound,
                            "one_body_rms_improves": float(
                                scores["one_body_rms_relative_error"]
                            )
                            < baseline_one_body_rms,
                        }
                        row["improvement_vs_baseline"] = {
                            "hydrogen_ground_delta": hydrogen_error - baseline_hydrogen_error,
                            "helium_ion_ground_delta": (
                                helium_ion_error - baseline_helium_ion_error
                            ),
                            "one_body_rms_relative_error_delta": (
                                float(scores["one_body_rms_relative_error"])
                                - baseline_one_body_rms
                            ),
                        }
                        row["promoted"] = bool(
                            hydrogen_priority_pass and helium_guardrail and physically_bound
                        )
                        rows.append(row)
                        print(
                            f"[{current_index}/{total_points}] "
                            f"stencil={kinetic_stencil} a={lattice_spacing:.4f} "
                            f"p={nuclear_profile} m={softening_multiplier:.2f} "
                            f"ct={counterterm_strength:+.2f} "
                            f"H={hydrogen_error:.4%} He+={helium_ion_error:.4%} "
                            f"rms={scores['one_body_rms_relative_error']:.6f} "
                            f"promoted={'YES' if row['promoted'] else 'NO'}",
                            flush=True,
                        )

    promoted_rows = [row for row in rows if row["promoted"]]
    guardrail_rows = [
        row
        for row in rows
        if row["guardrails"]["helium_ion_guardrail_pass"]
        and row["guardrails"]["physically_bound"]
    ]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "baseline_one_body_metrics": {
            "hydrogen_ground_error": baseline_hydrogen_error,
            "helium_ion_ground_error": baseline_helium_ion_error,
            "one_body_rms_relative_error": baseline_one_body_rms,
        },
        "search_configuration": {
            "kinetic_stencils": stencils,
            "lattice_spacings": spacings,
            "nuclear_profiles": profiles,
            "softening_multipliers": multipliers,
            "counterterm_strengths": counterterms,
            "helium_guard_band": float(args.helium_guard_band),
            "min_hydrogen_improvement": float(args.min_hydrogen_improvement),
        },
        "candidate_count": len(rows),
        "top_candidates": sorted(rows, key=_rank_key)[: int(args.top_k)],
        "top_guardrail_candidates": sorted(guardrail_rows, key=_rank_key)[: int(args.top_k)],
        "promoted_candidates": sorted(promoted_rows, key=_rank_key)[: int(args.top_k)],
        "best_by_hydrogen_under_guardrail": (
            min(guardrail_rows, key=_rank_key) if guardrail_rows else None
        ),
        "best_by_hydrogen_priority": min(rows, key=_rank_key),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body Hydrogen-Priority Search")
    print("========================================")
    print(f"- Promoted candidates: {len(promoted_rows)}.")
    best_row = output_payload["best_by_hydrogen_under_guardrail"]
    if best_row is None:
        print("- No family met the hydrogen-priority and He+ guardrail together.")
    else:
        print(
            f"- Best guardrail family: "
            f"{best_row['parameters']['kinetic_stencil']} "
            f"{best_row['parameters']['nuclear_profile']} "
            f"H={best_row['metrics']['relative_errors']['hydrogen_ground']:.4%} "
            f"He+={best_row['metrics']['relative_errors']['helium_ion_ground']:.4%}."
        )
    print(f"- Wrote search output to {args.write_json}.")


if __name__ == "__main__":
    main()
