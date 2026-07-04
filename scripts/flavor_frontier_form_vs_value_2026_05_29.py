#!/usr/bin/env python3
"""Flavor frontier map checks."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

PASS = 0
FAIL = 0

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
    expected_rows = [
        "koide_circulant_character_bridge_narrow_theorem_note_2026-05-09",
        "ckm_inverse_square_structural_sum_rule_narrow_theorem_note_2026-05-10",
        "ckm_cp_phase_structural_identity_narrow_theorem_note_2026-05-10",
        "wolfenstein_lambda_a_structural_identities_narrow_theorem_note_2026-05-10",
        "ckm_moduli_only_unitarity_jarlskog_area_certificate_theorem_note_2026-04-26",
        "pmns_oriented_cycle_channel_value_law_note",
        "pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16",
        "pmns_tm2_magnitudes_conditional_bounded_note_2026-05-26",
        "quark_rpsr_single_scalar_readout_underdetermination_note_2026-04-28",
        "quark_c3_circulant_source_law_boundary_note_2026-04-28",
    ]
    live_statuses = {}
    for claim_id in expected_rows:
        row = rows.get(claim_id)
        live_statuses[claim_id] = None if row is None else row.get("effective_status")
        detail = "missing" if row is None else "present"
        check(f"{claim_id} row is present in the audit ledger (presence only)", row is not None, detail)

    open_row = rows.get("quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26")
    live_statuses["quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26"] = (
        None if open_row is None else open_row.get("effective_status")
    )
    detail = "missing" if open_row is None else "present"
    check("quark mass spectrum Koide scheme row is present in the audit ledger (presence only)", open_row is not None, detail)
    print(f"  [info] live effective statuses (audit-lane-owned; not gated): {live_statuses}")

    delta = math.degrees(math.acos(1 / math.sqrt(6)))
    check("CKM CP angle arithmetic", abs(delta - 65.905157) < 1e-5, f"delta={delta:.6f}")
    check("PDG gamma comparison arithmetic", abs(abs(delta - 65.7) / 3.0 - 0.068386) < 1e-5)

    koide_two_thirds = 2 / 3
    ckm_two_thirds = 2 / 3
    ckm_perp_weight = 2 / (3 * 3)
    check("Koide and CKM 2/3 values are numerically equal", abs(koide_two_thirds - ckm_two_thirds) < 1e-12)
    check("CKM perpendicular weight is distinct from 2/3", abs(ckm_perp_weight - 2 / 3) > 1e-6, f"2/9={ckm_perp_weight:.6f}")

    print(f"\nPASS={PASS} FAIL={FAIL}")
    print("Form-support rows are present; continuous flavor values remain separate inputs/open surfaces.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
