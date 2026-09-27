#!/usr/bin/env python3
"""Retained-manifold hydrogen-like readout plus bounded helium-like proxy.

This runner does not invent a new helium solver. It combines:
  1. the retained polarity-corrected atomic lane,
  2. the existing Coulomb bound-state baseline, and
  3. one fresh d=3 spectrum solve,

to produce the strongest bounded statement the current codebase can support:
  - explicit hydrogen-like one-body numbers on the retained manifold, and
  - a clearly marked helium-like double-occupancy proxy only.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import (  # noqa: E402
    BOUND_STATE_CONFIGS,
    DEFAULT_OUTPUT_ROOT,
    build_bound_state_baseline,
    read_json,
    write_json,
)
from scripts.atomic_two_body_runtime import (  # noqa: E402
    solve_one_body_bound_orbitals,
)


def _float_stats(values: list[float]) -> dict[str, float]:
    return {
        "min": float(min(values)),
        "mean": float(sum(values) / len(values)),
        "max": float(max(values)),
    }


def _retained_manifold_terms(discriminator_payload: dict[str, Any]) -> list[str]:
    terms: list[str] = []
    for atom in discriminator_payload["atoms"]:
        feature_name = str(atom["feature_name"])
        polarity = str(atom["polarity"])
        if polarity == "positive":
            terms.append(f"{feature_name}=0")
        elif polarity == "zero":
            terms.append(f"{feature_name}>0")
        else:
            raise ValueError(f"unsupported polarity {polarity!r}")
    return terms


def _find_bound_state_config(dimension: int) -> tuple[int, tuple[int, ...], float]:
    for config in BOUND_STATE_CONFIGS:
        if config[0] == dimension:
            return config
    raise KeyError(f"no bound-state config registered for d={dimension}")


def _compute_dimension_spectrum(
    dimension: int,
    *,
    coupling: float,
    lattice_spacing: float,
    softening_radius: float,
    nuclear_profile: str,
    nuclear_quadrature_order: int,
    nuclear_counterterm_strength: float,
    nuclear_counterterm_radius: float | None,
) -> dict[str, Any]:
    one_body = solve_one_body_bound_orbitals(
        dimension=dimension,
        coupling=coupling,
        max_orbitals=None,
        n_eig=40,
        lattice_spacing=lattice_spacing,
        softening_radius=softening_radius,
        nuclear_profile=nuclear_profile,
        nuclear_quadrature_order=nuclear_quadrature_order,
        nuclear_counterterm_strength=nuclear_counterterm_strength,
        nuclear_counterterm_radius=nuclear_counterterm_radius,
    )
    negative_eigenvalues = list(np.asarray(one_body["orbital_energies"], dtype=float))
    energy_gaps = [
        float(right - left)
        for left, right in zip(negative_eigenvalues, negative_eigenvalues[1:], strict=False)
    ]
    first_orbital = dict(one_body["orbital_rows"][0])
    localization = {
        "ipr": float(first_orbital["ipr"]),
        "center_weight": float(first_orbital["center_weight"]),
        "decay_rate": float(first_orbital["decay_rate"]),
        "genuinely_localized": bool(first_orbital["genuinely_localized"]),
        "physical_bound": bool(first_orbital["physical_bound"]),
    }
    return {
        "d": int(one_body["dimension"]),
        "sizes": list(one_body["sizes"]),
        "coupling": float(coupling),
        "lattice_spacing": float(lattice_spacing),
        "softening_radius": float(softening_radius),
        "nuclear_profile": str(nuclear_profile),
        "nuclear_quadrature_order": int(nuclear_quadrature_order),
        "nuclear_counterterm_strength": float(nuclear_counterterm_strength),
        "nuclear_counterterm_radius": (
            float(nuclear_counterterm_radius)
            if nuclear_counterterm_radius is not None
            else None
        ),
        "n_bound": int(one_body["n_bound_total"]),
        "negative_eigenvalues": negative_eigenvalues,
        "energy_gaps": energy_gaps,
        "localization": localization,
    }


def _robust_dimensions(bound_state_baseline: dict[str, Any]) -> list[int]:
    return [
        int(row["d"])
        for row in bound_state_baseline["rows"]
        if int(row["n_bound"]) >= 2 and bool(row["localization"]["physical_bound"])
    ]


def _selector_summary(
    *,
    validation_payload: dict[str, Any],
    mechanism_payload: dict[str, Any],
) -> dict[str, Any]:
    tested_ensembles = list(validation_payload["tested_ensembles"])
    excluded_fraction = [float(row["excluded_fraction"]) for row in tested_ensembles]
    pocket_support = [float(row["pocket_support_fraction"]) for row in tested_ensembles]
    deep_support = [float(row["deep_support_fraction"]) for row in tested_ensembles]
    residual_fallback = [
        float(row["score"]["residual_fallback_fraction"])
        for row in tested_ensembles
    ]
    mechanism_labels = sorted(
        {str(row["mechanism_label"]) for row in mechanism_payload["mechanism_rows"]}
    )
    discriminator_payload = validation_payload["discriminator"]
    retained_terms = _retained_manifold_terms(discriminator_payload)
    return {
        "retained_discriminator": discriminator_payload,
        "retained_manifold_terms": retained_terms,
        "retained_manifold_label": " and ".join(retained_terms),
        "canonical_passes": bool(validation_payload["passes"]),
        "ensemble_count": len(tested_ensembles),
        "excluded_fraction": _float_stats(excluded_fraction),
        "pocket_support_fraction": _float_stats(pocket_support),
        "deep_support_fraction": _float_stats(deep_support),
        "low_support_fraction": _float_stats(
            [float(row["low_support_fraction"]) for row in tested_ensembles]
        ),
        "fallback_residual_fraction": _float_stats(residual_fallback),
        "fallback_residual_all_zero": all(value == 0.0 for value in residual_fallback),
        "nesting_floor_min": min(
            min(
                float(row["pocket_implies_low"]),
                float(row["deep_implies_pocket"]),
                float(row["deep_implies_low"]),
            )
            for row in tested_ensembles
        ),
        "mechanism_labels": mechanism_labels,
        "shell_localization_retained_all": mechanism_labels == ["shell-localization retained"],
    }


def _hydrogen_like_summary(
    *,
    selector_summary: dict[str, Any],
    bound_state_baseline: dict[str, Any],
    d3_spectrum: dict[str, Any],
) -> dict[str, Any]:
    robust_dims = _robust_dimensions(bound_state_baseline)
    highest_robust_dim = max(robust_dims) if robust_dims else None
    d3_row = next(row for row in bound_state_baseline["rows"] if int(row["d"]) == 3)
    hydrogen_supported = bool(
        selector_summary["canonical_passes"]
        and selector_summary["fallback_residual_all_zero"]
        and selector_summary["shell_localization_retained_all"]
        and highest_robust_dim == 3
        and int(d3_spectrum["n_bound"]) >= 2
        and bool(d3_spectrum["localization"]["physical_bound"])
    )
    return {
        "numerically_supported": hydrogen_supported,
        "highest_robust_dimension": highest_robust_dim,
        "robust_dimensions": robust_dims,
        "dimension": 3,
        "coupling": float(d3_spectrum["coupling"]),
        "lattice_sizes": d3_spectrum["sizes"],
        "n_bound": int(d3_spectrum["n_bound"]),
        "ground_energy": (
            float(d3_spectrum["negative_eigenvalues"][0])
            if d3_spectrum["negative_eigenvalues"]
            else None
        ),
        "negative_bound_energies": d3_spectrum["negative_eigenvalues"],
        "energy_gaps": d3_spectrum["energy_gaps"],
        "localization": d3_spectrum["localization"],
        "bound_state_baseline_row": d3_row,
        "bounded_claim": (
            "Hydrogen-like one-body numbers are supported only on the retained "
            "polarity manifold and only as a d=3 bound-state readout."
        ),
    }


def _helium_like_proxy_summary(
    *,
    selector_summary: dict[str, Any],
    hydrogen_like_summary: dict[str, Any],
) -> dict[str, Any]:
    ground_energy = hydrogen_like_summary["ground_energy"]
    proxy_energy = 2.0 * ground_energy if ground_energy is not None else None
    return {
        "physical_helium_supported": False,
        "bounded_proxy_available": proxy_energy is not None,
        "noninteracting_double_occupancy_total_energy": proxy_energy,
        "source_one_body_ground_energy": ground_energy,
        "available_bound_levels": int(hydrogen_like_summary["n_bound"]),
        "shell_localization_retained": bool(
            selector_summary["shell_localization_retained_all"]
        ),
        "missing_terms": [
            "electron-electron repulsion",
            "true two-body Hamiltonian",
            "antisymmetrization/spin structure",
            "correlation and screening corrections",
        ],
        "bounded_claim": (
            "This is only a double-occupancy one-body proxy. It is not a physical "
            "helium binding or spectral prediction."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_candidate_validation.json",
        help="retained polarity candidate validation JSON",
    )
    parser.add_argument(
        "--mechanism-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_mechanism.json",
        help="retained polarity mechanism JSON",
    )
    parser.add_argument(
        "--bridge-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_bridge.json",
        help="optional bridge JSON kept for provenance only",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_hydrogen_helium_readout.json",
        help="machine-readable readout output path",
    )
    parser.add_argument(
        "--reference-coupling",
        type=float,
        help="override the retained d=3 one-body coupling",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used to scale the Laplacian and Coulomb radius",
    )
    parser.add_argument(
        "--softening-radius",
        type=float,
        default=1.0,
        help="shared Coulomb softening radius for the one-body readout",
    )
    parser.add_argument(
        "--nuclear-profile",
        choices=("hard_floor", "plummer", "shifted", "erf_softcore", "exp_softcore"),
        default="hard_floor",
        help="short-distance nuclear core profile used in the one-body readout",
    )
    parser.add_argument(
        "--nuclear-quadrature-order",
        type=int,
        default=1,
        help="subcell quadrature order used to average the nuclear core over each lattice cell",
    )
    parser.add_argument(
        "--nuclear-counterterm-strength",
        type=float,
        default=0.0,
        help="dimensionless repulsive Gaussian UV counterterm strength",
    )
    parser.add_argument(
        "--nuclear-counterterm-radius",
        type=float,
        help="Gaussian UV counterterm radius; defaults to the softening radius",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    validation_payload = read_json(args.validation_json)
    mechanism_payload = read_json(args.mechanism_json)
    if not validation_payload.get("passes", False):
        raise SystemExit(
            f"validation JSON does not describe a retained candidate: {args.validation_json}"
        )

    selector_summary = _selector_summary(
        validation_payload=validation_payload,
        mechanism_payload=mechanism_payload,
    )

    bound_state_baseline = build_bound_state_baseline()
    _d, _sizes, default_coupling = _find_bound_state_config(3)
    reference_coupling = (
        float(args.reference_coupling)
        if args.reference_coupling is not None
        else float(default_coupling)
    )

    d3_spectrum = _compute_dimension_spectrum(
        3,
        coupling=reference_coupling,
        lattice_spacing=float(args.lattice_spacing),
        softening_radius=float(args.softening_radius),
        nuclear_profile=str(args.nuclear_profile),
        nuclear_quadrature_order=int(args.nuclear_quadrature_order),
        nuclear_counterterm_strength=float(args.nuclear_counterterm_strength),
        nuclear_counterterm_radius=args.nuclear_counterterm_radius,
    )
    hydrogen_like_summary = _hydrogen_like_summary(
        selector_summary=selector_summary,
        bound_state_baseline=bound_state_baseline,
        d3_spectrum=d3_spectrum,
    )
    helium_like_proxy = _helium_like_proxy_summary(
        selector_summary=selector_summary,
        hydrogen_like_summary=hydrogen_like_summary,
    )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "bridge_json": str(args.bridge_json),
        "bridge_json_present": args.bridge_json.exists(),
        "calibration": {
            "reference_coupling": reference_coupling,
            "lattice_spacing": float(args.lattice_spacing),
            "softening_radius": float(args.softening_radius),
            "nuclear_profile": str(args.nuclear_profile),
            "nuclear_quadrature_order": int(args.nuclear_quadrature_order),
            "nuclear_counterterm_strength": float(args.nuclear_counterterm_strength),
            "nuclear_counterterm_radius": (
                float(args.nuclear_counterterm_radius)
                if args.nuclear_counterterm_radius is not None
                else None
            ),
        },
        "selector_summary": selector_summary,
        "hydrogen_like": hydrogen_like_summary,
        "helium_like_proxy": helium_like_proxy,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Hydrogen/Helium Readout")
    print("==============================")
    print(f"- Retained manifold: {selector_summary['retained_manifold_label']}.")
    print(
        f"- Hydrogen-like d=3 readout: "
        f"n_bound={hydrogen_like_summary['n_bound']} "
        f"E0={hydrogen_like_summary['ground_energy']:.6f} "
        f"robust_dim_max={hydrogen_like_summary['highest_robust_dimension']}."
    )
    if helium_like_proxy["bounded_proxy_available"]:
        print(
            f"- Helium-like bounded proxy only: "
            f"2*E0={helium_like_proxy['noninteracting_double_occupancy_total_energy']:.6f}."
        )
    else:
        print("- Helium-like bounded proxy unavailable.")
    print(f"- Wrote readout to {args.write_json}.")


if __name__ == "__main__":
    main()
