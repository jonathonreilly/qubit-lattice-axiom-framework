#!/usr/bin/env python3
"""Search virtual-orbital basis upgrades for the retained atomic lane."""

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
from scripts.atomic_observable_metrics import (  # noqa: E402
    ACTUALS_HARTREE,
    candidate_metrics,
)
from scripts.atomic_two_body_runtime import solve_two_electron_atomic_model  # noqa: E402


def summarize_candidate(solution: dict[str, Any]) -> dict[str, Any]:
    model = solution["model"]
    return {
        "parameters": {
            "reference_coupling": float(model["reference_coupling"]),
            "lattice_spacing": float(model["lattice_spacing"]),
            "nuclear_softening_radius": float(model["nuclear_softening_radius"]),
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "nuclear_profile": str(model["nuclear_profile"]),
            "repulsion_profile": str(model["repulsion_profile"]),
            "max_orbitals": int(model["max_orbitals"]),
            "max_virtual_orbitals": int(model["max_virtual_orbitals"]),
            "n_eig": int(model["n_eig"]),
        },
        "metrics": candidate_metrics(solution),
        "spin_ground_sector": str(solution["two_electron"]["spin_ground_sector"]),
        "helium_like_bound": bool(solution["two_electron"]["helium_like_bound"]),
        "negative_orbital_count": int(solution["helium_ion_reference"]["n_negative_selected"]),
        "virtual_orbital_count": int(solution["helium_ion_reference"]["n_virtual_selected"]),
    }


def full_rms_key(summary: dict[str, Any]) -> tuple[float, float, float]:
    scores = summary["metrics"]["scores"]
    return (
        float(scores["full_rms_relative_error"]),
        float(scores["max_relative_error"]),
        float(scores["one_body_rms_relative_error"]),
    )


def helium_key(summary: dict[str, Any]) -> tuple[float, float, float]:
    scores = summary["metrics"]["scores"]
    return (
        float(scores["helium_rms_relative_error"]),
        float(scores["full_rms_relative_error"]),
        float(scores["max_relative_error"]),
    )


def _with_guardrails(
    summary: dict[str, Any],
    baseline_summary: dict[str, Any],
    *,
    full_rms_slack: float,
    helium_rms_slack: float,
) -> dict[str, Any]:
    row = dict(summary)
    scores = row["metrics"]["scores"]
    baseline_scores = baseline_summary["metrics"]["scores"]
    eligible = (
        row["spin_ground_sector"] == "singlet"
        and bool(row["helium_like_bound"])
        and float(scores["full_rms_relative_error"])
        <= float(baseline_scores["full_rms_relative_error"]) * (1.0 + full_rms_slack)
        and float(scores["helium_rms_relative_error"])
        <= float(baseline_scores["helium_rms_relative_error"])
        * (1.0 + helium_rms_slack)
    )
    row["guardrails"] = {
        "eligible_for_balanced_selection": bool(eligible),
        "baseline_full_rms_relative_error": float(
            baseline_scores["full_rms_relative_error"]
        ),
        "baseline_helium_rms_relative_error": float(
            baseline_scores["helium_rms_relative_error"]
        ),
        "full_rms_slack": float(full_rms_slack),
        "helium_rms_slack": float(helium_rms_slack),
    }
    return row


def unique_parameter_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in rows:
        params = row["parameters"]
        key = (
            int(params["max_virtual_orbitals"]),
            int(params["n_eig"]),
            int(params["max_orbitals"]),
        )
        incumbent = by_key.get(key)
        if incumbent is None or full_rms_key(row) < full_rms_key(incumbent):
            by_key[key] = row
    return list(by_key.values())


def solve_candidate(
    *,
    reference_coupling: float,
    lattice_spacing: float,
    nuclear_softening_radius: float,
    repulsion_softening_radius: float,
    max_orbitals: int,
    max_virtual_orbitals: int,
    n_eig: int,
) -> dict[str, Any]:
    total_spatial = int(max_orbitals) + int(max_virtual_orbitals)
    basis_sweep = tuple(
        size
        for size in (4, 6, 8, 10, 12, 14, 16, 18, 20, total_spatial)
        if 0 < size <= total_spatial
    )
    return solve_two_electron_atomic_model(
        reference_coupling=reference_coupling,
        lattice_spacing=lattice_spacing,
        nuclear_softening_radius=nuclear_softening_radius,
        repulsion_softening_radius=repulsion_softening_radius,
        nuclear_profile="hard_floor",
        repulsion_profile="hard_floor",
        max_orbitals=max_orbitals,
        max_virtual_orbitals=max_virtual_orbitals,
        n_eig=n_eig,
        basis_sweep=basis_sweep,
    )


def improvement_vs_baseline(
    candidate: dict[str, Any],
    baseline: dict[str, Any],
) -> dict[str, float]:
    candidate_errors = candidate["metrics"]["relative_errors"]
    baseline_errors = baseline["metrics"]["relative_errors"]
    candidate_scores = candidate["metrics"]["scores"]
    baseline_scores = baseline["metrics"]["scores"]
    return {
        "helium_rms_relative_error_delta": float(
            candidate_scores["helium_rms_relative_error"]
        )
        - float(baseline_scores["helium_rms_relative_error"]),
        "full_rms_relative_error_delta": float(
            candidate_scores["full_rms_relative_error"]
        )
        - float(baseline_scores["full_rms_relative_error"]),
        "helium_ground_error_delta": float(candidate_errors["helium_ground"])
        - float(baseline_errors["helium_ground"]),
        "helium_ionization_error_delta": float(candidate_errors["helium_ionization"])
        - float(baseline_errors["helium_ionization"]),
        "helium_triplet_error_delta": float(candidate_errors["helium_triplet"])
        - float(baseline_errors["helium_triplet"]),
        "singlet_triplet_gap_error_delta": float(candidate_errors["singlet_triplet_gap"])
        - float(baseline_errors["singlet_triplet_gap"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference-coupling",
        type=float,
        default=1.595,
        help="baseline UV-best coupling",
    )
    parser.add_argument(
        "--nuclear-softening-radius",
        type=float,
        default=0.75,
        help="baseline UV-best nuclear softening radius",
    )
    parser.add_argument(
        "--repulsion-softening-radius",
        type=float,
        default=1.10,
        help="baseline UV-best e-e softening radius",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used throughout the virtual-basis search",
    )
    parser.add_argument(
        "--max-orbitals",
        type=int,
        default=16,
        help="number of negative one-body orbitals kept in the reduced basis",
    )
    parser.add_argument(
        "--max-virtual-orbital-options",
        type=int,
        nargs="*",
        default=(0, 2, 4, 6, 8),
        help="virtual-orbital counts to test",
    )
    parser.add_argument(
        "--n-eig-options",
        type=int,
        nargs="*",
        default=(40, 56, 72),
        help="eigensolve depths to test when virtual orbitals are requested",
    )
    parser.add_argument(
        "--full-rms-slack",
        type=float,
        default=0.20,
        help="allowable fractional worsening vs the baseline full RMS score",
    )
    parser.add_argument(
        "--helium-rms-slack",
        type=float,
        default=0.35,
        help="allowable fractional worsening vs the baseline helium RMS score",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_virtual_basis_search.json",
        help="machine-readable virtual-basis search output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()

    baseline_solution = solve_candidate(
        reference_coupling=float(args.reference_coupling),
        lattice_spacing=float(args.lattice_spacing),
        nuclear_softening_radius=float(args.nuclear_softening_radius),
        repulsion_softening_radius=float(args.repulsion_softening_radius),
        max_orbitals=int(args.max_orbitals),
        max_virtual_orbitals=0,
        n_eig=max(int(value) for value in args.n_eig_options),
    )
    baseline_summary = summarize_candidate(baseline_solution)

    virtual_options = [int(value) for value in args.max_virtual_orbital_options]
    n_eig_options = [int(value) for value in args.n_eig_options]
    coarse_rows: list[dict[str, Any]] = []
    total_points = len(virtual_options) * len(n_eig_options)
    current_index = 0

    for max_virtual_orbitals in virtual_options:
        for n_eig in n_eig_options:
            if max_virtual_orbitals == 0 and n_eig != max(n_eig_options):
                continue
            current_index += 1
            scan_started = time.perf_counter()
            solution = solve_candidate(
                reference_coupling=float(args.reference_coupling),
                lattice_spacing=float(args.lattice_spacing),
                nuclear_softening_radius=float(args.nuclear_softening_radius),
                repulsion_softening_radius=float(args.repulsion_softening_radius),
                max_orbitals=int(args.max_orbitals),
                max_virtual_orbitals=max_virtual_orbitals,
                n_eig=n_eig,
            )
            summary = summarize_candidate(solution)
            summary["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            coarse_rows.append(summary)
            print(
                f"[{current_index}/{total_points}] "
                f"virt={max_virtual_orbitals} "
                f"n_eig={n_eig} "
                f"spatial={summary['negative_orbital_count'] + summary['virtual_orbital_count']} "
                f"full={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
                f"He={summary['metrics']['model_observables']['helium_ground_magnitude']:.6f} "
                f"I={summary['metrics']['model_observables']['helium_ionization_energy']:.6f}",
                flush=True,
            )

    unique_rows = unique_parameter_rows(coarse_rows)
    guarded_rows = [
        _with_guardrails(
            row,
            baseline_summary,
            full_rms_slack=float(args.full_rms_slack),
            helium_rms_slack=float(args.helium_rms_slack),
        )
        for row in unique_rows
    ]
    best_by_full = min(guarded_rows, key=full_rms_key)
    best_by_helium = min(guarded_rows, key=helium_key)

    selected_final_candidate = dict(best_by_full)
    selected_final_candidate["improvement_vs_baseline"] = improvement_vs_baseline(
        selected_final_candidate,
        baseline_summary,
    )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "actuals_hartree": ACTUALS_HARTREE,
        "baseline_candidate": baseline_summary,
        "scan_configuration": {
            "reference_coupling": float(args.reference_coupling),
            "nuclear_softening_radius": float(args.nuclear_softening_radius),
            "repulsion_softening_radius": float(args.repulsion_softening_radius),
            "lattice_spacing": float(args.lattice_spacing),
            "max_orbitals": int(args.max_orbitals),
            "max_virtual_orbital_options": virtual_options,
            "n_eig_options": n_eig_options,
            "full_rms_slack": float(args.full_rms_slack),
            "helium_rms_slack": float(args.helium_rms_slack),
        },
        "candidate_count": len(unique_rows),
        "top_candidates": sorted(guarded_rows, key=full_rms_key)[:15],
        "best_by_full_rms": best_by_full,
        "best_by_helium_rms": best_by_helium,
        "selected_final_candidate": selected_final_candidate,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    scores = selected_final_candidate["metrics"]["scores"]
    errors = selected_final_candidate["metrics"]["relative_errors"]
    print()
    print("Atomic Virtual-Basis Search")
    print("===========================")
    print(
        f"- Selected candidate: "
        f"virt={selected_final_candidate['parameters']['max_virtual_orbitals']} "
        f"n_eig={selected_final_candidate['parameters']['n_eig']}."
    )
    print(
        f"- Final relative errors: "
        f"He={errors['helium_ground']:.4f}, "
        f"I={errors['helium_ionization']:.4f}, "
        f"triplet={errors['helium_triplet']:.4f}, "
        f"gap={errors['singlet_triplet_gap']:.4f}."
    )
    print(
        f"- Final RMS scores: full={scores['full_rms_relative_error']:.4f}, "
        f"helium={scores['helium_rms_relative_error']:.4f}."
    )
    print(f"- Wrote search output to {args.write_json}.")


if __name__ == "__main__":
    main()
