#!/usr/bin/env python3
"""Cycle 832 independent adversarial checker: backbone exhaustion and skeleton.

The Cycle-832/831 primaries are evidence only: this checker reads the named
Cycle-832 source as bytes/AST and blocks every named primary from import.  The
only dynamic import is the landed Cycle-719 core needed for an independent
full-state recurrence replay.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, CORE_PATH = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
BLOCKLISTED_PRIMARY_MODULES = (
    "frontier_cycle832_cohort_moment_law_2026_07_28",
    "frontier_cycle831_deep_k2_forecast_tests_2026_07_28",
    "frontier_cycle831_cohorts_independent_check_2026_07_28",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_PRIMARY_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def assignment_value(tree: ast.Module, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def literal(tree: ast.Module, name: str) -> Any:
    return ast.literal_eval(assignment_value(tree, name))


def function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def is_twice_name(node: ast.AST, name: str) -> bool:
    return (
        isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mult)
        and isinstance(node.left, ast.Constant)
        and node.left.value == 2
        and isinstance(node.right, ast.Name)
        and node.right.id == name
    )


def range_is_twice_name(node: ast.AST, name: str) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "range"
        and len(node.args) == 1
        and is_twice_name(node.args[0], name)
    )


def source_evidence() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload.decode(), filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": (
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
        ),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "parseable_ast": isinstance(trees[path], ast.Module),
        "access": (
            "TEXT_AST_ONLY_BLOCKLISTED"
            if path == PRIMARY_PATH else "SOLE_DYNAMIC_IMPORT_SOURCE"
        ),
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "payloads": payloads,
        "trees": trees,
        "rows": rows,
        "AUDIT_INPUT_PATHS_literal":
            literal(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "all_paths_existing":
            all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "all_paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_paths_existing"]
        and result["all_paths_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["parseable_ast"]
            for row in rows
        )
    )
    return result


def separated_pairs(stations: int) -> tuple[tuple[int, int], ...]:
    rows = []
    for left in range(stations):
        for right in range(left + 1, stations):
            clockwise = (right - left) % stations
            counterclockwise = (left - right) % stations
            if min(clockwise, counterclockwise) > 1:
                rows.append((left, right))
    return tuple(rows)


def extract_earlier_resolved(
    tree: ast.Module,
    cohort_keys: dict[int, tuple[tuple[int, tuple[int, int]], ...]],
) -> frozenset[tuple[int, tuple[int, int]]]:
    node = assignment_value(tree, "EARLIER_RESOLVED")
    if not (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "frozenset"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Set)
    ):
        raise AssertionError("EARLIER_RESOLVED is not the declared frozenset")
    rows: set[tuple[int, tuple[int, int]]] = set()
    for element in node.args[0].elts:
        if isinstance(element, ast.Starred):
            subscript = element.value
            if not (
                isinstance(subscript, ast.Subscript)
                and isinstance(subscript.value, ast.Name)
                and subscript.value.id == "COHORT_KEYS"
                and isinstance(subscript.slice, ast.Constant)
                and isinstance(subscript.slice.value, int)
            ):
                raise AssertionError(ast.dump(element))
            rows.update(cohort_keys[subscript.slice.value])
        else:
            rows.add(ast.literal_eval(element))
    return frozenset(rows)


def subscripted_integer_keys(
    node: ast.AST,
    base_name: str,
) -> frozenset[int]:
    return frozenset(
        child.slice.value
        for child in ast.walk(node)
        if (
            isinstance(child, ast.Subscript)
            and isinstance(child.value, ast.Name)
            and child.value.id == base_name
            and isinstance(child.slice, ast.Constant)
            and isinstance(child.slice.value, int)
        )
    )


def catalog_certificate(
    primary_tree: ast.Module,
    core_tree: ast.Module,
) -> dict[str, object]:
    banks = literal(primary_tree, "FIXTURE_BANKS")
    stations = literal(primary_tree, "RING_STATIONS")
    declared_family_size = literal(primary_tree, "FAMILY_SIZE")
    ordered_cohort_events = literal(primary_tree, "EVENTS")
    backbone = literal(primary_tree, "BACKBONE")
    if not (
        isinstance(banks, int)
        and isinstance(stations, int)
        and isinstance(backbone, tuple)
        and isinstance(ordered_cohort_events, tuple)
    ):
        raise AssertionError("unexpected catalog literal types")

    held = function(core_tree, "held_certificate")
    held_event_loops = tuple(
        node for node in ast.walk(held)
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "event"
            and range_is_twice_name(node.iter, "bank_count")
        )
    )
    held_event_chain = tuple(
        node for node in ast.walk(held)
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "EventChain"
            and any(
                keyword.arg == "bank"
                and is_twice_name(keyword.value, "bank_count")
                for keyword in node.keywords
            )
        )
    )
    held_event_return = tuple(
        node for node in ast.walk(held)
        if (
            isinstance(node, ast.Dict)
            and any(
                isinstance(key, ast.Constant)
                and key.value == "events"
                and is_twice_name(value, "bank_count")
                for key, value in zip(node.keys, node.values)
            )
        )
    )
    seed = function(primary_tree, "build_seed_family")
    seed_event_loops = tuple(
        node for node in ast.walk(seed)
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "event"
            and range_is_twice_name(node.iter, "FIXTURE_BANKS")
        )
    )
    open_function = function(primary_tree, "open_pair_event_keys")
    open_event_ranges = tuple(
        node for node in ast.walk(open_function)
        if range_is_twice_name(node, "FIXTURE_BANKS")
    )
    resolved_assignments = tuple(
        node for node in ast.walk(open_function)
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "resolved"
                for target in node.targets
            )
        )
    )
    if len(resolved_assignments) != 1:
        raise AssertionError(("resolved assignments", len(resolved_assignments)))
    resolved_expression = resolved_assignments[0].value
    resolved_names = frozenset(
        child.id for child in ast.walk(resolved_expression)
        if isinstance(child, ast.Name)
    )
    resolved_cohort_events = subscripted_integer_keys(
        resolved_expression, "COHORT_KEYS"
    )

    lawful_events = tuple(range(2 * banks))
    pairs = separated_pairs(stations)
    cohort_keys = {
        event: tuple((event, pair) for pair in backbone)
        for event in ordered_cohort_events
    }
    earlier_resolved = extract_earlier_resolved(primary_tree, cohort_keys)
    landed_resolved = (
        set(earlier_resolved)
        | set(cohort_keys[2])
        | set(cohort_keys[1])
    )
    catalog = tuple(
        (event, pair) for pair in pairs for event in lawful_events
    )
    open_keys = tuple(
        (pair, event) for event, pair in catalog
        if (event, pair) not in landed_resolved
    )
    backbone_set = set(backbone)
    open_backbone = tuple(
        key for key in open_keys if key[0] in backbone_set
    )
    claimed_three_event_inventory = frozenset(
        (event, pair)
        for pair in backbone
        for event in set(ordered_cohort_events)
    )
    lawful_backbone_inventory = frozenset(
        (event, pair)
        for pair in backbone
        for event in lawful_events
    )
    event_census = {
        event: sum(key[1] == event for key in open_keys)
        for event in lawful_events
    }
    extra_lawful_backbone = tuple(sorted(
        lawful_backbone_inventory - claimed_three_event_inventory
    ))
    static_definition_exact = (
        len(held_event_loops) == 1
        and len(held_event_chain) == 1
        and len(held_event_return) == 1
        and len(seed_event_loops) == 1
        and len(open_event_ranges) == 1
        and "EARLIER_RESOLVED" in resolved_names
        and resolved_cohort_events == frozenset({1, 2})
    )
    narrow_inventory_resolved = claimed_three_event_inventory <= landed_resolved
    full_inventory_resolved = lawful_backbone_inventory <= landed_resolved
    primary_exhaustion_refuted = (
        static_definition_exact
        and lawful_events == (0, 1, 2, 3)
        and len(pairs) == 44
        and len(catalog) == declared_family_size == 176
        and len(claimed_three_event_inventory) == 27
        and len(lawful_backbone_inventory) == 36
        and len(extra_lawful_backbone) == 9
        and narrow_inventory_resolved
        and full_inventory_resolved
        and len(open_keys) == 133
        and not open_backbone
        and event_census == {0: 34, 1: 34, 2: 34, 3: 31}
    )
    return {
        "verdict": "FAIL",
        "finding":
            "FAIL: the k=2 catalog has four lawful events per pair "
            "(0,1,2,3), so the nine-pair backbone inventory is 36, not 27; "
            "event 3 exists at k=2 and makes the pre-registered predictions "
            "live.",
        "module_definition": {
            "core_path": CORE_PATH,
            "function": "held_certificate(bank_count)",
            "event_chain_bank_expression": "2 * bank_count",
            "event_loop_expression": "range(2 * bank_count)",
            "reported_events_expression": "2 * bank_count",
            "line": held.lineno,
            "primary_seed_function": "build_seed_family()",
            "primary_seed_event_loop_expression":
                "range(2 * FIXTURE_BANKS)",
            "primary_seed_line": seed.lineno,
            "static_definition_exact": static_definition_exact,
        },
        "fixture_banks": banks,
        "lawful_events_per_pair": len(lawful_events),
        "lawful_events": lawful_events,
        "separated_pair_count": len(pairs),
        "catalog_key_count": len(catalog),
        "declared_family_size": declared_family_size,
        "backbone_pair_count": len(backbone),
        "claimed_events_0_1_2_inventory_count":
            len(claimed_three_event_inventory),
        "claimed_27_all_resolved": narrow_inventory_resolved,
        "lawful_backbone_inventory_count": len(lawful_backbone_inventory),
        "extra_lawful_backbone_keys": extra_lawful_backbone,
        "all_36_lawful_backbone_keys_resolved": full_inventory_resolved,
        "open_key_count": len(open_keys),
        "open_event_census": event_census,
        "event3_open_key_count": event_census[3],
        "open_keys_on_nine_pair_backbone": open_backbone,
        "none_of_133_open_keys_on_backbone":
            len(open_keys) == 133 and not open_backbone,
        "landed_resolution_list_cross_check": {
            "earlier_resolved_count": len(earlier_resolved),
            "resolved_union_count": len(landed_resolved),
            "resolved_union_uses":
                ("EARLIER_RESOLVED", "COHORT_KEYS[2]", "COHORT_KEYS[1]"),
            "event3_backbone_keys_in_EARLIER_RESOLVED": all(
                (3, pair) in earlier_resolved for pair in backbone
            ),
        },
        "checker_pass": primary_exhaustion_refuted,
    }


def euclid(left: int, right: int) -> int:
    while right:
        left, right = right, left % right
    return abs(left)


def trial_factor(value: int) -> tuple[tuple[int, int], ...]:
    if value < 1:
        raise ValueError(value)
    rows = []
    remainder = value
    candidate = 2
    while candidate * candidate <= remainder:
        exponent = 0
        while remainder % candidate == 0:
            remainder //= candidate
            exponent += 1
        if exponent:
            rows.append((candidate, exponent))
        candidate += 1
    if remainder > 1:
        rows.append((remainder, 1))
    return tuple(rows)


def arithmetic_certificate(primary_tree: ast.Module) -> dict[str, object]:
    skeleton = literal(primary_tree, "LCM_SKELETON")
    moments = literal(primary_tree, "MOMENTS")
    transitions = literal(primary_tree, "TRANSITIONS")
    clocks = literal(primary_tree, "LANDED_CLOCKS")
    independently_derived_gaps = tuple(
        moments[index + 1] - moments[index]
        for index in range(len(moments) - 1)
    )
    transition_gaps = tuple(
        row["right"] - row["left"] for row in transitions
    )
    residuals = tuple(
        gap - skeleton for gap in independently_derived_gaps
    )
    gcd_value = euclid(4464, 5952)
    lcm_value = 4464 // gcd_value * 5952
    clock_rows = tuple({
        "clock": clock,
        "quotient": skeleton // clock,
        "remainder": skeleton % clock,
        "divides_17856": skeleton % clock == 0,
    } for clock in clocks)
    factor_rows = {
        value: trial_factor(value)
        for value in (4464, 5952, skeleton, *residuals)
    }
    relation_hits = []
    for residual in residuals:
        for clock in clocks:
            if residual == clock:
                relation_hits.append(f"{residual}={clock}")
            if clock % residual == 0:
                relation_hits.append(f"{residual}|{clock}")
            if residual % clock == 0:
                relation_hits.append(f"{clock}|{residual}")
    exact = (
        skeleton == 17856
        and moments == (14744, 33195, 51115)
        and independently_derived_gaps == (18451, 17920)
        and transition_gaps == independently_derived_gaps
        and residuals == (595, 64)
        and tuple(row["residual"] for row in transitions) == residuals
        and gcd_value == 1488
        and lcm_value == skeleton
        and factor_rows == {
            4464: ((2, 4), (3, 2), (31, 1)),
            5952: ((2, 6), (3, 1), (31, 1)),
            17856: ((2, 6), (3, 2), (31, 1)),
            595: ((5, 1), (7, 1), (17, 1)),
            64: ((2, 6),),
        }
        and tuple(
            row["clock"] for row in clock_rows
            if row["divides_17856"]
        ) == (2, 3, 288, 4464, 5952, 8928)
        and tuple(
            row["clock"] for row in clock_rows
            if not row["divides_17856"]
        ) == (8930,)
        and relation_hits == ["2|64", "64|5952"]
    )
    return {
        "verdict": "PASS",
        "finding":
            "PASS: the gaps are exactly 17856+595 and 17856+64; "
            "17856=lcm(4464,5952); 8930 is the sole nondividing landed "
            "clock; 595=5*7*17 and 64=2^6, with only the thin landed "
            "divisibility hits 2|64 and 64|5952.",
        "moments": moments,
        "gaps": independently_derived_gaps,
        "decompositions": tuple(
            (gap, skeleton, residual)
            for gap, residual in zip(independently_derived_gaps, residuals)
        ),
        "gcd_4464_5952": gcd_value,
        "lcm_4464_5952": lcm_value,
        "factorizations": factor_rows,
        "clock_rows": clock_rows,
        "thin_relation_hits": relation_hits,
        "checker_pass": exact,
    }


def string_constants(node: ast.AST) -> frozenset[str]:
    return frozenset(
        child.value for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    )


def prediction_certificate(
    primary_tree: ast.Module,
    catalog: dict[str, object],
) -> dict[str, object]:
    skeleton = literal(primary_tree, "LCM_SKELETON")
    moments = literal(primary_tree, "MOMENTS")
    events = literal(primary_tree, "EVENTS")
    transitions = literal(primary_tree, "TRANSITIONS")
    base = moments[-1] + skeleton
    event3_predictions = {
        "TARGET_PARITY_LOOKUP": {
            "next_event": 3,
            "residual": 64,
            "predicted_next_cohort_moment": base + 64,
        },
        "ABS_EVENT_JUMP_LOOKUP": {
            "source_event": events[-1],
            "next_event": 3,
            "absolute_jump": abs(3 - events[-1]),
            "residual": 595,
            "predicted_next_cohort_moment": base + 595,
        },
    }
    candidate = function(primary_tree, "candidate_residual")
    prereg = function(primary_tree, "build_preregistration")
    residual = function(primary_tree, "residual_certificate")
    prediction = function(primary_tree, "prediction_certificate")
    runner = function(primary_tree, "run")
    constants = (
        string_constants(candidate)
        | string_constants(prereg)
        | string_constants(residual)
        | string_constants(prediction)
        | string_constants(runner)
    )
    formula_text = ast.unparse(candidate)
    formulas_exact = (
        "595 if target_event % 2 == 0 else 64" in formula_text
        and "{1: 64, 2: 595}.get(abs(target_event - source_event))"
        in formula_text
    )
    no_event3_observation = (
        len(transitions) == 2
        and all(row["target_event"] != 3 for row in transitions)
    )
    treated_as_predictions_not_tests = (
        "PRE_REGISTERED_CANDIDATE" in constants
        and "CANDIDATE_TWO_POINTS_CANNOT_PROVE" in constants
        and "PREDICTED_PRE_REGISTERED_AND_SURVIVED_B" in constants
        and no_event3_observation
    )
    vacuity_refuted = (
        catalog["lawful_events"] == (0, 1, 2, 3)
        and catalog["event3_open_key_count"] == 31
        and event3_predictions == {
            "TARGET_PARITY_LOOKUP": {
                "next_event": 3,
                "residual": 64,
                "predicted_next_cohort_moment": 69035,
            },
            "ABS_EVENT_JUMP_LOOKUP": {
                "source_event": 1,
                "next_event": 3,
                "absolute_jump": 2,
                "residual": 595,
                "predicted_next_cohort_moment": 69566,
            },
        }
    )
    exact = formulas_exact and treated_as_predictions_not_tests and vacuity_refuted
    return {
        "verdict": "FAIL",
        "finding":
            "FAIL: vacuous-at-k=2 is false because lawful event 3 already "
            "exists.  The live event-3 predictions conflict: parity predicts "
            "69035 while absolute-jump predicts 69566.  The primary does not "
            "test either against an event-3 observation; it labels both as "
            "pre-registered two-point candidates.",
        "prediction_base": base,
        "event3_predictions_now_live": event3_predictions,
        "event3_open_key_count": catalog["event3_open_key_count"],
        "source_candidate_formulas_exact": formulas_exact,
        "source_has_event3_observation": not no_event3_observation,
        "source_treats_predictions_as_testable_claims":
            not treated_as_predictions_not_tests,
        "source_prediction_bookkeeping_only":
            treated_as_predictions_not_tests,
        "vacuity_at_k2": False,
        "checker_pass": exact,
    }


def brute_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate for candidate in range(1, value + 1)
        if value % candidate == 0
    )


def orbit_word(
    core: Any,
    program: tuple[object, ...],
    pair: tuple[int, int],
) -> tuple[object, ...]:
    rows = []
    stations = len(program)
    for step in range(stations):
        live = {
            (pair[0] + step) % stations,
            (pair[1] + step) % stations,
        }
        for station, macro in enumerate(program):
            if station in live:
                rows.extend(core.mapped_macro(macro))
    return tuple(rows)


def compile_word(word: tuple[object, ...]) -> tuple[tuple[int, int, int, int], ...]:
    schedule = []
    for gate in word:
        if len(set(gate.wires)) != len(gate.wires):
            raise AssertionError(("repeated gate wire", gate))
        if gate.kind == "X":
            schedule.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            schedule.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            schedule.append(
                (2, gate.wires[0], gate.wires[1], gate.wires[2])
            )
        else:
            raise AssertionError(("non-reversible gate", gate))
    return tuple(schedule)


def scalar_apply(
    state: tuple[int, ...],
    schedule: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, ...]:
    result = list(state)
    for kind, first, second, third in schedule:
        if kind == 0:
            result[first] ^= 1
        elif kind == 1:
            result[second] ^= result[first]
        else:
            result[third] ^= result[first] & result[second]
    return tuple(result)


def packed_advance(
    columns: list[int],
    schedule: tuple[tuple[int, int, int, int], ...],
    lane_mask: int,
) -> None:
    for kind, first, second, third in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def recurrence_certificate(
    primary_tree: ast.Module,
    catalog: dict[str, object],
) -> dict[str, object]:
    sys.path.insert(0, str(ROOT / "scripts"))
    core_name = Path(CORE_PATH).stem
    core = __import__(core_name)
    banks = catalog["fixture_banks"]
    backbone = literal(primary_tree, "BACKBONE")
    skeleton = literal(primary_tree, "LCM_SKELETON")
    funnel_moments = literal(primary_tree, "FUNNEL_MOMENTS")
    bound = funnel_moments[0]
    all_candidates = brute_divisors(skeleton)
    tested_candidates = tuple(
        candidate for candidate in all_candidates if candidate <= bound
    )
    untestable = tuple(
        candidate for candidate in all_candidates if candidate > bound
    )

    program = core.interleaved_program(banks)
    representative_pair = backbone[0]
    word = orbit_word(core, program, representative_pair)
    schedule = compile_word(word)
    genesis_banks, genesis_links = core.B.chain_genesis(banks)
    genesis = core.M.pack_state(genesis_banks, genesis_links)
    prepared = core.M.prepare_endpoint(genesis, (1, 0))
    initial = scalar_apply(prepared, schedule)
    core_initial = core.A.apply_semantic(prepared, word)
    if initial != core_initial:
        raise AssertionError("independent scalar compiler disagrees at seed")

    lane_mask = 0b11
    columns = [lane_mask if bit else 0 for bit in initial]
    initial_columns = columns.copy()
    tested_set = set(tested_candidates)
    return_rows = []
    duplicate_exact_at_every_test = True
    for moment in range(1, bound + 1):
        packed_advance(columns, schedule, lane_mask)
        if moment in tested_set:
            duplicate_exact = all(
                column in (0, lane_mask) for column in columns
            )
            duplicate_exact_at_every_test &= duplicate_exact
            return_rows.append({
                "candidate_period": moment,
                "exact_return_to_initial": columns == initial_columns,
                "duplicate_lanes_exact": duplicate_exact,
            })
    hits = tuple(
        row["candidate_period"] for row in return_rows
        if row["exact_return_to_initial"]
    )
    lane0_at_bound = bytes(column & 1 for column in columns)
    primary_evolve = function(primary_tree, "evolve_funnels")
    primary_recurrence = function(primary_tree, "recurrence_certificate")
    evolve_text = ast.unparse(primary_evolve)
    recurrence_text = ast.unparse(primary_recurrence)
    primary_scope_exact = (
        "recurrence_candidates = divisors(LCM_SKELETON)" in evolve_text
        and "moment <= FUNNEL_MOMENTS[0]" in evolve_text
        and "untestable == (LCM_SKELETON,)" in recurrence_text
    )
    enumeration_exact = (
        trial_factor(skeleton) == ((2, 6), (3, 2), (31, 1))
        and len(all_candidates) == (6 + 1) * (2 + 1) * (1 + 1) == 42
        and len(tested_candidates) == 41
        and len(return_rows) == 41
        and tuple(row["candidate_period"] for row in return_rows)
        == tested_candidates
        and untestable == (17856,)
        and max(tested_candidates) == 8928
        and set(tested_candidates).isdisjoint(untestable)
        and tuple(sorted((*tested_candidates, *untestable)))
        == all_candidates
    )
    exact = (
        primary_scope_exact
        and enumeration_exact
        and not hits
        and duplicate_exact_at_every_test
        and sum(lane0_at_bound) == 44
        and len(program) == 11
        and len(schedule) == 6212
        and len(initial) == literal(primary_tree, "STATE_BITS") == 5815
    )
    return {
        "verdict": "PASS",
        "finding":
            "PASS: 17856 has exactly 42 positive divisors; the declared "
            "inclusive pre-funnel bound 14739 tests all 41 divisors at or "
            "below the bound, leaves only 17856 untestable, and an "
            "independent exact 5815-bit replay finds no return.",
        "representative_key": (0, representative_pair),
        "configuration": "full landed 5815-bit state",
        "program_stations": len(program),
        "word_gate_count": len(schedule),
        "candidate_divisors": all_candidates,
        "candidate_count": len(all_candidates),
        "pre_funnel_bound_inclusive": bound,
        "tested_divisors": tested_candidates,
        "tested_candidate_count": len(tested_candidates),
        "untestable_above_bound": untestable,
        "max_tested_divisor": max(tested_candidates),
        "no_silent_truncation": enumeration_exact,
        "exact_recurrence_hits": hits,
        "duplicate_lanes_exact_at_every_test":
            duplicate_exact_at_every_test,
        "independent_seed_equals_core_semantics": initial == core_initial,
        "state_at_bound_sha256": sha256(lane0_at_bound).hexdigest(),
        "state_at_bound_hamming_weight": sum(lane0_at_bound),
        "primary_declared_scope_exact": primary_scope_exact,
        "checker_pass": exact,
    }


def stable_output(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        lines = [
            (
                f"CERTIFICATE {name} {certificate['verdict']} "
                + compact(certificate)
            )
            for name, certificate in certificates.items()
        ]
        lines.append("SUMMARY_JSON " + compact(report))
        lines.append(str(report["terminal"]))
        output = "\n".join(lines) + "\n"
        size = len(output.encode())
        controls = certificates["E_CONTROLS"]
        if (
            report["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_evidence()
    primary_tree = sources["trees"][PRIMARY_PATH]
    core_tree = sources["trees"][CORE_PATH]
    if not isinstance(primary_tree, ast.Module):
        raise AssertionError("primary AST missing")
    if not isinstance(core_tree, ast.Module):
        raise AssertionError("core AST missing")

    certificate_a = catalog_certificate(primary_tree, core_tree)
    certificate_b = arithmetic_certificate(primary_tree)
    certificate_c = prediction_certificate(primary_tree, certificate_a)
    certificate_d = recurrence_certificate(primary_tree, certificate_a)
    elapsed = monotonic() - started
    evidence_payload = (
        certificate_a, certificate_b, certificate_c, certificate_d
    )
    evidence_digest_first = sha256(compact(evidence_payload).encode()).hexdigest()
    evidence_digest_second = sha256(compact(evidence_payload).encode()).hexdigest()
    blocked_loaded = tuple(
        name for name in BLOCKLISTED_PRIMARY_MODULES if name in sys.modules
    )
    controls_pass = (
        sources["pass"]
        and not blocked_loaded
        and not FIREWALL.hits
        and evidence_digest_first == evidence_digest_second
        and certificate_d["duplicate_lanes_exact_at_every_test"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificate_e = {
        "verdict": "PASS" if controls_pass else "FAIL",
        "finding": (
            "PASS: both literal worktree-relative inputs exist and match "
            "their SHA-256/Git-blob pins; Cycle-832/831 primaries remained "
            "text/AST-only and blocklisted; duplicate state lanes and "
            "canonical evidence renders are deterministic."
            if controls_pass else
            "FAIL: at least one source, blocklist, determinism, or runtime "
            "control failed."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": sources["AUDIT_INPUT_PATHS_literal"],
        "all_paths_existing": sources["all_paths_existing"],
        "all_paths_worktree_relative":
            sources["all_paths_worktree_relative"],
        "source_rows": sources["rows"],
        "blocklisted_primary_modules": BLOCKLISTED_PRIMARY_MODULES,
        "blocked_modules_loaded_at_end": blocked_loaded,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "dynamic_imports_from_audit_inputs": (Path(CORE_PATH).stem,),
        "primary_sources_executed": False,
        "evidence_sha256_first": evidence_digest_first,
        "evidence_sha256_second": evidence_digest_second,
        "canonical_evidence_deterministic":
            evidence_digest_first == evidence_digest_second,
        "duplicate_state_lanes_deterministic":
            certificate_d["duplicate_lanes_exact_at_every_test"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checker_pass": controls_pass,
    }
    certificates = {
        "A_THE_EXHAUSTION_CLAIM": certificate_a,
        "B_THE_ARITHMETIC": certificate_b,
        "C_THE_PREDICTION_BOOKKEEPING": certificate_c,
        "D_THE_RECURRENCE_PROBE": certificate_d,
        "E_CONTROLS": certificate_e,
    }
    checker_pass = all(
        certificate["checker_pass"] for certificate in certificates.values()
    )
    primary_refuted = (
        certificate_a["verdict"] == "FAIL"
        and certificate_c["verdict"] == "FAIL"
    )
    report = {
        "cycle": 832,
        "target": "backbone exhaustion and skeleton",
        "primary_verdict": "REFUTED" if primary_refuted else "NOT_REFUTED",
        "refutation":
            "k=2 has lawful event 3; backbone inventory is 36, not 27; "
            "event-3 predictions are live and disagree (69035 vs 69566).",
        "certificate_verdicts": {
            name: certificate["verdict"]
            for name, certificate in certificates.items()
        },
        "checker_pass": checker_pass,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "terminal": (
            "CYCLE832_MOMENT_LAW_INDEPENDENT_REFUTATION_PASS"
            if checker_pass and primary_refuted else
            "CYCLE832_MOMENT_LAW_INDEPENDENT_CHECK_FAIL"
        ),
    }
    output = stable_output(certificates, report)
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    certificate_e["checker_pass"] = controls_pass and stdout_ok
    certificate_e["verdict"] = (
        "PASS" if certificate_e["checker_pass"] else "FAIL"
    )
    checker_pass = all(
        certificate["checker_pass"] for certificate in certificates.values()
    )
    report["checker_pass"] = checker_pass
    report["terminal"] = (
        "CYCLE832_MOMENT_LAW_INDEPENDENT_REFUTATION_PASS"
        if checker_pass and primary_refuted else
        "CYCLE832_MOMENT_LAW_INDEPENDENT_CHECK_FAIL"
    )
    output = stable_output(certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE832_MOMENT_LAW_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if checker_pass and primary_refuted else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE832_MOMENT_LAW_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
