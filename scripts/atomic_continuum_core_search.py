#!/usr/bin/env python3
"""Search continuum-aware nuclear core models for the retained atomic lane."""

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

from scripts.atomic_coulomb_calibration import (  # noqa: E402
    ACTUALS_HARTREE,
    candidate_metrics,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, write_json  # noqa: E402
from scripts.atomic_two_body_runtime import (  # noqa: E402
    SUPPORTED_NUCLEAR_PROFILES,
    solve_two_electron_atomic_model,
)


def _scan_grid(start: float, stop: float, step: float) -> list[float]:
    values: list[float] = []
    current = start
    while current <= stop + 0.5 * step:
        values.append(round(current, 12))
        current += step
    return values


def summarize_candidate(solution: dict[str, Any]) -> dict[str, Any]:
    model = solution["model"]
    return {
        "parameters": {
            "reference_coupling": float(model["reference_coupling"]),
            "lattice_spacing": float(model["lattice_spacing"]),
            "nuclear_softening_radius": float(model["nuclear_softening_radius"]),
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "nuclear_profile": str(model["nuclear_profile"]),
            "nuclear_quadrature_order": int(model["nuclear_quadrature_order"]),
            "max_orbitals": int(model["max_orbitals"]),
        },
        "metrics": candidate_metrics(solution),
        "spin_ground_sector": str(solution["two_electron"]["spin_ground_sector"]),
        "helium_like_bound": bool(solution["two_electron"]["helium_like_bound"]),
    }


def full_rms_key(summary: dict[str, Any]) -> tuple[float, float, float]:
    scores = summary["metrics"]["scores"]
    return (
        float(scores["full_rms_relative_error"]),
        float(scores["max_relative_error"]),
        float(scores["one_body_rms_relative_error"]),
    )


def hydrogen_key(summary: dict[str, Any]) -> tuple[float, float, float]:
    errors = summary["metrics"]["relative_errors"]
    scores = summary["metrics"]["scores"]
    return (
        float(errors["hydrogen_ground"]),
        float(scores["full_rms_relative_error"]),
        float(scores["helium_rms_relative_error"]),
    )


def balanced_key(summary: dict[str, Any]) -> tuple[float, float, float, float]:
    errors = summary["metrics"]["relative_errors"]
    scores = summary["metrics"]["scores"]
    return (
        float(errors["hydrogen_ground"]),
        float(errors["helium_ion_ground"]),
        float(scores["helium_rms_relative_error"]),
        float(scores["full_rms_relative_error"]),
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
            float(params["reference_coupling"]),
            float(params["nuclear_softening_radius"]),
            float(params["repulsion_softening_radius"]),
            str(params["nuclear_profile"]),
            int(params["nuclear_quadrature_order"]),
        )
        incumbent = by_key.get(key)
        if incumbent is None:
            by_key[key] = row
            continue
        incumbent_orbitals = int(incumbent["parameters"]["max_orbitals"])
        challenger_orbitals = int(params["max_orbitals"])
        if challenger_orbitals > incumbent_orbitals or (
            challenger_orbitals == incumbent_orbitals
            and full_rms_key(row) < full_rms_key(incumbent)
        ):
            by_key[key] = row
    return list(by_key.values())


def solve_candidate(
    *,
    reference_coupling: float,
    lattice_spacing: float,
    nuclear_softening_radius: float,
    repulsion_softening_radius: float,
    nuclear_profile: str,
    nuclear_quadrature_order: int,
    max_orbitals: int,
) -> dict[str, Any]:
    return solve_two_electron_atomic_model(
        reference_coupling=reference_coupling,
        lattice_spacing=lattice_spacing,
        nuclear_softening_radius=nuclear_softening_radius,
        repulsion_softening_radius=repulsion_softening_radius,
        nuclear_profile=nuclear_profile,
        nuclear_quadrature_order=nuclear_quadrature_order,
        max_orbitals=max_orbitals,
        basis_sweep=(max_orbitals,),
    )


def top_candidate_pool(
    coarse_rows: list[dict[str, Any]],
    baseline_summary: dict[str, Any],
    *,
    top_candidates: int,
    full_rms_slack: float,
    helium_rms_slack: float,
) -> list[dict[str, Any]]:
    guarded_rows = [
        _with_guardrails(
            row,
            baseline_summary,
            full_rms_slack=full_rms_slack,
            helium_rms_slack=helium_rms_slack,
        )
        for row in coarse_rows
    ]
    by_full_rms = sorted(guarded_rows, key=full_rms_key)[:top_candidates]
    eligible = [row for row in guarded_rows if row["guardrails"]["eligible_for_balanced_selection"]]
    if not eligible:
        eligible = guarded_rows
    by_balanced = sorted(eligible, key=balanced_key)[:top_candidates]
    by_hydrogen = sorted(guarded_rows, key=hydrogen_key)[:top_candidates]
    return unique_parameter_rows(by_full_rms + by_balanced + by_hydrogen)


def select_candidates(
    rows: list[dict[str, Any]],
    baseline_summary: dict[str, Any],
    *,
    full_rms_slack: float,
    helium_rms_slack: float,
) -> dict[str, dict[str, Any] | None]:
    guarded_rows = [
        _with_guardrails(
            row,
            baseline_summary,
            full_rms_slack=full_rms_slack,
            helium_rms_slack=helium_rms_slack,
        )
        for row in rows
    ]
    best_full = min(guarded_rows, key=full_rms_key)
    best_hydrogen = min(guarded_rows, key=hydrogen_key)
    eligible = [row for row in guarded_rows if row["guardrails"]["eligible_for_balanced_selection"]]
    best_balanced = min(eligible, key=balanced_key) if eligible else None
    return {
        "best_by_full_rms": best_full,
        "best_by_hydrogen_error": best_hydrogen,
        "best_balanced_candidate": best_balanced,
    }


def improvement_vs_baseline(
    candidate: dict[str, Any],
    baseline: dict[str, Any],
) -> dict[str, float]:
    candidate_errors = candidate["metrics"]["relative_errors"]
    baseline_errors = baseline["metrics"]["relative_errors"]
    candidate_scores = candidate["metrics"]["scores"]
    baseline_scores = baseline["metrics"]["scores"]
    return {
        "hydrogen_ground_error_delta": float(candidate_errors["hydrogen_ground"])
        - float(baseline_errors["hydrogen_ground"]),
        "helium_ion_ground_error_delta": float(candidate_errors["helium_ion_ground"])
        - float(baseline_errors["helium_ion_ground"]),
        "helium_rms_relative_error_delta": float(
            candidate_scores["helium_rms_relative_error"]
        )
        - float(baseline_scores["helium_rms_relative_error"]),
        "full_rms_relative_error_delta": float(
            candidate_scores["full_rms_relative_error"]
        )
        - float(baseline_scores["full_rms_relative_error"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference-couplings",
        type=float,
        nargs="*",
        default=_scan_grid(1.57, 1.61, 0.01),
        help="reference one-body couplings scanned during the coarse continuum-core stage",
    )
    parser.add_argument(
        "--nuclear-softening-radii",
        type=float,
        nargs="*",
        default=(0.55, 0.65, 0.75, 0.85),
        help="nuclear softening radii scanned during the coarse stage",
    )
    parser.add_argument(
        "--repulsion-softening-radii",
        type=float,
        nargs="*",
        default=(0.95, 1.05, 1.15),
        help="e-e softening radii scanned during the coarse stage",
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=("hard_floor", "erf_softcore", "exp_softcore"),
        choices=SUPPORTED_NUCLEAR_PROFILES,
        help="nuclear core families scanned during the continuum-aware stage",
    )
    parser.add_argument(
        "--nuclear-quadrature-orders",
        type=int,
        nargs="*",
        default=(1, 2, 3),
        help="subcell quadrature orders scanned during the continuum-aware stage",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used throughout the continuum-core search",
    )
    parser.add_argument(
        "--scan-max-orbitals",
        type=int,
        default=10,
        help="reduced basis size used during the coarse stage",
    )
    parser.add_argument(
        "--final-max-orbitals",
        type=int,
        default=16,
        help="reduced basis size used when recomputing the shortlisted candidates",
    )
    parser.add_argument(
        "--top-candidates",
        type=int,
        default=12,
        help="number of coarse candidates promoted into the final-basis shortlist",
    )
    parser.add_argument(
        "--baseline-reference-coupling",
        type=float,
        default=1.625,
        help="baseline retained-lane coupling used for guardrails",
    )
    parser.add_argument(
        "--baseline-nuclear-softening-radius",
        type=float,
        default=0.85,
        help="baseline retained-lane nuclear softening radius used for guardrails",
    )
    parser.add_argument(
        "--baseline-repulsion-softening-radius",
        type=float,
        default=0.85,
        help="baseline retained-lane e-e softening radius used for guardrails",
    )
    parser.add_argument(
        "--baseline-nuclear-profile",
        choices=SUPPORTED_NUCLEAR_PROFILES,
        default="hard_floor",
        help="baseline retained-lane nuclear profile used for guardrails",
    )
    parser.add_argument(
        "--baseline-nuclear-quadrature-order",
        type=int,
        default=1,
        help="baseline retained-lane nuclear quadrature order used for guardrails",
    )
    parser.add_argument(
        "--full-rms-slack",
        type=float,
        default=0.10,
        help="allowable fractional worsening vs the baseline full RMS score",
    )
    parser.add_argument(
        "--helium-rms-slack",
        type=float,
        default=1.00,
        help="allowable fractional worsening vs the baseline helium RMS score",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_continuum_core_search.json",
        help="machine-readable continuum-core search output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()

    baseline_solution = solve_candidate(
        reference_coupling=float(args.baseline_reference_coupling),
        lattice_spacing=float(args.lattice_spacing),
        nuclear_softening_radius=float(args.baseline_nuclear_softening_radius),
        repulsion_softening_radius=float(args.baseline_repulsion_softening_radius),
        nuclear_profile=str(args.baseline_nuclear_profile),
        nuclear_quadrature_order=int(args.baseline_nuclear_quadrature_order),
        max_orbitals=int(args.final_max_orbitals),
    )
    baseline_summary = summarize_candidate(baseline_solution)

    reference_couplings = [float(value) for value in args.reference_couplings]
    nuclear_radii = [float(value) for value in args.nuclear_softening_radii]
    repulsion_radii = [float(value) for value in args.repulsion_softening_radii]
    nuclear_profiles = [str(value) for value in args.nuclear_profiles]
    quadrature_orders = [int(value) for value in args.nuclear_quadrature_orders]
    total_points = (
        len(reference_couplings)
        * len(nuclear_radii)
        * len(repulsion_radii)
        * len(nuclear_profiles)
        * len(quadrature_orders)
    )

    coarse_rows: list[dict[str, Any]] = []
    current_index = 0
    for reference_coupling in reference_couplings:
        for nuclear_softening_radius in nuclear_radii:
            for repulsion_softening_radius in repulsion_radii:
                for nuclear_profile in nuclear_profiles:
                    for nuclear_quadrature_order in quadrature_orders:
                        current_index += 1
                        scan_started = time.perf_counter()
                        solution = solve_candidate(
                            reference_coupling=reference_coupling,
                            lattice_spacing=float(args.lattice_spacing),
                            nuclear_softening_radius=nuclear_softening_radius,
                            repulsion_softening_radius=repulsion_softening_radius,
                            nuclear_profile=nuclear_profile,
                            nuclear_quadrature_order=nuclear_quadrature_order,
                            max_orbitals=int(args.scan_max_orbitals),
                        )
                        summary = summarize_candidate(solution)
                        summary["elapsed_seconds"] = round(
                            time.perf_counter() - scan_started,
                            6,
                        )
                        coarse_rows.append(summary)
                        print(
                            f"[coarse {current_index}/{total_points}] "
                            f"g={reference_coupling:.3f} "
                            f"rn={nuclear_softening_radius:.3f} "
                            f"ree={repulsion_softening_radius:.3f} "
                            f"profile={nuclear_profile} "
                            f"q={nuclear_quadrature_order} "
                            f"full={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
                            f"H={summary['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f} "
                            f"He={summary['metrics']['model_observables']['helium_ground_magnitude']:.6f}",
                            flush=True,
                        )

    promoted_rows = top_candidate_pool(
        coarse_rows,
        baseline_summary,
        top_candidates=int(args.top_candidates),
        full_rms_slack=float(args.full_rms_slack),
        helium_rms_slack=float(args.helium_rms_slack),
    )

    final_rows: list[dict[str, Any]] = []
    for candidate in promoted_rows:
        params = candidate["parameters"]
        scan_started = time.perf_counter()
        solution = solve_candidate(
            reference_coupling=float(params["reference_coupling"]),
            lattice_spacing=float(args.lattice_spacing),
            nuclear_softening_radius=float(params["nuclear_softening_radius"]),
            repulsion_softening_radius=float(params["repulsion_softening_radius"]),
            nuclear_profile=str(params["nuclear_profile"]),
            nuclear_quadrature_order=int(params["nuclear_quadrature_order"]),
            max_orbitals=int(args.final_max_orbitals),
        )
        summary = summarize_candidate(solution)
        summary["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
        final_rows.append(summary)
        print(
            f"[final {len(final_rows)}/{len(promoted_rows)}] "
            f"g={params['reference_coupling']:.3f} "
            f"rn={params['nuclear_softening_radius']:.3f} "
            f"ree={params['repulsion_softening_radius']:.3f} "
            f"profile={params['nuclear_profile']} "
            f"q={params['nuclear_quadrature_order']} "
            f"full={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
            f"H={summary['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f} "
            f"He={summary['metrics']['model_observables']['helium_ground_magnitude']:.6f}",
            flush=True,
        )

    selected_rows = select_candidates(
        final_rows + [baseline_summary],
        baseline_summary,
        full_rms_slack=float(args.full_rms_slack),
        helium_rms_slack=float(args.helium_rms_slack),
    )
    selected_final_candidate = _with_guardrails(
        selected_rows["best_by_full_rms"],
        baseline_summary,
        full_rms_slack=float(args.full_rms_slack),
        helium_rms_slack=float(args.helium_rms_slack),
    )
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
            "reference_couplings": reference_couplings,
            "nuclear_softening_radii": nuclear_radii,
            "repulsion_softening_radii": repulsion_radii,
            "nuclear_profiles": nuclear_profiles,
            "nuclear_quadrature_orders": quadrature_orders,
            "lattice_spacing": float(args.lattice_spacing),
            "scan_max_orbitals": int(args.scan_max_orbitals),
            "final_max_orbitals": int(args.final_max_orbitals),
            "top_candidates": int(args.top_candidates),
            "full_rms_slack": float(args.full_rms_slack),
            "helium_rms_slack": float(args.helium_rms_slack),
        },
        "coarse_stage": {
            "candidate_count": len(coarse_rows),
            "top_candidates": sorted(coarse_rows, key=full_rms_key)[:20],
        },
        "final_stage": {
            "promoted_candidates": promoted_rows,
            "candidate_count": len(final_rows),
            "top_candidates": sorted(final_rows, key=full_rms_key)[:20],
        },
        "best_by_full_rms": selected_rows["best_by_full_rms"],
        "best_by_hydrogen_error": selected_rows["best_by_hydrogen_error"],
        "best_balanced_candidate": selected_rows["best_balanced_candidate"],
        "selected_final_candidate": selected_final_candidate,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    selected_params = selected_final_candidate["parameters"]
    selected_scores = selected_final_candidate["metrics"]["scores"]
    selected_errors = selected_final_candidate["metrics"]["relative_errors"]

    print()
    print("Atomic Continuum-Core Search")
    print("============================")
    print(
        f"- Selected best full-RMS candidate: "
        f"profile={selected_params['nuclear_profile']} "
        f"q={selected_params['nuclear_quadrature_order']} "
        f"g={selected_params['reference_coupling']:.6f} "
        f"rn={selected_params['nuclear_softening_radius']:.6f} "
        f"ree={selected_params['repulsion_softening_radius']:.6f}."
    )
    print(
        f"- Final relative errors: "
        f"H={selected_errors['hydrogen_ground']:.4f}, "
        f"He+={selected_errors['helium_ion_ground']:.4f}, "
        f"He={selected_errors['helium_ground']:.4f}, "
        f"I={selected_errors['helium_ionization']:.4f}."
    )
    print(
        f"- Final RMS scores: full={selected_scores['full_rms_relative_error']:.4f}, "
        f"helium={selected_scores['helium_rms_relative_error']:.4f}."
    )
    print(f"- Wrote search output to {args.write_json}.")


if __name__ == "__main__":
    main()
