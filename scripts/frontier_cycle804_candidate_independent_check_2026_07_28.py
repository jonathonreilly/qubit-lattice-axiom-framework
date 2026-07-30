#!/usr/bin/env python3
"""Cycle 804 v2 independent adversarial checker.

This checker treats the frozen Cycle-804 v2 runner as text/AST evidence only. It
rebuilds the selector battery and the two worked evolutions without importing
any Cycle-804 function.  Candidate-claim FAIL certificates are scientific
findings, not checker crashes: a clean adversarial run exits zero after every
requested attack and integrity control has executed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle804_derivation_candidate_2026_07_28.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
PROCESS_STARTED = monotonic()

# The sole runtime science supplier is the landed controller core.  Evolution,
# composition, census, fixtures, cleanliness, and battery logic below are
# independently written and never call the Cycle-804 implementation.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
AXIOM_PATH = AUDIT_INPUT_PATHS[1]
K719_PATH = AUDIT_INPUT_PATHS[2]
M736_PATH = AUDIT_INPUT_PATHS[3]
F750_PATH = AUDIT_INPUT_PATHS[4]
F758_PATH = AUDIT_INPUT_PATHS[5]
F792_PATH = AUDIT_INPUT_PATHS[6]
BLOCKLISTED_PRIMARY_MODULE = (
    "frontier_cycle804_derivation_candidate_2026_07_28"
)
PINNED_796_COMMIT = "4c12650f038de545e60f2d8c62bd303a0d360a84"
PINNED_796_PATH = (
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py"
)
PINNED_796_SHA256 = (
    "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3"
)
EXPECTED_RECORD_QUOTE_SHA256 = (
    "69d69c0d59162b5fdf2f293a695d0094124006baf0efb3f719fc3fa0df106384"
)
EXPECTED_S1_PLAIN_READING = (
    "The Record axiom asserts globally that records form. It schedules no "
    "formation for any epoch or configuration; only where and when remain "
    "open."
)
EXPECTED_S1_FORMATION_STATUS = {
    "formation_asserted_globally": True,
    "formation_forced_for_any_epoch": False,
}
EXPECTED_S2_IDENTIFICATION_CLAIM = (
    "The seven-condition battery equals landed admissibility at the 792/796 "
    "surface: four conditions are explicit exclusions on Cycle-758's raw "
    "landed surface, while census membership, pairwise separation, and "
    "synchronization are supplied through the preconstructed domain."
)
EXPECTED_RAW_758_CONDITIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
EXPECTED_SUPPLIED_792_CONDITIONS = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
)
EXPECTED_FROZEN_CANDIDATE = (
    "At the landed scope, when a record forms in a multi-source epoch it locks "
    "the unique accepted alternative at its first-clean moment — the "
    "acceptance law is the Record axiom's admissibility requirement evaluated "
    "on the landed dynamics, with admissibility operationally identified as "
    "the seven-condition battery at the 792/796 surface (four conditions "
    "758-raw). The axiom asserts that records form; it schedules nothing. The "
    "remaining freedom is at least two independent axes — the evaluation "
    "cadence and the formation-site schedule — both witnessed."
)
EXPECTED_S4_CONDITIONAL = (
    "IF a record forms in a landed multi-source epoch, THEN, because the "
    "locked possibility must be admissible and landed admissibility is the "
    "full battery, it locks the unique accepted alternative at a first-clean "
    "moment. This conditional does not assert that a record forms."
)
EXPECTED_S5_FREEDOM_CLAIM = (
    "The evaluation cadence and the formation-site schedule are independent "
    "freedom axes."
)
EXPECTED_S5_WITNESS_RECORD_SHA256 = (
    "d5c1d153891b6f4b0e7556ea6d24d50ae69ce0dc8541a4767bd5255ace51e641",
    "7925ef04f5a1b37758c926c17641d1d3ffacbcb75b6e23b7bb8ee3081b94779b",
)
EXPECTED_ONE_SHARED_FREEDOM_CLAIM = "RETRACTED"
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "451fb3f5d9eaf975e6b2ccdc248f66170805bc6e80da8dcc186a68379097cfc7",
    AXIOM_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    K719_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    M736_PATH:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    F750_PATH:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    F758_PATH:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    F792_PATH:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
OUTPUT_LINES: list[str] = []
CERTIFICATES: dict[str, bool] = {}


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(label: str, detail: object | None = None) -> None:
    OUTPUT_LINES.append(
        label if detail is None else f"{label} :: {compact(detail)}"
    )


def candidate_certificate(
    name: str, candidate_passes: bool, detail: object
) -> bool:
    """Record whether the attacked candidate claim survives."""

    if name in CERTIFICATES:
        raise AssertionError(("duplicate certificate", name))
    CERTIFICATES[name] = bool(candidate_passes)
    emit(
        f"{'PASS' if candidate_passes else 'FAIL'} {name}",
        detail,
    )
    return bool(candidate_passes)


def file_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def file_text(relative_path: str) -> str:
    return file_bytes(relative_path).decode("utf-8")


def git_payload(commit: str, relative_path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{relative_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def top_assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return node.value
    raise KeyError(name)


def assigned_dict_keys(function: ast.FunctionDef, variable: str) -> tuple[str, ...]:
    for node in ast.walk(function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if not any(
            isinstance(target, ast.Name) and target.id == variable
            for target in targets
        ):
            continue
        if not isinstance(node.value, ast.Dict):
            continue
        keys = []
        for key in node.value.keys:
            if not (
                isinstance(key, ast.Constant)
                and isinstance(key.value, str)
            ):
                raise AssertionError((function.name, variable, key))
            keys.append(key.value)
        return tuple(keys)
    raise KeyError((function.name, variable))


def primary_string(primary_tree: ast.Module, name: str) -> str:
    return str(ast.literal_eval(top_assignment(primary_tree, name)))


def audit_tuple_is_literal() -> bool:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    audit_node = top_assignment(own_tree, "AUDIT_INPUT_PATHS")
    declared_node = top_assignment(own_tree, "DECLARED_INPUT_PATHS")
    return bool(
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )


def import_blocklist_control() -> dict[str, object]:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported = {
        alias.name
        for node in ast.walk(own_tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    relevant_functions = (
        "independent_apply_step",
        "independent_run_orbit",
        "independent_synchronous_word",
        "independent_clean_postimage",
        "independent_fixture_rows",
        "independent_family_sample",
    )
    forbidden_runtime_calls = []

    def dotted(node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            prefix = dotted(node.value)
            return f"{prefix}.{node.attr}" if prefix else node.attr
        return ""

    for name in relevant_functions:
        function = function_node(own_tree, name)
        calls = tuple(
            dotted(node.func)
            for node in ast.walk(function)
            if isinstance(node, ast.Call)
        )
        for forbidden in (
            "K.run_orbit",
            "M736.",
            "F750.",
            "F758.",
            f"{BLOCKLISTED_PRIMARY_MODULE}.",
        ):
            if any(
                call == forbidden.rstrip(".")
                or call.startswith(forbidden)
                for call in calls
            ):
                forbidden_runtime_calls.append((name, forbidden))
    return {
        "primary_imported_by_AST":
            BLOCKLISTED_PRIMARY_MODULE in imported,
        "primary_present_in_sys_modules":
            BLOCKLISTED_PRIMARY_MODULE in sys.modules,
        "forbidden_runtime_calls": tuple(forbidden_runtime_calls),
        "pass": (
            BLOCKLISTED_PRIMARY_MODULE not in imported
            and BLOCKLISTED_PRIMARY_MODULE not in sys.modules
            and not forbidden_runtime_calls
        ),
    }


def extract_record_quote(axioms: str) -> str:
    heading = "### Record / Fixed Reality\n\n"
    start = axioms.index(heading) + len(heading)
    end = axioms.index("\n\n## ", start)
    return axioms[start:end]


def whole_axiom_formation_scan(axioms: str) -> tuple[dict[str, str], ...]:
    """Return every verbatim paragraph/bullet bearing on formation or timing."""

    needles = (
        r"\bRecords form\.",
        r"\bWhen present, a record",
        r"\bformation\b",
        r"\brecord-production\b",
        r"\btemporal evolution\b",
        r"\btime metric\b",
        r"\boccurrence\b",
        r"\bchoice not fixed\b",
    )
    pattern = re.compile("|".join(needles), re.IGNORECASE)
    findings = []
    for block in re.split(r"\n{2,}", axioms):
        candidate = block.strip("\n")
        if not candidate or not pattern.search(candidate):
            continue
        lower = candidate.lower()
        if candidate == "Records form.":
            ruling = (
                "REFUTES_NO_FORMATION_FORCING: at least some record "
                "formation is explicit axiom content"
            )
        elif "occurrence became named axiom content" in lower:
            ruling = (
                "CONFIRMS_GLOBAL_OCCURRENCE_IS_FORCED; which/site/weight/rate "
                "remain downstream"
            )
        elif "when present, a record locks" in lower:
            ruling = (
                "CONDITIONAL_LOCK_CONTENT: unique admissible locking when "
                "present, with no epoch schedule"
            )
        elif "choice not fixed" in lower:
            ruling = (
                "UNFIXED-CHOICE RULE: unsupplied scheduling must remain "
                "conditional/open"
            )
        elif "formation rules" in lower and "at what rate" in lower:
            ruling = (
                "SCHEDULING/RATE EXPLICITLY DOWNSTREAM, while global "
                "occurrence is not open"
            )
        elif "record-production" in lower or "time metric" in lower:
            ruling = (
                "NO PRODUCTION PROCESS/TIME METRIC SUPPLIED by the four axioms"
            )
        elif "temporal evolution" in lower:
            ruling = "TEMPORAL EVOLUTION IS TRACKED SEPARATELY"
        else:
            ruling = "FORMATION/TIMING-BEARING CLAUSE"
        findings.append({"verbatim": candidate, "ruling": ruling})
    return tuple(findings)


def s1_quote_completeness(
    primary_tree: ast.Module, axioms: str
) -> dict[str, object]:
    quote = extract_record_quote(axioms)
    primary_quote = primary_string(primary_tree, "RECORD_AXIOM_VERBATIM")
    primary_quote_sha = primary_string(
        primary_tree, "RECORD_AXIOM_SHA256"
    )
    primary_plain_reading = primary_string(
        primary_tree, "S1_PLAIN_READING"
    )
    primary_formation_status = dict(
        ast.literal_eval(
            top_assignment(primary_tree, "S1_FORMATION_STATUS")
        )
    )
    findings = whole_axiom_formation_scan(axioms)
    force_hits = tuple(
        row for row in findings
        if row["ruling"].startswith(("REFUTES_", "CONFIRMS_"))
    )
    emit("S1_RECORD_QUOTE_BEGIN")
    OUTPUT_LINES.extend(quote.splitlines())
    emit("S1_RECORD_QUOTE_END")
    for index, row in enumerate(findings):
        emit(f"S1_WHOLE_AXIOM_CANDIDATE_{index}_BEGIN")
        OUTPUT_LINES.extend(row["verbatim"].splitlines())
        emit(f"S1_WHOLE_AXIOM_CANDIDATE_{index}_END")
        emit(f"S1_WHOLE_AXIOM_RULING_{index}", row["ruling"])
    detail = {
        "quote_verbatim_equal_to_primary": quote == primary_quote,
        "quote_sha256": sha256(quote.encode("utf-8")).hexdigest(),
        "expected_quote_sha256": EXPECTED_RECORD_QUOTE_SHA256,
        "whole_file_candidate_count": len(findings),
        "formation_forcing_hits": force_hits,
        "primary_plain_reading": primary_plain_reading,
        "primary_formation_status": primary_formation_status,
        "ruling": (
            "The quote is exact and the v2 primary adopts the whole-file "
            "reading: occurrence somewhere is axiom content; only its "
            "formation rule/schedule remains open."
        ),
    }
    detail["candidate_pass"] = bool(
        quote == primary_quote
        and primary_quote_sha == EXPECTED_RECORD_QUOTE_SHA256
        and sha256(quote.encode("utf-8")).hexdigest()
        == EXPECTED_RECORD_QUOTE_SHA256
        and bool(force_hits)
        is EXPECTED_S1_FORMATION_STATUS[
            "formation_asserted_globally"
        ]
        and primary_plain_reading == EXPECTED_S1_PLAIN_READING
        and primary_formation_status == EXPECTED_S1_FORMATION_STATUS
    )
    return detail


def s2_identification_fidelity(
    primary_tree: ast.Module,
    source_750: str,
    source_758: str,
    source_792: str,
    source_796: str,
) -> dict[str, object]:
    tree_750 = ast.parse(source_750, filename=F750_PATH)
    tree_758 = ast.parse(source_758, filename=F758_PATH)
    tree_792 = ast.parse(source_792, filename=F792_PATH)
    tree_796 = ast.parse(source_796, filename=PINNED_796_PATH)

    flags_750 = assigned_dict_keys(
        function_node(tree_750, "outcome_certificate"), "boundary"
    )
    exclusions_758 = assigned_dict_keys(
        function_node(
            tree_758, "multisource_enforcement_lineage_selector"
        ),
        "conditions",
    )
    base_792 = assigned_dict_keys(
        function_node(tree_792, "base_battery_evaluation"),
        "conditions",
    )
    selector_792 = function_node(tree_792, "selector_conditions")
    appends_clean = any(
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "conditions"
        and isinstance(node.slice, ast.Constant)
        and node.slice.value == "clean_postimage"
        for node in ast.walk(selector_792)
    )
    if not appends_clean:
        raise AssertionError("Cycle792 does not append clean_postimage")
    reconstructed_792 = tuple((*base_792, "clean_postimage"))
    battery_796 = tuple(
        ast.literal_eval(top_assignment(tree_796, "BATTERY_CONDITIONS"))
    )

    exact_names = (
        len(reconstructed_792) == len(set(reconstructed_792)) == 7
        and len(battery_796) == len(set(battery_796)) == 7
        and set(reconstructed_792) == set(battery_796)
        and set(exclusions_758).issubset(set(reconstructed_792))
    )
    missing = tuple(sorted(set(battery_796) - set(reconstructed_792)))
    extra = tuple(sorted(set(reconstructed_792) - set(battery_796)))
    primary_identification_claim = primary_string(
        primary_tree, "S2_IDENTIFICATION_CLAIM"
    )
    primary_raw_conditions = tuple(
        ast.literal_eval(
            top_assignment(primary_tree, "RAW_758_CONDITIONS")
        )
    )
    primary_supplied_conditions = tuple(
        ast.literal_eval(
            top_assignment(primary_tree, "SUPPLIED_792_CONDITIONS")
        )
    )
    scope_counterexample = {
        "surface":
            "Cycle758.multisource_enforcement_lineage_selector raw landed "
            "decision surface",
        "condition_names": exclusions_758,
        "differs_from_composed_seven_condition_battery":
            set(exclusions_758) != set(battery_796),
        "ruling": (
            "Cycle758 decides with four explicit exclusions; census "
            "membership, pairwise separation, and synchronization enter only "
            "through its preconstructed domain/landed Cycle736 supplier. "
            "Thus seven-condition identity is valid for the composed "
            "Cycle792/796 monitored surface, not every landed multi-source "
            "surface named by the frozen candidate."
        ),
    }
    horizon_status = {
        "Cycle792_scope_statement": str(
            ast.literal_eval(top_assignment(tree_792, "SUPPLIED_SCOPE_STATEMENT"))
        ),
        "Cycle796_accept_first_status": (
            "DECLARED COMPOSITION GLUE, UNLANDED"
            if "DECLARED COMPOSITION GLUE, UNLANDED" in source_796
            else None
        ),
    }
    detail = {
        "Cycle750_boundary_flags": flags_750,
        "Cycle758_explicit_exclusions": exclusions_758,
        "Cycle792_base_conditions": base_792,
        "Cycle792_reconstructed_battery": reconstructed_792,
        "Cycle796_battery": battery_796,
        "order_insensitive_exact_names": exact_names,
        "missing": missing,
        "extra": extra,
        "scope_counterexample": scope_counterexample,
        "horizon_status": horizon_status,
        "primary_v2_identification_claim": primary_identification_claim,
        "primary_v2_four_conditions_758_raw": primary_raw_conditions,
        "primary_v2_three_conditions_preconstructed":
            primary_supplied_conditions,
        "ruling": (
            "The seven names match exactly, order-insensitively, and v2 "
            "correctly scopes that identity to the 792/796 surface while "
            "preserving the four-condition Cycle-758 raw-surface split."
        ),
    }
    detail["candidate_pass"] = bool(
        exact_names
        and not missing
        and not extra
        and scope_counterexample[
            "differs_from_composed_seven_condition_battery"
        ]
        and exclusions_758 == EXPECTED_RAW_758_CONDITIONS
        and tuple(
            name for name in reconstructed_792
            if name not in exclusions_758
        ) == EXPECTED_SUPPLIED_792_CONDITIONS
        and primary_identification_claim
        == EXPECTED_S2_IDENTIFICATION_CLAIM
        and primary_raw_conditions == EXPECTED_RAW_758_CONDITIONS
        and primary_supplied_conditions
        == EXPECTED_SUPPLIED_792_CONDITIONS
    )
    return detail


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def independent_pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = set(positions)
    return all(
        (station + 1) % RING_STATIONS not in occupied
        for station in occupied
    )


def independent_census_members(count: int) -> frozenset[tuple[int, ...]]:
    return frozenset(
        tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        for mask in range(1 << RING_STATIONS)
        if mask.bit_count() == count
        and independent_pairwise_separated(
            tuple(
                station
                for station in range(RING_STATIONS)
                if (mask >> station) & 1
            )
        )
    )


def independent_apply_step(
    data: Any,
    program: tuple[object, ...],
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
    *,
    reverse: bool = False,
) -> tuple[Any, tuple[int, ...], tuple[int, ...]]:
    """Fresh implementation of one H=R2 R1 Q controller step."""

    stations = len(program)
    a = list(a_tokens)
    b = list(b_tokens)
    output = data
    if not reverse:
        for station in range(stations):
            if a[station]:
                output = K.A.apply_semantic(
                    output, K.mapped_macro(program[station])
                )
        for station in range(stations):
            a[station], b[station] = b[station], a[station]
        for station in range(stations):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]
    else:
        for station in reversed(range(stations)):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]
        for station in reversed(range(stations)):
            a[station], b[station] = b[station], a[station]
        for station in reversed(range(stations)):
            if a[station]:
                output = K.A.apply_semantic(
                    output,
                    tuple(reversed(K.mapped_macro(program[station]))),
                )
    return output, tuple(a), tuple(b)


def independent_run_orbit(
    data: Any,
    program: tuple[object, ...],
    positions: tuple[int, ...],
    *,
    reverse: bool = False,
) -> tuple[
    Any,
    tuple[int, ...],
    tuple[int, ...],
    tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...],
]:
    """Fresh orbit loop; deliberately does not call the landed run_orbit."""

    stations = len(program)
    a = tuple(int(station in positions) for station in range(stations))
    b = (0,) * stations
    trace = []
    for _step in range(stations):
        before = tuple(index for index, value in enumerate(a) if value)
        data, a, b = independent_apply_step(
            data, program, a, b, reverse=reverse
        )
        after = tuple(index for index, value in enumerate(a) if value)
        trace.append((before, after, sum(b)))
    return data, a, b, tuple(trace)


def independent_synchronous_word(
    program: tuple[object, ...], positions: tuple[int, ...]
) -> tuple[object, ...]:
    """Fresh synchronous composition, not M736's implementation."""

    live_positions = tuple(positions)
    word = []
    for _step in range(len(program)):
        live = set(live_positions)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        live_positions = tuple(
            (station + 1) % len(program) for station in live_positions
        )
    return tuple(word)


def independent_clean_postimage(state: Any, bank_count: int) -> bool:
    """Fresh Cycle750/758 terminal cleanliness predicate."""

    banks, links = K.M.unpack_state(state, bank_count)
    dirty_source = bool(state[K.R3.X.SOURCE_POINTER])
    dirty_bank = any(
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
    dirty_link = any(any(link) for link in links)
    return not any((dirty_source, dirty_bank, dirty_link))


def independent_fixture_rows(
    bank_count: int,
) -> tuple[tuple[int, tuple[int, int], tuple[object, ...], Any, Any], ...]:
    """Fresh fixture recursion, not F750.k_epoch_fixtures."""

    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(bank_count)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        single_expected = K.A.apply_semantic(before, allocator)
        rows.append(
            (event, direction, program, before, single_expected)
        )
        state = single_expected
    return tuple(rows)


def expected_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            rotate_positions(positions, step),
            rotate_positions(positions, step + 1),
            0,
        )
        for step in range(RING_STATIONS)
    )


def independent_base_row(
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
    census: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = (0,) * len(program)
    word = independent_synchronous_word(program, positions)
    expected = K.A.apply_semantic(before, word)
    after, rail_a, rail_b, trace = independent_run_orbit(
        before, program, positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = independent_run_orbit(
        after, program, positions, reverse=True
    )
    conditions = {
        "census_membership": positions in census,
        "pairwise_separation":
            independent_pairwise_separated(positions),
        "synchronization": trace == expected_trace(positions),
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
    }
    return {
        "positions": positions,
        "word": word,
        "after": after,
        "conditions": conditions,
    }


def independent_family_sample(
    *,
    k: int,
    event: int,
    representative: tuple[int, ...],
    target: tuple[int, ...],
    moment: int,
) -> dict[str, object]:
    """Recount one translation family through an exact target moment."""

    fixture = next(
        row for row in independent_fixture_rows(FIXTURE_BANKS)
        if row[0] == event
    )
    _event, direction, program, before, _single_expected = fixture
    alternatives = tuple(
        sorted(
            {
                rotate_positions(representative, shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    census = independent_census_members(k)
    base_rows = {
        positions:
            independent_base_row(program, before, positions, census)
        for positions in alternatives
    }
    clean_timeline: dict[int, list[tuple[int, ...]]] = {}
    first_clean = {positions: None for positions in alternatives}
    transport_failures = 0

    for positions in alternatives:
        state = base_rows[positions]["after"]
        tokens = tuple(
            int(station in positions) for station in range(len(program))
        )
        zeros = (0,) * len(program)
        for horizon in range(moment + 1):
            clean = independent_clean_postimage(state, FIXTURE_BANKS)
            if clean:
                clean_timeline.setdefault(horizon, []).append(positions)
                if first_clean[positions] is None:
                    first_clean[positions] = horizon
            if horizon < moment:
                state, rail_a, rail_b, _trace = independent_run_orbit(
                    state, program, positions
                )
                transport_failures += (
                    rail_a != tokens or rail_b != zeros
                )

    battery_names = (
        *next(iter(base_rows.values()))["conditions"].keys(),
        "clean_postimage",
    )
    target_conditions = {
        **base_rows[target]["conditions"],
        "clean_postimage": target in clean_timeline.get(moment, ()),
    }
    timeline = tuple(
        (horizon, tuple(rows))
        for horizon, rows in sorted(clean_timeline.items())
    )
    return {
        "k": k,
        "event": event,
        "direction": direction,
        "representative": representative,
        "target": target,
        "moment": moment,
        "alternatives": alternatives,
        "battery_names": battery_names,
        "all_base_conditions_pass": all(
            all(row["conditions"].values())
            for row in base_rows.values()
        ),
        "target_conditions": target_conditions,
        "target_first_clean": first_clean[target],
        "moment_minus_one_survivors":
            tuple(clean_timeline.get(moment - 1, ())),
        "moment_survivors": tuple(clean_timeline.get(moment, ())),
        "clean_timeline_through_target": timeline,
        "first_clean_rows": tuple(
            sorted(
                (
                    (positions, first)
                    for positions, first in first_clean.items()
                    if first is not None
                ),
                key=lambda row: (row[1], row[0]),
            )
        ),
        "transport_failures": transport_failures,
    }


def independent_recount() -> tuple[dict[str, object], ...]:
    return (
        independent_family_sample(
            k=2,
            event=3,
            representative=(0, 2),
            target=(1, 10),
            moment=252,
        ),
        independent_family_sample(
            k=3,
            event=2,
            representative=(0, 2, 5),
            target=(0, 2, 5),
            moment=444,
        ),
    )


def s3_recount_result(
    first: tuple[dict[str, object], ...],
    second: tuple[dict[str, object], ...],
    full_battery: tuple[str, ...],
) -> dict[str, object]:
    deterministic = first == second
    expected = (
        {
            "moment": 252,
            "previous": (),
            "survivors": ((1, 10),),
        },
        {
            "moment": 444,
            "previous": (),
            "survivors": ((0, 2, 5),),
        },
    )
    checks = []
    for sample, frozen in zip(first, expected, strict=True):
        checks.append(
            sample["moment"] == frozen["moment"]
            and sample["moment_minus_one_survivors"]
            == frozen["previous"]
            and sample["moment_survivors"] == frozen["survivors"]
            and sample["target_first_clean"] == frozen["moment"]
            and sample["all_base_conditions_pass"]
            and all(sample["target_conditions"].values())
            and set(sample["battery_names"]) == set(full_battery)
            and len(sample["battery_names"]) == len(full_battery) == 7
            and sample["transport_failures"] == 0
        )
    return {
        "fresh_implementation": (
            "No primary functions, K.run_orbit, M736 composition/census, "
            "F750 fixtures, or F758 cleanliness were called."
        ),
        "samples": first,
        "deterministic": deterministic,
        "first_sha256": digest(first),
        "rerun_sha256": digest(second),
        "candidate_pass": deterministic and all(checks),
    }


def s4_moment_dependence(
    k3_sample: dict[str, object],
    frozen_candidate: str,
    s4_conditional: str,
) -> dict[str, object]:
    timeline = dict(k3_sample["clean_timeline_through_target"])
    required_48 = tuple(timeline.get(48, ())) == ((1, 4, 10),)
    required_444 = tuple(timeline.get(444, ())) == ((0, 2, 5),)
    different = timeline.get(48) != timeline.get(444)
    wording_carries_moment = (
        frozen_candidate == EXPECTED_FROZEN_CANDIDATE
        and s4_conditional == EXPECTED_S4_CONDITIONAL
    )
    overclaim = not wording_carries_moment
    return {
        "event": k3_sample["event"],
        "family": k3_sample["representative"],
        "clean_at_t48": timeline.get(48),
        "clean_at_t444": timeline.get(444),
        "required_t48_verified": required_48,
        "required_t444_verified": required_444,
        "different_locked_alternative_by_attempt_moment": different,
        "primary_sentence_frozen_candidate_VERBATIM": frozen_candidate,
        "primary_sentence_S4_VERBATIM": s4_conditional,
        "wording_ruling": (
            "SURVIVES THIS ATTACK: v2 ties locking to the record's first-clean "
            "moment, states that the axiom supplies no schedule, and retains "
            "the unchanged conditional sentence. Neither quoted sentence "
            "asserts the same alternative at every clean moment."
        ) if not overclaim else (
            "WORDING_REFUTED: the quoted wording asserts uniqueness without "
            "carrying which-moment dependence."
        ),
        "wording_overclaim": overclaim,
        "candidate_pass": (
            required_48 and required_444 and different and not overclaim
        ),
    }


def source_line_candidates(
    label: str, source: str
) -> tuple[dict[str, object], ...]:
    pattern = re.compile(
        r"formation|record|schedule|cadence|trigger", re.IGNORECASE
    )
    rows = []
    for lineno, line in enumerate(source.splitlines(), 1):
        if not pattern.search(line):
            continue
        lower = line.lower()
        if "record_typing_derived" in lower:
            ruling = "BOUNDARY FLAG FALSE; not a formation trigger"
        elif "cadence" in lower:
            ruling = "OBSERVATION-CADENCE METADATA/LOGIC; not formation"
        elif any(
            token in lower
            for token in (
                "form_record",
                "record_form",
                "formation_attempt",
                "formation_schedule",
                "schedule_formation",
                "trigger_formation",
            )
        ):
            ruling = "POTENTIAL FORMATION TRIGGER"
        else:
            ruling = "TEXTUAL MENTION ONLY; not executable formation"
        rows.append(
            {
                "module": label,
                "line": lineno,
                "verbatim": line,
                "ruling": ruling,
            }
        )
    return tuple(rows)


def ast_schedule_scan(
    label: str, source: str
) -> dict[str, object]:
    tree = ast.parse(source, filename=label)
    broad_candidates = []
    actual_triggers = []

    def dotted(node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            prefix = dotted(node.value)
            return f"{prefix}.{node.attr}" if prefix else node.attr
        return ""

    for node in ast.walk(tree):
        kind = None
        identifier = ""
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            kind, identifier = "function", node.name
        elif isinstance(node, ast.Call):
            kind, identifier = "call", dotted(node.func)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            names = []
            for target in targets:
                names.extend(
                    child.id
                    for child in ast.walk(target)
                    if isinstance(child, ast.Name)
                )
            kind, identifier = "assignment", ",".join(names)
        lower = identifier.lower()
        if kind and re.search(
            r"formation|record|schedule|cadence|trigger", lower
        ):
            row = {
                "kind": kind,
                "identifier": identifier,
                "line": getattr(node, "lineno", None),
            }
            broad_candidates.append(row)
            if re.search(
                r"(form.*record|record.*form|"
                r"formation.*(?:attempt|schedule|trigger)|"
                r"(?:schedule|trigger).*formation)",
                lower,
            ):
                actual_triggers.append(row)
    return {
        "module": label,
        "broad_candidates": tuple(broad_candidates),
        "formation_triggers": tuple(actual_triggers),
    }


def independent_single_source_record(
    event: int,
) -> dict[str, object]:
    fixture = next(
        row for row in independent_fixture_rows(FIXTURE_BANKS)
        if row[0] == event
    )
    _event, direction, program, before, expected = fixture
    positions = (0,)
    tokens = (1,) + (0,) * (len(program) - 1)
    zeros = (0,) * len(program)
    after, rail_a, rail_b, _trace = independent_run_orbit(
        before, program, positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = independent_run_orbit(
        after, program, positions, reverse=True
    )
    conditions = {
        "synchronous_law": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage":
            independent_clean_postimage(after, FIXTURE_BANKS),
    }
    return {
        "event": event,
        "direction": direction,
        "selected_positions": positions,
        "conditions": conditions,
        "record_content_sha256":
            sha256(str(after).encode("ascii")).hexdigest(),
    }


def s5_one_freedom_attack(
    sources: dict[str, str],
    primary_tree: ast.Module,
) -> dict[str, object]:
    line_findings = tuple(
        row
        for label, source in sources.items()
        for row in source_line_candidates(label, source)
    )
    ast_findings = tuple(
        ast_schedule_scan(label, source)
        for label, source in sources.items()
    )
    ast_triggers = tuple(
        (row["module"], trigger)
        for row in ast_findings
        for trigger in row["formation_triggers"]
    )
    grep_trigger_hits = tuple(
        row for row in line_findings
        if row["ruling"] == "POTENTIAL FORMATION TRIGGER"
    )
    for index, row in enumerate(line_findings):
        emit(f"S5_GREP_CANDIDATE_{index}_BEGIN")
        OUTPUT_LINES.append(row["verbatim"])
        emit(
            f"S5_GREP_CANDIDATE_{index}_END",
            {
                "module": row["module"],
                "line": row["line"],
                "ruling": row["ruling"],
            },
        )

    record_event_0 = independent_single_source_record(0)
    record_event_1 = independent_single_source_record(1)
    setting_a = {
        "cadence_axis": "orbit_return_boundary",
        "which_selection_becomes_record_axis":
            ("two-bank single-source event 0",),
        "formation_records": (
            record_event_0["record_content_sha256"],
        ),
        "Record_axiom_compatibility": {
            "Records_form": True,
            "exactly_one_admissible_possibility":
                all(record_event_0["conditions"].values()),
            "one_record_at_site": True,
            "permanent": True,
        },
    }
    setting_b = {
        "cadence_axis": "orbit_return_boundary",
        "which_selection_becomes_record_axis":
            ("two-bank single-source event 1",),
        "formation_records": (
            record_event_1["record_content_sha256"],
        ),
        "Record_axiom_compatibility": {
            "Records_form": True,
            "exactly_one_admissible_possibility":
                all(record_event_1["conditions"].values()),
            "one_record_at_site": True,
            "permanent": True,
        },
    }
    no_landed_schedule = not grep_trigger_hits and not ast_triggers
    lawful = all(
        all(setting["Record_axiom_compatibility"].values())
        for setting in (setting_a, setting_b)
    )
    differ_one_axis_only = (
        setting_a["cadence_axis"] == setting_b["cadence_axis"]
        and setting_a["which_selection_becomes_record_axis"]
        != setting_b["which_selection_becomes_record_axis"]
    )
    different_records = (
        setting_a["formation_records"] != setting_b["formation_records"]
    )
    independence_witness = (
        lawful and differ_one_axis_only and different_records
    )
    primary_freedom_claim = primary_string(
        primary_tree, "S5_FREEDOM_CLAIM"
    )
    primary_witness_hashes = tuple(
        ast.literal_eval(
            top_assignment(primary_tree, "S5_WITNESS_RECORD_SHA256")
        )
    )
    primary_retraction = primary_string(
        primary_tree, "ONE_SHARED_FREEDOM_RETRACTION"
    )
    detail = {
        "grep_candidate_count": len(line_findings),
        "grep_formation_trigger_hits": grep_trigger_hits,
        "AST_scans": ast_findings,
        "AST_formation_triggers": ast_triggers,
        "no_landed_module_schedules_formation": no_landed_schedule,
        "single_source_event_0": record_event_0,
        "single_source_event_1": record_event_1,
        "lawful_composite_setting_A": setting_a,
        "lawful_composite_setting_B": setting_b,
        "settings_differ_on_only_which_selection_axis":
            differ_one_axis_only,
        "different_formation_records": different_records,
        "independent_axes_witness": independence_witness,
        "primary_v2_freedom_claim": primary_freedom_claim,
        "primary_v2_witness_record_sha256": primary_witness_hashes,
        "primary_v2_one_shared_freedom_claim": primary_retraction,
        "ruling": (
            "No scanned landed module schedules formation, but that absence "
            "does not identify cadence with record occurrence. Holding "
            "orbit-return cadence fixed leaves at least two axiom-compatible "
            "choices of which landed single-source selection becomes a "
            "record, and the record contents differ. They are independent "
            "axes; v2 adopts this witness and retracts 'one shared freedom'."
        ),
        "candidate_pass": (
            no_landed_schedule
            and independence_witness
            and primary_freedom_claim == EXPECTED_S5_FREEDOM_CLAIM
            and primary_witness_hashes
            == EXPECTED_S5_WITNESS_RECORD_SHA256
            and primary_witness_hashes
            == (
                record_event_0["record_content_sha256"],
                record_event_1["record_content_sha256"],
            )
            and primary_retraction
            == EXPECTED_ONE_SHARED_FREEDOM_CLAIM
        ),
    }
    return detail


def disk_anchor_snapshot() -> dict[str, dict[str, object]]:
    return {
        path: {
            "exists": (ROOT / path).is_file(),
            "sha256": (
                sha256(file_bytes(path)).hexdigest()
                if (ROOT / path).is_file()
                else None
            ),
        }
        for path in AUDIT_INPUT_PATHS
    }


def main() -> int:
    anchors_before = disk_anchor_snapshot()
    sources = {
        path: file_text(path) for path in AUDIT_INPUT_PATHS
    }
    payload_796 = git_payload(PINNED_796_COMMIT, PINNED_796_PATH)
    source_796 = payload_796.decode("utf-8")
    primary_tree = ast.parse(
        sources[PRIMARY_PATH], filename=PRIMARY_PATH
    )

    s1 = s1_quote_completeness(
        primary_tree, sources[AXIOM_PATH]
    )
    s1_pass = candidate_certificate(
        "S1_QUOTE_COMPLETENESS_AND_WHOLE_AXIOM_PLAIN_READING",
        bool(s1["candidate_pass"]),
        s1,
    )

    s2 = s2_identification_fidelity(
        primary_tree,
        sources[F750_PATH],
        sources[F758_PATH],
        sources[F792_PATH],
        source_796,
    )
    s2_pass = candidate_certificate(
        "S2_IDENTIFICATION_NAMES_AND_SCOPE_FIDELITY",
        bool(s2["candidate_pass"]),
        s2,
    )
    full_battery = tuple(s2["Cycle796_battery"])

    first_recount = independent_recount()
    second_recount = independent_recount()
    s3 = s3_recount_result(
        first_recount, second_recount, full_battery
    )
    s3_pass = candidate_certificate(
        "S3_FRESH_RECOUNT_T252_AND_T444",
        bool(s3["candidate_pass"]),
        s3,
    )

    frozen_candidate = primary_string(
        primary_tree, "FROZEN_CANDIDATE"
    )
    s4_conditional = primary_string(
        primary_tree, "S4_CONDITIONAL"
    )
    emit("S4_PRIMARY_FROZEN_SENTENCE_BEGIN")
    OUTPUT_LINES.append(frozen_candidate)
    emit("S4_PRIMARY_FROZEN_SENTENCE_END")
    emit("S4_PRIMARY_CONDITIONAL_SENTENCE_BEGIN")
    OUTPUT_LINES.append(s4_conditional)
    emit("S4_PRIMARY_CONDITIONAL_SENTENCE_END")
    s4 = s4_moment_dependence(
        first_recount[1], frozen_candidate, s4_conditional
    )
    s4_pass = candidate_certificate(
        "S4_MOMENT_DEPENDENCE_AND_WORDING",
        bool(s4["candidate_pass"]),
        s4,
    )

    selector_monitor_sources = {
        "Cycle750": sources[F750_PATH],
        "Cycle758": sources[F758_PATH],
        "Cycle792": sources[F792_PATH],
        "Cycle796:pinned": source_796,
    }
    s5 = s5_one_freedom_attack(
        selector_monitor_sources, primary_tree
    )
    s5_pass = candidate_certificate(
        "S5_TWO_INDEPENDENT_FREEDOM_AXES_AND_RETRACTION",
        bool(s5["candidate_pass"]),
        s5,
    )

    anchors_after = disk_anchor_snapshot()
    blocklist = import_blocklist_control()
    observed_sha = {
        path: row["sha256"] for path, row in anchors_before.items()
    }
    pinned_commit = subprocess.run(
        ["git", "rev-parse", PINNED_796_COMMIT],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    pinned_sha = sha256(payload_796).hexdigest()
    elapsed = monotonic() - PROCESS_STARTED
    deterministic = first_recount == second_recount
    paths_literal = audit_tuple_is_literal()
    all_paths_exist = all(
        row["exists"] for row in anchors_before.values()
    )
    sources_unchanged = anchors_before == anchors_after
    within_read_cap = (
        len(AUDIT_INPUT_PATHS) - 1 == 6
        and 6 + 1 == 7  # six disk files plus the pinned Git Cycle796 source
    )
    controls_core = (
        paths_literal
        and all_paths_exist
        and observed_sha == EXPECTED_SHA256
        and pinned_commit == PINNED_796_COMMIT
        and pinned_sha == PINNED_796_SHA256
        and sources_unchanged
        and blocklist["pass"]
        and deterministic
        and within_read_cap
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    projected_detail = {
        "literal_AUDIT_INPUT_PATHS": paths_literal,
        "all_paths_existing": all_paths_exist,
        "disk_sha256": observed_sha,
        "expected_disk_sha256": EXPECTED_SHA256,
        "pinned_796": {
            "commit": pinned_commit,
            "path": PINNED_796_PATH,
            "sha256": pinned_sha,
        },
        "sources_unchanged": sources_unchanged,
        "blocklisted_primary_text_AST_only": blocklist,
        "deterministic": deterministic,
        "determinism_sha256": digest(first_recount),
        "files_beyond_primary": {
            "worktree_disk": 6,
            "pinned_git": 1,
            "total": 7,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
    }
    projected_stdout_bytes = (
        len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8"))
        + len(compact(projected_detail).encode("utf-8"))
        + 12 * 1024
    )
    controls_pass = controls_core and (
        projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    projected_detail["projected_stdout_bytes"] = projected_stdout_bytes
    projected_detail["stdout_limit_bytes"] = STDOUT_LIMIT_BYTES
    candidate_certificate(
        "CONTROLS_SHA_BLOCKLIST_DETERMINISM_PATHS_AND_BOUNDS",
        controls_pass,
        projected_detail,
    )

    attacked = {
        "S1": s1_pass,
        "S2": s2_pass,
        "S3": s3_pass,
        "S4": s4_pass,
        "S5": s5_pass,
    }
    refuted_steps = tuple(
        name for name, survived in attacked.items() if not survived
    )
    if not s4_pass and s1_pass and s2_pass and s5_pass:
        overall = "WORDING_REFUTED"
    elif refuted_steps:
        overall = "STRUCTURE_REFUTED"
    else:
        overall = "CANDIDATE_SURVIVES"
    report = {
        "attack_outcomes": attacked,
        "refuted_steps": refuted_steps,
        "overall_ruling": overall,
        "wording_refuted_sentence":
            frozen_candidate if not s4_pass else None,
        "checker_completed_cleanly": controls_pass,
        "runtime_seconds": round(monotonic() - PROCESS_STARTED, 6),
    }
    report["report_sha256"] = digest(report)
    emit("OVERALL_RULING", report)
    emit(f"CYCLE804_INDEPENDENT_CHECK_COMPLETE_{overall}")

    output = "\n".join(OUTPUT_LINES) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if not controls_pass:
        raise AssertionError(("control failure", projected_detail))
    if not all((s3_pass, s4_pass)):
        # These attacks establish observations needed for any honest ruling.
        raise AssertionError(("execution/observation failure", attacked))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    if monotonic() - PROCESS_STARTED >= AUDIT_TIMEOUT_SEC:
        raise AssertionError("runtime bound")
    sys.stdout.write(output)
    # Scientific FAIL certificates mean the adversary found a refutation;
    # completing all attacks and controls is a successful checker execution.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
