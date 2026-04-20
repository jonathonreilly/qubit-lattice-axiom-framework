#!/usr/bin/env python3
"""Search one-body families in the local neighborhood of the retained shell baseline."""

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
        float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
        float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
    )


def _baseline_model(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return dict(payload["accepted_candidate"]["solution"]["model"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--kinetic-stencils",
        nargs="*",
        default=("five_point", "seven_point"),
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=("hard_floor", "tanh_softcore", "gaussian_floor", "erf_softcore"),
    )
    parser.add_argument(
        "--softening-multipliers",
        type=float,
        nargs="*",
        default=(0.65, 0.75, 0.85),
    )
    parser.add_argument(
        "--counterterm-strengths",
        type=float,
        nargs="*",
        default=(-0.10, -0.05, 0.0, 0.05, 0.10),
    )
    parser.add_argument(
        "--counterterm-radius-scales",
        type=float,
        nargs="*",
        default=(0.75, 1.0),
    )
    parser.add_argument("--helium-guard-band", type=float, default=0.01)
    parser.add_argument("--min-hydrogen-improvement", type=float, default=0.002)
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_family_search.json",
    )
    args = parser.parse_args()

    baseline_payload = read_json(args.baseline_readout_json)
    baseline_model = _baseline_model(args.baseline_readout_json)
    baseline_metrics = baseline_payload["accuracy_metrics"]
    baseline_h_error = float(baseline_metrics["relative_errors"]["hydrogen_ground"])
    baseline_he_error = float(baseline_metrics["relative_errors"]["helium_ion_ground"])
    baseline_rms = float(baseline_metrics["scores"]["one_body_rms_relative_error"])
    baseline_sizes = tuple(int(size) for size in baseline_model["custom_sizes"])

    stencils = [str(value) for value in args.kinetic_stencils]
    profiles = [str(value) for value in args.nuclear_profiles]
    multipliers = [float(value) for value in args.softening_multipliers]
    counterterm_strengths = [float(value) for value in args.counterterm_strengths]
    radius_scales = [float(value) for value in args.counterterm_radius_scales]

    total_points = 0
    for _stencil in stencils:
        for _profile in profiles:
            for _mult in multipliers:
                for strength in counterterm_strengths:
                    total_points += 1 if strength == 0.0 else len(radius_scales)

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    current_index = 0
    for kinetic_stencil in stencils:
        for nuclear_profile in profiles:
            for softening_multiplier in multipliers:
                softening_radius = (
                    float(softening_multiplier) * float(baseline_model["lattice_spacing"])
                )
                for counterterm_strength in counterterm_strengths:
                    active_radius_scales = [1.0] if counterterm_strength == 0.0 else radius_scales
                    for radius_scale in active_radius_scales:
                        current_index += 1
                        scan_started = time.perf_counter()
                        counterterm_radius = (
                            None
                            if counterterm_strength == 0.0
                            else float(radius_scale) * float(softening_radius)
                        )
                        benchmark = benchmark_one_body_candidate(
                            dimension=int(baseline_model["dimension"]),
                            reference_coupling=float(baseline_model["reference_coupling"]),
                            nuclear_charge=float(baseline_model["nuclear_charge"]),
                            lattice_spacing=float(baseline_model["lattice_spacing"]),
                            softening_radius=float(softening_radius),
                            softening_multiplier=float(softening_multiplier),
                            nuclear_profile=str(nuclear_profile),
                            nuclear_quadrature_order=int(baseline_model["nuclear_quadrature_order"]),
                            nuclear_counterterm_strength=float(counterterm_strength),
                            nuclear_counterterm_radius=counterterm_radius,
                            kinetic_stencil=str(kinetic_stencil),
                            max_orbitals=int(baseline_model["max_orbitals"]),
                            n_eig=int(baseline_model["n_eig"]),
                            custom_sizes=baseline_sizes,
                            fixed_physical_box=False,
                        )
                        benchmark["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
                        errors = benchmark["metrics"]["relative_errors"]
                        scores = benchmark["metrics"]["scores"]
                        hydrogen_error = float(errors["hydrogen_ground"])
                        helium_error = float(errors["helium_ion_ground"])
                        row = dict(benchmark)
                        row["guardrails"] = {
                            "hydrogen_improves": hydrogen_error
                            <= baseline_h_error - float(args.min_hydrogen_improvement),
                            "helium_ion_guardrail_pass": helium_error
                            <= baseline_he_error + float(args.helium_guard_band),
                            "one_body_rms_improves": float(scores["one_body_rms_relative_error"])
                            < baseline_rms,
                            "physically_bound": bool(
                                benchmark["hydrogen_ground_orbital"]["physical_bound"]
                                and benchmark["helium_ion_ground_orbital"]["physical_bound"]
                            ),
                        }
                        row["improvement_vs_baseline"] = {
                            "hydrogen_ground_delta": hydrogen_error - baseline_h_error,
                            "helium_ion_ground_delta": helium_error - baseline_he_error,
                            "one_body_rms_relative_error_delta": (
                                float(scores["one_body_rms_relative_error"]) - baseline_rms
                            ),
                        }
                        row["promoted"] = bool(
                            row["guardrails"]["hydrogen_improves"]
                            and row["guardrails"]["helium_ion_guardrail_pass"]
                            and row["guardrails"]["one_body_rms_improves"]
                            and row["guardrails"]["physically_bound"]
                        )
                        rows.append(row)
                        print(
                            f"[{current_index}/{total_points}] "
                            f"stencil={kinetic_stencil} profile={nuclear_profile} "
                            f"m={softening_multiplier:.2f} "
                            f"ct={counterterm_strength:+.2f} "
                            f"rs={radius_scale:.2f} "
                            f"H={hydrogen_error:.4%} He+={helium_error:.4%} "
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
            "hydrogen_ground_error": baseline_h_error,
            "helium_ion_ground_error": baseline_he_error,
            "one_body_rms_relative_error": baseline_rms,
        },
        "search_configuration": {
            "kinetic_stencils": stencils,
            "nuclear_profiles": profiles,
            "softening_multipliers": multipliers,
            "counterterm_strengths": counterterm_strengths,
            "counterterm_radius_scales": radius_scales,
            "helium_guard_band": float(args.helium_guard_band),
            "min_hydrogen_improvement": float(args.min_hydrogen_improvement),
            "baseline_sizes": [int(size) for size in baseline_sizes],
        },
        "candidate_count": len(rows),
        "top_candidates": sorted(rows, key=_rank_key)[: int(args.top_k)],
        "top_guardrail_candidates": sorted(guardrail_rows, key=_rank_key)[: int(args.top_k)],
        "promoted_candidates": sorted(promoted_rows, key=_rank_key)[: int(args.top_k)],
        "best_by_one_body_rms": min(rows, key=_rank_key),
        "best_by_hydrogen_under_guardrail": (
            min(guardrail_rows, key=lambda row: (
                float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
                float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ))
            if guardrail_rows
            else None
        ),
        "best_by_hydrogen_priority": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
                float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell One-Body Family Search")
    print("===================================")
    print(f"- Promoted candidates: {len(promoted_rows)}.")
    best = output_payload["best_by_hydrogen_under_guardrail"]
    if best is None:
        print("- No family improved hydrogen under the He+ guardrail.")
    else:
        print(
            f"- Best guardrail family: "
            f"{best['parameters']['kinetic_stencil']} "
            f"{best['parameters']['nuclear_profile']} "
            f"H={best['metrics']['relative_errors']['hydrogen_ground']:.4%} "
            f"He+={best['metrics']['relative_errors']['helium_ion_ground']:.4%}."
        )
    print(f"- Wrote search output to {args.write_json}.")


if __name__ == "__main__":
    main()
