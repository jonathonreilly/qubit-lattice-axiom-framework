#!/usr/bin/env python3
"""Finite D=4 effective-potential-density readout bridge.

This runner checks the bounded bridge:

    rho_* = A(L_t) v(L_t)^4
    v(L_t) = (rho_* / A(L_t))^(1/4)

on the hierarchy endpoint coefficients A_2, A_4, and A_inf. It fixes the
exponent, inverse/direct placement, sign, and normalization of the finite
readout map. It does not derive the physical electroweak insertion map or
apply an audit verdict.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md"
PARENT = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"
ENDPOINT = ROOT / "docs" / "HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md"
EXPECTED_PASS = 15
PASS = 0
FAIL = 0
TOL = 1e-12


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def temporal_modes(lt: int) -> list[float]:
    return [(2 * n + 1) * math.pi / lt for n in range(lt)]


def a_coeff(lt: int, u0: float) -> float:
    return (1.0 / (2.0 * lt * u0**2)) * sum(
        1.0 / (3.0 + math.sin(w) ** 2) for w in temporal_modes(lt)
    )


def a2(u0: float) -> float:
    return 1.0 / (8.0 * u0**2)


def a4(u0: float) -> float:
    return 1.0 / (7.0 * u0**2)


def ainf(u0: float) -> float:
    return 1.0 / (4.0 * math.sqrt(3.0) * u0**2)


def readout_ratio(a_from: float, a_to: float) -> float:
    # Common rho_* gives v_to/v_from = (A_from/A_to)^(1/4).
    return (a_from / a_to) ** 0.25


def main() -> int:
    print("Hierarchy D=4 effective-potential readout bridge")
    print("=" * 72)
    u0_values = [0.7, 0.9, 1.0, 1.2]
    u0 = 0.9

    a_2 = a_coeff(2, u0)
    a_4 = a_coeff(4, u0)
    a_inf = ainf(u0)
    c_42 = readout_ratio(a_2, a_4)
    c_inf2 = readout_ratio(a_2, a_inf)

    print(f"  A_2   = {a_2:.12f}")
    print(f"  A_4   = {a_4:.12f}")
    print(f"  A_inf = {a_inf:.12f}")
    print(f"  v_4/v_2     = {c_42:.12f}")
    print(f"  v_inf/v_2   = {c_inf2:.12f}")

    check("A_2 endpoint formula", abs(a_2 - a2(u0)) < TOL)
    check("A_4 endpoint formula", abs(a_4 - a4(u0)) < TOL)
    check("A_inf endpoint formula", abs(a_inf - 1.0 / (4.0 * math.sqrt(3.0) * u0**2)) < TOL)
    check("A_4/A_2 = 8/7", abs((a_4 / a_2) - (8.0 / 7.0)) < TOL)
    check("A_inf/A_2 = 2/sqrt(3)", abs((a_inf / a_2) - (2.0 / math.sqrt(3.0))) < TOL)
    check("D=4 readout uses fourth root", abs(readout_ratio(1.0, 16.0) - 0.5) < TOL)
    check("v_4/v_2 = (7/8)^(1/4)", abs(c_42 - (7.0 / 8.0) ** 0.25) < TOL)
    check("v_inf/v_2 = (3/4)^(1/8)", abs(c_inf2 - (3.0 / 4.0) ** 0.125) < TOL)
    check("sign is downward compression for L_t=4", a_4 > a_2 and c_42 < 1.0)
    check("sign is downward compression for L_t->inf", a_inf > a_2 and c_inf2 < 1.0)

    placement_ok = True
    for left, right in [(a_2, a_4), (a_2, a_inf), (1.0, 16.0), (2.0, 32.0)]:
        placement_ok = placement_ok and (right > left) and (readout_ratio(left, right) < 1.0)
    check("inverse placement: larger A gives smaller v", placement_ok)

    norm_ok = True
    c_values = []
    for test_u0 in u0_values:
        c = readout_ratio(a2(test_u0), a4(test_u0))
        c_values.append(c)
        norm_ok = norm_ok and abs(c - (7.0 / 8.0) ** 0.25) < TOL
    check("u0 normalization cancels in endpoint ratio", norm_ok, detail=str([round(x, 12) for x in c_values]))

    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    parent = PARENT.read_text(encoding="utf-8")
    runner_text = Path(__file__).read_text(encoding="utf-8")

    forbidden = ["v_" + "obs", "M_" + "Pl", "alpha_" + "LM", "PD" + "G", "proposed_" + "retained"]
    check("runner has no observed-target or alpha load-bearing input", all(token not in runner_text for token in forbidden))
    check("bridge note leaves audit/status movement to independent review", "independent review/audit owns any effective status change" in note_flat and "does not claim" in note)
    check("parent note links the bridge without claiming closure", NOTE.name in parent and ENDPOINT.name in note and "does not promote" in parent)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if PASS != EXPECTED_PASS:
        print(f"ERROR: expected {EXPECTED_PASS} PASS checks, got {PASS}.")
        return 1
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
