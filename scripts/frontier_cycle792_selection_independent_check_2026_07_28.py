#!/usr/bin/env python3
"""Cycle 792 independent adversarial check of the first k=2 selection.

The Cycle 758 and Cycle 792 modules are blocklisted as executable suppliers:
they are read only as pinned source text for provenance and AST comparison.
The executable reconstruction below imports exactly the landed Cycle 750,
Cycle 736, and Cycle 719 suppliers named in ``AUDIT_INPUT_PATHS``.

The horizon extension remains a SUPPLIED acceptance-law probe.  This checker
does not promote it to landed law and makes no actuality claim.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
LANDED_HORIZON = 0
CONTROL_HORIZON = 251
EXTENDED_HORIZON = 252
PROBE_HORIZON = 256
TARGET_EVENT = 3
TARGET_POSITIONS = (1, 10)
TARGET_KEY = (TARGET_EVENT, TARGET_POSITIONS)
STDOUT_LIMIT_BYTES = 150 * 1024

REFERENCE_758_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
PRIMARY_792_PATH = (
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py"
)
TEXT_ONLY_BLOCKLIST_PREFIXES = (
    "frontier_cycle758_",
    "frontier_cycle790_",
    "frontier_cycle791_",
    "frontier_cycle792_",
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    REFERENCE_758_PATH:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    PRIMARY_792_PATH:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    REFERENCE_758_PATH: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    PRIMARY_792_PATH: "63948b09c41dd02b14350084ec33f7df9ad83b47",
}

REFERENCE_EXCLUSIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
PRIMARY_SCOPE_GUARDS = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def file_sha256(relative_path: str) -> str:
    return sha256(file_bytes(relative_path)).hexdigest()


def git_blob_sha1(relative_path: str) -> str:
    payload = file_bytes(relative_path)
    framed = b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload
    return sha1(framed).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def independent_families(
    positions_rows: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for positions in positions_rows:
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def independent_clean_postimage(
    state: tuple[int, ...], bank_count: int
) -> bool:
    """Re-derive the Cycle 750/758 immediate-postimage exclusion."""

    banks, links = K.M.unpack_state(state, bank_count)
    dirty_source_pointer = bool(state[K.R3.X.SOURCE_POINTER])
    dirty_bank_work = any(
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
    dirty_links = any(any(link) for link in links)
    return not (
        dirty_source_pointer or dirty_bank_work or dirty_links
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


def independent_base_evaluation(
    event: int,
    direction: tuple[int, int],
    program: tuple[object, ...],
    before: tuple[int, ...],
    positions: tuple[int, ...],
    k2_members: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    """Evaluate the landed battery without calling Cycle 758 or Cycle 792."""

    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(0 for _token in tokens)
    composition_word = M736.synchronous_composition_word(
        program, positions
    )
    expected = K.A.apply_semantic(before, composition_word)
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    config = tuple(
        int(station in positions)
        for station in range(RING_STATIONS)
    )
    reference_nonclean_conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
    }
    scope_guards = {
        "census_membership": positions in k2_members,
        "pairwise_separation": M736.is_pairwise_separated(config),
        "synchronization":
            trace == expected_synchronization_trace(positions),
    }
    return {
        "key": (event, positions),
        "event": event,
        "direction": direction,
        "program": program,
        "before": before,
        "positions": positions,
        "tokens": tokens,
        "after": after,
        "reference_nonclean_conditions":
            reference_nonclean_conditions,
        "scope_guards": scope_guards,
        "evidence": {
            "composition_word_gates": len(composition_word),
            "composition_word_sha256": K.gate_digest(composition_word),
            "before_state_sha256": state_sha256(before),
            "expected_state_sha256": state_sha256(expected),
            "after_state_sha256": state_sha256(after),
            "restored_state_sha256": state_sha256(restored),
            "rail_a_positions": tuple(
                station
                for station, value in enumerate(rail_a)
                if value
            ),
            "rail_b_weight": sum(rail_b),
            "trace_sha256": digest(trace),
        },
    }


def independent_horizon_trajectory(
    evaluation: dict[str, object],
    maximum_horizon: int = PROBE_HORIZON,
) -> dict[str, object]:
    """Run the supplied repeated-orbit probe while retaining every horizon."""

    state = evaluation["after"]
    program = evaluation["program"]
    positions = evaluation["positions"]
    tokens = evaluation["tokens"]
    zeros = tuple(0 for _token in tokens)
    clean_at = {
        LANDED_HORIZON:
            independent_clean_postimage(state, FIXTURE_BANKS)
    }
    first_clean = LANDED_HORIZON if clean_at[LANDED_HORIZON] else None
    seen = {state: LANDED_HORIZON}
    first_cycle = None
    transport_failures = 0
    state_digests = {LANDED_HORIZON: state_sha256(state)}
    for horizon in range(1, maximum_horizon + 1):
        state, rail_a, rail_b, _trace = K.run_orbit(
            state, program, token_positions=positions
        )
        transport_failures += (
            rail_a != tokens or rail_b != zeros
        )
        clean = independent_clean_postimage(state, FIXTURE_BANKS)
        clean_at[horizon] = clean
        if clean and first_clean is None:
            first_clean = horizon
        if state in seen and first_cycle is None:
            first_cycle = {
                "entry_horizon": seen[state],
                "return_horizon": horizon,
                "period": horizon - seen[state],
            }
        elif state not in seen:
            seen[state] = horizon
        if horizon >= CONTROL_HORIZON:
            state_digests[horizon] = state_sha256(state)
    return {
        "key": evaluation["key"],
        "clean_at": clean_at,
        "first_clean_horizon": first_clean,
        "first_cycle": first_cycle,
        "transport_failures": transport_failures,
        "state_digests_t251_t256": {
            horizon: state_digests[horizon]
            for horizon in range(CONTROL_HORIZON, PROBE_HORIZON + 1)
        },
    }


def reference_conditions_at(
    evaluation: dict[str, object],
    trajectory: dict[str, object],
    horizon: int,
) -> dict[str, bool]:
    conditions = dict(evaluation["reference_nonclean_conditions"])
    conditions["clean_postimage"] = bool(
        trajectory["clean_at"][horizon]
    )
    return conditions


def primary_reconstruction_conditions_at(
    evaluation: dict[str, object],
    trajectory: dict[str, object],
    horizon: int,
) -> dict[str, bool]:
    """Model the primary's acceptance conjunction, independently."""

    conditions = dict(evaluation["reference_nonclean_conditions"])
    conditions.update(evaluation["scope_guards"])
    conditions["clean_postimage"] = bool(
        trajectory["clean_at"][horizon]
    )
    return conditions


def selected_at(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    trajectories:
        dict[tuple[int, tuple[int, ...]], dict[str, object]],
    horizon: int,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    return tuple(
        key
        for key in sorted(rows)
        if all(
            reference_conditions_at(
                rows[key], trajectories[key], horizon
            ).values()
        )
    )


def run_independent_sweep(
    *, reverse_order: bool = False
) -> dict[str, object]:
    census = M736.configuration_census()
    configurations = census["configurations"]
    k2_positions = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    k2_members = frozenset(k2_positions)
    families = independent_families(k2_positions)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    work = tuple(
        (
            event,
            direction,
            program,
            before,
            positions,
        )
        for event, direction, program, before, _expected in fixtures
        for positions in k2_positions
    )
    if reverse_order:
        work = tuple(reversed(work))

    rows = {}
    trajectories = {}
    for event, direction, program, before, positions in work:
        evaluation = independent_base_evaluation(
            event,
            direction,
            program,
            before,
            positions,
            k2_members,
        )
        key = evaluation["key"]
        rows[key] = evaluation
        trajectories[key] = independent_horizon_trajectory(evaluation)

    selected_by_horizon = {
        horizon: selected_at(rows, trajectories, horizon)
        for horizon in range(PROBE_HORIZON + 1)
    }
    semantic_diff_keys = tuple(
        (key, horizon)
        for key in sorted(rows)
        for horizon in range(PROBE_HORIZON + 1)
        if all(
            reference_conditions_at(
                rows[key], trajectories[key], horizon
            ).values()
        )
        != all(
            primary_reconstruction_conditions_at(
                rows[key], trajectories[key], horizon
            ).values()
        )
    )
    signature_rows = tuple(
        {
            "key": key,
            "reference_nonclean":
                rows[key]["reference_nonclean_conditions"],
            "scope_guards": rows[key]["scope_guards"],
            "clean_bits": tuple(
                int(trajectories[key]["clean_at"][horizon])
                for horizon in range(PROBE_HORIZON + 1)
            ),
            "first_clean":
                trajectories[key]["first_clean_horizon"],
            "cycle": trajectories[key]["first_cycle"],
            "transport_failures":
                trajectories[key]["transport_failures"],
            "state_digests":
                trajectories[key]["state_digests_t251_t256"],
        }
        for key in sorted(rows)
    )
    return {
        "census": {
            "agreement": census["agreement"],
            "counts": census["direct_counts_by_k"],
        },
        "k2_positions": k2_positions,
        "families": families,
        "rows": rows,
        "trajectories": trajectories,
        "selected_by_horizon": selected_by_horizon,
        "semantic_diff_keys": semantic_diff_keys,
        "signature_sha256": digest(signature_rows),
    }


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def top_level_assignments(tree: ast.Module) -> dict[str, ast.expr]:
    assignments = {}
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
    return assignments


def condition_expression_map(
    function: ast.FunctionDef,
) -> dict[str, ast.expr]:
    matches = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "conditions"
            and isinstance(node.value, ast.Dict)
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(
            ("conditions dictionaries", function.name, len(matches))
        )
    result = {}
    for key, value in zip(matches[0].keys, matches[0].values):
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise AssertionError(("non-string condition", literal_key))
        result[literal_key] = value
    return result


class _CanonicalNames(ast.NodeTransformer):
    def __init__(self, renames: dict[str, str]):
        self.renames = renames

    def visit_Name(self, node: ast.Name) -> ast.Name:
        return ast.copy_location(
            ast.Name(
                id=self.renames.get(node.id, node.id),
                ctx=node.ctx,
            ),
            node,
        )


def canonical_function_body(
    function: ast.FunctionDef, renames: dict[str, str]
) -> str:
    body = list(function.body)
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        body = body[1:]
    module = ast.Module(body=body, type_ignores=[])
    normalized = _CanonicalNames(renames).visit(module)
    return ast.dump(normalized, include_attributes=False)


def ast_semantics_audit(
    scope_guard_failures:
        tuple[tuple[tuple[int, tuple[int, ...]], str], ...],
    semantic_diff_keys:
        tuple[tuple[tuple[int, tuple[int, ...]], int], ...],
) -> dict[str, object]:
    """Diff the blocklisted source texts without importing either module."""

    reference_tree = ast.parse(
        file_bytes(REFERENCE_758_PATH).decode("utf-8"),
        filename=REFERENCE_758_PATH,
    )
    primary_tree = ast.parse(
        file_bytes(PRIMARY_792_PATH).decode("utf-8"),
        filename=PRIMARY_792_PATH,
    )
    reference_functions = top_level_functions(reference_tree)
    primary_functions = top_level_functions(primary_tree)
    reference_assignments = top_level_assignments(reference_tree)
    primary_assignments = top_level_assignments(primary_tree)

    reference_condition_nodes = condition_expression_map(
        reference_functions[
            "multisource_enforcement_lineage_selector"
        ]
    )
    primary_condition_nodes = condition_expression_map(
        primary_functions["base_battery_evaluation"]
    )
    shared_keys = REFERENCE_EXCLUSIONS[:-1]
    shared_expression_equal = {
        key: (
            ast.dump(
                reference_condition_nodes[key],
                include_attributes=False,
            )
            == ast.dump(
                primary_condition_nodes[key],
                include_attributes=False,
            )
        )
        for key in shared_keys
    }
    reference_clean_body = canonical_function_body(
        reference_functions["clean_postimage"],
        {"after": "state"},
    )
    primary_clean_body = canonical_function_body(
        primary_functions["landed_clean_postimage"],
        {},
    )
    clean_predicate_equal = reference_clean_body == primary_clean_body

    reference_keys = tuple(reference_condition_nodes)
    primary_base_keys = tuple(primary_condition_nodes)
    added_primary_keys = tuple(
        key for key in primary_base_keys if key not in shared_keys
    )
    missing_primary_keys = tuple(
        key for key in shared_keys if key not in primary_base_keys
    )

    selector_source = ast.unparse(
        primary_functions["selector_conditions"]
    )
    horizon_source = ast.unparse(
        primary_functions["horizon_trajectory"]
    )
    horizon_plumbing_exact = all(
        fragment in selector_source
        for fragment in (
            "conditions = dict(evaluation['conditions'])",
            "conditions['clean_postimage'] = bool("
            "trajectory['clean_at'][horizon])",
            "return conditions",
        )
    )
    repeated_orbit_exact = all(
        fragment in horizon_source
        for fragment in (
            "state = evaluation['after']",
            "for horizon in range(1, maximum_horizon + 1):",
            "K.run_orbit(state, program, token_positions=positions)",
            "clean = landed_clean_postimage(state, FIXTURE_BANKS)",
        )
    ) and "reverse=True" not in horizon_source

    landed_horizon = ast.literal_eval(
        primary_assignments["LANDED_POSTIMAGE_HORIZON"]
    )
    control_horizon = ast.literal_eval(
        primary_assignments["CONTROL_HORIZON"]
    )
    extended_horizon = ast.literal_eval(
        primary_assignments["EXTENDED_HORIZON"]
    )
    structural_scope_guards_exact = (
        added_primary_keys == PRIMARY_SCOPE_GUARDS
    )
    scope_guards_extensionally_neutral = (
        not scope_guard_failures and not semantic_diff_keys
    )

    second_deviations = []
    if reference_keys != REFERENCE_EXCLUSIONS:
        second_deviations.append(
            "reference exclusion set was not the four landed exclusions"
        )
    if missing_primary_keys:
        second_deviations.append(
            "primary omitted landed non-horizon exclusions: "
            + compact(missing_primary_keys)
        )
    unequal_shared = tuple(
        key
        for key, equal in shared_expression_equal.items()
        if not equal
    )
    if unequal_shared:
        second_deviations.append(
            "primary changed landed exclusion expressions: "
            + compact(unequal_shared)
        )
    if not clean_predicate_equal:
        second_deviations.append(
            "primary changed the clean-postimage predicate"
        )
    if not structural_scope_guards_exact:
        second_deviations.append(
            "primary added unexpected acceptance conjuncts: "
            + compact(added_primary_keys)
        )
    if scope_guard_failures:
        second_deviations.append(
            "primary scope guards veto lawful swept alternatives: "
            + compact(scope_guard_failures[:8])
        )
    if semantic_diff_keys:
        second_deviations.append(
            "primary and reference acceptance semantics differ on sweep: "
            + compact(semantic_diff_keys[:8])
        )
    if not horizon_plumbing_exact:
        second_deviations.append(
            "primary clean condition has non-horizon plumbing changes"
        )
    if not repeated_orbit_exact:
        second_deviations.append(
            "primary horizon evolution is not the stated repeated orbit"
        )
    if (
        landed_horizon,
        control_horizon,
        extended_horizon,
    ) != (
        LANDED_HORIZON,
        CONTROL_HORIZON,
        EXTENDED_HORIZON,
    ):
        second_deviations.append(
            "primary horizon constants differ from 0/251/252"
        )

    return {
        "reference_exclusion_keys": reference_keys,
        "primary_base_condition_keys": primary_base_keys,
        "shared_expression_equal": shared_expression_equal,
        "clean_predicate_equal_after_argument_normalization":
            clean_predicate_equal,
        "structural_ast_additions": added_primary_keys,
        "structural_ast_additions_classification": (
            "landed-domain certificates; extensionally neutral on all "
            "176 scoped event/configuration rows and therefore not an "
            "acceptance-law deviation within the claimed domain"
        ),
        "scope_guard_failures": scope_guard_failures,
        "semantic_diff_keys_all_horizons_t0_t256":
            semantic_diff_keys,
        "horizon_plumbing_exact": horizon_plumbing_exact,
        "repeated_orbit_exact": repeated_orbit_exact,
        "horizons": {
            "landed": landed_horizon,
            "control": control_horizon,
            "extended": extended_horizon,
        },
        "reference_clean_body_sha256":
            sha256(reference_clean_body.encode()).hexdigest(),
        "primary_clean_body_sha256":
            sha256(primary_clean_body.encode()).hexdigest(),
        "reference_condition_ast_sha256": digest(
            {
                key: ast.dump(value, include_attributes=False)
                for key, value in reference_condition_nodes.items()
            }
        ),
        "primary_condition_ast_sha256": digest(
            {
                key: ast.dump(value, include_attributes=False)
                for key, value in primary_condition_nodes.items()
            }
        ),
        "second_deviations": tuple(second_deviations),
        "pass": not second_deviations,
    }


def source_control_audit() -> dict[str, object]:
    anchors = {
        path: {
            "sha256": file_sha256(path),
            "git_blob_sha1": git_blob_sha1(path),
        }
        for path in (
            *AUDIT_INPUT_PATHS,
            REFERENCE_758_PATH,
            PRIMARY_792_PATH,
        )
    }
    sha_pass = all(
        anchors[path]["sha256"] == EXPECTED_SHA256[path]
        and anchors[path]["git_blob_sha1"]
        == EXPECTED_GIT_BLOB_SHA1[path]
        for path in anchors
    )
    imported_blocklisted = tuple(
        sorted(
            name
            for name in sys.modules
            if name.startswith(TEXT_ONLY_BLOCKLIST_PREFIXES)
        )
    )
    direct_imports = {
        "F750": F750.__name__,
        "M736": M736.__name__,
        "K": K.__name__,
    }
    expected_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple_length": len(AUDIT_INPUT_PATHS),
        "declared_inputs_equal": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "direct_imports": direct_imports,
        "anchors": anchors,
        "pinned_758_reference_blob":
            anchors[REFERENCE_758_PATH]["git_blob_sha1"],
        "text_only_blocklist_prefixes": TEXT_ONLY_BLOCKLIST_PREFIXES,
        "imported_blocklisted_modules": imported_blocklisted,
        "pass": (
            len(AUDIT_INPUT_PATHS) == 3
            and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
            and direct_imports == expected_imports
            and sha_pass
            and not imported_blocklisted
            and anchors[REFERENCE_758_PATH]["git_blob_sha1"]
            == "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0"
        ),
    }


def render_output(
    certificates: list[dict[str, object]],
    findings: tuple[str, ...],
    report: dict[str, object],
) -> str:
    lines = [
        (
            "SUPPLIED_HORIZON_ONLY: t=252 is a supplied "
            "acceptance-law probe; it is not landed law"
        ),
    ]
    lines.extend(
        (
            ("PASS " if certificate["pass"] else "FAIL ")
            + certificate["name"]
            + " :: "
            + compact(certificate["detail"])
        )
        for certificate in certificates
    )
    if findings:
        lines.append(
            "REFUTES_PRIMARY_LOUDLY :: " + compact(findings)
        )
    else:
        lines.append("FINDINGS_VERBATIM :: []")
    lines.extend(
        (
            "actuality_claim: false",
            "horizon_extended_postimage_law_landed: false",
            report["terminal"],
            "REPORT :: " + compact(report),
        )
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    controls = source_control_audit()
    first = run_independent_sweep()

    rows = first["rows"]
    trajectories = first["trajectories"]
    k2_positions = first["k2_positions"]
    families = first["families"]
    selected_by_horizon = first["selected_by_horizon"]

    scope_guard_failures = tuple(
        (key, condition)
        for key in sorted(rows)
        for condition, passed in rows[key]["scope_guards"].items()
        if not passed
    )
    ast_audit = ast_semantics_audit(
        scope_guard_failures,
        first["semantic_diff_keys"],
    )

    landed_failure_census: Counter[str] = Counter()
    for key in sorted(rows):
        for condition, passed in reference_conditions_at(
            rows[key], trajectories[key], LANDED_HORIZON
        ).items():
            if not passed:
                landed_failure_census[condition] += 1
    all_nonclean_reference_conditions_pass = all(
        all(row["reference_nonclean_conditions"].values())
        for row in rows.values()
    )
    landed_zero_survivor_positions = tuple(
        positions
        for positions in k2_positions
        if all(
            (event, positions)
            not in selected_by_horizon[LANDED_HORIZON]
            for event in range(2 * FIXTURE_BANKS)
        )
    )
    expected_families = {
        (0, 2): 11,
        (0, 3): 11,
        (0, 4): 11,
        (0, 5): 11,
    }
    fidelity_pass = (
        controls["pass"]
        and first["census"]["agreement"]
        and first["census"]["counts"][2] == 44
        and len(k2_positions) == 44
        and {
            representative: len(alternatives)
            for representative, alternatives in families.items()
        }
        == expected_families
        and len(rows) == 176
        and all_nonclean_reference_conditions_pass
        and not scope_guard_failures
        and not first["semantic_diff_keys"]
        and not selected_by_horizon[LANDED_HORIZON]
        and len(landed_zero_survivor_positions) == 44
        and dict(landed_failure_census)
        == {"clean_postimage": 176}
        and all(ast_audit["shared_expression_equal"].values())
        and ast_audit[
            "clean_predicate_equal_after_argument_normalization"
        ]
    )
    fidelity_detail = {
        "reference_exclusions": REFERENCE_EXCLUSIONS,
        "k2_configurations": len(k2_positions),
        "k2_families": {
            ",".join(map(str, representative)): len(alternatives)
            for representative, alternatives in families.items()
        },
        "event_configuration_evaluations": len(rows),
        "landed_horizon": LANDED_HORIZON,
        "landed_selected": selected_by_horizon[LANDED_HORIZON],
        "landed_zero_survivor_configurations":
            len(landed_zero_survivor_positions),
        "landed_failure_census":
            dict(sorted(landed_failure_census.items())),
        "all_nonclean_reference_conditions_pass":
            all_nonclean_reference_conditions_pass,
        "scope_guard_failures": scope_guard_failures,
        "reference_vs_primary_semantic_diff_count_t0_t256":
            len(first["semantic_diff_keys"]),
    }

    target_representative = next(
        representative
        for representative, alternatives in families.items()
        if TARGET_POSITIONS in alternatives
    )
    target_alternatives = families[target_representative]
    target_family_window = {
        horizon: tuple(
            positions
            for positions in target_alternatives
            if (
                TARGET_EVENT,
                positions,
            ) in selected_by_horizon[horizon]
        )
        for horizon in range(CONTROL_HORIZON, PROBE_HORIZON + 1)
    }
    global_selection_window = {
        horizon: selected_by_horizon[horizon]
        for horizon in range(CONTROL_HORIZON, PROBE_HORIZON + 1)
    }
    target_exclusion_certificates = {
        horizon: reference_conditions_at(
            rows[TARGET_KEY],
            trajectories[TARGET_KEY],
            horizon,
        )
        for horizon in range(CONTROL_HORIZON, PROBE_HORIZON + 1)
    }
    first_selection_horizon = next(
        (
            horizon
            for horizon, selected in selected_by_horizon.items()
            if selected
        ),
        None,
    )
    persistence_window = {
        f"t{horizon}": target_family_window[horizon]
        for horizon in range(EXTENDED_HORIZON, PROBE_HORIZON + 1)
    }
    recount_pass = (
        first_selection_horizon == EXTENDED_HORIZON
        and target_family_window[CONTROL_HORIZON] == ()
        and target_family_window[EXTENDED_HORIZON]
        == (TARGET_POSITIONS,)
        and selected_by_horizon[EXTENDED_HORIZON]
        == (TARGET_KEY,)
        and trajectories[TARGET_KEY]["first_clean_horizon"]
        == EXTENDED_HORIZON
        and target_exclusion_certificates[CONTROL_HORIZON]
        == {
            "synchronous_composition": True,
            "token_rail_return": True,
            "literal_inverse": True,
            "clean_postimage": False,
        }
        and all(
            target_exclusion_certificates[EXTENDED_HORIZON].values()
        )
    )
    recount_detail = {
        "target_event": TARGET_EVENT,
        "target_family_representative": target_representative,
        "target_positions": TARGET_POSITIONS,
        "first_selection_horizon_t0_t256":
            first_selection_horizon,
        "target_first_clean_horizon":
            trajectories[TARGET_KEY]["first_clean_horizon"],
        "t251_vs_t252": {
            "t251": target_family_window[CONTROL_HORIZON],
            "t252": target_family_window[EXTENDED_HORIZON],
        },
        "per_exclusion_certificates_t251_t256":
            target_exclusion_certificates,
        "persistence_window": persistence_window,
        "global_selection_window_t251_t256":
            global_selection_window,
    }

    target_alternative_sweep_t252 = tuple(
        {
            "positions": positions,
            "conditions": reference_conditions_at(
                rows[(TARGET_EVENT, positions)],
                trajectories[(TARGET_EVENT, positions)],
                EXTENDED_HORIZON,
            ),
            "firing_exclusions": tuple(
                condition
                for condition, passed in reference_conditions_at(
                    rows[(TARGET_EVENT, positions)],
                    trajectories[(TARGET_EVENT, positions)],
                    EXTENDED_HORIZON,
                ).items()
                if not passed
            ),
        }
        for positions in target_alternatives
    )
    other_keys = tuple(
        key for key in sorted(rows) if key != TARGET_KEY
    )
    other_clean_at_t252 = tuple(
        key
        for key in other_keys
        if trajectories[key]["clean_at"][EXTENDED_HORIZON]
    )
    identity_control_positions = (
        TARGET_POSITIONS,
        (0, 2),
        (0, 3),
        (1, 3),
        (0, 4),
        (1, 4),
    )
    landed_identity_controls = tuple(
        {
            "positions": positions,
            "conditions": reference_conditions_at(
                rows[(TARGET_EVENT, positions)],
                trajectories[(TARGET_EVENT, positions)],
                LANDED_HORIZON,
            ),
            "selected": (
                TARGET_EVENT,
                positions,
            ) in selected_by_horizon[LANDED_HORIZON],
            "firing_exclusions": tuple(
                condition
                for condition, passed in reference_conditions_at(
                    rows[(TARGET_EVENT, positions)],
                    trajectories[(TARGET_EVENT, positions)],
                    LANDED_HORIZON,
                ).items()
                if not passed
            ),
        }
        for positions in identity_control_positions
    )
    target_family_selected_t252 = tuple(
        row["positions"]
        for row in target_alternative_sweep_t252
        if not row["firing_exclusions"]
    )
    uniqueness_pass = (
        target_family_selected_t252 == (TARGET_POSITIONS,)
        and selected_by_horizon[EXTENDED_HORIZON]
        == (TARGET_KEY,)
        and len(other_keys) == 175
        and not other_clean_at_t252
        and all(
            not control["selected"]
            and control["firing_exclusions"] == ("clean_postimage",)
            for control in landed_identity_controls
        )
    )
    uniqueness_detail = {
        "full_target_alternative_sweep_t252":
            target_alternative_sweep_t252,
        "target_family_selected_t252":
            target_family_selected_t252,
        "global_selected_t252":
            selected_by_horizon[EXTENDED_HORIZON],
        "other_event_configuration_rows_checked": len(other_keys),
        "other_clean_postimages_t252": other_clean_at_t252,
        "landed_epoch3_identity_controls":
            landed_identity_controls,
    }

    supplied_change_pass = ast_audit["pass"]
    supplied_change_detail = {
        "only_effective_acceptance_law_change":
            "clean_postimage observation horizon: t0 -> supplied t252",
        "ast_diff": ast_audit,
        "actuality_claim": False,
        "horizon_extended_postimage_law_landed": False,
    }

    second = run_independent_sweep(reverse_order=True)
    deterministic_pass = (
        first["signature_sha256"] == second["signature_sha256"]
        and first["selected_by_horizon"]
        == second["selected_by_horizon"]
        and first["semantic_diff_keys"]
        == second["semantic_diff_keys"]
    )
    elapsed = monotonic() - started

    findings_list = []
    if not fidelity_pass:
        findings_list.append(
            "BATTERY INFIDELITY: "
            + compact(fidelity_detail)
        )
    if not recount_pass:
        findings_list.append(
            "SELECTION RECOUNT REFUTES: "
            + compact(recount_detail)
        )
    if target_family_selected_t252 != (TARGET_POSITIONS,):
        findings_list.append(
            "NON-UNIQUE SURVIVOR: target-family t252 sweep selected "
            + compact(target_family_selected_t252)
        )
    spurious_t252 = tuple(
        key
        for key in selected_by_horizon[EXTENDED_HORIZON]
        if key != TARGET_KEY
    )
    if spurious_t252:
        findings_list.append(
            "SPURIOUS SELECTION: non-target t252 survivors "
            + compact(spurious_t252)
        )
    if not supplied_change_pass:
        findings_list.extend(
            "SECOND DEVIATION: " + finding
            for finding in ast_audit["second_deviations"]
        )
    if not controls["pass"]:
        findings_list.append(
            "CONTROL FAILURE: source anchors or executable blocklist "
            + compact(controls)
        )
    if not deterministic_pass:
        findings_list.append(
            "CONTROL FAILURE: nondeterministic sweep signatures "
            + compact(
                (
                    first["signature_sha256"],
                    second["signature_sha256"],
                )
            )
        )
    if elapsed >= AUDIT_TIMEOUT_SEC:
        findings_list.append(
            "CONTROL FAILURE: runtime seconds "
            + str(round(elapsed, 6))
            + " is not below "
            + str(AUDIT_TIMEOUT_SEC)
        )
    findings = tuple(findings_list)

    certificates = [
        {
            "name": "Certificate_A_BATTERY_FIDELITY_ATTACK",
            "pass": fidelity_pass,
            "detail": fidelity_detail,
        },
        {
            "name": "Certificate_B_SELECTION_RECOUNT",
            "pass": recount_pass,
            "detail": recount_detail,
        },
        {
            "name": "Certificate_C_UNIQUENESS_ATTACK",
            "pass": uniqueness_pass,
            "detail": uniqueness_detail,
        },
        {
            "name": "Certificate_D_SUPPLIED_CHANGE_AST_AUDIT",
            "pass": supplied_change_pass,
            "detail": supplied_change_detail,
        },
        {
            "name": "Certificate_E_CONTROLS",
            "pass": False,
            "detail": {
                "source_controls": controls,
                "deterministic_forward_signature":
                    first["signature_sha256"],
                "deterministic_reverse_signature":
                    second["signature_sha256"],
                "deterministic": deterministic_pass,
                "runtime_seconds": round(elapsed, 6),
                "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                "stdout_bytes": 0,
                "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            },
        },
    ]

    output = ""
    for _iteration in range(6):
        stdout_bytes = len(output.encode("utf-8")) if output else 0
        controls_pass = (
            controls["pass"]
            and deterministic_pass
            and elapsed < AUDIT_TIMEOUT_SEC
            and stdout_bytes < STDOUT_LIMIT_BYTES
        )
        certificates[-1]["pass"] = controls_pass
        certificates[-1]["detail"]["stdout_bytes"] = stdout_bytes
        all_pass = all(
            certificate["pass"] for certificate in certificates
        )
        checks = {
            certificate["name"]: certificate["pass"]
            for certificate in certificates
        }
        report_core = {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "checks": checks,
            "findings_verbatim": findings,
            "first_multisource_selection_at_extended_horizon":
                recount_pass,
            "persistence_window": persistence_window,
            "actuality_claim": False,
            "horizon_extended_postimage_law_landed": False,
            "runtime_seconds": round(elapsed, 6),
            "pass": all_pass,
            "terminal": (
                "CYCLE792_SELECTION_INDEPENDENT_CHECK_PASS"
                if all_pass
                else "CYCLE792_SELECTION_INDEPENDENT_CHECK_REFUTES"
            ),
        }
        report = {
            **report_core,
            "report_sha256": digest(report_core),
        }
        candidate = render_output(certificates, findings, report)
        candidate_bytes = len(candidate.encode("utf-8"))
        if candidate_bytes == stdout_bytes:
            output = candidate
            break
        output = candidate
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", final_bytes))
    if certificates[-1]["detail"]["stdout_bytes"] != final_bytes:
        certificates[-1]["detail"]["stdout_bytes"] = final_bytes
        all_pass = all(
            certificate["pass"] for certificate in certificates
        )
        report_core["pass"] = all_pass
        report_core["terminal"] = (
            "CYCLE792_SELECTION_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE792_SELECTION_INDEPENDENT_CHECK_REFUTES"
        )
        report = {
            **report_core,
            "report_sha256": digest(report_core),
        }
        output = render_output(certificates, findings, report)
        final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", final_bytes))
    sys.stdout.write(output)
    return 0 if all(
        certificate["pass"] for certificate in certificates
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
