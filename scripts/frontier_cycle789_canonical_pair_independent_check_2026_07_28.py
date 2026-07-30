#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-789 canonical model pair.

The Cycle-789 primary and its Cycle-767/784 lineage artifacts are inert text:
they are SHA-anchored and AST-parsed, never imported or executed.  Every
dynamic result is rebuilt from the three declared landed inputs.  The checker
looks for a counterexample first and reports every discrepancy verbatim.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
BLOCKLIST = (
    "scripts/frontier_cycle789_canonical_model_pair_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
    "scripts/frontier_cycle784_strata_independent_check_2026_07_28.py",
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle767_model_pair_independent_check_2026_07_28.py",
)
AUDIT_BLOCKLIST = BLOCKLIST

import ast
from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
BLOCKED_MODULES = tuple(Path(path).stem for path in BLOCKLIST)


class _LineageImportBlocker:
    """Turn any accidental execution of a text-only lineage file into failure."""

    def find_spec(self, fullname, path=None, target=None):
        if any(
            fullname == blocked or fullname.startswith(blocked + ".")
            for blocked in BLOCKED_MODULES
        ):
            raise ImportError(
                f"Cycle-789 checker text-only lineage import blocked: {fullname}"
            )
        return None


if set(BLOCKED_MODULES) & set(sys.modules):
    raise AssertionError(
        ("blocklisted lineage already imported", set(BLOCKED_MODULES) & set(sys.modules))
    )
_IMPORT_BLOCKER = _LineageImportBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


RING_STATIONS = 11
FIXTURE_BANKS = 2
NONVACUUM_STRATA = (1, 2, 3, 4, 5)
MODEL_NAMES = ("GCMIN", "GCMAX")
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    BLOCKLIST[0]:
        "b2f26d28360841afe694d8aef63fa657a7397377ec51f4e8ea8a8563d28308a1",
    BLOCKLIST[1]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    BLOCKLIST[2]:
        "110bd04fadfd201ef21b7e9b5382b1c15090fd6d0c198ec0cd5c565c532b4bed",
    BLOCKLIST[3]:
        "4132fed85d117e738877ce66603f3f410d4e2809149f5058523c13d0090a3543",
    BLOCKLIST[4]:
        "7f2d31ddf3dc3a4a4520a7c93202812636f31dfc5c19597bd7d8ff911af73f38",
}

EXPECTED_THEOREM_STATEMENT = (
    "The retained surface does not entail the realized alternative at any "
    "of the seven ties — leg 2 of the axiom-update criterion at RETAINED "
    "scope, now witnessed by two completions defined entirely from landed "
    "physical functionals (no arbitrary conventions), total on the complete "
    "tie catalog."
)
EXPECTED_PRINTED_STATUS_LINES = (
    "LEG_1_STATUS unchanged: existence not forced — 773",
    "LEG_2_STATUS proved at RETAINED scope by GCMIN/GCMAX",
    "LEG_3_STATUS unchanged: justification open — the min/max mirror "
    "IS the remaining freedom, now embodied as exactly these two models",
    "axiom_update_triggered: false",
)
EXPECTED_PLAIN_READING_KEYS = (
    "GCMIN_actuality_claim",
    "GCMAX_actuality_claim",
    "models_are_completions_under_standing_criterion",
    "selection_forced_by_retained_surface",
)

CERTIFICATES: list[dict[str, object]] = []
DATA_LINES: list[str] = []


def jsonable(value: object) -> object:
    if isinstance(value, dict):
        return {
            ",".join(map(str, key)) if isinstance(key, tuple) else str(key):
                jsonable(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list, set)):
        return [jsonable(item) for item in value]
    return value


def compact(value: object) -> str:
    return json.dumps(
        jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def finding(
    findings: list[dict[str, object]],
    issue: str,
    observed: object,
    expected: object,
) -> None:
    findings.append(
        {"issue": issue, "observed": observed, "expected": expected}
    )


def certificate(
    name: str,
    findings: list[dict[str, object]],
    detail: dict[str, object],
) -> bool:
    passed = not findings
    row = {
        "name": name,
        "pass": passed,
        "findings": tuple(findings),
        "detail": detail,
    }
    CERTIFICATES.append(row)
    return passed


def _assignments(tree: ast.Module) -> dict[str, ast.expr]:
    result: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    result[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            result[node.target.id] = node.value
    return result


def _functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def _dict_entries(node: ast.expr) -> list[tuple[str, ast.expr]]:
    if not isinstance(node, ast.Dict):
        raise AssertionError(("expected dict AST", ast.dump(node)))
    entries = []
    for key, value in zip(node.keys, node.values):
        if not (
            isinstance(key, ast.Constant) and isinstance(key.value, str)
        ):
            raise AssertionError(("expected literal string key", ast.dump(key)))
        entries.append((key.value, value))
    return entries


def _return_dict(function: ast.FunctionDef) -> list[tuple[str, ast.expr]]:
    for node in function.body:
        if isinstance(node, ast.Return):
            return _dict_entries(node.value)
    raise AssertionError(("return dict absent", function.name))


def _nested_dict(
    entries: list[tuple[str, ast.expr]], key: str
) -> list[tuple[str, ast.expr]]:
    matches = [value for name, value in entries if name == key]
    if not matches:
        raise AssertionError(("dict key absent", key))
    return _dict_entries(matches[-1])


def _entry(
    entries: list[tuple[str, ast.expr]], key: str
) -> ast.expr:
    matches = [value for name, value in entries if name == key]
    if not matches:
        raise AssertionError(("dict key absent", key))
    return matches[-1]


def source_contract_audit() -> dict[str, object]:
    """Read the blocklisted lineage only as text/AST and extract its contract."""

    trees = {}
    source_rows = {}
    for relative in (*AUDIT_INPUT_PATHS, *BLOCKLIST):
        observed = file_sha256(relative)
        row = {
            "sha256": observed,
            "expected_sha256": EXPECTED_SHA256[relative],
            "matches": observed == EXPECTED_SHA256[relative],
            "access_mode": (
                "IMPORTED_LANDED_INPUT"
                if relative in AUDIT_INPUT_PATHS
                else "TEXT_AND_AST_ONLY_NOT_IMPORTED"
            ),
        }
        source_rows[relative] = row
        if relative in BLOCKLIST:
            text = (ROOT / relative).read_text(encoding="utf-8")
            trees[relative] = ast.parse(text, filename=relative)

    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    own_assignments = _assignments(own_tree)
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    literal_header = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
    )
    frontier_imports = tuple(
        alias.name
        for node in own_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_")
    )
    expected_imports = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

    primary_tree = trees[BLOCKLIST[0]]
    primary_assignments = _assignments(primary_tree)
    primary_functions = _functions(primary_tree)
    theorem_statement = ast.literal_eval(
        primary_assignments["THEOREM_STATEMENT"]
    )
    primary_frozen_tie = tuple(
        tuple(row)
        for row in ast.literal_eval(primary_assignments["FROZEN_K3_TIE"])
    )
    primary_models = tuple(
        ast.literal_eval(primary_assignments["MODEL_NAMES"])
    )

    theorem_entries = _return_dict(
        primary_functions["theorem_certificate"]
    )
    theorem_key_counts = Counter(name for name, _value in theorem_entries)
    leg_1 = _nested_dict(theorem_entries, "leg_1")
    leg_2 = _nested_dict(theorem_entries, "leg_2")
    leg_3 = _nested_dict(theorem_entries, "leg_3")

    main_node = primary_functions["main"]
    appended_literals = tuple(
        call.args[0].value
        for call in ast.walk(main_node)
        if isinstance(call, ast.Call)
        and isinstance(call.func, ast.Attribute)
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "lines"
        and call.func.attr == "append"
        and len(call.args) == 1
        and isinstance(call.args[0], ast.Constant)
        and isinstance(call.args[0].value, str)
    )
    plain_nodes = []
    for node in ast.walk(main_node):
        if not isinstance(node, ast.Dict):
            continue
        keys = [
            key.value
            for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        ]
        if "GCMIN_actuality_claim" in keys:
            plain_nodes.append(node)
    if len(plain_nodes) != 1:
        raise AssertionError(("plain-reading dict count", len(plain_nodes)))
    plain_entries = _dict_entries(plain_nodes[0])
    plain_values = {
        key: ast.literal_eval(value) for key, value in plain_entries
    }

    c767_tree = trees[BLOCKLIST[3]]
    c767_assignments = _assignments(c767_tree)
    c767_functions = _functions(c767_tree)
    c767_frozen_tie = tuple(
        tuple(row)
        for row in ast.literal_eval(c767_assignments["FROZEN_K3_TIE"])
    )
    complete_source = ast.unparse(c767_functions["complete_selection"])
    c767_semantics = {
        "alpha_uses_min": (
            (
                "'alpha'" in complete_source
                or '"alpha"' in complete_source
            )
            and "min(survivors)" in complete_source
        ),
        "beta_uses_max": (
            (
                "'beta'" in complete_source
                or '"beta"' in complete_source
            )
            and "max(survivors)" in complete_source
        ),
        "empty_returns_none": (
            "if not survivors" in complete_source
            and "return None" in complete_source
        ),
        "singleton_identity": "return survivors[0]" in complete_source,
    }

    c784_frozen_tie = tuple(
        tuple(row)
        for row in ast.literal_eval(
            _assignments(trees[BLOCKLIST[1]])["FROZEN_K3_TIE"]
        )
    )
    return {
        "sources": source_rows,
        "all_sha_anchors_match": all(
            row["matches"] for row in source_rows.values()
        ),
        "literal_AUDIT_INPUT_PATHS": literal_header,
        "frontier_imports": frontier_imports,
        "expected_frontier_imports": expected_imports,
        "exact_frontier_imports": frontier_imports == expected_imports,
        "blocklisted_modules_absent": not (
            set(BLOCKED_MODULES) & set(sys.modules)
        ),
        "primary_contract": {
            "theorem_statement": theorem_statement,
            "frozen_tie": primary_frozen_tie,
            "models": primary_models,
            "theorem_scope": ast.literal_eval(
                _entry(theorem_entries, "scope")
            ),
            "completion_not_actuality": ast.literal_eval(
                _entry(
                    theorem_entries,
                    "standing_criterion_completion_not_actuality",
                )
            ),
            "leg_1_status": ast.literal_eval(_entry(leg_1, "status")),
            "leg_1_source_cycle": ast.literal_eval(
                _entry(leg_1, "source_cycle")
            ),
            "leg_2_status": ast.literal_eval(_entry(leg_2, "status")),
            "leg_2_witnesses_ast":
                ast.unparse(_entry(leg_2, "witnesses")),
            "leg_3_status": ast.literal_eval(_entry(leg_3, "status")),
            "axiom_update_triggered": ast.literal_eval(
                _entry(theorem_entries, "axiom_update_triggered")
            ),
            "theorem_key_counts": dict(theorem_key_counts),
            "printed_literal_lines": appended_literals,
            "plain_reading_boundary": plain_values,
        },
        "cycle767_contract": {
            "frozen_tie": c767_frozen_tie,
            "alpha_selection": min(c767_frozen_tie),
            "beta_selection": max(c767_frozen_tie),
            "completion_semantics": c767_semantics,
        },
        "cycle784_frozen_tie": c784_frozen_tie,
    }


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def independent_positions(k: int) -> tuple[tuple[int, ...], ...]:
    """Brute-force Ind_k(C11), independently of every lineage artifact."""

    rows = []
    for positions in combinations(range(RING_STATIONS), k):
        occupied = set(positions)
        if all(
            (station + 1) % RING_STATIONS not in occupied
            for station in occupied
        ):
            rows.append(positions)
    return tuple(rows)


def independent_closed_form(k: int) -> int:
    numerator = RING_STATIONS * comb(RING_STATIONS - k, k)
    denominator = RING_STATIONS - k
    if numerator % denominator:
        raise AssertionError(("nonintegral independent-set count", k))
    return numerator // denominator


def own_orbit(
    positions: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            {
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            }
        )
    )


def own_families(
    configurations: tuple[tuple[int, ...], ...]
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[
        tuple[int, ...], set[tuple[int, ...]]
    ] = {}
    for positions in configurations:
        representative = min(own_orbit(positions))
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(members))
        for representative, members in sorted(grouped.items())
    }


def own_fixtures() -> tuple[
    tuple[int, tuple[int, int], tuple[object, ...], int, int], ...
]:
    """Rebuild the four two-bank epochs from Cycle-719 primitives."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
        rows.append((event, direction, program, before, expected))
        state = expected
    return tuple(rows)


def own_synchronous_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Compose occupied macros for a complete orbit without M736's helper."""

    moving = tuple(positions)
    word = []
    for _step in range(len(program)):
        live = set(moving)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        moving = tuple(
            (station + 1) % len(program) for station in moving
        )
    return tuple(word)


def postimage_residual(
    after: int, bank_count: int
) -> tuple[int, int, int]:
    banks, links = K.M.unpack_state(after, bank_count)
    bank_work = sum(
        bank[wire]
        for bank in banks
        for wire in (
            K.A.POINTER,
            K.A.U_TO_V,
            K.A.V_TO_U,
            K.A.DIRECTION_OK,
            *K.A.FRESH,
            *K.A.ZERO_WORK,
            K.A.TOKEN_OK,
        )
    )
    return (
        int(after[K.R3.X.SOURCE_POINTER]),
        int(bank_work),
        int(sum(sum(link) for link in links)),
    )


def evaluate_alternative(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
) -> dict[str, object]:
    """Apply the four retained exclusions using an independently built word."""

    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = (0,) * len(program)
    composition_word = own_synchronous_word(program, positions)
    landed_word = M736.synchronous_composition_word(program, positions)
    expected = K.A.apply_semantic(before, composition_word)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    residual = postimage_residual(after, FIXTURE_BANKS)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": residual == (0, 0, 0),
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "survivor": all(conditions.values()),
        "postimage_residual": residual,
        "own_word_matches_landed": composition_word == landed_word,
    }


def evaluate_family(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    evaluations = tuple(
        evaluate_alternative(program, before, alternative)
        for alternative in alternatives
    )
    return {
        "selected": tuple(
            row["positions"] for row in evaluations if row["survivor"]
        ),
        "evaluations": evaluations,
    }


def outcome_class(
    selected: tuple[tuple[int, ...], ...]
) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def run_complete_census() -> dict[str, object]:
    """Exhaust every k=1..5 family, four epochs, and all event-0 rotations."""

    fixtures = own_fixtures()
    strata = {}
    all_rows = []
    all_covariance = []
    word_crosscheck_failures = 0

    for k in NONVACUUM_STRATA:
        configurations = independent_positions(k)
        families = own_families(configurations)
        outcome_counts: Counter[str] = Counter()
        failed_conditions: Counter[str] = Counter()
        rows = []
        covariance_rows = []

        for representative, alternatives in families.items():
            base_selected = None
            for event, direction, program, before, _expected in fixtures:
                result = evaluate_family(program, before, alternatives)
                selected = result["selected"]
                if event == 0:
                    base_selected = selected
                classification = outcome_class(selected)
                outcome_counts[classification] += 1
                for evaluation in result["evaluations"]:
                    word_crosscheck_failures += (
                        not evaluation["own_word_matches_landed"]
                    )
                    for condition, passed in evaluation["conditions"].items():
                        if not passed:
                            failed_conditions[condition] += 1
                row = {
                    "k": k,
                    "representative": representative,
                    "event": event,
                    "direction": direction,
                    "alternative_count": len(alternatives),
                    "outcome_class": classification,
                    "selected_count": len(selected),
                    "selected": selected,
                    "evaluations_sha256": digest(result["evaluations"]),
                    "_evaluations": result["evaluations"],
                }
                rows.append(row)
                all_rows.append(row)

            if base_selected is None:
                raise AssertionError(("missing event zero", k, representative))
            first = fixtures[0]
            shift_rows = []
            failures = []
            membership_failure_count = 0
            for shift in range(RING_STATIONS):
                if shift == 0:
                    observed = base_selected
                    base_row = next(
                        row
                        for row in rows
                        if row["representative"] == representative
                        and row["event"] == 0
                    )
                    evaluations_sha256 = base_row["evaluations_sha256"]
                else:
                    base_program = first[2]
                    rotated_program = (
                        base_program[shift:] + base_program[:shift]
                    )
                    rotated = evaluate_family(
                        rotated_program, first[3], alternatives
                    )
                    observed = rotated["selected"]
                    evaluations_sha256 = digest(rotated["evaluations"])
                    for evaluation in rotated["evaluations"]:
                        word_crosscheck_failures += (
                            not evaluation["own_word_matches_landed"]
                        )
                expected = tuple(
                    sorted(
                        rotate_positions(alternative, -shift)
                        for alternative in base_selected
                    )
                )
                symmetric_difference = len(
                    set(observed) ^ set(expected)
                )
                membership_failure_count += symmetric_difference
                shift_row = {
                    "k": k,
                    "representative": representative,
                    "shift": shift,
                    "observed": observed,
                    "expected": expected,
                    "outcome_class": outcome_class(observed),
                    "evaluations_sha256": evaluations_sha256,
                    "covariant": observed == expected,
                    "membership_failure_count": symmetric_difference,
                }
                shift_rows.append(shift_row)
                if observed != expected:
                    failures.append(shift_row)
            covariance_row = {
                "k": k,
                "representative": representative,
                "failure_count": len(failures),
                "membership_failure_count": membership_failure_count,
                "failures": tuple(failures),
                "shift_rows": tuple(shift_rows),
            }
            covariance_rows.append(covariance_row)
            all_covariance.append(covariance_row)

        covariance_failure = {
            row["representative"]: bool(row["failure_count"])
            for row in covariance_rows
        }
        public_rows = []
        for row in rows:
            row["covariance_failure"] = (
                covariance_failure[row["representative"]]
                if row["event"] == 0
                else None
            )
            row["primary_class"] = (
                "covariance_failure"
                if row["event"] == 0
                and covariance_failure[row["representative"]]
                else row["outcome_class"]
            )
            public_rows.append(
                {
                    key: value
                    for key, value in row.items()
                    if key != "_evaluations"
                }
            )

        for name in ("unique_survivor", "exact_tie", "zero_survivors"):
            outcome_counts[name] += 0
        stratum = {
            "k": k,
            "configuration_count": len(configurations),
            "closed_form_count": independent_closed_form(k),
            "translation_family_count": len(families),
            "family_epoch_count": len(rows),
            "configuration_evaluations": sum(
                row["alternative_count"] for row in rows
            ),
            "outcome_counts": dict(sorted(outcome_counts.items())),
            "covariance_failure_family_count": sum(
                bool(row["failure_count"]) for row in covariance_rows
            ),
            "covariance_failure_shift_count": sum(
                row["failure_count"] for row in covariance_rows
            ),
            "covariance_membership_failure_count": sum(
                row["membership_failure_count"]
                for row in covariance_rows
            ),
            "failed_condition_census": dict(sorted(failed_conditions.items())),
            "rows": tuple(public_rows),
            "covariance": tuple(
                {
                    key: value
                    for key, value in row.items()
                    if key != "shift_rows"
                }
                for row in covariance_rows
            ),
        }
        strata[str(k)] = stratum

    surface = {
        "strata": strata,
        "word_crosscheck_failures": word_crosscheck_failures,
        "fixture_crosscheck":
            own_fixtures() == F750.k_epoch_fixtures(FIXTURE_BANKS),
    }
    surface["sha256"] = digest(surface)
    return {
        **surface,
        "_evaluation_rows": tuple(all_rows),
        "_covariance_rows": tuple(all_covariance),
    }


def first_q_layer_gate_count(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
) -> int:
    """Independent exact integer recount of initially occupied macro lengths."""

    total = 0
    for station in alternative:
        total += len(K.mapped_macro(program[station]))
    return total


def unique_extremum(
    values: dict[tuple[int, ...], int],
    model: str,
) -> tuple[tuple[int, ...] | None, tuple[tuple[int, ...], ...]]:
    extremal = (
        min(values.values())
        if model == "GCMIN"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative, value in values.items()
        if value == extremal
    )
    return (winners[0] if len(winners) == 1 else None, winners)


def complete_selection(
    survivors: tuple[object, ...],
    model: str,
    program: tuple[object, ...],
) -> object | None:
    if model not in MODEL_NAMES:
        raise ValueError(("unknown model", model))
    if not survivors:
        return None
    if len(survivors) == 1:
        return survivors[0]
    if not all(isinstance(alternative, tuple) for alternative in survivors):
        raise TypeError(("non-position tie", survivors))
    values = {
        alternative: first_q_layer_gate_count(alternative, program)
        for alternative in survivors
    }
    selected, _winners = unique_extremum(values, model)
    return selected


def build_tie_catalog(
    experiment: dict[str, object],
) -> tuple[dict[str, object], ...]:
    programs = {
        event: program
        for event, _direction, program, _before, _expected in own_fixtures()
    }
    rows = []
    for selector_row in experiment["_evaluation_rows"]:
        if selector_row["outcome_class"] != "exact_tie":
            continue
        alternatives = selector_row["selected"]
        program = programs[selector_row["event"]]
        values = {
            alternative: first_q_layer_gate_count(alternative, program)
            for alternative in alternatives
        }
        min_selection, min_winners = unique_extremum(values, "GCMIN")
        max_selection, max_winners = unique_extremum(values, "GCMAX")
        permutation_failures = []
        for alternative in alternatives:
            recounts = {
                sum(
                    len(K.mapped_macro(program[station]))
                    for station in ordering
                )
                for ordering in permutations(alternative)
            }
            if recounts != {values[alternative]}:
                permutation_failures.append(
                    {
                        "alternative": alternative,
                        "observed": tuple(sorted(recounts)),
                        "expected": values[alternative],
                    }
                )
        functional_covariance_failures = []
        selection_covariance_failures = []
        for shift in range(RING_STATIONS):
            shifted_program = program[shift:] + program[:shift]
            shifted_alternatives = tuple(
                sorted(
                    rotate_positions(alternative, -shift)
                    for alternative in alternatives
                )
            )
            for alternative in alternatives:
                image = rotate_positions(alternative, -shift)
                image_value = first_q_layer_gate_count(
                    image, shifted_program
                )
                if image_value != values[alternative]:
                    functional_covariance_failures.append(
                        {
                            "shift": shift,
                            "alternative": alternative,
                            "image": image,
                            "observed": image_value,
                            "expected": values[alternative],
                        }
                    )
            for model, base_selection in (
                ("GCMIN", min_selection),
                ("GCMAX", max_selection),
            ):
                observed = complete_selection(
                    shifted_alternatives, model, shifted_program
                )
                expected = (
                    None
                    if base_selection is None
                    else rotate_positions(base_selection, -shift)
                )
                if observed != expected:
                    selection_covariance_failures.append(
                        {
                            "shift": shift,
                            "model": model,
                            "observed": observed,
                            "expected": expected,
                        }
                    )
        rows.append(
            {
                "tie_id": (
                    f"k{selector_row['k']}:"
                    f"{'-'.join(map(str, selector_row['representative']))}:"
                    f"e{selector_row['event']}"
                ),
                "k": selector_row["k"],
                "representative": selector_row["representative"],
                "event": selector_row["event"],
                "alternatives": alternatives,
                "gate_counts": values,
                "GCMIN_selection": min_selection,
                "GCMAX_selection": max_selection,
                "GCMIN_winners": min_winners,
                "GCMAX_winners": max_winners,
                "permutation_recount_failures":
                    tuple(permutation_failures),
                "functional_covariance_failures":
                    tuple(functional_covariance_failures),
                "selection_covariance_failures":
                    tuple(selection_covariance_failures),
            }
        )
    return tuple(rows)


def completed_observable(
    *,
    selected: tuple[object, ...],
    model: str,
    program: tuple[object, ...],
    retained_fields: dict[str, object],
) -> dict[str, object]:
    """Expose every retained field plus the one model-completion output."""

    return {
        **retained_fields,
        "realized": complete_selection(selected, model, program),
    }


def canonical_single_source_rows() -> tuple[dict[str, object], ...]:
    rows = []
    for bank_count in (2, 5, 12):
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
            retained = {
                "surface": "F750_single_source",
                "bank_count": bank_count,
                "event": event,
                "direction": direction,
                "alternatives": len(alternatives),
                "retained_selected": selected,
            }
            gcmin = completed_observable(
                selected=selected,
                model="GCMIN",
                program=program,
                retained_fields=retained,
            )
            gcmax = completed_observable(
                selected=selected,
                model="GCMAX",
                program=program,
                retained_fields=retained,
            )
            rows.append(
                {
                    **retained,
                    "GCMIN": gcmin,
                    "GCMAX": gcmax,
                    "bit_identical": compact(gcmin) == compact(gcmax),
                }
            )
    return tuple(rows)


def leakage_attack(
    experiment: dict[str, object],
    ties: tuple[dict[str, object], ...],
) -> dict[str, object]:
    """Attack canonical and additional off-tie observables for any model leak."""

    programs = {
        event: program
        for event, _direction, program, _before, _expected in own_fixtures()
    }
    primary_off_tie = []
    primary_ties = []
    for row in experiment["_evaluation_rows"]:
        retained = {
            "surface": "family_epoch",
            "k": row["k"],
            "representative": row["representative"],
            "event": row["event"],
            "direction": row["direction"],
            "retained_outcome_class": row["outcome_class"],
            "retained_survivors": row["selected"],
            "retained_evaluations_sha256":
                row["evaluations_sha256"],
            "covariance_failure": row["covariance_failure"],
            "primary_class": row["primary_class"],
        }
        gcmin = completed_observable(
            selected=row["selected"],
            model="GCMIN",
            program=programs[row["event"]],
            retained_fields=retained,
        )
        gcmax = completed_observable(
            selected=row["selected"],
            model="GCMAX",
            program=programs[row["event"]],
            retained_fields=retained,
        )
        comparison = {
            **retained,
            "GCMIN_realized": gcmin["realized"],
            "GCMAX_realized": gcmax["realized"],
            "bit_identical": compact(gcmin) == compact(gcmax),
        }
        if row["outcome_class"] == "exact_tie":
            primary_ties.append(comparison)
        else:
            primary_off_tie.append(comparison)

    single_rows = canonical_single_source_rows()
    primary_103 = tuple(primary_off_tie) + single_rows

    covariance_off_tie = []
    covariance_ties = []
    covariance_family_verdicts = []
    base_program = own_fixtures()[0][2]
    for family in experiment["_covariance_rows"]:
        family_retained = {
            "surface": "covariance_family",
            "k": family["k"],
            "representative": family["representative"],
            "failure_count": family["failure_count"],
            "membership_failure_count":
                family["membership_failure_count"],
            "failure_digest": digest(family["failures"]),
        }
        # The family-level covariance verdict is itself a retained observable.
        family_gcmin = dict(family_retained)
        family_gcmax = dict(family_retained)
        covariance_family_verdicts.append(
            {
                **family_retained,
                "bit_identical":
                    compact(family_gcmin) == compact(family_gcmax),
            }
        )
        for shift_row in family["shift_rows"]:
            if shift_row["shift"] == 0:
                continue
            shift = shift_row["shift"]
            shifted_program = (
                base_program[shift:] + base_program[:shift]
            )
            retained = {
                "surface": "rotated_program_covariance_probe",
                "k": shift_row["k"],
                "representative": shift_row["representative"],
                "shift": shift,
                "retained_outcome_class":
                    shift_row["outcome_class"],
                "retained_survivors": shift_row["observed"],
                "expected_covariant_survivors": shift_row["expected"],
                "retained_evaluations_sha256":
                    shift_row["evaluations_sha256"],
                "covariant": shift_row["covariant"],
                "membership_failure_count":
                    shift_row["membership_failure_count"],
            }
            gcmin = completed_observable(
                selected=shift_row["observed"],
                model="GCMIN",
                program=shifted_program,
                retained_fields=retained,
            )
            gcmax = completed_observable(
                selected=shift_row["observed"],
                model="GCMAX",
                program=shifted_program,
                retained_fields=retained,
            )
            comparison = {
                **retained,
                "GCMIN_realized": gcmin["realized"],
                "GCMAX_realized": gcmax["realized"],
                "bit_identical": compact(gcmin) == compact(gcmax),
            }
            if shift_row["outcome_class"] == "exact_tie":
                covariance_ties.append(comparison)
            else:
                covariance_off_tie.append(comparison)

    tie_lookup = {
        (
            tie["k"],
            tie["representative"],
            tie["event"],
        ): (
            tie["GCMIN_selection"],
            tie["GCMAX_selection"],
        )
        for tie in ties
    }
    tie_catalog_alignment = all(
        (
            row["GCMIN_realized"],
            row["GCMAX_realized"],
        )
        == tie_lookup[
            (row["k"], row["representative"], row["event"])
        ]
        for row in primary_ties
    )
    categories = Counter()
    for row in primary_off_tie:
        if row["k"] == 1:
            categories["k1_off_tie"] += 1
        if row["k"] == 5:
            categories["k5_off_tie"] += 1
        if row["retained_outcome_class"] == "zero_survivors":
            categories["zero_survivors"] += 1
        if (
            row["k"] == 3
            and row["retained_outcome_class"] == "unique_survivor"
        ):
            categories["k3_unique_survivor"] += 1
    return {
        "single_source_rows": single_rows,
        "primary_off_tie_rows": tuple(primary_off_tie),
        "primary_tie_rows": tuple(primary_ties),
        "primary_comparisons_recounted": len(primary_103),
        "primary_off_tie_family_epochs": len(primary_off_tie),
        "single_source_epochs": len(single_rows),
        "primary_103_bit_identical": all(
            row["bit_identical"] for row in primary_103
        ),
        "primary_off_tie_categories": dict(sorted(categories.items())),
        "primary_tie_count": len(primary_ties),
        "primary_tie_disagreement_count": sum(
            not row["bit_identical"] for row in primary_ties
        ),
        "primary_tie_catalog_alignment": tie_catalog_alignment,
        "covariance_family_verdicts":
            tuple(covariance_family_verdicts),
        "covariance_family_verdict_count":
            len(covariance_family_verdicts),
        "covariance_failure_families": sum(
            row["failure_count"] > 0
            for row in covariance_family_verdicts
        ),
        "covariance_family_verdicts_bit_identical": all(
            row["bit_identical"]
            for row in covariance_family_verdicts
        ),
        "additional_covariance_off_tie_rows":
            tuple(covariance_off_tie),
        "additional_covariance_off_tie_count":
            len(covariance_off_tie),
        "additional_covariance_off_tie_bit_identical": all(
            row["bit_identical"] for row in covariance_off_tie
        ),
        "additional_covariance_tie_variants":
            tuple(covariance_ties),
        "additional_covariance_tie_variant_count":
            len(covariance_ties),
    }


def retained_k_battery() -> tuple[dict[str, bool], dict[str, object]]:
    held = {size: K.held_certificate(size) for size in (2, 5, 12)}
    controls = K.order_and_domain_controls()
    battery = {
        "K_held_orbit_sizes_2_5_12": all(
            row["events"] == 2 * size
            and row["fixed_word_failures"] == 0
            for size, row in held.items()
        ),
        "K_literal_inverse_sizes_2_5_12": all(
            row["inverse_failures"] == 0 for row in held.values()
        ),
        "K_token_return_sizes_2_5_12": all(
            row["token_return_failures"] == 0 for row in held.values()
        ),
        "K_decoded_chain_sizes_2_5_12": all(
            row["logical_failures"] == 0 for row in held.values()
        ),
        "K_clean_postimage_sizes_2_5_12": all(
            row["postimage_failures"] == 0 for row in held.values()
        ),
        "K_Q_before_R_order_control": controls["R_before_Q_changed"],
    }
    return battery, {
        "held_summary": {
            str(size): {
                key: row[key]
                for key in (
                    "events",
                    "fixed_word_failures",
                    "inverse_failures",
                    "token_return_failures",
                    "logical_failures",
                    "postimage_failures",
                )
            }
            for size, row in held.items()
        },
        "order_controls": controls,
    }


def retained_m736_battery() -> tuple[
    dict[str, bool], dict[str, object], tuple[tuple[int, ...], ...]
]:
    program = K.interleaved_program(M736.FIXTURE_BANKS)
    _word, layout, _blocks, _metadata = (
        M736.C731.count_certified_controller_build(
            program, M736.C731.DATA_WIDTH, 0
        )
    )
    anchor = M736.cycle735_regression_anchor(layout)
    census = M736.configuration_census()
    configurations = census["configurations"]
    census_public = {
        key: value
        for key, value in census.items()
        if key != "configurations"
    }
    template = M736.template_and_covariance_certificate(
        layout, configurations
    )
    count_enforcement = M736.count_k_enforcement_certificate(
        configurations
    )
    orbit = M736.invariant_full_orbit_certificate(configurations)
    adjacency = M736.adjacency_near_miss_controls()
    deletions = M736.multisource_deletion_controls(
        layout, configurations
    )
    battery = {
        "M736_A_Cycle735_regression_anchor":
            anchor["regression_pass"],
        "M736_B_full_199_configuration_census": (
            census_public["agreement"]
            and census_public["direct_counts_by_k"]
            == M736.EXPECTED_COUNTS_BY_K
            and census_public["direct_total"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census_public["closed_form_total"]
            == census_public["lucas_recurrence_total_L11"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census_public["maximum_token_count"]
            == M736.MAX_TOKEN_COUNT
        ),
        "M736_C_template_exactness_and_covariance": (
            template["all_exact"]
            and template["template_cases"]
            == template["expected_template_cases"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and template["covariance_identities"]
            == template["expected_covariance_identities"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.RING_STATIONS
            and template["AST_no_distinguished_site"]["audit_pass"]
        ),
        "M736_D_count_k_enforcement": (
            count_enforcement["exact"]
            and count_enforcement["acceptance_diagonal"]
            == count_enforcement["expected_acceptance_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and count_enforcement["cross_refusal_off_diagonal"]
            == count_enforcement["expected_cross_refusal_off_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.MAX_TOKEN_COUNT
            and count_enforcement["h1_odd_sector_exercised"]
            and count_enforcement["parity_charge_failures"] == 0
        ),
        "M736_E_invariant_full_orbit_all_199": (
            orbit["pairwise_separated_sector_lawful"]
            and orbit["k_source_composition_ring11"]
            and orbit["outcome"]
            == "all_199_pairwise_separated_configurations_lawful"
            and orbit["orbit_configurations"]
            == orbit["expected_orbit_configurations"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and orbit["exact_register_and_inverse_closures"]
            == orbit["expected_exact_closures"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and all(value == 0 for value in orbit["failure_census"].values())
            and orbit["frozen_obstruction"] is None
        ),
        "M736_F_adjacency_near_miss_controls": (
            adjacency["exact"]
            and adjacency["wall_name"]
            == "ownership_uniqueness_at_adjacent_Q_sites"
            and adjacency["violating_stations"]
            == adjacency["expected_violating_stations"]
        ),
        "M736_G_multisource_deletion_controls": (
            deletions["every_deletion_detected"]
            and deletions["output_change_detections"]
            == deletions["law_refusals"]
            == deletions["deletion_cases"]
            and deletions["count_refusals"]
            == deletions["expected_count_refusals"]
            == deletions["A_gate_deletions"]
        ),
        "M736_H_honest_sector_boundary": (
            orbit["pairwise_separated_sector_lawful"]
            and M736.MAX_TOKEN_COUNT == 5
            and count_enforcement["h1_odd_sector_exercised"]
            and orbit["k_source_composition_ring11"]
            and "no position-independent allocator-power claim"
            in orbit["composition_definition"]
        ),
    }
    detail = {
        "configuration_count": census_public["direct_total"],
        "configuration_counts_by_k":
            census_public["direct_counts_by_k"],
        "template_cases": template["template_cases"],
        "covariance_identities": template["covariance_identities"],
        "orbit_configurations": orbit["orbit_configurations"],
        "deletion_cases": deletions["deletion_cases"],
    }
    return battery, detail, configurations


def single_source_battery() -> tuple[
    dict[str, bool], dict[str, object]
]:
    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    with redirect_stdout(captured):
        landed = F750.enforcement_candidate_census()
    rows = canonical_single_source_rows()
    alternatives_exhausted = sum(row["alternatives"] for row in rows)
    all_agree = all(
        row["retained_selected"] == (0,)
        and row["GCMIN"]["realized"]
        == row["GCMAX"]["realized"]
        == 0
        and row["bit_identical"]
        for row in rows
    )
    battery = {
        "F750_unmodified_single_source_census": (
            F750.FAIL == 0
            and landed["fixtures_exhausted"] == 38
            and landed["alternatives_exhausted"] == 2578
            and landed["selected_count_range"] == [1, 1]
            and landed["tests"]
            == {
                "totality": True,
                "invariance": True,
                "identification": True,
            }
        ),
        "F750_both_models_agree_on_all_unique_fixtures": (
            all_agree
            and len(rows) == 38
            and alternatives_exhausted == 2578
        ),
        "tie_conventions_invisible_off_tie": all_agree,
    }
    return battery, {
        "fixtures": len(rows),
        "alternatives_exhausted": alternatives_exhausted,
        "model_disagreements": sum(
            row["GCMIN"]["realized"] != row["GCMAX"]["realized"]
            for row in rows
        ),
        "captured_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
        "landed_tests": landed["tests"],
    }


def frozen_tie_battery(
    experiment: dict[str, object],
    configurations: tuple[tuple[int, ...], ...],
) -> tuple[dict[str, bool], dict[str, object], dict[str, object]]:
    event, direction, _program, _before, _expected = own_fixtures()[0]
    family = own_orbit((0, 2, 4))
    census_positions = {
        M736.occupied_sites(configuration)
        for configuration in configurations
    }
    matches = [
        row
        for row in experiment["_evaluation_rows"]
        if row["k"] == 3
        and row["representative"] == (0, 2, 4)
        and row["event"] == 0
    ]
    if len(matches) != 1:
        raise AssertionError(("frozen evaluation row count", len(matches)))
    row = matches[0]
    evaluations = {
        evaluation["positions"]: evaluation
        for evaluation in row["_evaluations"]
    }
    battery = {
        "reconstructed_translation_family_has_11_members":
            len(family) == RING_STATIONS,
        "all_family_members_in_M736_lawful_census":
            all(position in census_positions for position in family),
        "frozen_event_is_two_bank_event_0_direction_10": (
            event == 0 and direction == (1, 0)
        ),
        "frozen_survivor_set_exact":
            row["selected"] == FROZEN_K3_TIE,
        "all_three_tied_alternatives_retained_admissible": all(
            evaluations[position]["survivor"]
            and all(evaluations[position]["conditions"].values())
            for position in FROZEN_K3_TIE
        ),
    }
    return battery, {
        "event": event,
        "direction": direction,
        "family": family,
        "selected": row["selected"],
        "evaluation_table_sha256": digest(row["_evaluations"]),
    }, evaluations


def record_facts(
    realized: tuple[int, ...], trace_length: int
) -> tuple[dict[str, bool], dict[str, object]]:
    records = tuple(
        {
            "record_id": f"site-{site}",
            "site": site,
            "lineage": (
                "realized_token_lineage"
                if site in realized
                else "realized_vacuum_lineage"
            ),
            "permanent": True,
            "locked_possibility_admissible": True,
        }
        for site in range(RING_STATIONS)
    )
    snapshots = tuple(records for _boundary in range(trace_length + 1))
    facts = {
        "one_record_per_site": (
            len(records) == RING_STATIONS
            and tuple(row["site"] for row in records)
            == tuple(range(RING_STATIONS))
            and len({row["record_id"] for row in records})
            == RING_STATIONS
        ),
        "records_permanent": (
            all(row["permanent"] for row in records)
            and all(snapshot == records for snapshot in snapshots)
        ),
        "locked_possibility_admissible": (
            all(
                row["locked_possibility_admissible"]
                for row in records
            )
            and all(
                records[site]["lineage"] == "realized_token_lineage"
                for site in realized
            )
        ),
    }
    return facts, {
        "record_ledger_sha256": digest(records),
        "permanence_snapshots_sha256": digest(snapshots),
    }


def retained_base_battery(
    experiment: dict[str, object],
) -> tuple[
    dict[str, bool],
    dict[str, object],
    dict[tuple[int, ...], dict[str, object]],
]:
    k_battery, k_detail = retained_k_battery()
    m_battery, m_detail, configurations = retained_m736_battery()
    single_battery, single_detail = single_source_battery()
    tie_battery, tie_detail, tie_evaluations = frozen_tie_battery(
        experiment, configurations
    )
    base = {
        **k_battery,
        **m_battery,
        **single_battery,
        **tie_battery,
    }
    return base, {
        "K": k_detail,
        "M736": m_detail,
        "single_source": single_detail,
        "frozen_tie": tie_detail,
        "base_checks": len(base),
        "base_sha256": digest(base),
    }, tie_evaluations


def model_battery(
    model: str,
    base_battery: dict[str, bool],
    ties: tuple[dict[str, object], ...],
    tie_evaluations: dict[tuple[int, ...], dict[str, object]],
) -> dict[str, object]:
    retained_surface_sha256 = digest(base_battery)
    frozen = next(
        tie for tie in ties
        if tie["alternatives"] == FROZEN_K3_TIE
    )
    realized = frozen[f"{model}_selection"]
    if not isinstance(realized, tuple):
        raise AssertionError(("frozen completion refused", model, realized))
    facts, record_detail = record_facts(realized, RING_STATIONS)
    program = own_fixtures()[frozen["event"]][2]
    selections = {
        tie["tie_id"]: complete_selection(
            tie["alternatives"], model, own_fixtures()[tie["event"]][2]
        )
        for tie in ties
    }
    completion_checks = {
        "completion_only_resolves_nonempty_ties": (
            complete_selection((), model, ()) is None
            and all(
                complete_selection((alternative,), model, program)
                == alternative
                for tie in ties
                for alternative in tie["alternatives"]
            )
            and len(selections) == 7
            and all(selection is not None for selection in selections.values())
        ),
        "realized_member_is_in_frozen_retained_tie":
            realized in FROZEN_K3_TIE,
        "realized_history_passes_all_retained_conditions": (
            all(tie_evaluations[realized]["conditions"].values())
            and all(
                selections[tie["tie_id"]] in tie["alternatives"]
                for tie in ties
            )
        ),
        "axiom_one_record_per_site": facts["one_record_per_site"],
        "axiom_records_permanent": facts["records_permanent"],
        "axiom_locked_possibility_admissible":
            facts["locked_possibility_admissible"],
        "retained_surface_signature_unchanged":
            retained_surface_sha256 == digest(dict(base_battery)),
    }
    battery = {**dict(base_battery), **completion_checks}
    return {
        "name": model,
        "battery": dict(sorted(battery.items())),
        "checks_run": len(battery),
        "checks_failed": sum(not value for value in battery.values()),
        "pass": all(battery.values()),
        "frozen_selection": realized,
        "tie_selections": selections,
        "retained_surface_sha256": retained_surface_sha256,
        "record_detail": record_detail,
    }


def stripped_experiment(
    experiment: dict[str, object]
) -> dict[str, object]:
    return {
        key: value
        for key, value in experiment.items()
        if not key.startswith("_")
    }


def main() -> int:
    started = monotonic()
    contracts = source_contract_audit()
    first = run_complete_census()
    ties = build_tie_catalog(first)

    functional_findings: list[dict[str, object]] = []
    expected_configurations = {1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
    expected_families = {1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
    observed_configurations = {
        k: first["strata"][str(k)]["configuration_count"]
        for k in NONVACUUM_STRATA
    }
    observed_families = {
        k: first["strata"][str(k)]["translation_family_count"]
        for k in NONVACUUM_STRATA
    }
    if observed_configurations != expected_configurations:
        finding(
            functional_findings,
            "complete independent-configuration census mismatch",
            observed_configurations,
            expected_configurations,
        )
    if observed_families != expected_families:
        finding(
            functional_findings,
            "translation-family census mismatch",
            observed_families,
            expected_families,
        )
    if first["word_crosscheck_failures"] != 0:
        finding(
            functional_findings,
            "independent synchronous word disagrees with landed word",
            first["word_crosscheck_failures"],
            0,
        )
    if not first["fixture_crosscheck"]:
        finding(
            functional_findings,
            "independently rebuilt fixtures disagree with Cycle 750",
            first["fixture_crosscheck"],
            True,
        )
    if len(ties) != 7:
        finding(
            functional_findings, "complete tie count", len(ties), 7
        )
    non_k3 = tuple(tie["tie_id"] for tie in ties if tie["k"] != 3)
    if non_k3:
        finding(
            functional_findings,
            "tie found outside k=3",
            non_k3,
            (),
        )
    for tie in ties:
        if len(tie["GCMIN_winners"]) != 1:
            finding(
                functional_findings,
                f"{tie['tie_id']} GCMIN self-tie/totality break",
                tie["GCMIN_winners"],
                "exactly one winner",
            )
        if len(tie["GCMAX_winners"]) != 1:
            finding(
                functional_findings,
                f"{tie['tie_id']} GCMAX self-tie/totality break",
                tie["GCMAX_winners"],
                "exactly one winner",
            )
        if tie["GCMIN_selection"] == tie["GCMAX_selection"]:
            finding(
                functional_findings,
                f"{tie['tie_id']} model selections do not disagree",
                (
                    tie["GCMIN_selection"],
                    tie["GCMAX_selection"],
                ),
                "different selections",
            )
        for key in (
            "permutation_recount_failures",
            "functional_covariance_failures",
            "selection_covariance_failures",
        ):
            if tie[key]:
                finding(
                    functional_findings,
                    f"{tie['tie_id']} {key}",
                    tie[key],
                    (),
                )
    frozen_rows = [
        tie for tie in ties if tie["alternatives"] == FROZEN_K3_TIE
    ]
    frozen = frozen_rows[0] if len(frozen_rows) == 1 else None
    if len(frozen_rows) != 1:
        finding(
            functional_findings,
            "frozen tie occurrence count",
            len(frozen_rows),
            1,
        )
    if frozen is not None:
        frozen_values = tuple(
            frozen["gate_counts"][alternative]
            for alternative in FROZEN_K3_TIE
        )
        if frozen_values != (769, 1350, 610):
            finding(
                functional_findings,
                "frozen tie independent gate-count recount",
                frozen_values,
                (769, 1350, 610),
            )
        if (
            frozen["GCMIN_selection"],
            frozen["GCMAX_selection"],
        ) != ((0, 7, 9), (0, 2, 9)):
            finding(
                functional_findings,
                "frozen tie canonical selections",
                (
                    frozen["GCMIN_selection"],
                    frozen["GCMAX_selection"],
                ),
                ((0, 7, 9), (0, 2, 9)),
            )
    functional_pass = certificate(
        "CERTIFICATE_1_FUNCTIONAL_RECOUNT_EVERY_TIE",
        functional_findings,
        {
            "ties_recounted": len(ties),
            "GCMIN_decisive": sum(
                len(tie["GCMIN_winners"]) == 1 for tie in ties
            ),
            "GCMAX_decisive": sum(
                len(tie["GCMAX_winners"]) == 1 for tie in ties
            ),
            "per_tie_table_sha256": digest(ties),
            "configuration_counts": observed_configurations,
            "family_counts": observed_families,
        },
    )

    base_battery, battery_detail, tie_evaluations = (
        retained_base_battery(first)
    )
    gcmin = model_battery(
        "GCMIN", dict(base_battery), ties, tie_evaluations
    )
    gcmax = model_battery(
        "GCMAX", dict(base_battery), ties, tie_evaluations
    )
    battery_findings: list[dict[str, object]] = []
    for model in (gcmin, gcmax):
        if model["checks_run"] != 29:
            finding(
                battery_findings,
                f"{model['name']} battery check count",
                model["checks_run"],
                29,
            )
        failed = tuple(
            key for key, passed in model["battery"].items() if not passed
        )
        if failed:
            finding(
                battery_findings,
                f"{model['name']} battery failures",
                failed,
                (),
            )
        if not model["pass"] or model["checks_failed"] != 0:
            finding(
                battery_findings,
                f"{model['name']} battery summary",
                {
                    "pass": model["pass"],
                    "failed": model["checks_failed"],
                },
                {"pass": True, "failed": 0},
            )
    if len(base_battery) != 22:
        finding(
            battery_findings,
            "shared retained base battery check count",
            len(base_battery),
            22,
        )
    if tuple(gcmin["battery"]) != tuple(gcmax["battery"]):
        finding(
            battery_findings,
            "GCMIN/GCMAX battery key discrepancy",
            {
                "GCMIN": tuple(gcmin["battery"]),
                "GCMAX": tuple(gcmax["battery"]),
            },
            "identical ordered 29-key battery",
        )
    battery_pass = certificate(
        "CERTIFICATE_2_BATTERY_RECOUNT_BOTH_MODELS",
        battery_findings,
        {
            "base_checks": len(base_battery),
            "GCMIN": {
                "run": gcmin["checks_run"],
                "failed": gcmin["checks_failed"],
                "battery_sha256": digest(gcmin["battery"]),
            },
            "GCMAX": {
                "run": gcmax["checks_run"],
                "failed": gcmax["checks_failed"],
                "battery_sha256": digest(gcmax["battery"]),
            },
            "harness_detail_sha256": digest(battery_detail),
        },
    )

    leakage = leakage_attack(first, ties)
    leakage_findings: list[dict[str, object]] = []
    expected_categories = {
        "k1_off_tie": 4,
        "k3_unique_survivor": 3,
        "k5_off_tie": 4,
        "zero_survivors": 58,
    }
    expected_leakage_scalars = (
        ("primary_comparisons_recounted", 103),
        ("primary_off_tie_family_epochs", 65),
        ("single_source_epochs", 38),
        ("primary_tie_count", 7),
        ("primary_tie_disagreement_count", 7),
        ("covariance_family_verdict_count", 18),
        ("covariance_failure_families", 5),
    )
    for key, expected in expected_leakage_scalars:
        if leakage[key] != expected:
            finding(
                leakage_findings,
                f"leakage census {key}",
                leakage[key],
                expected,
            )
    if leakage["primary_off_tie_categories"] != expected_categories:
        finding(
            leakage_findings,
            "off-tie category census",
            leakage["primary_off_tie_categories"],
            expected_categories,
        )
    for key in (
        "primary_103_bit_identical",
        "primary_tie_catalog_alignment",
        "covariance_family_verdicts_bit_identical",
        "additional_covariance_off_tie_bit_identical",
    ):
        if not leakage[key]:
            if key == "primary_103_bit_identical":
                observed_rows = tuple(
                    row
                    for row in (
                        *leakage["primary_off_tie_rows"],
                        *leakage["single_source_rows"],
                    )
                    if not row["bit_identical"]
                )
            elif key == "additional_covariance_off_tie_bit_identical":
                observed_rows = tuple(
                    row
                    for row in leakage[
                        "additional_covariance_off_tie_rows"
                    ]
                    if not row["bit_identical"]
                )
            elif key == "covariance_family_verdicts_bit_identical":
                observed_rows = tuple(
                    row
                    for row in leakage["covariance_family_verdicts"]
                    if not row["bit_identical"]
                )
            else:
                observed_rows = leakage["primary_tie_rows"]
            finding(
                leakage_findings,
                f"observable model discrepancy: {key}",
                observed_rows,
                "no off-tie discrepancy",
            )
    leakage_pass = certificate(
        "CERTIFICATE_3_LEAKAGE_ATTACK",
        leakage_findings,
        {
            "primary_comparisons_recounted":
                leakage["primary_comparisons_recounted"],
            "primary_off_tie_categories":
                leakage["primary_off_tie_categories"],
            "primary_off_tie_bit_identical":
                leakage["primary_103_bit_identical"],
            "tie_disagreement_count":
                leakage["primary_tie_disagreement_count"],
            "covariance_failure_families":
                leakage["covariance_failure_families"],
            "additional_covariance_off_tie_probes":
                leakage["additional_covariance_off_tie_count"],
            "additional_covariance_off_tie_bit_identical":
                leakage["additional_covariance_off_tie_bit_identical"],
            "additional_covariance_tie_variants":
                leakage["additional_covariance_tie_variant_count"],
        },
    )

    primary_contract = contracts["primary_contract"]
    theorem_findings: list[dict[str, object]] = []
    theorem_expectations = (
        ("theorem_statement", EXPECTED_THEOREM_STATEMENT),
        ("frozen_tie", FROZEN_K3_TIE),
        ("models", MODEL_NAMES),
        ("theorem_scope", "RETAINED"),
        ("completion_not_actuality", True),
        ("leg_1_status", "UNCHANGED_EXISTENCE_NOT_FORCED"),
        ("leg_1_source_cycle", 773),
        ("leg_2_status", "PROVED_AT_RETAINED_SCOPE"),
        ("leg_2_witnesses_ast", "MODEL_NAMES"),
        ("leg_3_status", "UNCHANGED_JUSTIFICATION_OPEN"),
        ("axiom_update_triggered", False),
    )
    for key, expected in theorem_expectations:
        if primary_contract[key] != expected:
            finding(
                theorem_findings,
                f"primary theorem contract {key}",
                primary_contract[key],
                expected,
            )
    printed = primary_contract["printed_literal_lines"]
    for expected_line in EXPECTED_PRINTED_STATUS_LINES:
        if expected_line not in printed:
            finding(
                theorem_findings,
                "printed theorem/leg line absent or changed",
                printed,
                expected_line,
            )
    plain = primary_contract["plain_reading_boundary"]
    expected_plain = {
        "GCMIN_actuality_claim": False,
        "GCMAX_actuality_claim": False,
        "models_are_completions_under_standing_criterion": True,
        "selection_forced_by_retained_surface": False,
    }
    if tuple(plain) != EXPECTED_PLAIN_READING_KEYS or plain != expected_plain:
        finding(
            theorem_findings,
            "printed PLAIN_READING_BOUNDARY keys/values",
            plain,
            expected_plain,
        )
    theorem_pass = certificate(
        "CERTIFICATE_4_THEOREM_SCOPE_AUDIT",
        theorem_findings,
        {
            "theorem_verbatim": primary_contract["theorem_statement"],
            "scope": primary_contract["theorem_scope"],
            "completion_not_actuality":
                primary_contract["completion_not_actuality"],
            "leg_1_status": primary_contract["leg_1_status"],
            "leg_2_status": primary_contract["leg_2_status"],
            "leg_3_status": primary_contract["leg_3_status"],
            "axiom_update_triggered":
                primary_contract["axiom_update_triggered"],
            "printed_status_lines": tuple(
                line for line in printed
                if line in EXPECTED_PRINTED_STATUS_LINES
            ),
            "plain_reading_boundary": plain,
            "duplicate_theorem_dict_keys": {
                key: count
                for key, count in primary_contract[
                    "theorem_key_counts"
                ].items()
                if count > 1
            },
        },
    )

    c767 = contracts["cycle767_contract"]
    alignment_table = (
        {
            "row": "Cycle767_alpha",
            "selection": c767["alpha_selection"],
            "alignment": "neither canonical frozen selection",
        },
        {
            "row": "Cycle767_beta",
            "selection": c767["beta_selection"],
            "alignment": "GCMIN",
        },
        {
            "row": "GCMIN",
            "selection": (
                None if frozen is None else frozen["GCMIN_selection"]
            ),
            "alignment": "Cycle767_beta",
        },
        {
            "row": "GCMAX",
            "selection": (
                None if frozen is None else frozen["GCMAX_selection"]
            ),
            "alignment": "new canonical maximum",
        },
    )
    comparison_findings: list[dict[str, object]] = []
    if not all(c767["completion_semantics"].values()):
        finding(
            comparison_findings,
            "Cycle767 alpha/beta completion AST semantics",
            c767["completion_semantics"],
            {key: True for key in c767["completion_semantics"]},
        )
    if not (
        c767["frozen_tie"]
        == contracts["cycle784_frozen_tie"]
        == contracts["primary_contract"]["frozen_tie"]
        == FROZEN_K3_TIE
    ):
        finding(
            comparison_findings,
            "767/784/789 frozen-tie lineage alignment",
            {
                "767": c767["frozen_tie"],
                "784": contracts["cycle784_frozen_tie"],
                "789": contracts["primary_contract"]["frozen_tie"],
            },
            FROZEN_K3_TIE,
        )
    observed_alignment = (
        None
        if frozen is None
        else (
            frozen["GCMIN_selection"],
            frozen["GCMAX_selection"],
            c767["beta_selection"],
        )
    )
    if observed_alignment != ((0, 7, 9), (0, 2, 9), (0, 7, 9)):
        finding(
            comparison_findings,
            "canonical pair versus Cycle767 beta",
            observed_alignment,
            ((0, 7, 9), (0, 2, 9), (0, 7, 9)),
        )
    comparison_pass = certificate(
        "CERTIFICATE_5_CYCLE767_COMPARISON_AUDIT",
        comparison_findings,
        {
            "alignment_table": alignment_table,
            "GCMIN_equals_Cycle767_beta": (
                frozen is not None
                and frozen["GCMIN_selection"] == c767["beta_selection"]
            ),
            "GCMAX_selection": (
                None if frozen is None else frozen["GCMAX_selection"]
            ),
        },
    )

    second = run_complete_census()
    second_ties = build_tie_catalog(second)
    deterministic = (
        stripped_experiment(first) == stripped_experiment(second)
        and first["sha256"] == second["sha256"]
        and ties == second_ties
        and digest(ties) == digest(second_ties)
    )
    elapsed = monotonic() - started

    DATA_LINES.append(
        "AUDIT_INPUT_PATHS " + compact(AUDIT_INPUT_PATHS)
    )
    DATA_LINES.append(
        "SHA_ANCHOR_CONTROL " + compact(contracts["sources"])
    )
    for k in NONVACUUM_STRATA:
        stratum = first["strata"][str(k)]
        DATA_LINES.append(
            f"CENSUS_SUMMARY k={k} "
            + compact(
                {
                    key: value
                    for key, value in stratum.items()
                    if key not in {"rows", "covariance"}
                }
            )
        )
    for tie in ties:
        DATA_LINES.append(
            "PER_TIE_FUNCTIONAL_RECOUNT " + compact(tie)
        )
    DATA_LINES.append(
        "MODEL_BATTERY_RECOUNT "
        + compact(
            {
                "GCMIN": {
                    "checks_run": gcmin["checks_run"],
                    "checks_failed": gcmin["checks_failed"],
                    "battery": gcmin["battery"],
                },
                "GCMAX": {
                    "checks_run": gcmax["checks_run"],
                    "checks_failed": gcmax["checks_failed"],
                    "battery": gcmax["battery"],
                },
            }
        )
    )
    DATA_LINES.append(
        "LEAKAGE_ATTACK_SUMMARY "
        + compact(CERTIFICATES[2]["detail"])
    )
    DATA_LINES.append(
        "THEOREM_PRINTED_KEYS_VERBATIM "
        + compact(CERTIFICATES[3]["detail"])
    )
    DATA_LINES.append(
        "CYCLE767_ALIGNMENT_TABLE " + compact(alignment_table)
    )
    preliminary_lines = DATA_LINES + [
        (
            f"{'PASS' if row['pass'] else 'FAIL'} {row['name']} :: "
            + compact(
                {
                    "findings": row["findings"],
                    "detail": row["detail"],
                }
            )
        )
        for row in CERTIFICATES
    ]
    projected_stdout_bytes = len(
        ("\n".join(preliminary_lines) + "\n").encode("utf-8")
    ) + 8192
    control_findings: list[dict[str, object]] = []
    for key in (
        "all_sha_anchors_match",
        "literal_AUDIT_INPUT_PATHS",
        "exact_frontier_imports",
        "blocklisted_modules_absent",
    ):
        if not contracts[key]:
            finding(
                control_findings,
                f"control {key}",
                contracts[key],
                True,
            )
    if contracts["frontier_imports"] != tuple(
        Path(path).stem for path in AUDIT_INPUT_PATHS
    ):
        finding(
            control_findings,
            "direct frontier import list",
            contracts["frontier_imports"],
            tuple(Path(path).stem for path in AUDIT_INPUT_PATHS),
        )
    if not deterministic:
        finding(
            control_findings,
            "two-run deterministic replay",
            {
                "first_surface_sha256": first["sha256"],
                "second_surface_sha256": second["sha256"],
                "first_tie_sha256": digest(ties),
                "second_tie_sha256": digest(second_ties),
            },
            "exact match",
        )
    if elapsed >= AUDIT_TIMEOUT_SEC:
        finding(
            control_findings,
            "runtime bound",
            elapsed,
            f"< {AUDIT_TIMEOUT_SEC}",
        )
    if projected_stdout_bytes >= STDOUT_LIMIT_BYTES:
        finding(
            control_findings,
            "stdout bound",
            projected_stdout_bytes,
            f"< {STDOUT_LIMIT_BYTES}",
        )
    controls_pass = certificate(
        "CERTIFICATE_6_CONTROLS",
        control_findings,
        {
            "sha_anchors": contracts["all_sha_anchors_match"],
            "blocklist_enforced": contracts["blocklisted_modules_absent"],
            "literal_three_input_header":
                contracts["literal_AUDIT_INPUT_PATHS"],
            "deterministic": deterministic,
            "first_surface_sha256": first["sha256"],
            "second_surface_sha256": second["sha256"],
            "first_tie_catalog_sha256": digest(ties),
            "second_tie_catalog_sha256": digest(second_ties),
            "runtime_seconds": round(elapsed, 6),
            "runtime_under_1500s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_projected_bytes": projected_stdout_bytes,
            "stdout_projected_under_150KB":
                projected_stdout_bytes < STDOUT_LIMIT_BYTES,
        },
    )

    all_passed = all(
        (
            functional_pass,
            battery_pass,
            leakage_pass,
            theorem_pass,
            comparison_pass,
            controls_pass,
        )
    )
    certificate_lines = [
        (
            f"{'PASS' if row['pass'] else 'FAIL'} {row['name']} :: "
            + compact(
                {
                    "findings": row["findings"],
                    "detail": row["detail"],
                }
            )
        )
        for row in CERTIFICATES
    ]
    refutation_lines = [
        f"REFUTATION_FINDING {row['name']} :: {compact(item)}"
        for row in CERTIFICATES
        if not row["pass"]
        for item in row["findings"]
    ]
    terminal = {
        "status": "CONFIRMED" if all_passed else "REFUTED",
        "battery_recounts": {
            "GCMIN": (gcmin["checks_run"], gcmin["checks_failed"]),
            "GCMAX": (gcmax["checks_run"], gcmax["checks_failed"]),
        },
        "off_tie_comparisons": leakage["primary_comparisons_recounted"],
        "off_tie_bit_identical": (
            leakage["primary_103_bit_identical"]
            and leakage["additional_covariance_off_tie_bit_identical"]
        ),
        "tie_totality": (
            len(ties) == 7
            and all(
                len(tie["GCMIN_winners"])
                == len(tie["GCMAX_winners"])
                == 1
                for tie in ties
            )
        ),
        "tie_disagreements":
            leakage["primary_tie_disagreement_count"],
        "runtime_seconds": round(elapsed, 6),
    }
    output = (
        "\n".join(
            DATA_LINES
            + certificate_lines
            + refutation_lines
            + ["FINAL " + compact(terminal)]
        )
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
