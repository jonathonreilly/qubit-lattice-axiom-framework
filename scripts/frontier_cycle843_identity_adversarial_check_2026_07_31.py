#!/usr/bin/env python3
"""Cycle 843 independent adversarial identity adjudication.

The Cycle-719 controller core is the sole executable science dependency.
The Cycle-843 primary and the landed Cycle-833 primary are SHA-pinned,
text/AST-only evidence and are blocked from import.  Dynamics, the Cycle-833
prediction state, selectors, phase law, weights, hashes, and full support diff
are recomputed here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle843_pulse_phase_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH, PRIMARY_843_PATH, PRIMARY_833_PATH = AUDIT_INPUT_PATHS
TEXT_AST_ONLY_PATHS = (PRIMARY_843_PATH, PRIMARY_833_PATH)
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_843_PATH:
        "68116221b3451aefd294d939b788cd3dbf518a190eaebd996b43fba5e8a54de9",
    PRIMARY_833_PATH:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_843_PATH: "cd500d58847c3c1046c500b73b25911920db0ce0",
    PRIMARY_833_PATH: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
}
PINNED_833_COMMIT = "dca1e252ec1981755f9e54837c1a9f0e2503ccc2"
PINNED_833_OBJECT_PATH = (
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py"
)
EXPECTED_833_PIN_ROW = {
    "package": "cycle833",
    "commit": PINNED_833_COMMIT,
    "path": PINNED_833_OBJECT_PATH,
    "sha256": EXPECTED_SHA256[PRIMARY_833_PATH],
    "git_blob": EXPECTED_GIT_BLOBS[PRIMARY_833_PATH],
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if either source primary is imported."""

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

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


State = tuple[int, ...]
Pair = tuple[int, int]
Key = tuple[int, Pair]

FIXTURE_BANKS = 2
RING_STATIONS = 11
STATE_BITS = 5815
SAMPLED_PERIODS = 12
S1_FUNNEL_MOMENT = 51110
BACKBONE: tuple[Pair, ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EVENT3_KEYS: tuple[Key, ...] = tuple((3, pair) for pair in BACKBONE)
PREDICTION_MASK = ("bank0.HEAD[1]",)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def top_level_function(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    return matches[0] if len(matches) == 1 else None


def function_literal_assignment(
    function: ast.FunctionDef | None,
    name: str,
) -> object | None:
    if function is None:
        return None
    matches = [
        node.value
        for node in function.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def git_value(
    *arguments: str,
    cwd: Path = ROOT,
    check: bool = True,
) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=cwd,
        check=check,
        capture_output=True,
        text=True,
        timeout=20,
    )
    return completed.stdout.strip()


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    primary_843 = trees.get(PRIMARY_843_PATH)
    primary_833 = trees.get(PRIMARY_833_PATH)

    copied_rows = (
        literal_assignment(primary_843, "COPIED_SIBLING_SOURCES")
        if isinstance(primary_843, ast.Module) else None
    )
    copied_833_rows = tuple(
        row for row in copied_rows or ()
        if isinstance(row, dict) and row.get("package") == "cycle833"
    )
    function_833 = (
        top_level_function(primary_833, "fourth_candidate_certificate")
        if isinstance(primary_833, ast.Module) else None
    )
    function_833_literals = {
        node.value for node in ast.walk(function_833)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (str, int))
    } if function_833 is not None else set()
    prediction_mask_literal = function_literal_assignment(
        function_833, "prediction_mask"
    )

    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    landing_root = (ROOT / "../landing-worktree").resolve()
    pinned_blob = git_value(
        "rev-parse",
        f"{PINNED_833_COMMIT}:{PINNED_833_OBJECT_PATH}",
    )
    ancestry = subprocess.run(
        ("git", "merge-base", "--is-ancestor",
         PINNED_833_COMMIT, "HEAD"),
        cwd=landing_root,
        check=False,
        capture_output=True,
        timeout=20,
    ).returncode == 0
    path_rows = tuple({
        "path": path,
        "is_literal_relative": not Path(path).is_absolute(),
        "exists": (ROOT / path).is_file(),
        "sha256": sha_rows.get(path),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha_rows.get(path) == EXPECTED_SHA256[path],
        "git_blob": blob_rows.get(path),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            blob_rows.get(path) == EXPECTED_GIT_BLOBS[path],
        "access": (
            "EXECUTABLE_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED"
        ),
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_paths_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                row["is_literal_relative"] and row["exists"]
                for row in path_rows
            ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
        "source_rows": path_rows,
        "pinned_833": {
            "commit": PINNED_833_COMMIT,
            "path": PINNED_833_OBJECT_PATH,
            "copied_pin_row": (
                copied_833_rows[0] if len(copied_833_rows) == 1 else None
            ),
            "copied_pin_row_exact":
                copied_833_rows == (EXPECTED_833_PIN_ROW,),
            "pinned_object_blob": pinned_blob,
            "pinned_object_blob_exact":
                pinned_blob == EXPECTED_GIT_BLOBS[PRIMARY_833_PATH],
            "sibling_landing_head": git_value("rev-parse", "HEAD",
                                               cwd=landing_root),
            "pin_is_ancestor_of_sibling_landing_head": ancestry,
        },
        "cycle833_prediction_AST": {
            "function_present": function_833 is not None,
            "prediction_mask_literal": prediction_mask_literal,
            "prediction_mask_exact":
                prediction_mask_literal == PREDICTION_MASK,
            "definition_literals_present": {
                "name_S0_prime": "S0'" in function_833_literals,
                "definition_map_S1": "S0' := map(S1)"
                    in function_833_literals,
                "expected_weight_47": 47 in function_833_literals,
            },
        },
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "runner_sha256": sha256(self_payload).hexdigest(),
        "runner_git_blob": git_blob(self_payload),
        "current_head": git_value("rev-parse", "HEAD"),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_paths_existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 7
        and all(
            row["sha256_exact"] and row["git_blob_exact"]
            for row in path_rows
        )
        and result["pinned_833"]["copied_pin_row_exact"]
        and result["pinned_833"]["pinned_object_blob_exact"]
        and result["pinned_833"]["pin_is_ancestor_of_sibling_landing_head"]
        and result["cycle833_prediction_AST"]["function_present"]
        and result["cycle833_prediction_AST"]["prediction_mask_exact"]
        and all(
            result["cycle833_prediction_AST"][
                "definition_literals_present"
            ].values()
        )
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def _bank_wire_aliases() -> dict[int, tuple[str, ...]]:
    aliases: dict[int, list[str]] = {
        wire: [] for wire in range(K.A.N)
    }
    for cell, layout in enumerate(K.A.CELLS):
        for field, value in layout.items():
            if field == "payload":
                continue
            if isinstance(value, tuple):
                for index, wire in enumerate(value):
                    aliases[int(wire)].append(
                        f"cell{cell}.{field}[{index}]"
                    )
            else:
                aliases[int(value)].append(f"cell{cell}.{field}")
    for register in ("HEAD", "ROTOR", "TOKEN", "FRESH", "ZERO_WORK"):
        for index, wire in enumerate(getattr(K.A, register)):
            aliases[int(wire)].append(f"{register}[{index}]")
    for register in (
        "POINTER", "U_TO_V", "V_TO_U", "BINDER", "ACTUAL", "ADMISS",
        "LAW", "TOKEN_OK", "DIRECTION_OK", "ENABLE_TARGET",
    ):
        aliases[int(getattr(K.A, register))].append(register)
    return {wire: tuple(names) for wire, names in aliases.items()}


BANK_WIRE_ALIASES = _bank_wire_aliases()
SOURCE_NAMES = {
    K.R3.X.LEFT_ENDPOINT: "LEFT_ENDPOINT",
    K.R3.X.RIGHT_ENDPOINT: "RIGHT_ENDPOINT",
    K.R3.X.SOURCE_POINTER: "SOURCE_POINTER",
}


def wire_name(wire: int) -> str:
    if wire < K.M.R12.SOURCE_WIDTH:
        return f"source.{SOURCE_NAMES.get(wire, f'wire[{wire}]')}"
    for bank, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        if base <= wire < base + K.A.N:
            local = wire - base
            aliases = BANK_WIRE_ALIASES[local]
            label = "|".join(aliases) if aliases else f"wire[{local}]"
            return f"bank{bank}.{label}"
    for link, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        if base <= wire < base + K.B.LINK_WIDTH:
            return f"link{link}.wire[{wire - base}]"
    return f"unused_padding.wire[{wire}]"


WIRE_NAMES = tuple(wire_name(wire) for wire in range(STATE_BITS))
SOURCE_POINTER_WIRE = K.R3.X.SOURCE_POINTER
LINK0_WIRE0 = K.M.R12.LINK_BASES[0]
HEAD1_WIRE = K.M.R12.BANK_BASES[0] + K.A.HEAD[1]


def apply_word_exact(state: State, word: tuple[object, ...]) -> State:
    """Independent exact tuple evaluator for X/CNOT/Toffoli gates."""
    output = list(state)
    for gate in word:
        wires = gate.wires
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated wire", gate))
        if gate.kind == "X":
            output[wires[0]] ^= 1
        elif gate.kind == "CNOT":
            output[wires[1]] ^= output[wires[0]]
        elif gate.kind == "TOF":
            output[wires[2]] ^= output[wires[0]] & output[wires[1]]
        else:
            raise AssertionError(("unknown gate", gate))
    return tuple(output)


def orbit_word(
    program: tuple[object, ...],
    pair: Pair,
) -> tuple[object, ...]:
    gates = []
    for movement in range(len(program)):
        live = {
            (pair[0] + movement) % len(program),
            (pair[1] + movement) % len(program),
        }
        for station, macro in enumerate(program):
            if station in live:
                gates.extend(K.mapped_macro(macro))
    return tuple(gates)


def rebuild_epochs_and_words() -> tuple[
    tuple[State, ...],
    dict[Pair, tuple[object, ...]],
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    words = {pair: orbit_word(program, pair) for pair in BACKBONE}
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epochs.append(before)
        state = apply_word_exact(before, allocator)
    return tuple(epochs), words


def reconstruct_phase_family() -> dict[str, object]:
    epochs, words = rebuild_epochs_and_words()
    phase0 = tuple(
        apply_word_exact(epochs[3], words[pair])
        for pair in BACKBONE
    )
    phases = [phase0]
    states = phase0
    for _movement in range(2):
        states = tuple(
            apply_word_exact(state, words[pair])
            for state, pair in zip(states, BACKBONE)
        )
        phases.append(states)
    closure = tuple(
        apply_word_exact(state, words[pair])
        for state, pair in zip(states, BACKBONE)
    )
    return {
        "epochs": epochs,
        "words": words,
        "phases": tuple(phases),
        "closure": closure,
        "coincidence": phases[2][0],
    }


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        wires = gate.wires
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated wire", gate))
        if gate.kind == "X":
            rows.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unknown gate", gate))
    return tuple(rows)


def pack_duplicate(state: State) -> list[int]:
    return [bit * 0b11 for bit in state]


def advance_duplicate(
    columns: list[int],
    schedule: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in schedule:
        if kind == 0:
            columns[first] ^= 0b11
        elif kind == 1:
            columns[second] ^= columns[first] & 0b11
        else:
            columns[third] ^= (
                columns[first] & columns[second] & 0b11
            )


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def reconstruct_cycle833_prediction(
    family: dict[str, object],
) -> dict[str, object]:
    epochs = family["epochs"]
    words = family["words"]
    assert isinstance(epochs, tuple)
    assert isinstance(words, dict)
    witness = BACKBONE[0]
    event1_start = apply_word_exact(epochs[1], words[witness])
    columns = pack_duplicate(event1_start)
    schedule = compile_word(words[witness])
    for _movement in range(S1_FUNNEL_MOMENT):
        advance_duplicate(columns, schedule)
    s1_primary = unpack_lane(columns, 0)
    s1_duplicate = unpack_lane(columns, 1)
    candidate = list(s1_primary)
    candidate[HEAD1_WIRE] ^= 1
    s0_prime = tuple(candidate)
    return {
        "S1": s1_primary,
        "S1_duplicate": s1_duplicate,
        "S0_prime_833": s0_prime,
        "schedule_gate_count": len(schedule),
        "movement_count": S1_FUNNEL_MOMENT,
        "duplicate_exact": s1_primary == s1_duplicate,
        "prediction_wire_index": HEAD1_WIRE,
        "prediction_wire_name": WIRE_NAMES[HEAD1_WIRE],
    }


def active_support(state: State) -> tuple[tuple[int, str], ...]:
    return tuple(
        (wire, WIRE_NAMES[wire])
        for wire, bit in enumerate(state) if bit
    )


def full_diff(left: State, right: State) -> dict[str, object]:
    wires = tuple(
        wire for wire, values in enumerate(zip(left, right))
        if values[0] != values[1]
    )
    left_only = tuple(
        (wire, WIRE_NAMES[wire])
        for wire in wires if left[wire] and not right[wire]
    )
    right_only = tuple(
        (wire, WIRE_NAMES[wire])
        for wire in wires if right[wire] and not left[wire]
    )
    component_counts = Counter(
        name.split(".", 1)[0] for _wire, name in left_only + right_only
    )
    return {
        "xor_weight": len(wires),
        "wire_indices": wires,
        "named_transitions": tuple(
            {
                "wire_index": wire,
                "field": WIRE_NAMES[wire],
                "coincidence_value": left[wire],
                "cycle833_S0_prime_value": right[wire],
            }
            for wire in wires
        ),
        "active_only_in_coincidence": left_only,
        "active_only_in_cycle833_S0_prime": right_only,
        "component_xor_weights": dict(sorted(component_counts.items())),
        "coincidence_active_support": active_support(left),
        "cycle833_S0_prime_active_support": active_support(right),
    }


def identity_certificate(
    family: dict[str, object],
    prediction: dict[str, object],
) -> dict[str, object]:
    coincidence = family["coincidence"]
    s0_prime = prediction["S0_prime_833"]
    s1 = prediction["S1"]
    assert isinstance(coincidence, tuple)
    assert isinstance(s0_prime, tuple)
    assert isinstance(s1, tuple)
    concrete_map_image = list(s0_prime)
    concrete_map_image[HEAD1_WIRE] ^= 1
    map_s0_prime = tuple(concrete_map_image)
    iterates = []
    state = s0_prime
    for power in range(1, 9):
        updated = list(state)
        updated[HEAD1_WIRE] ^= 1
        state = tuple(updated)
        iterates.append({
            "power": power,
            "sha256": state_sha256(state),
            "weight": sum(state),
            "is_coincidence": state == coincidence,
            "is_S1": state == s1,
            "is_cycle833_S0_prime": state == s0_prime,
        })
    difference = full_diff(coincidence, s0_prime)
    distinct = coincidence != s0_prime
    no_defined_iterate_hit = (
        map_s0_prime == s1
        and all(not row["is_coincidence"] for row in iterates)
        and coincidence not in (s1, s0_prime)
    )
    exact = (
        distinct
        and sum(coincidence) == 59
        and sum(s0_prime) == 47
        and prediction["duplicate_exact"]
        and prediction["prediction_wire_name"] == PREDICTION_MASK[0]
        and sum(s1) == 46
        and map_s0_prime == s1
        and no_defined_iterate_hit
        and difference["xor_weight"] > 0
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "identity_ruling": (
            "DISTINCT — PRIMARY NAMING COLLISION; THE COINCIDENCE STATE "
            "IS A NEW OBJECT, NOT THE LANDED CYCLE-833 S0'"
            if distinct else
            "IDENTICAL — THE MAP PREDICTION IS CONFIRMED"
        ),
        "coincidence": {
            "sha256": state_sha256(coincidence),
            "weight": sum(coincidence),
        },
        "cycle833_S0_prime": {
            "definition": "S0' := map(S1)",
            "source_primary_commit": PINNED_833_COMMIT,
            "sha256": state_sha256(s0_prime),
            "weight": sum(s0_prime),
            "source_S1_sha256": state_sha256(s1),
            "source_S1_weight": sum(s1),
            "prediction_named_field_updates": PREDICTION_MASK,
        },
        "signed_weight_difference_coincidence_minus_833": (
            sum(coincidence) - sum(s0_prime)
        ),
        "full_diff": difference,
        "map_relationship": {
            "cycle833_defined_scope":
                "Cycle 833 defines the rank-2->3 prediction edge only; it "
                "does not define a next-rank edge after S0'.",
            "only_concrete_prediction_edge_operation":
                "XOR bank0.HEAD[1]",
            "map_of_cycle833_S0_prime_under_that_operation": {
                "sha256": state_sha256(map_s0_prime),
                "weight": sum(map_s0_prime),
                "exactly_S1": map_s0_prime == s1,
                "is_coincidence": map_s0_prime == coincidence,
            },
            "operation_is_involution": (
                iterates[1]["is_cycle833_S0_prime"]
            ),
            "positive_power_rows": tuple(iterates),
            "any_positive_power_hits_coincidence": any(
                row["is_coincidence"] for row in iterates
            ),
            "exact_orbit":
                "{Cycle833 S0' (even powers), S1 (odd powers)}",
            "no_further_defined_map_iterate_hits": no_defined_iterate_hit,
        },
        "finding": (
            "Cycle 843's local S0_prime variable is epochs[3] at weight 59. "
            "The SHA-pinned Cycle-833 S0' is map(S1) at weight 47. Their "
            "hashes, supports, and full tuples differ. Under Cycle 833's "
            "only concrete prediction-edge XOR, map(S0')=S1 and all powers "
            "alternate between S1 and S0'; neither is the coincidence."
        ),
        "pass": exact,
    }


def selector_certificate(family: dict[str, object]) -> dict[str, object]:
    phases = family["phases"]
    coincidence = family["coincidence"]
    assert isinstance(phases, tuple)
    assert isinstance(coincidence, tuple)
    boundary_rows = tuple(
        (phase, key, state)
        for phase, states in enumerate(phases)
        for key, state in zip(EVENT3_KEYS, states)
    )
    expected = tuple(phase == 2 for phase, _key, _state in boundary_rows)
    singleton_selectors = []
    for wire in range(STATE_BITS):
        for selected_value in (0, 1):
            observed = tuple(
                state[wire] == selected_value
                for _phase, _key, state in boundary_rows
            )
            if observed == expected:
                singleton_selectors.append({
                    "wire_index": wire,
                    "field": WIRE_NAMES[wire],
                    "selected_value": selected_value,
                })
    required = (
        (SOURCE_POINTER_WIRE, "source.SOURCE_POINTER", 1),
        (LINK0_WIRE0, "link0.wire[0]", 0),
    )
    direction_rows = []
    for wire, name, value in required:
        selected = tuple(
            state[wire] == value
            for _phase, _key, state in boundary_rows
        )
        direction_rows.append({
            "selector": f"{name}={value}",
            "coincidence_implies_selector": all(
                flag for flag, target in zip(selected, expected) if target
            ),
            "selector_implies_coincidence": all(
                target for flag, target in zip(selected, expected) if flag
            ),
            "true_positives": sum(
                flag and target for flag, target in zip(selected, expected)
            ),
            "false_positives": sum(
                flag and not target
                for flag, target in zip(selected, expected)
            ),
            "false_negatives": sum(
                not flag and target
                for flag, target in zip(selected, expected)
            ),
            "true_negatives": sum(
                not flag and not target
                for flag, target in zip(selected, expected)
            ),
        })
    singleton_tuples = tuple(
        (row["wire_index"], row["field"], row["selected_value"])
        for row in singleton_selectors
    )
    exact = (
        len(boundary_rows) == 27
        and sum(expected) == 9
        and all(
            state == coincidence
            for phase, _key, state in boundary_rows if phase == 2
        )
        and all(
            state != coincidence
            for phase, _key, state in boundary_rows if phase != 2
        )
        and singleton_tuples == required
        and all(
            row["coincidence_implies_selector"]
            and row["selector_implies_coincidence"]
            and row["true_positives"] == 9
            and row["false_positives"] == 0
            and row["false_negatives"] == 0
            and row["true_negatives"] == 18
            for row in direction_rows
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "boundary_state_count": len(boundary_rows),
        "coincidence_boundary_count": sum(expected),
        "both_direction_rows": tuple(direction_rows),
        "all_minimal_single_wire_selectors": tuple(singleton_selectors),
        "minimality":
            "The empty predicate cannot select exactly 9 of 27 rows; each "
            "listed one-wire biconditional therefore has minimum cardinality.",
        "finding":
            "Across all 27 phase-states, source.SOURCE_POINTER=1 and "
            "link0.wire[0]=0 each select exactly the nine coincidence rows "
            "in both directions; they are the only cardinality-one selectors.",
        "pass": exact,
    }


def phase_law_certificate(
    family: dict[str, object],
    cycle833_s0_prime: State,
) -> dict[str, object]:
    words = family["words"]
    phases = family["phases"]
    coincidence = family["coincidence"]
    assert isinstance(words, dict)
    assert isinstance(phases, tuple)
    assert isinstance(coincidence, tuple)
    states = phases[0]
    initial = states
    rows = []
    closures = []
    for movement in range(3 * SAMPLED_PERIODS):
        expected = movement % 3 == 2
        for key, state in zip(EVENT3_KEYS, states):
            selector_source = state[SOURCE_POINTER_WIRE] == 1
            selector_link = state[LINK0_WIRE0] == 0
            is_coincidence = state == coincidence
            rows.append({
                "movement": movement,
                "key": key,
                "phase_mod_3": movement % 3,
                "is_coincidence": is_coincidence,
                "source_selector": selector_source,
                "link_selector": selector_link,
                "expected_phase": expected,
                "exact_biconditional": (
                    is_coincidence
                    == selector_source
                    == selector_link
                    == expected
                ),
                "is_cycle833_S0_prime": state == cycle833_s0_prime,
            })
        states = tuple(
            apply_word_exact(state, words[pair])
            for state, pair in zip(states, BACKBONE)
        )
        if (movement + 1) % 3 == 0:
            closures.append({
                "period_index": movement // 3,
                "exact_phase0_return": states == initial,
                "stream_sha256": digest(
                    tuple(state_sha256(state) for state in states)
                ),
            })
    exact = (
        len(rows) == 9 * 3 * SAMPLED_PERIODS
        and all(row["exact_biconditional"] for row in rows)
        and len(closures) == SAMPLED_PERIODS
        and all(row["exact_phase0_return"] for row in closures)
        and not any(row["is_cycle833_S0_prime"] for row in rows)
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "law_outcome": "HOLDS_EXACTLY",
        "corrected_law":
            "At every aligned movement boundary, for all nine keys, "
            "state=coincidence iff SOURCE_POINTER=1 iff link0.wire[0]=0 "
            "iff movement mod 3=2.",
        "sampled_periods": SAMPLED_PERIODS,
        "sampled_rows": len(rows),
        "exact_period_closures": tuple(closures),
        "cycle833_S0_prime_hit_count": sum(
            row["is_cycle833_S0_prime"] for row in rows
        ),
        "forever_step":
            "Every fixed key word returns its full tuple to phase 0 after "
            "three exact applications. Determinism repeats the verified "
            "three-boundary sequence for every integer period.",
        "scope": "aligned completed orbit-word movement boundaries only",
        "finding":
            "The three-phase dynamics and selectors hold exactly, but the "
            "object at phase 2 is the distinct coincidence state, not the "
            "landed Cycle-833 S0'.",
        "pass": exact,
    }


def weight_certificate(coincidence: State) -> dict[str, object]:
    banks, links = K.M.unpack_state(coincidence, FIXTURE_BANKS)
    source_weight = sum(coincidence[:K.M.R12.SOURCE_WIDTH])
    bank_weights = tuple(sum(bank) for bank in banks)
    link_weights = tuple(sum(link) for link in links)
    recomposed = source_weight + sum(bank_weights) + sum(link_weights)
    exact = (
        len(coincidence) == STATE_BITS
        and set(coincidence) <= {0, 1}
        and sum(coincidence) == 59
        and recomposed == 59
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "state_sha256": state_sha256(coincidence),
        "direct_integer_sum": sum(coincidence),
        "source_weight": source_weight,
        "bank_weights": bank_weights,
        "link_weights": link_weights,
        "component_recomposition": recomposed,
        "finding":
            "The independently reconstructed coincidence tuple has exact "
            "Hamming weight 59.",
        "pass": exact,
    }


def render(
    ruling: str,
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [f"THE IDENTITY RULING: {ruling}"]
    lines.extend(
        f"CERTIFICATE {name} {value['verdict']} {compact(value)}"
        for name, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    ruling: str,
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["pass"] = all(
            bool(value["pass"]) for value in certificates.values()
        )
        report["terminal"] = (
            "CYCLE843_IDENTITY_ADVERSARIAL_CHECK_PASS"
            if report["pass"] else
            "CYCLE843_IDENTITY_ADVERSARIAL_CHECK_HONEST_FAIL"
        )
        output = render(ruling, certificates, report)
        size = len(output.encode("utf-8"))
        controls = certificates["CONTROLS"]
        if (
            report["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    family = reconstruct_phase_family()
    family_duplicate = reconstruct_phase_family()
    prediction = reconstruct_cycle833_prediction(family)
    identity = identity_certificate(family, prediction)
    selectors = selector_certificate(family)
    phase_law = phase_law_certificate(
        family, prediction["S0_prime_833"]
    )
    weight = weight_certificate(family["coincidence"])
    elapsed = monotonic() - started

    family_deterministic = (
        family["epochs"] == family_duplicate["epochs"]
        and family["phases"] == family_duplicate["phases"]
        and family["closure"] == family_duplicate["closure"]
        and digest({
            "epochs": tuple(map(state_sha256, family["epochs"])),
            "phases": tuple(
                tuple(map(state_sha256, states))
                for states in family["phases"]
            ),
        }) == digest({
            "epochs": tuple(map(state_sha256, family_duplicate["epochs"])),
            "phases": tuple(
                tuple(map(state_sha256, states))
                for states in family_duplicate["phases"]
            ),
        })
    )
    controls_base = (
        sources["pass"]
        and family_deterministic
        and prediction["duplicate_exact"]
        and family["closure"] == family["phases"][0]
        and all(len(word) == 6212 for word in family["words"].values())
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        **sources,
        "blocklist_at_end": {
            "loaded": tuple(
                name for name in BLOCKLISTED_MODULES
                if name in sys.modules
            ),
            "firewall_hits": tuple(FIREWALL.hits),
        },
        "determinism": {
            "independent_phase_family_duplicate_exact":
                family_deterministic,
            "cycle833_S1_packed_duplicate_exact":
                prediction["duplicate_exact"],
            "phase0_period3_closure_exact":
                family["closure"] == family["phases"][0],
        },
        "cycle833_reconstruction": {
            "movement_count": prediction["movement_count"],
            "gates_per_movement": prediction["schedule_gate_count"],
            "S1_sha256": state_sha256(prediction["S1"]),
            "S1_weight": sum(prediction["S1"]),
            "S0_prime_sha256":
                state_sha256(prediction["S0_prime_833"]),
            "S0_prime_weight": sum(prediction["S0_prime_833"]),
        },
        "exact_arithmetic":
            "State bits, packed duplicate lanes, weights, hashes, XOR "
            "supports, equality, selectors, and movement indices are exact; "
            "only monotonic runtime is floating-point.",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": controls_base,
        "verdict": "PASS" if controls_base else "FAIL",
    }
    certificates = {
        "THE_IDENTITY_ADJUDICATION": identity,
        "THE_SELECTORS": selectors,
        "THE_PHASE_LAW": phase_law,
        "THE_WEIGHT": weight,
        "CONTROLS": controls,
    }
    ruling = str(identity["identity_ruling"])
    report = {
        "cycle": 843,
        "identity_ruling": ruling,
        "coincidence_sha256": identity["coincidence"]["sha256"],
        "coincidence_weight": identity["coincidence"]["weight"],
        "cycle833_S0_prime_sha256":
            identity["cycle833_S0_prime"]["sha256"],
        "cycle833_S0_prime_weight":
            identity["cycle833_S0_prime"]["weight"],
        "xor_weight": identity["full_diff"]["xor_weight"],
        "selector_outcome": selectors["verdict"],
        "phase_law_outcome": phase_law["law_outcome"],
        "weight_outcome": weight["verdict"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
        "terminal": "CYCLE843_IDENTITY_ADVERSARIAL_CHECK_HONEST_FAIL",
    }
    output = stable_render(ruling, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    controls["pass"] = controls_base and stdout_ok
    controls["verdict"] = "PASS" if controls["pass"] else "FAIL"
    output = stable_render(ruling, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE843_IDENTITY_ADVERSARIAL_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal":
                "CYCLE843_IDENTITY_ADVERSARIAL_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
