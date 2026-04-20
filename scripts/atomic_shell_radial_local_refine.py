#!/usr/bin/env python3
"""Locally refine the retained shell-radial one-body family."""

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
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_radial.json",
    )
    parser.add_argument(
        "--coupling-offsets",
        type=float,
        nargs="*",
        default=(-0.02, -0.01, 0.0, 0.01, 0.02),
    )
    parser.add_argument(
        "--counterterm-offsets",
        type=float,
        nargs="*",
        default=(-0.05, -0.025, 0.0, 0.025, 0.05),
    )
    parser.add_argument(
        "--shell-strength-offsets",
        type=float,
        nargs="*",
        default=(-0.02, -0.01, 0.0, 0.01, 0.02),
    )
    parser.add_argument(
        "--shell-radius-offsets",
        type=float,
        nargs="*",
        default=(-0.2, -0.1, 0.0, 0.1, 0.2),
    )
    parser.add_argument(
        "--shell-width-offsets",
        type=float,
        nargs="*",
        default=(-0.08, -0.04, 0.0, 0.04, 0.08),
    )
    parser.add_argument("--hydrogen-guard-band", type=float, default=0.004)
    parser.add_argument("--helium-guard-band", type=float, default=0.004)
    parser.add_argument("--min-material-improvement", type=float, default=1.0e-4)
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_radial_local_refine.json",
    )
    args = parser.parse_args()

    baseline_payload = read_json(args.baseline_readout_json)
    baseline_model = _baseline_model(args.baseline_readout_json)
    baseline_metrics = baseline_payload["accuracy_metrics"]
    baseline_h_error = float(baseline_metrics["relative_errors"]["hydrogen_ground"])
    baseline_he_error = float(baseline_metrics["relative_errors"]["helium_ion_ground"])
    baseline_rms = float(baseline_metrics["scores"]["one_body_rms_relative_error"])
    baseline_max = float(baseline_metrics["scores"]["max_relative_error"])
    baseline_sizes = tuple(int(size) for size in baseline_model["custom_sizes"])

    coupling_offsets = [float(value) for value in args.coupling_offsets]
    counterterm_offsets = [float(value) for value in args.counterterm_offsets]
    shell_strength_offsets = [float(value) for value in args.shell_strength_offsets]
    shell_radius_offsets = [float(value) for value in args.shell_radius_offsets]
    shell_width_offsets = [float(value) for value in args.shell_width_offsets]

    total_points = (
        len(coupling_offsets)
        * len(counterterm_offsets)
        * len(shell_strength_offsets)
        * len(shell_radius_offsets)
        * len(shell_width_offsets)
    )

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    current_index = 0
    base_coupling = float(baseline_model["reference_coupling"])
    base_counterterm = float(baseline_model["nuclear_counterterm_strength"])
    base_shell_strength = float(baseline_model["nuclear_shell_strength"])
    base_shell_radius = float(baseline_model["nuclear_shell_radius"])
    base_shell_width = float(baseline_model["nuclear_shell_width"])
    for coupling_offset in coupling_offsets:
        reference_coupling = base_coupling + float(coupling_offset)
        for counterterm_offset in counterterm_offsets:
            counterterm_strength = base_counterterm + float(counterterm_offset)
            for shell_strength_offset in shell_strength_offsets:
                shell_strength = base_shell_strength + float(shell_strength_offset)
                for shell_radius_offset in shell_radius_offsets:
                    shell_radius = max(
                        1.0e-3,
                        base_shell_radius + float(shell_radius_offset),
                    )
                    for shell_width_offset in shell_width_offsets:
                        current_index += 1
                        scan_started = time.perf_counter()
                        shell_width = max(
                            1.0e-3,
                            base_shell_width + float(shell_width_offset),
                        )
                        benchmark = benchmark_one_body_candidate(
                            dimension=int(baseline_model["dimension"]),
                            reference_coupling=float(reference_coupling),
                            nuclear_charge=float(baseline_model["nuclear_charge"]),
                            lattice_spacing=float(baseline_model["lattice_spacing"]),
                            softening_radius=float(baseline_model["nuclear_softening_radius"]),
                            softening_multiplier=float(
                                baseline_model["nuclear_softening_radius"]
                                / baseline_model["lattice_spacing"]
                            ),
                            nuclear_profile=str(baseline_model["nuclear_profile"]),
                            nuclear_quadrature_order=int(
                                baseline_model["nuclear_quadrature_order"]
                            ),
                            nuclear_counterterm_strength=float(counterterm_strength),
                            nuclear_counterterm_radius=baseline_model["nuclear_counterterm_radius"],
                            nuclear_shell_strength=float(shell_strength),
                            nuclear_shell_radius=float(shell_radius),
                            nuclear_shell_width=float(shell_width),
                            kinetic_stencil=str(baseline_model["kinetic_stencil"]),
                            max_orbitals=int(baseline_model["max_orbitals"]),
                            n_eig=int(baseline_model["n_eig"]),
                            custom_sizes=baseline_sizes,
                            fixed_physical_box=False,
                        )
                        benchmark["elapsed_seconds"] = round(
                            time.perf_counter() - scan_started,
                            6,
                        )
                        errors = benchmark["metrics"]["relative_errors"]
                        scores = benchmark["metrics"]["scores"]
                        hydrogen_error = float(errors["hydrogen_ground"])
                        helium_error = float(errors["helium_ion_ground"])
                        row = dict(benchmark)
                        row["guardrails"] = {
                            "hydrogen_guardrail_pass": hydrogen_error
                            <= baseline_h_error + float(args.hydrogen_guard_band),
                            "helium_ion_guardrail_pass": helium_error
                            <= baseline_he_error + float(args.helium_guard_band),
                            "one_body_rms_improves": (
                                float(scores["one_body_rms_relative_error"])
                                < baseline_rms - float(args.min_material_improvement)
                            ),
                            "max_relative_error_improves": (
                                float(scores["max_relative_error"])
                                < baseline_max - float(args.min_material_improvement)
                            ),
                            "physically_bound": bool(
                                benchmark["hydrogen_ground_orbital"]["physical_bound"]
                                and benchmark["helium_ion_ground_orbital"]["physical_bound"]
                            ),
                            "observable_delta_exists": bool(
                                hydrogen_error
                                < baseline_h_error - float(args.min_material_improvement)
                                or helium_error
                                < baseline_he_error - float(args.min_material_improvement)
                            ),
                        }
                        row["improvement_vs_baseline"] = {
                            "hydrogen_ground_delta": hydrogen_error - baseline_h_error,
                            "helium_ion_ground_delta": helium_error - baseline_he_error,
                            "one_body_rms_relative_error_delta": (
                                float(scores["one_body_rms_relative_error"]) - baseline_rms
                            ),
                            "max_relative_error_delta": (
                                float(scores["max_relative_error"]) - baseline_max
                            ),
                        }
                        row["promoted"] = bool(
                            row["guardrails"]["hydrogen_guardrail_pass"]
                            and row["guardrails"]["helium_ion_guardrail_pass"]
                            and row["guardrails"]["one_body_rms_improves"]
                            and row["guardrails"]["max_relative_error_improves"]
                            and row["guardrails"]["physically_bound"]
                            and row["guardrails"]["observable_delta_exists"]
                        )
                        rows.append(row)
                        print(
                            f"[{current_index}/{total_points}] "
                            f"g={reference_coupling:.4f} "
                            f"ct={counterterm_strength:+.3f} "
                            f"shell={shell_strength:+.3f} "
                            f"r={shell_radius:.3f} "
                            f"w={shell_width:.3f} "
                            f"H={hydrogen_error:.4%} "
                            f"He+={helium_error:.4%} "
                            f"rms={scores['one_body_rms_relative_error']:.6f} "
                            f"promoted={'YES' if row['promoted'] else 'NO'}",
                            flush=True,
                        )

    promoted_rows = [row for row in rows if row["promoted"]]
    guardrail_rows = [
        row
        for row in rows
        if row["guardrails"]["hydrogen_guardrail_pass"]
        and row["guardrails"]["helium_ion_guardrail_pass"]
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
            "max_relative_error": baseline_max,
        },
        "search_configuration": {
            "coupling_offsets": coupling_offsets,
            "counterterm_offsets": counterterm_offsets,
            "shell_strength_offsets": shell_strength_offsets,
            "shell_radius_offsets": shell_radius_offsets,
            "shell_width_offsets": shell_width_offsets,
            "hydrogen_guard_band": float(args.hydrogen_guard_band),
            "helium_guard_band": float(args.helium_guard_band),
            "min_material_improvement": float(args.min_material_improvement),
            "baseline_sizes": [int(size) for size in baseline_sizes],
        },
        "candidate_count": len(rows),
        "top_candidates": sorted(rows, key=_rank_key)[: int(args.top_k)],
        "top_guardrail_candidates": sorted(guardrail_rows, key=_rank_key)[: int(args.top_k)],
        "promoted_candidates": sorted(promoted_rows, key=_rank_key)[: int(args.top_k)],
        "selected_final_candidates": sorted(
            promoted_rows or guardrail_rows or rows,
            key=_rank_key,
        )[: int(args.top_k)],
        "best_by_one_body_rms": min(rows, key=_rank_key),
        "best_by_guardrail": (
            min(guardrail_rows, key=_rank_key)
            if guardrail_rows
            else None
        ),
        "best_by_hydrogen_priority": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
                float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        ),
        "best_selected_candidate": min(
            promoted_rows or guardrail_rows or rows,
            key=_rank_key,
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell Radial Local Refine")
    print("================================")
    print(f"- Promoted candidates: {len(promoted_rows)}.")
    best = output_payload["best_selected_candidate"]
    print(
        f"- Best selected candidate: "
        f"g={best['parameters']['reference_coupling']:.4f} "
        f"ct={best['parameters']['nuclear_counterterm_strength']:+.3f} "
        f"shell={best['parameters']['nuclear_shell_strength']:+.3f} "
        f"r={best['parameters']['nuclear_shell_radius']:.3f} "
        f"w={best['parameters']['nuclear_shell_width']:.3f} "
        f"H={best['metrics']['relative_errors']['hydrogen_ground']:.4%} "
        f"He+={best['metrics']['relative_errors']['helium_ion_ground']:.4%}."
    )
    print(f"- Wrote refine output to {args.write_json}.")


if __name__ == "__main__":
    main()
