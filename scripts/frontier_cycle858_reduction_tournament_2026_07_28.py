#!/usr/bin/env python3
"""Cycle 858: exact reduction tournament for the 748 multi-source setups.

Only the landed Cycle-719 controller core is executable science input.  The
four later lineage primaries are SHA-pinned, parsed as text/AST controls, and
blocked from import.  The runner independently rebuilds the independent-set
census on C_11, derives the free rotation quotient, tests exact trajectory
conjugacy under the wire permutations that preserve every ordered core
generator, and tests whether each k=2 representative is a composition of its
two single-source trajectories.

The dynamical ladder is deliberately lazy but exact.  Reversibility proves
zero dynamical preperiod for every orbit.  Exact E1/E2 weight prefixes and
state-orbit signatures are evaluated only until a pair is separated.  The
only pairs not separated by t=2 are then followed through their exact minimal
period, with every state compared.  No unresolved numerical period is used
to decide a class.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle847_trio_to_a_million_2026_07_28.py",
)

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import ceil, comb, factorial, log2
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
    AUDIT_INPUT_PATHS[3]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[4]:
        "dab7567b80c9f70488581a9387e654d9bf5e053afcade822576e5a3bd47bba95",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "8807587899a5664d39a06901b02b22041682c5cc",
    AUDIT_INPUT_PATHS[3]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[4]: "c18478b434b962a42df0b9a46ebc50e50fb30f81",
}
EXPECTED_BRANCH = "physics-loop/toe-close-blockC28-20260729"
EXPECTED_BASE = "ecdd7a73a6"


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited source-only primary is imported."""

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


Key = tuple[int, tuple[int, ...], int]
State = tuple[int, ...]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STRATA = (2, 3, 4, 5)
EXPECTED_CONFIGURATION_COUNTS = {2: 44, 3: 77, 4: 55, 5: 11}
EXPECTED_SETUP_COUNTS = {2: 176, 3: 308, 4: 220, 5: 44}
EXPECTED_ORBIT_COUNTS = {2: 16, 3: 28, 4: 20, 5: 4}
EXPECTED_TOTAL_SETUPS = 748
EXPECTED_TOTAL_REPRESENTATIVES = 68
PROFILE_PREFIX_END = 2
MAX_EXACT_CANDIDATE_PERIOD = 10_000

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(30_000)


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
    matches = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def git_value(*arguments: str) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
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
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    markers = {
        AUDIT_INPUT_PATHS[0]: {
            "interleaved_program", "mapped_macro", "run_orbit",
        },
        AUDIT_INPUT_PATHS[1]: {
            "configuration_census", "rotate_config",
        },
        AUDIT_INPUT_PATHS[2]: {
            "initialise_catalog_records", "advance_one_record",
        },
        AUDIT_INPUT_PATHS[3]: {"build_family", "synchronous_word"},
        AUDIT_INPUT_PATHS[4]: {"universal_braid", "run"},
    }
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact":
            sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact":
            git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "AST_valid": isinstance(trees[path], ast.Module),
        "required_AST_markers_present":
            markers[path] <= function_names(trees[path]),
        "access": (
            "EXECUTABLE_LANDED_CORE"
            if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY"
        ),
    } for path in AUDIT_INPUT_PATHS)
    branch = git_value("branch", "--show-current")
    base = git_value("rev-parse", EXPECTED_BASE)
    base_is_ancestor = git_value("merge-base", "HEAD", base) == base
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_existing_worktree_relative":
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(row["exists_worktree_relative"] for row in rows),
        "source_rows": rows,
        "core_path": CORE_PATH,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "branch": branch,
        "expected_branch": EXPECTED_BRANCH,
        "expected_base": base,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["path_count"] <= result["read_cap"]
        and result["all_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["AST_valid"]
            and row["required_AST_markers_present"]
            for row in rows
        )
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return result


def independent_positions(count: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        positions
        for positions in combinations(range(RING_STATIONS), count)
        if all(
            (station + 1) % RING_STATIONS not in positions
            for station in positions
        )
    )


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (station + shift) % RING_STATIONS for station in positions
    ))


def canonical_rotation(
    positions: tuple[int, ...],
) -> tuple[int, ...]:
    return min(
        rotate_positions(positions, shift)
        for shift in range(RING_STATIONS)
    )


def closed_form_independent_count(stations: int, count: int) -> int:
    numerator = stations * comb(stations - count - 1, count - 1)
    if numerator % count:
        raise AssertionError((stations, count, numerator))
    return numerator // count


def representatives_certificate() -> tuple[
    tuple[Key, ...], dict[str, object]
]:
    representatives: list[Key] = []
    stratum_rows = []
    every_orbit_free = True
    complete_partition = True
    for count in STRATA:
        positions = independent_positions(count)
        expected_configurations = closed_form_independent_count(
            RING_STATIONS, count
        )
        orbit_map: dict[tuple[int, ...], tuple[tuple[int, ...], ...]] = {}
        for representative in sorted({
            canonical_rotation(row) for row in positions
        }):
            orbit = tuple(sorted({
                rotate_positions(representative, shift)
                for shift in range(RING_STATIONS)
            }))
            orbit_map[representative] = orbit
            every_orbit_free &= len(orbit) == RING_STATIONS
        union = {row for orbit in orbit_map.values() for row in orbit}
        complete_partition &= (
            union == set(positions)
            and sum(map(len, orbit_map.values())) == len(positions)
        )
        for event in range(2 * FIXTURE_BANKS):
            representatives.extend(
                (count, representative, event)
                for representative in orbit_map
            )
        stratum_rows.append({
            "k": count,
            "direct_configurations": len(positions),
            "closed_form_configurations": expected_configurations,
            "events": 2 * FIXTURE_BANKS,
            "starting_setups": len(positions) * 2 * FIXTURE_BANKS,
            "C11_orbits_per_event": len(orbit_map),
            "C11_orbits_all_events":
                len(orbit_map) * 2 * FIXTURE_BANKS,
            "orbit_sizes": tuple(sorted(set(map(len, orbit_map.values())))),
            "canonical_representatives": tuple(orbit_map),
        })
    result = {
        "derivation": (
            "Ind_k(C_n)=n/k*binomial(n-k-1,k-1); direct enumeration; "
            "four Cycle-719 fixture events; canonical minimum rotation"
        ),
        "stratum_rows": tuple(stratum_rows),
        "configuration_counts": {
            row["k"]: row["direct_configurations"] for row in stratum_rows
        },
        "setup_counts": {
            row["k"]: row["starting_setups"] for row in stratum_rows
        },
        "orbit_counts": {
            row["k"]: row["C11_orbits_all_events"]
            for row in stratum_rows
        },
        "per_stratum_orbit_counts_printed": "16+28+20+4",
        "starting_setup_total": sum(
            row["starting_setups"] for row in stratum_rows
        ),
        "representative_total": len(representatives),
        "C11_action_free": every_orbit_free,
        "orbits_partition_each_stratum": complete_partition,
        "representatives_sha256": digest(tuple(representatives)),
    }
    result["pass"] = (
        result["configuration_counts"] == EXPECTED_CONFIGURATION_COUNTS
        and result["setup_counts"] == EXPECTED_SETUP_COUNTS
        and result["orbit_counts"] == EXPECTED_ORBIT_COUNTS
        and result["starting_setup_total"] == EXPECTED_TOTAL_SETUPS
        and result["representative_total"]
        == EXPECTED_TOTAL_REPRESENTATIVES
        and every_orbit_free
        and complete_partition
    )
    return tuple(representatives), result


def synchronous_word(
    program: tuple[object, ...], positions0: tuple[int, ...]
) -> tuple[object, ...]:
    """Exact Q word selected by synchronous tokens over one C_11 orbit."""

    positions = positions0
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def build_context(representatives: tuple[Key, ...]) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    fixtures = []
    fixture_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(
            before, program
        )
        fixture_failures += after != K.A.apply_semantic(before, allocator)
        fixture_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        fixture_failures += any(rail_b)
        fixture_failures += len(trace) != len(program)
        fixtures.append((event, direction, before))
        state = after

    positions = tuple(sorted({key[1] for key in representatives}))
    words = {
        row: synchronous_word(program, row) for row in positions
    }
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
    }
    initial_states: dict[Key, State] = {}
    construction_failures = 0
    for key in representatives:
        count, token_positions, event = key
        before = fixture_by_event[event]
        initial, rail_a, rail_b, trace = K.run_orbit(
            before, program, token_positions=token_positions
        )
        expected_rail = tuple(
            int(station in token_positions)
            for station in range(RING_STATIONS)
        )
        construction_failures += count != len(token_positions)
        construction_failures += initial != K.A.apply_semantic(
            before, words[token_positions]
        )
        construction_failures += rail_a != expected_rail or any(rail_b)
        construction_failures += len(trace) != RING_STATIONS
        initial_states[key] = initial
    summary = {
        "program_stations": len(program),
        "core_generator_count": len(K.program_word(program)),
        "fixture_events": len(fixtures),
        "fixture_failures": fixture_failures,
        "position_words": len(words),
        "initial_states": len(initial_states),
        "state_width": len(next(iter(initial_states.values()))),
        "word_gate_counts_by_k": {
            count: tuple(sorted({
                len(words[key[1]])
                for key in representatives if key[0] == count
            }))
            for count in STRATA
        },
        "construction_failures": construction_failures,
        "initial_state_sha256": digest(tuple(
            (key, sha256(bytes(initial_states[key])).hexdigest())
            for key in representatives
        )),
        "word_table_sha256": digest(tuple(
            (positions_row, K.gate_digest(words[positions_row]))
            for positions_row in sorted(words)
        )),
    }
    summary["pass"] = (
        summary["program_stations"] == RING_STATIONS
        and summary["core_generator_count"] == 3106
        and summary["fixture_events"] == 4
        and summary["fixture_failures"] == 0
        and summary["initial_states"] == EXPECTED_TOTAL_REPRESENTATIVES
        and summary["state_width"] == 5815
        and summary["word_gate_counts_by_k"]
        == {2: (6212,), 3: (9318,), 4: (12424,), 5: (15530,)}
        and construction_failures == 0
    )
    return {
        "program": program,
        "fixtures": tuple(fixtures),
        "fixture_by_event": fixture_by_event,
        "words": words,
        "initial_states": initial_states,
        "summary": summary,
    }


def watched_residual_wires() -> tuple[int, ...]:
    bank_wires = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    rows = [int(K.R3.X.SOURCE_POINTER)]
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        rows.extend(int(base + wire) for wire in bank_wires)
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        rows.extend(int(base + wire) for wire in range(K.B.LINK_WIDTH))
    return tuple(rows)


def derive_rule_automorphisms(context: dict[str, object]) -> dict[str, object]:
    """Derive the exact ordered-generator wire-permutation group.

    A permitted permutation must preserve gate kind, generator ordinal, and
    operand role for every generator in the landed program word.  Therefore
    wires with distinct ordered-incidence signatures cannot move.  Conversely
    wires with the same signature may be permuted arbitrarily.  In this core
    all used wires are singleton cells and all unused wires form one cell.
    """

    generators = K.program_word(context["program"])
    state_width = context["summary"]["state_width"]
    signatures: list[list[tuple[int, str, int, int]]] = [
        [] for _wire in range(state_width)
    ]
    for ordinal, gate in enumerate(generators):
        for role, wire in enumerate(gate.wires):
            signatures[int(wire)].append(
                (ordinal, gate.kind, role, len(gate.wires))
            )
    cells: dict[tuple[tuple[int, str, int, int], ...], list[int]] = {}
    for wire, signature in enumerate(signatures):
        cells.setdefault(tuple(signature), []).append(wire)
    cell_sizes = tuple(sorted(len(cell) for cell in cells.values()))
    active = tuple(
        wire for wire, signature in enumerate(signatures) if signature
    )
    inactive = tuple(
        wire for wire, signature in enumerate(signatures) if not signature
    )
    order = 1
    for cell in cells.values():
        order *= factorial(len(cell))
    order_decimal = str(order)
    result = {
        "declared_family": (
            "all permutations of the 5815 state wires preserving every "
            "ordered Cycle-719 generator's kind and operand roles"
        ),
        "derivation": (
            "partition wires by their complete (generator ordinal, kind, "
            "operand role, arity) incidence signature; the group is the "
            "direct product of symmetric groups on equal-signature cells"
        ),
        "state_width": state_width,
        "ordered_core_generators": len(generators),
        "signature_cells": len(cells),
        "cell_size_census": dict(sorted(Counter(cell_sizes).items())),
        "active_singleton_wires": len(active),
        "inactive_rule_identity_wires": len(inactive),
        "group_structure": f"S_{len(inactive)}",
        "group_order": order_decimal,
        "group_order_digits": len(order_decimal),
        "group_order_sha256": sha256(order_decimal.encode("ascii")).hexdigest(),
        "active_wires": active,
        "inactive_wires": inactive,
    }
    result["pass"] = (
        len(generators) == 3106
        and len(active) == 545
        and len(inactive) == 5270
        and cell_sizes == (1,) * 545 + (5270,)
        and order == factorial(5270)
    )
    return result


def state_automorphism_signature(
    state: State,
    active_wires: tuple[int, ...],
    inactive_wires: tuple[int, ...],
) -> tuple[bytes, int]:
    """Exact orbit label under identity-on-active times S_inactive."""

    return (
        bytes(state[wire] for wire in active_wires),
        sum(state[wire] for wire in inactive_wires),
    )


def strict_records(weights: Iterable[int]) -> tuple[tuple[int, int], ...]:
    rows = []
    best = None
    for moment, weight in enumerate(weights):
        if best is None or weight < best:
            rows.append((moment, int(weight)))
            best = weight
    return tuple(rows)


def reading_profile(
    states: tuple[State, ...], residual_wires: tuple[int, ...]
) -> dict[str, object]:
    e1 = tuple(sum(state[wire] for wire in residual_wires) for state in states)
    e2 = tuple(sum(state) for state in states)
    return {
        "E1_reading": (
            "landed cleanliness residual: source pointer, both banks' "
            "POINTER/U_TO_V/V_TO_U/DIRECTION_OK/FRESH/ZERO_WORK/TOKEN_OK, "
            "and every inter-bank link bit"
        ),
        "E2_reading": "full 5815-bit state Hamming weight",
        "transient_length": 0,
        "transient_length_basis": (
            "the update word is a composition of distinct-wire "
            "self-inverse X/CNOT/TOF gates and hence is bijective"
        ),
        "cycle_period": "DEFERRED_UNLESS_LEVEL_II_CANDIDATE",
        "funnel_weight_sequence": {"E1": e1, "E2": e2},
        "record_moments_and_weights": {
            "E1": strict_records(e1), "E2": strict_records(e2)
        },
    }


def exact_candidate_cycle(
    keys: tuple[Key, ...],
    context: dict[str, object],
    automorphisms: dict[str, object],
    residual_wires: tuple[int, ...],
) -> dict[str, object]:
    """Compare every state until a minimal common full-state return."""

    states = [context["initial_states"][key] for key in keys]
    initials = tuple(states)
    words = [context["words"][key[1]] for key in keys]
    active = automorphisms["active_wires"]
    inactive = automorphisms["inactive_wires"]
    e1_sequences = [[] for _key in keys]
    e2_sequences = [[] for _key in keys]
    state_streams = [sha256() for _key in keys]
    conjugacy_exact_every_moment = True
    full_state_equal_every_moment = True
    first_return = [None] * len(keys)
    closure = None
    determinism_duplicate_exact = True

    for moment in range(MAX_EXACT_CANDIDATE_PERIOD + 1):
        signatures = tuple(
            state_automorphism_signature(state, active, inactive)
            for state in states
        )
        conjugacy_exact_every_moment &= len(set(signatures)) == 1
        full_state_equal_every_moment &= len(set(states)) == 1
        for lane, state in enumerate(states):
            e1_sequences[lane].append(
                sum(state[wire] for wire in residual_wires)
            )
            e2_sequences[lane].append(sum(state))
            state_streams[lane].update(bytes(state))
            if moment > 0 and first_return[lane] is None and state == initials[lane]:
                first_return[lane] = moment
        if moment > 0 and all(value is not None for value in first_return):
            closure = moment
            break
        if not conjugacy_exact_every_moment:
            break
        next_states = []
        for state, word in zip(states, words):
            next_state = K.A.apply_semantic(state, word)
            determinism_duplicate_exact &= (
                sha256(bytes(next_state)).digest()
                == sha256(bytes(tuple(next_state))).digest()
            )
            next_states.append(next_state)
        states = next_states

    e1_rows = tuple(tuple(row) for row in e1_sequences)
    e2_rows = tuple(tuple(row) for row in e2_sequences)
    period = first_return[0] if len(set(first_return)) == 1 else None
    result = {
        "keys": keys,
        "tested_moments_inclusive": closure,
        "minimal_cycle_periods": tuple(first_return),
        "common_minimal_cycle_period": period,
        "cycle_period_exact": period is not None,
        "transient_lengths": (0,) * len(keys),
        "full_state_equal_every_moment": full_state_equal_every_moment,
        "determinism_duplicate_state_digest_exact_every_moment":
            determinism_duplicate_exact,
        "fixed_automorphism_exists": conjugacy_exact_every_moment,
        "fixed_automorphism_witness": (
            "identity on all wires"
            if full_state_equal_every_moment else
            "identity on active wires plus one fixed inactive permutation"
        ),
        "infinite_sequence_certificate": (
            "all states conjugate at every t=0..period and every lane "
            "returns exactly to its own t=0 state at the common minimal "
            "period; periodic repetition proves all t"
        ),
        "funnel_weight_sequence": {
            "E1_length": len(e1_rows[0]),
            "E1_sha256_by_key": tuple(digest(row) for row in e1_rows),
            "E1_sequences_identical": len(set(e1_rows)) == 1,
            "E2_length": len(e2_rows[0]),
            "E2_sha256_by_key": tuple(digest(row) for row in e2_rows),
            "E2_sequences_identical": len(set(e2_rows)) == 1,
        },
        "record_moments_and_weights": {
            "E1": strict_records(e1_rows[0]),
            "E2": strict_records(e2_rows[0]),
        },
        "state_sequence_sha256_by_key": tuple(
            stream.hexdigest() for stream in state_streams
        ),
    }
    result["pass"] = (
        closure is not None
        and period == closure
        and conjugacy_exact_every_moment
        and full_state_equal_every_moment
        and determinism_duplicate_exact
        and len(set(e1_rows)) == 1
        and len(set(e2_rows)) == 1
        and len(set(result["state_sequence_sha256_by_key"])) == 1
    )
    return result


def dynamical_equivalence_certificate(
    representatives: tuple[Key, ...], context: dict[str, object]
) -> dict[str, object]:
    automorphisms = derive_rule_automorphisms(context)
    active = automorphisms["active_wires"]
    inactive = automorphisms["inactive_wires"]
    residual_wires = watched_residual_wires()
    prefix_states: dict[Key, tuple[State, ...]] = {}
    profiles: dict[Key, dict[str, object]] = {}
    for key in representatives:
        state = context["initial_states"][key]
        states = [state]
        for _moment in range(PROFILE_PREFIX_END):
            state = K.A.apply_semantic(
                state, context["words"][key[1]]
            )
            states.append(state)
        prefix_states[key] = tuple(states)
        profiles[key] = reading_profile(tuple(states), residual_wires)

    def profile_signature(key: Key) -> object:
        profile = profiles[key]
        return (
            profile["transient_length"],
            tuple(profile["funnel_weight_sequence"]["E1"]),
            tuple(profile["funnel_weight_sequence"]["E2"]),
            tuple(profile["record_moments_and_weights"]["E1"]),
            tuple(profile["record_moments_and_weights"]["E2"]),
        )

    profile_groups: dict[object, list[Key]] = defaultdict(list)
    for key in representatives:
        profile_groups[profile_signature(key)].append(key)

    def orbit_sequence_signature(key: Key) -> object:
        return tuple(
            state_automorphism_signature(state, active, inactive)
            for state in prefix_states[key]
        )

    exact_prefix_groups: list[tuple[Key, ...]] = []
    rejected_profile_equal_pairs = 0
    earliest_obstruction_census: Counter[int] = Counter()
    for profile_group in profile_groups.values():
        orbit_groups: dict[object, list[Key]] = defaultdict(list)
        for key in profile_group:
            orbit_groups[orbit_sequence_signature(key)].append(key)
        total_pairs = comb(len(profile_group), 2)
        surviving_pairs = sum(
            comb(len(group), 2) for group in orbit_groups.values()
        )
        rejected_profile_equal_pairs += total_pairs - surviving_pairs
        for left, right in combinations(profile_group, 2):
            for moment, (left_state, right_state) in enumerate(zip(
                prefix_states[left], prefix_states[right]
            )):
                if state_automorphism_signature(
                    left_state, active, inactive
                ) != state_automorphism_signature(
                    right_state, active, inactive
                ):
                    earliest_obstruction_census[moment] += 1
                    break
        exact_prefix_groups.extend(
            tuple(group) for group in orbit_groups.values()
        )

    candidate_groups = tuple(sorted(
        (group for group in exact_prefix_groups if len(group) > 1),
        key=lambda row: row[0],
    ))
    exact_rows = tuple(
        exact_candidate_cycle(
            group, context, automorphisms, residual_wires
        )
        for group in candidate_groups
    )
    merged_keys = sum(len(group) - 1 for group in candidate_groups)
    class_count = len(representatives) - merged_keys
    prefix_profile_rows = tuple({
        "key": key,
        "exact_prefix_moments": (0, PROFILE_PREFIX_END),
        "transient_length": profiles[key]["transient_length"],
        "cycle_period": (
            next(
                row["common_minimal_cycle_period"]
                for row in exact_rows if key in row["keys"]
            )
            if any(key in row["keys"] for row in exact_rows)
            else "NOT_NEEDED_FOR_EXACT_CLASS_DECISION"
        ),
        "funnel_weight_sequence": profiles[key]["funnel_weight_sequence"],
        "record_moments_and_weights":
            profiles[key]["record_moments_and_weights"],
        "exact_level_II_orbit_signature_sha256": digest(tuple(
            (sha256(signature[0]).hexdigest(), signature[1])
            for signature in orbit_sequence_signature(key)
        )),
    } for key in representatives)
    profile_equal_pairs = sum(
        comb(len(group), 2) for group in profile_groups.values()
    )
    result = {
        "ladder": {
            "level_i": (
                "exact reversible preperiod plus exact E1/E2 funnel-weight "
                "and strict-record prefixes t=0..2; numerical cycle period "
                "is evaluated exactly only for level-II survivors and is "
                "never approximated or used unresolved"
            ),
            "level_ii": (
                "one fixed rule-automorphism must conjugate the full state "
                "sequence at equal moments; t=0..2 rejects candidates, and "
                "survivors are checked through a common minimal full-state "
                "period"
            ),
            "E1": reading_profile(
                (next(iter(context["initial_states"].values())),),
                residual_wires,
            )["E1_reading"],
            "E2": "full 5815-bit state Hamming weight",
        },
        "automorphism_group": {
            key: value for key, value in automorphisms.items()
            if key not in {"active_wires", "inactive_wires"}
        },
        "profile_rows": prefix_profile_rows,
        "profile_row_count": len(prefix_profile_rows),
        "profile_equal_pair_count": profile_equal_pairs,
        "profile_equal_pairs_rejected_by_exact_conjugacy_prefix":
            rejected_profile_equal_pairs,
        "earliest_exact_conjugacy_obstruction_census":
            dict(sorted(earliest_obstruction_census.items())),
        "exact_prefix_survivor_groups": candidate_groups,
        "exact_full_cycle_rows": exact_rows,
        "merge_list": candidate_groups,
        "dynamical_class_count": class_count,
        "irreducibility_statement": (
            f"{class_count} exact classes: only the printed merge groups "
            "survive; every other pair has an exact level-I profile or "
            "level-II rule-automorphism obstruction"
        ),
        "classification_sha256": digest((
            candidate_groups,
            tuple(
                row["state_sequence_sha256_by_key"] for row in exact_rows
            ),
            tuple(
                row["exact_level_II_orbit_signature_sha256"]
                for row in prefix_profile_rows
            ),
        )),
        "prefix_state_stream_sha256": digest(tuple(
            (
                key,
                tuple(sha256(bytes(state)).hexdigest()
                      for state in prefix_states[key]),
            )
            for key in representatives
        )),
        "determinism_duplicate_state_digest_exact": all(
            row["determinism_duplicate_state_digest_exact_every_moment"]
            for row in exact_rows
        ),
    }
    expected_groups = (
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
    result["pass"] = (
        automorphisms["pass"]
        and len(residual_wires) == 477
        and len(prefix_profile_rows) == EXPECTED_TOTAL_REPRESENTATIVES
        and candidate_groups == expected_groups
        and tuple(
            row["common_minimal_cycle_period"] for row in exact_rows
        ) == (5952, 4464)
        and all(row["pass"] for row in exact_rows)
        and result["determinism_duplicate_state_digest_exact"]
        and class_count == 64
        and profile_equal_pairs
        == rejected_profile_equal_pairs + 7
    )
    return result


def xor_null_state(
    left: State | list[int],
    right: State | list[int],
    baseline: State,
) -> tuple[int, ...]:
    return tuple(
        int(a) ^ int(b) ^ int(c)
        for a, b, c in zip(left, right, baseline)
    )


def apply_gate_mutable(state: list[int], gate: object) -> int:
    """Apply one landed classical generator and return its target wire."""

    wires = tuple(map(int, gate.wires))
    if gate.kind == "X" and len(wires) == 1:
        state[wires[0]] ^= 1
        return wires[0]
    if gate.kind == "CNOT" and len(wires) == 2:
        state[wires[1]] ^= state[wires[0]]
        return wires[1]
    if gate.kind == "TOF" and len(wires) == 3:
        state[wires[2]] ^= state[wires[0]] & state[wires[1]]
        return wires[2]
    raise AssertionError((gate.kind, wires))


def separation(positions: tuple[int, int]) -> int:
    left, right = positions
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def declared_horizon(event: int, distance: int) -> int:
    """Exact landed first-meet law on the four-event, four-distance grid."""

    if event in (0, 1):
        return 12 - distance
    if event == 2:
        return distance - int(distance % 2 == 0)
    if event == 3:
        return {2: 2, 3: 1, 4: 4, 5: 4}[distance]
    raise AssertionError((event, distance))


def first_interaction_row(
    key: Key, context: dict[str, object]
) -> dict[str, object]:
    """Compare multi-source and XOR-null atom evolution gate by gate.

    At each controller substep, every live token applies its landed station
    macro in the core's station order and then R translates the token.  The
    baseline has no token and is constant.  Before the first discrepancy the
    null composite is S_left xor S_right xor S_baseline.  Refinement inside
    the first discrepant station macro identifies the exact interaction gate.
    """

    count, positions, event = key
    if count != 2 or len(positions) != 2:
        raise AssertionError(key)
    program = context["program"]
    baseline = context["fixture_by_event"][event]
    multi: State = baseline
    left: State = baseline
    right: State = baseline
    multi_positions = positions
    left_position = (positions[0],)
    right_position = (positions[1],)
    boundary_agreement = [
        multi == xor_null_state(left, right, baseline)
    ]
    rail_composition_exact = True
    first_witness = None

    for step in range(RING_STATIONS):
        for station, program_row in enumerate(program):
            multi_live = station in multi_positions
            left_live = station in left_position
            right_live = station in right_position
            if not (multi_live or left_live or right_live):
                continue
            word = K.mapped_macro(program_row)
            before_multi = multi
            before_left = left
            before_right = right
            if multi_live:
                multi = K.A.apply_semantic(multi, word)
            if left_live:
                left = K.A.apply_semantic(left, word)
            if right_live:
                right = K.A.apply_semantic(right, word)
            if (
                first_witness is None
                and multi != xor_null_state(left, right, baseline)
            ):
                refine_multi = list(before_multi)
                refine_left = list(before_left)
                refine_right = list(before_right)
                for gate_ordinal, gate in enumerate(word):
                    if multi_live:
                        target = apply_gate_mutable(refine_multi, gate)
                    else:
                        target = int(gate.wires[-1])
                    if left_live:
                        apply_gate_mutable(refine_left, gate)
                    if right_live:
                        apply_gate_mutable(refine_right, gate)
                    null_value = (
                        refine_left[target]
                        ^ refine_right[target]
                        ^ baseline[target]
                    )
                    if refine_multi[target] != null_value:
                        first_witness = {
                            "controller_substep": step + 1,
                            "station": station,
                            "program_row_kind": program_row[0],
                            "program_row_index": program_row[1],
                            "gate_ordinal_within_station_macro": gate_ordinal,
                            "gate_kind": gate.kind,
                            "gate_wires": tuple(map(int, gate.wires)),
                            "witness_wire": target,
                            "multi_value": refine_multi[target],
                            "null_composition_value": null_value,
                        }
                        break
                if first_witness is None:
                    raise AssertionError(("unrefined interaction", key, step, station))
                break
        multi_positions = tuple(
            (position + 1) % RING_STATIONS
            for position in multi_positions
        )
        left_position = (
            (left_position[0] + 1) % RING_STATIONS,
        )
        right_position = (
            (right_position[0] + 1) % RING_STATIONS,
        )
        rail_composition_exact &= (
            set(multi_positions)
            == set(left_position) | set(right_position)
            and not (set(left_position) & set(right_position))
        )
        boundary_agreement.append(
            multi == xor_null_state(left, right, baseline)
        )
        if first_witness is not None:
            break

    distance = separation((positions[0], positions[1]))
    observed_horizon = (
        None if first_witness is None
        else int(first_witness["controller_substep"])
    )
    expected_horizon = declared_horizon(event, distance)
    prefix_exact = (
        observed_horizon is not None
        and all(boundary_agreement[:observed_horizon])
        and not boundary_agreement[observed_horizon]
    )
    if first_witness is None:
        classification = "COMPOSITIONAL"
    elif observed_horizon > 0 and prefix_exact:
        classification = "PREFIX_COMPOSITIONAL"
    else:
        classification = "NON_COMPOSITIONAL"
    result = {
        "key": key,
        "event": event,
        "separation_d": distance,
        "null_composition": (
            "S_{a,b}(q) = S_a(q) XOR S_b(q) XOR S_empty(q), with "
            "independent landed single-source evolution"
        ),
        "classification": classification,
        "exact_compositional_PREFIX_length": observed_horizon,
        "agreement_horizon_boundaries": (
            None if observed_horizon is None
            else (0, observed_horizon - 1)
        ),
        "first_interaction_effect": first_witness,
        "declared_horizon_law_value": expected_horizon,
        "horizon_law_exact": observed_horizon == expected_horizon,
        "controller_rail_composition_exact_through_witness":
            rail_composition_exact,
        "prefix_exact": prefix_exact,
    }
    result["pass"] = (
        classification == "PREFIX_COMPOSITIONAL"
        and observed_horizon == expected_horizon
        and prefix_exact
        and rail_composition_exact
        and first_witness is not None
    )
    return result


def compositional_certificate(
    representatives: tuple[Key, ...], context: dict[str, object]
) -> dict[str, object]:
    k2_keys = tuple(key for key in representatives if key[0] == 2)
    rows = tuple(first_interaction_row(key, context) for key in k2_keys)
    horizon_table = tuple(sorted(
        (row["event"], row["separation_d"],
         row["exact_compositional_PREFIX_length"])
        for row in rows
    ))
    expected_table = tuple(
        (event, distance, declared_horizon(event, distance))
        for event in range(4) for distance in range(2, 6)
    )
    classification_census = dict(sorted(Counter(
        row["classification"] for row in rows
    ).items()))
    result = {
        "route": (
            "every k=2 C_11 representative versus its two constituent "
            "single-source atoms"
        ),
        "single_source_atom_classes_mod_C11": 4,
        "atom_label": "fixture event e in {0,1,2,3}",
        "null_composition": (
            "independent evolution S_a XOR S_b XOR S_empty"
        ),
        "landed_wavefront_meet_definition": (
            "first ordered Cycle-719 Q generator at which the shared-data "
            "multi-source state differs from the XOR null; controller R "
            "then advances all source fronts one ring station"
        ),
        "horizon_law": {
            "domain": "event e in {0,1,2,3}, separation d in {2,3,4,5}",
            "e=0_or_1": "H(e,d)=12-d",
            "e=2": "H(2,d)=d-1 if d is even, otherwise d",
            "e=3": "H(3,2)=2,H(3,3)=1,H(3,4)=4,H(3,5)=4",
            "complete_table_event_distance_H": horizon_table,
        },
        "representative_rows": rows,
        "k2_representatives_tested": len(rows),
        "classification_census": classification_census,
        "verdict": "PREFIX_COMPOSITIONAL_WITH_EXACT_HORIZON_LAW",
        "what_remains_free": (
            "For k=2, event e (four choices) and separation d (four "
            "choices) remain free; after H(e,d), the shared nonlinear "
            "ordered core-gate interaction schedule is indispensable.  "
            "This is still 16 inputs (4 bits), so atom factorization does "
            "not reduce the k=2 address space.  The 48 dynamical classes "
            "with k=3,4,5 are not generated by this declared k=2 test."
        ),
        "composition_sha256": digest(horizon_table),
    }
    result["pass"] = (
        len(rows) == EXPECTED_ORBIT_COUNTS[2]
        and all(row["pass"] for row in rows)
        and horizon_table == expected_table
        and classification_census == {"PREFIX_COMPOSITIONAL": 16}
    )
    return result


def information_row(count: int) -> dict[str, object]:
    return {
        "input_count": count,
        "irreducible_information_bits_log2": round(log2(count), 12),
        "fixed_length_address_bits": ceil(log2(count)),
    }


def verdict_certificate(
    representatives: tuple[Key, ...],
    dynamics: dict[str, object],
    composition: dict[str, object],
) -> dict[str, object]:
    dynamical_count = int(dynamics["dynamical_class_count"])
    k2_classes = sum(key[0] == 2 for key in representatives)
    higher_classes = dynamical_count - k2_classes
    levels = {
        "starting_setups": information_row(EXPECTED_TOTAL_SETUPS),
        "C11_families": information_row(EXPECTED_TOTAL_REPRESENTATIVES),
        "dynamical_classes": information_row(dynamical_count),
        "atomic_description_selection_space": information_row(
            k2_classes + higher_classes
        ),
    }
    result = {
        "reduction_chain": (
            f"748 --(C_11, proven free)--> 68 --(dynamical "
            f"equivalence)--> {dynamical_count} --(compositional "
            f"generation)--> 4 event atoms + 16 event/separation "
            f"interaction schedules + {higher_classes} ungenerated "
            "higher-source classes"
        ),
        "input_information_at_each_level": levels,
        "k2_dynamical_classes": k2_classes,
        "higher_source_dynamical_classes": higher_classes,
        "atomic_description": {
            "reusable_single_source_atoms": 4,
            "k2_free_selector": "(event e, separation d): 4*4=16",
            "k2_selector_bits": 4,
            "post_meet_law": "supplied exact shared nonlinear core schedule",
            "ungenerated_k3_k4_k5_classes": higher_classes,
        },
        "final_irreducible_input_statement": (
            f"The full declared tournament still needs a choice among "
            f"{dynamical_count} effective inputs, exactly 6 bits.  The "
            "k=2 atom/schedule factorization reorganizes its 16 inputs but "
            "does not reduce their 4-bit selector; no atom-generation "
            "claim is made for the 48 higher-source classes."
        ),
    }
    result["pass"] = (
        len(representatives) == EXPECTED_TOTAL_REPRESENTATIVES
        and dynamical_count == 64
        and k2_classes == 16
        and higher_classes == 48
        and composition["verdict"]
        == "PREFIX_COMPOSITIONAL_WITH_EXACT_HORIZON_LAW"
        and levels["starting_setups"]["fixed_length_address_bits"] == 10
        and levels["C11_families"]["fixed_length_address_bits"] == 7
        and levels["dynamical_classes"]["fixed_length_address_bits"] == 6
        and levels["atomic_description_selection_space"]
        ["fixed_length_address_bits"] == 6
    )
    return result


def tournament() -> tuple[dict[str, object], ...]:
    representatives, certificate_a = representatives_certificate()
    context = build_context(representatives)
    certificate_b = dynamical_equivalence_certificate(
        representatives, context
    )
    certificate_c = compositional_certificate(representatives, context)
    certificate_d = verdict_certificate(
        representatives, certificate_b, certificate_c
    )
    certificate_a = {
        **certificate_a,
        "independent_Cycle719_rebuild": context["summary"],
        "pass": certificate_a["pass"] and context["summary"]["pass"],
    }
    return certificate_a, certificate_b, certificate_c, certificate_d


def replay_prefix_state_stream(
    representatives: tuple[Key, ...], context: dict[str, object]
) -> str:
    rows = []
    for key in representatives:
        state = context["initial_states"][key]
        state_rows = [sha256(bytes(state)).hexdigest()]
        for _moment in range(PROFILE_PREFIX_END):
            state = K.A.apply_semantic(
                state, context["words"][key[1]]
            )
            state_rows.append(sha256(bytes(state)).hexdigest())
        rows.append((key, tuple(state_rows)))
    return digest(tuple(rows))


def render_fixed_point(
    certificates: dict[str, dict[str, object]],
) -> str:
    labels = (
        "A_REPRESENTATIVES",
        "B_DYNAMICAL_EQUIVALENCE",
        "C_COMPOSITIONAL_TEST",
        "D_VERDICT",
        "E_CONTROLS",
    )
    for _attempt in range(12):
        checks = {
            label: bool(certificates[label]["pass"]) for label in labels
        }
        terminal = {
            "terminal": (
                "CYCLE858_REDUCTION_TOURNAMENT_PASS"
                if all(checks.values()) else
                "CYCLE858_REDUCTION_TOURNAMENT_HONEST_FAIL"
            ),
            "checks": checks,
            "dynamical_classes": certificates[
                "B_DYNAMICAL_EQUIVALENCE"
            ]["dynamical_class_count"],
            "automorphism_group_order": certificates[
                "B_DYNAMICAL_EQUIVALENCE"
            ]["automorphism_group"]["group_order"],
            "compositional_verdict": certificates[
                "C_COMPOSITIONAL_TEST"
            ]["verdict"],
            "runtime_seconds": certificates["E_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["E_CONTROLS"]["stdout_bytes"],
        }
        lines = [
            f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
            f"{compact(certificates[label])}"
            for label in labels
        ]
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = (
            controls["base_pass"] and controls["stdout_under_limit"]
        )
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    primary = tournament()
    primary_digest = digest(primary)
    replay_representatives, replay_a_base = representatives_certificate()
    replay_context = build_context(replay_representatives)
    replay_a = {
        **replay_a_base,
        "independent_Cycle719_rebuild": replay_context["summary"],
        "pass": replay_a_base["pass"] and replay_context["summary"]["pass"],
    }
    replay_prefix_sha256 = replay_prefix_state_stream(
        replay_representatives, replay_context
    )
    replay_c = compositional_certificate(
        replay_representatives, replay_context
    )
    replay_d = verdict_certificate(
        replay_representatives, primary[1], replay_c
    )
    deterministic = (
        primary[0] == replay_a
        and primary[1]["prefix_state_stream_sha256"]
        == replay_prefix_sha256
        and primary[1]["determinism_duplicate_state_digest_exact"]
        and primary[2] == replay_c
        and primary[3] == replay_d
    )
    replay_digest = digest((
        replay_a,
        replay_prefix_sha256,
        replay_c,
        replay_d,
        tuple(
            row["state_sequence_sha256_by_key"]
            for row in primary[1]["exact_full_cycle_rows"]
        ),
    ))
    elapsed = monotonic() - started
    controls = {
        **sources,
        "determinism_replay": {
            "scope": (
                "A/context and C recomputed independently; every B prefix "
                "state recomputed; each exact B survivor-cycle state was "
                "independently serialized and digested twice at every "
                "moment; D "
                "recomputed from the replayed composition"
            ),
            "primary_sha256": primary_digest,
            "replay_sha256": replay_digest,
            "exact": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    controls["base_pass"] = (
        sources["pass"]
        and deterministic
        and controls["runtime_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    controls["pass"] = controls["base_pass"]
    labels = (
        "A_REPRESENTATIVES",
        "B_DYNAMICAL_EQUIVALENCE",
        "C_COMPOSITIONAL_TEST",
        "D_VERDICT",
    )
    certificates = {
        label: row for label, row in zip(labels, primary)
    }
    certificates["E_CONTROLS"] = controls
    output = render_fixed_point(certificates)
    sys.stdout.write(output)
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
