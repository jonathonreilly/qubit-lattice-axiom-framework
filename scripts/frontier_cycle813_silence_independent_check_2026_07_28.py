#!/usr/bin/env python3
"""Cycle 813 independent adversarial checker.

The Cycle-813 primary is SHA-pinned text/AST evidence only and is blocked from
import.  The only executable science input is the landed Cycle-719 controller
core.  This checker rebuilds the Boolean evolution, cleanliness predicate,
translation-family census, and conserved-sector search independently.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle813_silence_theorem_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

PRIMARY_MODULE = "frontier_cycle813_silence_theorem_2026_07_28"
EXPECTED_ANCHORS = {
    AUDIT_INPUT_PATHS[0]: {
        "sha256": "2cc32c3bf06d0e93bd594288509e3d6f54cbb50a7eeee023932316ae979e64f2",
        "git_blob": "2106c04a17cdb9e7a2b12efbf5115b9f0b19c99b",
    },
    AUDIT_INPUT_PATHS[1]: {
        "sha256": "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
        "git_blob": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    },
}


class PrimaryBlocklist(importlib.abc.MetaPathFinder):
    """Forbid execution of the attacked primary."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname == PRIMARY_MODULE:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


FIREWALL = PrimaryBlocklist()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
BANK_COUNT = 2
INVARIANT_NAMES = (
    "UNWRITTEN_LINK_VECTOR_ZERO",
    "UNWRITTEN_LINK_OCCUPANCY_ZERO",
    "UNWRITTEN_LINK_PARITY_EVEN",
)
SILENT_REPRESENTATIVES = {
    4: (
        (0, 2, 4, 6),
        (0, 2, 4, 7),
        (0, 2, 4, 8),
        (0, 2, 5, 7),
        (0, 2, 5, 8),
    ),
    5: ((0, 2, 4, 6, 8),),
}
TRANSIENT_CONTROLS = (
    (2, (1, 10), 3, 252),
    (2, (0, 7), 3, 371),
    (3, (0, 2, 5), 2, 444),
    (3, (0, 2, 5), 3, 532),
    (3, (0, 2, 4), 1, 681),
    (3, (0, 2, 4), 2, 1385),
)

CERTIFICATES: dict[str, bool] = {}
LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def certificate(name: str, passed: bool, finding: object) -> None:
    if name in CERTIFICATES:
        raise AssertionError(("duplicate certificate", name))
    CERTIFICATES[name] = bool(passed)
    LINES.append(
        f"{'PASS' if passed else 'FAIL'} {name} :: {compact(finding)}"
    )


def literal_audit_input_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    return (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value)) == AUDIT_INPUT_PATHS
    )


def source_controls() -> dict[str, object]:
    rows = []
    primary_ast_functions = -1
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        parsed = ast.parse(payload.decode("utf-8"), filename=relative)
        if relative == AUDIT_INPUT_PATHS[0]:
            primary_ast_functions = sum(
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                for node in parsed.body
            )
        observed = {
            "path": relative,
            "exists": path.is_file(),
            "worktree_relative": not Path(relative).is_absolute(),
            "sha256": sha256(payload).hexdigest(),
            "git_blob": git_blob(payload),
        }
        observed["anchor_match"] = (
            observed["sha256"] == EXPECTED_ANCHORS[relative]["sha256"]
            and observed["git_blob"] == EXPECTED_ANCHORS[relative]["git_blob"]
        )
        rows.append(observed)

    blocked = False
    block_message = ""
    try:
        importlib.import_module(PRIMARY_MODULE)
    except ImportError as error:
        blocked = True
        block_message = str(error)

    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": literal_audit_input_paths(),
        "rows": rows,
        "primary_AST_top_level_function_count": primary_ast_functions,
        "primary_text_AST_only": True,
        "primary_import_probe_blocked": blocked,
        "primary_import_probe_message": block_message,
        "firewall_hits": tuple(FIREWALL.hits),
        "primary_absent_from_runtime_modules": PRIMARY_MODULE not in sys.modules,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and all(
            row["exists"] and row["worktree_relative"] and row["anchor_match"]
            for row in rows
        )
        and primary_ast_functions > 0
        and blocked
        and tuple(FIREWALL.hits) == (PRIMARY_MODULE,)
        and result["primary_absent_from_runtime_modules"]
    )
    return result


def tuple_to_int(state: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def int_to_tuple(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> index) & 1 for index in range(width))


def compile_gates(gates: tuple[object, ...]) -> tuple[tuple[int, int], ...]:
    """Compile X/CNOT/Toffoli gates without the landed evaluator."""

    expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
    compiled = []
    for gate in gates:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind not in expected_arity or len(wires) != expected_arity[kind]:
            raise AssertionError(("unsupported gate", kind, wires))
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated gate wire", kind, wires))
        compiled.append(
            (
                sum(1 << wire for wire in wires[:-1]),
                1 << wires[-1],
            )
        )
    return tuple(compiled)


def apply_gate(state: int, gate: tuple[int, int]) -> int:
    controls, target = gate
    return state ^ target if state & controls == controls else state


def apply_word(state: int, word: tuple[tuple[int, int], ...]) -> int:
    for gate in word:
        state = apply_gate(state, gate)
    return state


def synchronous_gates(
    program: tuple[object, ...], positions: tuple[int, ...]
) -> tuple[object, ...]:
    """Compose one orbit directly from rotating occupied stations."""

    live = tuple(positions)
    output = []
    for _ in range(len(program)):
        live_set = frozenset(live)
        for station, row in enumerate(program):
            if station in live_set:
                output.extend(K.mapped_macro(row))
        live = tuple((station + 1) % len(program) for station in live)
    return tuple(output)


def rotate(positions: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied for position in occupied
    )


def family_catalog() -> dict[
    int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
]:
    grouped: dict[int, dict[tuple[int, ...], set[tuple[int, ...]]]] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if mask & (1 << station)
        )
        if not separated(positions):
            continue
        representative = (
            min(rotate(positions, shift) for shift in range(RING_STATIONS))
            if positions
            else ()
        )
        grouped.setdefault(len(positions), {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        k: {
            representative: tuple(sorted(configurations))
            for representative, configurations in sorted(rows.items())
        }
        for k, rows in sorted(grouped.items())
    }


def changed_coordinate(
    before: tuple[int, ...], after: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, pair in enumerate(zip(before, after))
        if pair[0] != pair[1]
    )
    if len(before) != len(after) or len(changed) != 1:
        raise AssertionError(("not a coordinate perturbation", len(changed)))
    return changed[0]


def watched_registers() -> tuple[int, ...]:
    return (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )


def reconstruct_watched_basis() -> dict[str, object]:
    banks, links = K.B.chain_genesis(BANK_COUNT)
    packed = K.M.pack_state(banks, links)
    labels: dict[int, tuple[str, int, int]] = {
        K.R3.X.SOURCE_POINTER: ("source", 0, K.R3.X.SOURCE_POINTER)
    }

    for bank_index in range(BANK_COUNT):
        for wire in watched_registers():
            changed_banks = [list(bank) for bank in banks]
            changed_banks[bank_index][wire] ^= 1
            altered = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks), links
            )
            coordinate = changed_coordinate(packed, altered)
            if coordinate in labels:
                raise AssertionError(("duplicate coordinate", coordinate))
            labels[coordinate] = ("bank", bank_index, wire)

    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            altered = K.M.pack_state(
                banks, tuple(tuple(item) for item in changed_links)
            )
            coordinate = changed_coordinate(packed, altered)
            if coordinate in labels:
                raise AssertionError(("duplicate coordinate", coordinate))
            labels[coordinate] = ("link", link_index, wire)

    return {
        "state_width": len(packed),
        "labels": labels,
        "mask": sum(1 << coordinate for coordinate in labels),
        "count": len(labels),
    }


def clean_structural(state: int, width: int) -> bool:
    """Reimplement the landed clean-postimage definition structurally."""

    unpacked = int_to_tuple(state, width)
    banks, links = K.M.unpack_state(unpacked, BANK_COUNT)
    return (
        not unpacked[K.R3.X.SOURCE_POINTER]
        and not any(
            bank[wire]
            for bank in banks
            for wire in watched_registers()
        )
        and not any(bit for link in links for bit in link)
    )


def clean_mask(state: int, watched_mask: int) -> bool:
    return not bool(state & watched_mask)


def build_fixtures() -> dict[int, dict[str, object]]:
    """Build the four event inputs with the independent gate evaluator."""

    banks, links = K.B.chain_genesis(BANK_COUNT)
    state = tuple_to_int(K.M.pack_state(banks, links))
    allocator = compile_gates(tuple(K.M.global_allocator_word(BANK_COUNT)))
    rows = {}
    for event in range(2 * BANK_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(
            int_to_tuple(state, len(K.M.pack_state(banks, links))),
            direction,
        )
        before = tuple_to_int(prepared)
        rows[event] = {
            "event": event,
            "direction": direction,
            "before": before,
        }
        state = apply_word(before, allocator)
    return rows


def silent_keys(
    families: dict[
        int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
    ],
) -> tuple[tuple[int, tuple[int, ...], int], ...]:
    return tuple(
        (k, representative, event)
        for k in (4, 5)
        for representative in families[k]
        for event in range(2 * BANK_COUNT)
    )


def build_evolution_basis(
    program: tuple[object, ...],
    watched: dict[str, object],
    positions_rows: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    words = {}
    target_sets = {}
    for positions in positions_rows:
        compiled = compile_gates(synchronous_gates(program, positions))
        targets = frozenset(target.bit_length() - 1 for _controls, target in compiled)
        words[positions] = compiled
        target_sets[positions] = targets

    distinct_targets = {tuple(sorted(targets)) for targets in target_sets.values()}
    common_targets = frozenset(next(iter(distinct_targets)))
    watched_coordinates = frozenset(int(c) for c in watched["labels"])
    unwritten_watched = watched_coordinates - common_targets
    state_width = int(watched["state_width"])
    globally_unwritten = frozenset(range(state_width)) - common_targets
    unwritten_labels = tuple(
        watched["labels"][coordinate]
        for coordinate in sorted(unwritten_watched)
    )
    return {
        "words": words,
        "target_sets_identical": len(distinct_targets) == 1,
        "targets": common_targets,
        "unwritten_watched": unwritten_watched,
        "unwritten_mask": sum(1 << coordinate for coordinate in unwritten_watched),
        "globally_unwritten": globally_unwritten,
        "unwritten_labels": unwritten_labels,
        "all_unwritten_watched_are_links": all(
            label[0] == "link" for label in unwritten_labels
        ),
        "word_rows": tuple(
            {
                "positions": positions,
                "k": len(positions),
                "gate_count": len(words[positions]),
                "target_count": len(target_sets[positions]),
                "sha256": digest(words[positions]),
            }
            for positions in positions_rows
        ),
    }


def invariant_values(state: int, unwritten_mask: int) -> dict[str, int]:
    vector = state & unwritten_mask
    return {
        INVARIANT_NAMES[0]: vector,
        INVARIANT_NAMES[1]: vector.bit_count(),
        INVARIANT_NAMES[2]: vector.bit_count() & 1,
    }


def invariance_attack(
    keys: tuple[tuple[int, tuple[int, ...], int], ...],
    fixtures: dict[int, dict[str, object]],
    basis: dict[str, object],
) -> dict[str, object]:
    """Probe exact gate-level drift in ordinary and orbit-boundary windows."""

    unwritten = tuple(sorted(basis["unwritten_watched"]))
    targets = tuple(sorted(basis["targets"]))
    mask = int(basis["unwritten_mask"])
    drift_counts = {name: 0 for name in INVARIANT_NAMES}
    first_drifts: dict[str, object] = {}
    gates_checked = 0
    boundary_crossings = 0
    strata = Counter()

    for key_index, (k, positions, event) in enumerate(keys):
        strata[k] += 1
        word = basis["words"][positions]
        word_length = len(word)
        if not word_length:
            raise AssertionError(("empty adversarial word", positions))

        base = int(fixtures[event]["before"])
        selected_unwritten = tuple(
            unwritten[(key_index * 17 + offset * 29) % len(unwritten)]
            for offset in range(1 + key_index % 5)
        )
        selected_targets = tuple(
            targets[(key_index * 11 + offset * 31) % len(targets)]
            for offset in range(1 + event)
        )
        adversarial = base
        for coordinate in selected_unwritten + selected_targets:
            adversarial ^= 1 << coordinate

        windows = (
            (3 + event, 19),
            (word_length - 7 - event, 23),
            (2 * word_length - 5 - key_index % 3, 17),
        )
        for start, length in windows:
            state = adversarial
            for gate_index in range(start):
                state = apply_gate(state, word[gate_index % word_length])
            expected = invariant_values(state, mask)
            crosses = start // word_length != (start + length - 1) // word_length
            boundary_crossings += int(crosses)
            for offset in range(length):
                gate_index = (start + offset) % word_length
                state = apply_gate(state, word[gate_index])
                observed = invariant_values(state, mask)
                gates_checked += 1
                for name in INVARIANT_NAMES:
                    if observed[name] != expected[name]:
                        drift_counts[name] += 1
                        first_drifts.setdefault(
                            name,
                            {
                                "key": (k, positions, event),
                                "window": (start, length),
                                "gate_offset": offset,
                                "expected": expected[name],
                                "observed": observed[name],
                            },
                        )

    return {
        "passes": {name: drift_counts[name] == 0 for name in INVARIANT_NAMES},
        "drift_counts": drift_counts,
        "first_drifts": first_drifts,
        "key_count": len(keys),
        "strata": dict(sorted(strata.items())),
        "windows_per_key": 3,
        "boundary_crossing_windows": boundary_crossings,
        "gates_checked": gates_checked,
        "adversarial_states_have_nonzero_unwritten_vectors": True,
    }


def necessity_attack(
    watched: dict[str, object], basis: dict[str, object]
) -> dict[str, object]:
    width = int(watched["state_width"])
    watched_mask = int(watched["mask"])
    unwritten_mask = int(basis["unwritten_mask"])
    coordinates = tuple(sorted(basis["unwritten_watched"]))
    if len(coordinates) < 7:
        raise AssertionError("insufficient unwritten coordinates")

    cases = {
        INVARIANT_NAMES[0]: (coordinates[0], coordinates[1]),
        INVARIANT_NAMES[1]: (coordinates[2], coordinates[3]),
        INVARIANT_NAMES[2]: (coordinates[4],),
    }
    rows = {}
    for name, flipped in cases.items():
        near_clean = sum(1 << coordinate for coordinate in flipped)
        values = invariant_values(near_clean, unwritten_mask)
        violation = {
            INVARIANT_NAMES[0]: values[INVARIANT_NAMES[0]] != 0,
            INVARIANT_NAMES[1]: values[INVARIANT_NAMES[1]] != 0,
            INVARIANT_NAMES[2]: values[INVARIANT_NAMES[2]] != 0,
        }[name]
        direct_clean = clean_structural(near_clean, width)
        mask_clean = clean_mask(near_clean, watched_mask)
        rows[name] = {
            "flipped_unwritten_coordinates": flipped,
            "unwritten_occupancy": values[INVARIANT_NAMES[1]],
            "unwritten_parity": values[INVARIANT_NAMES[2]],
            "named_condition_violated": violation,
            "all_other_watched_coordinates_zero": not bool(
                near_clean & (watched_mask & ~unwritten_mask)
            ),
            "landed_definition_reimplementation_accepts": direct_clean,
            "independent_mask_predicate_accepts": mask_clean,
            "landed_test_REJECTS": not direct_clean,
            "pass": (
                violation
                and not bool(near_clean & (watched_mask & ~unwritten_mask))
                and not direct_clean
                and direct_clean == mask_clean
            ),
        }

    zero_is_clean = (
        clean_structural(0, width) and clean_mask(0, watched_mask)
    )
    return {
        "passes": {
            name: zero_is_clean and bool(rows[name]["pass"])
            for name in INVARIANT_NAMES
        },
        "zero_configuration_is_clean": zero_is_clean,
        "near_clean_rows": rows,
        "contrapositive_checked_mechanically": True,
    }


def compatibility_recount(
    families: dict[
        int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
    ],
    keys: tuple[tuple[int, tuple[int, ...], int], ...],
    fixtures: dict[int, dict[str, object]],
    watched: dict[str, object],
    basis: dict[str, object],
) -> dict[str, object]:
    watched_mask = int(watched["mask"])
    unwritten_mask = int(basis["unwritten_mask"])
    width = int(watched["state_width"])
    configuration_counts = {
        k: sum(len(configurations) for configurations in rows.values())
        for k, rows in families.items()
    }
    family_counts = {k: len(rows) for k, rows in families.items()}

    silent_rows = []
    for k, positions, event in keys:
        initial = int(fixtures[event]["before"])
        after_t0 = apply_word(initial, basis["words"][positions])
        values = invariant_values(initial, unwritten_mask)
        values_t0 = invariant_values(after_t0, unwritten_mask)
        violated = tuple(
            name for name, value in values.items() if value != 0
        )
        silent_rows.append(
            {
                "key": (k, positions, event),
                "values": values,
                "preserved_at_t0": values == values_t0,
                "outcome": "VIOLATED-FOREVER" if violated else "COMPATIBLE",
                "violated": violated,
            }
        )

    transient_rows = []
    for k, positions, event, moment in TRANSIENT_CONTROLS:
        state = int(fixtures[event]["before"])
        initial_values = invariant_values(state, unwritten_mask)
        word = basis["words"][positions]
        first_clean = None
        t_minus_one_clean = None
        values_preserved = True
        for horizon_t in range(moment + 1):
            state = apply_word(state, word)
            values_preserved &= (
                invariant_values(state, unwritten_mask) == initial_values
            )
            if clean_mask(state, watched_mask) and first_clean is None:
                first_clean = horizon_t
            if horizon_t == moment - 1:
                t_minus_one_clean = clean_mask(state, watched_mask)
        final_clean_mask = clean_mask(state, watched_mask)
        final_clean_structural = clean_structural(state, width)
        final_values = invariant_values(state, unwritten_mask)
        transient_rows.append(
            {
                "key": (k, positions, event),
                "claimed_first_clean_t": moment,
                "recounted_first_clean_t": first_clean,
                "t_minus_1_clean": t_minus_one_clean,
                "t_clean": final_clean_mask,
                "clean_predicates_agree": (
                    final_clean_mask == final_clean_structural
                ),
                "initial_values": initial_values,
                "final_values": final_values,
                "values_preserved": values_preserved,
                "all_three_identity_values": all(
                    value == 0 for value in final_values.values()
                ),
                "pass": (
                    first_clean == moment
                    and t_minus_one_clean is False
                    and final_clean_mask
                    and final_clean_structural
                    and values_preserved
                    and all(value == 0 for value in final_values.values())
                ),
            }
        )

    violated_rows = tuple(
        row for row in silent_rows if row["outcome"] == "VIOLATED-FOREVER"
    )
    compatible_rows = tuple(
        row for row in silent_rows if row["outcome"] == "COMPATIBLE"
    )
    catalog_matches = (
        configuration_counts == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and family_counts == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and {k: tuple(families[k]) for k in (4, 5)}
        == SILENT_REPRESENTATIVES
        and len(keys) == 24
        and Counter(k for k, _positions, _event in keys)
        == Counter({4: 20, 5: 4})
    )
    return {
        "pass": (
            catalog_matches
            and len(violated_rows) == 0
            and len(compatible_rows) == 24
            and all(row["preserved_at_t0"] for row in silent_rows)
            and len(transient_rows) == 6
            and all(row["pass"] for row in transient_rows)
        ),
        "catalog_matches": catalog_matches,
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "silent_key_counts": dict(
            sorted(Counter(row["key"][0] for row in silent_rows).items())
        ),
        "VIOLATED-FOREVER": len(violated_rows),
        "COMPATIBLE": len(compatible_rows),
        "identity_controls_passed": sum(row["pass"] for row in transient_rows),
        "identity_controls_total": len(transient_rows),
        "identity_moments": tuple(
            row["recounted_first_clean_t"] for row in transient_rows
        ),
        "identity_rows": transient_rows,
        "silent_zero_fiber": all(
            row["values"][INVARIANT_NAMES[0]] == 0 for row in silent_rows
        ),
    }


def missed_invariant_hunt(
    keys: tuple[tuple[int, tuple[int, ...], int], ...],
    fixtures: dict[int, dict[str, object]],
    watched: dict[str, object],
    basis: dict[str, object],
) -> dict[str, object]:
    """Exhaust a declared gate-by-gate unwritten-sector invariant class.

    Class L: all integer linear functionals on the full Boolean state basis
    that are invariant under every primitive gate and vanish on every clean
    state.  Gate-by-gate invariance removes every targeted coordinate; clean
    necessity then removes every un-watched coordinate.

    Class Q2: all square-free GF(2) polynomials of degree one or two in the
    common globally untargeted coordinates that vanish on every clean state.
    Its monomial basis is exactly the monomials containing at least one
    cleanliness-watched unwritten coordinate.
    """

    watched_coordinates = frozenset(int(c) for c in watched["labels"])
    globally_unwritten = frozenset(basis["globally_unwritten"])
    necessary_unwritten = frozenset(basis["unwritten_watched"])
    free_unwritten = globally_unwritten - watched_coordinates
    targets = frozenset(basis["targets"])
    state_width = int(watched["state_width"])

    linear_basis = tuple(sorted(necessary_unwritten))
    q2_cross_count = 0
    q2_watched_pair_count = 0
    for _left in necessary_unwritten:
        for _right in free_unwritten:
            q2_cross_count += 1
    ordered_watched = tuple(sorted(necessary_unwritten))
    for left_index, _left in enumerate(ordered_watched):
        for _right in ordered_watched[left_index + 1 :]:
            q2_watched_pair_count += 1
    q2_basis_count = (
        len(linear_basis) + q2_cross_count + q2_watched_pair_count
    )

    silent_vectors = []
    for k, positions, event in keys:
        state = int(fixtures[event]["before"])
        vector = state & int(basis["unwritten_mask"])
        silent_vectors.append(
            {
                "key": (k, positions, event),
                "necessary_unwritten_vector": vector,
            }
        )

    linear_derivation_exact = (
        not (targets & globally_unwritten)
        and necessary_unwritten == globally_unwritten & watched_coordinates
        and len(targets | globally_unwritten) == state_width
        and not (targets & globally_unwritten)
    )
    class_q2_exhausted = (
        q2_basis_count
        == (
            len(necessary_unwritten)
            + len(necessary_unwritten) * len(free_unwritten)
            + len(necessary_unwritten)
            * (len(necessary_unwritten) - 1)
            // 2
        )
        and q2_basis_count > 0
    )
    all_silent_features_zero = all(
        row["necessary_unwritten_vector"] == 0 for row in silent_vectors
    )
    found_ruling_invariant = not all_silent_features_zero
    ruled_keys = tuple(
        row["key"]
        for row in silent_vectors
        if row["necessary_unwritten_vector"] != 0
    )

    return {
        "pass": linear_derivation_exact and class_q2_exhausted,
        "outcome": "FOUND" if found_ruling_invariant else "EXHAUSTED_NO_FIND",
        "found_ruling_invariant": found_ruling_invariant,
        "ruled_silent_keys": ruled_keys,
        "declared_search_class": (
            "L = all gate-by-gate invariant integer linear functionals on "
            "the full Boolean state basis that vanish on the exact clean "
            "subspace; Q2 = all square-free GF(2) polynomials of degree "
            "1 or 2 over common globally untargeted coordinates that vanish "
            "on that clean subspace."
        ),
        "state_width": state_width,
        "gate_target_coordinate_count": len(targets),
        "globally_unwritten_coordinate_count": len(globally_unwritten),
        "cleanliness_watched_coordinate_count": len(watched_coordinates),
        "necessary_unwritten_coordinate_count": len(necessary_unwritten),
        "clean_free_unwritten_coordinate_count": len(free_unwritten),
        "class_L_dimension": len(linear_basis),
        "class_Q2_monomial_basis_count": q2_basis_count,
        "class_Q2_linear_generators": len(linear_basis),
        "class_Q2_watched_free_quadratic_generators": q2_cross_count,
        "class_Q2_watched_watched_quadratic_generators":
            q2_watched_pair_count,
        "silent_feature_vectors_all_zero": all_silent_features_zero,
        "excluded_if_no_find": (
            "No quantity in L or Q2 can rule out any of the 24 silent keys. "
            "More strongly, no function only of the 102-bit necessary "
            "unwritten vector can distinguish a silent initial state from "
            "the clean zero fiber because all 24 vectors equal zero."
        ),
    }


def science_run() -> dict[str, object]:
    program = K.interleaved_program(BANK_COUNT)
    watched = reconstruct_watched_basis()
    families = family_catalog()
    keys = silent_keys(families)
    positions_rows = tuple(
        sorted(
            {positions for _k, positions, _event in keys}
            | {positions for _k, positions, _event, _moment in TRANSIENT_CONTROLS}
        )
    )
    basis = build_evolution_basis(program, watched, positions_rows)
    fixtures = build_fixtures()
    invariance = invariance_attack(keys, fixtures, basis)
    necessity = necessity_attack(watched, basis)
    compatibility = compatibility_recount(
        families, keys, fixtures, watched, basis
    )
    hunt = missed_invariant_hunt(keys, fixtures, watched, basis)
    return {
        "basis_summary": {
            "state_width": watched["state_width"],
            "watched_count": watched["count"],
            "unwritten_watched_count": len(basis["unwritten_watched"]),
            "globally_unwritten_count": len(basis["globally_unwritten"]),
            "target_sets_identical": basis["target_sets_identical"],
            "all_unwritten_watched_are_links":
                basis["all_unwritten_watched_are_links"],
            "word_rows": basis["word_rows"],
        },
        "invariance": invariance,
        "necessity": necessity,
        "compatibility": compatibility,
        "hunt": hunt,
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    first = science_run()
    second = science_run()
    deterministic = first == second and digest(first) == digest(second)

    basis_ok = (
        first["basis_summary"]["watched_count"] == 477
        and first["basis_summary"]["unwritten_watched_count"] == 102
        and first["basis_summary"]["target_sets_identical"]
        and first["basis_summary"]["all_unwritten_watched_are_links"]
    )
    invariance = first["invariance"]
    for name in INVARIANT_NAMES:
        certificate(
            f"INVARIANCE_ATTACK_{name}",
            basis_ok and invariance["passes"][name],
            {
                "quantity": name,
                "drift_count": invariance["drift_counts"][name],
                "first_drift": invariance["first_drifts"].get(name),
                "keys": invariance["key_count"],
                "strata": invariance["strata"],
                "windows_per_key": invariance["windows_per_key"],
                "boundary_crossing_windows":
                    invariance["boundary_crossing_windows"],
                "primitive_gates_checked": invariance["gates_checked"],
            },
        )

    necessity = first["necessity"]
    for name in INVARIANT_NAMES:
        certificate(
            f"NECESSITY_ATTACK_{name}",
            basis_ok and necessity["passes"][name],
            necessity["near_clean_rows"][name],
        )

    compatibility = first["compatibility"]
    certificate(
        "COMPATIBILITY_RECOUNT",
        basis_ok and compatibility["pass"],
        compatibility,
    )

    hunt = first["hunt"]
    certificate(
        "MISSED_INVARIANT_HUNT",
        basis_ok and hunt["pass"],
        hunt,
    )

    elapsed_before_controls = monotonic() - started
    projected_stdout = len("\n".join(LINES).encode("utf-8")) + 24 * 1024
    controls_pass = (
        controls["pass"]
        and deterministic
        and elapsed_before_controls < AUDIT_TIMEOUT_SEC
        and projected_stdout < STDOUT_LIMIT_BYTES
    )
    certificate(
        "CONTROLS_SHA_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT",
        controls_pass,
        {
            "source_controls": controls,
            "deterministic": deterministic,
            "first_sha256": digest(first),
            "second_sha256": digest(second),
            "runtime_seconds_before_terminal": round(elapsed_before_controls, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    primary_survived = (
        all(invariance["passes"].values())
        and all(necessity["passes"].values())
        and compatibility["pass"]
    )
    if hunt["found_ruling_invariant"]:
        overall = "OVERTURNED"
        LINES.append(
            "OVERTURNED FOURTH CONSERVED NECESSARY INVARIANT FOUND :: "
            + compact(hunt["ruled_silent_keys"])
        )
    elif primary_survived and all(CERTIFICATES.values()):
        overall = "CONFIRMED"
    else:
        overall = "REFUTED"

    elapsed = monotonic() - started
    terminal = {
        "terminal": (
            "CYCLE813_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if all(CERTIFICATES.values())
            else "CYCLE813_INDEPENDENT_ADVERSARIAL_CHECK_HONEST_FAIL"
        ),
        "pass": all(CERTIFICATES.values()),
        "overall": overall,
        "invariance_attack": (
            "NO_DRIFT" if all(invariance["passes"].values()) else "DRIFT_FOUND"
        ),
        "necessity_attack": (
            "CONTRAPOSITIVES_REJECTED"
            if all(necessity["passes"].values())
            else "COUNTEREXAMPLE_FOUND"
        ),
        "VIOLATED-FOREVER": compatibility["VIOLATED-FOREVER"],
        "COMPATIBLE": compatibility["COMPATIBLE"],
        "identity_controls": (
            compatibility["identity_controls_passed"],
            compatibility["identity_controls_total"],
        ),
        "missed_invariant_hunt": hunt["outcome"],
        "excluded_search_class": hunt["declared_search_class"],
        "determinism_sha256": digest(first),
        "runtime_seconds": round(elapsed, 6),
    }
    output = "\n".join(LINES) + "\nFINAL " + compact(terminal) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
