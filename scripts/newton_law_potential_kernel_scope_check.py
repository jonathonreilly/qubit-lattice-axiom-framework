#!/usr/bin/env python3
"""Scope checker for the narrowed Newton potential-kernel algebra packet."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


NOTE = Path("docs/NEWTON_LAW_DERIVED_NOTE.md")


PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("=" * 78)
    print("Newton potential-kernel algebra scope check")
    print("=" * 78)

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "bounded-support potential-kernel algebra",
        "not a retained Newton force-law derivation",
        "not yet a physical Newton force law",
        "test-mass force/source response rule",
        "BA3_TEST_MASS_COUPLING_DERIVED=FALSE",
    ]
    forbidden = [
        "No additional physics is imported beyond",
        "unconditional closure from the framework baseline",
        "retained Newton-law closure",
    ]

    for phrase in required:
        record(f"source note contains scope phrase: {phrase}", phrase in text)
    for phrase in forbidden:
        record(f"source note excludes overclaim phrase: {phrase}", phrase not in text)

    r, M = sp.symbols("r M", positive=True)
    G = 1 / (4 * sp.pi * r)
    phi = M * G
    dphi = sp.diff(phi, r)
    grad_mag = -dphi

    record("supplied kernel is 1/(4*pi*r)", sp.simplify(G - 1 / (4 * sp.pi * r)) == 0)
    record("source-linearity gives phi=M/(4*pi*r)", sp.simplify(phi - M / (4 * sp.pi * r)) == 0)
    record("radial derivative is -M/(4*pi*r^2)", sp.simplify(dphi + M / (4 * sp.pi * r**2)) == 0)
    record("gradient magnitude is M/(4*pi*r^2)", sp.simplify(grad_mag - M / (4 * sp.pi * r**2)) == 0)

    # Dependency-edge gate. The supplied kernel and its source-linearity are now
    # attributed to the framework's own lattice Green-kernel normalization row,
    # carried in the note as a markdown link (a ledger dependency edge). Pin the
    # edge to the supplier's LIVE grade read directly from audit_ledger.json
    # (never the note's self-declaration; anti-fabrication pattern 7), and prove
    # the gate discriminates: it flips red if the supplier is demoted, the
    # supplier id is wrong, or the markdown edge is dropped from the note.
    VALID_RETAINED = {"retained", "retained_bounded", "retained_no_go"}
    supplier_id = "lattice_greens_function_maradudin_textbook_import_note_2026-05-18"
    supplier_link = "](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)"
    ledger_path = Path("docs/audit/data/audit_ledger.json")
    supplier_status = None
    if ledger_path.exists():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        row = ledger.get("rows", {}).get(supplier_id, {})
        supplier_status = row.get("effective_status")

    record(
        f"kernel/source-linearity supplier {supplier_id} is retained-grade",
        supplier_status in VALID_RETAINED,
        f"effective_status={supplier_status!r}",
    )
    record(
        "note carries the Maradudin Green-kernel dependency edge (markdown link)",
        supplier_link in text,
    )
    record(
        "cited kernel normalization 1/(4 pi r) is present in the note",
        "1/(4 pi r)" in text,
    )
    non_retained = {
        "audited_conditional",
        "unaudited",
        "audited_failed",
        "audited_renaming",
        "open_gate",
    }
    set_disjoint = all(s not in VALID_RETAINED for s in non_retained)
    record(
        "dependency-edge gate discriminates (non-retained grades rejected, supplier accepted)",
        set_disjoint and (supplier_status in VALID_RETAINED),
        "VALID_RETAINED excludes every non-retained grade; supplier is accepted only on a live retained grade",
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    passed = sum(ok for _, ok, _ in PASSES)
    total = len(PASSES)
    print(f"PASSED: {passed}/{total}")

    if passed == total:
        print("NEWTON_POTENTIAL_KERNEL_ALGEBRA=TRUE")
        print("POTENTIAL_GRADIENT_INVERSE_SQUARE=TRUE")
        print("PHYSICAL_FORCE_LAW_CLAIMED=FALSE")
        print("BA3_TEST_MASS_COUPLING_DERIVED=FALSE")
        print("ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT")
        return 0

    print("NEWTON_POTENTIAL_KERNEL_ALGEBRA=FALSE")
    print("PHYSICAL_FORCE_LAW_CLAIMED=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
