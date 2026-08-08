#!/usr/bin/env python3
"""Cycle 874: R-fold replication of a stipulated whole-state fingerprint
into dead-wire slot groups -- BOUNDED SUPPORT CERTIFICATES ONLY.

Grade: bounded support (demoted on physics review, iteration 1,
2026-08-08).  This runner certifies finite computations on a model built
in this file over the landed, sha-pinned Cycle-719 kernel -- its ONLY
computed input.  It does NOT establish a copy-redundancy no-go, a
near/far locality effect, a framework-Record statement, or a
sharding-protection theorem.  Earlier wordings of those four claims are
retired.

What is stipulated in this file (model conventions, not framework
content):

  content word -- the first CONTENT_BITS bits of SHA-256 over the packed
      lane state with every register slot wire zeroed.  This is a
      model-defined state fingerprint.  Whether it corresponds to
      framework "record content" (one admissible local possibility) is
      an OPEN bridge that this package does not supply.
  decoder -- strict bitwise majority over the first r copies; an even-r
      tie resolves to 0.
  sides -- perturbation wires are drawn from two FIXED pools: bank0
      (pack-state bank-0 payload wires) and bank1 (bank-1 payload
      wires).  The sides are fixed bank labels, NOT distances from a
      record: no record-location selector is defined in this package and
      no bank-swap control was run, so no locality reading is available.

What the probes do and do not test (declared semantic scope): every
perturbation changes the SOURCE state BEFORE any copy is formed, so all
copies of a perturbed walk digest the same changed state (a common-mode
probe).  For identical replicas majority([w]*r, r) = w for every r, so
the emitted R-invariance of replicated-mode majority readback is forced
by construction; it is reported as an exact identity, not as evidence
about fault tolerance.  No stored copy slot is ever mutated, erased, or
read under a fault after writing.  Untested routes, named: post-write
faults on a proper subset of copy groups, erasure of selected copies,
channel-local noise, error-detecting/erasure codes, and any decoder
acting on a fixed message.

Certificates:

A. A_REDUNDANT_CONTENT_REGISTER: derive the structurally-dead safe pool;
   allocate the existence register plus 2 x R_MAX x CONTENT_BITS content
   slots; verify disjointness and structural inertness for all copies;
   run the composed scan with real wire-mutating writes.
B. B_CONTENT_READBACK: read every copy back out of the final state
   columns; per-R agreement census; readback-versus-host fidelity;
   content diversity.
C. C_REDUNDANCY_UNDER_PERTURBATION: the four declared perturbation
   classes (one_flip, late_acting, untouched_in_chunk, flip_and_restore)
   on the fixed bank0/bank1 wire pools; per R in {1,2,3} and per mode:
   per-copy survival, majority-readback survival, and the flip-and-
   restore firing/content decomposition between the two fixed banks.
D. D_CONTROLS: source pins (Cycle-719 kernel only), seed/initial-state
   integrity, determinism, runtime.

Declared scope: B=2 banks, k=2..5 census (748 lanes), horizon 16,384
orbits; dead-wire derivation window 512 orbits chunk-granular then 4,096
orbit-granular; existence register cap 64 wire-visible ordinals per
(tag, lane); content word 32 bits; R in {1,2,3}; staggered-copy walk cap
64 boundaries; sample 32 early-formation lanes with first-clean boundary
<= 1,100, up to 4 payload wires per side.  All caps disclosed in the
emitted certificates.  Integrity gates are bookkeeping only: the
R-dependence is reported as data whichever way it falls.

Provenance context (non-load-bearing): the design descends from the
unlanded Cycle-863/866/867 line.  Nothing from that line is read,
pinned, imported, or gated on here; every needed definition is stipulated
in this file over the landed kernel.

claim_type bounded_theorem carried as a bounded support note; authority
none; audit unset.  Independent audit still required (companion checker
spec'd to refute).
"""
from __future__ import annotations

import ast
from hashlib import sha1, sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

# ---- declared scope of this cycle (every cap is emitted below) ----------
BANKS = 2
KMIN = 2
KMAX = 5
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
CONTENT_BITS = 32
R_VALUES = (1, 2, 3)
R_MAX = 3
REDUNDANCY_MODES = ("replicated", "staggered")
STAGGER_WALK_CAP = 64
SAMPLE_LANE_CAP = 32
SAMPLE_BOUNDARY_CAP = 1_100
PAYLOAD_WIRES_PER_SIDE = 4
PERTURBATION_CLASSES = (
    "one_flip", "late_acting", "untouched_in_chunk", "flip_and_restore"
)
SIDES = ("bank0", "bank1")
DETERMINISM_LANES = 4


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v) -> str:
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(b: bytes) -> str:
    return sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"), filename="self")
    literal = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    result = {
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "statement": (
            "the only computed input is the landed Cycle-719 kernel; every"
            " other definition used by this runner is stipulated in this"
            " file"
        ),
    }
    result["pass"] = (
        result["literal_ok"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
    )
    return result


# ---- substrate, stipulated in-file over the landed kernel ---------------
def lanes_of(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def clean_mask(columns, indices, universe):
    """Lanes whose every watched-dirty wire is zero (the clean edge)."""
    dirty = 0
    for w in indices:
        dirty |= columns[w]
    return universe & ~dirty


def separated(positions, stations):
    occ = set(positions)
    return all((s + 1) % stations not in occ for s in occ)


def build_census(program):
    stations = len(program)
    return tuple(sorted(
        (k, event, pos)
        for k in range(KMIN, KMAX + 1)
        for pos in combinations(range(stations), k)
        if separated(pos, stations)
        for event in range(2 * BANKS)
    ))


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


def dirty_partition(bank_count):
    """Row index sets: watched-per-bank, links, source pointer."""
    banks, links = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks)
    zl = tuple(tuple(0 for _ in link) for link in links)
    base = K.M.pack_state(zb, zl)
    watched = set(watched_wires())
    per_bank, bad = [], 0
    for bi in range(bank_count):
        w_rows = set()
        for wire in range(len(zb[bi])):
            ch = [list(b) for b in zb]
            ch[bi][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in ch), zl)
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            bad += int(len(d) != 1)
            if wire in watched:
                w_rows.add(d[0])
        per_bank.append(tuple(sorted(w_rows)))
    link_rows = set()
    for li, link in enumerate(zl):
        for wire in range(len(link)):
            ch = [list(r) for r in zl]
            ch[li][wire] = 1
            marked = K.M.pack_state(zb, tuple(tuple(r) for r in ch))
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            bad += int(len(d) != 1)
            link_rows.add(d[0])
    return {"per_bank": tuple(per_bank), "links": tuple(sorted(link_rows)),
            "source": K.R3.X.SOURCE_POINTER, "marker_failures": bad}


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


def true_step_chunks(program, positions):
    """Per-step gate lists on the true trajectory (v3's corrected form)."""
    stations_local = len(program)
    macros = [K.mapped_macro(row) for row in program]
    chunks = []
    for step in range(stations_local):
        gates = []
        for station in range(stations_local):
            if (station - step) % stations_local in positions:
                gates.extend(macros[station])
        chunks.append(tuple(gates))
    return tuple(chunks)


def bank_wire_rows(bank_count):
    """TRUE bank membership of packed rows via single-bit pack-state
    marking (v3's corrected form)."""
    banks, links = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks)
    zl = tuple(tuple(0 for _ in link) for link in links)
    base = K.M.pack_state(zb, zl)
    rows = []
    for bi in range(bank_count):
        marked_rows = set()
        for wire in range(len(zb[bi])):
            changed = [list(b) for b in zb]
            changed[bi][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in changed), zl)
            diff = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            if len(diff) != 1:
                raise AssertionError(("bank marking not injective", bi, wire))
            marked_rows.add(diff[0])
        rows.append(frozenset(marked_rows))
    return tuple(rows)


def majority_word(words, r):
    """Bitwise majority over the first r copies.  Declared tie rule for
    even r: a tie resolves to 0 (no strict majority for a 1)."""
    out = 0
    for j in range(CONTENT_BITS):
        ones = sum((words[c] >> j) & 1 for c in range(r))
        if ones * 2 > r:
            out |= 1 << j
    return out


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program = K.interleaved_program(BANKS)
    census = build_census(program)
    stations = len(program)
    n = len(census)
    seeds, seed_fail = kernel_seeds(program, BANKS)
    states, init_fail = initial_states(program, seeds, census)
    sim = census + (census[0],)
    dup = n
    columns = pack_columns(states + (states[0],))
    raw_schedules = masked_schedules(program, sim)
    fast = compile_chunks(raw_schedules)
    part = dirty_partition(BANKS)
    per_bank = part["per_bank"]
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(part["links"])
        | {part["source"]}
    ))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1

    # --- Certificate A part 1: the dead-wire safe pool (v3 derivation) ----
    acc = [0] * len(columns)
    work = [c for c in columns]
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
    dead_wires = tuple(w for w in range(len(acc)) if (acc[w] & uni_sim) == 0)
    dead_set = set(dead_wires)

    gate_inputs: set = set()
    gate_targets: set = set()
    for schedule in raw_schedules:
        for kind, a, b, c3, _mask in schedule:
            if kind == 0:
                gate_targets.add(a)
            elif kind == 1:
                gate_inputs.add(a)
                gate_targets.add(b)
            else:
                gate_inputs.update((a, b))
                gate_targets.add(c3)
    safe_slots_pool = tuple(
        w for w in dead_wires
        if w not in gate_inputs and w not in gate_targets
    )

    # --- Certificate A part 2: R-fold disjoint slot allocation ------------
    existence_tags = [("E", "G", 0)] + [
        ("E", f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    content_tags = [
        ("C", mode, copy, bit)
        for mode in REDUNDANCY_MODES
        for copy in range(R_MAX)
        for bit in range(CONTENT_BITS)
    ]
    slot_tags = existence_tags + content_tags
    if len(safe_slots_pool) < len(slot_tags):
        raise AssertionError(("insufficient safe slots",
                              len(safe_slots_pool), len(slot_tags)))
    slot_of = {tag: safe_slots_pool[i] for i, tag in enumerate(slot_tags)}
    slot_wires = set(slot_of.values())
    exist_slot = {tag[1:]: slot_of[tag] for tag in existence_tags}
    content_slot = {tag[1:]: slot_of[tag] for tag in content_tags}
    copy_groups = {
        (mode, copy): frozenset(
            content_slot[(mode, copy, bit)] for bit in range(CONTENT_BITS)
        )
        for mode in REDUNDANCY_MODES for copy in range(R_MAX)
    }
    group_keys = sorted(copy_groups)
    pairwise_overlaps = sum(
        len(copy_groups[a] & copy_groups[b])
        for i, a in enumerate(group_keys) for b in group_keys[i + 1:]
    )
    existence_group = frozenset(exist_slot.values())
    content_all = frozenset().union(*copy_groups.values())
    disjointness = {
        "slot_tags": len(slot_tags),
        "distinct_slot_wires": len(slot_wires),
        "copy_group_size": CONTENT_BITS,
        "copy_groups": len(copy_groups),
        "pairwise_copy_overlaps": pairwise_overlaps,
        "content_existence_overlap": len(content_all & existence_group),
        "all_slots_in_safe_pool": len(slot_wires - set(safe_slots_pool)) == 0,
    }
    inertness = {
        "slots_in_gate_inputs": len(slot_wires & gate_inputs),
        "slots_in_gate_targets": len(slot_wires & gate_targets),
        "content_slots_in_gate_inputs": len(content_all & gate_inputs),
        "content_slots_in_gate_targets": len(content_all & gate_targets),
        "content_slots_all_dead": len(content_all - dead_set) == 0,
        "statement": (
            "every copy's slots are dead wires that no gate reads or"
            " writes; mutation is structurally inert for ALL copies, and"
            " the writes really mutate the state columns"
        ),
    }

    def content_word_of(state):
        """CONTENT_BITS-wide word over the LIVE payload projection: all
        register slots are zeroed first, so the word is a function of the
        active state alone (no self-reference through the register)."""
        payload = bytearray(state)
        for w in slot_wires:
            payload[w] = 0
        return int.from_bytes(
            sha256(bytes(payload)).digest()[:(CONTENT_BITS + 7) // 8], "big"
        ) & ((1 << CONTENT_BITS) - 1)

    # --- The composed scan: base dynamics + REAL existence and content ----
    columns = pack_columns(states + (states[0],))
    register_counts = [0] * n
    bank_write_ordinal = [[0, 0] for _ in range(n)]
    write_once_violations = 0
    content_write_once_violations = 0
    dead_activation_conflicts = 0
    wire_visible_writes = 0
    content_bit_writes = 0
    host_words: dict = {}
    written_lanes: dict = {key: 0 for key in copy_groups}

    def wire_write(tag, lane):
        nonlocal write_once_violations, wire_visible_writes
        wire = exist_slot[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit
        wire_visible_writes += 1

    def content_write(mode, copy, lane, word):
        nonlocal content_write_once_violations, content_bit_writes
        key = (mode, copy)
        bit = 1 << lane
        if written_lanes[key] & bit:
            content_write_once_violations += 1
        written_lanes[key] |= bit
        for j in range(CONTENT_BITS):
            if (word >> j) & 1:
                columns[content_slot[(mode, copy, j)]] |= bit
        content_bit_writes += CONTENT_BITS
        host_words[(mode, copy, lane)] = word

    prev_bank = [
        clean_mask(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    e1_first_composed: dict = {}
    stag_pending = 0
    stag_count = [0] * n
    prev_global = clean_mask(columns, global_dirty, uni_sim)
    mism = int(bool(prev_global & 1) != bool(prev_global & (1 << dup)))
    for lane in lanes_of(prev_global & uni_all):
        e1_first_composed.setdefault(census[lane], 0)
        wire_write(("G", 0), lane)
        word = content_word_of(lane_state(columns, lane))
        for copy in range(R_MAX):
            content_write("replicated", copy, lane, word)
        content_write("staggered", 0, lane, word)
        stag_count[lane] = 1
        stag_pending |= 1 << lane
        register_counts[lane] += 1

    boundary = 0
    for orbit in range(1, HORIZON + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, uni_sim)
            mism += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            todo = ga & stag_pending
            if todo:
                for lane in lanes_of(todo):
                    copy = stag_count[lane]
                    content_write(
                        "staggered", copy, lane,
                        content_word_of(lane_state(columns, lane))
                    )
                    stag_count[lane] = copy + 1
                    if copy + 1 >= R_MAX:
                        stag_pending &= ~(1 << lane)
            for lane in lanes_of(ga):
                if census[lane] not in e1_first_composed:
                    e1_first_composed[census[lane]] = boundary
                    word = content_word_of(lane_state(columns, lane))
                    for copy in range(R_MAX):
                        content_write("replicated", copy, lane, word)
                    content_write("staggered", 0, lane, word)
                    stag_count[lane] = 1
                    stag_pending |= 1 << lane
            for b in (0, 1):
                bm = clean_mask(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in lanes_of(edge):
                    ordinal = bank_write_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                    bank_write_ordinal[lane][b] = ordinal + 1
                    register_counts[lane] += 1
                prev_bank[b] = bm
            for w in dead_wires:
                if w in slot_wires:
                    continue
                if columns[w] & uni_sim:
                    dead_activation_conflicts += 1
                    break

    cert_a = {
        "certificate": "A_REDUNDANT_CONTENT_REGISTER",
        "declared_scope": {
            "banks": BANKS,
            "census_k_range": (KMIN, KMAX),
            "horizon_orbits": HORIZON,
            "dead_window_chunk_granular_orbits": DEAD_CHUNK_ORBITS,
            "dead_window_orbit_granular_orbits": DEAD_ORBIT_ORBITS,
            "existence_register_cap_per_tag_lane": REGISTER_CAP,
            "content_bits_per_copy": CONTENT_BITS,
            "r_values": R_VALUES,
            "r_max": R_MAX,
            "redundancy_modes": REDUNDANCY_MODES,
        },
        "content_word_convention": (
            "the content word is a STIPULATED model fingerprint: the first"
            " 32 bits of SHA-256 over the packed lane state with every"
            " register slot wire zeroed; no framework record-content"
            " identification is claimed (open bridge)"
        ),
        "dead_wire_count": len(dead_wires),
        "safe_slot_pool": len(safe_slots_pool),
        "disjointness": disjointness,
        "structural_inertness": inertness,
        "dead_activation_conflicts_through_horizon": dead_activation_conflicts,
        "existence_write_once_violations": write_once_violations,
        "content_write_once_violations": content_write_once_violations,
        "wire_visible_existence_writes": wire_visible_writes,
        "content_bit_write_events": content_bit_writes,
        "lanes_with_content_per_group": {
            compact(key): bin(mask).count("1")
            for key, mask in sorted(written_lanes.items())
        },
    }
    cert_a["pass"] = (
        len(dead_wires) > 0
        and disjointness["distinct_slot_wires"] == disjointness["slot_tags"]
        and disjointness["pairwise_copy_overlaps"] == 0
        and disjointness["content_existence_overlap"] == 0
        and disjointness["all_slots_in_safe_pool"]
        and inertness["slots_in_gate_inputs"] == 0
        and inertness["slots_in_gate_targets"] == 0
        and inertness["content_slots_all_dead"]
        and dead_activation_conflicts == 0
        and write_once_violations == 0
        and content_write_once_violations == 0
        and content_bit_writes > 0
    )

    # --- Certificate B: read every copy back out of the state -------------
    def readback(mode, copy, lane):
        bit = 1 << lane
        return sum(
            ((columns[content_slot[(mode, copy, j)]] & bit) != 0) << j
            for j in range(CONTENT_BITS)
        )

    content_lanes = {
        mode: sorted(lanes_of(written_lanes[(mode, 0)]))
        for mode in REDUNDANCY_MODES
    }
    readback_mismatches = 0
    for (mode, copy, lane), word in host_words.items():
        readback_mismatches += int(readback(mode, copy, lane) != word)
    agreement: dict = {}
    diversity: dict = {}
    for mode in REDUNDANCY_MODES:
        complete = [
            lane for lane in content_lanes[mode]
            if all((written_lanes[(mode, c)] >> lane) & 1
                   for c in range(R_MAX))
        ]
        rows = {}
        for r in R_VALUES:
            all_agree = 0
            for lane in complete:
                words = [readback(mode, c, lane) for c in range(r)]
                all_agree += int(len(set(words)) == 1)
            rows[str(r)] = {
                "lanes": len(complete),
                "all_copies_agree": all_agree,
                "agreement_rate": (
                    round(all_agree / len(complete), 6) if complete else None
                ),
            }
        agreement[mode] = rows
        diversity[mode] = {
            "lanes_with_copy0": len(content_lanes[mode]),
            "lanes_with_all_copies": len(complete),
            "distinct_copy0_words": len({
                readback(mode, 0, lane) for lane in content_lanes[mode]
            }),
        }

    existence_lane_count = len(
        set(lanes_of(columns[exist_slot[("G", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B0", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B1", 0)]] & uni_all))
    )
    cert_b = {
        "certificate": "B_CONTENT_READBACK",
        "readback_source": (
            "the stored content word (a stipulated model fingerprint, not"
            " established framework record content) is reconstructed"
            " bit-by-bit from the final state columns of the disjoint"
            " dead-wire slot groups; the host word log is kept only to"
            " cross-check the readback"
        ),
        "readback_host_mismatches": readback_mismatches,
        "content_words_written": len(host_words),
        "agreement_census": agreement,
        "diversity": diversity,
        "existence_leg": {
            "composed_first_writes": len(e1_first_composed),
            "lanes_with_any_first_slot_bit": existence_lane_count,
        },
        "tie_rule": (
            "majority over r copies sets a bit iff strictly more than r/2"
            " copies carry it; for even r a tie resolves to 0"
        ),
    }
    cert_b["pass"] = (
        readback_mismatches == 0
        and len(host_words) > 0
        and all(
            diversity[m]["lanes_with_all_copies"] > 0 for m in REDUNDANCY_MODES
        )
        and all(
            0 <= agreement[m][str(r)]["all_copies_agree"]
            <= agreement[m][str(r)]["lanes"]
            for m in REDUNDANCY_MODES for r in R_VALUES
        )
    )

    # --- Certificate C: redundancy under the declared perturbations -------
    payload_pool = [
        w for w in range(len(columns))
        if w not in dead_set and w not in set(global_dirty)
    ]
    bank_rows_true = bank_wire_rows(2)
    bank_payload = {
        b: [w for w in payload_pool if w in bank_rows_true[b]]
        [:PAYLOAD_WIRES_PER_SIDE]
        for b in (0, 1)
    }
    if not bank_payload[0] or not bank_payload[1]:
        raise AssertionError(("empty bank payload pool",
                              len(bank_payload[0]), len(bank_payload[1])))
    chunk_cache: dict = {}

    def step_chunks_for(positions):
        if positions not in chunk_cache:
            chunk_cache[positions] = true_step_chunks(program, positions)
        return chunk_cache[positions]

    def is_clean(state):
        return all(state[w] == 0 for w in global_dirty)

    def stagger_words(state, chunks_t, at_boundary):
        """Words at the first R_MAX global-clean edges from `at_boundary`
        (where `state` is already clean), walking at most
        STAGGER_WALK_CAP boundaries.  None if the cap is hit first."""
        words = [content_word_of(state)]
        cur, b, steps = state, at_boundary, 0
        while len(words) < R_MAX and steps < STAGGER_WALK_CAP:
            cur = K.A.apply_semantic(cur, chunks_t[b % stations])
            b += 1
            steps += 1
            if is_clean(cur):
                words.append(content_word_of(cur))
        return words if len(words) == R_MAX else None

    def new_cell():
        return {"probes": 0, "fired": 0, "copy_survivals": 0,
                "all_copies_equal": 0, "majority_equal": 0}

    tally = {
        mode: {
            str(r): {cls: {side: new_cell() for side in SIDES}
                     for cls in PERTURBATION_CLASSES}
            for r in R_VALUES
        }
        for mode in REDUNDANCY_MODES
    }
    full_state_tally = {
        cls: {side: {"probes": 0, "fired": 0, "content_equal": 0}
              for side in SIDES}
        for cls in PERTURBATION_CLASSES
    }
    sampled = 0
    base_not_clean = 0
    degenerate_restore_skips = 0
    stagger_incomplete_base = 0
    stagger_incomplete_probe = 0
    scan_probe_content_agree = 0
    scan_probe_content_checked = 0
    per_lane_determinism: list = []
    key_index = {key: lane for lane, key in enumerate(census)}
    candidates = sorted(
        (b, key_index[key]) for key, b in e1_first_composed.items()
        if 0 < b <= SAMPLE_BOUNDARY_CAP
    )[:SAMPLE_LANE_CAP]

    for first, lane in candidates:
        key = census[lane]
        chunks_t = step_chunks_for(key[2])
        state, _ra, _rb, _t = K.run_orbit(
            seeds[key[1]], program, token_positions=key[2]
        )
        for b in range(first - 1):
            state = K.A.apply_semantic(state, chunks_t[b % stations])
        pre = state
        last_chunk = chunks_t[(first - 1) % stations]
        base_after = K.A.apply_semantic(pre, last_chunk)
        if not is_clean(base_after):
            base_not_clean += 1
            continue
        sampled += 1
        base_full = sha256(bytes(base_after)).hexdigest()
        base_word = content_word_of(base_after)
        base_stag = stagger_words(base_after, chunks_t, first)
        if base_stag is None:
            stagger_incomplete_base += 1
        base_words = {
            "replicated": [base_word] * R_MAX,
            "staggered": base_stag,
        }
        # scan-versus-probe cross-check: the register's stored word for
        # this lane must equal the probe's independently walked word.
        if ("replicated", 0, lane) in host_words:
            scan_probe_content_checked += 1
            scan_probe_content_agree += int(
                readback("replicated", 0, lane) == base_word
            )
        # Sides are FIXED perturbation banks.  (An earlier revision derived
        # a "record bank" here, but its selector was tautological -- the
        # accepted-candidate cleanliness condition forces bank 0 -- so no
        # record-location labelling is available from this probe.)
        first_touch: dict = {}
        for idx, gate in enumerate(last_chunk):
            for w in gate.wires:
                first_touch.setdefault(w, idx)
        lane_cells: list = []
        for side, bank in (("bank0", 0), ("bank1", 1)):
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
                        degenerate_restore_skips += 1
                        continue
                    walk_state, _a, _b2, _t2 = K.run_orbit(
                        seeds[key[1]], program, token_positions=key[2]
                    )
                    flipped = list(walk_state)
                    flipped[wire] ^= 1
                    walk_state = tuple(flipped)
                    for b in range(first - 1):
                        walk_state = K.A.apply_semantic(
                            walk_state, chunks_t[b % stations]
                        )
                    restored = list(walk_state)
                    restored[wire] ^= 1
                    after = K.A.apply_semantic(tuple(restored), last_chunk)
                else:
                    mut = list(pre)
                    mut[wire] ^= 1
                    after = K.A.apply_semantic(tuple(mut), last_chunk)
                fired = is_clean(after)
                fs = full_state_tally[cls][side]
                fs["probes"] += 1
                fs["fired"] += int(fired)
                if fired:
                    fs["content_equal"] += int(
                        sha256(bytes(after)).hexdigest() == base_full
                    )
                probe_words = {"replicated": None, "staggered": None}
                if fired:
                    w0 = content_word_of(after)
                    probe_words["replicated"] = [w0] * R_MAX
                    stag = stagger_words(after, chunks_t, first)
                    if stag is None:
                        stagger_incomplete_probe += 1
                    probe_words["staggered"] = stag
                for mode in REDUNDANCY_MODES:
                    have = (
                        base_words[mode] is not None
                        and (not fired or probe_words[mode] is not None)
                    )
                    for r in R_VALUES:
                        cell = tally[mode][str(r)][cls][side]
                        if not have:
                            continue
                        cell["probes"] += 1
                        cell["fired"] += int(fired)
                        if not fired:
                            continue
                        bw = base_words[mode]
                        pw = probe_words[mode]
                        survivals = sum(
                            int(pw[c] == bw[c]) for c in range(r)
                        )
                        cell["copy_survivals"] += survivals
                        cell["all_copies_equal"] += int(survivals == r)
                        cell["majority_equal"] += int(
                            majority_word(pw, r) == majority_word(bw, r)
                        )
                        if len(lane_cells) < DETERMINISM_LANES * 8:
                            lane_cells.append(
                                (mode, r, cls, side, survivals,
                                 majority_word(pw, r))
                            )
        if len(per_lane_determinism) < DETERMINISM_LANES:
            per_lane_determinism.append(digest(lane_cells))

    def rate(mode, r, cls, side, field):
        cell = tally[mode][str(r)][cls][side]
        return (
            round(cell[field] / cell["probes"], 6) if cell["probes"] else None
        )

    def copy_rate(mode, r, cls, side):
        cell = tally[mode][str(r)][cls][side]
        denom = cell["fired"] * r
        return round(cell["copy_survivals"] / denom, 6) if denom else None

    def given_fired(mode, r, cls, side, field):
        cell = tally[mode][str(r)][cls][side]
        return (
            round(cell[field] / cell["fired"], 6) if cell["fired"] else None
        )

    computed = {}
    for mode in REDUNDANCY_MODES:
        rows = {}
        for r in R_VALUES:
            rows[str(r)] = {
                "per_copy_survival": {
                    f"{cls}.{side}": copy_rate(mode, r, cls, side)
                    for cls in PERTURBATION_CLASSES for side in SIDES
                },
                "majority_readback_survival": {
                    f"{cls}.{side}": rate(mode, r, cls, side, "majority_equal")
                    for cls in PERTURBATION_CLASSES for side in SIDES
                },
                "majority_survival_given_fired": {
                    f"{cls}.{side}":
                        given_fired(mode, r, cls, side, "majority_equal")
                    for cls in PERTURBATION_CLASSES for side in SIDES
                },
                "firing_rate": {
                    f"{cls}.{side}": rate(mode, r, cls, side, "fired")
                    for cls in PERTURBATION_CLASSES for side in SIDES
                },
                "restore_bank0_minus_bank1": (
                    None
                    if rate(mode, r, "flip_and_restore", "bank0",
                            "majority_equal") is None
                    or rate(mode, r, "flip_and_restore", "bank1",
                            "majority_equal") is None
                    else round(
                        rate(mode, r, "flip_and_restore", "bank0",
                             "majority_equal")
                        - rate(mode, r, "flip_and_restore", "bank1",
                               "majority_equal"), 6
                    )
                ),
            }
        computed[mode] = rows

    # The R-dependence, computed: does raising R change ANY majority cell?
    r_dependence = {}
    for mode in REDUNDANCY_MODES:
        deltas = {}
        for cls in PERTURBATION_CLASSES:
            for side in SIDES:
                a = rate(mode, 1, cls, side, "majority_equal")
                b = rate(mode, R_MAX, cls, side, "majority_equal")
                deltas[f"{cls}.{side}"] = (
                    None if a is None or b is None else round(b - a, 6)
                )
        nonzero = sorted(k for k, v in deltas.items() if v not in (None, 0.0))
        gains = sorted(k for k, v in deltas.items()
                       if v is not None and v > 0.0)
        r_dependence[mode] = {
            "majority_delta_R3_minus_R1": deltas,
            "cells_changed_by_redundancy": nonzero,
            "cells_improved_by_redundancy": gains,
            "any_change": bool(nonzero),
            "any_gain": bool(gains),
        }
    contrast_by_r = {
        mode: {str(r): computed[mode][str(r)]["restore_bank0_minus_bank1"]
               for r in R_VALUES}
        for mode in REDUNDANCY_MODES
    }
    # Decompose the restore-class fixed-bank gap: is it a FIRING
    # difference or a CONTENT difference?  Computed, not asserted; this
    # is bank-0-versus-bank-1 arithmetic on the declared sample, not a
    # near/far locality statement.
    contrast_decomposition = {}
    for mode in REDUNDANCY_MODES:
        rows = {}
        for r in R_VALUES:
            fire = {
                side: rate(mode, r, "flip_and_restore", side, "fired")
                for side in SIDES
            }
            cond = {
                side: given_fired(mode, r, "flip_and_restore", side,
                                  "majority_equal")
                for side in SIDES
            }
            rows[str(r)] = {
                "firing_rate": fire,
                "majority_survival_given_fired": cond,
                "firing_gap_bank0_minus_bank1": (
                    None if fire["bank0"] is None or fire["bank1"] is None
                    else round(fire["bank0"] - fire["bank1"], 6)
                ),
                "content_gap_given_fired_bank0_minus_bank1": (
                    None if cond["bank0"] is None or cond["bank1"] is None
                    else round(cond["bank0"] - cond["bank1"], 6)
                ),
            }
        contrast_decomposition[mode] = rows

    verdict_bits = []
    for mode in REDUNDANCY_MODES:
        dep = r_dependence[mode]
        verdict_bits.append(
            f"{mode}: R=1->{R_MAX} changes "
            f"{len(dep['cells_changed_by_redundancy'])}/"
            f"{len(dep['majority_delta_R3_minus_R1'])} majority cells"
            f" ({len(dep['cells_improved_by_redundancy'])} improved);"
            f" restore bank0-minus-bank1 gap by R = "
            + ",".join(f"R{r}={contrast_by_r[mode][str(r)]}"
                       for r in R_VALUES)
        )
    cert_c = {
        "certificate": "C_REDUNDANCY_UNDER_PERTURBATION",
        "declared_sample": {
            "lanes": sampled,
            "boundary_cap": SAMPLE_BOUNDARY_CAP,
            "lane_cap": SAMPLE_LANE_CAP,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE,
            "classes": PERTURBATION_CLASSES,
            "r_values": R_VALUES,
            "modes": REDUNDANCY_MODES,
            "sides": SIDES,
            "stagger_walk_cap_boundaries": STAGGER_WALK_CAP,
            "base_not_clean_skips": base_not_clean,
            "degenerate_restore_skips": degenerate_restore_skips,
            "stagger_incomplete_base_lanes": stagger_incomplete_base,
            "stagger_incomplete_probes": stagger_incomplete_probe,
        },
        "side_semantics": (
            "sides are FIXED perturbation banks (bank0 = pack-state bank-0"
            " payload wires, bank1 = bank-1 payload wires); they are NOT a"
            " near/far record-locality contrast: no record-location"
            " selector is defined in this package and no bank-swap control"
            " was run"
        ),
        "probe_semantics": (
            "every perturbation changes the SOURCE state before any copy"
            " is formed (common-mode); no stored copy slot is faulted"
            " after writing, so for identical replicas the majority"
            " R-invariance is forced by construction and is reported as an"
            " exact identity, not as fault-tolerance evidence"
        ),
        "payload_derivation": {
            "pool_size": len(payload_pool),
            "bank_pool_sizes": [len(bank_payload[0]), len(bank_payload[1])],
            "membership": "kernel pack-state single-bit marking",
        },
        "per_r_per_mode": tally,
        "full_state_content_tally": full_state_tally,
        "computed_reading": computed,
        "r_dependence": r_dependence,
        "restore_gap_by_r": contrast_by_r,
        "restore_gap_decomposition": contrast_decomposition,
        "scan_probe_content_agreement":
            f"{scan_probe_content_agree}/{scan_probe_content_checked}",
        "finding": (
            "computed R-dependence of majority readback under the declared"
            " common-mode probes (see probe_semantics; not a stored-copy"
            " fault test) -- "
            + " | ".join(verdict_bits)
            + " || restore-class decomposition at R=1, fixed banks: "
            + "; ".join(
                f"{mode} firing_gap="
                f"{contrast_decomposition[mode]['1']['firing_gap_bank0_minus_bank1']}"
                f" content_gap_given_fired="
                f"{contrast_decomposition[mode]['1']['content_gap_given_fired_bank0_minus_bank1']}"
                for mode in REDUNDANCY_MODES
            )
        ),
    }
    cells_ok = all(
        0 <= cell["majority_equal"] <= cell["fired"] <= cell["probes"]
        <= sampled
        and 0 <= cell["all_copies_equal"] <= cell["fired"]
        and 0 <= cell["copy_survivals"] <= cell["fired"] * r
        for mode in REDUNDANCY_MODES for r in R_VALUES
        for cls in PERTURBATION_CLASSES
        for cell in (tally[mode][str(r)][cls]["bank0"],
                     tally[mode][str(r)][cls]["bank1"])
    )
    full_ok = all(
        0 <= cell["content_equal"] <= cell["fired"] <= cell["probes"]
        <= sampled
        for cls in PERTURBATION_CLASSES
        for cell in (full_state_tally[cls]["bank0"],
                     full_state_tally[cls]["bank1"])
    )
    # Integrity gates only -- bookkeeping consistency, never the outcome.
    cert_c["pass"] = (
        sampled > 0
        and cells_ok
        and full_ok
        and sampled + base_not_clean == len(candidates)
        and len(bank_payload[0]) > 0 and len(bank_payload[1]) > 0
        and scan_probe_content_checked > 0
        and scan_probe_content_agree == scan_probe_content_checked
    )

    # --- Certificate D: controls -----------------------------------------
    determinism = {
        "per_lane_probe_digests": per_lane_determinism,
        "slot_allocation_digest": digest(sorted(
            (compact(t), w) for t, w in slot_of.items()
        )),
        "repeat_slot_allocation_digest": digest(sorted(
            (compact(t), safe_slots_pool[i])
            for i, t in enumerate(slot_tags)
        )),
        "bank_rows_digest": digest([sorted(r) for r in bank_wire_rows(2)]),
        "repeat_bank_rows_digest": digest([sorted(r) for r in bank_wire_rows(2)]),
    }
    determinism["pass"] = (
        determinism["slot_allocation_digest"]
        == determinism["repeat_slot_allocation_digest"]
        and determinism["bank_rows_digest"]
        == determinism["repeat_bank_rows_digest"]
        and len(per_lane_determinism) > 0
    )
    runtime = round(monotonic() - started, 3)
    cert_d = {
        "certificate": "D_CONTROLS",
        "source_controls": controls,
        "seed_failures": seed_fail,
        "initial_state_failures": init_fail,
        "partition_marker_failures": part["marker_failures"],
        "duplicate_lane_mismatches": mism,
        "determinism": determinism,
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
    }
    cert_d["pass"] = bool(
        controls["pass"] and seed_fail == 0 and init_fail == 0
        and part["marker_failures"] == 0 and mism == 0
        and determinism["pass"] and runtime < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "A_REDUNDANT_CONTENT_REGISTER": cert_a["pass"],
        "B_CONTENT_READBACK": cert_b["pass"],
        "C_REDUNDANCY_UNDER_PERTURBATION": cert_c["pass"],
        "D_CONTROLS": cert_d["pass"],
    }
    lines = ["CYCLE874_COPY_REDUNDANCY_CONTENT",
             "BOUNDED_SUPPORT_CERTIFICATES_ONLY_NO_AXIOM_SURFACE_TOUCHED",
             "COMMON_MODE_PROBES_NO_STORED_COPY_FAULT_TESTED",
             "SIDES_ARE_FIXED_BANKS_NOT_RECORD_LOCALITY"]
    for name, payload in (("A_REDUNDANT_CONTENT_REGISTER", cert_a),
                          ("B_CONTENT_READBACK", cert_b),
                          ("C_REDUNDANCY_UNDER_PERTURBATION", cert_c),
                          ("D_CONTROLS", cert_d)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 874,
        "r_values": R_VALUES, "modes": REDUNDANCY_MODES,
        "semantic_scope": (
            "common-mode probes on fixed bank sides; identical-replica"
            " majority R-invariance is forced by construction; no"
            " stored-copy fault, locality, or framework-record claim"
        ),
        "redundancy_changes_majority_readback": {
            mode: r_dependence[mode]["any_change"] for mode in REDUNDANCY_MODES
        },
        "redundancy_improves_majority_readback": {
            mode: r_dependence[mode]["any_gain"] for mode in REDUNDANCY_MODES
        },
        "restore_gap_by_r": contrast_by_r,
        "restore_gap_decomposition_R1": {
            mode: {
                "firing_gap_R1":
                    contrast_decomposition[mode]["1"][
                        "firing_gap_bank0_minus_bank1"],
                "content_gap_given_fired_R1":
                    contrast_decomposition[mode]["1"][
                        "content_gap_given_fired_bank0_minus_bank1"],
            }
            for mode in REDUNDANCY_MODES
        },
        "runtime_seconds": round(monotonic() - started, 3),
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE874_COPY_REDUNDANCY_CONTENT_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
