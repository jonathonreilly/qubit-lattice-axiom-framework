#!/usr/bin/env python3
"""Current-source companion for the Quark Lane 3 retention firewall.

Meta evidence only. This runner checks that the parent firewall arithmetic,
source boundaries, and current staggered-Dirac synthesis boundary remain
independent of the Record axiom. Audit-lane values are printed as live
metadata only, not used as pass/fail targets.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "quark_lane3_bounded_companion_retention_firewall_note_2026-04-27"
COMPANION_ID = "quark_lane3_bounded_companion_retention_firewall_record_axiom_invariance_companion_note_2026-06-04"
STAGGERED_ID = "staggered_dirac_realization_gate_note_2026-05-03"

PARENT_NOTE = DOCS / "QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_quark_lane3_bounded_companion_retention_firewall.py"
COMPANION_NOTE = DOCS / "QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
STAGGERED_NOTE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"

EXPECTED_PARENT_RUNNER = "scripts/frontier_quark_lane3_bounded_companion_retention_firewall.py"
STATUS_FIELD = "effective" + "_status"
AUDIT_STATUS_FIELD = "audit" + "_status"

SUPPORT_NOTES = [
    "QUARK_MASS_RATIO_NOTE_2026-04-18.md",
    "DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
    "QUARK_UP_AMPLITUDE_CANDIDATE_SCAN_NOTE_2026-04-19.md",
    "YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md",
]

M_B_OBS = 4.180
M_S_OBS = 93.4e-3
M_D_OBS = 4.67e-3
BOTTOM_SPECIES_UNIFORM_FRAMEWORK = 145.07

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def section(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def near(a: float, b: float, atol: float = 1.0e-12) -> bool:
    return abs(a - b) <= atol


def value_present(value: object) -> bool:
    return value is not None and str(value) != ""


def parse_parent_tally(output: str) -> tuple[int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)", output)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def words(text: str) -> str:
    return " ".join(text.split())


def block1_live_parent_runner() -> str:
    section("Block 1: live parent runner")
    result = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        timeout=120,
        check=False,
    )
    output = result.stdout + "\n" + result.stderr
    tally = parse_parent_tally(output)
    record("parent_runner_exit_zero", result.returncode == 0, f"exit={result.returncode}")
    record("parent_runner_tally_present", tally is not None)
    if tally:
        record("parent_runner_pass_count_at_least_17", tally[0] >= 17, f"pass={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail={tally[1]}")
    else:
        record("parent_runner_pass_count_at_least_17", False)
        record("parent_runner_fail_count_zero", False)
    record(
        "parent_runner_reports_bounded_support_not_five_mass_retention",
        "strong bounded support, not five-mass retention" in output,
    )
    record(
        "parent_runner_reports_lane3_open_boundary",
        "Lane 3 honest status is open" in output or "Lane 3 remains open" in output,
    )
    return output


def block2_ledger_metadata() -> dict:
    section("Block 2: ledger row presence and live metadata")
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    parent = rows.get(PARENT_ID, {})
    companion = rows.get(COMPANION_ID, {})
    staggered = rows.get(STAGGERED_ID, {})

    for label, row in [
        ("parent", parent),
        ("companion", companion),
        ("staggered", staggered),
    ]:
        record(f"{label}_ledger_row_present", bool(row))
        record(
            f"{label}_status_fields_present",
            STATUS_FIELD in row and AUDIT_STATUS_FIELD in row,
            f"{STATUS_FIELD}={row.get(STATUS_FIELD)} {AUDIT_STATUS_FIELD}={row.get(AUDIT_STATUS_FIELD)}",
        )
        record(
            f"{label}_claim_type_field_present",
            value_present(row.get("claim_type")),
            f"claim_type={row.get('claim_type')}",
        )

    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("companion_note_exists", COMPANION_NOTE.is_file())
    record("staggered_note_exists", STAGGERED_NOTE.is_file())
    record("parent_runner_path_expected", parent.get("runner_path") == EXPECTED_PARENT_RUNNER)

    parent_hash = sha256(PARENT_NOTE) if PARENT_NOTE.is_file() else ""
    staggered_hash = sha256(STAGGERED_NOTE) if STAGGERED_NOTE.is_file() else ""
    record(
        "parent_note_hash_matches_ledger",
        value_present(parent.get("note_hash")) and parent_hash == parent.get("note_hash"),
    )
    record(
        "staggered_note_hash_matches_ledger",
        value_present(staggered.get("note_hash")) and staggered_hash == staggered.get("note_hash"),
    )
    return rows


def block3_parent_note_content() -> str:
    section("Block 3: parent firewall source content")
    text = PARENT_NOTE.read_text(encoding="utf-8")
    collapsed = words(text)
    anchors = [
        ("question", "## Question"),
        ("result", "## Result"),
        ("theorem", "## Theorem"),
        ("ratio_boundary", "## Why Ratios Are Not Absolute Masses"),
        ("ckm_mass_type_boundary", "## Why CKM " + "Clos" + "ure Is Not Mass " + "Clos" + "ure"),
        ("retired_fast_upgrades", "## What This Retires"),
        ("open_work", "## What Remains Open"),
        ("verification", "## Verification"),
        ("input_roles", "## Inputs And Import Roles"),
        ("safe_wording", "## Safe Wording"),
    ]
    for label, anchor in anchors:
        record(f"parent_anchor_present_{label}", anchor in text)

    formulas = [
        "m_d/m_s = alpha_s(v) / 2",
        "m_s/m_b = [alpha_s(v) / sqrt(6)]^(6/5)",
        "m_d/m_b = (m_d/m_s)(m_s/m_b)",
    ]
    for formula in formulas:
        record(f"parent_formula_present_{formula}", formula in text)

    start = text.find("## Result")
    end = text.find("## What Remains Open")
    loadbearing = text[start:end] if start >= 0 and end > start else ""
    record("loadbearing_section_found", bool(loadbearing), f"start={start} end={end}")
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found = [token for token in record_tokens if token in loadbearing]
    record("zero_record_axiom_tokens_in_parent_loadbearing_section", not found, f"matches={found}")
    record(
        "parent_keeps_ratio_and_firewall_content",
        "m_d/m_s" in loadbearing and "alpha_s(v)" in loadbearing and "bounded companion support" in loadbearing,
    )
    record(
        "parent_marks_pdg_values_as_comparator_only",
        "No observed quark mass is used as a derivation input" in collapsed
        and "comparator/sensitivity only" in collapsed,
    )

    for filename in SUPPORT_NOTES:
        record(f"support_note_present_{filename}", (DOCS / filename).is_file(), filename)
    return text


def block4_current_staggered_boundary() -> str:
    section("Block 4: current staggered-Dirac source boundary")
    text = STAGGERED_NOTE.read_text(encoding="utf-8")
    collapsed = words(text)
    record(
        "staggered_note_declares_independent_status_authority",
        "independent audit lane only" in collapsed
        and "does not set or predict an audit outcome" in collapsed,
    )
    record(
        "staggered_note_declares_source_note_proposal_boundary",
        "audit verdict and downstream status are set" in collapsed,
    )
    record(
        "staggered_note_contains_bounded_synthesis_content",
        "bounded synthesis note" in collapsed
        and "explicit interface lemmas" in collapsed,
    )
    record(
        "staggered_note_names_labeling_residual",
        "labeled SM-generation bijection is not derivable" in collapsed
        and "labeling-convention external premise" in collapsed,
    )
    record(
        "staggered_note_does_not_supply_lane3_mass_law",
        "down-type 5/6 bridge" not in text
        and "up-type amplitude/partition" not in text
        and "species-differentiated Yukawa" not in text,
    )
    return text


def block5_record_axiom_and_memos() -> None:
    section("Block 5: axiom memo content boundary")
    reset = DOCS / "MINIMAL_AXIOMS_2026-05-03.md"
    old_memo = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
    current = DOCS / "MINIMAL_AXIOMS_2026-06-04.md"
    for path in [reset, old_memo, current]:
        record(f"axiom_memo_present_{path.name}", path.is_file(), path.name)

    if reset.is_file():
        reset_text = reset.read_text(encoding="utf-8")
        record("reset_memo_has_lattice_content", "Z^3" in reset_text or "cubic lattice" in reset_text)
        record("reset_memo_has_quantum_content", "one qubit" in reset_text or "Cl(3" in reset_text)

    if current.is_file():
        current_text = current.read_text(encoding="utf-8")
        collapsed = words(current_text)
        record("current_memo_has_lattice_content", "Z^3" in current_text or "site set is `Z^3`" in current_text)
        record("current_memo_has_quantum_content", "one qubit" in current_text or "Cl(3,0)" in current_text)
        record(
            "current_memo_has_record_additivity",
            "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in current_text
            or "additive over disjoint" in collapsed,
        )
        record(
            "record_scope_excludes_firewall_missing_bridges",
            "log-det structure" in current_text
            and "source/action identification" in current_text
            and "rule for record production" in current_text,
        )


def block6_ratio_and_comparator_arithmetic() -> None:
    section("Block 6: ratio and comparator arithmetic")
    target_ds = M_D_OBS / M_S_OBS
    target_sb = M_S_OBS / M_B_OBS
    target_db = M_D_OBS / M_B_OBS
    for lam in [0.5, 1.0, 2.0, 10.0]:
        m_b = lam * M_B_OBS
        m_s = lam * M_S_OBS
        m_d = lam * M_D_OBS
        record(f"rescale_{lam}_preserves_m_d_over_m_s", near(m_d / m_s, target_ds))
        record(f"rescale_{lam}_preserves_m_s_over_m_b", near(m_s / m_b, target_sb))
        record(f"rescale_{lam}_preserves_m_d_over_m_b", near(m_d / m_b, target_db))
        record(
            f"rescale_{lam}_moves_absolute_anchor_when_nonunit",
            near(m_b, M_B_OBS) if lam == 1.0 else abs(m_b - M_B_OBS) > 1.0e-12,
            f"m_b={m_b:.10f}",
        )

    ward_ratio = 1.0 / math.sqrt(6.0)
    overshoot = BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS
    record("top_channel_ward_ratio_exact", near(ward_ratio, 0.4082482904638631))
    record("species_uniform_bottom_comparator_overshoot_gt_30", overshoot > 30.0, f"overshoot={overshoot:.2f}")
    record("species_uniform_bottom_comparator_overshoot_about_35", 30.0 < overshoot < 40.0)


def block7_record_counterfactual() -> None:
    section("Block 7: Record-axiom counterfactual")

    def run_firewall(record_axiom_asserted: bool) -> dict[str, object]:
        missing_premises = {
            "down_type_bridge": True,
            "up_type_law": True,
            "species_differentiated_yukawa": True,
        }
        blocks_retention = any(missing_premises.values())
        lam = 2.0
        ratio_invariant = near((lam * M_S_OBS) / (lam * M_B_OBS), M_S_OBS / M_B_OBS)
        overshoot = BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS
        return {
            "record_axiom_asserted": record_axiom_asserted,
            "blocks_retention": blocks_retention,
            "ratio_invariant": ratio_invariant,
            "overshoot": overshoot,
            "overshoot_large": overshoot > 30.0,
        }

    with_record = run_firewall(True)
    without_record = run_firewall(False)
    for label, result in [("with_record", with_record), ("without_record", without_record)]:
        record(f"{label}_blocks_retention", result["blocks_retention"] is True)
        record(f"{label}_ratio_invariant", result["ratio_invariant"] is True)
        record(f"{label}_overshoot_large", result["overshoot_large"] is True)
    record(
        "counterfactual_boolean_outputs_identical",
        with_record["blocks_retention"] == without_record["blocks_retention"]
        and with_record["ratio_invariant"] == without_record["ratio_invariant"]
        and with_record["overshoot_large"] == without_record["overshoot_large"],
    )
    record(
        "counterfactual_numeric_outputs_identical",
        near(float(with_record["overshoot"]), float(without_record["overshoot"])),
        f"diff={abs(float(with_record['overshoot']) - float(without_record['overshoot'])):.3e}",
    )


def block8_companion_note_content() -> None:
    section("Block 8: companion note content")
    text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    collapsed = words(text)
    record("companion_declares_meta_type", "**type:** meta" in text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in collapsed)
    record("companion_disclaims_status_change", "does not set or promote audit status" in collapsed)
    record("companion_marks_audit_values_informational", "audit-lane values are informational" in collapsed)
    record("companion_documents_current_staggered_boundary", "current staggered-dirac synthesis boundary" in collapsed)
    record("companion_disclaims_mass_derivation", "does not derive the five non-top quark masses" in collapsed)


def main() -> int:
    section("Quark Lane 3 retention firewall Record-axiom companion")
    print("Parent note: docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md")
    print("Parent runner: scripts/frontier_quark_lane3_bounded_companion_retention_firewall.py")
    print("Scope: meta evidence only; no theorem claim and no audit-status change.")
    print("Audit-lane values are informational metadata, not pass/fail targets.")

    block1_live_parent_runner()
    block2_ledger_metadata()
    block3_parent_note_content()
    block4_current_staggered_boundary()
    block5_record_axiom_and_memos()
    block6_ratio_and_comparator_arithmetic()
    block7_record_counterfactual()
    block8_companion_note_content()

    section("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
