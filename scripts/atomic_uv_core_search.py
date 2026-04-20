#!/usr/bin/env python3
"""Search UV/core-shape corrections for the retained atomic-lane atom model."""

from __future__ import annotations

import argparse
from datetime import datetime
from math import sqrt
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


def _candidate_parameters(solution: dict[str, Any]) -> dict[str, Any]:
    model = solution["model"]
    return {
        "reference_coupling": float(model["reference_coupling"]),
        "lattice_spacing": float(model["lattice_spacing"]),
        "nuclear_softening_radius": float(model["nuclear_softening_radius"]),
        "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
        "nuclear_profile": str(model["nuclear_profile"]),
        "nuclear_counterterm_strength": float(model["nuclear_counterterm_strength"]),
        "nuclear_counterterm_radius": (
            float(model["nuclear_counterterm_radius"])
            if model["nuclear_counterterm_radius"] is not None
            else None
        ),
        "max_orbitals": int(model["max_orbitals"]),
    }


def summarize_candidate(solution: dict[str, Any]) -> dict[str, Any]:
    metrics = candidate_metrics(solution)
    return {
        "parameters": _candidate_parameters(solution),
        "metrics": metrics,
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


def balanced_key(summary: dict[str, Any]) -> tuple[float, float, float, float]:
    errors = summary["metrics"]["relative_errors"]
    scores = summary["metrics"]["scores"]
    return (
        float(errors["hydrogen_ground"]),
        float(errors["helium_ion_ground"]),
        float(scores["helium_rms_relative_error"]),
        float(scores["full_rms_relative_error"]),
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


def unique_parameter_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in rows:
        params = row["parameters"]
        key = (
            float(params["reference_coupling"]),
            float(params["nuclear_softening_radius"]),
            float(params["repulsion_softening_radius"]),
            str(params["nuclear_profile"]),
            float(params["nuclear_counterterm_strength"]),
            params["nuclear_counterterm_radius"],
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


def candidate_pool_for_refinement(
    coarse_rows: list[dict[str, Any]],
    baseline_summary: dict[str, Any],
    *,
    stage2_base_candidates: int,
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
    by_full_rms = sorted(guarded_rows, key=full_rms_key)[:stage2_base_candidates]
    eligible = [row for row in guarded_rows if row["guardrails"]["eligible_for_balanced_selection"]]
    if not eligible:
        eligible = guarded_rows
    by_balanced = sorted(eligible, key=balanced_key)[:stage2_base_candidates]
    by_hydrogen = sorted(guarded_rows, key=hydrogen_key)[:stage2_base_candidates]
    return unique_parameter_rows(by_full_rms + by_balanced + by_hydrogen)


def solve_candidate(
    *,
    reference_coupling: float,
    lattice_spacing: float,
    nuclear_softening_radius: float,
    repulsion_softening_radius: float,
    nuclear_profile: str,
    nuclear_counterterm_strength: float,
    nuclear_counterterm_radius: float | None,
    max_orbitals: int,
) -> dict[str, Any]:
    return solve_two_electron_atomic_model(
        reference_coupling=reference_coupling,
        lattice_spacing=lattice_spacing,
        nuclear_softening_radius=nuclear_softening_radius,
        repulsion_softening_radius=repulsion_softening_radius,
        nuclear_profile=nuclear_profile,
        nuclear_counterterm_strength=nuclear_counterterm_strength,
        nuclear_counterterm_radius=nuclear_counterterm_radius,
        max_orbitals=max_orbitals,
        basis_sweep=(max_orbitals,),
    )


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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference-couplings",
        type=float,
        nargs="*",
        default=_scan_grid(1.55, 1.70, 0.025),
        help="reference one-body couplings used during the coarse UV search",
    )
    parser.add_argument(
        "--nuclear-softening-radii",
        type=float,
        nargs="*",
        default=_scan_grid(0.75, 1.05, 0.05),
        help="nuclear softening radii scanned during the coarse stage",
    )
    parser.add_argument(
        "--repulsion-softening-radii",
        type=float,
        nargs="*",
        default=_scan_grid(0.70, 1.00, 0.05),
        help="e-e softening radii scanned during the coarse stage",
    )
    parser.add_argument(
        "--nuclear-profiles",
        nargs="*",
        default=list(SUPPORTED_NUCLEAR_PROFILES),
        choices=SUPPORTED_NUCLEAR_PROFILES,
        help="nuclear core profiles scanned during the coarse stage",
    )
    parser.add_argument(
        "--counterterm-strengths",
        type=float,
        nargs="*",
        default=(0.05, 0.10, 0.15, 0.20),
        help="repulsive Gaussian counterterm strengths explored during refinement",
    )
    parser.add_argument(
        "--counterterm-radius-scales",
        type=float,
        nargs="*",
        default=(0.5, 0.75, 1.0, 1.25),
        help="counterterm radii expressed as multiples of the nuclear softening radius",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used throughout the UV/core search",
    )
    parser.add_argument(
        "--coarse-max-orbitals",
        type=int,
        default=10,
        help="reduced basis size used during the coarse stage",
    )
    parser.add_argument(
        "--refine-max-orbitals",
        type=int,
        default=12,
        help="reduced basis size used during the counterterm refinement stage",
    )
    parser.add_argument(
        "--final-max-orbitals",
        type=int,
        default=16,
        help="reduced basis size used for the selected final candidate",
    )
    parser.add_argument(
        "--stage2-base-candidates",
        type=int,
        default=10,
        help="number of coarse candidates promoted into the counterterm stage",
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
        "--full-rms-slack",
        type=float,
        default=0.08,
        help="allowable fractional worsening vs the baseline full RMS score",
    )
    parser.add_argument(
        "--helium-rms-slack",
        type=float,
        default=0.08,
        help="allowable fractional worsening vs the baseline helium RMS score",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_uv_core_search.json",
        help="machine-readable UV/core search output path",
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
        nuclear_counterterm_strength=0.0,
        nuclear_counterterm_radius=None,
        max_orbitals=int(args.final_max_orbitals),
    )
    baseline_summary = summarize_candidate(baseline_solution)

    coarse_rows: list[dict[str, Any]] = []
    reference_couplings = [float(value) for value in args.reference_couplings]
    nuclear_radii = [float(value) for value in args.nuclear_softening_radii]
    repulsion_radii = [float(value) for value in args.repulsion_softening_radii]
    nuclear_profiles = [str(value) for value in args.nuclear_profiles]
    total_coarse = (
        len(reference_couplings)
        * len(nuclear_radii)
        * len(repulsion_radii)
        * len(nuclear_profiles)
    )

    coarse_index = 0
    for reference_coupling in reference_couplings:
        for nuclear_softening_radius in nuclear_radii:
            for repulsion_softening_radius in repulsion_radii:
                for nuclear_profile in nuclear_profiles:
                    coarse_index += 1
                    scan_started = time.perf_counter()
                    solution = solve_candidate(
                        reference_coupling=reference_coupling,
                        lattice_spacing=float(args.lattice_spacing),
                        nuclear_softening_radius=nuclear_softening_radius,
                        repulsion_softening_radius=repulsion_softening_radius,
                        nuclear_profile=nuclear_profile,
                        nuclear_counterterm_strength=0.0,
                        nuclear_counterterm_radius=None,
                        max_orbitals=int(args.coarse_max_orbitals),
                    )
                    summary = summarize_candidate(solution)
                    summary["elapsed_seconds"] = round(
                        time.perf_counter() - scan_started,
                        6,
                    )
                    coarse_rows.append(summary)
                    print(
                        f"[coarse {coarse_index}/{total_coarse}] "
                        f"g={reference_coupling:.3f} "
                        f"rn={nuclear_softening_radius:.3f} "
                        f"ree={repulsion_softening_radius:.3f} "
                        f"profile={nuclear_profile} "
                        f"full={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
                        f"H={summary['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f} "
                        f"He={summary['metrics']['model_observables']['helium_ground_magnitude']:.6f}",
                        flush=True,
                    )

    promoted_rows = candidate_pool_for_refinement(
        coarse_rows,
        baseline_summary,
        stage2_base_candidates=int(args.stage2_base_candidates),
        full_rms_slack=float(args.full_rms_slack),
        helium_rms_slack=float(args.helium_rms_slack),
    )

    refine_rows: list[dict[str, Any]] = []
    counterterm_strengths = [float(value) for value in args.counterterm_strengths]
    counterterm_radius_scales = [
        float(value) for value in args.counterterm_radius_scales
    ]
    total_refine = (
        len(promoted_rows) * len(counterterm_strengths) * len(counterterm_radius_scales)
    )
    refine_index = 0
    for promoted in promoted_rows:
        params = promoted["parameters"]
        for counterterm_strength in counterterm_strengths:
            for radius_scale in counterterm_radius_scales:
                refine_index += 1
                counterterm_radius = (
                    float(params["nuclear_softening_radius"]) * radius_scale
                )
                scan_started = time.perf_counter()
                solution = solve_candidate(
                    reference_coupling=float(params["reference_coupling"]),
                    lattice_spacing=float(args.lattice_spacing),
                    nuclear_softening_radius=float(params["nuclear_softening_radius"]),
                    repulsion_softening_radius=float(params["repulsion_softening_radius"]),
                    nuclear_profile=str(params["nuclear_profile"]),
                    nuclear_counterterm_strength=counterterm_strength,
                    nuclear_counterterm_radius=counterterm_radius,
                    max_orbitals=int(args.refine_max_orbitals),
                )
                summary = summarize_candidate(solution)
                summary["elapsed_seconds"] = round(
                    time.perf_counter() - scan_started,
                    6,
                )
                refine_rows.append(summary)
                print(
                    f"[refine {refine_index}/{total_refine}] "
                    f"base_profile={params['nuclear_profile']} "
                    f"g={params['reference_coupling']:.3f} "
                    f"rn={params['nuclear_softening_radius']:.3f} "
                    f"ree={params['repulsion_softening_radius']:.3f} "
                    f"ct={counterterm_strength:.3f} "
                    f"rc={counterterm_radius:.3f} "
                    f"full={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
                    f"H={summary['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f}",
                    flush=True,
                )

    combined_rows = unique_parameter_rows(
        coarse_rows
        + refine_rows
        + [baseline_summary]
    )
    selected_rows = select_candidates(
        combined_rows,
        baseline_summary,
        full_rms_slack=float(args.full_rms_slack),
        helium_rms_slack=float(args.helium_rms_slack),
    )

    selected_strategy = (
        "balanced_guardrailed"
        if selected_rows["best_balanced_candidate"] is not None
        else "full_rms_fallback"
    )
    selected_candidate = (
        selected_rows["best_balanced_candidate"]
        if selected_rows["best_balanced_candidate"] is not None
        else selected_rows["best_by_full_rms"]
    )
    assert selected_candidate is not None
    selected_params = selected_candidate["parameters"]
    selected_solution = solve_candidate(
        reference_coupling=float(selected_params["reference_coupling"]),
        lattice_spacing=float(args.lattice_spacing),
        nuclear_softening_radius=float(selected_params["nuclear_softening_radius"]),
        repulsion_softening_radius=float(selected_params["repulsion_softening_radius"]),
        nuclear_profile=str(selected_params["nuclear_profile"]),
        nuclear_counterterm_strength=float(
            selected_params["nuclear_counterterm_strength"]
        ),
        nuclear_counterterm_radius=selected_params["nuclear_counterterm_radius"],
        max_orbitals=int(args.final_max_orbitals),
    )
    selected_final_candidate = _with_guardrails(
        summarize_candidate(selected_solution),
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
            "counterterm_strengths": counterterm_strengths,
            "counterterm_radius_scales": counterterm_radius_scales,
            "lattice_spacing": float(args.lattice_spacing),
            "coarse_max_orbitals": int(args.coarse_max_orbitals),
            "refine_max_orbitals": int(args.refine_max_orbitals),
            "final_max_orbitals": int(args.final_max_orbitals),
            "stage2_base_candidates": int(args.stage2_base_candidates),
            "full_rms_slack": float(args.full_rms_slack),
            "helium_rms_slack": float(args.helium_rms_slack),
        },
        "coarse_stage": {
            "candidate_count": len(coarse_rows),
            "top_candidates": sorted(coarse_rows, key=full_rms_key)[:20],
        },
        "counterterm_stage": {
            "promoted_base_candidates": promoted_rows,
            "candidate_count": len(refine_rows),
            "top_candidates": sorted(refine_rows, key=full_rms_key)[:20],
        },
        "best_by_full_rms": selected_rows["best_by_full_rms"],
        "best_by_hydrogen_error": selected_rows["best_by_hydrogen_error"],
        "best_balanced_candidate": selected_rows["best_balanced_candidate"],
        "selected_strategy": selected_strategy,
        "selected_final_candidate": selected_final_candidate,
        "selected_solution": selected_solution,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    selected_metrics = selected_final_candidate["metrics"]
    selected_errors = selected_metrics["relative_errors"]
    selected_scores = selected_metrics["scores"]

    print()
    print("Atomic UV/Core Search")
    print("=====================")
    print(f"- Selected strategy: {selected_strategy}.")
    print(
        f"- Selected profile: {selected_params['nuclear_profile']} "
        f"with g={selected_params['reference_coupling']:.6f}, "
        f"rn={selected_params['nuclear_softening_radius']:.6f}, "
        f"ree={selected_params['repulsion_softening_radius']:.6f}."
    )
    print(
        f"- Counterterm: strength={selected_params['nuclear_counterterm_strength']:.6f}, "
        f"radius={selected_params['nuclear_counterterm_radius']}."
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
