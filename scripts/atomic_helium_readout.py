#!/usr/bin/env python3
"""Read out the retained-lane two-electron helium companion."""

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
from scripts.atomic_observable_metrics import (  # noqa: E402
    ACTUALS_HARTREE,
    fit_inverse_basis_limit,
    helium_readout_metrics,
)


def retained_manifold_terms(discriminator_payload: dict[str, Any]) -> list[str]:
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


def basis_tail_delta(rows: list[dict[str, Any]], key: str) -> float | None:
    usable = [row for row in rows if row.get(key) is not None]
    if len(usable) < 2:
        return None
    return float(usable[-1][key] - usable[-2][key])


def basis_extrapolation_summary(
    rows: list[dict[str, Any]],
) -> dict[str, dict[str, Any] | None]:
    summary: dict[str, dict[str, Any] | None] = {}
    actual_map = {
        "singlet_ground_energy": ACTUALS_HARTREE["helium_ground_magnitude"],
        "triplet_ground_energy": ACTUALS_HARTREE["helium_triplet_magnitude"],
        "ionization_energy": ACTUALS_HARTREE["helium_ionization_energy"],
        "singlet_triplet_gap": ACTUALS_HARTREE["singlet_triplet_gap"],
    }
    for key, actual_value in actual_map.items():
        fit = fit_inverse_basis_limit(rows, key=key)
        if fit is None:
            summary[key] = None
            continue
        fit["fitted_limit_magnitude"] = abs(float(fit["fitted_limit"]))
        fit["limit_relative_error"] = abs(
            abs(float(fit["fitted_limit"])) / float(actual_value) - 1.0
        )
        summary[key] = fit
    return summary


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
        "--solver-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_solver.json",
        help="two-electron helium solver JSON",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout.json",
        help="machine-readable helium readout path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    validation_payload = read_json(args.validation_json)
    mechanism_payload = read_json(args.mechanism_json)
    solver_payload = read_json(args.solver_json)

    if not validation_payload.get("passes", False):
        raise SystemExit(
            f"retained polarity validation is not passing: {args.validation_json}"
        )

    mechanism_labels = sorted(
        {str(row["mechanism_label"]) for row in mechanism_payload["mechanism_rows"]}
    )
    discriminator_payload = validation_payload["discriminator"]
    solution = solver_payload["solution"]
    basis_rows = solution["two_electron"]["basis_sweep"]
    singlet = solution["two_electron"]["singlet"]
    triplet = solution["two_electron"]["triplet"]
    manifold_terms = retained_manifold_terms(discriminator_payload)
    bounded_helium_like_binding = bool(
        validation_payload["passes"]
        and solution["two_electron"]["helium_like_bound"]
        and solution["two_electron"]["spin_ground_sector"] == "singlet"
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "selector_summary": {
            "retained_discriminator": discriminator_payload,
            "retained_manifold_terms": manifold_terms,
            "retained_manifold_label": " and ".join(manifold_terms),
            "canonical_passes": bool(validation_payload["passes"]),
            "mechanism_labels": mechanism_labels,
            "shell_localization_retained_all": mechanism_labels == ["shell-localization retained"],
        },
        "hydrogen_like_reference": solution["hydrogen_reference"],
        "helium_ion_reference": solution["helium_ion_reference"],
        "helium_two_electron": {
            "two_body_hamiltonian_present": True,
            "electron_repulsion_present": bool(solution["two_electron"]["electron_repulsion_present"]),
            "antisymmetry_present": bool(solution["two_electron"]["antisymmetry_present"]),
            "spin_sectors_present": solution["two_electron"]["spin_sectors_present"],
            "spatial_orbital_count": int(solution["two_electron"]["spatial_orbital_count"]),
            "negative_orbital_count": int(solution["helium_ion_reference"]["n_negative_selected"]),
            "virtual_orbital_count": int(solution["helium_ion_reference"]["n_virtual_selected"]),
            "spin_ground_sector": solution["two_electron"]["spin_ground_sector"],
            "helium_like_bound_on_current_basis": bool(solution["two_electron"]["helium_like_bound"]),
            "bounded_helium_like_binding_supported": bounded_helium_like_binding,
            "singlet_ground_energy": singlet["ground_energy"],
            "triplet_ground_energy": triplet["ground_energy"],
            "helium_ion_ground_energy": solution["helium_ion_reference"]["ground_energy"],
            "hydrogen_ground_energy": solution["hydrogen_reference"]["ground_energy"],
            "ionization_energy": solution["two_electron"]["ionization_energy"],
            "triplet_ionization_energy": solution["two_electron"]["triplet_ionization_energy"],
            "singlet_triplet_gap": solution["two_electron"]["singlet_triplet_gap"],
            "interaction_shift_from_double_occupancy": solution["two_electron"]["interaction_shift_from_double_occupancy"],
            "singlet_contact_probability": singlet["contact_probability"],
            "triplet_contact_probability": triplet["contact_probability"],
            "singlet_repulsion_energy": singlet["interaction_energy_expectation"],
            "triplet_repulsion_energy": triplet["interaction_energy_expectation"],
            "singlet_orbital_occupancies": singlet["orbital_occupancies"],
            "triplet_orbital_occupancies": triplet["orbital_occupancies"],
            "singlet_dominant_configurations": singlet["dominant_configurations"],
            "triplet_dominant_configurations": triplet["dominant_configurations"],
            "basis_sweep": basis_rows,
            "basis_tail_delta": {
                "singlet_ground_energy": basis_tail_delta(basis_rows, "singlet_ground_energy"),
                "triplet_ground_energy": basis_tail_delta(basis_rows, "triplet_ground_energy"),
                "ionization_energy": basis_tail_delta(basis_rows, "ionization_energy"),
            },
            "basis_extrapolation": basis_extrapolation_summary(basis_rows),
        },
        "bounded_claim": (
            "The retained polarity manifold now supports a true reduced-basis "
            "two-electron Hamiltonian with e-e repulsion, antisymmetry, and "
            "singlet/triplet spin sectors. The resulting helium-like numbers are "
            "bounded reduced-basis outputs, not continuum/QED predictions."
        ),
        "remaining_limits": [
            "reduced orbital basis rather than full site-basis two-body space",
            "no continuum extrapolation",
            "no relativistic or QED corrections",
            "finite lattice regularization of the Coulomb singularity",
        ],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    output_payload["actuals_hartree"] = ACTUALS_HARTREE
    output_payload["accuracy_metrics"] = helium_readout_metrics(output_payload)
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Helium Readout")
    print("=====================")
    print(
        f"- Retained manifold: "
        f"{output_payload['selector_summary']['retained_manifold_label']}."
    )
    print(
        f"- He singlet ground energy: "
        f"{output_payload['helium_two_electron']['singlet_ground_energy']:.6f}."
    )
    print(
        f"- He ionization energy on the current reduced basis: "
        f"{output_payload['helium_two_electron']['ionization_energy']:.6f}."
    )
    print(
        f"- Full RMS relative error vs actuals: "
        f"{output_payload['accuracy_metrics']['scores']['full_rms_relative_error']:.4f}."
    )
    print(
        f"- Bounded helium-like binding supported: "
        f"{'YES' if bounded_helium_like_binding else 'NO'}."
    )
    print(f"- Wrote readout to {args.write_json}.")


if __name__ == "__main__":
    main()
