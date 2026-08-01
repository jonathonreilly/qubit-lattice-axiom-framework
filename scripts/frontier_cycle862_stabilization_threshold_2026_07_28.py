#!/usr/bin/env python3
"""Cycle 862: bounded content-stabilization threshold certificate.

The census and evolution are rebuilt from the tracked Cycle-719 controller
core.  Records are observed at clean H-chunk boundaries, including the
initial (orbit-boundary) state produced by ``run_orbit``.
"""
from __future__ import annotations

from collections import Counter, deque
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
    for size in range(2, 6):
        size_placements = tuple(row for row_size, row in placements if row_size == size)
        for event, seed in enumerate(seeds):
            for positions in size_placements:
                state, a_tokens, b_tokens, _trace = C719.run_orbit(
                    seed, program, token_positions=positions
                )
                keys.append((size, event, positions))
                states.append(state)
                token_failures += (
                    tuple(index for index, bit in enumerate(a_tokens) if bit) != positions
                )
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
    """Full state bit-vector as one byte (zero or one) per coordinate."""
    return bytes((plane >> lane) & 1 for plane in planes)


def lane_content_sha(planes, lane):
    return sha256(lane_state_bytes(planes, lane)).hexdigest()


def static_content_bases(states, dynamic_targets):
    bases = []
    for state in states:
        base = bytearray(state)
        for wire in dynamic_targets:
            base[wire] = 0
        bases.append(bytes(base))
    return tuple(bases)


def content_signature(planes, lane, dynamic_targets):
    signature = 0
    for ordinal, wire in enumerate(dynamic_targets):
        signature |= ((planes[wire] >> lane) & 1) << ordinal
    return signature


def material_from_signature(base, signature, dynamic_targets):
    material = bytearray(base)
    remaining = signature
    while remaining:
        bit = remaining & -remaining
        material[dynamic_targets[bit.bit_length() - 1]] = 1
        remaining -= bit
    return bytes(material)


def iter_mask(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def cycle860_joint_content_digest(keys, e1_sha, e2_sha):
    payload = {
        "e1": tuple(sorted((compact(keys[lane]), value) for lane, value in e1_sha.items())),
        "e2": tuple(sorted((compact(keys[lane]), value) for lane, value in e2_sha.items())),
    }
    return sha256(compact(payload).encode("utf-8")).hexdigest()


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
    dynamic_targets = tuple(sorted({gate.wires[-1] for word in schedules for gate in word}))

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
    if len(program) != STATIONS or len(keys) != EXPECTED_KEYS:
        print("FAIL A_REGRESSION :: census construction failed")
        return 1

    planes = transpose_states(states)
    masks = station_masks(keys)
    census_mask = (1 << len(keys)) - 1
    evolution_mask = (1 << (len(keys) + 1)) - 1
    duplicate_lane = len(keys)
    bases = static_content_bases(states, dynamic_targets)
    content_cache = [dict() for _ in keys]

    depths = [0] * len(keys)
    current_sha = [None] * len(keys)
    current_count = [0] * len(keys)
    current_start = [None] * len(keys)
    run_counts = [0] * len(keys)
    run_total_counts = [0] * len(keys)
    run_hashers = [sha256() for _ in keys]
    run_heads = [[] for _ in keys]
    run_tails = [deque(maxlen=2) for _ in keys]
    last_clean_planes = {wire: 0 for wire in dynamic_targets}
    seen_content = 0
    witness_count = 0
    witness_examples = []

    e1_time = {}
    e2_time = {}
    e2_rung = {}
    e1_sha = {}
    e2_sha = {}
    duplicate_clean_mismatches = 0
    clean_occurrences = 0
    clean_moments = 0

    def finalize_run(lane):
        if current_sha[lane] is None:
            return
        row = (current_sha[lane], current_count[lane])
        encoded = f"{row[0]}:{row[1]};".encode()
        run_hashers[lane].update(encoded)
        run_counts[lane] += 1
        run_total_counts[lane] += current_count[lane]
        if len(run_heads[lane]) < 2:
            run_heads[lane].append(row)
        run_tails[lane].append(row)

    def observe(tick, orbit_boundary):
        nonlocal seen_content, witness_count
        nonlocal duplicate_clean_mismatches, clean_occurrences, clean_moments
        dirty = 0
        for wire in watched:
            dirty |= planes[wire]
        clean_all = evolution_mask & ~dirty
        clean = census_mask & clean_all
        duplicate_clean_mismatches += (
            ((clean_all >> 0) & 1) != ((clean_all >> duplicate_lane) & 1)
        )
        if not clean:
            return
        clean_moments += 1
        clean_occurrences += clean.bit_count()
        prior = clean & seen_content
        changed = clean & ~seen_content
        inverse_clean = ~clean
        for wire in dynamic_targets:
            previous = last_clean_planes[wire]
            present = planes[wire]
            changed |= prior & (present ^ previous)
            last_clean_planes[wire] = (previous & inverse_clean) | (present & clean)
        seen_content |= clean

        changed_set = set(iter_mask(changed))
        for lane in iter_mask(clean):
            depths[lane] += 1
            if lane in changed_set:
                signature = content_signature(planes, lane, dynamic_targets)
                cached = content_cache[lane].get(signature)
                if cached is None:
                    material = material_from_signature(bases[lane], signature, dynamic_targets)
                    cached = sha256(material).hexdigest()
                    content_cache[lane][signature] = cached
                new_sha = cached
                if current_sha[lane] is not None:
                    if new_sha == current_sha[lane]:
                        raise AssertionError(("signature/hash disagreement", lane, tick))
                    prior_sha = current_sha[lane]
                    prior_count = current_count[lane]
                    prior_start = current_start[lane]
                    finalize_run(lane)
                    witness_count += prior_count
                    if len(witness_examples) < 3:
                        witness_examples.append({
                            "key": short_key(keys[lane]),
                            "threshold_rung": prior_start,
                            "locked_sha": prior_sha,
                            "contradicting_rung": depths[lane],
                            "contradicting_sha": new_sha,
                            "candidates_witnessed_by_transition": prior_count,
                        })
                current_sha[lane] = new_sha
                current_count[lane] = 1
                current_start[lane] = depths[lane]
            else:
                current_count[lane] += 1

            if lane not in e1_time:
                e1_time[lane] = tick
                e1_sha[lane] = current_sha[lane]
            if orbit_boundary and lane not in e2_time:
                e2_time[lane] = tick
                e2_rung[lane] = depths[lane]
                e2_sha[lane] = current_sha[lane]

    observe(0, True)
    total_chunks = HORIZON_ORBITS * STATIONS
    for tick in range(1, total_chunks + 1):
        phase = (tick - 1) % STATIONS
        evolve_chunk(planes, schedules, masks[phase])
        observe(tick, tick % STATIONS == 0)

    for lane in range(len(keys)):
        finalize_run(lane)

    same_moment = sum(e1_time[lane] == e2_time[lane] for lane in e2_time)
    different_moment_equal = sum(
        e1_time[lane] != e2_time[lane] and e1_sha[lane] == e2_sha[lane]
        for lane in e2_time
    )
    different_content = sum(
        e1_time[lane] != e2_time[lane] and e1_sha[lane] != e2_sha[lane]
        for lane in e2_time
    )
    joint_content_digest = cycle860_joint_content_digest(keys, e1_sha, e2_sha)
    expected_joint_digest = (
        "f77c04f33b5c596a0bb5f80e3fa685ddee8b4497069470da6cc34a23a4616150"
    )

    regression = {
        "E1_stamped": len(e1_time),
        "E2_stamped": len(e2_time),
        "E2_subset_E1": not (set(e2_time) - set(e1_time)),
        "both_same_moment": same_moment,
        "both_different_moment_equal_content": different_moment_equal,
        "both_different_content": different_content,
        "E1_only": len(set(e1_time) - set(e2_time)),
        "joint_content_digest": joint_content_digest,
    }
    expected_regression = (
        len(e1_time) == 182
        and len(e2_time) == 114
        and regression["E2_subset_E1"]
        and same_moment == 34
        and different_moment_equal == 49
        and different_content == 31
        and regression["E1_only"] == 68
        and joint_content_digest == expected_joint_digest
        and allocator_failures == token_failures == 0
    )

    stamped = tuple(sorted(e1_time))
    stabilization = {
        lane: depths[lane] - current_count[lane] + 1 for lane in stamped
    }
    vacuous_censored = tuple(lane for lane in stamped if current_count[lane] < 2)
    no_ladder = tuple(lane for lane in range(len(keys)) if lane not in e1_time)
    stabilization_histogram = dict(sorted(Counter(stabilization.values()).items()))

    categories = {
        "E1": [],
        "E2_ORBIT_BOUNDARY": [],
        "OTHER_RUNG": [],
        "NEVER_WITHIN_HORIZON": [short_key(keys[lane]) for lane in no_ladder],
    }
    for lane in stamped:
        rung = stabilization[lane]
        if lane in vacuous_censored:
            categories["NEVER_WITHIN_HORIZON"].append(short_key(keys[lane]))
        elif rung == 1:
            categories["E1"].append(short_key(keys[lane]))
        elif e2_rung.get(lane) == rung:
            categories["E2_ORBIT_BOUNDARY"].append(short_key(keys[lane]))
        else:
            categories["OTHER_RUNG"].append(short_key(keys[lane]))
    category_counts = {label: len(rows) for label, rows in categories.items()}
    if categories["NEVER_WITHIN_HORIZON"]:
        coincidence_verdict = "STABILIZATION_INCOMPLETE_AT_HORIZON"
    else:
        nonempty = [label for label in categories if categories[label]]
        if len(nonempty) == 1:
            coincidence_verdict = f"THRESHOLD_DERIVED_AT_{nonempty[0]}"
        else:
            coincidence_verdict = "THRESHOLD_PER_KEY_STABILIZED_NO_UNIFORM_NAME"

    sequence_table = {}
    for lane in stamped:
        tail = list(run_tails[lane])
        sequence_table[short_key(keys[lane])] = {
            "depth": depths[lane],
            "runs": run_counts[lane],
            "rle_sha256": run_hashers[lane].hexdigest(),
            "head": run_heads[lane],
            "tail": tail,
            "stabilization_rung": stabilization[lane],
            "final_run_confirmations": current_count[lane],
            "within_horizon_only": True,
        }

    b_pass = (
        len(sequence_table) == len(e1_time)
        and all(run_total_counts[lane] == depths[lane] for lane in range(len(keys)))
        and all(run_counts[lane] >= 1 for lane in stamped)
    )
    c_pass = (
        len(stabilization) == 182
        and all(1 <= stabilization[lane] <= depths[lane] for lane in stamped)
    )
    expected_witnesses = sum(stabilization[lane] - 1 for lane in stamped)
    d_pass = witness_count == expected_witnesses and len(witness_examples) == 3
    e_pass = sum(category_counts.values()) == len(keys)

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
    final_lane_sha = lane_content_sha(planes, 0)
    duplicate_lane_sha = lane_content_sha(planes, duplicate_lane)
    runner_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    runtime = time.monotonic() - started

    compact = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "SETUP_JSON " + json.dumps(setup, **compact),
        "READING R: " + READING_R,
        "FIAT_PERMANENCE: " + FIAT_READING,
        ("PASS" if expected_regression else "FAIL")
        + " A_REGRESSION :: " + json.dumps(regression, **compact),
        ("PASS" if b_pass else "FAIL") + " B_CONTENT_SEQUENCES :: "
        + json.dumps({
            "stamped_keys": len(stamped),
            "clean_moments": clean_moments,
            "clean_occurrences": clean_occurrences,
            "ladder_depth_histogram": dict(sorted(Counter(depths).items())),
            "per_key_bounded_rle": sequence_table,
        }, **compact),
        ("PASS" if c_pass else "FAIL") + " C_STABILIZATION_INDEX :: "
        + json.dumps({
            "existence_within_horizon": len(stabilization),
            "no_clean_ladder_horizon_censored": len(no_ladder),
            "vacuous_final_rung_horizon_censored": len(vacuous_censored),
            "all_positive_claims_within_horizon_only": True,
            "stabilization_histogram": stabilization_histogram,
        }, **compact),
        ("PASS" if d_pass else "FAIL") + " D_FORCING_CHECK :: "
        + json.dumps({
            "threshold_candidates_below_stabilization": expected_witnesses,
            "contradiction_witnesses": witness_count,
            "verbatim_examples": witness_examples,
            "conditional_on_READING_R": True,
        }, **compact),
        "D_READING_R_CONCLUSION: Under R, every rung below the content-stabilization rung "
        "locks content contradicted by a later clean confirmation; the first sustained "
        "content is therefore forced within the declared horizon.",
        "D_FIAT_CONCLUSION: " + FIAT_READING,
        ("PASS" if e_pass else "FAIL") + " E_THE_COINCIDENCE :: "
        + json.dumps({
            "verdict": coincidence_verdict,
            "counts": category_counts,
            "per_key_table": categories,
        }, **compact),
    ]
    f_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "input_shas": input_shas,
        "runner_sha256": runner_sha,
        "initial_census_sha256": initial_hasher.hexdigest(),
        "duplicate_clean_mismatches": duplicate_clean_mismatches,
        "duplicate_final_state_equal": replay_equal,
        "final_lane_sha256": final_lane_sha,
        "duplicate_lane_sha256": duplicate_lane_sha,
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < 1400,
    }
    f_prepass = (
        f_core["audit_input_paths_exist"]
        and duplicate_clean_mismatches == 0
        and replay_equal
        and final_lane_sha == duplicate_lane_sha
        and runtime < 1400
    )
    verdicts = (expected_regression, b_pass, c_pass, d_pass, e_pass)
    final_line = "CYCLE862_STABILIZATION_THRESHOLD_PASS" if all(verdicts) and f_prepass else (
        "CYCLE862_STABILIZATION_THRESHOLD_HONEST_FAIL"
    )
    stdout_bytes = 0
    for _ in range(4):
        f_core["stdout_bytes"] = stdout_bytes
        f_core["stdout_under_150KB"] = stdout_bytes < 150 * 1024 if stdout_bytes else True
        f_line = ("PASS" if f_prepass and f_core["stdout_under_150KB"] else "FAIL") \
            + " F_CONTROLS :: " + json.dumps(f_core, **compact)
        stdout_bytes = len(("\n".join(lines + [f_line, final_line]) + "\n").encode())
    f_core["stdout_bytes"] = stdout_bytes
    f_core["stdout_under_150KB"] = stdout_bytes < 150 * 1024
    f_pass = f_prepass and f_core["stdout_under_150KB"]
    final_line = "CYCLE862_STABILIZATION_THRESHOLD_PASS" if all(verdicts) and f_pass else (
        "CYCLE862_STABILIZATION_THRESHOLD_HONEST_FAIL"
    )
    f_line = ("PASS" if f_pass else "FAIL") + " F_CONTROLS :: " + json.dumps(f_core, **compact)
    print("\n".join(lines + [f_line, final_line]))
    return 0 if all(verdicts) and f_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
