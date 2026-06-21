#!/usr/bin/env python3
"""Diamond/NV experiment-facing protocol probe.

This is a small theory harness, not an experimental simulator.

It prints the narrowest lab-facing protocol we can defend from the ideal
lock-in detector theorem and the cited retarded / wavefield proxy lanes:

- standard null: calibrated quasi-static coupling gives Y ~ 0 and flat phase
- ideal detector map: a phase-sensitive / lock-in readout should show a
  nonzero quadrature channel, a nonzero phase lag, and ideally a spatial phase
  ramp in widefield mode

The repo cannot yet support calibrated absolute gravity amplitudes, so the
output stays qualitative and discriminator-first.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

AUDIT_TIMEOUT_SEC = 120


@dataclass(frozen=True)
class ScanClass:
    drive_band: str
    separation_band: str
    null_x: str
    null_y: str
    null_phi: str
    proxy_expectation: str


@dataclass(frozen=True)
class AssertionResult:
    label: str
    passed: bool
    detail: str


SCAN_CLASSES = [
    ScanClass(
        drive_band="low",
        separation_band="near",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="weak / marginal phase-lag candidate",
    ),
    ScanClass(
        drive_band="low",
        separation_band="far",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="weak phase lag if the lane is real",
    ),
    ScanClass(
        drive_band="mid",
        separation_band="near",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="detectable quadrature becomes plausible",
    ),
    ScanClass(
        drive_band="mid",
        separation_band="far",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="stronger phase lag than near separation",
    ),
    ScanClass(
        drive_band="high",
        separation_band="near",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="stronger phase-sensitive response than low drive",
    ),
    ScanClass(
        drive_band="high",
        separation_band="far",
        null_x="dominant",
        null_y="~0",
        null_phi="~0",
        proxy_expectation="best candidate for coherent Y / phase ramp",
    ),
]


def protocol_assertions(card: str) -> list[AssertionResult]:
    assertions: list[AssertionResult] = []

    def expect(label: str, condition: bool, detail: str) -> None:
        assertions.append(AssertionResult(label=label, passed=condition, detail=detail))

    expect(
        "card names lock-in observables",
        all(token in card for token in ("quadrature Y", "phi = atan2(Y, X)", "widefield phase ramp")),
        "Y, phi, and widefield phase ramp are the protocol observables",
    )
    expect(
        "standard null is quasi-static",
        "quasi-static / instantaneous coupling -> Y ~ 0, phi ~ 0, flat phase" in card,
        "null baseline remains zero quadrature and flat phase after calibration",
    )
    expect(
        "proxy expectation is nonzero phase-sensitive response",
        "nonzero Y, nonzero phi, and a spatial phase ramp" in card,
        "bounded discriminator expectation is phase-sensitive rather than amplitude-budgeted",
    )
    expect(
        "ideal detector bridge is referenced",
        "scripts/diamond_ideal_lockin_detector_theorem.py" in card,
        "protocol depends on the ideal lock-in detector theorem",
    )
    expect(
        "minimal controls are explicit",
        all(
            token in card
            for token in (
                "drive off",
                "source retracted or dummy load",
                "pi reference flip",
                "static-source baseline",
            )
        ),
        "drive-off, retraction/dummy-load, pi-flip, and static controls are named",
    )
    expect(
        "protocol table has every scan class",
        all(f"| {row.drive_band} | {row.separation_band} |" in card for row in SCAN_CLASSES),
        "six drive/separation scan classes are printed",
    )
    expect(
        "all null columns stay bounded",
        all(row.null_x == "dominant" and row.null_y == "~0" and row.null_phi == "~0" for row in SCAN_CLASSES),
        "the table never turns the standard null into a positive signal",
    )
    expect(
        "high-far row is strongest candidate",
        any(
            row.drive_band == "high"
            and row.separation_band == "far"
            and "best candidate" in row.proxy_expectation
            for row in SCAN_CLASSES
        ),
        "qualitative ordering identifies high-drive/far-separation as strongest candidate",
    )
    expect(
        "interpretation demands calibration survival",
        "survive calibration" in card and "flip sign under the pi control" in card,
        "a hit must survive calibration and flip under the pi control",
    )
    expect(
        "absolute amplitude budget is disclaimed",
        "not an absolute gravity amplitude budget" in card,
        "the protocol does not claim calibrated detectability",
    )
    expect(
        "null-beating claim is disclaimed",
        "not a claim that the null is already beat" in card,
        "the protocol is a discriminator card, not an experimental result",
    )
    return assertions


def format_card() -> str:
    lines: list[str] = []
    lines.append("Diamond/NV phase-sensitive protocol card")
    lines.append("")
    lines.append("Observable:")
    lines.append("  lock-in quadrature Y, phase lag phi = atan2(Y, X), widefield phase ramp")
    lines.append("")
    lines.append("Standard null:")
    lines.append("  calibrated quasi-static / instantaneous coupling -> Y ~ 0, phi ~ 0, flat phase")
    lines.append("")
    lines.append("Cited proxy expectation:")
    lines.append("  a retarded / wave-like lane should produce nonzero Y, nonzero phi, and a spatial phase ramp")
    lines.append("")
    lines.append("Ideal detector bridge:")
    lines.append("  scripts/diamond_ideal_lockin_detector_theorem.py verifies the X/Y/phi map, controls, and widefield slope")
    lines.append("")
    lines.append("Minimal controls:")
    lines.append("  drive off; source retracted or dummy load; pi reference flip; static-source baseline")
    lines.append("")
    lines.append("Protocol table:")
    lines.append("| drive | separation | null X | null Y | null phi | proxy expectation |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for row in SCAN_CLASSES:
        lines.append(
            f"| {row.drive_band} | {row.separation_band} | {row.null_x} | {row.null_y} | {row.null_phi} | {row.proxy_expectation} |"
        )
    lines.append("")
    lines.append("Interpretation rule:")
    lines.append("  any real signal should survive calibration, flip sign under the pi control, and strengthen with drive and separation")
    lines.append("")
    lines.append("What this is not:")
    lines.append("  not an absolute gravity amplitude budget, and not a claim that the null is already beat")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a bounded diamond/NV experiment-facing protocol card."
    )
    return parser.parse_args()


def main() -> int:
    parse_args()
    card = format_card()
    print(card)
    print("")
    print("Protocol card assertions:")
    assertions = protocol_assertions(card)
    passed = sum(result.passed for result in assertions)
    failed = len(assertions) - passed
    for result in assertions:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
