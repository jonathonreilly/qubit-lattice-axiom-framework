#!/usr/bin/env python3
"""Cycle 834 independent adversarial check of the k=3 backbone census.

The Cycle-824 and Cycle-834 science primaries are evidence targets only:
they are SHA-pinned, parsed as text/AST, and blocked from import.  The sole
executable repository input is the landed Cycle-719 controller core.  This
checker independently enumerates the geometry and executes every orbit with
its own exact X/CNOT/Toffoli evaluator.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle824_k3_merger_probe_2026_07_28.py",
    "scripts/frontier_cycle834_k3_backbone_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

import numpy as np
from numba import njit, prange


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
REFERENCE_PRIMARY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in REFERENCE_PRIMARY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "b279582fb8deab4b8713c08353a3c6f3f1239135f1d0f666bdc6b35fe3b99223",
    AUDIT_INPUT_PATHS[2]:
        "8ed75c4e6f19fa5e8a9492225aae681ab85017dcfac00f8ab109b7c587aeddaa",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "423992108cbe1f2d8ce57e2f1618e85c14ac0a2c",
    AUDIT_INPUT_PATHS[2]: "89d4506c6df9738bf0458027ab76cc9d2f9710ab",
}
REQUIRED_FUNCTIONS = {
    AUDIT_INPUT_PATHS[0]: {"interleaved_program", "mapped_macro"},
    AUDIT_INPUT_PATHS[1]:
        {"k3_families", "transient_certificate", "cycle_certificate"},
    AUDIT_INPUT_PATHS[2]:
        {"class_census", "transient_cohort_probe", "forecast_surface"},
}


class _BlockedPrimaryFinder(importlib.abc.MetaPathFinder):
    """Fail closed if either attacked primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _BlockedPrimaryFinder()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
EVENT_COUNT = 2 * FIXTURE_BANKS
OPEN_HORIZON = 65536
EXPECTED_STATE_WIDTH = 5815
EXPECTED_WATCHED_COUNT = 477
FUNNEL_LAGS = tuple(range(1, 9))
EXPECTED_CENSUS = {
    (2, 2, 4): (2, 2, 0, 0),
    (2, 3, 5): (6, 2, 2, 2),
    (2, 4, 5): (6, 0, 2, 4),
    (3, 3, 5): (2, 0, 0, 2),
    (3, 4, 4): (2, 0, 0, 2),
}
FORECAST_TARGETS = frozenset({
    (3, (0, 2, 6), 2),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 3),
})

Key = tuple[int, tuple[int, int, int], int]
CompiledWord = tuple[tuple[int, int, int, int], ...]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
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


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    ast_rows = {
        path: {
            "required": tuple(sorted(REQUIRED_FUNCTIONS[path])),
            "present":
                REQUIRED_FUNCTIONS[path] <= top_level_functions(trees[path]),
            "mode": (
                "EXECUTABLE_LANDED_CORE"
                if path == CORE_PATH
                else "TEXT_AST_ONLY_BLOCKLISTED"
            ),
        }
        for path in AUDIT_INPUT_PATHS
    }

    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute()
                and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "source_AST": ast_rows,
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "dependency_policy":
            "Cycle-719 supplies gates/layout only; Cycle-824 and "
            "Cycle-834 are SHA-pinned text/AST evidence targets",
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(row["present"] for row in ast_rows.values())
        and direct_frontier_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, trees


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (position + shift) % RING_STATIONS for position in positions
    ))


def independently_enumerate_families(
) -> dict[tuple[int, int, int], tuple[tuple[int, int, int], ...]]:
    """Enumerate by bit masks, not the primary's combinations route."""

    grouped: dict[
        tuple[int, int, int], set[tuple[int, int, int]]
    ] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if mask & (1 << station)
        )
        if len(positions) != 3:
            continue
        occupied = frozenset(positions)
        if any(
            (station + 1) % RING_STATIONS in occupied
            for station in positions
        ):
            continue
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def separation_profile(
    positions: tuple[int, int, int],
) -> tuple[int, int, int]:
    distances = []
    for left_index in range(3):
        for right_index in range(left_index + 1, 3):
            left = positions[left_index]
            right = positions[right_index]
            clockwise = (right - left) % RING_STATIONS
            distances.append(min(clockwise, RING_STATIONS - clockwise))
    return tuple(sorted(distances))


def compile_word(word: tuple[object, ...]) -> CompiledWord:
    compiled = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind == "X" and len(wires) == 1:
            compiled.append((1, wires[0], -1, wires[0]))
        elif kind == "CNOT" and len(wires) == 2:
            compiled.append((2, wires[0], -1, wires[1]))
        elif kind == "TOF" and len(wires) == 3:
            compiled.append((3, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported gate", kind, wires))
    return tuple(compiled)


def synchronous_compiled_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> CompiledWord:
    live = tuple(positions)
    gates = []
    for _step in range(len(program)):
        live_set = frozenset(live)
        for station, row in enumerate(program):
            if station in live_set:
                gates.extend(K.mapped_macro(row))
        live = tuple(
            (station + 1) % len(program) for station in live
        )
    return compile_word(tuple(gates))


def apply_compiled(
    state: tuple[int, ...],
    compiled: CompiledWord,
) -> tuple[int, ...]:
    """Independent exact evaluator used for all initial compositions."""

    output = [int(bit) for bit in state]
    for kind, first, second, target in compiled:
        if kind == 1:
            output[target] ^= 1
        elif kind == 2:
            output[target] ^= output[first]
        else:
            output[target] ^= output[first] & output[second]
    return tuple(output)


def build_fixtures() -> tuple[tuple[int, ...], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = compile_word(K.M.global_allocator_word(FIXTURE_BANKS))
    rows = []
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append(before)
        state = apply_compiled(before, allocator)
    return tuple(rows)


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, (left_bit, right_bit) in enumerate(zip(left, right))
        if left_bit != right_bit
    )
    if len(left) != len(right) or len(changed) != 1:
        raise AssertionError(("coordinate basis", len(changed)))
    return changed[0]


def watched_indices() -> tuple[int, ...]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(banks0, links0)
    banks, links = K.M.unpack_state(packed, FIXTURE_BANKS)
    indices = {int(K.R3.X.SOURCE_POINTER)}
    registers = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    for bank_index in range(FIXTURE_BANKS):
        for wire in registers:
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(link) for link in links]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(link) for link in changed_links),
            )
            indices.add(one_changed_coordinate(packed, changed))
    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(item) for item in changed_links),
            )
            indices.add(one_changed_coordinate(packed, changed))
    result = tuple(sorted(indices))
    if (
        len(packed) != EXPECTED_STATE_WIDTH
        or len(result) != EXPECTED_WATCHED_COUNT
    ):
        raise AssertionError(("watched basis", len(packed), len(result)))
    return result


def is_clean(
    state: tuple[int, ...] | bytes | np.ndarray,
    watched: tuple[int, ...],
) -> bool:
    return not any(int(state[index]) for index in watched)


@njit(parallel=True, cache=False)
def classify_all_orbits(
    initial_masks: np.ndarray,
    circuits: np.ndarray,
    zero_masks: np.ndarray,
    watched: np.ndarray,
    zobrist: np.ndarray,
    horizon: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Classify all zero keys with an independent bit-sliced evaluator.

    The XOR fingerprint is only a candidate filter.  Every candidate return
    is confirmed by exact comparison of all state coordinates.
    """

    family_count = circuits.shape[0]
    width = initial_masks.shape[1]
    gate_count = circuits.shape[1]
    first_clean = np.full((family_count, 4), -1, dtype=np.int64)
    first_return = np.full((family_count, 4), -1, dtype=np.int64)
    steps = np.zeros(family_count, dtype=np.int64)
    for family_index in prange(family_count):
        state = initial_masks[family_index].copy()
        active = np.int64(zero_masks[family_index])
        hashes = np.zeros(4, dtype=np.uint64)
        for coordinate in range(width):
            lane_bits = np.int64(state[coordinate])
            if lane_bits:
                label = zobrist[coordinate]
                for lane in range(4):
                    if lane_bits & np.int64(1 << lane):
                        hashes[lane] ^= label
        initial_hashes = hashes.copy()

        for horizon_t in range(horizon + 1):
            dirty_mask = np.int64(0)
            for watched_index in range(watched.shape[0]):
                dirty_mask |= np.int64(
                    state[watched[watched_index]]
                )
            clean_mask = active & ((~dirty_mask) & np.int64(15))
            if clean_mask:
                for lane in range(4):
                    lane_mask = np.int64(1 << lane)
                    if clean_mask & lane_mask:
                        first_clean[family_index, lane] = horizon_t
                        active ^= lane_mask

            if horizon_t > 0 and active:
                for lane in range(4):
                    lane_mask = np.int64(1 << lane)
                    if (
                        active & lane_mask
                        and hashes[lane] == initial_hashes[lane]
                    ):
                        exact = True
                        for coordinate in range(width):
                            current = (
                                np.int64(state[coordinate]) >> lane
                            ) & 1
                            initial = (
                                np.int64(
                                    initial_masks[
                                        family_index, coordinate
                                    ]
                                ) >> lane
                            ) & 1
                            if current != initial:
                                exact = False
                                break
                        if exact:
                            first_return[family_index, lane] = horizon_t
                            active ^= lane_mask

            steps[family_index] = horizon_t
            if active == 0 or horizon_t == horizon:
                break

            for gate_index in range(gate_count):
                kind = circuits[family_index, gate_index, 0]
                first = circuits[family_index, gate_index, 1]
                second = circuits[family_index, gate_index, 2]
                target = circuits[family_index, gate_index, 3]
                if kind == 1:
                    toggle = active
                elif kind == 2:
                    toggle = np.int64(state[first]) & active
                else:
                    toggle = (
                        np.int64(state[first])
                        & np.int64(state[second])
                        & active
                    )
                if toggle:
                    state[target] = np.uint8(
                        np.int64(state[target]) ^ toggle
                    )
                    label = zobrist[target]
                    for lane in range(4):
                        if toggle & np.int64(1 << lane):
                            hashes[lane] ^= label
    return first_clean, first_return, steps


@njit(cache=False)
def capture_trajectory(
    initial: np.ndarray,
    circuit: np.ndarray,
    end_t: int,
) -> np.ndarray:
    """Capture a single exact trajectory with the checker's evaluator."""

    width = initial.shape[0]
    trajectory = np.empty((end_t + 1, width), dtype=np.uint8)
    state = initial.copy()
    for horizon_t in range(end_t + 1):
        trajectory[horizon_t, :] = state
        if horizon_t == end_t:
            break
        for gate_index in range(circuit.shape[0]):
            kind = circuit[gate_index, 0]
            first = circuit[gate_index, 1]
            second = circuit[gate_index, 2]
            target = circuit[gate_index, 3]
            if kind == 1:
                state[target] ^= np.uint8(1)
            elif kind == 2:
                state[target] ^= state[first]
            else:
                state[target] ^= state[first] & state[second]
    return trajectory


@njit(cache=False)
def cycle_phase_scan(
    initials: np.ndarray,
    circuits: np.ndarray,
    period: int,
) -> tuple[bool, int, np.ndarray]:
    """Check exact phase equality for four separately evolved circuits."""

    states = initials.copy()
    initial_equal = True
    for lane in range(1, states.shape[0]):
        for coordinate in range(states.shape[1]):
            if states[lane, coordinate] != states[0, coordinate]:
                initial_equal = False
                break
    identical_phase_count = 0
    for _horizon_t in range(period):
        equal = True
        for lane in range(1, states.shape[0]):
            for coordinate in range(states.shape[1]):
                if states[lane, coordinate] != states[0, coordinate]:
                    equal = False
                    break
            if not equal:
                break
        if equal:
            identical_phase_count += 1
        for lane in range(states.shape[0]):
            circuit = circuits[lane]
            state = states[lane]
            for gate_index in range(circuit.shape[0]):
                kind = circuit[gate_index, 0]
                first = circuit[gate_index, 1]
                second = circuit[gate_index, 2]
                target = circuit[gate_index, 3]
                if kind == 1:
                    state[target] ^= np.uint8(1)
                elif kind == 2:
                    state[target] ^= state[first]
                else:
                    state[target] ^= state[first] & state[second]
    closures = np.zeros(states.shape[0], dtype=np.uint8)
    for lane in range(states.shape[0]):
        exact = True
        for coordinate in range(states.shape[1]):
            if states[lane, coordinate] != initials[lane, coordinate]:
                exact = False
                break
        closures[lane] = 1 if exact else 0
    return initial_equal, identical_phase_count, closures


def prepare_model() -> dict[str, object]:
    families = independently_enumerate_families()
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures()
    watched = watched_indices()
    representatives = tuple(families)

    compiled_by_position: dict[tuple[int, int, int], CompiledWord] = {}
    initial_by_position: dict[
        tuple[int, int, int], tuple[tuple[int, ...], ...]
    ] = {}
    all_positions = tuple(sorted({
        positions
        for alternatives in families.values()
        for positions in alternatives
    }))
    for positions in all_positions:
        compiled = synchronous_compiled_word(program, positions)
        compiled_by_position[positions] = compiled
        initial_by_position[positions] = tuple(
            apply_compiled(before, compiled) for before in fixtures
        )

    zero_keys = []
    for representative, alternatives in families.items():
        for event in range(EVENT_COUNT):
            if not any(
                is_clean(initial_by_position[positions][event], watched)
                for positions in alternatives
            ):
                zero_keys.append((3, representative, event))
    zero_keys_tuple = tuple(zero_keys)

    gate_counts = {
        len(compiled_by_position[representative])
        for representative in representatives
    }
    if len(gate_counts) != 1:
        raise AssertionError(("unequal circuit lengths", gate_counts))
    circuits = np.asarray(
        [
            compiled_by_position[representative]
            for representative in representatives
        ],
        dtype=np.int32,
    )
    width = len(fixtures[0])
    initial_masks = np.zeros(
        (len(representatives), width), dtype=np.uint8
    )
    for family_index, representative in enumerate(representatives):
        for event in range(EVENT_COUNT):
            initial_masks[family_index] |= (
                np.asarray(
                    initial_by_position[representative][event],
                    dtype=np.uint8,
                ) << np.uint8(event)
            )
    zero_masks = np.zeros(len(representatives), dtype=np.uint8)
    representative_index = {
        representative: index
        for index, representative in enumerate(representatives)
    }
    for _k, representative, event in zero_keys_tuple:
        zero_masks[representative_index[representative]] |= np.uint8(
            1 << event
        )
    modulus = (1 << 64) - 1
    multiplier = 0x9E3779B97F4A7C15
    zobrist = np.asarray(
        [
            ((coordinate + 1) * multiplier) & modulus
            for coordinate in range(width)
        ],
        dtype=np.uint64,
    )
    return {
        "families": families,
        "representatives": representatives,
        "representative_index": representative_index,
        "fixtures": fixtures,
        "watched": watched,
        "compiled_by_position": compiled_by_position,
        "initial_by_position": initial_by_position,
        "zero_keys": zero_keys_tuple,
        "circuits": circuits,
        "initial_masks": initial_masks,
        "zero_masks": zero_masks,
        "zobrist": zobrist,
        "configuration_count": len(all_positions),
    }


def computed_statuses(
    model: dict[str, object],
) -> tuple[
    dict[Key, str],
    dict[Key, int],
    dict[Key, int],
    tuple[int, ...],
]:
    first_clean, first_return, steps = classify_all_orbits(
        model["initial_masks"],
        model["circuits"],
        model["zero_masks"],
        np.asarray(model["watched"], dtype=np.int32),
        model["zobrist"],
        OPEN_HORIZON,
    )
    statuses: dict[Key, str] = {}
    transients: dict[Key, int] = {}
    cycles: dict[Key, int] = {}
    family_index = model["representative_index"]
    for key in model["zero_keys"]:
        _k, representative, event = key
        row = family_index[representative]
        clean_t = int(first_clean[row, event])
        return_t = int(first_return[row, event])
        if clean_t >= 0:
            statuses[key] = "TRANSIENT"
            transients[key] = clean_t
        elif return_t >= 0:
            statuses[key] = "CYCLE"
            cycles[key] = return_t
        else:
            statuses[key] = "OPEN"
    return statuses, transients, cycles, tuple(int(x) for x in steps)


def census_certificate(
    model: dict[str, object],
    statuses: dict[Key, str],
    transients: dict[Key, int],
    cycles: dict[Key, int],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    primary = trees[AUDIT_INPUT_PATHS[2]]
    claimed_zero = tuple(
        literal_assignment(primary, "LANDED_K3_ZERO_KEYS") or ()
    )
    claimed_transients = dict(
        literal_assignment(primary, "LANDED_K3_TRANSIENTS") or ()
    )
    claimed_cycles = dict(
        literal_assignment(primary, "LANDED_K3_CYCLES") or ()
    )
    claimed_open = set(
        literal_assignment(
            primary, "LANDED_K3_OPEN_THROUGH_65536"
        ) or ()
    )

    grouped: dict[
        tuple[int, int, int], list[Key]
    ] = {}
    for key in model["zero_keys"]:
        grouped.setdefault(separation_profile(key[1]), []).append(key)
    rows = {}
    for profile, keys in sorted(grouped.items()):
        counts = Counter(statuses[key] for key in keys)
        rows[profile] = (
            len(keys),
            counts["TRANSIENT"],
            counts["CYCLE"],
            counts["OPEN"],
        )
    actual_open = {key for key, status in statuses.items() if status == "OPEN"}
    exact_claim_match = (
        set(model["zero_keys"]) == set(claimed_zero)
        and transients == claimed_transients
        and cycles == claimed_cycles
        and actual_open == claimed_open
    )
    passed = (
        len(model["families"]) == 7
        and model["configuration_count"] == 77
        and len(model["zero_keys"]) == 18
        and rows == EXPECTED_CENSUS
        and exact_claim_match
    )
    finding = (
        "224=2/2/0/0, 235=6/2/2/2, 245=6/0/2/4, "
        "335=2/0/0/2, 344=2/0/0/2 as "
        "total/transient/cycle/open"
        if passed
        else "computed cells=" + compact({
            "".join(str(value) for value in profile): row
            for profile, row in rows.items()
        })
    )
    return {
        "name": "THE CENSUS",
        "profiles": tuple({
            "profile": profile,
            "total": row[0],
            "transient": row[1],
            "cycle": row[2],
            "open": row[3],
        } for profile, row in sorted(rows.items())),
        "transient_moments": tuple(sorted(
            transients.items(), key=lambda item: (item[1], item[0])
        )),
        "cycle_periods": tuple(sorted(cycles.items())),
        "open_keys": tuple(sorted(actual_open)),
        "zero_catalog_exact": set(model["zero_keys"]) == set(claimed_zero),
        "all_status_rows_exact": exact_claim_match,
        "finding": finding,
        "pass": passed,
    }


def transient_and_cycle_certificate(
    model: dict[str, object],
    transients: dict[Key, int],
    cycles: dict[Key, int],
) -> dict[str, object]:
    transient_keys = tuple(sorted(
        transients, key=lambda key: (transients[key], key)
    ))
    trajectories: dict[Key, np.ndarray] = {}
    for key in transient_keys:
        _k, representative, event = key
        family_index = model["representative_index"][representative]
        initial = (
            model["initial_masks"][family_index] >> np.uint8(event)
        ) & np.uint8(1)
        trajectories[key] = capture_trajectory(
            initial,
            model["circuits"][family_index],
            transients[key],
        )

    same_time_matches = []
    for left_index, right_index in combinations(
        range(len(transient_keys)), 2
    ):
        left_key = transient_keys[left_index]
        right_key = transient_keys[right_index]
        shared_stop = min(
            transients[left_key], transients[right_key]
        )
        equality = np.all(
            trajectories[left_key][:shared_stop]
            == trajectories[right_key][:shared_stop],
            axis=1,
        )
        times = tuple(
            int(value) for value in np.flatnonzero(equality)
        )
        if times:
            same_time_matches.append({
                "keys": (left_key, right_key),
                "times": times,
            })

    lag_matches = []
    for lag in FUNNEL_LAGS:
        states = tuple(
            trajectories[key][transients[key] - lag]
            for key in transient_keys
        )
        for left_index, right_index in combinations(
            range(len(states)), 2
        ):
            if np.array_equal(
                states[left_index], states[right_index]
            ):
                lag_matches.append({
                    "lag": lag,
                    "keys": (
                        transient_keys[left_index],
                        transient_keys[right_index],
                    ),
                })

    minus_five_states = tuple(
        trajectories[key][transients[key] - 5].tobytes()
        for key in transient_keys
    )
    minus_five_hashes = tuple(
        sha256(state).hexdigest() for state in minus_five_states
    )
    clean_time_rows = []
    watched = np.asarray(model["watched"], dtype=np.int32)
    for key in transient_keys:
        dirty = np.any(trajectories[key][:, watched] != 0, axis=1)
        clean_times = tuple(
            int(value) for value in np.flatnonzero(~dirty)
        )
        clean_time_rows.append((key, clean_times))

    cycle_keys = tuple(sorted(cycles))
    cycle_initials = []
    cycle_circuits = []
    for key in cycle_keys:
        _k, representative, event = key
        family_index = model["representative_index"][representative]
        cycle_initials.append(
            (
                model["initial_masks"][family_index]
                >> np.uint8(event)
            ) & np.uint8(1)
        )
        cycle_circuits.append(model["circuits"][family_index])
    periods = tuple(cycles[key] for key in cycle_keys)
    if len(cycle_keys) == 4 and len(set(periods)) == 1:
        cycle_period = periods[0]
        initial_equal, identical_count, closures = cycle_phase_scan(
            np.asarray(cycle_initials, dtype=np.uint8),
            np.asarray(cycle_circuits, dtype=np.int32),
            cycle_period,
        )
        exact_closures = tuple(bool(value) for value in closures)
    else:
        cycle_period = -1
        initial_equal = False
        identical_count = -1
        exact_closures = ()

    transient_pass = (
        len(transient_keys) == 4
        and tuple(transients[key] for key in transient_keys)
        == (444, 532, 681, 1385)
        and not same_time_matches
        and not lag_matches
        and len(set(minus_five_states)) == 4
        and all(
            clean_times == (transients[key],)
            for key, clean_times in clean_time_rows
        )
    )
    cycle_pass = (
        len(cycle_keys) == 4
        and periods == (5952, 5952, 5952, 5952)
        and initial_equal
        and identical_count == 5952
        and exact_closures == (True, True, True, True)
    )
    passed = transient_pass and cycle_pass
    if passed:
        finding = (
            "distinct moments; no shared-time matches; no lag-1..8 "
            "matches; four distinct moment-5 states; the 5952 cycle "
            "quadruple is identical-in-phase"
        )
    else:
        finding = compact({
            "moments": tuple(
                transients[key] for key in transient_keys
            ),
            "shared_time_matches": same_time_matches,
            "lag_matches": lag_matches,
            "moment_5_distinct": len(set(minus_five_states)),
            "cycle_periods": periods,
            "cycle_identical_phase_count": identical_count,
        })
    return {
        "name": "THE NO-SYNC CLAIM",
        "transient_keys": transient_keys,
        "moments": tuple(transients[key] for key in transient_keys),
        "shared_time_matches": tuple(same_time_matches),
        "lag_1_through_8_pair_matches": tuple(lag_matches),
        "moment_minus_5_sha256_labels": minus_five_hashes,
        "moment_minus_5_exact_distinct_count":
            len(set(minus_five_states)),
        "clean_time_rows": tuple(clean_time_rows),
        "cycle_keys": cycle_keys,
        "cycle_periods": periods,
        "cycle_initial_states_exactly_equal": initial_equal,
        "cycle_identical_in_phase_count": identical_count,
        "cycle_exact_closures": exact_closures,
        "finding": finding,
        "pass": passed,
    }


def backbone_certificate(
    zero_keys: tuple[Key, ...],
    statuses: dict[Key, str],
) -> dict[str, object]:
    resolved = {
        key for key in zero_keys if statuses[key] != "OPEN"
    }
    candidate = {
        key
        for key in zero_keys
        if min(separation_profile(key[1])) == 2
    }
    candidate_open = {
        key for key in candidate if statuses[key] == "OPEN"
    }
    grouped = {}
    for key in zero_keys:
        grouped.setdefault(separation_profile(key[1]), set()).add(key)
    profiles = tuple(sorted(grouped))
    candidate_profiles = frozenset(
        profile for profile in profiles if min(profile) == 2
    )

    complete_profile_unions = []
    for subset_size in range(1, len(profiles) + 1):
        for subset in combinations(profiles, subset_size):
            union = set().union(*(grouped[profile] for profile in subset))
            if resolved <= union:
                complete_profile_unions.append({
                    "profiles": subset,
                    "total": len(union),
                    "resolved": len(resolved & union),
                    "open": sum(
                        statuses[key] == "OPEN" for key in union
                    ),
                })
    minimum_open = min(
        row["open"] for row in complete_profile_unions
    )
    optimal = tuple(
        row for row in complete_profile_unions
        if row["open"] == minimum_open
    )
    alternative_better = tuple(
        row for row in complete_profile_unions
        if row["open"] < len(candidate_open)
    )
    passed = (
        len(candidate) == 14
        and len(resolved) == 8
        and resolved <= candidate
        and len(candidate_open) == 6
        and minimum_open == 6
        and len(optimal) == 1
        and frozenset(optimal[0]["profiles"]) == candidate_profiles
        and not alternative_better
    )
    finding = (
        "min-sep-2 contains all 8 resolutions and exactly 6 open; "
        "it is the unique minimum-open union of whole separation "
        "profiles covering every resolution"
        if passed
        else compact({
            "candidate_total": len(candidate),
            "candidate_resolved": len(resolved & candidate),
            "candidate_open": len(candidate_open),
            "minimum_open_cover": minimum_open,
            "optimal": optimal,
        })
    )
    return {
        "name": "THE BACKBONE CLASS",
        "predicate": "minimum pairwise cyclic separation equals 2",
        "candidate_keys": tuple(sorted(candidate)),
        "total": len(candidate),
        "resolved": len(resolved & candidate),
        "open": len(candidate_open),
        "candidate_profiles": tuple(sorted(candidate_profiles)),
        "complete_profile_union_audit":
            tuple(complete_profile_unions),
        "minimum_open_full_resolution_cover": minimum_open,
        "unique_optimum": len(optimal) == 1,
        "alternative_better": alternative_better,
        "finding": finding,
        "pass": passed,
    }


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None


def literal_dict_fields(function: ast.FunctionDef) -> dict[str, object]:
    fields = {}
    for node in ast.walk(function):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(node.keys, node.values):
            if (
                isinstance(key_node, ast.Constant)
                and isinstance(key_node.value, str)
            ):
                try:
                    fields[key_node.value] = ast.literal_eval(value_node)
                except (TypeError, ValueError):
                    pass
    return fields


def forecast_certificate(
    model: dict[str, object],
    statuses: dict[Key, str],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    primary = trees[AUDIT_INPUT_PATHS[2]]
    forecast_function = function_node(primary, "forecast_surface")
    fields = (
        literal_dict_fields(forecast_function)
        if forecast_function is not None
        else {}
    )
    primary_open = set(
        literal_assignment(
            primary, "LANDED_K3_OPEN_THROUGH_65536"
        ) or ()
    )
    actual_open = {
        key for key, status in statuses.items() if status == "OPEN"
    }
    per_event = {
        event: tuple(sorted(
            key for key in FORECAST_TARGETS if key[2] == event
        ))
        for event in (2, 3)
    }
    bookkeeping = (
        fields.get("status")
        == "PRE_REGISTERED_UNTESTED_CONDITIONAL_FORECAST"
        and fields.get("derivation_scope")
        == "conditional extension of the k=2 per-event cohort pattern"
        and fields.get("not_observed_data") is True
        and fields.get("broad_k3_transient_law_already_supported")
        is False
    )
    targets_lawful = (
        FORECAST_TARGETS <= actual_open
        and FORECAST_TARGETS <= primary_open
        and all(
            min(separation_profile(key[1])) == 2
            for key in FORECAST_TARGETS
        )
        and set(per_event) == {2, 3}
        and all(len(keys) == 3 for keys in per_event.values())
    )
    passed = bookkeeping and targets_lawful
    finding = (
        "the pre-registered untested conditional forecast names existing "
        "open min-sep-2 keys: event-2 and event-3 trios at "
        "(0,2,6/7/8)"
        if passed
        else compact({
            "bookkeeping": bookkeeping,
            "targets_missing_computed_open":
                tuple(sorted(FORECAST_TARGETS - actual_open)),
            "targets_missing_primary_open":
                tuple(sorted(FORECAST_TARGETS - primary_open)),
            "per_event": per_event,
        })
    )
    return {
        "name": "THE FORECAST BOOKKEEPING",
        "source_status": fields.get("status"),
        "source_derivation_scope": fields.get("derivation_scope"),
        "source_not_observed_data": fields.get("not_observed_data"),
        "targets": tuple(sorted(FORECAST_TARGETS)),
        "per_event": per_event,
        "all_targets_computed_open": FORECAST_TARGETS <= actual_open,
        "all_targets_candidate_backbone": all(
            min(separation_profile(key[1])) == 2
            for key in FORECAST_TARGETS
        ),
        "finding": finding,
        "pass": passed,
    }


def science_probe(
    model: dict[str, object],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    statuses, transients, cycles, steps = computed_statuses(model)
    census = census_certificate(
        model, statuses, transients, cycles, trees
    )
    no_sync = transient_and_cycle_certificate(
        model, transients, cycles
    )
    backbone = backbone_certificate(model["zero_keys"], statuses)
    forecast = forecast_certificate(model, statuses, trees)
    return {
        "THE_CENSUS": census,
        "THE_NO_SYNC_CLAIM": no_sync,
        "THE_BACKBONE_CLASS": backbone,
        "THE_FORECAST_BOOKKEEPING": forecast,
        "classification_steps_by_family": tuple(zip(
            model["representatives"], steps
        )),
        "pass": all((
            census["pass"],
            no_sync["pass"],
            backbone["pass"],
            forecast["pass"],
        )),
    }


def render_output(
    science: dict[str, object],
    controls: dict[str, object],
    report: dict[str, object],
) -> str:
    named = (
        science["THE_CENSUS"],
        science["THE_NO_SYNC_CLAIM"],
        science["THE_BACKBONE_CLASS"],
        science["THE_FORECAST_BOOKKEEPING"],
    )
    lines = ["CYCLE834_BACKBONE_INDEPENDENT_CHECK"]
    for certificate in named:
        label = "PASS" if certificate["pass"] else "FAIL"
        lines.append(
            f"{label} {certificate['name']} :: "
            f"{certificate['finding']}"
        )
    controls_label = "PASS" if controls["pass"] else "FAIL"
    lines.append(
        f"{controls_label} CONTROLS :: {controls['finding']}"
    )
    for name in (
        "THE_CENSUS",
        "THE_NO_SYNC_CLAIM",
        "THE_BACKBONE_CLASS",
        "THE_FORECAST_BOOKKEEPING",
    ):
        lines.append(f"CERTIFICATE_{name}={compact(science[name])}")
    lines.append("CERTIFICATE_CONTROLS=" + compact(controls))
    lines.append("REPORT=" + compact(report))
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    sources, trees = source_controls()
    model = prepare_model()
    primary = science_probe(model, trees)
    replay = science_probe(model, trees)
    deterministic = primary == replay
    elapsed = monotonic() - started

    controls_base = (
        sources["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not FIREWALL.hits
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
    )
    controls = {
        **sources,
        "determinism_scope":
            "all 18 horizon-65536 classifications, exact transient "
            "cross-key scans, 5952-cycle phase scan, exhaustive "
            "separation-profile cover audit, and forecast bookkeeping",
        "primary_science_sha256": digest(primary),
        "replay_science_sha256": digest(replay),
        "deterministic_exact_certificate_equality": deterministic,
        "classification_engine":
            "independent native bit-sliced X/CNOT/Toffoli evaluator; "
            "fingerprints filter candidates only and every return is "
            "confirmed by exact full-state equality",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "finding": "",
        "pass": False,
    }
    report = {
        "cycle": 834,
        "checker":
            "frontier_cycle834_backbone_independent_check_2026_07_28",
        "primary_survives": primary["pass"],
        "primary_verdict": (
            "PRIMARY_SURVIVES_INDEPENDENT_CHECK"
            if primary["pass"]
            else "PRIMARY_REFUTED"
        ),
        "checks": {},
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
        "terminal": "CYCLE834_BACKBONE_INDEPENDENT_HONEST_FAIL",
    }
    output = ""
    for _iteration in range(8):
        controls["pass"] = (
            controls_base
            and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        controls["finding"] = (
            "SHA-256/git blobs pinned; Cycle-824/834 primaries "
            "text/AST-only and blocklisted; exact deterministic replay; "
            "literal AUDIT_INPUT_PATHS exist worktree-relative; "
            f"runtime {controls['runtime_seconds']} < "
            f"{AUDIT_TIMEOUT_SEC}s; stdout "
            f"{controls['stdout_bytes']} < {STDOUT_LIMIT_BYTES} bytes"
        )
        report["checks"] = {
            "THE CENSUS": primary["THE_CENSUS"]["pass"],
            "THE NO-SYNC CLAIM":
                primary["THE_NO_SYNC_CLAIM"]["pass"],
            "THE BACKBONE CLASS":
                primary["THE_BACKBONE_CLASS"]["pass"],
            "THE FORECAST BOOKKEEPING":
                primary["THE_FORECAST_BOOKKEEPING"]["pass"],
            "CONTROLS": controls["pass"],
        }
        report["pass"] = all(report["checks"].values())
        report["terminal"] = (
            "CYCLE834_BACKBONE_INDEPENDENT_EXACT_PASS"
            if report["pass"]
            else (
                "CYCLE834_PRIMARY_REFUTED"
                if controls["pass"] and not primary["pass"]
                else "CYCLE834_BACKBONE_INDEPENDENT_HONEST_FAIL"
            )
        )
        output = render_output(primary, controls, report)
        stdout_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = stdout_bytes
        report["stdout_bytes"] = stdout_bytes

    output = render_output(primary, controls, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE834_BACKBONE_INDEPENDENT_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal": "CYCLE834_BACKBONE_INDEPENDENT_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
