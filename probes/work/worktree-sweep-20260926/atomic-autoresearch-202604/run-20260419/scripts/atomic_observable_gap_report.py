#!/usr/bin/env python3
"""Report model-vs-actual observable gaps for a helium readout."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402
from scripts.atomic_observable_metrics import helium_readout_metrics  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
        help="helium readout JSON to compare against actuals",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_observable_gap_report.json",
        help="machine-readable gap report path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    readout_payload = read_json(args.readout_json)
    metrics = helium_readout_metrics(readout_payload)

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_readout_json": str(args.readout_json),
        "selector_summary": readout_payload["selector_summary"],
        "model_observables": metrics["model_observables"],
        "gap_rows": metrics["gap_rows"],
        "scores": metrics["scores"],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Observable Gap Report")
    print("============================")
    for row in output_payload["gap_rows"]:
        print(
            f"- {row['observable']}: "
            f"model={row['model_value']:.12f} "
            f"actual={row['actual_value']:.12f} "
            f"delta={row['absolute_delta']:+.12f} "
            f"rel={row['relative_error']:.4%}."
        )
    print(
        f"- Full RMS relative error: "
        f"{output_payload['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote gap report to {args.write_json}.")


if __name__ == "__main__":
    main()
