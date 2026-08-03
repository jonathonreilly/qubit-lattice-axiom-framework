#!/usr/bin/env python3
"""Cycles 866-867 finale: INDEPENDENT ADVERSARIAL CHECKER.

Isolated re-implementation.  The two primaries (866 scaled banks, 867
composed record write) and the 863 replay substrate they lean on are
BLOCKLISTED at import: they are read as text/AST only.  Every number is
re-derived here from the pinned Cycle-719 kernel alone.

Attacks:
  THE_SCALED_REPLAY   -- own B=3/B=4 substrate, census, dirty partition,
                         sync bookkeeping; verify 866's declared numbers,
                         plus an uncapped-stream control on the headline.
  THE_COMPOSED_REPLAY -- own dead-wire derivation (structural AND
                         dynamical), own register write model, own
                         annotation replay; verify 867's headline numbers.
  THE_GENTLER_PROBE   -- constructive: correct the chunk decomposition and
                         the near/far labelling, then test three gentler
                         declared perturbation classes.
  THE_SCOPE_AUDIT     -- cap/granularity disclosure completeness of both
                         primaries, by AST over their sources.
  CONTROLS            -- shas, blocklist, determinism, paths, runtime.

Declared probe of this checker (complete):
  866 leg: B in {3,4}, events {0,1}, k=2 pairwise-separated, horizon 8,192
    orbits, event/pair store cap 1,024 per lane (matching the primary),
    plus an UNCAPPED counter for the on-tick control; pair-cadence
    signatures compared at top-3 gaps (primary's granularity) and at the
    FULL gap histogram.
  867 leg: B=2, k=2..5 census (748 lanes), horizon 16,384 orbits,
    dead-wire window 512 orbits chunk-granular then 4,096 orbit-granular,
    register cap 64 slots per bank per lane (the primary's undisclosed
    REGISTER_CAP, reproduced and reported), locality boundary cap 1,100,
    lane cap 32, plus a declared path-dependence sample of up to 32 lanes
    with first-clean boundary >= 2.
bounded_theorem, authority none, audit unset.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle863_time_from_records_2026_07_28.py",
    "scripts/frontier_cycle866_scaled_banks_2026_07_28.py",
    "scripts/frontier_cycle867_composed_record_write_2026_07_28.py",
)
KERNEL_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "acabf4e0df9d2290842eb94599f19e2a7ea4a99dd7729905896feddb3c6822cc",
    AUDIT_INPUT_PATHS[3]:
        "49605f6d0730e224d6c4cd25a182ec49e0c7d2f2316851bc2755632dcbe2c828",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "1eed343ece2880de0933ee6d5f69c06ab1e5e05a",
    AUDIT_INPUT_PATHS[3]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
}
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

# ---- declared probe constants (this checker) ---------------------------
B866 = (3, 4)
EVENTS_866 = (0, 1)
K866 = 2
HORIZON_866 = 8_192
STORE_CAP_866 = 1_024

B867 = 2
KMIN_867, KMAX_867 = 2, 5
HORIZON_867 = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
LOC_BOUNDARY_CAP = 1_100
LOC_LANE_CAP = 32

CLAIM_866 = {
    3: {"stations": 19, "census_size": 304, "on_tick": 0.058037,
        "first_allsync_equals_e2": "0/38", "stamped_e1": 60,
        "stamped_e2": 38, "native_functional": False,
        "gauge_functional": False, "max_offset": 8,
        "distinct_pair_signatures": 3},
    4: {"stations": 27, "census_size": 648, "on_tick": 0.048992,
        "first_allsync_equals_e2": "0/70", "stamped_e1": 107,
        "stamped_e2": 70, "native_functional": False,
        "gauge_functional": False, "max_offset": 16,
        "distinct_pair_signatures": 6},
}
CLAIM_867 = {
    "dead_wire_count": 5668, "safe_slot_pool": 5270, "slots_allocated": 129,
    "wire_bits_set_total": 92_120, "total_register_write_events": 3_948_825,
    "dead_activation_conflicts": 0, "write_once_violations": 0,
    "moment_exact": 164, "annotation_stamps": 164,
    "composed_first_writes": 164, "lanes_with_first_slot_bit": 748,
    # v3 certificate C (the in-block repair this checker forced): 32 lanes,
    # 4 payload wires per side by kernel pack-state bank membership,
    # (probes, fired, content_equal) per class and side, all caps disclosed.
    "locality_lanes": 32, "wires_per_side": 4,
    "wire_visible_write_events": 92_120,
    "write_events_beyond_cap_not_wire_visible": 3_856_705,
    "per_class": {
        "one_flip": {"near": (32, 32, 0), "far": (32, 32, 0)},
        "late_acting": {"near": (13, 13, 0), "far": (25, 25, 0)},
        "untouched_in_chunk": {"near": (19, 19, 0), "far": (15, 15, 0)},
        "flip_and_restore": {"near": (32, 32, 32), "far": (32, 29, 29)},
    },
}
# The v2 certificate C this checker REFUTED, kept as the regression target:
# 2 lanes sampled, near 0/0, far 0/0, produced by uniform chunk slicing and
# a positional near/far split whose far arm was empty.
CLAIM_867_V2_SUPERSEDED = {"locality_lanes": 2, "near_fired": 0,
                           "far_fired": 0}


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(b: bytes) -> str:
    return sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def lanes_of(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def clean_mask(columns, indices, universe):
    dirty = 0
    for w in indices:
        dirty |= columns[w]
    return universe & ~dirty


def separated(positions, stations):
    occ = set(positions)
    return all((s + 1) % stations not in occ for s in occ)


# ---- own substrate ------------------------------------------------------
def kernel_seeds(program, bank_count):
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(bank_count)
    stations = len(program)
    seeds, failures = {}, 0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, ra, rb, trace = K.run_orbit(before, program)
        failures += int(not (
            after == K.A.apply_semantic(before, allocator)
            and ra == (1,) + (0,) * (stations - 1) and not any(rb)
            and len(trace) == stations
        ))
        seeds[event] = before
        state = after
    return seeds, failures


def watched_wires():
    return (K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
            *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK)


def partition(bank_count):
    """Index sets: watched-per-bank, FULL per-bank block, links, source."""
    banks, links = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks)
    zl = tuple(tuple(0 for _ in l) for l in links)
    base = K.M.pack_state(zb, zl)
    watched = set(watched_wires())
    per_bank, full_bank, bad = [], [], 0
    for bi in range(bank_count):
        w_rows, a_rows = set(), set()
        for wire in range(len(zb[bi])):
            ch = [list(b) for b in zb]
            ch[bi][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in ch), zl)
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            bad += int(len(d) != 1)
            a_rows.add(d[0])
            if wire in watched:
                w_rows.add(d[0])
        per_bank.append(tuple(sorted(w_rows)))
        full_bank.append(frozenset(a_rows))
    link_rows = set()
    for li, link in enumerate(zl):
        for wire in range(len(link)):
            ch = [list(r) for r in zl]
            ch[li][wire] = 1
            marked = K.M.pack_state(zb, tuple(tuple(r) for r in ch))
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            bad += int(len(d) != 1)
            link_rows.add(d[0])
    return {"per_bank": tuple(per_bank), "full_bank": tuple(full_bank),
            "links": tuple(sorted(link_rows)),
            "source": K.R3.X.SOURCE_POINTER, "marker_failures": bad,
            "state_width": len(base)}


def semantic_partition_control(bank_count, part):
    """Independent check of the index sets against K.M.unpack_state."""
    banks, links = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks)
    zl = tuple(tuple(0 for _ in l) for l in links)
    watched = watched_wires()
    disagreements = 0
    for bi in range(bank_count):
        for wire in (watched[0], watched[-1]):
            ch = [list(b) for b in zb]
            ch[bi][wire] = 1
            state = K.M.pack_state(tuple(tuple(b) for b in ch), zl)
            ub, _ul = K.M.unpack_state(state, bank_count)
            semantic_dirty = any(
                ub[j][w] for j in range(bank_count) for w in watched
            )
            index_dirty = any(
                state[i] for j in range(bank_count) for i in part["per_bank"][j]
            )
            disagreements += int(semantic_dirty != index_dirty)
            disagreements += int(not ub[bi][wire])
    return disagreements


def masked_schedules(program, sim_keys):
    stations = len(program)
    macros = [K.mapped_macro(row) for row in program]
    rows = []
    for step in range(stations):
        sched = []
        for station in range(stations):
            mask = sum(
                1 << lane
                for lane, (_k, _e, pos) in enumerate(sim_keys)
                if (station - step) % stations in pos
            )
            if mask:
                for g in macros[station]:
                    if g.kind == "X":
                        sched.append((0, g.wires[0], 0, 0, mask))
                    elif g.kind == "CNOT":
                        sched.append((1, g.wires[0], g.wires[1], 0, mask))
                    else:
                        sched.append(
                            (2, g.wires[0], g.wires[1], g.wires[2], mask))
        rows.append(tuple(sched))
    return tuple(rows)


def compile_chunks(schedules):
    fns = []
    for sched in schedules:
        src = ["def step(c):"]
        for kind, a, b, c3, mask in sched:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["step"])
    return tuple(fns)


def initial_states(program, seeds, census):
    stations = len(program)
    states, failures = [], 0
    for _k, event, pos in census:
        after, ra, rb, _ = K.run_orbit(seeds[event], program,
                                       token_positions=pos)
        failures += int(ra != tuple(int(s in pos) for s in range(stations))
                        or any(rb))
        states.append(after)
    return tuple(states), failures


def pack_columns(states):
    return [sum(s[w] << lane for lane, s in enumerate(states))
            for w in range(len(states[0]))]


def true_chunks(program, positions):
    """CORRECT per-step gate lists (variable length, station order)."""
    stations = len(program)
    macros = [K.mapped_macro(row) for row in program]
    out = []
    for step in range(stations):
        gates = []
        for station in range(stations):
            if (station - step) % stations in positions:
                gates.extend(macros[station])
        out.append(tuple(gates))
    return tuple(out)


# ---- ATTACK 1: THE_SCALED_REPLAY ---------------------------------------
def scaled_leg(bank_count):
    program = K.interleaved_program(bank_count)
    stations = len(program)
    seeds, seed_fail = kernel_seeds(program, bank_count)
    census = tuple(sorted(
        (K866, event, pos)
        for pos in combinations(range(stations), K866)
        if separated(pos, stations)
        for event in EVENTS_866
    ))
    n = len(census)
    part = partition(bank_count)
    global_dirty = tuple(sorted(
        set().union(*[set(x) for x in part["per_bank"]])
        | set(part["links"]) | {part["source"]}))
    states, init_fail = initial_states(program, seeds, census)
    sim = census + (census[0],)
    columns = pack_columns(states + (states[0],))
    chunks = compile_chunks(masked_schedules(program, sim))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    dup = n
    B = bank_count

    allsync_store = [[] for _ in range(n)]
    global_store = [[] for _ in range(n)]
    global_count = [0] * n
    pair_ids = tuple(combinations(range(B), 2))
    pair_store = {p: [[] for _ in range(n)] for p in pair_ids}
    pair_on_uncapped = {p: [0, 0] for p in pair_ids}
    bank_first = [[None] * B for _ in range(n)]
    e1, e2 = {}, {}
    mismatches = 0
    uncapped_total = uncapped_on = 0

    def observe(boundary):
        nonlocal mismatches, uncapped_total, uncapped_on
        g = clean_mask(columns, global_dirty, uni_sim)
        mismatches += int(bool(g & 1) != bool(g & (1 << dup)))
        ga = g & uni_all
        bmasks = [clean_mask(columns, part["per_bank"][bi], uni_all)
                  for bi in range(B)]
        for lane in lanes_of(ga):
            global_count[lane] += 1
            if len(global_store[lane]) < STORE_CAP_866:
                global_store[lane].append(boundary)
            if census[lane] not in e1:
                e1[census[lane]] = boundary
        allm = uni_all
        for bm in bmasks:
            allm &= bm
        on_tick = boundary % stations == 0
        pop = bin(allm).count("1")
        uncapped_total += pop
        uncapped_on += pop if on_tick else 0
        for lane in lanes_of(allm):
            if len(allsync_store[lane]) < STORE_CAP_866:
                allsync_store[lane].append(boundary)
        for (i, j) in pair_ids:
            pm = bmasks[i] & bmasks[j]
            cnt = bin(pm).count("1")
            pair_on_uncapped[(i, j)][0] += cnt
            if on_tick:
                pair_on_uncapped[(i, j)][1] += cnt
            for lane in lanes_of(pm):
                store = pair_store[(i, j)][lane]
                if len(store) < STORE_CAP_866:
                    store.append(boundary)
        for bi, bm in enumerate(bmasks):
            for lane in lanes_of(bm):
                if bank_first[lane][bi] is None:
                    bank_first[lane][bi] = (boundary, global_count[lane])
        return ga

    observe(0)
    ga = 0
    for orbit in range(1, HORIZON_866 + 1):
        for step, chunk in enumerate(chunks, 1):
            chunk(columns)
            ga = observe((orbit - 1) * stations + step)
        for lane in lanes_of(ga):
            if census[lane] not in e2:
                e2[census[lane]] = orbit

    stored_total = stored_on = 0
    first_match = first_total = 0
    for lane, key in enumerate(census):
        syncs = allsync_store[lane]
        for b in syncs:
            stored_total += 1
            stored_on += int(b % stations == 0)
        if key in e2 and syncs:
            first_total += 1
            first_match += int(syncs[0] == e2[key] * stations
                               or (syncs[0] == 0 and e2[key] == 0))

    pair_top3, pair_full_sig, pair_frac = {}, {}, {}
    for pid in pair_ids:
        gaps = Counter()
        pt = po = 0
        for lane in range(n):
            seq = pair_store[pid][lane]
            for b in seq:
                pt += 1
                po += int(b % stations == 0)
            for a, b2 in zip(seq, seq[1:]):
                gaps[b2 - a] += 1
        pair_top3[str(pid)] = gaps.most_common(3)
        pair_full_sig[str(pid)] = compact(sorted(gaps.items()))
        pair_frac[str(pid)] = round(po / pt, 4) if pt else None
    distinct_top3 = len({compact(v) for v in pair_top3.values()})
    distinct_full = len(set(pair_full_sig.values()))

    cohorts = defaultdict(list)
    rung = {}
    for lane, key in enumerate(census):
        if key not in e2:
            continue
        boundary = e2[key] * stations
        events = global_store[lane]
        if boundary in events:
            rung[key] = events.index(boundary) + 1
        elif e2[key] == 0 and events and events[0] == 0:
            rung[key] = 1
    for key, r in rung.items():
        cohorts[e2[key]].append((key, r))
    rows = []
    for _moment, members in sorted(cohorts.items()):
        if len(members) < 2:
            continue
        base = min(r for _k, r in members)
        for key, r in members:
            lane = census.index(key)
            bf = bank_first[lane]
            native = (tuple(sorted((bf[i][1], i) for i in range(B) if bf[i]))
                      if any(bf) else None)
            rows.append({"offset": r - base, "native": compact(native),
                         "gauge": e1.get(key)})

    def functional(field):
        seen = {}
        for row in rows:
            v = row[field]
            if v in seen and seen[v] != row["offset"]:
                return False
            seen[v] = row["offset"]
        return True

    hist = dict(sorted(Counter(r["offset"] for r in rows).items()))
    claim = CLAIM_866[bank_count]
    observed = {
        "B": bank_count, "stations": stations, "census_size": n,
        "stamped_e1": len(e1), "stamped_e2": len(e2),
        "allsync_stored": stored_total,
        "allsync_on_tick_fraction":
            round(stored_on / stored_total, 6) if stored_total else None,
        "first_allsync_equals_e2": f"{first_match}/{first_total}",
        "cohort_member_rows": len(rows),
        "offset_histogram_max_key": max(hist) if hist else None,
        "native_pattern_functional": functional("native"),
        "gauge_e1_functional": functional("gauge"),
        "distinct_pair_cadence_signatures_top3": distinct_top3,
        "mismatches": mismatches,
    }
    controls = {
        "seed_failures": seed_fail, "init_failures": init_fail,
        "marker_failures": part["marker_failures"],
        "stations_equals_8B_minus_5": stations == 8 * bank_count - 5,
        "semantic_partition_disagreements":
            semantic_partition_control(bank_count, part),
        "uncapped_allsync_events": uncapped_total,
        "uncapped_on_tick_fraction":
            round(uncapped_on / uncapped_total, 6) if uncapped_total else None,
        "store_cap_binding_lanes": sum(
            1 for lane in range(n)
            if len(allsync_store[lane]) >= STORE_CAP_866),
        "distinct_pair_cadence_signatures_full_histogram": distinct_full,
        "pair_on_tick_fractions_capped": pair_frac,
        "pair_on_tick_fractions_uncapped": {
            str(p): (round(v[1] / v[0], 4) if v[0] else None)
            for p, v in pair_on_uncapped.items()},
        "pair_dominant_gaps_top3": pair_top3,
    }
    agree = {
        "stations": stations == claim["stations"],
        "census_size": n == claim["census_size"],
        "on_tick": observed["allsync_on_tick_fraction"] == claim["on_tick"],
        "first_allsync_equals_e2":
            observed["first_allsync_equals_e2"]
            == claim["first_allsync_equals_e2"],
        "stamped_e1": len(e1) == claim["stamped_e1"],
        "stamped_e2": len(e2) == claim["stamped_e2"],
        "native_functional":
            observed["native_pattern_functional"] == claim["native_functional"],
        "gauge_functional":
            observed["gauge_e1_functional"] == claim["gauge_functional"],
        "max_offset": observed["offset_histogram_max_key"]
            == claim["max_offset"],
        "distinct_pair_signatures":
            distinct_top3 == claim["distinct_pair_signatures"],
        "mismatches_zero": mismatches == 0,
    }
    return {"observed": observed, "controls": controls, "agree": agree}


def kernel_cross_check(bank_count, lanes_to_check=2, boundaries=22):
    """Validate the bitsliced fast path against K.A.apply_semantic."""
    program = K.interleaved_program(bank_count)
    stations = len(program)
    seeds, _ = kernel_seeds(program, bank_count)
    census = tuple(sorted(
        (K866, event, pos)
        for pos in combinations(range(stations), K866)
        if separated(pos, stations) for event in EVENTS_866))
    sub = census[:lanes_to_check]
    states, _ = initial_states(program, seeds, sub)
    columns = pack_columns(states)
    chunks = compile_chunks(masked_schedules(program, sub))
    walks = [list(s) for s in states]
    chunkings = [true_chunks(program, key[2]) for key in sub]
    failures = 0
    for b in range(boundaries):
        chunks[b % stations](columns)
        for i in range(len(sub)):
            walks[i] = list(K.A.apply_semantic(
                tuple(walks[i]), chunkings[i][b % stations]))
            bit = 1 << i
            sliced = tuple(int(bool(c & bit)) for c in columns)
            failures += int(sliced != tuple(walks[i]))
    return {"lanes": len(sub), "boundaries": boundaries,
            "bitslice_vs_kernel_failures": failures}


# ---- ATTACK 2/3: composed record write + gentler probe -----------------
def composed_leg():
    program = K.interleaved_program(B867)
    stations = len(program)
    seeds, seed_fail = kernel_seeds(program, B867)
    census = tuple(sorted(
        (k, event, pos)
        for k in range(KMIN_867, KMAX_867 + 1)
        for pos in combinations(range(stations), k)
        if separated(pos, stations)
        for event in range(2 * B867)))
    n = len(census)
    part = partition(B867)
    global_dirty = tuple(sorted(
        set(part["per_bank"][0]) | set(part["per_bank"][1])
        | set(part["links"]) | {part["source"]}))
    bank_dirty = part["per_bank"]
    states, init_fail = initial_states(program, seeds, census)
    sim = census + (census[0],)
    schedules = masked_schedules(program, sim)
    chunks = compile_chunks(schedules)
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    dup = n
    columns0 = pack_columns(states + (states[0],))
    width = len(columns0)

    gate_inputs, gate_targets = set(), set()
    for sched in schedules:
        for kind, a, b, c3, _m in sched:
            if kind == 0:
                gate_targets.add(a)
            elif kind == 1:
                gate_inputs.add(a)
                gate_targets.add(b)
            else:
                gate_inputs.update((a, b))
                gate_targets.add(c3)
    touched = gate_inputs | gate_targets
    structural_pool = tuple(w for w in range(width)
                            if w not in touched and columns0[w] == 0)

    # Dynamical dead-wire derivation over the primary's declared window.
    # Only gate TARGETS can ever change a column, so accumulating over the
    # target set is exactly equivalent to accumulating over all wires
    # (non-targets keep their initial column forever); asserted below.
    acc = list(columns0)
    work = list(columns0)
    target_list = tuple(sorted(gate_targets))
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in chunks:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in target_list:
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in target_list:
                acc[w] |= work[w]
    nontarget_drift = sum(
        1 for w in range(width) if w not in gate_targets
        and work[w] != columns0[w])
    dead_wires = tuple(w for w in range(width) if (acc[w] & uni_sim) == 0)
    dead_set = set(dead_wires)
    dynamical_pool = tuple(w for w in dead_wires if w not in touched)

    slot_tags = [("G", 0)] + [(f"B{b}", k) for b in (0, 1)
                              for k in range(REGISTER_CAP)]
    slot_of = {tag: structural_pool[i] for i, tag in enumerate(slot_tags)}
    slot_wires = set(slot_of.values())

    # composed scan with REAL register writes
    columns = list(columns0)
    register_events = 0
    bank_ordinal = [[0, 0] for _ in range(n)]
    write_once_violations = 0
    dead_conflicts = 0
    written_pairs = set()
    single_slot_collisions = 0
    single_slot_seen = set()
    # Non-target dead wires provably cannot change; monitoring the dead
    # wires that ARE gate targets is equivalent to monitoring all of them,
    # and the residual is re-verified over the full dead set after the run.
    monitored = tuple(w for w in dead_wires
                      if w in gate_targets and w not in slot_wires)

    def wire_write(tag, lane):
        nonlocal write_once_violations
        wire = slot_of[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit
        written_pairs.add((tag, lane))

    e1_composed: dict = {}
    prev_bank = [clean_mask(columns, bank_dirty[b], uni_all) for b in (0, 1)]
    g0 = clean_mask(columns, global_dirty, uni_sim)
    mismatches = int(bool(g0 & 1) != bool(g0 & (1 << dup)))
    for lane in lanes_of(g0 & uni_all):
        e1_composed.setdefault(census[lane], 0)
        wire_write(("G", 0), lane)
        register_events += 1
    boundary = 0
    for orbit in range(1, HORIZON_867 + 1):
        for chunk in chunks:
            chunk(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, uni_sim)
            mismatches += int(bool(g & 1) != bool(g & (1 << dup)))
            for lane in lanes_of(g & uni_all):
                if census[lane] not in e1_composed:
                    e1_composed[census[lane]] = boundary
            for b in (0, 1):
                bm = clean_mask(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in lanes_of(edge):
                    ordinal = bank_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                    if (b, lane) in single_slot_seen:
                        single_slot_collisions += 1
                    single_slot_seen.add((b, lane))
                    bank_ordinal[lane][b] = ordinal + 1
                    register_events += 1
                prev_bank[b] = bm
            for w in monitored:
                if columns[w] & uni_sim:
                    dead_conflicts += 1
                    break

    residual_dead_drift = sum(
        1 for w in dead_wires
        if w not in slot_wires and w not in gate_targets
        and columns[w] & uni_sim)
    wire_bits_set = sum(bin(columns[slot_of[t]]).count("1") for t in slot_tags)
    first_slot_lanes = set()
    for tag in (("G", 0), ("B0", 0), ("B1", 0)):
        first_slot_lanes |= set(lanes_of(columns[slot_of[tag]] & uni_all))

    # independent annotation replay (no register writes), same horizon
    anno = list(columns0)
    anno_e1: dict = {}
    anno_first_clean = [None] * n
    anno_mismatch = 0
    ga0 = clean_mask(anno, global_dirty, uni_sim)
    anno_mismatch += int(bool(ga0 & 1) != bool(ga0 & (1 << dup)))
    for lane in lanes_of(ga0 & uni_all):
        anno_e1.setdefault(census[lane], 0)
        if anno_first_clean[lane] is None:
            anno_first_clean[lane] = 0
    boundary = 0
    for orbit in range(1, HORIZON_867 + 1):
        for chunk in chunks:
            chunk(anno)
            boundary += 1
            g = clean_mask(anno, global_dirty, uni_sim)
            anno_mismatch += int(bool(g & 1) != bool(g & (1 << dup)))
            for lane in lanes_of(g & uni_all):
                if census[lane] not in anno_e1:
                    anno_e1[census[lane]] = boundary
                if anno_first_clean[lane] is None:
                    anno_first_clean[lane] = boundary

    moment_exact = sum(1 for key, b in e1_composed.items()
                       if anno_e1.get(key) == b)

    composed = {
        "certificate_A": {
            "state_width": width,
            "dead_wire_count": len(dead_wires),
            "safe_slot_pool_dynamical": len(dynamical_pool),
            "safe_slot_pool_structural": len(structural_pool),
            "slots_allocated": len(slot_of),
            "slots_in_gate_inputs": len(slot_wires & gate_inputs),
            "slots_in_gate_targets": len(slot_wires & gate_targets),
            "slots_in_global_dirty": len(slot_wires & set(global_dirty)),
            "slots_in_bank_blocks": len(
                slot_wires & (part["full_bank"][0] | part["full_bank"][1])),
            "dead_wires_monitored_per_boundary": len(monitored),
            "nontarget_wire_drift": nontarget_drift,
            "residual_dead_drift_end_of_run": residual_dead_drift,
            "dead_activation_conflicts": dead_conflicts,
            "write_once_violations": write_once_violations,
            "total_register_write_events": register_events,
            "wire_bits_set_total": wire_bits_set,
            "distinct_slot_lane_pairs": len(written_pairs),
            "writes_dropped_by_undisclosed_register_cap":
                register_events - wire_bits_set,
            "collisions_if_one_slot_per_bank_per_lane":
                single_slot_collisions,
        },
        "certificate_B": {
            "annotation_stamps_at_horizon": len(anno_e1),
            "composed_first_writes": len(e1_composed),
            "moment_exact_matches": moment_exact,
            "lanes_with_any_first_slot_bit": len(first_slot_lanes),
            "census_lanes": n,
            "existence_readback_is_saturated": len(first_slot_lanes) == n,
            "annotation_replay_mismatches": anno_mismatch,
        },
        "controls": {"seed_failures": seed_fail, "init_failures": init_fail,
                     "composed_mismatches": mismatches},
    }
    return composed, {
        "program": program, "stations": stations, "census": census,
        "seeds": seeds, "part": part, "global_dirty": global_dirty,
        "bank_dirty": bank_dirty, "dead_set": dead_set, "width": width,
        "first_clean": anno_first_clean,
    }


def gentler_probe(ctx):
    program = ctx["program"]
    stations = ctx["stations"]
    census = ctx["census"]
    seeds = ctx["seeds"]
    part = ctx["part"]
    global_dirty = ctx["global_dirty"]
    bank_dirty = ctx["bank_dirty"]
    dead_set = ctx["dead_set"]
    width = ctx["width"]
    first_clean = ctx["first_clean"]

    payload_pool = [w for w in range(width)
                    if w not in dead_set and w not in set(global_dirty)]
    primary_split = {
        0: [w for w in payload_pool if w < width // 2][:4],
        1: [w for w in payload_pool if w >= width // 2][:4],
    }
    correct_split = {
        b: [w for w in payload_pool if w in part["full_bank"][b]][:4]
        for b in (0, 1)
    }
    labelling = {
        "primary_bank_payload_0": primary_split[0],
        "primary_bank_payload_1": primary_split[1],
        "primary_bank1_list_is_empty": primary_split[1] == [],
        "primary_bank0_members_actually_in_bank0":
            [w in part["full_bank"][0] for w in primary_split[0]],
        "state_width_half": width // 2,
        "payload_pool_max_index": max(payload_pool),
        "bank1_block_range": [min(part["full_bank"][1]),
                              max(part["full_bank"][1])],
        "corrected_bank_payload_0": correct_split[0],
        "corrected_bank_payload_1": correct_split[1],
    }

    candidates = sorted(
        (first_clean[lane], lane) for lane in range(len(census))
        if first_clean[lane] is not None
        and 0 < first_clean[lane] <= LOC_BOUNDARY_CAP)[:LOC_LANE_CAP]
    path_candidates = sorted(
        (first_clean[lane], lane) for lane in range(len(census))
        if first_clean[lane] is not None
        and 1 < first_clean[lane] <= LOC_BOUNDARY_CAP)[:LOC_LANE_CAP]

    chunk_cache: dict = {}

    def chunking(pos):
        if pos not in chunk_cache:
            chunks = true_chunks(program, pos)
            word = tuple(g for c in chunks for g in c)
            per = len(word) // stations
            buggy = tuple(word[(s % stations) * per:((s % stations) + 1) * per]
                          for s in range(stations))
            chunk_cache[pos] = (chunks, buggy, [len(c) for c in chunks], per)
        return chunk_cache[pos]

    def walk(key, upto, correct=True):
        pos = key[2]
        chunks, buggy, _lens, _per = chunking(pos)
        state, _ra, _rb, _t = K.run_orbit(seeds[key[1]], program,
                                          token_positions=pos)
        use = chunks if correct else buggy
        for b in range(upto):
            state = K.A.apply_semantic(state, use[b % stations])
        return state

    def is_clean(state):
        return all(state[w] == 0 for w in global_dirty)

    # (i) reproduce the primary's buggy reconstruction verdict
    buggy_clean = 0
    buggy_rows = {"near_fired": 0, "near_content_equal": 0,
                  "far_fired": 0, "far_content_equal": 0, "sampled": 0}
    nonuniform = 0
    for first, lane in candidates:
        key = census[lane]
        chunks, buggy, lens, per = chunking(key[2])
        nonuniform += int(len(set(lens)) != 1)
        pre = walk(key, first - 1, correct=False)
        after = K.A.apply_semantic(pre, buggy[(first - 1) % stations])
        if not is_clean(after):
            continue
        buggy_clean += 1
        base_content = sha256(bytes(after)).hexdigest()
        rec = 0 if all(after[w] == 0 for w in bank_dirty[0]) else 1
        for kind, wires in (("far", primary_split[1 - rec]),
                            ("near", primary_split[rec])):
            for wire in wires[:1]:
                mut = list(pre)
                mut[wire] ^= 1
                out = K.A.apply_semantic(tuple(mut),
                                         buggy[(first - 1) % stations])
                fired = is_clean(out)
                buggy_rows[f"{kind}_fired"] += int(fired)
                if fired:
                    buggy_rows[f"{kind}_content_equal"] += int(
                        sha256(bytes(out)).hexdigest() == base_content)
        buggy_rows["sampled"] += 1

    # (ii) corrected chunking + corrected near/far, three perturbation classes
    classes = ("one_flip", "late_acting", "untouched_in_chunk",
               "flip_and_restore")
    tally = {c: {s: {"probes": 0, "fired": 0, "content_equal": 0}
                 for s in ("near", "far")} for c in classes}
    corrected_clean = 0
    degenerate_restore = 0
    for first, lane in candidates:
        key = census[lane]
        chunks, _buggy, _lens, _per = chunking(key[2])
        pre = walk(key, first - 1, correct=True)
        last = chunks[(first - 1) % stations]
        base_after = K.A.apply_semantic(pre, last)
        if not is_clean(base_after):
            continue
        corrected_clean += 1
        base_content = sha256(bytes(base_after)).hexdigest()
        rec = 0 if all(base_after[w] == 0 for w in bank_dirty[0]) else 1
        order: dict = {}
        for idx, g in enumerate(last):
            for w in g.wires:
                order.setdefault(w, idx)
        for side, bank in (("near", rec), ("far", 1 - rec)):
            pool = correct_split[bank]
            if not pool:
                continue
            picks = {}
            picks["one_flip"] = pool[0]
            late = [w for w in pool if w in order]
            picks["late_acting"] = (max(late, key=lambda w: order[w])
                                    if late else None)
            untouched = [w for w in pool if w not in order]
            picks["untouched_in_chunk"] = untouched[0] if untouched else None
            picks["flip_and_restore"] = pool[0]
            for cls, wire in picks.items():
                if wire is None:
                    continue
                if cls == "flip_and_restore":
                    if first - 1 == 0:
                        degenerate_restore += 1
                        continue
                    pos = key[2]
                    state, _a, _b, _t = K.run_orbit(seeds[key[1]], program,
                                                    token_positions=pos)
                    s = list(state)
                    s[wire] ^= 1
                    state = tuple(s)
                    for b in range(first - 1):
                        state = K.A.apply_semantic(state,
                                                   chunks[b % stations])
                    s = list(state)
                    s[wire] ^= 1
                    out = K.A.apply_semantic(tuple(s), last)
                else:
                    mut = list(pre)
                    mut[wire] ^= 1
                    out = K.A.apply_semantic(tuple(mut), last)
                fired = is_clean(out)
                cell = tally[cls][side]
                cell["probes"] += 1
                cell["fired"] += int(fired)
                if fired:
                    cell["content_equal"] += int(
                        sha256(bytes(out)).hexdigest() == base_content)

    # (iii) path-dependence on lanes with first >= 2 (declared extension)
    path = {s: {"probes": 0, "fired": 0, "content_equal": 0}
            for s in ("near", "far")}
    for first, lane in path_candidates:
        key = census[lane]
        chunks, _b, _l, _p = chunking(key[2])
        pre = walk(key, first - 1, correct=True)
        last = chunks[(first - 1) % stations]
        base_after = K.A.apply_semantic(pre, last)
        if not is_clean(base_after):
            continue
        base_content = sha256(bytes(base_after)).hexdigest()
        rec = 0 if all(base_after[w] == 0 for w in bank_dirty[0]) else 1
        for side, bank in (("near", rec), ("far", 1 - rec)):
            pool = correct_split[bank]
            if not pool:
                continue
            wire = pool[0]
            state, _a, _bb, _t = K.run_orbit(seeds[key[1]], program,
                                             token_positions=key[2])
            s = list(state)
            s[wire] ^= 1
            state = tuple(s)
            for b in range(first - 1):
                state = K.A.apply_semantic(state, chunks[b % stations])
            s = list(state)
            s[wire] ^= 1
            out = K.A.apply_semantic(tuple(s), last)
            fired = is_clean(out)
            path[side]["probes"] += 1
            path[side]["fired"] += int(fired)
            if fired:
                path[side]["content_equal"] += int(
                    sha256(bytes(out)).hexdigest() == base_content)

    total_probes = sum(tally[c][s]["probes"] for c in classes
                       for s in ("near", "far"))
    total_fired = sum(tally[c][s]["fired"] for c in classes
                      for s in ("near", "far"))
    return {
        "labelling_audit": labelling,
        "candidates": len(candidates),
        "path_candidates": len(path_candidates),
        "chunking_bug": {
            "primary_uses_uniform_slice_len_word_over_stations": True,
            "candidate_keys_with_nonuniform_true_chunks": nonuniform,
            "primary_reconstruction_clean_lanes": buggy_clean,
            "corrected_reconstruction_clean_lanes": corrected_clean,
        },
        "primary_class_reproduced": buggy_rows,
        "corrected_classes": tally,
        "path_dependence_first_ge_2": path,
        "degenerate_restore_skips": degenerate_restore,
        "totals": {"probes": total_probes, "fired": total_fired},
    }


# ---- ATTACK 4: THE_SCOPE_AUDIT -----------------------------------------
def scope_audit():
    out = {}
    for path in (AUDIT_INPUT_PATHS[2], AUDIT_INPUT_PATHS[3]):
        text = (ROOT / path).read_text(encoding="utf-8")
        tree = ast.parse(text, filename=path)
        doc = ast.get_docstring(tree) or ""
        consts = {}
        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(
                    node.value, (ast.Constant, ast.Tuple)):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id.isupper():
                        try:
                            consts[t.id] = ast.literal_eval(node.value)
                        except Exception:
                            pass
        emitted_names: set = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.JoinedStr):
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Name):
                        emitted_names.add(sub.id)
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                tgt = node.targets[0]
                if isinstance(tgt, ast.Name) and tgt.id in (
                        "cert_a", "cert_b", "cert_c", "derived", "birth",
                        "second_clock", "summary"):
                    for sub in ast.walk(node.value):
                        if isinstance(sub, ast.Name):
                            emitted_names.add(sub.id)
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                for sub in ast.walk(node.value):
                    if isinstance(sub, ast.Dict):
                        for sn in ast.walk(sub):
                            if isinstance(sn, ast.Name) and sn.id.isupper():
                                emitted_names.add(sn.id)
        truncations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript) and isinstance(
                    node.slice, ast.Slice) and isinstance(
                    node.slice.upper, ast.Constant):
                truncations.append(f"[:{node.slice.upper.value}]")
            if isinstance(node, ast.Call) and isinstance(
                    node.func, ast.Attribute) and node.func.attr \
                    == "most_common" and node.args and isinstance(
                    node.args[0], ast.Constant):
                truncations.append(f"most_common({node.args[0].value})")
        caps = {}
        for name, value in consts.items():
            if not isinstance(value, int) or name.endswith("_BYTES") \
                    or name in ("AUDIT_TIMEOUT_SEC",):
                continue
            in_doc = (str(value) in doc
                      or f"{value:,}" in doc
                      or name.lower().replace("_", " ") in doc.lower())
            caps[name] = {"value": value, "in_docstring": in_doc,
                          "in_emitted_payload": name in emitted_names,
                          "disclosed": bool(in_doc or name in emitted_names)}
        declared_sample_keys = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Dict):
                keys = [k.value for k in node.keys
                        if isinstance(k, ast.Constant)]
                if "boundary_cap" in keys:
                    declared_sample_keys = sorted(keys)
        out[path] = {
            "declared_sample_keys": declared_sample_keys,
            "perturbation_wire_count_disclosed": any(
                "wire" in k or "perturb" in k for k in declared_sample_keys),
            "module_caps": caps,
            "undisclosed_caps": sorted(k for k, v in caps.items()
                                       if not v["disclosed"]),
            "literal_truncations": sorted(Counter(truncations).items()),
        }
    return out


# ---- CONTROLS -----------------------------------------------------------
def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"),
                     filename="self")
    literal = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    result = {
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_matches_pins": sha_rows == EXPECTED_SHA256,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_matches_pins"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"])
    return result


def determinism_control():
    digests = []
    for _ in range(2):
        program = K.interleaved_program(B867)
        stations = len(program)
        seeds, _ = kernel_seeds(program, B867)
        census = tuple(sorted(
            (k, e, p) for k in range(KMIN_867, KMAX_867 + 1)
            for p in combinations(range(stations), k) if separated(p, stations)
            for e in range(2 * B867)))
        part = partition(B867)
        gd = tuple(sorted(set(part["per_bank"][0]) | set(part["per_bank"][1])
                          | set(part["links"]) | {part["source"]}))
        states, _ = initial_states(program, seeds, census)
        cols = pack_columns(states + (states[0],))
        chunks = compile_chunks(masked_schedules(program, census + (census[0],)))
        uni = (1 << len(census)) - 1
        acc = []
        for orbit in range(1, 65):
            for chunk in chunks:
                chunk(cols)
                acc.append(clean_mask(cols, gd, uni))
        digests.append(sha256(compact(
            [len(census), gd[:8], sum(acc) % (1 << 61),
             sha256(str(acc).encode()).hexdigest()]).encode()).hexdigest())
    return {"repeat_digests_equal": digests[0] == digests[1],
            "digest": digests[0][:16]}


def main() -> int:
    started = monotonic()
    controls = source_controls()

    scaled = {}
    for B in B866:
        scaled[B] = scaled_leg(B)
    cross = kernel_cross_check(3)
    scaled_pass = all(all(scaled[B]["agree"].values()) for B in B866)
    scaled_cert = {
        "verdict": "CONFIRMED" if scaled_pass else "REFUTED",
        "per_B": {B: {"observed": scaled[B]["observed"],
                      "agreement_with_claim": scaled[B]["agree"],
                      "controls": scaled[B]["controls"]} for B in B866},
        "kernel_cross_check": cross,
        "finding": (
            "866's declared-probe numbers re-derived from the kernel alone;"
            " the store cap and the uncapped control are both reported, and"
            " pair-cadence distinctness is reported at the primary's top-3"
            " granularity AND at full gap histograms"),
    }
    scaled_cert["pass"] = bool(
        scaled_pass and cross["bitslice_vs_kernel_failures"] == 0
        and all(scaled[B]["controls"]["seed_failures"] == 0
                and scaled[B]["controls"]["init_failures"] == 0
                and scaled[B]["controls"]["marker_failures"] == 0
                and scaled[B]["controls"]["semantic_partition_disagreements"]
                == 0 and scaled[B]["controls"]["stations_equals_8B_minus_5"]
                for B in B866))

    composed, ctx = composed_leg()
    a = composed["certificate_A"]
    b = composed["certificate_B"]
    comp_agree = {
        "dead_wire_count": a["dead_wire_count"]
            == CLAIM_867["dead_wire_count"],
        "safe_slot_pool": a["safe_slot_pool_dynamical"]
            == CLAIM_867["safe_slot_pool"],
        "slots_allocated": a["slots_allocated"]
            == CLAIM_867["slots_allocated"],
        "wire_bits_set_total": a["wire_bits_set_total"]
            == CLAIM_867["wire_bits_set_total"],
        "total_register_write_events": a["total_register_write_events"]
            == CLAIM_867["total_register_write_events"],
        "dead_activation_conflicts_zero": a["dead_activation_conflicts"] == 0,
        "write_once_violations_zero": a["write_once_violations"] == 0,
        "annotation_stamps": b["annotation_stamps_at_horizon"]
            == CLAIM_867["annotation_stamps"],
        "composed_first_writes": b["composed_first_writes"]
            == CLAIM_867["composed_first_writes"],
        "moment_exact": b["moment_exact_matches"] == CLAIM_867["moment_exact"],
        "lanes_with_first_slot_bit": b["lanes_with_any_first_slot_bit"]
            == CLAIM_867["lanes_with_first_slot_bit"],
    }
    composed_cert = {
        "verdict": "CONFIRMED" if all(comp_agree.values()) else "REFUTED",
        "observed": composed,
        "agreement_with_claim": comp_agree,
        "structural_pool_equals_dynamical_pool":
            a["safe_slot_pool_structural"] == a["safe_slot_pool_dynamical"],
        "findings": [
            "safe slot pool is FULLY structural (wires no gate reads or"
            " writes, zero initial column): the declared 512/4096-orbit"
            " derivation window is not load-bearing for it",
            "write-once on the wires is enforced by the allocation policy"
            " (a strictly increasing ordinal per lane per bank indexes a"
            " fresh slot), so zero violations is a property of the code,"
            " not a discovered property of the dynamics; under a"
            " one-slot-per-bank-per-lane policy the same run produces"
            f" {a['collisions_if_one_slot_per_bank_per_lane']} rewrites",
            "record EXISTENCE readback is saturated: every one of the"
            f" {b['census_lanes']} census lanes carries a first-slot bit,"
            f" so the wire-level readback does not discriminate the"
            f" {b['composed_first_writes']} stamped keys",
            f"{a['writes_dropped_by_undisclosed_register_cap']} of"
            f" {a['total_register_write_events']} register write events are"
            " silently dropped by the undisclosed REGISTER_CAP=64",
            "stronger inertness than claimed does hold: slot wires meet"
            " neither the global-dirty set nor either bank block, so the"
            " writes cannot feed back into the clean-edge observable",
        ],
    }
    composed_cert["pass"] = bool(
        all(comp_agree.values())
        and composed["controls"]["composed_mismatches"] == 0
        and composed["controls"]["init_failures"] == 0
        and b["annotation_replay_mismatches"] == 0
        and a["nontarget_wire_drift"] == 0
        and a["residual_dead_drift_end_of_run"] == 0
        and a["slots_in_global_dirty"] == 0 and a["slots_in_bank_blocks"] == 0)

    probe = gentler_probe(ctx)
    lab = probe["labelling_audit"]
    prim = probe["primary_class_reproduced"]
    reproduced = (
        prim["sampled"] == CLAIM_867_V2_SUPERSEDED["locality_lanes"]
        and prim["near_fired"] == CLAIM_867_V2_SUPERSEDED["near_fired"]
        and prim["far_fired"] == CLAIM_867_V2_SUPERSEDED["far_fired"]
    )
    primary_text = (ROOT / AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8")
    v2_bug_absent_in_v3 = (
        "true_step_chunks" in primary_text
        and "bank_wire_rows" in primary_text
        and "len(word) // stations" not in primary_text
        and "len(columns) // 2][:4]" not in primary_text
    )
    cells_match = all(
        (cell["probes"], cell["fired"], cell["content_equal"])
        == tuple(CLAIM_867["per_class"][cls][side])
        for cls, sides in probe["corrected_classes"].items()
        if cls in CLAIM_867["per_class"]
        for side, cell in sides.items()
    ) and set(probe["corrected_classes"]) >= set(CLAIM_867["per_class"])

    def rates(cls, side):
        cell = probe["corrected_classes"][cls][side]
        if not cell["probes"]:
            return None
        return (round(cell["fired"] / cell["probes"], 4),
                round(cell["content_equal"] / cell["probes"], 4))

    rate_table = {c: {s: rates(c, s) for s in ("near", "far")}
                  for c in probe["corrected_classes"]}
    contrast = any(
        rate_table[c]["near"] is not None and rate_table[c]["far"] is not None
        and rate_table[c]["near"] != rate_table[c]["far"]
        for c in rate_table)
    fired_any = sum(probe["corrected_classes"][c][s]["fired"]
                    for c in probe["corrected_classes"]
                    for s in ("near", "far"))
    one_flip_fired = sum(probe["corrected_classes"]["one_flip"][s]["fired"]
                         for s in ("near", "far"))
    one_flip_probes = sum(probe["corrected_classes"]["one_flip"][s]["probes"]
                          for s in ("near", "far"))
    probe_cert = {
        "verdict": ("PRIMARY_READING_CORROBORATED"
                    if cells_match and v2_bug_absent_in_v3
                    else "PRIMARY_CELLS_NOT_REPRODUCED"),
        "detail": probe,
        "corrected_rates_fired_contentequal": rate_table,
        "near_far_contrast_found": contrast,
        "corrected_one_flip_fired": f"{one_flip_fired}/{one_flip_probes}",
        "total_fired_all_classes": fired_any,
        "v3_cells_match_checker_cells": cells_match,
        "v2_defects_absent_in_v3_source": v2_bug_absent_in_v3,
        "v2_regression_record": {
            "superseded_claim": CLAIM_867_V2_SUPERSEDED,
            "reproduced_by_reimplementing_v2_defects": reproduced,
            "note": (
                "this checker's first run (2026-08-03) REFUTED the v2"
                " certificate C: uniform chunk slicing was off-trajectory"
                " and the positional near/far split left the far arm"
                " empty; the v3 primary repaired both in-block and this"
                " arm re-implements the v2 defects to keep the refutation"
                " reproducible"
            ),
        },
        "findings": [
            "the v2 locality walk sliced the synchronous word into"
            " stations equal-length chunks, but the per-step gate counts"
            f" are NOT uniform for"
            f" {probe['chunking_bug']['candidate_keys_with_nonuniform_true_chunks']}"
            f" of {probe['candidates']} sampled keys; only"
            f" {probe['chunking_bug']['primary_reconstruction_clean_lanes']}"
            " lanes reproduced a clean formation edge, against"
            f" {probe['chunking_bug']['corrected_reconstruction_clean_lanes']}"
            " with correct variable-length chunking — REPAIRED in v3",
            "the v2 near/far split was positional"
            f" (index < {lab['state_width_half']}), not a bank-membership"
            " test; bank 1's whole block lies at indices"
            f" {lab['bank1_block_range']}, so the v2 'bank 1' payload list"
            f" was {lab['primary_bank_payload_1']} and one comparison arm"
            " ran ZERO perturbations — REPAIRED in v3 by kernel pack-state"
            " bank membership",
            "with correct chunking and correct bank labelling the one-flip"
            f" class fires {one_flip_fired}/{one_flip_probes}: formation"
            " firing is NOT globally hypersensitive at that class; content"
            " equality fails everywhere except flip-and-restore, and"
            " flip-and-restore shows a near/far rate contrast"
            " (path-dependence in the far arm) — the v3 primary reports"
            " exactly these cells and this checker corroborates them"
            " cell-for-cell",
        ],
    }
    probe_cert["pass"] = bool(cells_match and v2_bug_absent_in_v3)

    audit = scope_audit()
    undisclosed = {p: v["undisclosed_caps"] for p, v in audit.items()}
    scope_cert = {
        "verdict": "REFUTED" if any(undisclosed.values()) else "CONFIRMED",
        "detail": audit,
        "undisclosed_caps": undisclosed,
        "findings": [
            "v2 HISTORY (repaired in-block): REGISTER_CAP=64 appeared in no"
            " docstring and no emitted payload while silently dropping the"
            " majority of write events, and the v2 probe flipped exactly"
            " one payload wire per side (wire_list[:1]) undisclosed; the v3"
            " primary discloses the register cap, the beyond-cap event"
            " count, wires_per_side, and the class list in its emitted"
            " certificates — this audit re-checks that disclosure on the"
            " pinned v3 source",
            "866 computes distinct_pair_cadence_signatures from"
            " most_common(3) truncated gap histograms; the granularity is"
            " undisclosed (it is conservative: full histograms give the"
            " same or more distinctness, reported in the scaled leg)",
        ],
    }
    scope_cert["pass"] = not any(undisclosed.values())

    determinism = determinism_control()
    runtime = round(monotonic() - started, 3)
    controls_cert = {
        "source_controls": controls,
        "determinism": determinism,
        "runtime_seconds": runtime,
        "runtime_under_budget": runtime < AUDIT_TIMEOUT_SEC,
    }
    controls_cert["pass"] = bool(
        controls["pass"] and determinism["repeat_digests_equal"]
        and runtime < AUDIT_TIMEOUT_SEC)

    checks = {
        "THE_SCALED_REPLAY": scaled_cert["pass"],
        "THE_COMPOSED_REPLAY": composed_cert["pass"],
        "THE_GENTLER_PROBE": probe_cert["pass"],
        "THE_SCOPE_AUDIT": scope_cert["pass"],
        "CONTROLS": controls_cert["pass"],
    }
    lines = ["CYCLE866_867_FINALE_INDEPENDENT_CHECK",
             "INDEPENDENT_ADVERSARIAL_CHECKER_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("THE_SCALED_REPLAY", scaled_cert),
                          ("THE_COMPOSED_REPLAY", composed_cert),
                          ("THE_GENTLER_PROBE", probe_cert),
                          ("THE_SCOPE_AUDIT", scope_cert),
                          ("CONTROLS", controls_cert)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    refutations = []
    if not scaled_cert["pass"]:
        refutations.append("866 declared-probe numbers not reproduced")
    if not composed_cert["pass"]:
        refutations.append("867 headline numbers not reproduced")
    if not probe_cert["pass"]:
        refutations.append(
            "867 certificate C: the v3 per-class cells do not match this"
            " checker's independent recomputation, or a v2 defect pattern"
            " is still present in the v3 source")
    if not scope_cert["pass"]:
        refutations.append(
            "declared-probe disclosure incomplete: "
            + compact(scope_cert["undisclosed_caps"]))
    summary = {"checks": checks, "cycles": [866, 867],
               "refutations": refutations,
               "numbers_reproduced": {
                   "866": scaled_pass,
                   "867_headline": all(comp_agree.values()),
                   "867_v3_locality_cells": cells_match,
                   "867_v2_regression_reproduced": reproduced},
               "runtime_seconds": runtime, "pass": all(checks.values())}
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE866_867_FINALE_INDEPENDENT_CHECK_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
