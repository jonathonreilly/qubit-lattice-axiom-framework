#!/usr/bin/env python3
"""Cycle 869 independent check: an attempt to REFUTE the clock-relation result.

The Cycle-869 primary is BLOCKLISTED.  It is read as text and AST only -- a
meta-path firewall turns any import of it into a hard failure -- so nothing
here can inherit its measurement code, its search code, or its verdicts.  Only
the Cycle-719 controller core is imported, and that is the shared substrate
under test, not a source primary.

This checker is built to make the primary fail, along four axes.

  1  DIFFERENT MEASUREMENT.  The watched coordinates are located by the
     COMPLEMENTARY probe (fill every bank/link wire, clear one, find the single
     zero) rather than the primary's one-hot probe.  The census lanes are
     packed in REVERSED order, and the per-chunk station masks are produced by
     simulating the controller's A/B token swap network directly instead of the
     primary's closed-form (start + phase) mod STATIONS.

  2  REFERENCE REPLAY.  For a declared subsample of keys the whole horizon is
     replayed through ``C719.apply_controller_step`` on ordinary state tuples,
     which is the reference semantics with real token routing and no bit-slice
     trick at all.  Those cadences must agree event for event.

  3  CLAIM REPLICATION.  Every pinned number the primary published is
     recomputed from the independently measured corpus.

  4  A COMPLEMENTARY BOUNDED SEARCH.  The primary's transformation family is
     re-searched with loosened scalar caps: the constant offset is searched
     over a provably COMPLETE candidate set instead of eight head and tail
     anchors; the lag map allows PARTIAL overlap in both directions instead of
     full containment; the index map drops the exhaustion requirement; the
     affine map is solved from every anchor rather than the endpoints; and the
     period law scans every transient up to a bounded cap and admits the least
     common period of the two clocks.  This is COMPLEMENTARY BOUNDED coverage,
     not a proven superset of the primary's search: in particular the period
     member's transient scan is capped while the primary's tail-ladder
     transient pushback is uncapped, so the two period detectors have
     different reach and period disagreements are adjudicated by DIRECT
     MEMBERSHIP instead (axis 3).  Any substantive non-identity relation this
     search finds on a pair the primary did not publish REFUTES the primary's
     negative; the found relation set is gated on EXACT KEYED WITNESS-SET
     EQUALITY with the primary's published set, not on count equality.
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
PRIMARY_869 = "scripts/frontier_cycle869_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle869_clock_relation_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

EXPECTED_SHA256 = {
    PRIMARY_869: "3ff406e5ddb9e4972c52a8e6e7681af04dfbaecf3c2dbc595dcf94ca0f09c4bd",
    CORE_719: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB = {
    PRIMARY_869: "6f179e395498dce027225099b3a9293ab1389c03",
    CORE_719: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}

# The primary's published claims, pinned as literals and recomputed below.
PINNED = {
    "initial_census_sha256": (
        "34005ca812cf0e0b2652aeb0d6f6a50089da9fb2f791c40712655f7edd6e02cd"
    ),
    "corpus_sha256": (
        "2a77355e7410c10e2dec13b8213543fb1d750249c205888009975dcefdd37e33"
    ),
    "bank_clean_occurrences": [104542, 122849, 448799],
    "pair_clean_occurrences": [8584, 46670, 95017],
    "silent_pair_clocks": 135,
    "saturated_pair_clocks": 1,
    "saturated_bank_clocks": 8,
    "pair_clock_information_content": {
        "BOTH_BANK_CLOCKS_IDENTICAL": 2,
        "ONE_BANK_GATES_THE_PAIR": 62,
        "SILENT_PAIR": 135,
        "STRICTLY_JOINT": 713,
    },
    "within_key_member_histogram": {
        "F1": 10,
        "F3": 5,
        "F3P": 38,
        "NO_RELATION_IN_F": 593,
        "ONE_SIDE_SILENT": 266,
    },
    "within_key_evidence_split": {
        "PARTIAL": 38,
        "SUBSTANTIVE_NO_RELATION": 429,
        "SUBSTANTIVE_RELATION": 13,
        "THIN_NO_RELATION": 164,
        "THIN_RELATION": 2,
    },
    "within_key_trivial_saturation": 0,
    "within_key_substantive_nonidentity_full_dictionaries": 1,
    "within_key_substantive_partial_matches": 38,
    "within_key_substantive_nonidentity_partial_matches": 31,
    # The primary's published keyed witness set ("<lane>:<from>|<to>") for
    # every substantive non-identity relation, full and partial.  The
    # refutation search is gated on EXACT equality with this set, so a wider
    # witness replacing a missed primary witness cannot hide behind an
    # unchanged total.
    "within_key_substantive_nonidentity_relation_keys": [
        "108:02|12", "117:02|12", "125:02|12", "132:02|12", "138:02|12",
        "143:02|12", "147:02|12", "150:02|12", "162:01|12", "166:02|12",
        "169:02|12", "17:02|12", "185:02|12", "200:02|12", "214:02|12",
        "227:02|12", "239:02|12", "250:02|12", "260:02|12", "269:02|12",
        "277:02|12", "284:02|12", "290:02|12", "295:02|12", "299:02|12",
        "302:02|12", "33:02|12", "48:02|12", "62:02|12", "75:02|12",
        "87:02|12", "98:02|12",
    ],
    "within_key_bank_clock_histogram": {
        "F1": 1,
        "NO_RELATION_IN_F": 910,
        "TRIVIAL_SATURATION": 1,
    },
    "across_key_F1_edges": 632,
    "across_key_F1_edges_with_nonzero_offset": 632,
    "nondegenerate_periods": {
        "19": {"bank": 0, "pair": 2},
        "114": {"bank": 5, "pair": 3},
        "1444": {"bank": 12, "pair": 12},
    },
    "every_nondegenerate_period_is_whole_orbits": True,
}

# Independently declared box; cross-checked against the primary's AST literals.
FIXTURE_BANKS = 3
STATIONS = 19
HORIZON_CHUNKS = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
EXPECTED_KEYS = 304
EVIDENCE_FLOOR = 8
MIN_LAG_OVERLAP = 8
RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

# Loosened search box.  The scalar caps are at least as wide as the
# primary's, but the coverage is COMPLEMENTARY BOUNDED, not a proven
# superset: the transient scan below is capped while the primary's
# tail-ladder transient pushback is uncapped.
WIDE_PERIOD_TRANSIENTS = 256          # bounded transient scan (see note above)
WIDE_PERIOD_BLOCK_GAPS = 2_048        # primary caps blocks at 512
WIDE_PERIOD_MAX_TICKS = 65_536        # ceiling on an admitted common period
WIDE_LAG_CANDIDATE_CAP = 40_000       # lags examined per ordered comparison
WIDE_AFFINE_ANCHOR_CAP = 2_048        # affine anchors per ordered comparison
# Non-vacuity floor shared with the primary: a period claimed on a two-gap tail
# is not a period.  Widening the transient scan is the point; widening it into
# vacuity would only manufacture fake disagreements.
WIDE_MIN_PERIODIC_GAPS = 16
REFERENCE_REPLAY_KEYS = 12            # keys replayed through the reference route
WITNESS_PRINT_CAP = 6
MIN_SATURATION_RUN = 8                # matches the primary's exact definition
# A relation only REFUTES the primary if it is a real dictionary: it must move
# the tick values (non-identity) and it must explain at least this fraction of
# the shorter clock.  A nine-event window inside an 848-event clock is a
# coincidence, and counting it as a refutation would be as dishonest as the
# primary hiding it -- so both the strong and the weak matches are reported.
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


BLOCKLISTED_MODULES = (Path(PRIMARY_869).stem,)
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
    trees = {path: ast.parse(payload, filename=path)
             for path, payload in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": (
            "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED" if path == PRIMARY_869
            else "AUTHORIZED_EXECUTABLE_CYCLE719_CORE"
        ),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOB[path],
    } for path in AUDIT_INPUT_PATHS)

    primary = trees[PRIMARY_869]
    declared = {
        "FIXTURE_BANKS": literal_assignment(primary, "FIXTURE_BANKS"),
        "STATIONS": literal_assignment(primary, "STATIONS"),
        "HORIZON_CHUNKS": literal_assignment(primary, "HORIZON_CHUNKS"),
        "TOKEN_K": literal_assignment(primary, "TOKEN_K"),
        "EVENT_COUNT": literal_assignment(primary, "EVENT_COUNT"),
        "EVIDENCE_FLOOR": literal_assignment(primary, "EVIDENCE_FLOOR"),
        "MIN_LAG_OVERLAP": literal_assignment(primary, "MIN_LAG_OVERLAP"),
        "WINDOWED_OFFSET_ANCHORS": literal_assignment(
            primary, "WINDOWED_OFFSET_ANCHORS"
        ),
        "PERIOD_TAIL_WINDOW": literal_assignment(primary, "PERIOD_TAIL_WINDOW"),
        "PERIOD_TAIL_FLOOR": literal_assignment(primary, "PERIOD_TAIL_FLOOR"),
        "PERIOD_MAX_BLOCK_GAPS": literal_assignment(primary, "PERIOD_MAX_BLOCK_GAPS"),
        "MIN_SATURATION_RUN": literal_assignment(primary, "MIN_SATURATION_RUN"),
        "AUDIT_INPUT_PATHS": literal_assignment(primary, "AUDIT_INPUT_PATHS"),
    }
    box_agrees = (
        declared["FIXTURE_BANKS"] == FIXTURE_BANKS
        and declared["STATIONS"] == STATIONS
        and declared["HORIZON_CHUNKS"] == HORIZON_CHUNKS
        and declared["TOKEN_K"] == TOKEN_K
        and declared["EVENT_COUNT"] == EVENT_COUNT
        and declared["EVIDENCE_FLOOR"] == EVIDENCE_FLOOR
        and declared["MIN_LAG_OVERLAP"] == MIN_LAG_OVERLAP
        and declared["AUDIT_INPUT_PATHS"] == (CORE_719,)
    )
    # The primary's declared scalar caps must not exceed this checker's
    # loosened scalar caps.  That makes the family re-search COMPLEMENTARY
    # BOUNDED coverage -- deliberately different detectors with
    # at-least-as-wide scalar caps -- NOT a proven superset of the primary's
    # search: the period member's transient scan here is capped while the
    # primary's tail-ladder transient pushback is uncapped, so period
    # disagreements are adjudicated by direct membership (D block) rather
    # than by any containment argument.
    search_complementary_bounded = (
        declared["PERIOD_TAIL_FLOOR"] is not None
        and declared["PERIOD_TAIL_WINDOW"] is not None
        and declared["PERIOD_TAIL_FLOOR"] > 1
        and declared["PERIOD_MAX_BLOCK_GAPS"] < WIDE_PERIOD_BLOCK_GAPS
        and declared["WINDOWED_OFFSET_ANCHORS"] < WIDE_AFFINE_ANCHOR_CAP
        and declared["MIN_SATURATION_RUN"] == MIN_SATURATION_RUN
    )
    markers = {
        PRIMARY_869: {"relate", "f1_constant_offset", "f3_lag_offset",
                      "f3p_partial_lag", "period_profile", "saturation_profile",
                      "family_controls"},
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
        and search_complementary_bounded
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return {
        "source_rows": rows,
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "primary_declared_box": declared,
        "declared_box_agrees": box_agrees,
        "refutation_search_complementary_bounded": search_complementary_bounded,
        "refutation_search_coverage_note": (
            "the scalar caps are at least as wide as the primary's, but the "
            "coverage is complementary bounded, NOT a proven superset: the "
            "period transient scan is capped at "
            f"{WIDE_PERIOD_TRANSIENTS} while the primary's tail-ladder "
            "transient pushback is uncapped; period disagreements are "
            "adjudicated by direct membership in the D block"
        ),
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
    return program, tuple(keys), tuple(states), allocator_failures


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
                bank_clocks[lane_count - 1 - lane][bank].append(tick)
                mask -= low
        for index, (left, right) in enumerate(BANK_PAIRS):
            mask = clean[left] & clean[right]
            while mask:
                low = mask & -mask
                lane = low.bit_length() - 1
                pair_clocks[lane_count - 1 - lane][index].append(tick)
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


# ------------------------- the complementary bounded loosened-cap search
def gaps_of(cadence):
    return tuple(cadence[i + 1] - cadence[i] for i in range(len(cadence) - 1))


def kmp_border(sequence):
    length = len(sequence)
    if length == 0:
        return 0
    failure = [0] * length
    border = 0
    for index in range(1, length):
        while border and sequence[index] != sequence[border]:
            border = failure[border - 1]
        if sequence[index] == sequence[border]:
            border += 1
        failure[index] = border
    return failure[-1]


def brute_force_period(cadence, period, min_gaps=WIDE_MIN_PERIODIC_GAPS):
    """Decide directly whether a cadence is P-periodic on a long enough tail.

    No string algorithm, no transient ladder: the membership test t in S <=>
    t+P in S is evaluated on the largest suffix where it holds.  This is what
    adjudicates a disagreement between two period-DETECTION methods -- either a
    claimed period survives this test or it does not.
    """
    if period <= 0 or len(cadence) < 2:
        return None
    members = set(cadence)
    last = cadence[-1]
    position = len(cadence) - 1
    while position >= 0:
        tick = cadence[position]
        if tick + period <= last and (tick + period) not in members:
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
    """Smallest eventual period FOUND by scanning every transient up to the
    loosened cap.  This is a bounded detector, not a least-period oracle."""
    gaps = gaps_of(cadence)
    best = None
    limit = min(len(gaps), WIDE_PERIOD_TRANSIENTS)
    for transient in range(limit):
        suffix = gaps[transient:]
        block = len(suffix) - kmp_border(suffix)
        if block == 0 or block > WIDE_PERIOD_BLOCK_GAPS:
            continue
        if len(suffix) < 2 * block or len(suffix) < WIDE_MIN_PERIODIC_GAPS:
            continue
        period = sum(suffix[:block])
        if period <= 0:
            continue
        if best is None or period < best[0]:
            best = (period, transient)
    if best is None:
        return None
    period, transient = best
    stable = tuple(tick for tick in cadence if tick >= cadence[transient])
    residues = frozenset(tick % period for tick in stable)
    return {
        "period": period,
        "transient_tick": cadence[transient],
        "residues": residues,
        "saturated": len(residues) == period,
        "stable": stable,
    }


def wide_offset(x, y, x_set, horizon=HORIZON_CHUNKS):
    """Complete constant-offset search: c must satisfy y[0] - c in X."""
    tail = y[-1]
    for anchor in x:
        offset = y[0] - anchor
        if abs(offset) > horizon:
            continue
        if tail - offset not in x_set:
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
    """Lag map with PARTIAL overlap allowed in both directions."""
    span = len(x) + len(y)
    if span > WIDE_LAG_CANDIDATE_CAP:
        return None
    for lag in range(-(len(y) - 1), len(x)):
        start = max(0, -lag)
        stop = min(len(y), len(x) - lag)
        if stop - start < MIN_LAG_OVERLAP:
            continue
        shift = y[start] - x[start + lag]
        # Cheap two-element prune before the full comparison.
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


def wide_index_map(x, y, x_index):
    """Index-affine map without the primary's exhaustion requirement."""
    if len(y) < 2 or y[0] not in x_index or y[1] not in x_index:
        return None
    start = x_index[y[0]]
    step = x_index[y[1]] - start
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
    source = {tick % period for tick in left["stable"]}
    target = {tick % period for tick in right["stable"]}
    if len(source) != len(target) or not source or len(source) == period:
        return None
    for anchor in sorted(source):
        offset = (min(target) - anchor) % period
        if {(value + offset) % period for value in source} == target:
            return {"member": "F4wide", "P": period, "c": offset}
    return None


def wide_relation(left, right):
    """Any relation in the loosened family, searched in both directions."""
    for source, target, direction in (
        (left, right, "forward"), (right, left, "reverse")
    ):
        x, y = source["ticks"], target["ticks"]
        if not x or not y:
            continue
        found = wide_offset(x, y, source["set"])
        if found is None:
            found = wide_affine(x, y)
        if found is None:
            found = wide_index_map(x, y, source["index"])
        if found is None:
            found = wide_lag(x, y)
        if found is None:
            if source["saturation"] is None and target["saturation"] is None:
                found = wide_residue_law(source["period"], target["period"])
        if found is not None:
            return {**found, "direction": direction}
    return None


def wide_profile(cadence):
    """Profile a cadence.  A detected period is kept only if it survives the
    direct membership test, so this checker never carries a period claim its
    own adjudicator would reject."""
    detected = wide_period(cadence) if len(cadence) >= MIN_LAG_OVERLAP else None
    kept = detected
    dropped = 0
    if detected is not None:
        if brute_force_period(cadence, detected["period"]) is None:
            kept, dropped = None, 1
    return {
        "ticks": cadence,
        "set": set(cadence),
        "index": {tick: position for position, tick in enumerate(cadence)},
        "period": kept,
        "raw_period_claim": detected["period"] if detected else None,
        "period_claim_dropped": dropped,
        "saturation": exact_saturation(cadence),
    }


def main():
    started = time.monotonic()
    controls = source_controls()

    program, keys, states, allocator_failures = build_census()
    per_bank, source_pointer = complementary_watched_layout()
    substrate_ok = (
        len(program) == STATIONS
        and len(keys) == EXPECTED_KEYS
        and allocator_failures == 0
        and all(len(row) == 47 for row in per_bank.values())
        and all(
            not (set(per_bank[left]) & set(per_bank[right]))
            for left, right in BANK_PAIRS
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
    silent_pair = sum(1 for lane in pair_cadences for row in lane if not row)
    bank_profiles = tuple(tuple(wide_profile(row) for row in lane)
                          for lane in bank_cadences)
    pair_profiles = tuple(tuple(wide_profile(row) for row in lane)
                          for lane in pair_cadences)

    def saturated_count(profiles):
        return sum(
            1 for lane in profiles for profile in lane
            if profile["saturation"] is not None
        )

    def wide_period_only_saturated(profiles):
        """Clocks the WIDE period scan alone would have called saturated."""
        return sum(
            1 for lane in profiles for profile in lane
            if profile["saturation"] is None
            and profile["period"] is not None and profile["period"]["saturated"]
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

    # The 1444-tick period, recomputed under the far wider transient scan.
    wide_periods_bank = Counter(
        profile["period"]["period"]
        for lane in bank_profiles for profile in lane
        if profile["period"] is not None and not profile["period"]["saturated"]
        and profile["saturation"] is None
    )
    wide_periods_pair = Counter(
        profile["period"]["period"]
        for lane in pair_profiles for profile in lane
        if profile["period"] is not None and not profile["period"]["saturated"]
        and profile["saturation"] is None
    )

    # Adjudicate the two period-detection methods by brute force rather than
    # by comparing algorithms: a claimed period either survives the direct
    # membership test or it does not.
    wide_raw_claims = wide_dropped = 0
    for profiles in (bank_profiles, pair_profiles):
        for lane in profiles:
            for profile in lane:
                if profile["raw_period_claim"] is not None:
                    wide_raw_claims += 1
                wide_dropped += profile["period_claim_dropped"]
    pinned_period_support = {}
    for period_text, counts in PINNED["nondegenerate_periods"].items():
        period = int(period_text)
        support = {"bank": 0, "pair": 0}
        for label, profiles in (("bank", bank_profiles), ("pair", pair_profiles)):
            for lane in profiles:
                for profile in lane:
                    if profile["saturation"] is not None:
                        continue
                    verdict = brute_force_period(profile["ticks"], period)
                    if verdict is not None and not verdict["saturated"]:
                        support[label] += 1
        pinned_period_support[period_text] = support

    replication = {
        "bank_clean_occurrences": bank_occurrences,
        "pair_clean_occurrences": pair_occurrences,
        "silent_pair_clocks": silent_pair,
        "saturated_pair_clocks": saturated_count(pair_profiles),
        "saturated_bank_clocks": saturated_count(bank_profiles),
        "pair_clock_information_content": dict(sorted(domination.items())),
        "pair_is_intersection_failures": intersection_failures,
        "wide_scan_nondegenerate_bank_periods": dict(sorted(wide_periods_bank.items())),
        "wide_scan_nondegenerate_pair_periods": dict(sorted(wide_periods_pair.items())),
        "wide_period_scan_only_saturated_bank": wide_period_only_saturated(bank_profiles),
        "wide_period_scan_only_saturated_pair": wide_period_only_saturated(pair_profiles),
        "wide_scan_raw_period_claims": wide_raw_claims,
        "wide_scan_claims_dropped_by_brute_force": wide_dropped,
        "primary_pinned_period_brute_force_support": pinned_period_support,
        "method_reach_note": (
            "The two period DETECTORS have different minimality reach -- this "
            "checker scans every transient up to a cap, the primary reads its "
            "block off a tail ladder -- so their histograms differ.  That is "
            "not a refutation: what is gated is that every period either side "
            "claims survives the direct membership test, and that the "
            "primary's published counts are supported by that test."
        ),
        "wide_scan_nonorbit_periods": sorted(
            period for period in set(wide_periods_bank) | set(wide_periods_pair)
            if period % STATIONS
        ),
    }
    d_pass = (
        bank_occurrences == PINNED["bank_clean_occurrences"]
        and pair_occurrences == PINNED["pair_clean_occurrences"]
        and silent_pair == PINNED["silent_pair_clocks"]
        and replication["saturated_pair_clocks"] == PINNED["saturated_pair_clocks"]
        and replication["saturated_bank_clocks"] == PINNED["saturated_bank_clocks"]
        and replication["pair_clock_information_content"]
        == PINNED["pair_clock_information_content"]
        and intersection_failures == 0
        and (not replication["wide_scan_nonorbit_periods"])
        == PINNED["every_nondegenerate_period_is_whole_orbits"]
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
        nonidentity = weak = 0
        nonidentity_keys = []
        for lane in range(len(keys)):
            for left, right in combinations(range(len(labels)), 2):
                x_profile = profiles[lane][left]
                y_profile = profiles[lane][right]
                if not x_profile["ticks"] or not y_profile["ticks"]:
                    silent += 1
                    continue
                if (
                    x_profile["saturation"] is not None
                    and y_profile["saturation"] is not None
                ):
                    saturated_both += 1
                    continue
                comparable += 1
                thin = min(len(x_profile["ticks"]), len(y_profile["ticks"])) \
                    < EVIDENCE_FLOOR
                if not thin:
                    substantive += 1
                found = wide_relation(x_profile, y_profile)
                if found is None:
                    continue
                wide_relations[found["member"]] += 1
                shorter = min(len(x_profile["ticks"]), len(y_profile["ticks"]))
                covered = found.get("overlap", shorter)
                coverage = Fraction(covered, shorter)
                identity_like = (
                    found.get("c") == 0
                    or (found["member"] == "F3wide" and found["d"] == 0)
                    or (found["member"] == "F2Bwide" and found["s"] == 1)
                )
                row = {
                    "key_index": lane,
                    "clocks": [labels[left], labels[right]],
                    "witness": {
                        key: value for key, value in found.items()
                        if key != "stable"
                    },
                    "lengths": [len(x_profile["ticks"]), len(y_profile["ticks"])],
                    "coverage": f"{coverage.numerator}/{coverage.denominator}",
                }
                if thin or identity_like:
                    continue
                if coverage < REFUTATION_COVERAGE:
                    weak += 1
                    if len(weak_examples) < WITNESS_PRINT_CAP:
                        weak_examples.append(row)
                    continue
                nonidentity += 1
                nonidentity_keys.append(
                    f"{lane}:{labels[left]}|{labels[right]}"
                )
                if len(refutations) < WITNESS_PRINT_CAP:
                    refutations.append(row)
        return {
            "one_side_silent": silent,
            "both_saturated": saturated_both,
            "comparable": comparable,
            "substantive": substantive,
            "wide_family_hits": dict(sorted(wide_relations.items())),
            "substantive_nonidentity_relations_above_coverage_floor": nonidentity,
            "substantive_nonidentity_relations_below_coverage_floor": weak,
            "substantive_nonidentity_relation_keys": sorted(nonidentity_keys),
            "refuting_examples": refutations,
            "below_floor_examples": weak_examples,
        }

    pair_labels = tuple(f"{left}{right}" for left, right in BANK_PAIRS)
    bank_labels = tuple(str(bank) for bank in range(FIXTURE_BANKS))
    pair_refute = refute(pair_profiles, pair_labels)
    bank_refute = refute(bank_profiles, bank_labels)

    # A refutation is a substantive NON-IDENTITY relation this search finds on
    # a keyed pair the primary did NOT publish.  The gate is EXACT KEYED
    # WITNESS-SET EQUALITY against the primary's published set -- not count
    # equality -- so a wider-only witness replacing a missed primary witness
    # cannot hide behind an unchanged total.  Extra keys refute the primary's
    # negative; missing keys mean this search failed to replicate a published
    # witness, which is an honest failure of this check, not a pass.
    primary_nonidentity = (
        PINNED["within_key_substantive_nonidentity_full_dictionaries"]
        + PINNED["within_key_substantive_nonidentity_partial_matches"]
    )
    pinned_relation_keys = set(
        PINNED["within_key_substantive_nonidentity_relation_keys"]
    )
    wider_relation_keys = set(
        pair_refute["substantive_nonidentity_relation_keys"]
    )
    extra_relation_keys = sorted(wider_relation_keys - pinned_relation_keys)
    missing_relation_keys = sorted(pinned_relation_keys - wider_relation_keys)
    keyed_witness_sets_equal = (
        not extra_relation_keys and not missing_relation_keys
        and len(pinned_relation_keys) == primary_nonidentity
    )
    refuted = bool(extra_relation_keys)
    bookkeeping_agrees = (
        pair_refute["one_side_silent"]
        == PINNED["within_key_member_histogram"]["ONE_SIDE_SILENT"]
        and pair_refute["both_saturated"] == PINNED["within_key_trivial_saturation"]
        and pair_refute["comparable"] + pair_refute["one_side_silent"]
        + pair_refute["both_saturated"] == len(keys) * len(BANK_PAIRS)
        and pair_refute["substantive"]
        == PINNED["within_key_evidence_split"]["SUBSTANTIVE_NO_RELATION"]
        + PINNED["within_key_evidence_split"]["SUBSTANTIVE_RELATION"]
        + PINNED["within_key_evidence_split"]["PARTIAL"]
    )
    e_pass = bookkeeping_agrees and keyed_witness_sets_equal

    # ------------------------------------------- across-key constant offsets
    across = {}
    across_edges = across_nonzero = 0
    for index, label in enumerate(pair_labels):
        buckets = defaultdict(list)
        for lane in range(len(keys)):
            cadence = pair_cadences[lane][index]
            if not cadence:
                continue
            buckets[gaps_of(cadence)].append(lane)
        edges = nonzero = 0
        for word, lanes in buckets.items():
            if len(lanes) < 2:
                continue
            base = pair_cadences[lanes[0]][index]
            for lane in lanes[1:]:
                other = pair_cadences[lane][index]
                offset = other[0] - base[0]
                if len(other) != len(base):
                    continue
                if any(
                    left + offset != right for left, right in zip(base, other)
                ):
                    continue
                edges += 1
                nonzero += offset != 0
        across[label] = {"F1_edges": edges, "F1_nonzero_offset_edges": nonzero,
                         "distinct_gap_words": len(buckets)}
        across_edges += edges
        across_nonzero += nonzero
    f_pass = (
        across_edges == PINNED["across_key_F1_edges"]
        and across_nonzero == PINNED["across_key_F1_edges_with_nonzero_offset"]
    )

    runtime = time.monotonic() - started
    dumps = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "PURPOSE: an attempt to refute Cycle 869 by independent measurement and "
        "a complementary bounded loosened-cap search, gated on exact keyed "
        "witness-set equality.  A PASS here means the refutation attempt "
        "FAILED and the primary survived it within this checker's declared "
        "reach; it is not a superset guarantee.",
        ("PASS" if controls["pass"] else "FAIL") + " A_SOURCE_CONTROLS :: "
        + json.dumps(controls, **dumps),
        ("PASS" if b_pass else "FAIL") + " B_INDEPENDENT_MEASUREMENT :: "
        + json.dumps({
            "route": (
                "complementary fill-and-clear probe, reversed lane packing, "
                "station masks from the A/B swap network"
            ),
            "substrate_ok": substrate_ok,
            "allocator_failures": allocator_failures,
            "census_keys": len(keys),
            "initial_census_sha256": initial_sha,
            "initial_census_sha256_matches_primary": (
                initial_sha == PINNED["initial_census_sha256"]
            ),
            "corpus_sha256": corpus_sha,
            "corpus_sha256_matches_primary": corpus_sha == PINNED["corpus_sha256"],
        }, **dumps),
        ("PASS" if c_pass else "FAIL") + " C_REFERENCE_REPLAY :: "
        + json.dumps({
            "route": (
                "full horizon through C719.apply_controller_step on state "
                "tuples, with the controller's own token routing"
            ),
            "keys_replayed": len(replay_lanes),
            "replay_key_indices": list(replay_lanes),
            "mismatches": replay_mismatches,
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " D_CLAIM_REPLICATION :: "
        + json.dumps({"recomputed": replication, "pinned": PINNED}, **dumps),
        ("PASS" if e_pass else "FAIL") + " E_REFUTATION_SEARCH :: "
        + json.dumps({
            "loosened_box": {
                "period_transients_scanned": WIDE_PERIOD_TRANSIENTS,
                "period_block_gap_cap": WIDE_PERIOD_BLOCK_GAPS,
                "period_admitted_up_to_lcm_ticks": WIDE_PERIOD_MAX_TICKS,
                "offset_candidates": "complete: every c with y[0]-c in X",
                "lag_overlap": "partial overlap allowed in both directions",
                "index_map": "exhaustion requirement dropped",
                "affine_anchors": WIDE_AFFINE_ANCHOR_CAP,
                "coverage_note": (
                    "complementary bounded coverage, not a proven superset of "
                    "the primary's search: the period transient scan is capped "
                    f"at {WIDE_PERIOD_TRANSIENTS} while the primary's "
                    "tail-ladder transient pushback is uncapped; period "
                    "disagreements are adjudicated by direct membership in "
                    "the D block"
                ),
            },
            "pair_clocks": pair_refute,
            "bank_clocks": bank_refute,
            "primary_substantive_nonidentity_witnesses_full_plus_partial": (
                primary_nonidentity
            ),
            "refutation_criterion": (
                "a relation refutes only if it is substantive, moves the tick "
                "values, covers at least "
                f"{REFUTATION_COVERAGE.numerator}/"
                f"{REFUTATION_COVERAGE.denominator} of the shorter clock, and "
                "falls on a keyed pair OUTSIDE the primary's published "
                "witness set; the gate below is exact keyed set equality, not "
                "count equality"
            ),
            "wider_search_relations_above_floor": (
                pair_refute["substantive_nonidentity_relations_above_coverage_floor"]
            ),
            "wider_search_below_floor_partial_matches": (
                pair_refute["substantive_nonidentity_relations_below_coverage_floor"]
            ),
            "keyed_witness_sets_equal": keyed_witness_sets_equal,
            "wider_keys_not_published_by_primary": extra_relation_keys,
            "primary_keys_missed_by_wider_search": missing_relation_keys,
            "bookkeeping_agrees_with_primary": bookkeeping_agrees,
            "primary_negative_refuted": refuted,
        }, **dumps),
        ("PASS" if f_pass else "FAIL") + " F_ACROSS_KEY_OFFSETS :: "
        + json.dumps({
            "per_pair": across,
            "total_F1_edges": across_edges,
            "total_nonzero_offset_edges": across_nonzero,
            "matches_primary": f_pass,
        }, **dumps),
    ]
    g_core = {
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
        "blocklisted_modules_loaded": [
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ],
        "firewall_hits": list(FIREWALL.hits),
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    g_prepass = (
        g_core["audit_input_paths_exist"]
        and g_core["audit_input_paths_repo_relative"]
        and not g_core["blocklisted_modules_loaded"]
        and not g_core["firewall_hits"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (controls["pass"], b_pass, c_pass, d_pass, e_pass, f_pass)
    stdout_bytes = 0
    for _ in range(4):
        g_core["stdout_bytes"] = stdout_bytes
        g_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True
        )
        g_line = (
            ("PASS" if g_prepass and g_core["stdout_under_150KB"] else "FAIL")
            + " G_CONTROLS :: " + json.dumps(g_core, **dumps)
        )
        stdout_bytes = len(
            ("\n".join(lines + [g_line, "CYCLE869_INDEPENDENT_CHECK_PASS"]) + "\n")
            .encode()
        )
    g_core["stdout_bytes"] = stdout_bytes
    g_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    g_pass = g_prepass and g_core["stdout_under_150KB"]
    g_line = ("PASS" if g_pass else "FAIL") + " G_CONTROLS :: " + json.dumps(
        g_core, **dumps
    )
    final = (
        "CYCLE869_INDEPENDENT_CHECK_PASS" if all(verdicts) and g_pass
        else "CYCLE869_INDEPENDENT_CHECK_REFUTES_PRIMARY"
        if refuted else "CYCLE869_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    print("\n".join(lines + [g_line, final]))
    return 0 if all(verdicts) and g_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
