#!/usr/bin/env python3
"""Cycle 878 INDEPENDENT CHECK -- specified to REFUTE.

Target: scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py and
its committed stdout cache.  The target runner, the Cycle-867 composed
record-write primary and the Cycle-863 replay substrate are ALL
SHA/blob-pinned text/AST-only inputs and are BLOCKLISTED from import: the
only computational import is the landed Cycle-719 core.  Everything the
target claims is rebuilt here from that core with independent code.

Attacks mounted:

CK_A  Rebuild the realized record-write event space from scratch with a
      DIFFERENT lane bit-layout (census index i occupies bit n-i, the
      duplicate-consistency lane sits at bit 0), an independently derived
      dirty partition, an independently derived dead-wire register, and
      an independently derived slot allocation.  Compare cell-for-cell
      against the target's cache: cardinalities, per-tag counts, the
      per-world event-count histogram, and the event-space digest.  Then
      re-execute a declared SAMPLE of worlds through the slow per-lane
      semantic path (no bit-parallelism at all) and demand the same
      (world, moment, tag, ordinal, content) rows.
CK_B  Rebuild the refinement/crossing lattice by a DIFFERENT algorithm --
      explicit set-inclusion of cell index sets, not key-determines-key --
      and demand every claimed refinement be witnessed by containment and
      every claimed crossing be witnessed by an explicit pair of cells
      that neither contains.
CK_C  Recompute the measure-candidate inventory with plain Fraction
      arithmetic (the target uses integer numerators over a common
      denominator; agreement is then a real cross-check).  Attack the
      additivity certification with ADVERSARIAL family choices: an
      overlapping pseudo-family and a non-covering pseudo-family MUST
      break additivity for every candidate, otherwise the target's
      additivity certificate is vacuous.  Attack the covariance
      certification by feeding the SAME orbit-constancy predicate a
      deterministic NON-symmetry (the transposition of the lightest and
      heaviest world cells): it must break covariance wherever the world
      masses are not already constant, and the certified verdicts must
      separate the candidates, otherwise the predicate is inert.
CK_D  Recompute every exact fraction table and every table digest,
      recompute the pairwise disagreement matrix and the atom-level
      disagreement counts, and verify that every emitted number carries
      the "bookkeeping fraction, not probability" label.
CK_E  Verify the verbatim axiom-baseline exclusion quote byte-for-byte in
      the pinned in-tree source AND inside the target's own emitted
      certificate (no paraphrase), plus all shas/blobs, determinism, the
      declared caps, runtime and stdout budgets.

A FAIL here is a real refutation of the target, not a checker bug to be
smoothed over.  bounded_theorem, authority none, audit unset.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
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
    "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py",
    "logs/runner-cache/frontier_cycle878_event_space_groundwork_2026_07_28.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
COMPUTATIONAL_INPUT_PATHS = AUDIT_INPUT_PATHS[:1]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:4]
TEXT_ONLY_PATHS = AUDIT_INPUT_PATHS[4:]
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "49605f6d0730e224d6c4cd25a182ec49e0c7d2f2316851bc2755632dcbe2c828",
    AUDIT_INPUT_PATHS[3]: "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    AUDIT_INPUT_PATHS[4]: "dbf33c9677cfff61e88f0bfe100fa09ae47a30d5aeb6d58b5a370dadb3c16a6b",
    AUDIT_INPUT_PATHS[5]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
    AUDIT_INPUT_PATHS[3]: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    AUDIT_INPUT_PATHS[4]: "ab88312b24487d1625cbbc1d75b79c44fc2062c4",
    AUDIT_INPUT_PATHS[5]: "4a863da1f3f255354839277271a3a69a5c205133",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
DETERMINISM_ORBITS = 192
SEQUENTIAL_WORLDS = 12
SEQUENTIAL_ORBITS = 96
FRACTION_LABEL = "bookkeeping fraction, not probability"
EXCLUSION_NEEDLE = (
    "- context selection, measurement basis selection, Born weights,"
    " probability\n  rules, update laws, decoherence mechanisms, and"
    " formation rules (which\n  admissible possibility a new record locks,"
    " at which site, with what weight,\n  or at what rate);"
)
CANDIDATE_NAMES = (
    "M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
)
CONTROL_NAME = "M0_CONTENT_DIVERSITY"
FAMILY_ORDER = (
    "F_WORLD", "F_TAG", "F_TAG_ORDINAL", "F_MOMENT", "F_ORBIT",
    "F_CONTENT", "F_WORLD_TAG", "F_ATOM",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# ---------------------------------------------------------------------------
# Independent rebuild of the fixture
# ---------------------------------------------------------------------------

def cyclically_isolated(positions, stations):
    """No two occupied stations are cyclic neighbours (independent form:
    all ordered pairs tested against a circular distance of one)."""
    for a in positions:
        for b in positions:
            if a != b and ((a - b) % stations == 1 or (b - a) % stations == 1):
                return False
    return True


def rebuild_seeds(program):
    banks, links = K.B.chain_genesis(BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(BANKS)
    rows = []
    for event in range(2 * BANKS):
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
    return dict(rows)


def rebuild_census(program):
    stations = len(program)
    keys = []
    for k in range(MIN_SOURCES, MAX_SOURCES + 1):
        for positions in combinations(range(stations), k):
            if not cyclically_isolated(positions, stations):
                continue
            for event in range(2 * BANKS):
                keys.append((k, event, positions))
    return tuple(sorted(keys))


def rebuild_dirty_partition():
    """Independently marked dirty coordinates (single-bit pack marking)."""
    banks0, links0 = K.B.chain_genesis(BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    watched = (
        K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
        *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK,
    )
    per_bank = []
    for bank_index in range(len(zero_banks)):
        rows = set()
        for wire in watched:
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
            rows.add(diffs[0])
        per_bank.append(tuple(sorted(rows)))
    link_rows = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(r) for r in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(tuple(r) for r in changed))
            diffs = [
                i for i, (l, r) in enumerate(zip(baseline, marked)) if l != r
            ]
            if len(diffs) != 1:
                raise AssertionError(("link marker", diffs))
            link_rows.add(diffs[0])
    return tuple(per_bank), tuple(sorted(link_rows)), K.R3.X.SOURCE_POINTER


def initial_states(program, seeds, census):
    stations = len(program)
    states = []
    failures = 0
    for _k, event, positions in census:
        after, rail_a, rail_b, _t = K.run_orbit(
            seeds[event], program, token_positions=positions
        )
        expected = tuple(int(s in positions) for s in range(stations))
        failures += (rail_a != expected) or any(rail_b)
        states.append(after)
    return tuple(states), failures


def bitpos(index, n):
    """DIFFERENT layout from the target: census index i occupies bit n-i,
    and the duplicate-consistency copy of census[0] sits at bit 0."""
    return n - index


def pack_reversed(states, n):
    width = len(states[0])
    columns = [0] * width
    for index, state in enumerate(states):
        bit = 1 << bitpos(index, n)
        for wire in range(width):
            if state[wire]:
                columns[wire] |= bit
    duplicate = states[0]
    for wire in range(width):
        if duplicate[wire]:
            columns[wire] |= 1
    return columns


def step_schedules(program, census, n):
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = 0
            for index, (_k, _e, positions) in enumerate(census):
                if (station - step) % stations in positions:
                    mask |= 1 << bitpos(index, n)
            if (census[0][2] and (station - step) % stations in census[0][2]):
                mask |= 1
            if mask:
                for gate in K.mapped_macro(row):
                    if gate.kind == "X":
                        schedule.append((0, gate.wires[0], 0, 0, mask))
                    elif gate.kind == "CNOT":
                        schedule.append(
                            (1, gate.wires[0], gate.wires[1], 0, mask)
                        )
                    elif gate.kind == "TOF":
                        schedule.append(
                            (2, gate.wires[0], gate.wires[1],
                             gate.wires[2], mask)
                        )
                    else:
                        raise ValueError(("gate", gate))
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_chunks(schedules):
    fns = []
    for schedule in schedules:
        src = ["def chunk(c):"]
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["chunk"])
    return tuple(fns)


def clean_mask(columns, indices, universe):
    dirty = 0
    for wire in indices:
        dirty |= columns[wire]
    return universe & ~dirty


def bits_of(mask):
    out = []
    while mask:
        low = mask & -mask
        out.append(low.bit_length() - 1)
        mask ^= low
    return out


def lane_bits(columns, bit):
    probe = 1 << bit
    return tuple(int(bool(col & probe)) for col in columns)


def true_step_chunks(program, positions):
    stations = len(program)
    macros = [K.mapped_macro(row) for row in program]
    chunks = []
    for step in range(stations):
        gates = []
        for station in range(stations):
            if (station - step) % stations in positions:
                gates.extend(macros[station])
        chunks.append(tuple(gates))
    return tuple(chunks)


# ---------------------------------------------------------------------------
# Independent composed scan
# ---------------------------------------------------------------------------

def rebuild_rig(program, census, states, n):
    chunks = compile_chunks(step_schedules(program, census, n))
    universe = (1 << (n + 1)) - 1
    work = pack_reversed(states, n)
    acc = list(work)
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in chunks:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    dead = tuple(w for w in range(len(acc)) if (acc[w] & universe) == 0)
    touched: set = set()
    for schedule in step_schedules(program, census, n):
        for kind, a, b, c3, _m in schedule:
            if kind == 0:
                touched.add(a)
            elif kind == 1:
                touched.update((a, b))
            else:
                touched.update((a, b, c3))
    safe = tuple(w for w in dead if w not in touched)
    tags = [("F", 0)] + [
        (f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    if len(safe) < len(tags):
        raise AssertionError(("safe slots", len(safe), len(tags)))
    return {
        "chunks": chunks,
        "dead": dead,
        "safe": safe,
        "slot_of": {tag: safe[i] for i, tag in enumerate(tags)},
        "touched": touched,
    }


def rebuild_scan(program, census, states, rig, orbits, n):
    slot_of = rig["slot_of"]
    chunks = rig["chunks"]
    columns = pack_reversed(states, n)
    per_bank, links, source_ptr = rebuild_dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    universe = (1 << (n + 1)) - 1
    census_mask = universe ^ 1
    slot_wires = set(slot_of.values())
    watch_dead = tuple(w for w in rig["dead"] if w not in slot_wires)

    events: list[tuple] = []
    occ_global = [0] * n
    ordinal_of = [[0, 0] for _ in range(n)]
    formed: dict[int, int] = {}
    beyond_cap = 0
    rewrites = 0
    dead_acc = 0
    mismatches = 0

    def write(tag, index):
        nonlocal rewrites
        wire = slot_of[tag]
        bit = 1 << bitpos(index, n)
        if columns[wire] & bit:
            rewrites += 1
        columns[wire] |= bit

    def content(index):
        return sha256(
            bytes(lane_bits(columns, bitpos(index, n)))
        ).hexdigest()[:16]

    g0 = clean_mask(columns, global_dirty, universe)
    mismatches += int(bool(g0 & (1 << bitpos(0, n))) != bool(g0 & 1))
    prev = [
        clean_mask(columns, per_bank[b], universe) & census_mask
        for b in (0, 1)
    ]
    initial_clean = 0
    for bit in bits_of(g0 & census_mask):
        index = n - bit
        occ_global[index] += 1
        formed[index] = 0
        write(("F", 0), index)
        events.append((index, 0, "F", 0, content(index)))
        initial_clean += 1

    boundary = 0
    for orbit in range(1, orbits + 1):
        for chunk in chunks:
            chunk(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, universe)
            mismatches += int(bool(g & (1 << bitpos(0, n))) != bool(g & 1))
            for bit in bits_of(g & census_mask):
                index = n - bit
                occ_global[index] += 1
                if index not in formed:
                    formed[index] = boundary
                    write(("F", 0), index)
                    events.append((index, boundary, "F", 0, content(index)))
            for b in (0, 1):
                bm = clean_mask(columns, per_bank[b], universe) & census_mask
                for bit in bits_of(bm & ~prev[b]):
                    index = n - bit
                    ordinal = ordinal_of[index][b]
                    if ordinal < REGISTER_CAP:
                        write((f"B{b}", ordinal), index)
                        events.append(
                            (index, boundary, f"B{b}", ordinal,
                             content(index))
                        )
                    else:
                        beyond_cap += 1
                    ordinal_of[index][b] = ordinal + 1
                prev[b] = bm
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in watch_dead:
                    dead_acc |= columns[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in watch_dead:
                dead_acc |= columns[w]
    events.sort(key=lambda e: (e[1], _tag_rank(e[2]), e[0]))
    return {
        "events": events,
        "occ_global": occ_global,
        "formed": formed,
        "beyond_cap": beyond_cap,
        "rewrites": rewrites,
        "dead_conflicts": bin(dead_acc & universe).count("1"),
        "mismatches": mismatches,
        "boundaries": boundary,
        "initial_clean": initial_clean,
        "global_dirty": global_dirty,
        "per_bank": per_bank,
    }


def _tag_rank(tag):
    return {"F": 0, "B0": 1, "B1": 2}[tag]


def sequential_events(program, seeds, census, rig, index, orbits,
                      global_dirty, per_bank, n):
    """Slow path: one world, no bit-parallelism, plain semantic gates."""
    _k, event, positions = census[index]
    stations = len(program)
    chunks = true_step_chunks(program, positions)
    state = list(K.run_orbit(
        seeds[event], program, token_positions=positions
    )[0])
    slot_of = rig["slot_of"]
    rows = []
    ordinal = [0, 0]
    formed = False

    def clean(indices):
        return all(state[w] == 0 for w in indices)

    def content():
        return sha256(bytes(state)).hexdigest()[:16]

    if clean(global_dirty):
        formed = True
        state[slot_of[("F", 0)]] = 1
        rows.append((index, 0, "F", 0, content()))
    prev = [clean(per_bank[b]) for b in (0, 1)]
    for boundary in range(1, orbits * stations + 1):
        state = list(K.A.apply_semantic(
            tuple(state), chunks[(boundary - 1) % stations]
        ))
        if clean(global_dirty) and not formed:
            formed = True
            state[slot_of[("F", 0)]] = 1
            rows.append((index, boundary, "F", 0, content()))
        for b in (0, 1):
            now = clean(per_bank[b])
            if now and not prev[b]:
                if ordinal[b] < REGISTER_CAP:
                    state[slot_of[(f"B{b}", ordinal[b])]] = 1
                    rows.append(
                        (index, boundary, f"B{b}", ordinal[b], content())
                    )
                ordinal[b] += 1
            prev[b] = now
    return rows


# ---------------------------------------------------------------------------
# Families, lattice, measures -- independent implementations
# ---------------------------------------------------------------------------

def family_key(fam, event, stations):
    lane, moment, tag, ordinal, cont = event
    if fam == "F_WORLD":
        return ("w", lane)
    if fam == "F_TAG":
        return ("t", tag)
    if fam == "F_TAG_ORDINAL":
        return ("to", tag, ordinal)
    if fam == "F_MOMENT":
        return ("m", moment)
    if fam == "F_ORBIT":
        return ("o", 0 if moment == 0 else ((moment - 1) // stations) + 1)
    if fam == "F_CONTENT":
        return ("c", cont)
    if fam == "F_WORLD_TAG":
        return ("wt", lane, tag)
    if fam == "F_ATOM":
        return ("a", lane, tag, ordinal)
    raise ValueError(fam)


def cell_index_sets(events, fam, stations):
    out: dict = {}
    for i, event in enumerate(events):
        out.setdefault(family_key(fam, event, stations), set()).add(i)
    return out


def owner_list(cells_b, size):
    """Owner cell of every event index, derived from the cell index sets
    themselves (not from a fresh key computation)."""
    owner = [None] * size
    for key, idx in cells_b.items():
        for i in idx:
            owner[i] = key
    return owner


def refines_by_containment(cells_a, owner_b):
    """Set-inclusion algorithm: every A-cell must sit inside one B-cell."""
    for _key, idx in cells_a.items():
        it = iter(idx)
        first = owner_b[next(it)]
        for i in it:
            if owner_b[i] != first:
                return False
    return True


def crossing_witness(cells_a, cells_b):
    for ka, ia in cells_a.items():
        for kb, ib in cells_b.items():
            if (ia & ib) and (ia - ib) and (ib - ia):
                return {"cell_a": compact(list(ka)),
                        "cell_b": compact(list(kb)),
                        "overlap": len(ia & ib),
                        "a_minus_b": len(ia - ib),
                        "b_minus_a": len(ib - ia)}
    return None


def candidate_weights(events, occ_global, formed, boundaries):
    """Plain-Fraction reimplementation (the target uses integer numerators
    over a common denominator; agreement is a genuine cross-check)."""
    per_world = Counter(e[0] for e in events)
    supported = sorted(per_world)
    weights: dict[str, list[Fraction]] = {}

    def world_weighted(a_of):
        total = sum(a_of(w) for w in supported)
        if total == 0:
            return [Fraction(0)] * len(events)
        return [
            Fraction(a_of(e[0]), total * per_world[e[0]]) for e in events
        ]

    weights["M1_COUNTING"] = [Fraction(1)] * len(events)
    weights["M2_PER_WORLD_UNIFORM"] = world_weighted(lambda w: 1)
    weights["M3_OCCUPATION_WEIGHTED"] = world_weighted(
        lambda w: occ_global[w]
    )
    weights["M4_FORMATION_LIFETIME"] = world_weighted(
        lambda w: (boundaries - formed[w] + 1) if w in formed else 0
    )
    weights["M5_FORMATION_MOMENT"] = world_weighted(
        lambda w: formed[w] if w in formed else 0
    )
    return weights, per_world, supported


# ---------------------------------------------------------------------------
# Target cache parsing
# ---------------------------------------------------------------------------

def parse_cache(text):
    certs = {}
    summary = None
    for line in text.splitlines():
        if line.startswith("CERTIFICATE "):
            _kw, name, _status, payload = line.split(" ", 3)
            certs[name] = json.loads(payload)
        elif line.startswith("SUMMARY_JSON "):
            summary = json.loads(line[len("SUMMARY_JSON "):])
    return certs, summary


def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in COMPUTATIONAL_INPUT_PATHS + TEXT_AST_ONLY_PATHS:
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
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "blocked_modules_loaded": tuple(
            m for m in BLOCKLISTED_MODULES if m in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
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


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    controls = source_controls()
    cache_text = (ROOT / AUDIT_INPUT_PATHS[4]).read_text(encoding="utf-8")
    certs, summary = parse_cache(cache_text)
    t_a = certs["A_EVENT_SPACE"]
    t_b = certs["B_MEASURE_CANDIDATE_INVENTORY"]
    t_c = certs["C_FRACTION_LEDGER"]
    t_d = certs["D_BOUNDARY_WHAT_IS_NOT_SUPPLIED"]
    t_e = certs["E_CONTROLS"]

    program = K.interleaved_program(BANKS)
    stations = len(program)
    seeds = rebuild_seeds(program)
    census = rebuild_census(program)
    n = len(census)
    states, init_fail = initial_states(program, seeds, census)
    rig = rebuild_rig(program, census, states, n)
    scan = rebuild_scan(program, census, states, rig, HORIZON, n)
    events = scan["events"]
    total_events = len(events)

    # ---- CK_A: event-space rebuild ----------------------------------------
    target_events_digest = t_e["event_space_digest"]
    target_order = sorted(
        events, key=lambda e: (e[0], e[1], e[2], e[3], e[4])
    )
    # The target emits events in scan order; rebuild both orderings so an
    # ordering convention cannot mask a content difference.
    scan_order = sorted(events, key=lambda e: (e[1], _tag_rank(e[2]), e[0]))
    per_world_counts = Counter(e[0] for e in events)
    tag_counts = dict(sorted(Counter(e[2] for e in events).items()))
    histogram = dict(sorted(Counter(per_world_counts.values()).items()))
    multiset_digest = digest(sorted(compact(list(e)) for e in events))

    sample_indices = sorted(per_world_counts)[:SEQUENTIAL_WORLDS]
    seq_rows = []
    for index in sample_indices:
        seq_rows.extend(sequential_events(
            program, seeds, census, rig, index, SEQUENTIAL_ORBITS,
            scan["global_dirty"], scan["per_bank"], n
        ))
    fast_rows = [
        e for e in events
        if e[0] in set(sample_indices)
        and e[1] <= SEQUENTIAL_ORBITS * stations
    ]
    seq_sorted = sorted(seq_rows)
    fast_sorted = sorted(fast_rows)
    sequential_agrees = seq_sorted == fast_sorted
    seq_coord_agrees = (
        sorted(r[:4] for r in seq_rows) == sorted(r[:4] for r in fast_rows)
    )

    ck_a = {
        "certificate": "CK_A_EVENT_SPACE_REBUILD",
        "independence": (
            "census, seeds, initial states, dirty partition, schedules,"
            " dead wires and slot allocation all rebuilt from the"
            " Cycle-719 core with a reversed lane bit-layout; the target"
            " runner and its two upstream primaries are blocklisted"
        ),
        "rebuilt_event_cardinality": total_events,
        "target_event_cardinality": t_a["event_cardinality"],
        "cardinality_agrees": total_events == t_a["event_cardinality"],
        "rebuilt_events_by_tag": tag_counts,
        "tag_counts_agree": tag_counts == t_a["events_by_tag"],
        "rebuilt_per_world_histogram": histogram,
        "histogram_agrees":
            {str(k): v for k, v in histogram.items()}
            == {str(k): v for k, v in
                t_a["per_world_event_count_histogram_eventcount_to_worlds"]
                .items()},
        "rebuilt_worlds_with_events": len(per_world_counts),
        "worlds_with_events_agree":
            len(per_world_counts) == t_a["worlds_with_at_least_one_event"],
        "event_multiset_digest": multiset_digest,
        "event_space_digest_scan_order": digest(scan_order),
        "event_space_digest_world_order": digest(target_order),
        "target_event_space_digest": target_events_digest,
        "digest_matches_some_declared_order": target_events_digest in (
            digest(scan_order), digest(target_order)
        ),
        "rebuilt_beyond_cap": scan["beyond_cap"],
        "beyond_cap_agrees": scan["beyond_cap"] == t_a["declared_caps"][
            "bank_edge_events_beyond_cap_not_wire_visible"],
        "rebuilt_initial_global_clean": scan["initial_clean"],
        "cycle867_relation_agrees": (
            scan["initial_clean"]
            == t_a["relation_to_landed_cycle867"][
                "cycle867_global_tag_writes_at_boundary_zero"]
            and scan["initial_clean"]
            == t_a["relation_to_landed_cycle867"]["f_events_at_moment_zero"]
        ),
        "rebuilt_integrity": {
            "write_once_violations": scan["rewrites"],
            "dead_activation_conflicts": scan["dead_conflicts"],
            "duplicate_lane_mismatches": scan["mismatches"],
            "initial_state_failures": init_fail,
            "dead_wires": len(rig["dead"]),
            "safe_slot_pool": len(rig["safe"]),
            "slots_in_touched_wires":
                len(set(rig["slot_of"].values()) & rig["touched"]),
        },
        "integrity_agrees": (
            scan["rewrites"]
            == t_a["composed_model_integrity"]["write_once_violations"]
            and scan["dead_conflicts"]
            == t_a["composed_model_integrity"]["dead_activation_conflicts"]
            and len(rig["dead"])
            == t_a["composed_model_integrity"]["dead_wires"]
            and len(rig["safe"])
            == t_a["composed_model_integrity"]["safe_slot_pool"]
        ),
        "sequential_probe": {
            "declared_worlds": len(sample_indices),
            "declared_orbits": SEQUENTIAL_ORBITS,
            "rows_from_slow_path": len(seq_rows),
            "rows_from_bit_parallel": len(fast_rows),
            "coordinates_agree": seq_coord_agrees,
            "coordinates_and_content_agree": sequential_agrees,
            "statement": (
                "one world at a time through K.A.apply_semantic with no"
                " bit-parallelism, its own register writes, and its own"
                " clean predicate"
            ),
        },
    }
    ck_a["pass"] = bool(
        ck_a["cardinality_agrees"] and ck_a["tag_counts_agree"]
        and ck_a["histogram_agrees"] and ck_a["worlds_with_events_agree"]
        and ck_a["digest_matches_some_declared_order"]
        and ck_a["beyond_cap_agrees"] and ck_a["cycle867_relation_agrees"]
        and ck_a["integrity_agrees"] and sequential_agrees
        and init_fail == 0
    )

    # ---- CK_B: lattice rebuilt by containment ------------------------------
    cellsets = {
        fam: cell_index_sets(events, fam, stations) for fam in FAMILY_ORDER
    }
    partitions = {
        fam: sum(len(v) for v in cellsets[fam].values()) == total_events
        for fam in FAMILY_ORDER
    }
    owners = {
        fam: owner_list(cellsets[fam], total_events) for fam in FAMILY_ORDER
    }
    rebuilt_matrix = {}
    for a in FAMILY_ORDER:
        for b in FAMILY_ORDER:
            if a != b:
                rebuilt_matrix[f"{a}<={b}"] = refines_by_containment(
                    cellsets[a], owners[b]
                )
    matrix_agrees = rebuilt_matrix == t_a["refinement_matrix_a_refines_b"]
    rebuilt_crossing = tuple(sorted(
        f"{a}~{b}" for i, a in enumerate(FAMILY_ORDER)
        for b in FAMILY_ORDER[i + 1:]
        if not rebuilt_matrix[f"{a}<={b}"] and not rebuilt_matrix[f"{b}<={a}"]
    ))
    crossing_agrees = list(rebuilt_crossing) == list(
        t_a["crossing_pairs_neither_refines_the_other"]
    )
    crossing_witnesses = {}
    all_crossings_witnessed = True
    for label in rebuilt_crossing:
        a, b = label.split("~")
        witness = crossing_witness(cellsets[a], cellsets[b])
        if witness is None:
            all_crossings_witnessed = False
        elif len(crossing_witnesses) < 4:
            crossing_witnesses[label] = witness
    atom_sizes = Counter(len(v) for v in cellsets["F_ATOM"].values())
    duplicate_atoms = sum(1 for v in cellsets["F_ATOM"].values() if len(v) > 1)
    ck_b = {
        "certificate": "CK_B_LATTICE_BY_CONTAINMENT",
        "algorithm": (
            "explicit set-inclusion over cell index sets, not the target's"
            " key-determines-key test"
        ),
        "cells_per_family": {
            fam: len(cellsets[fam]) for fam in FAMILY_ORDER
        },
        "cells_per_family_agrees": {
            fam: len(cellsets[fam]) for fam in FAMILY_ORDER
        } == t_a["cells_per_family"],
        "families_are_partitions": partitions,
        "refinement_matrix_agrees": matrix_agrees,
        "banktag_ordinal_refines_global_tag":
            rebuilt_matrix["F_TAG_ORDINAL<=F_TAG"],
        "banktag_refinement_agrees":
            rebuilt_matrix["F_TAG_ORDINAL<=F_TAG"]
            == t_a["banktag_ordinal_refines_global_tag"],
        "crossing_pairs_agree": crossing_agrees,
        "every_claimed_crossing_has_a_witness": all_crossings_witnessed,
        "crossing_witness_sample": crossing_witnesses,
        "atom_cell_size_histogram": dict(sorted(atom_sizes.items())),
        "duplicate_atom_cells_found": duplicate_atoms,
        "atoms_are_singletons_agrees":
            (duplicate_atoms == 0) == t_a["atoms_are_singletons"],
    }
    ck_b["pass"] = bool(
        ck_b["cells_per_family_agrees"] and all(partitions.values())
        and matrix_agrees and crossing_agrees and all_crossings_witnessed
        and ck_b["banktag_refinement_agrees"]
        and ck_b["atoms_are_singletons_agrees"] and duplicate_atoms == 0
    )

    # ---- CK_C: measure inventory + adversarial attacks ---------------------
    weights, per_world, supported = candidate_weights(
        events, scan["occ_global"], scan["formed"], scan["boundaries"]
    )
    contents = [e[4] for e in events]
    totals = {
        name: sum(weights[name], Fraction(0)) for name in CANDIDATE_NAMES
    }
    masses = {
        fam: {
            name: {
                key: sum((weights[name][i] for i in idx), Fraction(0))
                for key, idx in cellsets[fam].items()
            }
            for name in CANDIDATE_NAMES
        }
        for fam in FAMILY_ORDER
    }
    inventory_agrees = True
    rebuilt_rows = {}
    for name in CANDIDATE_NAMES:
        target_row = t_b["candidates"][name]
        additive = all(
            sum(masses[fam][name].values(), Fraction(0)) == totals[name]
            for fam in FAMILY_ORDER
        )
        normalizable = totals[name] > 0
        support = all(w > 0 for w in weights[name])
        zeros = sum(1 for w in weights[name] if w == 0)
        row = {
            "additive": additive,
            "normalizable": normalizable,
            "total_mass": fr(totals[name]),
            "support_faithful": support,
            "zero_weight_events": zeros,
            "admissible": bool(additive and normalizable),
        }
        row["agrees"] = (
            additive == target_row[
                "finite_additivity_over_certified_disjoint_families"]
            and normalizable == target_row["normalizable"]
            and fr(totals[name]) == target_row["total_mass"]
            and support == target_row[
                "support_faithful_disclosed_extra_diagnostic"]
            and zeros == target_row["zero_weight_events"]
            and row["admissible"] == target_row["admissible"]
        )
        inventory_agrees = inventory_agrees and row["agrees"]
        rebuilt_rows[name] = row

    whole_diversity = len(set(contents))
    control_additive = all(
        sum(
            len({contents[i] for i in idx})
            for idx in cellsets[fam].values()
        ) == whole_diversity
        for fam in FAMILY_ORDER
    )
    control_agrees = (
        control_additive == t_b["candidates"][CONTROL_NAME][
            "finite_additivity_over_certified_disjoint_families"]
        and t_b["candidates"][CONTROL_NAME]["admissible"] is False
        and t_b["candidates"][CONTROL_NAME][
            "additivity_failure_witness"] is not None
    )

    # ADVERSARIAL family 1: overlapping cells (tag F|B0 and tag B0|B1).
    overlap_cells = [
        {i for i, e in enumerate(events) if e[2] in ("F", "B0")},
        {i for i, e in enumerate(events) if e[2] in ("B0", "B1")},
    ]
    overlap_breaks = {}
    for name in CANDIDATE_NAMES:
        summed = sum(
            (sum((weights[name][i] for i in cell), Fraction(0))
             for cell in overlap_cells), Fraction(0)
        )
        overlap_breaks[name] = summed != totals[name]
    # ADVERSARIAL family 2: drop one nonempty cell (non-covering).
    drop_key = sorted(cellsets["F_TAG_ORDINAL"])[0]
    partial_breaks = {}
    for name in CANDIDATE_NAMES:
        summed = sum(
            (masses["F_TAG_ORDINAL"][name][key]
             for key in cellsets["F_TAG_ORDINAL"] if key != drop_key),
            Fraction(0),
        )
        partial_breaks[name] = summed != totals[name]
    # ADVERSARIAL covariance: the SAME orbit-constancy predicate fed a
    # deterministic NON-symmetry (the transposition of the lightest and
    # heaviest world cells).  It must break covariance wherever the world
    # masses are not already constant, otherwise the predicate is inert.
    world_mass = masses["F_WORLD"]

    def orbit_constant(cell_mass, orbits):
        return all(
            cell_mass.get(("w", orbit[0]), Fraction(0))
            == cell_mass.get(("w", x), Fraction(0))
            for orbit in orbits for x in orbit
        )

    covariance_teeth = {}
    for name in CANDIDATE_NAMES:
        ordered_cells = sorted(
            world_mass[name].items(), key=lambda kv: (kv[1], str(kv[0]))
        )
        lo_key, lo_val = ordered_cells[0]
        hi_key, hi_val = ordered_cells[-1]
        transposition = (tuple(sorted((lo_key[1], hi_key[1]))),)
        covariance_teeth[name] = {
            "world_masses_constant": lo_val == hi_val,
            "nonsymmetry_breaks_covariance":
                not orbit_constant(world_mass[name], transposition),
            "transposed_worlds": list(transposition[0]),
        }
    covariance_agrees = True
    for name in CANDIDATE_NAMES:
        target_cov = t_b["candidates"][name]["permutation_covariance"]
        bank_keys = [k for k in cellsets["F_TAG_ORDINAL"] if k[1] == "B0"]
        rebuilt_bank = all(
            masses["F_TAG_ORDINAL"][name].get(k, Fraction(0))
            == masses["F_TAG_ORDINAL"][name].get(
                ("to", "B1", k[2]), Fraction(0))
            for k in bank_keys
        )
        if rebuilt_bank != target_cov["bank_label_swap_on_tag_ordinal_cells"]:
            covariance_agrees = False
        rebuilt_rows[name]["bank_swap_covariant"] = rebuilt_bank
    teeth_ok = all(
        row["nonsymmetry_breaks_covariance"] or row["world_masses_constant"]
        for row in covariance_teeth.values()
    ) and any(
        row["nonsymmetry_breaks_covariance"]
        for row in covariance_teeth.values()
    )
    covariance_separates = (
        len({
            t_b["candidates"][name]["permutation_covariance"][
                "landed_monitor_phase_group_on_worlds"]
            for name in CANDIDATE_NAMES
        }) > 1
    )
    ck_c = {
        "certificate": "CK_C_MEASURE_INVENTORY_ATTACK",
        "arithmetic": (
            "plain Fraction arithmetic; the target used integer numerators"
            " over a common denominator, so agreement is a real"
            " cross-check of the exact rationals"
        ),
        "rebuilt_rows": rebuilt_rows,
        "inventory_agrees": inventory_agrees,
        "negative_control_agrees": control_agrees,
        "negative_control_additive_rebuilt": control_additive,
        "adversarial_overlapping_family_breaks_additivity": overlap_breaks,
        "adversarial_noncovering_family_breaks_additivity": partial_breaks,
        "additivity_test_has_teeth": (
            all(overlap_breaks.values()) and all(partial_breaks.values())
        ),
        "covariance_nonsymmetry_attack": covariance_teeth,
        "covariance_test_has_teeth": teeth_ok,
        "covariance_verdict_separates_candidates": covariance_separates,
        "bank_swap_covariance_agrees": covariance_agrees,
        "finding": (
            "the target's additivity certificate is non-vacuous exactly"
            " because disjointness is load-bearing: overlapping and"
            " non-covering pseudo-families break it for every candidate;"
            " the covariance predicate is non-inert because a declared"
            " non-symmetry breaks it wherever world masses are not"
            " already constant, and it separates the candidates"
        ),
    }
    ck_c["pass"] = bool(
        inventory_agrees and control_agrees
        and ck_c["additivity_test_has_teeth"]
        and teeth_ok and covariance_separates
        and covariance_agrees
        and control_additive is False
    )

    # ---- CK_D: fraction tables recomputed exactly --------------------------
    admissible = tuple(t_c["admissible_candidates_tabulated"])
    families = tuple(t_c["families_tabulated"])
    pairs = [
        (a, b) for i, a in enumerate(admissible) for b in admissible[i + 1:]
    ]
    digest_rows = {name: {} for name in admissible}
    tables_agree = True
    labels_ok = True
    disagreement = {f"{a}|{b}": None for a, b in pairs}
    resolved: set = set()
    atom_counts_agree = True
    for fam in families:
        normalized = {}
        for name in admissible:
            rows = [
                (compact(list(key)), value / totals[name])
                for key, value in sorted(masses[fam][name].items())
            ]
            normalized[name] = dict(rows)
            table_digest = digest([[k, fr(v)] for k, v in rows])
            target_table = t_c["tables"][name][fam]
            agrees = (
                table_digest == target_table["exact_table_digest"]
                and fr(sum((v for _k, v in rows), Fraction(0)))
                == target_table["sum_of_fractions"]
                and len({v for _k, v in rows})
                == target_table["distinct_values"]
                and fr(min(v for _k, v in rows))
                == target_table["min_fraction"]
                and fr(max(v for _k, v in rows))
                == target_table["max_fraction"]
                and sum(1 for _k, v in rows if v == 0)
                == target_table["zero_mass_cells"]
                and {
                    k: fr(v) for k, v in
                    sorted(rows, key=lambda kv: (-kv[1], kv[0]))[:5]
                } == target_table["largest_cells"]
            )
            if "table" in target_table:
                agrees = agrees and (
                    {k: fr(v) for k, v in rows} == target_table["table"]
                )
            if target_table.get("label") != FRACTION_LABEL:
                labels_ok = False
            digest_rows[name][fam] = agrees
            tables_agree = tables_agree and agrees
        for a, b in pairs:
            if (a, b) in resolved:
                continue
            ta, tb = normalized[a], normalized[b]
            for key in sorted(ta):
                if ta[key] != tb[key]:
                    disagreement[f"{a}|{b}"] = {
                        "family": fam, "cell": key,
                        a: fr(ta[key]), b: fr(tb[key]),
                    }
                    resolved.add((a, b))
                    break
        if fam == "F_ATOM":
            for a, b in pairs:
                ta, tb = normalized[a], normalized[b]
                differing = sum(1 for key in ta if ta[key] != tb[key])
                if differing != t_c["atom_level_disagreement_counts"][
                        f"{a}|{b}"]["differing_atoms"]:
                    atom_counts_agree = False
        del normalized
    disagreement_agrees = all(
        (disagreement[k] is not None)
        == t_c["pairwise_disagreement"][k]["disagree"]
        and (
            disagreement[k] is None
            or disagreement[k]
            == t_c["pairwise_disagreement"][k]["first_witness_cell"]
        )
        for k in disagreement
    )
    ck_d = {
        "certificate": "CK_D_FRACTION_LEDGER_REBUILD",
        "tables_checked": sum(len(v) for v in digest_rows.values()),
        "per_table_agreement": digest_rows,
        "all_table_digests_agree": tables_agree,
        "every_table_labelled_bookkeeping_not_probability": labels_ok,
        "pairwise_disagreement_agrees": disagreement_agrees,
        "atom_level_counts_agree": atom_counts_agree,
        "rebuilt_discriminating_pairs": tuple(
            sorted(k for k, v in disagreement.items() if v is not None)
        ),
        "target_discriminating_pairs": tuple(t_c["discriminating_pairs"]),
        "discriminating_pairs_agree": tuple(
            sorted(k for k, v in disagreement.items() if v is not None)
        ) == tuple(t_c["discriminating_pairs"]),
        "finding": (
            "every exact rational cell fraction was recomputed from an"
            " independently rebuilt event space and independently"
            " reimplemented arithmetic"
        ),
    }
    ck_d["pass"] = bool(
        tables_agree and labels_ok and disagreement_agrees
        and atom_counts_agree and ck_d["discriminating_pairs_agree"]
    )

    # ---- CK_E: boundary quote, controls ------------------------------------
    axiom_bytes = (ROOT / AUDIT_INPUT_PATHS[5]).read_bytes()
    needle_in_source = EXCLUSION_NEEDLE in axiom_bytes.decode("utf-8")
    needle_in_target_cert = (
        t_d["verbatim_exclusion_list"] == EXCLUSION_NEEDLE
    )
    forbidden = ("probability of", "Born rule holds", "we therefore select")
    no_smuggled_claim = not any(
        phrase in cache_text for phrase in forbidden
    )
    label_everywhere = t_c["label_on_every_number"] == FRACTION_LABEL
    ck_e = {
        "certificate": "CK_E_BOUNDARY_AND_CONTROLS",
        "source_controls": controls,
        "axiom_baseline_sha256": sha256(axiom_bytes).hexdigest(),
        "axiom_baseline_git_blob": git_blob(axiom_bytes),
        "verbatim_needle_present_in_pinned_source": needle_in_source,
        "target_quoted_verbatim_not_paraphrased": needle_in_target_cert,
        "target_boundary_certificate_passed": t_d[
            "verbatim_present_in_pinned_source"],
        "no_probability_claim_smuggled_into_cache": no_smuggled_claim,
        "fraction_label_declared_by_target": label_everywhere,
        "target_determinism": t_e["determinism"],
        "target_runtime_seconds": t_e["runtime_seconds"],
        "target_runtime_within_budget":
            t_e["runtime_seconds"] < AUDIT_TIMEOUT_SEC,
        "target_stdout_bytes": len(cache_text.encode()),
        "target_stdout_within_budget":
            len(cache_text.encode()) < STDOUT_LIMIT_BYTES,
        "target_summary_pass": bool(summary and summary["pass"]),
    }
    ck_e["pass"] = bool(
        controls["pass"] and needle_in_source and needle_in_target_cert
        and t_d["verbatim_present_in_pinned_source"]
        and no_smuggled_claim and label_everywhere
        and t_e["determinism"]["repeat_digest_equal"]
        and t_e["determinism"]["full_run_prefix_matches_short_scan"]
        and ck_e["target_runtime_within_budget"]
        and ck_e["target_stdout_within_budget"]
    )

    runtime = round(monotonic() - started, 3)
    checks = {
        "CK_A_EVENT_SPACE_REBUILD": ck_a["pass"],
        "CK_B_LATTICE_BY_CONTAINMENT": ck_b["pass"],
        "CK_C_MEASURE_INVENTORY_ATTACK": ck_c["pass"],
        "CK_D_FRACTION_LEDGER_REBUILD": ck_d["pass"],
        "CK_E_BOUNDARY_AND_CONTROLS": ck_e["pass"],
    }
    verdict = "CORROBORATES" if all(checks.values()) else "REFUTES"
    lines = [
        "CYCLE878_EVENT_SPACE_INDEPENDENT_CHECK",
        "SPECIFIED_TO_REFUTE_TARGET_AND_ITS_TWO_UPSTREAM_PRIMARIES_BLOCKLISTED",
    ]
    for name, payload in (
        ("CK_A_EVENT_SPACE_REBUILD", ck_a),
        ("CK_B_LATTICE_BY_CONTAINMENT", ck_b),
        ("CK_C_MEASURE_INVENTORY_ATTACK", ck_c),
        ("CK_D_FRACTION_LEDGER_REBUILD", ck_d),
        ("CK_E_BOUNDARY_AND_CONTROLS", ck_e),
    ):
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    out_summary = {
        "checks": checks,
        "cycle": 878,
        "verdict": verdict,
        "rebuilt_event_cardinality": total_events,
        "runtime_seconds": runtime,
        "runtime_within_budget": runtime < AUDIT_TIMEOUT_SEC,
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(out_summary))
    lines.append("CYCLE878_EVENT_SPACE_INDEPENDENT_CHECK_" + verdict)
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if out_summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
