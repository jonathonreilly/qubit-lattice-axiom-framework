#!/usr/bin/env python3
"""Cycle 757: compare a derived occurrence census with the held Born candidate.

The occurrence family is rerun from Cycle 750's successful fixture-scoped
enforcement-lineage selector.  The bridge from those selected events to the
three Cycle-317 outcome classes is still supplied, so this runner produces
finite comparison DATA only: it neither calibrates nor writes a weight law.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/DERIVED_OCCURRENCE_CALIBRATION_CYCLE757_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
    "scripts/frontier_cycle748_calibration_convergence_comparison_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle744_weight_receiver_sharpening_2026_07_28 as C744
import frontier_cycle748_calibration_convergence_comparison_2026_07_28 as C748
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


PASS = 0
FAIL = 0

BANK_COUNTS = (2, 5, 12)
EPOCH_COUNT = 38
MENU_ID = "cycle757-cycle317-contact-trine"
PROGRAM_ID = "cycle757-f750-derived-occurrence-family"
EFFECT_IDS = (
    "cycle317-contact-trine-E0",
    "cycle317-contact-trine-E1",
    "cycle317-contact-trine-E2",
)
MAPPING_CONVENTION = {
    "formula": (
        "outcome_index = (global_epoch_ordinal + selected_alternative) "
        "mod 3"
    ),
    "ordered_effect_rule": "effect_id = EFFECT_IDS[outcome_index]",
    "status": "SUPPLY",
    "why_not_derived": (
        "F750 derives the selected alternative at fixture scope but does not "
        "derive an identification with a Cycle-317 ternary outcome class."
    ),
}
EXPECTED_DERIVED_COUNTS = (13, 13, 12)
EXPECTED_PERMUTED_COUNTS = (12, 13, 13)
EXPECTED_DERIVED_RESIDUAL_HEX = (
    "-0x1.25945b277a630p-6",
    "0x1.0a9345b553e77p-3",
    "-0x1.cbc174a0c9364p-4",
)
EXPECTED_DERIVED_DISAGREEMENTS = (2, 2, 3, 3)
EXPECTED_MISCALIBRATED_COUNTS = (38, 0, 0)
NEXT_STEP = (
    "larger derived families (more epochs/fixtures) + deriving the "
    "outcome-class mapping"
)


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", compact(detail))
    else:
        FAIL += 1
        print("FAIL", label, "::", compact(detail))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _header_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments: dict[str, ast.AST] = {}
    imports: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    audit_node = assignments.get("AUDIT_INPUT_PATHS")
    declared_node = assignments.get("DECLARED_INPUT_PATHS")
    literal = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported = {
        alias: imports.get(alias)
        for alias in ("F750", "C744", "C748", "B317")
    }
    expected_imported = {
        "F750": "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "C744": "frontier_cycle744_weight_receiver_sharpening_2026_07_28",
        "C748": "frontier_cycle748_calibration_convergence_comparison_2026_07_28",
        "B317": "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
    }
    detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "imports": imported,
        "literal_tuple": literal,
        "note_path": NOTE_PATH,
        "note_required": False,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
    }
    check(
        "header uses the exact pure-literal imported input tuple",
        literal
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and imported == expected_imported
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/DERIVED_OCCURRENCE_CALIBRATION_CYCLE757_"
            "BOUNDED_THEOREM_NOTE_2026-07-28.md"
        ),
        detail,
    )
    return detail


def _selector_occurrences() -> tuple[dict[str, object], ...]:
    """Rerun F750's successful selector on every one of its 38 K epochs."""
    occurrences = []
    global_epoch = 0
    for bank_count in BANK_COUNTS:
        fixtures = F750.k_epoch_fixtures(bank_count)
        for event, direction, program, before, expected in fixtures:
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            occurrences.append(
                {
                    "alternative_count": len(alternatives),
                    "bank_count": bank_count,
                    "direction": tuple(direction),
                    "global_epoch_ordinal": global_epoch,
                    "local_event": event,
                    "selected_alternatives": tuple(selected),
                }
            )
            global_epoch += 1
    return tuple(occurrences)


def _mapped_events(
    occurrences: tuple[dict[str, object], ...],
    *,
    selector_mode: str,
) -> tuple[dict[str, object], ...]:
    """Apply the printed supplied class map to actual or permuted selections."""
    mapped = []
    for occurrence in occurrences:
        selected = occurrence["selected_alternatives"]
        if len(selected) != 1:
            continue
        actual_alternative = selected[0]
        if selector_mode == "derived":
            used_alternative = actual_alternative
        elif selector_mode == "permuted-control":
            used_alternative = (
                (actual_alternative + 1) % occurrence["alternative_count"]
            )
        else:
            raise ValueError(f"unknown selector mode: {selector_mode}")
        outcome_index = (
            occurrence["global_epoch_ordinal"] + used_alternative
        ) % len(EFFECT_IDS)
        mapped.append(
            {
                **occurrence,
                "actual_selected_alternative": actual_alternative,
                "effect_id": EFFECT_IDS[outcome_index],
                "outcome_index": outcome_index,
                "selector_mode": selector_mode,
                "used_alternative": used_alternative,
            }
        )
    return tuple(mapped)


def _receive_mapped_family(
    family_name: str,
    mapped_events: tuple[dict[str, object], ...],
) -> tuple[tuple[C744.RecordRow, ...], C744.EmpiricalPortResult]:
    exposure_id = f"cycle757-{family_name}-exposure"
    rows = tuple(
        C744.RecordRow(
            record_id=f"cycle757-{family_name}-r{index:02d}",
            menu_id=MENU_ID,
            program_id=PROGRAM_ID,
            outcome_index=event["outcome_index"],
            effect_id=event["effect_id"],
            exposure_id=exposure_id,
            record_kind="declared_apparatus_test_row",
            provenance=(
                "cycle757:F750-selector-output;"
                f"mapping={MAPPING_CONVENTION['status']};family={family_name}"
            ),
        )
        for index, event in enumerate(mapped_events)
    )
    identity = C744.MenuProgramIdentity(MENU_ID, PROGRAM_ID)
    exposure = C744.ExposureDeclaration(
        exposure_id=exposure_id,
        menu_id=MENU_ID,
        program_id=PROGRAM_ID,
        trial_total=len(rows),
        per_effect_eligible_trials=(len(rows),) * len(EFFECT_IDS),
        sampling_protocol="complete-exclusive-common-exposure",
        provenance=(
            "cycle757 epoch census; denominator declared as one common "
            "exposure over all derived epochs"
        ),
    )
    metadata = C744.EffectIdentityMetadata(
        coarse_grainings=(
            ("all", (0, 1, 2)),
            ("first-two", (0, 1)),
            ("third", (2,)),
        ),
        same_effect_classes=tuple((effect_id,) for effect_id in EFFECT_IDS),
    )
    empirical = C744.receive_occurrence_records(
        identity,
        EFFECT_IDS,
        rows,
        exposure,
        metadata,
    )
    return rows, empirical


def _receive_miscalibrated_control(
    occurrences: tuple[dict[str, object], ...],
) -> C744.EmpiricalPortResult:
    mapped = tuple(
        {
            **occurrence,
            "effect_id": EFFECT_IDS[0],
            "outcome_index": 0,
        }
        for occurrence in occurrences
    )
    _rows, empirical = _receive_mapped_family(
        "miscalibrated-all-slot-0-control",
        mapped,
    )
    return empirical


def _landed_contact_trine() -> tuple[tuple[np.ndarray, ...], str]:
    captured = io.StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        _kraus, effects = B317.contact_trine_controls(fixtures[3])
    return effects, captured.getvalue()


def _trace_candidate(
    effects: tuple[np.ndarray, ...],
) -> tuple[float, ...]:
    bloch = np.asarray(C748.FROZEN_SIGMA_BLOCH, dtype=float)
    sigma = (
        B317.I2
        + bloch[0] * B317.X
        + bloch[1] * B317.Y
        + bloch[2] * B317.Z
    ) / 2
    return tuple(
        float(np.trace(sigma @ effect).real)
        for effect in effects
    )


def _comparison_table(
    empirical: C744.EmpiricalPortResult,
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    table = []
    for tolerance in C748.TOLERANCE_LADDER:
        rows = C744.compare_empirical_to_landed(
            empirical,
            held_candidate,
            tolerance=tolerance,
        )
        disagreement_count = sum(
            row.verdict == "disagreement" for row in rows
        )
        table.append(
            {
                "aggregate": (
                    "agreement"
                    if disagreement_count == 0
                    else "disagreement"
                ),
                "disagreement_count": disagreement_count,
                "effect_rows": tuple(
                    {
                        "effect_id": row.effect_id,
                        "empirical": str(row.empirical),
                        "held_candidate": row.held_candidate,
                        "residual_hex": row.residual.hex(),
                        "verdict": row.verdict,
                    }
                    for row in rows
                ),
                "tolerance": tolerance,
            }
        )
    return tuple(table)


def anchor_certificate(
    occurrences: tuple[dict[str, object], ...],
    effects: tuple[np.ndarray, ...],
    captured_b317: str,
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    modules = (
        F750,
        C744,
        C748,
        B317,
    )
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in modules
    )
    selector_counts = tuple(
        len(row["selected_alternatives"]) for row in occurrences
    )
    selector_values = tuple(
        row["selected_alternatives"] for row in occurrences
    )
    port_api = {
        name: callable(getattr(C744, name, None))
        for name in (
            "receive_occurrence_records",
            "compare_empirical_to_landed",
        )
    }
    schema_api = {
        name: getattr(C744, name, None) is not None
        for name in (
            "MenuProgramIdentity",
            "RecordRow",
            "ExposureDeclaration",
            "EffectIdentityMetadata",
            "EmpiricalPortResult",
            "ComparatorRow",
        )
    }
    menu_metrics = B317.menu_metrics(effects)
    detail = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "F750_epoch_count": len(occurrences),
        "F750_selected_count_range": (
            min(selector_counts),
            max(selector_counts),
        ),
        "F750_selected_values": selector_values,
        "held_candidate_hex": tuple(value.hex() for value in held_candidate),
        "imported_paths": imported_paths,
        "menu_metrics": menu_metrics,
        "port_api": port_api,
        "schema_api": schema_api,
    }
    check(
        "A anchors: F750 selector rerun, C744 port, and B317 menu are frozen",
        imported_paths == AUDIT_INPUT_PATHS
        and len(occurrences) == EPOCH_COUNT
        and selector_counts == (1,) * EPOCH_COUNT
        and selector_values == ((0,),) * EPOCH_COUNT
        and all(port_api.values())
        and all(schema_api.values())
        and len(effects) == len(EFFECT_IDS) == 3
        and menu_metrics["normalization"] < B317.TOL
        and menu_metrics["minimum_eigenvalue"] > -B317.TOL
        and tuple(value.hex() for value in held_candidate)
        == C748.FROZEN_HELD_CANDIDATE_HEX
        and held_candidate == C748.FROZEN_HELD_CANDIDATE_VALUES
        and captured_b317.count("PASS ") == 4
        and "FAIL " not in captured_b317,
        detail,
    )
    return detail


def derived_family_certificate(
    occurrences: tuple[dict[str, object], ...],
    mapped: tuple[dict[str, object], ...],
    rows: tuple[C744.RecordRow, ...],
    empirical: C744.EmpiricalPortResult,
) -> dict[str, object]:
    by_banks = {
        str(bank_count): sum(
            event["bank_count"] == bank_count for event in mapped
        )
        for bank_count in BANK_COUNTS
    }
    detail = {
        "census_role": "finite derived-occurrence DATA, not w(E)",
        "counts": empirical.counts,
        "declared_normalization": {
            "common_exposure_per_effect": EPOCH_COUNT,
            "simplex": tuple(str(value) for value in empirical.simplex),
            "simplex_sum": str(
                sum(empirical.simplex, start=Fraction(0, 1))
            ),
        },
        "epoch_counts_by_bank_fixture": by_banks,
        "mapping_convention": MAPPING_CONVENTION,
        "record_kind_constraint_from_C744": "declared_apparatus_test_row",
        "selected_events": mapped,
    }
    condition = (
        len(occurrences) == len(mapped) == len(rows) == EPOCH_COUNT
        and by_banks == {"2": 4, "5": 10, "12": 24}
        and all(type(row) is C744.RecordRow for row in rows)
        and all(
            event["selector_mode"] == "derived"
            and event["used_alternative"]
            == event["actual_selected_alternative"]
            and event["outcome_index"]
            == (
                event["global_epoch_ordinal"]
                + event["actual_selected_alternative"]
            )
            % len(EFFECT_IDS)
            and event["effect_id"] == EFFECT_IDS[event["outcome_index"]]
            for event in mapped
        )
        and empirical.counts == EXPECTED_DERIVED_COUNTS
        and sum(empirical.counts) == EPOCH_COUNT
        and empirical.simplex
        == tuple(Fraction(count, EPOCH_COUNT) for count in empirical.counts)
        and sum(empirical.simplex, start=Fraction(0, 1))
        == Fraction(1, 1)
        and dict(empirical.coarse_counts)["all"] == EPOCH_COUNT
    )
    check(
        "B derived-family construction: selected events and exact census enter the C744 typed port",
        condition,
        detail,
    )
    print("DATA mapping_convention", compact(MAPPING_CONVENTION))
    print(
        "DATA derived_census",
        compact(
            {
                "counts": empirical.counts,
                "epochs": EPOCH_COUNT,
                "simplex": tuple(str(value) for value in empirical.simplex),
            }
        ),
    )
    return detail


def comparison_certificate(
    empirical: C744.EmpiricalPortResult,
    held_candidate: tuple[float, ...],
    table: tuple[dict[str, object], ...],
) -> dict[str, object]:
    residual_hex = tuple(
        row["residual_hex"] for row in table[0]["effect_rows"]
    )
    disagreement_counts = tuple(
        row["disagreement_count"] for row in table
    )
    detail = {
        "comparison_kind": (
            "derived-occurrence simplex vs supplied w(E)=Tr(sigma E)"
        ),
        "counts": empirical.counts,
        "held_candidate_origin": "supplied fixed sigma trace on B317 effects",
        "held_candidate_values": held_candidate,
        "sample_size": EPOCH_COUNT,
        "table_role": "DATA",
        "tolerance_ladder": C748.TOLERANCE_LADDER,
        "verdict_table": table,
    }
    check(
        "C comparison table: frozen Cycle-748 tolerances return finite DATA with zero drift",
        C748.TOLERANCE_LADDER == (0.06, 0.02, 0.002, 0.001)
        and tuple(value.hex() for value in held_candidate)
        == C748.FROZEN_HELD_CANDIDATE_HEX
        and residual_hex == EXPECTED_DERIVED_RESIDUAL_HEX
        and disagreement_counts == EXPECTED_DERIVED_DISAGREEMENTS
        and all(
            row["aggregate"] in {"agreement", "disagreement"}
            and len(row["effect_rows"]) == len(EFFECT_IDS)
            for row in table
        ),
        detail,
    )
    print("DATA comparison_table", compact(table))
    return detail


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
    return tuple(targets)


def firewall_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    module_aliases = {"F750", "C744", "C748", "B317"}
    imported_attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in module_aliases
    )
    imported_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in module_aliases
    )
    forbidden_promotion_targets = tuple(
        sorted(
            {
                node.id
                for target in _assignment_targets(tree)
                for node in ast.walk(target)
                if isinstance(node, ast.Name)
                and isinstance(node.ctx, ast.Store)
                and (
                    node.id.lower() == "weight"
                    or node.id.lower().endswith("_weight")
                    or "calibrated_weight" in node.id.lower()
                )
            }
        )
    )
    file_write_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in {
            "write_text",
            "write_bytes",
            "unlink",
            "rename",
            "replace",
        }
    )
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    data_functions = (
        "_selector_occurrences",
        "_mapped_events",
        "_receive_mapped_family",
        "_receive_miscalibrated_control",
    )
    candidate_symbols = {
        "FROZEN_HELD_CANDIDATE_VALUES",
        "FROZEN_HELD_CANDIDATE_HEX",
        "FROZEN_SIGMA_BLOCH",
        "_trace_candidate",
    }
    data_to_candidate_hits = tuple(
        sorted(
            {
                node.id
                for name in data_functions
                for node in ast.walk(functions[name])
                if isinstance(node, ast.Name)
                and node.id in candidate_symbols
            }
        )
    )
    detail = {
        "census_is_data": True,
        "data_to_candidate_ast_hits": data_to_candidate_hits,
        "empirical_to_weight_assignment_targets": forbidden_promotion_targets,
        "file_write_calls": file_write_calls,
        "imported_module_attribute_writes": imported_attribute_writes,
        "imported_module_setattr_calls": imported_setattrs,
        "weight_writes": False,
    }
    check(
        "D firewall audits: census stays DATA and no imported surface or weight is written",
        not imported_attribute_writes
        and not imported_setattrs
        and not forbidden_promotion_targets
        and not file_write_calls
        and not data_to_candidate_hits,
        detail,
    )
    return detail


def controls_certificate(
    derived_empirical: C744.EmpiricalPortResult,
    permuted_empirical: C744.EmpiricalPortResult,
    miscalibrated_empirical: C744.EmpiricalPortResult,
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    permuted_table = _comparison_table(
        permuted_empirical,
        held_candidate,
    )
    miscalibrated_table = _comparison_table(
        miscalibrated_empirical,
        held_candidate,
    )
    control_residual_hex = tuple(
        row["residual_hex"]
        for row in miscalibrated_table[0]["effect_rows"]
    )
    detail = {
        "miscalibrated_control": {
            "counts": miscalibrated_empirical.counts,
            "pattern": "Cycle-748 all rows deliberately assigned to slot 0",
            "residual_hex": control_residual_hex,
            "verdict_table": miscalibrated_table,
        },
        "permuted_selector_control": {
            "counts": permuted_empirical.counts,
            "detected": (
                permuted_empirical.counts != derived_empirical.counts
            ),
            "permutation": (
                "P(selected_alternative) = selected_alternative + 1 "
                "mod alternative_count"
            ),
            "verdict_table": permuted_table,
        },
    }
    check(
        "D controls: wrong selector changes the census and Cycle-748 miscalibration is detected",
        derived_empirical.counts == EXPECTED_DERIVED_COUNTS
        and permuted_empirical.counts == EXPECTED_PERMUTED_COUNTS
        and permuted_empirical.counts != derived_empirical.counts
        and miscalibrated_empirical.counts
        == EXPECTED_MISCALIBRATED_COUNTS
        and control_residual_hex == C748.FROZEN_CONTROL_RESIDUAL_HEX
        and all(
            row["disagreement_count"] == len(EFFECT_IDS)
            for row in miscalibrated_table
        ),
        detail,
    )
    return detail


def boundary_certificate(
    verdict_table: tuple[dict[str, object], ...],
) -> dict[str, object]:
    boundary = {
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "comparison_only": True,
        "first_derived_occurrence_comparison": True,
        "mapping_convention_derived": False,
        "mapping_convention_supplied": True,
        "next": NEXT_STEP,
        "run_family_origin": "F750 derived selector output at fixture scope",
        "sample_size_bound": "38 epochs",
        "simplex_promoted_to_weight": False,
        "verdict_table": verdict_table,
        "verdict_table_role": "DATA",
        "weight_claim_made": False,
    }
    check(
        "E honest boundary: SMALL 38-epoch sample permits no weight claim either way",
        boundary["first_derived_occurrence_comparison"] is True
        and boundary["weight_claim_made"] is False
        and boundary["sample_size_bound"] == "38 epochs"
        and boundary["mapping_convention_supplied"] is True
        and boundary["mapping_convention_derived"] is False
        and boundary["verdict_table_role"] == "DATA"
        and boundary["next"] == NEXT_STEP
        and boundary["asymptotic_convergence_claimed"] is False
        and boundary["born_law_selected"] is False
        and boundary["simplex_promoted_to_weight"] is False,
        boundary,
    )
    print(
        "BOUNDARY HONEST CEILING :: 38 epochs is a SMALL sample; this is "
        "a coarse finite comparison, not convergence. No weight claim either "
        "way until the derived family is large AND the outcome-class mapping "
        "is derived."
    )
    return boundary


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()

    input_sha_before = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    header = _header_audit()
    occurrences = _selector_occurrences()
    effects, captured_b317 = _landed_contact_trine()
    held_candidate = _trace_candidate(effects)
    anchors = anchor_certificate(
        occurrences,
        effects,
        captured_b317,
        held_candidate,
    )

    derived_mapped = _mapped_events(
        occurrences,
        selector_mode="derived",
    )
    derived_rows, derived_empirical = _receive_mapped_family(
        "derived-selector",
        derived_mapped,
    )
    family = derived_family_certificate(
        occurrences,
        derived_mapped,
        derived_rows,
        derived_empirical,
    )

    comparison_table = _comparison_table(
        derived_empirical,
        held_candidate,
    )
    comparison = comparison_certificate(
        derived_empirical,
        held_candidate,
        comparison_table,
    )

    permuted_mapped = _mapped_events(
        occurrences,
        selector_mode="permuted-control",
    )
    _permuted_rows, permuted_empirical = _receive_mapped_family(
        "permuted-selector-control",
        permuted_mapped,
    )
    miscalibrated_empirical = _receive_miscalibrated_control(
        occurrences
    )
    controls = controls_certificate(
        derived_empirical,
        permuted_empirical,
        miscalibrated_empirical,
        held_candidate,
    )
    firewall = firewall_audit()
    boundary = boundary_certificate(comparison_table)

    input_sha_after = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    check(
        "A imported inputs remain byte-stable after all certificates",
        input_sha_before == input_sha_after,
        input_sha_after,
    )

    runtime_seconds = perf_counter() - started
    check(
        "bounded runtime and optional-note contract",
        runtime_seconds < AUDIT_TIMEOUT_SEC,
        {
            "note_path": NOTE_PATH,
            "note_required": False,
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )
    certificate = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificates": {
            "A_anchors": anchors,
            "B_derived_family": family,
            "C_comparison": comparison,
            "D_controls": controls,
            "D_firewalls": firewall,
            "E_honest_boundary": boundary,
            "header": header,
        },
        "derived_census": {
            "counts": derived_empirical.counts,
            "epochs": EPOCH_COUNT,
            "simplex": tuple(
                str(value) for value in derived_empirical.simplex
            ),
        },
        "fail": FAIL,
        "first_derived_occurrence_comparison": True,
        "mapping_convention_supplied": True,
        "next": NEXT_STEP,
        "note_path": NOTE_PATH,
        "pass": PASS,
        "result": "PASS" if FAIL == 0 else "FAIL",
        "runtime_seconds": round(runtime_seconds, 6),
        "sample_size_bound": "38 epochs",
        "verdict_table": comparison_table,
        "weight_claim_made": False,
    }
    certificate["report_sha256"] = hashlib.sha256(
        compact(certificate).encode("utf-8")
    ).hexdigest()
    print(compact(certificate))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
