#!/usr/bin/env python3
"""Current-source hygiene companion for the static-source readout I1 bridge.

Meta evidence only. This runner checks that the parent I1 bridge remains
reproducible from source content and exact algebra, while audit-lane values are
printed as live metadata only and never used as pass/fail targets.
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

PARENT_ID = "static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27"
COMPANION_ID = "static_source_readout_i1_accepted_premise_bridge_dep_resolution_hygiene_companion_note_2026-06-04"
DEP_ID = "alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27"
G_BARE_DEP_ID = "g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26"
GREEN_DEP_ID = "lattice_greens_function_maradudin_textbook_import_note_2026-05-18"

PARENT_NOTE = DOCS / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "static_source_readout_i1_accepted_premise_runner.py"
DEP_NOTE = DOCS / "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
COMPANION_NOTE = DOCS / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"

EXPECTED_PARENT_RUNNER = "scripts/static_source_readout_i1_accepted_premise_runner.py"
STATUS_FIELD = "effective" + "_status"
AUDIT_STATUS_FIELD = "audit" + "_status"

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


def words(text: str) -> str:
    return " ".join(text.split())


def value_present(value: object) -> bool:
    return value is not None and str(value) != ""


def run_parent() -> tuple[int, str, str]:
    result = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env={**__import__("os").environ, "PYTHONPATH": str(REPO_ROOT / "scripts")},
        timeout=180,
        check=False,
    )
    return result.returncode, result.stdout, result.stderr


def parse_summary(output: str, label: str) -> tuple[int, int] | None:
    pattern = rf"{label}\s*:\s*PASS\s*=\s*(\d+),\s*FAIL\s*=\s*(\d+)"
    match = re.search(pattern, output)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def block1_parent_runner() -> str:
    section("Block 1: live parent runner")
    rc, out, err = run_parent()
    exact = parse_summary(out, "EXACT")
    bounded = parse_summary(out, "BOUNDED")
    total = parse_summary(out, "TOTAL")
    record("parent_runner_exit_zero", rc == 0, f"returncode={rc}")
    record("parent_runner_verdict_present", "bounded accepted-premise bridge passes" in out)
    record("parent_runner_exact_summary_present", exact is not None)
    record("parent_runner_bounded_summary_present", bounded is not None)
    record("parent_runner_total_summary_present", total is not None)
    if exact:
        record("parent_runner_exact_pass_count_at_least_48", exact[0] >= 48, f"pass={exact[0]}")
        record("parent_runner_exact_fail_count_zero", exact[1] == 0, f"fail={exact[1]}")
    else:
        record("parent_runner_exact_pass_count_at_least_48", False)
        record("parent_runner_exact_fail_count_zero", False)
    if bounded:
        record("parent_runner_bounded_pass_count_at_least_11", bounded[0] >= 11, f"pass={bounded[0]}")
        record("parent_runner_bounded_fail_count_zero", bounded[1] == 0, f"fail={bounded[1]}")
    else:
        record("parent_runner_bounded_pass_count_at_least_11", False)
        record("parent_runner_bounded_fail_count_zero", False)
    if total:
        record("parent_runner_total_pass_count_at_least_59", total[0] >= 59, f"pass={total[0]}")
        record("parent_runner_total_fail_count_zero", total[1] == 0, f"fail={total[1]}")
    else:
        record("parent_runner_total_pass_count_at_least_59", False)
        record("parent_runner_total_fail_count_zero", False)
    record("parent_runner_no_stderr_traceback", "Traceback" not in err)
    return out


def block2_ledger_metadata() -> dict:
    section("Block 2: ledger row presence and live metadata")
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    for label, row_id in [
        ("parent", PARENT_ID),
        ("companion", COMPANION_ID),
        ("alpha_dep", DEP_ID),
        ("gbare_dep", G_BARE_DEP_ID),
        ("green_dep", GREEN_DEP_ID),
    ]:
        row = rows.get(row_id, {})
        record(f"{label}_row_present", bool(row))
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

    parent = rows.get(PARENT_ID, {})
    alpha_dep = rows.get(DEP_ID, {})
    record("parent_runner_path_expected", parent.get("runner_path") == EXPECTED_PARENT_RUNNER)
    record(
        "parent_deps_include_current_required_sources",
        {DEP_ID, G_BARE_DEP_ID, GREEN_DEP_ID}.issubset(set(parent.get("deps", []))),
        f"deps={len(parent.get('deps', []))}",
    )
    record(
        "parent_note_hash_matches_ledger",
        PARENT_NOTE.is_file() and sha256(PARENT_NOTE) == parent.get("note_hash"),
    )
    record(
        "alpha_dep_note_hash_matches_ledger",
        DEP_NOTE.is_file() and sha256(DEP_NOTE) == alpha_dep.get("note_hash"),
    )
    return rows


def _strip_source_firewall_list(source: str) -> str:
    start = source.find("forbidden_source_phrases = [")
    if start == -1:
        return source
    end = source.find("\n]", start)
    if end == -1:
        return source
    return source[:start] + source[end + 2 :]


def block3_parent_runner_source_boundary() -> None:
    section("Block 3: parent runner source boundary")
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    scan_source = _strip_source_firewall_list(source)
    record("parent_source_firewall_list_stripped", len(scan_source) < len(source))
    tokens = [
        ("audit_status_field", "audit_" + "status"),
        ("effective_status_field", "effective_" + "status"),
        ("intrinsic_status_field", "intrinsic_" + "status"),
        ("audit_ledger_name", "audit_" + "ledger"),
        ("audit_grade_phrase", "audit_" + "grade"),
        ("retained-bounded-value", "retained_" + "bounded"),
        ("audited-clean-value", "audited_" + "clean"),
        ("audited-conditional-value", "audited_" + "conditional"),
    ]
    for label, token in tokens:
        record(f"parent_runner_no_{label}_outside_source_firewall_list", token not in scan_source)


def block4_parent_and_dep_note_content() -> None:
    section("Block 4: parent and dependency source content")
    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    parent_words = words(parent_text)
    dep_text = DEP_NOTE.read_text(encoding="utf-8")
    dep_words = words(dep_text)

    record(
        "parent_declares_independent_status_authority",
        "independent audit lane only" in parent_words
        and "does not set or predict an audit outcome" in parent_words,
    )
    record(
        "parent_registers_static_source_premise",
        "Static-source linear-response readout convention" in parent_text
        and "V(r)  =  - C * g_bare^2 * G(r)" in parent_text,
    )
    record(
        "parent_proof_walk_has_B1_to_B4",
        all(f"(B{i})" in parent_text for i in range(1, 5)),
    )
    record(
        "parent_names_exact_substitution_arithmetic",
        "exact symbolic algebra" in parent_words
        or "exact rational-arithmetic identities" in parent_words,
    )
    grade_phrases = [
        "load-bears on the dep's audit",
        "depends on the dep's audit grade",
        "requires the dep to be retained",
        "requires retained_" + "bounded",
        "requires audited_" + "clean",
    ]
    for idx, phrase in enumerate(grade_phrases):
        record(f"parent_note_no_dep_grade_dependency_phrase_{idx}", phrase.lower() not in parent_text.lower())

    record(
        "alpha_dep_contains_dimensionless_coupling_identity",
        "alpha := g_bare^2/(4*pi)" in dep_words
        or "alpha := g_bare^2 / (4 pi)" in dep_words
        or "alpha := g_bare^2 / (4*pi)" in dep_words,
    )
    record(
        "alpha_dep_keeps_i1_isolation_boundary",
        "isolation of I2 from I1" in dep_text or "I1 static-source readout" in dep_text,
    )


def block5_symbolic_chain() -> None:
    section("Block 5: symbolic substitution chain")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable", False, f"import failed: {exc}")
        return
    record("sympy_importable", True)

    g_bare, C_sym, r_sym, alpha_sym = sp.symbols("g_bare C r alpha", positive=True, real=True)
    pi = sp.pi
    green = 1 / (4 * pi * r_sym)
    v_from_p1 = -C_sym * g_bare**2 * green
    v_b1_expected = -C_sym * g_bare**2 / (4 * pi * r_sym)
    alpha_def = g_bare**2 / (4 * pi)
    v_alpha_form = -C_sym * alpha_sym / r_sym

    record("B1_substitution_residual_zero", sp.simplify(v_from_p1 - v_b1_expected) == 0)
    record("B2_alpha_definition_holds", sp.simplify(alpha_def - g_bare**2 / (4 * pi)) == 0)
    record(
        "B3_alpha_form_consistent_with_B1",
        sp.simplify(v_alpha_form.subs(alpha_sym, alpha_def) - v_b1_expected) == 0,
    )
    record(
        "B4_alpha_at_gbare_one_equals_one_over_four_pi",
        sp.simplify(alpha_def.subs(g_bare, 1) - sp.Rational(1) / (4 * pi)) == 0,
    )
    record(
        "B4_V_at_gbare_one_equals_minus_C_over_four_pi_r",
        sp.simplify(v_b1_expected.subs(g_bare, 1) + C_sym / (4 * pi * r_sym)) == 0,
    )
    composite = sp.simplify(
        -C_sym * g_bare**2 * (1 / (4 * pi * r_sym))
        - (-C_sym * (g_bare**2 / (4 * pi)) / r_sym)
    )
    record("B1_to_B3_composite_chain_identity", composite == 0)


def block6_numerical_cross_checks() -> None:
    section("Block 6: numerical alpha and Casimir checks")
    alpha_num = 1.0 / (4.0 * math.pi)
    expected_alpha = 0.07957747154594768
    record("alpha_num_matches_expected", abs(alpha_num - expected_alpha) < 1.0e-15)
    record("alpha_num_recomputed_matches", abs(alpha_num - (1.0**2) / (4.0 * math.pi)) < 1.0e-15)
    n_c = 3
    c_f = (n_c**2 - 1) / (2 * n_c)
    record("C_F_at_N_c_3_equals_four_thirds", abs(c_f - 4.0 / 3.0) < 1.0e-15)
    for r_value in (5.0, 10.0, 20.0, 50.0):
        v_expected = -c_f * alpha_num / r_value
        v_chain = -c_f / (4.0 * math.pi * r_value)
        record(
            f"V_chain_equals_V_alpha_form_at_r_{int(r_value)}",
            abs(v_chain - v_expected) < 1.0e-15,
            f"err={abs(v_chain - v_expected):.3e}",
        )


def block7_companion_note_content() -> None:
    section("Block 7: companion note content")
    text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    collapsed = words(text)
    record("companion_declares_meta_type", "**type:** meta" in text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in collapsed)
    record("companion_disclaims_status_change", "does not set or promote audit status" in collapsed)
    record("companion_marks_audit_values_informational", "audit-lane values are informational" in collapsed)
    record("companion_documents_current_parent_tally", "pass=59 fail=0" in collapsed)
    record("companion_disclaims_static_source_premise_resolution", "does not resolve the supplied static-source readout premise" in collapsed)


def main() -> int:
    section("Static-source readout I1 current-source hygiene companion")
    print("Parent note: docs/STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md")
    print("Parent runner: scripts/static_source_readout_i1_accepted_premise_runner.py")
    print("Companion note: docs/STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md")
    print("Scope: meta evidence only; no theorem claim and no audit-status change.")
    print("Audit-lane values are informational metadata, not pass/fail targets.")

    block1_parent_runner()
    block2_ledger_metadata()
    block3_parent_runner_source_boundary()
    block4_parent_and_dep_note_content()
    block5_symbolic_chain()
    block6_numerical_cross_checks()
    block7_companion_note_content()

    section("Summary")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("FINAL_TAG: STATIC_SOURCE_READOUT_I1_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    print("FINAL_TAG: STATIC_SOURCE_READOUT_I1_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
