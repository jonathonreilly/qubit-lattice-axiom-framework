#!/usr/bin/env python3
"""Cycle 877: shard-partitioned fingerprint registers under formation-edge
flips -- BOUNDED SUPPORT CERTIFICATES ONLY.

Grade: bounded support (demoted on physics review, iteration 1,
2026-08-08).  This runner certifies finite computations on a model built
in this file over the landed, sha-pinned Cycle-719 kernel -- its ONLY
computed input.  It does NOT establish record-content reconstruction, a
one-wire "survival law" beyond the six declared sample cells, physical
lattice locality, a contiguity design rule, or any adversarial-cost or
necessity statement.  Earlier wordings of those claims are retired.

What is stipulated in this file (model conventions, not framework
content):

  shard word -- the first CONTENT_BITS bits of SHA-256 over one block of
      the live payload projection.  This is a model-defined fingerprint.
      At the declared block sizes the map is NOT injective (at S=2 the
      147 payload bits map to 64 total digest bits; pigeonhole), so
      word equality is fingerprint agreement on the tested pairs, never
      payload reconstruction.  No decoder from stored words back to the
      payload exists in this package (open obligation), and whether the
      fingerprint corresponds to framework "record content" is an OPEN
      bridge that this package does not supply.
  damage set -- computed by comparing the HOST-RESIDENT perturbed and
      unperturbed states wire by wire.  Nothing in this package infers
      damage, coverage, or agreement from the register alone.
  blocks / "contiguity" -- contiguity in the ascending list of live
      packed-state wire indices.  No map from wire indices or blocks to
      lattice sites, nearest-neighbor adjacency, or spatial regions is
      defined here, so no physical-locality reading is available.
  sides -- perturbation wires are drawn from two FIXED pools: bank0
      (pack-state bank-0 payload wires) and bank1 (bank-1 payload
      wires).  The sides are fixed bank labels, NOT distances from a
      record; no record-location selector is defined in this package.

Certificates:

A. A_SHARDED_CONTENT_REGISTER: derive the structurally-dead safe pool;
   decompose the live payload into S contiguous blocks for S in
   {2, 4, 8}; allocate one disjoint inert slot group per shard; run the
   composed scan with real wire-mutating writes; read every word back.
B. B_SHARD_DAMAGE_INCIDENCE: the four declared perturbation classes on
   the fixed bank0/bank1 wire pools; exact host-computed damage sets;
   the per-shard incidence matrix; the monotone structural forward-cone
   superset check.  The confinement verdict and the incidence matrix
   are reported data, never gated.
C. C_FINGERPRINT_COVERAGE: per class and per S, the fraction of fired
   probes whose every registered shard word is unchanged, and the share
   of live wires lying in unhit shards.  Bookkeeping over host-computed
   damage; not reconstruction.
D. D_SLOT_BUDGET_TRADE: exact slot costs versus S against the derived
   safe-pool size.
E. E_CONTROLS: source pins (Cycle-719 kernel only), seed/initial-state
   integrity, reproduction of the landed Cycle-874 pool constants,
   determinism, runtime.

Declared scope: B=2 banks, k=2..5 census (748 lanes), horizon 16,384
orbits; dead-wire derivation window 512 orbits chunk-granular then 4,096
orbit-granular; existence register cap 64 wire-visible ordinals per
(tag, lane); shard content word 32 bits; S in {2, 4, 8}; sample 32
early-formation lanes with first-clean boundary <= 1,100, up to 4
payload wires per side; cost ladder up to S=512.  All caps disclosed in
the emitted certificates.  Integrity gates are bookkeeping and
mathematical soundness only: the incidence matrix, the confinement
verdict, and the coverage curves are data whichever way they fall.

Provenance context (non-load-bearing): the design descends from the
unlanded Cycle-863/867 line and the pre-review Cycle-874 submission.
Nothing from that line is read, pinned, imported, or gated on here;
every needed definition is stipulated in this file over the landed
kernel.  The pool-reproduction constants below are certified on
current main by the landed Cycle-874 bounded support note.

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
SHARD_COUNTS = (2, 4, 8)
SAMPLE_LANE_CAP = 32
SAMPLE_BOUNDARY_CAP = 1_100
PAYLOAD_WIRES_PER_SIDE = 4
PERTURBATION_CLASSES = (
    "one_flip", "late_acting", "untouched_in_chunk", "flip_and_restore"
)
COST_LADDER = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
DETERMINISM_LANES = 4
SIDES = ("bank0", "bank1")
WORD_MASK = (1 << CONTENT_BITS) - 1
DIGEST_BYTES = (CONTENT_BITS + 7) // 8

# Pool constants certified on current main by the landed Cycle-874
# bounded support note (docs/COPY_REDUNDANCY_CONTENT_CYCLE874_BOUNDED_
# THEOREM_NOTE_2026-07-28.md).  Reproduced here as a control, never as a
# physics gate on outcomes.
LANDED_874_POOL = {
    "dead_wire_count": 5_668,
    "safe_slot_pool": 5_270,
}


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
    """Per-step gate lists on the true trajectory."""
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
    marking."""
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


def block_decomposition(live, shards):
    """DECLARED decomposition: contiguous blocks of the live payload wire
    list in ascending wire index; the first (len(live) % shards) blocks
    carry one extra wire.  Contiguity here is wire-coordinate contiguity
    only; no spatial meaning is defined."""
    size, rem = divmod(len(live), shards)
    blocks, cursor = [], 0
    for idx in range(shards):
        width = size + (1 if idx < rem else 0)
        blocks.append(tuple(live[cursor:cursor + width]))
        cursor += width
    return tuple(blocks)


def shard_word(state, rows) -> int:
    """CONTENT_BITS truncated-SHA-256 fingerprint of one block of the
    LIVE payload -- a stipulated model convention.  The block contains no
    slot wire (slots are dead, live excludes dead), so the word never
    reads the register back into itself.  The map block-bits -> word is
    not injective at the declared block sizes, so word equality is
    fingerprint agreement, not payload identity."""
    return int.from_bytes(
        sha256(bytes(bytearray(state[w] for w in rows))).digest()[:DIGEST_BYTES],
        "big",
    ) & WORD_MASK


def forward_cone(chunk, seed_wires):
    """MONOTONE structural forward cone of `seed_wires` through one chunk.

    X flips its target unconditionally, so it can neither create nor
    destroy a difference and contributes nothing.  CNOT b ^= a propagates
    a difference on a into b.  Toffoli c ^= a & b propagates a difference
    on a or b into c.  Membership is only ever added, so the result is a
    SUPERSET of the true set of wires on which two states entering the
    chunk differing exactly on `seed_wires` can differ on exit.
    """
    cone = set(seed_wires)
    for gate in chunk:
        wires = gate.wires
        if gate.kind == "X":
            continue
        if gate.kind == "CNOT":
            if wires[0] in cone:
                cone.add(wires[1])
        elif wires[0] in cone or wires[1] in cone:
            cone.add(wires[2])
    return cone


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
    width = len(columns)
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

    # --- Certificate A part 1: the dead-wire safe pool --------------------
    acc = [0] * width
    work = list(columns)
    for w, c in enumerate(work):
        acc[w] |= c
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(width):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(width):
                acc[w] |= work[w]
    dead_wires = tuple(w for w in range(width) if (acc[w] & uni_sim) == 0)
    dead_set = set(dead_wires)
    live_wires = tuple(w for w in range(width) if w not in dead_set)

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

    # --- Certificate A part 2: the declared block decompositions ----------
    blocks = {s: block_decomposition(live_wires, s) for s in SHARD_COUNTS}
    block_sets = {
        s: tuple(frozenset(b) for b in blocks[s]) for s in SHARD_COUNTS
    }
    shard_of = {
        s: {w: idx for idx, blk in enumerate(blocks[s]) for w in blk}
        for s in SHARD_COUNTS
    }
    decomposition_disclosure = {
        str(s): {
            "rule": (
                "contiguous blocks of the live payload wire list in"
                " ascending wire index; the first (len(live) % S) blocks"
                " carry one extra wire; wire-coordinate contiguity only,"
                " no spatial meaning defined"
            ),
            "block_sizes": [len(b) for b in blocks[s]],
            "block_first_wire": [b[0] for b in blocks[s]],
            "block_last_wire": [b[-1] for b in blocks[s]],
            "covers_live_exactly": (
                sorted(w for b in blocks[s] for w in b) == list(live_wires)
            ),
            "pairwise_disjoint": (
                sum(len(b) for b in blocks[s]) == len(live_wires)
            ),
            "no_empty_block": all(len(b) > 0 for b in blocks[s]),
        }
        for s in SHARD_COUNTS
    }

    # --- Certificate A part 3: one dead slot group per shard --------------
    existence_tags = [("E", "G", 0)] + [
        ("E", f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    content_tags = [
        ("C", s, shard, bit)
        for s in SHARD_COUNTS
        for shard in range(s)
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
    shard_groups = {
        (s, shard): frozenset(
            content_slot[(s, shard, bit)] for bit in range(CONTENT_BITS)
        )
        for s in SHARD_COUNTS for shard in range(s)
    }
    group_keys = sorted(shard_groups)
    pairwise_overlaps = sum(
        len(shard_groups[a] & shard_groups[b])
        for i, a in enumerate(group_keys) for b in group_keys[i + 1:]
    )
    existence_group = frozenset(exist_slot.values())
    content_all = frozenset().union(*shard_groups.values())
    disjointness = {
        "slot_tags": len(slot_tags),
        "distinct_slot_wires": len(slot_wires),
        "shard_group_size": CONTENT_BITS,
        "shard_groups": len(shard_groups),
        "pairwise_shard_group_overlaps": pairwise_overlaps,
        "content_existence_overlap": len(content_all & existence_group),
        "all_slots_in_safe_pool": len(slot_wires - set(safe_slots_pool)) == 0,
    }
    inertness = {
        "slots_in_gate_inputs": len(slot_wires & gate_inputs),
        "slots_in_gate_targets": len(slot_wires & gate_targets),
        "content_slots_in_gate_inputs": len(content_all & gate_inputs),
        "content_slots_in_gate_targets": len(content_all & gate_targets),
        "content_slots_all_dead": len(content_all - dead_set) == 0,
        "slots_disjoint_from_live_payload": len(slot_wires & set(live_wires)),
        "statement": (
            "every shard's slots are dead wires that no gate reads or"
            " writes, so mutation is structurally inert for every shard;"
            " the live payload excludes all dead wires, so the block"
            " decomposition is independent of S and of the allocation"
        ),
    }

    # --- The composed scan: base dynamics + real existence and shard writes
    columns = pack_columns(states + (states[0],))
    nonslot_dead = tuple(w for w in dead_wires if w not in slot_wires)
    over_universe = sum(1 for col in columns if col >> (n + 1))
    bank_write_ordinal = [[0, 0] for _ in range(n)]
    write_once_violations = 0
    content_write_once_violations = 0
    dead_activation_conflicts = 0
    wire_visible_writes = 0
    content_bit_writes = 0
    host_words: dict = {}
    written_lanes: dict = {key: 0 for key in shard_groups}

    def wire_write(tag, lane):
        nonlocal write_once_violations, wire_visible_writes
        wire = exist_slot[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit
        wire_visible_writes += 1

    def shard_write(lane, state):
        nonlocal content_write_once_violations, content_bit_writes
        bit = 1 << lane
        for s in SHARD_COUNTS:
            for shard in range(s):
                key = (s, shard)
                if written_lanes[key] & bit:
                    content_write_once_violations += 1
                written_lanes[key] |= bit
                word = shard_word(state, blocks[s][shard])
                for j in range(CONTENT_BITS):
                    if (word >> j) & 1:
                        columns[content_slot[(s, shard, j)]] |= bit
                content_bit_writes += CONTENT_BITS
                host_words[(s, shard, lane)] = word

    prev_bank = [
        clean_mask(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    e1_first_composed: dict = {}
    prev_global = clean_mask(columns, global_dirty, uni_sim)
    mism = int(bool(prev_global & 1) != bool(prev_global & (1 << dup)))
    for lane in lanes_of(prev_global & uni_all):
        e1_first_composed.setdefault(census[lane], 0)
        wire_write(("G", 0), lane)
        shard_write(lane, lane_state(columns, lane))

    boundary = 0
    getter = columns.__getitem__
    for orbit in range(1, HORIZON + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, uni_sim)
            mism += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            for lane in lanes_of(ga):
                if census[lane] not in e1_first_composed:
                    e1_first_composed[census[lane]] = boundary
                    shard_write(lane, lane_state(columns, lane))
            for b in (0, 1):
                bm = clean_mask(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in lanes_of(edge):
                    ordinal = bank_write_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                    bank_write_ordinal[lane][b] = ordinal + 1
                prev_bank[b] = bm
            if any(map(getter, nonslot_dead)):
                dead_activation_conflicts += 1

    cert_a = {
        "certificate": "A_SHARDED_CONTENT_REGISTER",
        "declared_scope": {
            "banks": BANKS,
            "census_k_range": (KMIN, KMAX),
            "horizon_orbits": HORIZON,
            "dead_window_chunk_granular_orbits": DEAD_CHUNK_ORBITS,
            "dead_window_orbit_granular_orbits": DEAD_ORBIT_ORBITS,
            "existence_register_cap_per_tag_lane": REGISTER_CAP,
            "content_bits_per_shard": CONTENT_BITS,
            "shard_counts": SHARD_COUNTS,
        },
        "word_convention": (
            "each shard word is a STIPULATED model fingerprint: the first"
            " 32 bits of SHA-256 over the block's bits; not injective at"
            " the declared block sizes, so word equality is fingerprint"
            " agreement, not payload identity; no framework record-content"
            " identification is claimed (open bridge)"
        ),
        "state_width": width,
        "dead_wire_count": len(dead_wires),
        "live_payload_wires": len(live_wires),
        "safe_slot_pool": len(safe_slots_pool),
        "decomposition": decomposition_disclosure,
        "disjointness": disjointness,
        "structural_inertness": inertness,
        "columns_above_universe": over_universe,
        "dead_activation_conflicts_through_horizon": dead_activation_conflicts,
        "existence_write_once_violations": write_once_violations,
        "content_write_once_violations": content_write_once_violations,
        "wire_visible_existence_writes": wire_visible_writes,
        "content_bit_write_events": content_bit_writes,
        "lanes_with_content_per_shard_group": {
            compact(key): bin(mask).count("1")
            for key, mask in sorted(written_lanes.items())
        },
        "reproduces_landed_874_pool": (
            len(dead_wires) == LANDED_874_POOL["dead_wire_count"]
            and len(safe_slots_pool) == LANDED_874_POOL["safe_slot_pool"]
        ),
    }
    cert_a["pass"] = (
        len(dead_wires) > 0
        and len(live_wires) > 0
        and disjointness["distinct_slot_wires"] == disjointness["slot_tags"]
        and disjointness["pairwise_shard_group_overlaps"] == 0
        and disjointness["content_existence_overlap"] == 0
        and disjointness["all_slots_in_safe_pool"]
        and inertness["slots_in_gate_inputs"] == 0
        and inertness["slots_in_gate_targets"] == 0
        and inertness["content_slots_all_dead"]
        and inertness["slots_disjoint_from_live_payload"] == 0
        and all(
            decomposition_disclosure[str(s)]["covers_live_exactly"]
            and decomposition_disclosure[str(s)]["pairwise_disjoint"]
            and decomposition_disclosure[str(s)]["no_empty_block"]
            for s in SHARD_COUNTS
        )
        and over_universe == 0
        and dead_activation_conflicts == 0
        and write_once_violations == 0
        and content_write_once_violations == 0
        and content_bit_writes > 0
    )

    # --- read every shard back out of the state ---------------------------
    def readback(s, shard, lane):
        bit = 1 << lane
        return sum(
            ((columns[content_slot[(s, shard, j)]] & bit) != 0) << j
            for j in range(CONTENT_BITS)
        )

    readback_mismatches = 0
    for (s, shard, lane), word in host_words.items():
        readback_mismatches += int(readback(s, shard, lane) != word)
    content_lane_masks = {
        s: written_lanes[(s, 0)] for s in SHARD_COUNTS
    }
    shard_diversity = {
        str(s): {
            "lanes_with_shards": bin(content_lane_masks[s]).count("1"),
            "distinct_words_per_shard": [
                len({
                    readback(s, shard, lane)
                    for lane in lanes_of(content_lane_masks[s])
                })
                for shard in range(s)
            ],
        }
        for s in SHARD_COUNTS
    }
    existence_lane_count = len(
        set(lanes_of(columns[exist_slot[("G", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B0", 0)]] & uni_all))
        | set(lanes_of(columns[exist_slot[("B1", 0)]] & uni_all))
    )

    # --- Certificate B: damage incidence under perturbation ---------------
    payload_pool = [
        w for w in range(width)
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

    def new_cell(s):
        return {
            "probes": 0, "fired": 0,
            "shard_deaths": [0] * s,
            "predicted_deaths": [0] * s,
            "all_shards_survive": 0, "any_shard_survives": 0,
            "no_shard_survives": 0,
            "confined_to_flip_shard": 0,
            "law_violations": 0,
            "digest_vs_bits_disagreements": 0,
            "surviving_wire_fraction_sum": 0.0,
            "surviving_shard_count_sum": 0,
            "flip_shard_index_counts": {},
        }

    tally = {
        str(s): {cls: {side: new_cell(s) for side in SIDES}
                 for cls in PERTURBATION_CLASSES}
        for s in SHARD_COUNTS
    }
    damage = {
        cls: {side: {"n": 0, "size_sum": 0, "size_min": None, "size_max": None,
                     "fired_n": 0, "fired_size_sum": 0,
                     "fired_size_max": None,
                     "cone_sum": 0, "cone_min": None, "cone_max": None,
                     "entry_divergence_sum": 0,
                     "damage_outside_live": 0,
                     "damage_contains_flip_wire": 0,
                     "damage_within_cone": 0,
                     "empty_damage": 0}
              for side in SIDES}
        for cls in PERTURBATION_CLASSES
    }
    full_state_tally = {
        cls: {side: {"probes": 0, "fired": 0, "content_equal": 0}
              for side in SIDES}
        for cls in PERTURBATION_CLASSES
    }
    sampled = 0
    base_not_clean = 0
    degenerate_restore_skips = 0
    scan_probe_shard_agree = 0
    scan_probe_shard_checked = 0
    per_lane_determinism: list = []
    live_set = set(live_wires)
    live_total = len(live_wires)
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
        base_shard_words = {
            s: [shard_word(base_after, blocks[s][i]) for i in range(s)]
            for s in SHARD_COUNTS
        }
        # scan-versus-probe cross-check: every shard word the register
        # stored for this lane must equal the probe's walked shard word.
        if (SHARD_COUNTS[0], 0, lane) in host_words:
            for s in SHARD_COUNTS:
                for shard in range(s):
                    scan_probe_shard_checked += 1
                    scan_probe_shard_agree += int(
                        readback(s, shard, lane) == base_shard_words[s][shard]
                    )
        # Sides are FIXED perturbation banks.  (An earlier revision derived
        # a "record bank" here, but its selector was tautological -- the
        # accepted-candidate cleanliness condition forces bank 0 -- so no
        # near/far record-location labelling is available from this probe.)
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
                    entry = tuple(restored)
                else:
                    mut = list(pre)
                    mut[wire] ^= 1
                    entry = tuple(mut)
                after = K.A.apply_semantic(entry, last_chunk)
                fired = is_clean(after)
                fs = full_state_tally[cls][side]
                fs["probes"] += 1
                fs["fired"] += int(fired)
                if fired:
                    fs["content_equal"] += int(
                        sha256(bytes(after)).hexdigest() == base_full
                    )
                entry_div = tuple(
                    w for w in range(width) if entry[w] != pre[w]
                )
                cone = forward_cone(last_chunk, entry_div)
                dmg = tuple(
                    w for w in range(width) if after[w] != base_after[w]
                )
                dset = set(dmg)
                dm = damage[cls][side]
                dm["n"] += 1
                dm["size_sum"] += len(dmg)
                dm["size_min"] = (
                    len(dmg) if dm["size_min"] is None
                    else min(dm["size_min"], len(dmg))
                )
                dm["size_max"] = (
                    len(dmg) if dm["size_max"] is None
                    else max(dm["size_max"], len(dmg))
                )
                dm["cone_sum"] += len(cone)
                dm["cone_min"] = (
                    len(cone) if dm["cone_min"] is None
                    else min(dm["cone_min"], len(cone))
                )
                dm["cone_max"] = (
                    len(cone) if dm["cone_max"] is None
                    else max(dm["cone_max"], len(cone))
                )
                if fired:
                    dm["fired_n"] += 1
                    dm["fired_size_sum"] += len(dmg)
                    dm["fired_size_max"] = (
                        len(dmg) if dm["fired_size_max"] is None
                        else max(dm["fired_size_max"], len(dmg))
                    )
                dm["entry_divergence_sum"] += len(entry_div)
                dm["damage_outside_live"] += len(dset - live_set)
                dm["damage_contains_flip_wire"] += int(wire in dset)
                dm["damage_within_cone"] += int(dset <= cone)
                dm["empty_damage"] += int(not dmg)
                for s in SHARD_COUNTS:
                    cell = tally[str(s)][cls][side]
                    cell["probes"] += 1
                    cell["fired"] += int(fired)
                    flip_shard = shard_of[s][wire]
                    fkey = str(flip_shard)
                    cell["flip_shard_index_counts"][fkey] = (
                        cell["flip_shard_index_counts"].get(fkey, 0) + 1
                    )
                    predicted = {
                        i for i in range(s) if cone & block_sets[s][i]
                    }
                    for i in predicted:
                        cell["predicted_deaths"][i] += 1
                    if not fired:
                        continue
                    dead_by_bits = {
                        i for i in range(s) if dset & block_sets[s][i]
                    }
                    dead_by_word = {
                        i for i in range(s)
                        if shard_word(after, blocks[s][i])
                        != base_shard_words[s][i]
                    }
                    cell["digest_vs_bits_disagreements"] += int(
                        dead_by_bits != dead_by_word
                    )
                    for i in dead_by_bits:
                        cell["shard_deaths"][i] += 1
                    survivors = [i for i in range(s) if i not in dead_by_bits]
                    cell["surviving_shard_count_sum"] += len(survivors)
                    cell["surviving_wire_fraction_sum"] += (
                        sum(len(blocks[s][i]) for i in survivors) / live_total
                    )
                    cell["all_shards_survive"] += int(not dead_by_bits)
                    cell["any_shard_survives"] += int(len(survivors) > 0)
                    cell["no_shard_survives"] += int(not survivors)
                    cell["confined_to_flip_shard"] += int(
                        dead_by_bits <= {flip_shard}
                    )
                    cell["law_violations"] += int(
                        not dead_by_bits <= predicted
                    )
                    if len(lane_cells) < DETERMINISM_LANES * 24:
                        lane_cells.append(
                            (s, cls, side, sorted(dead_by_bits), len(dmg))
                        )
        if len(per_lane_determinism) < DETERMINISM_LANES:
            per_lane_determinism.append(digest(lane_cells))

    def ratio(num, den):
        return round(num / den, 6) if den else None

    incidence = {}
    for s in SHARD_COUNTS:
        rows = {}
        for cls in PERTURBATION_CLASSES:
            for side in SIDES:
                cell = tally[str(s)][cls][side]
                rows[f"{cls}.{side}"] = {
                    "probes": cell["probes"],
                    "fired": cell["fired"],
                    "shard_deaths": cell["shard_deaths"],
                    "predicted_deaths": cell["predicted_deaths"],
                    "flip_shard_index_counts": cell["flip_shard_index_counts"],
                    "mean_shards_dead_given_fired": ratio(
                        sum(cell["shard_deaths"]), cell["fired"]
                    ),
                    "any_shard_survives_given_fired": ratio(
                        cell["any_shard_survives"], cell["fired"]
                    ),
                    "confined_to_flip_shard_given_fired": ratio(
                        cell["confined_to_flip_shard"], cell["fired"]
                    ),
                }
        incidence[str(s)] = rows

    damage_reading = {
        f"{cls}.{side}": {
            "probes": damage[cls][side]["n"],
            "mean_damage_wires": ratio(
                damage[cls][side]["size_sum"], damage[cls][side]["n"]
            ),
            "min_damage_wires": damage[cls][side]["size_min"],
            "max_damage_wires": damage[cls][side]["size_max"],
            "mean_damage_density_of_live": ratio(
                damage[cls][side]["size_sum"],
                damage[cls][side]["n"] * live_total
            ),
            "fired_probes": damage[cls][side]["fired_n"],
            "mean_damage_wires_given_fired": ratio(
                damage[cls][side]["fired_size_sum"], damage[cls][side]["fired_n"]
            ),
            "max_damage_wires_given_fired": damage[cls][side]["fired_size_max"],
            "mean_damage_density_given_fired": ratio(
                damage[cls][side]["fired_size_sum"],
                damage[cls][side]["fired_n"] * live_total
            ),
            "mean_cone_wires": ratio(
                damage[cls][side]["cone_sum"], damage[cls][side]["n"]
            ),
            "max_cone_wires": damage[cls][side]["cone_max"],
            "mean_entry_divergence_wires": ratio(
                damage[cls][side]["entry_divergence_sum"],
                damage[cls][side]["n"]
            ),
            "damage_outside_live_wires": damage[cls][side]["damage_outside_live"],
            "damage_contains_flip_wire": damage[cls][side][
                "damage_contains_flip_wire"],
            "damage_within_cone": damage[cls][side]["damage_within_cone"],
            "empty_damage_probes": damage[cls][side]["empty_damage"],
        }
        for cls in PERTURBATION_CLASSES for side in SIDES
    }
    law_violations_total = sum(
        tally[str(s)][cls][side]["law_violations"]
        for s in SHARD_COUNTS for cls in PERTURBATION_CLASSES for side in SIDES
    )
    collision_total = sum(
        tally[str(s)][cls][side]["digest_vs_bits_disagreements"]
        for s in SHARD_COUNTS for cls in PERTURBATION_CLASSES for side in SIDES
    )
    cone_containment_failures = sum(
        damage[cls][side]["n"] - damage[cls][side]["damage_within_cone"]
        for cls in PERTURBATION_CLASSES for side in SIDES
    )
    direct_classes = tuple(c for c in PERTURBATION_CLASSES
                           if c != "flip_and_restore")
    confined_cells = []
    unconfined_cells = []
    for s in SHARD_COUNTS:
        for cls in direct_classes:
            for side in SIDES:
                cell = tally[str(s)][cls][side]
                if not cell["fired"]:
                    continue
                if cell["confined_to_flip_shard"] == cell["fired"]:
                    confined_cells.append(f"S{s}.{cls}.{side}")
                if cell["no_shard_survives"] == cell["fired"]:
                    unconfined_cells.append(f"S{s}.{cls}.{side}")
    cert_b = {
        "certificate": "B_SHARD_DAMAGE_INCIDENCE",
        "declared_sample": {
            "lanes": sampled,
            "boundary_cap": SAMPLE_BOUNDARY_CAP,
            "lane_cap": SAMPLE_LANE_CAP,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE,
            "classes": PERTURBATION_CLASSES,
            "shard_counts": SHARD_COUNTS,
            "base_not_clean_skips": base_not_clean,
            "degenerate_restore_skips": degenerate_restore_skips,
        },
        "side_semantics": (
            "sides are FIXED perturbation banks (bank0 = pack-state bank-0"
            " payload wires, bank1 = bank-1 payload wires); they are NOT a"
            " near/far record-locality contrast: no record-location"
            " selector is defined in this package and no bank-swap control"
            " was run"
        ),
        "shard_death_semantics": (
            "a shard 'dies' iff its block intersects the HOST-COMPUTED"
            " damage set (perturbed versus unperturbed state, both host-"
            "resident); this is checked exactly against registered-word"
            " change per fired probe; an unchanged fingerprint is not"
            " payload recovery and no reconstruction claim is made"
        ),
        "payload_derivation": {
            "pool_size": len(payload_pool),
            "bank_pool_sizes": [len(bank_payload[0]), len(bank_payload[1])],
            "membership": "kernel pack-state single-bit marking",
        },
        "cone_superset_statement": (
            "the monotone structural forward cone of the perturbation's"
            " entry divergence set is a SUPERSET of the true post-chunk"
            " difference set by construction, so cone containment is a"
            " soundness check; the shard incidence matrix on the declared"
            " sample cells is data, not a universal law"
        ),
        "incidence_matrix": incidence,
        "damage_reading": damage_reading,
        "full_state_content_tally": full_state_tally,
        "per_shard_count_cells": tally,
        "cone_containment_failures": cone_containment_failures,
        "law_violations_total": law_violations_total,
        "digest_vs_bits_disagreements_total": collision_total,
        "scan_probe_shard_agreement":
            f"{scan_probe_shard_agree}/{scan_probe_shard_checked}",
        "shard_diversity": shard_diversity,
        "verdict": {
            "scope": (
                "wire-coordinate confinement on the declared sample cells"
                " only; not physical locality and not a statement beyond"
                " the declared classes, sides, and caps"
            ),
            "cells_with_damage_confined_to_flip_shard": confined_cells,
            "cells_with_no_surviving_shard": unconfined_cells,
            "reading": (
                "CONFINED" if confined_cells and not unconfined_cells
                else "UNCONFINED" if unconfined_cells and not confined_cells
                else "MIXED"
            ),
        },
    }
    cells_ok = all(
        0 <= cell["fired"] <= cell["probes"] <= sampled
        and 0 <= cell["any_shard_survives"] <= cell["fired"]
        and 0 <= cell["all_shards_survive"] <= cell["any_shard_survives"]
        and 0 <= cell["confined_to_flip_shard"] <= cell["fired"]
        and all(0 <= d <= cell["fired"] for d in cell["shard_deaths"])
        and all(0 <= d <= cell["probes"] for d in cell["predicted_deaths"])
        for s in SHARD_COUNTS for cls in PERTURBATION_CLASSES
        for cell in (tally[str(s)][cls]["bank0"], tally[str(s)][cls]["bank1"])
    )
    full_ok = all(
        0 <= cell["content_equal"] <= cell["fired"] <= cell["probes"] <= sampled
        for cls in PERTURBATION_CLASSES
        for cell in (full_state_tally[cls]["bank0"],
                     full_state_tally[cls]["bank1"])
    )
    # Integrity gates: bookkeeping consistency, the mathematical soundness
    # of the cone construction, and hash-collision freedom.  The
    # confinement verdict and the incidence matrix are never gated.
    cert_b["pass"] = (
        sampled > 0
        and cells_ok
        and full_ok
        and sampled + base_not_clean == len(candidates)
        and cone_containment_failures == 0
        and law_violations_total == 0
        and collision_total == 0
        and scan_probe_shard_checked > 0
        and scan_probe_shard_agree == scan_probe_shard_checked
        and all(
            damage[cls][side]["damage_outside_live"] == 0
            for cls in PERTURBATION_CLASSES for side in SIDES
        )
    )

    # --- Certificate C: fingerprint coverage over host-computed damage ----
    coverage = {}
    for s in SHARD_COUNTS:
        rows = {}
        for cls in PERTURBATION_CLASSES:
            for side in SIDES:
                cell = tally[str(s)][cls][side]
                rows[f"{cls}.{side}"] = {
                    "fired": cell["fired"],
                    "all_shard_words_unchanged": ratio(
                        cell["all_shards_survive"], cell["fired"]
                    ),
                    "any_shard_word_unchanged": ratio(
                        cell["any_shard_survives"], cell["fired"]
                    ),
                    "mean_surviving_shard_fraction": ratio(
                        cell["surviving_shard_count_sum"], cell["fired"] * s
                    ),
                    "mean_unhit_shard_wire_fraction": (
                        round(cell["surviving_wire_fraction_sum"]
                              / cell["fired"], 6) if cell["fired"] else None
                    ),
                }
        coverage[str(s)] = rows
    marginal = {}
    for cls in PERTURBATION_CLASSES:
        for side in SIDES:
            row = f"{cls}.{side}"
            curve = {
                str(s): coverage[str(s)][row][
                    "mean_unhit_shard_wire_fraction"]
                for s in SHARD_COUNTS
            }
            dens = damage_reading[row]["mean_damage_density_given_fired"]
            deltas = {}
            for a, b in zip(SHARD_COUNTS, SHARD_COUNTS[1:]):
                lo, hi = curve[str(a)], curve[str(b)]
                deltas[f"S{a}_to_S{b}"] = (
                    None if lo is None or hi is None else round(hi - lo, 6)
                )
            marginal[row] = {
                "unhit_wire_fraction_by_S": curve,
                "marginal_gain": deltas,
                "saturation_limit_one_minus_damage_density": (
                    None if dens is None else round(1.0 - dens, 6)
                ),
                "gap_to_saturation_at_S_max": (
                    None if curve[str(SHARD_COUNTS[-1])] is None or dens is None
                    else round(
                        (1.0 - dens) - curve[str(SHARD_COUNTS[-1])], 6
                    )
                ),
                "all_words_unchanged_by_S": {
                    str(s): coverage[str(s)][row][
                        "all_shard_words_unchanged"]
                    for s in SHARD_COUNTS
                },
            }
    cert_c = {
        "certificate": "C_FINGERPRINT_COVERAGE",
        "definitions": (
            "all shard words unchanged == every shard's registered 32-bit"
            " truncated-hash fingerprint equals the unperturbed run's; a"
            " finite fingerprint-agreement observation on the tested pairs,"
            " NOT payload reconstruction (the words are non-injective"
            " digests and no decoder exists in this package); unhit-shard"
            " wire fraction == the share of live wires lying in shards"
            " whose blocks miss the HOST-COMPUTED damage set; both are"
            " bookkeeping over host data, not register-only recovery"
        ),
        "per_shard_count": coverage,
        "marginal_value_of_S": marginal,
        "live_payload_wires": live_total,
        "saturation_note": (
            "as S grows the unhit-shard wire fraction is bounded above by"
            " 1 - damage_density on the sampled cells; the exact per-cell"
            " value is 1 - |hit block|/147 and depends on which block is"
            " hit, so the side-resolved branch is disclosed and no exact"
            " halving law is claimed"
        ),
    }
    cert_c["pass"] = all(
        (row["all_shard_words_unchanged"] is None
         or 0.0 <= row["all_shard_words_unchanged"] <= 1.0)
        and (row["mean_unhit_shard_wire_fraction"] is None
             or 0.0 <= row["mean_unhit_shard_wire_fraction"] <= 1.0)
        and (row["any_shard_word_unchanged"] is None
             or row["all_shard_words_unchanged"] is None
             or row["all_shard_words_unchanged"]
             <= row["any_shard_word_unchanged"])
        for s in SHARD_COUNTS for row in coverage[str(s)].values()
    )

    # --- Certificate D: the slot budget trade -----------------------------
    existence_slots = len(existence_tags)
    pool_size = len(safe_slots_pool)
    max_feasible_s = (pool_size - existence_slots) // CONTENT_BITS
    cost_curve = {
        str(s): {
            "content_slots": s * CONTENT_BITS,
            "existence_slots": existence_slots,
            "total_slots": s * CONTENT_BITS + existence_slots,
            "fraction_of_safe_pool": round(
                (s * CONTENT_BITS + existence_slots) / pool_size, 6
            ),
            "feasible": s * CONTENT_BITS + existence_slots <= pool_size,
            "block_size_wires": len(live_wires) // s,
            "block_granularity_ok": s <= len(live_wires),
        }
        for s in COST_LADDER
    }
    measured_total = len(slot_tags)
    # One live wire per shard is the finest decomposition the payload
    # admits; on the sampled cells it is where the unhit fraction meets
    # its bound.  Exact arithmetic under the declared 32-bit convention.
    s_sat = live_total
    saturating = {
        "saturating_S_one_wire_per_shard": s_sat,
        "content_slots": s_sat * CONTENT_BITS,
        "total_slots": s_sat * CONTENT_BITS + existence_slots,
        "fraction_of_safe_pool": round(
            (s_sat * CONTENT_BITS + existence_slots) / pool_size, 6
        ),
        "feasible": s_sat * CONTENT_BITS + existence_slots <= pool_size,
        "binding_constraint": (
            "payload granularity" if s_sat <= max_feasible_s else "safe pool"
        ),
    }
    efficiency = {}
    for cls in PERTURBATION_CLASSES:
        for side in SIDES:
            row = f"{cls}.{side}"
            eff = {}
            for a, b in zip(SHARD_COUNTS, SHARD_COUNTS[1:]):
                gain = marginal[row]["marginal_gain"][f"S{a}_to_S{b}"]
                spend = (b - a) * CONTENT_BITS
                eff[f"S{a}_to_S{b}"] = (
                    None if gain is None else round(gain / spend, 9)
                )
            efficiency[row] = eff
    cert_d = {
        "certificate": "D_SLOT_BUDGET_TRADE",
        "safe_slot_pool": pool_size,
        "content_bits_per_shard": CONTENT_BITS,
        "existence_register_slots": existence_slots,
        "slots_used_by_this_run": measured_total,
        "shard_counts_carried_simultaneously": SHARD_COUNTS,
        "cost_ladder": COST_LADDER,
        "cost_curve": cost_curve,
        "max_feasible_S_from_pool": max_feasible_s,
        "pool_bounds_measured_S": any(
            not cost_curve[str(s)]["feasible"] for s in SHARD_COUNTS
        ),
        "saturating_S": saturating,
        "unhit_fraction_gain_per_slot": efficiency,
        "structural_note": (
            "slots are drawn from the structurally-dead safe pool and the"
            " live payload excludes every dead wire, so raising S spends"
            " slot budget without shrinking the payload being sharded;"
            " the pool is the only budget the trade touches; all costs are"
            " exact arithmetic under the stipulated 32-bit word and"
            " 129-slot existence-register conventions"
        ),
    }
    ladder_totals = [cost_curve[str(s)]["total_slots"] for s in COST_LADDER]
    cert_d["pass"] = (
        pool_size > 0
        and measured_total == existence_slots + sum(SHARD_COUNTS) * CONTENT_BITS
        and measured_total <= pool_size
        and ladder_totals == sorted(ladder_totals)
        and all(
            cost_curve[str(s)]["feasible"]
            == (cost_curve[str(s)]["total_slots"] <= pool_size)
            for s in COST_LADDER
        )
    )

    # --- Certificate E: controls ------------------------------------------
    reproduction = {
        "expected": LANDED_874_POOL,
        "observed": {
            "dead_wire_count": len(dead_wires),
            "safe_slot_pool": len(safe_slots_pool),
        },
        "source": (
            "pool constants certified by the landed Cycle-874 bounded"
            " support note on current main; a control, not an outcome gate"
        ),
    }
    reproduction["pass"] = (
        reproduction["observed"]["dead_wire_count"]
        == LANDED_874_POOL["dead_wire_count"]
        and reproduction["observed"]["safe_slot_pool"]
        == LANDED_874_POOL["safe_slot_pool"]
    )
    determinism = {
        "determinism_lane_cap": DETERMINISM_LANES,
        "per_lane_probe_digests": per_lane_determinism,
        "decomposition_digest": digest(
            {str(s): [list(b) for b in blocks[s]] for s in SHARD_COUNTS}
        ),
        "repeat_decomposition_digest": digest(
            {str(s): [list(b) for b in block_decomposition(live_wires, s)]
             for s in SHARD_COUNTS}
        ),
        "slot_allocation_digest": digest(sorted(
            (compact(t), w) for t, w in slot_of.items()
        )),
        "repeat_slot_allocation_digest": digest(sorted(
            (compact(t), safe_slots_pool[i]) for i, t in enumerate(slot_tags)
        )),
        "bank_rows_digest": digest([sorted(r) for r in bank_wire_rows(2)]),
        "repeat_bank_rows_digest": digest([sorted(r) for r in bank_wire_rows(2)]),
    }
    determinism["pass"] = (
        determinism["decomposition_digest"]
        == determinism["repeat_decomposition_digest"]
        and determinism["slot_allocation_digest"]
        == determinism["repeat_slot_allocation_digest"]
        and determinism["bank_rows_digest"]
        == determinism["repeat_bank_rows_digest"]
        and len(per_lane_determinism) > 0
    )
    runtime = round(monotonic() - started, 3)
    cert_e = {
        "certificate": "E_CONTROLS",
        "source_controls": controls,
        "seed_failures": seed_fail,
        "initial_state_failures": init_fail,
        "partition_marker_failures": part["marker_failures"],
        "duplicate_lane_mismatches": mism,
        "shard_readback_host_mismatches": readback_mismatches,
        "shard_words_written": len(host_words),
        "existence_leg": {
            "composed_first_writes": len(e1_first_composed),
            "lanes_with_any_first_slot_bit": existence_lane_count,
        },
        "landed_pool_reproduction": reproduction,
        "determinism": determinism,
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
    }
    cert_e["pass"] = bool(
        controls["pass"] and seed_fail == 0 and init_fail == 0
        and part["marker_failures"] == 0 and mism == 0
        and readback_mismatches == 0
        and len(host_words) > 0 and reproduction["pass"]
        and determinism["pass"] and runtime < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "A_SHARDED_CONTENT_REGISTER": cert_a["pass"],
        "B_SHARD_DAMAGE_INCIDENCE": cert_b["pass"],
        "C_FINGERPRINT_COVERAGE": cert_c["pass"],
        "D_SLOT_BUDGET_TRADE": cert_d["pass"],
        "E_CONTROLS": cert_e["pass"],
    }
    direct_any_survive = {
        str(s): {
            f"{cls}.{side}": incidence[str(s)][f"{cls}.{side}"][
                "any_shard_survives_given_fired"]
            for cls in direct_classes for side in SIDES
        }
        for s in SHARD_COUNTS
    }
    finding = (
        "bounded support, sampled cells only: mean shard fingerprints"
        " changed per fired probe on the direct-flip classes = "
        + compact({
            str(s): {
                f"{cls}.{side}": incidence[str(s)][f"{cls}.{side}"][
                    "mean_shards_dead_given_fired"]
                for cls in direct_classes for side in SIDES
            }
            for s in SHARD_COUNTS
        })
        + f"; confinement reading {cert_b['verdict']['reading']}"
        + f" (confined-to-flip-shard cells: {len(confined_cells)},"
        + f" no-survivor cells: {len(unconfined_cells)}) on the declared"
        + " sample cells (wire-coordinate confinement, not physical"
        + " locality); all-shard-words-unchanged fraction = "
        + compact({
            str(s): {
                f"{cls}.{side}": coverage[str(s)][f"{cls}.{side}"][
                    "all_shard_words_unchanged"]
                for cls in direct_classes for side in SIDES
            }
            for s in SHARD_COUNTS
        })
        + " (fingerprint agreement over host-computed damage, not"
        + " reconstruction); mean damage wires given fired on the direct"
        + " classes = "
        + compact({
            f"{cls}.{side}":
                damage_reading[f"{cls}.{side}"]["mean_damage_wires_given_fired"]
            for cls in direct_classes for side in SIDES
        })
        + f" of {live_total} live wires; the safe pool admits S<="
        + f"{max_feasible_s} while the payload granularity caps S at"
        + f" {live_total} (binding constraint:"
        + f" {saturating['binding_constraint']}, cost"
        + f" {saturating['fraction_of_safe_pool']} of the pool); no"
        + " reconstruction, locality, design-rule, or necessity claim"
    )
    lines = ["CYCLE877_SHARDED_CONTENT",
             "BOUNDED_SUPPORT_CERTIFICATES_ONLY_NO_AXIOM_SURFACE_TOUCHED",
             "FINGERPRINT_BOOKKEEPING_NO_RECONSTRUCTION_CLAIM",
             "SIDES_ARE_FIXED_BANKS_NOT_RECORD_LOCALITY",
             "CONFINEMENT_IS_WIRE_COORDINATE_NOT_PHYSICAL_LOCALITY"]
    for name, payload in (("A_SHARDED_CONTENT_REGISTER", cert_a),
                          ("B_SHARD_DAMAGE_INCIDENCE", cert_b),
                          ("C_FINGERPRINT_COVERAGE", cert_c),
                          ("D_SLOT_BUDGET_TRADE", cert_d),
                          ("E_CONTROLS", cert_e)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 877,
        "shard_counts": SHARD_COUNTS,
        "live_payload_wires": live_total,
        "confinement_verdict": cert_b["verdict"]["reading"],
        "any_shard_word_unchanged_direct_classes": direct_any_survive,
        "all_shard_words_unchanged_by_S": {
            str(s): {
                f"{cls}.{side}": coverage[str(s)][f"{cls}.{side}"][
                    "all_shard_words_unchanged"]
                for cls in PERTURBATION_CLASSES for side in SIDES
            }
            for s in SHARD_COUNTS
        },
        "unhit_wire_fraction_by_S": {
            row: marginal[row]["unhit_wire_fraction_by_S"] for row in marginal
        },
        "max_feasible_S_from_pool": max_feasible_s,
        "saturating_S": saturating,
        "finding": finding,
        "runtime_seconds": round(monotonic() - started, 3),
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE877_SHARDED_CONTENT_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
