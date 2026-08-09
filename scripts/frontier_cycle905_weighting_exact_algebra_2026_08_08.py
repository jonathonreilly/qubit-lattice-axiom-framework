#!/usr/bin/env python3
"""Cycle 905 (salvage pass): exact algebra of the five candidate weightings
on the stipulated composed-record model.

CONDITIONAL FINITE-MODEL SUPPORT.  This runner is the review-loop salvage
rebuild of the rejected Cycle-905 package (PR #5967, FAIL/SALVAGE_REJECT).
It carries EXACTLY the finite calculations the reviewer named durable --
the rank, zero-set, residual, difference-support and factorization
calculations -- and nothing else.  Every statement below is conditional on
the stipulated in-file model; nothing here is a statement about the axiom
surface, about probability, about physical occurrence, about any
interface or bridge, or about the selection of any weighting.

NO probability postulate is introduced, NO Born-rule claim is made, NO
measure is selected, NO candidate is promoted or eliminated.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

What is certified (all exact, all on the stipulated model):

  (i)   the 5 x 92,260 integer weighting matrix has rank 5, by three
        agreeing routes, with an exhibited nonsingular 5 x 5 minor;
  (ii)  the world-coefficient identity a4 + a5 = (boundaries + 1) *
        [formed] holds on all 748 world rows, and the candidate
        combination it suggests, (boundaries+1)*M2 - M4 - M5, has
        nonzero event-level residual exactly on the never-formed block;
  (iii) the exact zero-event sets and counts of the five weightings,
        including the set identities zero(M3) = zero(M4) and
        zero(M3) strictly contained in zero(M5);
  (iv)  the exact pairwise difference supports of the five weightings,
        with the unequal values expressly retained in the witnesses;
  (v)   the totals and exact subset-mass lattices with their verified
        prime factorizations, stated as NECESSARY divisibility filters
        only -- no subset realizability is decided;
  (vi)  a conditional one-way positivity lemma: a weighting whose event
        masses are strictly positive everywhere assigns strictly
        positive mass to every nonempty subset of events.  Whether any
        constraint demanding zero mass on a nonempty subset applies to
        this model is expressly NOT decided here.

SELF-CONTAINED input closure: the ONLY file input is the landed
Cycle-719 controller core, sha/blob-pinned, present on origin/main at
the pinned blob.  The composed record-write model is stipulated IN-FILE
below (the same in-file stipulation, function for function, as the
current-main Cycle-878 support note's primary; that note is a
cross-reference, not an input).  No unlanded, superseded, or absent
file is read, pinned, or imported.

Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024

# SELF-CONTAINED input closure: the ONLY input is the landed Cycle-719
# core (present on origin/main at this exact blob).  The composed
# record-write model itself is stipulated IN-FILE below.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
COMPUTATIONAL_INPUT_PATHS = AUDIT_INPUT_PATHS
# Import firewall against the legacy fixture-lineage modules and the
# rejected Cycle-905 draft: NAME STRINGS only (provenance context,
# non-load-bearing); the files are NOT inputs and need not exist.
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
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


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

# ---------------------------------------------------------------------------
# Stipulated scope inputs.  These are computational boundary conditions
# that materially determine the event set and every count below.  They
# are stipulated, not measured and not axiom-derived.
# ---------------------------------------------------------------------------
FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
FRACTION_LABEL = "bookkeeping fraction, not probability"

CANDIDATE_NAMES = (
    "M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
)
CONTROL_NAME = "M0_CONTENT_DIVERSITY"
FAMILY_ORDER = (
    "F_WORLD", "F_TAG", "F_TAG_ORDINAL", "F_MOMENT", "F_ORBIT",
    "F_CONTENT", "F_WORLD_TAG", "F_ATOM",
)
# The three weightings whose event masses vanish somewhere (their world
# coefficient reads the formation/occupation ledger) and the two whose
# event masses are strictly positive everywhere (their world coefficient
# is the constant 1).  These are descriptive groupings of a computed
# fact, not a selection.
ZERO_CARRYING = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
                 "M5_FORMATION_MOMENT")
EVERYWHERE_POSITIVE = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")

BOUNDARY_STATEMENT = (
    "this package supplies no occurrence rule, no probability, no update"
    " law, no observable, no symmetry action on event atoms, and no"
    " constraint imported from any other lane; it selects no candidate"
    " weighting and eliminates none; it certifies exact finite algebra of"
    " the five candidate weightings over a stipulated in-file model, as"
    " conditional finite-model support"
)

# ---------------------------------------------------------------------------
# Expected headline values.  Every number the note quotes is gated here
# value-for-value, so the note cannot drift from the computation.  These
# are in-file expected constants for THIS stipulated model, frozen from
# the computation itself; the gates recompute everything and fail closed
# on any mismatch.
# ---------------------------------------------------------------------------
EXPECTED = {
    "events": 92_260,
    "worlds": 748,
    "boundaries": 180_224,
    "stations": 11,
    "worlds_formed": 164,
    "worlds_never_formed": 584,
    "never_formed_events": 73_088,
    "worlds_formed_at_moment_zero": 24,
    "events_by_tag": {"B0": 47_872, "B1": 44_224, "F": 164},
    "per_world_event_count_range": [64, 129],
    "cells_per_family": {
        "F_WORLD": 748, "F_TAG": 3, "F_TAG_ORDINAL": 129, "F_MOMENT": 24_362,
        "F_ORBIT": 3_470, "F_CONTENT": 52_018, "F_WORLD_TAG": 1_603,
        "F_ATOM": 92_260,
    },
    "common_denominator": 1_073_280,
    "rank": 5,
    "zero_carrying_triple_rank": 3,
    "coefficient_identity_violations": 0,
    "residual_nonzero_events": 73_088,
    "residual_nonzero_worlds": 584,
    "zero_weight_events": {
        "M1_COUNTING": 0, "M2_PER_WORLD_UNIFORM": 0,
        "M3_OCCUPATION_WEIGHTED": 73_088, "M4_FORMATION_LIFETIME": 73_088,
        "M5_FORMATION_MOMENT": 76_184,
    },
    "min_event_numerators_everywhere_positive": {
        "M1_COUNTING": 1, "M2_PER_WORLD_UNIFORM": 8_320,
    },
    "m5_extra_zero_events": 3_096,
    "totals": {
        "M1_COUNTING": 92_260,
        "M2_PER_WORLD_UNIFORM": 802_813_440,
        "M3_OCCUPATION_WEIGHTED": 897_595_870_080,
        "M4_FORMATION_LIFETIME": 29_530_480_287_360,
        "M5_FORMATION_MOMENT": 2_192_349_344_640,
    },
    "mass_lattices": {
        "M1_COUNTING": 92_260,
        "M2_PER_WORLD_UNIFORM": 802_813_440,
        "M3_OCCUPATION_WEIGHTED": 7_012_467_735,
        "M4_FORMATION_LIFETIME": 230_706_877_245,
        "M5_FORMATION_MOMENT": 17_127_729_255,
    },
    "total_factorizations": {
        "M1_COUNTING": {2: 2, 5: 1, 7: 1, 659: 1},
        "M2_PER_WORLD_UNIFORM":
            {2: 9, 3: 1, 5: 1, 11: 1, 13: 1, 17: 1, 43: 1},
        "M3_OCCUPATION_WEIGHTED":
            {2: 7, 3: 1, 5: 1, 7: 1, 13: 1, 37: 1, 43: 1, 3229: 1},
        "M4_FORMATION_LIFETIME":
            {2: 7, 3: 1, 5: 1, 13: 1, 43: 1, 59: 1, 163: 1, 2861: 1},
        "M5_FORMATION_MOMENT":
            {2: 7, 3: 1, 5: 1, 7: 2, 13: 1, 43: 1, 41687: 1},
    },
    "lattice_factorizations": {
        "M1_COUNTING": {2: 2, 5: 1, 7: 1, 659: 1},
        "M2_PER_WORLD_UNIFORM":
            {2: 9, 3: 1, 5: 1, 11: 1, 13: 1, 17: 1, 43: 1},
        "M3_OCCUPATION_WEIGHTED":
            {3: 1, 5: 1, 7: 1, 13: 1, 37: 1, 43: 1, 3229: 1},
        "M4_FORMATION_LIFETIME":
            {3: 1, 5: 1, 13: 1, 43: 1, 59: 1, 163: 1, 2861: 1},
        "M5_FORMATION_MOMENT":
            {3: 1, 5: 1, 7: 2, 13: 1, 43: 1, 41687: 1},
    },
    "difference_support_cardinalities": {
        "M1_COUNTING|M2_PER_WORLD_UNIFORM": 92_260,
        "M1_COUNTING|M3_OCCUPATION_WEIGHTED": 92_260,
        "M1_COUNTING|M4_FORMATION_LIFETIME": 92_260,
        "M1_COUNTING|M5_FORMATION_MOMENT": 92_260,
        "M2_PER_WORLD_UNIFORM|M3_OCCUPATION_WEIGHTED": 92_260,
        "M2_PER_WORLD_UNIFORM|M4_FORMATION_LIFETIME": 92_260,
        "M2_PER_WORLD_UNIFORM|M5_FORMATION_MOMENT": 92_260,
        "M3_OCCUPATION_WEIGHTED|M4_FORMATION_LIFETIME": 19_172,
        "M3_OCCUPATION_WEIGHTED|M5_FORMATION_MOMENT": 19_172,
        "M4_FORMATION_LIFETIME|M5_FORMATION_MOMENT": 19_172,
    },
    "per_family_differing_cells_zero_carrying_pairs": {
        "F_WORLD": 164, "F_TAG": 3, "F_TAG_ORDINAL": 129, "F_MOMENT": 8_199,
        "F_ORBIT": 2_037, "F_CONTENT": 11_627, "F_WORLD_TAG": 461,
        "F_ATOM": 19_172,
    },
    "nonsingular_minor_worlds": [0, 1, 7, 8, 11],
    "nonsingular_minor_determinant": 138_978_185_647_720_130_150_400_000,
}


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin, valid far beyond every integer that
    appears in this runner (all are < 2**63)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factorize(value: int) -> dict:
    out: dict = {}
    n, p = value, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def factorization_verified(value: int, factors: dict) -> bool:
    product = 1
    for p, e in factors.items():
        if not is_prime(p):
            return False
        product *= p ** e
    return product == value


def source_controls() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in COMPUTATIONAL_INPUT_PATHS:
        ast.parse(payloads[p], filename=p)
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) \
                        and target.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_SOURCE_CONTROLS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "input_closure_statement": (
            "self-contained: the only input is the landed Cycle-719 core;"
            " the composed record-write model is stipulated in-file; the"
            " legacy fixture-lineage module names and the rejected"
            " Cycle-905 draft are import-blocklisted and their files are"
            " not read, pinned, or required to exist"
        ),
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "no_docs_paths_in_input_closure": not any(
            p.startswith("docs/") for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_ok"]
        and result["existing_worktree_relative"]
        and result["no_docs_paths_in_input_closure"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# ---------------------------------------------------------------------------
# Stipulated in-file model machinery (built from the landed Cycle-719 core
# alone).  Everything below this banner is part of THIS runner's stipulated
# definition of the composed record-write model: census, seeds, initial
# states, dirty partition, lane packing, masked schedules, dead-wire
# register, slot allocation, and the composed scan.  It is the same
# in-file stipulation, function for function, as the current-main
# Cycle-878 support note's primary; that note is a cross-reference, not
# an input, and no other file supplies any of it.
# ---------------------------------------------------------------------------

def pairwise_separated(positions, stations):
    occupied = set(positions)
    return all((s + 1) % stations not in occupied for s in occupied)


def derive_event_seeds(program):
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            raise AssertionError(("event seed", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def derive_census():
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    keys = tuple(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _s in event_seeds
    )
    return program, event_seeds, tuple(sorted(keys))


def watched_registers():
    return (
        ("POINTER", K.A.POINTER), ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U), ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{i}", w) for i, w in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{i}", w) for i, w in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def dirty_partition():
    """Global dirty coordinates partitioned: per-bank, links, source pointer."""
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    per_bank: list[set] = [set() for _ in zero_banks]
    for bank_index in range(len(zero_banks)):
        for _name, wire in watched_registers():
            changed = [list(b) for b in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(b) for b in changed), zero_links
            )
            diffs = [
                i for i, (l, r) in enumerate(zip(baseline, marked)) if l != r
            ]
            if len(diffs) != 1:
                raise AssertionError(("bank marker", diffs))
            per_bank[bank_index].add(diffs[0])
    link_set: set = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(tuple(r) for r in changed))
            diffs = [
                i for i, (l, r) in enumerate(zip(baseline, marked)) if l != r
            ]
            if len(diffs) != 1:
                raise AssertionError(("link marker", diffs))
            link_set.add(diffs[0])
    return (
        tuple(tuple(sorted(s)) for s in per_bank),
        tuple(sorted(link_set)),
        K.R3.X.SOURCE_POINTER,
    )


def build_initial_states(program, event_seeds, census):
    seed_by_event = dict(event_seeds)
    states = []
    failures = 0
    for _k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _ = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(s in positions) for s in range(len(program))
        )
        failures += rail_a != expected_rail or any(rail_b)
        states.append(after)
    return tuple(states), failures


def pack_lanes(states):
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate, mask):
    if gate.kind == "X":
        return (0, gate.wires[0], 0, 0, mask)
    if gate.kind == "CNOT":
        return (1, gate.wires[0], gate.wires[1], 0, mask)
    if gate.kind == "TOF":
        return (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
    raise ValueError(("gate", gate))


def masked_h_schedules(program, census):
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_k, _e, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if mask:
                schedule.extend(
                    compile_masked_gate(g, mask) for g in K.mapped_macro(row)
                )
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_fast(schedules):
    fns = []
    for schedule in schedules:
        src = ["def apply_chunk(c):"]
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


def mask_over(columns, indices, universe):
    dirty = 0
    for wire in indices:
        dirty |= columns[wire]
    return universe & ~dirty


def lanes_of(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def lane_state(columns, lane):
    bit = 1 << lane
    return tuple(int(bool(col & bit)) for col in columns)


def dead_wire_rig(program, sim, columns_proto):
    """Derive boundary-dead wires, then the structurally inert safe slots."""
    fast = compile_fast(masked_h_schedules(program, sim))
    universe_sim = (1 << len(sim)) - 1
    work = list(columns_proto)
    acc = list(work)
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    dead_wires = tuple(
        w for w in range(len(acc)) if (acc[w] & universe_sim) == 0
    )
    gate_inputs: set = set()
    gate_targets: set = set()
    for schedule in masked_h_schedules(program, sim):
        for kind, a, b, c3, _mask in schedule:
            if kind == 0:
                gate_targets.add(a)
            elif kind == 1:
                gate_inputs.add(a)
                gate_targets.add(b)
            else:
                gate_inputs.update((a, b))
                gate_targets.add(c3)
    safe_pool = tuple(
        w for w in dead_wires
        if w not in gate_inputs and w not in gate_targets
    )
    slot_tags = [("F", 0)] + [
        (f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    if len(safe_pool) < len(slot_tags):
        raise AssertionError(
            ("insufficient safe slots", len(safe_pool), len(slot_tags))
        )
    return {
        "fast": fast,
        "dead_wires": dead_wires,
        "safe_pool": safe_pool,
        "slot_of": {tag: safe_pool[i] for i, tag in enumerate(slot_tags)},
        "gate_inputs": gate_inputs,
        "gate_targets": gate_targets,
    }


def composed_scan(program, census, states, rig, orbits):
    """The composed model: base dynamics + REAL register writes into the
    inert dead-wire slots.  Returns the realized record-write event list
    plus the occupation ledger accumulated on the same trajectory."""
    slot_of = rig["slot_of"]
    fast = rig["fast"]
    n = len(census)
    dup = n
    columns = pack_lanes(states + (states[0],))
    per_bank, links, source_ptr = dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    slot_wires = set(slot_of.values())
    watch_dead = tuple(w for w in rig["dead_wires"] if w not in slot_wires)

    events: list[tuple] = []
    occ_global = [0] * n
    occ_bank = ([0] * n, [0] * n)
    bank_ordinal = [[0, 0] for _ in range(n)]
    beyond_cap = 0
    write_once_violations = 0
    formed: dict[int, int] = {}
    mismatches = 0
    dead_acc = 0

    def wire_write(tag, lane):
        nonlocal write_once_violations
        wire = slot_of[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit

    def content_of(lane):
        return sha256(bytes(lane_state(columns, lane))).hexdigest()[:16]

    g0 = mask_over(columns, global_dirty, uni_sim)
    mismatches += int(bool(g0 & 1) != bool(g0 & (1 << dup)))
    ga0 = g0 & uni_all
    b_mask = [
        mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    for lane in lanes_of(ga0):
        occ_global[lane] += 1
    for b in (0, 1):
        for lane in lanes_of(b_mask[b]):
            occ_bank[b][lane] += 1
    for lane in lanes_of(ga0):
        formed[lane] = 0
        wire_write(("F", 0), lane)
        events.append((lane, 0, "F", 0, content_of(lane)))
    prev_bank = list(b_mask)

    boundary = 0
    for orbit in range(1, orbits + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = mask_over(columns, global_dirty, uni_sim)
            mismatches += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            for lane in lanes_of(ga):
                occ_global[lane] += 1
                if lane not in formed:
                    formed[lane] = boundary
                    wire_write(("F", 0), lane)
                    events.append((lane, boundary, "F", 0, content_of(lane)))
            for b in (0, 1):
                bm = mask_over(columns, bank_dirty[b], uni_all)
                for lane in lanes_of(bm):
                    occ_bank[b][lane] += 1
                for lane in lanes_of(bm & ~prev_bank[b]):
                    ordinal = bank_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                        events.append(
                            (lane, boundary, f"B{b}", ordinal,
                             content_of(lane))
                        )
                    else:
                        beyond_cap += 1
                    bank_ordinal[lane][b] = ordinal + 1
                prev_bank[b] = bm
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in watch_dead:
                    dead_acc |= columns[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in watch_dead:
                dead_acc |= columns[w]
    return {
        "events": events,
        "occ_global": occ_global,
        "occ_bank": occ_bank,
        "formed": formed,
        "beyond_cap": beyond_cap,
        "write_once_violations": write_once_violations,
        "dead_activation_conflicts": bin(dead_acc & uni_sim).count("1"),
        "mismatches": mismatches,
        "columns": columns,
        "global_dirty": global_dirty,
        "bank_dirty": bank_dirty,
        "boundaries": boundary,
        "initial_global_clean_lanes": len(lanes_of(ga0)),
    }


def family_keys(events, stations):
    """Cell key of every event under every declared family."""
    keys = {name: [] for name in FAMILY_ORDER}
    for lane, moment, tag, ordinal, content in events:
        keys["F_WORLD"].append(("w", lane))
        keys["F_TAG"].append(("t", tag))
        keys["F_TAG_ORDINAL"].append(("to", tag, ordinal))
        keys["F_MOMENT"].append(("m", moment))
        keys["F_ORBIT"].append(
            ("o", 0 if moment == 0 else ((moment - 1) // stations) + 1)
        )
        keys["F_CONTENT"].append(("c", content))
        keys["F_WORLD_TAG"].append(("wt", lane, tag))
        keys["F_ATOM"].append(("a", lane, tag, ordinal))
    return keys


def cells_of(key_list):
    cells: dict = {}
    for index, key in enumerate(key_list):
        cells.setdefault(key, []).append(index)
    return cells


def build_candidates(events, occ_global, formed, boundaries):
    """Declared candidate weightings computable from the stipulated
    model's record bookkeeping alone.  Each candidate is an EVENT-LEVEL
    weight w: E -> Q_{>=0}, carried as integer numerators over one common
    denominator per candidate.  "Candidate" means finite-measure
    candidate; NO framework-Admissibility compatibility is claimed."""
    per_world = Counter(e[0] for e in events)
    supported = sorted(per_world)
    n_supported = len(supported)
    common = 1
    for count in set(per_world.values()):
        common = lcm(common, count)

    def world_weighted(a_of_world):
        totals = sum(a_of_world(w) for w in supported)
        nums = [
            a_of_world(e[0]) * (common // per_world[e[0]]) for e in events
        ]
        return nums, totals * common

    nums: dict[str, list[int]] = {}
    dens: dict[str, int] = {}

    nums["M1_COUNTING"] = [1] * len(events)
    dens["M1_COUNTING"] = 1

    nums["M2_PER_WORLD_UNIFORM"], dens["M2_PER_WORLD_UNIFORM"] = \
        world_weighted(lambda w: 1)

    nums["M3_OCCUPATION_WEIGHTED"], dens["M3_OCCUPATION_WEIGHTED"] = \
        world_weighted(lambda w: occ_global[w])

    nums["M4_FORMATION_LIFETIME"], dens["M4_FORMATION_LIFETIME"] = \
        world_weighted(
            lambda w: (boundaries - formed[w] + 1) if w in formed else 0
        )

    nums["M5_FORMATION_MOMENT"], dens["M5_FORMATION_MOMENT"] = \
        world_weighted(lambda w: formed[w] if w in formed else 0)

    return nums, dens, per_world, supported, n_supported, common


def build_event_space():
    program, event_seeds, census = derive_census()
    stations = len(program)
    states, init_fail = build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = dead_wire_rig(program, sim, pack_lanes(states + (states[0],)))
    scan = composed_scan(program, census, states, rig, HORIZON)
    return {
        "program": program, "census": census, "stations": stations,
        "states": states, "rig": rig, "scan": scan,
        "events": scan["events"], "init_failures": init_fail,
    }


# ---------------------------------------------------------------------------
# Exact rank routes (two mandatory routes plus a world-reduced cross-check)
# ---------------------------------------------------------------------------

def rank_by_rational_elimination(rows):
    """Route A: full-pivot Gaussian elimination over Q.  No fraction-free
    (Bareiss) bookkeeping anywhere -- it corrupts ranks on rank-deficient
    matrices with skipped columns."""
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank, pivots = 0, []
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if work[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        lead = work[rank][col]
        work[rank] = [x / lead for x in work[rank]]
        for r in range(n_rows):
            if r != rank and work[r][col] != 0:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == n_rows:
            break
    return rank, tuple(pivots)


def det_laplace(matrix):
    """Division-free exact determinant by cofactor expansion."""
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    total = 0
    for col in range(size):
        if matrix[0][col] == 0:
            continue
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        total += ((-1) ** col) * matrix[0][col] * det_laplace(minor)
    return total


def rank_by_gram_minors(rows):
    """Route B: rank(M) = rank(M M^T) over an ordered field; the rank of
    the small Gram matrix is read off division-free by the largest
    non-vanishing principal minor, searched over subsets."""
    k = len(rows)
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]
    for size in range(k, 0, -1):
        for subset in combinations(range(k), size):
            minor = [[gram[i][j] for j in subset] for i in subset]
            if det_laplace(minor) != 0:
                return size, subset, gram
    return 0, (), gram


def rank_by_world_reduction(rows, world_of, worlds):
    """Cross-check route: every candidate is constant on worlds, so the
    rank is the rank of the 5 x |worlds| coefficient matrix.  Constancy is
    VERIFIED, not assumed."""
    first_index = {}
    for index, world in enumerate(world_of):
        first_index.setdefault(world, index)
    constant = True
    for row in rows:
        seen = {}
        for world, value in zip(world_of, row):
            if world in seen and seen[world] != value:
                constant = False
                break
            seen[world] = value
        if not constant:
            break
    reduced = [[row[first_index[w]] for w in worlds] for row in rows]
    rank, pivots = rank_by_rational_elimination(reduced)
    return rank, pivots, constant, reduced


def deterministic_indices(seed: int, count: int, universe: int) -> list:
    """Deterministic linear-congruential index stream (no RNG import; the
    subsets it generates are reproducible byte-for-byte)."""
    state = seed & 0x7FFFFFFF
    out = []
    for _ in range(count):
        state = (1103515245 * state + 12345) % (1 << 31)
        out.append(state % universe)
    return sorted(set(out))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a = source_controls()
    if not cert_a["pass"]:
        sys.stdout.write(
            "CERTIFICATE A_SOURCE_CONTROLS FAIL " + compact(cert_a) + "\n"
            + "CYCLE905_WEIGHTING_EXACT_ALGEBRA_PIN_FAILURE\n"
        )
        return 2

    build_a = build_event_space()
    events = build_a["events"]
    scan = build_a["scan"]
    stations = build_a["stations"]
    boundaries = scan["boundaries"]
    formed = scan["formed"]
    occupation = scan["occ_global"]
    world_of = [e[0] for e in events]
    worlds = sorted(set(world_of))
    never_formed_worlds = [w for w in worlds if w not in formed]
    never_formed_events = {i for i, w in enumerate(world_of)
                           if w not in formed}
    formed_at_zero = sorted(w for w, b in formed.items() if b == 0)
    event_digest = digest(events)

    numerators, denominators, per_world, supported, n_supported, common = \
        build_candidates(events, occupation, formed, boundaries)
    totals = {name: sum(numerators[name]) for name in CANDIDATE_NAMES}
    tag_counts = dict(sorted(Counter(e[2] for e in events).items()))
    keys = family_keys(events, stations)
    cells = {fam: cells_of(keys[fam]) for fam in FAMILY_ORDER}
    atoms_singleton = bool(events) and set(
        len(v) for v in cells["F_ATOM"].values()
    ) == {1}

    # ---- B: the stipulated model, built and gated -----------------------
    cert_b = {
        "certificate": "B_MODEL_BUILD",
        "reading": (
            "the stipulated in-file model is built from the pinned core"
            " alone and every headline count is gated against the in-file"
            " expected constants; internal integrity counters must all be"
            " zero"
        ),
        "computed": {
            "events": len(events),
            "worlds": len(worlds),
            "boundaries": boundaries,
            "stations": stations,
            "worlds_formed": len(formed),
            "worlds_never_formed": len(never_formed_worlds),
            "never_formed_events": len(never_formed_events),
            "worlds_formed_at_moment_zero": len(formed_at_zero),
            "events_by_tag": tag_counts,
            "per_world_event_count_range": [
                min(per_world.values()), max(per_world.values())
            ],
            "cells_per_family": {fam: len(cells[fam])
                                 for fam in FAMILY_ORDER},
            "atoms_are_singletons": atoms_singleton,
            "common_denominator": common,
            "supported_worlds": n_supported,
        },
        "expected": {
            k: EXPECTED[k] for k in (
                "events", "worlds", "boundaries", "stations", "worlds_formed",
                "worlds_never_formed", "never_formed_events",
                "worlds_formed_at_moment_zero", "events_by_tag",
                "per_world_event_count_range", "cells_per_family",
                "common_denominator",
            )
        },
        "integrity": {
            "write_once_violations": scan["write_once_violations"],
            "dead_activation_conflicts": scan["dead_activation_conflicts"],
            "duplicate_lane_mismatches": scan["mismatches"],
            "initial_state_failures": build_a["init_failures"],
        },
        "event_space_digest": event_digest,
    }
    cert_b["headline_matches"] = all(
        cert_b["computed"][k] == EXPECTED[k]
        for k in cert_b["expected"]
    )
    cert_b["pass"] = bool(
        cert_b["headline_matches"] and atoms_singleton
        and scan["write_once_violations"] == 0
        and scan["dead_activation_conflicts"] == 0
        and scan["mismatches"] == 0 and build_a["init_failures"] == 0
    )

    # ---- C: the rank of the weighting matrix ----------------------------
    matrix = [numerators[name] for name in CANDIDATE_NAMES]
    rank_a, pivots_a = rank_by_rational_elimination(matrix)
    rank_b, gram_subset, gram = rank_by_gram_minors(matrix)
    rank_c, pivots_c, world_constant, reduced = rank_by_world_reduction(
        matrix, world_of, worlds
    )
    triple_matrix = [numerators[name] for name in ZERO_CARRYING]
    rank_triple_a, _ = rank_by_rational_elimination(triple_matrix)
    rank_triple_b, _, _ = rank_by_gram_minors(triple_matrix)
    minor_worlds = [worlds[c] for c in pivots_c]
    minor_matrix = [[row[c] for c in pivots_c] for row in reduced]
    minor_det = det_laplace(minor_matrix)
    cert_c = {
        "certificate": "C_RANK",
        "statement": (
            "the exact rank of the five candidate weightings as functions"
            " on the stipulated model's 92,260-event census, by three"
            " agreeing routes, with an exhibited nonsingular minor"
        ),
        "matrix_shape": [len(CANDIDATE_NAMES), len(events)],
        "route_A_rational_elimination": {
            "rank": rank_a, "pivot_columns": list(pivots_a),
            "method": "full pivot search, exact Fraction arithmetic, no"
                      " fraction-free (Bareiss) bookkeeping anywhere",
        },
        "route_B_gram_laplace": {
            "rank": rank_b, "nonvanishing_principal_minor": list(gram_subset),
            "gram_determinant": det_laplace(gram),
            "method": "rank(M) = rank(M M^T) over Q; largest non-vanishing"
                      " principal minor by division-free cofactor expansion",
        },
        "route_C_world_reduction_crosscheck": {
            "rank": rank_c, "pivot_worlds": list(pivots_c),
            "candidates_constant_on_worlds_verified": world_constant,
            "reduced_shape": [len(CANDIDATE_NAMES), len(worlds)],
        },
        "routes_agree": rank_a == rank_b == rank_c,
        "rank": rank_a,
        "five_are_linearly_independent": rank_a == len(CANDIDATE_NAMES),
        "zero_carrying_triple_rank": {
            "route_A": rank_triple_a, "route_B": rank_triple_b,
            "agree": rank_triple_a == rank_triple_b,
        },
        "exhibited_nonsingular_minor": {
            "worlds": minor_worlds,
            "world_coefficient_matrix_rows_are_candidates":
                list(CANDIDATE_NAMES),
            "matrix": minor_matrix,
            "determinant": minor_det,
            "nonsingular": minor_det != 0,
            "reading": (
                "a 5 x 5 submatrix of the world-reduced numerator matrix"
                " with nonzero determinant; its columns are the exhibited"
                " worlds and its rows the five candidates -- an explicit"
                " witness that the rank is at least 5"
            ),
        },
    }
    cert_c["pass"] = bool(
        cert_c["routes_agree"] and world_constant
        and rank_a == EXPECTED["rank"]
        and rank_triple_a == rank_triple_b
        == EXPECTED["zero_carrying_triple_rank"]
        and minor_det == EXPECTED["nonsingular_minor_determinant"]
        and minor_worlds == EXPECTED["nonsingular_minor_worlds"]
        and minor_det != 0
    )

    # ---- D: the world-coefficient identity and its event-level residual -
    coefficient_rows = {
        w: {
            "a2": 1,
            "a3": occupation[w],
            "a4": (boundaries - formed[w] + 1) if w in formed else 0,
            "a5": formed[w] if w in formed else 0,
            "formed": w in formed,
        }
        for w in worlds
    }
    coeff_violations = [
        w for w, row in coefficient_rows.items()
        if row["a4"] + row["a5"] != (boundaries + 1) * int(row["formed"])
    ]
    residual = [
        (boundaries + 1) * numerators["M2_PER_WORLD_UNIFORM"][i]
        - numerators["M4_FORMATION_LIFETIME"][i]
        - numerators["M5_FORMATION_MOMENT"][i]
        for i in range(len(events))
    ]
    residual_nonzero = {i for i, v in enumerate(residual) if v != 0}
    residual_worlds = sorted({world_of[i] for i in residual_nonzero})
    cert_d = {
        "certificate": "D_COEFFICIENT_IDENTITY",
        "statement": (
            "the world-coefficient identity a4 + a5 = (boundaries + 1) *"
            " [formed] holds on every world row of the stipulated model,"
            " and the candidate combination it suggests,"
            " (boundaries+1)*M2 - M4 - M5, has nonzero event-level"
            " residual EXACTLY on the never-formed block -- so the"
            " identity induces no linear dependence among the five"
            " event-level weightings (consistent with rank 5)"
        ),
        "boundaries": boundaries,
        "coefficient_level_violations": len(coeff_violations),
        "coefficient_level_holds": not coeff_violations,
        "residual_vector": "(boundaries+1)*M2 - M4 - M5",
        "residual_nonzero_events": len(residual_nonzero),
        "residual_nonzero_worlds": len(residual_worlds),
        "residual_set_equals_never_formed_block":
            residual_nonzero == never_formed_events,
        "witness_events": [
            {"index": i, "event": list(events[i]),
             "residual_numerator": residual[i]}
            for i in sorted(residual_nonzero)[:3]
        ],
    }
    cert_d["pass"] = bool(
        len(coeff_violations) == EXPECTED["coefficient_identity_violations"]
        and len(residual_nonzero) == EXPECTED["residual_nonzero_events"]
        and len(residual_worlds) == EXPECTED["residual_nonzero_worlds"]
        and cert_d["residual_set_equals_never_formed_block"]
    )

    # ---- E: exact zero sets and the one-way positivity lemma ------------
    zero_sets = {name: {i for i, v in enumerate(numerators[name]) if v == 0}
                 for name in CANDIDATE_NAMES}
    zero_counts = {name: len(zero_sets[name]) for name in CANDIDATE_NAMES}
    min_numerators = {name: min(numerators[name]) for name in CANDIDATE_NAMES}
    m5_extra = zero_sets["M5_FORMATION_MOMENT"] \
        - zero_sets["M3_OCCUPATION_WEIGHTED"]
    formed_at_zero_events = {i for i, w in enumerate(world_of)
                             if w in set(formed_at_zero)}
    cert_e = {
        "certificate": "E_ZERO_SETS",
        "statement": (
            "the exact zero-event sets of the five candidate weightings on"
            " the stipulated model, with their set identities"
        ),
        "zero_weight_events": zero_counts,
        "min_event_numerators": min_numerators,
        "everywhere_positive": {
            name: min_numerators[name] > 0 for name in CANDIDATE_NAMES
        },
        "set_identities": {
            "zero_M3_equals_zero_M4_as_sets":
                zero_sets["M3_OCCUPATION_WEIGHTED"]
                == zero_sets["M4_FORMATION_LIFETIME"],
            "zero_M3_strict_subset_of_zero_M5":
                zero_sets["M3_OCCUPATION_WEIGHTED"]
                < zero_sets["M5_FORMATION_MOMENT"],
            "zero_M3_equals_never_formed_block":
                zero_sets["M3_OCCUPATION_WEIGHTED"] == never_formed_events,
            "zero_M5_equals_block_plus_moment_zero_worlds":
                zero_sets["M5_FORMATION_MOMENT"]
                == never_formed_events | formed_at_zero_events,
            "distinct_zero_sets_among_the_zero_carrying_triple": len({
                frozenset(zero_sets[name]) for name in ZERO_CARRYING
            }),
        },
        "m5_extra_zero_events": len(m5_extra),
        "never_formed_block_tag_mix": dict(sorted(Counter(
            events[i][2] for i in sorted(never_formed_events)).items())),
        "example_zero_events": {
            name: [list(events[i]) for i in sorted(zero_sets[name])[:2]]
            for name in ZERO_CARRYING
        },
        "mechanism": (
            "M1 and M2 have world coefficient constant 1, so their event"
            " numerator is a product of two strictly positive quantities"
            " and their zero set is EMPTY.  M3, M4 and M5 read their world"
            " coefficient off the formation/occupation ledger, which is"
            " identically zero on the never-formed block, so their zero"
            " sets are exactly that block (M5 additionally zeroes the"
            " worlds formed at moment 0).  This is a fact about the"
            " stipulated model's bookkeeping, nothing more"
        ),
        "one_way_positivity_lemma": {
            "statement": (
                "CONDITIONAL, ONE-WAY: if a weighting's event masses are"
                " strictly positive on every event, then every NONEMPTY"
                " subset of events carries strictly positive total mass;"
                " hence such a weighting cannot satisfy any constraint"
                " that would require zero total mass on some nonempty"
                " subset.  On this model the hypothesis holds for M1 and"
                " M2 (minimum event numerators 1 and 8320)."
            ),
            "expressly_not_decided_here": (
                "whether ANY constraint demanding zero mass on a nonempty"
                " subset applies to this model; the converse direction"
                " (that a weighting with a nonempty zero set can satisfy"
                " any particular such constraint); and any statement about"
                " interfaces, bridges, or selection"
            ),
            "hypothesis_holds_for": [
                name for name in CANDIDATE_NAMES if min_numerators[name] > 0
            ],
        },
        "label": FRACTION_LABEL,
    }
    cert_e["pass"] = bool(
        zero_counts == EXPECTED["zero_weight_events"]
        and {n: min_numerators[n] for n in EVERYWHERE_POSITIVE}
        == EXPECTED["min_event_numerators_everywhere_positive"]
        and cert_e["set_identities"]["zero_M3_equals_zero_M4_as_sets"]
        and cert_e["set_identities"]["zero_M3_strict_subset_of_zero_M5"]
        and cert_e["set_identities"]["zero_M3_equals_never_formed_block"]
        and cert_e["set_identities"][
            "zero_M5_equals_block_plus_moment_zero_worlds"]
        and len(m5_extra) == EXPECTED["m5_extra_zero_events"]
        and sorted(cert_e["one_way_positivity_lemma"]["hypothesis_holds_for"])
        == sorted(EVERYWHERE_POSITIVE)
    )

    # ---- F: exact pairwise difference supports --------------------------
    # Route: candidates are world-constant (verified in certificate C), so
    # the normalized mass of every event in world w is coeff(w) /
    # (total_coeff * |events(w)|); two candidates differ on an event iff
    # they differ on its world's normalized mass.
    first_index = {}
    for index, world in enumerate(world_of):
        first_index.setdefault(world, index)
    world_mass = {
        name: {
            w: Fraction(numerators[name][first_index[w]], totals[name])
            for w in worlds
        }
        for name in CANDIDATE_NAMES
    }
    events_of_world: dict = {}
    for index, world in enumerate(world_of):
        events_of_world.setdefault(world, []).append(index)
    pairs = [(a, b) for i, a in enumerate(CANDIDATE_NAMES)
             for b in CANDIDATE_NAMES[i + 1:]]
    support_sets = {}
    support_rows = {}
    for a, b in pairs:
        diff_worlds = [w for w in worlds
                       if world_mass[a][w] != world_mass[b][w]]
        indices = sorted(
            i for w in diff_worlds for i in events_of_world[w]
        )
        support_sets[f"{a}|{b}"] = frozenset(indices)
        witness = None
        if indices:
            i0 = indices[0]
            witness = {
                "event": list(events[i0]),
                a: fr(Fraction(numerators[a][i0], totals[a])),
                b: fr(Fraction(numerators[b][i0], totals[b])),
                "values_differ": Fraction(numerators[a][i0], totals[a])
                != Fraction(numerators[b][i0], totals[b]),
                "label": FRACTION_LABEL,
            }
        support_rows[f"{a}|{b}"] = {
            "differing_events": len(indices),
            "differing_worlds": len(diff_worlds),
            "by_tag": dict(sorted(Counter(
                events[i][2] for i in indices).items())),
            "support_digest": digest(indices),
            "first_witness": witness,
        }
    triple_pair_names = [f"{a}|{b}" for a, b in pairs
                        if a in ZERO_CARRYING and b in ZERO_CARRYING]
    triple_supports_identical = len({
        support_sets[p] for p in triple_pair_names
    }) == 1
    triple_on_formed_worlds = all(
        all(world_of[i] in formed for i in support_sets[p])
        for p in triple_pair_names
    )

    def fractions_for(name, fam):
        total = totals[name]
        return {
            key: Fraction(sum(numerators[name][i] for i in idx), total)
            for key, idx in cells[fam].items()
        }
    tables = {(name, fam): fractions_for(name, fam)
              for name in CANDIDATE_NAMES for fam in FAMILY_ORDER}
    per_family = {}
    for fam in FAMILY_ORDER:
        row = {}
        for pair_name in triple_pair_names:
            a, b = pair_name.split("|")
            ta, tb = tables[(a, fam)], tables[(b, fam)]
            differing = sorted(k for k in ta if ta[k] != tb[k])
            row[pair_name] = {
                "cells": len(ta), "differing_cells": len(differing),
                "differing_cell_digest": digest([compact(list(k))
                                                 for k in differing]),
            }
        row["all_three_pairs_differ_on_the_same_cells"] = len({
            v["differing_cell_digest"]
            for k, v in row.items() if isinstance(v, dict)
        }) == 1
        per_family[fam] = row
    cert_f = {
        "certificate": "F_DIFFERENCE_SUPPORTS",
        "statement": (
            "the exact pairwise difference supports of the five candidate"
            " weightings under per-candidate normalization.  For the three"
            " zero-carrying candidates every pair differs on IDENTICALLY"
            " the same events (the formed-world block) and on identically"
            " the same cells of every declared family, while the exact"
            " fraction VALUES at those events differ -- equal difference"
            " supports are a support/cardinality fact only and are NOT"
            " equality of the weightings, which remain mathematically"
            " distinct"
        ),
        "pairwise": support_rows,
        "all_pairs_differ_somewhere": all(
            row["differing_events"] > 0 for row in support_rows.values()
        ),
        "zero_carrying_pairs": triple_pair_names,
        "zero_carrying_supports_identical_as_sets": triple_supports_identical,
        "zero_carrying_supports_all_on_formed_worlds":
            triple_on_formed_worlds,
        "per_family_zero_carrying": per_family,
        "label": FRACTION_LABEL,
    }
    cert_f["pass"] = bool(
        {k: v["differing_events"] for k, v in support_rows.items()}
        == EXPECTED["difference_support_cardinalities"]
        and cert_f["all_pairs_differ_somewhere"]
        and triple_supports_identical and triple_on_formed_worlds
        and all(
            per_family[fam][triple_pair_names[0]]["differing_cells"]
            == EXPECTED["per_family_differing_cells_zero_carrying_pairs"][fam]
            and per_family[fam]["all_three_pairs_differ_on_the_same_cells"]
            for fam in FAMILY_ORDER
        )
    )

    # ---- G: totals, mass lattices, verified factorizations --------------
    lattices = {}
    for name in CANDIDATE_NAMES:
        denominator = 1
        total = totals[name]
        for num in set(numerators[name]):
            denominator = lcm(denominator, Fraction(num, total).denominator)
        lattices[name] = denominator
    total_factors = {name: factorize(totals[name]) for name in CANDIDATE_NAMES}
    lattice_factors = {name: factorize(lattices[name])
                       for name in CANDIDATE_NAMES}
    factors_verified = all(
        factorization_verified(totals[name], total_factors[name])
        and factorization_verified(lattices[name], lattice_factors[name])
        for name in CANDIDATE_NAMES
    )
    sample_rows = []
    for seed in (905, 1905, 2905, 3905):
        indices = deterministic_indices(seed, 500, len(events))
        row_ok = True
        for name in CANDIDATE_NAMES:
            mass = Fraction(sum(numerators[name][i] for i in indices),
                            totals[name])
            if lattices[name] % mass.denominator != 0:
                row_ok = False
        sample_rows.append({"seed": seed, "subset_size": len(indices),
                            "reduced_denominators_divide_lattice": row_ok})
    cert_g = {
        "certificate": "G_MASS_LATTICES",
        "statement": (
            "totals and exact subset-mass lattices of the five candidate"
            " weightings with verified prime factorizations.  NECESSARY"
            " FILTER ONLY: if a subset of events has total mass p/q in"
            " lowest terms under a weighting, then q divides that"
            " weighting's lattice L (and L divides the total T).  No"
            " statement is made or implied about which denominators are"
            " ACHIEVED by actual subsets, about subset realizability,"
            " about separating any candidates, or about any selection"
        ),
        "totals": totals,
        "mass_lattices": lattices,
        "lattice_divides_total": {
            name: totals[name] % lattices[name] == 0
            for name in CANDIDATE_NAMES
        },
        "total_factorizations": {
            name: {str(p): e for p, e in sorted(total_factors[name].items())}
            for name in CANDIDATE_NAMES
        },
        "lattice_factorizations": {
            name: {str(p): e for p, e in sorted(lattice_factors[name].items())}
            for name in CANDIDATE_NAMES
        },
        "factorizations_verified": (
            "every factor passed deterministic Miller-Rabin and every"
            " product was recomposed to the factored value"
        ),
        "factorizations_verified_ok": factors_verified,
        "sampled_subset_denominator_checks": sample_rows,
        "label": FRACTION_LABEL,
    }
    cert_g["pass"] = bool(
        totals == EXPECTED["totals"]
        and lattices == EXPECTED["mass_lattices"]
        and total_factors == EXPECTED["total_factorizations"]
        and lattice_factors == EXPECTED["lattice_factorizations"]
        and factors_verified
        and all(cert_g["lattice_divides_total"].values())
        and all(r["reduced_denominators_divide_lattice"] for r in sample_rows)
    )

    # ---- H: falsifiers ---------------------------------------------------
    plant_dependent = [
        3 * numerators["M3_OCCUPATION_WEIGHTED"][i]
        + 5 * numerators["M4_FORMATION_LIFETIME"][i]
        for i in range(len(events))
    ]
    plant_independent = [0] * len(events)
    plant_independent[-1] = 1
    plant_relation_vector = [
        (1 if world_of[i] in formed else 0)
        * numerators["M2_PER_WORLD_UNIFORM"][i]
        for i in range(len(events))
    ]
    rank_with_dependent, _ = rank_by_rational_elimination(
        matrix + [plant_dependent]
    )
    rank_with_independent, _ = rank_by_rational_elimination(
        matrix + [plant_independent]
    )
    rank_with_relation, _ = rank_by_rational_elimination(
        matrix + [plant_relation_vector]
    )
    rank_dep_gram, _, _ = rank_by_gram_minors(matrix + [plant_dependent])
    rank_ind_gram, _, _ = rank_by_gram_minors(matrix + [plant_independent])
    rank_rel_gram, _, _ = rank_by_gram_minors(matrix + [plant_relation_vector])
    tampered_zero = dict(zero_counts)
    tampered_zero["M3_OCCUPATION_WEIGHTED"] += 1
    tampered_factors = {p: e for p, e in total_factors["M1_COUNTING"].items()}
    tampered_factors[2] = tampered_factors.get(2, 0) + 1
    cert_h = {
        "certificate": "H_FALSIFIERS",
        "planted_rank_dependent": {
            "construction": "3*M3 + 5*M4, an exact combination of two rows",
            "rank_with_row_added": rank_with_dependent,
            "gram_route": rank_dep_gram,
            "designed_outcome": "rank unchanged",
            "observed_as_designed": bool(
                rank_with_dependent == rank_a == rank_dep_gram
            ),
        },
        "planted_rank_independent": {
            "construction": (
                "the indicator of a single event.  Every candidate is"
                " world-constant (verified in certificate C) and the"
                " smallest world carries 64 events, so this vector is"
                " PROVABLY outside the span of the five"
            ),
            "rank_with_row_added": rank_with_independent,
            "gram_route": rank_ind_gram,
            "designed_outcome": "rank increases by exactly one",
            "observed_as_designed": bool(
                rank_with_independent == rank_a + 1 == rank_ind_gram
            ),
        },
        "planted_relation_vector": {
            "construction": (
                "the formed-world indicator times the per-world equaliser"
                " -- the vector (M4 + M5) / (boundaries + 1) that the"
                " world-coefficient identity actually equates M4 + M5 to"
            ),
            "rank_with_row_added": rank_with_relation,
            "gram_route": rank_rel_gram,
            "designed_outcome": (
                "rank unchanged: the vector lies INSIDE the span of the"
                " five, so the identity constrains nothing among them"
            ),
            "observed_as_designed": bool(
                rank_with_relation == rank_a == rank_rel_gram
            ),
        },
        "tampered_zero_count_detected": (
            tampered_zero != EXPECTED["zero_weight_events"]
        ),
        "tampered_factorization_detected": not factorization_verified(
            totals["M1_COUNTING"], tampered_factors
        ),
    }
    cert_h["pass"] = bool(
        cert_h["planted_rank_dependent"]["observed_as_designed"]
        and cert_h["planted_rank_independent"]["observed_as_designed"]
        and cert_h["planted_relation_vector"]["observed_as_designed"]
        and cert_h["tampered_zero_count_detected"]
        and cert_h["tampered_factorization_detected"]
    )

    # ---- I: deterministic double build ----------------------------------
    build_b = build_event_space()
    numerators_b, _, _, _, _, common_b = build_candidates(
        build_b["events"], build_b["scan"]["occ_global"],
        build_b["scan"]["formed"], build_b["scan"]["boundaries"],
    )
    rank_b2, _ = rank_by_rational_elimination(
        [numerators_b[name] for name in CANDIDATE_NAMES]
    )
    cert_i = {
        "certificate": "I_DOUBLE_BUILD",
        "event_digest_A": event_digest,
        "event_digest_B": digest(build_b["events"]),
        "weighting_digest_A": digest(
            {name: numerators[name] for name in CANDIDATE_NAMES}
        ),
        "weighting_digest_B": digest(
            {name: numerators_b[name] for name in CANDIDATE_NAMES}
        ),
        "rank_A": rank_a, "rank_B": rank_b2,
        "common_denominator_A": common, "common_denominator_B": common_b,
        "deterministic": bool(
            event_digest == digest(build_b["events"])
            and digest({name: numerators[name] for name in CANDIDATE_NAMES})
            == digest({name: numerators_b[name] for name in CANDIDATE_NAMES})
            and rank_a == rank_b2 and common == common_b
        ),
    }
    cert_i["pass"] = cert_i["deterministic"]

    # ---- J: runtime ------------------------------------------------------
    elapsed = round(monotonic() - started, 3)
    cert_j = {
        "certificate": "J_RUNTIME",
        "elapsed_sec": elapsed,
        "budget_sec": AUDIT_TIMEOUT_SEC,
        "within_budget": elapsed <= AUDIT_TIMEOUT_SEC,
        "scope": (
            "the full event census of the stipulated in-file model"
            f" ({HORIZON} orbits, {boundaries} boundaries, {len(events)}"
            " events); no sub-census restriction was needed"
        ),
    }
    cert_j["pass"] = cert_j["within_budget"]

    certificates = (
        ("A_SOURCE_CONTROLS", cert_a), ("B_MODEL_BUILD", cert_b),
        ("C_RANK", cert_c), ("D_COEFFICIENT_IDENTITY", cert_d),
        ("E_ZERO_SETS", cert_e), ("F_DIFFERENCE_SUPPORTS", cert_f),
        ("G_MASS_LATTICES", cert_g), ("H_FALSIFIERS", cert_h),
        ("I_DOUBLE_BUILD", cert_i), ("J_RUNTIME", cert_j),
    )
    checks = {name: bool(payload["pass"]) for name, payload in certificates}

    certified_statements = {
        "base_rank_statement": (
            f"on the stipulated model the five candidate weightings have"
            f" rank {rank_a} as functions on the {len(events)}-event"
            " census (three agreeing routes; an exhibited nonsingular"
            " 5 x 5 minor); the three zero-carrying candidates alone have"
            f" rank {rank_triple_a}"
        ),
        "coefficient_identity_statement": (
            "the world-coefficient identity a4 + a5 = (boundaries + 1) *"
            f" [formed] holds on all {len(worlds)} world rows"
            f" ({len(coeff_violations)} violations); the candidate"
            " combination (boundaries+1)*M2 - M4 - M5 has nonzero"
            f" event-level residual on exactly the {len(residual_nonzero)}"
            " events of the never-formed block, so the identity induces no"
            " dependence among the five event-level weightings"
        ),
        "zero_set_statement": (
            "M1 and M2 have EMPTY zero sets (minimum event numerators 1"
            " and 8320); the zero sets of M3 and M4 are IDENTICAL AS SETS"
            f" and equal the never-formed block ({len(never_formed_events)}"
            " events, all bank-tag writes); the zero set of M5 strictly"
            " contains it (the worlds formed at moment 0 add"
            f" {len(m5_extra)} events)"
        ),
        "difference_support_statement": (
            "all ten candidate pairs differ somewhere; the three"
            " zero-carrying pairs differ on IDENTICALLY the same"
            f" {len(support_sets[triple_pair_names[0]])} events (the"
            " formed-world block) and the same cells of every declared"
            " family, while the exact fraction values at those events"
            " differ -- an equal-support fact, not equality of weightings"
        ),
        "mass_lattice_statement": (
            "the totals and exact subset-mass lattices factor as recorded,"
            " with every factorization machine-verified; divisibility of a"
            " demanded denominator into the lattice is a NECESSARY"
            " condition only, and no subset realizability is decided"
        ),
        "one_way_positivity_lemma": cert_e["one_way_positivity_lemma"][
            "statement"],
    }

    machine_status = {
        "claim_type": "bounded_theorem",
        "surface_label": "bounded support note",
        "surface_reading": "conditional finite-model support",
        "conditional_on": (
            "the stipulated in-file composed record-write model and its"
            " declared scope inputs (banks, source counts, horizon,"
            " dead-window lengths, register cap), all stipulated"
            " computational boundary conditions, not measured and not"
            " axiom-derived; identification of this model with any landed"
            " substrate is an OPEN bridge"
        ),
        "boundary": BOUNDARY_STATEMENT,
        "expressly_absent_claims": [
            "no measure selection and no candidate elimination",
            "no framework-Admissibility compatibility claim",
            "no interface, pullback, or bridge claim from any other lane",
            "no symmetry or covariance claim on event atoms",
            "no observable, no operational bridge, no experiment",
            "no probability, no occurrence rule, no update law",
            "no negative claim of any universal form",
        ],
        "review_record": (
            "this package is the review-loop SALVAGE of the rejected"
            " Cycle-905 submission (PR #5967, FAIL/SALVAGE_REJECT); only"
            " the finite calculations the review named durable are carried"
            " here, recomputed self-contained; see the source note's"
            " Review record for the rejection grounds"
        ),
    }

    receipt = {
        "cycle": 905,
        "role": "salvage primary",
        "question": (
            "Cycle 905 salvage -- carry the durable exact finite"
            " calculations of the rejected Cycle-905 package as"
            " conditional finite-model support on a stipulated in-file"
            " model."
        ),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "machine_status": machine_status,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "label_on_every_fraction": FRACTION_LABEL,
        "rank": rank_a,
        "rank_routes": {
            "rational_elimination": rank_a, "gram_laplace": rank_b,
            "world_reduction_crosscheck": rank_c,
        },
        "zero_carrying_triple_rank": rank_triple_a,
        "nonsingular_minor": cert_c["exhibited_nonsingular_minor"],
        "coefficient_identity_violations": len(coeff_violations),
        "residual_nonzero_events": len(residual_nonzero),
        "residual_set_equals_never_formed_block":
            cert_d["residual_set_equals_never_formed_block"],
        "zero_weight_events": zero_counts,
        "min_event_numerators": min_numerators,
        "zero_set_identities": cert_e["set_identities"],
        "difference_support_cardinalities": {
            k: v["differing_events"] for k, v in support_rows.items()
        },
        "difference_support_digests": {
            k: v["support_digest"] for k, v in support_rows.items()
        },
        "zero_carrying_supports_identical_as_sets": triple_supports_identical,
        "per_family_differing_cells_zero_carrying": {
            fam: per_family[fam][triple_pair_names[0]]["differing_cells"]
            for fam in FAMILY_ORDER
        },
        "totals": totals,
        "mass_lattices": lattices,
        "total_factorizations": cert_g["total_factorizations"],
        "lattice_factorizations": cert_g["lattice_factorizations"],
        "certified_statements": certified_statements,
        "event_space_digest": event_digest,
        "deterministic_double_build": cert_i["deterministic"],
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "elapsed_sec": elapsed,
        "scope": (
            "the full realized record-write census of the stipulated"
            f" in-file model at horizon {HORIZON} orbits ({len(events)}"
            f" events over {len(worlds)} worlds), built from the pinned"
            " landed Cycle-719 core alone.  Exact rational arithmetic"
            " throughout; no probability, no occurrence rule, no update"
            " law, no selection."
        ),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_pins": [
            {"path": p, "sha256": cert_a["sha256"][p],
             "git_blob": cert_a["git_blobs"][p]}
            for p in AUDIT_INPUT_PATHS
        ],
    }
    receipt["science_digest"] = digest({
        "rank": rank_a,
        "zero_counts": zero_counts,
        "residual_events": len(residual_nonzero),
        "totals": totals,
        "lattices": lattices,
        "event_digest": event_digest,
    })
    out_path = (ROOT / "outputs"
                / "weighting_exact_algebra_cycle905_receipt_2026_08_08.json")
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")

    lines = [
        "CYCLE905_WEIGHTING_EXACT_ALGEBRA_SALVAGE",
        "CONDITIONAL_FINITE_MODEL_SUPPORT_ON_A_STIPULATED_IN_FILE_MODEL",
        "EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY",
        "NO_SELECTION_NO_ELIMINATION_NO_PROBABILITY_NO_INTERFACE_CLAIM",
    ]
    for name, payload in certificates:
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    for key, statement in certified_statements.items():
        lines.append("STATEMENT " + key + " " + statement)
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 905, "checks": checks,
        "rank": rank_a,
        "zero_weight_events": zero_counts,
        "elapsed_sec": elapsed,
        "pass": all(checks.values()),
    }))
    lines.append(
        "CYCLE905_WEIGHTING_EXACT_ALGEBRA_"
        + ("PASS" if all(checks.values()) else "HONEST_FAIL")
    )
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
