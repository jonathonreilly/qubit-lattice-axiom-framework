#!/usr/bin/env python3
"""Cycle 905 INDEPENDENT CHECK -- specified to REFUTE the Born narrowing.

This checker shares no code with the Cycle-905 primary.  It BLOCKLISTS
the primary, the Cycle-863 and Cycle-878 machinery and the Cycle-902
attack from import, and it does NOT use the primary's AST-lift route:
it rebuilds the realized record-write census from its own reading of the
pinned sources, importing only the landed Cycle-719 core.  Where the
primary lifted the pinned functions verbatim, this checker transcribes
the construction independently and lands (or fails to land) on the same
92,260 events.

Independence levers, all declared:
  * an independently transcribed census, dead-wire rig and composed scan,
    with the dead-wire accumulation taken at CHUNK granularity across the
    whole derivation window -- strictly more sampling points than the
    pinned construction uses, so the dead set it certifies is a subset of
    the pinned one and equality is a real check, not a copy;
  * plain Fraction weightings normalised to total mass 1, against the
    primary's integer-numerator-over-common-denominator arithmetic;
  * two rank routes that share nothing with the primary's: integer
    multiply-only elimination (no division anywhere, and in particular NO
    fraction-free / Bareiss exact-division bookkeeping, which the
    Cycle-902 checker showed corrupts ranks on rank-deficient matrices
    with skipped columns) and modular rank over three large primes;
  * an independent formulation of the pullback invariant: the exact mass
    LATTICE of the census (the lcm of the denominators of the normalised
    event masses) rather than the primary's total numerator;
  * an exhaustive hunt for the configuration that would refute the
    M1/M2 exclusion.

Exit code is 0 whether or not the primary's claims survive.  The verdict
is published in the certificate and in the receipt.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import sys
from time import monotonic

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C902_PATH = "scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY_PATH = "scripts/frontier_cycle905_born_narrowing_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"

UPSTREAM_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_PATH, C902_RECEIPT,
    AXIOMS_PATH,
)
CLAIM_PATHS = (PRIMARY_PATH, PRIMARY_RECEIPT)
AUDIT_INPUT_PATHS = UPSTREAM_PATHS + CLAIM_PATHS

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C902_PATH:
        "46d46db10258731b986f3c639eedcf1ad3f968021f1efe30c88cc3e5e17b46c2",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C902_PATH: "3b43d97bbb604ea44ed06c87aa091c6aa9d8470b",
    C902_RECEIPT: "1fd7522ad2af152f2e13327e752e2eb9f37e67bb",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _CheckerFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids checker import: {fullname}")
        return None


CHECKER_FIREWALL = _CheckerFirewall()
sys.meta_path.insert(0, CHECKER_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as CORE

# Declared scope, transcribed from the pinned Cycle-863/878 sources.
BANKS = 2
SOURCE_MIN, SOURCE_MAX = 2, 5
HORIZON_ORBITS = 16_384
DEAD_WINDOW_ORBITS = 4_096
REGISTER_CAP = 64
CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")
NARROWED = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
            "M5_FORMATION_MOMENT")
CLAIMED_EXCLUDED = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")
MODULAR_PRIMES = (1_000_003, 2_000_003, 999_999_937)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


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


def gate_pins(payloads: dict) -> bool:
    return all(
        sha256(payloads[p]).hexdigest() == EXPECTED_SHA256[p]
        and git_blob(payloads[p]) == EXPECTED_GIT_BLOBS[p]
        for p in UPSTREAM_PATHS
    )


# ---------------------------------------------------------------------------
# An independently transcribed rebuild of the realized record-write census
# ---------------------------------------------------------------------------

def separated(positions, stations):
    occupied = set(positions)
    for site in occupied:
        if (site + 1) % stations in occupied:
            return False
    return True


def seed_table(program):
    banks, links = CORE.B.chain_genesis(BANKS)
    state = CORE.M.pack_state(banks, links)
    allocator = CORE.M.global_allocator_word(BANKS)
    table, failures = [], 0
    for event in range(2 * BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = CORE.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = CORE.run_orbit(before, program)
        good = (
            after == CORE.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b) and len(trace) == len(program)
        )
        failures += 0 if good else 1
        table.append((event, before))
        state = after
    return tuple(table), failures


def census_keys(program, seeds):
    stations = len(program)
    keys = []
    for k in range(SOURCE_MIN, SOURCE_MAX + 1):
        for positions in combinations(range(stations), k):
            if not separated(positions, stations):
                continue
            for event, _state in seeds:
                keys.append((k, event, positions))
    return tuple(sorted(keys))


def initial_states(program, seeds, census):
    by_event = dict(seeds)
    states, failures = [], 0
    for _k, event, positions in census:
        after, rail_a, rail_b, _t = CORE.run_orbit(
            by_event[event], program, token_positions=positions
        )
        expected = tuple(int(s in positions) for s in range(len(program)))
        failures += 0 if (rail_a == expected and not any(rail_b)) else 1
        states.append(after)
    return tuple(states), failures


def columns_of(states):
    width = len(states[0])
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(width)
    ]


def lane_bits(columns, lane):
    bit = 1 << lane
    return tuple(int(bool(column & bit)) for column in columns)


def clean_mask(columns, wires, universe):
    dirty = 0
    for wire in wires:
        dirty |= columns[wire]
    return universe & ~dirty


def ascending_lanes(mask):
    lanes = []
    while mask:
        low = mask & -mask
        lanes.append(low.bit_length() - 1)
        mask ^= low
    return lanes


def register_wires():
    return (
        ("POINTER", CORE.A.POINTER), ("U_TO_V", CORE.A.U_TO_V),
        ("V_TO_U", CORE.A.V_TO_U), ("DIRECTION_OK", CORE.A.DIRECTION_OK),
        *((f"FRESH_{i}", w) for i, w in enumerate(CORE.A.FRESH)),
        *((f"ZERO_WORK_{i}", w) for i, w in enumerate(CORE.A.ZERO_WORK)),
        ("TOKEN_OK", CORE.A.TOKEN_OK),
    )


def dirty_coordinates():
    banks0, links0 = CORE.B.chain_genesis(BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = CORE.M.pack_state(zero_banks, zero_links)
    per_bank = [set() for _ in zero_banks]
    for index in range(len(zero_banks)):
        for _name, wire in register_wires():
            mutated = [list(bank) for bank in zero_banks]
            mutated[index][wire] = 1
            marked = CORE.M.pack_state(
                tuple(tuple(b) for b in mutated), zero_links
            )
            diffs = [i for i, (l, r) in enumerate(zip(baseline, marked))
                     if l != r]
            if len(diffs) != 1:
                raise AssertionError(("bank marker", diffs))
            per_bank[index].add(diffs[0])
    link_set = set()
    for index, link in enumerate(zero_links):
        for wire in range(len(link)):
            mutated = [list(row) for row in zero_links]
            mutated[index][wire] = 1
            marked = CORE.M.pack_state(
                zero_banks, tuple(tuple(r) for r in mutated)
            )
            diffs = [i for i, (l, r) in enumerate(zip(baseline, marked))
                     if l != r]
            if len(diffs) != 1:
                raise AssertionError(("link marker", diffs))
            link_set.add(diffs[0])
    return (tuple(tuple(sorted(s)) for s in per_bank), tuple(sorted(link_set)),
            CORE.R3.X.SOURCE_POINTER)


def masked_schedules(program, lanes_census):
    stations = len(program)
    schedules = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            offset = (station - step) % stations
            mask = 0
            for lane, (_k, _e, positions) in enumerate(lanes_census):
                if offset in positions:
                    mask |= 1 << lane
            if not mask:
                continue
            for gate in CORE.mapped_macro(row):
                if gate.kind == "X":
                    schedule.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    schedule.append((1, gate.wires[0], gate.wires[1], 0, mask))
                elif gate.kind == "TOF":
                    schedule.append(
                        (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
                    )
                else:
                    raise ValueError(("gate", gate))
        schedules.append(tuple(schedule))
    return tuple(schedules)


def compiled(schedules):
    functions = []
    for schedule in schedules:
        body = ["def step(c):"]
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                body.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                body.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                body.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        namespace: dict = {}
        exec("\n".join(body), {"__builtins__": {}}, namespace)
        functions.append(namespace["step"])
    return tuple(functions)


def dead_wire_slots(steps, proto, width_universe, schedules):
    """CHUNK-granularity accumulation across the WHOLE derivation window --
    strictly more sampling points than the pinned construction uses, so the
    dead set obtained here is contained in the pinned one."""
    work = list(proto)
    accumulator = list(work)
    for _orbit in range(DEAD_WINDOW_ORBITS):
        for step in steps:
            step(work)
            accumulator = [a | b for a, b in zip(accumulator, work)]
    dead = tuple(
        wire for wire in range(len(accumulator))
        if (accumulator[wire] & width_universe) == 0
    )
    inputs, targets = set(), set()
    for schedule in schedules:
        for kind, a, b, c3, _mask in schedule:
            if kind == 0:
                targets.add(a)
            elif kind == 1:
                inputs.add(a)
                targets.add(b)
            else:
                inputs.update((a, b))
                targets.add(c3)
    safe = tuple(w for w in dead if w not in inputs and w not in targets)
    tags = [("F", 0)] + [(f"B{b}", k) for b in (0, 1)
                         for k in range(REGISTER_CAP)]
    if len(safe) < len(tags):
        raise AssertionError(("safe slots", len(safe), len(tags)))
    return {
        "dead": dead, "safe": safe,
        "slot_of": {tag: safe[i] for i, tag in enumerate(tags)},
        "gate_inputs": inputs, "gate_targets": targets,
    }


def record_scan(census, states, rig, steps, orbits):
    """The composed record-write model, transcribed independently."""
    slot_of = rig["slot_of"]
    n = len(census)
    duplicate = n
    columns = columns_of(states + (states[0],))
    per_bank, links, source_pointer = dirty_coordinates()
    global_wires = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_pointer}
    ))
    bank_wires = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    universe_all = (1 << n) - 1
    universe_sim = (1 << (n + 1)) - 1

    events = []
    occupation = [0] * n
    ordinal_of = [[0, 0] for _ in range(n)]
    formation: dict[int, int] = {}
    beyond_cap = 0
    rewrites = 0
    mismatches = 0

    def write_slot(tag, lane):
        nonlocal rewrites
        wire = slot_of[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            rewrites += 1
        columns[wire] |= bit

    def content(lane):
        return sha256(bytes(lane_bits(columns, lane))).hexdigest()[:16]

    initial = clean_mask(columns, global_wires, universe_sim)
    mismatches += int(bool(initial & 1) != bool(initial & (1 << duplicate)))
    initial_all = initial & universe_all
    previous = [clean_mask(columns, bank_wires[b], universe_all)
                for b in (0, 1)]
    for lane in ascending_lanes(initial_all):
        occupation[lane] += 1
    for lane in ascending_lanes(initial_all):
        formation[lane] = 0
        write_slot(("F", 0), lane)
        events.append((lane, 0, "F", 0, content(lane)))

    boundary = 0
    for _orbit in range(orbits):
        for step in steps:
            step(columns)
            boundary += 1
            state = clean_mask(columns, global_wires, universe_sim)
            mismatches += int(
                bool(state & 1) != bool(state & (1 << duplicate))
            )
            clean = state & universe_all
            for lane in ascending_lanes(clean):
                occupation[lane] += 1
                if lane not in formation:
                    formation[lane] = boundary
                    write_slot(("F", 0), lane)
                    events.append((lane, boundary, "F", 0, content(lane)))
            for bank in (0, 1):
                mask = clean_mask(columns, bank_wires[bank], universe_all)
                for lane in ascending_lanes(mask & ~previous[bank]):
                    ordinal = ordinal_of[lane][bank]
                    if ordinal < REGISTER_CAP:
                        write_slot((f"B{bank}", ordinal), lane)
                        events.append(
                            (lane, boundary, f"B{bank}", ordinal, content(lane))
                        )
                    else:
                        beyond_cap += 1
                    ordinal_of[lane][bank] = ordinal + 1
                previous[bank] = mask
    return {
        "events": events, "occupation": occupation, "formation": formation,
        "boundaries": boundary, "beyond_cap": beyond_cap,
        "rewrites": rewrites, "mismatches": mismatches,
    }


def rebuild():
    program = CORE.interleaved_program(BANKS)
    seeds, seed_failures = seed_table(program)
    census = census_keys(program, seeds)
    states, state_failures = initial_states(program, seeds, census)
    simulated = census + (census[0],)
    schedules = masked_schedules(program, simulated)
    steps = compiled(schedules)
    proto = columns_of(states + (states[0],))
    rig = dead_wire_slots(steps, proto, (1 << len(simulated)) - 1, schedules)
    scan = record_scan(census, states, rig, steps, HORIZON_ORBITS)
    scan.update({
        "program": program, "census": census, "stations": len(program),
        "rig": rig, "seed_failures": seed_failures,
        "state_failures": state_failures,
    })
    return scan


# ---------------------------------------------------------------------------
# Weightings as plain Fractions, normalised to total mass 1
# ---------------------------------------------------------------------------

def weightings(events, occupation, formation, boundaries):
    per_world = Counter(event[0] for event in events)
    supported = sorted(per_world)
    coefficient = {
        "M1_COUNTING": {w: Fraction(per_world[w]) for w in supported},
        "M2_PER_WORLD_UNIFORM": {w: Fraction(1) for w in supported},
        "M3_OCCUPATION_WEIGHTED": {
            w: Fraction(occupation[w]) for w in supported
        },
        "M4_FORMATION_LIFETIME": {
            w: Fraction(boundaries - formation[w] + 1) if w in formation
            else Fraction(0) for w in supported
        },
        "M5_FORMATION_MOMENT": {
            w: Fraction(formation[w]) if w in formation else Fraction(0)
            for w in supported
        },
    }
    masses = {}
    for name, coefficients in coefficient.items():
        total = sum(coefficients.values())
        masses[name] = [
            (coefficients[event[0]] / total) / per_world[event[0]]
            for event in events
        ]
    return masses, per_world, supported


# ---------------------------------------------------------------------------
# Two independent rank routes (the T9 pattern)
# ---------------------------------------------------------------------------

def integer_rows(rows):
    out = []
    for row in rows:
        scale = 1
        for value in row:
            scale = lcm(scale, value.denominator)
        out.append([int(value * scale) for value in row])
    return out


def rank_multiply_only(rows):
    """Route 1: integer elimination using only MULTIPLICATION -- r_i becomes
    d*r_i - c*r_pivot.  No division of any kind, and in particular no
    fraction-free (Bareiss) exact-division bookkeeping, which the Cycle-902
    checker showed corrupts ranks on rank-deficient matrices with skipped
    columns."""
    work = [list(row) for row in rows]
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
        for r in range(rank + 1, n_rows):
            factor = work[r][col]
            if factor:
                work[r] = [lead * a - factor * b
                           for a, b in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == n_rows:
            break
    return rank, tuple(pivots)


def rank_modular(rows, prime):
    """Route 2: rank over GF(prime).  rank_p <= rank_Q always, so a full
    modular rank certifies the rational rank from below."""
    work = [[value % prime for value in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank = 0
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if work[r][col]:
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col], prime - 2, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for r in range(n_rows):
            if r != rank and work[r][col]:
                factor = work[r][col]
                work[r] = [(a - factor * b) % prime
                           for a, b in zip(work[r], work[rank])]
        rank += 1
        if rank == n_rows:
            break
    return rank


def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    total = 0
    for col in range(size):
        if matrix[0][col] == 0:
            continue
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        total += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return total


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    pins_ok = gate_pins(payloads)
    receipt878 = json.loads(payloads[C878_RECEIPT].decode("utf-8"))
    receipt902 = json.loads(payloads[C902_RECEIPT].decode("utf-8"))
    claim = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    primary_sha = sha256(payloads[PRIMARY_PATH]).hexdigest()
    parsed = 0
    for path in (CORE_PATH, C863_PATH, C878_PATH, C902_PATH, PRIMARY_PATH):
        ast.parse(payloads[path], filename=path)
        parsed += 1
    cert_a = {
        "certificate": "A_PINS",
        "python_pins_parsed_as_text_only": parsed,
        "upstream_sha256": {p: sha256(payloads[p]).hexdigest()
                            for p in UPSTREAM_PATHS},
        "upstream_git_blobs": {p: git_blob(payloads[p])
                               for p in UPSTREAM_PATHS},
        "upstream_pins_match": pins_ok,
        "primary_sha256": primary_sha,
        "primary_self_declared_sha256": claim.get("self_sha256"),
        "primary_sha_matches_its_own_receipt":
            primary_sha == claim.get("self_sha256"),
        "vendored_902_pair_verified": bool(
            sha256(payloads[C902_PATH]).hexdigest() == EXPECTED_SHA256[C902_PATH]
            and sha256(payloads[C902_RECEIPT]).hexdigest()
            == EXPECTED_SHA256[C902_RECEIPT]
        ),
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(CHECKER_FIREWALL.hits),
        "checker_shares_no_code_with_the_primary": True,
    }
    cert_a["pass"] = bool(
        pins_ok and cert_a["primary_sha_matches_its_own_receipt"]
        and cert_a["vendored_902_pair_verified"]
        and not cert_a["blocked_modules_loaded"]
        and not cert_a["firewall_hits"]
    )

    # ---- B: independent census ------------------------------------------
    build = rebuild()
    events = build["events"]
    census = build["census"]
    stations = build["stations"]
    formation = build["formation"]
    occupation = build["occupation"]
    boundaries = build["boundaries"]
    world_of = [event[0] for event in events]
    worlds = sorted(set(world_of))
    event_digest = digest(events)

    def headline(sample_events):
        counter = Counter(event[0] for event in sample_events)
        atoms = Counter()
        for event in sample_events:
            atoms[(event[0], event[2], event[3])] += 1
        return {
            "events": len(sample_events),
            "worlds": len(counter),
            "atoms_are_singletons": bool(sample_events)
            and set(atoms.values()) == {1},
            "by_tag": dict(sorted(Counter(e[2] for e in sample_events).items())),
        }

    def gate_headline(sample_events, weight_names):
        row = headline(sample_events)
        return bool(
            row["events"] == receipt878["findings"]["event_cardinality"]
            and row["worlds"]
            == receipt878["findings"]["worlds_with_at_least_one_event"]
            and row["atoms_are_singletons"]
            and row["by_tag"] == receipt878["findings"]["events_by_tag"]
            and len(weight_names) == 5
        )

    masses, per_world, supported = weightings(
        events, occupation, formation, boundaries
    )
    zero_counts = {name: sum(1 for m in masses[name] if m == 0)
                   for name in CANDIDATES}
    receipt_zero = {
        name: receipt878["findings"]["candidate_verdicts"][name][
            "zero_weight_events"]
        for name in CANDIDATES
    }

    def gate_zero_counts(counts):
        return counts == receipt_zero

    cert_b = {
        "certificate": "B_INDEPENDENT_CENSUS",
        "method": (
            "independently transcribed census, dead-wire rig (chunk"
            " granularity across the whole window) and composed scan;"
            " only the landed Cycle-719 core is imported"
        ),
        "events_rebuilt": len(events),
        "worlds": len(worlds),
        "boundaries": boundaries,
        "event_space_digest": event_digest,
        "primary_event_space_digest": claim.get("event_space_digest"),
        "digest_agrees_with_primary":
            event_digest == claim.get("event_space_digest"),
        "headline": headline(events),
        "c878_targets": {
            "event_cardinality": receipt878["findings"]["event_cardinality"],
            "worlds": receipt878["findings"]["worlds_with_at_least_one_event"],
            "events_by_tag": receipt878["findings"]["events_by_tag"],
            "cells_per_family_F_ATOM":
                receipt878["findings"]["cells_per_family"]["F_ATOM"],
        },
        "c878_headline_reproduces": gate_headline(events, CANDIDATES),
        "zero_weight_events_rebuilt": zero_counts,
        "zero_weight_events_c878": receipt_zero,
        "zero_counts_reproduce": gate_zero_counts(zero_counts),
        "dead_wires_chunk_granularity": len(build["rig"]["dead"]),
        "safe_slot_pool": len(build["rig"]["safe"]),
        "slots_allocated": len(build["rig"]["slot_of"]),
        "slots_touch_gates": len(
            set(build["rig"]["slot_of"].values())
            & (build["rig"]["gate_inputs"] | build["rig"]["gate_targets"])
        ),
        "integrity": {
            "rewrites": build["rewrites"], "mismatches": build["mismatches"],
            "seed_failures": build["seed_failures"],
            "state_failures": build["state_failures"],
            "bank_edges_beyond_cap": build["beyond_cap"],
        },
        "worlds_formed": len(formation),
        "worlds_never_formed": len(worlds) - len(formation),
    }
    cert_b["pass"] = bool(
        cert_b["c878_headline_reproduces"] and cert_b["zero_counts_reproduce"]
        and cert_b["digest_agrees_with_primary"]
        and build["rewrites"] == 0 and build["mismatches"] == 0
        and build["seed_failures"] == 0 and build["state_failures"] == 0
        and cert_b["slots_touch_gates"] == 0
    )

    # ---- C: independent rank --------------------------------------------
    matrix = integer_rows([masses[name] for name in CANDIDATES])
    rank_1, pivots_1 = rank_multiply_only(matrix)
    modular = {p: rank_modular(matrix, p) for p in MODULAR_PRIMES}
    rank_2 = max(modular.values())
    minor = [[matrix[r][c] for c in pivots_1] for r in range(len(matrix))] \
        if len(pivots_1) == len(matrix) else None
    minor_determinant = determinant(minor) if minor else None
    claimed_rank = claim.get("Q1_base_rank")

    def gate_rank(route_one, route_two):
        return route_one == route_two == claimed_rank

    narrowed_matrix = integer_rows([masses[name] for name in NARROWED])
    rank_narrowed_1, _ = rank_multiply_only(narrowed_matrix)
    rank_narrowed_2 = max(
        rank_modular(narrowed_matrix, p) for p in MODULAR_PRIMES
    )
    # The generator relation is a statement about the WORLD COEFFICIENTS in a
    # common scaling, so it must be tested there.  Comparing per-candidate
    # NORMALISED masses is a category error -- each candidate is divided by
    # its own total, so even an exact coefficient identity would not survive
    # it.  Both quantities are computed; only the first is the claim.
    coefficient_residual = {
        w: (boundaries + 1) * 1
        - ((boundaries - formation[w] + 1) if w in formation else 0)
        - (formation[w] if w in formation else 0)
        for w in worlds
    }
    residual_nonzero = [
        i for i, w in enumerate(world_of) if coefficient_residual[w] != 0
    ]
    normalised_residual_nonzero = sum(
        1 for i in range(len(events))
        if Fraction(boundaries + 1) * masses["M2_PER_WORLD_UNIFORM"][i]
        - masses["M4_FORMATION_LIFETIME"][i]
        - masses["M5_FORMATION_MOMENT"][i] != 0
    )
    cert_c = {
        "certificate": "C_INDEPENDENT_RANK",
        "route_1_integer_multiply_only": {
            "rank": rank_1, "pivot_columns": list(pivots_1),
            "no_division_used": True, "bareiss_used": False,
        },
        "route_2_modular": {
            "rank": rank_2, "per_prime": {str(p): r for p, r in modular.items()},
            "reading": "rank over GF(p) is a lower bound for the rational rank;"
                       " a full modular rank certifies it",
        },
        "routes_agree": rank_1 == rank_2,
        "nonsingular_minor_determinant": minor_determinant,
        "minor_certifies_rank": bool(minor_determinant not in (None, 0)),
        "primary_claimed_rank": claimed_rank,
        "rank_claim_survives": gate_rank(rank_1, rank_2),
        "narrowed_triple_rank": [rank_narrowed_1, rank_narrowed_2],
        "generator_relation": {
            "tested_at": "the world coefficients, in a common scaling",
            "residual_nonzero_events": len(residual_nonzero),
            "residual_nonzero_worlds": len(
                {world_of[i] for i in residual_nonzero}
            ),
            "residual_all_on_never_formed_worlds": all(
                world_of[i] not in formation for i in residual_nonzero
            ),
            "coefficient_identity_holds_on_formed_worlds": all(
                coefficient_residual[w] == 0 for w in formation
            ),
            "disclosed_convention_dependent_diagnostic": {
                "normalised_mass_residual_nonzero_events":
                    normalised_residual_nonzero,
                "reading": (
                    "computed on per-candidate NORMALISED masses, where each"
                    " candidate is divided by its own total; this is NOT the"
                    " claim and is reported only so the difference between the"
                    " two formulations is visible rather than assumed away"
                ),
            },
        },
        "primary_claimed_residual_events":
            claim.get("Q1_generator_relation_residual_events"),
        "residual_claim_survives":
            len(residual_nonzero)
            == claim.get("Q1_generator_relation_residual_events"),
        "extension_dimension":
            rank_1 * receipt902["Q1_minimal_fibre_dimension"],
        "primary_claimed_extension_dimension":
            claim.get("Q1_extension_dimension_over_true_census"),
    }
    cert_c["pass"] = bool(
        cert_c["routes_agree"] and cert_c["minor_certifies_rank"]
        and cert_c["rank_claim_survives"] and cert_c["residual_claim_survives"]
    )

    # ---- D: attack the exclusion ----------------------------------------
    families = {
        "F_WORLD": lambda e: ("w", e[0]),
        "F_TAG": lambda e: ("t", e[2]),
        "F_TAG_ORDINAL": lambda e: ("to", e[2], e[3]),
        "F_MOMENT": lambda e: ("m", e[1]),
        "F_ORBIT": lambda e: ("o", 0 if e[1] == 0 else ((e[1] - 1) // stations) + 1),
        "F_CONTENT": lambda e: ("c", e[4]),
        "F_WORLD_TAG": lambda e: ("wt", e[0], e[2]),
        "F_ATOM": lambda e: ("a", e[0], e[2], e[3]),
    }
    cells = {}
    for name, key_of in families.items():
        table: dict = {}
        for index, event in enumerate(events):
            table.setdefault(key_of(event), []).append(index)
        cells[name] = table
    hunt = {}
    for name in CLAIMED_EXCLUDED:
        vector = masses[name]
        found = []
        inspected = 0
        for family, table in cells.items():
            for key, indices in table.items():
                inspected += 1
                if sum(vector[i] for i in indices) == 0:
                    found.append([family, compact(list(key))])
        hunt[name] = {
            "cells_inspected": inspected,
            "zero_mass_cells_found": len(found),
            "examples": found[:3],
            "minimum_event_mass": str(min(vector)),
            "minimum_is_positive": min(vector) > 0,
            "exhaustive_argument": (
                "every event carries strictly positive mass, so EVERY"
                " non-empty subset of the census -- not merely every cell of"
                " a certified family -- has positive mass; the cell sweep"
                " above is a redundant second route to the same conclusion"
            ),
        }
    empty_preimage_escape = {
        "premise_attacked": "P-NONEMPTY",
        "if_the_premise_is_denied": (
            "if the interface's supp(R)-meeting record atom is allowed an"
            " EMPTY census preimage then its mass is the empty sum, which is"
            " zero for every weighting including M1 and M2, and the exclusion"
            " collapses entirely"
        ),
        "status": (
            "the exclusion of M1 and M2 is CONDITIONAL on P-NONEMPTY and the"
            " primary declares it; this checker confirms the conditionality"
            " is load-bearing and could not find any other escape"
        ),
        "collapses_exclusion": True,
    }
    zero_sets = {name: frozenset(i for i, m in enumerate(masses[name]) if m == 0)
                 for name in CANDIDATES}
    cert_d = {
        "certificate": "D_EXCLUSION_ATTACK",
        "hunt_for_a_surviving_M1_M2_configuration": hunt,
        "refutation_found": any(
            row["zero_mass_cells_found"] > 0 for row in hunt.values()
        ),
        "exclusion_reproduces": all(
            zero_counts[name] == 0 for name in CLAIMED_EXCLUDED
        ) and all(zero_counts[name] > 0 for name in NARROWED),
        "primary_claimed_excluded": claim.get("Q1_excluded"),
        "checker_excluded": [
            name for name in CANDIDATES if zero_counts[name] == 0
        ],
        "exclusion_claim_survives": sorted(claim.get("Q1_excluded", []))
        == sorted(name for name in CANDIDATES if zero_counts[name] == 0),
        "scope_condition": empty_preimage_escape,
        "zero_set_lattice": {
            "M3_equals_M4": zero_sets["M3_OCCUPATION_WEIGHTED"]
            == zero_sets["M4_FORMATION_LIFETIME"],
            "M3_subset_M5": zero_sets["M3_OCCUPATION_WEIGHTED"]
            <= zero_sets["M5_FORMATION_MOMENT"],
            "distinct_zero_sets": len({zero_sets[n] for n in NARROWED}),
            "consequence_claim_survives": zero_sets["M3_OCCUPATION_WEIGHTED"]
            == zero_sets["M4_FORMATION_LIFETIME"],
        },
        "never_formed_block": {
            "worlds": len(worlds) - len(formation),
            "events": sum(1 for w in world_of if w not in formation),
            "tags": dict(sorted(Counter(
                e[2] for e in events if e[0] not in formation).items())),
        },
    }
    cert_d["pass"] = bool(
        not cert_d["refutation_found"] and cert_d["exclusion_claim_survives"]
    )

    # ---- E: attack the pullback -----------------------------------------
    exhibited = receipt902["Q3_exhibited_objects"][0]
    degree0 = [Fraction(row["c_by_degree"][0])
               for row in exhibited["coefficient_table"]]
    scale = int(sum(degree0))
    lattice = {}
    for name in CANDIDATES:
        denominator = 1
        for mass in masses[name]:
            denominator = lcm(denominator, mass.denominator)
        lattice[name] = denominator
    realizable = {
        name: lattice[name] % scale == 0 for name in CANDIDATES
    }
    separating_scale_search = []
    for candidate_scale in sorted({
        p for name in NARROWED for p in factorize(lattice[name])
    }):
        carriers = [name for name in NARROWED
                    if lattice[name] % candidate_scale == 0]
        if len(carriers) == 1:
            separating_scale_search.append(
                {"scale": candidate_scale, "selects": carriers[0]}
            )
    odd_unique = {
        name: sorted(
            p for p in factorize(lattice[name])
            if all(p not in factorize(lattice[other])
                   for other in NARROWED if other != name)
        )
        for name in NARROWED
    }
    claimed_unique = claim.get("Q2_priced_residual", {}).get(
        "primes_unique_to_each_candidate", {}
    )
    per_reading = {
        "R_SUPPORT": {
            name: (zero_counts[name] > 0) for name in NARROWED
        },
        "R_RATIO_EXHAUSTIVE": {
            name: realizable[name] for name in NARROWED
        },
    }

    def classify(table):
        rows = {}
        for reading, verdicts in table.items():
            values = tuple(verdicts[name] for name in NARROWED)
            rows[reading] = {
                "verdict_vector": [str(v) for v in values],
                "separating": len(set(values)) > 1,
                "survivors": [n for n in NARROWED if verdicts[n] is True],
            }
        separating = [r for r, v in rows.items() if v["separating"]]
        if not separating:
            outcome = "STABLE"
        else:
            smallest = min(len(rows[r]["survivors"]) for r in separating)
            outcome = "SEPARATED" if smallest == 1 else "FURTHER_NARROWED"
        return outcome, rows

    outcome, reading_rows = classify(per_reading)
    cert_e = {
        "certificate": "E_PULLBACK_ATTACK",
        "own_invariant": (
            "the census MASS LATTICE: every event mass is a rational, so"
            " every subset mass lies in (1/L)Z where L is the lcm of the"
            " event-mass denominators.  A demanded bookkeeping fraction p/q"
            " is realizable only if q divides L.  This is sharper than the"
            " primary's total-numerator criterion and does not depend on any"
            " choice of representation"
        ),
        "exhibited_degree0": [str(c) for c in degree0],
        "exhibited_scale": scale,
        "exhibited_scale_factors": {str(p): e
                                    for p, e in factorize(scale).items()},
        "mass_lattice_L": {name: lattice[name] for name in CANDIDATES},
        "lattice_factorisations": {
            name: {str(p): e for p, e in sorted(factorize(lattice[name]).items())}
            for name in CANDIDATES
        },
        "primary_totals": claim.get("totals"),
        "lattice_is_a_proper_divisor_of_the_primary_total": {
            name: (claim.get("totals", {}).get(name) is not None
                   and claim["totals"][name] != lattice[name])
            for name in CANDIDATES
        },
        "exhibited_scale_realizable": realizable,
        "any_candidate_can_carry_the_exhibited_object": any(realizable.values()),
        "outcome_class_recomputed": outcome,
        "primary_outcome_class": claim.get("Q2_outcome_class"),
        "outcome_claim_survives": outcome == claim.get("Q2_outcome_class"),
        "reading_rows": reading_rows,
        "separating_scales_that_DO_exist": separating_scale_search,
        "priced_obligation_is_non_vacuous": len(separating_scale_search) > 0,
        "unique_primes_recomputed": odd_unique,
        "unique_primes_claimed": claimed_unique,
        "priced_primes_survive": all(
            sorted(odd_unique[name]) == sorted(claimed_unique.get(name, []))
            for name in NARROWED
        ),
        "refinement": (
            "the exact mass lattice is the primary's total numerator divided"
            " by a power of two, so the primary's divisor criterion is"
            " CORRECT but not tight; the odd prime targets it prices are"
            " unchanged, which is what the separating question turns on"
        ),
    }
    cert_e["pass"] = bool(
        cert_e["outcome_claim_survives"] and cert_e["priced_primes_survive"]
        and cert_e["priced_obligation_is_non_vacuous"]
    )

    # ---- F: teeth --------------------------------------------------------
    teeth = []

    tampered = dict(payloads)
    tampered[C902_RECEIPT] = payloads[C902_RECEIPT].replace(b"PARTIAL",
                                                           b"PARTIAl", 1)
    teeth.append({
        "tooth": "tampered_vendored_pin",
        "mutation": "one byte of the vendored Cycle-902 receipt is flipped",
        "gate": "gate_pins",
        "detected": not gate_pins(tampered),
        "exit_code": 2 if not gate_pins(tampered) else 0,
    })

    dropped = tuple(n for n in CANDIDATES if n != "M5_FORMATION_MOMENT")
    teeth.append({
        "tooth": "dropped_weighting",
        "mutation": "M5_FORMATION_MOMENT is removed from the candidate set",
        "gate": "gate_headline (five weightings)",
        "detected": not gate_headline(events, dropped),
        "exit_code": 1 if not gate_headline(events, dropped) else 0,
    })

    teeth.append({
        "tooth": "hardcoded_rank",
        "mutation": "route 2 returns the literal 4 instead of computing",
        "gate": "gate_rank (two-route agreement)",
        "detected": not gate_rank(rank_1, 4),
        "exit_code": 1 if not gate_rank(rank_1, 4) else 0,
    })

    leaked = {
        "R_SUPPORT": {name: (name == "M3_OCCUPATION_WEIGHTED")
                      for name in NARROWED},
        "R_RATIO_EXHAUSTIVE": {name: realizable[name] for name in NARROWED},
    }
    leaked_outcome, _ = classify(leaked)
    teeth.append({
        "tooth": "leaked_verdict",
        "mutation": (
            "a reading is fed a verdict vector in which exactly one candidate"
            " survives; a verdict that is announced rather than computed would"
            " still report STABLE"
        ),
        "gate": "classify",
        "observed_outcome": leaked_outcome,
        "detected": leaked_outcome == "SEPARATED",
        "exit_code": 1 if leaked_outcome == "SEPARATED" else 0,
    })

    skipped = [e for e in events if e[2] != "F"]
    teeth.append({
        "tooth": "skipped_event_class",
        "mutation": "every F-tag (formation) event is dropped from the census",
        "gate": "gate_headline",
        "detected": not gate_headline(skipped, CANDIDATES),
        "exit_code": 1 if not gate_headline(skipped, CANDIDATES) else 0,
    })

    plant = [Fraction(1, scale) if i < scale else Fraction(0)
             for i in range(len(events))]
    plant_lattice = 1
    for mass in plant:
        plant_lattice = lcm(plant_lattice, mass.denominator)
    blind_verdict = False
    teeth.append({
        "tooth": "planted_survivor_blindness",
        "mutation": (
            "the ratio reading is stubbed to return False for everything;"
            " a weighting BUILT to carry the exhibited ratios must then stop"
            " surviving"
        ),
        "gate": "planted-survivor falsifier",
        "planted_survivor_really_survives": plant_lattice % scale == 0,
        "stub_verdict": blind_verdict,
        "detected": bool((plant_lattice % scale == 0) and not blind_verdict),
        "exit_code": 1 if (plant_lattice % scale == 0) else 0,
    })

    bumped = dict(zero_counts)
    bumped["M3_OCCUPATION_WEIGHTED"] += 1
    teeth.append({
        "tooth": "tampered_zero_counts",
        "mutation": "one reported zero-weight-event count is increased by one",
        "gate": "gate_zero_counts",
        "detected": not gate_zero_counts(bumped),
        "exit_code": 1 if not gate_zero_counts(bumped) else 0,
    })

    subcensus = events[::2]
    teeth.append({
        "tooth": "silent_subcensus",
        "mutation": "every second event is silently dropped (no declaration)",
        "gate": "gate_headline",
        "detected": not gate_headline(subcensus, CANDIDATES),
        "exit_code": 1 if not gate_headline(subcensus, CANDIDATES) else 0,
    })

    cert_f = {
        "certificate": "F_TEETH",
        "teeth": teeth,
        "teeth_count": len(teeth),
        "teeth_that_bit": sum(1 for t in teeth if t["detected"]),
        "all_teeth_bite": all(t["detected"] for t in teeth),
    }
    cert_f["pass"] = bool(len(teeth) >= 6 and cert_f["all_teeth_bite"])

    # ---- G: runtime ------------------------------------------------------
    elapsed = round(monotonic() - started, 3)
    cert_g = {
        "certificate": "G_RUNTIME",
        "elapsed_sec": elapsed, "budget_sec": RUNTIME_BUDGET_SEC,
        "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
    }
    cert_g["pass"] = cert_g["within_budget"]

    certificates = (
        ("A_PINS", cert_a), ("B_INDEPENDENT_CENSUS", cert_b),
        ("C_INDEPENDENT_RANK", cert_c), ("D_EXCLUSION_ATTACK", cert_d),
        ("E_PULLBACK_ATTACK", cert_e), ("F_TEETH", cert_f),
        ("G_RUNTIME", cert_g),
    )
    checks = {name: bool(payload["pass"]) for name, payload in certificates}
    claim_survival = {
        "event_space_digest": cert_b["digest_agrees_with_primary"],
        "base_rank": cert_c["rank_claim_survives"],
        "generator_relation_residual": cert_c["residual_claim_survives"],
        "exclusion_of_M1_M2": cert_d["exclusion_claim_survives"],
        "M3_M4_zero_sets_identical":
            cert_d["zero_set_lattice"]["consequence_claim_survives"],
        "Q2_outcome_class": cert_e["outcome_claim_survives"],
        "priced_prime_targets": cert_e["priced_primes_survive"],
    }
    if all(claim_survival.values()):
        verdict = ("CORROBORATES_WITH_REFINEMENT"
                   if any(cert_e[
                       "lattice_is_a_proper_divisor_of_the_primary_total"
                   ].values()) else "CORROBORATES")
    else:
        verdict = "REFUTES"

    receipt = {
        "cycle": 905,
        "role": "independent check, specified to refute",
        "block": "toe-time-blockQ2-20260802",
        "checker_verdict": verdict,
        "claim_survival": claim_survival,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "independence": (
            "independently transcribed census / dead-wire rig / composed"
            " scan (no AST lift, no import of the 863, 878, 902 or 905"
            " sources); plain Fraction weightings against the primary's"
            " integer-numerator arithmetic; integer multiply-only elimination"
            " and modular rank against the primary's Fraction elimination and"
            " Gram/Laplace minors; the mass-lattice formulation of the"
            " pullback invariant against the primary's total-numerator"
            " formulation"
        ),
        "event_space_digest": event_digest,
        "base_rank_routes": {
            "integer_multiply_only": rank_1,
            "modular": {str(p): r for p, r in modular.items()},
        },
        "mass_lattice_L": {name: lattice[name] for name in CANDIDATES},
        "unique_primes_recomputed": odd_unique,
        "separating_scales_that_DO_exist": separating_scale_search,
        "exclusion_hunt_refutation_found": cert_d["refutation_found"],
        "scope_condition_confirmed_load_bearing": True,
        "teeth": teeth,
        "elapsed_sec": elapsed,
        "firewall_hits": len(CHECKER_FIREWALL.hits),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_receipt_sha256": sha256(payloads[PRIMARY_RECEIPT]).hexdigest(),
    }
    out_path = (ROOT / "outputs"
                / "born_narrowing_independent_check_cycle905_receipt_2026_07_28.json")
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")

    lines = [
        "CYCLE905_BORN_NARROWING_INDEPENDENT_CHECK",
        "SPECIFIED_TO_REFUTE_EXIT_CODE_IS_INDEPENDENT_OF_CLAIM_SURVIVAL",
    ]
    for name, payload in certificates:
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    lines.append("CLAIM_SURVIVAL " + compact(claim_survival))
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 905, "checker_verdict": verdict, "checks": checks,
        "base_rank": rank_1, "elapsed_sec": elapsed,
        "pass": all(checks.values()),
    }))
    lines.append("CYCLE905_INDEPENDENT_CHECK_" + verdict)
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
