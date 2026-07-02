#!/usr/bin/env python3
"""Bounded finite-extraction core for the Poisson teleportation resource row."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from frontier_teleportation_resource_from_poisson import (  # noqa: E402
    DEFAULT_CASES,
    AuditCase,
    audit_case,
    helper_source_certificate,
    logical_carrier_certificate,
    retained_axis_source_certificate,
    source_status_firewall_certificate,
    verify_teleportation_convention,
)


DOCS = ROOT / "docs"
CORE_NOTE = DOCS / "TELEPORTATION_POISSON_FINITE_EXTRACTION_CORE_BOUNDED_NOTE_2026-06-18.md"
PARENT_NOTE = DOCS / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def check_source_boundaries() -> None:
    section("T0: source status and open-gate firewalls")
    core = read(CORE_NOTE)
    parent = read(PARENT_NOTE)

    for phrase in (
        "Claim type:** bounded_theorem",
        "Actual current-surface status:** bounded-support",
        "Trace class:** upstream_support",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
        "TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md",
    ):
        check(f"core note contains {phrase}", phrase in core)

    for phrase in (
        "Finite Extraction Core Split",
        CORE_NOTE.name,
        "open-gate status",
        "native preparation/readout and apparatus theorem remains open",
    ):
        check(f"parent cites bounded split boundary: {phrase}", phrase in parent)

    for phrase in (
        "deterministic physical teleportation-resource closure",
        "native Poisson-resource preparation/readout authority",
        "retained-grade status for the parent open gate",
    ):
        check(f"core note forbids overclaim: {phrase}", phrase in core)

    for phrase in (
        "parent is retained",
        "physical deterministic resource theorem is closed",
        "native preparation/readout theorem is proved",
        "proposed_retained",
    ):
        check(f"forbidden promotion absent: {phrase}", phrase not in core and phrase not in parent)


def check_source_certificates() -> None:
    section("T1: helper and retained-axis source certificates")
    helper = helper_source_certificate()
    check("Poisson/CHSH helper source has required symbols", helper["symbol_count"] == 11)
    check("Poisson/CHSH helper source is nontrivial", helper["line_count"] > 500, helper["line_count"])

    rala = retained_axis_source_certificate()
    check(
        "RALA source status is retained-grade",
        rala["status"] in {"retained", "retained_bounded", "retained_no_go"},
    )
    check("RALA source snippets are present", rala["snippet_count"] >= 5, rala["snippet_count"])

    firewall = source_status_firewall_certificate()
    check("parent source firewall remains intact", firewall["snippet_count"] >= 18, firewall["snippet_count"])


def check_logical_carriers() -> None:
    section("T2: last-taste logical carrier checks")
    for case in DEFAULT_CASES:
        cert = logical_carrier_certificate(case)
        label = cert["case"]
        check(f"{label}: environments present", cert["n_env"] > 0, cert["n_env"])
        check(f"{label}: pair-hop X is last logical X", cert["x_is_last_logical_x"])
        check(f"{label}: last-bit Z is Pauli", cert["z_last_pauli"])
        if case.dim == 1:
            check(f"{label}: sublattice Z equals last-bit Z in 1D", cert["sublattice_z_equals_z_last"])
        else:
            check(f"{label}: 2D sublattice Z is distinct from last-bit Z", not cert["sublattice_z_equals_z_last"])


def check_resource_extraction() -> None:
    section("T3: bounded finite resource extraction")
    sanity = verify_teleportation_convention(seed=20260424)
    check("ideal Phi+ convention has unit minimum fidelity", abs(sanity["min"] - 1.0) < 1e-12, sanity)
    check("ideal Phi+ convention preserves trace", sanity["max_trace_error"] <= 1e-12, sanity)

    results = [
        audit_case(case, trials=32, seed=20260618 + index, high_fidelity_threshold=0.90, probability_floor=1e-12)
        for index, case in enumerate(DEFAULT_CASES)
    ]
    by_label = {result["case"].label: result for result in results if isinstance(result["case"], AuditCase)}

    null = by_label["1d_null"]
    check("G=0 null is not high-fidelity", not null["deterministic_high_fidelity_resource"], null["logical_bell_fidelity"])
    check("G=0 null has zero negativity", abs(null["negativity"]) < 1e-12, null["negativity"])
    check("G=0 null Bell overlap is 1/2", abs(null["logical_bell_fidelity"] - 0.5) < 1e-12, null["logical_bell_fidelity"])

    for label in ("1d_poisson_chsh", "2d_poisson_chsh"):
        result = by_label[label]
        teleportation = result["teleportation"]
        check(f"{label}: deterministic traced resource passes threshold", result["deterministic_high_fidelity_resource"])
        check(f"{label}: Bell overlap > 0.95", result["logical_bell_fidelity"] > 0.95, result["logical_bell_fidelity"])
        check(f"{label}: negativity > 0.45", result["negativity"] > 0.45, result["negativity"])
        check(f"{label}: standard teleportation min fidelity > 0.95", teleportation["min"] > 0.95, teleportation)
        check(f"{label}: trace preservation", teleportation["max_trace_error"] <= 1e-12, teleportation)


def main() -> int:
    print("# Teleportation Poisson finite extraction core")
    print(f"# Source note: {CORE_NOTE.relative_to(ROOT)}")
    check_source_boundaries()
    check_source_certificates()
    check_logical_carriers()
    check_resource_extraction()
    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
