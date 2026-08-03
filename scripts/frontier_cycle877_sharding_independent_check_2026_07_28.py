#!/usr/bin/env python3
"""Cycle 877 sharded content: INDEPENDENT ADVERSARIAL CHECKER.

Isolated re-implementation, spec'd to REFUTE.  The 877 primary, the 874
primary and checker it extends, the 867 primary and the 863 replay
substrate are all BLOCKLISTED at import: they are read as text/AST only.
Every number below is re-derived from the pinned Cycle-719 kernel alone,
with this checker's own census, own dirty partition, own dead-wire
derivation, own live-payload set, own shard-boundary derivations, own
slot allocator, own composed scan and own perturbation probe.

Deliberate divergences from the primary, so that agreement cannot come
from sharing an implementation:

  * SHARD BOUNDARIES.  The primary slices the live wire list into
    contiguous blocks.  This checker derives shard membership by ARITHMETIC
    RANK MAP instead of slicing, and carries two further rules the primary
    never builds: STRIDED (rank mod S) and HASH_SCATTERED (a sha256 of the
    wire index mod S).  Those two scatter shard membership across the whole
    payload, so if the primary's survival law is an artefact of contiguous
    blocks it must break here.
  * SLOT ALLOCATOR.  The primary walks the safe pool from the front,
    existence tags first.  This checker walks it from the FAR END, content
    groups first, with the shard counts in reverse order.

Attacks:
  THE_SHARDED_REGISTER -- own pool, own live payload, own decompositions
      under all three rules, disjointness and structural inertness for
      every shard group, own composed scan, own readback.
  THE_LOCALITY_PROBE -- own four declared perturbation classes near/far,
      own damage sets, own monotone structural forward cones, own
      incidence matrix, compared CELL FOR CELL with the primary's pinned
      claim.
  THE_BOUNDARY_ATTACK -- the refutation attempt.  (a) The same probes
      re-scored under the strided and hash-scattered decompositions: does
      a surviving shard depend on where the boundaries fall?  (b) An
      EXHAUSTIVE single-flip sweep over the payload wires of a lane
      subsample, including every wire adjacent to a contiguous block
      boundary, searching for one flip that kills more than one shard or
      leaves no survivor.  (c) k-WIRE flips placed in k distinct shards,
      for k in the declared ladder, pricing how much adversarial power it
      takes to defeat sharding at all.  Refutation is confined to what the
      primary actually claims: a cone-law violation (the primary states
      that law universally) or a cell-for-cell mismatch on the declared
      classes.  The sweep runs wires and the k-flips run perturbations the
      primary never declared, so their outcomes PRICE THE SCOPE of the
      survival law and are reported whichever way they fall.
  THE_SCOPE_AUDIT -- AST over the primary: every declared cap constant
      must flow into an emitted certificate payload, and the certificate
      pass-gates must not reference the objects that carry the locality
      verdict, the incidence matrix or the S-curve.
  CONTROLS -- shas, blocklist, determinism, paths, runtime, stdout.

Declared probe of this checker (complete): B=2, k=2..5 census (748
lanes), horizon 16,384 orbits, dead-wire window 512 orbits chunk-granular
then 4,096 orbit-granular, existence register cap 64 per (tag, lane),
shard content word 32 bits, S in {2, 4, 8} under three boundary rules,
locality sample 32 lanes with first-clean boundary <= 1,100, 4 payload
wires per side, adversarial sweep over 12 of those lanes and up to 64
payload wires each, k-wire flips for k in {2, 4, 8} at three independent
wire-tuple offsets each.

bounded_theorem, authority none, audit unset.
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
    "scripts/frontier_cycle874_copy_redundancy_content_2026_07_28.py",
    "scripts/frontier_cycle874_redundancy_independent_check_2026_07_28.py",
    "scripts/frontier_cycle877_sharded_content_2026_07_28.py",
)
KERNEL_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_PATH = AUDIT_INPUT_PATHS[5]
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
        "02ffdec2e7e2c18b86900a428fd4360ccd54dc62d35e1ef5f72f89a6545439d3",
    AUDIT_INPUT_PATHS[4]:
        "94e1750d48907d3cfc0dea2d521562055f3bfefc140c913a51283f3cf34b8a76",
    AUDIT_INPUT_PATHS[5]:
        "2cbb9314ac8b74ac465f6552e2363f43be64efa36cb0f5c4591ccf06b2e61dd3",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
    AUDIT_INPUT_PATHS[3]: "7f4c00a5ef5d47db8a0061a34975ff1ce78294fc",
    AUDIT_INPUT_PATHS[4]: "83c5955f2c7fd59bf68e42c77ea63daa472d209a",
    AUDIT_INPUT_PATHS[5]: "bf03b74421462fba32eb8fd4061d188e1c13c9ab",
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
SHARD_COUNTS = (2, 4, 8)
RULES = ("contiguous", "strided", "hash_scattered")
LOC_LANE_CAP = 32
LOC_BOUNDARY_CAP = 1_100
PAYLOAD_WIRES_PER_SIDE = 4
CLASSES = ("one_flip", "late_acting", "untouched_in_chunk",
           "flip_and_restore")
SIDES = ("near", "far")
ADVERSARIAL_LANE_CAP = 12
ADVERSARIAL_WIRE_CAP = 64
MULTI_FLIP_K = (2, 4, 8)
MULTI_FLIP_OFFSETS = (0, 1, -1)
WORD_MASK = (1 << CONTENT_BITS) - 1
DIGEST_BYTES = (CONTENT_BITS + 7) // 8

# ---- the primary's declared numbers, reproduced or refuted here --------
_INCIDENCE = {
    "2": {
        "one_flip.near": [32, 0], "one_flip.far": [0, 32],
        "late_acting.near": [13, 0], "late_acting.far": [0, 25],
        "untouched_in_chunk.near": [19, 0], "untouched_in_chunk.far": [0, 15],
        "flip_and_restore.near": [0, 0], "flip_and_restore.far": [0, 0],
    },
    "4": {
        "one_flip.near": [32, 0, 0, 0], "one_flip.far": [0, 0, 32, 0],
        "late_acting.near": [13, 0, 0, 0], "late_acting.far": [0, 0, 25, 0],
        "untouched_in_chunk.near": [19, 0, 0, 0],
        "untouched_in_chunk.far": [0, 0, 15, 0],
        "flip_and_restore.near": [0, 0, 0, 0],
        "flip_and_restore.far": [0, 0, 0, 0],
    },
    "8": {
        "one_flip.near": [32, 0, 0, 0, 0, 0, 0, 0],
        "one_flip.far": [0, 0, 0, 32, 0, 0, 0, 0],
        "late_acting.near": [13, 0, 0, 0, 0, 0, 0, 0],
        "late_acting.far": [0, 0, 0, 0, 25, 0, 0, 0],
        "untouched_in_chunk.near": [19, 0, 0, 0, 0, 0, 0, 0],
        "untouched_in_chunk.far": [0, 0, 0, 15, 0, 0, 0, 0],
        "flip_and_restore.near": [0] * 8, "flip_and_restore.far": [0] * 8,
    },
}
_FIRED = {
    "one_flip.near": (32, 32), "one_flip.far": (32, 32),
    "late_acting.near": (13, 13), "late_acting.far": (25, 25),
    "untouched_in_chunk.near": (19, 19), "untouched_in_chunk.far": (15, 15),
    "flip_and_restore.near": (32, 32), "flip_and_restore.far": (32, 29),
}
_DAMAGE_GIVEN_FIRED = {
    "one_flip.near": 1.0, "one_flip.far": 1.0,
    "late_acting.near": 1.0, "late_acting.far": 1.0,
    "untouched_in_chunk.near": 1.0, "untouched_in_chunk.far": 1.0,
    "flip_and_restore.near": 0.0, "flip_and_restore.far": 0.0,
}
_RECOVERED = {
    "one_flip.near": {"2": 0.496599, "4": 0.748299, "8": 0.870748},
    "one_flip.far": {"2": 0.503401, "4": 0.748299, "8": 0.877551},
    "late_acting.near": {"2": 0.496599, "4": 0.748299, "8": 0.870748},
    "late_acting.far": {"2": 0.503401, "4": 0.748299, "8": 0.877551},
    "untouched_in_chunk.near": {"2": 0.496599, "4": 0.748299, "8": 0.870748},
    "untouched_in_chunk.far": {"2": 0.503401, "4": 0.748299, "8": 0.877551},
    "flip_and_restore.near": {"2": 1.0, "4": 1.0, "8": 1.0},
    "flip_and_restore.far": {"2": 1.0, "4": 1.0, "8": 1.0},
}
CLAIM_877 = {
    "state_width": 5_815,
    "dead_wire_count": 5_668,
    "live_payload_wires": 147,
    "safe_slot_pool": 5_270,
    "slot_tags": 577,
    "pairwise_shard_group_overlaps": 0,
    "content_existence_overlap": 0,
    "slots_in_gate_inputs": 0,
    "slots_in_gate_targets": 0,
    "slots_disjoint_from_live_payload": 0,
    "dead_activation_conflicts": 0,
    "block_sizes": {
        "2": [74, 73], "4": [37, 37, 37, 36],
        "8": [19, 19, 19, 18, 18, 18, 18, 18],
    },
    "block_first_wire": {
        "2": [1, 172], "4": [1, 85, 172, 219],
        "8": [1, 62, 86, 115, 173, 201, 219, 247],
    },
    "locality_lanes": 32,
    "probes_fired": _FIRED,
    "shard_deaths_contiguous": _INCIDENCE,
    "mean_damage_wires_given_fired": _DAMAGE_GIVEN_FIRED,
    "recovered_fraction_by_S": _RECOVERED,
    "full_reconstruction_direct_classes": 0.0,
    "locality_verdict": "LOCAL",
    "confined_to_flip_shard_direct": 1.0,
    "max_feasible_S_from_pool": 160,
    "saturating_S": 147,
}
DECLARED_CAPS = (
    "HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
    "CONTENT_BITS", "SHARD_COUNTS", "LOCALITY_SAMPLE",
    "LOCALITY_BOUNDARY_CAP", "PAYLOAD_WIRES_PER_SIDE",
    "PERTURBATION_CLASSES", "COST_LADDER", "DETERMINISM_LANES",
    "AUDIT_TIMEOUT_SEC",
)
GATE_ROOTS = ("cert_a", "cert_b", "cert_c", "cert_d", "cert_e")
DISCLOSURE_ROOTS = GATE_ROOTS + ("summary", "finding")
GATE_MUST_NOT_REFERENCE = (
    "incidence", "marginal", "damage_reading", "localised_cells",
    "diffuse_cells", "direct_any_survive", "finding", "LANDED_PRIOR",
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


def word_of(payload_bytes) -> int:
    return int.from_bytes(
        sha256(payload_bytes).digest()[:DIGEST_BYTES], "big"
    ) & WORD_MASK


def shard_word(state, rows) -> int:
    return word_of(bytes(bytearray(state[w] for w in rows)))


# ---- THREE shard-boundary derivations -----------------------------------
def rank_to_shard(rule, rank, total, shards):
    """Shard index of the live wire at `rank`, by arithmetic map.

    contiguous     -- the primary's declared rule, derived here by
                      arithmetic rather than by slicing the list.
    strided        -- rank mod S: every block's wires are spread across the
                      whole payload, so contiguity cannot be doing the work.
    hash_scattered -- sha256 of the rank, mod S: a pseudo-random partition.
    """
    if rule == "contiguous":
        size, rem = divmod(total, shards)
        big = rem * (size + 1)
        if rank < big:
            return rank // (size + 1)
        return rem + (rank - big) // size
    if rule == "strided":
        return rank % shards
    return int.from_bytes(
        sha256(str(rank).encode("ascii")).digest()[:8], "big"
    ) % shards


def decompositions(live):
    total = len(live)
    out = {}
    for rule in RULES:
        for s in SHARD_COUNTS:
            groups: list = [[] for _ in range(s)]
            for rank, wire in enumerate(live):
                groups[rank_to_shard(rule, rank, total, s)].append(wire)
            out[(rule, s)] = tuple(tuple(g) for g in groups)
    return out


def forward_cone(chunk, seed_wires):
    """Monotone structural forward cone: X cannot create a difference,
    CNOT carries a difference from its control to its target, Toffoli from
    either control to its target.  Membership is only added, so the result
    is a superset of the true post-chunk difference set."""
    cone = set(seed_wires)
    for gate in chunk:
        w = gate.wires
        if gate.kind == "X":
            continue
        if gate.kind == "CNOT":
            if w[0] in cone:
                cone.add(w[1])
        elif w[0] in cone or w[1] in cone:
            cone.add(w[2])
    return cone


# ---- ATTACK 1: THE_SHARDED_REGISTER -------------------------------------
def attack_register(ctx):
    program = ctx["program"]
    census = ctx["census"]
    n = len(census)
    sim = census + (census[0],)
    columns = pack_columns(ctx["states"] + (ctx["states"][0],))
    width = len(columns)
    fast = ctx["fast"]
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1

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
    dead = tuple(w for w in range(width) if (acc[w] & uni_sim) == 0)
    dead_set = set(dead)
    live = tuple(w for w in range(width) if w not in dead_set)

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
    pool = tuple(w for w in dead if w not in inputs and w not in targets)

    blocks = decompositions(live)
    # DIFFERENT ALLOCATOR: content groups first, shard counts in reverse,
    # rules in reverse, and the safe pool walked from the FAR END.
    content_tags = [
        (rule, s, shard, bit)
        for rule in reversed(RULES)
        for s in reversed(SHARD_COUNTS)
        for shard in range(s)
        for bit in range(CONTENT_BITS)
    ]
    exist_tags = [("G", 0)] + [
        (f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    need = len(content_tags) + len(exist_tags)
    if len(pool) < need:
        raise AssertionError(("insufficient safe slots", len(pool), need))
    rev = list(reversed(pool))
    content_slot = {tag: rev[i] for i, tag in enumerate(content_tags)}
    exist_slot = {
        tag: rev[len(content_tags) + i] for i, tag in enumerate(exist_tags)
    }
    slot_wires = set(content_slot.values()) | set(exist_slot.values())
    groups = {
        (rule, s, shard): frozenset(
            content_slot[(rule, s, shard, bit)] for bit in range(CONTENT_BITS)
        )
        for rule in RULES for s in SHARD_COUNTS for shard in range(s)
    }
    keys = sorted(groups)
    overlaps = sum(
        len(groups[a] & groups[b])
        for i, a in enumerate(keys) for b in keys[i + 1:]
    )
    content_all = frozenset().union(*groups.values())

    # own composed scan with real shard writes
    columns = pack_columns(ctx["states"] + (ctx["states"][0],))
    nonslot_dead = tuple(w for w in dead if w not in slot_wires)
    getter = columns.__getitem__
    written = {key: 0 for key in groups}
    host: dict = {}
    write_once = 0
    dead_conflicts = 0
    exist_writes = 0
    ordinal = [[0, 0] for _ in range(n)]

    def shard_write(lane, state):
        nonlocal write_once
        bit = 1 << lane
        for rule in RULES:
            for s in SHARD_COUNTS:
                for shard in range(s):
                    key = (rule, s, shard)
                    if written[key] & bit:
                        write_once += 1
                    written[key] |= bit
                    word = shard_word(state, blocks[(rule, s)][shard])
                    for j in range(CONTENT_BITS):
                        if (word >> j) & 1:
                            columns[content_slot[(rule, s, shard, j)]] |= bit
                    host[(rule, s, shard, lane)] = word

    def mask_over(indices, universe):
        dirty = 0
        for w in indices:
            dirty |= columns[w]
        return universe & ~dirty

    global_dirty = ctx["global_dirty"]
    bank_dirty = ctx["bank_dirty"]
    prev_bank = [mask_over(bank_dirty[b], uni_all) for b in (0, 1)]
    first_moment: dict = {}
    prev_global = mask_over(global_dirty, uni_sim)
    dup_mismatch = int(bool(prev_global & 1) != bool(prev_global & (1 << n)))
    for lane in lanes_of(prev_global & uni_all):
        first_moment.setdefault(census[lane], 0)
        columns[exist_slot[("G", 0)]] |= 1 << lane
        exist_writes += 1
        shard_write(lane, lane_state(columns, lane))
    boundary = 0
    for _orbit in range(HORIZON):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = mask_over(global_dirty, uni_sim)
            dup_mismatch += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            for lane in lanes_of(ga):
                if census[lane] not in first_moment:
                    first_moment[census[lane]] = boundary
                    shard_write(lane, lane_state(columns, lane))
            for b in (0, 1):
                bm = mask_over(bank_dirty[b], uni_all)
                for lane in lanes_of(bm & ~prev_bank[b]):
                    if ordinal[lane][b] < REGISTER_CAP:
                        columns[exist_slot[(f"B{b}", ordinal[lane][b])]] |= (
                            1 << lane
                        )
                        exist_writes += 1
                    ordinal[lane][b] += 1
                prev_bank[b] = bm
            if any(map(getter, nonslot_dead)):
                dead_conflicts += 1

    readback_mismatch = 0
    for (rule, s, shard, lane), word in host.items():
        bit = 1 << lane
        got = sum(
            ((columns[content_slot[(rule, s, shard, j)]] & bit) != 0) << j
            for j in range(CONTENT_BITS)
        )
        readback_mismatch += int(got != word)

    observed = {
        "state_width": width,
        "dead_wire_count": len(dead),
        "live_payload_wires": len(live),
        "safe_slot_pool": len(pool),
        # the primary allocates ONE rule; this checker allocates three, so
        # only the per-rule count is comparable
        "slot_tags": len(exist_tags) + sum(SHARD_COUNTS) * CONTENT_BITS,
        "pairwise_shard_group_overlaps": overlaps,
        "content_existence_overlap": len(
            content_all & frozenset(exist_slot.values())
        ),
        "slots_in_gate_inputs": len(slot_wires & inputs),
        "slots_in_gate_targets": len(slot_wires & targets),
        "slots_disjoint_from_live_payload": len(slot_wires & set(live)),
        "dead_activation_conflicts": dead_conflicts,
        "block_sizes": {
            str(s): [len(b) for b in blocks[("contiguous", s)]]
            for s in SHARD_COUNTS
        },
        "block_first_wire": {
            str(s): [b[0] for b in blocks[("contiguous", s)]]
            for s in SHARD_COUNTS
        },
    }
    refutations = [
        f"register.{k}: primary={CLAIM_877[k]} checker={v}"
        for k, v in observed.items()
        if k in CLAIM_877 and CLAIM_877[k] != v
    ]
    ctx.update({
        "dead_set": dead_set, "live": live, "blocks": blocks,
        "width": width, "first_moment": first_moment,
        "scan_words": {
            lane: host[("contiguous", SHARD_COUNTS[-1], 0, lane)]
            for (rule, s, shard, lane) in host
            if rule == "contiguous" and s == SHARD_COUNTS[-1] and shard == 0
        },
        "duplicate_mismatches": dup_mismatch,
        "safe_pool_size": len(pool),
    })
    result = {
        "attack": "THE_SHARDED_REGISTER",
        "allocator": (
            "content groups first, rules and shard counts in reverse, the"
            " safe pool walked from the far end -- a different allocation"
            " from the primary's, so agreement cannot come from sharing it"
        ),
        "boundary_rules": RULES,
        "observed": observed,
        "checker_total_slot_tags_all_three_rules": need,
        "shard_groups": len(groups),
        "existence_writes": exist_writes,
        "shard_words_written": len(host),
        "write_once_violations": write_once,
        "readback_host_mismatches": readback_mismatch,
        "strided_block_sizes": {
            str(s): [len(b) for b in blocks[("strided", s)]]
            for s in SHARD_COUNTS
        },
        "hash_scattered_block_sizes": {
            str(s): [len(b) for b in blocks[("hash_scattered", s)]]
            for s in SHARD_COUNTS
        },
        "refutations": refutations,
    }
    result["pass"] = (
        not refutations and readback_mismatch == 0 and write_once == 0
        and overlaps == 0 and dead_conflicts == 0
        and len(slot_wires & inputs) == 0 and len(slot_wires & targets) == 0
        and len(slot_wires & set(live)) == 0
        and all(
            sum(len(b) for b in blocks[(rule, s)]) == len(live)
            and all(len(b) > 0 for b in blocks[(rule, s)])
            for rule in RULES for s in SHARD_COUNTS
        )
    )
    return result


# ---- shared probe machinery ---------------------------------------------
def probe_common(ctx):
    program = ctx["program"]
    stations = len(program)
    global_dirty = ctx["global_dirty"]
    dead_set = ctx["dead_set"]
    payload_pool = [
        w for w in range(ctx["width"])
        if w not in dead_set and w not in set(global_dirty)
    ]
    rows = partition(BANKS)["full_bank"]
    bank_payload = {
        b: [w for w in payload_pool if w in rows[b]] for b in (0, 1)
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

    ctx.update({
        "stations": stations, "bank_payload": bank_payload,
        "chunks_for": chunks_for, "clean": clean,
        "payload_pool": payload_pool,
    })
    return ctx


def lane_setup(ctx, first, lane):
    """Walk one candidate lane to its formation edge; returns the state
    entering the formation chunk, the chunk, and the unperturbed exit."""
    census = ctx["census"]
    key = census[lane]
    chunks_t = ctx["chunks_for"](key[2])
    stations = ctx["stations"]
    state, _a, _b, _t = K.run_orbit(ctx["seeds"][key[1]], ctx["program"],
                                    token_positions=key[2])
    for b in range(first - 1):
        state = K.A.apply_semantic(state, chunks_t[b % stations])
    last_chunk = chunks_t[(first - 1) % stations]
    return key, chunks_t, state, last_chunk, K.A.apply_semantic(
        state, last_chunk)


def score(ctx, pre, entry, after, base_after, last_chunk):
    """Damage set, entry divergence, cone, and per-(rule, S) death sets."""
    width = ctx["width"]
    entry_div = tuple(w for w in range(width) if entry[w] != pre[w])
    cone = forward_cone(last_chunk, entry_div)
    dmg = set(w for w in range(width) if after[w] != base_after[w])
    deaths = {}
    for rule in RULES:
        for s in SHARD_COUNTS:
            blk = ctx["blocks"][(rule, s)]
            deaths[(rule, s)] = frozenset(
                i for i in range(s) if dmg.intersection(blk[i])
            )
    return {"entry_divergence": entry_div, "cone": cone, "damage": dmg,
            "deaths": deaths}


# ---- ATTACK 2: THE_LOCALITY_PROBE ---------------------------------------
def attack_probe(ctx):
    census = ctx["census"]
    stations = ctx["stations"]
    clean = ctx["clean"]
    bank_dirty = ctx["bank_dirty"]
    live_total = len(ctx["live"])
    cells = {
        rule: {str(s): {f"{cls}.{side}": {
            "probes": 0, "fired": 0, "deaths": [0] * s,
            "any_survives": 0, "all_survive": 0, "confined": 0,
            "recovered_sum": 0.0, "law_violations": 0, "word_mismatch": 0}
            for cls in CLASSES for side in SIDES}
            for s in SHARD_COUNTS}
        for rule in RULES
    }
    dmg_stats = {
        f"{cls}.{side}": {"probes": 0, "fired": 0, "fired_size_sum": 0,
                          "size_max": 0, "cone_max": 0, "in_cone": 0,
                          "has_flip": 0}
        for cls in CLASSES for side in SIDES
    }
    stats = {"sampled": 0, "base_not_clean": 0, "restore_skips": 0,
             "scan_agree": 0, "scan_checked": 0}
    lanes_used = []
    for first, lane in ctx["candidates"]:
        key, chunks_t, pre, last_chunk, base_after = lane_setup(
            ctx, first, lane)
        if not clean(base_after):
            stats["base_not_clean"] += 1
            continue
        stats["sampled"] += 1
        lanes_used.append((first, lane, pre, last_chunk, base_after, chunks_t,
                           key))
        if lane in ctx["scan_words"]:
            stats["scan_checked"] += 1
            stats["scan_agree"] += int(
                ctx["scan_words"][lane]
                == shard_word(base_after,
                              ctx["blocks"][("contiguous", SHARD_COUNTS[-1])][0])
            )
        base_words = {
            (rule, s): [
                shard_word(base_after, ctx["blocks"][(rule, s)][i])
                for i in range(s)
            ]
            for rule in RULES for s in SHARD_COUNTS
        }
        rec_bank = 0 if all(base_after[w] == 0 for w in bank_dirty[0]) else 1
        first_touch: dict = {}
        for idx, gate in enumerate(last_chunk):
            for w in gate.wires:
                first_touch.setdefault(w, idx)
        for side, bank in (("near", rec_bank), ("far", 1 - rec_bank)):
            pool = ctx["bank_payload"][bank][:PAYLOAD_WIRES_PER_SIDE]
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
                    ws, _x, _y, _z = K.run_orbit(
                        ctx["seeds"][key[1]], ctx["program"],
                        token_positions=key[2])
                    fl = list(ws)
                    fl[wire] ^= 1
                    ws = tuple(fl)
                    for b in range(first - 1):
                        ws = K.A.apply_semantic(ws, chunks_t[b % stations])
                    rs = list(ws)
                    rs[wire] ^= 1
                    entry = tuple(rs)
                else:
                    mut = list(pre)
                    mut[wire] ^= 1
                    entry = tuple(mut)
                after = K.A.apply_semantic(entry, last_chunk)
                fired = clean(after)
                sc = score(ctx, pre, entry, after, base_after, last_chunk)
                row = f"{cls}.{side}"
                ds = dmg_stats[row]
                ds["probes"] += 1
                ds["fired"] += int(fired)
                ds["size_max"] = max(ds["size_max"], len(sc["damage"]))
                ds["cone_max"] = max(ds["cone_max"], len(sc["cone"]))
                ds["in_cone"] += int(sc["damage"] <= sc["cone"])
                ds["has_flip"] += int(wire in sc["damage"])
                if fired:
                    ds["fired_size_sum"] += len(sc["damage"])
                for rule in RULES:
                    for s in SHARD_COUNTS:
                        cell = cells[rule][str(s)][row]
                        cell["probes"] += 1
                        cell["fired"] += int(fired)
                        if not fired:
                            continue
                        dead = sc["deaths"][(rule, s)]
                        blk = ctx["blocks"][(rule, s)]
                        by_word = frozenset(
                            i for i in range(s)
                            if shard_word(after, blk[i]) != base_words[
                                (rule, s)][i]
                        )
                        cell["word_mismatch"] += int(by_word != dead)
                        for i in dead:
                            cell["deaths"][i] += 1
                        survivors = [i for i in range(s) if i not in dead]
                        cell["any_survives"] += int(bool(survivors))
                        cell["all_survive"] += int(not dead)
                        cell["recovered_sum"] += (
                            sum(len(blk[i]) for i in survivors) / live_total
                        )
                        flip_shard = next(
                            i for i in range(s) if wire in set(blk[i])
                        )
                        cell["confined"] += int(dead <= {flip_shard})
                        predicted = {
                            i for i in range(s)
                            if sc["cone"].intersection(blk[i])
                        }
                        cell["law_violations"] += int(not dead <= predicted)
    ctx["lanes_used"] = lanes_used

    def rnd(num, den):
        return round(num / den, 6) if den else None

    observed = {
        "locality_lanes": stats["sampled"],
        "probes_fired": {
            row: (dmg_stats[row]["probes"], dmg_stats[row]["fired"])
            for row in dmg_stats
        },
        "shard_deaths_contiguous": {
            str(s): {row: cells["contiguous"][str(s)][row]["deaths"]
                     for row in dmg_stats}
            for s in SHARD_COUNTS
        },
        "mean_damage_wires_given_fired": {
            row: rnd(dmg_stats[row]["fired_size_sum"], dmg_stats[row]["fired"])
            for row in dmg_stats
        },
        "recovered_fraction_by_S": {
            row: {
                str(s): rnd(cells["contiguous"][str(s)][row]["recovered_sum"],
                            cells["contiguous"][str(s)][row]["fired"])
                for s in SHARD_COUNTS
            }
            for row in dmg_stats
        },
    }
    refutations = [
        f"probe.{k}: primary={compact(CLAIM_877[k])} checker={compact(v)}"
        for k, v in observed.items()
        if k in CLAIM_877 and CLAIM_877[k] != v
    ]
    direct = [f"{cls}.{side}" for cls in CLASSES for side in SIDES
              if cls != "flip_and_restore"]
    confined = {
        str(s): {
            row: rnd(cells["contiguous"][str(s)][row]["confined"],
                     cells["contiguous"][str(s)][row]["fired"])
            for row in direct
        }
        for s in SHARD_COUNTS
    }
    full_recon = {
        str(s): {
            row: rnd(cells["contiguous"][str(s)][row]["all_survive"],
                     cells["contiguous"][str(s)][row]["fired"])
            for row in direct
        }
        for s in SHARD_COUNTS
    }
    if any(v != CLAIM_877["confined_to_flip_shard_direct"]
           for rows in confined.values() for v in rows.values()):
        refutations.append(
            "probe.confined_to_flip_shard: primary claims "
            f"{CLAIM_877['confined_to_flip_shard_direct']} checker="
            + compact(confined)
        )
    if any(v != CLAIM_877["full_reconstruction_direct_classes"]
           for rows in full_recon.values() for v in rows.values()):
        refutations.append(
            "probe.full_reconstruction_direct: primary claims "
            f"{CLAIM_877['full_reconstruction_direct_classes']} checker="
            + compact(full_recon)
        )
    cone_failures = sum(
        d["probes"] - d["in_cone"] for d in dmg_stats.values()
    )
    if cone_failures:
        refutations.append(
            f"cone law violated on {cone_failures} probes: damage escaped"
            " the monotone structural forward cone"
        )
    law_violations = sum(
        cells[rule][str(s)][row]["law_violations"]
        for rule in RULES for s in SHARD_COUNTS for row in dmg_stats
    )
    if law_violations:
        refutations.append(
            f"{law_violations} shard deaths outside the cone prediction"
        )
    word_mismatch = sum(
        cells[rule][str(s)][row]["word_mismatch"]
        for rule in RULES for s in SHARD_COUNTS for row in dmg_stats
    )
    ctx["cells"] = cells
    result = {
        "attack": "THE_LOCALITY_PROBE",
        "declared_sample": {
            "lanes": stats["sampled"], "lane_cap": LOC_LANE_CAP,
            "boundary_cap": LOC_BOUNDARY_CAP,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE, "classes": CLASSES,
            "shard_counts": SHARD_COUNTS,
            "base_not_clean_skips": stats["base_not_clean"],
            "degenerate_restore_skips": stats["restore_skips"],
        },
        "observed": observed,
        "confined_to_flip_shard_direct": confined,
        "full_reconstruction_direct": full_recon,
        "damage_statistics": dmg_stats,
        "cone_containment_failures": cone_failures,
        "cone_prediction_violations": law_violations,
        "digest_vs_bits_disagreements": word_mismatch,
        "scan_vs_probe_shard_word":
            f"{stats['scan_agree']}/{stats['scan_checked']}",
        "refutations": refutations,
    }
    result["pass"] = (
        stats["sampled"] > 0 and not refutations and word_mismatch == 0
        and stats["scan_checked"] > 0
        and stats["scan_agree"] == stats["scan_checked"]
    )
    return result


# ---- ATTACK 3: THE_BOUNDARY_ATTACK --------------------------------------
def attack_boundary(ctx):
    """The refutation attempt: break the survival law by moving the
    boundaries and by placing the flip adversarially."""
    clean = ctx["clean"]
    live = ctx["live"]
    live_total = len(live)
    rank_of = {w: r for r, w in enumerate(live)}
    payload = ctx["payload_pool"]

    # (a) the declared probes, re-scored under every boundary rule
    boundary_sensitivity = {}
    direct = [f"{cls}.{side}" for cls in CLASSES for side in SIDES
              if cls != "flip_and_restore"]
    for rule in RULES:
        rows = {}
        for s in SHARD_COUNTS:
            cells = ctx["cells"][rule][str(s)]
            fired = sum(cells[row]["fired"] for row in direct)
            rows[str(s)] = {
                "fired": fired,
                "any_shard_survives": (
                    round(sum(cells[row]["any_survives"] for row in direct)
                          / fired, 6) if fired else None
                ),
                "mean_shards_dead": (
                    round(sum(sum(cells[row]["deaths"]) for row in direct)
                          / fired, 6) if fired else None
                ),
                "mean_recovered_fraction": (
                    round(sum(cells[row]["recovered_sum"] for row in direct)
                          / fired, 6) if fired else None
                ),
            }
        boundary_sensitivity[rule] = rows

    # (b) the exhaustive adversarial single-flip sweep, including every
    #     wire adjacent to a contiguous block boundary
    boundary_wires = set()
    for s in SHARD_COUNTS:
        for blk in ctx["blocks"][("contiguous", s)]:
            boundary_wires.add(blk[0])
            boundary_wires.add(blk[-1])
    boundary_payload = [w for w in payload if w in boundary_wires]
    others = [w for w in payload if w not in boundary_wires]
    sweep_wires = (boundary_payload + others)[:ADVERSARIAL_WIRE_CAP]
    worst = {
        f"{rule}.{s}": {"max_shards_killed": 0, "min_survivors": s,
                        "probes": 0, "fired": 0, "no_survivor_cases": 0,
                        "multi_shard_kills": 0, "law_violations": 0}
        for rule in RULES for s in SHARD_COUNTS
    }
    sweep_cone_failures = 0
    sweep_damage_max = 0
    sweep_damage_sum = 0
    sweep_fired = 0
    boundary_wire_multi_kills = 0
    damage_histogram: dict = {}
    for first, lane, pre, last_chunk, base_after, _ct, _key in (
            ctx["lanes_used"][:ADVERSARIAL_LANE_CAP]):
        for wire in sweep_wires:
            mut = list(pre)
            mut[wire] ^= 1
            entry = tuple(mut)
            after = K.A.apply_semantic(entry, last_chunk)
            fired = clean(after)
            sc = score(ctx, pre, entry, after, base_after, last_chunk)
            sweep_cone_failures += int(not sc["damage"] <= sc["cone"])
            if fired:
                sweep_fired += 1
                sweep_damage_sum += len(sc["damage"])
                sweep_damage_max = max(sweep_damage_max, len(sc["damage"]))
                hkey = str(len(sc["damage"]))
                damage_histogram[hkey] = damage_histogram.get(hkey, 0) + 1
            for rule in RULES:
                for s in SHARD_COUNTS:
                    slot = worst[f"{rule}.{s}"]
                    slot["probes"] += 1
                    if not fired:
                        continue
                    slot["fired"] += 1
                    dead = sc["deaths"][(rule, s)]
                    blk = ctx["blocks"][(rule, s)]
                    predicted = {
                        i for i in range(s) if sc["cone"].intersection(blk[i])
                    }
                    slot["law_violations"] += int(not dead <= predicted)
                    slot["max_shards_killed"] = max(
                        slot["max_shards_killed"], len(dead))
                    slot["min_survivors"] = min(
                        slot["min_survivors"], s - len(dead))
                    slot["no_survivor_cases"] += int(len(dead) == s)
                    slot["multi_shard_kills"] += int(len(dead) > 1)
                    if rule == "contiguous" and len(dead) > 1 and (
                            wire in boundary_wires):
                        boundary_wire_multi_kills += 1

    # (c) k-wire flips placed in k distinct contiguous shards
    multi = {}
    s_top = SHARD_COUNTS[-1]
    top_blocks = ctx["blocks"][("contiguous", s_top)]
    block_payload = [
        [w for w in payload if w in set(top_blocks[i])] for i in range(s_top)
    ]
    for k in MULTI_FLIP_K:
        probes = fired_n = 0
        killed_sum = 0
        no_survivor = 0
        damage_sum = 0
        variants = 0
        # several independent k-tuples, so a null cannot be one unlucky
        # choice of wires: take the first, the second and the last payload
        # wire of each targeted block.
        for offset in MULTI_FLIP_OFFSETS:
            chosen: list = []
            for i in range(s_top):
                if len(chosen) >= k:
                    break
                in_block = block_payload[i]
                if len(in_block) > abs(offset) or (
                        offset < 0 and in_block):
                    chosen.append(in_block[offset])
            if len(chosen) < k:
                continue
            variants += 1
            for first, lane, pre, last_chunk, base_after, _ct, _key in (
                    ctx["lanes_used"][:ADVERSARIAL_LANE_CAP]):
                mut = list(pre)
                for w in chosen:
                    mut[w] ^= 1
                entry = tuple(mut)
                after = K.A.apply_semantic(entry, last_chunk)
                probes += 1
                if not clean(after):
                    continue
                fired_n += 1
                sc = score(ctx, pre, entry, after, base_after, last_chunk)
                dead = sc["deaths"][("contiguous", s_top)]
                killed_sum += len(dead)
                damage_sum += len(sc["damage"])
                no_survivor += int(len(dead) == s_top)
        multi[str(k)] = {
            "wires_flipped": k,
            "distinct_shards_targeted": k,
            "wire_tuples_tried": variants,
            "probes": probes, "fired": fired_n,
            "firing_rate": round(fired_n / probes, 6) if probes else None,
            "mean_shards_killed_of_S": (
                round(killed_sum / fired_n, 6) if fired_n else None
            ),
            "mean_damage_wires": (
                round(damage_sum / fired_n, 6) if fired_n else None
            ),
            "no_survivor_cases": no_survivor,
        }

    # Refutations are confined to what the primary actually claims: the
    # cone law (universal) and the declared-class incidence matrix (scored
    # in THE_LOCALITY_PROBE).  The exhaustive sweep runs wires the primary
    # never declared, so what it finds PRICES THE SCOPE of the survival
    # law rather than refuting it -- reported either way it falls.
    refutations = []
    if sweep_cone_failures:
        refutations.append(
            "adversarial sweep: damage escaped the monotone structural"
            f" forward cone on {sweep_cone_failures} probes -- the"
            " primary's cone law is refuted"
        )
    sweep_law_violations = sum(v["law_violations"] for v in worst.values())
    if sweep_law_violations:
        refutations.append(
            f"adversarial sweep: {sweep_law_violations} shard deaths fell"
            " outside the cone prediction"
        )
    multi_kill_rules = sorted(
        k for k, v in worst.items() if v["multi_shard_kills"] > 0
    )
    no_survivor_rules = sorted(
        k for k, v in worst.items() if v["no_survivor_cases"] > 0
    )
    one_wire = damage_histogram.get("1", 0)
    contiguous_erased = sorted(
        k for k in no_survivor_rules if k.startswith("contiguous")
    )
    scope_findings = {
        "single_flip_can_kill_multiple_shards": multi_kill_rules,
        "single_flip_can_erase_all_shards": no_survivor_rules,
        "contiguous_rule_erased_all_shards": contiguous_erased,
        "single_flip_damage_size_histogram_given_fired": damage_histogram,
        "min_survivors_by_rule": {
            k: v["min_survivors"] for k, v in worst.items()
        },
        "reading": (
            f"{one_wire} of {sweep_fired} firing single-wire payload flips"
            " damage exactly one live wire"
            + (
                "; the remainder spread further, and under scattered"
                " boundaries that tail can reach every shard while"
                " contiguous blocks confine it"
                if one_wire < sweep_fired else
                ", so exactly one shard dies under every boundary rule"
            )
            + (
                " -- contiguous blocks never lost every shard"
                if not contiguous_erased else
                " -- contiguous blocks also lost every shard at "
                + compact(contiguous_erased)
            )
        ),
    }
    result = {
        "attack": "THE_BOUNDARY_ATTACK",
        "boundary_sensitivity_direct_classes": boundary_sensitivity,
        "adversarial_sweep": {
            "lanes": len(ctx["lanes_used"][:ADVERSARIAL_LANE_CAP]),
            "lane_cap": ADVERSARIAL_LANE_CAP,
            "wire_cap": ADVERSARIAL_WIRE_CAP,
            "wires_swept": len(sweep_wires),
            "block_boundary_wires_swept": len(
                [w for w in sweep_wires if w in boundary_wires]
            ),
            "fired_probes": sweep_fired,
            "mean_damage_wires_given_fired": (
                round(sweep_damage_sum / sweep_fired, 6) if sweep_fired
                else None
            ),
            "max_damage_wires_given_fired": sweep_damage_max,
            "live_payload_wires": live_total,
            "per_rule_worst_case": worst,
            "boundary_wire_multi_shard_kills": boundary_wire_multi_kills,
            "cone_failures": sweep_cone_failures,
            "cone_prediction_violations": sweep_law_violations,
            "scope_findings": scope_findings,
        },
        "multi_wire_flips": multi,
        "adjacent_finding": (
            "moving the boundaries and sweeping every payload wire is the"
            " refutation attempt; k-wire flips are OUTSIDE the declared"
            " single-flip classes, so their result prices the adversarial"
            " power sharding demands rather than refuting the law -- firing"
            " rate " + compact({k: multi[k].get("firing_rate")
                                for k in multi})
            + ", shards killed of S "
            + compact({k: multi[k].get("mean_shards_killed_of_S")
                       for k in multi})
        ),
        "rank_map_check": len(rank_of) == live_total,
        "refutations": refutations,
    }
    result["pass"] = not refutations and result["rank_map_check"]
    return result


# ---- ATTACK 4: THE_SCOPE_AUDIT ------------------------------------------
def attack_scope():
    src = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=PRIMARY_PATH)
    consts = set()
    flow: dict = {}
    gates: dict = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        names = {
            m.id for m in ast.walk(node.value) if isinstance(m, ast.Name)
        }
        for target in node.targets:
            if isinstance(target, ast.Name):
                consts.add(target.id)
                flow.setdefault(target.id, set()).update(names)
            elif (isinstance(target, ast.Subscript)
                  and isinstance(target.value, ast.Name)
                  and isinstance(target.slice, ast.Constant)
                  and target.slice.value == "pass"):
                gates.setdefault(target.value.id, set()).update(names)
    # a cap is disclosed iff it FLOWS into an emitted certificate payload
    seen = set()
    frontier = [r for r in DISCLOSURE_ROOTS if r in flow]
    while frontier:
        name = frontier.pop()
        if name in seen:
            continue
        seen.add(name)
        frontier.extend(flow.get(name, ()))
    missing = sorted(c for c in DECLARED_CAPS if c not in consts)
    undisclosed = sorted(
        c for c in DECLARED_CAPS if c in consts and c not in seen
    )
    leaks = sorted(
        f"{gate}:{name}"
        for gate, names in gates.items()
        for name in names if name in GATE_MUST_NOT_REFERENCE
    )
    result = {
        "attack": "THE_SCOPE_AUDIT",
        "primary": PRIMARY_PATH,
        "declared_caps_checked": DECLARED_CAPS,
        "caps_missing_from_primary": missing,
        "caps_not_reaching_any_certificate": undisclosed,
        "pass_gates_found": sorted(gates),
        "forbidden_names": GATE_MUST_NOT_REFERENCE,
        "outcome_objects_referenced_by_pass_gates": leaks,
        "statement": (
            "a cap is disclosed iff its constant flows through the"
            " primary's assignments into an emitted certificate payload;"
            " a gate is clean iff it never references the objects that"
            " carry the locality verdict, the incidence matrix or the"
            " S-curve -- range checks on the reconstruction rates are"
            " bookkeeping and cannot encode a preferred value"
        ),
        "refutations": (
            [f"undisclosed caps: {undisclosed}"] if undisclosed else []
        ) + (
            [f"missing caps: {missing}"] if missing else []
        ) + (
            [f"pass-gate references outcome: {leaks}"] if leaks else []
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
        "global_dirty": global_dirty,
        "bank_dirty": (part["per_bank"][0], part["per_bank"][1]),
    }
    a1 = attack_register(ctx)

    key_index = {key: lane for lane, key in enumerate(census)}
    ctx["candidates"] = sorted(
        (b, key_index[key]) for key, b in ctx["first_moment"].items()
        if 0 < b <= LOC_BOUNDARY_CAP
    )[:LOC_LANE_CAP]
    probe_common(ctx)
    a2 = attack_probe(ctx)
    a3 = attack_boundary(ctx)
    a4 = attack_scope()

    det_a = digest([sorted(r) for r in partition(BANKS)["full_bank"]])
    det_b = digest([sorted(r) for r in partition(BANKS)["full_bank"]])
    det_c = digest(build_census(K.interleaved_program(BANKS)))
    det_d = digest({
        f"{rule}.{s}": [list(b) for b in decompositions(ctx["live"])[(rule, s)]]
        for rule in RULES for s in SHARD_COUNTS
    })
    det_e = digest({
        f"{rule}.{s}": [list(b) for b in decompositions(ctx["live"])[(rule, s)]]
        for rule in RULES for s in SHARD_COUNTS
    })
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
        "kernel_imported": KERNEL_PATH,
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
            "decomposition_digest": det_d,
            "decomposition_repeatable": det_d == det_e,
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
        and det_a == det_b and det_d == det_e
        and runtime < AUDIT_TIMEOUT_SEC
    )

    all_refutations = (
        a1["refutations"] + a2["refutations"] + a3["refutations"]
        + a4["refutations"]
    )
    checks = {
        "THE_SHARDED_REGISTER": a1["pass"],
        "THE_LOCALITY_PROBE": a2["pass"],
        "THE_BOUNDARY_ATTACK": a3["pass"],
        "THE_SCOPE_AUDIT": a4["pass"],
        "CONTROLS": controls["pass"],
    }
    lines = ["CYCLE877_SHARDING_INDEPENDENT_CHECK",
             "ISOLATED_REIMPLEMENTATION_SPECD_TO_REFUTE"]
    for name, payload in (("THE_SHARDED_REGISTER", a1),
                          ("THE_LOCALITY_PROBE", a2),
                          ("THE_BOUNDARY_ATTACK", a3),
                          ("THE_SCOPE_AUDIT", a4),
                          ("CONTROLS", controls)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 877,
        "numbers_reproduced": {
            "register": not a1["refutations"],
            "probe": not a2["refutations"],
            "scope": not a4["refutations"],
        },
        "boundary_rules_tested": RULES,
        "cone_law_holds": not a3["refutations"],
        "boundary_sensitivity_any_shard_survives": {
            rule: {
                s: a3["boundary_sensitivity_direct_classes"][rule][s][
                    "any_shard_survives"]
                for s in a3["boundary_sensitivity_direct_classes"][rule]
            }
            for rule in RULES
        },
        "single_flip_worst_case": {
            k: v["max_shards_killed"]
            for k, v in a3["adversarial_sweep"]["per_rule_worst_case"].items()
        },
        "single_flip_scope": a3["adversarial_sweep"]["scope_findings"],
        "multi_wire_flip_firing_rate": {
            k: a3["multi_wire_flips"][k].get("firing_rate")
            for k in a3["multi_wire_flips"]
        },
        "multi_wire_flip_shards_killed": {
            k: a3["multi_wire_flips"][k].get("mean_shards_killed_of_S")
            for k in a3["multi_wire_flips"]
        },
        "refutations": all_refutations,
        "runtime_seconds": round(monotonic() - started, 3),
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE877_SHARDING_INDEPENDENT_CHECK_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
