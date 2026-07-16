#!/usr/bin/env python3
"""Flavor frontier map checks."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

PASS = 0
FAIL = 0

RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def load_rows() -> dict[str, dict]:
    data = json.loads(Path("docs/audit/data/audit_ledger.json").read_text())
    rows = data.get("rows", {})
    if not isinstance(rows, dict):
        raise RuntimeError("audit ledger rows are not a dictionary")
    return rows


def main() -> int:
    rows = load_rows()
    expected_retained = [
        "koide_circulant_character_bridge_narrow_theorem_note_2026-05-09",
        "ckm_inverse_square_structural_sum_rule_narrow_theorem_note_2026-05-10",
        "ckm_cp_phase_structural_identity_narrow_theorem_note_2026-05-10",
        "wolfenstein_lambda_a_structural_identities_narrow_theorem_note_2026-05-10",
        "ckm_moduli_only_unitarity_jarlskog_area_certificate_theorem_note_2026-04-26",
        "pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16",
        "pmns_tm2_magnitudes_conditional_bounded_note_2026-05-26",
        "quark_rpsr_single_scalar_readout_underdetermination_note_2026-04-28",
        "quark_c3_circulant_source_law_boundary_note_2026-04-28",
    ]
    for claim_id in expected_retained:
        row = rows.get(claim_id)
        detail = "missing" if row is None else f"effective_status={row.get('effective_status')}"
        check(f"{claim_id} is retained-grade", row is not None and row.get("effective_status") in RETAINED_GRADES, detail)

    cycle_note = Path("docs/PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md").read_text(encoding="utf-8")
    check(
        "PMNS cycle-coordinate row is scoped as bounded supplied-block algebra",
        "**Claim type:** bounded_theorem" in cycle_note
        and "Record-compatible physical observable/readout map" in cycle_note
        and "framework derivation or selection of the supplied matrix `A`" in cycle_note,
    )

    open_row = rows.get("quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26")
    detail = "missing" if open_row is None else f"effective_status={open_row.get('effective_status')}"
    check("quark mass spectrum Koide scheme remains open_gate", open_row is not None and open_row.get("effective_status") == "open_gate", detail)

    delta = math.degrees(math.acos(1 / math.sqrt(6)))
    check("CKM CP angle arithmetic", abs(delta - 65.905157) < 1e-5, f"delta={delta:.6f}")
    check("PDG gamma comparison arithmetic", abs(abs(delta - 65.7) / 3.0 - 0.068386) < 1e-5)

    koide_two_thirds = 2 / 3
    ckm_two_thirds = 2 / 3
    ckm_perp_weight = 2 / (3 * 3)
    check("Koide and CKM 2/3 values are numerically equal", abs(koide_two_thirds - ckm_two_thirds) < 1e-12)
    check("CKM perpendicular weight is distinct from 2/3", abs(ckm_perp_weight - 2 / 3) > 1e-6, f"2/9={ckm_perp_weight:.6f}")

    print(f"\nPASS={PASS} FAIL={FAIL}")
    print("Retained form support and bounded PMNS coordinate algebra remain distinct from physical value/readout bridges.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
