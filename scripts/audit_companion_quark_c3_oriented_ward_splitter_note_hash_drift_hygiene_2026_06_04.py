#!/usr/bin/env python3
"""Current-source hygiene companion for the Quark C3 Ward splitter note.

Meta evidence only. This runner checks the current parent note, parent runner,
ledger row, and finite C3 algebra after the 2026-06 source-side dependency
repairs. Audit-lane values are printed as live metadata only, not used as
pass/fail targets.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_ID = "quark_c3_oriented_ward_splitter_support_note_2026-04-28"
PARENT_NOTE = REPO_ROOT / "docs" / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_quark_c3_oriented_ward_splitter_support.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_HASH_DRIFT_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

EXPECTED_RUNNER_PATH = "scripts/frontier_quark_c3_oriented_ward_splitter_support.py"
STATUS_FIELD = "effective" + "_status"
AUDIT_STATUS_FIELD = "audit" + "_status"

REQUIRED_DEPS = {
    "three_generation_observable_theorem_note": "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md",
    "quark_c3_oriented_ward_splitter_algebraic_core_split_note_2026-06-18": (
        "QUARK_C3_ORIENTED_WARD_SPLITTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md"
    ),
    "quark_generation_equivariant_ward_degeneracy_no_go_note_2026-04-28": (
        "QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md"
    ),
    "s3_taste_cube_decomposition_note": "S3_TASTE_CUBE_DECOMPOSITION_NOTE.md",
}
STAGGERED_DEP_ID = "staggered_dirac_realization_gate_note_2026-05-03"
STAGGERED_FILENAME = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"

PASS = 0
FAIL = 0
TOL = 1.0e-10


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


def value_present(value: object) -> bool:
    return value is not None and str(value) != ""


def parse_parent_tally(output: str) -> tuple[int, int] | None:
    match = re.search(r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", output)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def markdown_targets(text: str) -> set[str]:
    return set(re.findall(r"\]\(([^)]+)\)", text))


def c3_cycle() -> np.ndarray:
    return np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )


def ward_op(a: float, b: float, c: float) -> np.ndarray:
    cycle = c3_cycle()
    cycle2 = cycle @ cycle
    ident = np.eye(3, dtype=complex)
    splitter = (cycle - cycle2) / (1j * np.sqrt(3.0))
    return a * ident + b * (cycle + cycle2) + c * splitter


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
    record("parent_runner_total_line_present", tally is not None)
    if tally:
        record("parent_runner_pass_count_at_least_58", tally[0] >= 58, f"pass={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail={tally[1]}")
    else:
        record("parent_runner_pass_count_at_least_58", False)
        record("parent_runner_fail_count_zero", False)
    record(
        "parent_runner_reports_support_boundary_result",
        "oriented C3 supplies an exact local splitter primitive" in output
        and "Lane 3 quark-mass Ward source/readout law open" in output,
    )
    record(
        "parent_runner_reports_dependency_graph_repair_block",
        "Dependency graph repair (2026-06-20)" in output,
    )
    return output


def block2_ledger_row() -> dict:
    section("Block 2: ledger row presence and live metadata")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger.get(PARENT_ID, {})
    record("parent_ledger_row_present", PARENT_ID in ledger)
    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("companion_note_exists", COMPANION_NOTE.is_file())
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_RUNNER_PATH)
    record(
        "parent_claim_type_field_present",
        value_present(row.get("claim_type")),
        f"claim_type={row.get('claim_type')}",
    )
    record(
        "parent_status_fields_present",
        STATUS_FIELD in row and AUDIT_STATUS_FIELD in row,
        f"{STATUS_FIELD}={row.get(STATUS_FIELD)} {AUDIT_STATUS_FIELD}={row.get(AUDIT_STATUS_FIELD)}",
    )
    record(
        "parent_criticality_field_present",
        value_present(row.get("criticality")),
        f"criticality={row.get('criticality')}",
    )
    record(
        "parent_load_field_present",
        value_present(row.get("load_bearing_score")),
        f"load={row.get('load_bearing_score')}",
    )

    live_hash = sha256(PARENT_NOTE) if PARENT_NOTE.is_file() else ""
    ledger_hash = row.get("note_hash")
    record("parent_note_hash_field_present", value_present(ledger_hash))
    record("parent_note_hash_matches_ledger", bool(ledger_hash) and live_hash == ledger_hash)

    row_deps = set(row.get("deps", []))
    record(
        "parent_deps_include_current_required_sources",
        set(REQUIRED_DEPS).issubset(row_deps),
        f"required={len(REQUIRED_DEPS)} row_deps={len(row_deps)}",
    )
    record(
        "staggered_gate_not_a_current_row_dependency",
        STAGGERED_DEP_ID not in row_deps,
        f"staggered_dep_present={STAGGERED_DEP_ID in row_deps}",
    )
    record(
        "helper_runner_paths_field_present",
        "helper_runner_paths" in row,
        f"count={len(row.get('helper_runner_paths') or [])}",
    )

    for dep_id in sorted(REQUIRED_DEPS):
        dep_row = ledger.get(dep_id)
        record(f"required_dep_row_present_{dep_id}", dep_row is not None)
        record(
            f"required_dep_status_fields_present_{dep_id}",
            dep_row is not None and STATUS_FIELD in dep_row and AUDIT_STATUS_FIELD in dep_row,
            (
                f"{STATUS_FIELD}={dep_row.get(STATUS_FIELD)} {AUDIT_STATUS_FIELD}={dep_row.get(AUDIT_STATUS_FIELD)}"
                if dep_row
                else "missing row"
            ),
        )
    record("previous_audit_history_field_present", "previous_audits" in row)
    return row


def block3_parent_note_content() -> str:
    section("Block 3: current parent note content")
    text = PARENT_NOTE.read_text(encoding="utf-8")
    words = " ".join(text.split())
    targets = markdown_targets(text)

    record(
        "parent_declares_independent_status_authority",
        "independent audit lane only" in words and "This source note does not set status" in words,
    )
    record("parent_has_dependency_rewire_section", "## Dependency rewire (2026-06-18)" in text)
    record("parent_has_dependency_repair_section", "## Dependency repair (2026-06-20)" in text)
    record("parent_has_machine_visible_dependency_links", "## Machine-Visible Dependency Links" in text)

    for dep_id, filename in sorted(REQUIRED_DEPS.items()):
        record(
            f"parent_note_markdown_links_required_dep_{dep_id}",
            filename in targets,
            filename,
        )

    record(
        "staggered_gate_kept_as_plain_text_pointer",
        STAGGERED_FILENAME in text and f"]({STAGGERED_FILENAME})" not in text,
    )
    record(
        "parent_notes_staggered_gate_not_load_bearing",
        "not as a markdown one-hop authority" in words
        and "non-load-bearing provenance pointer" in words,
    )
    record(
        "parent_note_keeps_finite_c3_scope",
        "Hermitian commutant of the oriented cycle" in text
        and "three-real-parameter family" in text,
    )
    record(
        "parent_note_keeps_lane3_open_boundary",
        "Lane 3 remains open" in text
        and "source/readout theorem" in text,
    )
    record(
        "parent_note_disclaims_numerical_quark_ratios",
        "numerical `y_u/y_t`" in text and "y_b/y_t" in text,
    )
    record(
        "parent_note_disclaims_absolute_non_top_scale",
        "absolute non-top quark mass scale" in text,
    )
    record(
        "parent_note_disclaims_status_change",
        "does not set status" in text and "does not promote this note" in text,
    )
    return text


def block4_companion_note_content() -> None:
    section("Block 4: companion note content")
    text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    words = " ".join(text.split())
    record("companion_declares_meta_type", "**type:** meta" in text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in text)
    record("companion_disclaims_status_change", "does not set or promote audit status" in words)
    record("companion_marks_audit_values_informational", "audit-lane values are informational" in words)
    record("companion_documents_current_parent_tally", "pass=58 fail=0" in words)
    record("companion_documents_dependency_repair", "dependency repair (2026-06-20)" in words)
    record("companion_disclaims_source_readout_resolution", "does not resolve the lane 3 source/readout law" in words)


def block5_normal_form_spectrum() -> None:
    section("Block 5: C3 Hermitian normal-form spectrum")
    cycle = c3_cycle()
    for a, b, c in [
        (0.7, -0.2, 0.4),
        (1.1, 0.3, -0.6),
        (-0.5, 0.55, 0.0),
        (0.0, 1.0, 1.5),
    ]:
        matrix = ward_op(a, b, c)
        predicted = sorted([a + 2 * b, a - b + c, a - b - c])
        actual = sorted(np.linalg.eigvalsh(matrix).real.tolist())
        record(
            f"W({a},{b},{c})_is_hermitian",
            np.linalg.norm(matrix - matrix.conj().T) < 1.0e-12,
            f"norm={np.linalg.norm(matrix - matrix.conj().T):.2e}",
        )
        record(
            f"W({a},{b},{c})_commutes_with_C3",
            np.linalg.norm(matrix @ cycle - cycle @ matrix) < 1.0e-12,
            f"norm={np.linalg.norm(matrix @ cycle - cycle @ matrix):.2e}",
        )
        record(
            f"W({a},{b},{c})_spectrum_matches_formula",
            all(abs(p - q) < 1.0e-12 for p, q in zip(predicted, actual)),
            f"predicted={[round(x, 6) for x in predicted]} actual={[round(x, 6) for x in actual]}",
        )


def block6_boundary_and_readout_checks() -> None:
    section("Block 6: splitter boundary and readout checks")
    cycle = c3_cycle()
    cycle2 = cycle @ cycle
    splitter = (cycle - cycle2) / (1j * np.sqrt(3.0))
    refl = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )

    eigs = sorted(np.linalg.eigvalsh(ward_op(0.5, 0.25, 0.0)).real.tolist())
    record(
        "c_zero_retains_E_doublet_degeneracy",
        abs(eigs[0] - eigs[1]) < 1.0e-12,
        f"eigs={[round(x, 6) for x in eigs]}",
    )
    eigs = sorted(np.linalg.eigvalsh(ward_op(0.5, 0.25, 0.3)).real.tolist())
    record(
        "generic_nonzero_c_gives_three_distinct_eigenvalues",
        abs(eigs[0] - eigs[1]) > 1.0e-9 and abs(eigs[1] - eigs[2]) > 1.0e-9,
        f"eigs={[round(x, 6) for x in eigs]}",
    )
    eigs = sorted(np.linalg.eigvalsh(ward_op(0.0, 0.5, 1.5)).real.tolist())
    record(
        "c_equals_plus_3b_is_boundary_collision",
        abs(eigs[0] - eigs[1]) < 1.0e-9 or abs(eigs[1] - eigs[2]) < 1.0e-9,
        f"eigs={[round(x, 6) for x in eigs]}",
    )
    record("splitter_is_hermitian", np.linalg.norm(splitter - splitter.conj().T) < TOL)
    record("reflection_is_involution", np.linalg.norm(refl @ refl - np.eye(3, dtype=complex)) < TOL)
    record("reflection_conjugates_C_to_C_squared", np.linalg.norm(refl @ cycle @ refl - cycle2) < TOL)
    record("reflection_flips_splitter", np.linalg.norm(refl @ splitter @ refl + splitter) < TOL)

    for x, y, z, expected in [
        (0.7, 0.7, 0.7, True),
        (0.7, 1.2, 0.7, False),
        (0.0, 0.0, 0.0, True),
        (1.0, 2.0, 3.0, False),
    ]:
        diag = np.diag([x, y, z]).astype(complex)
        commutes = np.linalg.norm(diag @ cycle - cycle @ diag) < 1.0e-12
        record(
            f"diag({x},{y},{z})_C3_equivariance_matches_scalar_test",
            commutes == expected,
            f"commutes={commutes} expected={expected}",
        )


def main() -> int:
    section("Quark C3 Ward splitter current-source hygiene companion")
    print("Parent note: docs/QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md")
    print("Parent runner: scripts/frontier_quark_c3_oriented_ward_splitter_support.py")
    print("Scope: meta evidence only; no theorem claim and no audit-status change.")
    print("Audit-lane values are informational metadata, not pass/fail targets.")

    block1_live_parent_runner()
    block2_ledger_row()
    block3_parent_note_content()
    block4_companion_note_content()
    block5_normal_form_spectrum()
    block6_boundary_and_readout_checks()

    section("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
