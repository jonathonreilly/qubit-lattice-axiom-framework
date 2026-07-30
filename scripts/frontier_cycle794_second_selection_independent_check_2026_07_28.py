#!/usr/bin/env python3
"""Independent adversarial check of the supplied Cycle-794 horizon claim.

The horizon index remains SUPPLIED: horizon t means t+1 complete landed
Cycle-719 controller orbits.  This checker makes no actuality, physical-time,
probability, or law-landing claim.  It reconstructs the exhaustive separated
k=2 battery without executing the Cycle-758, Cycle-792, or Cycle-794 runners.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import sys
import tempfile
from time import monotonic
import types
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_EVENT = 3
FIRST_KEY = (TARGET_EVENT, (1, 10))
SECOND_KEY = (TARGET_EVENT, (0, 7))
LANDED_T = 0
FIRST_SELECTION_T = 252
SECOND_SELECTION_T = 371
CAPTURE_HORIZONS = (LANDED_T, FIRST_SELECTION_T, SECOND_SELECTION_T)
FIRST_WINDOW = tuple(range(251, 257))
SECOND_WINDOW = tuple(range(370, 381))

M736_MODULE = (
    "frontier_cycle736_pairwise_separated_multisource_2026_07_28"
)
M736_PATH = AUDIT_INPUT_PATHS[1]
M736_REF = "origin/physics-loop/toe-close-blockA6-mainbase-20260729"
M736_SPEC = f"{M736_REF}:{M736_PATH}"
REFERENCE_758_MODULE = (
    "frontier_cycle758_selector_multisource_2026_07_28"
)
REFERENCE_758_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
REFERENCE_758_SPEC = (
    "origin/physics-loop/toe-close-blockA5-20260729:"
    + REFERENCE_758_PATH
)
REFERENCE_758_BLOB = "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0"
BLOCKLISTED_PRIMARY_MODULES = (
    "frontier_cycle792_extended_horizon_selector_2026_07_28",
    "frontier_cycle794_second_selection_2026_07_28",
)
EXPECTED_GIT_BLOBS = {
    "F750": "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    "M736": "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    "K719": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    "REFERENCE_758": REFERENCE_758_BLOB,
}
REFERENCE_EXECUTION_BLOCKLIST = (
    REFERENCE_758_MODULE,
    *BLOCKLISTED_PRIMARY_MODULES,
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    framed = f"blob {len(payload)}\0".encode("ascii") + payload
    return sha1(framed).hexdigest()


def state_sha256(state: object) -> str:
    if isinstance(state, int):
        width = max(1, (state.bit_length() + 7) // 8)
        payload = state.to_bytes(width, "little")
    elif isinstance(state, tuple):
        payload = bytes(state)
    else:
        raise TypeError(
            ("unsupported landed state representation", type(state))
        )
    return sha256(payload).hexdigest()


def fixed_command(arguments: tuple[str, ...]) -> subprocess.CompletedProcess:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=False,
        capture_output=True,
        timeout=60,
    )


def read_verified_blob(
    expected_blob: str, preferred_spec: str | None = None
) -> tuple[bytes, dict[str, object]]:
    """Read an immutable Git blob, preferring the named landed path."""

    preferred = (
        fixed_command(("git", "show", preferred_spec))
        if preferred_spec is not None
        else None
    )
    preferred_blob = (
        git_blob_sha(preferred.stdout)
        if preferred is not None and preferred.returncode == 0
        else None
    )
    if (
        preferred is not None
        and preferred.returncode == 0
        and preferred_blob == expected_blob
    ):
        payload = preferred.stdout
        method = "git_show_verified_landed_path"
    else:
        direct = fixed_command(("git", "cat-file", "blob", expected_blob))
        if direct.returncode != 0:
            raise RuntimeError(
                (
                    "immutable blob unavailable",
                    expected_blob,
                    direct.stderr.decode(
                        "utf-8", errors="replace"
                    )[:500],
                )
            )
        payload = direct.stdout
        method = "git_cat_file_immutable_blob"
    observed = git_blob_sha(payload)
    if observed != expected_blob:
        raise AssertionError(
            ("immutable blob mismatch", expected_blob, observed)
        )
    return payload, {
        "expected_git_blob_sha1": expected_blob,
        "observed_git_blob_sha1": observed,
        "preferred_spec": preferred_spec,
        "preferred_spec_present": (
            preferred is not None and preferred.returncode == 0
        ),
        "preferred_spec_blob_sha1": preferred_blob,
        "read_method": method,
    }


def load_verified_m736(payload: bytes) -> Any:
    """Import only the verified Cycle-736 blob.

    Two dependencies unused by this checker are inert stubs.  The checker uses
    only Cycle-736's census helpers and synchronous composition function; both
    depend solely on Python arithmetic and the already imported Cycle-719
    core.
    """

    if git_blob_sha(payload) != EXPECTED_GIT_BLOBS["M736"]:
        raise AssertionError("refusing unpinned Cycle-736 module")
    unused_dependencies = (
        "frontier_cycle735_separated_pair_lawful_control_2026_07_28",
        "frontier_cycle731_token_count_certificate_2026_07_28",
    )
    previous = {
        name: sys.modules.get(name) for name in unused_dependencies
    }
    previous_m736 = sys.modules.get(M736_MODULE)
    with tempfile.TemporaryDirectory(prefix="cycle794-m736-") as directory:
        module_path = Path(directory) / f"{M736_MODULE}.py"
        module_path.write_bytes(payload)
        try:
            for name in unused_dependencies:
                sys.modules[name] = types.ModuleType(name)
            spec = importlib.util.spec_from_file_location(
                M736_MODULE, module_path
            )
            if spec is None or spec.loader is None:
                raise RuntimeError("Cycle-736 import spec unavailable")
            module = importlib.util.module_from_spec(spec)
            sys.modules[M736_MODULE] = module
            spec.loader.exec_module(module)
        except BaseException:
            if previous_m736 is None:
                sys.modules.pop(M736_MODULE, None)
            else:
                sys.modules[M736_MODULE] = previous_m736
            raise
        finally:
            for name, old_module in previous.items():
                if old_module is None:
                    sys.modules.pop(name, None)
                else:
                    sys.modules[name] = old_module
    return module


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def source_control_audit(
    reference_text: str,
) -> dict[str, object]:
    checker_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    reference_tree = ast.parse(reference_text)
    assignments: dict[str, ast.AST] = {}
    direct_imports: dict[str, str] = {}
    for node in checker_tree.body:
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
                direct_imports[alias.asname or alias.name] = alias.name

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    literal_inputs = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(
            assignments["DECLARED_INPUT_PATHS"], ast.Name
        )
        and assignments["DECLARED_INPUT_PATHS"].id
        == "AUDIT_INPUT_PATHS"
    )
    imported_science = {
        alias: direct_imports.get(alias) for alias in ("F750", "K")
    }
    forbidden_direct_imports = tuple(
        imported
        for imported in direct_imports.values()
        if imported in REFERENCE_EXECUTION_BLOCKLIST
    )
    forbidden_runtime_modules = tuple(
        module
        for module in REFERENCE_EXECUTION_BLOCKLIST
        if module in sys.modules
    )
    forbidden_dynamic_calls = tuple(
        ast.unparse(node)
        for node in ast.walk(checker_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"exec", "eval", "compile", "__import__"}
    )

    reference_imports = {
        alias.asname or alias.name: alias.name
        for node in reference_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    reference_audit_node = next(
        node.value
        for node in reference_tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    )
    selector_source = ast.unparse(
        named_function(
            reference_tree,
            "multisource_enforcement_lineage_selector",
        )
    )
    clean_source = ast.unparse(
        named_function(reference_tree, "clean_postimage")
    )
    reference_clean_node = named_function(
        reference_tree, "clean_postimage"
    )
    local_clean_node = named_function(checker_tree, "clean_postimage")

    def without_docstring(
        node: ast.FunctionDef,
    ) -> tuple[ast.stmt, ...]:
        body = tuple(node.body)
        if (
            body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            body = body[1:]
        return body

    clean_reconstruction_exact = (
        ast.dump(
            ast.Module(
                body=list(without_docstring(reference_clean_node)),
                type_ignores=[],
            ),
            include_attributes=False,
        )
        == ast.dump(
            ast.Module(
                body=list(without_docstring(local_clean_node)),
                type_ignores=[],
            ),
            include_attributes=False,
        )
    )
    selector_tokens = (
        "M736.synchronous_composition_word",
        "K.A.apply_semantic",
        "K.run_orbit",
        "reverse=True",
        "'synchronous_composition'",
        "'token_rail_return'",
        "'literal_inverse'",
        "'clean_postimage'",
    )
    expected_reference_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }
    return {
        "AUDIT_INPUT_PATHS_literal_exact": literal_inputs,
        "direct_science_imports": imported_science,
        "M736_import_route": "verified_landed_blob_temporary_module",
        "reference_imports_exact": {
            alias: reference_imports.get(alias)
            for alias in expected_reference_imports
        }
        == expected_reference_imports,
        "reference_AUDIT_INPUT_PATHS_exact":
            tuple(ast.literal_eval(reference_audit_node))
            == AUDIT_INPUT_PATHS,
        "reference_selector_tokens_exact": all(
            token in selector_source for token in selector_tokens
        ),
        "reference_selector_ast_sha256":
            sha256(selector_source.encode("utf-8")).hexdigest(),
        "reference_clean_postimage_ast_sha256":
            sha256(clean_source.encode("utf-8")).hexdigest(),
        "reference_clean_postimage_exact":
            clean_reconstruction_exact,
        "forbidden_direct_imports": forbidden_direct_imports,
        "forbidden_runtime_modules": forbidden_runtime_modules,
        "forbidden_dynamic_calls": forbidden_dynamic_calls,
        "blocklisted_sources": REFERENCE_EXECUTION_BLOCKLIST,
        "reference_758_handling": "TEXT_ONLY_AST_PARSE",
        "reference_or_primary_execution": False,
    }


def circular_distance(left: int, right: int) -> int:
    forward = (right - left) % RING_STATIONS
    return min(forward, RING_STATIONS - forward)


def independent_k2_battery() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if circular_distance(left, right) >= 2
    )


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted(
            (position + shift) % RING_STATIONS
            for position in positions
        )
    )


def translation_families(
    battery: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for positions in battery:
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def independent_composition_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Derive the full orbit word from moving-token incidence."""

    stations = len(program)
    gates = []
    for offset in range(stations):
        occupied = {
            (position + offset) % stations for position in positions
        }
        gates.extend(
            gate
            for station, row in enumerate(program)
            if station in occupied
            for gate in K.mapped_macro(row)
        )
    return tuple(gates)


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


def clean_postimage(after: int, bank_count: int) -> bool:
    """Reconstructed Cycle-758 terminal landed exclusion."""

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


def failed_exclusions(
    conditions: dict[str, bool],
) -> tuple[str, ...]:
    return tuple(
        name for name, passed in conditions.items() if not passed
    )


def apply_word_power(
    state: int, word: tuple[object, ...], exponent: int
) -> int:
    output = state
    for _ in range(exponent):
        output = K.A.apply_semantic(output, word)
    return output


def summarize_selector_row(
    key: tuple[int, tuple[int, ...]],
    horizon: int,
    state: int,
    base_conditions: dict[str, bool],
    literal_inverse: bool,
) -> dict[str, object]:
    conditions = {
        "synchronous_composition":
            base_conditions["synchronous_composition"],
        "token_rail_return":
            base_conditions["token_rail_return"],
        "literal_inverse": literal_inverse,
        "clean_postimage":
            clean_postimage(state, FIXTURE_BANKS),
    }
    failures = failed_exclusions(conditions)
    return {
        "key": key,
        "horizon_t_SUPPLIED": horizon,
        "complete_orbits_applied": horizon + 1,
        "conditions": conditions,
        "failed_exclusions": failures,
        "selected": not failures,
        "postimage_sha256": state_sha256(state),
    }


def target_window(
    M736: Any,
    fixture: tuple[object, ...],
    positions: tuple[int, ...],
    requested: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    event, _direction, program, before, _expected = fixture
    own_word = independent_composition_word(program, positions)
    landed_word = M736.synchronous_composition_word(
        program, positions
    )
    inverse_word = tuple(reversed(own_word))
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = (0,) * len(program)
    semantic_state = before
    controller_state = before
    rows = []
    requested_set = set(requested)
    for horizon in range(max(requested) + 1):
        semantic_state = K.A.apply_semantic(
            semantic_state, own_word
        )
        (
            controller_state,
            rail_a,
            rail_b,
            trace,
        ) = K.run_orbit(
            controller_state,
            program,
            token_positions=positions,
        )
        if horizon not in requested_set:
            continue
        restored = apply_word_power(
            semantic_state, inverse_word, horizon + 1
        )
        conditions = {
            "synchronous_composition": (
                own_word == landed_word
                and semantic_state == controller_state
            ),
            "token_rail_return": (
                rail_a == tokens
                and rail_b == zeros
                and trace == expected_trace(positions)
            ),
            "literal_inverse": restored == before,
            "clean_postimage":
                clean_postimage(semantic_state, FIXTURE_BANKS),
        }
        failures = failed_exclusions(conditions)
        rows.append(
            {
                "key": (event, positions),
                "horizon_t_SUPPLIED": horizon,
                "complete_orbits_applied": horizon + 1,
                "selected": not failures,
                "failed_exclusions": failures,
                "conditions": conditions,
                "controller_identity_exact":
                    semantic_state == controller_state,
                "postimage_sha256": state_sha256(semantic_state),
            }
        )
    return tuple(rows)


def run_experiment(M736: Any) -> dict[str, object]:
    battery = independent_k2_battery()
    families = translation_families(battery)
    census = M736.configuration_census()
    landed_k2 = tuple(
        M736.occupied_sites(configuration)
        for configuration in census["configurations"]
        if sum(configuration) == 2
    )
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    program = fixtures[0][2]
    words = {
        positions: {
            "own": independent_composition_word(program, positions),
            "M736": M736.synchronous_composition_word(
                program, positions
            ),
        }
        for positions in battery
    }

    landed_rows = []
    rows_t252 = []
    rows_t371 = []
    for event, _direction, event_program, before, _expected in fixtures:
        if event_program != program:
            raise AssertionError("fixture programs unexpectedly differ")
        for positions in battery:
            key = (event, positions)
            own_word = words[positions]["own"]
            landed_word = words[positions]["M736"]
            tokens = tuple(
                int(station in positions)
                for station in range(len(program))
            )
            zeros = (0,) * len(program)
            expected = K.A.apply_semantic(before, own_word)
            landed_expected = K.A.apply_semantic(
                before, landed_word
            )
            after, rail_a, rail_b, trace = K.run_orbit(
                before, program, token_positions=positions
            )
            (
                restored,
                inverse_a,
                inverse_b,
                _inverse_trace,
            ) = K.run_orbit(
                after,
                program,
                token_positions=positions,
                reverse=True,
            )
            base_conditions = {
                "synchronous_composition": (
                    own_word == landed_word
                    and after == expected == landed_expected
                ),
                "token_rail_return": (
                    rail_a == tokens
                    and rail_b == zeros
                    and trace == expected_trace(positions)
                ),
                "literal_inverse": (
                    restored == before
                    and inverse_a == rail_a
                    and inverse_b == rail_b
                ),
            }
            landed_conditions = {
                **base_conditions,
                "clean_postimage":
                    clean_postimage(after, FIXTURE_BANKS),
            }
            landed_failures = failed_exclusions(landed_conditions)
            landed_rows.append(
                {
                    "key": key,
                    "conditions": landed_conditions,
                    "failed_exclusions": landed_failures,
                    "selected": not landed_failures,
                    "postimage_sha256": state_sha256(after),
                }
            )

            state = before
            captured: dict[int, int] = {}
            for horizon in range(SECOND_SELECTION_T + 1):
                state = K.A.apply_semantic(state, own_word)
                if horizon in CAPTURE_HORIZONS:
                    captured[horizon] = state
            if captured[LANDED_T] != after:
                raise AssertionError(("landed identity", key))

            inverse_word = tuple(reversed(own_word))
            reverse_state = captured[SECOND_SELECTION_T]
            t252_from_t371 = None
            steps_t371_to_t252 = (
                SECOND_SELECTION_T - FIRST_SELECTION_T
            )
            for reverse_step in range(1, SECOND_SELECTION_T + 2):
                reverse_state = K.A.apply_semantic(
                    reverse_state, inverse_word
                )
                if reverse_step == steps_t371_to_t252:
                    t252_from_t371 = reverse_state
            inverse_t371 = reverse_state == before
            inverse_t252 = (
                t252_from_t371 == captured[FIRST_SELECTION_T]
                and inverse_t371
            )
            rows_t252.append(
                summarize_selector_row(
                    key,
                    FIRST_SELECTION_T,
                    captured[FIRST_SELECTION_T],
                    base_conditions,
                    inverse_t252,
                )
            )
            rows_t371.append(
                summarize_selector_row(
                    key,
                    SECOND_SELECTION_T,
                    captured[SECOND_SELECTION_T],
                    base_conditions,
                    inverse_t371,
                )
            )

    first_window = target_window(
        M736,
        fixtures[TARGET_EVENT],
        FIRST_KEY[1],
        FIRST_WINDOW,
    )
    second_window = target_window(
        M736,
        fixtures[TARGET_EVENT],
        SECOND_KEY[1],
        SECOND_WINDOW,
    )

    def survivors(
        rows: list[dict[str, object]],
    ) -> tuple[tuple[int, tuple[int, ...]], ...]:
        return tuple(row["key"] for row in rows if row["selected"])

    def failure_census(
        rows: list[dict[str, object]],
    ) -> dict[str, int]:
        counts: Counter[str] = Counter()
        for row in rows:
            counts.update(row["failed_exclusions"])
        return dict(sorted(counts.items()))

    landed_by_event = {
        str(event): {
            "rows": sum(row["key"][0] == event for row in landed_rows),
            "survivors": tuple(
                row["key"][1]
                for row in landed_rows
                if row["key"][0] == event and row["selected"]
            ),
        }
        for event in range(len(fixtures))
    }
    word_gate_kinds = tuple(
        sorted(
            {
                gate.kind
                for pair in words.values()
                for gate in pair["own"]
            }
        )
    )
    return {
        "battery": battery,
        "battery_sha256": digest(battery),
        "battery_closed_form_count":
            RING_STATIONS
            * comb(RING_STATIONS - 2, 2)
            // (RING_STATIONS - 2),
        "families": tuple(families.items()),
        "family_representatives": tuple(families),
        "family_sizes": {
            compact(representative): len(alternatives)
            for representative, alternatives in families.items()
        },
        "M736_k2_battery": landed_k2,
        "M736_k2_battery_sorted": tuple(sorted(landed_k2)),
        "M736_census_counts": census["direct_counts_by_k"],
        "M736_census_agreement": census["agreement"],
        "word_match_count": sum(
            pair["own"] == pair["M736"] for pair in words.values()
        ),
        "word_count": len(words),
        "word_gate_kinds": word_gate_kinds,
        "landed_rows": tuple(landed_rows),
        "landed_by_event": landed_by_event,
        "landed_survivors": survivors(landed_rows),
        "landed_failure_census": failure_census(landed_rows),
        "rows_t252": tuple(rows_t252),
        "survivors_t252": survivors(rows_t252),
        "failure_census_t252": failure_census(rows_t252),
        "rows_t371": tuple(rows_t371),
        "survivors_t371": survivors(rows_t371),
        "failure_census_t371": failure_census(rows_t371),
        "first_key_t371": next(
            row for row in rows_t371 if row["key"] == FIRST_KEY
        ),
        "second_key_t371": next(
            row for row in rows_t371 if row["key"] == SECOND_KEY
        ),
        "windows_side_by_side": {
            "cycle792_key_3_1_10_t251_t256": first_window,
            "cycle794_key_3_0_7_t370_t380": second_window,
        },
    }


def main() -> int:
    started = monotonic()
    m736_payload, m736_provenance = read_verified_blob(
        EXPECTED_GIT_BLOBS["M736"], M736_SPEC
    )
    reference_payload, reference_provenance = read_verified_blob(
        REFERENCE_758_BLOB, REFERENCE_758_SPEC
    )
    M736 = load_verified_m736(m736_payload)
    controls = source_control_audit(
        reference_payload.decode("utf-8")
    )
    observed_blobs = {
        "F750": git_blob_sha((ROOT / AUDIT_INPUT_PATHS[0]).read_bytes()),
        "M736": git_blob_sha(m736_payload),
        "K719": git_blob_sha((ROOT / AUDIT_INPUT_PATHS[2]).read_bytes()),
        "REFERENCE_758": git_blob_sha(reference_payload),
    }
    input_resolution = {
        AUDIT_INPUT_PATHS[0]: (ROOT / AUDIT_INPUT_PATHS[0]).is_file(),
        AUDIT_INPUT_PATHS[1]:
            m736_provenance["preferred_spec_present"]
            and m736_provenance["preferred_spec_blob_sha1"]
            == EXPECTED_GIT_BLOBS["M736"],
        AUDIT_INPUT_PATHS[2]: (ROOT / AUDIT_INPUT_PATHS[2]).is_file(),
    }

    first = run_experiment(M736)
    second = run_experiment(M736)
    experiment_deterministic = first == second
    first_digest = digest(first)
    second_digest = digest(second)
    elapsed = monotonic() - started

    landed_event3 = first["landed_by_event"][str(TARGET_EVENT)]
    landed_identity_exact = all(
        row["failed_exclusions"] == ("clean_postimage",)
        and not row["selected"]
        and all(
            passed
            for name, passed in row["conditions"].items()
            if name != "clean_postimage"
        )
        for row in first["landed_rows"]
    )
    certificate_a_detail = {
        "observed_git_blobs": observed_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "input_resolution": input_resolution,
        "M736_provenance": m736_provenance,
        "reference_758_provenance": reference_provenance,
        "reference_758_handling": controls["reference_758_handling"],
        "battery_count": len(first["battery"]),
        "battery_closed_form_count":
            first["battery_closed_form_count"],
        "battery_sha256": first["battery_sha256"],
        "M736_battery_matches":
            first["M736_k2_battery_sorted"] == first["battery"],
        "M736_census_counts": first["M736_census_counts"],
        "family_representatives":
            first["family_representatives"],
        "family_sizes": first["family_sizes"],
        "own_vs_M736_composition_words":
            (first["word_match_count"], first["word_count"]),
        "landed_event3_rows": landed_event3["rows"],
        "landed_event3_survivors": landed_event3["survivors"],
        "landed_survivors_all_176":
            first["landed_survivors"],
        "landed_failure_census_all_176":
            first["landed_failure_census"],
        "landed_identity_controls_exact": landed_identity_exact,
    }
    certificate_a = (
        observed_blobs == EXPECTED_GIT_BLOBS
        and all(input_resolution.values())
        and controls["AUDIT_INPUT_PATHS_literal_exact"]
        and controls["reference_imports_exact"]
        and controls["reference_AUDIT_INPUT_PATHS_exact"]
        and controls["reference_selector_tokens_exact"]
        and controls["reference_clean_postimage_exact"]
        and len(first["battery"]) == 44
        and first["battery_closed_form_count"] == 44
        and first["M736_k2_battery_sorted"] == first["battery"]
        and first["M736_census_counts"] == (1, 11, 44, 77, 55, 11)
        and first["M736_census_agreement"]
        and first["family_representatives"]
        == ((0, 2), (0, 3), (0, 4), (0, 5))
        and set(first["family_sizes"].values()) == {11}
        and first["word_match_count"] == first["word_count"] == 44
        and first["word_gate_kinds"] == ("CNOT", "TOF", "X")
        and landed_event3
        == {"rows": 44, "survivors": ()}
        and all(
            row == {"rows": 44, "survivors": ()}
            for row in first["landed_by_event"].values()
        )
        and first["landed_failure_census"]
        == {"clean_postimage": 176}
        and landed_identity_exact
    )

    second_window = first["windows_side_by_side"][
        "cycle794_key_3_0_7_t370_t380"
    ]
    target_t370 = next(
        row for row in second_window
        if row["horizon_t_SUPPLIED"] == 370
    )
    target_t371 = next(
        row for row in second_window
        if row["horizon_t_SUPPLIED"] == 371
    )
    target_persistence = tuple(
        row for row in second_window
        if row["horizon_t_SUPPLIED"] >= 372
    )
    certificate_b_detail = {
        "key": SECOND_KEY,
        "t370_control": target_t370,
        "t371_recount": target_t371,
        "per_exclusion_certificate_t371":
            target_t371["conditions"],
        "persistence_window_t372_t380": target_persistence,
        "reappears_t372_t380":
            tuple(
                row["horizon_t_SUPPLIED"]
                for row in target_persistence
                if row["selected"]
            ),
    }
    certificate_b = (
        not target_t370["selected"]
        and target_t370["failed_exclusions"]
        == ("clean_postimage",)
        and target_t371["selected"]
        and not target_t371["failed_exclusions"]
        and all(target_t371["conditions"].values())
        and tuple(
            row["horizon_t_SUPPLIED"]
            for row in target_persistence
        )
        == tuple(range(372, 381))
        and all(
            not row["selected"]
            and row["failed_exclusions"] == ("clean_postimage",)
            and row["controller_identity_exact"]
            for row in target_persistence
        )
    )

    first_at_t371 = first["first_key_t371"]
    certificate_c_detail = {
        "rows_recounted_t371": len(first["rows_t371"]),
        "survivor_count_t371": len(first["survivors_t371"]),
        "survivors_t371": first["survivors_t371"],
        "failure_census_t371":
            first["failure_census_t371"],
        "key_3_1_10_landed_test_at_t371": first_at_t371,
        "all_176_rows_t371_verbatim": first["rows_t371"],
        "all_176_rows_t371_sha256": digest(first["rows_t371"]),
    }
    certificate_c = (
        len(first["rows_t371"]) == 176
        and first["survivors_t371"] == (SECOND_KEY,)
        and first["failure_census_t371"]
        == {"clean_postimage": 175}
        and not first_at_t371["selected"]
        and first_at_t371["failed_exclusions"]
        == ("clean_postimage",)
        and not first_at_t371["conditions"]["clean_postimage"]
        and all(
            row["selected"]
            == (row["key"] == SECOND_KEY)
            for row in first["rows_t371"]
        )
    )

    first_window = first["windows_side_by_side"][
        "cycle792_key_3_1_10_t251_t256"
    ]
    first_window_expected = {
        251: False,
        252: True,
        253: False,
        254: False,
        255: False,
        256: False,
    }
    first_window_exact = all(
        row["selected"]
        == first_window_expected[row["horizon_t_SUPPLIED"]]
        and (
            row["failed_exclusions"] == ()
            if row["selected"]
            else row["failed_exclusions"] == ("clean_postimage",)
        )
        and row["controller_identity_exact"]
        for row in first_window
    )
    pattern = (
        "TWO_FOR_TWO_UNIQUE"
        if (
            first["survivors_t252"] == (FIRST_KEY,)
            and first["survivors_t371"] == (SECOND_KEY,)
            and first_window_exact
            and certificate_b
        )
        else "DIVERGENT"
    )
    certificate_d_detail = {
        "rows_recounted_t252": len(first["rows_t252"]),
        "survivor_count_t252": len(first["survivors_t252"]),
        "survivors_t252": first["survivors_t252"],
        "failure_census_t252":
            first["failure_census_t252"],
        "windows_side_by_side":
            first["windows_side_by_side"],
        "pattern_verdict": pattern,
    }
    certificate_d = (
        len(first["rows_t252"]) == 176
        and first["survivors_t252"] == (FIRST_KEY,)
        and first["failure_census_t252"]
        == {"clean_postimage": 175}
        and first_window_exact
        and pattern == "TWO_FOR_TWO_UNIQUE"
    )

    boundaries = {
        "horizon_status": "SUPPLIED",
        "horizon_definition":
            "terminal orbit index t; t+1 complete landed Cycle-719 orbits",
        "actuality_claim": False,
        "physical_time_claim": False,
        "probability_or_weights_used": False,
        "law_landing_claim": False,
        "fixture_scope_only": True,
    }
    controls_without_output = (
        not controls["forbidden_direct_imports"]
        and not controls["forbidden_runtime_modules"]
        and not controls["forbidden_dynamic_calls"]
        and not controls["reference_or_primary_execution"]
        and controls["reference_758_handling"]
        == "TEXT_ONLY_AST_PARSE"
        and experiment_deterministic
        and first_digest == second_digest
        and elapsed < AUDIT_TIMEOUT_SEC
        and boundaries
        == {
            "horizon_status": "SUPPLIED",
            "horizon_definition":
                "terminal orbit index t; t+1 complete landed "
                "Cycle-719 orbits",
            "actuality_claim": False,
            "physical_time_claim": False,
            "probability_or_weights_used": False,
            "law_landing_claim": False,
            "fixture_scope_only": True,
        }
    )

    base_certificates = (
        (
            "CERTIFICATE_A_BATTERY_FIDELITY_AND_LANDED_IDENTITY",
            certificate_a,
            certificate_a_detail,
        ),
        (
            "CERTIFICATE_B_T371_RECOUNT_AND_EXTENDED_PERSISTENCE",
            certificate_b,
            certificate_b_detail,
        ),
        (
            "CERTIFICATE_C_FULL_176_UNIQUENESS_AND_SIMULTANEITY",
            certificate_c,
            certificate_c_detail,
        ),
        (
            "CERTIFICATE_D_CYCLE792_WINDOW_AND_PATTERN_ATTACK",
            certificate_d,
            certificate_d_detail,
        ),
    )

    def render(stdout_bytes: int) -> tuple[str, bool]:
        certificate_e_detail = {
            "controls": controls,
            "observed_git_blobs": observed_blobs,
            "expected_git_blobs": EXPECTED_GIT_BLOBS,
            "blocklist_clean": (
                not controls["forbidden_direct_imports"]
                and not controls["forbidden_runtime_modules"]
                and not controls["forbidden_dynamic_calls"]
            ),
            "determinism_sha256_first": first_digest,
            "determinism_sha256_second": second_digest,
            "deterministic": experiment_deterministic,
            "boundaries": boundaries,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        certificate_e = (
            controls_without_output
            and observed_blobs == EXPECTED_GIT_BLOBS
            and stdout_bytes < STDOUT_LIMIT_BYTES
        )
        certificates = base_certificates + (
            (
                "CERTIFICATE_E_CONTROLS_DETERMINISM_AND_BOUNDS",
                certificate_e,
                certificate_e_detail,
            ),
        )
        checks = {
            label: bool(passed)
            for label, passed, _detail in certificates
        }
        passed = all(checks.values())
        summary = {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
            "checks": checks,
            "checks_passed": sum(checks.values()),
            "checks_failed": sum(not value for value in checks.values()),
            "windows_side_by_side":
                first["windows_side_by_side"],
            "survivors_t252": first["survivors_t252"],
            "survivors_t371": first["survivors_t371"],
            "simultaneous_selection_count_t371":
                len(first["survivors_t371"]),
            "pattern_verdict": pattern,
            "runtime_seconds": round(elapsed, 6),
            "determinism_sha256": first_digest,
            "pass": passed,
            "terminal": (
                "CYCLE794_SECOND_SELECTION_INDEPENDENT_CHECK_PASS"
                if passed
                else
                "CYCLE794_SECOND_SELECTION_INDEPENDENT_CHECK_HONEST_FAIL"
            ),
        }
        summary["report_sha256"] = digest(summary)
        lines = [
            (
                ("PASS " if cert_pass else "FAIL ")
                + label
                + " :: "
                + compact(detail)
            )
            for label, cert_pass, detail in certificates
        ]
        lines.append(
            "WINDOWS_SIDE_BY_SIDE :: "
            + compact(first["windows_side_by_side"])
        )
        lines.append(compact(summary))
        return "\n".join(lines) + "\n", passed

    size_guess = 0
    output = ""
    passed = False
    for _iteration in range(8):
        output, passed = render(size_guess)
        observed_size = len(output.encode("utf-8"))
        if observed_size == size_guess:
            break
        size_guess = observed_size
    else:
        raise AssertionError("stdout byte count did not stabilize")
    if len(output.encode("utf-8")) != size_guess:
        raise AssertionError("stdout byte count drift")
    if size_guess >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", size_guess, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
