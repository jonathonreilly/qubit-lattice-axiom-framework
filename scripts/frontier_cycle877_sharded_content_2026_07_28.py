#!/usr/bin/env python3
"""Cycle 877: SHARDED record content -- survival and reconstruction.

Campaign-5 continuation.  Cycle 874 (sha-pinned below) proved that whole-
state copy redundancy does NOT protect record content: at R=1..3, in both
the replicated and staggered modes, no majority-readback cell moved, and
the restore-class near/far contrast decomposed into a pure FIRING gap
(content_gap_given_fired = 0.0).  Its independent checker, attacking that
null with a projection-SHARDED scheme (each copy digesting a different
block of the live state), found the adjacent positive: a surviving shard
under every direct-flip class (any_copy_survives_at_R3 = 1.0 for
one_flip, late_acting and untouched_in_chunk, both sides).

This cycle makes sharding the primary object and asks the four questions
that positive raises.

A. A_SHARDED_CONTENT_REGISTER -- DESIGN AS DATA.  The live payload
   projection (every wire that is not structurally dead) is decomposed
   into S contiguous blocks in ascending wire order, for each declared
   S in {2, 4, 8}; the blocks are derived from the state layout alone and
   their exact boundaries are disclosed.  Each shard is digested to a
   CONTENT_BITS word and written into its OWN structurally-dead slot
   group, with disjointness and structural inertness certified exactly as
   874 does.  Because every slot is a dead wire and the live payload
   excludes all dead wires, the decomposition is independent of S and of
   which safe wires a run happens to allocate.

B. B_SHARD_SURVIVAL_LAW -- WHICH SHARDS DIE.  Under 874's four declared
   perturbation classes (one_flip, late_acting, untouched_in_chunk,
   flip_and_restore), near/far by kernel pack-state bank membership, on
   the same declared 32-lane sample, every probe reports its exact
   DAMAGE SET (the wires on which the perturbed and unperturbed states
   differ after the formation chunk) and the exact per-shard incidence
   matrix.  The candidate law is stated so it can fail: damage is
   confined to the monotone structural forward cone of the perturbation's
   ENTRY DIVERGENCE SET through the formation chunk, so a shard disjoint
   from that cone survives.  Locality versus diffusion is reported as
   data whichever way it falls.

C. C_RECONSTRUCTION -- WHAT IS RECOVERABLE.  Per class and per S: the
   fraction of records whose FULL content is reconstructible from
   surviving shards alone (no host data), the graded fraction of the live
   payload covered by surviving shards, and the marginal value of S
   (does S=4 beat S=2, does S=8 saturate?) against the computed
   saturation limit set by the damage density.

D. D_SLOT_BUDGET_TRADE -- THE COST.  Sharding buys locality with slot
   budget: the exact cost curve (slots used versus S) against the derived
   safe-pool size, and whether the pool bounds S.

E. E_CONTROLS, including reproduction of the sha-pinned 867/874 numbers.

Declared scope: B=2, the 852 census (748 lanes), horizon 16,384 orbits;
dead-wire derivation window 512 orbits chunk-granular then 4,096
orbit-granular; existence register cap 64 wire-visible ordinals per
(tag, lane); shard content word 32 bits; S in {2, 4, 8}; locality sample
32 early-formation lanes with first-clean boundary <= 1,100, up to 4
payload wires per side; cost ladder up to S=256.  All caps disclosed in
the emitted certificates.  Integrity gates are bookkeeping and
mathematical soundness only: the locality-versus-diffuse verdict and the
S-curve are data whichever way they fall.

bounded_theorem, authority none, audit unset.  Independent audit still
required (companion checker spec'd to refute).
"""
from __future__ import annotations

import ast
from hashlib import sha1, sha256
import importlib.abc
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
    "scripts/frontier_cycle874_copy_redundancy_content_2026_07_28.py",
    "scripts/frontier_cycle874_redundancy_independent_check_2026_07_28.py",
)
IMPORTABLE_PATHS = AUDIT_INPUT_PATHS[:2]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[2:]
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "49605f6d0730e224d6c4cd25a182ec49e0c7d2f2316851bc2755632dcbe2c828",
    AUDIT_INPUT_PATHS[3]:
        "02ffdec2e7e2c18b86900a428fd4360ccd54dc62d35e1ef5f72f89a6545439d3",
    AUDIT_INPUT_PATHS[4]:
        "94e1750d48907d3cfc0dea2d521562055f3bfefc140c913a51283f3cf34b8a76",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
    AUDIT_INPUT_PATHS[3]: "7f4c00a5ef5d47db8a0061a34975ff1ce78294fc",
    AUDIT_INPUT_PATHS[4]: "83c5955f2c7fd59bf68e42c77ea63daa472d209a",
}
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PriorFirewall(importlib.abc.MetaPathFinder):
    """The cited 867/874 primaries and the 874 checker are read as
    text/AST only, never imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids prior import: {fullname}")
        return None


PRIOR_FIREWALL = _PriorFirewall()
sys.meta_path.insert(0, PRIOR_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle863_time_from_records_2026_07_28 as C863

# ---- declared scope of this cycle (every cap is emitted below) ----------
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
CONTENT_BITS = 32
SHARD_COUNTS = (2, 4, 8)
LOCALITY_SAMPLE = 32
LOCALITY_BOUNDARY_CAP = 1_100
PAYLOAD_WIRES_PER_SIDE = 4
PERTURBATION_CLASSES = (
    "one_flip", "late_acting", "untouched_in_chunk", "flip_and_restore"
)
COST_LADDER = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
DETERMINISM_LANES = 4
SIDES = ("near", "far")
WORD_MASK = (1 << CONTENT_BITS) - 1
DIGEST_BYTES = (CONTENT_BITS + 7) // 8

# Sha-pinned Cycle-867 v3 / Cycle-874 numbers, reproduced here as controls
# (never physics gates): the landed pool, the landed annotation match, and
# the landed full-state locality cells (probes, fired, content_equal).
LANDED_PRIOR = {
    "dead_wire_count": 5_668,
    "safe_slot_pool": 5_270,
    "moment_exact": 164,
    "annotation_stamps": 164,
    "composed_first_writes": 164,
    "lanes_with_first_slot_bit": 748,
    "locality_cells": {
        "one_flip": {"near": (32, 32, 0), "far": (32, 32, 0)},
        "late_acting": {"near": (13, 13, 0), "far": (25, 25, 0)},
        "untouched_in_chunk": {"near": (19, 19, 0), "far": (15, 15, 0)},
        "flip_and_restore": {"near": (32, 32, 32), "far": (32, 29, 29)},
    },
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
        "importable": IMPORTABLE_PATHS,
        "text_ast_only": TEXT_AST_ONLY_PATHS,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIOR_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_ok"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def true_step_chunks(program, positions):
    """Per-step gate lists on the true trajectory (867 v3's corrected form)."""
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
    marking (867 v3's corrected form)."""
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
    carry one extra wire.  Derived from the state layout alone."""
    size, rem = divmod(len(live), shards)
    blocks, cursor = [], 0
    for idx in range(shards):
        width = size + (1 if idx < rem else 0)
        blocks.append(tuple(live[cursor:cursor + width]))
        cursor += width
    return tuple(blocks)


def shard_word(state, rows) -> int:
    """CONTENT_BITS digest of one shard's block of the LIVE payload.  The
    block contains no slot wire (slots are dead, live excludes dead), so
    the word never reads the register back into itself."""
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
    program, event_seeds, census = C863.derive_census()
    stations = len(program)
    n = len(census)
    states, init_fail = C863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    dup = n
    columns = C863.pack_lanes(states + (states[0],))
    width = len(columns)
    fast = C863.compile_fast(C863.masked_h_schedules(program, sim))
    per_bank, links, source_ptr = C863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1

    # --- Certificate A part 1: the dead-wire safe pool (867 v3 derivation) -
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

    raw_schedules = C863.masked_h_schedules(program, sim)
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
                " carry one extra wire"
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
    columns = C863.pack_lanes(states + (states[0],))
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
        C863.mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    e1_first_composed: dict = {}
    prev_global = C863.mask_over(columns, global_dirty, uni_sim)
    mism = int(bool(prev_global & 1) != bool(prev_global & (1 << dup)))
    for lane in C863.lanes_of(prev_global & uni_all):
        e1_first_composed.setdefault(census[lane], 0)
        wire_write(("G", 0), lane)
        shard_write(lane, C863.lane_state(columns, lane))

    boundary = 0
    getter = columns.__getitem__
    for orbit in range(1, HORIZON + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = C863.mask_over(columns, global_dirty, uni_sim)
            mism += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            for lane in C863.lanes_of(ga):
                if census[lane] not in e1_first_composed:
                    e1_first_composed[census[lane]] = boundary
                    shard_write(lane, C863.lane_state(columns, lane))
            for b in (0, 1):
                bm = C863.mask_over(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in C863.lanes_of(edge):
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
            "horizon_orbits": HORIZON,
            "dead_window_chunk_granular_orbits": DEAD_CHUNK_ORBITS,
            "dead_window_orbit_granular_orbits": DEAD_ORBIT_ORBITS,
            "existence_register_cap_per_tag_lane": REGISTER_CAP,
            "content_bits_per_shard": CONTENT_BITS,
            "shard_counts": SHARD_COUNTS,
        },
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
        "reproduces_landed_pool": (
            len(dead_wires) == LANDED_PRIOR["dead_wire_count"]
            and len(safe_slots_pool) == LANDED_PRIOR["safe_slot_pool"]
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
                    for lane in C863.lanes_of(content_lane_masks[s])
                })
                for shard in range(s)
            ],
        }
        for s in SHARD_COUNTS
    }

    old_h = C863.TRAJECTORY_HORIZON
    C863.TRAJECTORY_HORIZON = HORIZON
    try:
        rep = C863.replay(program, event_seeds, census)
    finally:
        C863.TRAJECTORY_HORIZON = old_h
    anno_e1 = rep["e1_moment"]
    moment_exact = sum(
        1 for key, b in e1_first_composed.items() if anno_e1.get(key) == b
    )
    existence_lane_count = len(
        set(C863.lanes_of(columns[exist_slot[("G", 0)]] & uni_all))
        | set(C863.lanes_of(columns[exist_slot[("B0", 0)]] & uni_all))
        | set(C863.lanes_of(columns[exist_slot[("B1", 0)]] & uni_all))
    )

    # --- Certificate B: the shard survival law under perturbation ---------
    seeds = dict(C863.derive_event_seeds(program))
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
    candidates = sorted(
        (rep["stores"]["global"][lane][0], lane)
        for lane, key in enumerate(census)
        if rep["stores"]["global"][lane]
        and 0 < rep["stores"]["global"][lane][0] <= LOCALITY_BOUNDARY_CAP
    )[:LOCALITY_SAMPLE]

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
        rec_bank = 0 if all(base_after[w] == 0 for w in bank_dirty[0]) else 1
        first_touch: dict = {}
        for idx, gate in enumerate(last_chunk):
            for w in gate.wires:
                first_touch.setdefault(w, idx)
        lane_cells: list = []
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
    localised_cells = []
    diffuse_cells = []
    for s in SHARD_COUNTS:
        for cls in direct_classes:
            for side in SIDES:
                cell = tally[str(s)][cls][side]
                if not cell["fired"]:
                    continue
                if cell["confined_to_flip_shard"] == cell["fired"]:
                    localised_cells.append(f"S{s}.{cls}.{side}")
                if cell["no_shard_survives"] == cell["fired"]:
                    diffuse_cells.append(f"S{s}.{cls}.{side}")
    cert_b = {
        "certificate": "B_SHARD_SURVIVAL_LAW",
        "declared_sample": {
            "lanes": sampled,
            "boundary_cap": LOCALITY_BOUNDARY_CAP,
            "lane_cap": LOCALITY_SAMPLE,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE,
            "classes": PERTURBATION_CLASSES,
            "shard_counts": SHARD_COUNTS,
            "base_not_clean_skips": base_not_clean,
            "degenerate_restore_skips": degenerate_restore_skips,
        },
        "payload_derivation": {
            "pool_size": len(payload_pool),
            "bank_pool_sizes": [len(bank_payload[0]), len(bank_payload[1])],
            "membership": "kernel pack-state single-bit marking",
        },
        "candidate_law": (
            "damage is confined to the monotone structural forward cone of"
            " the perturbation's entry divergence set through the formation"
            " chunk, so a shard disjoint from that cone survives; the cone"
            " is a superset by construction, so cone containment is a"
            " soundness check, while the shard incidence matrix is data"
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
            "cells_with_damage_confined_to_flip_shard": localised_cells,
            "cells_with_no_surviving_shard": diffuse_cells,
            "reading": (
                "LOCAL" if localised_cells and not diffuse_cells
                else "DIFFUSE" if diffuse_cells and not localised_cells
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
        for cell in (tally[str(s)][cls]["near"], tally[str(s)][cls]["far"])
    )
    full_ok = all(
        0 <= cell["content_equal"] <= cell["fired"] <= cell["probes"] <= sampled
        for cls in PERTURBATION_CLASSES
        for cell in (full_state_tally[cls]["near"], full_state_tally[cls]["far"])
    )
    # Integrity gates: bookkeeping consistency, the mathematical soundness
    # of the cone construction, and hash-collision freedom.  The locality
    # verdict and the incidence matrix are never gated.
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

    # --- Certificate C: reconstruction from surviving shards --------------
    reconstruction = {}
    for s in SHARD_COUNTS:
        rows = {}
        for cls in PERTURBATION_CLASSES:
            for side in SIDES:
                cell = tally[str(s)][cls][side]
                rows[f"{cls}.{side}"] = {
                    "fired": cell["fired"],
                    "full_content_reconstructible": ratio(
                        cell["all_shards_survive"], cell["fired"]
                    ),
                    "any_content_reconstructible": ratio(
                        cell["any_shard_survives"], cell["fired"]
                    ),
                    "mean_surviving_shard_fraction": ratio(
                        cell["surviving_shard_count_sum"], cell["fired"] * s
                    ),
                    "mean_recovered_live_wire_fraction": (
                        round(cell["surviving_wire_fraction_sum"]
                              / cell["fired"], 6) if cell["fired"] else None
                    ),
                }
        reconstruction[str(s)] = rows
    marginal = {}
    for cls in PERTURBATION_CLASSES:
        for side in SIDES:
            row = f"{cls}.{side}"
            curve = {
                str(s): reconstruction[str(s)][row][
                    "mean_recovered_live_wire_fraction"]
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
                "recovered_fraction_by_S": curve,
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
                "full_reconstruction_by_S": {
                    str(s): reconstruction[str(s)][row][
                        "full_content_reconstructible"]
                    for s in SHARD_COUNTS
                },
            }
    cert_c = {
        "certificate": "C_RECONSTRUCTION",
        "definitions": (
            "full content reconstructible == every shard's registered word"
            " equals the unperturbed run's word, so the whole live payload"
            " projection is certified from the register alone; recovered"
            " live wire fraction == the share of live wires lying in"
            " surviving shards; both are read from the register with no"
            " host data"
        ),
        "per_shard_count": reconstruction,
        "marginal_value_of_S": marginal,
        "live_payload_wires": live_total,
        "saturation_note": (
            "as S grows the recovered fraction is bounded above by"
            " 1 - damage_density; a plateau at the bound means S has"
            " saturated and further sharding buys nothing"
        ),
    }
    cert_c["pass"] = all(
        (row["full_content_reconstructible"] is None
         or 0.0 <= row["full_content_reconstructible"] <= 1.0)
        and (row["mean_recovered_live_wire_fraction"] is None
             or 0.0 <= row["mean_recovered_live_wire_fraction"] <= 1.0)
        and (row["any_content_reconstructible"] is None
             or row["full_content_reconstructible"] is None
             or row["full_content_reconstructible"]
             <= row["any_content_reconstructible"])
        for s in SHARD_COUNTS for row in reconstruction[str(s)].values()
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
    # The saturating S: one live wire per shard is the finest decomposition
    # the payload admits, and by the measured damage law it is the S at
    # which the recovered fraction reaches its bound.  Derived, not declared.
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
        "recovered_fraction_gain_per_slot": efficiency,
        "structural_note": (
            "slots are drawn from the structurally-dead safe pool and the"
            " live payload excludes every dead wire, so raising S spends"
            " slot budget without shrinking the payload being sharded;"
            " the pool is the only budget the trade touches"
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
    landed_cells = {
        cls: {side: (full_state_tally[cls][side]["probes"],
                     full_state_tally[cls][side]["fired"],
                     full_state_tally[cls][side]["content_equal"])
              for side in SIDES}
        for cls in PERTURBATION_CLASSES
    }
    reproduction = {
        "pool": cert_a["reproduces_landed_pool"],
        "annotation": (
            moment_exact == LANDED_PRIOR["moment_exact"]
            and len(anno_e1) == LANDED_PRIOR["annotation_stamps"]
            and len(e1_first_composed) == LANDED_PRIOR["composed_first_writes"]
            and existence_lane_count == LANDED_PRIOR["lanes_with_first_slot_bit"]
        ),
        "locality_cells": landed_cells == LANDED_PRIOR["locality_cells"],
        "observed_locality_cells": landed_cells,
        "observed_annotation": {
            "moment_exact": moment_exact,
            "annotation_stamps": len(anno_e1),
            "composed_first_writes": len(e1_first_composed),
            "lanes_with_first_slot_bit": existence_lane_count,
        },
    }
    reproduction["pass"] = all(
        reproduction[k] for k in ("pool", "annotation", "locality_cells")
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
        "initial_state_failures": init_fail,
        "duplicate_lane_mismatches": mism,
        "replay_mismatches": rep["mismatches"],
        "shard_readback_host_mismatches": readback_mismatches,
        "shard_words_written": len(host_words),
        "landed_prior_reproduction": reproduction,
        "determinism": determinism,
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
    }
    cert_e["pass"] = bool(
        controls["pass"] and init_fail == 0 and mism == 0
        and rep["mismatches"] == 0 and readback_mismatches == 0
        and len(host_words) > 0 and reproduction["pass"]
        and determinism["pass"] and runtime < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "A_SHARDED_CONTENT_REGISTER": cert_a["pass"],
        "B_SHARD_SURVIVAL_LAW": cert_b["pass"],
        "C_RECONSTRUCTION": cert_c["pass"],
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
        "sharded record content: the incidence matrix says damage kills "
        + compact({
            str(s): {
                f"{cls}.{side}": incidence[str(s)][f"{cls}.{side}"][
                    "mean_shards_dead_given_fired"]
                for cls in direct_classes for side in SIDES
            }
            for s in SHARD_COUNTS
        })
        + f" shards of S on the direct-flip classes; locality verdict "
        + f"{cert_b['verdict']['reading']}"
        + f" (confined-to-flip-shard cells: {len(localised_cells)}, "
        + f"no-survivor cells: {len(diffuse_cells)});"
        + " full-content reconstruction from surviving shards alone = "
        + compact({
            str(s): {
                f"{cls}.{side}": reconstruction[str(s)][f"{cls}.{side}"][
                    "full_content_reconstructible"]
                for cls in direct_classes for side in SIDES
            }
            for s in SHARD_COUNTS
        })
        + "; mean damage wires given fired on the direct classes = "
        + compact({
            f"{cls}.{side}":
                damage_reading[f"{cls}.{side}"]["mean_damage_wires_given_fired"]
            for cls in direct_classes for side in SIDES
        })
        + f" of {live_total} live wires; the safe pool admits S<="
        + f"{max_feasible_s} while the payload saturates at S={live_total}"
        + f" (binding constraint: {saturating['binding_constraint']},"
        + f" cost {saturating['fraction_of_safe_pool']} of the pool)"
    )
    lines = ["CYCLE877_SHARDED_CONTENT",
             "CAMPAIGN5_CONTENT_ROBUSTNESS_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("A_SHARDED_CONTENT_REGISTER", cert_a),
                          ("B_SHARD_SURVIVAL_LAW", cert_b),
                          ("C_RECONSTRUCTION", cert_c),
                          ("D_SLOT_BUDGET_TRADE", cert_d),
                          ("E_CONTROLS", cert_e)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 877,
        "shard_counts": SHARD_COUNTS,
        "live_payload_wires": live_total,
        "locality_verdict": cert_b["verdict"]["reading"],
        "any_shard_survives_direct_classes": direct_any_survive,
        "full_content_reconstructible_by_S": {
            str(s): {
                f"{cls}.{side}": reconstruction[str(s)][f"{cls}.{side}"][
                    "full_content_reconstructible"]
                for cls in PERTURBATION_CLASSES for side in SIDES
            }
            for s in SHARD_COUNTS
        },
        "recovered_fraction_by_S": {
            row: marginal[row]["recovered_fraction_by_S"] for row in marginal
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
