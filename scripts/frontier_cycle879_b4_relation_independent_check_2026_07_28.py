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

  4  A STRICTLY LARGER SEARCH, ADJUDICATED PER COMPARISON.  The declared
     family is re-searched with every cap loosened: the constant offset over a
     provably COMPLETE candidate set instead of eight anchors; the lag map
     with PARTIAL overlap down to eight events instead of half a clock; the
     index map without the exhaustion requirement; the affine map solved from
     every anchor; and the period law from the FULL border chain of several
     tail windows rather than one minimal border per rung, every candidate
     then adjudicated by a direct membership test.  The primary's COMPLETE
     per-comparison disposition table (parsed from its pinned cache) is then
     matched comparison by canonical comparison: every wide relation found
     where the primary recorded NO_RELATION_IN_F is adjudicated against the
     primary's DECLARED caps -- a within-caps witness on a refused comparison
     REFUTES the primary (its search missed a relation it declared it would
     find); a beyond-caps witness is reported as beyond-family surplus, which
     the priced negative explicitly does not exclude.  Every comparison the
     primary admitted must be re-found, and every published witness is
     re-verified from its serialized parameters with its identity-like flag
     recomputed.  Aggregate counts are bookkeeping only; no aggregate budget
     can pass this gate.

  5  THE HEADLINE-LAUNDERING ATTACK (Cycle 875's A4 standard, turned on this
     block's OWN emitted figures).  Every headline the primary publishes is
     recomputed at every scope it could have been quoted at, and the scope the
     primary actually used is identified from the numbers.  A headline that
     silently quotes a sub-corpus, a coverage fraction whose denominator is
     narrower than its own population, an identity-like split that misfiles a
     value-moving witness (checked per published witness, never by counts), a
     disclosed deviation whose size is understated, or a BREAK claimed without
     the exact canonical clock set surviving brute force -- each is a FAIL
     here, in the direction that costs the primary its result.

Axis 5 is symmetric on purpose.  The primary reports that the B=3
whole-orbit divisibility of DETECTOR-SELECTED periods fails at B=4.  This
checker fails the primary BOTH if that break is manufactured (the exact
published clock set does not survive the direct membership test, or the
station period also explains any of those clocks) AND if the primary had
understated it.  The break gate carries three executed mutation controls
(understated published count, injected extra supporting clock, and a
saturation-closure double-support probe), each required to fail exactly the
intended gate.  A negative finding is not a licence to skip the adversarial
work.
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
PRIMARY_CACHE_879 = (
    "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt"
)
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

# Every pinned input is the exact landed/committed byte revision: the Cycle-719
# core and the Cycle-869 cache are pinned at their landed-on-main blobs
# (verified against origin/main at fix time), and the primary runner/cache are
# pinned at the co-committed revisions of this package.
EXPECTED_SHA256 = {
    PRIMARY_879: "5ed813c21b22a8076a48a279f606f0099c9426b6375b0972d80b5cc4fec48f90",
    PRIMARY_CACHE_879: (
        "0d4184440a95ed13e451da55631fc014061b6fcf17adced30613579ca2729f4f"
    ),
    CORE_719: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    CACHE_869: "586fd6a628142250c7fa859448e004fd445d9f479c71813afd50d0674a67b0fe",
}
EXPECTED_GIT_BLOB = {
    PRIMARY_879: "fd405f484466a2cd8226a93d2630f78df4743d89",
    PRIMARY_CACHE_879: "9dd75ebb85f7d8bdc4e7c4044aa98cddd88bdf9b",
    CORE_719: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    CACHE_869: "dbc876ba8433616b5ddb56f06a91202b8c934201",
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
        "F1": 186, "F1W": 3, "F3": 240, "F3P": 60, "F4": 19,
        "NO_RELATION_IN_F": 8099, "ONE_SIDE_SILENT": 1083,
        "TRIVIAL_SATURATION": 30,
    },
    "within_key_evidence_split": {
        "PARTIAL": 60, "SUBSTANTIVE_NO_RELATION": 7675,
        "SUBSTANTIVE_RELATION": 436, "THIN_NO_RELATION": 424,
        "THIN_RELATION": 12,
    },
    "within_key_bank_clock_histogram": {
        "F3P": 5, "F4": 18, "NO_RELATION_IN_F": 3823, "ONE_SIDE_SILENT": 9,
        "TRIVIAL_SATURATION": 33,
    },
    "within_key_substantive_relations": 436,
    "within_key_substantive_pairs": 8171,
    "within_key_comparable_pairs": 8607,
    "within_key_substantive_nonidentity_full_dictionaries": 9,
    "within_key_substantive_identity_like_full_dictionaries": 427,
    "within_key_substantive_partial_matches": 60,
    "within_key_substantive_nonidentity_partial_matches": 60,
    "bank_clock_substantive_relations": 18,
    "bank_clock_substantive_pairs": 3840,
    "bank_clock_nonidentity_full_dictionaries": 4,
    "detector_selected_periods": {
        "11": {"bank": 8, "pair": 8},
        "27": {"bank": 32, "pair": 29},
        "54": {"bank": 19, "pair": 21},
        "81": {"bank": 20, "pair": 22},
        "1512": {"bank": 2, "pair": 3},
        "1971": {"bank": 16, "pair": 64},
        "2214": {"bank": 0, "pair": 36},
    },
    "every_detected_period_is_whole_orbits": False,
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
            else "READ_ONLY_PINNED_PRIMARY_CACHE" if path == PRIMARY_CACHE_879
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
            "PERIOD_TAIL_FLOOR", "PERIOD_TAIL_RATIO", "PERIOD_MAX_BLOCK_GAPS",
            "MIN_PERIOD_REPEATS", "MIN_SATURATION_RUN",
            "CADENCE_STORE_CAP", "CYCLE866_DECLARED_STORE_CAP",
            "ACROSS_KEY_REP_CAP", "AUDIT_INPUT_PATHS",
        )
    }
    # The in-caps adjudicator re-implements the primary's DECLARED detector
    # and candidate boxes; those boxes must be byte-equal to the primary's own
    # literal declarations or the adjudication would be against the wrong caps.
    declared_boxes_match_adjudicator = (
        declared["PERIOD_TAIL_WINDOW"] == DECLARED_PERIOD_TAIL_WINDOW
        and declared["PERIOD_TAIL_FLOOR"] == DECLARED_PERIOD_TAIL_FLOOR
        and tuple(declared["PERIOD_TAIL_RATIO"] or ())
        == DECLARED_PERIOD_TAIL_RATIO
        and declared["PERIOD_MAX_BLOCK_GAPS"] == DECLARED_PERIOD_MAX_BLOCK_GAPS
        and declared["MIN_PERIOD_REPEATS"] == DECLARED_MIN_PERIOD_REPEATS
        and declared["WINDOWED_OFFSET_ANCHORS"]
        == DECLARED_WINDOWED_OFFSET_ANCHORS
    )
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
    # The pinned primary cache must be the harness-emitted record of a clean
    # run of the pinned primary source: header path, source sha, exit code and
    # status are all decisive.
    cache_head = payloads[PRIMARY_CACHE_879].decode("utf-8", "replace").split(
        "----- stdout -----", 1
    )[0]
    cache_header = {}
    for line in cache_head.splitlines():
        if ": " in line:
            label, value = line.split(": ", 1)
            cache_header[label.strip()] = value.strip()
    primary_cache_binds_primary = (
        cache_header.get("runner") == PRIMARY_879
        and cache_header.get("runner_sha256") == EXPECTED_SHA256[PRIMARY_879]
        and cache_header.get("exit_code") == "0"
        and cache_header.get("status") == "ok"
    )
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    passed = bool(
        literal_paths == AUDIT_INPUT_PATHS
        and all(row["exists"] and row["worktree_relative"] for row in rows)
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
        and markers_exact
        and box_agrees
        and declared_boxes_match_adjudicator
        and search_is_wider
        and deviation_is_a_widening
        and primary_cache_binds_primary
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
        "declared_boxes_match_in_caps_adjudicator": (
            declared_boxes_match_adjudicator
        ),
        "refutation_search_is_strictly_wider": search_is_wider,
        "disclosed_store_cap_deviation_is_a_widening": deviation_is_a_widening,
        "source_AST_markers_exact": markers_exact,
        "primary_cache_binds_pinned_primary_source": primary_cache_binds_primary,
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


# ------------------- the primary's published per-comparison disposition table
def short_key_name(key):
    event, positions = key
    return f"e{event}p{'.'.join(str(position) for position in positions)}"


def load_primary_blocks():
    """Parse the pinned primary cache into its labelled JSON blocks."""
    text = (ROOT / PRIMARY_CACHE_879).read_text(encoding="utf-8")
    blocks = {}
    for line in text.splitlines():
        if " :: " not in line:
            continue
        tag, payload = line.split(" :: ", 1)
        parts = tag.split(" ", 1)
        if len(parts) == 2 and parts[0] in ("PASS", "FAIL"):
            try:
                blocks[parts[1]] = json.loads(payload)
            except json.JSONDecodeError:
                pass
    return blocks


# The primary's DECLARED detector box, re-implemented here from its declared
# contract (and cross-checked against the primary's AST literals in the
# source controls).  Used ONLY to adjudicate whether a wide-search witness on
# a primary-refused comparison lies INSIDE the primary's declared caps.
DECLARED_PERIOD_TAIL_WINDOW = 2_048
DECLARED_PERIOD_TAIL_FLOOR = 16
DECLARED_PERIOD_TAIL_RATIO = (3, 4)
DECLARED_PERIOD_MAX_BLOCK_GAPS = 512
DECLARED_MIN_PERIOD_REPEATS = 2
DECLARED_WINDOWED_OFFSET_ANCHORS = 8
DECLARED_PARTIAL_COVERAGE_FLOOR = Fraction(1, 2)


def declared_detector_profile(cadence, horizon=HORIZON_CHUNKS):
    """The primary's declared tail-ladder period detector, re-implemented.

    One minimal border per rung, block cap, repeat floor, exact transient
    pushback, residue extraction and the shift-exact window test -- written
    from the declared contract, not imported.
    """
    gaps = gaps_of(cadence)
    if len(gaps) < DECLARED_MIN_PERIOD_REPEATS:
        return None
    best = None
    length = min(len(gaps), DECLARED_PERIOD_TAIL_WINDOW)
    while length >= min(DECLARED_PERIOD_TAIL_FLOOR, len(gaps)):
        tail = gaps[-length:]
        failure = kmp_failure(tail)
        block = len(tail) - (failure[-1] if failure else 0)
        if block and block <= DECLARED_PERIOD_MAX_BLOCK_GAPS \
                and len(tail) >= DECLARED_MIN_PERIOD_REPEATS * block:
            period = sum(tail[:block])
            if period > 0 and (best is None or period < best[0]):
                best = (period, block)
        if length <= DECLARED_PERIOD_TAIL_FLOOR:
            break
        length = max(
            DECLARED_PERIOD_TAIL_FLOOR,
            length * DECLARED_PERIOD_TAIL_RATIO[0]
            // DECLARED_PERIOD_TAIL_RATIO[1],
        )
    if best is None:
        return None
    period, block = best
    transient = len(gaps) - block
    while transient and gaps[transient - 1] == gaps[transient - 1 + block]:
        transient -= 1
    if len(gaps) - transient < DECLARED_MIN_PERIOD_REPEATS * block:
        return None
    stable = tuple(tick for tick in cadence if tick >= cadence[transient])
    residues = tuple(sorted({tick % period for tick in stable}))
    window_hi = max(stable) - period
    lower = {tick for tick in stable if tick <= window_hi}
    upper = {tick for tick in stable if tick >= cadence[transient] + period}
    return {
        "period_ticks": period,
        "transient_tick": cadence[transient],
        "residues": residues,
        "saturated": len(residues) == period,
        "shift_exact_on_window": {tick + period for tick in lower} == upper,
    }


def declared_offset_candidates(x, y):
    """The primary's DECLARED windowed-offset candidate set for (x, y)."""
    anchors = DECLARED_WINDOWED_OFFSET_ANCHORS
    candidates = {0}
    for left in x[:anchors] + x[-anchors:]:
        for right in y[:anchors] + y[-anchors:]:
            candidates.add(right - left)
    return candidates


def declared_run_covers_whole_cadence(x_events, y_events, lag, start, overlap):
    """The primary's declared PARTIAL clause, re-implemented from its text.

    The lag run explains y[start : start+overlap] and x[start+lag :
    start+lag+overlap].  It carries a WHOLE cadence -- and so is a total map
    the partial member may never report -- when it covers all of Y or all of
    X.  The declared contract reserves those for the index-lag member.
    """
    return bool(
        (start == 0 and overlap == y_events)
        or (start + lag == 0 and overlap == x_events)
    )


def witness_in_declared_caps(found, x, y):
    """Would the primary's declared family search, at its declared caps, have
    admitted this wide-search witness?  True means a NO_RELATION_IN_F on this
    comparison is REFUTED; False means the witness lies beyond the declared
    caps and only prices the beyond-family surplus.

    The witness arrives oriented: x is the source, y the target.
    """
    member = found["member"]
    if member == "F1/F1W":
        # In caps iff the offset lies in the declared anchor-drawn candidate
        # set (the family's own declared search box for the offset members).
        return found["c"] in declared_offset_candidates(x, y)
    if member == "F2Awide":
        # The primary solves the affine pair from the endpoints only.
        if len(x) != len(y) or len(x) < 3 or x[-1] == x[0]:
            return False
        slope = Fraction(y[-1] - y[0], x[-1] - x[0])
        if slope <= 0 or slope == 1:
            return False
        intercept = Fraction(y[0]) - slope * x[0]
        return all(slope * left + intercept == right
                   for left, right in zip(x, y))
    if member == "F2Bwide":
        # The primary requires the index map to run to exhaustion.
        return bool(found.get("exhausted"))
    if member == "F3wide":
        lag, overlap = found["L"], found["overlap"]
        shorter = min(len(x), len(y))
        if shorter < MIN_LAG_OVERLAP:
            return False
        if lag >= 0 and overlap == len(y):
            return True  # the whole-of-Y lag member's box
        # Otherwise the partial member's box: the coverage floor of the
        # shorter clock AND the declared partial clause -- a run that carries
        # a whole cadence is outside this member's box in this orientation.
        start = max(0, -lag)
        if declared_run_covers_whole_cadence(len(x), len(y), lag, start, overlap):
            return False
        return Fraction(overlap, shorter) >= DECLARED_PARTIAL_COVERAGE_FLOOR
    if member == "F4wide":
        # In caps iff the primary's declared detector selects THIS period on
        # both clocks with valid windows and the rotation holds.
        period, offset = found["P"], found["c"]
        left = declared_detector_profile(x)
        right = declared_detector_profile(y)
        if left is None or right is None:
            return False
        if left["period_ticks"] != period or right["period_ticks"] != period:
            return False
        if not (left["shift_exact_on_window"] and right["shift_exact_on_window"]):
            return False
        if left["saturated"] or right["saturated"]:
            return False
        source, target = set(left["residues"]), set(right["residues"])
        if not source or len(source) != len(target) or len(source) >= period:
            return False
        return {(value + offset) % period for value in source} == target
    return False


def eventual_residues(cadence, period):
    """Residue set of the final full period window of an eventually-periodic
    cadence -- robust to transient-selection differences between detectors."""
    top = cadence[-1]
    return {tick % period for tick in cadence if tick > top - period}


def verify_primary_record(member, params, x, y, horizon=HORIZON_CHUNKS):
    """Re-verify one published witness record under the member's declared
    contract, from independent implementations and the serialized parameters
    alone.  Returns True only if every declared clause holds."""
    if not x or not y:
        return False
    if member == "F1":
        (offset,) = params
        return (
            abs(offset) <= horizon and len(x) == len(y)
            and tuple(tick + offset for tick in x) == tuple(y)
        )
    if member == "F1W":
        (offset,) = params
        if abs(offset) > horizon:
            return False
        low, high = max(0, offset), min(horizon, horizon + offset)
        if high <= low or y[0] < low or y[-1] > high:
            return False
        shifted = tuple(
            tick + offset for tick in x if low <= tick + offset <= high
        )
        return shifted == tuple(y)
    if member == "F2A":
        a_num, a_den, b_num, b_den = params
        slope = Fraction(a_num, a_den)
        intercept = Fraction(b_num, b_den)
        if slope <= 0 or slope == 1 or len(x) != len(y) or len(x) < 3:
            return False
        return all(slope * left + intercept == right
                   for left, right in zip(x, y))
    if member == "F2B":
        step, start = params
        if step < 1 or start < 0 or len(y) < 2 or start >= len(x):
            return False
        return tuple(x[start::step]) == tuple(y)
    if member == "F3":
        lag, shift = params
        if lag < 0 or len(y) < MIN_LAG_OVERLAP or lag + len(y) > len(x):
            return False
        return all(x[lag + ordinal] + shift == tick
                   for ordinal, tick in enumerate(y))
    if member == "F3P":
        lag, shift, overlap = params
        shorter = min(len(x), len(y))
        if overlap < MIN_LAG_OVERLAP or shorter < MIN_LAG_OVERLAP:
            return False
        if Fraction(overlap, shorter) < DECLARED_PARTIAL_COVERAGE_FLOOR:
            return False
        start = max(0, -lag)
        stop = start + overlap
        if stop > len(y) or stop + lag > len(x):
            return False
        # The declared PARTIAL clause: the rest of BOTH clocks must be left
        # unexplained.  A whole-cadence run is a total map and is refused
        # here; it must be published as the index-lag member instead.
        if declared_run_covers_whole_cadence(len(x), len(y), lag, start, overlap):
            return False
        return all(
            x[start + lag + ordinal] + shift == y[start + ordinal]
            for ordinal in range(overlap)
        )
    if member == "F4":
        # The member's declared contract is detector-defined: the declared
        # tail-ladder detector (re-implemented above) must select THIS period
        # on both clocks with shift-exact windows, neither clock saturated,
        # both residue sets proper nonempty equal-size subsets, and the
        # rotation exact.  The eventual-tail residue rotation is additionally
        # cross-checked directly on the final full period window, which is
        # detector-free.
        period, offset = params
        if period <= 0:
            return False
        left = declared_detector_profile(x)
        right = declared_detector_profile(y)
        if left is None or right is None:
            return False
        if left["period_ticks"] != period or right["period_ticks"] != period:
            return False
        if not (left["shift_exact_on_window"] and right["shift_exact_on_window"]):
            return False
        if exact_saturation(x) is not None or exact_saturation(y) is not None:
            return False
        if left["saturated"] or right["saturated"]:
            return False
        source, target = set(left["residues"]), set(right["residues"])
        if not source or len(source) != len(target) or len(source) >= period:
            return False
        if {(value + offset) % period for value in source} != target:
            return False
        tail_source = eventual_residues(x, period)
        tail_target = eventual_residues(y, period)
        return {(value + offset) % period
                for value in tail_source} == tail_target
    return False


def record_identity_flag(member, params):
    """The primary's DECLARED identity-like rule, recomputed from the
    serialized witness parameters: c = 0 for the offset and residue members,
    d = 0 for the lag members, s = 1 for the index member."""
    if member in ("F1", "F1W", "F4"):
        return params[-1] == 0 if member == "F4" else params[0] == 0
    if member in ("F3", "F3P"):
        return params[1] == 0
    if member == "F2B":
        return params[0] == 1
    return False


# ---------------------------- the EXHAUSTIVE in-declared-caps refutation gate
def declared_box_witness(x, y, detector=declared_detector_profile):
    """EXHAUSTIVE search of the primary's DECLARED family box, x -> y.

    Every member of F is searched over its COMPLETE declared parameter range,
    and no member is abandoned because an earlier member produced a candidate:
    the search returns only when a witness INSIDE the declared box is found or
    when the whole declared box has been exhausted.  That is what makes it
    safe as the decisive refutation gate -- a within-caps witness can never be
    masked behind a beyond-caps one, whichever witness a first-hit search
    would have returned first.

    ``detector`` supplies the declared tail-ladder profile of a cadence
    (memoised by the caller).  Returns a witness dict, or None when the box is
    exhausted with no witness.
    """
    if not x or not y:
        return None
    horizon = HORIZON_CHUNKS
    # F1  constant time offset.  The offset is forced by the first events.
    if len(x) == len(y):
        offset = y[0] - x[0]
        if abs(offset) <= horizon and all(
            tick + offset == y[index] for index, tick in enumerate(x)
        ):
            return {"member": "F1", "c": offset}
    # F1W  windowed offset over the COMPLETE declared candidate set.
    for offset in sorted(declared_offset_candidates(x, y)):
        if abs(offset) > horizon:
            continue
        low, high = max(0, offset), min(horizon, horizon + offset)
        if high <= low or y[0] < low or y[-1] > high:
            continue
        left = bisect_left(x, low - offset)
        right = bisect_right(x, high - offset)
        if right - left != len(y):
            continue
        if all(x[left + index] + offset == y[index] for index in range(len(y))):
            return {"member": "F1W", "c": offset, "window": [low, high]}
    # F2A  tick affine, solved from the endpoints exactly as declared.
    if len(x) == len(y) and len(x) >= 3 and x[-1] != x[0]:
        slope = Fraction(y[-1] - y[0], x[-1] - x[0])
        if slope > 0 and slope != 1:
            intercept = Fraction(y[0]) - slope * x[0]
            if all(slope * left + intercept == right
                   for left, right in zip(x, y)):
                return {"member": "F2A", "a": str(slope), "b": str(intercept)}
    # F2B  index affine run to exhaustion; (s,r) is forced by y[0] and y[1].
    if len(y) >= 2:
        start = tick_position(x, y[0])
        second = tick_position(x, y[1])
        if start is not None and second is not None:
            step = second - start
            if (step >= 1
                    and not (step == 1 and start == 0 and len(x) == len(y))
                    and start + step * len(y) >= len(x)
                    and tuple(x[start::step]) == tuple(y)):
                return {"member": "F2B", "s": step, "r": start}
    # F3  whole-of-Y lag map at EVERY admissible lag, not only the first.
    if len(y) >= MIN_LAG_OVERLAP and len(x) >= len(y):
        for lag in range(0, len(x) - len(y) + 1):
            shift = y[0] - x[lag]
            if x[lag + 1] + shift != y[1]:
                continue
            if all(x[lag + index] + shift == y[index]
                   for index in range(len(y))):
                return {"member": "F3", "L": lag, "d": shift,
                        "overlap": len(y)}
    # F3P  partial lag at EVERY admissible lag, in both index directions,
    # with the declared coverage floor and the declared partial clause.
    shorter = min(len(x), len(y))
    if shorter >= MIN_LAG_OVERLAP:
        floor = max(
            MIN_LAG_OVERLAP,
            -(-shorter * DECLARED_PARTIAL_COVERAGE_FLOOR.numerator
              // DECLARED_PARTIAL_COVERAGE_FLOOR.denominator),
        )
        for lag in range(-(len(y) - 1), len(x)):
            start = max(0, -lag)
            stop = min(len(y), len(x) - lag)
            overlap = stop - start
            if overlap < floor:
                continue
            if declared_run_covers_whole_cadence(
                len(x), len(y), lag, start, overlap
            ):
                continue
            shift = y[start] - x[start + lag]
            if x[start + 1 + lag] + shift != y[start + 1]:
                continue
            if all(x[index + lag] + shift == y[index]
                   for index in range(start, stop)):
                return {"member": "F3P", "L": lag, "d": shift,
                        "overlap": overlap}
    # F4  detector-selected common period with an exact residue rotation.
    left_profile, right_profile = detector(x), detector(y)
    if (left_profile is not None and right_profile is not None
            and left_profile["period_ticks"] == right_profile["period_ticks"]
            and left_profile["shift_exact_on_window"]
            and right_profile["shift_exact_on_window"]
            and not left_profile["saturated"]
            and not right_profile["saturated"]
            and exact_saturation(x) is None and exact_saturation(y) is None):
        period = left_profile["period_ticks"]
        source = set(left_profile["residues"])
        target = set(right_profile["residues"])
        if source and len(source) == len(target) and len(source) < period:
            for anchor in sorted(source):
                offset = (min(target) - anchor) % period
                if {(value + offset) % period for value in source} == target:
                    return {"member": "F4", "P": period, "c": offset}
    return None


def declared_box_search(x, y, detector=declared_detector_profile):
    """The exhaustive declared-box search on BOTH orientations of one
    canonical comparison.  Returns (witness, direction); (None, None) means
    the declared box was exhausted in both directions with no witness."""
    found = declared_box_witness(x, y, detector)
    if found is not None:
        return found, "forward"
    found = declared_box_witness(y, x, detector)
    if found is not None:
        return found, "reverse"
    return None, None


# The two executed controls from the Cycle-879 confirmation round, carried
# here as PERMANENT probes on the decisive gate itself.  Each reproduces the
# defect it was written against: the first fails on a first-hit gate, the
# second fails on a verifier that does not enforce the declared partial
# clause.  Both must pass on every run.
MASKING_CONTROL_X = (10, 21, 35, 52, 70, 91, 115, 142, 210, 221, 235, 252,
                     270, 291, 315, 342, 400, 500)
MASKING_CONTROL_Y = (210, 221, 235, 252, 270, 291, 315, 342)
WHOLE_CLOCK_CONTROL_X = (10, 21, 35, 52, 70, 91, 115, 142)
WHOLE_CLOCK_CONTROL_Y = tuple(tick + 200 for tick in WHOLE_CLOCK_CONTROL_X)
WHOLE_SOURCE_CONTROL_Y = WHOLE_CLOCK_CONTROL_Y + (
    WHOLE_CLOCK_CONTROL_Y[-1] + 4096,
)


def decisive_gate_controls():
    """Permanent probes on the refutation gate and the partial clause."""
    x, y = MASKING_CONTROL_X, MASKING_CONTROL_Y
    first, _ = wide_relation(wide_profile(x), wide_profile(y))
    first_is_beyond_caps = (
        first is not None
        and first["direction"] == "forward"
        and not witness_in_declared_caps(first, x, y)
    )
    box, box_direction = declared_box_search(x, y)
    masking = {
        "first_wide_witness": first,
        "first_wide_witness_prices_beyond_caps": first_is_beyond_caps,
        "exhaustive_declared_box_witness": box,
        "declared_box_witness_direction": box_direction,
        "in_cap_witness_is_found_behind_the_beyond_cap_one": bool(
            first_is_beyond_caps and box is not None
            and box["member"] == "F3" and box["L"] == 0 and box["d"] == 200
        ),
        "record_verifier_agrees": verify_primary_record("F3", [0, 200], x, y),
    }
    masking["pass"] = bool(
        masking["in_cap_witness_is_found_behind_the_beyond_cap_one"]
        and masking["record_verifier_agrees"]
    )
    sx, sy = WHOLE_CLOCK_CONTROL_X, WHOLE_CLOCK_CONTROL_Y
    longer = WHOLE_SOURCE_CONTROL_Y
    partial_clause = {
        "whole_target_partial_witness_rejected": not verify_primary_record(
            "F3P", [0, 200, len(sy)], sx, sy
        ),
        "whole_source_partial_witness_rejected": not verify_primary_record(
            "F3P", [0, 200, len(sx)], sx, longer
        ),
        "total_member_accepts_the_same_map": verify_primary_record(
            "F3", [0, 200], sx, sy
        ),
        "partial_box_excludes_a_whole_source_run": not witness_in_declared_caps(
            {"member": "F3wide", "L": 0, "d": 200, "overlap": len(sx),
             "partial": True},
            sx, longer,
        ),
        "declared_box_reexpresses_it_as_the_total_member": (
            (lambda pair: pair[0] is not None and pair[0]["member"] == "F3")(
                declared_box_search(sx, longer))
        ),
        "below_floor_partial_still_rejected": not verify_primary_record(
            "F3P", [0, 200, MIN_LAG_OVERLAP - 1], sx, sy
        ),
    }
    partial_clause["pass"] = all(
        value for label, value in partial_clause.items() if label != "pass"
    )
    return {
        "F3_witness_masking_control": masking,
        "F3P_whole_cadence_clause_control": partial_clause,
        "pass": masking["pass"] and partial_clause["pass"],
    }


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
    for period_text, counts in PINNED["detector_selected_periods"].items():
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
            for period_text, counts in PINNED["detector_selected_periods"].items()
        )
    )

    # ---------------------------------------------------- the refutation search
    # The primary's COMPLETE per-comparison disposition table and its full
    # witness-record list are parsed from the pinned primary cache and
    # adjudicated comparison by canonical comparison.  Aggregate counts are
    # bookkeeping only.
    primary_blocks = load_primary_blocks()
    lane_of_key = {short_key_name(key): lane for lane, key in enumerate(keys)}

    def lane_code_table(block_payload, labels):
        codes = block_payload.get("full_disposition_codes", {})
        expected_len = len(labels) * (len(labels) - 1) // 2
        table = [None] * len(keys)
        problems = 0
        for key_name, code in codes.items():
            lane = lane_of_key.get(key_name)
            if lane is None or len(code) != expected_len:
                problems += 1
                continue
            table[lane] = code
        problems += sum(1 for entry in table if entry is None)
        return table, problems

    def refute(profiles, labels, lane_codes):
        silent = saturated_both = comparable = substantive = 0
        wide_relations = Counter()
        refutations = []
        surplus_examples = []
        weak_examples = []
        nonidentity = weak = cap_hits = 0
        identity_matches = moving_matches = 0
        class_mismatches = 0
        class_mismatch_examples = []
        in_caps_refutations = 0
        beyond_caps_surplus = 0
        admitted_but_wide_empty = 0
        admitted_wide_empty_examples = []
        adjudicated_refusals = 0
        declared_box_exhausted = 0
        masked_by_first_wide_witness = 0
        masked_examples = []
        gate_consistency_violations = 0
        detector_memo = {}

        def detector(cadence):
            if cadence not in detector_memo:
                detector_memo[cadence] = declared_detector_profile(cadence)
            return detector_memo[cadence]
        for lane in range(len(keys)):
            code_row = lane_codes[lane] or ""
            for position, (left, right) in enumerate(
                combinations(range(len(labels)), 2)
            ):
                code = code_row[position] if position < len(code_row) else "?"
                x_profile = profiles[lane][left]
                y_profile = profiles[lane][right]
                if not x_profile["ticks"] or not y_profile["ticks"]:
                    silent += 1
                    if code != "0":
                        class_mismatches += 1
                        if len(class_mismatch_examples) < WITNESS_PRINT_CAP:
                            class_mismatch_examples.append({
                                "key_index": lane,
                                "clocks": [labels[left], labels[right]],
                                "checker_class": "silent",
                                "primary_code": code,
                            })
                    continue
                if (x_profile["saturation"] is not None
                        and y_profile["saturation"] is not None):
                    saturated_both += 1
                    if code != "s":
                        class_mismatches += 1
                        if len(class_mismatch_examples) < WITNESS_PRINT_CAP:
                            class_mismatch_examples.append({
                                "key_index": lane,
                                "clocks": [labels[left], labels[right]],
                                "checker_class": "both_saturated",
                                "primary_code": code,
                            })
                    continue
                comparable += 1
                if code in ("0", "s", "?"):
                    class_mismatches += 1
                    if len(class_mismatch_examples) < WITNESS_PRINT_CAP:
                        class_mismatch_examples.append({
                            "key_index": lane,
                            "clocks": [labels[left], labels[right]],
                            "checker_class": "comparable",
                            "primary_code": code,
                        })
                x = x_profile["ticks"]
                y = y_profile["ticks"]
                shorter = min(len(x), len(y))
                thin = shorter < EVIDENCE_FLOOR
                if not thin:
                    substantive += 1
                found, hits = wide_relation(x_profile, y_profile)
                cap_hits += hits
                if found is not None:
                    wide_relations[found["member"]] += 1
                    covered = found.get("overlap", shorter)
                    coverage = Fraction(min(covered, shorter), shorter)
                    row = {
                        "key_index": lane,
                        "clocks": [labels[left], labels[right]],
                        "witness": found,
                        "lengths": [len(x), len(y)],
                        "coverage": f"{coverage.numerator}/{coverage.denominator}",
                        "primary_code": code,
                    }
                    if not thin:
                        if wide_identity_like(found):
                            identity_matches += 1
                        else:
                            moving_matches += 1
                        if not wide_identity_like(found):
                            if coverage < REFUTATION_COVERAGE:
                                weak += 1
                                if len(weak_examples) < WITNESS_PRINT_CAP:
                                    weak_examples.append(row)
                            else:
                                nonidentity += 1
                elif code in ("1", "w", "2", "3", "p") and not thin:
                    # The wide family is a strict superset of these members:
                    # a comparison the primary admitted must be re-found.
                    admitted_but_wide_empty += 1
                    if len(admitted_wide_empty_examples) < WITNESS_PRINT_CAP:
                        admitted_wide_empty_examples.append({
                            "key_index": lane,
                            "clocks": [labels[left], labels[right]],
                            "primary_code": code,
                        })

                # THE DECISIVE PER-COMPARISON GATE.  On every substantive
                # comparison the primary recorded as NO_RELATION_IN_F, the
                # primary's DECLARED box is searched EXHAUSTIVELY in both
                # orientations -- every member, every parameterisation inside
                # the declared caps -- independently of whichever witness the
                # wider first-hit search happened to return.  A witness inside
                # the declared box means the primary's own search missed a
                # relation it declared it would find, which REFUTES the
                # published refusal.  Only when that box is EXHAUSTED with no
                # witness is a wide relation priced as beyond-caps surplus.
                if code == "x" and not thin:
                    adjudicated_refusals += 1
                    in_cap, in_cap_direction = declared_box_search(x, y, detector)
                    if found is not None:
                        oriented = (x, y) if found["direction"] == "forward" \
                            else (y, x)
                        first_prices_in_caps = witness_in_declared_caps(
                            found, *oriented
                        )
                    else:
                        first_prices_in_caps = False
                    if in_cap is not None:
                        in_caps_refutations += 1
                        refutation_row = {
                            "key_index": lane,
                            "clocks": [labels[left], labels[right]],
                            "declared_box_witness": in_cap,
                            "declared_box_direction": in_cap_direction,
                            "first_wide_witness": found,
                            "lengths": [len(x), len(y)],
                            "primary_code": code,
                        }
                        if len(refutations) < WITNESS_PRINT_CAP:
                            refutations.append(refutation_row)
                        if not first_prices_in_caps:
                            # A first-hit gate would have MISSED this one.
                            masked_by_first_wide_witness += 1
                            if len(masked_examples) < WITNESS_PRINT_CAP:
                                masked_examples.append(refutation_row)
                    else:
                        declared_box_exhausted += 1
                        if first_prices_in_caps:
                            # The two adjudicators disagree; that is a defect
                            # in this checker, never a pass for the primary.
                            gate_consistency_violations += 1
                        if found is not None:
                            beyond_caps_surplus += 1
                            if len(surplus_examples) < WITNESS_PRINT_CAP:
                                surplus_examples.append({
                                    "key_index": lane,
                                    "clocks": [labels[left], labels[right]],
                                    "witness": found,
                                    "lengths": [len(x), len(y)],
                                    "primary_code": code,
                                })
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
            "disposition_class_mismatches": class_mismatches,
            "disposition_class_mismatch_examples": class_mismatch_examples,
            "in_caps_refutations_on_primary_refusals": in_caps_refutations,
            "beyond_caps_surplus_on_primary_refusals": beyond_caps_surplus,
            "substantive_refusals_adjudicated": adjudicated_refusals,
            "refusals_with_declared_box_exhausted": declared_box_exhausted,
            "declared_box_searched_to_exhaustion_on_every_refusal": (
                adjudicated_refusals == in_caps_refutations + declared_box_exhausted
            ),
            "in_cap_witnesses_a_first_hit_gate_would_have_masked": (
                masked_by_first_wide_witness
            ),
            "masked_witness_examples": masked_examples,
            "gate_adjudicator_disagreements": gate_consistency_violations,
            "primary_admitted_but_wide_search_empty": admitted_but_wide_empty,
            "admitted_wide_empty_examples": admitted_wide_empty_examples,
            "refuting_examples": refutations,
            "beyond_caps_examples": surplus_examples,
            "below_floor_examples": weak_examples,
        }

    def verify_records(block_payload, profiles, labels):
        records = block_payload.get("relation_records", [])
        codes = block_payload.get("full_disposition_codes", {})
        mismatches = 0
        mismatch_examples = []
        identity_substantive_full = 0
        per_key_counts = Counter()
        full_members = ("F1", "F1W", "F2A", "F2B", "F3", "F4")
        for record in records:
            key_name, from_label, to_label, member, params, identity, thin = record
            per_key_counts[key_name] += 1
            lane = lane_of_key.get(key_name)
            problem = None
            if lane is None or from_label not in labels or to_label not in labels:
                problem = "unresolvable canonical identity"
            else:
                x = profiles[lane][labels.index(from_label)]["ticks"]
                y = profiles[lane][labels.index(to_label)]["ticks"]
                if not verify_primary_record(member, params, x, y):
                    problem = "witness fails the member's declared contract"
                elif record_identity_flag(member, params) != bool(identity):
                    problem = "identity-like flag contradicts the witness"
                elif (min(len(x), len(y)) < EVIDENCE_FLOOR) != bool(thin):
                    problem = "thin flag contradicts the measured lengths"
            if problem is not None:
                mismatches += 1
                if len(mismatch_examples) < WITNESS_PRINT_CAP:
                    mismatch_examples.append({
                        "record": record, "problem": problem,
                    })
                continue
            if identity and not thin and member in full_members:
                identity_substantive_full += 1
        relation_chars = set("1w23p4")
        records_complete = (
            set(per_key_counts) <= set(codes)
            and all(
                sum(1 for char in code if char in relation_chars)
                == per_key_counts.get(key_name, 0)
                for key_name, code in codes.items()
            )
        )
        return {
            "records": len(records),
            "witness_record_mismatches": mismatches,
            "witness_record_mismatch_examples": mismatch_examples,
            "identity_like_substantive_full_dictionaries_recomputed": (
                identity_substantive_full
            ),
            "records_complete_against_disposition_codes": records_complete,
        }

    pair_labels = tuple(f"{left}{right}" for left, right in BANK_PAIRS)
    bank_labels = tuple(str(bank) for bank in range(FIXTURE_BANKS))
    primary_pair_block = primary_blocks.get("D_WITHIN_KEY_PAIR_OF_PAIRS", {})
    primary_bank_block = primary_blocks.get("E_WITHIN_KEY_BANK_CLOCKS", {})
    pair_codes, pair_code_problems = lane_code_table(
        primary_pair_block, pair_labels
    )
    bank_codes, bank_code_problems = lane_code_table(
        primary_bank_block, bank_labels
    )
    pair_refute = refute(pair_profiles, pair_labels, pair_codes)
    bank_refute = refute(bank_profiles, bank_labels, bank_codes)
    pair_records = verify_records(primary_pair_block, pair_profiles, pair_labels)
    bank_records = verify_records(primary_bank_block, bank_profiles, bank_labels)

    primary_nonidentity = (
        PINNED["within_key_substantive_nonidentity_full_dictionaries"]
        + PINNED["within_key_substantive_nonidentity_partial_matches"]
    )
    # REFUTED means a within-caps relation exists on a comparison the primary
    # recorded as NO_RELATION_IN_F.  Beyond-caps surplus never refutes: the
    # published negative is priced to the declared family and caps.
    refuted = (
        pair_refute["in_caps_refutations_on_primary_refusals"] > 0
        or bank_refute["in_caps_refutations_on_primary_refusals"] > 0
    )
    gate_controls = decisive_gate_controls()
    per_comparison_gates_pass = (
        pair_code_problems == 0
        and bank_code_problems == 0
        and gate_controls["pass"]
        and all(
            block["declared_box_searched_to_exhaustion_on_every_refusal"]
            and block["gate_adjudicator_disagreements"] == 0
            for block in (pair_refute, bank_refute)
        )
        and pair_refute["disposition_class_mismatches"] == 0
        and bank_refute["disposition_class_mismatches"] == 0
        and pair_refute["primary_admitted_but_wide_search_empty"] == 0
        and bank_refute["primary_admitted_but_wide_search_empty"] == 0
        and pair_records["witness_record_mismatches"] == 0
        and bank_records["witness_record_mismatches"] == 0
        and pair_records["records_complete_against_disposition_codes"]
        and bank_records["records_complete_against_disposition_codes"]
    )
    # Aggregate counts: bookkeeping consistency only, never the decisive gate.
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
        and pair_records["records"]
        + bank_records["records"] > 0
    )
    e_pass = bookkeeping_agrees and per_comparison_gates_pass and not refuted

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

    # L3  the whole-orbit divisibility of detector-selected periods.
    #     Symmetric: a manufactured break fails here exactly as an understated
    #     one would.  The gate is EXACT: the canonical identity of every clock
    #     brute-force-supporting each published non-orbit period is
    #     enumerated; the census must equal the published bank/pair counts
    #     exactly, and the station period must FAIL on every one of those
    #     clocks.  Three mutation controls are executed against this gate.
    def nonorbit_support_entries(period):
        entries = []
        for label, cadences in (("bank", bank_cadences), ("pair", pair_cadences)):
            for lane in range(len(keys)):
                for index, row in enumerate(cadences[lane]):
                    if not row or exact_saturation(row) is not None:
                        continue
                    verdict = brute_force_period(row, period)
                    if verdict is None or verdict["saturated"]:
                        continue
                    entries.append({
                        "clock": f"{label}{index}",
                        "key": short_key_name(keys[lane]),
                        "kind": label,
                        "events": len(row),
                        "brute_force_transient_tick": verdict["transient_tick"],
                        "brute_force_residue_count": verdict["residue_count"],
                        "station_period_also_holds": (
                            brute_force_period(row, STATIONS) is not None
                        ),
                    })
        return entries

    def nonorbit_exact_gate(published_counts, entries, published_total):
        bank_count = sum(1 for entry in entries if entry["kind"] == "bank")
        pair_count = sum(1 for entry in entries if entry["kind"] == "pair")
        return (
            bool(entries)
            and bank_count == published_counts["bank"]
            and pair_count == published_counts["pair"]
            and bank_count + pair_count == published_total
            and all(
                not entry["station_period_also_holds"] for entry in entries
            )
        )

    nonorbit_periods = sorted(
        {int(text) for text in PINNED["detector_selected_periods"]}
        | set(PINNED["non_orbit_periods"])
    )
    nonorbit_periods = [
        period for period in nonorbit_periods if period % STATIONS
    ]
    nonorbit_census = {
        str(period): nonorbit_support_entries(period)
        for period in nonorbit_periods
    }
    nonorbit_gate_results = {}
    for period in nonorbit_periods:
        text = str(period)
        published = PINNED["detector_selected_periods"].get(
            text, {"bank": 0, "pair": 0}
        )
        entries = nonorbit_census[text]
        nonorbit_gate_results[text] = {
            "published_bank": published["bank"],
            "published_pair": published["pair"],
            "recomputed_bank": sum(
                1 for entry in entries if entry["kind"] == "bank"
            ),
            "recomputed_pair": sum(
                1 for entry in entries if entry["kind"] == "pair"
            ),
            "station_period_fails_on_every_supporting_clock": all(
                not entry["station_period_also_holds"] for entry in entries
            ),
            "exact": nonorbit_exact_gate(
                published, entries,
                PINNED["clocks_carrying_a_non_orbit_period"],
            ),
        }
    break_is_real = bool(nonorbit_periods) and all(
        result["exact"] for result in nonorbit_gate_results.values()
    )

    # Mutation controls on the exact gate itself.  Each must fail exactly the
    # intended condition and nothing else.
    p11_entries = nonorbit_census.get("11", [])
    p11_published = PINNED["detector_selected_periods"].get(
        "11", {"bank": 0, "pair": 0}
    )
    p11_total = PINNED["clocks_carrying_a_non_orbit_period"]
    saturation_probe = tuple(range(0, 600))
    probe_11 = brute_force_period(saturation_probe, 11)
    probe_27 = brute_force_period(saturation_probe, 27)
    mutation_controls = {
        "understated_published_count_fails_exact_gate": (
            not nonorbit_exact_gate(
                {"bank": p11_published["bank"] - 1,
                 "pair": p11_published["pair"]},
                p11_entries, p11_total - 1,
            )
        ),
        "injected_extra_supporting_clock_fails_exact_gate": (
            not nonorbit_exact_gate(
                p11_published,
                p11_entries + [{
                    "kind": "bank", "clock": "bankX", "key": "synthetic",
                    "station_period_also_holds": False,
                }],
                p11_total,
            )
        ),
        "saturation_closure_double_support_is_excluded": (
            probe_11 is not None and probe_11["saturated"]
            and probe_27 is not None and probe_27["saturated"]
        ),
    }
    mutation_controls_pass = all(mutation_controls.values())

    launder["L3_whole_orbit_period_divisibility"] = {
        "attack": (
            "The primary reports that the B=3 whole-orbit divisibility of "
            "DETECTOR-SELECTED periods fails at B=4.  A break is as "
            "launderable as a positive: this test fails the primary if the "
            "break is MANUFACTURED (the exact published clock census does not "
            "survive the direct membership test, or the station period also "
            "explains one of those clocks) and equally if the primary had "
            "claimed the divisibility holds while a non-orbit period "
            "survives.  The adjudicator is brute force by canonical clock "
            "identity, never either detector and never an aggregate count."
        ),
        "primary_claim_every_detected_period_is_whole_orbits": PINNED[
            "every_detected_period_is_whole_orbits"
        ],
        "primary_non_orbit_periods": PINNED["non_orbit_periods"],
        "primary_clocks_carrying_a_non_orbit_period": PINNED[
            "clocks_carrying_a_non_orbit_period"
        ],
        "exact_census_by_period": nonorbit_gate_results,
        "canonical_supporting_clocks": {
            text: [
                {key: entry[key] for key in
                 ("clock", "key", "kind", "events",
                  "brute_force_transient_tick", "brute_force_residue_count",
                  "station_period_also_holds")}
                for entry in entries
            ]
            for text, entries in nonorbit_census.items()
        },
        "independent_wide_scan_non_orbit_periods": wide_nonorbit,
        "break_survives_exact_brute_force_census": break_is_real,
        "mutation_controls": mutation_controls,
        "mutation_controls_pass": mutation_controls_pass,
        "claim_and_evidence_agree": (
            PINNED["every_detected_period_is_whole_orbits"] is False
        ) == break_is_real,
        "pass": (
            ((PINNED["every_detected_period_is_whole_orbits"] is False)
             == break_is_real)
            and mutation_controls_pass
        ),
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

    # L5  the identity-like split: no value-moving map may be filed as
    #     identity.  DECISIVE ROUTE: every witness the primary published is
    #     re-verified from its serialized parameters against the member's
    #     declared contract, and its identity-like flag is recomputed from
    #     those parameters -- object by object, never by cardinality.  The
    #     wider search's own identity census is reported as bookkeeping.
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
            "shrink the headline 'non-identity dictionaries' count.  Every "
            "published witness record is independently re-verified and its "
            "identity flag recomputed from the witness parameters; one "
            "misfiled witness fails this gate.  Cardinality comparisons over "
            "different relation sets are reported below as bookkeeping only "
            "-- they can never pass this gate on their own."
        ),
        "published_identity_like": published_identity,
        "published_value_moving": published_moving,
        "published_witness_records_reverified": (
            pair_records["records"] + bank_records["records"]
        ),
        "witness_record_mismatches": (
            pair_records["witness_record_mismatches"]
            + bank_records["witness_record_mismatches"]
        ),
        "identity_like_substantive_full_dictionaries_recomputed_per_witness": (
            pair_records[
                "identity_like_substantive_full_dictionaries_recomputed"
            ]
        ),
        "recomputed_identity_class_equals_published": (
            pair_records[
                "identity_like_substantive_full_dictionaries_recomputed"
            ] == published_identity
        ),
        "bookkeeping_wide_search_identity_like": wide_identity,
        "bookkeeping_wide_search_value_moving": wide_moving,
        "pass": (
            pair_records["witness_record_mismatches"] == 0
            and bank_records["witness_record_mismatches"] == 0
            and pair_records[
                "identity_like_substantive_full_dictionaries_recomputed"
            ] == published_identity
        ),
    }

    g_pass = all(block["pass"] for block in launder.values())

    runtime = time.monotonic() - started
    dumps = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "PURPOSE: an attempt to refute Cycle 879 by independent measurement, a "
        "kernel replay, a strictly wider search adjudicated per canonical "
        "comparison against the primary's complete published disposition "
        "table, per-witness re-verification of every published relation, and "
        "the Cycle-875 headline-laundering attack turned on 879's own emitted "
        "figures.  A PASS here means the refutation attempt FAILED and the "
        "primary survived it; aggregate counts are bookkeeping only and can "
        "never carry a PASS.",
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
            "decisive_contract": (
                "the primary's complete per-comparison disposition table and "
                "full witness-record list (parsed from its pinned cache) are "
                "adjudicated comparison by canonical comparison: class "
                "structure must match, every admitted comparison must be "
                "re-found by the wider search, every published witness must "
                "re-verify with a correct identity flag, and every refused "
                "comparison has the primary's DECLARED box searched "
                "EXHAUSTIVELY in both orientations -- every member over its "
                "complete declared parameter range, never a first-hit search "
                "-- so no within-caps witness can be masked behind a "
                "beyond-caps one.  A within-caps witness refutes; only an "
                "EXHAUSTED declared box lets a wide relation be priced as "
                "surplus.  Aggregate counts are bookkeeping only."
            ),
            "decisive_gate_controls": gate_controls,
            "pair_clocks": pair_refute,
            "bank_clocks": bank_refute,
            "pair_witness_records": pair_records,
            "bank_witness_records": bank_records,
            "disposition_code_table_problems": {
                "pair": pair_code_problems, "bank": bank_code_problems,
            },
            "primary_published_nonidentity_relations": primary_nonidentity,
            "wider_search_value_moving_above_floor_bookkeeping": (
                pair_refute["substantive_nonidentity_relations_above_coverage_floor"]
            ),
            "wider_search_below_floor_partial_matches": (
                pair_refute["substantive_nonidentity_relations_below_coverage_floor"]
            ),
            "in_caps_refutations": (
                pair_refute["in_caps_refutations_on_primary_refusals"]
                + bank_refute["in_caps_refutations_on_primary_refusals"]
            ),
            "beyond_caps_surplus": (
                pair_refute["beyond_caps_surplus_on_primary_refusals"]
                + bank_refute["beyond_caps_surplus_on_primary_refusals"]
            ),
            "refusals_adjudicated_against_the_declared_box": (
                pair_refute["substantive_refusals_adjudicated"]
                + bank_refute["substantive_refusals_adjudicated"]
            ),
            "declared_box_exhausted_with_no_witness": (
                pair_refute["refusals_with_declared_box_exhausted"]
                + bank_refute["refusals_with_declared_box_exhausted"]
            ),
            "in_cap_witnesses_a_first_hit_gate_would_have_masked": (
                pair_refute["in_cap_witnesses_a_first_hit_gate_would_have_masked"]
                + bank_refute["in_cap_witnesses_a_first_hit_gate_would_have_masked"]
            ),
            "per_comparison_gates_pass": per_comparison_gates_pass,
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
