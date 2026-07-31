#!/usr/bin/env python3
"""Cycle 841: decide which cohort timeline convention landed definitions use.

All four source primaries are SHA-pinned, read as text/AST only, and blocked
from import.  Certificate A formalizes the three requested clocks.
Certificate B classifies each timing-bearing object from its definition,
without receiving the cohort residual targets.  Certificate C performs the
target comparison only after that classification.  Certificate D supplies
the bounded-execution and provenance controls.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1190
STDOUT_LIMIT_BYTES = 149 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from math import lcm
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVENT_ORDER = (0, 2, 1)
TRANSITIONS = ((0, 2), (2, 1))
LCM_SKELETON = lcm(4464, 5952)
COHORT_RESIDUALS = (595, 64)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[1]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[2]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[3]:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[1]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[2]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[3]: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
}
SOURCE_PRIMARY_COMMITS = {
    AUDIT_INPUT_PATHS[0]:
        "4c12650f038de545e60f2d8c62bd303a0d360a84",
    AUDIT_INPUT_PATHS[1]:
        "f3ec9213b4b02457bfc8bc092bf25510297e2813",
    AUDIT_INPUT_PATHS[2]:
        "dca1e252ec1981755f9e54837c1a9f0e2503ccc2",
    AUDIT_INPUT_PATHS[3]:
        "1522d92ec66956621093273f75eb4e4e4d366f7e",
}
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any source primary is accidentally imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_output(*arguments: str) -> str:
    return subprocess.check_output(
        ("git", *arguments), cwd=ROOT, text=True
    ).strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError((name, len(rows)))
    return rows[0]


def loaded_names(node: ast.AST) -> set[str]:
    return {
        child.id for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
    }


def called_leaf_names(node: ast.AST) -> set[str]:
    rows = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if isinstance(child.func, ast.Name):
            rows.add(child.func.id)
        elif isinstance(child.func, ast.Attribute):
            rows.add(child.func.attr)
    return rows


def string_literals(node: ast.AST) -> set[str]:
    return {
        child.value for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    }


def literal_values(node: ast.AST) -> tuple[object, ...]:
    rows = []
    for child in ast.walk(node):
        if not isinstance(child, (ast.Tuple, ast.List, ast.Dict)):
            continue
        try:
            rows.append(ast.literal_eval(child))
        except (TypeError, ValueError):
            pass
    return tuple(rows)


def times_in_event_order(times: dict[int, int]) -> tuple[int, ...]:
    return tuple(times[event] for event in EVENT_ORDER)


def raw_catchup(times: dict[int, int]) -> tuple[int, ...]:
    return tuple(
        times[target] - times[source] - LCM_SKELETON
        for source, target in TRANSITIONS
    )


def source_payloads() -> tuple[
    dict[str, bytes], dict[str, ast.Module], ast.Module
]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    return payloads, trees, self_tree


def clock_definitions(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    tree_832 = trees[AUDIT_INPUT_PATHS[1]]
    tree_833 = trees[AUDIT_INPUT_PATHS[2]]
    tree_835 = trees[AUDIT_INPUT_PATHS[3]]

    resolution_832 = literal_assignment(tree_832, "RESOLUTION_MOMENTS")
    funnel_832 = literal_assignment(tree_832, "FUNNEL_MOMENTS")
    funnel_833 = literal_assignment(tree_833, "FUNNEL_MOMENTS")
    funnel_835 = literal_assignment(tree_835, "FUNNEL_MOMENTS")
    if not all(
        isinstance(row, dict)
        for row in (resolution_832, funnel_832, funnel_833, funnel_835)
    ):
        raise AssertionError("clock dictionaries are not literal")

    resolution = {int(key): int(value)
                  for key, value in resolution_832.items()}
    funnel = {int(key): int(value)
              for key, value in funnel_832.items()}
    funnel_833_int = {
        int(key): int(value) for key, value in funnel_833.items()
    }
    funnel_835_int = {
        int(key): int(value) for key, value in funnel_835.items()
    }

    convention_function = function_node(
        tree_835, "timeline_convention_certificate"
    )
    convention_matrix = next(
        (
            row for row in literal_values(convention_function)
            if row == (
                (14739, 33190, 51110),
                (14734, 33185, 51105),
                (14739, 33189, 51110),
            )
        ),
        None,
    )
    if convention_matrix is None:
        raise AssertionError("Cycle 835 convention matrix missing")
    register_entries = dict(zip(EVENT_ORDER, convention_matrix[2]))

    evolve = function_node(tree_832, "evolve_funnels")
    reconstruct = function_node(tree_833, "reconstruct_funnels")
    tracker = function_node(tree_835, "track_register_trajectories")
    evolve_strings = string_literals(evolve)
    tracker_strings = string_literals(tracker)
    moment_ast = (
        {"advance", "nonclean_mask", "support_at_lane"}
        <= called_leaf_names(evolve)
        and {"RESOLUTION_MOMENTS", "FUNNEL_MOMENTS"}
        <= loaded_names(evolve)
        and {
            "every_earlier_moment_nonclean",
            "veto_at_t_minus_1",
            "all_landed_clean",
        } <= evolve_strings
    )
    funnel_ast = (
        "FUNNEL_MOMENTS" in loaded_names(reconstruct)
        and "advance" in called_leaf_names(reconstruct)
        and {"stop", "updates"} <= string_literals(reconstruct)
    )
    register_ast = (
        "FUNNEL_MOMENTS" in loaded_names(tracker)
        and "histories" in loaded_names(tracker)
        and {
            "final_projection_entry_time",
            "terminal_dwell_ticks",
        } <= tracker_strings
    )

    moment_minus_five_exact = all(
        resolution[event] - funnel[event] == 5
        for event in EVENT_ORDER
    )
    clocks = {
        "MOMENT": {
            "definition":
                "m is the completed-landed-orbit-word boundary at which "
                "the cohort is clean, with every earlier boundary nonclean "
                "and an explicit nonclean veto at m-1.",
            "times_by_event_0_2_1": times_in_event_order(resolution),
            "times": resolution,
            "module_provenance":
                f"{AUDIT_INPUT_PATHS[1]}::evolve_funnels/"
                "RESOLUTION_MOMENTS",
            "ast_identified": moment_ast,
        },
        "MOMENT_MINUS_FIVE": {
            "definition":
                "f=m-5 is the shared-state snapshot after exactly f landed "
                "full-orbit updates, before the five-update cleanliness "
                "resolution tail.",
            "times_by_event_0_2_1": times_in_event_order(funnel),
            "times": funnel,
            "module_provenance": (
                f"{AUDIT_INPUT_PATHS[1]}::FUNNEL_MOMENTS; "
                f"{AUDIT_INPUT_PATHS[2]}::reconstruct_funnels"
            ),
            "ast_identified": funnel_ast,
        },
        "REGISTER_FINAL_ENTRY": {
            "definition":
                "tau is the earliest integer tick from which the 39-field "
                "Cycle-833 rank-edge projection stays equal to its terminal "
                "value through the event's moment-5 funnel tick.",
            "times_by_event_0_2_1":
                times_in_event_order(register_entries),
            "times": register_entries,
            "module_provenance":
                f"{AUDIT_INPUT_PATHS[3]}::track_register_trajectories/"
                "final_projection_entry_time",
            "ast_identified": register_ast,
        },
    }
    local_label_audit = {
        "cycle835_FUNNEL_MOMENT_values":
            times_in_event_order(funnel_835_int),
        "canonical_identity":
            "Cycle835 FUNNEL_MOMENT is Cycle841 MOMENT_MINUS_FIVE",
        "cycle835_local_MOMENT_MINUS_FIVE_values":
            convention_matrix[1],
        "scope_note":
            "The second Cycle835 local label is moment-10 on the Cycle832 "
            "canonical clock and is not one of Cycle841's three requested "
            "definitions; its uniform shift leaves gap arithmetic unchanged.",
    }
    passed = (
        resolution == {0: 14744, 2: 33195, 1: 51115}
        and funnel == {0: 14739, 2: 33190, 1: 51110}
        and funnel_833_int == funnel
        and funnel_835_int == funnel
        and register_entries == {0: 14739, 2: 33189, 1: 51110}
        and moment_minus_five_exact
        and all(row["ast_identified"] for row in clocks.values())
    )
    return {
        "certificate": "A_THREE_CLOCKS_FORMALIZED",
        "clocks": clocks,
        "moment_minus_five_relation_exact_each_event":
            moment_minus_five_exact,
        "cycle835_local_label_audit": local_label_audit,
        "pass": passed,
    }


def forcing_test(
    trees: dict[str, ast.Module],
    clocks: dict[str, object],
) -> dict[str, object]:
    """Classify definitions only; cohort residual targets are not in scope."""

    tree_796 = trees[AUDIT_INPUT_PATHS[0]]
    tree_832 = trees[AUDIT_INPUT_PATHS[1]]
    tree_833 = trees[AUDIT_INPUT_PATHS[2]]
    tree_835 = trees[AUDIT_INPUT_PATHS[3]]

    monitor = function_node(tree_796, "monitor_family")
    advance_boundary = function_node(tree_796, "advance_one_boundary")
    main_796 = function_node(tree_796, "main")
    evolve = function_node(tree_832, "evolve_funnels")
    reconstruct = function_node(tree_833, "reconstruct_funnels")
    field_map = function_node(
        tree_833, "rank_edge_field_map_certificate"
    )
    pulse = function_node(tree_835, "pulse_replay")
    pulse_certificate = function_node(
        tree_835, "pulse_phase_certificate"
    )

    lock_ast = (
        {"RESOLUTION_MOMENTS", "previous_nonclean"}
        <= loaded_names(evolve)
        and {"advance", "nonclean_mask", "support_at_lane"}
        <= called_leaf_names(evolve)
        and {
            "every_earlier_moment_nonclean",
            "veto_at_t_minus_1",
            "all_landed_clean",
        } <= string_literals(evolve)
    )
    monitored_ast = (
        {"advance_one_boundary", "clean_postimage"}
        <= called_leaf_names(monitor)
        and {"first_clean", "horizon"} <= loaded_names(monitor)
        and "apply_semantic" in called_leaf_names(advance_boundary)
        and "orbit_return_boundary" in string_literals(main_796)
        and "DECLARED CONVENTION: orbit_return_boundary governs the "
        "176-key family run" in string_literals(main_796)
    )
    funnel_ast = (
        "FUNNEL_MOMENTS" in loaded_names(reconstruct)
        and "advance" in called_leaf_names(reconstruct)
        and {"xor_support", "apply_named_xor_update"}
        <= called_leaf_names(field_map)
        and "arrival_rank_edge" in string_literals(field_map)
    )
    absolute_clock_names = {
        "RESOLUTION_MOMENTS",
        "FUNNEL_MOMENTS",
        "MOMENT_MINUS_FIVE",
        "final_projection_entry_time",
    }
    pulse_absolute_references = tuple(sorted(
        (loaded_names(pulse) | loaded_names(pulse_certificate))
        & absolute_clock_names
    ))
    pulse_ast = (
        not pulse_absolute_references
        and {"movement", "gate_index"} <= loaded_names(pulse)
        and {"checkpoint", "boundary_row"} <= called_leaf_names(pulse)
        and {
            "canonical_phase_mod_3",
            "aligned_gate",
        } <= string_literals(pulse)
    )

    rows = (
        {
            "object": "lock_law_first_clean_moment",
            "clock": "MOMENT",
            "module_function":
                f"{AUDIT_INPUT_PATHS[1]}::evolve_funnels",
            "ast_identification": lock_ast,
            "behavioral_identification":
                "advance one full orbit, test landed nonclean support; "
                "resolution requires all earlier ticks nonclean, t-1 veto, "
                "and all clean at t",
        },
        {
            "object": "cycle796_monitored_acceptance_tick",
            "clock": "MOMENT",
            "module_function":
                f"{AUDIT_INPUT_PATHS[0]}::monitor_family",
            "ast_identification": monitored_ast,
            "behavioral_identification":
                "horizon increments only after advance_one_boundary applies "
                "one whole composition word; first clean postimage stores "
                "that orbit-return horizon",
        },
        {
            "object": "funnel_family_field_update_semantics",
            "clock": "MOMENT_MINUS_FIVE",
            "module_function":
                f"{AUDIT_INPUT_PATHS[2]}::reconstruct_funnels/"
                "rank_edge_field_map_certificate",
            "ast_identification": funnel_ast,
            "behavioral_identification":
                "snapshots are taken after FUNNEL_MOMENTS shared updates; "
                "the named-field XOR map consumes those snapshots",
        },
        {
            "object": "pulse_phase_bookkeeping",
            "clock": "RELATIVE_MOVEMENT_PHASE_ORIGIN_NEUTRAL",
            "module_function":
                f"{AUDIT_INPUT_PATHS[3]}::pulse_replay",
            "ast_identification": pulse_ast,
            "behavioral_identification":
                "phase is local movement modulo 3 at aligned gate "
                "boundaries; no absolute MOMENT, MOMENT_MINUS_FIVE, or "
                "REGISTER_FINAL_ENTRY name is read",
            "absolute_clock_references": pulse_absolute_references,
            "phase_sequence_movements_0_through_3": (0, 1, 2, 0),
        },
    )
    counts = Counter(row["clock"] for row in rows)
    absolute_counts = {
        name: counts[name]
        for name in (
            "MOMENT", "MOMENT_MINUS_FIVE", "REGISTER_FINAL_ENTRY"
        )
    }
    forced = (
        next(
            (
                name for name, count in absolute_counts.items()
                if count == len(rows)
            ),
            None,
        )
        if len(rows) else None
    )
    split = forced is None
    register_consumers = tuple(
        row["object"] for row in rows
        if row["clock"] == "REGISTER_FINAL_ENTRY"
    )
    passed = (
        all(row["ast_identification"] for row in rows)
        and counts == Counter({
            "MOMENT": 2,
            "MOMENT_MINUS_FIVE": 1,
            "RELATIVE_MOVEMENT_PHASE_ORIGIN_NEUTRAL": 1,
        })
        and split
        and forced is None
        and not register_consumers
        and set(clocks) == {
            "MOMENT", "MOMENT_MINUS_FIVE", "REGISTER_FINAL_ENTRY"
        }
    )
    return {
        "certificate": "B_LANDED_DEFINITION_FORCING_TEST",
        "classification_method":
            "AST plus operational behavior; no residual values are passed "
            "to this function",
        "rows": rows,
        "clock_use_counts": dict(sorted(counts.items())),
        "absolute_clock_use_counts": absolute_counts,
        "register_entry_consumers": register_consumers,
        "forced_clock": forced,
        "verdict":
            "LANDED_DEFINITION_SPLIT_NO_SINGLE_FORCED_CLOCK"
            if split else f"LANDED_FORCED_{forced}",
        "pass": passed,
    }


def accounting_consequence(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
    self_tree: ast.Module,
) -> dict[str, object]:
    clocks = certificate_a["clocks"]
    clock_rows = tuple({
        "clock": name,
        "times_by_event_0_2_1": row["times_by_event_0_2_1"],
        "raw_catchup": raw_catchup(row["times"]),
        "residuals_for_comparison_only": COHORT_RESIDUALS,
        "signed_raw_minus_residual": tuple(
            observed - target
            for observed, target in zip(
                raw_catchup(row["times"]), COHORT_RESIDUALS
            )
        ),
        "relation":
            "EQUALS_RESIDUALS"
            if raw_catchup(row["times"]) == COHORT_RESIDUALS
            else "DIFFERS_FROM_RESIDUALS",
    } for name, row in clocks.items())
    row_by_clock = {row["clock"]: row for row in clock_rows}
    per_object = tuple({
        "object": row["object"],
        "clock": row["clock"],
        "raw_catchup":
            row_by_clock[row["clock"]]["raw_catchup"]
            if row["clock"] in row_by_clock else None,
        "relation":
            row_by_clock[row["clock"]]["relation"]
            if row["clock"] in row_by_clock
            else "NOT_APPLICABLE_ORIGIN_NEUTRAL_PHASE",
    } for row in certificate_b["rows"])
    forcing_node = function_node(self_tree, "forcing_test")
    forbidden_selection_names = (
        loaded_names(forcing_node)
        & {"COHORT_RESIDUALS", "raw_catchup"}
    )
    landed_absolute_clock_ids = {
        row["clock"] for row in certificate_b["rows"]
        if row["clock"] in row_by_clock
    }
    landed_absolute_rows = tuple(
        row_by_clock[name] for name in sorted(landed_absolute_clock_ids)
    )
    passed = (
        not forbidden_selection_names
        and certificate_b["forced_clock"] is None
        and landed_absolute_clock_ids
        == {"MOMENT", "MOMENT_MINUS_FIVE"}
        and all(
            row["raw_catchup"] == COHORT_RESIDUALS
            for row in landed_absolute_rows
        )
        and row_by_clock["REGISTER_FINAL_ENTRY"]["raw_catchup"]
        == (594, 65)
        and row_by_clock["REGISTER_FINAL_ENTRY"][
            "signed_raw_minus_residual"
        ] == (-1, 1)
        and not certificate_b["register_entry_consumers"]
    )
    return {
        "certificate": "C_COHORT_GAP_ACCOUNTING",
        "formula": "raw(s,t)=t_target-t_source-lcm(4464,5952)",
        "lcm": LCM_SKELETON,
        "clock_rows": clock_rows,
        "per_object_rows": per_object,
        "target_aware_forcing_names": tuple(
            sorted(forbidden_selection_names)
        ),
        "selection_used_residual_targets": bool(
            forbidden_selection_names
        ),
        "status":
            "NO_SINGLE_LABEL_FORCED; ALL_LANDED_ABSOLUTE_READINGS_EQUAL_"
            "595_64; REGISTER_ENTRY_594_65_HAS_ZERO_LANDED_CONSUMERS",
        "consequence":
            "The definitions are plural (moment versus moment-5), but their "
            "uniform five-tick offset cancels in both gaps.  Every landed "
            "absolute cohort-timing consumer therefore gives raw {595,64}, "
            "exactly the residuals.  Register entry gives {594,65} and is "
            "not selected by any audited landed definition.",
        "pass": passed,
    }


def source_controls(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
    self_tree: ast.Module,
) -> dict[str, object]:
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    pinned_commit_blobs = {}
    commit_resolution = {}
    for path, commit in SOURCE_PRIMARY_COMMITS.items():
        commit_resolution[path] = git_output(
            "rev-parse", f"{commit}^{{commit}}"
        )
        pinned_commit_blobs[path] = git_output(
            "rev-parse", f"{commit}:{path}"
        )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    direct_frontier_from_imports = tuple(sorted(
        node.module
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module is not None
        and node.module.startswith("frontier_cycle")
    ))
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    result = {
        "certificate": "D_CONTROLS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            all(not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS)
            and len(payloads) == len(AUDIT_INPUT_PATHS)
            and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
        "source_mode": {
            path: "TEXT_AST_ONLY_BLOCKLISTED"
            for path in AUDIT_INPUT_PATHS
        },
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "source_primary_commits": SOURCE_PRIMARY_COMMITS,
        "resolved_source_commits": commit_resolution,
        "pinned_commit_blobs": pinned_commit_blobs,
        "current_git_head": git_output("rev-parse", "HEAD"),
        "current_branch": git_output(
            "rev-parse", "--abbrev-ref", "HEAD"
        ),
        "blocklisted_modules": BLOCKLISTED_MODULES,
        "blocklisted_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "direct_frontier_from_imports": direct_frontier_from_imports,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdlib_only_runner": (
            not direct_frontier_imports and not direct_frontier_from_imports
        ),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 7
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and pinned_commit_blobs == EXPECTED_GIT_BLOBS
        and commit_resolution == SOURCE_PRIMARY_COMMITS
        and not result["blocklisted_modules_loaded"]
        and not result["firewall_hits"]
        and result["stdlib_only_runner"]
        and AUDIT_TIMEOUT_SEC < 1200
        and STDOUT_LIMIT_BYTES < 150 * 1024
        and set(trees) == set(AUDIT_INPUT_PATHS)
    )
    return result


def build_science(
    trees: dict[str, ast.Module],
    self_tree: ast.Module,
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    certificate_a = clock_definitions(trees)
    certificate_b = forcing_test(trees, certificate_a["clocks"])
    certificate_c = accounting_consequence(
        certificate_a, certificate_b, self_tree
    )
    return certificate_a, certificate_b, certificate_c


def render(
    certificates: dict[str, object],
    summary: dict[str, object],
) -> str:
    lines = [
        f"{name} :: {compact(value)}"
        for name, value in certificates.items()
    ]
    lines.append("SUMMARY :: " + compact(summary))
    lines.append(str(summary["terminal"]))
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    payloads, trees, self_tree = source_payloads()
    first = build_science(trees, self_tree)
    second = build_science(trees, self_tree)
    deterministic = digest(first) == digest(second)
    certificate_a, certificate_b, certificate_c = first
    certificate_d = source_controls(payloads, trees, self_tree)
    science_pass = all(
        certificate["pass"]
        for certificate in (
            certificate_a, certificate_b, certificate_c, certificate_d
        )
    )
    elapsed = monotonic() - started
    runtime_pass = elapsed < AUDIT_TIMEOUT_SEC
    controls = {
        "science_digest": digest(first),
        "duplicate_science_digest": digest(second),
        "deterministic_duplicate_exact": deterministic,
        "runtime_seconds": round(elapsed, 6),
        "runtime_below_1200_seconds": elapsed < 1200,
        "runtime_below_declared_timeout": runtime_pass,
        "stdout_bytes": 0,
        "stdout_below_150KB": False,
        "pass": False,
    }
    certificate_d["execution"] = controls
    certificates = {
        "CERTIFICATE_A": certificate_a,
        "CERTIFICATE_B": certificate_b,
        "CERTIFICATE_C": certificate_c,
        "CERTIFICATE_D": certificate_d,
    }
    summary = {
        "cycle": 841,
        "forced_clock": certificate_b["forced_clock"],
        "verdict": certificate_b["verdict"],
        "clock_use_counts": certificate_b["clock_use_counts"],
        "landed_absolute_raw_catchup": (595, 64),
        "register_entry_raw_catchup": (594, 65),
        "accounting_status": certificate_c["status"],
        "pass": False,
        "terminal": "CYCLE841_DECIDING_THE_TICK_HONEST_FAIL",
    }

    output = ""
    for _attempt in range(12):
        output = render(certificates, summary)
        output_bytes = len(output.encode("utf-8"))
        stdout_pass = output_bytes < STDOUT_LIMIT_BYTES
        final_pass = (
            science_pass and deterministic and runtime_pass and stdout_pass
        )
        new_terminal = (
            "CYCLE841_DECIDING_THE_TICK_SPLIT_PASS"
            if final_pass
            else "CYCLE841_DECIDING_THE_TICK_HONEST_FAIL"
        )
        stable = (
            controls["stdout_bytes"] == output_bytes
            and controls["stdout_below_150KB"] == stdout_pass
            and controls["pass"] == final_pass
            and summary["pass"] == final_pass
            and summary["terminal"] == new_terminal
        )
        controls["stdout_bytes"] = output_bytes
        controls["stdout_below_150KB"] = stdout_pass
        controls["pass"] = final_pass
        certificate_d["pass"] = bool(
            certificate_d["pass"] and runtime_pass and stdout_pass
        )
        summary["pass"] = final_pass
        summary["terminal"] = new_terminal
        if stable:
            break
    output = render(certificates, summary)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        return 2
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
