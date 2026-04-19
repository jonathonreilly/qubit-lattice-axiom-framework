#!/usr/bin/env python3
"""Bounded bridge from the retained polarity lane to the bound-state / d=3 surface."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import (  # noqa: E402
    AtomicLaneEnsembleSummaryRow,
    DEFAULT_OUTPUT_ROOT,
    build_bound_state_baseline,
    compare_atomic_lane_to_bound_state,
    read_json,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mechanism-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_mechanism.json",
        help="polarity mechanism JSON",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_bridge.json",
        help="bridge output JSON path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    mechanism_payload = read_json(args.mechanism_json)
    summary_rows = [
        AtomicLaneEnsembleSummaryRow(**row_payload)
        for row_payload in mechanism_payload["summary_rows"]
    ]
    bound_state_baseline = build_bound_state_baseline()
    comparison_payload = compare_atomic_lane_to_bound_state(
        summary_rows=summary_rows,
        mechanism_rows=mechanism_payload["mechanism_rows"],
        bound_state_baseline=bound_state_baseline,
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "bridge_performed": True,
        "comparison": comparison_payload,
        "mechanism_json": str(args.mechanism_json),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Polarity Bridge")
    print("======================")
    print(
        f"- Bounded companion evidence: "
        f"{'YES' if comparison_payload['bounded_companion_evidence'] else 'NO'}."
    )
    print("- Dimension-selection claim support: NO.")
    print(f"- Wrote bridge output to {args.write_json}.")


if __name__ == "__main__":
    main()
