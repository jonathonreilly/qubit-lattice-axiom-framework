#!/usr/bin/env python3
"""Compare no-correction, contact, and finite-range correlated operators."""

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


def _validation_entry(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return {
        "label": "no_correction",
        "source_json": str(path),
        "scores": payload["metrics"]["scores"],
        "relative_errors": payload["metrics"]["relative_errors"],
        "accepted": bool(payload["acceptance"]["accepted_on_full_lane"]),
        "operator_parameters": {},
    }


def _scan_entry(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    candidate = payload.get("accepted_candidate") or payload["best_by_full_rms"]
    return {
        "label": label,
        "source_json": str(path),
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "accepted": bool(candidate["acceptance"]["accepted_on_full_lane"]),
        "operator_parameters": {
            key: candidate[key]
            for key in ("contact_correction_strength", "pair_profile", "pair_radius", "pair_strength")
            if key in candidate
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_fixed_basis_validation.json",
    )
    parser.add_argument(
        "--contact-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_scan_refined.json",
    )
    parser.add_argument(
        "--finite-range-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_finite_range_pair_scan.json",
    )
    parser.add_argument(
        "--shell-projector-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_refine.json",
    )
    parser.add_argument(
        "--shell-contact-joint-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_contact_joint_refine.json",
    )
    parser.add_argument(
        "--shell-pair-addon-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_pair_addon_scan.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_operator_scoreboard.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries = [
        _validation_entry(args.validation_json),
        _scan_entry("contact", args.contact_json),
        _scan_entry("finite_range", args.finite_range_json),
    ]
    if args.shell_projector_json.exists():
        entries.append(_scan_entry("shell_projector", args.shell_projector_json))
    if args.shell_contact_joint_json.exists():
        entries.append(_scan_entry("shell_contact_joint", args.shell_contact_joint_json))
    if args.shell_pair_addon_json.exists():
        entries.append(_scan_entry("shell_pair_addon", args.shell_pair_addon_json))
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "entries": entries,
        "best_by_full_rms": min(
            entries,
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "accepted_entries": [entry for entry in entries if entry["accepted"]],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Correlated Operator Scoreboard")
    print("=====================================")
    for entry in entries:
        print(
            f"- {entry['label']}: "
            f"full={entry['scores']['full_rms_relative_error']:.6f} "
            f"accepted={'YES' if entry['accepted'] else 'NO'}."
        )
    print(
        f"- Best operator entry: {output_payload['best_by_full_rms']['label']}."
    )
    print(f"- Wrote correlated operator scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
