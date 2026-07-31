#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-858 reduction claim.

The Cycle-858 primary is source evidence only: this checker SHA-pins and
parses it, but a meta-path firewall forbids importing it.  Executable science
comes only from the landed Cycle-719 controller core.  All census, orbit,
rule-support, profile, conjugacy, horizon, and bit-accounting calculations are
rebuilt here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle858_reduction_tournament_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import comb, factorial, log2
from pathlib import Path
import random
import sys
from time import monotonic
from typing import Iterable

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(30_000)


ROOT = Path(__file__).resolve().parents[1]
CORE_PATH, PRIMARY_PATH = AUDIT_INPUT_PATHS
PRIMARY_MODULE = Path(PRIMARY_PATH).stem
EXPECTED_SHA256 = {
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_PATH: "36ffd41228683eba9ae6084fb5d191f4264838d0a2552c3766cb27210b5e3773",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_PATH: "cbc24805c26d59a4a6d5382a0ff1e2936102d5fe",
}
RING_STATIONS = 11
FIXTURE_BANKS = 2
STRATA = (2, 3, 4, 5)
PERIOD_LIMIT = 50_000
EXPECTED_MERGES = (
    (
        (3, (0, 2, 5), 1),
        (3, (0, 2, 6), 1),
        (3, (0, 2, 7), 1),
        (3, (0, 2, 8), 1),
    ),
    (
        (4, (0, 2, 4, 7), 1),
        (4, (0, 2, 4, 8), 1),
    ),
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] == PRIMARY_MODULE:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, ...], int]
State = tuple[int, ...]


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    primary_tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    required = {
        "derive_rule_automorphisms",
        "dynamical_equivalence_certificate",
        "compositional_certificate",
        "verdict_certificate",
    }
    names = {
        node.name for node in primary_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    rows = tuple({
        "path": path,
        "exists_worktree_relative": not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "AST_valid": True,
        "access": "EXECUTABLE_LANDED_CORE" if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY",
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "source_rows": rows,
        "primary_required_AST_markers_present": required <= names,
        "BLOCKLIST": (PRIMARY_MODULE,),
        "blocked_primary_loaded": PRIMARY_MODULE in sys.modules,
        "firewall_hits": tuple(FIREWALL.hits),
    }
    result["pass"] = (
        len(rows) <= 6
        and all(
            row["exists_worktree_relative"]
            and row["sha256_exact"]
            and row["git_blob_exact"]
            for row in rows
        )
        and result["primary_required_AST_markers_present"]
        and not result["blocked_primary_loaded"]
        and not result["firewall_hits"]
    )
    return result


def independent_positions(count: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        row for row in combinations(range(RING_STATIONS), count)
        if all((station + 1) % RING_STATIONS not in row for station in row)
    )


def rotate(row: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((station + shift) % RING_STATIONS for station in row))


def representatives() -> tuple[tuple[Key, ...], dict[str, object]]:
    keys: list[Key] = []
    rows = []
    partition_exact = True
    for count in STRATA:
        configs = independent_positions(count)
        reps = tuple(sorted({min(rotate(row, s) for s in range(11)) for row in configs}))
        orbits = tuple({rotate(rep, s) for s in range(11)} for rep in reps)
        partition_exact &= (
            set().union(*orbits) == set(configs)
            and sum(map(len, orbits)) == len(configs)
            and all(len(orbit) == 11 for orbit in orbits)
        )
        for event in range(4):
            keys.extend((count, rep, event) for rep in reps)
        closed = RING_STATIONS * comb(RING_STATIONS - count - 1, count - 1) // count
        rows.append({
            "k": count,
            "direct_configurations": len(configs),
            "closed_form_configurations": closed,
            "C11_orbits_all_events": 4 * len(reps),
            "starting_setups": 4 * len(configs),
        })
    result = {
        "strata": tuple(rows),
        "starting_setups": sum(row["starting_setups"] for row in rows),
        "C11_representatives": len(keys),
        "free_action_and_exact_partition": partition_exact,
        "representatives_sha256": digest(tuple(keys)),
    }
    result["pass"] = (
        tuple(row["direct_configurations"] for row in rows) == (44, 77, 55, 11)
        and tuple(row["C11_orbits_all_events"] for row in rows) == (16, 28, 20, 4)
        and result["starting_setups"] == 748
        and len(keys) == 68
        and partition_exact
    )
    return tuple(keys), result


def synchronous_word(program: tuple[object, ...], positions0: tuple[int, ...]) -> tuple[object, ...]:
    positions = positions0
    output = []
    for _ in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                output.extend(K.mapped_macro(row))
        positions = tuple((position + 1) % len(program) for position in positions)
    return tuple(output)


def build_context(keys: tuple[Key, ...]) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    fixtures = {}
    fixture_failures = 0
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        fixture_failures += after != K.A.apply_semantic(before, allocator)
        fixture_failures += rail_a != (1,) + (0,) * 10 or any(rail_b) or len(trace) != 11
        fixtures[event] = before
        state = after
    position_rows = tuple(sorted({key[1] for key in keys}))
    words = {row: synchronous_word(program, row) for row in position_rows}
    initials = {}
    construction_failures = 0
    for key in keys:
        count, positions, event = key
        initial, rail_a, rail_b, trace = K.run_orbit(
            fixtures[event], program, token_positions=positions
        )
        construction_failures += initial != K.A.apply_semantic(fixtures[event], words[positions])
        construction_failures += rail_a != tuple(int(i in positions) for i in range(11))
        construction_failures += any(rail_b) or len(trace) != 11 or count != len(positions)
        initials[key] = initial
    result = {
        "program": program,
        "fixtures": fixtures,
        "words": words,
        "initials": initials,
        "summary": {
            "program_stations": len(program),
            "state_width": len(state),
            "fixture_failures": fixture_failures,
            "construction_failures": construction_failures,
            "word_table_sha256": digest(tuple(
                (row, K.gate_digest(words[row])) for row in position_rows
            )),
            "initial_state_sha256": digest(tuple(
                (key, sha256(bytes(initials[key])).hexdigest()) for key in keys
            )),
        },
    }
    result["summary"]["pass"] = (
        len(program) == 11 and len(state) == 5815
        and fixture_failures == construction_failures == 0
    )
    return result


def contiguous_ranges(wires: Iterable[int]) -> tuple[tuple[int, int], ...]:
    values = tuple(sorted(wires))
    if not values:
        return ()
    rows = []
    start = prior = values[0]
    for wire in values[1:]:
        if wire != prior + 1:
            rows.append((start, prior))
            start = wire
        prior = wire
    rows.append((start, prior))
    return tuple(rows)


def permute_state(state: State, swaps: tuple[tuple[int, int], ...]) -> State:
    output = list(state)
    for left, right in swaps:
        output[left], output[right] = output[right], output[left]
    return tuple(output)


def boundary_commutes(state: State, word: tuple[object, ...], swaps: tuple[tuple[int, int], ...]) -> bool:
    left = permute_state(K.A.apply_semantic(state, word), swaps)
    right = K.A.apply_semantic(permute_state(state, swaps), word)
    return left == right


def automorphism_autopsy(context: dict[str, object]) -> tuple[dict[str, object], tuple[int, ...], tuple[int, ...]]:
    program_generators = K.program_word(context["program"])
    width = context["summary"]["state_width"]
    signatures: list[list[tuple[int, str, int, int]]] = [[] for _ in range(width)]
    read_wires = set()
    write_wires = set()
    for ordinal, gate in enumerate(program_generators):
        wires = tuple(map(int, gate.wires))
        read_wires.update(wires)
        write_wires.add(wires[-1])
        for role, wire in enumerate(wires):
            signatures[wire].append((ordinal, gate.kind, role, len(wires)))
    cells: dict[tuple[tuple[int, str, int, int], ...], list[int]] = {}
    for wire, signature in enumerate(signatures):
        cells.setdefault(tuple(signature), []).append(wire)
    active = tuple(wire for wire, signature in enumerate(signatures) if signature)
    inactive = tuple(wire for wire, signature in enumerate(signatures) if not signature)

    boundary_operand_wires = {
        int(wire)
        for word in context["words"].values()
        for gate in word for wire in gate.wires
    }
    boundary_write_wires = {
        int(gate.wires[-1])
        for word in context["words"].values() for gate in word
    }
    group_swaps = (
        ((inactive[0], inactive[1]),),
        ((inactive[0], inactive[-1]),),
        ((inactive[1], inactive[len(inactive) // 2]), (inactive[2], inactive[-2])),
    )
    sample_words = tuple(context["words"][row] for row in sorted(context["words"])[:4])
    rng = random.Random(8585270)
    sample_states = (
        (0,) * width,
        (1,) * width,
        tuple(rng.getrandbits(1) for _ in range(width)),
    )
    positive_rows = tuple({
        "swaps": swaps,
        "ordered_generator_signatures_preserved": all(
            not signatures[left] and not signatures[right] for left, right in swaps
        ),
        "sampled_boundary_commutation_exact": all(
            boundary_commutes(state, word, swaps)
            for state in sample_states for word in sample_words
        ),
    } for swaps in group_swaps)

    kind_targets = {}
    for gate in program_generators:
        kind_targets.setdefault(gate.kind, int(gate.wires[-1]))
    negative_rows = []
    all_words = tuple(context["words"][row] for row in sorted(context["words"]))
    for offset, (kind, active_wire) in enumerate(sorted(kind_targets.items())):
        dead_wire = inactive[(offset * (len(inactive) - 1)) // max(1, len(kind_targets) - 1)]
        swaps = ((active_wire, dead_wire),)
        witness = None
        hostile_states = list(sample_states)
        hostile_rng = random.Random(8589000 + offset)
        hostile_states.extend(
            tuple(hostile_rng.getrandbits(1) for _ in range(width)) for _ in range(8)
        )
        for word_index, word in enumerate(all_words):
            for state_index, state in enumerate(hostile_states):
                left = permute_state(K.A.apply_semantic(state, word), swaps)
                right = K.A.apply_semantic(permute_state(state, swaps), word)
                if left != right:
                    differences = tuple(i for i, (a, b) in enumerate(zip(left, right)) if a != b)
                    witness = {
                        "word_index": word_index,
                        "state_index": state_index,
                        "difference_count": len(differences),
                        "first_difference_wires": differences[:12],
                    }
                    break
            if witness is not None:
                break
        negative_rows.append({
            "attempted_swap": swaps[0],
            "active_gate_kind_control": kind,
            "incidence_signature_preserved": signatures[active_wire] == signatures[dead_wire],
            "boundary_commutation_failed_as_required": witness is not None,
            "witness": witness,
        })

    order_decimal = str(factorial(len(inactive)))
    cell_sizes = tuple(sorted(map(len, cells.values())))
    result = {
        "finding": (
            "The honest declared group is exactly free permutation of 5270 "
            "never-operand wires.  It fixes all 545 active wires; sampled dead-wire "
            "permutations commute and active/dead swaps fail as negative controls."
        ),
        "declared_action_exact": (
            "identity on every generator-active wire; arbitrary free permutation "
            "of the exact never-operand wire set listed by inactive_wire_ranges"
        ),
        "disclosure": "free permutation of never-active wires; no additional active-wire permutations occur under the declared ordered-generator rule",
        "state_width": width,
        "ordered_core_generators": len(program_generators),
        "active_wire_count": len(active),
        "inactive_wire_count": len(inactive),
        "active_wire_ranges": contiguous_ranges(active),
        "inactive_wire_ranges": contiguous_ranges(inactive),
        "inactive_wires_sha256": digest(inactive),
        "read_wire_count": len(read_wires),
        "write_wire_count": len(write_wires),
        "boundary_operand_support_exactly_active": boundary_operand_wires == set(active),
        "boundary_write_support_subset_active": boundary_write_wires <= set(active),
        "inactive_never_read": not (set(inactive) & boundary_operand_wires),
        "inactive_never_written": not (set(inactive) & boundary_write_wires),
        "support_proof_scope": "all states, hence every boundary in the full reachable census",
        "signature_cell_size_census": dict(sorted(Counter(cell_sizes).items())),
        "group_structure": f"S_{len(inactive)}",
        "group_order_formula": f"{len(inactive)}!",
        "group_order_digits": len(order_decimal),
        "group_order_sha256": sha256(order_decimal.encode()).hexdigest(),
        "sampled_in_group_permutations": positive_rows,
        "active_dead_negative_controls": tuple(negative_rows),
    }
    result["pass"] = (
        len(program_generators) == 3106
        and len(active) == 545 and len(inactive) == 5270
        and cell_sizes == (1,) * 545 + (5270,)
        and result["boundary_operand_support_exactly_active"]
        and result["boundary_write_support_subset_active"]
        and result["inactive_never_read"] and result["inactive_never_written"]
        and all(row["ordered_generator_signatures_preserved"] and row["sampled_boundary_commutation_exact"] for row in positive_rows)
        and all(not row["incidence_signature_preserved"] and row["boundary_commutation_failed_as_required"] for row in negative_rows)
    )
    return result, active, inactive


def residual_wires() -> tuple[int, ...]:
    bank_wires = (
        K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
        *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK,
    )
    wires = [int(K.R3.X.SOURCE_POINTER)]
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        wires.extend(int(base + wire) for wire in bank_wires)
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        wires.extend(int(base + wire) for wire in range(K.B.LINK_WIDTH))
    return tuple(wires)


def strict_records(weights: Iterable[int]) -> tuple[tuple[int, int], ...]:
    output = []
    best = None
    for moment, weight in enumerate(weights):
        if best is None or weight < best:
            output.append((moment, int(weight)))
            best = weight
    return tuple(output)


def invariant_profiles(
    keys: tuple[Key, ...], context: dict[str, object],
    active: tuple[int, ...], inactive: tuple[int, ...],
) -> tuple[dict[str, object], tuple[tuple[Key, ...], ...]]:
    watched = residual_wires()
    rows = []
    states_by_key = {}
    profile_groups: dict[tuple[object, ...], list[Key]] = {}
    for key in keys:
        state = context["initials"][key]
        word = context["words"][key[1]]
        states = [state]
        for _ in range(2):
            state = K.A.apply_semantic(state, word)
            states.append(state)
        states_by_key[key] = tuple(states)
        e1 = tuple(sum(row[wire] for wire in watched) for row in states)
        e2 = tuple(sum(row) for row in states)
        records_e1 = strict_records(e1)
        records_e2 = strict_records(e2)
        profile_signature = (0, e1, e2, records_e1, records_e2)
        profile_groups.setdefault(profile_signature, []).append(key)
        rows.append({
            "key": key,
            "transient_length": 0,
            "transient_basis": "boundary word is a composition of reversible X/CNOT/TOF generators",
            "cycle_period": "EXACT_IN_FULL_CYCLE_ROW_IF_LEVEL_II_SURVIVOR; OTHERWISE_NOT_NEEDED_FOR_REFUTATION",
            "funnel_weight_sequence": {
                "boundary_moments": (0, 1, 2),
                "E1": e1,
                "E2": e2,
            },
            "record_moments_both_readings": {"E1": records_e1, "E2": records_e2},
            "prefix_state_stream_sha256": digest(tuple(sha256(bytes(row)).hexdigest() for row in states)),
        })

    exact_groups = []
    profile_equal_pairs = 0
    rejected_profile_equal_pairs = 0
    for group in profile_groups.values():
        profile_equal_pairs += comb(len(group), 2)
        orbit_groups: dict[tuple[object, ...], list[Key]] = {}
        for key in group:
            orbit_signature = tuple(
                (bytes(state[wire] for wire in active), sum(state[wire] for wire in inactive))
                for state in states_by_key[key]
            )
            orbit_groups.setdefault(orbit_signature, []).append(key)
        survivors = sum(comb(len(subgroup), 2) for subgroup in orbit_groups.values())
        rejected_profile_equal_pairs += comb(len(group), 2) - survivors
        exact_groups.extend(tuple(subgroup) for subgroup in orbit_groups.values() if len(subgroup) > 1)
    equal_groups = tuple(sorted(
        exact_groups,
        key=lambda group: group[0],
    ))
    result = {
        "E1_reading": "source pointer, declared bank cleanliness wires, and every inter-bank link bit",
        "E2_reading": "full 5815-bit Hamming weight",
        "profile_rows": tuple(rows),
        "profile_row_count": len(rows),
        "profile_equal_pair_count": profile_equal_pairs,
        "profile_equal_pairs_rejected_by_exact_rule_orbit_prefix": rejected_profile_equal_pairs,
        "exact_prefix_survivor_groups": equal_groups,
        "full_reachable_prefix_boundary_census_size": 3 * len(keys),
        "inactive_never_read_or_written_on_census": True,
        "inactive_census_basis": "the exact gate-support proof excludes every inactive wire on every possible state, stronger than a trajectory sample",
        "inactive_initial_projection_sha256": digest(tuple(
            (key, digest(tuple(context["initials"][key][wire] for wire in inactive)))
            for key in keys
        )),
        "period_disclosure": (
            "The primary did not compute periods for 62 non-survivors.  This checker does not "
            "mislabel deferred periods as exact; periods are computed exactly for every merge "
            "candidate, while exact t<=2 obstructions already decide all other pairs."
        ),
    }
    result["pass"] = (
        len(rows) == 68 and len(watched) == 477
        and equal_groups == EXPECTED_MERGES
        and profile_equal_pairs == rejected_profile_equal_pairs + 7
    )
    return result, equal_groups


def group_invariant_witness_states(
    width: int, active: tuple[int, ...], inactive: tuple[int, ...]
) -> tuple[State, ...]:
    rows = [(0,) * width, (1,) * width]
    rng = random.Random(8580064)
    for dead_value in (0, 1):
        for _ in range(8):
            state = [dead_value] * width
            for wire in active:
                state[wire] = rng.getrandbits(1)
            rows.append(tuple(state))
    return tuple(rows)


def merge_autopsy(
    keys: tuple[Key, ...], context: dict[str, object],
    active: tuple[int, ...], inactive: tuple[int, ...],
    candidate_groups: tuple[tuple[Key, ...], ...],
) -> dict[str, object]:
    cycle_rows = []
    pair_rows = []
    width = context["summary"]["state_width"]
    witness_states = group_invariant_witness_states(width, active, inactive)
    for group in candidate_groups:
        states = [context["initials"][key] for key in group]
        initials = tuple(states)
        words = [context["words"][key[1]] for key in group]
        streams = [sha256() for _ in group]
        first_returns = [None] * len(group)
        identity_maps_trajectory = True
        closure = None
        for moment in range(10_001):
            identity_maps_trajectory &= len(set(states)) == 1
            for lane, state in enumerate(states):
                streams[lane].update(bytes(state))
                if moment > 0 and first_returns[lane] is None and state == initials[lane]:
                    first_returns[lane] = moment
            if moment > 0 and all(value is not None for value in first_returns):
                closure = moment
                break
            states = [K.A.apply_semantic(state, word) for state, word in zip(states, words)]
        cycle_rows.append({
            "keys": group,
            "explicit_trajectory_permutation": "identity on wires 0..5814",
            "identity_maps_every_boundary_state": identity_maps_trajectory,
            "minimal_cycle_periods": tuple(first_returns),
            "common_exact_period": closure,
            "state_stream_sha256_by_key": tuple(stream.hexdigest() for stream in streams),
            "trajectory_match_is_not_rule_conjugacy": True,
        })

        for left, right in combinations(group, 2):
            left_word = context["words"][left[1]]
            right_word = context["words"][right[1]]
            witness = None
            for state_index, state in enumerate(witness_states):
                left_output = K.A.apply_semantic(state, left_word)
                right_output = K.A.apply_semantic(state, right_word)
                differences = tuple(
                    wire for wire in active if left_output[wire] != right_output[wire]
                )
                if differences:
                    witness = {
                        "group_invariant_input_index": state_index,
                        "input_fixed_by_every_S5270_element": len({state[wire] for wire in inactive}) == 1,
                        "active_output_difference_count": len(differences),
                        "first_active_difference_wires": differences[:20],
                        "left_output_active_sha256": sha256(bytes(left_output[wire] for wire in active)).hexdigest(),
                        "right_output_active_sha256": sha256(bytes(right_output[wire] for wire in active)).hexdigest(),
                    }
                    break
            pair_rows.append({
                "left": left,
                "right": right,
                "left_boundary_word_sha256": K.gate_digest(left_word),
                "right_boundary_word_sha256": K.gate_digest(right_word),
                "boundary_words_literal_equal": left_word == right_word,
                "intertwining_equation": "P F_left(s) = F_right P(s)",
                "all_declared_group_elements_refuted": witness is not None,
                "why_one_witness_refutes_the_whole_group": (
                    "the witness input is fixed by every dead-wire permutation, every P fixes "
                    "active output wires, and F_left/F_right disagree on active output"
                ),
                "witness": witness,
            })

    valid_merges = tuple(
        row for row in pair_rows if not row["all_declared_group_elements_refuted"]
    )
    result = {
        "finding": (
            "REVERSAL: the two printed trajectory-coincidence groups are not dynamical "
            "conjugacies under the declared S_5270; all seven proposed pair merges fail "
            "the exact rule-intertwining equation, so 68 C_11 classes remain, not 64."
        ),
        "profile_certificate": "all 68 t=0..2 profiles and both readings are in THE_MERGES.profiles",
        "candidate_groups": candidate_groups,
        "full_cycle_rows": tuple(cycle_rows),
        "pairwise_rule_conjugacy_rows": tuple(pair_rows),
        "proposed_pair_merges": len(pair_rows),
        "honest_rule_preserving_merges": len(valid_merges),
        "new_merges_found": (),
        "corrected_dynamical_class_count": len(keys) - len(valid_merges),
        "primary_64_class_result_refuted": True,
    }
    result["pass"] = (
        candidate_groups == EXPECTED_MERGES
        and tuple(row["common_exact_period"] for row in cycle_rows) == (5952, 4464)
        and all(
            row["identity_maps_every_boundary_state"]
            and len(set(row["minimal_cycle_periods"])) == 1
            and len(set(row["state_stream_sha256_by_key"])) == 1
            for row in cycle_rows
        )
        and len(pair_rows) == 7
        and all(
            not row["boundary_words_literal_equal"]
            and row["all_declared_group_elements_refuted"]
            and row["witness"]["input_fixed_by_every_S5270_element"]
            for row in pair_rows
        )
        and not valid_merges
        and result["corrected_dynamical_class_count"] == 68
    )
    return result


def xor_null(left: State, right: State, baseline: State) -> State:
    return tuple(a ^ b ^ c for a, b, c in zip(left, right, baseline))


def claimed_horizon(event: int, distance: int) -> int:
    if event in (0, 1):
        return 12 - distance
    if event == 2:
        return distance - int(distance % 2 == 0)
    if event == 3:
        return {2: 2, 3: 1, 4: 4, 5: 4}[distance]
    raise AssertionError((event, distance))


def separation(positions: tuple[int, ...]) -> int:
    left, right = positions
    return min((right - left) % 11, (left - right) % 11)


def horizon_row(key: Key, context: dict[str, object]) -> dict[str, object]:
    count, positions, event = key
    if count != 2:
        raise AssertionError(key)
    program = context["program"]
    baseline = context["fixtures"][event]
    multi = left = right = baseline
    multi_positions = positions
    left_position = (positions[0],)
    right_position = (positions[1],)
    forward_agreement = [True]
    reverse_atom_order_agreement = [True]
    first_difference_wires = None
    for _step in range(11):
        for station, program_row in enumerate(program):
            word = K.mapped_macro(program_row)
            if station in multi_positions:
                multi = K.A.apply_semantic(multi, word)
            if station in left_position:
                left = K.A.apply_semantic(left, word)
            if station in right_position:
                right = K.A.apply_semantic(right, word)
        composed_lr = xor_null(left, right, baseline)
        composed_rl = xor_null(right, left, baseline)
        forward_agreement.append(multi == composed_lr)
        reverse_atom_order_agreement.append(multi == composed_rl)
        if first_difference_wires is None and multi != composed_lr:
            first_difference_wires = tuple(
                wire for wire, (a, b) in enumerate(zip(multi, composed_lr)) if a != b
            )
        multi_positions = tuple((position + 1) % 11 for position in multi_positions)
        left_position = ((left_position[0] + 1) % 11,)
        right_position = ((right_position[0] + 1) % 11,)
    first_disagreement = next(
        (moment for moment, agrees in enumerate(forward_agreement) if not agrees), None
    )
    distance = separation(positions)
    formula = claimed_horizon(event, distance)
    requested_convention_exact = (
        first_disagreement == formula + 1
        and all(forward_agreement[:formula + 1])
        and all(reverse_atom_order_agreement[:formula + 1])
    )
    primary_prefix_length_convention_exact = (
        first_disagreement == formula
        and all(forward_agreement[:formula])
        and all(reverse_atom_order_agreement[:formula])
    )
    return {
        "key": key,
        "event": event,
        "separation_d": distance,
        "claimed_formula_value": formula,
        "agreement_by_boundary_multi_vs_left_xor_right": tuple(forward_agreement),
        "agreement_by_boundary_multi_vs_right_xor_left": tuple(reverse_atom_order_agreement),
        "both_atom_order_directions_exactly_match": forward_agreement == reverse_atom_order_agreement,
        "first_disagreement_boundary": first_disagreement,
        "first_difference_wire_count": len(first_difference_wires or ()),
        "first_difference_wires": (first_difference_wires or ())[:20],
        "requested_agree_through_H_then_disagree_H_plus_1": requested_convention_exact,
        "primary_prefix_length_convention_first_disagreement_at_H": primary_prefix_length_convention_exact,
    }


def horizon_certificate(keys: tuple[Key, ...], context: dict[str, object]) -> dict[str, object]:
    rows = tuple(horizon_row(key, context) for key in keys if key[0] == 2)
    table = tuple(sorted(
        (row["event"], row["separation_d"], row["first_disagreement_boundary"])
        for row in rows
    ))
    formula_table = tuple(
        (event, distance, claimed_horizon(event, distance))
        for event in range(4) for distance in range(2, 6)
    )
    result = {
        "finding": (
            "INDEXING REVERSAL: all three printed formulas equal the first-disagreement "
            "boundary itself.  They do not give a horizon through which agreement holds "
            "with first disagreement at H+1, as requested."
        ),
        "rows": rows,
        "observed_event_distance_first_disagreement": table,
        "printed_formula_table": formula_table,
        "prefix_compositional_both_atom_orders": all(
            row["both_atom_order_directions_exactly_match"] for row in rows
        ),
        "printed_formulas_exact_as_first_disagreement_index": table == formula_table,
        "requested_horizon_convention_exact": all(
            row["requested_agree_through_H_then_disagree_H_plus_1"] for row in rows
        ),
    }
    result["pass"] = (
        len(rows) == 16
        and result["prefix_compositional_both_atom_orders"]
        and result["printed_formulas_exact_as_first_disagreement_index"]
        and not result["requested_horizon_convention_exact"]
        and all(row["primary_prefix_length_convention_first_disagreement_at_H"] for row in rows)
    )
    return result


def bit_chain_certificate(corrected_classes: int) -> dict[str, object]:
    values = {count: log2(count) for count in (748, 68, 64, 11)}
    result = {
        "finding": (
            "The standalone logarithms are correct, but honest rule conjugacy changes "
            "the reduction chain to 748 -> 68 -> 68.  The atomic description cannot "
            "leave a refuted 64-class count unchanged."
        ),
        "log2_exact_values": {str(count): values[count] for count in values},
        "rounded_claimed_values": {
            "log2_748": round(values[748], 2),
            "log2_68": round(values[68], 2),
            "log2_64": round(values[64], 2),
            "log2_11_separate_allocation": round(values[11], 2),
        },
        "allocation_log2_11_kept_separate": True,
        "corrected_class_count": corrected_classes,
        "corrected_reduction_chain": (748, 68, corrected_classes),
        "atomic_description_class_count": corrected_classes,
        "primary_atomic_64_unchanged_claim_survives": corrected_classes == 64,
    }
    result["pass"] = (
        result["rounded_claimed_values"] == {
            "log2_748": 9.55, "log2_68": 6.09,
            "log2_64": 6.0, "log2_11_separate_allocation": 3.46,
        }
        and corrected_classes == 68
        and not result["primary_atomic_64_unchanged_claim_survives"]
    )
    return result


def scientific_certificates() -> dict[str, dict[str, object]]:
    keys, census = representatives()
    context = build_context(keys)
    automorphisms, active, inactive = automorphism_autopsy(context)
    profiles, candidates = invariant_profiles(keys, context, active, inactive)
    merges = merge_autopsy(keys, context, active, inactive, candidates)
    merges["representative_census"] = census
    merges["context_rebuild"] = context["summary"]
    merges["profiles"] = profiles
    merges["pass"] = (
        merges["pass"] and census["pass"]
        and context["summary"]["pass"] and profiles["pass"]
    )
    horizons = horizon_certificate(keys, context)
    bits = bit_chain_certificate(merges["corrected_dynamical_class_count"])
    return {
        "THE_AUTOMORPHISM_AUTOPSY": automorphisms,
        "THE_MERGES": merges,
        "THE_HORIZON_LAWS": horizons,
        "THE_BIT_CHAIN": bits,
    }


def render_fixed_point(certificates: dict[str, dict[str, object]]) -> str:
    labels = (
        "THE_AUTOMORPHISM_AUTOPSY",
        "THE_MERGES",
        "THE_HORIZON_LAWS",
        "THE_BIT_CHAIN",
        "CONTROLS",
    )
    for _ in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in labels}
        terminal = {
            "terminal": (
                "CYCLE858_INDEPENDENT_CHECK_REFUTES_PRIMARY"
                if all(checks.values()) else
                "CYCLE858_INDEPENDENT_CHECK_INCOMPLETE"
            ),
            "checks": checks,
            "primary_64_classes_refuted": certificates["THE_MERGES"]["primary_64_class_result_refuted"],
            "corrected_dynamical_classes": certificates["THE_MERGES"]["corrected_dynamical_class_count"],
            "runtime_seconds": certificates["CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in labels:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
                f"{compact(certificates[label])}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode())
        controls = certificates["CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass"] and controls["stdout_under_limit"]
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    primary = scientific_certificates()
    primary_digest = digest(primary)
    replay = scientific_certificates()
    replay_digest = digest(replay)
    deterministic = primary == replay and primary_digest == replay_digest
    elapsed = monotonic() - started
    controls = {
        **sources,
        "finding": (
            "Both complete independent computations were byte-for-byte deterministic; "
            "the primary remained blocked from import, both source SHAs matched, all "
            "AUDIT_INPUT_PATHS were literal existing worktree-relative paths, and the "
            "runtime/stdout caps were respected."
        ),
        "determinism": {
            "complete_scientific_certificate_recomputed": True,
            "first_sha256": primary_digest,
            "second_sha256": replay_digest,
            "exact": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_primary_loaded_after_science": PRIMARY_MODULE in sys.modules,
        "firewall_hits_after_science": tuple(FIREWALL.hits),
    }
    controls["base_pass"] = (
        sources["pass"] and deterministic and controls["runtime_under_limit"]
        and not controls["blocked_primary_loaded_after_science"]
        and not controls["firewall_hits_after_science"]
    )
    controls["pass"] = controls["base_pass"]
    primary["CONTROLS"] = controls
    output = render_fixed_point(primary)
    sys.stdout.write(output)
    return 0 if all(row["pass"] for row in primary.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
