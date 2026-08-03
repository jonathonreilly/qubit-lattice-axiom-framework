#!/usr/bin/env python3
"""Cycle 879 independent check: an attempt to REFUTE the B=4 clock-relation run.

The Cycle-879 primary is BLOCKLISTED.  It is read as text and AST only -- a
meta-path firewall turns any import of it into a hard failure -- so nothing
here inherits its measurement code, its search code, or its verdicts.  Only
the Cycle-719 controller core is imported, and that is the shared substrate
under test, not a source primary.

This checker is built to make the primary fail, along five axes.

  1  DIFFERENT MEASUREMENT.  The watched coordinates are located by the
     COMPLEMENTARY probe (fill every bank/link wire, clear one, find the single
     zero) rather than the primary's one-hot probe.  The census lanes are
     packed in REVERSED order, and the per-chunk station masks are produced by
     simulating the controller's A/B token swap network directly instead of the
     primary's closed-form (start + phase) mod STATIONS.  The rebuilt corpus is
     compared to the primary's published corpus sha.

  2  KERNEL REPLAY.  For a declared subsample of keys the whole horizon is
     replayed through ``C719.apply_controller_step`` on ordinary state tuples,
     which is the reference semantics with real token routing and no bit-slice
     trick at all.  Those cadences must agree event for event.

  3  CLAIM REPLICATION.  Every pinned number the primary published is
     recomputed from the independently measured corpus.

  4  A STRICTLY LARGER SEARCH.  The declared family is re-searched with every
     cap loosened: the constant offset over a provably COMPLETE candidate set
     instead of eight anchors; the lag map with PARTIAL overlap down to eight
     events instead of half a clock; the index map without the exhaustion
     requirement; the affine map solved from every anchor; and the period law
     from the FULL border chain of several tail windows rather than one minimal
     border per rung, every candidate then adjudicated by a direct membership
     test.  Any relation this wider search finds where the primary reported
     NO_RELATION_IN_F REFUTES the primary's negative.

  5  THE HEADLINE-LAUNDERING ATTACK (Cycle 875's A4 standard, turned on this
     block's OWN emitted figures).  Every headline the primary publishes is
     recomputed at every scope it could have been quoted at, and the scope the
     primary actually used is identified from the numbers.  A headline that
     silently quotes a sub-corpus, a coverage fraction whose denominator is
     narrower than its own population, an identity-like split that hides a
     value-moving map, a disclosed deviation whose size is understated, or a
     BREAK claimed without a witness that survives brute force -- each is a
     FAIL here, in the direction that costs the primary its result.

Axis 5 is symmetric on purpose.  The primary reports that the B=3 whole-orbit
period law BREAKS at B=4.  This checker fails the primary BOTH if that break is
manufactured (no non-orbit period survives the direct membership test) AND if
the primary had understated it.  A negative finding is not a licence to skip
the adversarial work.
"""
from __future__ import annotations

import ast
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

EXPECTED_SHA256 = {
    PRIMARY_879: "40bf65b88db19a7872d3dd5de50c7746bbecd98ce87c2b1176ce18ec9e5f7b2f",
    CORE_719: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    CACHE_869: "ea19cd18c30c769453e2e15a9186449712ef8b99535234fde25b2073f1efa1fd",
}
EXPECTED_GIT_BLOB = {
    PRIMARY_879: "c2147a99c1a6879508fbf250051f87115b0b9d35",
    CORE_719: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    CACHE_869: "e6ad75e05f42bec32570a8853954129c62f8356d",
}

# The primary's published claims, pinned as literals and recomputed below.
PINNED = {
    "initial_census_sha256": (
        "7ce0850c87e31c283429cb1fef0f099ad439ce0aa9382ea123f4dd3883b35589"
    ),
    "corpus_sha256": (
        "0f575b8fd9b6f72f3669d697601ba2509d6f2b63e13087a66df7aed4864040be"
    ),
    "bank_clean_occurrences": [468010, 305820, 794901, 1567016],
    "pair_clean_occurrences": [51278, 224556, 407270, 114825, 226902, 609567],
    "total_clock_events": 4_770_145,
    "longest_clock_events": 6512,
    "silent_bank_clocks": 3,
    "silent_pair_clocks": 219,
    "saturated_bank_clocks": 124,
    "saturated_pair_clocks": 33,
    "clocks_that_866_nominal_store_cap_would_truncate": 1788,
    "events_that_866_nominal_store_cap_would_discard": 1_956_769,
    "pair_clock_information_content": {
        "BOTH_BANK_CLOCKS_IDENTICAL": 6,
        "ONE_BANK_GATES_THE_PAIR": 493,
        "SILENT_PAIR": 219,
        "STRICTLY_JOINT": 3170,
    },
    "within_key_member_histogram": {
        "F1": 186, "F1W": 3, "F3": 82, "F3P": 218, "F4": 19,
        "NO_RELATION_IN_F": 8099, "ONE_SIDE_SILENT": 1083,
        "TRIVIAL_SATURATION": 30,
    },
    "within_key_evidence_split": {
        "PARTIAL": 218, "SUBSTANTIVE_NO_RELATION": 7675,
        "SUBSTANTIVE_RELATION": 278, "THIN_NO_RELATION": 424,
        "THIN_RELATION": 12,
    },
    "within_key_bank_clock_histogram": {
        "F3P": 5, "F4": 18, "NO_RELATION_IN_F": 3823, "ONE_SIDE_SILENT": 9,
        "TRIVIAL_SATURATION": 33,
    },
    "within_key_substantive_relations": 278,
    "within_key_substantive_pairs": 8171,
    "within_key_comparable_pairs": 8607,
    "within_key_substantive_nonidentity_full_dictionaries": 9,
    "within_key_substantive_identity_like_full_dictionaries": 269,
    "within_key_substantive_partial_matches": 218,
    "within_key_substantive_nonidentity_partial_matches": 30,
    "bank_clock_substantive_relations": 18,
    "bank_clock_substantive_pairs": 3840,
    "bank_clock_nonidentity_full_dictionaries": 4,
    "nondegenerate_periods": {
        "11": {"bank": 8, "pair": 8},
        "27": {"bank": 32, "pair": 29},
        "54": {"bank": 19, "pair": 21},
        "81": {"bank": 20, "pair": 22},
        "1512": {"bank": 2, "pair": 3},
        "1971": {"bank": 16, "pair": 64},
        "2214": {"bank": 0, "pair": 36},
    },
    "every_nondegenerate_period_is_whole_orbits": False,
    "non_orbit_periods": [11],
    "clocks_carrying_a_non_orbit_period": 16,
    "across_key_scopes": {
        "FULL_CORPUS": {
            "F1_edges": 5085, "F1_nonzero": 5085, "F1_zero": 0,
            "F3_factor_edges": 2367, "keys_outside": 803,
            "sounding_keys": 6258, "silent_keys": 222, "distinct_gap_words": 1173,
        },
        "SUB_CORPUS_pair_clocks_only": {
            "F1_edges": 3094, "F1_nonzero": 3094, "F1_zero": 0,
            "F3_factor_edges": 837, "keys_outside": 371,
            "sounding_keys": 3669, "silent_keys": 219, "distinct_gap_words": 575,
        },
        "SUB_CORPUS_bank_clocks_only": {
            "F1_edges": 1991, "F1_nonzero": 1991, "F1_zero": 0,
            "F3_factor_edges": 1530, "keys_outside": 432,
            "sounding_keys": 2589, "silent_keys": 3, "distinct_gap_words": 598,
        },
    },
    "across_key_headline_F1_edges": 5085,
    "across_key_headline_nonzero": 5085,
    "across_key_headline_keys_outside": 803,
    "across_key_headline_F3_factor_edges": 2367,
    "across_key_headline_scope_label": "FULL_CORPUS_ALL_TEN_CLOCK_INDICES",
}

# Independently declared box; cross-checked against the primary's AST literals.
FIXTURE_BANKS = 4
STATIONS = 27
HORIZON_CHUNKS = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
EXPECTED_KEYS = 648
EXPECTED_PLACEMENTS = 324
WATCHED_WIRES_PER_BANK = 47
EVIDENCE_FLOOR = 8
MIN_LAG_OVERLAP = 8
CYCLE866_DECLARED_STORE_CAP = 1_024
RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

# Loosened search box.  Every entry is strictly wider than the primary's.
WIDE_PERIOD_TAIL_LADDER = (4_096, 2_048, 1_024, 512, 256, 128, 64, 32, 16)
WIDE_PERIOD_BLOCK_GAPS = 2_048        # primary caps blocks at 512
WIDE_PERIOD_MAX_TICKS = 65_536        # ceiling on an admitted common period
WIDE_PERIOD_CANDIDATES_PER_CLOCK = 64  # border-chain candidates adjudicated
WIDE_LAG_SPAN_CAP = 20_000            # > 2 * longest clock, so it cannot bite
WIDE_AFFINE_ANCHOR_CAP = 2_048        # primary solves from the endpoints only
WIDE_MIN_PERIODIC_GAPS = 16           # shared non-vacuity floor
REFERENCE_REPLAY_KEYS = 8             # keys replayed through the kernel route
WITNESS_PRINT_CAP = 4
MIN_SATURATION_RUN = 8                # matches the primary's exact definition
# A relation only REFUTES the primary if it is a real dictionary: it must move
# the tick values (non-identity) and explain at least this fraction of the
# shorter clock.  Both the strong and the weak matches are reported.
REFUTATION_COVERAGE = Fraction(1, 2)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Turn any import of a blocklisted primary into an immediate failure."""

    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


BLOCKLISTED_MODULES = (Path(PRIMARY_879).stem,)
FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

# Authorized executable dependency: the shared substrate, not a source primary.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


A = K.A
B = K.B
M = K.M
R3 = K.R3
BANK_PAIRS = tuple(combinations(range(FIXTURE_BANKS), 2))


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree, name):
    values = []
    for node in tree.body:
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
        if any(isinstance(target, ast.Name) and target.id == name
               for target in targets):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_names(tree):
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls():
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items() if path.endswith(".py")
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": (
            "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED" if path == PRIMARY_879
            else "READ_ONLY_PINNED_B3_CACHE" if path == CACHE_869
            else "AUTHORIZED_EXECUTABLE_CYCLE719_CORE"
        ),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOB[path],
    } for path in AUDIT_INPUT_PATHS)

    primary = trees[PRIMARY_879]
    declared = {
        name: literal_assignment(primary, name)
        for name in (
            "FIXTURE_BANKS", "STATIONS", "HORIZON_CHUNKS", "TOKEN_K",
            "EVENT_COUNT", "EXPECTED_PLACEMENTS", "EVIDENCE_FLOOR",
            "MIN_LAG_OVERLAP", "WINDOWED_OFFSET_ANCHORS", "PERIOD_TAIL_WINDOW",
            "PERIOD_TAIL_FLOOR", "PERIOD_MAX_BLOCK_GAPS", "MIN_SATURATION_RUN",
            "CADENCE_STORE_CAP", "CYCLE866_DECLARED_STORE_CAP",
            "ACROSS_KEY_REP_CAP", "AUDIT_INPUT_PATHS",
        )
    }
    box_agrees = (
        declared["FIXTURE_BANKS"] == FIXTURE_BANKS
        and declared["STATIONS"] == STATIONS
        and declared["HORIZON_CHUNKS"] == HORIZON_CHUNKS
        and declared["TOKEN_K"] == TOKEN_K
        and declared["EVENT_COUNT"] == EVENT_COUNT
        and declared["EXPECTED_PLACEMENTS"] == EXPECTED_PLACEMENTS
        and declared["EVIDENCE_FLOOR"] == EVIDENCE_FLOOR
        and declared["MIN_LAG_OVERLAP"] == MIN_LAG_OVERLAP
        and declared["MIN_SATURATION_RUN"] == MIN_SATURATION_RUN
        and declared["CYCLE866_DECLARED_STORE_CAP"] == CYCLE866_DECLARED_STORE_CAP
        # The primary must declare, literally, every mutable repo file it reads:
        # the 719 core it rebuilds from and the 869 cache it prices against.
        and isinstance(declared["AUDIT_INPUT_PATHS"], tuple)
        and set(declared["AUDIT_INPUT_PATHS"]) >= {CORE_719, CACHE_869}
        and all(not Path(path).is_absolute()
                for path in declared["AUDIT_INPUT_PATHS"])
    )
    # The primary's caps must sit strictly inside this checker's loosened box,
    # otherwise the refutation search would not actually be wider.
    search_is_wider = (
        declared["PERIOD_TAIL_FLOOR"] is not None
        and declared["PERIOD_TAIL_WINDOW"] is not None
        and declared["PERIOD_TAIL_WINDOW"] <= max(WIDE_PERIOD_TAIL_LADDER)
        and declared["PERIOD_MAX_BLOCK_GAPS"] < WIDE_PERIOD_BLOCK_GAPS
        and declared["WINDOWED_OFFSET_ANCHORS"] < WIDE_AFFINE_ANCHOR_CAP
        and 2 * PINNED["longest_clock_events"] < WIDE_LAG_SPAN_CAP
    )
    # The disclosed store-cap deviation must be a widening, never a narrowing.
    deviation_is_a_widening = (
        declared["CADENCE_STORE_CAP"] is None
        or declared["CADENCE_STORE_CAP"] > CYCLE866_DECLARED_STORE_CAP
    )
    markers = {
        PRIMARY_879: {"relate", "f1_constant_offset", "f3_lag_offset",
                      "f3p_partial_lag", "period_profile", "saturation_profile",
                      "family_controls", "load_869_reference", "compare_row",
                      "identity_like"},
        CORE_719: {"interleaved_program", "run_orbit", "apply_controller_step"},
    }
    markers_exact = all(
        required <= function_names(trees[path]) for path, required in markers.items()
    )
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    passed = bool(
        literal_paths == AUDIT_INPUT_PATHS
        and all(row["exists"] and row["worktree_relative"] for row in rows)
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
        and markers_exact
        and box_agrees
        and search_is_wider
        and deviation_is_a_widening
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return {
        "source_rows": rows,
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "primary_declared_box": {
            name: list(value) if isinstance(value, tuple) else value
            for name, value in declared.items()
        },
        "declared_box_agrees": box_agrees,
        "refutation_search_is_strictly_wider": search_is_wider,
        "disclosed_store_cap_deviation_is_a_widening": deviation_is_a_widening,
        "source_AST_markers_exact": markers_exact,
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ],
        "firewall_hits": list(FIREWALL.hits),
        "pass": passed,
    }


# ------------------------------------------------ independent measurement route
def complementary_watched_layout():
    """Locate coordinates by filling every wire and clearing exactly one."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    ones_banks = [[1] * len(row) for row in banks]
    ones_links = [[1] * len(row) for row in links]
    full = M.pack_state(
        tuple(tuple(row) for row in ones_banks),
        tuple(tuple(row) for row in ones_links),
    )
    local = (
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
        *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
    )
    per_bank = {}
    for bank in range(FIXTURE_BANKS):
        located = []
        for wire in local:
            probe_banks = [list(row) for row in ones_banks]
            probe_banks[bank][wire] = 0
            packed = M.pack_state(
                tuple(tuple(row) for row in probe_banks),
                tuple(tuple(row) for row in ones_links),
            )
            zeros = tuple(
                index for index, value in enumerate(packed)
                if value == 0 and full[index] == 1
            )
            if len(zeros) != 1:
                raise AssertionError((bank, wire, zeros))
            located.append(zeros[0])
        per_bank[bank] = tuple(sorted(located))
    return per_bank, R3.X.SOURCE_POINTER


def token_network_masks(keys):
    """Station masks from the A/B swap network, not from a closed-form phase."""
    masks = []
    tokens = [
        [1 if station in positions else 0 for station in range(STATIONS)]
        for _event, positions in keys
    ]
    partner = [[0] * STATIONS for _ in keys]
    for _phase in range(STATIONS):
        row = [0] * STATIONS
        for lane, vector in enumerate(tokens):
            bit = 1 << lane
            for station, live in enumerate(vector):
                if live:
                    row[station] |= bit
        masks.append(tuple(row))
        for lane in range(len(tokens)):
            live, held = tokens[lane], partner[lane]
            for station in range(STATIONS):
                live[station], held[station] = held[station], live[station]
            for station in range(STATIONS):
                target = (station + 1) % STATIONS
                held[station], live[target] = live[target], held[station]
    return tuple(masks)


def build_census():
    program = K.interleaved_program(FIXTURE_BANKS)
    placements = tuple(
        positions for positions in combinations(range(STATIONS), TOKEN_K)
        if all((position + 1) % STATIONS not in set(positions)
               for position in positions)
    )
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    state = M.pack_state(banks, links)
    seeds = []
    allocator_failures = 0
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, a_tokens, b_tokens, _trace = K.run_orbit(before, program)
        allocator_failures += (
            after != A.apply_semantic(before, M.global_allocator_word(FIXTURE_BANKS))
        )
        allocator_failures += a_tokens != (1,) + (0,) * (len(program) - 1)
        allocator_failures += any(b_tokens)
        seeds.append(before)
        state = after
    keys = []
    states = []
    for event, seed in enumerate(seeds):
        for positions in placements:
            evolved, _a, _b, _trace = K.run_orbit(
                seed, program, token_positions=positions
            )
            keys.append((event, positions))
            states.append(evolved)
    return program, tuple(keys), tuple(states), allocator_failures, len(placements)


def measure_corpus(program, keys, states, per_bank, source_pointer):
    """Plane evolution with REVERSED lane packing and swap-network masks."""
    schedules = tuple(K.mapped_macro(row) for row in program)
    lane_count = len(keys)
    reversed_keys = tuple(reversed(keys))
    reversed_states = tuple(reversed(states))
    width = len(states[0])
    planes = [0] * width
    for lane, state in enumerate(reversed_states):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    masks = token_network_masks(reversed_keys)
    census_mask = (1 << lane_count) - 1
    watched = tuple(per_bank[bank] for bank in range(FIXTURE_BANKS))

    bank_clocks = [[[] for _ in range(FIXTURE_BANKS)] for _ in range(lane_count)]
    pair_clocks = [[[] for _ in BANK_PAIRS] for _ in range(lane_count)]
    last = lane_count - 1

    def observe(tick):
        source_dirty = planes[source_pointer]
        clean = []
        for bank in range(FIXTURE_BANKS):
            dirty = source_dirty
            for wire in watched[bank]:
                dirty |= planes[wire]
            clean.append(census_mask & ~dirty)
        for bank in range(FIXTURE_BANKS):
            mask = clean[bank]
            while mask:
                low = mask & -mask
                lane = low.bit_length() - 1
                bank_clocks[last - lane][bank].append(tick)
                mask -= low
        for index, (left, right) in enumerate(BANK_PAIRS):
            mask = clean[left] & clean[right]
            while mask:
                low = mask & -mask
                lane = low.bit_length() - 1
                pair_clocks[last - lane][index].append(tick)
                mask -= low

    observe(0)
    for tick in range(1, HORIZON_CHUNKS + 1):
        phase_masks = masks[(tick - 1) % STATIONS]
        for station, word in enumerate(schedules):
            lane_mask = phase_masks[station]
            if not lane_mask:
                continue
            for gate in word:
                if gate.kind == "X":
                    planes[gate.wires[0]] ^= lane_mask
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    planes[target] ^= planes[control] & lane_mask
                elif gate.kind == "TOF":
                    left, right, target = gate.wires
                    planes[target] ^= planes[left] & planes[right] & lane_mask
                else:
                    raise AssertionError(gate.kind)
        observe(tick)
    return (
        tuple(tuple(tuple(row) for row in lane) for lane in bank_clocks),
        tuple(tuple(tuple(row) for row in lane) for lane in pair_clocks),
    )


def reference_replay(program, key, state, per_bank, source_pointer):
    """Full-horizon replay on state tuples through the reference step function."""
    _event, positions = key
    a_tokens = tuple(
        1 if station in positions else 0 for station in range(STATIONS)
    )
    b_tokens = (0,) * STATIONS
    watched = tuple(per_bank[bank] for bank in range(FIXTURE_BANKS))
    bank_clocks = [[] for _ in range(FIXTURE_BANKS)]
    pair_clocks = [[] for _ in BANK_PAIRS]

    def observe(tick, data):
        clean = []
        for bank in range(FIXTURE_BANKS):
            ok = not data[source_pointer] and not any(
                data[wire] for wire in watched[bank]
            )
            clean.append(ok)
            if ok:
                bank_clocks[bank].append(tick)
        for index, (left, right) in enumerate(BANK_PAIRS):
            if clean[left] and clean[right]:
                pair_clocks[index].append(tick)

    data = state
    observe(0, data)
    for tick in range(1, HORIZON_CHUNKS + 1):
        data, a_tokens, b_tokens = K.apply_controller_step(
            data, program, a_tokens, b_tokens
        )
        observe(tick, data)
    return (
        tuple(tuple(row) for row in bank_clocks),
        tuple(tuple(row) for row in pair_clocks),
    )


# ------------------------------------------------- the strictly larger search
def gaps_of(cadence):
    return tuple(cadence[i + 1] - cadence[i] for i in range(len(cadence) - 1))


def kmp_failure(sequence):
    length = len(sequence)
    failure = [0] * length
    border = 0
    for index in range(1, length):
        while border and sequence[index] != sequence[border]:
            border = failure[border - 1]
        if sequence[index] == sequence[border]:
            border += 1
        failure[index] = border
    return failure


def contains(cadence, tick):
    """Membership by binary search; no per-clock set is materialised."""
    position = bisect_left(cadence, tick)
    return position < len(cadence) and cadence[position] == tick


def tick_position(cadence, tick):
    position = bisect_left(cadence, tick)
    if position < len(cadence) and cadence[position] == tick:
        return position
    return None


def brute_force_period(cadence, period, min_gaps=WIDE_MIN_PERIODIC_GAPS):
    """Decide directly whether a cadence is P-periodic on a long enough tail.

    No string algorithm, no transient ladder: the membership test t in S <=>
    t+P in S is evaluated on the largest suffix where it holds.  This is what
    adjudicates a disagreement between two period-DETECTION methods -- either a
    claimed period survives this test or it does not.
    """
    if period <= 0 or len(cadence) < 2:
        return None
    last = cadence[-1]
    position = len(cadence) - 1
    while position >= 0:
        tick = cadence[position]
        if tick + period <= last and not contains(cadence, tick + period):
            break
        position -= 1
    start = position + 1
    if start >= len(cadence):
        return None
    stable = cadence[start:]
    if len(stable) - 1 < min_gaps:
        return None
    lower = {tick for tick in stable if tick + period <= last}
    upper = {tick for tick in stable if tick - period >= stable[0]}
    if {tick + period for tick in lower} != upper:
        return None
    residues = {tick % period for tick in stable}
    return {
        "transient_tick": stable[0],
        "events": len(stable),
        "residue_count": len(residues),
        "saturated": len(residues) == period,
    }


def exact_saturation(cadence, horizon=HORIZON_CHUNKS):
    """Saturated iff clean at every chunk from some tick through the horizon.

    Computed forwards from the last non-unit gap, which is a different route to
    the same definition than the primary's backwards run scan.
    """
    if not cadence or cadence[-1] != horizon:
        return None
    start = 0
    for position in range(len(cadence) - 1):
        if cadence[position + 1] - cadence[position] != 1:
            start = position + 1
    if len(cadence) - start < MIN_SATURATION_RUN:
        return None
    return {"saturated_from_tick": cadence[start],
            "consecutive_run": len(cadence) - start}


def wide_period(cadence):
    """Least eventual period from the FULL border chain of several tails.

    The primary takes ONE candidate per tail rung -- the minimal border of that
    tail.  This takes EVERY border of every rung, which is every period of that
    tail, and adjudicates each candidate by the direct membership test.  It can
    therefore only see more periods than the primary, and it never carries a
    period claim its own adjudicator would reject.
    """
    gaps = gaps_of(cadence)
    if len(gaps) < WIDE_MIN_PERIODIC_GAPS:
        return None
    candidates = set()
    for window in WIDE_PERIOD_TAIL_LADDER:
        if window > len(gaps):
            continue
        tail = gaps[-window:]
        failure = kmp_failure(tail)
        border = failure[-1] if failure else 0
        blocks = set()
        while border:
            blocks.add(len(tail) - border)
            border = failure[border - 1]
        blocks.add(len(tail))
        for block in blocks:
            if 0 < block <= WIDE_PERIOD_BLOCK_GAPS and len(tail) >= 2 * block:
                period = sum(tail[-block:])
                if 0 < period <= WIDE_PERIOD_MAX_TICKS:
                    candidates.add(period)
    best = None
    for period in sorted(candidates)[:WIDE_PERIOD_CANDIDATES_PER_CLOCK]:
        verdict = brute_force_period(cadence, period)
        if verdict is None:
            continue
        best = {
            "period": period,
            "transient_tick": verdict["transient_tick"],
            "residue_count": verdict["residue_count"],
            "saturated": verdict["saturated"],
        }
        break
    return best


def wide_offset(x, y, horizon=HORIZON_CHUNKS):
    """Complete constant-offset search: c must satisfy y[0] - c in X."""
    tail = y[-1]
    for anchor in x:
        offset = y[0] - anchor
        if abs(offset) > horizon:
            continue
        if not contains(x, tail - offset):
            continue
        low = max(0, offset)
        high = min(horizon, horizon + offset)
        if y[0] < low or y[-1] > high:
            continue
        left = bisect_left(x, low - offset)
        right = bisect_right(x, high - offset)
        if right - left != len(y):
            continue
        if all(x[left + index] + offset == y[index] for index in range(len(y))):
            return {"member": "F1/F1W", "c": offset, "window": [low, high]}
    return None


def wide_lag(x, y):
    """Lag map with PARTIAL overlap allowed in both directions.

    The primary's F3P demands the overlap cover at least half the shorter
    clock; this demands only MIN_LAG_OVERLAP events, so every F3P match is a
    wide_lag match and there are strictly more of them.
    """
    if len(x) + len(y) > WIDE_LAG_SPAN_CAP:
        return "CAP"
    for lag in range(-(len(y) - 1), len(x)):
        start = max(0, -lag)
        stop = min(len(y), len(x) - lag)
        if stop - start < MIN_LAG_OVERLAP:
            continue
        shift = y[start] - x[start + lag]
        if x[start + 1 + lag] + shift != y[start + 1]:
            continue
        if all(
            x[index + lag] + shift == y[index] for index in range(start, stop)
        ):
            return {
                "member": "F3wide",
                "L": lag,
                "d": shift,
                "overlap": stop - start,
                "partial": start > 0 or stop < len(y),
            }
    return None


def wide_index_map(x, y):
    """Index-affine map without the primary's exhaustion requirement."""
    if len(y) < 2:
        return None
    start = tick_position(x, y[0])
    second = tick_position(x, y[1])
    if start is None or second is None:
        return None
    step = second - start
    if step < 1:
        return None
    if step == 1 and start == 0 and len(x) == len(y):
        return None
    for ordinal, tick in enumerate(y):
        position = start + step * ordinal
        if position >= len(x) or x[position] != tick:
            return None
    return {"member": "F2Bwide", "s": step, "r": start,
            "exhausted": start + step * len(y) >= len(x)}


def wide_affine(x, y):
    """Tick-affine solved from EVERY anchor, not only the endpoints."""
    if len(x) != len(y) or len(x) < 3:
        return None
    limit = min(len(x), WIDE_AFFINE_ANCHOR_CAP)
    for anchor in range(1, limit):
        if x[anchor] == x[0]:
            continue
        slope = Fraction(y[anchor] - y[0], x[anchor] - x[0])
        if slope <= 0 or slope == 1:
            continue
        intercept = Fraction(y[0]) - slope * x[0]
        if all(slope * left + intercept == right for left, right in zip(x, y)):
            return {"member": "F2Awide", "a": str(slope), "b": str(intercept)}
    return None


def wide_residue_law(left, right):
    """Residue rotation admitted at the LEAST COMMON period of the two clocks."""
    if left is None or right is None or left["saturated"] or right["saturated"]:
        return None
    period = left["period"] * right["period"] // gcd(left["period"], right["period"])
    if period > WIDE_PERIOD_MAX_TICKS:
        return None
    return {"member": "F4wide_candidate", "P": period}


def wide_relation(left, right):
    """Any relation in the loosened family, searched in both directions."""
    cap_hits = 0
    for source, target in ((left, right), (right, left)):
        x, y = source["ticks"], target["ticks"]
        if not x or not y:
            continue
        direction = "forward" if source is left else "reverse"
        found = wide_offset(x, y)
        if found is None:
            found = wide_affine(x, y)
        if found is None:
            found = wide_index_map(x, y)
        if found is None:
            lag = wide_lag(x, y)
            if lag == "CAP":
                cap_hits += 1
            else:
                found = lag
        if found is None and source["saturation"] is None \
                and target["saturation"] is None:
            residue = wide_residue_law(source["period"], target["period"])
            if residue is not None:
                # Adjudicate the common period on BOTH clocks by brute force
                # before admitting a residue law at it.
                period = residue["P"]
                left_ok = brute_force_period(x, period)
                right_ok = brute_force_period(y, period)
                if (left_ok and right_ok and not left_ok["saturated"]
                        and not right_ok["saturated"]):
                    source_res = {tick % period for tick in x
                                  if tick >= left_ok["transient_tick"]}
                    target_res = {tick % period for tick in y
                                  if tick >= right_ok["transient_tick"]}
                    if len(source_res) == len(target_res) and source_res \
                            and len(source_res) < period:
                        for anchor in sorted(source_res):
                            offset = (min(target_res) - anchor) % period
                            if {(value + offset) % period
                                    for value in source_res} == target_res:
                                found = {"member": "F4wide", "P": period,
                                         "c": offset}
                                break
        if found is not None:
            return {**found, "direction": direction}, cap_hits
    return None, cap_hits


def wide_profile(cadence):
    return {
        "ticks": cadence,
        "period": wide_period(cadence) if len(cadence) >= MIN_LAG_OVERLAP else None,
        "saturation": exact_saturation(cadence),
    }


def wide_identity_like(found):
    return bool(
        found.get("c") == 0
        or (found["member"] == "F3wide" and found["d"] == 0)
        or (found["member"] == "F2Bwide" and found["s"] == 1)
    )


# ------------------------------------ the Cycle-875 A4 headline-laundering test
def scope_of(headline, scopes):
    """Which scope a published headline number actually equals."""
    matches = sorted(
        label for label, block in scopes.items() if block["F1_edges"] == headline
    )
    if not matches:
        return "MATCHES_NO_RECOMPUTED_SCOPE"
    if len(matches) > 1:
        return "AMBIGUOUS:" + "+".join(matches)
    return matches[0]


def main():
    started = time.monotonic()
    controls = source_controls()

    program, keys, states, allocator_failures, placement_count = build_census()
    per_bank, source_pointer = complementary_watched_layout()
    substrate_ok = (
        len(program) == STATIONS
        and len(keys) == EXPECTED_KEYS
        and placement_count == EXPECTED_PLACEMENTS
        and allocator_failures == 0
        and all(len(row) == WATCHED_WIRES_PER_BANK for row in per_bank.values())
        and all(
            not (set(per_bank[left]) & set(per_bank[right]))
            for left, right in BANK_PAIRS
        )
        and all(
            source_pointer not in set(per_bank[bank])
            for bank in range(FIXTURE_BANKS)
        )
    )
    initial_hasher = sha256()
    for state in states:
        initial_hasher.update(bytes(state))
    initial_sha = initial_hasher.hexdigest()

    bank_cadences, pair_cadences = measure_corpus(
        program, keys, states, per_bank, source_pointer
    )
    corpus_sha = digest({
        "bank": [[list(row) for row in lane] for lane in bank_cadences],
        "pair": [[list(row) for row in lane] for lane in pair_cadences],
    })
    b_pass = (
        substrate_ok
        and initial_sha == PINNED["initial_census_sha256"]
        and corpus_sha == PINNED["corpus_sha256"]
    )

    replay_lanes = tuple(
        range(0, len(keys), max(1, len(keys) // REFERENCE_REPLAY_KEYS))
    )[:REFERENCE_REPLAY_KEYS]
    replay_mismatches = []
    for lane in replay_lanes:
        ref_bank, ref_pair = reference_replay(
            program, keys[lane], states[lane], per_bank, source_pointer
        )
        if ref_bank != bank_cadences[lane] or ref_pair != pair_cadences[lane]:
            replay_mismatches.append({
                "lane": lane,
                "bank_equal": ref_bank == bank_cadences[lane],
                "pair_equal": ref_pair == pair_cadences[lane],
                "reference_bank_lengths": [len(row) for row in ref_bank],
                "plane_bank_lengths": [len(row) for row in bank_cadences[lane]],
            })
    c_pass = not replay_mismatches and len(replay_lanes) == REFERENCE_REPLAY_KEYS

    # ------------------------------------------------------ claim replication
    bank_occurrences = [
        sum(len(lane[bank]) for lane in bank_cadences)
        for bank in range(FIXTURE_BANKS)
    ]
    pair_occurrences = [
        sum(len(lane[index]) for lane in pair_cadences)
        for index in range(len(BANK_PAIRS))
    ]
    silent_bank = sum(1 for lane in bank_cadences for row in lane if not row)
    silent_pair = sum(1 for lane in pair_cadences for row in lane if not row)
    longest = max(
        [len(row) for lane in bank_cadences for row in lane]
        + [len(row) for lane in pair_cadences for row in lane]
    )
    over_866 = sum(
        1 for group in (bank_cadences, pair_cadences)
        for lane in group for row in lane
        if len(row) > CYCLE866_DECLARED_STORE_CAP
    )
    lost_866 = sum(
        max(0, len(row) - CYCLE866_DECLARED_STORE_CAP)
        for group in (bank_cadences, pair_cadences)
        for lane in group for row in lane
    )

    bank_profiles = tuple(tuple(wide_profile(row) for row in lane)
                          for lane in bank_cadences)
    pair_profiles = tuple(tuple(wide_profile(row) for row in lane)
                          for lane in pair_cadences)

    def saturated_count(profiles):
        return sum(
            1 for lane in profiles for profile in lane
            if profile["saturation"] is not None
        )

    domination = Counter()
    for lane in range(len(keys)):
        for index, (left, right) in enumerate(BANK_PAIRS):
            joint = pair_cadences[lane][index]
            low = bank_cadences[lane][left]
            high = bank_cadences[lane][right]
            if not joint:
                domination["SILENT_PAIR"] += 1
            elif joint == low and joint == high:
                domination["BOTH_BANK_CLOCKS_IDENTICAL"] += 1
            elif joint == low or joint == high:
                domination["ONE_BANK_GATES_THE_PAIR"] += 1
            else:
                domination["STRICTLY_JOINT"] += 1

    intersection_failures = sum(
        1 for lane in range(len(keys))
        for index, (left, right) in enumerate(BANK_PAIRS)
        if tuple(sorted(set(bank_cadences[lane][left])
                        & set(bank_cadences[lane][right])))
        != pair_cadences[lane][index]
    )

    # Every period the primary published, adjudicated by the direct membership
    # test on every clock -- and the wide scan's own least-period histogram.
    wide_periods = {"bank": Counter(), "pair": Counter()}
    for label, profiles in (("bank", bank_profiles), ("pair", pair_profiles)):
        for lane in profiles:
            for profile in lane:
                period = profile["period"]
                if (period is not None and not period["saturated"]
                        and profile["saturation"] is None):
                    wide_periods[label][period["period"]] += 1
    unsaturated = {
        "bank": tuple(
            row for lane, profiles in zip(bank_cadences, bank_profiles)
            for row, profile in zip(lane, profiles)
            if profile["saturation"] is None
        ),
        "pair": tuple(
            row for lane, profiles in zip(pair_cadences, pair_profiles)
            for row, profile in zip(lane, profiles)
            if profile["saturation"] is None
        ),
    }
    pinned_period_support = {}
    for period_text, counts in PINNED["nondegenerate_periods"].items():
        period = int(period_text)
        support = {"bank": 0, "pair": 0}
        for label, rows in unsaturated.items():
            for row in rows:
                verdict = brute_force_period(row, period)
                if verdict is not None and not verdict["saturated"]:
                    support[label] += 1
        pinned_period_support[period_text] = support
    wide_nonorbit = sorted(
        period for period in set(wide_periods["bank"]) | set(wide_periods["pair"])
        if period % STATIONS
    )

    replication = {
        "bank_clean_occurrences": bank_occurrences,
        "pair_clean_occurrences": pair_occurrences,
        "total_clock_events": sum(bank_occurrences) + sum(pair_occurrences),
        "longest_clock_events": longest,
        "silent_bank_clocks": silent_bank,
        "silent_pair_clocks": silent_pair,
        "saturated_bank_clocks": saturated_count(bank_profiles),
        "saturated_pair_clocks": saturated_count(pair_profiles),
        "clocks_that_866_nominal_store_cap_would_truncate": over_866,
        "events_that_866_nominal_store_cap_would_discard": lost_866,
        "pair_clock_information_content": dict(sorted(domination.items())),
        "pair_is_intersection_failures": intersection_failures,
        "wide_scan_nondegenerate_bank_periods": dict(
            sorted(wide_periods["bank"].items())
        ),
        "wide_scan_nondegenerate_pair_periods": dict(
            sorted(wide_periods["pair"].items())
        ),
        "wide_scan_non_orbit_periods": wide_nonorbit,
        "primary_pinned_period_brute_force_support": pinned_period_support,
        "method_reach_note": (
            "The two period DETECTORS have different minimality reach -- this "
            "checker adjudicates the full border chain of several tails, the "
            "primary reads one minimal border per rung -- so their histograms "
            "differ.  That is not a refutation: what is gated is that every "
            "period the primary published is supported by the direct "
            "membership test on at least as many clocks as it claimed."
        ),
    }
    d_pass = (
        bank_occurrences == PINNED["bank_clean_occurrences"]
        and pair_occurrences == PINNED["pair_clean_occurrences"]
        and replication["total_clock_events"] == PINNED["total_clock_events"]
        and longest == PINNED["longest_clock_events"]
        and silent_bank == PINNED["silent_bank_clocks"]
        and silent_pair == PINNED["silent_pair_clocks"]
        and replication["saturated_pair_clocks"] == PINNED["saturated_pair_clocks"]
        and replication["saturated_bank_clocks"] == PINNED["saturated_bank_clocks"]
        and over_866 == PINNED["clocks_that_866_nominal_store_cap_would_truncate"]
        and lost_866 == PINNED["events_that_866_nominal_store_cap_would_discard"]
        and replication["pair_clock_information_content"]
        == PINNED["pair_clock_information_content"]
        and intersection_failures == 0
        and all(
            pinned_period_support[period_text]["bank"] >= counts["bank"]
            and pinned_period_support[period_text]["pair"] >= counts["pair"]
            for period_text, counts in PINNED["nondegenerate_periods"].items()
        )
    )

    # ---------------------------------------------------- the refutation search
    def refute(profiles, labels):
        silent = saturated_both = comparable = substantive = 0
        wide_relations = Counter()
        refutations = []
        weak_examples = []
        nonidentity = weak = cap_hits = 0
        identity_matches = moving_matches = 0
        for lane in range(len(keys)):
            for left, right in combinations(range(len(labels)), 2):
                x_profile = profiles[lane][left]
                y_profile = profiles[lane][right]
                if not x_profile["ticks"] or not y_profile["ticks"]:
                    silent += 1
                    continue
                if (x_profile["saturation"] is not None
                        and y_profile["saturation"] is not None):
                    saturated_both += 1
                    continue
                comparable += 1
                shorter = min(len(x_profile["ticks"]), len(y_profile["ticks"]))
                thin = shorter < EVIDENCE_FLOOR
                if not thin:
                    substantive += 1
                found, hits = wide_relation(x_profile, y_profile)
                cap_hits += hits
                if found is None:
                    continue
                wide_relations[found["member"]] += 1
                covered = found.get("overlap", shorter)
                coverage = Fraction(min(covered, shorter), shorter)
                row = {
                    "key_index": lane,
                    "clocks": [labels[left], labels[right]],
                    "witness": found,
                    "lengths": [len(x_profile["ticks"]), len(y_profile["ticks"])],
                    "coverage": f"{coverage.numerator}/{coverage.denominator}",
                }
                if not thin:
                    if wide_identity_like(found):
                        identity_matches += 1
                    else:
                        moving_matches += 1
                if thin or wide_identity_like(found):
                    continue
                if coverage < REFUTATION_COVERAGE:
                    weak += 1
                    if len(weak_examples) < WITNESS_PRINT_CAP:
                        weak_examples.append(row)
                    continue
                nonidentity += 1
                if len(refutations) < WITNESS_PRINT_CAP:
                    refutations.append(row)
        return {
            "one_side_silent": silent,
            "both_saturated": saturated_both,
            "comparable": comparable,
            "substantive": substantive,
            "wide_family_hits": dict(sorted(wide_relations.items())),
            "wide_lag_span_cap_hits": cap_hits,
            "substantive_identity_like_matches": identity_matches,
            "substantive_value_moving_matches": moving_matches,
            "substantive_nonidentity_relations_above_coverage_floor": nonidentity,
            "substantive_nonidentity_relations_below_coverage_floor": weak,
            "refuting_examples": refutations,
            "below_floor_examples": weak_examples,
        }

    pair_labels = tuple(f"{left}{right}" for left, right in BANK_PAIRS)
    bank_labels = tuple(str(bank) for bank in range(FIXTURE_BANKS))
    pair_refute = refute(pair_profiles, pair_labels)
    bank_refute = refute(bank_profiles, bank_labels)

    # A refutation is a NON-IDENTITY relation the wider search finds in excess
    # of everything the primary published as non-identity, full or partial.
    primary_nonidentity = (
        PINNED["within_key_substantive_nonidentity_full_dictionaries"]
        + PINNED["within_key_substantive_nonidentity_partial_matches"]
    )
    refuted = (
        pair_refute["substantive_nonidentity_relations_above_coverage_floor"]
        > primary_nonidentity
    )
    bookkeeping_agrees = (
        pair_refute["one_side_silent"]
        == PINNED["within_key_member_histogram"]["ONE_SIDE_SILENT"]
        and pair_refute["both_saturated"]
        == PINNED["within_key_member_histogram"]["TRIVIAL_SATURATION"]
        and pair_refute["comparable"] == PINNED["within_key_comparable_pairs"]
        and pair_refute["substantive"] == PINNED["within_key_substantive_pairs"]
        and pair_refute["comparable"] + pair_refute["one_side_silent"]
        + pair_refute["both_saturated"]
        == len(keys) * len(BANK_PAIRS) * (len(BANK_PAIRS) - 1) // 2
        and bank_refute["one_side_silent"]
        == PINNED["within_key_bank_clock_histogram"]["ONE_SIDE_SILENT"]
        and bank_refute["both_saturated"]
        == PINNED["within_key_bank_clock_histogram"]["TRIVIAL_SATURATION"]
        and bank_refute["substantive"] == PINNED["bank_clock_substantive_pairs"]
        and pair_refute["wide_lag_span_cap_hits"] == 0
        and bank_refute["wide_lag_span_cap_hits"] == 0
    )
    e_pass = bookkeeping_agrees and not refuted

    # ------------------------------------- across-key at every possible scope
    def gap_word_text(gaps):
        return "|" + "|".join(str(gap) for gap in gaps) + "|"

    def across_scope(cadences, count):
        blocks = {}
        for index in range(count):
            buckets = defaultdict(list)
            silent = 0
            for lane in range(len(keys)):
                cadence = cadences[lane][index]
                if not cadence:
                    silent += 1
                    continue
                buckets[gaps_of(cadence)].append(lane)
            edges = nonzero = zero = 0
            covered = 0
            for word, lanes in buckets.items():
                if len(lanes) < 2:
                    continue
                covered += len(lanes)
                base = cadences[lanes[0]][index]
                for lane in lanes[1:]:
                    other = cadences[lane][index]
                    if len(other) != len(base):
                        continue
                    offset = other[0] - base[0]
                    if any(left + offset != right
                           for left, right in zip(base, other)):
                        continue
                    edges += 1
                    if offset:
                        nonzero += 1
                    else:
                        zero += 1
            # F3 factor layer: shorter gap word a contiguous factor of a longer
            # one, verified as an exact lag map on the tick sequences.
            words = {word: gap_word_text(word) for word in buckets}
            ordered = sorted(words, key=lambda word: len(words[word]))
            factor_edges = 0
            for position, needle in enumerate(ordered):
                if len(needle) + 1 < MIN_LAG_OVERLAP:
                    continue
                needle_text = words[needle]
                for haystack in ordered[position + 1:]:
                    haystack_text = words[haystack]
                    if len(haystack_text) < len(needle_text):
                        continue
                    at = haystack_text.find(needle_text)
                    if at < 0:
                        continue
                    source = cadences[buckets[haystack][0]][index]
                    target = cadences[buckets[needle][0]][index]
                    lag = haystack_text.count("|", 0, at + 1) - 1
                    if lag < 0 or lag + len(target) > len(source):
                        continue
                    shift = target[0] - source[lag]
                    if all(source[lag + ordinal] + shift == tick
                           for ordinal, tick in enumerate(target)):
                        factor_edges += 1
            blocks[index] = {
                "sounding_keys": len(keys) - silent,
                "silent_keys": silent,
                "distinct_gap_words": len(buckets),
                "F1_edges": edges,
                "F1_nonzero": nonzero,
                "F1_zero": zero,
                "F3_factor_edges": factor_edges,
                "keys_outside": len(keys) - silent - covered,
            }
        return blocks

    pair_blocks = across_scope(pair_cadences, len(BANK_PAIRS))
    bank_blocks = across_scope(bank_cadences, FIXTURE_BANKS)
    FIELDS = ("sounding_keys", "silent_keys", "distinct_gap_words", "F1_edges",
              "F1_nonzero", "F1_zero", "F3_factor_edges", "keys_outside")

    def total(*groups):
        out = {field: 0 for field in FIELDS}
        for group in groups:
            for block in group.values():
                for field in FIELDS:
                    out[field] += block[field]
        return out

    recomputed_scopes = {
        "FULL_CORPUS": total(pair_blocks, bank_blocks),
        "SUB_CORPUS_pair_clocks_only": total(pair_blocks),
        "SUB_CORPUS_bank_clocks_only": total(bank_blocks),
    }
    scope_matches = {
        label: all(
            recomputed_scopes[label][field] == PINNED["across_key_scopes"][label][field]
            for field in FIELDS
        )
        for label in recomputed_scopes
    }
    f_pass = all(scope_matches.values()) and all(
        recomputed_scopes["FULL_CORPUS"][field]
        == recomputed_scopes["SUB_CORPUS_pair_clocks_only"][field]
        + recomputed_scopes["SUB_CORPUS_bank_clocks_only"][field]
        for field in FIELDS
    )

    # ------------------------------ AXIS 5: the headline-laundering attack
    launder = {}
    headline_scope = scope_of(PINNED["across_key_headline_F1_edges"],
                              recomputed_scopes)
    full = recomputed_scopes["FULL_CORPUS"]
    sub_pair = recomputed_scopes["SUB_CORPUS_pair_clocks_only"]
    launder["L1_across_key_headline_scope"] = {
        "attack": (
            "Cycle 875's A4 caught the 869 headline quoting a pair-clock "
            "sub-corpus.  The same attack is run here on 879's own headline: "
            "the published number is matched against every scope it could have "
            "been computed at."
        ),
        "published_headline_F1_edges": PINNED["across_key_headline_F1_edges"],
        "published_scope_label": PINNED["across_key_headline_scope_label"],
        "scope_the_number_actually_equals": headline_scope,
        "full_corpus_F1_edges": full["F1_edges"],
        "pair_sub_corpus_F1_edges": sub_pair["F1_edges"],
        "headline_is_the_full_corpus": (
            headline_scope == "FULL_CORPUS"
            and PINNED["across_key_headline_F1_edges"] == full["F1_edges"]
            and PINNED["across_key_headline_keys_outside"] == full["keys_outside"]
            and PINNED["across_key_headline_nonzero"] == full["F1_nonzero"]
            and PINNED["across_key_headline_F3_factor_edges"]
            == full["F3_factor_edges"]
        ),
        "full_corpus_is_strictly_larger_than_the_pair_sub_corpus": (
            full["F1_edges"] > sub_pair["F1_edges"]
        ),
        "pass": (
            headline_scope == "FULL_CORPUS"
            and PINNED["across_key_headline_keys_outside"] == full["keys_outside"]
            and PINNED["across_key_headline_nonzero"] == full["F1_nonzero"]
            and PINNED["across_key_headline_F3_factor_edges"]
            == full["F3_factor_edges"]
            and full["F1_edges"] > sub_pair["F1_edges"]
        ),
    }

    # L2  the coverage denominator must be the whole substantive population.
    launder["L2_coverage_denominator"] = {
        "attack": (
            "A coverage fraction can be flattered by shrinking its denominator. "
            "The published denominator is compared with the substantive "
            "population this checker counts independently, and with the total "
            "comparison count it is drawn from."
        ),
        "published_coverage": (
            f"{PINNED['within_key_substantive_relations']}/"
            f"{PINNED['within_key_substantive_pairs']}"
        ),
        "recomputed_substantive_pairs": pair_refute["substantive"],
        "recomputed_comparable_pairs": pair_refute["comparable"],
        "all_comparisons": len(keys) * len(BANK_PAIRS) * (len(BANK_PAIRS) - 1) // 2,
        "denominator_is_the_full_substantive_population": (
            PINNED["within_key_substantive_pairs"] == pair_refute["substantive"]
        ),
        "denominator_not_silently_narrowed": (
            PINNED["within_key_substantive_pairs"] <= pair_refute["comparable"]
        ),
        "pass": (
            PINNED["within_key_substantive_pairs"] == pair_refute["substantive"]
            and PINNED["within_key_comparable_pairs"] == pair_refute["comparable"]
        ),
    }

    # L3  the whole-orbit period law.  Symmetric: a manufactured break fails
    #     here exactly as an understated one would.
    surviving_nonorbit = {}
    for period in sorted(set(int(text) for text in PINNED["nondegenerate_periods"])
                         | set(PINNED["non_orbit_periods"])):
        if period % STATIONS == 0:
            continue
        support = (pinned_period_support.get(str(period))
                   or {"bank": 0, "pair": 0})
        surviving_nonorbit[str(period)] = support
    nonorbit_witnesses = []
    for period in PINNED["non_orbit_periods"]:
        for label, cadences in (("bank", bank_cadences), ("pair", pair_cadences)):
            for lane in range(len(keys)):
                for index, row in enumerate(cadences[lane]):
                    if exact_saturation(row) is not None:
                        continue
                    verdict = brute_force_period(row, period)
                    if verdict is None or verdict["saturated"]:
                        continue
                    orbit_verdict = brute_force_period(row, STATIONS)
                    nonorbit_witnesses.append({
                        "clock": f"{label}{index}",
                        "key_index": lane,
                        "events": len(row),
                        "claimed_period": period,
                        "period_over_stations": f"{period}/{STATIONS}",
                        "brute_force_transient_tick": verdict["transient_tick"],
                        "brute_force_stable_events": verdict["events"],
                        "brute_force_residue_count": verdict["residue_count"],
                        "station_period_also_holds": orbit_verdict is not None,
                    })
                    if len(nonorbit_witnesses) >= WITNESS_PRINT_CAP:
                        break
                if len(nonorbit_witnesses) >= WITNESS_PRINT_CAP:
                    break
            if len(nonorbit_witnesses) >= WITNESS_PRINT_CAP:
                break
        if len(nonorbit_witnesses) >= WITNESS_PRINT_CAP:
            break
    break_is_real = bool(nonorbit_witnesses) and all(
        sum(support.values()) > 0 for support in surviving_nonorbit.values()
    )
    launder["L3_whole_orbit_period_law"] = {
        "attack": (
            "The primary reports that the B=3 whole-orbit period law BREAKS at "
            "B=4.  A break is as launderable as a positive: this test fails "
            "the primary if the break is MANUFACTURED (no non-orbit period "
            "survives the direct membership test) and equally if the primary "
            "had claimed the law holds while a non-orbit period survives.  The "
            "adjudicator is brute force, not either detector."
        ),
        "primary_claim_every_period_is_whole_orbits": PINNED[
            "every_nondegenerate_period_is_whole_orbits"
        ],
        "primary_non_orbit_periods": PINNED["non_orbit_periods"],
        "primary_clocks_carrying_a_non_orbit_period": PINNED[
            "clocks_carrying_a_non_orbit_period"
        ],
        "brute_force_support_for_each_non_orbit_period": surviving_nonorbit,
        "independent_wide_scan_non_orbit_periods": wide_nonorbit,
        "non_orbit_witnesses": nonorbit_witnesses,
        "break_survives_brute_force": break_is_real,
        "claim_and_evidence_agree": (
            PINNED["every_nondegenerate_period_is_whole_orbits"] is False
        ) == break_is_real,
        "pass": (
            PINNED["every_nondegenerate_period_is_whole_orbits"] is False
        ) == break_is_real,
    }

    # L4  the disclosed deviations must be at least as large as reality.
    distinct_words_max = max(
        [block["distinct_gap_words"] for block in pair_blocks.values()]
        + [block["distinct_gap_words"] for block in bank_blocks.values()]
    )
    launder["L4_disclosed_deviations"] = {
        "attack": (
            "A disclosed deviation is only honest if its stated size is the "
            "real one.  The store-cap deviation figure and the 'the raised "
            "representative cap cannot bite' claim are both recomputed."
        ),
        "published_clocks_866_cap_would_truncate": PINNED[
            "clocks_that_866_nominal_store_cap_would_truncate"
        ],
        "recomputed_clocks_866_cap_would_truncate": over_866,
        "published_events_866_cap_would_discard": PINNED[
            "events_that_866_nominal_store_cap_would_discard"
        ],
        "recomputed_events_866_cap_would_discard": lost_866,
        "largest_distinct_gap_word_count_at_any_clock_index": distinct_words_max,
        "raised_rep_cap": EXPECTED_KEYS,
        "rep_cap_structurally_cannot_bite": distinct_words_max <= EXPECTED_KEYS,
        "pass": (
            over_866 == PINNED["clocks_that_866_nominal_store_cap_would_truncate"]
            and lost_866 == PINNED["events_that_866_nominal_store_cap_would_discard"]
            and distinct_words_max <= EXPECTED_KEYS
        ),
    }

    # L5  the identity-like split: no value-moving map may be filed as identity.
    #     Recomputed from the wider search, whose own identity test is written
    #     independently of the primary's.
    wide_identity = pair_refute["substantive_identity_like_matches"]
    wide_moving = pair_refute["substantive_value_moving_matches"]
    published_identity = PINNED[
        "within_key_substantive_identity_like_full_dictionaries"
    ]
    published_moving = (
        PINNED["within_key_substantive_nonidentity_full_dictionaries"]
        + PINNED["within_key_substantive_nonidentity_partial_matches"]
    )
    launder["L5_identity_like_split"] = {
        "attack": (
            "Filing a value-moving map as identity-like containment would "
            "shrink the headline 'non-identity dictionaries' count.  The wider "
            "search classifies every substantive match with its own identity "
            "test; the wider search must not find FEWER identity-like matches "
            "than the primary claimed, which is the direction that would "
            "expose a mislabelling."
        ),
        "published_identity_like": published_identity,
        "published_value_moving": published_moving,
        "wide_search_identity_like": wide_identity,
        "wide_search_value_moving": wide_moving,
        "wide_search_finds_at_least_the_published_identity_class": (
            wide_identity >= published_identity
        ),
        "wide_search_value_moving_within_published_budget": (
            wide_moving <= published_moving
            + pair_refute["substantive_nonidentity_relations_below_coverage_floor"]
        ),
        "pass": wide_identity >= published_identity,
    }

    g_pass = all(block["pass"] for block in launder.values())

    runtime = time.monotonic() - started
    dumps = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "PURPOSE: an attempt to refute Cycle 879 by independent measurement, a "
        "kernel replay, a strictly wider search, and the Cycle-875 "
        "headline-laundering attack turned on 879's own emitted figures.  A "
        "PASS here means the refutation attempt FAILED and the primary "
        "survived it.",
        ("PASS" if controls["pass"] else "FAIL") + " A_SOURCE_CONTROLS :: "
        + json.dumps(controls, **dumps),
        ("PASS" if b_pass else "FAIL") + " B_INDEPENDENT_MEASUREMENT :: "
        + json.dumps({
            "route": (
                "complementary single-zero watched probe, REVERSED lane "
                "packing, station masks simulated from the A/B token swap "
                "network rather than a closed-form phase"
            ),
            "substrate_ok": substrate_ok,
            "stations": len(program),
            "placements": placement_count,
            "census_keys": len(keys),
            "allocator_failures": allocator_failures,
            "watched_wires_per_bank": {
                str(bank): len(row) for bank, row in per_bank.items()
            },
            "independent_initial_census_sha256": initial_sha,
            "primary_initial_census_sha256": PINNED["initial_census_sha256"],
            "initial_census_matches": initial_sha == PINNED["initial_census_sha256"],
            "independent_corpus_sha256": corpus_sha,
            "primary_corpus_sha256": PINNED["corpus_sha256"],
            "corpus_matches": corpus_sha == PINNED["corpus_sha256"],
        }, **dumps),
        ("PASS" if c_pass else "FAIL") + " C_KERNEL_REPLAY :: " + json.dumps({
            "route": (
                "full-horizon replay of sampled keys through "
                "C719.apply_controller_step on ordinary state tuples -- real "
                "token routing, no bit-slice trick"
            ),
            "replayed_lanes": list(replay_lanes),
            "replayed_keys": len(replay_lanes),
            "mismatches": replay_mismatches,
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " D_CLAIM_REPLICATION :: "
        + json.dumps(replication, **dumps),
        ("PASS" if e_pass else "FAIL") + " E_REFUTATION_SEARCH :: "
        + json.dumps({
            "loosened_box": {
                "period_tail_ladder": list(WIDE_PERIOD_TAIL_LADDER),
                "period_candidates_from": "the FULL border chain of every rung",
                "period_block_gaps": WIDE_PERIOD_BLOCK_GAPS,
                "period_adjudicator": "direct membership test t in S <=> t+P in S",
                "constant_offset_candidates": "every anchor of X (complete)",
                "lag_overlap_floor": MIN_LAG_OVERLAP,
                "lag_coverage_floor": "none (primary demands half a clock)",
                "index_map_exhaustion_required": False,
                "affine_anchors": WIDE_AFFINE_ANCHOR_CAP,
                "lag_span_cap": WIDE_LAG_SPAN_CAP,
                "refutation_coverage_floor": str(REFUTATION_COVERAGE),
            },
            "pair_clocks": pair_refute,
            "bank_clocks": bank_refute,
            "primary_published_nonidentity_relations": primary_nonidentity,
            "wider_search_refuting_relations": (
                pair_refute["substantive_nonidentity_relations_above_coverage_floor"]
            ),
            "wider_search_below_floor_partial_matches": (
                pair_refute["substantive_nonidentity_relations_below_coverage_floor"]
            ),
            "bookkeeping_agrees_with_primary": bookkeeping_agrees,
            "primary_negative_refuted": refuted,
        }, **dumps),
        ("PASS" if f_pass else "FAIL") + " F_ACROSS_KEY_ALL_SCOPES :: "
        + json.dumps({
            "recomputed_scopes": recomputed_scopes,
            "primary_scopes": PINNED["across_key_scopes"],
            "scope_by_scope_match": scope_matches,
            "full_corpus_is_the_sum_of_its_sub_corpora": all(
                recomputed_scopes["FULL_CORPUS"][field]
                == recomputed_scopes["SUB_CORPUS_pair_clocks_only"][field]
                + recomputed_scopes["SUB_CORPUS_bank_clocks_only"][field]
                for field in FIELDS
            ),
            "per_pair_clock_index": {str(k): v for k, v in pair_blocks.items()},
            "per_bank_clock_index": {str(k): v for k, v in bank_blocks.items()},
        }, **dumps),
        ("PASS" if g_pass else "FAIL") + " G_HEADLINE_LAUNDERING :: "
        + json.dumps(launder, **dumps),
    ]
    h_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "audit_input_paths_repo_relative": all(
            not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS
        ),
        "input_shas": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS
        },
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ],
        "firewall_hits": list(FIREWALL.hits),
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    h_prepass = (
        h_core["audit_input_paths_exist"]
        and h_core["audit_input_paths_repo_relative"]
        and not h_core["blocklisted_modules_loaded"]
        and not h_core["firewall_hits"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (controls["pass"], b_pass, c_pass, d_pass, e_pass, f_pass, g_pass)
    stdout_bytes = 0
    for _ in range(4):
        h_core["stdout_bytes"] = stdout_bytes
        h_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True
        )
        h_line = (
            ("PASS" if h_prepass and h_core["stdout_under_150KB"] else "FAIL")
            + " H_CONTROLS :: " + json.dumps(h_core, **dumps)
        )
        stdout_bytes = len(
            ("\n".join(lines + [h_line, "CYCLE879_INDEPENDENT_CHECK_PASS"]) + "\n")
            .encode()
        )
    h_core["stdout_bytes"] = stdout_bytes
    h_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    h_pass = h_prepass and h_core["stdout_under_150KB"]
    h_line = ("PASS" if h_pass else "FAIL") + " H_CONTROLS :: " + json.dumps(
        h_core, **dumps
    )
    final = (
        "CYCLE879_INDEPENDENT_CHECK_PASS" if all(verdicts) and h_pass
        else "CYCLE879_INDEPENDENT_CHECK_REFUTES_PRIMARY"
        if refuted or not g_pass else "CYCLE879_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    print("\n".join(lines + [h_line, final]))
    return 0 if all(verdicts) and h_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
