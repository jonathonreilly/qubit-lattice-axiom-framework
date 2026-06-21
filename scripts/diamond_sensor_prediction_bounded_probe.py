#!/usr/bin/env python3
"""Bounded audit probe for the Diamond/NV prediction note.

This wrapper keeps the experiment-facing prediction note at bounded scope:
it checks the note metadata, verifies the toy phase-lag card, and delegates
the load-bearing detector-map assertions to the ideal lock-in theorem runner.
It does not assert an NV transfer coefficient, lab noise model, or calibrated
gravity detectability claim.
"""

from __future__ import annotations

from pathlib import Path

from diamond_ideal_lockin_detector_theorem import run_checks as run_lockin_checks
from diamond_sensor_prediction_probe import (
    PredictionPoint,
    build_points,
    format_card,
)

AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIAMOND_SENSOR_PREDICTION_NOTE.md"
PREDICTION_RUNNER = "scripts/diamond_sensor_prediction_probe.py"
THIS_RUNNER = "scripts/diamond_sensor_prediction_bounded_probe.py"
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
    record(results, "no_closed_lab_prediction", "not** a closed lab prediction" in note_text, "explicit non-closure boundary")
    record(
        results,
        "no_calibrated_signal_budget",
        "not** a calibrated NV detectability" in note_text
        and "absolute signal budget remain open" in note_text,
        "explicit amplitude-budget boundary",
    )
    record(results, "prediction_probe_cited", PREDICTION_RUNNER in note_text, PREDICTION_RUNNER)
    record(results, "ideal_detector_runner_cited", IDEAL_RUNNER in note_text, IDEAL_RUNNER)

    points = build_points([100.0, 1_000.0, 10_000.0], [0.0, 0.1e-6, 1.0e-6])
    card = format_card(points)
    record(results, "card_standard_null", "quasi-static / instantaneous coupling gives Y ~ 0" in card, "standard null named")
    record(results, "card_toy_scaling", "Y/X ~ omega * tau" in card, "toy scaling law named")
    record(results, "zero_delay_phase_zero", PredictionPoint(1_000.0, 0.0).phase_deg == 0.0, "zero delay gives zero phase")

    phase_100 = PredictionPoint(100.0, 0.1e-6).phase_deg
    phase_1k = PredictionPoint(1_000.0, 0.1e-6).phase_deg
    phase_10k = PredictionPoint(10_000.0, 0.1e-6).phase_deg
    record(
        results,
        "phase_grows_with_frequency",
        0.0 < phase_100 < phase_1k < phase_10k,
        f"{phase_100:.3e} < {phase_1k:.3e} < {phase_10k:.3e}",
    )

    phase_short = PredictionPoint(1_000.0, 0.1e-6).phase_deg
    phase_long = PredictionPoint(1_000.0, 1.0e-6).phase_deg
    record(
        results,
        "phase_grows_with_delay",
        0.0 < phase_short < phase_long,
        f"{phase_short:.3e} < {phase_long:.3e}",
    )

    lockin_ok, lockin_lines = run_lockin_checks()
    record(results, "ideal_lockin_detector_assertions", lockin_ok, "; ".join(lockin_lines[:2]))

    pass_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - pass_count

    print("DIAMOND SENSOR PREDICTION BOUNDED PROBE")
    print(f"Target note: {NOTE.relative_to(ROOT)}")
    print(f"Prediction card runner: {PREDICTION_RUNNER}")
    print(f"Ideal detector theorem runner: {IDEAL_RUNNER}")
    print("")
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {detail}")
    print("")
    print(f"SUMMARY: PASS={pass_count} FAIL={fail_count}")
    print("Scope: bounded discriminator design only; no absolute NV/lab detectability claim.")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
