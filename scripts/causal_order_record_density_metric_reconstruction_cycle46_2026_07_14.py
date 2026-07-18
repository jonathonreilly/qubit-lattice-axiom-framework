#!/usr/bin/env python3
"""Cycle 46: exact algebra and scope gate for order+number metric recovery."""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/CAUSAL_ORDER_RECORD_DENSITY_METRIC_RECONSTRUCTION_CYCLE46_NOTE_2026-07-14.md"

passed = 0
failed = 0


def check(label: str, condition: bool) -> None:
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS {label}")
    else:
        failed += 1
        print(f"FAIL {label}")


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def minkowski_norm(v: tuple[float, ...]) -> float:
    return -(v[0] ** 2) + sum(x * x for x in v[1:])


text = NOTE.read_text(encoding="utf-8")
normalized_text = " ".join(text.split())

print("CYCLE 46 — CAUSAL ORDER + RECORD DENSITY METRIC RECONSTRUCTION")

# Conformal rescaling preserves causal type and scales d-volume by Omega**d.
vectors = [
    (2.0, 1.0, 0.0, 0.0),
    (1.0, 1.0, 0.0, 0.0),
    (1.0, 2.0, 0.0, 0.0),
    (3.0, 1.0, 1.0, 1.0),
]
for omega in (0.25, 0.5, 1.0, 2.0, 7.0):
    for i, vector in enumerate(vectors):
        base = minkowski_norm(vector)
        scaled = omega * omega * base
        check(
            f"causal type invariant Omega={omega} vector={i}",
            (base < 0) == (scaled < 0)
            and (base == 0) == (scaled == 0)
            and (base > 0) == (scaled > 0),
        )

for dimension in (2, 3, 4, 5):
    for omega in (0.25, 0.5, 1.0, 2.0, 3.0):
        # det(Omega^2 g) = Omega^(2d) det(g); sqrt absolute determinant
        # therefore scales by Omega^d.
        determinant_ratio = omega ** (2 * dimension)
        volume_ratio = math.sqrt(determinant_ratio)
        check(
            f"volume scaling d={dimension} Omega={omega}",
            close(volume_ratio, omega**dimension),
        )

# A fixed density removes the conformal factor; a transformed density leaves
# the counted measure invariant and exhibits the exact underdetermination when
# density is not fixed.
for dimension in (2, 3, 4):
    rho = 11.0
    base_volume = 13.0
    base_measure = rho * base_volume
    for omega in (0.5, 1.0, 2.0, 5.0):
        scaled_volume = omega**dimension * base_volume
        compensating_rho = rho / omega**dimension
        check(
            f"unknown-density degeneracy d={dimension} Omega={omega}",
            close(compensating_rho * scaled_volume, base_measure),
        )
        fixed_density_same_measure = close(rho * scaled_volume, base_measure)
        check(
            f"fixed density forces Omega=1 d={dimension} Omega={omega}",
            fixed_density_same_measure == close(omega, 1.0),
        )

# A four-event diamond has four volume events but a maximal chain of three.
events = {"a", "b", "c", "d"}
relations = {("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("a", "d")}
chains = [
    ("a", "b", "d"),
    ("a", "c", "d"),
]
check("diamond has four total events", len(events) == 4)
check("diamond maximal chain has three events", max(map(len, chains)) == 3)
check("parallel pair is incomparable", ("b", "c") not in relations and ("c", "b") not in relations)
check("volume count differs from clock-chain count", len(events) != max(map(len, chains)))

# Required scope and no-go-discipline markers.
required_phrases = [
    "positive conditional theorem",
    "known uniform density",
    "dimension at least three",
    "causal faithfulness",
    "volume faithfulness",
    "dVol_g' = Omega^d dVol_g",
    "rho -> rho / Omega^d",
    "count along one clock chain is not spacetime volume",
    "does not select the microscopic law",
    "does not prove an Einstein equation",
    "does not by itself choose the density",
    "strict nearest-neighbor",
    "live constitutional cut: unchanged (HOLD; no edit)",
    "N1 — Alternative-route enumeration",
    "N2 — Wall-independence audit",
    "N3 — Hidden-wall scan",
    "N4 — Exact residual matching",
    "N5 — Resolution and rhetoric audit",
    "N6 — Partial-closure paths",
    "N7 — Strongest surviving steelman",
    "N8 — Cross-cycle echo",
    "10.1103/PhysRevLett.59.521",
    "10.1063/1.523436",
    "10.1063/1.522874",
]
for phrase in required_phrases:
    check(f"note contains {phrase!r}", phrase in normalized_text)

check("N1 marks at least eight routes ATTEMPTED", normalized_text.count("ATTEMPTED") >= 8)
check("N1 keeps at least two routes LIVE / UNTESTED", normalized_text.count("LIVE / UNTESTED") >= 2)
check("N1 rules out no live route rhetorically", "No live route is rhetorically ruled out." in text)
for route in (
    "causal order alone",
    "order plus fixed volume measure",
    "order plus unknown local density",
    "selected clock-chain count",
    "selected causal-set action / response law",
):
    check(f"N1 includes route {route!r}", route in normalized_text)
for wall in ("W_O", "W_V", "W_C", "W_G"):
    check(f"N2 names wall {wall}", wall in text)
for pair in (
    "`W_O`, `W_V`",
    "`W_O`, `W_C`",
    "`W_O`, `W_G`",
    "`W_V`, `W_C`",
    "`W_V`, `W_G`",
    "`W_C`, `W_G`",
):
    check(f"N2 tests pair {pair}", pair in text)
check("N2 records pairwise independence", "pairwise independent at the displayed resolution" in normalized_text)

for forbidden in (
    "the axioms derive the metric",
    "record count is proper time",
    "causal order proves general relativity",
    "the present candidate is TOE-predictively complete",
):
    check(f"forbidden overclaim absent: {forbidden!r}", forbidden not in text.lower())

print(f"PASS={passed} FAIL={failed}")
print("RESULT: " + ("PASS" if failed == 0 else "FAIL"))
raise SystemExit(1 if failed else 0)
