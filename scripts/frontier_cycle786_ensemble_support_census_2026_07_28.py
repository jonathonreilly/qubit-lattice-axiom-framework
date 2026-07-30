#!/usr/bin/env python3
"""Cycle 786: selector-epoch support census over formation channels.

This bounded runner keeps origin-resolved counts separate from the weaker
orientation correspondence that is actually present on the landed surfaces.
It reads counts/support only; it neither constructs nor interprets weights.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 1500
AUDIT_STDOUT_MAX_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
BLOCKLISTED_TEXT_BASENAME = "frontier_cycle785"
SELECTOR_MODULE_NAME = "frontier_cycle750_actual_selector_stretch_2026_07_28"
SELECTOR_LANDED_GIT_BLOB = "0a8f4562d28f12ed64130b3c3b23fccab677d333"

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]: "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    AUDIT_INPUT_PATHS[1]: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]: "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]: "d5403ebbf51d8ecfaf621d5e0983d333b8df9a7d589145095b598c530ac15ab4",
}

# Pinned from the first incremental execution of the exact landed functions.
EXPECTED_SELECTOR_ROWS_SHA256 = (
    "06acd9600b0a45f20aaace6737f6d7d4a0092c2d60a4e4d5e669de5e61666419"
)
EXPECTED_OUTCOME_ROWS_SHA256 = (
    "5833a7ca213ad8053fa05b3bc054db15b67188516b6b07a105c2396cddf5a71c"
)

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


def selector_source_bytes() -> tuple[bytes, str]:
    """Use the worktree file, or its immutable landed blob on stale bases."""
    selector_path = ROOT / AUDIT_INPUT_PATHS[2]
    if selector_path.is_file():
        return selector_path.read_bytes(), "worktree"
    completed = subprocess.run(
        ("git", "cat-file", "blob", SELECTOR_LANDED_GIT_BLOB),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return completed.stdout, "landed_git_blob"


def load_selector() -> tuple[ModuleType, str]:
    source, locator = selector_source_bytes()
    module = ModuleType(SELECTOR_MODULE_NAME)
    module.__file__ = str(ROOT / AUDIT_INPUT_PATHS[2])
    module.__package__ = ""
    sys.modules[SELECTOR_MODULE_NAME] = module
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    return module, locator


S750, SELECTOR_SOURCE_LOCATOR = load_selector()


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def literal_audit_tuple() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            continue
        return (
            isinstance(node.value, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in node.value.elts
            )
            and tuple(ast.literal_eval(node.value)) == AUDIT_INPUT_PATHS
        )
    return False


def observed_sha256() -> dict[str, str]:
    observed = {}
    for path in AUDIT_INPUT_PATHS:
        source = (
            selector_source_bytes()[0]
            if path == AUDIT_INPUT_PATHS[2]
            else (ROOT / path).read_bytes()
        )
        observed[path] = sha256(source).hexdigest()
    return observed


def packet_write_code(projection: dict[str, object]) -> int:
    """The Cycle-769-style seven-bit record/write projection."""
    fields = (
        "endpoint",
        "carry",
        "binder",
        "valid",
        "actuality",
        "admissibility",
        "law_domain",
    )
    return sum(int(projection[field]) << index for index, field in enumerate(fields))


def branch_target(basis: int) -> int:
    matter = basis & ((1 << 12) - 1)
    if matter.bit_count() != 1:
        raise AssertionError(("non-one-hot matter branch", matter))
    return matter.bit_length() - 1


def derive_origin_catalog() -> tuple[list[dict[str, object]], dict[str, object]]:
    """Derive 12 x 6 branches; execute exactly one write pass per origin."""
    transitions, transition_certificate = C719.instrument_transition()
    catalog: list[dict[str, object]] = []
    total_controller_write_passes = 0

    for origin in range(12):
        transition_row = transitions[origin]
        family = [
            {
                "branch_index": branch_index,
                "target": int(target),
                "orientation": int(orientation),
                "pointer_shaped": bool(orientation),
            }
            for branch_index, (target, orientation, _coefficient) in enumerate(
                transition_row
            )
        ]

        banks0, links0 = C719.B.chain_genesis(C719.BANKS)
        genesis_chain, _genesis_order = C719.B.decode_local_graph(banks0, links0)
        initial = C719.tuple_to_int(
            C719.M.pack_state(banks0, links0, matter=1 << origin)
        )
        sparse_branches = C719.C713.apply_sparse_word(
            {initial: 1.0 + 0.0j},
            C719.MATTER_WORD,
        )
        by_target = {branch_target(basis): basis for basis in sparse_branches}
        if not (len(sparse_branches) == len(by_target) == 6):
            raise AssertionError(("branch family not six distinct targets", origin))

        source_pointer = C719.R3_SOURCE_POINTER()
        pointer_rows = {
            target: (basis >> source_pointer) & 1
            for target, basis in by_target.items()
        }
        record_rows = [row for row in family if row["pointer_shaped"]]
        if len(record_rows) != 1:
            raise AssertionError(("record-shaped branch count", origin, record_rows))
        record_row = record_rows[0]
        record_target = int(record_row["target"])
        if pointer_rows != {
            int(row["target"]): int(row["target"] == record_target)
            for row in family
        }:
            raise AssertionError(("pointer/transition mismatch", origin, pointer_rows))

        # The bounded 769-style test: only this candidate gets one controller
        # write pass.  Other branches are excluded by the landed source pointer.
        written = C719.sparse_controller_orbit(
            {by_target[record_target]: 1.0 + 0.0j},
            C719.PROGRAM,
        )[0]
        total_controller_write_passes += 1
        if len(written) != 1:
            raise AssertionError(("nonclassical record write", origin, len(written)))
        written_basis = next(iter(written))
        written_bits = C719.int_to_tuple(written_basis)
        banks1, links1 = C719.M.unpack_state(written_bits, C719.BANKS)
        written_chain, written_order = C719.B.decode_local_graph(banks1, links1)
        projection = C719.A.packet_projection(banks1[0], 0)
        if projection is None:
            raise AssertionError(("missing packet projection", origin))
        write_code = packet_write_code(projection)
        pipeline = [len(genesis_chain.cells), pointer_rows[record_target], write_code]
        cell_rows = C719.B.cell_rows(written_chain)

        catalog.append(
            {
                "origin": origin,
                "branch_family": family,
                "record_branch_index": int(record_row["branch_index"]),
                "record_target": record_target,
                "record_orientation": int(record_row["orientation"]),
                "write_pipeline": pipeline,
                "event_cells": len(written_chain.cells),
                "event_cell": cell_rows[0] if len(cell_rows) == 1 else None,
                "decode_order": [list(pair) for pair in written_order],
                "postwrite_source_pointer": written_bits[source_pointer],
            }
        )

    evidence = {
        "transition_certificate": transition_certificate,
        "origins": len(catalog),
        "branches": sum(len(row["branch_family"]) for row in catalog),
        "controller_write_passes": total_controller_write_passes,
        "record_branches": sum(
            sum(bool(branch["pointer_shaped"]) for branch in row["branch_family"])
            for row in catalog
        ),
        "program_stations": len(C719.PROGRAM),
        "program_sha256": C719.K.gate_digest(C719.ALLOCATOR),
    }
    return catalog, evidence


def selector_epoch_rows(
    catalog: list[dict[str, object]],
) -> list[dict[str, object]]:
    orientation_origins = {
        orientation: [
            int(row["origin"])
            for row in catalog
            if row["record_orientation"] == orientation
        ]
        for orientation in (-1, 1)
    }
    rows: list[dict[str, object]] = []
    ordinal = 0
    for bank_count in (2, 5, 12):
        fixtures = S750.k_epoch_fixtures(bank_count)
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
            expected_orientation = 1 if direction == (1, 0) else -1
            new_cell = chain.cells[event]
            origins = orientation_origins[int(new_cell.orientation)]
            rows.append(
                {
                    "epoch_ordinal": ordinal,
                    "fixture": f"banks{bank_count}_event{event}",
                    "banks": bank_count,
                    "event": event,
                    "direction": list(direction),
                    "alternative_count": len(alternatives),
                    "selected_actual_alternatives": list(selected),
                    "selected_program_rows": [
                        [program[index][0], int(program[index][1])]
                        for index in selected
                    ],
                    "event_cell_count_after": len(chain.cells),
                    "new_event_cell_orientation": int(new_cell.orientation),
                    "orientation_control": int(new_cell.orientation)
                    == expected_orientation,
                    "decode_order_tail": list(decode_order[-1]),
                    "record_shaped_reached": True,
                    "origin_candidates": origins,
                    "origin_correspondence": "AMBIGUOUS_SIX_WAY",
                    "outcome_id": ordinal % len(R693.CONTENT),
                }
            )
            ordinal += 1
    return rows


def selector_identity_bytes(rows: list[dict[str, object]]) -> list[object]:
    return [
        [
            row["banks"],
            row["event"],
            row["direction"],
            row["alternative_count"],
            row["selected_actual_alternatives"],
        ]
        for row in rows
    ]


def outcome_identity_bytes(rows: list[dict[str, object]]) -> list[object]:
    return [
        [row["epoch_ordinal"], row["fixture"], row["outcome_id"]]
        for row in rows
    ]


def support_census(
    catalog: list[dict[str, object]],
    rows: list[dict[str, object]],
) -> dict[str, object]:
    orientations = Counter(int(row["new_event_cell_orientation"]) for row in rows)
    possible = Counter(
        origin
        for row in rows
        for origin in row["origin_candidates"]
    )
    per_origin = []
    for channel in catalog:
        origin = int(channel["origin"])
        compatible = possible[origin]
        per_origin.append(
            {
                "origin": origin,
                "record_branch_index": channel["record_branch_index"],
                "record_target": channel["record_target"],
                "orientation": channel["record_orientation"],
                "exact_epoch_count": None,
                "compatible_epoch_count": compatible,
                "one_origin_refinement_range": [0, compatible],
                "status": "AMBIGUOUS_SIX_WAY",
            }
        )
    outcomes = Counter(int(row["outcome_id"]) for row in rows)
    return {
        "epochs": len(rows),
        "exact_orientation_channel_counts": {
            "+1": orientations[1],
            "-1": orientations[-1],
        },
        "per_origin_channels": per_origin,
        "record_shaped_none_count": sum(
            not bool(row["record_shaped_reached"]) for row in rows
        ),
        "outcome_identity_census": [outcomes[index] for index in range(3)],
        "origin_count_status": (
            "UNDEFINED_BY_LANDED_SURFACES: each epoch fixes orientation but "
            "contains no one-hot matter-origin field"
        ),
    }


def main() -> int:
    started = monotonic()
    lines: list[str] = []

    observed_anchors = observed_sha256()
    catalog, catalog_evidence = derive_origin_catalog()
    epochs = selector_epoch_rows(catalog)
    census = support_census(catalog, epochs)

    selector_facts = selector_identity_bytes(epochs)
    outcome_facts = outcome_identity_bytes(epochs)
    selector_rows_sha256 = digest(selector_facts)
    outcome_rows_sha256 = digest(outcome_facts)

    # Determinism repeats the selector machinery but not the bounded
    # one-controller-pass-per-origin write test.
    epochs_repeat = selector_epoch_rows(catalog)
    deterministic = (
        selector_identity_bytes(epochs_repeat) == selector_facts
        and outcome_identity_bytes(epochs_repeat) == outcome_facts
        and support_census(catalog, epochs_repeat) == census
    )

    origin_zero = catalog[0]
    pipelines = [row["write_pipeline"] for row in catalog]
    event_cells = [row["event_cell"] for row in catalog]
    certificate_a = all(
        (
            literal_audit_tuple(),
            observed_anchors == EXPECTED_SHA256,
            SELECTOR_SOURCE_LOCATOR in ("worktree", "landed_git_blob"),
            C719.K is K719,
            S750.K is K719,
            not any(BLOCKLISTED_TEXT_BASENAME in name for name in sys.modules),
            catalog_evidence["transition_certificate"]
            == {
                "source_modes": 12,
                "transition_entries": 72,
                "failures": 0,
                "endpoint_aux_cleanup_failures": 0,
            },
            catalog_evidence["origins"] == 12,
            catalog_evidence["branches"] == 72,
            catalog_evidence["record_branches"] == 12,
            catalog_evidence["controller_write_passes"] == 12,
            all(pipeline == [0, 1, 125] for pipeline in pipelines),
            all(row["event_cells"] == 1 for row in catalog),
            all(row["postwrite_source_pointer"] == 0 for row in catalog),
        )
    )

    total_alternatives = sum(int(row["alternative_count"]) for row in epochs)
    bank_fixture_counts = {
        size: sum(int(row["banks"]) == size for row in epochs)
        for size in (2, 5, 12)
    }
    candidate_sets = {
        int(row["new_event_cell_orientation"]): tuple(row["origin_candidates"])
        for row in epochs
    }
    correspondence_evidence = {
        "basis": "AMBIGUOUS: LANDED ORIENTATION-ONLY CORRESPONDENCE",
        "selector_actual_alternative": 0,
        "selector_alternative_type": "controller program-station index",
        "selected_program_row": ["source", 0],
        "selector_fixture_fields": [
            "event",
            "direction",
            "program",
            "before",
            "expected",
        ],
        "origin_catalog_key": "one-hot Cycle719 matter origin in range(12)",
        "missing_landed_join_key": "matter origin",
        "landed_join_key_that_exists": "new EventCell orientation",
        "orientation_to_origin_candidates": {
            "+1": candidate_sets.get(1, ()),
            "-1": candidate_sets.get(-1, ()),
        },
        "supplied_correspondence_convention": None,
    }
    certificate_b = all(
        (
            len(epochs) == 38,
            bank_fixture_counts == {2: 4, 5: 10, 12: 24},
            all(row["selected_actual_alternatives"] == [0] for row in epochs),
            all(row["selected_program_rows"] == [["source", 0]] for row in epochs),
            all(row["orientation_control"] for row in epochs),
            all(row["record_shaped_reached"] for row in epochs),
            candidate_sets == {1: (0, 1, 2, 3, 4, 5), -1: (6, 7, 8, 9, 10, 11)},
            correspondence_evidence["supplied_correspondence_convention"] is None,
        )
    )

    expected_channel_rows = [
        {
            "origin": origin,
            "record_branch_index": 0 if origin < 6 else 1,
            "record_target": 6 if origin < 6 else 1,
            "orientation": 1 if origin < 6 else -1,
            "exact_epoch_count": None,
            "compatible_epoch_count": 19,
            "one_origin_refinement_range": [0, 19],
            "status": "AMBIGUOUS_SIX_WAY",
        }
        for origin in range(12)
    ]
    certificate_c = all(
        (
            census["epochs"] == 38,
            census["exact_orientation_channel_counts"] == {"+1": 19, "-1": 19},
            census["per_origin_channels"] == expected_channel_rows,
            census["record_shaped_none_count"] == 0,
        )
    )

    boundaries = (
        "counts are event-ensemble support DATA upstream of W6; "
        "`no_weights: true`, `no_rate_law: true`, `no_probability: true`; "
        "the W6 weight boundary and the 748 rule (no weight statement) unchanged; "
        "`axiom_update_triggered: false`."
    )
    identity_controls = {
        "selector_fixture_count": len(epochs),
        "fixture_counts_by_banks": bank_fixture_counts,
        "alternatives_exhausted": total_alternatives,
        "selected_actual_alternatives": sorted(
            {tuple(row["selected_actual_alternatives"]) for row in epochs}
        ),
        "selector_rows_sha256": selector_rows_sha256,
        "selector_rows_expected_sha256": EXPECTED_SELECTOR_ROWS_SHA256,
        "outcome_mapping": (
            "TASK-SUPPLIED landed Cycle757 identity: global selector fixture "
            "ordinal modulo the three landed R693 record identities"
        ),
        "outcome_rows_sha256": outcome_rows_sha256,
        "outcome_rows_expected_sha256": EXPECTED_OUTCOME_ROWS_SHA256,
        "outcome_census": census["outcome_identity_census"],
        "origin0_Cycle769_identity": {
            "record_branch_index": origin_zero["record_branch_index"],
            "record_target": origin_zero["record_target"],
            "record_orientation": origin_zero["record_orientation"],
            "write_pipeline": origin_zero["write_pipeline"],
            "event_cell": origin_zero["event_cell"],
        },
        "R693_record_identities": len(R693.CONTENT),
    }
    certificate_d = all(
        (
            len(epochs) == 38,
            bank_fixture_counts == {2: 4, 5: 10, 12: 24},
            total_alternatives == 2578,
            all(row["selected_actual_alternatives"] == [0] for row in epochs),
            selector_rows_sha256 == EXPECTED_SELECTOR_ROWS_SHA256,
            outcome_rows_sha256 == EXPECTED_OUTCOME_ROWS_SHA256,
            census["outcome_identity_census"] == [13, 13, 12],
            len(R693.CONTENT) == 3,
            origin_zero["record_branch_index"] == 0,
            origin_zero["record_target"] == 6,
            origin_zero["record_orientation"] == 1,
            origin_zero["write_pipeline"] == [0, 1, 125],
            boundaries
            == (
                "counts are event-ensemble support DATA upstream of W6; "
                "`no_weights: true`, `no_rate_law: true`, `no_probability: true`; "
                "the W6 weight boundary and the 748 rule (no weight statement) unchanged; "
                "`axiom_update_triggered: false`."
            ),
        )
    )

    lines.append("ANCHORS " + compact(observed_anchors))
    lines.append(
        "MODULE_EVIDENCE "
        + compact(
            {
                "controller_imports_core_object": C719.K is K719,
                "selector_imports_core_object": S750.K is K719,
                "selector_source_locator": SELECTOR_SOURCE_LOCATOR,
                "selector_landed_git_blob": SELECTOR_LANDED_GIT_BLOB,
                "cycle785_imported": any(
                    BLOCKLISTED_TEXT_BASENAME in name for name in sys.modules
                ),
            }
        )
    )
    lines.append("ORIGIN_CATALOG_CONSTRUCTION " + compact(catalog_evidence))
    lines.append(
        "WRITE_CODE_FIELD_ORDER "
        + compact(
            [
                "endpoint",
                "carry",
                "binder",
                "valid",
                "actuality",
                "admissibility",
                "law_domain",
            ]
        )
    )
    for row in catalog:
        lines.append("ORIGIN_CHANNEL " + compact(row))
    lines.append("CORRESPONDENCE_CONSTRUCTION " + compact(correspondence_evidence))
    for row in epochs:
        lines.append("EPOCH_CHANNEL_MAP " + compact(row))
    lines.append(
        "SUPPORT_CENSUS_ORIENTATION "
        + compact(census["exact_orientation_channel_counts"])
    )
    for row in census["per_origin_channels"]:
        lines.append("SUPPORT_CENSUS_CHANNEL " + compact(row))
    lines.append(
        "SUPPORT_CENSUS_NONE " + compact(census["record_shaped_none_count"])
    )
    lines.append("BOUNDARIES " + boundaries)
    lines.append("IDENTITY_CONTROLS " + compact(identity_controls))

    lines.append(
        ("CERTIFICATE_A_PASS" if certificate_a else "CERTIFICATE_A_FAIL")
        + " anchors + origin-catalog derivation :: "
        + compact(
            {
                "literal_AUDIT_INPUT_PATHS": literal_audit_tuple(),
                "sha_anchors": observed_anchors == EXPECTED_SHA256,
                "selector_source_locator": SELECTOR_SOURCE_LOCATOR,
                "origins": catalog_evidence["origins"],
                "branches": catalog_evidence["branches"],
                "write_passes": catalog_evidence["controller_write_passes"],
            }
        )
    )
    lines.append(
        ("CERTIFICATE_B_PASS" if certificate_b else "CERTIFICATE_B_FAIL")
        + " epoch-to-channel correspondence :: "
        + compact(correspondence_evidence)
    )
    lines.append(
        ("CERTIFICATE_C_PASS" if certificate_c else "CERTIFICATE_C_FAIL")
        + " 38-epoch support census :: "
        + compact(census)
    )
    lines.append(
        ("CERTIFICATE_D_PASS" if certificate_d else "CERTIFICATE_D_FAIL")
        + " boundaries + identity controls :: "
        + compact(identity_controls)
    )

    elapsed = monotonic() - started
    projected_stdout_bytes = len(("\n".join(lines) + "\n").encode("utf-8")) + 5000
    certificate_e = all(
        (
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
            projected_stdout_bytes < AUDIT_STDOUT_MAX_BYTES,
        )
    )
    lines.append(
        ("CERTIFICATE_E_PASS" if certificate_e else "CERTIFICATE_E_FAIL")
        + " determinism + bounds :: "
        + compact(
            {
                "deterministic": deterministic,
                "runtime_seconds": round(elapsed, 6),
                "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                "projected_stdout_bytes_upper_bound": projected_stdout_bytes,
                "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
            }
        )
    )

    passed = all(
        (certificate_a, certificate_b, certificate_c, certificate_d, certificate_e)
    )
    report = {
        "cycle": 786,
        "pass": passed,
        "certificates": {
            "A": certificate_a,
            "B": certificate_b,
            "C": certificate_c,
            "D": certificate_d,
            "E": certificate_e,
        },
        "correspondence_basis": correspondence_evidence["basis"],
        "supplied_correspondence_convention": None,
        "support_census": census,
        "selector_rows_sha256": selector_rows_sha256,
        "outcome_rows_sha256": outcome_rows_sha256,
        "runtime_seconds": round(elapsed, 6),
        "no_weights": True,
        "no_rate_law": True,
        "no_probability": True,
        "axiom_update_triggered": False,
    }
    report["report_sha256"] = digest(report)
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(
        "CYCLE786_ENSEMBLE_SUPPORT_CENSUS_PASS"
        if passed
        else "CYCLE786_ENSEMBLE_SUPPORT_CENSUS_INCOMPLETE"
    )

    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= AUDIT_STDOUT_MAX_BYTES:
        print(
            "CERTIFICATE_E_FAIL determinism + bounds :: "
            + compact(
                {
                    "actual_stdout_bytes": len(output.encode("utf-8")),
                    "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
                }
            )
        )
        print("CYCLE786_ENSEMBLE_SUPPORT_CENSUS_INCOMPLETE")
        return 1
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
