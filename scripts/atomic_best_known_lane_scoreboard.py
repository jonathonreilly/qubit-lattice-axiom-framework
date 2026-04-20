#!/usr/bin/env python3
"""Compare the best-known retained atomic-lane milestones."""

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
from scripts.atomic_observable_metrics import helium_readout_metrics  # noqa: E402


def _helium_entry(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    metrics = helium_readout_metrics(payload)
    helium = payload["helium_two_electron"]
    return {
        "label": label,
        "source_json": str(path),
        "entry_type": "helium_readout",
        "scores": metrics["scores"],
        "relative_errors": metrics["relative_errors"],
        "model_observables": metrics["model_observables"],
        "spatial_orbital_count": int(helium.get("spatial_orbital_count", 0)),
    }


def _one_body_entry(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    if "benchmark" in payload:
        benchmark = payload["benchmark"]
    else:
        benchmark = payload.get("best_selected_candidate")
        if benchmark is None:
            benchmark = payload["selected_final_candidates"][0]
    return {
        "label": label,
        "source_json": str(path),
        "entry_type": "one_body_benchmark",
        "scores": benchmark["metrics"]["scores"],
        "relative_errors": benchmark["metrics"]["relative_errors"],
        "model_observables": benchmark["metrics"]["model_observables"],
        "spatial_orbital_count": None,
    }


def _correlated_entry(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    candidate = payload["accepted_candidate"]
    return {
        "label": label,
        "source_json": str(path),
        "entry_type": "correlated_candidate",
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "model_observables": candidate["metrics"]["model_observables"],
        "spatial_orbital_count": int(candidate["solution"]["two_electron"]["spatial_orbital_count"]),
    }


def _retuned_contact_entry(label: str, path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    payload = read_json(path)
    candidate_row = payload.get("best_strong_candidate") or payload.get("best_accepted_candidate")
    if candidate_row is None:
        return None
    candidate = candidate_row["selected_lambda_row"]
    return {
        "label": label,
        "source_json": str(path),
        "entry_type": "retuned_contact_candidate",
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "model_observables": candidate["metrics"]["model_observables"],
        "spatial_orbital_count": int(candidate["solution"]["two_electron"]["spatial_orbital_count"]),
        "accepted_basis_count": int(candidate_row["accepted_basis_count"]),
        "strong_robust": bool(candidate_row["strong_robust"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--uv-core-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_uv_core.json",
    )
    parser.add_argument(
        "--virtual-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
    )
    parser.add_argument(
        "--one-body-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_multi_family_coupling_calibration.json",
    )
    parser.add_argument(
        "--contact-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--finite-range-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_finite_range.json",
    )
    parser.add_argument(
        "--retuned-contact-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_contact_retune_round.json",
    )
    parser.add_argument(
        "--shell-projector-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--shell-projector-continuum-live-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector_continuum_live.json",
    )
    parser.add_argument(
        "--shell-contact-joint-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_contact_joint.json",
    )
    parser.add_argument(
        "--shell-pair-addon-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_pair_addon.json",
    )
    parser.add_argument(
        "--shell-one-body-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_one_body.json",
    )
    parser.add_argument(
        "--shell-radial-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_radial.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_best_known_lane_scoreboard.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries = [
        _helium_entry("uv_core", args.uv_core_readout_json),
        _helium_entry("virtual_64", args.virtual_readout_json),
        _one_body_entry("one_body_calibrated", args.one_body_json),
        _correlated_entry("contact_accepted", args.contact_json),
        _correlated_entry("finite_range_best", args.finite_range_json),
    ]
    retuned_entry = _retuned_contact_entry("retuned_contact_candidate", args.retuned_contact_json)
    if retuned_entry is not None:
        entries.append(retuned_entry)
    if args.shell_projector_json.exists():
        entries.append(_correlated_entry("shell_projector_candidate", args.shell_projector_json))
    if args.shell_projector_continuum_live_json.exists():
        entries.append(
            _correlated_entry(
                "shell_projector_continuum_live",
                args.shell_projector_continuum_live_json,
            )
        )
    if args.shell_contact_joint_json.exists():
        entries.append(
            _correlated_entry(
                "shell_contact_joint_candidate",
                args.shell_contact_joint_json,
            )
        )
    if args.shell_pair_addon_json.exists():
        entries.append(
            _correlated_entry(
                "shell_pair_addon_candidate",
                args.shell_pair_addon_json,
            )
        )
    if args.shell_one_body_json.exists():
        entries.append(
            _correlated_entry(
                "shell_one_body_candidate",
                args.shell_one_body_json,
            )
        )
    if args.shell_radial_json.exists():
        entries.append(
            _correlated_entry(
                "shell_radial_candidate",
                args.shell_radial_json,
            )
        )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "entries": entries,
        "best_full_lane_entry": min(
            [entry for entry in entries if entry["entry_type"] != "one_body_benchmark"],
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "best_one_body_entry": min(
            [entry for entry in entries if entry["entry_type"] == "one_body_benchmark"],
            key=lambda row: (
                float(row["scores"].get("one_body_rms_relative_error", 1.0e9)),
                float(row["scores"].get("max_relative_error", 1.0e9)),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Best-Known Lane Scoreboard")
    print("=================================")
    for entry in entries:
        if "full_rms_relative_error" in entry["scores"]:
            score_text = f"full={entry['scores']['full_rms_relative_error']:.6f}"
        else:
            score_text = f"one-body={entry['scores']['one_body_rms_relative_error']:.6f}"
        print(f"- {entry['label']}: {score_text}.")
    print(
        f"- Best full-lane entry: {output_payload['best_full_lane_entry']['label']}."
    )
    print(f"- Wrote scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
