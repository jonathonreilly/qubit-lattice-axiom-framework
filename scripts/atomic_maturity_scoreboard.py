#!/usr/bin/env python3
"""Compare retained-lane milestone readouts on a common scorecard."""

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


def _parse_entry(raw_value: str) -> tuple[str, Path]:
    label, raw_path = raw_value.split("=", 1)
    return label, Path(raw_path)


def _entry_summary(label: str, readout_payload: dict[str, Any], source_path: Path) -> dict[str, Any]:
    metrics = helium_readout_metrics(readout_payload)
    helium = readout_payload["helium_two_electron"]
    basis_sweep = list(helium.get("basis_sweep", []))
    spatial_orbital_count = helium.get("spatial_orbital_count")
    if spatial_orbital_count is None and basis_sweep:
        spatial_orbital_count = basis_sweep[-1].get("spatial_orbital_count")
    virtual_orbital_count = helium.get("virtual_orbital_count")
    if virtual_orbital_count is None:
        negative_orbital_count = helium.get("negative_orbital_count")
        if negative_orbital_count is None:
            negative_orbital_count = len(helium.get("singlet_orbital_occupancies", []))
        if spatial_orbital_count is not None:
            virtual_orbital_count = max(
                0,
                int(spatial_orbital_count) - int(negative_orbital_count),
            )
        else:
            virtual_orbital_count = 0
    return {
        "label": label,
        "source_readout_json": str(source_path),
        "spatial_orbital_count": (
            int(spatial_orbital_count) if spatial_orbital_count is not None else None
        ),
        "virtual_orbital_count": int(virtual_orbital_count),
        "scores": metrics["scores"],
        "relative_errors": metrics["relative_errors"],
        "model_observables": metrics["model_observables"],
    }


def _improvement_vs_baseline(
    summary: dict[str, Any],
    baseline: dict[str, Any],
) -> dict[str, float]:
    output: dict[str, float] = {}
    for key, value in summary["scores"].items():
        output[f"{key}_delta"] = float(value) - float(baseline["scores"][key])
    for key, value in summary["relative_errors"].items():
        output[f"{key}_delta"] = float(value) - float(baseline["relative_errors"][key])
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--entry",
        action="append",
        default=[
            f"uv_core={DEFAULT_OUTPUT_ROOT / 'atomic_helium_readout_uv_core.json'}",
            f"virtual_32={DEFAULT_OUTPUT_ROOT / 'atomic_helium_readout_virtual_basis.json'}",
            f"virtual_64={DEFAULT_OUTPUT_ROOT / 'atomic_helium_readout_virtual_basis_tail.json'}",
        ],
        help="comparison entry in label=/abs/or/relative/path.json form",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_maturity_scoreboard.json",
        help="machine-readable maturity scoreboard path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries: list[dict[str, Any]] = []
    for raw_entry in args.entry:
        label, path = _parse_entry(raw_entry)
        entries.append(_entry_summary(label, read_json(path), path))

    baseline = entries[0]
    for entry in entries:
        entry["improvement_vs_baseline"] = _improvement_vs_baseline(entry, baseline)

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "entries": entries,
        "baseline_label": baseline["label"],
        "best_by_full_rms": min(
            entries,
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "best_by_helium_rms": min(
            entries,
            key=lambda row: (
                float(row["scores"]["helium_rms_relative_error"]),
                float(row["scores"]["full_rms_relative_error"]),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Maturity Scoreboard")
    print("==========================")
    for entry in entries:
        print(
            f"- {entry['label']}: "
            f"spatial={entry['spatial_orbital_count']} "
            f"virtual={entry['virtual_orbital_count']} "
            f"full={entry['scores']['full_rms_relative_error']:.6f} "
            f"helium={entry['scores']['helium_rms_relative_error']:.6f}."
        )
    print(
        f"- Best full-RMS entry: "
        f"{output_payload['best_by_full_rms']['label']}."
    )
    print(f"- Wrote scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
