#!/usr/bin/env python3
"""Cycle 874 copy-redundancy: INDEPENDENT ADVERSARIAL CHECKER.

Isolated re-implementation, spec'd to REFUTE.  The 874 primary, the 867
primary it extends, the 863 replay substrate and the 866-867 finale
checker are all BLOCKLISTED at import: they are read as text/AST only.
Every number below is re-derived here from the pinned Cycle-719 kernel
alone, with this checker's own census, own dirty partition, own dead-wire
derivation, own slot allocation (a DIFFERENT tag ordering, so agreement
cannot come from sharing an allocation), own composed scan, own content
model and own perturbation probe.

Attacks:
  THE_REDUNDANT_REGISTER -- own R-fold register: pool, disjointness,
      structural inertness for every copy, composed-scan write counts,
      readback and the per-R agreement census.  Verifies the primary's
      declared numbers and, independently, that a DIFFERENT choice of
      safe slot wires yields the SAME content words (the primary's
      payload-projection claim).
  THE_CONTENT_PROBE -- own four declared perturbation classes near/far,
      own per-R per-mode cells, own R-dependence verdict and own
      decomposition of the restore-class near/far contrast into a firing
      gap and a content gap.
  THE_HARDER_REDUNDANCY -- the refutation attempt.  Two redundancy
      schemes STRONGER than the primary's are built and measured: a
      DEEP-STAGGERED scheme (copies at clean edges 1, 1+stride,
      1+2*stride, a wider temporal spread than the primary's consecutive
      edges) and a PROJECTION-SHARDED scheme (copy c digests a different
      block of the live state).  If deep staggering buys an R-gain the
      primary missed, the primary's null is REFUTED.  The sharded scheme
      is not copy-identical, so a positive there is reported as an
      adjacent finding, not a refutation.
  THE_SCOPE_AUDIT -- AST over the primary: every declared cap constant
      must be referenced inside an emitted certificate payload, and the
      certificate pass-gates must not reference the outcome objects.
  CONTROLS -- shas, blocklist, determinism, paths, runtime, stdout.

Declared probe of this checker (complete): B=2, k=2..5 census (748
lanes), horizon 16,384 orbits, dead-wire window 512 orbits chunk-granular
then 4,096 orbit-granular, existence register cap 64 per (tag, lane),
content word 32 bits, R in {1,2,3}, consecutive-edge stagger walk cap 64
boundaries, deep-stagger stride 4 with walk cap 512 boundaries, locality
sample 32 lanes with first-clean boundary <= 1,100, 4 payload wires per
side.  bounded_theorem, authority none, audit unset.
"""
from __future__ import annotations

import ast
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
    "scripts/frontier_cycle867_composed_record_write_2026_07_28.py",
    "scripts/frontier_cycle866_867_finale_independent_check_2026_07_28.py",
    "scripts/frontier_cycle874_copy_redundancy_content_2026_07_28.py",
)
KERNEL_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_PATH = AUDIT_INPUT_PATHS[4]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "49605f6d0730e224d6c4cd25a182ec49e0c7d2f2316851bc2755632dcbe2c828",
    AUDIT_INPUT_PATHS[3]:
        "265498fc24a0b71d56e5de6ef1ebc4113510963407e0247fa80940c935e277ba",
    AUDIT_INPUT_PATHS[4]:
        "02ffdec2e7e2c18b86900a428fd4360ccd54dc62d35e1ef5f72f89a6545439d3",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
    AUDIT_INPUT_PATHS[3]: "4b6f18b00b087787c9f253d0c9b23a9ec74f9cb1",
    AUDIT_INPUT_PATHS[4]: "7f4c00a5ef5d47db8a0061a34975ff1ce78294fc",
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
BANKS = 2
KMIN, KMAX = 2, 5
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
CONTENT_BITS = 32
R_VALUES = (1, 2, 3)
R_MAX = 3
MODES = ("replicated", "staggered")
STAGGER_WALK_CAP = 64
DEEP_STAGGER_STRIDE = 4
DEEP_STAGGER_WALK_CAP = 512
LOC_LANE_CAP = 32
LOC_BOUNDARY_CAP = 1_100
PAYLOAD_WIRES_PER_SIDE = 4
CLASSES = ("one_flip", "late_acting", "untouched_in_chunk",
           "flip_and_restore")
DEAD_ZERO_SAMPLE = 64

# ---- the primary's declared numbers, reproduced or refuted here --------
# (probes, fired, majority_equal) per class and side, identical at every R
# in the primary's emitted tally -- that constancy IS the primary's claim.
_REP_CELLS = {
    "one_flip": {"near": (32, 32, 0), "far": (32, 32, 0)},
    "late_acting": {"near": (13, 13, 0), "far": (25, 25, 0)},
    "untouched_in_chunk": {"near": (19, 19, 0), "far": (15, 15, 0)},
    "flip_and_restore": {"near": (32, 32, 32), "far": (32, 29, 29)},
}
_STAG_CELLS = {
    "one_flip": {"near": (28, 28, 0), "far": (28, 28, 0)},
    "late_acting": {"near": (10, 10, 0), "far": (22, 22, 0)},
    "untouched_in_chunk": {"near": (18, 18, 0), "far": (11, 11, 0)},
    "flip_and_restore": {"near": (28, 28, 28), "far": (28, 25, 25)},
}
CLAIM_874 = {
    "dead_wire_count": 5_668,
    "safe_slot_pool": 5_270,
    "slot_tags": 321,
    "pairwise_copy_overlaps": 0,
    "content_existence_overlap": 0,
    "slots_in_gate_inputs": 0,
    "slots_in_gate_targets": 0,
    "dead_activation_conflicts": 0,
    "existence_write_once_violations": 0,
    "content_write_once_violations": 0,
    "composed_first_writes": 164,
    "lanes_with_first_slot_bit": 748,
    "content_lanes_replicated": 164,
    "content_lanes_staggered_all_copies": 157,
    "agreement_replicated_R3": 164,
    "agreement_staggered_R3": 115,
    "locality_lanes": 32,
    "per_r_cells": {
        "replicated": {str(r): _REP_CELLS for r in R_VALUES},
        "staggered": {str(r): _STAG_CELLS for r in R_VALUES},
    },
    "r_dependence_any_change": {"replicated": False, "staggered": False},
    "r_dependence_any_gain": {"replicated": False, "staggered": False},
    "restore_contrast_by_r": {
        "replicated": {"1": 0.09375, "2": 0.09375, "3": 0.09375},
        "staggered": {"1": 0.107143, "2": 0.107143, "3": 0.107143},
    },
}
DECLARED_CAPS = (
    "HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
    "CONTENT_BITS", "R_VALUES", "R_MAX", "REDUNDANCY_MODES",
    "STAGGER_WALK_CAP", "LOCALITY_SAMPLE", "LOCALITY_BOUNDARY_CAP",
    "PAYLOAD_WIRES_PER_SIDE", "PERTURBATION_CLASSES", "AUDIT_TIMEOUT_SEC",
)
GATE_MUST_NOT_REFERENCE = (
    "r_dependence", "computed", "contrast_by_r", "verdict_bits",
    "contrast_decomposition", "LANDED_867",
)


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v) -> str:
    return sha256(compact(v).encode("utf-8")).hexdigest()


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
    """Row index sets: watched-per-bank, FULL per-bank block, links, src."""
    banks, links = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks)
    zl = tuple(tuple(0 for _ in link) for link in links)
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


def build_census(program):
    stations = len(program)
    return tuple(sorted(
        (k, event, pos)
        for k in range(KMIN, KMAX + 1)
        for pos in combinations(range(stations), k)
        if separated(pos, stations)
        for event in range(2 * BANKS)
    ))


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


def lane_state(columns, lane):
    bit = 1 << lane
    return tuple(int(bool(col & bit)) for col in columns)


def true_chunks(program, positions):
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


def bank_row_sets(bank_count):
    return partition(bank_count)["full_bank"]


def word_of(payload_bytes) -> int:
    return int.from_bytes(
        sha256(payload_bytes).digest()[:(CONTENT_BITS + 7) // 8], "big"
    ) & ((1 << CONTENT_BITS) - 1)


def majority(words, r) -> int:
    out = 0
    for j in range(CONTENT_BITS):
        if sum((words[c] >> j) & 1 for c in range(r)) * 2 > r:
            out |= 1 << j
    return out


# ---- ATTACK 1: THE_REDUNDANT_REGISTER ----------------------------------
def attack_register(ctx):
    program = ctx["program"]
    census = ctx["census"]
    n = len(census)
    sim = census + (census[0],)
    columns = pack_columns(ctx["states"] + (ctx["states"][0],))
    fast = ctx["fast"]
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1

    # own dead-wire derivation
    acc = [0] * len(columns)
    work = list(columns)
    for w, c in enumerate(work):
        acc[w] |= c
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    dead = tuple(w for w in range(len(acc)) if (acc[w] & uni_sim) == 0)
    dead_set = set(dead)

    inputs: set = set()
    targets: set = set()
    for sched in ctx["raw_schedules"]:
        for kind, a, b, c3, _m in sched:
            if kind == 0:
                targets.add(a)
            elif kind == 1:
                inputs.add(a)
                targets.add(b)
            else:
                inputs.update((a, b))
                targets.add(c3)
    safe = tuple(w for w in dead if w not in inputs and w not in targets)

    # DELIBERATELY DIFFERENT allocation order from the primary: content
    # groups first, existence last, and the pool walked from the far end.
    content_tags = [(mode, copy, bit) for mode in MODES
                    for copy in range(R_MAX) for bit in range(CONTENT_BITS)]
    exist_tags = [("G", 0)] + [(f"B{b}", k) for b in (0, 1)
                               for k in range(REGISTER_CAP)]
    total = len(content_tags) + len(exist_tags)
    if len(safe) < total:
        raise AssertionError(("insufficient safe slots", len(safe), total))
    rev = tuple(reversed(safe))
    content_slot = {t: rev[i] for i, t in enumerate(content_tags)}
    exist_slot = {t: rev[len(content_tags) + i]
                  for i, t in enumerate(exist_tags)}
    slot_wires = set(content_slot.values()) | set(exist_slot.values())
    groups = {
        (mode, copy): frozenset(content_slot[(mode, copy, b)]
                                for b in range(CONTENT_BITS))
        for mode in MODES for copy in range(R_MAX)
    }
    gkeys = sorted(groups)
    overlaps = sum(len(groups[a] & groups[b])
                   for i, a in enumerate(gkeys) for b in gkeys[i + 1:])

    def content_word(state):
        payload = bytearray(state)
        for w in slot_wires:
            payload[w] = 0
        return word_of(bytes(payload))

    per_bank = ctx["per_bank"]
    global_dirty = ctx["global_dirty"]
    bank_dirty = ctx["bank_dirty"]

    host: dict = {}
    written = {key: 0 for key in groups}
    exist_writes = 0
    content_writes = 0
    exist_violations = 0
    content_violations = 0
    conflicts = 0
    dead_zero_failures = 0
    dead_zero_checked = 0
    nonslot_dead = [w for w in dead if w not in slot_wires]

    def put_content(mode, copy, lane, word):
        nonlocal content_violations, content_writes
        bit = 1 << lane
        if written[(mode, copy)] & bit:
            content_violations += 1
        written[(mode, copy)] |= bit
        for j in range(CONTENT_BITS):
            if (word >> j) & 1:
                columns[content_slot[(mode, copy, j)]] |= bit
        content_writes += CONTENT_BITS
        host[(mode, copy, lane)] = word

    def put_exist(tag, lane):
        nonlocal exist_violations, exist_writes
        wire = exist_slot[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            exist_violations += 1
        columns[wire] |= bit
        exist_writes += 1

    def record_first(lane, ls):
        nonlocal dead_zero_checked, dead_zero_failures
        if dead_zero_checked < DEAD_ZERO_SAMPLE:
            dead_zero_checked += 1
            dead_zero_failures += int(any(ls[w] for w in nonslot_dead))
        word = content_word(ls)
        for copy in range(R_MAX):
            put_content("replicated", copy, lane, word)
        put_content("staggered", 0, lane, word)
        return word

    prev_bank = [clean_mask(columns, bank_dirty[b], uni_all) for b in (0, 1)]
    first_moment: dict = {}
    stag_pending = 0
    stag_count = [0] * n
    ordinal = [[0, 0] for _ in range(n)]
    g0 = clean_mask(columns, global_dirty, uni_sim)
    mism = int(bool(g0 & 1) != bool(g0 & (1 << n)))
    for lane in lanes_of(g0 & uni_all):
        first_moment[census[lane]] = 0
        put_exist(("G", 0), lane)
        record_first(lane, lane_state(columns, lane))
        stag_count[lane] = 1
        stag_pending |= 1 << lane

    boundary = 0
    for orbit in range(1, HORIZON + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, uni_sim)
            mism += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            todo = ga & stag_pending
            if todo:
                for lane in lanes_of(todo):
                    copy = stag_count[lane]
                    put_content("staggered", copy, lane,
                                content_word(lane_state(columns, lane)))
                    stag_count[lane] = copy + 1
                    if copy + 1 >= R_MAX:
                        stag_pending &= ~(1 << lane)
            for lane in lanes_of(ga):
                if census[lane] not in first_moment:
                    first_moment[census[lane]] = boundary
                    record_first(lane, lane_state(columns, lane))
                    stag_count[lane] = 1
                    stag_pending |= 1 << lane
            for b in (0, 1):
                bm = clean_mask(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in lanes_of(edge):
                    o = ordinal[lane][b]
                    if o < REGISTER_CAP:
                        put_exist((f"B{b}", o), lane)
                    ordinal[lane][b] = o + 1
                prev_bank[b] = bm
            for w in nonslot_dead:
                if columns[w] & uni_sim:
                    conflicts += 1
                    break

    def readback(mode, copy, lane):
        bit = 1 << lane
        return sum(
            ((columns[content_slot[(mode, copy, j)]] & bit) != 0) << j
            for j in range(CONTENT_BITS)
        )

    readback_mismatch = sum(
        int(readback(m, c, l) != w) for (m, c, l), w in host.items()
    )
    agreement = {}
    lanes_all = {}
    for mode in MODES:
        complete = [
            lane for lane in lanes_of(written[(mode, 0)])
            if all((written[(mode, c)] >> lane) & 1 for c in range(R_MAX))
        ]
        lanes_all[mode] = len(complete)
        agreement[mode] = {
            str(r): sum(
                int(len({readback(mode, c, lane) for c in range(r)}) == 1)
                for lane in complete
            )
            for r in R_VALUES
        }
    exist_lane_count = len(
        set(lanes_of(columns[exist_slot[("G", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B0", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B1", 0)]] & uni_all))
    )
    ctx["dead"] = dead
    ctx["dead_set"] = dead_set
    ctx["safe"] = safe
    ctx["checker_slot_wires"] = slot_wires
    ctx["checker_content_word"] = content_word
    ctx["scan_words"] = {
        lane: host[("replicated", 0, lane)]
        for lane in lanes_of(written[("replicated", 0)])
    }
    ctx["first_moment"] = first_moment
    ctx["duplicate_mismatches"] = mism

    observed = {
        "dead_wire_count": len(dead),
        "safe_slot_pool": len(safe),
        "slot_tags": total,
        "pairwise_copy_overlaps": overlaps,
        "content_existence_overlap": len(
            frozenset().union(*groups.values()) & frozenset(exist_slot.values())
        ),
        "slots_in_gate_inputs": len(slot_wires & inputs),
        "slots_in_gate_targets": len(slot_wires & targets),
        "dead_activation_conflicts": conflicts,
        "existence_write_once_violations": exist_violations,
        "content_write_once_violations": content_violations,
        "composed_first_writes": len(first_moment),
        "lanes_with_first_slot_bit": exist_lane_count,
        "content_lanes_replicated": lanes_all["replicated"],
        "content_lanes_staggered_all_copies": lanes_all["staggered"],
        "agreement_replicated_R3": agreement["replicated"]["3"],
        "agreement_staggered_R3": agreement["staggered"]["3"],
    }
    refutations = [
        f"register.{k}: primary={CLAIM_874[k]} checker={v}"
        for k, v in observed.items()
        if k in CLAIM_874 and CLAIM_874[k] != "__FILL__"
        and CLAIM_874[k] != v
    ]
    result = {
        "attack": "THE_REDUNDANT_REGISTER",
        "own_allocation": (
            "content groups first, existence last, pool walked from the far"
            " end -- a different slot assignment from the primary's"
        ),
        "observed": observed,
        "agreement_census": agreement,
        "readback_host_mismatches": readback_mismatch,
        "content_bit_write_events": content_writes,
        "wire_visible_existence_writes": exist_writes,
        "dead_wires_zero_at_write_time": {
            "checked": dead_zero_checked, "failures": dead_zero_failures,
            "statement": (
                "confirms the primary's payload-projection claim: at write"
                " time every non-slot dead wire is zero, so zeroing the"
                " slots makes the content word independent of WHICH safe"
                " wires a run allocates"
            ),
        },
        "refutations": refutations,
    }
    result["pass"] = (
        readback_mismatch == 0 and dead_zero_failures == 0
        and not refutations and overlaps == 0
        and len(slot_wires & inputs) == 0 and len(slot_wires & targets) == 0
    )
    return result


# ---- ATTACK 2: THE_CONTENT_PROBE ---------------------------------------
def probe_common(ctx):
    """Shared walk machinery for attacks 2 and 3."""
    program = ctx["program"]
    census = ctx["census"]
    stations = len(program)
    global_dirty = ctx["global_dirty"]
    bank_dirty = ctx["bank_dirty"]
    dead_set = ctx["dead_set"]
    content_word = ctx["checker_content_word"]
    payload_pool = [
        w for w in range(ctx["width"])
        if w not in dead_set and w not in set(global_dirty)
    ]
    rows = bank_row_sets(BANKS)
    bank_payload = {
        b: [w for w in payload_pool if w in rows[b]][:PAYLOAD_WIRES_PER_SIDE]
        for b in (0, 1)
    }
    if not bank_payload[0] or not bank_payload[1]:
        raise AssertionError("empty bank payload pool")
    cache: dict = {}

    def chunks_for(pos):
        if pos not in cache:
            cache[pos] = true_chunks(program, pos)
        return cache[pos]

    def clean(state):
        return all(state[w] == 0 for w in global_dirty)

    def edge_words(state, chunks_t, at_boundary, indices, cap):
        """Words at the clean edges whose 0-based ordinals are `indices`,
        walking at most `cap` boundaries from a state already clean."""
        want = max(indices)
        seen = [content_word(state)]
        cur, b, steps = state, at_boundary, 0
        while len(seen) <= want and steps < cap:
            cur = K.A.apply_semantic(cur, chunks_t[b % stations])
            b += 1
            steps += 1
            if clean(cur):
                seen.append(content_word(cur))
        if len(seen) <= want:
            return None
        return [seen[i] for i in indices]

    ctx.update({
        "stations": stations, "bank_payload": bank_payload,
        "chunks_for": chunks_for, "clean": clean, "edge_words": edge_words,
        "payload_pool": payload_pool,
    })
    return ctx


def walk_probes(ctx, schemes):
    """One pass over the declared sample; every scheme in `schemes` gets
    its base and perturbed word vectors from the SAME walks.

    A scheme is (name, kind, params): kind 'replicated' | 'edges' |
    'projection'.
    """
    program, census = ctx["program"], ctx["census"]
    stations = ctx["stations"]
    seeds = ctx["seeds"]
    bank_dirty = ctx["bank_dirty"]
    bank_payload = ctx["bank_payload"]
    chunks_for, clean, edge_words = (
        ctx["chunks_for"], ctx["clean"], ctx["edge_words"]
    )
    content_word = ctx["checker_content_word"]
    part = ctx["partition"]
    shard_rows = (
        sorted(part["full_bank"][0]), sorted(part["full_bank"][1]),
        sorted(set(part["links"]) | {part["source"]}),
    )

    def project(state, rows):
        return word_of(bytes(bytearray(state[w] for w in rows)))

    def vector(state, chunks_t, at_boundary, kind, params):
        if kind == "replicated":
            return [content_word(state)] * R_MAX
        if kind == "edges":
            indices, cap = params
            return edge_words(state, chunks_t, at_boundary, indices, cap)
        return [project(state, shard_rows[c]) for c in range(R_MAX)]

    tally = {
        name: {str(r): {cls: {side: {
            "probes": 0, "fired": 0, "copy_survivals": 0,
            "all_copies_equal": 0, "any_copy_equal": 0, "majority_equal": 0}
            for side in ("near", "far")} for cls in CLASSES}
            for r in R_VALUES}
        for name, _k, _p in schemes
    }
    full_tally = {cls: {side: {"probes": 0, "fired": 0, "content_equal": 0}
                        for side in ("near", "far")} for cls in CLASSES}
    stats = {"sampled": 0, "base_not_clean": 0, "restore_skips": 0,
             "base_incomplete": {name: 0 for name, _k, _p in schemes},
             "probe_incomplete": {name: 0 for name, _k, _p in schemes},
             "scan_agree": 0, "scan_checked": 0}
    candidates = ctx["candidates"]
    for first, lane in candidates:
        key = census[lane]
        chunks_t = chunks_for(key[2])
        state, _a, _b, _t = K.run_orbit(seeds[key[1]], program,
                                        token_positions=key[2])
        for b in range(first - 1):
            state = K.A.apply_semantic(state, chunks_t[b % stations])
        pre = state
        last_chunk = chunks_t[(first - 1) % stations]
        base_after = K.A.apply_semantic(pre, last_chunk)
        if not clean(base_after):
            stats["base_not_clean"] += 1
            continue
        stats["sampled"] += 1
        base_full = sha256(bytes(base_after)).hexdigest()
        base_vec = {}
        for name, kind, params in schemes:
            v = vector(base_after, chunks_t, first, kind, params)
            base_vec[name] = v
            if v is None:
                stats["base_incomplete"][name] += 1
        if lane in ctx["scan_words"]:
            stats["scan_checked"] += 1
            stats["scan_agree"] += int(
                ctx["scan_words"][lane] == content_word(base_after)
            )
        rec_bank = 0 if all(base_after[w] == 0 for w in bank_dirty[0]) else 1
        first_touch: dict = {}
        for idx, gate in enumerate(last_chunk):
            for w in gate.wires:
                first_touch.setdefault(w, idx)
        for side, bank in (("near", rec_bank), ("far", 1 - rec_bank)):
            pool = bank_payload[bank]
            picks = {"one_flip": pool[0], "flip_and_restore": pool[0]}
            touched = [w for w in pool if w in first_touch]
            picks["late_acting"] = (
                max(touched, key=lambda w: first_touch[w]) if touched else None
            )
            untouched = [w for w in pool if w not in first_touch]
            picks["untouched_in_chunk"] = untouched[0] if untouched else None
            for cls, wire in picks.items():
                if wire is None:
                    continue
                if cls == "flip_and_restore":
                    if first - 1 == 0:
                        stats["restore_skips"] += 1
                        continue
                    ws, _x, _y, _z = K.run_orbit(seeds[key[1]], program,
                                                 token_positions=key[2])
                    fl = list(ws)
                    fl[wire] ^= 1
                    ws = tuple(fl)
                    for b in range(first - 1):
                        ws = K.A.apply_semantic(ws, chunks_t[b % stations])
                    rs = list(ws)
                    rs[wire] ^= 1
                    after = K.A.apply_semantic(tuple(rs), last_chunk)
                else:
                    mut = list(pre)
                    mut[wire] ^= 1
                    after = K.A.apply_semantic(tuple(mut), last_chunk)
                fired = clean(after)
                ft = full_tally[cls][side]
                ft["probes"] += 1
                ft["fired"] += int(fired)
                if fired:
                    ft["content_equal"] += int(
                        sha256(bytes(after)).hexdigest() == base_full
                    )
                for name, kind, params in schemes:
                    pv = None
                    if fired:
                        pv = vector(after, chunks_t, first, kind, params)
                        if pv is None:
                            stats["probe_incomplete"][name] += 1
                    if base_vec[name] is None or (fired and pv is None):
                        continue
                    for r in R_VALUES:
                        cell = tally[name][str(r)][cls][side]
                        cell["probes"] += 1
                        cell["fired"] += int(fired)
                        if not fired:
                            continue
                        bv = base_vec[name]
                        surv = sum(int(pv[c] == bv[c]) for c in range(r))
                        cell["copy_survivals"] += surv
                        cell["all_copies_equal"] += int(surv == r)
                        cell["any_copy_equal"] += int(surv > 0)
                        cell["majority_equal"] += int(
                            majority(pv, r) == majority(bv, r)
                        )
    return tally, full_tally, stats


def rates(tally, name, r, cls, side, field):
    cell = tally[name][str(r)][cls][side]
    return round(cell[field] / cell["probes"], 6) if cell["probes"] else None


def given_fired(tally, name, r, cls, side, field):
    cell = tally[name][str(r)][cls][side]
    return round(cell[field] / cell["fired"], 6) if cell["fired"] else None


def attack_probe(ctx):
    schemes = (
        ("replicated", "replicated", None),
        ("staggered", "edges", ((0, 1, 2), STAGGER_WALK_CAP)),
    )
    tally, full_tally, stats = walk_probes(ctx, schemes)
    r_dep = {}
    for name, _k, _p in schemes:
        deltas = {}
        for cls in CLASSES:
            for side in ("near", "far"):
                a = rates(tally, name, 1, cls, side, "majority_equal")
                b = rates(tally, name, R_MAX, cls, side, "majority_equal")
                deltas[f"{cls}.{side}"] = (
                    None if a is None or b is None else round(b - a, 6)
                )
        r_dep[name] = {
            "deltas": deltas,
            "any_change": any(v not in (None, 0.0) for v in deltas.values()),
            "any_gain": any(v is not None and v > 0.0
                            for v in deltas.values()),
        }
    contrast = {
        name: {str(r): (
            None
            if rates(tally, name, r, "flip_and_restore", "near",
                     "majority_equal") is None
            or rates(tally, name, r, "flip_and_restore", "far",
                     "majority_equal") is None
            else round(
                rates(tally, name, r, "flip_and_restore", "near",
                      "majority_equal")
                - rates(tally, name, r, "flip_and_restore", "far",
                        "majority_equal"), 6)
        ) for r in R_VALUES}
        for name, _k, _p in schemes
    }
    decomposition = {
        name: {
            "firing_gap_near_minus_far": (
                None
                if rates(tally, name, 1, "flip_and_restore", "near", "fired")
                is None
                else round(
                    rates(tally, name, 1, "flip_and_restore", "near", "fired")
                    - rates(tally, name, 1, "flip_and_restore", "far",
                            "fired"), 6)
            ),
            "content_gap_given_fired_near_minus_far": (
                None
                if given_fired(tally, name, 1, "flip_and_restore", "near",
                               "majority_equal") is None
                or given_fired(tally, name, 1, "flip_and_restore", "far",
                               "majority_equal") is None
                else round(
                    given_fired(tally, name, 1, "flip_and_restore", "near",
                                "majority_equal")
                    - given_fired(tally, name, 1, "flip_and_restore", "far",
                                  "majority_equal"), 6)
            ),
        }
        for name, _k, _p in schemes
    }
    observed = {
        "locality_lanes": stats["sampled"],
        "per_r_cells": {
            name: {str(r): {cls: {
                side: (tally[name][str(r)][cls][side]["probes"],
                       tally[name][str(r)][cls][side]["fired"],
                       tally[name][str(r)][cls][side]["majority_equal"])
                for side in ("near", "far")} for cls in CLASSES}
                for r in R_VALUES}
            for name, _k, _p in schemes
        },
        "r_dependence_any_change": {
            name: r_dep[name]["any_change"] for name, _k, _p in schemes
        },
        "r_dependence_any_gain": {
            name: r_dep[name]["any_gain"] for name, _k, _p in schemes
        },
        "restore_contrast_by_r": contrast,
    }
    refutations = [
        f"probe.{k}: primary={CLAIM_874[k]} checker={v}"
        for k, v in observed.items()
        if k in CLAIM_874 and CLAIM_874[k] != "__FILL__" and CLAIM_874[k] != v
    ]
    ctx["full_tally"] = full_tally
    result = {
        "attack": "THE_CONTENT_PROBE",
        "declared_sample": {
            "lanes": stats["sampled"], "lane_cap": LOC_LANE_CAP,
            "boundary_cap": LOC_BOUNDARY_CAP,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE, "classes": CLASSES,
            "r_values": R_VALUES,
            "stagger_walk_cap": STAGGER_WALK_CAP,
            "base_not_clean_skips": stats["base_not_clean"],
            "degenerate_restore_skips": stats["restore_skips"],
            "base_incomplete": stats["base_incomplete"],
            "probe_incomplete": stats["probe_incomplete"],
        },
        "observed": observed,
        "per_r_full_cells": tally,
        "full_state_content_tally": full_tally,
        "r_dependence": r_dep,
        "restore_contrast_decomposition": decomposition,
        "scan_vs_probe_content":
            f"{stats['scan_agree']}/{stats['scan_checked']}",
        "refutations": refutations,
    }
    result["pass"] = (
        stats["sampled"] > 0 and not refutations
        and stats["scan_checked"] > 0
        and stats["scan_agree"] == stats["scan_checked"]
    )
    return result


# ---- ATTACK 3: THE_HARDER_REDUNDANCY -----------------------------------
def attack_harder(ctx):
    deep_idx = (0, DEEP_STAGGER_STRIDE, 2 * DEEP_STAGGER_STRIDE)
    schemes = (
        ("deep_staggered", "edges", (deep_idx, DEEP_STAGGER_WALK_CAP)),
        ("projection_sharded", "projection", None),
    )
    tally, _full, stats = walk_probes(ctx, schemes)
    rows = {}
    for name, _k, _p in schemes:
        deltas = {}
        any_rows = {}
        for cls in CLASSES:
            for side in ("near", "far"):
                a = rates(tally, name, 1, cls, side, "majority_equal")
                b = rates(tally, name, R_MAX, cls, side, "majority_equal")
                deltas[f"{cls}.{side}"] = (
                    None if a is None or b is None else round(b - a, 6)
                )
                any_rows[f"{cls}.{side}"] = rates(
                    tally, name, R_MAX, cls, side, "any_copy_equal"
                )
        rows[name] = {
            "majority_delta_R3_minus_R1": deltas,
            "any_gain": any(v is not None and v > 0.0
                            for v in deltas.values()),
            "any_copy_survives_at_R3": any_rows,
            "any_copy_survives_somewhere": any(
                v is not None and v > 0.0 for v in any_rows.values()
            ),
        }
    # Only the deep-staggered scheme is copy-identical redundancy, so only
    # it can refute the primary's null.  The sharded scheme stores DIFFERENT
    # content per copy: a positive there is an adjacent finding.
    refutations = []
    if rows["deep_staggered"]["any_gain"]:
        refutations.append(
            "deep-staggered copy redundancy DOES buy majority-readback"
            " survival that the primary's consecutive-edge staggering"
            " missed: " + compact(
                rows["deep_staggered"]["majority_delta_R3_minus_R1"])
        )
    result = {
        "attack": "THE_HARDER_REDUNDANCY",
        "schemes": {
            "deep_staggered": {
                "clean_edge_ordinals": deep_idx,
                "walk_cap_boundaries": DEEP_STAGGER_WALK_CAP,
                "copy_identical": True,
            },
            "projection_sharded": {
                "copy_0": "bank-0 rows", "copy_1": "bank-1 rows",
                "copy_2": "link rows + source pointer",
                "copy_identical": False,
            },
        },
        "declared_sample": {
            "lanes": stats["sampled"],
            "base_incomplete": stats["base_incomplete"],
            "probe_incomplete": stats["probe_incomplete"],
        },
        "rows": rows,
        "per_r_full_cells": tally,
        "adjacent_finding": (
            "projection sharding is NOT copy redundancy (each copy holds a"
            " different word), so a bitwise majority over its copies is"
            " meaningless and its majority_delta row must NOT be read as"
            " an R-gain; the meaningful row is any_copy_survives, which"
            " prices a DIFFERENT successor (block-local record content)"
            " rather than this cycle's claim: "
            + compact(rows["projection_sharded"]["any_copy_survives_at_R3"])
        ),
        "refutations": refutations,
    }
    result["pass"] = stats["sampled"] > 0 and not refutations
    return result


# ---- ATTACK 4: THE_SCOPE_AUDIT -----------------------------------------
def attack_scope():
    src = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=PRIMARY_PATH)
    module_consts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id.isupper():
                    try:
                        module_consts[t.id] = ast.literal_eval(node.value)
                    except (ValueError, SyntaxError):
                        module_consts[t.id] = None
    cert_names: set = set()
    gate_names: dict = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id.startswith("cert_"):
                for sub in ast.walk(node.value):
                    if isinstance(sub, ast.Name):
                        cert_names.add(sub.id)
            if (isinstance(tgt, ast.Subscript)
                    and isinstance(tgt.value, ast.Name)
                    and tgt.value.id.startswith("cert_")):
                key = getattr(getattr(tgt, "slice", None), "value", None)
                if key == "pass":
                    gate_names[tgt.value.id] = {
                        sub.id for sub in ast.walk(node.value)
                        if isinstance(sub, ast.Name)
                    }
    undisclosed = sorted(
        c for c in DECLARED_CAPS
        if c in module_consts and c not in cert_names
    )
    missing_consts = sorted(c for c in DECLARED_CAPS if c not in module_consts)
    gate_leaks = sorted(
        f"{gate}:{name}"
        for gate, names in gate_names.items()
        for name in names if name in GATE_MUST_NOT_REFERENCE
    )
    result = {
        "attack": "THE_SCOPE_AUDIT",
        "primary": PRIMARY_PATH,
        "declared_caps_checked": DECLARED_CAPS,
        "caps_missing_from_primary": missing_consts,
        "caps_not_referenced_in_any_certificate": undisclosed,
        "pass_gates_found": sorted(gate_names),
        "outcome_objects_referenced_by_pass_gates": gate_leaks,
        "statement": (
            "a cap is disclosed iff its constant is referenced inside an"
            " emitted certificate payload; a gate is clean iff it never"
            " references the objects that carry the R-dependence answer"
        ),
        "refutations": (
            [f"undisclosed caps: {undisclosed}"] if undisclosed else []
        ) + (
            [f"missing caps: {missing_consts}"] if missing_consts else []
        ) + (
            [f"pass-gate references outcome: {gate_leaks}"]
            if gate_leaks else []
        ),
    }
    result["pass"] = not result["refutations"]
    return result


def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"),
                          filename="self")
    literal = None
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)

    program = K.interleaved_program(BANKS)
    census = build_census(program)
    seeds, seed_fail = kernel_seeds(program, BANKS)
    states, init_fail = initial_states(program, seeds, census)
    sim = census + (census[0],)
    raw_schedules = masked_schedules(program, sim)
    part = partition(BANKS)
    global_dirty = tuple(sorted(
        set(part["per_bank"][0]) | set(part["per_bank"][1])
        | set(part["links"]) | {part["source"]}
    ))
    ctx = {
        "program": program, "census": census, "seeds": seeds,
        "states": states, "raw_schedules": raw_schedules,
        "fast": compile_chunks(raw_schedules), "partition": part,
        "per_bank": part["per_bank"], "global_dirty": global_dirty,
        "bank_dirty": (part["per_bank"][0], part["per_bank"][1]),
        "width": len(states[0]),
    }
    a1 = attack_register(ctx)

    # candidates: own first-clean boundaries by direct walk (no replay
    # store), independently derived from the composed scan's first moments.
    key_index = {key: lane for lane, key in enumerate(census)}
    candidates = sorted(
        (b, key_index[key]) for key, b in ctx["first_moment"].items()
        if 0 < b <= LOC_BOUNDARY_CAP
    )[:LOC_LANE_CAP]
    ctx["candidates"] = candidates
    probe_common(ctx)
    a2 = attack_probe(ctx)
    a3 = attack_harder(ctx)
    a4 = attack_scope()

    det_a = digest([sorted(r) for r in bank_row_sets(BANKS)])
    det_b = digest([sorted(r) for r in bank_row_sets(BANKS)])
    det_c = digest(build_census(K.interleaved_program(BANKS)))
    runtime = round(monotonic() - started, 3)
    controls = {
        "attack": "CONTROLS",
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "text_ast_only": TEXT_AST_ONLY_PATHS,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "seed_failures": seed_fail,
        "initial_state_failures": init_fail,
        "marker_failures": part["marker_failures"],
        "duplicate_lane_mismatches": ctx["duplicate_mismatches"],
        "census_size": len(census),
        "stations": len(program),
        "determinism": {
            "bank_rows": det_a == det_b, "census_digest": det_c,
        },
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
    }
    controls["pass"] = (
        controls["literal_ok"] and controls["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256 and blob_rows == EXPECTED_GIT_BLOBS
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
        and seed_fail == 0 and init_fail == 0
        and part["marker_failures"] == 0
        and ctx["duplicate_mismatches"] == 0
        and det_a == det_b and runtime < AUDIT_TIMEOUT_SEC
    )

    all_refutations = (
        a1["refutations"] + a2["refutations"] + a3["refutations"]
        + a4["refutations"]
    )
    checks = {
        "THE_REDUNDANT_REGISTER": a1["pass"],
        "THE_CONTENT_PROBE": a2["pass"],
        "THE_HARDER_REDUNDANCY": a3["pass"],
        "THE_SCOPE_AUDIT": a4["pass"],
        "CONTROLS": controls["pass"],
    }
    lines = ["CYCLE874_REDUNDANCY_INDEPENDENT_CHECK",
             "ISOLATED_REIMPLEMENTATION_SPECD_TO_REFUTE"]
    for name, payload in (("THE_REDUNDANT_REGISTER", a1),
                          ("THE_CONTENT_PROBE", a2),
                          ("THE_HARDER_REDUNDANCY", a3),
                          ("THE_SCOPE_AUDIT", a4),
                          ("CONTROLS", controls)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 874,
        "numbers_reproduced": {
            "register": not a1["refutations"],
            "probe": not a2["refutations"],
            "scope": not a4["refutations"],
        },
        "harder_redundancy_gain": {
            name: a3["rows"][name]["any_gain"] for name in a3["rows"]
        },
        "refutations": all_refutations,
        "runtime_seconds": round(monotonic() - started, 3),
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE874_REDUNDANCY_INDEPENDENT_CHECK_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
