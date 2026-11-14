#!/usr/bin/env python3
"""
Lane 1 B2 diagnostic: the pure-gauge payload does not fix dynamical screening.

Question:
  Does the current beta=6.0 pure-gauge / quenched string-tension payload fix
  the rough 0.96 screening factor that the N_f=2+1 dynamical screening budget
  for sqrt(sigma) uses?

Answer on the 2026-04-29 repo surface (a diagnostic, not a no-go theorem):
  No. The payload numbers do not involve the factor, so they leave it open.
  The factor must come from a supplied determinant input. Ways to supply it
  include an N_f=2+1 determinant ensemble, a framework derivation of the
  determinant correction, and an explicitly budgeted external comparator;
  that list is not exhaustive.

What the checks are:
  - Part 1 and Part 4 text checks confirm phrases in the cited notes and in
    the confinement runner source.
  - Parts 2 to 4 compute on chosen examples: a supplied factor family, a toy
    determinant bank and chosen sea masses. Two in-run controls show that a
    degenerate factor family and a decoupled (very heavy) sea are rejected.
  - Part 5 prints a dated checklist of missing inputs as uncounted
    `SUPPLIED CHECKLIST:` lines. Those items are stipulated, not computed.
None of this is an exhaustive physical obstruction.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/lanes/open_science/01_HADRON_MASS_PROGRAM_OPEN_LANE_2026-04-26.md",
    "docs/HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md",
    "docs/CONFINEMENT_STRING_TENSION_NOTE.md",
    "scripts/frontier_confinement_string_tension.py",
)

PASS_COUNT = 0
FAIL_COUNT = 0

np.set_printoptions(precision=8, suppress=True, linewidth=120)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


SQRT_SIGMA_QUENCHED_MEV = 484.0
ROUGH_SCREENING_FACTOR = 0.96
PDG_COMPARATOR_MEV = 440.0
SUPPLIED_FACTOR_FAMILY = (0.90, 0.94, ROUGH_SCREENING_FACTOR, 1.00)
# Supplied scale-setting constants used by the confinement note's Method 2.
R0_FM = 0.472
HBARC_MEV_FM = 197.327


def pure_gauge_payload() -> tuple[float, float, float, float]:
    """Current Method-2 payload before the sea-fermion determinant enters."""
    beta = 6.0
    r0_over_a = 5.37
    sigma_a2 = 0.0465
    plaquette = 0.5934
    return beta, r0_over_a, sigma_a2, plaquette


def screened_readout(screening_factor: float) -> float:
    return SQRT_SIGMA_QUENCHED_MEV * screening_factor


def quenched_readout_from_payload(payload: tuple[float, float, float, float]) -> float:
    """sqrt(sigma) in MeV from the payload alone; the factor is not an input."""
    _beta, r0_over_a, sigma_a2, _plaquette = payload
    return math.sqrt(sigma_a2) * r0_over_a / R0_FM * HBARC_MEV_FM


def relative_spread(values: list[float]) -> float:
    return (max(values) - min(values)) / (sum(values) / len(values))


def supplied(item: str) -> None:
    print(f"  SUPPLIED CHECKLIST: {item}")


def determinant_factor(singular_values: np.ndarray, masses: tuple[float, ...]) -> float:
    factor = 1.0
    for mass in masses:
        factor *= float(np.prod(singular_values**2 + mass**2))
    return factor


def reweighted_observable(
    gauge_weights: np.ndarray,
    observable: np.ndarray,
    singular_value_bank: np.ndarray,
    masses: tuple[float, ...] | None,
) -> float:
    if masses is None:
        weights = gauge_weights
    else:
        dets = np.array([determinant_factor(vals, masses) for vals in singular_value_bank])
        weights = gauge_weights * dets
    return float(np.sum(weights * observable) / np.sum(weights))


def test_authority_text() -> None:
    print("\n" + "=" * 88)
    print("PART 1: CITED TEXT NAMES B2 AS THE LOAD-BEARING GAP (TEXT CHECKS)")
    print("=" * 88)

    lane = read("docs/lanes/open_science/01_HADRON_MASS_PROGRAM_OPEN_LANE_2026-04-26.md")
    audit = read("docs/HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md")
    confinement = read("docs/CONFINEMENT_STRING_TENSION_NOTE.md")
    runner = read("scripts/frontier_confinement_string_tension.py")

    check(
        "Lane 1 file names B2 as the current highest-leverage sqrt(sigma) gate",
        "B2" in lane and "quenched-to-dynamical" in lane and "screening budget" in lane,
    )
    check(
        "Audit note identifies B2 as the dominant numerical residual",
        "(B2)" in audit and "dynamical screening" in audit and "dominant" in audit,
    )
    check(
        "Audit note names a proper N_f=2+1 lattice calculation as one route",
        "proper `N_f = 2+1` lattice" in audit and "beta = 6.0" in audit,
    )
    check(
        "Confinement note says the current correction is rough",
        "rough screening correction" in confinement or "rough central estimate" in confinement,
    )
    check(
        "Current confinement runner is pure-gauge at beta=6.0",
        "Pure-gauge SU(3) Monte Carlo" in runner and "beta = 6.0" in runner,
    )


def test_screening_factor_degeneracy() -> list[float]:
    print("\n" + "=" * 88)
    print("PART 2: ONE PURE-GAUGE PAYLOAD, A SUPPLIED FAMILY OF SCREENING FACTORS")
    print("=" * 88)

    payload = pure_gauge_payload()
    factors = list(SUPPLIED_FACTOR_FAMILY)
    readouts = [screened_readout(factor) for factor in factors]
    quenched = quenched_readout_from_payload(payload)

    print(f"  pure-gauge payload = beta, r0/a, sigma_a2, plaquette = {payload}")
    print(f"  quenched sqrt(sigma) from the payload = {quenched:.2f} MeV (no factor enters)")
    for factor, value in zip(factors, readouts):
        print(f"  f_screen={factor:.2f} -> sqrt(sigma)={value:.2f} MeV")

    check(
        "The payload alone gives the 484 MeV quenched readout; the factor is not an input",
        abs(quenched - SQRT_SIGMA_QUENCHED_MEV) < 1.0,
        f"computed {quenched:.2f} MeV from sqrt(sigma a^2) (r0/a) / r0",
    )
    check(
        "Different factors in the supplied family give materially different readouts",
        max(readouts) - min(readouts) > 40.0,
        f"spread={max(readouts) - min(readouts):.2f} MeV",
    )
    check(
        "Distinct factors in the supplied family give distinct readouts from one payload",
        ROUGH_SCREENING_FACTOR in factors and len(set(readouts)) == len(factors),
    )
    check(
        "The comparator-implied factor is distinct from the rough factor",
        abs(PDG_COMPARATOR_MEV / SQRT_SIGMA_QUENCHED_MEV - ROUGH_SCREENING_FACTOR) > 0.04,
        f"440/484={PDG_COMPARATOR_MEV / SQRT_SIGMA_QUENCHED_MEV:.4f}",
    )
    degenerate = [screened_readout(ROUGH_SCREENING_FACTOR) for _ in factors]
    check(
        "Control: a degenerate family (every factor 0.96) is rejected by the spread test",
        not (max(degenerate) - min(degenerate) > 40.0) and len(set(degenerate)) == 1,
        "the spread test can fail; the witness is the supplied family, not the payload",
    )
    return readouts


def test_determinant_reweighting_is_load_bearing() -> None:
    print("\n" + "=" * 88)
    print("PART 3: SEA-FERMION DETERMINANT DATA CHANGE THE MEASURE")
    print("=" * 88)

    gauge_weights = np.array([1.0, 0.72, 0.46, 0.33])
    local_sigma_a2 = np.array([0.049, 0.0465, 0.043, 0.039])
    singular_value_bank = np.array(
        [
            [0.22, 0.35, 0.51, 0.73],
            [0.12, 0.19, 0.31, 0.58],
            [0.05, 0.09, 0.18, 0.41],
            [0.015, 0.04, 0.11, 0.29],
        ]
    )

    quenched = reweighted_observable(gauge_weights, local_sigma_a2, singular_value_bank, masses=None)
    light_sea = reweighted_observable(gauge_weights, local_sigma_a2, singular_value_bank, masses=(0.02, 0.03, 0.10))
    heavier_sea = reweighted_observable(gauge_weights, local_sigma_a2, singular_value_bank, masses=(0.50, 0.60, 0.70))

    decoupled = reweighted_observable(gauge_weights, local_sigma_a2, singular_value_bank, masses=(100.0, 100.0, 100.0))

    print("  (toy bank: chosen gauge weights, observables, singular values and sea masses)")
    print(f"  quenched <sigma a^2>       = {quenched:.8f}")
    print(f"  light-sea <sigma a^2>      = {light_sea:.8f}")
    print(f"  heavier-sea <sigma a^2>    = {heavier_sea:.8f}")
    print(f"  decoupled-sea <sigma a^2>  = {decoupled:.8f}")

    check(
        "In the toy bank, determinant weights change the measured observable",
        abs(light_sea - quenched) > 1.0e-3,
        f"delta={light_sea - quenched:+.6f}",
    )
    check(
        "In the toy bank, changing sea masses changes the determinant-weighted observable",
        abs(light_sea - heavier_sea) > 1.0e-4,
        f"delta={light_sea - heavier_sea:+.6f}",
    )
    check(
        "Control: a decoupled sea (masses 100) is rejected by the determinant-change test",
        not (abs(decoupled - quenched) > 1.0e-3),
        f"delta={decoupled - quenched:+.2e}; near-constant determinants leave the measure unchanged",
    )


def test_volume_and_budget_boundary(readouts: list[float]) -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE CURRENT FINITE RUNNER IS NOT A DYNAMICAL EXTRACTION")
    print("=" * 88)

    confinement_note = read("docs/CONFINEMENT_STRING_TENSION_NOTE.md")
    confinement_runner = read("scripts/frontier_confinement_string_tension.py")

    current_linear_size = 4
    target_linear_size = 16
    current_links = current_linear_size**4 * 4
    target_links = target_linear_size**4 * 4
    ratio = target_links / current_links

    check(
        "Confinement note says quantitative extraction needs larger volumes",
        "Quantitative" in confinement_note and "requires volumes" in confinement_note and "16" in confinement_note,
    )
    check(
        "Current runner uses L=4 for a qualitative pure-gauge check",
        "L = 4" in confinement_runner and "Pure-gauge SU(3) Monte Carlo" in confinement_runner,
    )
    check(
        "A 16^4 check has much larger link count than the current 4^4 runner",
        math.isclose(ratio, 256.0),
        f"link-count ratio={ratio:.0f}x",
    )
    spread = relative_spread(readouts)
    check(
        "The supplied factor family spreads the readout by more than one percent",
        spread > 0.01,
        f"relative spread of the Part 2 readouts = {spread:.4f}",
    )


def test_status_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 5: DATED CHECKLIST OF MISSING INPUTS (PRINTED, NOT COUNTED)")
    print("=" * 88)
    print("  These items describe the 2026-04-29 repo surface. They are stipulated,")
    print("  not computed by this runner, and they are not counted in the summary.")

    supplied("no sea-fermion determinant input is in the B2 payload")
    supplied("no N_f=2+1 beta=6.0 ensemble is in the B2 payload")
    supplied("no sea-mass specification is in the B2 payload")
    supplied("no large-volume Creutz-ratio extraction is in the B2 payload")
    supplied("consequence on that surface: the payload alone does not fix the factor")
    print("  Routes that would supply a determinant input include a dynamical ensemble,")
    print("  a framework derivation and an explicitly budgeted external comparator;")
    print("  the list is not exhaustive.")


def main() -> int:
    print("=" * 88)
    print("LANE 1 B2: DYNAMICAL SCREENING BOUNDARY")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the current pure-gauge beta=6.0 payload fix the rough 0.96 factor")
    print("  used for the N_f=2+1 dynamical screening budget of sqrt(sigma)?")
    print()
    print("Diagnostic (not a no-go theorem):")
    print("  The payload numbers do not involve the factor. On the 2026-04-29")
    print("  surface the factor is a supplied input, and the checks below use")
    print("  chosen examples.")

    test_authority_text()
    readouts = test_screening_factor_degeneracy()
    test_determinant_reweighting_is_load_bearing()
    test_volume_and_budget_boundary(readouts)
    test_status_firewall()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    print("Counted: text checks of the cited notes and runner, arithmetic on the")
    print("supplied factor family and toy determinant bank, and two controls.")
    print("Not counted: the Part 5 SUPPLIED CHECKLIST lines.")

    if FAIL_COUNT:
        print("B2 diagnostic runner failed; do not use the note.")
        return 1

    print("Result: B2 remains open; the current pure-gauge payload does not fix the factor.")
    print("A determinant input is needed: for example an N_f=2+1 ensemble, a framework")
    print("derivation of the determinant correction, or an explicitly budgeted comparator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
