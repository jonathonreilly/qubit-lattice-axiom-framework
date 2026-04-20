#!/usr/bin/env python3
"""Search one-body UV/discretization candidates for H and He+."""

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


def _with_gates(
    benchmark: dict[str, Any],
    baseline: dict[str, Any],
) -> dict[str, Any]:
    row = dict(benchmark)
    errors = row["metrics"]["relative_errors"]
    scores = row["metrics"]["scores"]
    baseline_errors = baseline["metrics"]["relative_errors"]
    baseline_scores = baseline["metrics"]["scores"]
    hydrogen_improves = float(errors["hydrogen_ground"]) < float(
        baseline_errors["hydrogen_ground"]
    )
    helium_ion_improves = float(errors["helium_ion_ground"]) < float(
        baseline_errors["helium_ion_ground"]
    )
    score_improves = (
        float(scores["one_body_rms_relative_error"])
        < float(baseline_scores["one_body_rms_relative_error"])
        and float(scores["max_relative_error"])
        <= float(baseline_scores["max_relative_error"])
    )
    physically_bound = bool(row["hydrogen_ground_orbital"]["physical_bound"]) and bool(
        row["helium_ion_ground_orbital"]["physical_bound"]
    )
    row["guardrails"] = {
        "hydrogen_improves": bool(hydrogen_improves),
        "helium_ion_improves": bool(helium_ion_improves),
        "score_improves": bool(score_improves),
        "physically_bound": bool(physically_bound),
        "eligible_for_promotion": bool(
            hydrogen_improves and helium_ion_improves and score_improves and physically_bound
        ),
    }
    row["improvement_vs_baseline"] = {
        "hydrogen_ground_delta": float(errors["hydrogen_ground"])
        - float(baseline_errors["hydrogen_ground"]),
        "helium_ion_ground_delta": float(errors["helium_ion_ground"])
        - float(baseline_errors["helium_ion_ground"]),
        "one_body_rms_relative_error_delta": float(scores["one_body_rms_relative_error"])
        - float(baseline_scores["one_body_rms_relative_error"]),
        "max_relative_error_delta": float(scores["max_relative_error"])
        - float(baseline_scores["max_relative_error"]),
    }
    return row


def _search_key(row: dict[str, Any]) -> tuple[float, float, float]:
    scores = row["metrics"]["scores"]
    return (
        float(scores["one_body_rms_relative_error"]),
        float(scores["max_relative_error"]),
        float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimension", type=int, default=3)
    parser.add_argument("--reference-coupling", type=float, default=1.595)
    parser.add_argument("--nuclear-charge", type=float, default=2.0)
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
        "--softening-multipliers",
        type=float,
        nargs="*",
        default=(0.5, 0.75, 1.0, 1.25),
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=("hard_floor",),
        choices=("hard_floor", "plummer", "shifted", "erf_softcore", "exp_softcore"),
    )
    parser.add_argument("--nuclear-quadrature-order", type=int, default=1)
    parser.add_argument("--nuclear-counterterm-strength", type=float, default=0.0)
    parser.add_argument("--nuclear-counterterm-radius", type=float)
    parser.add_argument("--max-orbitals", type=int, default=16)
    parser.add_argument("--n-eig", type=int, default=40)
    parser.add_argument("--reference-spacing", type=float, default=1.0)
    parser.add_argument("--reference-sizes", type=int, nargs="*")
    parser.add_argument("--min-size", type=int, default=8)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_uv_search.json",
    )
    args = parser.parse_args()

    reference_sizes = (
        tuple(int(value) for value in args.reference_sizes)
        if args.reference_sizes
        else None
    )
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    baseline = benchmark_one_body_candidate(
        dimension=int(args.dimension),
        reference_coupling=float(args.reference_coupling),
        nuclear_charge=float(args.nuclear_charge),
        lattice_spacing=1.0,
        softening_multiplier=0.75,
        nuclear_profile="hard_floor",
        nuclear_quadrature_order=1,
        kinetic_stencil="three_point",
        max_orbitals=int(args.max_orbitals),
        n_eig=int(args.n_eig),
        fixed_physical_box=True,
        reference_spacing=float(args.reference_spacing),
        reference_sizes=reference_sizes,
        min_size=int(args.min_size),
    )

    rows: list[dict[str, Any]] = []
    stencils = [str(value) for value in args.kinetic_stencils]
    spacings = [float(value) for value in args.lattice_spacings]
    multipliers = [float(value) for value in args.softening_multipliers]
    profiles = [str(value) for value in args.nuclear_profiles]
    total_points = len(stencils) * len(spacings) * len(multipliers) * len(profiles)
    current_index = 0
    for kinetic_stencil in stencils:
        for lattice_spacing in spacings:
            for softening_multiplier in multipliers:
                for nuclear_profile in profiles:
                    current_index += 1
                    scan_started = time.perf_counter()
                    benchmark = benchmark_one_body_candidate(
                        dimension=int(args.dimension),
                        reference_coupling=float(args.reference_coupling),
                        nuclear_charge=float(args.nuclear_charge),
                        lattice_spacing=float(lattice_spacing),
                        softening_multiplier=float(softening_multiplier),
                        nuclear_profile=nuclear_profile,
                        nuclear_quadrature_order=int(args.nuclear_quadrature_order),
                        nuclear_counterterm_strength=float(
                            args.nuclear_counterterm_strength
                        ),
                        nuclear_counterterm_radius=args.nuclear_counterterm_radius,
                        kinetic_stencil=kinetic_stencil,
                        max_orbitals=int(args.max_orbitals),
                        n_eig=int(args.n_eig),
                        fixed_physical_box=True,
                        reference_spacing=float(args.reference_spacing),
                        reference_sizes=reference_sizes,
                        min_size=int(args.min_size),
                    )
                    benchmark["elapsed_seconds"] = round(
                        time.perf_counter() - scan_started,
                        6,
                    )
                    row = _with_gates(benchmark, baseline)
                    rows.append(row)
                    print(
                        f"[{current_index}/{total_points}] "
                        f"stencil={kinetic_stencil} a={lattice_spacing:.4f} "
                        f"m={softening_multiplier:.4f} p={nuclear_profile} "
                        f"H={row['metrics']['relative_errors']['hydrogen_ground']:.4%} "
                        f"He+={row['metrics']['relative_errors']['helium_ion_ground']:.4%} "
                        f"rms={row['metrics']['scores']['one_body_rms_relative_error']:.6f}",
                        flush=True,
                    )

    promoted = [row for row in rows if row["guardrails"]["eligible_for_promotion"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "baseline_candidate": baseline,
        "scan_configuration": {
            "kinetic_stencils": stencils,
            "lattice_spacings": spacings,
            "softening_multipliers": multipliers,
            "nuclear_profiles": profiles,
            "reference_coupling": float(args.reference_coupling),
            "reference_spacing": float(args.reference_spacing),
            "reference_sizes": (
                [int(size) for size in reference_sizes]
                if reference_sizes is not None
                else None
            ),
        },
        "candidate_count": len(rows),
        "top_candidates": sorted(rows, key=_search_key)[:15],
        "best_by_one_body_rms": min(rows, key=_search_key),
        "promoted_candidate": min(promoted, key=_search_key) if promoted else None,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body UV Search")
    print("=========================")
    if output_payload["promoted_candidate"] is None:
        print("- No candidate cleared the promotion gates.")
    else:
        promoted_candidate = output_payload["promoted_candidate"]
        print(
            f"- Promoted candidate: stencil={promoted_candidate['parameters']['kinetic_stencil']} "
            f"a={promoted_candidate['parameters']['lattice_spacing']:.4f} "
            f"m={promoted_candidate['parameters']['softening_multiplier']:.4f}."
        )
    print(f"- Wrote search output to {args.write_json}.")


if __name__ == "__main__":
    main()
