#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-757 finite calibration data."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/DERIVED_OCCURRENCE_CALIBRATION_CYCLE757_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)

import ast
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
import math
from pathlib import Path
import sys
from time import perf_counter

import numpy as np

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
from frontier_cycle744_weight_receiver_sharpening_2026_07_28 import (
    EffectIdentityMetadata,
    ExposureDeclaration,
    MenuProgramIdentity,
    RecordRow,
    receive_occurrence_records,
)
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_RELATIVE_PATH = (
    "scripts/frontier_cycle757_derived_occurrence_calibration_2026_07_28.py"
)
PRIMARY_MODULE = (
    "frontier_cycle757_derived_occurrence_calibration_2026_07_28"
)
IMPORT_BLOCKLIST = (PRIMARY_MODULE,)
CEILING_LANGUAGE = (
    "38 epochs is a SMALL sample; this is a coarse finite comparison, "
    "not convergence. No weight claim either way until the derived family "
    "is large AND the outcome-class mapping is derived."
)
EXPECTED_TABLE = (
    (0.06, ("A", "D", "D")),
    (0.02, ("A", "D", "D")),
    (0.002, ("D", "D", "D")),
    (0.001, ("D", "D", "D")),
)

PASS = 0
FAIL = 0


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


def _assignments(tree: ast.Module) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(
            node.target, ast.Name
        ):
            found[node.target.id] = node.value
    return found


def _literal(assignments: dict[str, ast.AST], name: str) -> object:
    if name not in assignments:
        raise ValueError(f"missing primary assignment: {name}")
    return ast.literal_eval(assignments[name])


def _tolerance_literal(tree: ast.Module) -> tuple[float, ...]:
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Attribute)
            and node.left.attr == "TOLERANCE_LADDER"
            and len(node.comparators) == 1
            and isinstance(node.comparators[0], ast.Tuple)
        ):
            return tuple(ast.literal_eval(node.comparators[0]))
    raise ValueError("primary tolerance-ladder literal was not found")


def _boundary_literals(tree: ast.Module) -> dict[str, object]:
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "boundary_certificate"
    )
    boundary_node = next(
        node.value
        for node in function.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    )
    values: dict[str, object] = {}
    for key_node, value_node in zip(
        boundary_node.keys, boundary_node.values, strict=True
    ):
        key = ast.literal_eval(key_node)
        if key in {
            "weight_claim_made",
            "sample_size_bound",
            "mapping_convention_supplied",
        }:
            values[key] = ast.literal_eval(value_node)
    return values


def _held_bloch_literal() -> tuple[float, float, float]:
    source = (
        ROOT / AUDIT_INPUT_PATHS[2]
    ).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[2])
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "mixed_projective_forcing_basis_controls"
    )
    candidates = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "bloch"
            and isinstance(node.value, ast.Call)
            and node.value.args
        ):
            candidates.append(tuple(ast.literal_eval(node.value.args[0])))
    if len(candidates) != 1:
        raise ValueError("the single held B317 Bloch literal was not found")
    return candidates[0]


def extraction() -> dict[str, object]:
    """Extract primary data without importing or executing the primary."""
    primary_source = (
        ROOT / PRIMARY_RELATIVE_PATH
    ).read_text(encoding="utf-8")
    primary_tree = ast.parse(
        primary_source,
        filename=PRIMARY_RELATIVE_PATH,
    )
    primary_assignments = _assignments(primary_tree)

    self_source = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=str(Path(__file__)))
    self_assignments = _assignments(self_tree)
    self_audit_node = self_assignments["AUDIT_INPUT_PATHS"]
    primary_audit_node = primary_assignments["AUDIT_INPUT_PATHS"]

    epoch_count = int(_literal(primary_assignments, "EPOCH_COUNT"))
    bank_counts = tuple(_literal(primary_assignments, "BANK_COUNTS"))
    counts = tuple(
        _literal(primary_assignments, "EXPECTED_DERIVED_COUNTS")
    )
    effect_ids = tuple(_literal(primary_assignments, "EFFECT_IDS"))
    mapping = dict(_literal(primary_assignments, "MAPPING_CONVENTION"))
    residual_hex = tuple(
        _literal(primary_assignments, "EXPECTED_DERIVED_RESIDUAL_HEX")
    )
    disagreement_counts = tuple(
        _literal(primary_assignments, "EXPECTED_DERIVED_DISAGREEMENTS")
    )
    tolerances = _tolerance_literal(primary_tree)
    boundary_raw = _boundary_literals(primary_tree)

    simplex = tuple(Fraction(count, epoch_count) for count in counts)
    residuals = tuple(float.fromhex(value) for value in residual_hex)
    comparator_values = tuple(
        float(empirical) - residual
        for empirical, residual in zip(simplex, residuals, strict=True)
    )
    verdict_table = tuple(
        (
            tolerance,
            tuple(
                "A" if abs(residual) <= tolerance else "D"
                for residual in residuals
            ),
        )
        for tolerance in tolerances
    )
    primary_audit = tuple(ast.literal_eval(primary_audit_node))
    self_audit = tuple(ast.literal_eval(self_audit_node))
    sample_size = int(str(boundary_raw["sample_size_bound"]).split()[0])
    boundary = {
        "weight_claim_made": boundary_raw["weight_claim_made"],
        "sample_size_bound": sample_size,
        "mapping_convention_supplied": boundary_raw[
            "mapping_convention_supplied"
        ],
    }
    bloch = _held_bloch_literal()

    condition = (
        isinstance(primary_audit_node, ast.Tuple)
        and isinstance(self_audit_node, ast.Tuple)
        and primary_audit
        == (
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
            "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
            "scripts/frontier_cycle748_calibration_convergence_comparison_2026_07_28.py",
            "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
        )
        and self_audit == AUDIT_INPUT_PATHS
        and epoch_count == 38
        and bank_counts == (2, 5, 12)
        and counts == (13, 13, 12)
        and simplex
        == (Fraction(13, 38), Fraction(13, 38), Fraction(6, 19))
        and len(comparator_values) == 3
        and all(math.isfinite(value) for value in comparator_values)
        and tolerances == (0.06, 0.02, 0.002, 0.001)
        and disagreement_counts == (2, 2, 3, 3)
        and verdict_table == EXPECTED_TABLE
        and mapping
        == {
            "formula": (
                "outcome_index = (global_epoch_ordinal + "
                "selected_alternative) mod 3"
            ),
            "ordered_effect_rule": (
                "effect_id = EFFECT_IDS[outcome_index]"
            ),
            "status": "SUPPLY",
            "why_not_derived": (
                "F750 derives the selected alternative at fixture scope "
                "but does not derive an identification with a Cycle-317 "
                "ternary outcome class."
            ),
        }
        and boundary
        == {
            "weight_claim_made": False,
            "sample_size_bound": 38,
            "mapping_convention_supplied": True,
        }
        and bloch == (0.21, -0.32, 0.41)
    )
    detail = {
        "epochs": epoch_count,
        "counts": counts,
        "simplex": tuple(str(value) for value in simplex),
        "comparator_hex": tuple(value.hex() for value in comparator_values),
        "verdict_table": verdict_table,
        "mapping_status": mapping["status"],
        "boundary": boundary,
        "audit_tuple_literal_eval": True,
    }
    check("extraction", condition, detail)
    return {
        **detail,
        "bank_counts": bank_counts,
        "effect_ids": effect_ids,
        "mapping": mapping,
        "residual_hex": residual_hex,
        "disagreement_counts": disagreement_counts,
        "tolerances": tolerances,
        "comparator_values": comparator_values,
        "simplex_exact": simplex,
        "bloch": bloch,
        "primary_source": primary_source,
        "primary_tree": primary_tree,
    }


def _port_receive(
    family: str,
    outcome_indices: tuple[int, ...],
    effect_ids: tuple[str, ...],
):
    menu_id = "cycle757-independent-contact-trine"
    program_id = "cycle757-independent-f750-selector"
    exposure_id = f"cycle757-independent-{family}-exposure"
    records = tuple(
        RecordRow(
            record_id=f"cycle757-independent-{family}-r{index:02d}",
            menu_id=menu_id,
            program_id=program_id,
            outcome_index=outcome_index,
            effect_id=effect_ids[outcome_index],
            exposure_id=exposure_id,
            record_kind="declared_apparatus_test_row",
            provenance=(
                "cycle757-independent:F750-selector;"
                f"mapping=SUPPLY;family={family}"
            ),
        )
        for index, outcome_index in enumerate(outcome_indices)
    )
    total = len(records)
    identity = MenuProgramIdentity(menu_id, program_id)
    exposure = ExposureDeclaration(
        exposure_id=exposure_id,
        menu_id=menu_id,
        program_id=program_id,
        trial_total=total,
        per_effect_eligible_trials=(total,) * len(effect_ids),
        sampling_protocol="complete-exclusive-common-exposure",
        provenance="cycle757 independent common exposure",
    )
    metadata = EffectIdentityMetadata(
        coarse_grainings=(("all", tuple(range(len(effect_ids)))),),
        same_effect_classes=tuple(
            (effect_id,) for effect_id in effect_ids
        ),
    )
    return receive_occurrence_records(
        identity,
        effect_ids,
        records,
        exposure,
        metadata,
    )


def census_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Rerun F750's selector and independently remap all fixture epochs."""
    occurrences = []
    outcome_indices = []
    ordinal = 0
    bank_fixture_counts: Counter[int] = Counter()
    for bank_count in extracted["bank_counts"]:
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
            if len(selected) == 1:
                outcome_index = (ordinal + selected[0]) % 3
                outcome_indices.append(outcome_index)
            else:
                outcome_index = None
            occurrences.append(
                {
                    "ordinal": ordinal,
                    "bank_count": bank_count,
                    "event": event,
                    "direction": tuple(direction),
                    "alternative_count": len(alternatives),
                    "selected": tuple(selected),
                    "outcome_index": outcome_index,
                }
            )
            bank_fixture_counts[bank_count] += 1
            ordinal += 1

    own_counts = tuple(
        outcome_indices.count(index)
        for index in range(len(extracted["effect_ids"]))
    )
    own_simplex = tuple(
        Fraction(count, len(outcome_indices)) for count in own_counts
    )
    port = _port_receive(
        "derived",
        tuple(outcome_indices),
        extracted["effect_ids"],
    )
    expected_path = (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
    condition = (
        Path(F750.__file__).resolve() == expected_path
        and extracted["mapping"]["status"] == "SUPPLY"
        and extracted["mapping"]["formula"]
        == (
            "outcome_index = (global_epoch_ordinal + "
            "selected_alternative) mod 3"
        )
        and len(occurrences) == len(outcome_indices) == 38
        and dict(bank_fixture_counts) == {2: 4, 5: 10, 12: 24}
        and all(row["selected"] == (0,) for row in occurrences)
        and own_counts == extracted["counts"] == (13, 13, 12)
        and own_simplex == extracted["simplex_exact"]
        and sum(own_simplex, start=Fraction(0, 1)) == Fraction(1, 1)
        and port.counts == own_counts
        and port.simplex == own_simplex
        and dict(port.coarse_counts)["all"] == 38
    )
    detail = {
        "epochs": len(occurrences),
        "fixture_counts": dict(bank_fixture_counts),
        "counts": own_counts,
        "simplex": tuple(str(value) for value in own_simplex),
        "selector_singletons": sum(
            len(row["selected"]) == 1 for row in occurrences
        ),
        "port_recount_matches": (
            port.counts == own_counts and port.simplex == own_simplex
        ),
    }
    check("census_recount", condition, detail)
    return {
        **detail,
        "counts_exact": own_counts,
        "simplex_exact": own_simplex,
        "occurrences": tuple(occurrences),
    }


def comparison_recount(
    extracted: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    """Use own Fraction normalization and own tolerance comparisons."""
    captured = io.StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        _kraus, effects = B317.contact_trine_controls(fixtures[3])

    bloch = np.asarray(extracted["bloch"], dtype=float)
    sigma = (
        B317.I2
        + bloch[0] * B317.X
        + bloch[1] * B317.Y
        + bloch[2] * B317.Z
    ) / 2
    traced_comparator = tuple(
        float(np.trace(sigma @ effect).real) for effect in effects
    )
    supplied_comparator = tuple(extracted["comparator_values"])
    simplex = tuple(
        Fraction(count, 38) for count in census["counts_exact"]
    )
    residuals = tuple(
        float(empirical) - candidate
        for empirical, candidate in zip(
            simplex, supplied_comparator, strict=True
        )
    )
    table = tuple(
        (
            tolerance,
            tuple(
                "A" if abs(residual) <= tolerance else "D"
                for residual in residuals
            ),
        )
        for tolerance in extracted["tolerances"]
    )
    disagreements = tuple(
        sum(verdict == "D" for verdict in verdicts)
        for _tolerance, verdicts in table
    )
    b317_output = captured.getvalue()
    condition = (
        Path(B317.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[2]).resolve()
        and len(effects) == 3
        and B317.menu_metrics(effects)["normalization"] < B317.TOL
        and np.min(np.linalg.eigvalsh(sigma)) > 0
        and supplied_comparator == traced_comparator
        and simplex
        == (Fraction(13, 38), Fraction(13, 38), Fraction(6, 19))
        and tuple(value.hex() for value in residuals)
        == extracted["residual_hex"]
        and table == EXPECTED_TABLE
        and disagreements == extracted["disagreement_counts"]
        and b317_output.count("PASS ") == 4
        and "FAIL " not in b317_output
    )
    detail = {
        "comparator_hex": tuple(
            value.hex() for value in supplied_comparator
        ),
        "residual_hex": tuple(value.hex() for value in residuals),
        "table": table,
        "disagreement_counts": disagreements,
        "b317_anchor_passes": b317_output.count("PASS "),
    }
    check("comparison_recount", condition, detail)
    return detail


def control_recount(
    extracted: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    """Reverse every alternative order before applying the supplied map."""
    control_indices = []
    permutation_cases = 0
    for row in census["occurrences"]:
        alternatives = tuple(range(row["alternative_count"]))
        if len(row["selected"]) != 1:
            continue
        selected = row["selected"][0]
        permutation = tuple(reversed(alternatives))
        if tuple(sorted(permutation)) == alternatives:
            permutation_cases += 1
        permuted_selected = row["alternative_count"] - 1 - selected
        control_indices.append(
            (row["ordinal"] + permuted_selected) % 3
        )
    control_counts = tuple(
        control_indices.count(index)
        for index in range(len(extracted["effect_ids"]))
    )
    detected = control_counts != census["counts_exact"]
    condition = (
        permutation_cases == len(census["occurrences"]) == 38
        and control_counts == (12, 13, 13)
        and detected
    )
    detail = {
        "permutation": (
            "selected_alternative -> "
            "alternative_count - 1 - selected_alternative"
        ),
        "permutation_cases": permutation_cases,
        "derived_counts": census["counts_exact"],
        "control_counts": control_counts,
        "detected": detected,
    }
    check("control_recount", condition, detail)
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


def _tree_firewall(
    tree: ast.Module,
    imported_roots: set[str],
) -> dict[str, object]:
    attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in imported_roots
    )
    imported_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in imported_roots
    )
    promotion_targets = tuple(
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
    file_writes = tuple(
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
    return {
        "attribute_writes": attribute_writes,
        "imported_setattrs": imported_setattrs,
        "promotion_targets": promotion_targets,
        "file_writes": file_writes,
    }


def _false_claim_keys(tree: ast.Module) -> dict[str, tuple[object, ...]]:
    names = {
        "asymptotic_convergence_claimed",
        "born_law_selected",
        "simplex_promoted_to_weight",
        "weight_claim_made",
    }
    located: dict[str, list[object]] = {name: [] for name in names}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(
            node.keys, node.values, strict=True
        ):
            try:
                key = ast.literal_eval(key_node)
                value = ast.literal_eval(value_node)
            except (ValueError, TypeError):
                continue
            if key in located:
                located[key].append(value)
    return {
        name: tuple(values)
        for name, values in located.items()
        if values
    }


def _only_false_claims(value: object) -> bool:
    if type(value) is bool:
        return value is False
    if isinstance(value, (tuple, list)):
        return bool(value) and all(
            _only_false_claims(item) for item in value
        )
    return False


def firewall_recount(extracted: dict[str, object]) -> dict[str, object]:
    """AST-audit primary and checker in both directions, with no writes."""
    primary_tree = extracted["primary_tree"]
    self_source = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=str(Path(__file__)))
    primary_scan = _tree_firewall(
        primary_tree, {"F750", "C744", "C748", "B317"}
    )
    self_scan = _tree_firewall(self_tree, {"F750", "B317"})

    self_imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            self_imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            self_imports.add(node.module)

    functions = {
        node.name: node
        for node in self_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    selector_forbidden_reads = tuple(
        sorted(
            {
                node.id
                for name in ("census_recount", "control_recount")
                for node in ast.walk(functions[name])
                if isinstance(node, ast.Name)
                and node.id
                in {
                    "B317",
                    "sigma",
                    "supplied_comparator",
                    "traced_comparator",
                }
            }
        )
    )
    comparison_selector_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(functions["comparison_recount"])
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in {
            "F750.k_epoch_fixtures",
            "F750.enforcement_lineage_selector",
        }
    )
    primary_claims = _false_claim_keys(primary_tree)
    self_claims = _false_claim_keys(self_tree)
    string_constants = tuple(
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    )
    self_string_constants = tuple(
        node.value
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    )
    ceiling_verbatim = any(
        CEILING_LANGUAGE in value for value in string_constants
    )
    self_ceiling_verbatim = any(
        value == CEILING_LANGUAGE for value in self_string_constants
    )
    imported_primary = any(
        name in sys.modules for name in IMPORT_BLOCKLIST
    )
    scans_clean = all(
        not scan[key]
        for scan in (primary_scan, self_scan)
        for key in (
            "attribute_writes",
            "imported_setattrs",
            "promotion_targets",
            "file_writes",
        )
    )
    required_primary_claims = {
        "asymptotic_convergence_claimed",
        "born_law_selected",
        "simplex_promoted_to_weight",
        "weight_claim_made",
    }
    required_self_claims = {
        "asymptotic_convergence_claimed",
        "weight_claim_made",
    }
    claims_clean = (
        required_primary_claims <= set(primary_claims)
        and required_self_claims <= set(self_claims)
        and all(
            _only_false_claims(value)
            for values in primary_claims.values()
            for value in values
        )
        and all(
            _only_false_claims(value)
            for values in self_claims.values()
            for value in values
        )
    )
    condition = (
        scans_clean
        and not selector_forbidden_reads
        and not comparison_selector_calls
        and PRIMARY_MODULE not in self_imports
        and not imported_primary
        and ceiling_verbatim
        and self_ceiling_verbatim
        and claims_clean
    )
    detail = {
        "ast_directions": (PRIMARY_RELATIVE_PATH, str(Path(__file__).name)),
        "primary_scan": primary_scan,
        "checker_scan": self_scan,
        "selector_to_comparator_reads": selector_forbidden_reads,
        "comparator_to_selector_calls": comparison_selector_calls,
        "primary_import_blocked": not imported_primary,
        "ceiling_verbatim": (
            ceiling_verbatim and self_ceiling_verbatim
        ),
        "claim_flags": {
            "primary": primary_claims,
            "checker": self_claims,
        },
        "weight_writes": False,
    }
    check("firewall_recount", condition, detail)
    print("BOUNDARY HONEST CEILING ::", CEILING_LANGUAGE)
    return detail


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    watched_paths = (PRIMARY_RELATIVE_PATH,) + AUDIT_INPUT_PATHS
    before = {
        path: _sha256(ROOT / path) for path in watched_paths
    }

    extracted = extraction()
    census = census_recount(extracted)
    comparison = comparison_recount(extracted, census)
    control = control_recount(extracted, census)
    firewall = firewall_recount(extracted)

    after = {
        path: _sha256(ROOT / path) for path in watched_paths
    }
    check(
        "read_only_inputs",
        before == after,
        {"stable_files": len(after)},
    )
    runtime = perf_counter() - started
    check(
        "bounded_runtime",
        runtime < AUDIT_TIMEOUT_SEC,
        {
            "runtime_seconds": round(runtime, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
            "note_path": NOTE_PATH,
            "note_required": False,
        },
    )

    report = {
        "result": "PASS" if FAIL == 0 else "FAIL",
        "pass": PASS,
        "fail": FAIL,
        "derived_census": {
            "epochs": census["epochs"],
            "counts": census["counts_exact"],
            "simplex": tuple(
                str(value) for value in census["simplex_exact"]
            ),
        },
        "verdict_table": comparison["table"],
        "control": {
            "counts": control["control_counts"],
            "detected": control["detected"],
            "permutation": control["permutation"],
        },
        "boundary": {
            "weight_claim_made": False,
            "sample_size_bound": 38,
            "mapping_convention_supplied": True,
            "asymptotic_convergence_claimed": False,
        },
        "firewall": {
            "primary_import_blocked": firewall[
                "primary_import_blocked"
            ],
            "weight_writes": firewall["weight_writes"],
            "ceiling_verbatim": firewall["ceiling_verbatim"],
        },
        "runtime_seconds": round(runtime, 6),
    }
    print("CENSUS", compact(report["derived_census"]))
    print("TABLE", compact(report["verdict_table"]))
    print("CONTROL", compact(report["control"]))
    print("RUNTIME_SEC", f"{runtime:.6f}")
    print("CERTIFICATE", compact(report))
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    return 0 if FAIL == 0 else 1


def main() -> int:
    started = perf_counter()
    try:
        return _run()
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(
            "FAIL unexpected_checker_error ::",
            compact(
                {
                    "type": type(exc).__name__,
                    "message": str(exc),
                    "runtime_seconds": round(
                        perf_counter() - started, 6
                    ),
                }
            ),
        )
        print("SUMMARY PASS", PASS, "FAIL", FAIL)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
