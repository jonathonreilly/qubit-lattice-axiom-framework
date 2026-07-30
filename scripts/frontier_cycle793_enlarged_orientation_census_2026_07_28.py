#!/usr/bin/env python3
"""Cycle 793: enlarged selector-family EventCell orientation census.

Counts only.  The Cycle-786 orientation rule is reimplemented from its pinned,
blocklisted text reference; the Cycle-788 primary is imported without running
its guarded main.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_STDOUT_MAX_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle788_selector_scope_extension_2026_07_28 as C788


S750 = C788.S750
K719 = C788.K719

EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py":
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py":
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py":
        "b8afe7e4697b0838715a079203930fb37bc7a6fc133e092f02a22141049aad8c",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
REFERENCE_REF = "origin/physics-loop/proof-grade-blockR7-20260729"
REFERENCE_COMMIT = "6a4d3a49f68808236403fe6310097459c2f7c07a"
REFERENCE_PATH = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py"
)
REFERENCE_SHA256 = (
    "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6"
)
BLOCKLISTED_MODULE_BASENAME = (
    "frontier_cycle786_ensemble_support_census_2026_07_28"
)
LANDED_BANKS = (2, 5, 12)
EXTENSION_BANKS = (1, 3)
SUPPLY_CAVEAT = (
    "the new events carry the declared selecting-supply layer (788); "
    "their orientations inherit that caveat; the landed 38's census does "
    "not change."
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def literal_audit_tuple() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
    audit = assignments.get("AUDIT_INPUT_PATHS")
    declared = assignments.get("DECLARED_INPUT_PATHS")
    return bool(
        isinstance(audit, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit.elts
        )
        and tuple(ast.literal_eval(audit)) == AUDIT_INPUT_PATHS
        and isinstance(declared, ast.Name)
        and declared.id == "AUDIT_INPUT_PATHS"
    )


def observed_input_sha256() -> dict[str, str]:
    return {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }


def pinned_reference_provenance() -> tuple[dict[str, object], str]:
    resolved = subprocess.run(
        ("git", "rev-parse", REFERENCE_REF),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    source_bytes = subprocess.run(
        ("git", "show", f"{REFERENCE_COMMIT}:{REFERENCE_PATH}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    source = source_bytes.decode("utf-8")
    normalized = " ".join(source.split())
    construction_checks = {
        "uses_landed_fixtures":
            "fixtures = S750.k_epoch_fixtures(bank_count)" in normalized,
        "unpacks_expected_state":
            "banks, links = K719.M.unpack_state(expected, bank_count)"
            in normalized,
        "decodes_local_graph":
            "chain, decode_order = K719.B.decode_local_graph(banks, links)"
            in normalized,
        "selects_eventcell_by_epoch":
            "new_cell = chain.cells[event]" in normalized,
        "reads_eventcell_orientation":
            '"new_event_cell_orientation": int(new_cell.orientation)'
            in normalized,
        "orientation_control_from_mode":
            "expected_orientation = 1 if direction == (1, 0) else -1"
            in normalized,
    }
    provenance = {
        "reference_ref": REFERENCE_REF,
        "resolved_commit": resolved,
        "pinned_commit": REFERENCE_COMMIT,
        "reference_path": REFERENCE_PATH,
        "reference_sha256": sha256(source_bytes).hexdigest(),
        "expected_reference_sha256": REFERENCE_SHA256,
        "handling": "pinned_text_only_blocklisted_not_imported",
        "construction_checks": construction_checks,
    }
    return provenance, source


def extension_machinery() -> tuple[
    dict[int, tuple[object, object, dict[str, object]]],
    dict[int, dict[str, object]],
]:
    fixtures = {}
    battery_controls = {}
    for bank_count in EXTENSION_BANKS:
        program, track, construction = C788.extension_fixture(bank_count)
        battery = C788.run_selector_battery(bank_count, program, track)
        fixtures[bank_count] = (program, track, construction)
        battery_controls[bank_count] = {
            "pass": bool(battery["pass"]),
            "epochs": int(battery["epochs"]),
            "selected": [
                row["selected"] for row in battery["selector_outputs"]
            ],
            "selected_count_range": battery["selected_count_range"],
            "tie_epochs": battery["tie_epochs"],
            "empty_epochs": battery["empty_epochs"],
            "program_stations": int(battery["program_stations"]),
            "track_sites": int(battery["spatial"]["track_sites"]),
        }
    return fixtures, battery_controls


def eventcell_orientation_rows(
    bank_counts: tuple[int, ...],
    extension_fixtures: dict[
        int, tuple[object, object, dict[str, object]]
    ],
) -> list[dict[str, object]]:
    """Reimplement the pinned Cycle-786 EventCell extraction."""
    rows: list[dict[str, object]] = []
    for bank_count in bank_counts:
        fixtures = S750.k_epoch_fixtures(bank_count)
        extension_program = (
            extension_fixtures[bank_count][0]
            if bank_count in extension_fixtures
            else None
        )
        for event, direction, program, before, expected in fixtures:
            alternatives = tuple(range(len(program)))
            selected = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            banks, links = K719.M.unpack_state(expected, bank_count)
            chain, decode_order = K719.B.decode_local_graph(banks, links)
            new_cell = chain.cells[event]
            mode = tuple(int(value) for value in direction)
            expected_orientation = 1 if mode == (1, 0) else -1
            rows.append(
                {
                    "family": (
                        "new_788" if bank_count in EXTENSION_BANKS
                        else "landed_786"
                    ),
                    "bank": bank_count,
                    "epoch_index": int(event),
                    "mode": list(mode),
                    "orientation": int(new_cell.orientation),
                    "orientation_control":
                        int(new_cell.orientation) == expected_orientation,
                    "eventcell_identity_control":
                        int(new_cell.identity) == int(event),
                    "eventcell_count_after": len(chain.cells),
                    "decode_order_tail": list(decode_order[-1]),
                    "selected": list(selected),
                    "selected_program_rows": [
                        [program[index][0], int(program[index][1])]
                        for index in selected
                    ],
                    "extension_program_identity": (
                        program == extension_program
                        if extension_program is not None
                        else None
                    ),
                }
            )
    return rows


def orientation_counts(rows: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(int(row["orientation"]) for row in rows)
    return {
        "+1": counts[1],
        "-1": counts[-1],
        "total": len(rows),
    }


def per_bank_counts(
    rows: list[dict[str, object]],
) -> dict[int, dict[str, int]]:
    banks = sorted({int(row["bank"]) for row in rows})
    return {
        bank: orientation_counts(
            [row for row in rows if int(row["bank"]) == bank]
        )
        for bank in banks
    }


def main() -> int:
    started = monotonic()
    lines: list[str] = []

    observed_anchors = observed_input_sha256()
    reference, _reference_source = pinned_reference_provenance()
    extension_fixtures, battery_controls = extension_machinery()
    landed_rows = eventcell_orientation_rows(
        LANDED_BANKS, extension_fixtures
    )
    new_rows = eventcell_orientation_rows(
        EXTENSION_BANKS, extension_fixtures
    )
    enlarged_rows = landed_rows + new_rows

    landed_counts = orientation_counts(landed_rows)
    new_counts = orientation_counts(new_rows)
    enlarged_counts = orientation_counts(enlarged_rows)
    by_bank = per_bank_counts(enlarged_rows)
    landed_by_bank = per_bank_counts(landed_rows)
    new_by_bank = per_bank_counts(new_rows)

    machinery_basis = {
        "cycle788_usage": "direct_import_guarded_main_not_called",
        "cycle788_module": C788.__name__,
        "cycle750_module": S750.__name__,
        "cycle719_controller_module": K719.__name__,
        "cycle719_core_module": K719.B.__name__,
        "cycle788_imports_cycle750_object": C788.S750 is S750,
        "cycle788_imports_cycle719_controller_object": C788.K719 is K719,
        "cycle750_imports_cycle719_controller_object": S750.K is K719,
        "cycle788_extension_banks": list(C788.EXTENSION_BANK_SIZES),
        "orientation_rule": (
            "fixture expected state -> K719.M.unpack_state -> "
            "K719.B.decode_local_graph -> chain.cells[event].orientation"
        ),
        "mode_control": (
            "(1,0) -> +1; (0,1) -> -1, exactly as pinned Cycle 786"
        ),
        "reference_module_imported": any(
            BLOCKLISTED_MODULE_BASENAME in name for name in sys.modules
        ),
    }

    certificate_a = all(
        (
            literal_audit_tuple(),
            observed_anchors == EXPECTED_INPUT_SHA256,
            reference["resolved_commit"] == REFERENCE_COMMIT,
            reference["reference_sha256"] == REFERENCE_SHA256,
            all(reference["construction_checks"].values()),
            machinery_basis["cycle788_imports_cycle750_object"],
            machinery_basis["cycle788_imports_cycle719_controller_object"],
            machinery_basis["cycle750_imports_cycle719_controller_object"],
            K719.B.__name__
            == "frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26",
            tuple(C788.EXTENSION_BANK_SIZES) == EXTENSION_BANKS,
            not machinery_basis["reference_module_imported"],
            C788.PASS == 0,
            C788.FAIL == 0,
        )
    )

    landed_fixture_counts = Counter(
        int(row["bank"]) for row in landed_rows
    )
    certificate_b = all(
        (
            len(landed_rows) == 38,
            landed_fixture_counts == {2: 4, 5: 10, 12: 24},
            landed_counts == {"+1": 19, "-1": 19, "total": 38},
            landed_by_bank == {
                2: {"+1": 2, "-1": 2, "total": 4},
                5: {"+1": 5, "-1": 5, "total": 10},
                12: {"+1": 12, "-1": 12, "total": 24},
            },
            all(row["orientation_control"] for row in landed_rows),
            all(row["eventcell_identity_control"] for row in landed_rows),
            all(row["selected"] == [0] for row in landed_rows),
            all(
                row["selected_program_rows"] == [["source", 0]]
                for row in landed_rows
            ),
        )
    )

    expected_new_signature = [
        (1, 0, (1, 0), 1),
        (1, 1, (0, 1), -1),
        (3, 0, (1, 0), 1),
        (3, 1, (0, 1), -1),
        (3, 2, (1, 0), 1),
        (3, 3, (0, 1), -1),
        (3, 4, (1, 0), 1),
        (3, 5, (0, 1), -1),
    ]
    observed_new_signature = [
        (
            int(row["bank"]),
            int(row["epoch_index"]),
            tuple(int(value) for value in row["mode"]),
            int(row["orientation"]),
        )
        for row in new_rows
    ]
    certificate_c = all(
        (
            len(new_rows) == 8,
            Counter(int(row["bank"]) for row in new_rows) == {1: 2, 3: 6},
            observed_new_signature == expected_new_signature,
            new_counts == {"+1": 4, "-1": 4, "total": 8},
            new_by_bank == {
                1: {"+1": 1, "-1": 1, "total": 2},
                3: {"+1": 3, "-1": 3, "total": 6},
            },
            all(row["orientation_control"] for row in new_rows),
            all(row["eventcell_identity_control"] for row in new_rows),
            all(row["extension_program_identity"] for row in new_rows),
            all(row["selected"] == [0] for row in new_rows),
            all(control["pass"] for control in battery_controls.values()),
            battery_controls[1]["epochs"] == 2,
            battery_controls[3]["epochs"] == 6,
            all(
                control["selected_count_range"] == [1, 1]
                and not control["tie_epochs"]
                and not control["empty_epochs"]
                for control in battery_controls.values()
            ),
        )
    )

    balance_verdict = (
        "BALANCED_23_23"
        if enlarged_counts == {"+1": 23, "-1": 23, "total": 46}
        else f"NOT_BALANCED_{enlarged_counts['+1']}_{enlarged_counts['-1']}"
    )
    certificate_d = all(
        (
            len(enlarged_rows) == 46,
            enlarged_counts == {"+1": 23, "-1": 23, "total": 46},
            by_bank == {
                1: {"+1": 1, "-1": 1, "total": 2},
                2: {"+1": 2, "-1": 2, "total": 4},
                3: {"+1": 3, "-1": 3, "total": 6},
                5: {"+1": 5, "-1": 5, "total": 10},
                12: {"+1": 12, "-1": 12, "total": 24},
            },
            balance_verdict == "BALANCED_23_23",
            landed_counts["+1"] + new_counts["+1"] == 23,
            landed_counts["-1"] + new_counts["-1"] == 23,
        )
    )

    extension_fixtures_repeat, battery_controls_repeat = extension_machinery()
    landed_rows_repeat = eventcell_orientation_rows(
        LANDED_BANKS, extension_fixtures_repeat
    )
    new_rows_repeat = eventcell_orientation_rows(
        EXTENSION_BANKS, extension_fixtures_repeat
    )
    deterministic = all(
        (
            battery_controls_repeat == battery_controls,
            {
                bank: construction
                for bank, (_program, _track, construction)
                in extension_fixtures_repeat.items()
            }
            == {
                bank: construction
                for bank, (_program, _track, construction)
                in extension_fixtures.items()
            },
            landed_rows_repeat == landed_rows,
            new_rows_repeat == new_rows,
            orientation_counts(landed_rows_repeat + new_rows_repeat)
            == enlarged_counts,
        )
    )
    boundaries = {
        "counts_only": True,
        "no_weights": True,
        "no_rate": True,
        "no_probability": True,
        "axiom_update_triggered": False,
    }

    lines.append("ANCHORS " + compact(observed_anchors))
    lines.append("REFERENCE_PROVENANCE " + compact(reference))
    lines.append("MACHINERY_BASIS " + compact(machinery_basis))
    for bank_count in EXTENSION_BANKS:
        _program, _track, construction = extension_fixtures[bank_count]
        lines.append(
            "EXTENSION_SUPPLY_CONSTRUCTION " + compact(construction)
        )
        lines.append(
            "EXTENSION_BATTERY_CONTROL "
            + compact(
                {"bank": bank_count, **battery_controls[bank_count]}
            )
        )
    lines.append("LANDED_38_CENSUS " + compact(landed_counts))
    for row in new_rows:
        lines.append("NEW_EVENT_ORIENTATION " + compact(row))
    for bank_count in sorted(by_bank):
        lines.append(
            "ORIENTATION_BY_BANK "
            + compact({"bank": bank_count, **by_bank[bank_count]})
        )
    composition = {
        "landed_banks_2_5_12": landed_counts,
        "new_bank_1": new_by_bank[1],
        "new_bank_3": new_by_bank[3],
        "new_788_total": new_counts,
        "enlarged_46": enlarged_counts,
    }
    lines.append("ORIENTATION_COMPOSITION " + compact(composition))
    lines.append(
        "BALANCE_VERDICT "
        + compact(
            {
                "verdict": balance_verdict,
                "split": enlarged_counts,
            }
        )
    )
    lines.append("SUPPLY_CAVEAT " + SUPPLY_CAVEAT)
    lines.append("BOUNDARIES " + compact(boundaries))
    lines.append(
        ("CERTIFICATE_A_PASS" if certificate_a else "CERTIFICATE_A_FAIL")
        + " anchors + machinery basis + reference provenance :: "
        + compact(
            {
                "literal_AUDIT_INPUT_PATHS": literal_audit_tuple(),
                "sha_anchors": observed_anchors == EXPECTED_INPUT_SHA256,
                "reference": reference,
                "machinery_basis": machinery_basis,
            }
        )
    )
    lines.append(
        ("CERTIFICATE_B_PASS" if certificate_b else "CERTIFICATE_B_FAIL")
        + " landed 19/19 identity control :: "
        + compact(
            {
                "census": landed_counts,
                "by_bank": landed_by_bank,
                "rows_sha256": digest(landed_rows),
            }
        )
    )
    lines.append(
        ("CERTIFICATE_C_PASS" if certificate_c else "CERTIFICATE_C_FAIL")
        + " eight new EventCell orientations :: "
        + compact(
            {
                "signature": observed_new_signature,
                "by_bank": new_by_bank,
                "battery_controls": battery_controls,
            }
        )
    )
    lines.append(
        ("CERTIFICATE_D_PASS" if certificate_d else "CERTIFICATE_D_FAIL")
        + " enlarged census + per-bank structure + verdict :: "
        + compact(
            {
                "composition": composition,
                "by_bank": by_bank,
                "verdict": balance_verdict,
            }
        )
    )

    elapsed = monotonic() - started
    certificate_e_base = all(
        (
            boundaries
            == {
                "counts_only": True,
                "no_weights": True,
                "no_rate": True,
                "no_probability": True,
                "axiom_update_triggered": False,
            },
            SUPPLY_CAVEAT
            == (
                "the new events carry the declared selecting-supply layer "
                "(788); their orientations inherit that caveat; the landed "
                "38's census does not change."
            ),
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
        )
    )

    actual_stdout_bytes = 0
    final_lines: list[str] = []
    for _iteration in range(10):
        certificate_e = (
            certificate_e_base
            and actual_stdout_bytes < AUDIT_STDOUT_MAX_BYTES
        )
        passed = all(
            (
                certificate_a,
                certificate_b,
                certificate_c,
                certificate_d,
                certificate_e,
            )
        )
        certificate_e_line = (
            ("CERTIFICATE_E_PASS" if certificate_e else "CERTIFICATE_E_FAIL")
            + " boundaries + determinism + bounds :: "
            + compact(
                {
                    "boundaries": boundaries,
                    "deterministic": deterministic,
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                    "actual_stdout_bytes": actual_stdout_bytes,
                    "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
                }
            )
        )
        summary = {
            "cycle": 793,
            "pass": passed,
            "certificates": {
                "A": certificate_a,
                "B": certificate_b,
                "C": certificate_c,
                "D": certificate_d,
                "E": certificate_e,
            },
            "landed_38": landed_counts,
            "new_8": new_counts,
            "enlarged_46": enlarged_counts,
            "per_bank": by_bank,
            "balance_verdict": balance_verdict,
            "event_rows_sha256": digest(enlarged_rows),
            "runtime_seconds": round(elapsed, 6),
            **boundaries,
        }
        final_lines = lines + [
            certificate_e_line,
            "SUMMARY_JSON " + compact(summary),
            (
                "CYCLE793_ENLARGED_ORIENTATION_CENSUS_PASS"
                if passed
                else "CYCLE793_ENLARGED_ORIENTATION_CENSUS_INCOMPLETE"
            ),
        ]
        measured = len(("\n".join(final_lines) + "\n").encode("utf-8"))
        if measured == actual_stdout_bytes:
            break
        actual_stdout_bytes = measured

    output = "\n".join(final_lines) + "\n"
    if len(output.encode("utf-8")) >= AUDIT_STDOUT_MAX_BYTES:
        print(
            "CERTIFICATE_E_FAIL boundaries + determinism + bounds :: "
            + compact(
                {
                    "actual_stdout_bytes": len(output.encode("utf-8")),
                    "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
                }
            )
        )
        print("CYCLE793_ENLARGED_ORIENTATION_CENSUS_INCOMPLETE")
        return 1
    sys.stdout.write(output)
    return 0 if all(
        (
            certificate_a,
            certificate_b,
            certificate_c,
            certificate_d,
            certificate_e,
        )
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
