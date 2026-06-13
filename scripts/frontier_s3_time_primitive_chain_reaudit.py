#!/usr/bin/env python3
"""Review helper for S3_TIME_PRIMITIVE_CHAIN_NOTE.

The runner verifies the narrow repair surface:

* the row cites the Route-2 readout/time authorities;
* the E-channel naturality no-go supplies the repair-requested admissibility
  boundary;
* the current restricted carrier/readout class leaves rho_E free, so the
  primitive chain is an open gate rather than a positive readout theorem.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXACT_TOL = 1.0e-12

PASS_COUNT = 0
FAIL_COUNT = 0

SOURCE_BOUNDARY_REQUIRED_PHRASES = [
    "Downstream source-boundary firewall",
    "Route-2 carrier/readout/time authority chain",
    "admissibility boundary",
    "current restricted",
    "leaves `beta_E / alpha_E` free",
    "derive an E-center endpoint ratio",
    "do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`",
    "unique readout-to-slice time-coupling theorem",
    "final Einstein/Regge identification",
    "exhaustive no-go",
    "positive readout theorem",
]


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def reduced_map(rho_e: Fraction) -> np.ndarray:
    rho = float(rho_e)
    return np.array(
        [
            [1.0, 0.0, rho, 0.0],
            [0.0, -2.0, 0.0, 2.0],
        ],
        dtype=float,
    )


def e_center_lift(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def center_te_ratio(rho_e: Fraction) -> Fraction:
    # Granted T side: q_T = 5/6 and shell T/E = -2.
    return Fraction(-2, 1) * Fraction(5, 6) / e_center_lift(rho_e)


def main() -> int:
    note = DOCS / "S3_TIME_PRIMITIVE_CHAIN_NOTE.md"
    readout = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    time = DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
    no_go = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"

    print("S3 primitive-chain open-gate re-audit helper")
    print("=" * 72)

    for path in (note, readout, time, no_go):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note_text = note.read_text(encoding="utf-8")
    readout_text = readout.read_text(encoding="utf-8")
    time_text = time.read_text(encoding="utf-8")
    no_go_text = no_go.read_text(encoding="utf-8")

    print()
    print("A. Direct authority checks")
    print("-" * 72)
    check("S3 row cites exact readout map note", readout.name in note_text)
    check("S3 row cites exact time-coupling note", time.name in note_text)
    check("S3 row cites E-channel naturality no-go", no_go.name in note_text)
    check("readout authority names rho_E as missing map entry", "beta_E / alpha_E = 21/4" in readout_text)
    check("time authority says unique time coupling is blocked by readout", "does not yet exist as a unique theorem" in time_text)
    check("naturality no-go states rho_E remains free", "remains a free parameter" in no_go_text)

    print()
    print("B. Reduced-family algebra")
    print("-" * 72)
    data = restricted_readout_data()
    e_shell = data.carrier_e_shell
    e_center = data.carrier_e_center
    expected_shell = np.array([1.0, 0.0, 0.0, 0.0])
    expected_center = np.array([1.0, 0.0, 1.0 / 6.0, 0.0])

    check("E-shell carrier column is exact", np.max(np.abs(e_shell - expected_shell)) < EXACT_TOL, str(e_shell))
    check("E-center carrier column is exact", np.max(np.abs(e_center - expected_center)) < EXACT_TOL, str(e_center))

    rho_zero = Fraction(0, 1)
    rho_target = Fraction(21, 4)
    p_zero = reduced_map(rho_zero)
    p_target = reduced_map(rho_target)
    shell_zero = p_zero @ e_shell
    shell_target = p_target @ e_shell
    center_zero = p_zero @ e_center
    center_target = p_target @ e_center

    check("rho_E=0 and rho_E=21/4 agree on shell normalization", np.max(np.abs(shell_zero - shell_target)) < EXACT_TOL)
    check("rho_E=0 and rho_E=21/4 differ on center lift", abs(center_zero[0] - center_target[0]) > 0.5, f"{center_zero[0]:.6f} vs {center_target[0]:.6f}")
    check("rho_E=21/4 gives q_E=15/8", e_center_lift(rho_target) == Fraction(15, 8), str(e_center_lift(rho_target)))
    check("rho_E=0 gives q_E=1", e_center_lift(rho_zero) == Fraction(1, 1), str(e_center_lift(rho_zero)))
    check("rho_E=21/4 is equivalent to center T/E=-8/9 under granted T side", center_te_ratio(rho_target) == Fraction(-8, 9), str(center_te_ratio(rho_target)))
    check("rho_E=0 is admissible but not the endpoint target", center_te_ratio(rho_zero) != Fraction(-8, 9), str(center_te_ratio(rho_zero)))

    print()
    print("C. Scope firewall")
    print("-" * 72)
    check("S3 row states current objects do not uniquely select 21/4", "do not uniquely select" in note_text)
    check("S3 row keeps positive target open", "new E-center/source/readout" in note_text)
    check("S3 row remains open_gate rather than positive theorem", "open_gate" in note_text)
    check("S3 row does not claim beta_E derivation", "does not uniquely select `beta_E / alpha_E = 21/4`" in note_text)
    check("S3 row contains downstream source-boundary firewall", all(phrase in note_text for phrase in SOURCE_BOUNDARY_REQUIRED_PHRASES))
    check(
        "S3 firewall forbids readout/time-coupling/E-channel promotion",
        "do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`" in note_text
        and "do not cite it as a unique readout-to-slice time-coupling theorem" in note_text
        and "do not promote the primitive chain from open gate to positive theorem" in note_text,
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: S3 primitive chain is an open gate backed by Route-2 non-selection.")
        return 0
    print("VERDICT: S3 primitive-chain repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
