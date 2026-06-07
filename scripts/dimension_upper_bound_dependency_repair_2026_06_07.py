#!/usr/bin/env python3
"""Repair verifier for the D3 upper-bound dependency wrapper.

This runner checks the source-side repair to
docs/DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md.

It does not apply audit verdicts. It verifies that the wrapper now cites the
audited one-hop support packets and that the finite set composition is exactly
the scoped bounded claim.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PASS = 0
FAIL = 0


PATHS = {
    "wrapper": ROOT / "docs" / "DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    "lower": ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md",
    "bertrand": ROOT / "docs" / "BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "coulomb": ROOT / "docs" / "COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "gate": ROOT / "docs" / "D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md",
    "ledger": ROOT / "docs" / "audit" / "data" / "audit_ledger.json",
}


CLAIMS = {
    "wrapper": "dimension_selection_upper_bound_textbook_import_note_2026-05-17",
    "lower": "dimension_selection_note",
    "bertrand": "bertrand_stable_orbit_upper_bound_support_note_2026-05-20",
    "coulomb": "coulomb_stability_upper_bound_support_note_2026-05-20",
    "gate": "d3_upper_bound_import_scope_gate_note_2026-06-06",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def text(label: str) -> str:
    path = PATHS[label]
    check(f"{label} file exists", path.exists(), path.relative_to(ROOT).as_posix())
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> int:
    print("Dimension upper-bound dependency repair")
    print("=" * 60)

    wrapper = text("wrapper")
    lower = text("lower")
    bertrand = text("bertrand")
    coulomb = text("coulomb")
    gate = text("gate")

    ledger_path = PATHS["ledger"]
    check("audit ledger data exists for status inspection", ledger_path.exists())
    rows = json.loads(ledger_path.read_text(encoding="utf-8"))["rows"]

    expected_statuses = {
        "lower": ("audited_clean", "retained_bounded"),
        "bertrand": ("audited_clean", "retained_bounded"),
        "coulomb": ("audited_clean", "retained_bounded"),
        "gate": ("audited_clean", "retained_bounded"),
    }
    for label, (audit_status, effective_status) in expected_statuses.items():
        row = rows.get(CLAIMS[label], {})
        check(
            f"{label} ledger status is {audit_status}/{effective_status}",
            row.get("audit_status") == audit_status and row.get("effective_status") == effective_status,
            f"got {row.get('audit_status')}/{row.get('effective_status')}",
        )

    check(
        "wrapper has 2026-06-07 dependency repair section",
        "2026-06-07 dependency-edge repair" in wrapper
        and "direct one-hop support packets" in wrapper,
    )
    check(
        "wrapper directly cites Bertrand support packet",
        "BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md" in wrapper
        and "bertrand_stable_orbit_green_kernel_bridge.py" in wrapper,
    )
    check(
        "wrapper directly cites Coulomb support packet",
        "COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md" in wrapper
        and "frontier_coulomb_stability_scaling_repair.py" in wrapper,
    )
    check(
        "wrapper directly cites D3 composition gate",
        "D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md" in wrapper
        and "frontier_d3_upper_bound_import_scope_gate_2026_06_06.py" in wrapper,
    )
    check(
        "wrapper preserves bounded-support firewall",
        "does not claim a framework-internal derivation" in wrapper
        and "does not claim a framework-native electromagnetic sector" in wrapper
        and "does not promote the downstream dimension-selection lane" in wrapper
        and "not a complete re-derivation of Bertrand's theorem" in wrapper
        and "not a complete re-derivation of the atomic-stability upper bound" in wrapper,
    )

    check(
        "lower note remains lower-bound only",
        "lower-bound support only" in lower and "not a unique-dimension\ntheorem" in lower,
    )
    check(
        "Bertrand support is scoped to circular-orbit stability",
        "stable circular orbits require" in bertrand
        and "does not retire the Bertrand theorem import completely" in bertrand,
    )
    check(
        "Coulomb support is scoped to Green-kernel scaling",
        "Green-kernel scaling lemma" in coulomb
        and "does not establish a framework-native electromagnetic sector" in coulomb,
    )
    check(
        "gate states current finite lower set and import composition",
        "L_runner = {3,4,5}" in gate
        and "L_runner intersect {d : d <= 3} = {3}" in gate,
    )

    lower_set = {3, 4, 5}
    bertrand_upper = {d for d in range(1, 9) if d <= 3}
    atomic_weak_upper = {d for d in range(1, 9) if d <= 4}
    atomic_strict_spectrum = {3}
    check("lower ∩ Bertrand = {3}", lower_set & bertrand_upper == {3})
    check("lower ∩ weak atomic stability = {3,4}", lower_set & atomic_weak_upper == {3, 4})
    check("lower ∩ strict atomic spectrum = {3}", lower_set & atomic_strict_spectrum == {3})

    print("=" * 60)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
