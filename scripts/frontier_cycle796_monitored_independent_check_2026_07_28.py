#!/usr/bin/env python3
"""Cycle 796 independent adversarial provenance/cadence checker.

Cycle 796, Cycle 792, Cycle 794, Cycle 758, and Cycle 781 are text-only
blocklisted inputs.  The executable reconstruction imports only the three
landed suppliers declared literally in ``AUDIT_INPUT_PATHS``.

The checker preserves the v1 provenance and cadence measurements, then tests
that v2 declares their convention/glue status and robustness split exactly.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


RING_STATIONS = 11
FIXTURE_BANKS = 2
GLOBAL_CUTOFFS = (512, 1024, 2048)
PRIMARY_CUTOFF = 1024
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_KEYS = (
    (3, (1, 10), 252),
    (3, (0, 7), 371),
)
EXPECTED_COUNTS = {
    "transient_accept": 2,
    "certified_cycle_refusal": 12,
    "open_refusal_through_cutoff": 162,
}
NEAR_MISS_TICKS = (251, 252, 253, 370, 371, 372)

PRIMARY_796_PATH = (
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py"
)
PRIMARY_792_PATH = (
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py"
)
PRIMARY_794_COMMIT = "0f4bace05de9b2830ea0b9a3f8a99f42a56cc301"
PRIMARY_794_PATH = (
    "scripts/frontier_cycle794_second_selection_2026_07_28.py"
)
REFERENCE_758_COMMIT = PRIMARY_794_COMMIT
REFERENCE_758_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
REFERENCE_781_COMMIT = "72efa390fc444a220719ebd261d367145f1e895a"
REFERENCE_781_PATH = (
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py"
)

TEXT_ONLY_BLOCKLIST_PREFIXES = (
    "frontier_cycle796_monitored_selector_",
    "frontier_cycle792_extended_horizon_selector_",
    "frontier_cycle794_second_selection_",
    "frontier_cycle758_selector_multisource_",
    "frontier_cycle781_checkpoint_refusal_law_",
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[1]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_796_PATH:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    PRIMARY_792_PATH:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    PRIMARY_794_PATH:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    REFERENCE_758_PATH:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    REFERENCE_781_PATH:
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
}
EXPECTED_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[1]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[2]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_796_PATH: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    PRIMARY_792_PATH: "63948b09c41dd02b14350084ec33f7df9ad83b47",
    PRIMARY_794_PATH: "a6debf306793270a4cda61638b619d4ad55dea69",
    REFERENCE_758_PATH: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    REFERENCE_781_PATH: "d14cd0ece611c647d3cb7b184830ef9b10754b1d",
}

OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def blob_sha1(payload: bytes) -> str:
    header = b"blob " + str(len(payload)).encode("ascii") + b"\0"
    return sha1(header + payload).hexdigest()


def emit(line: str) -> None:
    OUTPUT_LINES.append(line)
    print(line, flush=True)


def certificate(name: str, passed: bool, detail: object) -> dict[str, object]:
    row = {"name": name, "pass": bool(passed), "detail": detail}
    emit(
        ("PASS " if row["pass"] else "FAIL ")
        + name
        + " :: "
        + compact(detail)
    )
    return row


def local_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def git_output(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=60,
    ).stdout


def git_text(spec: str) -> bytes:
    return git_output("show", spec)


def git_rev_parse(spec: str) -> str:
    return git_output("rev-parse", spec).decode("ascii").strip()


def fetch_text_copies(directory: Path) -> dict[str, object]:
    """Materialize every fetched text-only source before AST inspection."""

    sources = {
        "reference_758": (
            f"{REFERENCE_758_COMMIT}:{REFERENCE_758_PATH}",
            REFERENCE_758_PATH,
        ),
        "reference_781": (
            f"{REFERENCE_781_COMMIT}:{REFERENCE_781_PATH}",
            REFERENCE_781_PATH,
        ),
        "primary_794": (
            f"{PRIMARY_794_COMMIT}:{PRIMARY_794_PATH}",
            PRIMARY_794_PATH,
        ),
    }
    copies = {}
    for label, (spec, canonical_path) in sources.items():
        payload = git_text(spec)
        destination = directory / Path(canonical_path).name
        destination.write_bytes(payload)
        copies[label] = {
            "path": destination,
            "canonical_path": canonical_path,
            "spec": spec,
            "sha256": sha256(destination.read_bytes()).hexdigest(),
            "blob_sha1": blob_sha1(destination.read_bytes()),
        }
    return copies


def parse_path(path: Path) -> ast.Module:
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function surface", name, len(matches)))
    return matches[0]


def top_assignments(tree: ast.Module) -> dict[str, ast.expr]:
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    result[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(
            node.target, ast.Name
        ):
            result[node.target.id] = node.value
    return result


def condition_map(function: ast.FunctionDef) -> dict[str, ast.expr]:
    dictionaries = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "conditions"
            and isinstance(node.value, ast.Dict)
        ):
            dictionaries.append(node.value)
    if len(dictionaries) != 1:
        raise AssertionError(
            ("conditions dictionary", function.name, len(dictionaries))
        )
    result = {}
    for key, value in zip(dictionaries[0].keys, dictionaries[0].values):
        literal = ast.literal_eval(key)
        if not isinstance(literal, str):
            raise AssertionError(("condition key", literal))
        result[literal] = value
    return result


def body_ast(function: ast.FunctionDef) -> str:
    body = list(function.body)
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        body = body[1:]
    return ast.dump(
        ast.Module(body=body, type_ignores=[]),
        include_attributes=False,
    )


def dotted_calls(node: ast.AST) -> tuple[str, ...]:
    calls = []
    for item in ast.walk(node):
        if not isinstance(item, ast.Call):
            continue
        function = item.func
        if (
            isinstance(function, ast.Attribute)
            and isinstance(function.value, ast.Name)
        ):
            calls.append(function.value.id + "." + function.attr)
        elif isinstance(function, ast.Name):
            calls.append(function.id)
    return tuple(calls)


def literal_audit_tuple(tree: ast.Module) -> tuple[str, ...] | None:
    assignment = top_assignments(tree).get("AUDIT_INPUT_PATHS")
    if not isinstance(assignment, ast.Tuple) or not all(
        isinstance(item, ast.Constant) and isinstance(item.value, str)
        for item in assignment.elts
    ):
        return None
    return tuple(ast.literal_eval(assignment))


def provenance_audit(
    copies: dict[str, object],
) -> tuple[dict[str, object], tuple[str, ...]]:
    """Attack every composition element against its claimed source text."""

    own_tree = parse_path(Path(__file__))
    primary_tree = parse_path(ROOT / PRIMARY_796_PATH)
    source_736_tree = parse_path(ROOT / AUDIT_INPUT_PATHS[0])
    source_750_tree = parse_path(ROOT / AUDIT_INPUT_PATHS[1])
    source_719_tree = parse_path(ROOT / AUDIT_INPUT_PATHS[2])
    reference_758_tree = parse_path(copies["reference_758"]["path"])
    reference_781_tree = parse_path(copies["reference_781"]["path"])

    anchor_payloads = {
        AUDIT_INPUT_PATHS[0]: local_bytes(AUDIT_INPUT_PATHS[0]),
        AUDIT_INPUT_PATHS[1]: local_bytes(AUDIT_INPUT_PATHS[1]),
        AUDIT_INPUT_PATHS[2]: local_bytes(AUDIT_INPUT_PATHS[2]),
        PRIMARY_796_PATH: local_bytes(PRIMARY_796_PATH),
        PRIMARY_792_PATH: local_bytes(PRIMARY_792_PATH),
        PRIMARY_794_PATH:
            copies["primary_794"]["path"].read_bytes(),
        REFERENCE_758_PATH:
            copies["reference_758"]["path"].read_bytes(),
        REFERENCE_781_PATH:
            copies["reference_781"]["path"].read_bytes(),
    }
    anchors = {
        path: {
            "sha256": sha256(payload).hexdigest(),
            "blob_sha1": blob_sha1(payload),
            "expected_sha256": EXPECTED_SHA256[path],
            "expected_blob_sha1": EXPECTED_BLOB_SHA1[path],
        }
        for path, payload in anchor_payloads.items()
    }
    anchors_exact = all(
        row["sha256"] == row["expected_sha256"]
        and row["blob_sha1"] == row["expected_blob_sha1"]
        for row in anchors.values()
    )
    fetched_copies_exact = (
        copies["reference_758"]["sha256"]
        == EXPECTED_SHA256[REFERENCE_758_PATH]
        and copies["reference_758"]["blob_sha1"]
        == EXPECTED_BLOB_SHA1[REFERENCE_758_PATH]
        and copies["reference_781"]["sha256"]
        == EXPECTED_SHA256[REFERENCE_781_PATH]
        and copies["reference_781"]["blob_sha1"]
        == EXPECTED_BLOB_SHA1[REFERENCE_781_PATH]
        and copies["primary_794"]["sha256"]
        == EXPECTED_SHA256[PRIMARY_794_PATH]
        and copies["primary_794"]["blob_sha1"]
        == EXPECTED_BLOB_SHA1[PRIMARY_794_PATH]
    )
    commits_exact = (
        git_rev_parse(REFERENCE_758_COMMIT) == REFERENCE_758_COMMIT
        and git_rev_parse(REFERENCE_781_COMMIT) == REFERENCE_781_COMMIT
        and git_rev_parse(PRIMARY_794_COMMIT) == PRIMARY_794_COMMIT
    )
    local_758_matches_fetched = (
        local_bytes(REFERENCE_758_PATH)
        == copies["reference_758"]["path"].read_bytes()
    )

    primary_conditions = condition_map(
        function_node(primary_tree, "build_base_rows")
    )
    reference_conditions = condition_map(
        function_node(
            reference_758_tree,
            "multisource_enforcement_lineage_selector",
        )
    )
    shared_exclusions = (
        "synchronous_composition",
        "token_rail_return",
        "literal_inverse",
    )
    shared_expression_exact = {
        name: (
            ast.dump(primary_conditions[name], include_attributes=False)
            == ast.dump(reference_conditions[name], include_attributes=False)
        )
        for name in shared_exclusions
    }
    clean_ast_exact = body_ast(
        function_node(primary_tree, "clean_postimage")
    ) == body_ast(function_node(reference_758_tree, "clean_postimage"))
    reference_exclusions = (
        *shared_exclusions,
        "clean_postimage",
    )
    scope_additions = tuple(
        name for name in primary_conditions if name not in shared_exclusions
    )

    source_736_functions = {
        node.name
        for node in source_736_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    source_750_functions = {
        node.name
        for node in source_750_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    source_719_functions = {
        node.name
        for node in source_719_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    invariant_736 = function_node(
        source_736_tree, "invariant_full_orbit_certificate"
    )
    calls_736 = set(dotted_calls(invariant_736))
    landed_battery_sources_present = (
        set(shared_exclusions).issubset(reference_conditions)
        and tuple(reference_conditions) == reference_exclusions
        and all(shared_expression_exact.values())
        and clean_ast_exact
        and scope_additions
        == (
            "census_membership",
            "pairwise_separation",
            "synchronization",
        )
        and {
            "configuration_census",
            "is_pairwise_separated",
            "synchronous_composition_word",
            "invariant_full_orbit_certificate",
        }.issubset(source_736_functions)
        and "k_epoch_fixtures" in source_750_functions
        and {
            "mapped_macro",
            "apply_controller_step",
            "run_orbit",
            "controller_word",
        }.issubset(source_719_functions)
        and {
            "K.apply_controller_step",
            "K.run_orbit",
            "synchronous_composition_word",
        }.issubset(calls_736)
    )

    reference_imports = {
        alias.asname or alias.name: alias.name
        for node in reference_781_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    non_interference = function_node(reference_781_tree, "non_interference")
    non_interference_source = ast.unparse(non_interference)
    landed_781_station_monitor = (
        reference_imports.get("C719")
        == "frontier_cycle719_recurrent_matter_history_controller_2026_07_26"
        and reference_imports.get("K719")
        == "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        and "for step in range(C719.CONTROLLER_STATIONS):"
        in non_interference_source
        and non_interference_source.count(
            "C719.apply_fast_int("
        ) >= 2
        and "decoded_cell_rows(controller_data(guarded))"
        in non_interference_source
    )
    monitor_source = ast.unparse(
        function_node(primary_tree, "monitor_family")
    )
    advance_source = ast.unparse(
        function_node(primary_tree, "advance_one_boundary")
    )
    run_orbit_source = ast.unparse(
        function_node(source_719_tree, "run_orbit")
    )
    primary_full_orbit_monitor = (
        "advance_one_boundary(" in monitor_source
        and "K.A.apply_semantic(state, composition_word)"
        in advance_source
        and "for step in iterable:" in run_orbit_source
        and "apply_controller_step(" in run_orbit_source
        and ast.literal_eval(
            top_assignments(primary_tree)["RING_STATIONS"]
        )
        == RING_STATIONS
    )
    cadence_traceable = not (
        landed_781_station_monitor and primary_full_orbit_monitor
    )
    first_pass_glue_landed = False
    expected_corrected_provenance_table = (
        {
            "composition_element": "battery elements",
            "classification": "LANDED",
            "landed_source":
                "Cycles 736, 750, 719, and pinned Cycle 758",
        },
        {
            "composition_element": "monitoring concept",
            "classification":
                "LANDED AT PLURAL GRANULARITIES — THE CHOICE AMONG THEM "
                "IS A DECLARED CONVENTION",
            "landed_source": "K719 structure and pinned Cycle 781",
        },
        {
            "composition_element": "accept-first-pass glue",
            "classification": "DECLARED COMPOSITION GLUE, UNLANDED",
            "landed_source": "Cycle 796 v2 composition",
        },
    )
    primary_assignments = top_assignments(primary_tree)
    primary_corrected_provenance_table = ast.literal_eval(
        primary_assignments["PROVENANCE_TABLE"]
    )
    primary_landed_cadences = ast.literal_eval(
        primary_assignments["LANDED_CADENCES"]
    )
    expected_cadence_names = (
        "orbit_return_boundary",
        "H_station_boundary",
        "Q_R1_R2_layer_boundary",
        "program_macro_completion",
    )
    corrected_provenance_matches = (
        primary_corrected_provenance_table
        == expected_corrected_provenance_table
        and tuple(row["name"] for row in primary_landed_cadences)
        == expected_cadence_names
        and landed_battery_sources_present
        and landed_781_station_monitor
        and primary_full_orbit_monitor
        and not first_pass_glue_landed
    )

    composition_elements = (
        {
            "element": "k=2 census, separation, synchronous composition",
            "claimed_source": "Cycle 736",
            "traceable": landed_battery_sources_present,
        },
        {
            "element": "fixtures, token return, literal inverse",
            "claimed_source": "Cycles 750/719 and pinned Cycle 758",
            "traceable":
                landed_battery_sources_present
                and all(shared_expression_exact.values()),
        },
        {
            "element": "clean_postimage",
            "claimed_source": "pinned Cycle 758",
            "traceable": clean_ast_exact,
        },
        {
            "element": "every-boundary monitoring cadence",
            "claimed_source": "pinned Cycle 781",
            "traceable": cadence_traceable,
            "observed_781_granularity":
                "one C719 H application/station boundary",
            "observed_796_granularity":
                "one complete 11-step K719 orbit return",
        },
        {
            "element": "accept first full-battery pass / else refuse",
            "claimed_source": "Cycle 796 composition glue",
            "traceable": first_pass_glue_landed,
        },
    )
    findings = []
    if not corrected_provenance_matches:
        findings.append(
            "PROVENANCE MISMATCH: the v2 provenance table does not classify "
            "the battery as landed, monitoring as landed at plural declared "
            "cadences, and accept-first-pass as declared unlanded glue."
        )
    imported_blocklisted = tuple(
        sorted(
            name
            for name in sys.modules
            if name.startswith(TEXT_ONLY_BLOCKLIST_PREFIXES)
        )
    )
    direct_imports = {
        "M736": M736.__name__,
        "F750": F750.__name__,
        "K719": K719.__name__,
    }
    expected_imports = {
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "K719":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }
    controls_exact = (
        anchors_exact
        and fetched_copies_exact
        and commits_exact
        and local_758_matches_fetched
        and literal_audit_tuple(own_tree) == AUDIT_INPUT_PATHS
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and direct_imports == expected_imports
        and not imported_blocklisted
    )
    result = {
        "anchors": anchors,
        "reference_commits": {
            "Cycle758": REFERENCE_758_COMMIT,
            "Cycle781": REFERENCE_781_COMMIT,
            "Cycle794": PRIMARY_794_COMMIT,
        },
        "references_materialized_as_disk_copies": {
            label: {
                "spec": row["spec"],
                "sha256": row["sha256"],
                "blob_sha1": row["blob_sha1"],
            }
            for label, row in copies.items()
        },
        "local_758_matches_fetched_copy": local_758_matches_fetched,
        "literal_AUDIT_INPUT_PATHS": literal_audit_tuple(own_tree),
        "direct_executable_imports": direct_imports,
        "text_only_blocklist_prefixes": TEXT_ONLY_BLOCKLIST_PREFIXES,
        "imported_blocklisted_modules": imported_blocklisted,
        "reference_758_exclusion_keys": tuple(reference_conditions),
        "primary_condition_keys": tuple(primary_conditions),
        "shared_expression_exact": shared_expression_exact,
        "clean_postimage_AST_exact": clean_ast_exact,
        "landed_battery_sources_present": landed_battery_sources_present,
        "landed_781_station_monitor": landed_781_station_monitor,
        "primary_full_orbit_monitor": primary_full_orbit_monitor,
        "primary_corrected_provenance_table":
            primary_corrected_provenance_table,
        "expected_corrected_provenance_table":
            expected_corrected_provenance_table,
        "primary_landed_cadences": primary_landed_cadences,
        "corrected_provenance_matches":
            corrected_provenance_matches,
        "composition_elements": composition_elements,
        "controls_exact": controls_exact,
        "pass": controls_exact and corrected_provenance_matches,
    }
    return result, tuple(findings)


def exact_tuple_literals(tree: ast.Module) -> tuple[tuple[int, object], ...]:
    rows = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Tuple):
            continue
        try:
            value = ast.literal_eval(node)
        except (ValueError, TypeError):
            continue
        rows.append((getattr(node, "lineno", -1), value))
    return tuple(rows)


def no_per_configuration_values_audit() -> dict[str, object]:
    primary_tree = parse_path(ROOT / PRIMARY_796_PATH)
    assignments = top_assignments(primary_tree)
    law_function_names = (
        "clean_postimage",
        "build_base_rows",
        "advance_one_boundary",
        "monitor_family",
    )
    law_functions = tuple(
        function_node(primary_tree, name) for name in law_function_names
    )
    forbidden_numbers = {252, 371}
    law_literal_hits = tuple(
        (function.name, node.lineno, node.value)
        for function in law_functions
        for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
        and node.value in forbidden_numbers
    )
    expected_symbol_hits = tuple(
        (function.name, node.lineno)
        for function in law_functions
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
        and node.id == "EXPECTED_ACCEPTANCE_MOMENTS"
    )
    target_keys = (
        (3, (1, 10)),
        (3, (0, 7)),
    )
    law_key_literal_hits = tuple(
        (function.name, line, value)
        for function in law_functions
        for line, value in exact_tuple_literals(
            ast.Module(body=function.body, type_ignores=[])
        )
        if value in target_keys
    )
    all_number_sites = tuple(
        (
            "top_level",
            node.lineno,
            item.value,
        )
        for node in primary_tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for item in ast.walk(node)
        if isinstance(item, ast.Constant)
        and isinstance(item.value, int)
        and not isinstance(item.value, bool)
        and item.value in forbidden_numbers
    )
    expected_binding = ast.literal_eval(
        assignments["EXPECTED_ACCEPTANCE_MOMENTS"]
    )
    cutoff_binding = ast.literal_eval(assignments["MONITOR_CUTOFF"])
    specific_key_literals_anywhere = tuple(
        (line, value)
        for line, value in exact_tuple_literals(primary_tree)
        if value in target_keys
    )
    return {
        "law_functions": law_function_names,
        "forbidden_acceptance_literals": tuple(sorted(forbidden_numbers)),
        "law_literal_hits": law_literal_hits,
        "law_expected_symbol_hits": expected_symbol_hits,
        "law_specific_key_literal_hits": law_key_literal_hits,
        "all_252_371_literal_sites": all_number_sites,
        "prediction_binding": expected_binding,
        "specific_key_literals_anywhere": specific_key_literals_anywhere,
        "global_cutoff_binding": cutoff_binding,
        "separation":
            "252/371 occur only in EXPECTED_ACCEPTANCE_MOMENTS; the law "
            "functions neither load that symbol nor contain either target key",
        "pass": (
            expected_binding == (252, 371)
            and cutoff_binding == PRIMARY_CUTOFF
            and not law_literal_hits
            and not expected_symbol_hits
            and not law_key_literal_hits
            and not specific_key_literals_anywhere
            and len(all_number_sites) == 2
        ),
    }


def bits_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(value) << wire for wire, value in enumerate(bits))


def int_to_bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> wire) & 1 for wire in range(width))


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, ...], ...]:
    kinds = {"X": 0, "CNOT": 1, "TOF": 2}
    compiled = []
    for gate in word:
        if gate.kind not in kinds:
            raise ValueError(("nonclassical gate in monitored word", gate))
        compiled.append((kinds[gate.kind], *gate.wires))
    return tuple(compiled)


def apply_fast(value: int, word: tuple[tuple[int, ...], ...]) -> int:
    output = value
    for gate in word:
        if gate[0] == 0:
            output ^= 1 << gate[1]
        elif gate[0] == 1:
            output ^= ((output >> gate[1]) & 1) << gate[2]
        else:
            controls = (
                ((output >> gate[1]) & 1)
                & ((output >> gate[2]) & 1)
            )
            output ^= controls << gate[3]
    return output


def clean_mask(bank_count: int) -> int:
    mask = 1 << K719.R3.X.SOURCE_POINTER
    bank_wires = (
        K719.A.POINTER,
        K719.A.U_TO_V,
        K719.A.V_TO_U,
        K719.A.DIRECTION_OK,
        *K719.A.FRESH,
        *K719.A.ZERO_WORK,
        K719.A.TOKEN_OK,
    )
    for base in K719.M.R12.BANK_BASES[:bank_count]:
        for wire in bank_wires:
            mask |= 1 << (base + wire)
    for base in K719.M.R12.LINK_BASES[:bank_count - 1]:
        for wire in range(K719.B.LINK_WIDTH):
            mask |= 1 << (base + wire)
    return mask


CLEAN_MASK = clean_mask(FIXTURE_BANKS)


def clean_int(state: int) -> bool:
    return state & CLEAN_MASK == 0


def rail_step(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a_tokens)
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(stations):
        a[station], b[station] = b[station], a[station]
    for station in range(stations):
        target = (station + 1) % stations
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def independent_rail_orbit(
    positions: tuple[int, ...],
    stations: int,
) -> dict[str, object]:
    a = tuple(int(station in positions) for station in range(stations))
    initial_a = a
    b = (0,) * stations
    trace = []
    for _step in range(stations):
        before = tuple(
            station for station, value in enumerate(a) if value
        )
        a, b = rail_step(a, b)
        after = tuple(
            station for station, value in enumerate(a) if value
        )
        trace.append((before, after, sum(b)))
    return {
        "a": a,
        "b": b,
        "initial_a": initial_a,
        "trace": tuple(trace),
    }


def expected_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            tuple(
                sorted(
                    (position + step) % RING_STATIONS
                    for position in positions
                )
            ),
            tuple(
                sorted(
                    (position + step + 1) % RING_STATIONS
                    for position in positions
                )
            ),
            0,
        )
        for step in range(RING_STATIONS)
    )


def state_sha256(state: int, width: int) -> str:
    byte_width = (width + 7) // 8
    return sha256(state.to_bytes(byte_width, "little")).hexdigest()


def build_independent_family() -> tuple[
    dict[tuple[int, tuple[int, ...]], dict[str, object]],
    dict[str, object],
]:
    """Build all rows without importing any Cycle 758/792/794/796 module."""

    census = M736.configuration_census()
    configurations = census["configurations"]
    positions_rows = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    position_members = frozenset(positions_rows)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    program = fixtures[0][2]
    words = {
        positions: M736.synchronous_composition_word(
            program, positions
        )
        for positions in positions_rows
    }
    compiled_words = {
        positions: compile_word(word)
        for positions, word in words.items()
    }
    inverse_words = {
        positions: tuple(reversed(word))
        for positions, word in compiled_words.items()
    }
    rail_certificates = {
        positions:
            independent_rail_orbit(positions, len(program))
        for positions in positions_rows
    }

    rows = {}
    failure_census: Counter[str] = Counter()
    width = len(fixtures[0][3])
    for event, direction, fixture_program, before, _expected in fixtures:
        if fixture_program != program:
            raise AssertionError("fixture program drift")
        before_int = bits_to_int(before)
        for positions in positions_rows:
            after_int = apply_fast(
                before_int, compiled_words[positions]
            )
            restored_int = apply_fast(
                after_int, inverse_words[positions]
            )
            rail = rail_certificates[positions]
            config = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            conditions = {
                "synchronous_composition": True,
                "token_rail_return": (
                    rail["a"] == rail["initial_a"]
                    and not any(rail["b"])
                ),
                "literal_inverse": (
                    restored_int == before_int
                    and rail["a"] == rail["initial_a"]
                    and not any(rail["b"])
                ),
                "census_membership":
                    positions in position_members,
                "pairwise_separation":
                    M736.is_pairwise_separated(config),
                "synchronization":
                    rail["trace"] == expected_trace(positions),
            }
            for name, passed in conditions.items():
                if not passed:
                    failure_census[name] += 1
            key = (event, positions)
            rows[key] = {
                "key": key,
                "event": event,
                "direction": direction,
                "program": program,
                "before": before,
                "before_int": before_int,
                "positions": positions,
                "word": words[positions],
                "compiled_word": compiled_words[positions],
                "after_int": after_int,
                "conditions": conditions,
                "width": width,
            }

    compiler_cases = (
        (0, (0, 2)),
        (0, (1, 10)),
        (1, (0, 3)),
        (1, (0, 7)),
        (2, (0, 4)),
        (2, (2, 10)),
        (3, (1, 10)),
        (3, (0, 7)),
    )
    semantic_failures = []
    orbit_failures = []
    accepted_key_condition_checks = {}
    for key in compiler_cases:
        row = rows[key]
        direct = K719.A.apply_semantic(
            row["before"], row["word"]
        )
        if bits_to_int(direct) != row["after_int"]:
            semantic_failures.append(key)
        observed, rail_a, rail_b, trace = K719.run_orbit(
            row["before"],
            row["program"],
            token_positions=row["positions"],
        )
        restored, inverse_a, inverse_b, _inverse_trace = K719.run_orbit(
            observed,
            row["program"],
            token_positions=row["positions"],
            reverse=True,
        )
        expected_a = tuple(
            int(station in row["positions"])
            for station in range(len(row["program"]))
        )
        orbit_conditions = {
            "synchronous_composition":
                bits_to_int(observed) == row["after_int"],
            "token_rail_return":
                rail_a == expected_a and not any(rail_b),
            "literal_inverse": (
                restored == row["before"]
                and inverse_a == rail_a
                and inverse_b == rail_b
            ),
            "synchronization":
                trace == expected_trace(row["positions"]),
        }
        if not all(orbit_conditions.values()):
            orbit_failures.append((key, orbit_conditions))
        if key in {
            (3, (1, 10)),
            (3, (0, 7)),
        }:
            accepted_key_condition_checks[
                f"{key[0]}:{key[1]}"
            ] = orbit_conditions

    all_static_conditions_pass = all(
        all(row["conditions"].values())
        for row in rows.values()
    )
    initial_clean_count = sum(
        clean_int(row["after_int"]) for row in rows.values()
    )
    control = {
        "census_agreement": census["agreement"],
        "k2_configurations": len(positions_rows),
        "fixtures": len(fixtures),
        "family_keys": len(rows),
        "word_gate_count_range": (
            min(map(len, words.values())),
            max(map(len, words.values())),
        ),
        "compiled_gate_kinds": tuple(
            sorted(
                {
                    gate[0]
                    for word in compiled_words.values()
                    for gate in word
                }
            )
        ),
        "dirty_mask_bits": CLEAN_MASK.bit_count(),
        "static_failure_census": dict(sorted(failure_census.items())),
        "initial_clean_count": initial_clean_count,
        "compiler_crosscheck_cases": compiler_cases,
        "semantic_crosscheck_failures": tuple(semantic_failures),
        "run_orbit_crosscheck_failures": tuple(orbit_failures),
        "accepted_key_condition_checks":
            accepted_key_condition_checks,
        "pass": (
            census["agreement"]
            and len(positions_rows)
            == M736.EXPECTED_COUNTS_BY_K[2]
            == 44
            and len(fixtures) == 4
            and len(rows) == 176
            and all_static_conditions_pass
            and initial_clean_count == 0
            and not semantic_failures
            and not orbit_failures
            and all(
                all(conditions.values())
                for conditions
                in accepted_key_condition_checks.values()
            )
        ),
    }
    return rows, control


def monitor_family(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    *,
    cutoff: int,
    label: str,
    reverse_order: bool = False,
) -> dict[str, object]:
    """Independent first-pass scan at full-orbit return boundaries."""

    started = monotonic()
    ordered_keys = tuple(sorted(rows, reverse=reverse_order))
    state = {key: rows[key]["after_int"] for key in ordered_keys}
    seen = {key: {state[key]: 0} for key in ordered_keys}
    first_clean = {key: None for key in ordered_keys}
    cycles = {key: None for key in ordered_keys}
    unresolved = set(ordered_keys)
    evolving = set(ordered_keys)
    clean_survivors = {
        tick: () for tick in NEAR_MISS_TICKS if tick <= cutoff
    }

    for key in ordered_keys:
        if (
            all(rows[key]["conditions"].values())
            and clean_int(state[key])
        ):
            first_clean[key] = 0
            unresolved.remove(key)
            seen[key].clear()

    for tick in range(1, cutoff + 1):
        retired_cycles = []
        clean_now = []
        for key in ordered_keys:
            if key not in evolving:
                continue
            next_state = apply_fast(
                state[key], rows[key]["compiled_word"]
            )
            state[key] = next_state
            full_pass = (
                clean_int(next_state)
                and all(rows[key]["conditions"].values())
            )
            if full_pass:
                clean_now.append(key)
                if key in unresolved:
                    first_clean[key] = tick
                    unresolved.remove(key)
                    seen[key].clear()
            elif key in unresolved:
                if next_state in seen[key]:
                    entry = seen[key][next_state]
                    cycles[key] = {
                        "entry_boundary": entry,
                        "return_boundary": tick,
                        "period": tick - entry,
                    }
                    unresolved.remove(key)
                    retired_cycles.append(key)
                else:
                    seen[key][next_state] = tick
        evolving.difference_update(retired_cycles)
        if tick in clean_survivors:
            clean_survivors[tick] = tuple(sorted(clean_now))
        if tick % 256 == 0:
            emit(
                "PROGRESS "
                + compact(
                    {
                        "scan": label,
                        "boundary": tick,
                        "evolving": len(evolving),
                        "unresolved": len(unresolved),
                        "accepted": sum(
                            moment is not None
                            for moment in first_clean.values()
                        ),
                        "cycles": sum(
                            row is not None for row in cycles.values()
                        ),
                        "elapsed_seconds":
                            round(monotonic() - started, 3),
                    }
                )
            )

    table = []
    for key in sorted(rows):
        moment = first_clean[key]
        if moment is not None:
            classification = "transient_accept"
        elif cycles[key] is not None:
            classification = "certified_cycle_refusal"
        else:
            classification = "open_refusal_through_cutoff"
        table.append(
            {
                "key": key,
                "classification": classification,
                "acceptance_moment": moment,
                "cycle": cycles[key],
                "final_state_sha256": state_sha256(
                    state[key], rows[key]["width"]
                ),
            }
        )
    counts = Counter(row["classification"] for row in table)
    acceptance_rows = tuple(
        sorted(
            (
                (
                    key[0],
                    key[1],
                    moment,
                )
                for key, moment in first_clean.items()
                if moment is not None
            ),
            key=lambda row: row[2],
        )
    )
    acceptance_certificates = tuple(
        {
            "event": event,
            "positions": positions,
            "moment": moment,
            "conditions": {
                **rows[(event, positions)]["conditions"],
                "clean_postimage": True,
            },
        }
        for event, positions, moment in acceptance_rows
    )
    signature = {
        "cutoff": cutoff,
        "table": table,
        "clean_survivors": clean_survivors,
        "acceptance_certificates": acceptance_certificates,
    }
    return {
        "cutoff": cutoff,
        "table": tuple(table),
        "classification_counts": dict(sorted(counts.items())),
        "acceptance_keys": acceptance_rows,
        "acceptance_moments": tuple(
            row[2] for row in acceptance_rows
        ),
        "acceptance_certificates": acceptance_certificates,
        "clean_survivors_near_misses": clean_survivors,
        "table_sha256": digest(signature),
        "runtime_seconds": round(monotonic() - started, 6),
    }


CADENCE_CANDIDATES = (
    {
        "name": "orbit_return_boundary",
        "landed_surface":
            "K719.run_orbit return after len(program) H applications",
        "aliases": ("full_orbit", "token_rail_return"),
    },
    {
        "name": "H_station_boundary",
        "landed_surface":
            "K719.apply_controller_step return after H=R2 R1 Q",
        "aliases": (
            "controller_step",
            "program_step",
            "station_boundary",
            "H_application",
        ),
    },
    {
        "name": "Q_R1_R2_layer_boundary",
        "landed_surface":
            "K719.controller_word explicit q + r1 + r2 layer split",
        "aliases": ("Q_boundary", "R1_boundary", "R2_boundary"),
    },
    {
        "name": "program_macro_completion",
        "landed_surface":
            "K719.mapped_macro completions inside the Q layer",
        "aliases": ("active_station_macro",),
    },
)


def cadence_probe_for_key(
    row: dict[str, object],
    *,
    maximum_orbit: int,
    window: tuple[int, int, int],
) -> dict[str, object]:
    program = row["program"]
    stations = len(program)
    macro_words = tuple(
        compile_word(K719.mapped_macro(program[station]))
        for station in range(stations)
    )
    state = row["after_int"]
    a = tuple(
        int(station in row["positions"])
        for station in range(stations)
    )
    b = (0,) * stations
    first = {
        "orbit_return_boundary": None,
        "H_station_boundary": None,
        "Q_boundary": None,
        "R1_boundary": None,
        "R2_boundary": None,
        "program_macro_completion": None,
    }
    window_counts = {
        name: Counter()
        for name in first
    }
    window_examples = {
        name: []
        for name in first
    }
    recomposition_failures = []

    def observe(
        cadence: str,
        coordinate: dict[str, object],
        clean: bool,
    ) -> None:
        if not clean:
            return
        if first[cadence] is None:
            first[cadence] = coordinate
        orbit = int(coordinate["orbit"])
        if orbit in window:
            window_counts[cadence][orbit] += 1
            if len(window_examples[cadence]) < 12:
                window_examples[cadence].append(coordinate)

    absolute_h = 0
    for orbit in range(1, maximum_orbit + 1):
        orbit_input = state
        for step in range(1, stations + 1):
            absolute_h += 1
            live_stations = tuple(
                station
                for station, value in enumerate(a)
                if value
            )
            for station in live_stations:
                state = apply_fast(state, macro_words[station])
                observe(
                    "program_macro_completion",
                    {
                        "orbit": orbit,
                        "step": step,
                        "absolute_H": absolute_h,
                        "station": station,
                    },
                    clean_int(state),
                )
            layer_coordinate = {
                "orbit": orbit,
                "step": step,
                "absolute_H": absolute_h,
            }
            observe("Q_boundary", layer_coordinate, clean_int(state))

            a_list = list(a)
            b_list = list(b)
            for station in range(stations):
                a_list[station], b_list[station] = (
                    b_list[station],
                    a_list[station],
                )
            a, b = tuple(a_list), tuple(b_list)
            observe("R1_boundary", layer_coordinate, clean_int(state))

            a_list = list(a)
            b_list = list(b)
            for station in range(stations):
                target = (station + 1) % stations
                b_list[station], a_list[target] = (
                    a_list[target],
                    b_list[station],
                )
            a, b = tuple(a_list), tuple(b_list)
            observe("R2_boundary", layer_coordinate, clean_int(state))
            observe(
                "H_station_boundary",
                layer_coordinate,
                clean_int(state),
            )

        expected_orbit_state = apply_fast(
            orbit_input, row["compiled_word"]
        )
        if state != expected_orbit_state:
            recomposition_failures.append(orbit)
        orbit_coordinate = {
            "orbit": orbit,
            "step": stations,
            "absolute_H": absolute_h,
        }
        observe(
            "orbit_return_boundary",
            orbit_coordinate,
            clean_int(state),
        )

    return {
        "key": row["key"],
        "program_stations": stations,
        "first": first,
        "window": window,
        "window_clean_observation_counts": {
            name: {
                str(orbit): counts[orbit]
                for orbit in window
            }
            for name, counts in window_counts.items()
        },
        "window_examples": {
            name: tuple(rows)
            for name, rows in window_examples.items()
        },
        "orbit_recomposition_failures":
            tuple(recomposition_failures),
    }


def cadence_attack(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    primary_claims: dict[str, object],
) -> tuple[dict[str, object], tuple[str, ...]]:
    target_specs = (
        ((3, (1, 10)), 253, (251, 252, 253)),
        ((3, (0, 7)), 372, (370, 371, 372)),
    )
    probes = {
        f"{key[0]}:{key[1]}":
            cadence_probe_for_key(
                rows[key],
                maximum_orbit=maximum,
                window=window,
            )
        for key, maximum, window in target_specs
    }
    first_key = probes["3:(1, 10)"]
    second_key = probes["3:(0, 7)"]
    first_orbit = first_key["first"]["orbit_return_boundary"]
    first_h = first_key["first"]["H_station_boundary"]
    second_orbit = second_key["first"]["orbit_return_boundary"]
    second_h = second_key["first"]["H_station_boundary"]
    moment_sensitive = (
        first_h["absolute_H"] != first_orbit["absolute_H"]
        or second_h["absolute_H"] != second_orbit["absolute_H"]
    )
    existence_sensitive = any(
        (probe["first"]["orbit_return_boundary"] is None)
        != (probe["first"][cadence] is None)
        for probe in probes.values()
        for cadence in (
            "H_station_boundary",
            "Q_boundary",
            "R1_boundary",
            "R2_boundary",
            "program_macro_completion",
        )
    )
    near_miss_sensitive = any(
        probe["window_clean_observation_counts"][
            "orbit_return_boundary"
        ]
        != probe["window_clean_observation_counts"][cadence]
        for probe in probes.values()
        for cadence in (
            "H_station_boundary",
            "Q_boundary",
            "R1_boundary",
            "R2_boundary",
            "program_macro_completion",
        )
    )
    recomposition_failures = tuple(
        (label, probe["orbit_recomposition_failures"])
        for label, probe in probes.items()
        if probe["orbit_recomposition_failures"]
    )
    sensitive = moment_sensitive or existence_sensitive or near_miss_sensitive
    cadence_names = tuple(row["name"] for row in CADENCE_CANDIDATES)
    probe_rows = (
        ((3, (1, 10)), first_key),
        ((3, (0, 7)), second_key),
    )

    def grouped_first(
        probe: dict[str, object], cadence: str
    ) -> dict[str, object]:
        if cadence != "Q_R1_R2_layer_boundary":
            return probe["first"][cadence]
        layer_rows = tuple(
            probe["first"][name]
            for name in ("Q_boundary", "R1_boundary", "R2_boundary")
        )
        if not all(row == layer_rows[0] for row in layer_rows):
            raise AssertionError(("layer first-acceptance disagreement", layer_rows))
        return layer_rows[0]

    measured_first_acceptance_table = tuple(
        {
            "cadence": cadence,
            "key": key,
            "orbit": grouped_first(probe, cadence)["orbit"],
            "step": grouped_first(probe, cadence)["step"],
            "absolute_H":
                grouped_first(probe, cadence)["absolute_H"],
        }
        for cadence in cadence_names
        for key, probe in probe_rows
    )

    def grouped_window_counts(
        probe: dict[str, object], cadence: str
    ) -> dict[str, int]:
        counts = probe["window_clean_observation_counts"]
        if cadence != "Q_R1_R2_layer_boundary":
            return counts[cadence]
        return {
            str(orbit): sum(
                counts[layer][str(orbit)]
                for layer in ("Q_boundary", "R1_boundary", "R2_boundary")
            )
            for orbit in probe["window"]
        }

    measured_window_structure = tuple(
        {
            "cadence": cadence,
            "key": key,
            "window": probe["window"],
            "clean_observation_counts":
                grouped_window_counts(probe, cadence),
        }
        for cadence in cadence_names
        for key, probe in probe_rows
    )
    primary_report = primary_claims["report"]
    primary_first_acceptance_table = primary_report.get(
        "cadence_first_acceptance_table"
    )
    primary_window_structure = tuple(
        {
            "cadence": row["cadence"],
            "key": row["key"],
            "window": row["window"],
            "clean_observation_counts":
                row["clean_observation_counts"],
        }
        for row in primary_report.get("cadence_window_structure", ())
    )
    cadence_table_matches_measurements = (
        compact(primary_first_acceptance_table)
        == compact(measured_first_acceptance_table)
    )
    window_structure_matches_measurements = (
        compact(primary_window_structure)
        == compact(measured_window_structure)
    )
    selection_existence_cadence_robust = (
        not existence_sensitive
        and all(
            row["orbit"] is not None
            for row in measured_first_acceptance_table
        )
        and all(
            Counter(
                row["orbit"]
                for row in measured_first_acceptance_table
                if row["cadence"] == cadence
            ) == Counter((252, 371))
            for cadence in cadence_names
        )
    )
    orbit_level_moments_cadence_robust = all(
        tuple(
            row["orbit"]
            for row in measured_first_acceptance_table
            if row["cadence"] == cadence
        ) == (252, 371)
        for cadence in cadence_names
    )
    orbit_spill = second_key[
        "window_clean_observation_counts"
    ]["orbit_return_boundary"]["372"]
    h_spill = second_key[
        "window_clean_observation_counts"
    ]["H_station_boundary"]["372"]
    measured_robustness_split = {
        "selection_existence_cadence_robust":
            selection_existence_cadence_robust,
        "orbit_level_moments_cadence_robust":
            orbit_level_moments_cadence_robust,
        "sub_orbit_timing_cadence_sensitive":
            moment_sensitive,
        "window_fine_structure_cadence_sensitive":
            near_miss_sensitive and h_spill > 0 and orbit_spill == 0,
    }
    expected_robustness_split = {
        "selection_existence_cadence_robust": True,
        "orbit_level_moments_cadence_robust": True,
        "sub_orbit_timing_cadence_sensitive": True,
        "window_fine_structure_cadence_sensitive": True,
    }
    primary_robustness_split = primary_report.get("robustness_split")
    robustness_split_matches_measurements = (
        measured_robustness_split == expected_robustness_split
        and primary_robustness_split == expected_robustness_split
    )
    primary_v2_claims_match = (
        primary_claims["returncode"] == 0
        and primary_claims["stderr_bytes"] == 0
        and primary_claims["terminal"]
        == "CYCLE796_MONITORED_SELECTOR_PASS"
        and primary_report.get("pass") is True
        and cadence_table_matches_measurements
        and window_structure_matches_measurements
        and robustness_split_matches_measurements
        and primary_report.get("verdict")
        == "CONSTRUCTED_WITH_CADENCE_CONVENTION"
        and primary_report.get("exact_time_law_constructed_at_scope")
        == {
            "robust_content_constructed": True,
            "full_construction_convention_free": False,
        }
        and primary_report.get("axiom_update_triggered") is False
    )
    cadence_pass = primary_v2_claims_match and not recomposition_failures
    findings = ()
    if not cadence_pass:
        findings = (
            "CADENCE CLAIM MISMATCH: the v2 cadence table, window structure, "
            "or robustness split does not match the independent measurements.",
        )
    result = {
        "candidate_cadences_from_719": CADENCE_CANDIDATES,
        "Cycle781_idiom_matches":
            "H_station_boundary, not orbit_return_boundary",
        "target_probes": probes,
        "summary_table": (
            {
                "key": (3, (1, 10)),
                "orbit_return_first": first_orbit,
                "H_station_first": first_h,
                "program_macro_first":
                    first_key["first"]["program_macro_completion"],
                "existence_changed": False,
            },
            {
                "key": (3, (0, 7)),
                "orbit_return_first": second_orbit,
                "H_station_first": second_h,
                "program_macro_first":
                    second_key["first"]["program_macro_completion"],
                "existence_changed": False,
            },
        ),
        "moment_sensitive": moment_sensitive,
        "existence_sensitive_on_two_transients": existence_sensitive,
        "near_miss_pattern_sensitive": near_miss_sensitive,
        "cadence_sensitive": sensitive,
        "measured_first_acceptance_table":
            measured_first_acceptance_table,
        "primary_first_acceptance_table":
            primary_first_acceptance_table,
        "cadence_table_matches_measurements":
            cadence_table_matches_measurements,
        "measured_window_structure":
            measured_window_structure,
        "primary_window_structure":
            primary_window_structure,
        "window_structure_matches_measurements":
            window_structure_matches_measurements,
        "measured_robustness_split":
            measured_robustness_split,
        "primary_robustness_split":
            primary_robustness_split,
        "robustness_split_matches_measurements":
            robustness_split_matches_measurements,
        "primary_run": {
            "returncode": primary_claims["returncode"],
            "stdout_bytes": primary_claims["stdout_bytes"],
            "stderr_bytes": primary_claims["stderr_bytes"],
            "terminal": primary_claims["terminal"],
        },
        "orbit_recomposition_failures": recomposition_failures,
        "pass": cadence_pass,
    }
    return result, findings


def stdout_bytes() -> int:
    return len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8"))


def run_primary_claims() -> dict[str, object]:
    completed = subprocess.run(
        (sys.executable, str(ROOT / PRIMARY_796_PATH)),
        cwd=ROOT,
        check=False,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    stdout_text = completed.stdout.decode("utf-8")
    report_rows = tuple(
        line.removeprefix("REPORT :: ")
        for line in stdout_text.splitlines()
        if line.startswith("REPORT :: ")
    )
    if len(report_rows) != 1:
        raise AssertionError(("primary report rows", len(report_rows)))
    terminal = stdout_text.splitlines()[-1] if stdout_text else ""
    return {
        "returncode": completed.returncode,
        "stdout_bytes": len(completed.stdout),
        "stderr_bytes": len(completed.stderr),
        "terminal": terminal,
        "report": json.loads(report_rows[0]),
    }


def main() -> int:
    started = monotonic()
    certificates = []
    findings: list[str] = []

    with TemporaryDirectory(prefix="cycle796-independent-") as temporary:
        copies = fetch_text_copies(Path(temporary))
        provenance, provenance_findings = provenance_audit(copies)
        findings.extend(provenance_findings)
        certificates.append(
            certificate(
                "Certificate_A_PROVENANCE_AUDIT",
                provenance["pass"],
                provenance,
            )
        )

        rows, family_control = build_independent_family()
        primary_claims = run_primary_claims()
        cadence, cadence_findings = cadence_attack(rows, primary_claims)
        findings.extend(cadence_findings)
        certificates.append(
            certificate(
                "Certificate_B_CADENCE_UNIQUENESS_ATTACK",
                cadence["pass"],
                cadence,
            )
        )

        scans = {
            cutoff: monitor_family(
                rows,
                cutoff=cutoff,
                label=f"T{cutoff}",
            )
            for cutoff in GLOBAL_CUTOFFS
        }
        primary = scans[PRIMARY_CUTOFF]
        deterministic_rerun = monitor_family(
            rows,
            cutoff=PRIMARY_CUTOFF,
            label="T1024_reverse_order_determinism",
            reverse_order=True,
        )

        expected_acceptance_conditions = {
            "synchronous_composition": True,
            "token_rail_return": True,
            "literal_inverse": True,
            "census_membership": True,
            "pairwise_separation": True,
            "synchronization": True,
            "clean_postimage": True,
        }
        expected_near_misses = {
            251: (),
            252: ((3, (1, 10)),),
            253: (),
            370: (),
            371: ((3, (0, 7)),),
            372: (),
        }
        recount_pass = (
            family_control["pass"]
            and len(primary["table"]) == 176
            and primary["classification_counts"] == EXPECTED_COUNTS
            and primary["acceptance_keys"] == EXPECTED_KEYS
            and primary["acceptance_moments"] == (252, 371)
            and primary["clean_survivors_near_misses"]
            == expected_near_misses
            and all(
                row["conditions"] == expected_acceptance_conditions
                for row in primary["acceptance_certificates"]
            )
        )
        recount_detail = {
            "family_control": family_control,
            "cutoff": PRIMARY_CUTOFF,
            "classification_counts":
                primary["classification_counts"],
            "acceptance_keys": primary["acceptance_keys"],
            "acceptance_moments": primary["acceptance_moments"],
            "unique_survivors_and_near_misses":
                primary["clean_survivors_near_misses"],
            "per_exclusion_certificates":
                primary["acceptance_certificates"],
            "table_sha256": primary["table_sha256"],
            "runtime_seconds": primary["runtime_seconds"],
        }
        certificates.append(
            certificate(
                "Certificate_C_FAMILY_RUN_RECOUNT",
                recount_pass,
                recount_detail,
            )
        )
        if not recount_pass:
            findings.append(
                "FAMILY RECOUNT REFUTES: "
                + compact(recount_detail)
            )

        cutoff_acceptance = {
            cutoff: scans[cutoff]["acceptance_keys"]
            for cutoff in GLOBAL_CUTOFFS
        }
        cutoff_counts = {
            cutoff: scans[cutoff]["classification_counts"]
            for cutoff in GLOBAL_CUTOFFS
        }
        cutoff_pass = (
            all(
                acceptance == EXPECTED_KEYS
                for acceptance in cutoff_acceptance.values()
            )
            and all(
                counts == EXPECTED_COUNTS
                for counts in cutoff_counts.values()
            )
        )
        cutoff_detail = {
            "cutoffs": GLOBAL_CUTOFFS,
            "acceptance_keys": cutoff_acceptance,
            "classification_counts": cutoff_counts,
            "cutoff_role":
                "only bounds the 162 open refusals on this probe",
            "table_sha256": {
                cutoff: scans[cutoff]["table_sha256"]
                for cutoff in GLOBAL_CUTOFFS
            },
            "runtime_seconds": {
                cutoff: scans[cutoff]["runtime_seconds"]
                for cutoff in GLOBAL_CUTOFFS
            },
        }
        certificates.append(
            certificate(
                "Certificate_D_CUTOFF_SENSITIVITY_PROBE",
                cutoff_pass,
                cutoff_detail,
            )
        )
        if not cutoff_pass:
            findings.append(
                "CUTOFF DEPENDENCE: " + compact(cutoff_detail)
            )

        no_values = no_per_configuration_values_audit()
        certificates.append(
            certificate(
                "Certificate_E_NO_PER_CONFIGURATION_VALUES_AST",
                no_values["pass"],
                no_values,
            )
        )
        if not no_values["pass"]:
            findings.append(
                "PER-CONFIGURATION VALUE LEAK: "
                + compact(no_values)
            )

        deterministic = (
            primary["table"] == deterministic_rerun["table"]
            and primary["classification_counts"]
            == deterministic_rerun["classification_counts"]
            and primary["acceptance_keys"]
            == deterministic_rerun["acceptance_keys"]
            and primary["clean_survivors_near_misses"]
            == deterministic_rerun["clean_survivors_near_misses"]
            and primary["table_sha256"]
            == deterministic_rerun["table_sha256"]
        )
        elapsed_before_control = monotonic() - started
        projected_stdout = stdout_bytes() + 12 * 1024
        controls_pass = (
            provenance["controls_exact"]
            and family_control["pass"]
            and not cadence["orbit_recomposition_failures"]
            and deterministic
            and elapsed_before_control < AUDIT_TIMEOUT_SEC
            and projected_stdout < STDOUT_LIMIT_BYTES
        )
        controls_detail = {
            "sha_anchors_exact": provenance["controls_exact"],
            "literal_AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "text_only_blocklist_prefixes":
                TEXT_ONLY_BLOCKLIST_PREFIXES,
            "imported_blocklisted_modules":
                provenance["imported_blocklisted_modules"],
            "family_reconstruction_control":
                family_control["pass"],
            "cadence_orbit_recomposition_failures":
                cadence["orbit_recomposition_failures"],
            "deterministic": deterministic,
            "primary_table_sha256": primary["table_sha256"],
            "rerun_table_sha256":
                deterministic_rerun["table_sha256"],
            "runtime_seconds":
                round(elapsed_before_control, 6),
            "runtime_bound_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_projected_upper_bound_bytes":
                projected_stdout,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        certificates.append(
            certificate(
                "Certificate_F_ANCHORS_BLOCKLIST_DETERMINISM_BOUNDS",
                controls_pass,
                controls_detail,
            )
        )
        if not controls_pass:
            findings.append(
                "CONTROL FAILURE: " + compact(controls_detail)
            )

    for finding in findings:
        emit("FINDING_VERBATIM :: " + finding)

    cadence_refutes = not cadence["pass"]
    provenance_refutes = not provenance["pass"]
    if provenance_refutes and cadence_refutes:
        status = "REFUTED_PROVENANCE_AND_CADENCE"
    elif provenance_refutes:
        status = "REFUTED_PROVENANCE"
    elif cadence_refutes:
        status = "WEAKENED_TO_ONE_CADENCE_CONVENTION"
    elif not recount_pass or not cutoff_pass or not no_values["pass"]:
        status = "REFUTED_NUMERIC_OR_SUPPLY"
    else:
        status = "CONSTRUCTED_WITH_CADENCE_CONVENTION"

    audit_completed_cleanly = (
        provenance["pass"]
        and cadence["pass"]
        and recount_pass
        and cutoff_pass
        and no_values["pass"]
        and controls_pass
    )
    report = {
        "status": status,
        "audit_completed_cleanly": audit_completed_cleanly,
        "primary_claim_survives": not findings,
        "provenance_pass": provenance["pass"],
        "cadence_sensitive": cadence["cadence_sensitive"],
        "recount_pass": recount_pass,
        "cutoff_pass": cutoff_pass,
        "no_per_configuration_values_pass": no_values["pass"],
        "acceptance_keys": primary["acceptance_keys"],
        "classification_counts": primary["classification_counts"],
        "findings_verbatim": tuple(findings),
        "runtime_seconds": round(monotonic() - started, 6),
        "stdout_bytes_before_report": stdout_bytes(),
    }
    report["report_sha256"] = digest(report)
    emit("STATUS :: " + status)
    emit("REPORT :: " + compact(report))
    terminal = (
        "CYCLE796_MONITORED_INDEPENDENT_CHECK_COMPLETE"
        if audit_completed_cleanly
        else "CYCLE796_MONITORED_INDEPENDENT_CHECK_INCOMPLETE"
    )
    emit(terminal)
    final_stdout = stdout_bytes()
    if final_stdout >= STDOUT_LIMIT_BYTES:
        return 1
    return 0 if audit_completed_cleanly else 1


if __name__ == "__main__":
    raise SystemExit(main())
