#!/usr/bin/env python3
"""Bounded audit probe for the Diamond/NV protocol note.

This wrapper checks that the protocol card stays at discriminator-protocol
scope and that the existing ideal lock-in detector theorem still supplies the
load-bearing `X`, `Y`, `phi`, and widefield phase-slope map. It does not assert
an NV transfer coefficient, a calibrated signal budget, or a closed lab
prediction.
"""

from __future__ import annotations

from pathlib import Path

from diamond_ideal_lockin_detector_theorem import run_checks as run_lockin_checks
from diamond_sensor_protocol_probe import SCAN_CLASSES, format_card

AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIAMOND_SENSOR_PROTOCOL_NOTE.md"
PROTOCOL_RUNNER = "scripts/diamond_sensor_protocol_probe.py"
THIS_RUNNER = "scripts/diamond_sensor_protocol_bounded_probe.py"
IDEAL_RUNNER = "scripts/diamond_ideal_lockin_detector_theorem.py"


def record(results: list[tuple[str, bool, str]], name: str, ok: bool, detail: str) -> None:
    results.append((name, ok, detail))


def main() -> int:
    results: list[tuple[str, bool, str]] = []

    note_text = NOTE.read_text(encoding="utf-8")
    record(results, "note_exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    record(results, "claim_type_bounded", "**Claim type:** bounded_theorem" in note_text, "bounded_theorem metadata present")
    record(results, "status_authority_independent", "**Status authority:** independent audit lane only." in note_text, "audit lane owns status")
    record(results, "runner_metadata", f"**Runner:** `{THIS_RUNNER}`" in note_text, THIS_RUNNER)
    record(results, "no_closed_nv_prediction", "not** a closed NV prediction" in note_text, "explicit non-closure boundary")
    record(
        results,
        "no_calibrated_signal_budget",
        "calibrated" in note_text and "signal budget" in note_text,
        "explicit signal-budget boundary",
    )
    record(results, "protocol_probe_cited", PROTOCOL_RUNNER in note_text, PROTOCOL_RUNNER)
    record(results, "ideal_detector_runner_cited", IDEAL_RUNNER in note_text, IDEAL_RUNNER)

    card = format_card()
    record(results, "card_standard_null", "Y ~ 0, phi ~ 0, flat phase" in card, "standard null named")
    record(results, "card_protocol_table", "| drive | separation | null X | null Y | null phi | proxy expectation |" in card, "protocol table present")
    record(results, "card_interpretation_rule", "survive calibration" in card and "pi control" in card, "calibration and pi-control rule present")
    record(results, "card_no_amplitude_budget", "not an absolute gravity amplitude budget" in card, "no amplitude-budget claim")
    record(results, "six_scan_classes", len(SCAN_CLASSES) == 6, f"scan classes={len(SCAN_CLASSES)}")

    all_nulls = all(row.null_x == "dominant" and row.null_y == "~0" and row.null_phi == "~0" for row in SCAN_CLASSES)
    record(results, "all_standard_null_columns", all_nulls, "all scan classes keep null Y/phi near zero")

    drive_order = [row.drive_band for row in SCAN_CLASSES]
    expected_drive_order = ["low", "low", "mid", "mid", "high", "high"]
    record(results, "drive_ordering_present", drive_order == expected_drive_order, ",".join(drive_order))

    high_far = next(
        (row for row in SCAN_CLASSES if row.drive_band == "high" and row.separation_band == "far"),
        None,
    )
    record(
        results,
        "high_far_best_candidate",
        high_far is not None and "best candidate" in high_far.proxy_expectation,
        high_far.proxy_expectation if high_far else "missing",
    )

    lockin_ok, lockin_lines = run_lockin_checks()
    record(results, "ideal_lockin_detector_assertions", lockin_ok, "; ".join(lockin_lines[:2]))

    pass_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - pass_count

    print("DIAMOND SENSOR PROTOCOL BOUNDED PROBE")
    print(f"Target note: {NOTE.relative_to(ROOT)}")
    print(f"Protocol card runner: {PROTOCOL_RUNNER}")
    print(f"Ideal detector theorem runner: {IDEAL_RUNNER}")
    print("")
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {detail}")
    print("")
    print(f"SUMMARY: PASS={pass_count} FAIL={fail_count}")
    print("Scope: bounded discriminator protocol only; no absolute NV/lab detectability claim.")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
