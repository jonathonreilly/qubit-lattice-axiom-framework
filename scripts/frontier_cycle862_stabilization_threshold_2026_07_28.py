#!/usr/bin/env python3
"""Cycle 862: bounded content-stabilization threshold certificate.

The census and evolution are rebuilt from the tracked Cycle-719 controller
core.  Records are observed at clean H-chunk boundaries, including the
initial (orbit-boundary) state produced by ``run_orbit``.
"""
from __future__ import annotations

from collections import Counter, defaultdict
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

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as C719


A = C719.A
B = C719.B
M = C719.M
R3 = C719.R3

FIXTURE_BANKS = 2
STATIONS = 11
HORIZON_ORBITS = 51_115
EXPECTED_KEYS = 748
READING_R = (
    '"a record locks exactly one admissible local possibility" + "records are permanent" '
    "read together as: the locked content must be the content the admissible dynamics "
    "SUSTAINS — a lock whose content a later clean confirmation contradicts locks a "
    "possibility the universe itself revises, violating R."
)
FIAT_READING = (
    "Under fiat-permanence (the record keeps its content regardless of later dynamics) "
    "NO threshold is forced — the derivation is conditional on reading R."
)


def independent_positions(stations: int = STATIONS):
    """All size 2..5 subsets with no adjacent pair on the cyclic ring."""
    rows = []
    for size in range(2, 6):
        for positions in combinations(range(stations), size):
            occupied = set(positions)
            if any((position + 1) % stations in occupied for position in positions):
                continue
            rows.append((size, positions))
    return tuple(rows)


def event_seeds(program):
    """Build the four alternating endpoint events and certify the allocator."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    state = M.pack_state(banks, links)
    seeds = []
    failures = 0
    for event in range(4):
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
    """Create the literal (k,event,positions) census via ``run_orbit``."""
    keys = []
    states = []
    token_failures = 0
    for size, positions in placements:
        for event, seed in enumerate(seeds):
            state, a_tokens, b_tokens, _trace = C719.run_orbit(
                seed, program, token_positions=positions
            )
            keys.append((size, event, positions))
            states.append(state)
            token_failures += tuple(index for index, bit in enumerate(a_tokens) if bit) != positions
            token_failures += any(b_tokens)
    return tuple(keys), tuple(states), token_failures


def single_bit_location(zero_banks, zero_links, *, bank=None, link=None, wire):
    """Locate one logical coordinate by the required pack_state probe."""
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


def watched_coordinates():
    """Locate SOURCE_POINTER, per-bank work/admission bits, and every link bit."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    # SOURCE_POINTER is the singular physical source coordinate used directly
    # by prepare_endpoint/source_compute_word.  The bank-local wire bearing the
    # same ordinal is a distinct coordinate after packing and is not watched.
    watched = {R3.X.SOURCE_POINTER}
    local = (
        A.POINTER,
        A.U_TO_V,
        A.V_TO_U,
        A.DIRECTION_OK,
        *A.FRESH,
        *A.ZERO_WORK,
        A.TOKEN_OK,
    )
    for bank in range(FIXTURE_BANKS):
        for wire in local:
            watched.add(
                single_bit_location(zero_banks, zero_links, bank=bank, wire=wire)
            )
    for link, row in enumerate(zero_links):
        for wire in range(len(row)):
            watched.add(
                single_bit_location(zero_banks, zero_links, link=link, wire=wire)
            )
    return tuple(sorted(watched))


def transpose_states(states, duplicate_source=0):
    """Transpose lane tuples into Python-integer bit slices and add one replay lane."""
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
    """Per-phase, per-station masks for the fixed circulating token sets."""
    masks = [[0] * STATIONS for _ in range(STATIONS)]
    for lane, (_size, _event, positions) in enumerate(keys):
        bit = 1 << lane
        for phase in range(STATIONS):
            for start in positions:
                masks[phase][(start + phase) % STATIONS] |= bit
    duplicate_bit = 1 << len(keys)
    positions = keys[duplicate_source][2]
    for phase in range(STATIONS):
        for start in positions:
            masks[phase][(start + phase) % STATIONS] |= duplicate_bit
    return tuple(tuple(row) for row in masks)


def apply_masked_word(planes, word, lane_mask):
    """Apply a semantic word simultaneously to exactly ``lane_mask`` lanes."""
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


def evolve_chunk(planes, schedules, phase):
    for station, word in enumerate(schedules):
        apply_masked_word(planes, word, phase[station])


def clean_mask(planes, watched, census_mask):
    dirty = 0
    for wire in watched:
        dirty |= planes[wire]
    return census_mask & ~dirty


def lane_state_bytes(planes, lane):
    """Full state bit-vector, little-endian by increasing state coordinate."""
    packed = bytearray((len(planes) + 7) // 8)
    for wire, plane in enumerate(planes):
        packed[wire >> 3] |= ((plane >> lane) & 1) << (wire & 7)
    return bytes(packed)


def lane_content_sha(planes, lane):
    return sha256(lane_state_bytes(planes, lane)).hexdigest()


def short_key(key):
    size, event, positions = key
    return f"k{size}e{event}p{''.join(format(position, 'x') for position in positions)}"


def main():
    started = time.monotonic()
    program = C719.interleaved_program(FIXTURE_BANKS)
    placements = independent_positions()
    seeds, allocator_failures = event_seeds(program)
    keys, states, token_failures = census_initial_states(program, seeds, placements)
    watched = watched_coordinates()
    schedules = tuple(C719.mapped_macro(row) for row in program)

    setup = {
        "fixture_banks": FIXTURE_BANKS,
        "program_stations": len(program),
        "placement_histogram": dict(Counter(size for size, _ in placements)),
        "census_keys": len(keys),
        "state_width": len(states[0]),
        "watched_coordinates": len(watched),
        "allocator_failures": allocator_failures,
        "token_return_failures": token_failures,
    }
    print("SETUP_JSON", json.dumps(setup, sort_keys=True))
    print("READING_R", READING_R)
    print("FIAT_PERMANENCE", FIAT_READING)

    if len(program) != STATIONS or len(keys) != EXPECTED_KEYS:
        print("FAIL A_REGRESSION :: census construction failed")
        return 1

    planes = transpose_states(states)
    masks = station_masks(keys)
    census_mask = (1 << len(keys)) - 1
    initial_clean = clean_mask(planes, watched, census_mask)
    print("DEV_INITIAL_CLEAN", initial_clean.bit_count())
    for phase in range(STATIONS):
        evolve_chunk(planes, schedules, masks[phase])
        print("DEV_PHASE_CLEAN", phase + 1, clean_mask(planes, watched, census_mask).bit_count())
    print("DEV_ONE_ORBIT_REPLAY_EQUAL", all(
        ((plane >> 0) & 1) == ((plane >> len(keys)) & 1) for plane in planes
    ))
    print("DEV_RUNTIME_SECONDS", f"{time.monotonic() - started:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
