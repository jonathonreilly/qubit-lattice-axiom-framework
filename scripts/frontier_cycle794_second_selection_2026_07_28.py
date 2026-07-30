#!/usr/bin/env python3
"""Cycle 794: the second extended-horizon k=2 selection at supplied t=371.

The Cycle-758 four-family k=2 sample is augmented by the two supplied
transient configurations from Cycles 791/792.  Cycle-758's four exclusions
are unchanged.  The only scientific-law deviation is an explicit, supplied
terminal orbit index t: horizon t applies t+1 complete Cycle-719 controller
orbits.  This is a bounded fixture calculation, not an actuality or time-law
claim.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import base64
from hashlib import sha1, sha256
import inspect
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


REFERENCE_BRANCH = "origin/physics-loop/toe-close-blockA5-20260729"
REFERENCE_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
REFERENCE_SPEC = f"{REFERENCE_BRANCH}:{REFERENCE_PATH}"
REFERENCE_BLOB_SHA = "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0"
REFERENCE_GITHUB_REPOSITORY = (
    "jonathonreilly/qubit-lattice-axiom-framework"
)
REFERENCE_EXECUTION_BLOCKLIST = (
    "exec",
    "eval",
    "compile",
    "importlib",
    "runpy",
)

M736_LANDED_SPEC = (
    "origin/physics-loop/toe-close-blockA6-mainbase-20260729:"
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py"
)
EXPECTED_BLOBS = {
    "F750": "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    "M736": "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    "K719": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    "REFERENCE_758": REFERENCE_BLOB_SHA,
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
EPOCH_KEY = 3
TARGET_POSITIONS = (0, 7)
FIRST_TRANSIENT_POSITIONS = (1, 10)
TARGET_HORIZON_T = 371
TARGET_CONTROL_T = 370
FIRST_TRANSIENT_T = 252
FIRST_TRANSIENT_CONTROL_T = 251
PERSISTENCE_WINDOW = tuple(range(372, 377))
LANDED_HORIZON_T = 0

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def fixed_command(arguments: tuple[str, ...]) -> subprocess.CompletedProcess:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=False,
        capture_output=True,
        timeout=60,
    )


def fetch_reference_text() -> tuple[str, dict[str, object]]:
    """Fetch the exact Cycle-758 blob as text and never import or execute it."""

    branch_commit = fixed_command(
        ("git", "rev-parse", "--verify", REFERENCE_BRANCH)
    )
    direct = fixed_command(("git", "show", REFERENCE_SPEC))
    direct_sha = (
        git_blob_sha(direct.stdout) if direct.returncode == 0 else None
    )
    if direct.returncode == 0 and direct_sha == REFERENCE_BLOB_SHA:
        payload = direct.stdout
        method = "git_show_pinned_branch_path"
        supplied_transport_deviation = False
    else:
        endpoint = (
            f"repos/{REFERENCE_GITHUB_REPOSITORY}/git/blobs/"
            f"{REFERENCE_BLOB_SHA}"
        )
        recovered = fixed_command(("gh", "api", endpoint))
        if recovered.returncode != 0:
            raise RuntimeError(
                (
                    "Cycle-758 immutable blob recovery failed",
                    recovered.stderr.decode("utf-8", errors="replace")[:500],
                )
            )
        response = json.loads(recovered.stdout)
        payload = base64.b64decode(response["content"])
        method = "github_immutable_blob_fallback"
        supplied_transport_deviation = True

    observed_sha = git_blob_sha(payload)
    if observed_sha != REFERENCE_BLOB_SHA:
        raise AssertionError(
            ("Cycle-758 reference blob mismatch", observed_sha)
        )
    provenance = {
        "requested_git_show": REFERENCE_SPEC,
        "requested_branch_commit": branch_commit.stdout.decode().strip(),
        "requested_path_present": direct.returncode == 0,
        "requested_path_blob_sha": direct_sha,
        "fetch_method": method,
        "immutable_blob_sha": observed_sha,
        "reference_execution": "TEXT_ONLY_BLOCKED",
        "execution_blocklist": REFERENCE_EXECUTION_BLOCKLIST,
        "SUPPLIED_transport_deviation":
            supplied_transport_deviation,
    }
    return payload.decode("utf-8"), provenance


def fetch_landed_736_text() -> tuple[str, dict[str, object]]:
    direct = fixed_command(("git", "show", M736_LANDED_SPEC))
    if direct.returncode != 0:
        raise RuntimeError(
            (
                "landed Cycle-736 text unavailable",
                direct.stderr.decode("utf-8", errors="replace")[:500],
            )
        )
    observed_sha = git_blob_sha(direct.stdout)
    return direct.stdout.decode("utf-8"), {
        "checkout_path_present": (
            ROOT
            / "scripts"
            / "frontier_cycle736_pairwise_separated_multisource_2026_07_28.py"
        ).is_file(),
        "landed_text_spec": M736_LANDED_SPEC,
        "blob_sha": observed_sha,
        "SUPPLIED_source_availability_adapter": True,
        "law_change": False,
    }


def synchronous_composition_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    stations = len(program)
    positions = tuple(token_positions)
    word = []
    for _step in range(stations):
        live = set(positions)
        for station in range(stations):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple((station + 1) % stations for station in positions)
    return tuple(word)


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated_k2_configurations() -> tuple[tuple[int, ...], ...]:
    return tuple(
        (left, right)
        for left in range(RING_STATIONS)
        for right in range(left + 1, RING_STATIONS)
        if (right - left) not in (1, RING_STATIONS - 1)
    )


def cycle758_k2_representatives() -> tuple[tuple[int, ...], ...]:
    families: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for positions in pairwise_separated_k2_configurations():
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        families.setdefault(representative, set()).add(positions)
    return tuple(sorted(families))


def reconstructed_battery() -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            set(cycle758_k2_representatives())
            | {FIRST_TRANSIENT_POSITIONS, TARGET_POSITIONS}
        )
    )


def clean_postimage(after: int, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
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
            ),
            any(any(link) for link in links),
        )
    )


def reverse_extended_horizon(
    after: int,
    final_a: tuple[int, ...],
    final_b: tuple[int, ...],
    program: tuple[object, ...],
    horizon_t: int,
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    restored = after
    inverse_a = final_a
    inverse_b = final_b
    for _orbit in range(horizon_t + 1):
        for _step in range(len(program)):
            restored, inverse_a, inverse_b = K.apply_controller_step(
                restored,
                program,
                inverse_a,
                inverse_b,
                reverse=True,
            )
    return restored, inverse_a, inverse_b


def configuration_snapshots(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
    horizons: tuple[int, ...],
) -> dict[
    int,
    tuple[
        int,
        int,
        tuple[int, ...],
        tuple[int, ...],
    ],
]:
    """Build actual and independent landed-composition states once per orbit."""

    requested = set(horizons)
    initial_a = tuple(
        int(station in positions) for station in range(len(program))
    )
    a = initial_a
    b = (0,) * len(program)
    actual = before
    expected = before
    one_orbit_word = synchronous_composition_word(program, positions)
    snapshots = {}
    for horizon_t in range(max(requested) + 1):
        for _step in range(len(program)):
            actual, a, b = K.apply_controller_step(
                actual, program, a, b
            )
        expected = K.A.apply_semantic(expected, one_orbit_word)
        if horizon_t in requested:
            snapshots[horizon_t] = (actual, expected, a, b)
    return snapshots


def evaluate_snapshot(
    before: int,
    program: tuple[object, ...],
    positions: tuple[int, ...],
    horizon_t: int,
    snapshot: tuple[
        int,
        int,
        tuple[int, ...],
        tuple[int, ...],
    ],
) -> dict[str, object]:
    actual, expected, rail_a, rail_b = snapshot
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    restored, inverse_a, inverse_b = reverse_extended_horizon(
        actual, rail_a, rail_b, program, horizon_t
    )
    conditions = {
        "synchronous_composition": actual == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": clean_postimage(actual, FIXTURE_BANKS),
    }
    failed = tuple(
        name for name, passed in conditions.items() if not passed
    )
    return {
        "positions": positions,
        "horizon_t_SUPPLIED": horizon_t,
        "complete_orbits_applied": horizon_t + 1,
        "controller_steps_applied":
            (horizon_t + 1) * len(program),
        "conditions": conditions,
        "failed_exclusions": failed,
        "selected": not failed,
        "postimage_sha256": sha256(
            str(actual).encode("ascii")
        ).hexdigest(),
    }


def public_battery(
    evaluations: dict[
        tuple[tuple[int, ...], int], dict[str, object]
    ],
    battery: tuple[tuple[int, ...], ...],
    horizon_t: int,
) -> dict[str, object]:
    rows = tuple(evaluations[(positions, horizon_t)] for positions in battery)
    survivors = tuple(
        row["positions"] for row in rows if row["selected"]
    )
    return {
        "horizon_t_SUPPLIED": horizon_t,
        "rows": rows,
        "survivors": survivors,
        "survivor_count": len(survivors),
        "unique": len(survivors) == 1,
    }


def run_experiment() -> dict[str, object]:
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    event, direction, program, before, _expected = fixtures[EPOCH_KEY]
    battery = reconstructed_battery()
    needed_by_configuration = {
        positions: {
            LANDED_HORIZON_T,
            FIRST_TRANSIENT_T,
            TARGET_HORIZON_T,
        }
        for positions in battery
    }
    needed_by_configuration[FIRST_TRANSIENT_POSITIONS].add(
        FIRST_TRANSIENT_CONTROL_T
    )
    needed_by_configuration[TARGET_POSITIONS].update(
        (TARGET_CONTROL_T, *PERSISTENCE_WINDOW)
    )

    evaluations = {}
    raw_snapshots = {}
    for positions in battery:
        horizons = tuple(sorted(needed_by_configuration[positions]))
        snapshots = configuration_snapshots(
            program, before, positions, horizons
        )
        for horizon_t in horizons:
            raw_snapshots[(positions, horizon_t)] = snapshots[horizon_t]
            evaluations[(positions, horizon_t)] = evaluate_snapshot(
                before,
                program,
                positions,
                horizon_t,
                snapshots[horizon_t],
            )

    landed = public_battery(
        evaluations, battery, LANDED_HORIZON_T
    )
    first_control = evaluations[
        (FIRST_TRANSIENT_POSITIONS, FIRST_TRANSIENT_CONTROL_T)
    ]
    first_selection = public_battery(
        evaluations, battery, FIRST_TRANSIENT_T
    )
    target_control = evaluations[
        (TARGET_POSITIONS, TARGET_CONTROL_T)
    ]
    at_371 = public_battery(
        evaluations, battery, TARGET_HORIZON_T
    )
    target_row = evaluations[
        (TARGET_POSITIONS, TARGET_HORIZON_T)
    ]
    persistence = tuple(
        evaluations[(TARGET_POSITIONS, horizon_t)]
        for horizon_t in PERSISTENCE_WINDOW
    )

    identity_rows = []
    for positions in battery:
        direct_after, direct_a, direct_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        actual, expected, rail_a, rail_b = raw_snapshots[
            (positions, LANDED_HORIZON_T)
        ]
        identity_rows.append(
            {
                "positions": positions,
                "actual_matches_K_run_orbit": actual == direct_after,
                "composition_matches_K_run_orbit":
                    expected == direct_after,
                "rails_match_K_run_orbit":
                    rail_a == direct_a and rail_b == direct_b,
            }
        )

    target_outcome = (
        "SELECTED" if target_row["selected"] else "STILL_EXCLUDED"
    )
    first_unique = (
        first_selection["survivors"]
        == (FIRST_TRANSIENT_POSITIONS,)
        and not first_control["selected"]
    )
    second_unique = (
        at_371["survivors"] == (TARGET_POSITIONS,)
        and not target_control["selected"]
    )
    if first_unique and second_unique:
        pattern = "TWO_FOR_TWO_UNIQUE"
        divergence = ()
    else:
        pattern = "DIVERGENT"
        divergence = tuple(
            label
            for label, passed in (
                (
                    "first_transient_not_unique_at_first_clean_t252",
                    first_unique,
                ),
                (
                    "second_transient_not_unique_at_first_clean_t371",
                    second_unique,
                ),
            )
            if not passed
        )

    cross_rows = tuple(
        row for row in at_371["rows"]
        if row["positions"] != TARGET_POSITIONS
    )
    return {
        "key_identity": {
            "key": (EPOCH_KEY, TARGET_POSITIONS),
            "epoch_indexing": "Cycle-750 zero-based event index",
            "event": event,
            "ordinal_epoch": event + 1,
            "direction": direction,
            "positions": TARGET_POSITIONS,
            "program_stations": len(program),
            "fixture_count": len(fixtures),
        },
        "battery": battery,
        "cycle758_k2_representatives":
            cycle758_k2_representatives(),
        "landed_horizon_identity_rows": tuple(identity_rows),
        "landed_horizon": landed,
        "first_transient_control_t251": first_control,
        "first_transient_t252": first_selection,
        "target_control_t370": target_control,
        "target_t371": at_371,
        "target_outcome": target_outcome,
        "target_exclusions": target_row["failed_exclusions"],
        "persistence_t372_t376": persistence,
        "cross_configuration_rows_t371": cross_rows,
        "simultaneous_selection_count_t371":
            at_371["survivor_count"],
        "simultaneous_survivors_t371": at_371["survivors"],
        "pattern": pattern,
        "divergence": divergence,
    }


def named_function(
    tree: ast.Module, name: str
) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def source_and_reference_audit(
    reference_text: str, landed_736_text: str
) -> dict[str, object]:
    runner_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    reference_tree = ast.parse(reference_text)
    landed_736_tree = ast.parse(landed_736_text)

    assignments = {}
    imports = {}
    for node in runner_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    literal_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 4
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
    )
    reference_imports = {
        alias.asname or alias.name: alias.name
        for node in reference_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    reference_selector_ast = ast.unparse(
        named_function(
            reference_tree,
            "multisource_enforcement_lineage_selector",
        )
    )
    required_selector_tokens = (
        "M736.synchronous_composition_word",
        "K.A.apply_semantic",
        "K.run_orbit",
        "reverse=True",
        "synchronous_composition",
        "token_rail_return",
        "literal_inverse",
        "clean_postimage",
    )
    dangerous_calls = tuple(
        node.func.id
        for node in ast.walk(runner_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in REFERENCE_EXECUTION_BLOCKLIST
    )
    reference_direct_imports = tuple(
        alias.name
        for node in runner_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if "cycle758_selector_multisource" in alias.name
    )

    landed_sync = named_function(
        landed_736_tree, "synchronous_composition_word"
    )
    local_sync = ast.parse(
        inspect.getsource(synchronous_composition_word)
    ).body[0]
    reference_clean = named_function(reference_tree, "clean_postimage")
    local_clean = ast.parse(inspect.getsource(clean_postimage)).body[0]
    exact_sync_reconstruction = (
        ast.dump(landed_sync, include_attributes=False)
        == ast.dump(local_sync, include_attributes=False)
    )
    exact_clean_reconstruction = (
        ast.dump(reference_clean, include_attributes=False)
        == ast.dump(local_clean, include_attributes=False)
    )

    return {
        "AUDIT_INPUT_PATHS_literal_tuple": literal_audit_tuple,
        "DECLARED_INPUT_PATHS_identity":
            DECLARED_INPUT_PATHS is AUDIT_INPUT_PATHS,
        "exact_imports": {
            alias: imports.get(alias) for alias in ("F750", "K")
        }
        == {
            "F750":
                "frontier_cycle750_actual_selector_stretch_2026_07_28",
            "K":
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        },
        "reference_imports": {
            alias: reference_imports.get(alias)
            for alias in ("F750", "M736", "K")
        },
        "reference_imports_exact": {
            alias: reference_imports.get(alias)
            for alias in ("F750", "M736", "K")
        }
        == {
            "F750":
                "frontier_cycle750_actual_selector_stretch_2026_07_28",
            "M736":
                "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
            "K":
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        },
        "reference_selector_tokens_exact": all(
            token in reference_selector_ast
            for token in required_selector_tokens
        ),
        "reference_selector_ast_sha256":
            sha256(reference_selector_ast.encode("utf-8")).hexdigest(),
        "landed_736_synchronous_composition_exact":
            exact_sync_reconstruction,
        "reference_clean_postimage_exact":
            exact_clean_reconstruction,
        "reference_direct_imports": reference_direct_imports,
        "reference_execution_blocklist_violations": dangerous_calls,
        "reference_text_only": (
            not reference_direct_imports and not dangerous_calls
        ),
    }


def source_anchors(
    reference_text: str,
    landed_736_text: str,
) -> dict[str, str]:
    observed = {
        "F750": git_blob_sha(
            (
                ROOT
                / "scripts"
                / "frontier_cycle750_actual_selector_stretch_2026_07_28.py"
            ).read_bytes()
        ),
        "M736": git_blob_sha(landed_736_text.encode("utf-8")),
        "K719": git_blob_sha(
            (
                ROOT
                / "scripts"
                / "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
            ).read_bytes()
        ),
        "REFERENCE_758": git_blob_sha(reference_text.encode("utf-8")),
    }
    return observed


def main() -> int:
    started = monotonic()
    reference_text, reference_provenance = fetch_reference_text()
    landed_736_text, landed_736_provenance = fetch_landed_736_text()
    audit = source_and_reference_audit(reference_text, landed_736_text)
    observed_blobs = source_anchors(reference_text, landed_736_text)

    certificate_a_detail = {
        "observed_blobs": observed_blobs,
        "expected_blobs": EXPECTED_BLOBS,
        "reference_provenance": reference_provenance,
        "landed_736_provenance": landed_736_provenance,
        "reference_sha_printed": observed_blobs["REFERENCE_758"],
    }
    check(
        "CERTIFICATE_A_ANCHORS_AND_REFERENCE_PROVENANCE",
        observed_blobs == EXPECTED_BLOBS
        and reference_provenance["immutable_blob_sha"]
        == REFERENCE_BLOB_SHA
        and reference_provenance["reference_execution"]
        == "TEXT_ONLY_BLOCKED"
        and not audit["reference_direct_imports"]
        and not audit["reference_execution_blocklist_violations"],
        certificate_a_detail,
    )

    first_run = run_experiment()
    key = first_run["key_identity"]
    landed = first_run["landed_horizon"]
    expected_battery = (
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 7),
        (1, 10),
    )
    landed_rows = landed["rows"]
    identity_rows = first_run["landed_horizon_identity_rows"]
    certificate_b_detail = {
        "audit": audit,
        "key_identity": key,
        "cycle758_k2_representatives":
            first_run["cycle758_k2_representatives"],
        "reconstructed_battery": first_run["battery"],
        "landed_horizon_t_SUPPLIED": LANDED_HORIZON_T,
        "landed_survivors": landed["survivors"],
        "landed_failed_exclusions": tuple(
            (row["positions"], row["failed_exclusions"])
            for row in landed_rows
        ),
        "landed_horizon_identity_rows": identity_rows,
    }
    check(
        "CERTIFICATE_B_BATTERY_RECONSTRUCTION_AND_IDENTITY_CONTROLS",
        audit["AUDIT_INPUT_PATHS_literal_tuple"]
        and audit["DECLARED_INPUT_PATHS_identity"]
        and audit["exact_imports"]
        and audit["reference_imports_exact"]
        and audit["reference_selector_tokens_exact"]
        and audit["landed_736_synchronous_composition_exact"]
        and audit["reference_clean_postimage_exact"]
        and first_run["cycle758_k2_representatives"]
        == ((0, 2), (0, 3), (0, 4), (0, 5))
        and first_run["battery"] == expected_battery
        and key
        == {
            "key": (3, (0, 7)),
            "epoch_indexing": "Cycle-750 zero-based event index",
            "event": 3,
            "ordinal_epoch": 4,
            "direction": (0, 1),
            "positions": (0, 7),
            "program_stations": 11,
            "fixture_count": 4,
        }
        and landed["survivor_count"] == 0
        and all(
            row["failed_exclusions"] == ("clean_postimage",)
            for row in landed_rows
        )
        and all(
            row["actual_matches_K_run_orbit"]
            and row["composition_matches_K_run_orbit"]
            and row["rails_match_K_run_orbit"]
            for row in identity_rows
        ),
        certificate_b_detail,
    )

    target_control = first_run["target_control_t370"]
    target_battery = first_run["target_t371"]
    target_row = next(
        row
        for row in target_battery["rows"]
        if row["positions"] == TARGET_POSITIONS
    )
    persistence = first_run["persistence_t372_t376"]
    certificate_c_detail = {
        "t370_control": target_control,
        "t371_target": target_row,
        "outcome": first_run["target_outcome"],
        "which_exclusion": first_run["target_exclusions"],
        "survivor_set_t371": target_battery["survivors"],
        "unique_t371": target_battery["unique"],
        "persistence_window": tuple(
            {
                "horizon_t_SUPPLIED": row["horizon_t_SUPPLIED"],
                "selected": row["selected"],
                "failed_exclusions": row["failed_exclusions"],
            }
            for row in persistence
        ),
    }
    check(
        "CERTIFICATE_C_T371_T370_RUN_AND_OUTCOME",
        not target_control["selected"]
        and target_control["failed_exclusions"]
        == ("clean_postimage",)
        and (
            (
                first_run["target_outcome"] == "SELECTED"
                and target_row["selected"]
                and not target_row["failed_exclusions"]
            )
            or (
                first_run["target_outcome"] == "STILL_EXCLUDED"
                and not target_row["selected"]
                and bool(target_row["failed_exclusions"])
            )
        )
        and tuple(
            row["horizon_t_SUPPLIED"] for row in persistence
        )
        == PERSISTENCE_WINDOW,
        certificate_c_detail,
    )

    cross_rows = first_run["cross_configuration_rows_t371"]
    first_at_371 = next(
        row
        for row in cross_rows
        if row["positions"] == FIRST_TRANSIENT_POSITIONS
    )
    simultaneous_count = first_run[
        "simultaneous_selection_count_t371"
    ]
    certificate_d_detail = {
        "cross_configuration_rows_t371": cross_rows,
        "first_transient_1_10_at_t371": first_at_371,
        "all_other_configs_vetoed":
            all(not row["selected"] for row in cross_rows),
        "simultaneous_selection_count_t371": simultaneous_count,
        "simultaneous_survivors_t371":
            first_run["simultaneous_survivors_t371"],
        "pattern": first_run["pattern"],
        "divergence": first_run["divergence"],
        "first_transient_t252_survivors":
            first_run["first_transient_t252"]["survivors"],
    }
    check(
        "CERTIFICATE_D_CROSS_CONFIGURATIONS_AND_SIMULTANEITY",
        len(cross_rows) == len(expected_battery) - 1
        and first_at_371["positions"] == FIRST_TRANSIENT_POSITIONS
        and simultaneous_count
        == sum(row["selected"] for row in target_battery["rows"])
        and first_run["simultaneous_survivors_t371"]
        == target_battery["survivors"]
        and first_run["pattern"]
        in {"TWO_FOR_TWO_UNIQUE", "DIVERGENT"}
        and (
            first_run["pattern"] != "DIVERGENT"
            or bool(first_run["divergence"])
        ),
        certificate_d_detail,
    )

    second_run = run_experiment()
    first_digest = digest(first_run)
    second_digest = digest(second_run)
    elapsed = monotonic() - started
    supplied_deviations = (
        {
            "name": "extended_horizon",
            "status": "SUPPLIED",
            "definition":
                "terminal orbit index t; exactly t+1 complete "
                "Cycle-719 controller orbits",
            "landed_selector_exclusions_changed": False,
        },
        {
            "name": "battery_transient_rows",
            "status": "SUPPLIED",
            "positions":
                (FIRST_TRANSIENT_POSITIONS, TARGET_POSITIONS),
            "cycle758_family_representatives_changed": False,
        },
        {
            "name": "reference_transport_recovery",
            "status": "SUPPLIED",
            "used":
                reference_provenance["SUPPLIED_transport_deviation"],
            "scientific_law_changed": False,
        },
        {
            "name": "cycle736_checkout_source_adapter",
            "status": "SUPPLIED",
            "used":
                landed_736_provenance[
                    "SUPPLIED_source_availability_adapter"
                ],
            "scientific_law_changed": False,
        },
    )
    boundaries = {
        "horizon_stays_SUPPLIED": True,
        "horizon_is_actuality_or_physical_time": False,
        "actuality_claim": False,
        "fixture_scope_only": True,
        "axiom_update_triggered": False,
        "supplied_deviations": supplied_deviations,
    }
    projected_payload_bytes = len(
        compact(
            {
                "experiment": first_run,
                "boundaries": boundaries,
                "checks": CHECKS,
            }
        ).encode("utf-8")
    ) + len("\n".join(OUTPUT_LINES).encode("utf-8")) + 16 * 1024
    certificate_e_detail = {
        "boundaries": boundaries,
        "determinism_digest_first": first_digest,
        "determinism_digest_second": second_digest,
        "deterministic": first_run == second_run,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "projected_stdout_bytes": projected_payload_bytes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    check(
        "CERTIFICATE_E_BOUNDARIES_DETERMINISM_AND_BOUNDS",
        boundaries["horizon_stays_SUPPLIED"]
        and not boundaries["horizon_is_actuality_or_physical_time"]
        and not boundaries["actuality_claim"]
        and boundaries["fixture_scope_only"]
        and not boundaries["axiom_update_triggered"]
        and all(
            row["status"] == "SUPPLIED"
            for row in supplied_deviations
        )
        and first_run == second_run
        and first_digest == second_digest
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_payload_bytes < STDOUT_LIMIT_BYTES,
        certificate_e_detail,
    )

    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "experiment": first_run,
        "outcome": first_run["target_outcome"],
        "pattern_statement": first_run["pattern"],
        "simultaneous_selection_count_t371": simultaneous_count,
        "simultaneous_survivors_t371":
            first_run["simultaneous_survivors_t371"],
        "boundaries": boundaries,
        "determinism_sha256": first_digest,
        "runtime_seconds": round(elapsed, 6),
        "pass": all(CHECKS.values()),
    }
    report["report_sha256"] = digest(report)
    report["terminal"] = (
        "CYCLE794_SECOND_SELECTION_PASS"
        if report["pass"]
        else "CYCLE794_SECOND_SELECTION_HONEST_FAIL"
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
