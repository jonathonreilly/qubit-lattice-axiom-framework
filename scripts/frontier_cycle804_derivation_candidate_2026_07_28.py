#!/usr/bin/env python3
"""Cycle 804 v2: corrected executable exact-time derivation candidate.

This runner does not land a law.  It checks a six-step argument: records form
globally, without a per-epoch or per-configuration schedule; at the bounded
landed multi-source scope, the Record axiom's admissibility clause is evaluated
by the seven-condition battery at the 792/796 surface, with four conditions
explicit on the Cycle-758 raw surface.  No actuality or probability is claimed,
and every premise needed by the candidate has a loud certificate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle790_horizon_independent_check_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
    "scripts/frontier_cycle791_resolution_independent_check_2026_07_28.py",
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle758_selector_multisource_2026_07_28 as F758


EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[3]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[4]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[5]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[6]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[7]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    AUDIT_INPUT_PATHS[8]:
        "cacd49aadb9e9dcb71b26cc910df6a40d0ca592b904a882dea13fe5aacab14e4",
    AUDIT_INPUT_PATHS[9]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    AUDIT_INPUT_PATHS[10]:
        "40dfd1f10aae8480a3192bcea8906dceada4add7917e32989963c9ab1aa41889",
    AUDIT_INPUT_PATHS[11]:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    AUDIT_INPUT_PATHS[12]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    AUDIT_INPUT_PATHS[13]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
FULL_BATTERY = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
RAW_758_CONDITIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
SUPPLIED_792_CONDITIONS = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
)
RECORD_AXIOM_SHA256 = (
    "69d69c0d59162b5fdf2f293a695d0094124006baf0efb3f719fc3fa0df106384"
)
S1_PLAIN_READING = (
    "The Record axiom asserts globally that records form. It schedules no "
    "formation for any epoch or configuration; only where and when remain "
    "open."
)
S1_FORMATION_STATUS = {
    "formation_asserted_globally": True,
    "formation_forced_for_any_epoch": False,
}
S2_IDENTIFICATION_CLAIM = (
    "The seven-condition battery equals landed admissibility at the 792/796 "
    "surface: four conditions are explicit exclusions on Cycle-758's raw "
    "landed surface, while census membership, pairwise separation, and "
    "synchronization are supplied through the preconstructed domain."
)
ONE_SHARED_FREEDOM_RETRACTION = "RETRACTED"
S5_FREEDOM_CLAIM = (
    "The evaluation cadence and the formation-site schedule are independent "
    "freedom axes."
)
S5_WITNESS_RECORD_SHA256 = (
    "d5c1d153891b6f4b0e7556ea6d24d50ae69ce0dc8541a4767bd5255ace51e641",
    "7925ef04f5a1b37758c926c17641d1d3ffacbcb75b6e23b7bb8ee3081b94779b",
)
FROZEN_CANDIDATE = (
    "At the landed scope, when a record forms in a multi-source epoch it locks "
    "the unique accepted alternative at its first-clean moment — the "
    "acceptance law is the Record axiom's admissibility requirement evaluated "
    "on the landed dynamics, with admissibility operationally identified as "
    "the seven-condition battery at the 792/796 surface (four conditions "
    "758-raw). The axiom asserts that records form; it schedules nothing. The "
    "remaining freedom is at least two independent axes — the evaluation "
    "cadence and the formation-site schedule — both witnessed."
)

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


def certificate(name: str, passed: bool, detail: object) -> bool:
    if name in CERTIFICATES:
        raise AssertionError(("duplicate certificate", name))
    CERTIFICATES[name] = bool(passed)
    emit(f"{'PASS' if passed else 'FAIL'} {name}", detail)
    return bool(passed)


PINNED_GIT_CITATIONS = (
    {
        "name": "Cycle796",
        "commit": "4c12650f038de545e60f2d8c62bd303a0d360a84",
        "path":
            "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
        "sha256":
            "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
        "git_blob_sha1": "eb2f34cd78fae3ce579d426df2ffe62832003504",
    },
    {
        "name": "Cycle799",
        "commit": "c21af306f030a7296fae887dfb320e58c29c2025",
        "path":
            "scripts/frontier_cycle799_cadence_preference_2026_07_28.py",
        "sha256":
            "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
        "git_blob_sha1": "49964118073bcd784af0f2e4c03723a9d3bd47e9",
    },
    {
        "name": "Cycle788",
        "commit": "608c1a8adc0f321c0f2320b3e089828506e04329",
        "path":
            "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
        "sha256":
            "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
        "git_blob_sha1": "1e691cb4b2477f86e1c81e017de44b53c4edec88",
    },
    {
        "name": "Cycle750_flags",
        "commit": "3d994fec5a83a1fcff7d8c1b1201734ca0fd2d14",
        "path":
            "docs/ACTUAL_SELECTOR_STRETCH_CYCLE750_BOUNDED_THEOREM_NOTE_"
            "2026-07-28.md",
        "sha256":
            "6dacefd5f2f92b431c6fcb239c024e16985ff1910a462d2e240f33234b28d784",
        "git_blob_sha1": "55ab20515913ca95bd64fb3dc289c34562eae4b9",
    },
)


def file_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def git_blob_sha1(payload: bytes) -> str:
    framed = b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload
    return sha1(framed).hexdigest()


def git_show(commit: str, relative_path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{relative_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def disk_and_git_anchor_audit() -> dict[str, Any]:
    disk = {
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
    git_rows = {}
    git_payloads = {}
    for citation in PINNED_GIT_CITATIONS:
        payload = git_show(citation["commit"], citation["path"])
        git_payloads[citation["name"]] = payload.decode("utf-8")
        observed_commit = subprocess.run(
            ["git", "rev-parse", citation["commit"]],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        git_rows[citation["name"]] = {
            "commit": observed_commit,
            "path": citation["path"],
            "sha256": sha256(payload).hexdigest(),
            "git_blob_sha1": git_blob_sha1(payload),
        }

    expected_git = {
        citation["name"]: {
            "commit": citation["commit"],
            "path": citation["path"],
            "sha256": citation["sha256"],
            "git_blob_sha1": citation["git_blob_sha1"],
        }
        for citation in PINNED_GIT_CITATIONS
    }
    runner_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments: dict[str, ast.AST] = {}
    for node in runner_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
    audit_node = assignments.get("AUDIT_INPUT_PATHS")
    declared_node = assignments.get("DECLARED_INPUT_PATHS")
    literal_tuple = bool(
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
    observed_disk_sha = {
        path: row["sha256"] for path, row in disk.items()
    }
    return {
        "pass": (
            literal_tuple
            and all(row["exists"] for row in disk.values())
            and observed_disk_sha == EXPECTED_SHA256
            and git_rows == expected_git
        ),
        "literal_AUDIT_INPUT_PATHS": literal_tuple,
        "disk": disk,
        "git": git_rows,
        "git_payloads": git_payloads,
    }


RECORD_AXIOM_VERBATIM = (
    "Records form.\n\n"
    "When present, a record locks exactly one admissible local possibility. A\n"
    "site never carries more than one record; records are permanent.\n\n"
    "Only records are readable. A readout value is determined by record content\n"
    "alone. For any finite collection of pairwise-disjoint records, scalar "
    "readout\n"
    "`I` is additive, with `I(empty)=0`."
)


def extract_record_axiom_quote() -> str:
    """Read the minimal-axiom file solely to extract the Record axiom text."""

    text = file_bytes(AUDIT_INPUT_PATHS[0]).decode("utf-8")
    heading = "### Record / Fixed Reality\n\n"
    start = text.index(heading) + len(heading)
    end = text.index("\n\n## ", start)
    return text[start:end]


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    node = next(
        item
        for item in tree.body
        if isinstance(item, ast.FunctionDef) and item.name == name
    )
    return node


def top_level_assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return node.value
    raise KeyError(name)


def assigned_dict_keys(function: ast.FunctionDef, variable: str) -> tuple[str, ...]:
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == variable
            for target in node.targets
        ):
            continue
        if isinstance(node.value, ast.Dict):
            keys = []
            for key in node.value.keys:
                if not isinstance(key, ast.Constant) or not isinstance(
                    key.value, str
                ):
                    raise AssertionError((function.name, variable, key))
                keys.append(key.value)
            return tuple(keys)
    raise KeyError((function.name, variable))


def s2_battery_identification(git_payloads: dict[str, str]) -> dict[str, Any]:
    trees = {
        path: ast.parse(file_bytes(path), filename=path)
        for path in (AUDIT_INPUT_PATHS[4], AUDIT_INPUT_PATHS[11])
    }
    cycle796_tree = ast.parse(
        git_payloads["Cycle796"], filename="Cycle796:pinned"
    )

    battery_796 = tuple(
        ast.literal_eval(top_level_assignment(cycle796_tree, "BATTERY_CONDITIONS"))
    )
    conditions_758 = assigned_dict_keys(
        named_function(
            trees[AUDIT_INPUT_PATHS[4]],
            "multisource_enforcement_lineage_selector",
        ),
        "conditions",
    )
    conditions_792 = assigned_dict_keys(
        named_function(
            trees[AUDIT_INPUT_PATHS[11]], "base_battery_evaluation"
        ),
        "conditions",
    )
    reconstructed_792 = tuple((*conditions_792, "clean_postimage"))
    raw_module = AUDIT_INPUT_PATHS[4]
    surface_module = AUDIT_INPUT_PATHS[11]
    four_raw_provenance = {
        name: {
            "module": raw_module,
            "constant":
                f"multisource_enforcement_lineage_selector.conditions[{name!r}]",
        }
        for name in RAW_758_CONDITIONS
    }
    three_supplied_provenance = {
        name: {
            "module": surface_module,
            "constant": f"base_battery_evaluation.conditions[{name!r}]",
        }
        for name in SUPPLIED_792_CONDITIONS
    }
    surface_provenance = {
        "Cycle792_module": surface_module,
        "Cycle792_constant":
            "base_battery_evaluation.conditions + "
            "selector_conditions.conditions['clean_postimage']",
        "Cycle796_module":
            "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
        "Cycle796_constant": "BATTERY_CONDITIONS",
    }
    exact_identity = (
        len(battery_796) == len(FULL_BATTERY)
        and set(battery_796) == set(FULL_BATTERY)
        and set(reconstructed_792) == set(FULL_BATTERY)
        and conditions_758 == RAW_758_CONDITIONS
        and tuple(
            name for name in reconstructed_792
            if name not in conditions_758
        ) == SUPPLIED_792_CONDITIONS
    )
    result = {
        "operational_identification": S2_IDENTIFICATION_CLAIM,
        "scope": "792/796 surface",
        "full_battery": FULL_BATTERY,
        "Cycle796_battery_conditions": battery_796,
        "Cycle792_reconstructed_battery": reconstructed_792,
        "four_conditions_758_raw": conditions_758,
        "three_conditions_preconstructed": SUPPLIED_792_CONDITIONS,
        "four_raw_module_constant_provenance": four_raw_provenance,
        "three_supplied_module_constant_provenance":
            three_supplied_provenance,
        "surface_module_constant_provenance": surface_provenance,
    }
    result["pass"] = (
        exact_identity
        and tuple(four_raw_provenance) == RAW_758_CONDITIONS
        and tuple(three_supplied_provenance) == SUPPLIED_792_CONDITIONS
        and all(
            row["module"] and row["constant"]
            for row in (
                *four_raw_provenance.values(),
                *three_supplied_provenance.values(),
            )
        )
    )
    return result


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def expected_synchronization_trace(
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


def family_base_row(
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
    census_members: frozenset[tuple[int, ...]],
) -> dict[str, Any]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    word = M736.synchronous_composition_word(program, positions)
    expected = K.A.apply_semantic(before, word)
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    config = tuple(
        int(station in positions) for station in range(RING_STATIONS)
    )
    conditions = {
        "census_membership": positions in census_members,
        "pairwise_separation": M736.is_pairwise_separated(config),
        "synchronization":
            trace == expected_synchronization_trace(positions),
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


def worked_family_sample(
    *,
    k: int,
    event: int,
    representative: tuple[int, ...],
    target: tuple[int, ...],
    moment: int,
) -> dict[str, Any]:
    fixture = next(
        row for row in F750.k_epoch_fixtures(FIXTURE_BANKS)
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
    census = M736.configuration_census()["configurations"]
    census_members = frozenset(
        M736.occupied_sites(config)
        for config in census
        if sum(config) == k
    )
    rows = {
        positions: family_base_row(
            program, before, positions, census_members
        )
        for positions in alternatives
    }
    clean_timeline: dict[int, list[tuple[int, ...]]] = {}
    first_clean: dict[tuple[int, ...], int | None] = {
        positions: None for positions in alternatives
    }
    state_hashes: dict[
        tuple[int, ...], dict[int, str]
    ] = {positions: {} for positions in alternatives}

    for positions in alternatives:
        state = rows[positions]["after"]
        word = rows[positions]["word"]
        for horizon_t in range(moment + 1):
            clean = F758.clean_postimage(state, FIXTURE_BANKS)
            if clean:
                clean_timeline.setdefault(horizon_t, []).append(positions)
                if first_clean[positions] is None:
                    first_clean[positions] = horizon_t
            if horizon_t in (moment - 1, moment):
                state_hashes[positions][horizon_t] = sha256(
                    str(state).encode("ascii")
                ).hexdigest()
            if horizon_t < moment:
                state = K.A.apply_semantic(state, word)

    first_clean_rows = tuple(
        sorted(
            (
                (positions, first)
                for positions, first in first_clean.items()
                if first is not None
            ),
            key=lambda row: (row[1], row[0]),
        )
    )
    target_conditions = {
        **rows[target]["conditions"],
        "clean_postimage": target in clean_timeline.get(moment, ()),
    }
    previous_survivors = tuple(
        clean_timeline.get(moment - 1, ())
    )
    target_survivors = tuple(clean_timeline.get(moment, ()))
    every_pass_is_first_clean_through_target = all(
        first_clean[positions] == horizon_t
        for horizon_t, positions_rows in clean_timeline.items()
        for positions in positions_rows
    )
    one_at_a_time_through_target = all(
        len(positions_rows) == 1
        for positions_rows in clean_timeline.values()
    )
    result = {
        "k": k,
        "event": event,
        "direction": direction,
        "representative": representative,
        "target": target,
        "moment": moment,
        "moment_minus_one": moment - 1,
        "alternatives": alternatives,
        "alternative_count": len(alternatives),
        "all_non_postimage_conditions_pass": all(
            all(row["conditions"].values()) for row in rows.values()
        ),
        "first_clean_rows_through_target": first_clean_rows,
        "clean_timeline_through_target": tuple(
            (horizon_t, tuple(positions_rows))
            for horizon_t, positions_rows in sorted(clean_timeline.items())
        ),
        "moment_minus_one_survivors": previous_survivors,
        "moment_survivors": target_survivors,
        "target_full_battery": target_conditions,
        "target_state_hashes": state_hashes[target],
        "every_pass_is_first_clean_through_target":
            every_pass_is_first_clean_through_target,
        "one_at_a_time_through_target": one_at_a_time_through_target,
    }
    result["pass"] = (
        len(alternatives) == RING_STATIONS
        and result["all_non_postimage_conditions_pass"]
        and tuple(target_conditions) == FULL_BATTERY
        and all(target_conditions.values())
        and first_clean[target] == moment
        and not previous_survivors
        and target_survivors == (target,)
        and every_pass_is_first_clean_through_target
        and one_at_a_time_through_target
    )
    return result


def worked_fact_samples() -> tuple[dict[str, Any], ...]:
    return (
        worked_family_sample(
            k=2,
            event=3,
            representative=(0, 2),
            target=(1, 10),
            moment=252,
        ),
        worked_family_sample(
            k=3,
            event=2,
            representative=(0, 2, 5),
            target=(0, 2, 5),
            moment=444,
        ),
    )


def assignment_within(function: ast.FunctionDef, name: str) -> ast.AST:
    for node in ast.walk(function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return node.value
    raise KeyError((function.name, name))


def relevant_schedule_identifiers(
    tree: ast.Module, function_names: tuple[str, ...]
) -> tuple[str, ...]:
    identifiers = set()
    for function_name in function_names:
        function = named_function(tree, function_name)
        for node in ast.walk(function):
            if isinstance(node, ast.Name):
                identifiers.add(node.id)
            elif isinstance(node, ast.Attribute):
                identifiers.add(node.attr)
    return tuple(
        sorted(
            name
            for name in identifiers
            if any(
                token in name.lower()
                for token in ("form_record", "record_form", "formation_schedule")
            )
        )
    )


def single_source_record_witness(event: int) -> dict[str, Any]:
    fixture = next(
        row for row in F750.k_epoch_fixtures(FIXTURE_BANKS)
        if row[0] == event
    )
    _event, direction, program, before, expected = fixture
    positions = (0,)
    tokens = (1,) + (0,) * (len(program) - 1)
    zeros = (0,) * len(program)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
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
            F758.clean_postimage(after, FIXTURE_BANKS),
    }
    return {
        "event": event,
        "direction": direction,
        "selected_positions": positions,
        "conditions": conditions,
        "record_content_sha256":
            sha256(str(after).encode("ascii")).hexdigest(),
    }


def s5_freedom_identification(axiom_quote: str) -> dict[str, Any]:
    record_event_0 = single_source_record_witness(0)
    record_event_1 = single_source_record_witness(1)
    fixed_cadence = "orbit_return_boundary"
    setting_a = {
        "cadence_axis": fixed_cadence,
        "formation_site_schedule": ("two-bank single-source event 0",),
        "formation_records": (
            record_event_0["record_content_sha256"],
        ),
    }
    setting_b = {
        "cadence_axis": fixed_cadence,
        "formation_site_schedule": ("two-bank single-source event 1",),
        "formation_records": (
            record_event_1["record_content_sha256"],
        ),
    }
    both_lawful = all(
        all(record["conditions"].values())
        for record in (record_event_0, record_event_1)
    )
    cadence_fixed = (
        setting_a["cadence_axis"] == setting_b["cadence_axis"]
    )
    formation_site_schedule_differs = (
        setting_a["formation_site_schedule"]
        != setting_b["formation_site_schedule"]
    )
    records_distinct = (
        setting_a["formation_records"] != setting_b["formation_records"]
    )
    independent_axes_witness = (
        both_lawful
        and cadence_fixed
        and formation_site_schedule_differs
        and records_distinct
    )
    result = {
        "single_source_event_0": record_event_0,
        "single_source_event_1": record_event_1,
        "lawful_composite_setting_A": setting_a,
        "lawful_composite_setting_B": setting_b,
        "fixed_evaluation_cadence": cadence_fixed,
        "formation_site_schedule_differs":
            formation_site_schedule_differs,
        "distinct_lawful_records": records_distinct,
        "independent_axes_witness": independent_axes_witness,
        "freedom_count_lower_bound": 2,
        "freedom_identification": S5_FREEDOM_CLAIM,
        "formation_asserted_globally": "Records form." in axiom_quote,
        "formation_forced": False,
        "one_shared_freedom_claim": ONE_SHARED_FREEDOM_RETRACTION,
        "actuality_claim": False,
        "probability_claim": False,
    }
    result["pass"] = (
        independent_axes_witness
        and (
            record_event_0["record_content_sha256"],
            record_event_1["record_content_sha256"],
        ) == S5_WITNESS_RECORD_SHA256
        and result["formation_asserted_globally"] is True
        and result["formation_forced"] is False
        and result["one_shared_freedom_claim"] == "RETRACTED"
        and result["actuality_claim"] is False
        and result["probability_claim"] is False
    )
    return result


S4_CONDITIONAL = (
    "IF a record forms in a landed multi-source epoch, THEN, because the "
    "locked possibility must be admissible and landed admissibility is the "
    "full battery, it locks the unique accepted alternative at a first-clean "
    "moment. This conditional does not assert that a record forms."
)


def conditional_logic(
    record_forms: bool,
    *,
    axiom_lock_requires_admissible: bool,
    admissibility_is_full_battery: bool,
    battery_unique_at_first_clean: bool,
) -> str:
    if not record_forms:
        return "ANTECEDENT_FALSE_NO_FORMATION_CONCLUSION"
    if not (
        axiom_lock_requires_admissible
        and admissibility_is_full_battery
        and battery_unique_at_first_clean
    ):
        raise AssertionError("conditional conclusion lacks a checked premise")
    return "LOCKS_UNIQUE_ACCEPTED_ALTERNATIVE_AT_FIRST_CLEAN"


def main() -> int:
    started = monotonic()
    anchors_before = disk_and_git_anchor_audit()

    axiom_quote = extract_record_axiom_quote()
    emit("S1_AXIOM_TEXT_BEGIN")
    OUTPUT_LINES.extend(axiom_quote.splitlines())
    emit("S1_AXIOM_TEXT_END")
    formation_asserted_globally = "Records form." in axiom_quote
    formation_forced_for_any_epoch = any(
        needle in axiom_quote.lower()
        for needle in (
            "every epoch",
            "each epoch",
            "any epoch",
            "every configuration",
            "each configuration",
            "any configuration",
        )
    )
    s1_plain_reading = S1_PLAIN_READING
    s1_pass = certificate(
        "S1_RECORD_AXIOM_VERBATIM_AND_PLAIN_READING",
        (
            axiom_quote == RECORD_AXIOM_VERBATIM
            and sha256(axiom_quote.encode("utf-8")).hexdigest()
            == RECORD_AXIOM_SHA256
            and axiom_quote.startswith("Records form.\n\nWhen present,")
            and "exactly one admissible local possibility" in axiom_quote
            and formation_asserted_globally
            is S1_FORMATION_STATUS["formation_asserted_globally"]
            and formation_forced_for_any_epoch
            is S1_FORMATION_STATUS["formation_forced_for_any_epoch"]
        ),
        {
            "source": AUDIT_INPUT_PATHS[0],
            "quote_sha256": sha256(axiom_quote.encode("utf-8")).hexdigest(),
            "expected_quote_sha256": RECORD_AXIOM_SHA256,
            "plain_reading": s1_plain_reading,
            "formation_asserted_globally": formation_asserted_globally,
            "formation_forced_for_any_epoch":
                formation_forced_for_any_epoch,
        },
    )

    s2 = s2_battery_identification(anchors_before["git_payloads"])
    s2_pass = certificate(
        "S2_BATTERY_EQUALS_LANDED_ADMISSIBILITY",
        s2["pass"],
        s2,
    )

    first_samples = worked_fact_samples()
    second_samples = worked_fact_samples()
    sample_deterministic = first_samples == second_samples
    s3_pass = certificate(
        "S3_WORKED_FIRST_CLEAN_SELECTIONS_T252_T444",
        (
            sample_deterministic
            and all(sample["pass"] for sample in first_samples)
            and tuple(sample["moment"] for sample in first_samples)
            == (252, 444)
            and tuple(
                sample["moment_minus_one_survivors"]
                for sample in first_samples
            )
            == ((), ())
            and tuple(
                sample["moment_survivors"] for sample in first_samples
            )
            == (((1, 10),), ((0, 2, 5),))
        ),
        {
            "lineage": (
                "Cycles 792/794 establish the k=2 moments; Cycle 798 "
                "establishes the k=3 t=444 instance. This runner directly "
                "re-verifies the requested bounded samples, so no unavailable "
                "Cycle-800 module is used as a premise."
            ),
            "samples": first_samples,
            "deterministic": sample_deterministic,
            "first_sha256": digest(first_samples),
            "rerun_sha256": digest(second_samples),
        },
    )

    premise_list = (
        "S1: conditional lock requires an admissible possibility",
        "S2: landed multi-source admissibility is the full battery",
        "S3: bounded family passes are unique first-clean events",
    )
    false_antecedent = conditional_logic(
        False,
        axiom_lock_requires_admissible=s1_pass,
        admissibility_is_full_battery=s2_pass,
        battery_unique_at_first_clean=s3_pass,
    )
    true_antecedent = conditional_logic(
        True,
        axiom_lock_requires_admissible=s1_pass,
        admissibility_is_full_battery=s2_pass,
        battery_unique_at_first_clean=s3_pass,
    )
    s4_pass = certificate(
        "S4_PURE_CONDITIONAL_INFERENCE",
        (
            all((s1_pass, s2_pass, s3_pass))
            and S4_CONDITIONAL.startswith("IF a record forms")
            and S4_CONDITIONAL.endswith(
                "This conditional does not assert that a record forms."
            )
            and false_antecedent == "ANTECEDENT_FALSE_NO_FORMATION_CONCLUSION"
            and true_antecedent
            == "LOCKS_UNIQUE_ACCEPTED_ALTERNATIVE_AT_FIRST_CLEAN"
        ),
        {
            "premises": premise_list,
            "conditional": S4_CONDITIONAL,
            "false_antecedent_control": false_antecedent,
            "true_antecedent_consequence": true_antecedent,
            "formation_forced": False,
        },
    )

    s5 = s5_freedom_identification(axiom_quote)
    emit("S5_RECORD_EVENT_0_VERBATIM", s5["single_source_event_0"])
    emit("S5_RECORD_EVENT_1_VERBATIM", s5["single_source_event_1"])
    s5_pass = certificate(
        "S5_TWO_INDEPENDENT_FREEDOM_AXES",
        s5["pass"],
        s5,
    )

    assembled = all((s1_pass, s2_pass, s3_pass, s4_pass, s5_pass))
    status_keys = {
        "derivation_candidate_assembled": assembled,
        "proposed_not_landed": True,
        "axiom_update_triggered": False,
        "formation_forced": False,
        "formation_asserted_globally": True,
        "one_shared_freedom_claim": ONE_SHARED_FREEDOM_RETRACTION,
    }
    candidate_guardrails = (
        FROZEN_CANDIDATE
        == (
            "At the landed scope, when a record forms in a multi-source epoch "
            "it locks the unique accepted alternative at its first-clean "
            "moment — the acceptance law is the Record axiom's admissibility "
            "requirement evaluated on the landed dynamics, with admissibility "
            "operationally identified as the seven-condition battery at the "
            "792/796 surface (four conditions 758-raw). The axiom asserts that "
            "records form; it schedules nothing. The remaining freedom is at "
            "least two independent axes — the evaluation cadence and the "
            "formation-site schedule — both witnessed."
        )
        and "actuality" not in FROZEN_CANDIDATE.lower()
        and "probability" not in FROZEN_CANDIDATE.lower()
        and status_keys["proposed_not_landed"] is True
        and status_keys["axiom_update_triggered"] is False
        and status_keys["formation_forced"] is False
        and status_keys["formation_asserted_globally"] is True
        and status_keys["one_shared_freedom_claim"] == "RETRACTED"
    )
    emit("S6_FROZEN_DERIVATION_CANDIDATE", FROZEN_CANDIDATE)
    emit("S6_STATUS_KEYS", status_keys)
    s6_pass = certificate(
        "S6_FROZEN_CANDIDATE_AND_HONEST_STATUS",
        assembled and candidate_guardrails,
        {
            "candidate": FROZEN_CANDIDATE,
            "status_keys": status_keys,
            "formation_forced_scope": "per-epoch",
            "no_actuality": True,
            "no_probability": True,
        },
    )

    anchors_after = disk_and_git_anchor_audit()
    sources_unchanged = (
        {
            "disk": anchors_before["disk"],
            "git": anchors_before["git"],
        }
        == {
            "disk": anchors_after["disk"],
            "git": anchors_after["git"],
        }
    )
    elapsed = monotonic() - started
    preliminary = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "certificates": CERTIFICATES,
        "determinism_sha256": digest(first_samples),
        "runtime_seconds": round(elapsed, 6),
        **status_keys,
    }
    projected_stdout_bytes = (
        len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8"))
        + len(compact(preliminary).encode("utf-8"))
        + 8192
    )
    controls_pass = certificate(
        "CONTROLS_LITERAL_PATHS_SHA_DETERMINISM_AND_BOUNDS",
        (
            anchors_before["pass"]
            and anchors_after["pass"]
            and sources_unchanged
            and sample_deterministic
            and elapsed < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < STDOUT_LIMIT_BYTES
        ),
        {
            "literal_AUDIT_INPUT_PATHS":
                anchors_before["literal_AUDIT_INPUT_PATHS"],
            "all_disk_inputs_exist": all(
                row["exists"] for row in anchors_before["disk"].values()
            ),
            "disk_sha256": {
                path: row["sha256"]
                for path, row in anchors_before["disk"].items()
            },
            "pinned_git_citations": anchors_before["git"],
            "sources_unchanged": sources_unchanged,
            "sample_deterministic": sample_deterministic,
            "sample_sha256": digest(first_samples),
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CERTIFICATES.values())
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "certificates": dict(CERTIFICATES),
        "pass": passed,
        **status_keys,
        "frozen_candidate": FROZEN_CANDIDATE,
        "runtime_seconds": round(monotonic() - started, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "terminal": (
            "CYCLE804_DERIVATION_CANDIDATE_PASS"
            if passed
            else "CYCLE804_DERIVATION_CANDIDATE_HONEST_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    emit("SUMMARY_JSON", report)
    emit(report["terminal"])
    output = "\n".join(OUTPUT_LINES) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    if controls_pass != CERTIFICATES[
        "CONTROLS_LITERAL_PATHS_SHA_DETERMINISM_AND_BOUNDS"
    ]:
        raise AssertionError("control certificate mutation")
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
