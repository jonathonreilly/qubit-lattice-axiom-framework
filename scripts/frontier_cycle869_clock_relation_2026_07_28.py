#!/usr/bin/env python3
"""Cycle 869: the local-clock relation theory on the B=3 substrate.

Cycle 866 reported that at B=3/4 the bank-pair synchronisation cadences
fragment: every pair carries its own signature and no global record-time
exists.  This runner does not reuse that claim; it rebuilds the substrate
from the tracked Cycle-719 controller core and asks the next question.

    Given that each bank-pair carries its OWN clock, is there a LAWFUL
    RELATION between those local clocks -- an exact dictionary carrying
    one pair's cadence onto another's, within a key and across keys?

Two clock levels are measured, both from single-bit ``pack_state`` probes of
the watched registers:

  L1  bank clock      -- ticks at which bank b alone is clean
  L2  pair clock      -- ticks at which banks i and j are jointly clean
                         (this is the Cycle-866 "sync cadence")

The transformation family F is DECLARED UP FRONT (see FAMILY) and is the
only thing this runner searches.  A relation found inside F is reported with
an exactly re-verified witness; exhaustion of F is reported as a priced
negative naming F, its parameter ranges, and its declared search caps.

Every gate in this runner tests STRUCTURE (well-formedness, definitional
identities, re-verification of witnesses, positive and negative controls on
the tests themselves).  No gate tests for a preferred verdict: the relation
verdict is computed from the measured corpus and is not compared against any
expected value.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as C719


A = C719.A
B = C719.B
M = C719.M
R3 = C719.R3

# ---------------------------------------------------------------- declared box
FIXTURE_BANKS = 3
STATIONS = 19
HORIZON_CHUNKS = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
EXPECTED_PLACEMENTS = 152
EXPECTED_KEYS = EXPECTED_PLACEMENTS * EVENT_COUNT
BANK_PAIRS = tuple(combinations(range(FIXTURE_BANKS), 2))

RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

# Declared storage / search caps.  Every cap is reported with a saturation
# counter so a cap that bites can never be mistaken for an absence of data.
CADENCE_STORE_CAP = HORIZON_CHUNKS + 1        # ticks 0..H inclusive
PERIOD_TAIL_WINDOW = 2_048                    # longest tail fed to the ladder
PERIOD_TAIL_FLOOR = 16                        # shortest tail on the ladder
PERIOD_MAX_BLOCK_GAPS = 512
MIN_SATURATION_RUN = 8                        # consecutive ticks to call it saturated
WINDOWED_OFFSET_ANCHORS = 8                   # head/tail anchors for F1W search
MIN_LAG_OVERLAP = 8                           # non-vacuity floor for F3
PARTIAL_COVERAGE_FLOOR = Fraction(1, 2)       # F3P must explain half a clock
MIN_PERIOD_REPEATS = 2                        # full repeats required for F4
ACROSS_KEY_REP_CAP = 600                      # distinct gap words compared
WITNESS_PRINT_CAP = 4
SAMPLE_PRINT_CAP = 6

FAMILY = (
    "F1  CONSTANT_TIME_OFFSET      Y = X + c exactly, as sets, over the whole "
    "horizon.  Witness c in [-H,H].",
    "F1W WINDOWED_TIME_OFFSET      the WHOLE of Y lies inside the window "
    "[max(0,c), min(H,H+c)] in which a shift by c is fully observed, and there "
    "Y = (X + c).  X may carry extra events that the shift pushes outside the "
    "horizon; Y may not.  Candidate c drawn from differences of the first/last "
    f"{WINDOWED_OFFSET_ANCHORS} events of each cadence, plus c=0.",
    "F2A TICK_AFFINE               |X| = |Y| >= 3 and y_n = a*x_n + b for all "
    "n with a a positive rational, b rational; a != 1 (a = 1 is F1).  Witness "
    "(a,b) solved from the endpoints and re-verified exactly in Fraction "
    "arithmetic on every event.",
    "F2B INDEX_AFFINE              Y is the arithmetic-index subsequence "
    "y_n = x_{s*n + r} of X, s >= 1, r >= 0, run to exhaustion "
    "(r + s*|Y| >= |X|), so Y is exactly reconstructible from X and (s,r).",
    "F3  INDEX_LAG_PLUS_OFFSET     y_n = x_{n+L} + d for every n in [0,|Y|), "
    f"with |Y| >= {MIN_LAG_OVERLAP}.  This is periodic interleaving with lag: "
    "Y's whole gap word is a contiguous factor of X's at lag L, replayed at "
    "time offset d.  Witness (L,d).",
    "F3P PARTIAL_LAG_OVERLAP       the same map as F3 but on a PARTIAL "
    "overlap: y_n = x_{n+L} + d holds on a contiguous run of at least "
    f"{MIN_LAG_OVERLAP} events covering at least "
    f"{PARTIAL_COVERAGE_FLOOR.numerator}/{PARTIAL_COVERAGE_FLOOR.denominator} "
    "of the shorter clock, with the rest of both clocks unexplained.  F3P is "
    "reported as a PARTIAL match, never as a dictionary: it does not carry one "
    "whole cadence onto another.  Witness (L,d,overlap,coverage).",
    "F4  PERIODIC_RESIDUE_LAW      Beyond their transients both cadences are "
    "unions of residue classes modulo one common period P, and the residue "
    "sets differ by a rotation: R_Y = R_X + c (mod P).  Neither clock may be "
    "SATURATED, and both residue sets must be PROPER subsets of Z_P.  The "
    "block is read off the tail window and the transient is then pushed back "
    "as far as the gap word allows, so the least transient is found exactly "
    "rather than picked off a ladder.  F4 is a TAIL law by construction: it is "
    "insensitive to any edit before the transient, because the transient is "
    "free to move past it while enough whole periods survive.  Witness "
    "(P,c,transients).",
)
SATURATION_NOTE = (
    "A clock is SATURATED when it is clean at every chunk boundary from some "
    "tick through the horizon.  The test is exact and cap-free -- the maximal "
    "run of consecutive ticks ending at the horizon, at least "
    f"{8} long -- so no declared cap can hide or invent one.  Two saturated "
    "clocks agree on their common tail by construction, so that agreement is "
    "classified TRIVIAL_SATURATION and never counted as a relation."
)
EVIDENCE_FLOOR = 8
EVIDENCE_NOTE = (
    f"A relation is SUBSTANTIVE when the shorter of the two clocks carries at "
    f"least {EVIDENCE_FLOOR} events, and THIN otherwise.  Thin relations are "
    "reported but kept out of the headline coverage figure."
)
FAMILY_CLOSURE = (
    "F is searched in the order F1, F1W, F2A, F2B, F3, F3P, F4 and the first "
    "member that holds is reported.  NO_RELATION_IN_F means every member was "
    "searched over its declared parameter range and refused a witness; it is "
    "a negative priced to F and its caps, not a claim about all conceivable "
    "transformations."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------- substrate
def separated_placements(stations=STATIONS, size=TOKEN_K):
    """All size-``size`` station subsets with no cyclically adjacent pair."""
    rows = []
    for positions in combinations(range(stations), size):
        occupied = set(positions)
        if any((position + 1) % stations in occupied for position in positions):
            continue
        rows.append(positions)
    return tuple(rows)


def event_seeds(program):
    """Build the alternating-direction endpoint events; certify the allocator."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    state = M.pack_state(banks, links)
    seeds = []
    failures = 0
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, a_tokens, b_tokens, _trace = C719.run_orbit(before, program)
        expected = A.apply_semantic(before, M.global_allocator_word(FIXTURE_BANKS))
        failures += after != expected
        failures += a_tokens != (1,) + (0,) * (len(program) - 1)
        failures += any(b_tokens)
        seeds.append(before)
        state = after
    return tuple(seeds), failures


def census_initial_states(program, seeds, placements):
    """Literal (event, positions) census produced by ``run_orbit``."""
    keys = []
    states = []
    token_failures = 0
    for event, seed in enumerate(seeds):
        for positions in placements:
            state, a_tokens, b_tokens, _trace = C719.run_orbit(
                seed, program, token_positions=positions
            )
            keys.append((event, positions))
            states.append(state)
            token_failures += (
                tuple(index for index, bit in enumerate(a_tokens) if bit) != positions
            )
            token_failures += any(b_tokens)
    return tuple(keys), tuple(states)


def single_bit_location(zero_banks, zero_links, *, bank=None, link=None, wire):
    """Locate one logical coordinate by the required ``pack_state`` probe."""
    banks = [list(row) for row in zero_banks]
    links = [list(row) for row in zero_links]
    if bank is not None:
        banks[bank][wire] = 1
    else:
        links[link][wire] = 1
    packed = M.pack_state(
        tuple(tuple(row) for row in banks), tuple(tuple(row) for row in links)
    )
    locations = tuple(index for index, bit in enumerate(packed) if bit)
    if len(locations) != 1:
        raise AssertionError((bank, link, wire, locations))
    return locations[0]


def watched_layout():
    """Per-bank watched coordinate sets plus the shared SOURCE_POINTER."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (
        A.POINTER,
        A.U_TO_V,
        A.V_TO_U,
        A.DIRECTION_OK,
        *A.FRESH,
        *A.ZERO_WORK,
        A.TOKEN_OK,
    )
    per_bank = {}
    for bank in range(FIXTURE_BANKS):
        per_bank[bank] = tuple(sorted(
            single_bit_location(zero_banks, zero_links, bank=bank, wire=wire)
            for wire in local
        ))
    return per_bank, R3.X.SOURCE_POINTER, len(local)


def transpose_states(states, duplicate_source=0):
    """Bit-slice the census into per-coordinate lane planes; add a replay lane."""
    width = len(states[0])
    planes = [0] * width
    for lane, state in enumerate(states):
        lane_bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= lane_bit
    duplicate_bit = 1 << len(states)
    for wire, value in enumerate(states[duplicate_source]):
        if value:
            planes[wire] |= duplicate_bit
    return planes


def station_masks(keys, duplicate_source=0):
    """Per-phase, per-station lane masks for the circulating token sets."""
    masks = [[0] * STATIONS for _ in range(STATIONS)]
    for lane, (_event, positions) in enumerate(keys):
        bit = 1 << lane
        for phase in range(STATIONS):
            for start in positions:
                masks[phase][(start + phase) % STATIONS] |= bit
    duplicate_bit = 1 << len(keys)
    for phase in range(STATIONS):
        for start in keys[duplicate_source][1]:
            masks[phase][(start + phase) % STATIONS] |= duplicate_bit
    return tuple(tuple(row) for row in masks)


def iter_mask(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def short_key(key):
    event, positions = key
    return f"e{event}p{'.'.join(str(position) for position in positions)}"


# --------------------------------------------------------- transformation family
def gaps_of(cadence):
    return tuple(
        cadence[index + 1] - cadence[index] for index in range(len(cadence) - 1)
    )


def gap_word(gaps):
    """Delimiter-bounded encoding so ``str.find`` only matches on gap borders."""
    return "|" + "|".join(str(gap) for gap in gaps) + "|"


def kmp_border(sequence):
    """Longest proper border length of ``sequence`` (KMP failure value)."""
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


def saturation_profile(cadence, horizon=HORIZON_CHUNKS):
    """Exact, cap-free saturation test.

    A clock is SATURATED when it is clean at every chunk boundary from some
    tick through the horizon.  This is decided by measuring the maximal run of
    consecutive ticks ending at the last event -- no period search, no
    transient cap, so no declared cap can hide or invent a saturated clock.
    """
    if not cadence or cadence[-1] != horizon:
        return None
    start = len(cadence) - 1
    while start and cadence[start - 1] == cadence[start] - 1:
        start -= 1
    run = len(cadence) - start
    if run < MIN_SATURATION_RUN:
        return None
    return {
        "saturated_from_tick": cadence[start],
        "consecutive_run": run,
        "runs_to_horizon": True,
    }


def period_profile(cadence):
    """Least eventual time period of a cadence, or ``None``.

    The block is read off the TAIL window -- the eventual behaviour is what a
    period claims -- and the transient is then pushed back as far as the gap
    word allows.  This is O(len) and finds the least transient exactly, so the
    result does not depend on any transient-offset ladder.
    """
    gaps = gaps_of(cadence)
    if len(gaps) < MIN_PERIOD_REPEATS:
        return None
    # Halving ladder of tail lengths.  A single fixed tail would swallow the
    # transient whenever the cadence is short, and would then report no period
    # at all; the ladder lets the block be read off a tail that excludes it.
    best = None
    length = min(len(gaps), PERIOD_TAIL_WINDOW)
    while length >= min(PERIOD_TAIL_FLOOR, len(gaps)):
        tail = gaps[-length:]
        block = len(tail) - kmp_border(tail)
        if block and block <= PERIOD_MAX_BLOCK_GAPS \
                and len(tail) >= MIN_PERIOD_REPEATS * block:
            period = sum(tail[:block])
            if period > 0 and (best is None or period < best[0]):
                best = (period, block)
        if length == 1:
            break
        length //= 2
    if best is None:
        return None
    period, block = best
    transient = len(gaps) - block
    while transient and gaps[transient - 1] == gaps[transient - 1 + block]:
        transient -= 1
    if len(gaps) - transient < MIN_PERIOD_REPEATS * block:
        return None
    best = {
        "period_ticks": period,
        "block_gaps": block,
        "transient_events": transient,
        "transient_tick": cadence[transient],
        "repeats": (len(gaps) - transient) // block,
        "tail_window": min(len(gaps), PERIOD_TAIL_WINDOW),
    }
    stable = tuple(tick for tick in cadence if tick >= best["transient_tick"])
    best["residues"] = tuple(sorted({tick % period for tick in stable}))
    best["residue_count"] = len(best["residues"])
    best["saturated"] = len(best["residues"]) == period
    window_hi = max(stable) - period
    lower = {tick for tick in stable if tick <= window_hi}
    upper = {tick for tick in stable if tick >= best["transient_tick"] + period}
    best["shift_exact_on_window"] = {tick + period for tick in lower} == upper
    return best


def cadence_profile(cadence):
    gaps = gaps_of(cadence)
    return {
        "length": len(cadence),
        "first": cadence[0] if cadence else None,
        "last": cadence[-1] if cadence else None,
        "gaps": gaps,
        "word": gap_word(gaps),
        "index": {tick: position for position, tick in enumerate(cadence)},
        "period": period_profile(cadence) if len(cadence) >= MIN_LAG_OVERLAP else None,
        "saturation": saturation_profile(cadence),
        "ticks": cadence,
    }


def f1_constant_offset(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if not x or len(x) != len(y):
        return None
    offset = y[0] - x[0]
    if any(right - left != offset for left, right in zip(x, y)):
        return None
    return {"member": "F1", "c": offset}


def f1w_windowed_offset(x_profile, y_profile, horizon):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if not x or not y:
        return None
    anchors = WINDOWED_OFFSET_ANCHORS
    candidates = {0}
    for left in x[:anchors] + x[-anchors:]:
        for right in y[:anchors] + y[-anchors:]:
            candidates.add(right - left)
    x_set, y_set = set(x), set(y)
    for offset in sorted(candidates, key=lambda value: (abs(value), value)):
        if abs(offset) > horizon:
            continue
        low = max(0, offset)
        high = min(horizon, horizon + offset)
        if high <= low:
            continue
        # The whole of Y must sit inside the observable window; only X is
        # allowed to carry events the shift pushes out of [0,H].
        if y[0] < low or y[-1] > high:
            continue
        shifted = {tick + offset for tick in x_set if low <= tick + offset <= high}
        if shifted != y_set:
            continue
        return {
            "member": "F1W",
            "c": offset,
            "window": [low, high],
            "events_in_window": len(y_set),
        }
    return None


def f2a_tick_affine(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if len(x) != len(y) or len(x) < 3 or x[-1] == x[0]:
        return None
    slope = Fraction(y[-1] - y[0], x[-1] - x[0])
    if slope <= 0 or slope == 1:
        return None
    intercept = Fraction(y[0]) - slope * x[0]
    for left, right in zip(x, y):
        if slope * left + intercept != right:
            return None
    return {
        "member": "F2A",
        "a_num": slope.numerator,
        "a_den": slope.denominator,
        "b_num": intercept.numerator,
        "b_den": intercept.denominator,
    }


def f2b_index_affine(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    lookup = x_profile["index"]
    if len(y) < 2 or len(x) < 2 or y[0] not in lookup or y[1] not in lookup:
        return None
    start = lookup[y[0]]
    step = lookup[y[1]] - start
    if step < 1:
        return None
    if step == 1 and start == 0 and len(x) == len(y):
        return None  # identity re-indexing; F1 already owns this shape
    if start + step * len(y) < len(x):
        return None  # not run to exhaustion: Y would not be reconstructible
    for ordinal, tick in enumerate(y):
        position = start + step * ordinal
        if position >= len(x) or x[position] != tick:
            return None
    return {"member": "F2B", "s": step, "r": start}


def f3_lag_offset(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if len(y) < MIN_LAG_OVERLAP or len(x) < len(y):
        return None
    position = x_profile["word"].find(y_profile["word"])
    if position < 0:
        return None
    lag = x_profile["word"].count("|", 0, position + 1) - 1
    if lag < 0 or lag + len(y) > len(x):
        return None
    shift = y[0] - x[lag]
    for ordinal, tick in enumerate(y):
        if x[lag + ordinal] + shift != tick:
            return None
    return {"member": "F3", "L": lag, "d": shift, "overlap": len(y)}


def f3p_partial_lag(x_profile, y_profile):
    """Lag map on a partial overlap, in either index direction.

    This is deliberately the most permissive member of F.  It is reported
    separately from F3 because a map that explains only part of a clock is a
    partial match, not a dictionary.
    """
    x, y = x_profile["ticks"], y_profile["ticks"]
    shorter = min(len(x), len(y))
    if shorter < MIN_LAG_OVERLAP:
        return None
    floor = max(
        MIN_LAG_OVERLAP,
        -(-shorter * PARTIAL_COVERAGE_FLOOR.numerator
          // PARTIAL_COVERAGE_FLOOR.denominator),
    )
    for lag in range(-(len(y) - 1), len(x)):
        start = max(0, -lag)
        stop = min(len(y), len(x) - lag)
        if stop - start < floor:
            continue
        shift = y[start] - x[start + lag]
        if x[start + 1 + lag] + shift != y[start + 1]:
            continue
        if all(x[index + lag] + shift == y[index]
               for index in range(start, stop)):
            coverage = Fraction(stop - start, shorter)
            return {
                "member": "F3P",
                "L": lag,
                "d": shift,
                "overlap": stop - start,
                "coverage": f"{coverage.numerator}/{coverage.denominator}",
                "partial": start > 0 or stop < len(y),
            }
    return None


def f4_periodic_residue(x_profile, y_profile):
    left, right = x_profile["period"], y_profile["period"]
    if left is None or right is None:
        return None
    if not (left["shift_exact_on_window"] and right["shift_exact_on_window"]):
        return None
    if x_profile["saturation"] or y_profile["saturation"]:
        return None  # no cadence to relate; reported as TRIVIAL_SATURATION
    if left["saturated"] or right["saturated"]:
        return None
    period = left["period_ticks"]
    if period != right["period_ticks"]:
        return None
    source, target = set(left["residues"]), set(right["residues"])
    if len(source) != len(target) or not source:
        return None
    for anchor in sorted(source):
        offset = (min(target) - anchor) % period
        if {(value + offset) % period for value in source} == target:
            return {
                "member": "F4",
                "P": period,
                "c": offset,
                "transient_X": left["transient_tick"],
                "transient_Y": right["transient_tick"],
                "residue_count": len(source),
            }
    return None


FULL_MEMBERS = ("F1", "F1W", "F2A", "F2B", "F3", "F4")
PARTIAL_MEMBERS = ("F3P",)


def relate(x_profile, y_profile, horizon=HORIZON_CHUNKS, allow_partial=True):
    """First member of the declared family F carrying X onto Y, else None.

    ``allow_partial=False`` restricts the search to the members that carry a
    WHOLE cadence onto another; the partial member F3P is then skipped.
    """
    if not x_profile["ticks"] or not y_profile["ticks"]:
        return None
    tests = [
        lambda: f1_constant_offset(x_profile, y_profile),
        lambda: f1w_windowed_offset(x_profile, y_profile, horizon),
        lambda: f2a_tick_affine(x_profile, y_profile),
        lambda: f2b_index_affine(x_profile, y_profile),
        lambda: f3_lag_offset(x_profile, y_profile),
    ]
    if allow_partial:
        tests.append(lambda: f3p_partial_lag(x_profile, y_profile))
    tests.append(lambda: f4_periodic_residue(x_profile, y_profile))
    for test in tests:
        found = test()
        if found is not None:
            return found
    return None


def apply_witness(x_profile, witness):
    """Re-derive Y from X and the witness alone; None when not reconstructible."""
    x = x_profile["ticks"]
    member = witness["member"]
    if member == "F1":
        return tuple(tick + witness["c"] for tick in x)
    if member == "F2A":
        slope = Fraction(witness["a_num"], witness["a_den"])
        intercept = Fraction(witness["b_num"], witness["b_den"])
        rebuilt = []
        for tick in x:
            value = slope * tick + intercept
            if value.denominator != 1:
                return None
            rebuilt.append(int(value))
        return tuple(rebuilt)
    if member == "F2B":
        step, start = witness["s"], witness["r"]
        rebuilt = []
        position = start
        while position < len(x):
            rebuilt.append(x[position])
            position += step
        return tuple(rebuilt)
    if member == "F3":
        lag, shift, overlap = witness["L"], witness["d"], witness["overlap"]
        return tuple(x[lag + ordinal] + shift for ordinal in range(overlap))
    return None


def verify_witness(x_profile, y_profile, witness):
    """Exact re-verification of a reported witness, independent of the search."""
    member = witness["member"]
    rebuilt = apply_witness(x_profile, witness)
    if rebuilt is not None:
        if member == "F2B":
            return rebuilt == y_profile["ticks"]
        return rebuilt == y_profile["ticks"]
    if member == "F1W":
        low, high = witness["window"]
        offset = witness["c"]
        left = {tick + offset for tick in x_profile["ticks"]
                if low - offset <= tick <= high - offset}
        right = {tick for tick in y_profile["ticks"] if low <= tick <= high}
        return left == right and bool(right)
    if member == "F3P":
        source_ticks = x_profile["ticks"]
        lag, shift, overlap = witness["L"], witness["d"], witness["overlap"]
        start = max(0, -lag)
        rebuilt = tuple(
            source_ticks[start + lag + ordinal] + shift
            for ordinal in range(overlap)
        )
        return rebuilt == y_profile["ticks"][start:start + overlap]
    if member == "F4":
        period, offset = witness["P"], witness["c"]
        left = x_profile["period"]
        right = y_profile["period"]
        if left is None or right is None or left["period_ticks"] != period:
            return False
        mapped = {(value + offset) % period for value in left["residues"]}
        return mapped == set(right["residues"])
    return False


# --------------------------------------------------------------------- controls
def family_controls(sample_profiles):
    """Positive and negative controls on the tests themselves.

    Positive: synthetic images built by each family member must be accepted
    with the constructed witness.  Negative: a one-tick perturbation of a real
    cadence must be refused by every member.  These gates prove the family can
    say YES when a relation exists and NO when it does not; they say nothing
    about the measured corpus.
    """
    rows = []
    for name, source in sample_profiles:
        base = source["ticks"]
        if len(base) < max(MIN_LAG_OVERLAP + 4, 12):
            continue
        checks = {}
        source_gap_values = set(source["gaps"])

        shifted = cadence_profile(tuple(tick + 7 for tick in base))
        found = relate(source, shifted)
        checks["F1_positive"] = bool(
            found and found["member"] == "F1" and found["c"] == 7
            and verify_witness(source, shifted, found)
        )

        scaled = cadence_profile(tuple(3 * tick + 5 for tick in base))
        found = relate(source, scaled)
        checks["F2A_positive"] = bool(
            found and found["member"] == "F2A"
            and Fraction(found["a_num"], found["a_den"]) == 3
            and Fraction(found["b_num"], found["b_den"]) == 5
            and verify_witness(source, scaled, found)
        )

        thinned = cadence_profile(base[1::3])
        found = relate(source, thinned)
        checks["F2B_positive"] = bool(
            found and found["member"] in ("F2B", "F3")
            and verify_witness(source, thinned, found)
        )

        lagged = cadence_profile(tuple(tick + 11 for tick in base[3:]))
        found = relate(source, lagged)
        checks["F3_positive"] = bool(
            found and verify_witness(source, lagged, found)
        )

        # Negative 1: shift one interior tick by a delta that manufactures two
        # gap values absent from X, so the perturbed gap word provably cannot
        # be a factor of X's and no member of F can hold.
        perturbed = None
        centre = len(base) // 2
        order = sorted(
            range(1, len(base) - 1), key=lambda index: abs(index - centre)
        )
        for middle in order:
            for delta in range(1, 65):
                left_gap = base[middle] - base[middle - 1] + delta
                right_gap = base[middle + 1] - base[middle] - delta
                if right_gap < 1:
                    break
                if left_gap in source_gap_values or right_gap in source_gap_values:
                    continue
                broken = list(base)
                broken[middle] += delta
                perturbed = cadence_profile(tuple(broken))
                break
            if perturbed is not None:
                break
        if perturbed is not None:
            # The exact whole-cadence members must all refuse.  F4 is a tail
            # law and may legitimately survive an edit before its transient --
            # but only by MOVING that transient past the edit, which is checked.
            exact = [
                f1_constant_offset(source, perturbed),
                f1w_windowed_offset(source, perturbed, HORIZON_CHUNKS),
                f2a_tick_affine(source, perturbed),
                f2b_index_affine(source, perturbed),
                f3_lag_offset(source, perturbed),
            ]
            residue = f4_periodic_residue(source, perturbed)
            partial = f3p_partial_lag(source, perturbed)
            checks["negative_one_tick_perturbation_refused_by_exact_members"] = (
                perturbed["ticks"] != base and not any(exact)
            )
            checks["negative_perturbation_F4_only_by_moving_its_transient"] = (
                residue is None
                or residue["transient_Y"] > residue["transient_X"]
            )
            checks["negative_one_tick_perturbation_partial_is_identity_only"] = (
                partial is None or partial["d"] == 0
            )

        # Negative 1b: an edit inside the final period leaves no periodic tail
        # for F4 to retreat to, so the tail law must refuse it outright.
        tail_broken = None
        last = len(base) - 2
        for delta in range(1, 65):
            if base[last] + delta >= base[last + 1]:
                break
            left_gap = base[last] - base[last - 1] + delta
            right_gap = base[last + 1] - base[last] - delta
            if left_gap in source_gap_values or right_gap in source_gap_values:
                continue
            broken = list(base)
            broken[last] += delta
            tail_broken = cadence_profile(tuple(broken))
            break
        if tail_broken is not None:
            checks["negative_tail_edit_refused_by_F4"] = (
                f4_periodic_residue(source, tail_broken) is None
            )

        # Negative 2: triangular-index thinning is neither an arithmetic index
        # map nor a contiguous gap-word factor.
        indices = []
        step = 0
        position = 0
        while position < len(base):
            indices.append(position)
            step += 1
            position += step
        if len(indices) >= 4:
            thinned_triangular = cadence_profile(tuple(base[i] for i in indices))
            # The triangular thinning must be refused by EVERY member, the
            # permissive partial one included.
            checks["negative_triangular_thinning_refused"] = (
                relate(source, thinned_triangular) is None
                and relate(thinned_triangular, source) is None
            )

        rows.append({"clock": name, **checks})
        if len(rows) >= 3:
            break
    required = (
        "F1_positive",
        "F2A_positive",
        "F2B_positive",
        "F3_positive",
        "negative_one_tick_perturbation_refused_by_exact_members",
        "negative_perturbation_F4_only_by_moving_its_transient",
        "negative_one_tick_perturbation_partial_is_identity_only",
        "negative_tail_edit_refused_by_F4",
        "negative_triangular_thinning_refused",
    )
    passed = (
        bool(rows)
        and all(
            all(value for label, value in row.items() if label != "clock")
            for row in rows
        )
        # Every declared control must be constructible on at least one clock:
        # a control that never ran must not pass by absence.
        and all(any(label in row for row in rows) for label in required)
    )
    return rows, passed


# ----------------------------------------------------------------------- report
def main():
    started = time.monotonic()
    program = C719.interleaved_program(FIXTURE_BANKS)
    placements = separated_placements()
    seeds, allocator_failures = event_seeds(program)
    keys, states = census_initial_states(program, seeds, placements)
    per_bank_watched, source_pointer, local_wire_count = watched_layout()
    schedules = tuple(C719.mapped_macro(row) for row in program)

    setup = {
        "fixture_banks": FIXTURE_BANKS,
        "program_stations": len(program),
        "token_k": TOKEN_K,
        "events": EVENT_COUNT,
        "separated_placements": len(placements),
        "census_keys": len(keys),
        "state_width": len(states[0]) if states else 0,
        "watched_wires_per_bank": local_wire_count,
        "source_pointer_coordinate": source_pointer,
        "horizon_chunks": HORIZON_CHUNKS,
        "bank_pairs": [list(pair) for pair in BANK_PAIRS],
        "allocator_failures": allocator_failures,
    }
    structural_ok = (
        len(program) == STATIONS
        and len(placements) == EXPECTED_PLACEMENTS
        and len(keys) == EXPECTED_KEYS
        and allocator_failures == 0
        and all(len(row) == local_wire_count for row in per_bank_watched.values())
        and all(
            not (set(per_bank_watched[left]) & set(per_bank_watched[right]))
            for left, right in BANK_PAIRS
        )
        and all(
            source_pointer not in set(per_bank_watched[bank])
            for bank in range(FIXTURE_BANKS)
        )
    )
    if not structural_ok:
        print("FAIL A_SUBSTRATE :: " + compact(setup))
        return 1

    lane_count = len(keys)
    planes = transpose_states(states)
    masks = station_masks(keys)
    census_mask = (1 << lane_count) - 1
    evolution_mask = (1 << (lane_count + 1)) - 1
    duplicate_lane = lane_count

    bank_clocks = [[[] for _ in range(FIXTURE_BANKS)] for _ in range(lane_count)]
    pair_clocks = [[[] for _ in BANK_PAIRS] for _ in range(lane_count)]
    duplicate_bank_clocks = [[] for _ in range(FIXTURE_BANKS)]
    duplicate_pair_clocks = [[] for _ in BANK_PAIRS]
    duplicate_mismatches = 0
    store_saturations = 0
    bank_clean_totals = [0] * FIXTURE_BANKS
    pair_clean_totals = [0] * len(BANK_PAIRS)
    watched_by_bank = tuple(per_bank_watched[bank] for bank in range(FIXTURE_BANKS))

    def observe(tick):
        nonlocal duplicate_mismatches, store_saturations
        source_dirty = planes[source_pointer]
        clean = []
        for bank in range(FIXTURE_BANKS):
            dirty = source_dirty
            for wire in watched_by_bank[bank]:
                dirty |= planes[wire]
            clean.append(evolution_mask & ~dirty)
        for bank in range(FIXTURE_BANKS):
            duplicate_mismatches += (
                ((clean[bank] >> 0) & 1) != ((clean[bank] >> duplicate_lane) & 1)
            )
            if (clean[bank] >> duplicate_lane) & 1:
                duplicate_bank_clocks[bank].append(tick)
            mask = clean[bank] & census_mask
            bank_clean_totals[bank] += mask.bit_count()
            for lane in iter_mask(mask):
                row = bank_clocks[lane][bank]
                if len(row) < CADENCE_STORE_CAP:
                    row.append(tick)
                else:
                    store_saturations += 1
        for index, (left, right) in enumerate(BANK_PAIRS):
            if (clean[left] >> duplicate_lane) & (clean[right] >> duplicate_lane) & 1:
                duplicate_pair_clocks[index].append(tick)
            mask = clean[left] & clean[right] & census_mask
            pair_clean_totals[index] += mask.bit_count()
            for lane in iter_mask(mask):
                row = pair_clocks[lane][index]
                if len(row) < CADENCE_STORE_CAP:
                    row.append(tick)
                else:
                    store_saturations += 1

    observe(0)
    for tick in range(1, HORIZON_CHUNKS + 1):
        phase = (tick - 1) % STATIONS
        phase_masks = masks[phase]
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

    bank_cadences = tuple(
        tuple(tuple(row) for row in lane) for lane in bank_clocks
    )
    pair_cadences = tuple(
        tuple(tuple(row) for row in lane) for lane in pair_clocks
    )

    # Definitional identity: a pair clock is the intersection of its bank clocks.
    intersection_failures = 0
    monotone_failures = 0
    horizon_failures = 0
    for lane in range(lane_count):
        for bank in range(FIXTURE_BANKS):
            row = bank_cadences[lane][bank]
            monotone_failures += any(
                row[i] >= row[i + 1] for i in range(len(row) - 1)
            )
            horizon_failures += any(not 0 <= tick <= HORIZON_CHUNKS for tick in row)
        for index, (left, right) in enumerate(BANK_PAIRS):
            expected = tuple(sorted(
                set(bank_cadences[lane][left]) & set(bank_cadences[lane][right])
            ))
            intersection_failures += expected != pair_cadences[lane][index]

    bank_profiles = tuple(
        tuple(cadence_profile(row) for row in lane) for lane in bank_cadences
    )
    pair_profiles = tuple(
        tuple(cadence_profile(row) for row in lane) for lane in pair_cadences
    )

    corpus_digest = digest({
        "bank": [[list(row) for row in lane] for lane in bank_cadences],
        "pair": [[list(row) for row in lane] for lane in pair_cadences],
    })

    # 135 silent and 135 saturated pair clocks is a numeric coincidence, not a
    # double count: a silent clock has no events and therefore no period.
    silent_and_saturated = sum(
        1 for lane in pair_profiles for profile in lane
        if not profile["ticks"] and profile["saturation"] is not None
    )
    b_pass = (
        silent_and_saturated == 0
        and intersection_failures == 0
        and monotone_failures == 0
        and horizon_failures == 0
        and store_saturations == 0
        and sum(bank_clean_totals) == sum(
            len(row) for lane in bank_cadences for row in lane
        )
        and sum(pair_clean_totals) == sum(
            len(row) for lane in pair_cadences for row in lane
        )
    )

    empty_bank = sum(
        1 for lane in bank_cadences for row in lane if not row
    )
    empty_pair = sum(
        1 for lane in pair_cadences for row in lane if not row
    )
    bank_length_histogram = Counter(
        len(row) for lane in bank_cadences for row in lane
    )
    pair_length_histogram = Counter(
        len(row) for lane in pair_cadences for row in lane
    )
    def periodic_census(profiles):
        periodic = saturated = 0
        periods = Counter()
        for lane in profiles:
            for profile in lane:
                if profile["saturation"] is not None:
                    saturated += 1
                period = profile["period"]
                if period is None or not period["shift_exact_on_window"]:
                    continue
                periodic += 1
                if not period["saturated"] and profile["saturation"] is None:
                    periods[period["period_ticks"]] += 1
        return periodic, saturated, dict(sorted(periods.items()))

    periodic_pair_clocks, saturated_pair_clocks, pair_period_hist = periodic_census(
        pair_profiles
    )
    periodic_bank_clocks, saturated_bank_clocks, bank_period_hist = periodic_census(
        bank_profiles
    )

    # Is a pair clock ever more than the sparser of its two bank clocks?  If a
    # pair clock equals one bank clock outright, that bank gates the pair and
    # the "pair clock" carries no joint information.
    domination = Counter()
    for lane in range(lane_count):
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

    sample_rows = []
    for lane in range(lane_count):
        if len(sample_rows) >= SAMPLE_PRINT_CAP:
            break
        if min(len(row) for row in pair_cadences[lane]) < 4:
            continue
        sample_rows.append({
            "key": short_key(keys[lane]),
            "bank_clock_lengths": [len(row) for row in bank_cadences[lane]],
            "pair_clock_lengths": [len(row) for row in pair_cadences[lane]],
            "pair_clock_heads": [list(row[:8]) for row in pair_cadences[lane]],
            "pair_periods": [
                None if profile["period"] is None else profile["period"]["period_ticks"]
                for profile in pair_profiles[lane]
            ],
        })

    control_pool = []
    for lane in range(lane_count):
        for index, profile in enumerate(pair_profiles[lane]):
            if len(profile["ticks"]) >= 24:
                control_pool.append((f"{short_key(keys[lane])}/pair{index}", profile))
        if len(control_pool) >= 6:
            break
    control_rows, controls_pass = family_controls(control_pool)

    # ------------------------------------------------- within-key comparisons
    def is_saturated(profile):
        return profile["saturation"] is not None

    def within_key_block(profiles, labels):
        verdicts = Counter()
        evidence = Counter()
        parameters = Counter()
        witnesses = []
        thin_witnesses = []
        per_key_codes = []
        witness_failures = 0
        comparable = 0
        substantive = 0
        substantive_related = 0
        for lane in range(lane_count):
            codes = []
            for left, right in combinations(range(len(labels)), 2):
                x_profile = profiles[lane][left]
                y_profile = profiles[lane][right]
                if not x_profile["ticks"] or not y_profile["ticks"]:
                    verdicts["ONE_SIDE_SILENT"] += 1
                    codes.append("0")
                    continue
                if is_saturated(x_profile) and is_saturated(y_profile):
                    verdicts["TRIVIAL_SATURATION"] += 1
                    codes.append("s")
                    continue
                comparable += 1
                shorter = min(len(x_profile["ticks"]), len(y_profile["ticks"]))
                thin = shorter < EVIDENCE_FLOOR
                if not thin:
                    substantive += 1
                found = relate(x_profile, y_profile)
                direction = "forward"
                if found is None:
                    found = relate(y_profile, x_profile)
                    direction = "reverse"
                if found is None:
                    verdicts["NO_RELATION_IN_F"] += 1
                    evidence["THIN_NO_RELATION" if thin else "SUBSTANTIVE_NO_RELATION"] += 1
                    codes.append("x")
                    continue
                source, target = (
                    (x_profile, y_profile) if direction == "forward"
                    else (y_profile, x_profile)
                )
                reverified = verify_witness(source, target, found)
                if not reverified:
                    witness_failures += 1
                verdicts[found["member"]] += 1
                full_member = found["member"] in FULL_MEMBERS
                if full_member:
                    evidence["THIN_RELATION" if thin else "SUBSTANTIVE_RELATION"] += 1
                if full_member and not thin:
                    substantive_related += 1
                # Identity-like means the map leaves the tick VALUES alone:
                # one clock is literally a sub-run of the other at the same
                # absolute times.  That is containment, not a transformation
                # law, whichever family member reports it.
                identity_like = (
                    found.get("c") == 0
                    or (found["member"] in ("F3", "F3P") and found["d"] == 0)
                    or (found["member"] == "F2B" and found["s"] == 1)
                )
                if found["member"] in PARTIAL_MEMBERS:
                    evidence["PARTIAL" if thin is False else "THIN_PARTIAL"] += 1
                    if not thin and not identity_like:
                        parameters["#SUBSTANTIVE_NONIDENTITY_PARTIAL"] += 1
                if not thin and not identity_like and found["member"] in FULL_MEMBERS:
                    parameters["#SUBSTANTIVE_NONIDENTITY"] += 1
                if found["member"] in ("F1", "F1W"):
                    parameters[f"{found['member']}:c={found['c']}"] += 1
                elif found["member"] in ("F3", "F3P"):
                    parameters[
                        f"{found['member']}:L={found['L']},d={found['d']}"
                    ] += 1
                elif found["member"] == "F4":
                    parameters[f"F4:P={found['P']},c={found['c']}"] += 1
                else:
                    parameters[found["member"]] += 1
                codes.append(
                    "w" if found["member"] == "F1W"
                    else "p" if found["member"] == "F3P"
                    else found["member"][1:2]
                )
                row = {
                    "key": short_key(keys[lane]),
                    "from": labels[left if direction == "forward" else right],
                    "to": labels[right if direction == "forward" else left],
                    "witness": found,
                    "reverified": reverified,
                    "source_length": len(source["ticks"]),
                    "target_length": len(target["ticks"]),
                }
                bucket = thin_witnesses if thin else witnesses
                if len(bucket) < WITNESS_PRINT_CAP:
                    bucket.append(row)
            per_key_codes.append(short_key(keys[lane]) + ":" + "".join(codes))
        return {
            "verdicts": dict(sorted(verdicts.items())),
            "evidence_split": dict(sorted(evidence.items())),
            "witness_parameter_histogram": dict(sorted(
                (label, count) for label, count in parameters.items()
                if not label.startswith("#")
            )),
            "substantive_nonidentity_full_dictionaries": (
                parameters["#SUBSTANTIVE_NONIDENTITY"]
            ),
            "substantive_nonidentity_partial_matches": (
                parameters["#SUBSTANTIVE_NONIDENTITY_PARTIAL"]
            ),
            "substantive_partial_matches": evidence["PARTIAL"],
            "comparable_pairs_of_clocks": comparable,
            "substantive_pairs_of_clocks": substantive,
            "substantive_relations": substantive_related,
            "witness_reverification_failures": witness_failures,
            "substantive_witness_examples": witnesses,
            "thin_witness_examples": thin_witnesses,
            "per_key_codes": per_key_codes,
        }

    pair_labels = tuple(f"{left}{right}" for left, right in BANK_PAIRS)
    bank_labels = tuple(str(bank) for bank in range(FIXTURE_BANKS))
    within_pair = within_key_block(pair_profiles, pair_labels)
    within_bank = within_key_block(bank_profiles, bank_labels)
    d_pass = (
        within_pair["witness_reverification_failures"] == 0
        and within_bank["witness_reverification_failures"] == 0
        and sum(within_pair["verdicts"].values()) == lane_count * len(BANK_PAIRS)
        and sum(within_bank["verdicts"].values()) == lane_count * FIXTURE_BANKS
        and all(
            sum(block["evidence_split"].values())
            == block["comparable_pairs_of_clocks"]
            for block in (within_pair, within_bank)
        )
    )

    # --------------------------------------------------- across-key comparisons
    def across_key_block(profiles, labels):
        blocks = {}
        cap_hits = 0
        witness_failures = 0
        for index, label in enumerate(labels):
            buckets = defaultdict(list)
            silent = 0
            for lane in range(lane_count):
                profile = profiles[lane][index]
                if not profile["ticks"]:
                    silent += 1
                    continue
                buckets[profile["word"]].append(lane)
            reps = sorted(buckets, key=lambda word: (-len(buckets[word]), word))
            capped = reps[:ACROSS_KEY_REP_CAP]
            cap_hits += len(reps) - len(capped)
            offset_classes = Counter(len(buckets[word]) for word in reps)
            # F1 across keys is exactly gap-word equality plus equal length,
            # which the gap word already encodes.  Confirm the offsets are real.
            offset_witnesses = []
            offset_values = Counter()
            zero_offset_edges = 0
            nonzero_offset_edges = 0
            for word in reps:
                lanes = buckets[word]
                if len(lanes) < 2:
                    continue
                source = profiles[lanes[0]][index]
                for lane in lanes[1:]:
                    target = profiles[lane][index]
                    found = f1_constant_offset(source, target)
                    if found is None or not verify_witness(source, target, found):
                        witness_failures += 1
                        continue
                    if found["c"]:
                        nonzero_offset_edges += 1
                        offset_values[found["c"]] += 1
                    else:
                        zero_offset_edges += 1
                if len(offset_witnesses) < WITNESS_PRINT_CAP:
                    partner = profiles[lanes[1]][index]
                    found = f1_constant_offset(source, partner)
                    if found is not None:
                        offset_witnesses.append({
                            "from_key": short_key(keys[lanes[0]]),
                            "to_key": short_key(keys[lanes[1]]),
                            "witness": found,
                            "class_size": len(lanes),
                        })
            # F3 across keys: shorter gap word a contiguous factor of a longer one.
            ordered = sorted(capped, key=len)
            factor_edges = 0
            factor_examples = []
            for position, needle in enumerate(ordered):
                needle_len = needle.count("|") - 1
                if needle_len + 1 < MIN_LAG_OVERLAP:
                    continue
                for haystack in ordered[position + 1:]:
                    if len(haystack) < len(needle):
                        continue
                    if haystack.find(needle) < 0:
                        continue
                    source = profiles[buckets[haystack][0]][index]
                    target = profiles[buckets[needle][0]][index]
                    found = f3_lag_offset(source, target)
                    if found is None:
                        continue
                    if not verify_witness(source, target, found):
                        witness_failures += 1
                        continue
                    factor_edges += 1
                    if len(factor_examples) < WITNESS_PRINT_CAP:
                        factor_examples.append({
                            "from_key": short_key(keys[buckets[haystack][0]]),
                            "to_key": short_key(keys[buckets[needle][0]]),
                            "witness": found,
                        })
            periods = Counter(
                profiles[lane][index]["period"]["period_ticks"]
                for lane in range(lane_count)
                if profiles[lane][index]["period"] is not None
                and profiles[lane][index]["period"]["shift_exact_on_window"]
            )
            blocks[label] = {
                "sounding_keys": lane_count - silent,
                "silent_keys": silent,
                "distinct_gap_words": len(reps),
                "F1_offset_classes_by_size": dict(sorted(offset_classes.items())),
                "largest_F1_class": max(offset_classes) if offset_classes else 0,
                "keys_in_nontrivial_F1_class": sum(
                    size * count for size, count in offset_classes.items() if size > 1
                ),
                "F1_offset_witnesses": offset_witnesses,
                "F1_edges_to_class_representative": zero_offset_edges
                + nonzero_offset_edges,
                "F1_edges_with_nonzero_offset": nonzero_offset_edges,
                "F1_edges_with_zero_offset_identical_cadences": zero_offset_edges,
                "F1_distinct_nonzero_offsets": len(offset_values),
                "F1_offset_extremes": (
                    [min(offset_values), max(offset_values)] if offset_values else []
                ),
                "F3_factor_edges_between_distinct_words": factor_edges,
                "F3_factor_examples": factor_examples,
                "F4_period_histogram": dict(sorted(periods.items())),
            }
        return blocks, cap_hits, witness_failures

    across_pair, pair_cap_hits, pair_witness_failures = across_key_block(
        pair_profiles, pair_labels
    )
    across_bank, bank_cap_hits, bank_witness_failures = across_key_block(
        bank_profiles, bank_labels
    )
    e_pass = (
        pair_cap_hits == 0
        and bank_cap_hits == 0
        and pair_witness_failures == 0
        and bank_witness_failures == 0
        and all(
            block["sounding_keys"] + block["silent_keys"] == lane_count
            for block in list(across_pair.values()) + list(across_bank.values())
        )
    )

    # -------------------------------------------------------------- the verdict
    # The only nondegenerate periods present, expressed in ring units.  The
    # arithmetic is computed, not asserted.
    period_arithmetic = []
    for period in sorted(set(bank_period_hist) | set(pair_period_hist)):
        row = {
            "period_ticks": period,
            "orbits": Fraction(period, STATIONS).limit_denominator(),
            "period_over_stations_squared": str(
                Fraction(period, STATIONS * STATIONS)
            ),
            "exact_multiple_of_stations": period % STATIONS == 0,
            "exact_multiple_of_stations_squared": period % (STATIONS * STATIONS) == 0,
            "bank_clocks_carrying_it": bank_period_hist.get(period, 0),
            "pair_clocks_carrying_it": pair_period_hist.get(period, 0),
        }
        row["orbits"] = str(row["orbits"])
        period_arithmetic.append(row)

    pair_totals = within_pair["verdicts"]
    comparable = within_pair["comparable_pairs_of_clocks"]
    related = comparable - pair_totals.get("NO_RELATION_IN_F", 0)
    substantive = within_pair["substantive_pairs_of_clocks"]
    substantive_related = within_pair["substantive_relations"]
    coverage = Fraction(substantive_related, substantive) if substantive else Fraction(0)
    unrelated_across = sum(
        block["sounding_keys"] - block["keys_in_nontrivial_F1_class"]
        for block in across_pair.values()
    )
    substantive_nonidentity = within_pair["substantive_nonidentity_full_dictionaries"]
    substantive_partial = within_pair["substantive_partial_matches"]
    substantive_partial_nonidentity = within_pair[
        "substantive_nonidentity_partial_matches"
    ]
    if substantive and substantive_related == substantive:
        relation_verdict = "DICTIONARY_TOTAL_WITHIN_KEY"
    elif substantive_related == 0:
        relation_verdict = "FAMILY_EXHAUSTED_NO_SUBSTANTIVE_RELATION"
    elif substantive_nonidentity == 0:
        relation_verdict = "COINCIDENCE_ONLY_NO_TRANSFORMATION_LAW_WITHIN_KEY"
    else:
        relation_verdict = "DICTIONARY_SPARSE_WITHIN_KEY"
    cross_key_nonzero = sum(
        block["F1_edges_with_nonzero_offset"] for block in across_pair.values()
    )
    cross_key_edges = sum(
        block["F1_edges_to_class_representative"] for block in across_pair.values()
    )
    if all(block["largest_F1_class"] <= 1 for block in across_pair.values()) and all(
        block["F3_factor_edges_between_distinct_words"] == 0
        for block in across_pair.values()
    ):
        across_verdict = "NO_CROSS_KEY_DICTIONARY"
    elif cross_key_nonzero == 0:
        across_verdict = "CROSS_KEY_COINCIDENCE_ONLY"
    else:
        across_verdict = "CROSS_KEY_TIME_TRANSLATION_DICTIONARY"
    pricing = {
        "family": list(FAMILY),
        "closure": FAMILY_CLOSURE,
        "declared_caps": {
            "horizon_chunks": HORIZON_CHUNKS,
            "cadence_store_cap": CADENCE_STORE_CAP,
            "cadence_store_saturations": store_saturations,
            "period_tail_window": PERIOD_TAIL_WINDOW,
            "period_max_block_gaps": PERIOD_MAX_BLOCK_GAPS,
            "min_saturation_run": MIN_SATURATION_RUN,
            "saturation_detection": (
                "exact and cap-free: maximal consecutive run ending at the "
                "horizon, no period search involved"
            ),
            "windowed_offset_anchors": WINDOWED_OFFSET_ANCHORS,
            "min_lag_overlap": MIN_LAG_OVERLAP,
            "across_key_rep_cap": ACROSS_KEY_REP_CAP,
            "across_key_rep_cap_hits": pair_cap_hits + bank_cap_hits,
        },
        "what_a_negative_costs": (
            "A NO_RELATION_IN_F entry is priced to this family at these caps and "
            "this horizon.  It does not exclude transformations outside F, nor "
            "relations that only appear beyond tick "
            f"{HORIZON_CHUNKS}."
        ),
    }
    verdict_block = {
        "within_key_pair_clock_verdict": relation_verdict,
        "headline_substantive_full_dictionary_coverage": (
            f"{substantive_related}/{substantive}"
        ),
        "headline_coverage_fraction": (
            f"{coverage.numerator}/{coverage.denominator}"
        ),
        "all_comparable_coverage_including_thin": f"{related}/{comparable}",
        "within_key_member_histogram": pair_totals,
        "within_key_evidence_split": within_pair["evidence_split"],
        "within_key_witness_parameters": within_pair["witness_parameter_histogram"],
        "within_key_substantive_nonidentity_full_dictionaries": substantive_nonidentity,
        "within_key_substantive_partial_matches": substantive_partial,
        "within_key_substantive_nonidentity_partial_matches": (
            substantive_partial_nonidentity
        ),
        "nondegenerate_periods_in_corpus": period_arithmetic,
        "every_nondegenerate_period_is_whole_orbits": all(
            row["exact_multiple_of_stations"] for row in period_arithmetic
        ),
        "within_key_bank_clock_histogram": within_bank["verdicts"],
        "within_key_bank_clock_substantive_coverage": (
            f"{within_bank['substantive_relations']}/"
            f"{within_bank['substantive_pairs_of_clocks']}"
        ),
        "across_key_verdict": across_verdict,
        "across_key_keys_outside_any_nontrivial_F1_class": unrelated_across,
        "across_key_F1_edges": cross_key_edges,
        "across_key_F1_edges_with_nonzero_offset": cross_key_nonzero,
        "pair_clock_information_content": dict(sorted(domination.items())),
        "saturation_note": SATURATION_NOTE,
        "evidence_note": EVIDENCE_NOTE,
        "reading": (
            f"On the {substantive} substantive pairs-of-pair-clocks the declared "
            f"family supplies a WHOLE-cadence dictionary for "
            f"{substantive_related}, of which {substantive_nonidentity} move the "
            f"tick values at all; the permissive partial member F3P matches a "
            f"further {substantive_partial} on at least half a clock, "
            f"{substantive_partial_nonidentity} of them non-identity.  On the "
            f"single-bank clocks the dictionary count is "
            f"{within_bank['substantive_relations']} of "
            f"{within_bank['substantive_pairs_of_clocks']}.  Of the "
            f"{lane_count * len(BANK_PAIRS)} pair clocks, "
            f"{domination.get('STRICTLY_JOINT', 0)} carry information neither "
            f"bank clock carries alone, "
            f"{domination.get('ONE_BANK_GATES_THE_PAIR', 0)} are one bank clock "
            f"outright, {domination.get('BOTH_BANK_CLOCKS_IDENTICAL', 0)} are "
            f"both, and {domination.get('SILENT_PAIR', 0)} never sound.  "
            f"Across keys, at a FIXED bank pair, {cross_key_nonzero} of "
            f"{cross_key_edges} constant-offset edges carry a nonzero offset."
        ),
        "pricing": pricing,
    }
    g_pass = (
        comparable + pair_totals.get("ONE_SIDE_SILENT", 0)
        + pair_totals.get("TRIVIAL_SATURATION", 0) == lane_count * len(BANK_PAIRS)
        and related + pair_totals.get("NO_RELATION_IN_F", 0) == comparable
        and substantive_related <= related
        and sum(domination.values()) == lane_count * len(BANK_PAIRS)
        and domination.get("SILENT_PAIR", 0) == empty_pair
    )

    # ------------------------------------------------------------------ controls
    input_shas = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    initial_hasher = sha256()
    for state in states:
        initial_hasher.update(bytes(state))
    replay_equal = all(
        ((plane >> 0) & 1) == ((plane >> duplicate_lane) & 1) for plane in planes
    )
    duplicate_clock_equal = (
        all(
            tuple(duplicate_bank_clocks[bank]) == bank_cadences[0][bank]
            for bank in range(FIXTURE_BANKS)
        )
        and all(
            tuple(duplicate_pair_clocks[index]) == pair_cadences[0][index]
            for index in range(len(BANK_PAIRS))
        )
    )
    runner_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    runtime = time.monotonic() - started

    dumps = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "SETUP_JSON " + json.dumps(setup, **dumps),
        "QUESTION: Cycle 866 found that at B=3/4 every bank pair carries its own "
        "sync cadence and no global record-time exists.  This runner asks whether "
        "those local clocks are nevertheless related by an exact dictionary.",
        "FAMILY_DECLARED :: " + json.dumps(list(FAMILY), **dumps),
        "FAMILY_CLOSURE: " + FAMILY_CLOSURE,
        "PASS A_SUBSTRATE :: " + json.dumps({
            "structural_checks": True,
            "per_bank_watched_disjoint": True,
            "source_pointer_outside_bank_sets": True,
            "watched_coordinates_per_bank": local_wire_count,
            "initial_census_sha256": initial_hasher.hexdigest(),
        }, **dumps),
        ("PASS" if b_pass else "FAIL") + " B_CLOCKS :: " + json.dumps({
            "bank_clock_count": lane_count * FIXTURE_BANKS,
            "pair_clock_count": lane_count * len(BANK_PAIRS),
            "bank_clean_occurrences": bank_clean_totals,
            "pair_clean_occurrences": pair_clean_totals,
            "silent_bank_clocks": empty_bank,
            "silent_pair_clocks": empty_pair,
            "bank_clock_length_histogram": dict(sorted(bank_length_histogram.items())),
            "pair_clock_length_histogram": dict(sorted(pair_length_histogram.items())),
            "eventually_periodic_bank_clocks": periodic_bank_clocks,
            "eventually_periodic_pair_clocks": periodic_pair_clocks,
            "saturated_bank_clocks": saturated_bank_clocks,
            "saturated_pair_clocks": saturated_pair_clocks,
            "silent_and_saturated_overlap": silent_and_saturated,
            "nondegenerate_bank_period_histogram": bank_period_hist,
            "nondegenerate_pair_period_histogram": pair_period_hist,
            "saturation_note": SATURATION_NOTE,
            "pair_clock_information_content": dict(sorted(domination.items())),
            "pair_clock_is_bank_clock_intersection_failures": intersection_failures,
            "monotonicity_failures": monotone_failures,
            "out_of_horizon_failures": horizon_failures,
            "store_cap_saturations": store_saturations,
            "corpus_sha256": corpus_digest,
            "verbatim_samples": sample_rows,
        }, **dumps),
        ("PASS" if controls_pass else "FAIL") + " C_FAMILY_CONTROLS :: "
        + json.dumps({
            "meaning": (
                "Positive controls build synthetic images under each family "
                "member and require acceptance with a witness that re-derives "
                "the image exactly.  Negative controls require refusal of a "
                "one-tick perturbation that manufactures two gap values absent "
                "from the source, and refusal of a triangular-index thinning.  "
                "These gate the tests themselves, not the outcome."
            ),
            "constructible_negative_controls": {
                "one_tick_perturbation": sum(
                    1 for row in control_rows
                    if "negative_one_tick_perturbation_refused_by_exact_members" in row
                ),
                "tail_edit": sum(
                    1 for row in control_rows
                    if "negative_tail_edit_refused_by_F4" in row
                ),
                "triangular_thinning": sum(
                    1 for row in control_rows
                    if "negative_triangular_thinning_refused" in row
                ),
            },
            "rows": control_rows,
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " D_WITHIN_KEY_PAIR_OF_PAIRS :: "
        + json.dumps({
            "scope": "the three pair clocks of each key, compared pairwise",
            "code_legend": {
                "1": "F1", "w": "F1W", "2": "F2A/F2B", "3": "F3", "4": "F4",
                "x": "NO_RELATION_IN_F", "0": "one side silent",
                "s": "TRIVIAL_SATURATION (both clocks clean at every tick)",
            },
            "direction_note": (
                "Each unordered pair of clocks is searched forward and, if that "
                "refuses, reversed; the witness records which direction held."
            ),
            "evidence_note": EVIDENCE_NOTE,
            **{label: value for label, value in within_pair.items()
               if label != "per_key_codes"},
            "per_key_codes": within_pair["per_key_codes"],
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " E_WITHIN_KEY_BANK_CLOCKS :: "
        + json.dumps({
            "scope": "the three single-bank clocks of each key, compared pairwise",
            **{label: value for label, value in within_bank.items()
               if label != "per_key_codes"},
            "per_key_codes": within_bank["per_key_codes"],
        }, **dumps),
        ("PASS" if e_pass else "FAIL") + " F_ACROSS_KEYS :: " + json.dumps({
            "scope": "one clock index at a time, all keys compared",
            "pair_clocks": across_pair,
            "bank_clocks": across_bank,
            "rep_cap_hits": pair_cap_hits + bank_cap_hits,
        }, **dumps),
        ("PASS" if g_pass else "FAIL") + " G_RELATION_VERDICT :: "
        + json.dumps(verdict_block, **dumps),
    ]
    h_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "audit_input_paths_repo_relative": all(
            not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS
        ),
        "input_shas": input_shas,
        "runner_sha256": runner_sha,
        "initial_census_sha256": initial_hasher.hexdigest(),
        "corpus_sha256": corpus_digest,
        "duplicate_lane_clean_mismatches": duplicate_mismatches,
        "duplicate_final_state_equal": replay_equal,
        "duplicate_clock_stable": duplicate_clock_equal,
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    h_prepass = (
        h_core["audit_input_paths_exist"]
        and h_core["audit_input_paths_repo_relative"]
        and duplicate_mismatches == 0
        and replay_equal
        and duplicate_clock_equal
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (b_pass, controls_pass, d_pass, e_pass, g_pass)
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
        final = "CYCLE869_CLOCK_RELATION_PASS"
        stdout_bytes = len(("\n".join(lines + [h_line, final]) + "\n").encode())
    h_core["stdout_bytes"] = stdout_bytes
    h_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    h_pass = h_prepass and h_core["stdout_under_150KB"]
    h_line = ("PASS" if h_pass else "FAIL") + " H_CONTROLS :: " + json.dumps(
        h_core, **dumps
    )
    final = (
        "CYCLE869_CLOCK_RELATION_PASS" if all(verdicts) and h_pass
        else "CYCLE869_CLOCK_RELATION_HONEST_FAIL"
    )
    print("\n".join(lines + [h_line, final]))
    return 0 if all(verdicts) and h_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
