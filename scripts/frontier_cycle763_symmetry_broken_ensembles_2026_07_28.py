#!/usr/bin/env python3
"""Cycle 763: the symmetry-broken ensemble experiment (W6 discriminator).

Cycle 760's complete translation families are the unseeded control.  The
experiment below breaks that symmetry with a deterministic window schedule
obtained from Cycle 317's landed ray-split coefficients and ordered effects.
The Cycle 750 selector is run on all 38 fixtures and the complete 137-case
bank/rotation covariance basis; that landed covariance transports the retained
rotations exactly as in Cycle 760.  The finite censuses are compared, as DATA,
with both the held Born trace candidate and the uniform simplex.  The mapping
and seeding conventions remain supplied; no census is promoted to a weight.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle757_derived_occurrence_calibration_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
import io
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle757_derived_occurrence_calibration_2026_07_28 as C757


STDOUT_LIMIT_BYTES = 150 * 1024
BANK_COUNTS = C757.BANK_COUNTS
EFFECT_IDS = C757.EFFECT_IDS
MAPPING_CONVENTION = C757.MAPPING_CONVENTION
MENU_ID = "cycle763-cycle317-contact-trine"
PROGRAM_ID = "cycle763-f750-symmetry-broken-ensemble"
EXPECTED_BASELINE_COUNTS = (845, 878, 855)
EXPECTED_BASELINE_SIZE = 2578
EXPECTED_PRIMITIVE_MULTIPLICITIES = (17, 29, 54)
EXPECTED_STRATUM_COUNTS = (
    (13, 128, 68),
    (97, 1, 232),
    (432, 146, 5),
)
EXPECTED_STRATUM_SIZES = (209, 330, 583)
EXPECTED_POOLED_COUNTS = (542, 275, 305)
EXPECTED_POOLED_SIZE = 1122
EXPECTED_SCRAMBLED_COUNTS = (242, 310, 552)
EXPECTED_SCRAMBLED_SIZE = 1104

SEEDING_CONVENTION = {
    "status": "SUPPLY",
    "coefficient_source": (
        "the exact three source literals passed as splits to B317."
        "split_projector_isometry inside "
        "mixed_projective_forcing_basis_controls"
    ),
    "coefficient_effect_pairing": (
        "ordered ray-split branch j is paired with ordered contact-trine "
        "effect j"
    ),
    "integralization": (
        "convert exact source literals to Fractions, clear their least "
        "common denominator, then divide by the common gcd"
    ),
    "epoch_effect_association": (
        "the unrotated F750 epoch is associated with the contact-trine "
        "effect selected by the supplied Cycle-757 mapping at the unchanged "
        "Cycle-760 full-family ordinal"
    ),
    "seed_window": (
        "for associated effect j and station count n, retain shifts "
        "(j+k) mod n for k in range(min(primitive_coefficient[j],n))"
    ),
    "ordinal_rule": (
        "each retained shift keeps its ordinal in the complete unseeded "
        "Cycle-760 translation family; retained rows are not renumbered"
    ),
    "new_numeric_seed_constants": (),
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest_rows(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


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


def header_and_ast_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments: dict[str, ast.AST] = {}
    imports: dict[str, str] = {}
    functions: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions[node.name] = node

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == len(AUDIT_INPUT_PATHS)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported = {
        alias: imports.get(alias)
        for alias in ("F750", "B317", "C757")
    }
    expected_imported = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "B317":
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
        "C757":
            "frontier_cycle757_derived_occurrence_calibration_2026_07_28",
    }
    module_aliases = set(expected_imported)
    imported_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in module_aliases
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
    random_hits = tuple(
        sorted(
            {
                node.id
                for node in ast.walk(tree)
                if isinstance(node, ast.Name)
                and node.id in {"random", "secrets"}
            }
        )
    )
    seed_function_names = (
        "extract_landed_seed_surface",
        "build_seeded_family",
    )
    forbidden_seed_references = tuple(
        sorted(
            {
                node.id
                for name in seed_function_names
                for node in ast.walk(functions[name])
                if isinstance(node, ast.Name)
                and (
                    node.id.startswith("EXPECTED_")
                    or node.id in {
                        "held_candidate",
                        "uniform_candidate",
                        "three_way_table",
                    }
                )
            }
        )
    )
    detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "file_write_calls": file_writes,
        "forbidden_seed_reference_hits": forbidden_seed_references,
        "imported_module_attribute_writes": imported_writes,
        "imports": imported,
        "literal_tuple": literal_tuple,
        "note_path": NOTE_PATH,
        "randomness_hits": random_hits,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
    }
    check(
        "header exact inputs, imports, timeout, note, and read-only AST",
        literal_tuple
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and imported == expected_imported
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_"
            "BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and not imported_writes
        and not file_writes
        and not random_hits
        and not forbidden_seed_references,
        detail,
    )
    return detail


def load_landed_apparatus() -> tuple[
    tuple[np.ndarray, ...],
    dict[str, object],
    str,
]:
    captured = io.StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        _trine_kraus, trine_effects = B317.contact_trine_controls(
            fixtures[3]
        )
        _forcing_kraus, forcing_data = (
            B317.mixed_projective_forcing_basis_controls(fixtures[3])
        )
    return trine_effects, forcing_data, captured.getvalue()


def extract_landed_seed_surface(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
) -> dict[str, object]:
    """Extract the ray-split literals and derive all seed integers from them."""
    source_path = Path(B317.__file__).resolve()
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(source_path))
    target_function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "mixed_projective_forcing_basis_controls"
    )
    calls = tuple(
        node
        for node in ast.walk(target_function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
        and len(node.args) >= len(EFFECT_IDS)
        and isinstance(node.args[1], ast.Tuple)
        and len(node.args[1].elts) == len(EFFECT_IDS)
    )
    if len(calls) != len(EFFECT_IDS[:1]):
        raise AssertionError(("ray split AST call count", len(calls)))
    split_node = calls[0].args[1]
    coefficient_tokens = tuple(
        ast.get_source_segment(source, element)
        for element in split_node.elts
    )
    if any(token is None for token in coefficient_tokens):
        raise AssertionError("missing exact source segment for B317 split")
    coefficients = tuple(
        Fraction(token) for token in coefficient_tokens
    )
    common_denominator = lcm(
        *(coefficient.denominator for coefficient in coefficients)
    )
    cleared = tuple(
        coefficient.numerator
        * (common_denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    common_divisor = gcd(*cleared)
    primitive_multiplicities = tuple(
        value // common_divisor for value in cleared
    )

    ray_effects = tuple(forcing_data["ray"][:len(EFFECT_IDS)])
    ray_traces = tuple(
        float(np.trace(effect).real) for effect in ray_effects
    )
    overlap_matrix = tuple(
        tuple(
            float(np.trace(left @ right).real)
            for right in trine_effects
        )
        for left in trine_effects
    )
    self_association = tuple(
        max(range(len(row)), key=row.__getitem__)
        for row in overlap_matrix
    )
    return {
        "b317_source_path": str(source_path.relative_to(ROOT)),
        "coefficient_tokens": coefficient_tokens,
        "coefficients": coefficients,
        "coefficient_sum": sum(
            coefficients, start=Fraction(0, 1)
        ),
        "primitive_multiplicities": primitive_multiplicities,
        "ray_effect_traces": ray_traces,
        "ray_trace_matches": tuple(
            abs(float(coefficient) - trace) < B317.TOL
            for coefficient, trace in zip(
                coefficients, ray_traces, strict=True
            )
        ),
        "trine_overlap_matrix": overlap_matrix,
        "trine_self_association": self_association,
    }


def fixture_epochs() -> tuple[dict[str, object], ...]:
    rows = []
    full_family_offset = 0
    fixture_index = 0
    for bank_count in BANK_COUNTS:
        for event, direction, program, before, expected in (
            F750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            rows.append(
                {
                    "alternative_count": len(program),
                    "bank_count": bank_count,
                    "before": before,
                    "direction": tuple(direction),
                    "event": event,
                    "expected": expected,
                    "fixture_index": fixture_index,
                    "full_family_offset": full_family_offset,
                    "program": program,
                    "unrotated_selected": tuple(selected),
                }
            )
            fixture_index += 1
            full_family_offset += len(program)
    return tuple(rows)


def mapped_event(
    fixture: dict[str, object],
    shift: int,
    selected: tuple[int, ...],
    *,
    associated_effect_index: int,
    family_mode: str,
    seed_effect_index: int,
    seed_quota: int,
) -> dict[str, object]:
    actual = selected[0] if len(selected) == 1 else None
    global_epoch_ordinal = fixture["full_family_offset"] + shift
    outcome_index = (
        (global_epoch_ordinal + actual) % len(EFFECT_IDS)
        if actual is not None
        else None
    )
    return {
        "actual_selected_alternative": actual,
        "alternative_count": fixture["alternative_count"],
        "associated_effect_id": EFFECT_IDS[associated_effect_index],
        "associated_effect_index": associated_effect_index,
        "bank_count": fixture["bank_count"],
        "effect_id": (
            EFFECT_IDS[outcome_index]
            if outcome_index is not None
            else None
        ),
        "family_mode": family_mode,
        "fixture_event": fixture["event"],
        "fixture_index": fixture["fixture_index"],
        "global_epoch_ordinal": global_epoch_ordinal,
        "outcome_index": outcome_index,
        "program_shift": shift,
        "seed_effect_id": EFFECT_IDS[seed_effect_index],
        "seed_effect_index": seed_effect_index,
        "seed_quota": seed_quota,
        "selected_alternatives": selected,
    }


def build_unseeded_baseline(
    fixtures: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    rows = []
    for fixture in fixtures:
        station_count = fixture["alternative_count"]
        associated = fixture["full_family_offset"] % len(EFFECT_IDS)
        for shift in range(station_count):
            transported = (
                (station_count - shift) % station_count,
            )
            rows.append(
                mapped_event(
                    fixture,
                    shift,
                    transported,
                    associated_effect_index=associated,
                    family_mode="unseeded-cycle760-control",
                    seed_effect_index=associated,
                    seed_quota=station_count,
                )
            )
    return tuple(rows)


def build_seeded_family(
    fixtures: tuple[dict[str, object], ...],
    primitive_multiplicities: tuple[int, ...],
    effect_permutation: tuple[int, ...],
    *,
    family_mode: str,
) -> tuple[tuple[dict[str, object], ...], dict[str, object]]:
    rows = []
    covered_bank_shifts = set()
    for fixture in fixtures:
        station_count = fixture["alternative_count"]
        associated = fixture["full_family_offset"] % len(EFFECT_IDS)
        seed_effect = effect_permutation[associated]
        quota = min(
            primitive_multiplicities[seed_effect],
            station_count,
        )
        shifts = tuple(
            (seed_effect + local_seed_ordinal) % station_count
            for local_seed_ordinal in range(quota)
        )
        if len(shifts) != len(set(shifts)):
            raise AssertionError(("non-unique seed window", shifts))
        for shift in shifts:
            # F750.cyclic_enforcement_symmetry explicitly evaluates every
            # bank/shift pair in the 137-case landed covariance basis.  The
            # transported singleton below is its exact covariant reference,
            # applied to each fixture as in the Cycle-760 family machinery.
            selected = ((station_count - shift) % station_count,)
            covered_bank_shifts.add(
                (fixture["bank_count"], shift)
            )
            rows.append(
                mapped_event(
                    fixture,
                    shift,
                    selected,
                    associated_effect_index=associated,
                    family_mode=family_mode,
                    seed_effect_index=seed_effect,
                    seed_quota=quota,
                )
            )
    stats = {
        "covariance_transported_rows": len(rows),
        "covered_bank_shift_pairs": len(covered_bank_shifts),
        "family_mode": family_mode,
        "F750_selector_basis": (
            "38 unrotated fixture calls plus all 137 explicit landed "
            "bank/rotation covariance cases"
        ),
        "retained_rotations": len(rows),
        "row_digest": digest_rows(
            tuple(
                {
                    key: value
                    for key, value in row.items()
                    if key not in {"selected_alternatives"}
                }
                for row in rows
            )
        ),
        "selected_count_range": (
            min(len(row["selected_alternatives"]) for row in rows),
            max(len(row["selected_alternatives"]) for row in rows),
        ),
    }
    return tuple(rows), stats


def receive_family(
    family_name: str,
    events: tuple[dict[str, object], ...],
) -> tuple[tuple[object, ...], object]:
    if any(
        event["effect_id"] is None or event["outcome_index"] is None
        for event in events
    ):
        raise AssertionError("non-total selector result reached receiver")
    return C757._receive_mapped_family(f"cycle763-{family_name}", events)


def census_summary(empirical: object) -> dict[str, object]:
    return {
        "counts": empirical.counts,
        "sample_size": sum(empirical.counts),
        "simplex": tuple(str(value) for value in empirical.simplex),
        "simplex_sum": str(
            sum(empirical.simplex, start=Fraction(0, 1))
        ),
    }


def three_way_table(
    empirical: object,
    held_candidate: tuple[float, ...],
    uniform_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    born_table = C757._comparison_table(
        empirical,
        held_candidate,
    )
    uniform_table = C757._comparison_table(
        empirical,
        uniform_candidate,
    )
    table = []
    for born_level, uniform_level in zip(
        born_table, uniform_table, strict=True
    ):
        effect_rows = []
        for born_row, uniform_row in zip(
            born_level["effect_rows"],
            uniform_level["effect_rows"],
            strict=True,
        ):
            effect_rows.append(
                {
                    "born_Tr_sigma_E": born_row["held_candidate"],
                    "census_simplex": born_row["empirical"],
                    "census_minus_born_hex": born_row["residual_hex"],
                    "census_minus_uniform_hex":
                        uniform_row["residual_hex"],
                    "effect_id": born_row["effect_id"],
                    "uniform": uniform_row["held_candidate"],
                    "verdict_vs_born": born_row["verdict"],
                    "verdict_vs_uniform": uniform_row["verdict"],
                }
            )
        table.append(
            {
                "born_aggregate": born_level["aggregate"],
                "born_disagreement_count":
                    born_level["disagreement_count"],
                "effect_rows": tuple(effect_rows),
                "table_role": "DATA",
                "tolerance": born_level["tolerance"],
                "uniform_aggregate": uniform_level["aggregate"],
                "uniform_disagreement_count":
                    uniform_level["disagreement_count"],
            }
        )
    return tuple(table)


def total_variation(
    simplex: tuple[Fraction, ...],
    candidate: tuple[float, ...],
) -> float:
    return sum(
        abs(float(observed) - target)
        for observed, target in zip(
            simplex, candidate, strict=True
        )
    ) / len(candidate[:2])


def anchors_certificate(
    fixtures: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    captured_b317: str,
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (F750, B317, C757)
    )
    fixture_counts = {
        bank_count: sum(
            fixture["bank_count"] == bank_count
            for fixture in fixtures
        )
        for bank_count in BANK_COUNTS
    }
    program_lengths = {
        bank_count: tuple(
            sorted(
                {
                    fixture["alternative_count"]
                    for fixture in fixtures
                    if fixture["bank_count"] == bank_count
                }
            )
        )
        for bank_count in BANK_COUNTS
    }
    covariance_rows = []
    for bank_count in BANK_COUNTS:
        fixture = next(
            row
            for row in fixtures
            if row["bank_count"] == bank_count
        )
        covariance_rows.append(
            F750.cyclic_enforcement_symmetry(
                bank_count,
                fixture["before"],
                fixture["expected"],
            )
        )
    metrics = B317.menu_metrics(trine_effects)
    detail = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "F750_fixture_count": len(fixtures),
        "F750_fixture_counts_by_bank": fixture_counts,
        "F750_program_lengths_by_bank": program_lengths,
        "F750_unrotated_selected_values": tuple(
            fixture["unrotated_selected"] for fixture in fixtures
        ),
        "cycle760_covariance_cases": sum(
            row["cases"] for row in covariance_rows
        ),
        "cycle760_covariance_failures": sum(
            len(row["failures"]) for row in covariance_rows
        ),
        "held_candidate_hex": tuple(
            value.hex() for value in held_candidate
        ),
        "imported_paths": imported_paths,
        "menu_metrics": metrics,
        "module_identity": {
            "F750_is_C757_F750": F750 is C757.F750,
            "B317_is_C757_B317": B317 is C757.B317,
        },
        "tolerance_ladder": C757.C748.TOLERANCE_LADDER,
    }
    check(
        "A anchors: landed F750, B317, C757, menu, selector, and tolerances",
        imported_paths == AUDIT_INPUT_PATHS
        and F750 is C757.F750
        and B317 is C757.B317
        and len(fixtures) == C757.EPOCH_COUNT == 38
        and fixture_counts == {2: 4, 5: 10, 12: 24}
        and program_lengths == {2: (11,), 5: (35,), 12: (91,)}
        and all(
            fixture["unrotated_selected"] == (0,)
            for fixture in fixtures
        )
        and detail["cycle760_covariance_cases"] == 137
        and detail["cycle760_covariance_failures"] == 0
        and captured_b317.count("PASS ") == 7
        and "FAIL " not in captured_b317
        and len(trine_effects) == len(EFFECT_IDS)
        and metrics["normalization"] < B317.TOL
        and metrics["minimum_eigenvalue"] > -B317.TOL
        and C757.C748.TOLERANCE_LADDER
        == (0.06, 0.02, 0.002, 0.001)
        and tuple(value.hex() for value in held_candidate)
        == C757.C748.FROZEN_HELD_CANDIDATE_HEX,
        detail,
    )
    return detail


def seeding_certificate(
    surface: dict[str, object],
    primary_events: tuple[dict[str, object], ...],
    primary_stats: dict[str, object],
    header_audit: dict[str, object],
) -> dict[str, object]:
    multiplicities = surface["primitive_multiplicities"]
    expected_selected = all(
        event["actual_selected_alternative"]
        == (
            event["alternative_count"]
            - event["program_shift"]
        )
        % event["alternative_count"]
        for event in primary_events
    )
    expected_association = all(
        event["associated_effect_index"]
        == (
            event["global_epoch_ordinal"]
            - event["program_shift"]
        )
        % len(EFFECT_IDS)
        for event in primary_events
    )
    expected_windows = all(
        event["seed_effect_index"]
        == event["associated_effect_index"]
        and event["seed_quota"]
        == min(
            multiplicities[event["associated_effect_index"]],
            event["alternative_count"],
        )
        for event in primary_events
    )
    detail = {
        "ast_audit": {
            "forbidden_seed_reference_hits":
                header_audit["forbidden_seed_reference_hits"],
            "randomness_hits": header_audit["randomness_hits"],
        },
        "b317_source_path": surface["b317_source_path"],
        "coefficient_sum": str(surface["coefficient_sum"]),
        "coefficient_tokens": surface["coefficient_tokens"],
        "primitive_multiplicities": multiplicities,
        "ray_effect_traces": surface["ray_effect_traces"],
        "ray_trace_matches": surface["ray_trace_matches"],
        "retained_rotations": len(primary_events),
        "seeding_convention": SEEDING_CONVENTION,
        "selector_stats": primary_stats,
        "trine_overlap_matrix": surface["trine_overlap_matrix"],
        "trine_self_association":
            surface["trine_self_association"],
    }
    check(
        "B seeding: deterministic landed B317 coefficients/effects with AST firewall",
        surface["coefficient_tokens"] == ("0.17", "0.29", "0.54")
        and surface["coefficient_sum"] == Fraction(1, 1)
        and multiplicities == EXPECTED_PRIMITIVE_MULTIPLICITIES
        and all(surface["ray_trace_matches"])
        and surface["trine_self_association"]
        == tuple(range(len(EFFECT_IDS)))
        and not header_audit["forbidden_seed_reference_hits"]
        and not header_audit["randomness_hits"]
        and SEEDING_CONVENTION["status"] == "SUPPLY"
        and not SEEDING_CONVENTION["new_numeric_seed_constants"]
        and primary_stats["selected_count_range"] == (1, 1)
        and primary_stats["covariance_transported_rows"]
        == len(primary_events)
        and primary_stats["covered_bank_shift_pairs"] > 0
        and expected_selected
        and expected_association
        and expected_windows,
        {
            "coefficient_tokens": surface["coefficient_tokens"],
            "primitive_multiplicities": multiplicities,
            "retained_rotations": len(primary_events),
            "row_digest": primary_stats["row_digest"],
            "seeding_convention": SEEDING_CONVENTION,
        },
    )
    OUTPUT_LINES.append(
        "DATA seeding_rule :: "
        + compact(
            {
                "coefficients": surface["coefficient_tokens"],
                "primitive_multiplicities": multiplicities,
                "rule": SEEDING_CONVENTION,
            }
        )
    )
    return detail


def census_certificate(
    primary_events: tuple[dict[str, object], ...],
    stratum_empiricals: tuple[object, ...],
    pooled_empirical: object,
) -> dict[str, object]:
    strata = tuple(
        {
            "associated_effect_id": EFFECT_IDS[index],
            **census_summary(empirical),
        }
        for index, empirical in enumerate(stratum_empiricals)
    )
    pooled = census_summary(pooled_empirical)
    event_counts = tuple(
        sum(
            event["associated_effect_index"] == index
            for event in primary_events
        )
        for index in range(len(EFFECT_IDS))
    )
    detail = {
        "census_role": "finite selector DATA, not w(E)",
        "per_stratum": strata,
        "pooled": pooled,
        "typed_receiver": (
            "C757._receive_mapped_family / C757.C744"
        ),
    }
    check(
        "C per-stratum and pooled exact censuses/simplexes",
        event_counts == EXPECTED_STRATUM_SIZES
        and tuple(
            empirical.counts for empirical in stratum_empiricals
        )
        == EXPECTED_STRATUM_COUNTS
        and pooled_empirical.counts == EXPECTED_POOLED_COUNTS
        and len(primary_events) == EXPECTED_POOLED_SIZE
        and sum(pooled_empirical.counts) == EXPECTED_POOLED_SIZE
        and all(
            sum(empirical.simplex, start=Fraction(0, 1))
            == Fraction(1, 1)
            for empirical in (*stratum_empiricals, pooled_empirical)
        )
        and all(
            event["effect_id"]
            == EFFECT_IDS[event["outcome_index"]]
            and event["outcome_index"]
            == (
                event["global_epoch_ordinal"]
                + event["actual_selected_alternative"]
            )
            % len(EFFECT_IDS)
            for event in primary_events
        ),
        {
            "per_stratum_counts": tuple(
                empirical.counts
                for empirical in stratum_empiricals
            ),
            "per_stratum_sizes": event_counts,
            "pooled": pooled,
        },
    )
    OUTPUT_LINES.append(
        "DATA seeded_censuses :: " + compact(detail)
    )
    return detail


def comparisons_certificate(
    stratum_empiricals: tuple[object, ...],
    pooled_empirical: object,
    baseline_empirical: object,
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], dict[str, object]]:
    uniform_candidate = tuple(
        float(Fraction(1, len(EFFECT_IDS)))
        for _effect_id in EFFECT_IDS
    )
    tables = {
        EFFECT_IDS[index]: three_way_table(
            empirical,
            held_candidate,
            uniform_candidate,
        )
        for index, empirical in enumerate(stratum_empiricals)
    }
    tables["pooled"] = three_way_table(
        pooled_empirical,
        held_candidate,
        uniform_candidate,
    )

    baseline_uniform = total_variation(
        baseline_empirical.simplex,
        uniform_candidate,
    )
    seeded_uniform = total_variation(
        pooled_empirical.simplex,
        uniform_candidate,
    )
    baseline_born = total_variation(
        baseline_empirical.simplex,
        held_candidate,
    )
    seeded_born = total_variation(
        pooled_empirical.simplex,
        held_candidate,
    )
    direction = {
        "baseline_TV_to_Born": baseline_born,
        "baseline_TV_to_uniform": baseline_uniform,
        "census_delta_seeded_minus_baseline": tuple(
            float(seeded) - float(baseline)
            for seeded, baseline in zip(
                pooled_empirical.simplex,
                baseline_empirical.simplex,
                strict=True,
            )
        ),
        "finding": (
            "SYMMETRY_BREAKS_FARTHER_FROM_UNIFORM_AND_AWAY_FROM_BORN"
        ),
        "seeded_TV_to_Born": seeded_born,
        "seeded_TV_to_uniform": seeded_uniform,
        "symmetry_break_detected": (
            pooled_empirical.counts != baseline_empirical.counts
            and seeded_uniform > baseline_uniform
        ),
        "toward_Born": seeded_born < baseline_born,
    }
    detail = {
        "comparison_kind": (
            "derived census vs Born Tr(sigma E) vs uniform"
        ),
        "direction": direction,
        "held_Born_candidate": held_candidate,
        "table_role": "DATA",
        "three_way_tables": tables,
        "tolerance_ladder": C757.C748.TOLERANCE_LADDER,
        "uniform_candidate": uniform_candidate,
    }
    check(
        "D frozen-tolerance three-way tables and direction discriminator",
        C757.C748.TOLERANCE_LADDER
        == (0.06, 0.02, 0.002, 0.001)
        and tuple(value.hex() for value in held_candidate)
        == C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and set(tables) == {*EFFECT_IDS, "pooled"}
        and all(
            tuple(
                level["tolerance"] for level in table
            )
            == C757.C748.TOLERANCE_LADDER
            and all(
                level["table_role"] == "DATA"
                and len(level["effect_rows"]) == len(EFFECT_IDS)
                for level in table
            )
            for table in tables.values()
        )
        and direction["symmetry_break_detected"] is True
        and direction["toward_Born"] is False
        and seeded_uniform > baseline_uniform
        and seeded_born > baseline_born
        and direction["finding"]
        == (
            "SYMMETRY_BREAKS_FARTHER_FROM_UNIFORM_AND_AWAY_FROM_BORN"
        ),
        {
            "direction": direction,
            "pooled_disagreements": tuple(
                {
                    "born": level["born_disagreement_count"],
                    "uniform":
                        level["uniform_disagreement_count"],
                }
                for level in tables["pooled"]
            ),
            "tolerance_ladder": C757.C748.TOLERANCE_LADDER,
        },
    )
    OUTPUT_LINES.append(
        "DATA direction_finding :: " + compact(direction)
    )
    return detail, direction


def controls_certificate(
    baseline_events: tuple[dict[str, object], ...],
    baseline_empirical: object,
    primary_empirical: object,
    scrambled_events: tuple[dict[str, object], ...],
    scrambled_empirical: object,
    scrambled_stats: dict[str, object],
    effect_permutation: tuple[int, ...],
) -> dict[str, object]:
    baseline = census_summary(baseline_empirical)
    scrambled = census_summary(scrambled_empirical)
    exact_control_delta = tuple(
        Fraction(scrambled_count, EXPECTED_SCRAMBLED_SIZE)
        - Fraction(primary_count, EXPECTED_POOLED_SIZE)
        for scrambled_count, primary_count in zip(
            scrambled_empirical.counts,
            primary_empirical.counts,
            strict=True,
        )
    )
    detail = {
        "scrambled_seeding_control": {
            **scrambled,
            "detected": (
                scrambled_empirical.counts
                != primary_empirical.counts
            ),
            "exact_scrambled_minus_primary":
                tuple(str(value) for value in exact_control_delta),
            "permutation": effect_permutation,
            "permutation_rule": (
                "cyclically move each associated effect to the next "
                "landed ordered effect before applying its seed window"
            ),
            "selector_stats": scrambled_stats,
        },
        "unseeded_cycle760_control": {
            **baseline,
            "construction": (
                "complete F750 singleton translation families with the "
                "landed cyclic-covariance transport used by Cycle 760"
            ),
            "reproduces_cycle760": True,
            "row_digest": digest_rows(
                tuple(
                    (
                        event["global_epoch_ordinal"],
                        event["program_shift"],
                        event["actual_selected_alternative"],
                        event["outcome_index"],
                    )
                    for event in baseline_events
                )
            ),
        },
    }
    check(
        "E controls: Cycle 760 baseline reproduced and scrambled seed detected",
        len(baseline_events) == EXPECTED_BASELINE_SIZE
        and baseline_empirical.counts == EXPECTED_BASELINE_COUNTS
        and tuple(
            str(value) for value in baseline_empirical.simplex
        )
        == tuple(
            str(Fraction(count, EXPECTED_BASELINE_SIZE))
            for count in EXPECTED_BASELINE_COUNTS
        )
        and len(scrambled_events) == EXPECTED_SCRAMBLED_SIZE
        and scrambled_empirical.counts
        == EXPECTED_SCRAMBLED_COUNTS
        and scrambled_empirical.counts
        != primary_empirical.counts
        and any(exact_control_delta)
        and effect_permutation
        != tuple(range(len(EFFECT_IDS)))
        and sorted(effect_permutation)
        == list(range(len(EFFECT_IDS)))
        and scrambled_stats["selected_count_range"] == (1, 1),
        {
            "baseline_counts": baseline_empirical.counts,
            "baseline_size": len(baseline_events),
            "scrambled_counts": scrambled_empirical.counts,
            "scrambled_detected": (
                scrambled_empirical.counts
                != primary_empirical.counts
            ),
            "scrambled_size": len(scrambled_events),
        },
    )
    OUTPUT_LINES.append(
        "DATA controls :: "
        + compact(
            {
                "baseline": baseline,
                "scrambled": scrambled,
                "scrambled_detected": (
                    scrambled_empirical.counts
                    != primary_empirical.counts
                ),
            }
        )
    )
    return detail


def boundary_certificate(
    direction: dict[str, object],
) -> dict[str, object]:
    boundary = {
        "apparatus_coefficients_derived_from_landed_data": True,
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "comparison_only": True,
        "direction_finding": direction["finding"],
        "direction_finding_role": "DATA",
        "finite_fixture_scope": (
            "38 landed F750 fixtures; 1,122 retained seeded rotations"
        ),
        "mapping_convention_derived": False,
        "mapping_convention_supplied": True,
        "seeding_convention_derived": False,
        "seeding_convention_supplied": True,
        "seeding_is_probability_law": False,
        "simplex_promoted_to_weight": False,
        "weight_claim_made": False,
    }
    check(
        "F boundary: supplied map/seed, finite direction DATA, no weight",
        boundary["apparatus_coefficients_derived_from_landed_data"]
        is True
        and boundary["comparison_only"] is True
        and boundary["direction_finding_role"] == "DATA"
        and boundary["mapping_convention_supplied"] is True
        and boundary["mapping_convention_derived"] is False
        and boundary["seeding_convention_supplied"] is True
        and boundary["seeding_convention_derived"] is False
        and boundary["seeding_is_probability_law"] is False
        and boundary["simplex_promoted_to_weight"] is False
        and boundary["weight_claim_made"] is False
        and boundary["born_law_selected"] is False
        and boundary["asymptotic_convergence_claimed"] is False,
        boundary,
    )
    OUTPUT_LINES.append(
        "BOUNDARY HONEST CEILING :: mapping and seed-window conventions "
        "are supplied; the landed coefficients deterministically construct "
        "a finite ensemble, but neither its simplex nor its direction is a "
        "weight, frequency, convergence, or Born-law claim."
    )
    return boundary


def main() -> int:
    started = perf_counter()
    input_sha_before = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    header = header_and_ast_audit()

    trine_effects, forcing_data, captured_b317 = (
        load_landed_apparatus()
    )
    held_candidate = C757._trace_candidate(trine_effects)
    surface = extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    fixtures = fixture_epochs()
    anchors = anchors_certificate(
        fixtures,
        trine_effects,
        captured_b317,
        held_candidate,
    )

    identity_permutation = tuple(range(len(EFFECT_IDS)))
    primary_events, primary_stats = build_seeded_family(
        fixtures,
        surface["primitive_multiplicities"],
        identity_permutation,
        family_mode="landed-seeded",
    )
    seeding = seeding_certificate(
        surface,
        primary_events,
        primary_stats,
        header,
    )

    stratum_events = tuple(
        tuple(
            event
            for event in primary_events
            if event["associated_effect_index"] == index
        )
        for index in range(len(EFFECT_IDS))
    )
    stratum_empiricals = []
    for index, events in enumerate(stratum_events):
        _rows, empirical = receive_family(
            f"seeded-stratum-{index}",
            events,
        )
        stratum_empiricals.append(empirical)
    stratum_empiricals_tuple = tuple(stratum_empiricals)
    _pooled_rows, pooled_empirical = receive_family(
        "seeded-pooled",
        primary_events,
    )
    census = census_certificate(
        primary_events,
        stratum_empiricals_tuple,
        pooled_empirical,
    )

    baseline_events = build_unseeded_baseline(fixtures)
    _baseline_rows, baseline_empirical = receive_family(
        "unseeded-cycle760-control",
        baseline_events,
    )
    comparisons, direction = comparisons_certificate(
        stratum_empiricals_tuple,
        pooled_empirical,
        baseline_empirical,
        held_candidate,
    )

    scrambled_permutation = (
        identity_permutation[1:] + identity_permutation[:1]
    )
    scrambled_events, scrambled_stats = build_seeded_family(
        fixtures,
        surface["primitive_multiplicities"],
        scrambled_permutation,
        family_mode="scrambled-seeding-control",
    )
    _scrambled_rows, scrambled_empirical = receive_family(
        "scrambled-seeding-control",
        scrambled_events,
    )
    controls = controls_certificate(
        baseline_events,
        baseline_empirical,
        pooled_empirical,
        scrambled_events,
        scrambled_empirical,
        scrambled_stats,
        scrambled_permutation,
    )
    boundary = boundary_certificate(direction)

    input_sha_after = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    check(
        "A imported inputs remain byte-stable",
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

    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificates": {
            "A_anchors": anchors,
            "B_seeding_construction": seeding,
            "C_per_stratum_censuses": census,
            "D_three_way_tables": comparisons,
            "E_controls": controls,
            "F_boundary_keys": boundary,
            "header_ast": header,
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "direction_finding": direction["finding"],
        "mapping_convention": MAPPING_CONVENTION,
        "note_path": NOTE_PATH,
        "pass": all(CHECKS.values()),
        "pooled_census": census_summary(pooled_empirical),
        "runtime_seconds": round(runtime_seconds, 6),
        "seeding_convention": SEEDING_CONVENTION,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE763_SYMMETRY_BROKEN_ENSEMBLES_PASS"
        if report["pass"]
        else "CYCLE763_SYMMETRY_BROKEN_ENSEMBLES_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    final_json = compact(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
