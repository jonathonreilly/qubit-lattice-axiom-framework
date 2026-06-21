#!/usr/bin/env python3
"""Bounded audit probe for the Diamond/NV phase-ramp signal-budget note.

The target note is intentionally a proxy/qualitative discriminator card. This
wrapper checks that boundary, verifies the existing proxy-budget and phase-ramp
cards, and delegates the detector-map assertions to the ideal lock-in theorem.
It does not assert a calibrated source-to-NV transfer coefficient, noise floor,
or lab detectability claim.
"""

from __future__ import annotations

from pathlib import Path

from diamond_ideal_lockin_detector_theorem import run_checks as run_lockin_checks
from diamond_phase_ramp_bridge_card import DEPTH_ROWS, STRENGTH_ROWS, build_report as build_ramp_report
from diamond_signal_budget_hardening import GEOMETRY, ROWS, build_report as build_budget_report

AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md"
THIS_RUNNER = "scripts/diamond_nv_phase_ramp_signal_budget_bounded_probe.py"
BUDGET_RUNNER = "scripts/diamond_signal_budget_hardening.py"
RAMP_RUNNER = "scripts/diamond_phase_ramp_bridge_card.py"
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
    record(results, "not_closed_signal_budget", "not** a closed signal budget" in note_text, "explicit non-closure boundary")
    record(results, "qualitative_not_absolute", "qualitative ordering structure" in note_text and "not to a calibrated absolute amplitude budget" in note_text, "qualitative budget boundary")
    record(results, "open_transfer_bridge", "source-to-NV coupling" in note_text and "calibrated amplitude/noise" in note_text, "open physical transfer bridge named")
    record(results, "budget_runner_cited", BUDGET_RUNNER in note_text or "proxy-budget" in note_text, BUDGET_RUNNER)
    record(results, "ramp_runner_cited", RAMP_RUNNER in note_text or "phase-ramp" in note_text, RAMP_RUNNER)
    record(results, "ideal_detector_runner_cited", IDEAL_RUNNER in note_text, IDEAL_RUNNER)

    budget_report = build_budget_report()
    ramp_report = build_ramp_report()
    record(results, "budget_report_transfer_gap", "missing transfer coefficient" in budget_report, "absolute NV transfer coefficient remains missing")
    record(results, "budget_geometry_fixed", GEOMETRY["seeds"] == 6 and GEOMETRY["h"] == 0.5, f"seeds={GEOMETRY['seeds']} h={GEOMETRY['h']}")
    record(results, "budget_zero_velocity_null", any(row.velocity == 0.0 and row.delta_y_vs_static == 0.0 and row.phase_lag_rad == 0.0 for row in ROWS), "zero-velocity proxy null present")
    record(results, "budget_signed_centroid", ROWS[0].delta_y_vs_static < 0.0 and ROWS[-1].delta_y_vs_static > 0.0, "centroid sign changes with velocity sign")
    record(results, "budget_phase_positive_nonzero", all(row.phase_lag_rad > 0.0 for row in ROWS if row.velocity != 0.0), "nonzero proxy phase lags are positive magnitudes")

    slopes = [abs(row.ramp_slope) for row in STRENGTH_ROWS]
    record(results, "ramp_strength_rows", len(STRENGTH_ROWS) == 4, f"strength rows={len(STRENGTH_ROWS)}")
    record(results, "ramp_slope_grows_with_strength", slopes == sorted(slopes), ",".join(f"{x:.4f}" for x in slopes))
    record(results, "ramp_r2_high", all(row.ramp_r2 >= 0.95 for row in STRENGTH_ROWS + DEPTH_ROWS), "all ramp R^2 >= 0.95")
    record(results, "ramp_report_proxy_scope", "not an absolute NV claim" in ramp_report, "proxy-level bridge card")

    lockin_ok, lockin_lines = run_lockin_checks()
    record(results, "ideal_lockin_detector_assertions", lockin_ok, "; ".join(lockin_lines[:2]))

    pass_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - pass_count

    print("DIAMOND NV PHASE-RAMP SIGNAL-BUDGET BOUNDED PROBE")
    print(f"Target note: {NOTE.relative_to(ROOT)}")
    print(f"Proxy budget runner: {BUDGET_RUNNER}")
    print(f"Phase-ramp bridge runner: {RAMP_RUNNER}")
    print(f"Ideal detector theorem runner: {IDEAL_RUNNER}")
    print("")
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {detail}")
    print("")
    print(f"SUMMARY: PASS={pass_count} FAIL={fail_count}")
    print("Scope: bounded proxy discriminator card only; no calibrated NV/lab detectability claim.")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
