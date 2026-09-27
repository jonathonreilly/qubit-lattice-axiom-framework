#!/usr/bin/env python3
"""Broader one-body family search aimed at hydrogen improvement."""

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

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, write_json  # noqa: E402
from scripts.atomic_one_body_runtime import benchmark_one_body_candidate  # noqa: E402


def _search_key(row: dict[str, Any]) -> tuple[float, float, float]:
    scores = row["metrics"]["scores"]
    errors = row["metrics"]["relative_errors"]
    return (
        float(scores["one_body_rms_relative_error"]),
        float(scores["max_relative_error"]),
        float(errors["hydrogen_ground"]),
    )


def _with_guardrails(row: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    output = dict(row)
    scores = output["metrics"]["scores"]
    errors = output["metrics"]["relative_errors"]
    baseline_scores = baseline["metrics"]["scores"]
    baseline_errors = baseline["metrics"]["relative_errors"]
    output["guardrails"] = {
        "hydrogen_improves": float(errors["hydrogen_ground"])
        < float(baseline_errors["hydrogen_ground"]),
        "helium_ion_improves": float(errors["helium_ion_ground"])
        < float(baseline_errors["helium_ion_ground"]),
        "one_body_rms_improves": float(scores["one_body_rms_relative_error"])
        < float(baseline_scores["one_body_rms_relative_error"]),
        "physically_bound": bool(output["hydrogen_ground_orbital"]["physical_bound"])
        and bool(output["helium_ion_ground_orbital"]["physical_bound"]),
    }
    output["improvement_vs_baseline"] = {
        "hydrogen_ground_delta": float(errors["hydrogen_ground"])
        - float(baseline_errors["hydrogen_ground"]),
        "helium_ion_ground_delta": float(errors["helium_ion_ground"])
        - float(baseline_errors["helium_ion_ground"]),
        "one_body_rms_relative_error_delta": float(scores["one_body_rms_relative_error"])
        - float(baseline_scores["one_body_rms_relative_error"]),
        "max_relative_error_delta": float(scores["max_relative_error"])
        - float(baseline_scores["max_relative_error"]),
    }
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-coupling", type=float, default=1.595)
    parser.add_argument(
        "--kinetic-stencils",
        nargs="*",
        default=("three_point", "five_point"),
        choices=("three_point", "five_point"),
    )
    parser.add_argument(
        "--lattice-spacings",
        type=float,
        nargs="*",
        default=(1.0, 0.8),
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=("hard_floor", "erf_softcore", "exp_softcore", "shifted"),
        choices=("hard_floor", "plummer", "shifted", "erf_softcore", "exp_softcore"),
    )
    parser.add_argument(
        "--softening-multipliers",
        type=float,
        nargs="*",
        default=(0.5, 0.75, 1.0),
    )
    parser.add_argument(
        "--counterterm-strengths",
        type=float,
        nargs="*",
        default=(0.0, 0.1, 0.2),
    )
    parser.add_argument("--n-eig", type=int, default=40)
    parser.add_argument("--max-orbitals", type=int, default=16)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_family_search.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    baseline = benchmark_one_body_candidate(
        reference_coupling=float(args.reference_coupling),
        lattice_spacing=1.0,
        softening_multiplier=0.75,
        nuclear_profile="hard_floor",
        kinetic_stencil="three_point",
        max_orbitals=int(args.max_orbitals),
        n_eig=int(args.n_eig),
    )
    rows = []
    stencils = [str(value) for value in args.kinetic_stencils]
    spacings = [float(value) for value in args.lattice_spacings]
    profiles = [str(value) for value in args.nuclear_profiles]
    multipliers = [float(value) for value in args.softening_multipliers]
    counterterms = [float(value) for value in args.counterterm_strengths]
    total_points = len(stencils) * len(spacings) * len(profiles) * len(multipliers) * len(counterterms)
    current_index = 0
    for kinetic_stencil in stencils:
        for lattice_spacing in spacings:
            for nuclear_profile in profiles:
                for softening_multiplier in multipliers:
                    for counterterm_strength in counterterms:
                        current_index += 1
                        scan_started = time.perf_counter()
                        benchmark = benchmark_one_body_candidate(
                            reference_coupling=float(args.reference_coupling),
                            lattice_spacing=float(lattice_spacing),
                            softening_multiplier=float(softening_multiplier),
                            nuclear_profile=str(nuclear_profile),
                            nuclear_counterterm_strength=float(counterterm_strength),
                            kinetic_stencil=str(kinetic_stencil),
                            max_orbitals=int(args.max_orbitals),
                            n_eig=int(args.n_eig),
                        )
                        benchmark["elapsed_seconds"] = round(
                            time.perf_counter() - scan_started,
                            6,
                        )
                        row = _with_guardrails(benchmark, baseline)
                        rows.append(row)
                        print(
                            f"[{current_index}/{total_points}] "
                            f"stencil={kinetic_stencil} a={lattice_spacing:.3f} "
                            f"p={nuclear_profile} m={softening_multiplier:.2f} "
                            f"ct={counterterm_strength:.2f} "
                            f"H={row['metrics']['relative_errors']['hydrogen_ground']:.4%} "
                            f"He+={row['metrics']['relative_errors']['helium_ion_ground']:.4%} "
                            f"rms={row['metrics']['scores']['one_body_rms_relative_error']:.6f}",
                            flush=True,
                        )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "baseline_candidate": baseline,
        "candidate_count": len(rows),
        "top_candidates": sorted(rows, key=_search_key)[:20],
        "best_by_one_body_rms": min(rows, key=_search_key),
        "hydrogen_best_candidate": min(
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
    print("Atomic One-Body Family Search")
    print("=============================")
    print(
        f"- Best by RMS: "
        f"{output_payload['best_by_one_body_rms']['parameters']['kinetic_stencil']} "
        f"{output_payload['best_by_one_body_rms']['parameters']['nuclear_profile']} "
        f"full one-body RMS="
        f"{output_payload['best_by_one_body_rms']['metrics']['scores']['one_body_rms_relative_error']:.6f}."
    )
    print(
        f"- Best hydrogen candidate error: "
        f"{output_payload['hydrogen_best_candidate']['metrics']['relative_errors']['hydrogen_ground']:.4%}."
    )
    print(f"- Wrote family search output to {args.write_json}.")


if __name__ == "__main__":
    main()
