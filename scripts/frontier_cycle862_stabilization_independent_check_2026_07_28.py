#!/usr/bin/env python3
"""Cycle 862 independent adversarial stabilization checker.

This checker imports only the Cycle-719 controller core named by the primary.
It does not import, execute, or read the Cycle-862 primary.  Its scalar orbit
builder, bit-sliced horizon evolution, clean ladders, and tick-only ladders are
implemented locally.
"""
# Frozen-primary metadata only; the checker never reads or executes the primary.
# PRIMARY_V2_SHA256_PIN: b8ee658f2b9edb3b9c3fe9e0cb9216c88116c23939850b0828e283075c49e272
# PRIMARY_V2_GIT_BLOB_SHA1_PIN: 8d817e82f0f3d0780a2ffb18047a0d59503ffb1b
from __future__ import annotations

import ast
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

FORBIDDEN_PRIMARY_MODULE = "frontier_cycle862_stabilization_threshold_2026_07_28"
EXPECTED_JOINT_CONTENT_DIGEST = (
    "f77c04f33b5c596a0bb5f80e3fa685ddee8b4497069470da6cc34a23a4616150"
)
EXPECTED_WITNESSES = 2_223_285
FIXTURE_BANKS = 2
STATIONS = 11
HORIZON_ORBITS = 51_115
EXPECTED_KEYS = 748

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as C719


A = C719.A
B = C719.B
M = C719.M
R3 = C719.R3
H = C719.H


def compact(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def short_key(key) -> str:
    size, event, positions = key
    return f"k{size}e{event}p{''.join(format(position, 'x') for position in positions)}"


def independent_positions(stations: int = STATIONS):
    """Enumerate the cyclic non-neighbor placements without primary helpers."""
    rows = []
    for size in range(2, 6):
        for positions in combinations(range(stations), size):
            occupied = set(positions)
            if all((position + 1) % stations not in occupied for position in positions):
                rows.append((size, positions))
    return tuple(rows)


def local_program(bank_count: int = FIXTURE_BANKS):
    """Rebuild the geometry-carried program instead of calling C719's builder."""
    prefix = [("source", 0, R3.source_compute_word())]
    for bank in range(bank_count):
        prefix.append(("bank", bank, H.PACKET))
        if bank:
            prefix.append(("cross", bank - 1, ()))
        if bank < bank_count - 1:
            prefix.extend(
                (
                    ("handoff", bank, H.HANDOFF_FORWARD),
                    ("relay", bank, H.RELAY_LATCH),
                    ("relay", bank, H.RELAY_SWAP),
                )
            )
    reverse = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend(
            (
                ("relay", edge, H.RELAY_SWAP),
                ("relay", edge, H.RELAY_UNLATCH),
                ("handoff", edge, H.HANDOFF_RETURN),
            )
        )
    return tuple(prefix + reverse + [("finalizer", 0, M.source_finalizer_word(bank_count))])


def local_mapped_macro(row):
    kind, index, word = row
    if kind in ("source", "finalizer"):
        return tuple(word)
    if kind == "identity":
        return ()
    return H.mapped_action(kind, index, word)


def scalar_orbit(state, schedules, token_positions):
    """Direct Q-then-translation orbit, independent of C719.run_orbit."""
    stations = len(schedules)
    live = tuple(sorted(token_positions))
    for _phase in range(stations):
        for station in live:
            state = A.apply_semantic(state, schedules[station])
        live = tuple(sorted((station + 1) % stations for station in live))
    return state, live


def build_census(schedules, placements):
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    state = M.pack_state(banks, links)
    seeds = []
    allocator_failures = 0
    token_failures = 0
    flattened = tuple(gate for word in schedules for gate in word)
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, returned = scalar_orbit(before, schedules, (0,))
        allocator_failures += after != A.apply_semantic(before, flattened)
        token_failures += returned != (0,)
        seeds.append(before)
        state = after

    keys = []
    states = []
    for size in range(2, 6):
        size_rows = tuple(row for row_size, row in placements if row_size == size)
        for event, seed in enumerate(seeds):
            for positions in size_rows:
                after, returned = scalar_orbit(seed, schedules, positions)
                keys.append((size, event, positions))
                states.append(after)
                token_failures += returned != positions
    return tuple(keys), tuple(states), allocator_failures, token_failures


def single_bit_location(zero_banks, zero_links, *, bank=None, link=None, wire):
    banks = [list(row) for row in zero_banks]
    links = [list(row) for row in zero_links]
    if bank is not None:
        banks[bank][wire] = 1
    else:
        links[link][wire] = 1
    packed = M.pack_state(
        tuple(tuple(row) for row in banks), tuple(tuple(row) for row in links)
    )
    locations = tuple(index for index, value in enumerate(packed) if value)
    if len(locations) != 1:
        raise AssertionError((bank, link, wire, locations))
    return locations[0]


def watched_coordinates():
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
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
            watched.add(single_bit_location(zero_banks, zero_links, bank=bank, wire=wire))
    for link, row in enumerate(zero_links):
        for wire in range(len(row)):
            watched.add(single_bit_location(zero_banks, zero_links, link=link, wire=wire))
    return tuple(sorted(watched))


def mirrored_transpose(states):
    """Encode two complete identical censuses into lower and upper lane halves."""
    lanes = len(states)
    planes = [0] * len(states[0])
    for lane, state in enumerate(states):
        lane_bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= lane_bit
    lower_mask = (1 << lanes) - 1
    for wire in range(len(planes)):
        planes[wire] |= (planes[wire] & lower_mask) << lanes
    return planes


def mirrored_station_masks(keys):
    lanes = len(keys)
    lower = [[0] * STATIONS for _ in range(STATIONS)]
    for lane, (_size, _event, positions) in enumerate(keys):
        lane_bit = 1 << lane
        for phase in range(STATIONS):
            for start in positions:
                lower[phase][(start + phase) % STATIONS] |= lane_bit
    return tuple(
        tuple(mask | (mask << lanes) for mask in phase_masks)
        for phase_masks in lower
    )


def apply_masked_word(planes, word, lane_mask):
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


def evolve_chunk(planes, schedules, phase_masks):
    for station, word in enumerate(schedules):
        apply_masked_word(planes, word, phase_masks[station])


def iter_mask(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def lane_bytes(planes, lane):
    return bytes((plane >> lane) & 1 for plane in planes)


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


def content_sha(base, signature, dynamic_targets):
    material = bytearray(base)
    remaining = signature
    while remaining:
        bit = remaining & -remaining
        material[dynamic_targets[bit.bit_length() - 1]] = 1
        remaining -= bit
    return sha256(material).hexdigest()


def cycle860_joint_digest(keys, e1_sha, e2_sha):
    payload = {
        "e1": tuple(sorted((compact(keys[lane]), value) for lane, value in e1_sha.items())),
        "e2": tuple(sorted((compact(keys[lane]), value) for lane, value in e2_sha.items())),
    }
    return sha256(compact(payload).encode("utf-8")).hexdigest()


def primary_blocklist_report():
    """Prove from this source's text/AST that the primary is not consumed."""
    source_path = Path(__file__).resolve()
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(source_path))
    import_hits = []
    primary_io_hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            import_hits.extend(
                alias.name for alias in node.names if FORBIDDEN_PRIMARY_MODULE in alias.name
            )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if FORBIDDEN_PRIMARY_MODULE in module:
                import_hits.append(module)
        elif isinstance(node, ast.Call):
            constants = tuple(
                child.value
                for child in ast.walk(node)
                if isinstance(child, ast.Constant) and isinstance(child.value, str)
            )
            if not any(FORBIDDEN_PRIMARY_MODULE in value for value in constants):
                continue
            if isinstance(node.func, ast.Name):
                call_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                call_name = node.func.attr
            else:
                call_name = type(node.func).__name__
            if call_name in {
                "open",
                "read_text",
                "read_bytes",
                "run_path",
                "run_module",
                "__import__",
                "import_module",
                "Popen",
                "run",
                "check_call",
                "check_output",
            }:
                primary_io_hits.append((call_name, node.lineno))
    report = {
        "policy": "PRIMARY_BLOCKLIST_SOURCE_TEXT_AST_ONLY",
        "forbidden_module": FORBIDDEN_PRIMARY_MODULE,
        "literal_declaration_count": source.count(
            f'FORBIDDEN_PRIMARY_MODULE = "{FORBIDDEN_PRIMARY_MODULE}"'
        ),
        "import_hits": import_hits,
        "primary_io_or_execution_hits": primary_io_hits,
        "primary_loaded_in_sys_modules": FORBIDDEN_PRIMARY_MODULE in sys.modules,
    }
    report["pass"] = (
        report["literal_declaration_count"] == 1
        and not import_hits
        and not primary_io_hits
        and not report["primary_loaded_in_sys_modules"]
    )
    return report, source.encode("utf-8")


def main():
    started = time.monotonic()
    program = local_program()
    schedules = tuple(local_mapped_macro(row) for row in program)
    placements = independent_positions()
    keys, states, allocator_failures, token_failures = build_census(schedules, placements)
    watched = watched_coordinates()
    dynamic_targets = tuple(sorted({gate.wires[-1] for word in schedules for gate in word}))

    setup = {
        "fixture_banks": FIXTURE_BANKS,
        "program_stations": len(program),
        "placement_histogram": dict(sorted(Counter(size for size, _ in placements).items())),
        "census_keys": len(keys),
        "state_width": len(states[0]),
        "watched_coordinates": len(watched),
        "dynamic_targets": len(dynamic_targets),
        "allocator_failures": allocator_failures,
        "token_return_failures": token_failures,
        "primary_helpers_called": [],
    }
    setup_pass = (
        len(program) == STATIONS
        and len(keys) == EXPECTED_KEYS
        and setup["placement_histogram"] == {2: 44, 3: 77, 4: 55, 5: 11}
        and allocator_failures == token_failures == 0
    )

    lanes = len(keys)
    lower_mask = (1 << lanes) - 1
    full_mask = (1 << (2 * lanes)) - 1
    planes = mirrored_transpose(states)
    masks = mirrored_station_masks(keys)
    bases = static_content_bases(states, dynamic_targets)
    caches = [dict() for _ in keys]

    depths = [0] * lanes
    current_sha = [None] * lanes
    current_count = [0] * lanes
    current_start = [None] * lanes
    run_counts = [0] * lanes
    run_totals = [0] * lanes
    run_hashers = [sha256() for _ in keys]
    run_heads = [[] for _ in keys]
    run_tails = [deque(maxlen=2) for _ in keys]

    boundary_depths = [0] * lanes
    boundary_sha = [None] * lanes
    boundary_count = [0] * lanes
    boundary_start_ordinal = [None] * lanes
    boundary_start_tick = [None] * lanes
    boundary_runs = [0] * lanes
    boundary_hashers = [sha256() for _ in keys]

    last_clean_targets = {wire: 0 for wire in dynamic_targets}
    seen_clean = 0
    online_witness_count = 0
    clean_moments = 0
    clean_occurrences = 0
    clean_replay_mismatches = 0
    stamp_sha_replay_mismatches = 0

    e1_tick = {}
    e1_sha = {}
    e2_tick = {}
    e2_rung = {}
    e2_sha = {}
    post_e2_different = {}

    def cached_sha(lane):
        signature = content_signature(planes, lane, dynamic_targets)
        value = caches[lane].get(signature)
        if value is None:
            value = content_sha(bases[lane], signature, dynamic_targets)
            caches[lane][signature] = value
        return value

    def finalize_run(lane):
        if current_sha[lane] is None:
            return
        row = (current_sha[lane], current_count[lane])
        run_hashers[lane].update(f"{row[0]}:{row[1]};".encode("ascii"))
        run_counts[lane] += 1
        run_totals[lane] += current_count[lane]
        if len(run_heads[lane]) < 2:
            run_heads[lane].append(row)
        run_tails[lane].append(row)

    def finalize_boundary_run(lane):
        if boundary_sha[lane] is None:
            return
        boundary_hashers[lane].update(
            (
                f"{boundary_sha[lane]}:{boundary_count[lane]}:"
                f"{boundary_start_ordinal[lane]}:{boundary_start_tick[lane]};"
            ).encode("ascii")
        )
        boundary_runs[lane] += 1

    def observe(tick, orbit_boundary):
        nonlocal seen_clean, online_witness_count
        nonlocal clean_moments, clean_occurrences
        nonlocal clean_replay_mismatches, stamp_sha_replay_mismatches
        dirty = 0
        for wire in watched:
            dirty |= planes[wire]
        clean_all = full_mask & ~dirty
        clean = clean_all & lower_mask
        replay_clean = (clean_all >> lanes) & lower_mask
        clean_replay_mismatches += (clean ^ replay_clean).bit_count()
        if not clean:
            return
        clean_moments += 1
        clean_occurrences += clean.bit_count()

        prior = clean & seen_clean
        changed = clean & ~seen_clean
        for wire in dynamic_targets:
            previous = last_clean_targets[wire]
            present = planes[wire] & lower_mask
            changed |= prior & (present ^ previous)
            last_clean_targets[wire] = (previous & ~clean) | (present & clean)
        seen_clean |= clean

        for lane in iter_mask(clean):
            depths[lane] += 1
            if (changed >> lane) & 1:
                new_sha = cached_sha(lane)
                if current_sha[lane] is not None:
                    if new_sha == current_sha[lane]:
                        raise AssertionError(("content change mask/hash mismatch", lane, tick))
                    finalize_run(lane)
                    online_witness_count += current_count[lane]
                current_sha[lane] = new_sha
                current_count[lane] = 1
                current_start[lane] = depths[lane]
            else:
                current_count[lane] += 1

            if lane not in e1_tick:
                e1_tick[lane] = tick
                e1_sha[lane] = current_sha[lane]
                upper_sha = sha256(lane_bytes(planes, lane + lanes)).hexdigest()
                stamp_sha_replay_mismatches += upper_sha != current_sha[lane]

            if orbit_boundary:
                if lane not in e2_tick:
                    e2_tick[lane] = tick
                    e2_rung[lane] = depths[lane]
                    e2_sha[lane] = current_sha[lane]
                    upper_sha = sha256(lane_bytes(planes, lane + lanes)).hexdigest()
                    stamp_sha_replay_mismatches += upper_sha != current_sha[lane]

                boundary_depths[lane] += 1
                if boundary_sha[lane] != current_sha[lane]:
                    finalize_boundary_run(lane)
                    boundary_sha[lane] = current_sha[lane]
                    boundary_count[lane] = 1
                    boundary_start_ordinal[lane] = boundary_depths[lane]
                    boundary_start_tick[lane] = tick
                else:
                    boundary_count[lane] += 1

            if (
                lane in e2_tick
                and tick > e2_tick[lane]
                and lane not in post_e2_different
                and current_sha[lane] != e2_sha[lane]
            ):
                post_e2_different[lane] = {
                    "tick": tick,
                    "rung": depths[lane],
                    "sha256": current_sha[lane],
                }

    observe(0, True)
    scalar_shadow = states[0]
    scalar_shadow_match = False
    total_chunks = HORIZON_ORBITS * STATIONS
    for tick in range(1, total_chunks + 1):
        phase = (tick - 1) % STATIONS
        if tick <= STATIONS:
            active = sorted((start + phase) % STATIONS for start in keys[0][2])
            for station in active:
                scalar_shadow = A.apply_semantic(scalar_shadow, schedules[station])
        evolve_chunk(planes, schedules, masks[phase])
        observe(tick, tick % STATIONS == 0)
        if tick == STATIONS:
            scalar_shadow_match = tuple(lane_bytes(planes, 0)) == tuple(scalar_shadow)

    for lane in range(lanes):
        finalize_run(lane)
        finalize_boundary_run(lane)

    same_moment = sum(e1_tick[lane] == e2_tick[lane] for lane in e2_tick)
    different_moment_equal = sum(
        e1_tick[lane] != e2_tick[lane] and e1_sha[lane] == e2_sha[lane]
        for lane in e2_tick
    )
    different_content = sum(
        e1_tick[lane] != e2_tick[lane] and e1_sha[lane] != e2_sha[lane]
        for lane in e2_tick
    )
    joint_digest = cycle860_joint_digest(keys, e1_sha, e2_sha)
    regression = {
        "E1_stamped": len(e1_tick),
        "E2_stamped": len(e2_tick),
        "E2_subset_E1": not (set(e2_tick) - set(e1_tick)),
        "both_same_moment": same_moment,
        "both_different_moment_equal_content": different_moment_equal,
        "both_different_content": different_content,
        "E1_only": len(set(e1_tick) - set(e2_tick)),
        "joint_content_digest": joint_digest,
    }
    regression_pass = (
        regression
        == {
            "E1_stamped": 182,
            "E2_stamped": 114,
            "E2_subset_E1": True,
            "both_same_moment": 34,
            "both_different_moment_equal_content": 49,
            "both_different_content": 31,
            "E1_only": 68,
            "joint_content_digest": EXPECTED_JOINT_CONTENT_DIGEST,
        }
    )

    stamped = tuple(sorted(e1_tick))
    final_start = {
        lane: depths[lane] - current_count[lane] + 1 for lane in stamped
    }
    sequence_table = {
        short_key(keys[lane]): {
            "depth": depths[lane],
            "runs": run_counts[lane],
            "rle_sha256": run_hashers[lane].hexdigest(),
            "head": run_heads[lane],
            "tail": list(run_tails[lane]),
            "final_run_start": final_start[lane],
            "final_run_confirmations": current_count[lane],
        }
        for lane in stamped
    }
    sequence_digest = sha256(compact(sequence_table).encode("utf-8")).hexdigest()
    sequence_pass = (
        setup_pass
        and regression_pass
        and len(sequence_table) == 182
        and all(run_totals[lane] == depths[lane] for lane in range(lanes))
        and all(run_counts[lane] >= 1 for lane in stamped)
        and scalar_shadow_match
    )

    zero_table = {}
    counterexamples = []
    for lane in sorted(e2_tick, key=lambda index: short_key(keys[index])):
        name = short_key(keys[lane])
        row = {
            "E2_tick": e2_tick[lane],
            "E2_rung": e2_rung[lane],
            "E2_sha256": e2_sha[lane],
        }
        if lane in post_e2_different:
            row["status"] = "POST_E2_CLEAN_DIFFERENT_CONTENT"
            row["witness"] = post_e2_different[lane]
        else:
            row["status"] = (
                "COUNTEREXAMPLE_FIRST_STABILIZATION_AT_E2"
                if final_start[lane] == e2_rung[lane]
                else "COUNTEREXAMPLE_ALREADY_STABLE_BEFORE_E2"
            )
            row["first_full_stabilization_rung"] = final_start[lane]
            row["E2_rung_is_stable_within_horizon"] = (
                current_count[lane] >= 2 and final_start[lane] <= e2_rung[lane]
            )
            counterexamples.append(name)
        zero_table[name] = row
    changed_after_e2 = len(post_e2_different)
    counterexample_lanes = tuple(lane for lane in e2_tick if lane not in post_e2_different)
    first_at_e2 = tuple(
        lane for lane in counterexample_lanes if final_start[lane] == e2_rung[lane]
    )
    stable_before_e2 = tuple(
        lane for lane in counterexample_lanes if final_start[lane] < e2_rung[lane]
    )
    zero_pass = (
        len(e2_tick) == 114
        and changed_after_e2 + len(counterexamples) == 114
        and len(zero_table) == 114
        and all(
            current_count[lane] >= 2 and final_start[lane] <= e2_rung[lane]
            for lane in counterexample_lanes
        )
        and all(row["tick"] > e2_tick[lane] for lane, row in post_e2_different.items())
    )

    never_set = tuple(lane for lane in range(lanes) if lane not in e1_tick)
    set_but_uncertifiable = tuple(lane for lane in stamped if current_count[lane] < 2)
    categories = {
        "E1": [],
        "E2_ORBIT_BOUNDARY": [],
        "OTHER_RUNG": [],
        "NEVER_WITHIN_HORIZON": [short_key(keys[lane]) for lane in never_set],
    }
    for lane in stamped:
        name = short_key(keys[lane])
        if lane in set_but_uncertifiable:
            categories["NEVER_WITHIN_HORIZON"].append(name)
        elif final_start[lane] == 1:
            categories["E1"].append(name)
        elif e2_rung.get(lane) == final_start[lane]:
            categories["E2_ORBIT_BOUNDARY"].append(name)
        else:
            categories["OTHER_RUNG"].append(name)
    category_counts = {label: len(rows) for label, rows in categories.items()}
    stabilization_histogram = dict(sorted(Counter(final_start.values()).items()))
    censoring_verdict = (
        "STABILIZATION_INCOMPLETE_AT_HORIZON"
        if categories["NEVER_WITHIN_HORIZON"]
        else "STABILIZATION_COMPLETE_WITHIN_HORIZON"
    )
    histogram_pass = (
        category_counts
        == {
            "E1": 56,
            "E2_ORBIT_BOUNDARY": 0,
            "OTHER_RUNG": 126,
            "NEVER_WITHIN_HORIZON": 566,
        }
        and len(never_set) == 566
        and len(set_but_uncertifiable) == 0
        and censoring_verdict == "STABILIZATION_INCOMPLETE_AT_HORIZON"
        and sum(category_counts.values()) == lanes
    )

    tick_table = {}
    tick_at_e2 = []
    tick_later = []
    for lane in sorted(e2_tick, key=lambda index: short_key(keys[index])):
        name = short_key(keys[lane])
        if boundary_start_ordinal[lane] == 1:
            classification = "AT_E2_STAMP"
            tick_at_e2.append(name)
        else:
            classification = "LATER_TICK"
            tick_later.append(name)
        tick_table[name] = {
            "classification": classification,
            "E2_tick": e2_tick[lane],
            "tick_clean_depth": boundary_depths[lane],
            "tick_runs": boundary_runs[lane],
            "tick_rle_sha256": boundary_hashers[lane].hexdigest(),
            "stabilization_tick_ordinal": boundary_start_ordinal[lane],
            "stabilization_tick": boundary_start_tick[lane],
            "final_tick_run_confirmations": boundary_count[lane],
        }
    tick_never_set = lanes - len(e2_tick)
    tick_counts = {
        "AT_E2_STAMP": len(tick_at_e2),
        "LATER_TICK": len(tick_later),
        "NOWHERE": tick_never_set,
    }
    tick_certified = len(tick_at_e2) + len(tick_later)
    tick_final_singletons = sum(boundary_count[lane] == 1 for lane in e2_tick)
    tick_pass = (
        sum(tick_counts.values()) == lanes
        and tick_certified == len(e2_tick) == 114
        and tick_never_set == lanes - len(e2_tick)
        and all(
            boundary_depths[lane] >= boundary_count[lane] >= 1 for lane in e2_tick
        )
        and all(boundary_depths[lane] == 0 for lane in range(lanes) if lane not in e2_tick)
    )
    if tick_counts == {"AT_E2_STAMP": 114, "LATER_TICK": 0, "NOWHERE": 634}:
        tick_finding = (
            "Literal tick-stability rescues the landed E2 census uniformly: all 114 tick-set "
            "keys land at E2 and 634 are never tick-set. This is reversal-grade for the "
            "primary interpretation, not its computation; final-singleton cases are reported."
        )
    elif tick_later:
        tick_finding = (
            f"Literal tick-stability reproduces the landed E2 census of 114 but is not "
            f"uniform at E2: E2={len(tick_at_e2)}, later={len(tick_later)}, "
            f"nowhere={tick_counts['NOWHERE']}; final-singleton cases={tick_final_singletons}."
        )
    else:
        tick_finding = (
            f"Tick stability remains censored: certified={tick_certified}, "
            f"nowhere={tick_counts['NOWHERE']}."
        )

    arithmetic_witness_count = sum(depths[lane] - current_count[lane] for lane in stamped)
    witness_pass = (
        online_witness_count == arithmetic_witness_count == EXPECTED_WITNESSES
    )

    final_replay_bit_mismatches = sum(
        (
            (plane & lower_mask)
            ^ ((plane >> lanes) & lower_mask)
        ).bit_count()
        for plane in planes
    )
    blocklist, checker_source = primary_blocklist_report()
    input_paths_literal = list(AUDIT_INPUT_PATHS)
    input_paths_exist = all(
        not Path(path).is_absolute() and (ROOT / path).is_file()
        for path in AUDIT_INPUT_PATHS
    )
    input_shas = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    initial_hasher = sha256()
    for state in states:
        initial_hasher.update(bytes(state))
    runtime = time.monotonic() - started
    controls_core = {
        "audit_input_paths_literal": input_paths_literal,
        "audit_input_paths_exist_worktree_relative": input_paths_exist,
        "input_shas": input_shas,
        "checker_sha256": sha256(checker_source).hexdigest(),
        "initial_census_sha256": initial_hasher.hexdigest(),
        "primary_blocklist": blocklist,
        "determinism": {
            "full_census_mirrored_lanes": lanes,
            "clean_event_bit_mismatches": clean_replay_mismatches,
            "stamp_sha_mismatches": stamp_sha_replay_mismatches,
            "final_state_bit_mismatches": final_replay_bit_mismatches,
            "scalar_vs_bitslice_first_orbit_equal": scalar_shadow_match,
        },
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < 1400,
    }
    controls_prepass = (
        input_paths_exist
        and blocklist["pass"]
        and clean_replay_mismatches == 0
        and stamp_sha_replay_mismatches == 0
        and final_replay_bit_mismatches == 0
        and scalar_shadow_match
        and runtime < 1400
    )

    regression_payload = {
        "finding": (
            "Cycle-860 regression is reproduced exactly: E1=182, E2=114, "
            "split=34/49/31, E1-only=68, and the joint content digest matches."
        ),
        "setup": setup,
        "regression": regression,
        "clean_moments": clean_moments,
        "clean_occurrences": clean_occurrences,
        "ladder_depth_histogram": dict(sorted(Counter(depths).items())),
        "content_sequence_table_sha256": sequence_digest,
        "per_key_sequence_rows_verified": len(sequence_table),
    }
    zero_payload = {
        "finding": (
            f"Exactly {changed_after_e2} of 114 both-stamped keys change content after E2; "
            f"of the remaining {len(counterexamples)} reversal counterexamples, "
            f"{len(first_at_e2)} first stabilize exactly at E2 and {len(stable_before_e2)} "
            "were already stable before E2. The primary's claimed zero is refuted."
        ),
        "both_stamped": len(e2_tick),
        "content_changes_after_E2_stamp": changed_after_e2,
        "counterexamples": counterexamples,
        "counterexample_subtypes": {
            "first_stabilization_at_E2": len(first_at_e2),
            "already_stable_before_E2": len(stable_before_e2),
        },
        "per_key_evidence": zero_table,
    }
    histogram_payload = {
        "finding": (
            "The 56 / 0 / 126 / 566 histogram is reproduced; the 566 censored keys are "
            "566 never-set and 0 set-but-uncertifiable, so "
            "STABILIZATION_INCOMPLETE_AT_HORIZON is exact for unrestricted clean events."
        ),
        "counts": category_counts,
        "censoring": {
            "never_set": len(never_set),
            "set_but_uncertifiable": len(set_but_uncertifiable),
            "total_never_within_horizon": len(categories["NEVER_WITHIN_HORIZON"]),
        },
        "verdict": censoring_verdict,
        "stabilization_histogram": stabilization_histogram,
        "per_category_keys_sha256": sha256(compact(categories).encode("utf-8")).hexdigest(),
    }
    tick_payload = {
        "finding": tick_finding,
        "definition": (
            "first orbit-boundary clean event whose content equals every later "
            "orbit-boundary clean event within the horizon"
        ),
        "histogram": tick_counts,
        "tick_never_set": tick_never_set,
        "final_singleton_vacuous_cases": tick_final_singletons,
        "certified_tick_stability": tick_certified,
        "landed_census_reproduced": {
            "E1_182": tick_certified == 182,
            "E2_114": tick_certified == 114,
        },
        "per_tick_set_key_sha256": sha256(compact(tick_table).encode("utf-8")).hexdigest(),
        "at_E2_keys": tick_at_e2,
        "later_tick_keys": tick_later,
    }
    witness_payload = {
        "finding": (
            "Independent online transition counting and end-of-ladder arithmetic both "
            "give 2,223,285 contradiction witnesses."
        ),
        "online_transition_count": online_witness_count,
        "end_of_ladder_arithmetic_count": arithmetic_witness_count,
        "expected": EXPECTED_WITNESSES,
    }

    certificate_rows = (
        ("THE_REGRESSION_AND_LADDERS", sequence_pass, regression_payload),
        ("THE_ZERO_AT_E2", zero_pass, zero_payload),
        ("THE_HISTOGRAM_AND_CENSORING", histogram_pass, histogram_payload),
        ("THE_TICK_RESTRICTED_RESCUE", tick_pass, tick_payload),
        ("THE_WITNESS_COUNT", witness_pass, witness_payload),
    )
    base_lines = [
        ("PASS" if passed else "FAIL") + f" {label} :: " + compact(payload)
        for label, passed, payload in certificate_rows
    ]
    scientific_pass = all(passed for _label, passed, _payload in certificate_rows)

    stdout_bytes = 0
    output_lines = []
    controls_pass = False
    for _attempt in range(20):
        controls = dict(controls_core)
        controls["stdout_bytes"] = stdout_bytes
        controls["stdout_under_150KB"] = stdout_bytes < 150 * 1024 if stdout_bytes else True
        controls_pass = controls_prepass and controls["stdout_under_150KB"]
        final_pass = scientific_pass and controls_pass
        output_lines = base_lines + [
            ("PASS" if controls_pass else "FAIL") + " CONTROLS :: " + compact(controls),
            (
                "CYCLE862_STABILIZATION_INDEPENDENT_CHECK_PASS"
                if final_pass
                else "CYCLE862_STABILIZATION_INDEPENDENT_CHECK_HONEST_FAIL"
            ),
        ]
        measured = len(("\n".join(output_lines) + "\n").encode("utf-8"))
        if measured == stdout_bytes:
            break
        stdout_bytes = measured
    else:
        raise AssertionError("stdout byte count did not converge")

    print("\n".join(output_lines))
    return 0 if scientific_pass and controls_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
