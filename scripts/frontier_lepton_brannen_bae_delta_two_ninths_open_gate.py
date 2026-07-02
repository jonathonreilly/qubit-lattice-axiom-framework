#!/usr/bin/env python3
"""Verifier for the charged-lepton Brannen-BAE delta=2/9 open gate.

The runner checks only the conditional algebra and PDG comparator in
docs/LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md.
It does not derive the phase, the BAE coefficient, or the overall mass
scale.
"""

from __future__ import annotations

import math
from pathlib import Path

from lepton_brannen_boundary_checks_2026_06_13 import run_delta_boundary_checks, run_scale_boundary_checks


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS: {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"  FAIL: {name}" + (f" ({detail})" if detail else ""))


def brannen_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def koide_q(values: list[float]) -> float:
    return sum(v * v for v in values) / (sum(values) ** 2)


def main() -> int:
    print("Charged-lepton Brannen-BAE delta=2/9 open gate")
    print("=" * 72)

    delta = 2.0 / 9.0
    values_by_k = [brannen_ratio(k, delta) for k in range(3)]
    sorted_values = sorted(values_by_k)
    expected_sorted = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]

    print("\nConditional Brannen-BAE ratios at delta=2/9")
    for k, value in enumerate(values_by_k):
        print(f"  k={k}: {value:.15f}")

    check("all three conditional ratios are positive",
          all(v > 0.0 for v in values_by_k))
    check("sorted electron-like ratio matches independent target",
          abs(sorted_values[0] - expected_sorted[0]) < 1e-14,
          f"{sorted_values[0]:.15f}")
    check("sorted muon-like ratio matches independent target",
          abs(sorted_values[1] - expected_sorted[1]) < 1e-14,
          f"{sorted_values[1]:.15f}")
    check("sorted tau-like ratio matches independent target",
          abs(sorted_values[2] - expected_sorted[2]) < 1e-14,
          f"{sorted_values[2]:.15f}")
    check("Brannen root-of-unity sum gives sum ratios = 3",
          abs(sum(values_by_k) - 3.0) < 1e-14,
          f"sum={sum(values_by_k):.15f}")
    check("Koide Q is 2/3 at delta=2/9",
          abs(koide_q(values_by_k) - 2.0 / 3.0) < 1e-14,
          f"Q={koide_q(values_by_k):.15f}")

    # The Koide identity is phase-independent after the sqrt(2)
    # coefficient is assumed; this prevents overreading Q as evidence
    # for delta=2/9.
    for probe_delta in (0.0, 0.1, 0.5, 1.0):
        probe_values = [brannen_ratio(k, probe_delta) for k in range(3)]
        check(f"Koide Q remains 2/3 at probe delta={probe_delta}",
              abs(koide_q(probe_values) - 2.0 / 3.0) < 1e-14)

    print("\nPDG comparator")
    m_e = 0.5109989461
    m_mu = 105.6583755
    m_tau = 1776.86
    sqrt_m = [math.sqrt(m_e), math.sqrt(m_mu), math.sqrt(m_tau)]
    a_pdg = sum(sqrt_m) / 3.0
    pdg_ratios = sorted(v / a_pdg for v in sqrt_m)
    deviations = [pdg - pred for pdg, pred in zip(pdg_ratios, sorted_values)]

    cos_delta_pdg = (max(sqrt_m) - a_pdg) / (a_pdg * math.sqrt(2.0))
    delta_pdg = math.acos(cos_delta_pdg)
    delta_gap = delta_pdg - delta

    print(f"  a_PDG   = {a_pdg:.15f} sqrt(MeV)")
    print(f"  a_PDG^2 = {a_pdg * a_pdg:.15f} MeV")
    print(f"  delta_PDG = {delta_pdg:.15f}")
    print(f"  delta_PDG - 2/9 = {delta_gap:.15f}")
    print("  ratio deviations:")
    for label, dev in zip(("electron", "muon", "tau"), deviations):
        print(f"    {label}: {dev:+.15e}")

    check("PDG Koide Q is within 1e-5 of 2/3",
          abs((m_e + m_mu + m_tau) / (sum(sqrt_m) ** 2) - 2.0 / 3.0) < 1e-5)
    check("PDG-extracted phase is within 1e-4 rad of 2/9",
          abs(delta_gap) < 1e-4,
          f"gap={delta_gap:.15e}")
    check("electron ratio comparator within 3e-5 absolute",
          abs(deviations[0]) < 3e-5,
          f"dev={deviations[0]:+.15e}")
    check("muon ratio comparator within 3e-5 absolute",
          abs(deviations[1]) < 3e-5,
          f"dev={deviations[1]:+.15e}")
    check("tau ratio comparator within 3e-5 absolute",
          abs(deviations[2]) < 3e-5,
          f"dev={deviations[2]:+.15e}")
    check("a_PDG is an observational scale residual near 17.72 sqrt(MeV)",
          17.7 < a_pdg < 17.8,
          "not derived")
    check("a_PDG squared is near 313.84 MeV",
          313.0 < a_pdg * a_pdg < 315.0,
          "not derived")

    root = Path(__file__).resolve().parents[1]
    for ok in run_delta_boundary_checks(root, lambda n, c, d="": (check(n, c, d) or c), "downstream delta boundary"):
        pass
    for ok in run_scale_boundary_checks(root, lambda n, c, d="": (check(n, c, d) or c), "downstream scale boundary"):
        pass

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: lepton Brannen-BAE delta=2/9 open gate failed checks.")
        return 1
    print(
        "VERDICT: lepton Brannen-BAE delta=2/9 open gate verified; "
        "phase and scale remain open, with downstream bounded/no-go anchors now checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
