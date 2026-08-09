#!/usr/bin/env python3
"""Cycle 905 (salvage pass) INDEPENDENT CHECK -- specified to REFUTE the
exact-algebra support facts.

This checker shares no computational code with the salvage primary.  It
BLOCKLISTS the primary and the legacy fixture-lineage modules from
import, rebuilds the stipulated composed record-write model from its own
independent in-file transcription (importing only the landed Cycle-719
core), and recomputes every certified statement by different routes:

  * an independently transcribed census, dead-wire rig and composed
    scan, with the dead-wire accumulation taken at CHUNK granularity
    across the whole derivation window -- strictly more sampling points
    than the primary uses, so equality of the resulting event census is
    a real check, not a copy;
  * plain Fraction weightings normalised to total mass 1, against the
    primary's integer-numerator-over-common-denominator arithmetic;
  * two rank routes that share nothing with the primary's: integer
    multiply-only elimination (no division anywhere, and in particular
    NO fraction-free / Bareiss exact-division bookkeeping, which
    corrupts ranks on rank-deficient matrices with skipped columns) and
    modular rank over three large primes, plus an exhibited nonsingular
    minor determinant;
  * event-level brute-force difference supports against the primary's
    world-level route;
  * an exhaustive positivity sweep over every cell of every declared
    family for the two everywhere-positive weightings, plus the min-mass
    argument covering ALL subsets;
  * an independently reconstructed integer-numerator convention,
    cross-checked event by event against the Fraction masses, from
    which the exact totals, total factorizations, and minimum
    numerators are REBUILT (never read from the claim);
  * the exhibited nonsingular minor rebuilt at the receipt's own
    advertised worlds, with its determinant recomputed;
  * per-family differing-cell SETS compared by canonical digest, not
    by count alone;
  * the certified-statement texts rebuilt verbatim from the checker's
    recomputed values and compared byte for byte.

The verdict covers EVERY certified statement and value family of the
primary receipt -- one claim_survival row each, none omitted, and
every row a recomputed comparison.  Each repaired gate carries a
planted negative mutation in the teeth certificate.  Fail-closed: the
exit code is 0 only if every certificate passes AND every claim row
survives; any refutation or gate failure exits 1.

Conditional finite-model support only.  No probability, no selection,
no interface claim, no negative universal claim.  Independent audit
still required.
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

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
PRIMARY_PATH = "scripts/frontier_cycle905_weighting_exact_algebra_2026_08_08.py"
PRIMARY_RECEIPT = "outputs/weighting_exact_algebra_cycle905_receipt_2026_08_08.json"

UPSTREAM_PATHS = (CORE_PATH,)
CLAIM_PATHS = (PRIMARY_PATH, PRIMARY_RECEIPT)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle905_weighting_exact_algebra_2026_08_08.py",
    "outputs/weighting_exact_algebra_cycle905_receipt_2026_08_08.json",
)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle905_weighting_exact_algebra_2026_08_08",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
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

# Independently transcribed scope inputs of the stipulated model.
BANKS = 2
SOURCE_MIN, SOURCE_MAX = 2, 5
HORIZON_ORBITS = 16_384
DEAD_WINDOW_ORBITS = 4_096
REGISTER_CAP = 64
CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")
ZERO_CARRYING = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
                 "M5_FORMATION_MOMENT")
EVERYWHERE_POSITIVE = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")
FAMILY_ORDER = (
    "F_WORLD", "F_TAG", "F_TAG_ORDINAL", "F_MOMENT", "F_ORBIT",
    "F_CONTENT", "F_WORLD_TAG", "F_ATOM",
)
MODULAR_PRIMES = (1_000_003, 2_000_003, 999_999_937)
FRACTION_LABEL = "bookkeeping fraction, not probability"


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
# An independently transcribed rebuild of the stipulated model
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
    strictly more sampling points than the primary's construction uses, so
    the dead set obtained here is contained in the primary's."""
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


def integer_numerators(events, occupation, formation, boundaries):
    """Independent reconstruction of the primary's integer-numerator
    convention: counting carries numerator 1 per event over total |E|;
    every world-weighted candidate carries a(w) * (common / |events(w)|)
    per event over total (sum_w a(w)) * common, where common is the lcm
    of the per-world event counts.  Used to REBUILD (never read) the
    exact totals, factorizations, and minimum numerators."""
    per_world = Counter(event[0] for event in events)
    supported = sorted(per_world)
    common = 1
    for count in set(per_world.values()):
        common = lcm(common, count)
    a_of = {
        "M2_PER_WORLD_UNIFORM": lambda w: 1,
        "M3_OCCUPATION_WEIGHTED": lambda w: occupation[w],
        "M4_FORMATION_LIFETIME": (
            lambda w: (boundaries - formation[w] + 1) if w in formation
            else 0
        ),
        "M5_FORMATION_MOMENT": (
            lambda w: formation[w] if w in formation else 0
        ),
    }
    nums = {"M1_COUNTING": [1] * len(events)}
    totals = {"M1_COUNTING": len(events)}
    for name, a in a_of.items():
        nums[name] = [
            a(event[0]) * (common // per_world[event[0]]) for event in events
        ]
        totals[name] = sum(a(w) for w in supported) * common
    return nums, totals, common


# ---------------------------------------------------------------------------
# Independent rank routes
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
    fraction-free (Bareiss) exact-division bookkeeping, which corrupts
    ranks on rank-deficient matrices with skipped columns."""
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
    claim = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    primary_sha = sha256(payloads[PRIMARY_PATH]).hexdigest()
    parsed = 0
    for path in (CORE_PATH, PRIMARY_PATH):
        ast.parse(payloads[path], filename=path)
        parsed += 1
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
    cert_a = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "python_pins_parsed_as_text_only": parsed,
        "core_sha256": sha256(payloads[CORE_PATH]).hexdigest(),
        "core_git_blob": git_blob(payloads[CORE_PATH]),
        "core_pin_matches": pins_ok,
        "primary_sha256": primary_sha,
        "primary_self_declared_sha256": claim.get("self_sha256"),
        "primary_sha_matches_its_own_receipt":
            primary_sha == claim.get("self_sha256"),
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(CHECKER_FIREWALL.hits),
        "checker_shares_no_computational_code_with_the_primary": True,
    }
    cert_a["pass"] = bool(
        pins_ok and cert_a["literal_ok"]
        and cert_a["primary_sha_matches_its_own_receipt"]
        and not cert_a["blocked_modules_loaded"]
        and not cert_a["firewall_hits"]
    )
    if not cert_a["pass"]:
        sys.stdout.write(
            "CERTIFICATE A_PINS FAIL " + compact(cert_a) + "\n"
            + "CYCLE905_WEIGHTING_EXACT_ALGEBRA_CHECK_PIN_FAILURE\n"
        )
        return 2

    # ---- B: independent census ------------------------------------------
    build = rebuild()
    events = build["events"]
    stations = build["stations"]
    formation = build["formation"]
    occupation = build["occupation"]
    boundaries = build["boundaries"]
    world_of = [event[0] for event in events]
    worlds = sorted(set(world_of))
    event_digest = digest(events)
    never_formed_events = {i for i, w in enumerate(world_of)
                           if w not in formation}
    masses, per_world, supported = weightings(
        events, occupation, formation, boundaries
    )
    zero_sets = {name: frozenset(i for i, m in enumerate(masses[name])
                                 if m == 0)
                 for name in CANDIDATES}
    zero_counts = {name: len(zero_sets[name]) for name in CANDIDATES}

    # Rebuild the primary's integer-numerator convention independently
    # and cross-check it event by event against the Fraction masses.
    # The exact totals, total factorizations, minimum numerators, and
    # the exhibited minor are then REBUILT from this reconstruction --
    # never read from the claim.
    int_nums, totals_rebuilt, common_rebuilt = integer_numerators(
        events, occupation, formation, boundaries
    )
    numerator_mass_consistency = all(
        Fraction(int_nums[name][i], totals_rebuilt[name]) == masses[name][i]
        for name in CANDIDATES for i in range(len(events))
    )
    total_sums_consistent = all(
        sum(int_nums[name]) == totals_rebuilt[name] for name in CANDIDATES
    )
    min_numerators_rebuilt = {name: min(int_nums[name])
                              for name in CANDIDATES}

    def gate_totals(claimed):
        return claimed == totals_rebuilt

    total_factors_rebuilt = {
        name: {str(p): e
               for p, e in sorted(factorize(totals_rebuilt[name]).items())}
        for name in CANDIDATES
    }

    def gate_total_factorizations(claimed):
        return claimed == total_factors_rebuilt

    def gate_min_numerators(claimed):
        return claimed == min_numerators_rebuilt

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
            row["events"] == 92_260
            and row["worlds"] == 748
            and row["atoms_are_singletons"]
            and row["by_tag"] == {"B0": 47_872, "B1": 44_224, "F": 164}
            and len(weight_names) == 5
        )

    def gate_zero_counts(counts):
        return counts == claim.get("zero_weight_events")

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
        "headline_reproduces": gate_headline(events, CANDIDATES),
        "zero_weight_events_rebuilt": zero_counts,
        "zero_weight_events_primary": claim.get("zero_weight_events"),
        "zero_counts_reproduce": gate_zero_counts(zero_counts),
        "integrity": {
            "rewrites": build["rewrites"], "mismatches": build["mismatches"],
            "seed_failures": build["seed_failures"],
            "state_failures": build["state_failures"],
        },
        "worlds_formed": len(formation),
        "worlds_never_formed": len(worlds) - len(formation),
        "slots_touch_gates": len(
            set(build["rig"]["slot_of"].values())
            & (build["rig"]["gate_inputs"] | build["rig"]["gate_targets"])
        ),
        "integer_numerator_convention_consistent_with_masses":
            numerator_mass_consistency,
        "integer_numerator_totals_consistent": total_sums_consistent,
        "common_denominator_rebuilt": common_rebuilt,
    }
    cert_b["pass"] = bool(
        cert_b["headline_reproduces"] and cert_b["zero_counts_reproduce"]
        and cert_b["digest_agrees_with_primary"]
        and build["rewrites"] == 0 and build["mismatches"] == 0
        and build["seed_failures"] == 0 and build["state_failures"] == 0
        and cert_b["slots_touch_gates"] == 0
        and numerator_mass_consistency and total_sums_consistent
    )

    # ---- C: independent rank --------------------------------------------
    matrix = integer_rows([masses[name] for name in CANDIDATES])
    rank_1, pivots_1 = rank_multiply_only(matrix)
    modular = {p: rank_modular(matrix, p) for p in MODULAR_PRIMES}
    rank_2 = max(modular.values())
    minor = [[matrix[r][c] for c in pivots_1] for r in range(len(matrix))] \
        if len(pivots_1) == len(matrix) else None
    minor_determinant = determinant(minor) if minor else None
    claimed_rank = claim.get("rank")

    def gate_rank(route_one, route_two):
        return route_one == route_two == claimed_rank

    triple = integer_rows([masses[name] for name in ZERO_CARRYING])
    rank_triple_1, _ = rank_multiply_only(triple)
    rank_triple_2 = max(rank_modular(triple, p) for p in MODULAR_PRIMES)
    coefficient_residual = {
        w: (boundaries + 1) * 1
        - ((boundaries - formation[w] + 1) if w in formation else 0)
        - (formation[w] if w in formation else 0)
        for w in worlds
    }
    residual_nonzero = {
        i for i, w in enumerate(world_of) if coefficient_residual[w] != 0
    }
    first_index = {}
    for index, world in enumerate(world_of):
        first_index.setdefault(world, index)

    def gate_minor(claimed_minor):
        """Rebuild the minor matrix at the receipt's OWN advertised
        worlds from the independently reconstructed integer numerators,
        then require matrix equality, determinant equality, and a
        nonzero determinant."""
        worlds_claimed = claimed_minor.get("worlds") or []
        matrix_claimed = claimed_minor.get("matrix") or []
        det_claimed = claimed_minor.get("determinant")
        if not worlds_claimed or not matrix_claimed \
                or any(w not in first_index for w in worlds_claimed):
            return False, None, None
        rebuilt = [
            [int_nums[name][first_index[w]] for w in worlds_claimed]
            for name in CANDIDATES
        ]
        det_rebuilt = determinant(rebuilt)
        ok = bool(
            rebuilt == [list(row) for row in matrix_claimed]
            and det_rebuilt == det_claimed and det_rebuilt != 0
        )
        return ok, rebuilt, det_rebuilt

    primary_minor = claim.get("nonsingular_minor", {})
    minor_ok, minor_rebuilt, minor_det_rebuilt = gate_minor(primary_minor)
    cert_c = {
        "certificate": "C_INDEPENDENT_RANK",
        "route_1_integer_multiply_only": {
            "rank": rank_1, "pivot_columns": list(pivots_1),
            "no_division_used": True, "bareiss_used": False,
        },
        "route_2_modular": {
            "rank": rank_2, "per_prime": {str(p): r for p, r in modular.items()},
            "reading": "rank over GF(p) is a lower bound for the rational"
                       " rank; a full modular rank certifies it",
        },
        "routes_agree": rank_1 == rank_2,
        "nonsingular_minor_determinant": minor_determinant,
        "minor_certifies_rank": bool(minor_determinant not in (None, 0)),
        "primary_claimed_rank": claimed_rank,
        "rank_claim_survives": gate_rank(rank_1, rank_2),
        "zero_carrying_triple_rank": [rank_triple_1, rank_triple_2],
        "triple_rank_claim_survives": rank_triple_1 == rank_triple_2
        == claim.get("zero_carrying_triple_rank"),
        "primary_minor_rebuilt_at_advertised_worlds": {
            "worlds": primary_minor.get("worlds"),
            "matrix_rebuilt": minor_rebuilt,
            "determinant_rebuilt": minor_det_rebuilt,
            "matrix_and_determinant_match_claim_and_nonzero": minor_ok,
        },
        "primary_minor_survives": minor_ok,
        "coefficient_identity": {
            "tested_at": "the world coefficients, in a common scaling",
            "violations": sum(
                1 for w in formation if coefficient_residual[w] != 0
            ),
            "holds_on_formed_worlds": all(
                coefficient_residual[w] == 0 for w in formation
            ),
            "residual_nonzero_events": len(residual_nonzero),
            "residual_set_equals_never_formed_block":
                residual_nonzero == never_formed_events,
        },
        "primary_claimed_residual_events":
            claim.get("residual_nonzero_events"),
        "residual_claim_survives":
            len(residual_nonzero) == claim.get("residual_nonzero_events")
            and residual_nonzero == never_formed_events,
    }
    cert_c["pass"] = bool(
        cert_c["routes_agree"] and cert_c["minor_certifies_rank"]
        and cert_c["rank_claim_survives"]
        and cert_c["triple_rank_claim_survives"]
        and cert_c["residual_claim_survives"]
        and cert_c["primary_minor_survives"]
    )

    # ---- D: zero sets, identities, positivity sweep ---------------------
    families = {
        "F_WORLD": lambda e: ("w", e[0]),
        "F_TAG": lambda e: ("t", e[2]),
        "F_TAG_ORDINAL": lambda e: ("to", e[2], e[3]),
        "F_MOMENT": lambda e: ("m", e[1]),
        "F_ORBIT": lambda e: ("o", 0 if e[1] == 0
                              else ((e[1] - 1) // stations) + 1),
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
    sweep = {}
    for name in EVERYWHERE_POSITIVE:
        vector = masses[name]
        zero_cells_found = 0
        inspected = 0
        for family, table in cells.items():
            for key, indices in table.items():
                inspected += 1
                if sum(vector[i] for i in indices) == 0:
                    zero_cells_found += 1
        sweep[name] = {
            "cells_inspected": inspected,
            "zero_mass_cells_found": zero_cells_found,
            "minimum_event_mass": str(min(vector)),
            "minimum_is_positive": min(vector) > 0,
            "reading": (
                "every event carries strictly positive mass, so EVERY"
                " nonempty subset of the census -- not merely every cell"
                " of a declared family -- has positive mass; the cell"
                " sweep is a redundant second route to the same"
                " hypothesis-side fact of the primary's one-way"
                " positivity lemma"
            ),
        }
    formed_at_zero_worlds = {w for w, b in formation.items() if b == 0}
    moment_zero_events = {i for i, w in enumerate(world_of)
                          if w in formed_at_zero_worlds}
    identities = {
        "zero_M3_equals_zero_M4_as_sets":
            zero_sets["M3_OCCUPATION_WEIGHTED"]
            == zero_sets["M4_FORMATION_LIFETIME"],
        "zero_M3_strict_subset_of_zero_M5":
            zero_sets["M3_OCCUPATION_WEIGHTED"]
            < zero_sets["M5_FORMATION_MOMENT"],
        "zero_M3_equals_never_formed_block":
            set(zero_sets["M3_OCCUPATION_WEIGHTED"]) == never_formed_events,
        "zero_M5_equals_block_plus_moment_zero_worlds":
            set(zero_sets["M5_FORMATION_MOMENT"])
            == never_formed_events | moment_zero_events,
        "distinct_zero_sets_among_the_zero_carrying_triple": len({
            zero_sets[name] for name in ZERO_CARRYING
        }),
    }
    IDENTITY_KEYS = (
        "zero_M3_equals_zero_M4_as_sets",
        "zero_M3_strict_subset_of_zero_M5",
        "zero_M3_equals_never_formed_block",
        "zero_M5_equals_block_plus_moment_zero_worlds",
    )

    def gate_identities(claimed_ids):
        return all(
            identities[k] is True and claimed_ids.get(k) is True
            for k in IDENTITY_KEYS
        )

    claimed_identities = claim.get("zero_set_identities", {})
    cert_d = {
        "certificate": "D_ZERO_SETS_AND_POSITIVITY",
        "positivity_sweep": sweep,
        "identities_recomputed": identities,
        "identities_claimed": {
            k: claimed_identities.get(k) for k in IDENTITY_KEYS
        },
        "identities_survive": gate_identities(claimed_identities),
        "min_event_numerators_rebuilt": min_numerators_rebuilt,
        "min_event_numerators_claimed": claim.get("min_event_numerators"),
        "min_numerators_survive":
            gate_min_numerators(claim.get("min_event_numerators")),
        "min_mass_survives": all(
            sweep[name]["minimum_is_positive"]
            and sweep[name]["zero_mass_cells_found"] == 0
            for name in EVERYWHERE_POSITIVE
        ),
    }
    cert_d["pass"] = bool(
        cert_d["identities_survive"] and cert_d["min_mass_survives"]
        and cert_d["min_numerators_survive"]
        and gate_zero_counts(zero_counts)
    )

    # ---- E: difference supports, brute force at event level -------------
    pairs = [(a, b) for i, a in enumerate(CANDIDATES)
             for b in CANDIDATES[i + 1:]]
    support_sets = {}
    for a, b in pairs:
        va, vb = masses[a], masses[b]
        support_sets[f"{a}|{b}"] = [
            i for i in range(len(events)) if va[i] != vb[i]
        ]
    support_counts = {k: len(v) for k, v in support_sets.items()}
    support_digests = {k: digest(v) for k, v in support_sets.items()}
    triple_pair_names = [f"{a}|{b}" for a, b in pairs
                        if a in ZERO_CARRYING and b in ZERO_CARRYING]
    triple_identical = len({
        tuple(support_sets[p]) for p in triple_pair_names
    }) == 1
    values_differ_on_triple_supports = all(
        any(masses[p.split("|")[0]][i] != masses[p.split("|")[1]][i]
            for i in support_sets[p][:1])
        for p in triple_pair_names
    )
    cert_e = {
        "certificate": "E_DIFFERENCE_SUPPORTS",
        "method": (
            "brute-force event-level comparison of normalised Fraction"
            " masses, against the primary's world-level route"
        ),
        "cardinalities_recomputed": support_counts,
        "cardinalities_claimed": claim.get(
            "difference_support_cardinalities"),
        "cardinalities_survive": support_counts
        == claim.get("difference_support_cardinalities"),
        "support_digests_recomputed": support_digests,
        "support_digests_claimed": claim.get("difference_support_digests"),
        "support_digests_survive": support_digests
        == claim.get("difference_support_digests"),
        "zero_carrying_supports_identical_as_sets": triple_identical,
        "identity_claim_survives": bool(
            triple_identical
            and claim.get("zero_carrying_supports_identical_as_sets") is True
        ),
        "values_differ_on_shared_supports": values_differ_on_triple_supports,
        "label": FRACTION_LABEL,
    }
    per_family_counts = {}
    per_family_digests = {}
    per_family_pairwise_digests = {}
    per_family_setwise_identical = {}
    int_rows = {name: row for name, row in zip(CANDIDATES, matrix)}
    lattice_scale = {}
    for name in CANDIDATES:
        scale = 1
        for value in masses[name]:
            scale = lcm(scale, value.denominator)
        lattice_scale[name] = scale
    for fam in FAMILY_ORDER:
        table = cells[fam]
        cell_masses = {
            name: {
                key: Fraction(sum(int_rows[name][i] for i in idx),
                              lattice_scale[name])
                for key, idx in table.items()
            }
            for name in ZERO_CARRYING
        }
        counts = {}
        digests = {}
        for pair_name in triple_pair_names:
            a, b = pair_name.split("|")
            differing = sorted(
                key for key in table
                if cell_masses[a][key] != cell_masses[b][key]
            )
            counts[pair_name] = len(differing)
            digests[pair_name] = digest([compact(list(k))
                                         for k in differing])
        per_family_setwise_identical[fam] = len(set(digests.values())) == 1
        per_family_counts[fam] = (
            counts[triple_pair_names[0]]
            if len(set(counts.values())) == 1 else sorted(counts.values())
        )
        per_family_pairwise_digests[fam] = digests
        per_family_digests[fam] = digests[triple_pair_names[0]]

    def gate_per_family_counts(claimed):
        return claimed == per_family_counts

    def gate_per_family_digests(claimed):
        return bool(
            claimed == per_family_digests
            and all(per_family_setwise_identical.values())
        )

    cert_e["per_family_differing_cells_recomputed"] = per_family_counts
    cert_e["per_family_differing_cells_claimed"] = claim.get(
        "per_family_differing_cells_zero_carrying")
    cert_e["per_family_counts_survive"] = gate_per_family_counts(
        claim.get("per_family_differing_cells_zero_carrying"))
    cert_e["per_family_differing_cell_digests_recomputed"] = \
        per_family_digests
    cert_e["per_family_differing_cell_digests_claimed"] = claim.get(
        "per_family_differing_cell_digests_zero_carrying")
    cert_e["per_family_cell_sets_identical_across_pairs"] = \
        per_family_setwise_identical
    cert_e["per_family_digests_survive"] = gate_per_family_digests(
        claim.get("per_family_differing_cell_digests_zero_carrying"))
    cert_e["pass"] = bool(
        cert_e["cardinalities_survive"] and cert_e["support_digests_survive"]
        and cert_e["identity_claim_survives"]
        and values_differ_on_triple_supports
        and cert_e["per_family_counts_survive"]
        and cert_e["per_family_digests_survive"]
    )

    # ---- F: totals, lattices, and factorizations ------------------------
    lattices = dict(lattice_scale)
    lattice_factors = {
        name: {str(p): e for p, e in sorted(factorize(lattices[name]).items())}
        for name in CANDIDATES
    }
    normalization = {
        name: sum(masses[name]) == 1 for name in CANDIDATES
    }
    cert_f = {
        "certificate": "F_MASS_LATTICES",
        "own_invariant": (
            "the census MASS LATTICE: every event mass is rational, so"
            " every subset mass lies in (1/L)Z where L is the lcm of the"
            " event-mass denominators.  A demanded denominator q is"
            " realizable only if q divides L.  NECESSARY FILTER ONLY --"
            " nothing here decides which denominators are achieved by"
            " actual subsets, and no candidate is selected or eliminated"
        ),
        "normalization_total_mass_one": normalization,
        "totals_rebuilt_from_model": totals_rebuilt,
        "totals_claimed": claim.get("totals"),
        "totals_survive": gate_totals(claim.get("totals")),
        "mass_lattices_recomputed": lattices,
        "mass_lattices_claimed": claim.get("mass_lattices"),
        "lattices_survive": lattices == claim.get("mass_lattices"),
        "lattice_factorizations_recomputed": lattice_factors,
        "lattice_factorizations_claimed": claim.get(
            "lattice_factorizations"),
        "lattice_factorizations_survive": lattice_factors
        == claim.get("lattice_factorizations"),
        "total_factorizations_rebuilt_from_model": total_factors_rebuilt,
        "total_factorizations_claimed": claim.get("total_factorizations"),
        "total_factorizations_survive":
            gate_total_factorizations(claim.get("total_factorizations")),
        "lattice_divides_rebuilt_total": {
            name: totals_rebuilt[name] % lattices[name] == 0
            for name in CANDIDATES
        },
    }
    cert_f["pass"] = bool(
        all(normalization.values())
        and cert_f["totals_survive"]
        and cert_f["lattices_survive"]
        and cert_f["lattice_factorizations_survive"]
        and cert_f["total_factorizations_survive"]
        and all(cert_f["lattice_divides_rebuilt_total"].values())
    )

    # ---- G: certified-statement texts rebuilt verbatim -------------------
    identity_violations = sum(
        1 for w in worlds
        if (((boundaries - formation[w] + 1) if w in formation else 0)
            + (formation[w] if w in formation else 0))
        != (boundaries + 1) * int(w in formation)
    )
    m5_extra_events = set(zero_sets["M5_FORMATION_MOMENT"]) \
        - set(zero_sets["M3_OCCUPATION_WEIGHTED"])
    triple_support_size = len(support_sets[triple_pair_names[0]])
    expected_statements = {
        "base_rank_statement": (
            f"on the stipulated model the five candidate weightings have"
            f" rank {rank_1} as functions on the {len(events)}-event"
            " census (three agreeing routes; an exhibited nonsingular"
            " 5 x 5 minor); the three zero-carrying candidates alone have"
            f" rank {rank_triple_1}"
        ),
        "coefficient_identity_statement": (
            "the world-coefficient identity a4 + a5 = (boundaries + 1) *"
            f" [formed] holds on all {len(worlds)} world rows"
            f" ({identity_violations} violations); the candidate"
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
            f" {len(m5_extra_events)} events)"
        ),
        "difference_support_statement": (
            "all ten candidate pairs differ somewhere; the three"
            " zero-carrying pairs differ on IDENTICALLY the same"
            f" {triple_support_size} events (the"
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
        "one_way_positivity_lemma": (
            "CONDITIONAL, ONE-WAY: if a weighting's event masses are"
            " strictly positive on every event, then every NONEMPTY"
            " subset of events carries strictly positive total mass;"
            " hence such a weighting cannot satisfy any constraint"
            " that would require zero total mass on some nonempty"
            " subset.  On this model the hypothesis holds for M1 and"
            " M2 (minimum event numerators 1 and 8320)."
        ),
    }

    def gate_statements(claimed):
        return claimed == expected_statements

    cert_stmt = {
        "certificate": "G_CERTIFIED_STATEMENTS",
        "method": (
            "the primary's certified-statement texts are deterministic"
            " renderings of computed values; this checker rebuilds each"
            " text verbatim from its OWN recomputed values and compares"
            " byte for byte, so tampered prose fails closed"
        ),
        "statements_expected_keys": sorted(expected_statements),
        "statements_claimed_keys": sorted(claim.get(
            "certified_statements", {})),
        "statements_survive": gate_statements(
            claim.get("certified_statements")),
    }
    cert_stmt["pass"] = bool(cert_stmt["statements_survive"])

    # ---- H: teeth (one planted corruption per repaired gate class) -------
    teeth = []

    tampered = dict(payloads)
    tampered[CORE_PATH] = payloads[CORE_PATH].replace(b"def ", b"dEf ", 1)
    teeth.append({
        "tooth": "tampered_core_pin",
        "mutation": "one byte of the pinned Cycle-719 core is flipped",
        "gate": "gate_pins",
        "detected": not gate_pins(tampered),
    })

    dropped = tuple(n for n in CANDIDATES if n != "M5_FORMATION_MOMENT")
    teeth.append({
        "tooth": "dropped_weighting",
        "mutation": "M5_FORMATION_MOMENT is removed from the candidate set",
        "gate": "gate_headline (five weightings)",
        "detected": not gate_headline(events, dropped),
    })

    teeth.append({
        "tooth": "hardcoded_rank",
        "mutation": "route 2 returns the literal 4 instead of computing",
        "gate": "gate_rank (two-route agreement)",
        "detected": not gate_rank(rank_1, 4),
    })

    bumped = dict(zero_counts)
    bumped["M3_OCCUPATION_WEIGHTED"] += 1
    teeth.append({
        "tooth": "tampered_zero_counts",
        "mutation": "one reported zero-weight-event count is increased by one",
        "gate": "gate_zero_counts",
        "detected": not gate_zero_counts(bumped),
    })

    skipped = [e for e in events if e[2] != "F"]
    teeth.append({
        "tooth": "skipped_event_class",
        "mutation": "every F-tag (formation) event is dropped from the census",
        "gate": "gate_headline",
        "detected": not gate_headline(skipped, CANDIDATES),
    })

    subcensus = events[::2]
    teeth.append({
        "tooth": "silent_subcensus",
        "mutation": "every second event is silently dropped (no declaration)",
        "gate": "gate_headline",
        "detected": not gate_headline(subcensus, CANDIDATES),
    })

    tampered_lattice = dict(lattices)
    tampered_lattice["M3_OCCUPATION_WEIGHTED"] *= 2
    teeth.append({
        "tooth": "tampered_lattice",
        "mutation": "one recomputed mass lattice is doubled",
        "gate": "lattices_survive",
        "detected": tampered_lattice != claim.get("mass_lattices"),
    })

    tampered_support = dict(support_counts)
    first_pair = triple_pair_names[0]
    tampered_support[first_pair] += 1
    teeth.append({
        "tooth": "tampered_difference_support",
        "mutation": "one difference-support cardinality is increased by one",
        "gate": "cardinalities_survive",
        "detected": tampered_support
        != claim.get("difference_support_cardinalities"),
    })

    totals_mut = dict(claim.get("totals", {}))
    totals_mut["M1_COUNTING"] = totals_mut.get("M1_COUNTING", 0) * 2
    factors_mut = {k: dict(v) for k, v in claim.get(
        "total_factorizations", {}).items()}
    if "M1_COUNTING" in factors_mut:
        factors_mut["M1_COUNTING"]["2"] = \
            factors_mut["M1_COUNTING"].get("2", 0) + 1
    teeth.append({
        "tooth": "tampered_totals_with_consistent_factorization",
        "mutation": (
            "the claimed M1 total is doubled AND its stated factorization"
            " is updated consistently; both rebuilt-value gates must bite"
        ),
        "gate": "gate_totals + gate_total_factorizations (rebuilt values)",
        "detected": bool(not gate_totals(totals_mut)
                         and not gate_total_factorizations(factors_mut)),
    })

    min_mut = dict(claim.get("min_event_numerators", {}))
    min_mut["M2_PER_WORLD_UNIFORM"] = 8319
    teeth.append({
        "tooth": "tampered_min_numerator",
        "mutation": "the claimed M2 minimum numerator 8320 becomes 8319",
        "gate": "gate_min_numerators (rebuilt values)",
        "detected": not gate_min_numerators(min_mut),
    })

    minor_mut = dict(primary_minor)
    if minor_mut.get("worlds"):
        mut_worlds = list(minor_mut["worlds"])
        mut_worlds[-1] = mut_worlds[-1] + 1
        minor_mut["worlds"] = mut_worlds
    minor_mut_ok, _, _ = gate_minor(minor_mut)
    teeth.append({
        "tooth": "tampered_minor_worlds",
        "mutation": (
            "the exhibited minor's last advertised world is shifted by one"
            " while the old matrix is retained"
        ),
        "gate": "gate_minor (matrix rebuilt at advertised worlds)",
        "detected": not minor_mut_ok,
    })

    ids_mut = dict(claimed_identities)
    ids_mut["zero_M5_equals_block_plus_moment_zero_worlds"] = False
    teeth.append({
        "tooth": "flipped_m5_identity",
        "mutation": (
            "the claimed M5 block-plus-moment-zero identity is flipped to"
            " false"
        ),
        "gate": "gate_identities",
        "detected": not gate_identities(ids_mut),
    })

    digests_mut = dict(claim.get(
        "per_family_differing_cell_digests_zero_carrying", {}))
    if "F_ATOM" in digests_mut:
        old = digests_mut["F_ATOM"]
        digests_mut["F_ATOM"] = ("0" if old[:1] != "0" else "1") + old[1:]
    teeth.append({
        "tooth": "tampered_per_family_digest",
        "mutation": "one per-family differing-cell-set digest is altered",
        "gate": "gate_per_family_digests",
        "detected": not gate_per_family_digests(digests_mut),
    })

    stmt_mut = dict(claim.get("certified_statements", {}))
    stmt_mut["difference_support_statement"] = (
        "the three zero-carrying candidates are indistinguishable"
    )
    teeth.append({
        "tooth": "tampered_statement_text",
        "mutation": (
            "one certified-statement text is replaced by false prose"
        ),
        "gate": "gate_statements (verbatim rebuild)",
        "detected": not gate_statements(stmt_mut),
    })

    cert_teeth = {
        "certificate": "H_TEETH",
        "teeth": teeth,
        "teeth_count": len(teeth),
        "teeth_that_bit": sum(1 for t in teeth if t["detected"]),
        "all_teeth_bite": all(t["detected"] for t in teeth),
    }
    cert_teeth["pass"] = bool(
        len(teeth) >= 14 and cert_teeth["all_teeth_bite"]
    )

    # ---- I: runtime ------------------------------------------------------
    elapsed = round(monotonic() - started, 3)
    cert_runtime = {
        "certificate": "I_RUNTIME",
        "elapsed_sec": elapsed, "budget_sec": AUDIT_TIMEOUT_SEC,
        "within_budget": elapsed <= AUDIT_TIMEOUT_SEC,
    }
    cert_runtime["pass"] = cert_runtime["within_budget"]

    certificates = (
        ("A_PINS", cert_a), ("B_INDEPENDENT_CENSUS", cert_b),
        ("C_INDEPENDENT_RANK", cert_c),
        ("D_ZERO_SETS_AND_POSITIVITY", cert_d),
        ("E_DIFFERENCE_SUPPORTS", cert_e), ("F_MASS_LATTICES", cert_f),
        ("G_CERTIFIED_STATEMENTS", cert_stmt), ("H_TEETH", cert_teeth),
        ("I_RUNTIME", cert_runtime),
    )
    checks = {name: bool(payload["pass"]) for name, payload in certificates}
    # One survival row for EVERY certified statement and value family of
    # the primary receipt -- none omitted, every row a recomputed
    # comparison.
    claim_survival = {
        "event_space_digest": cert_b["digest_agrees_with_primary"],
        "base_rank": cert_c["rank_claim_survives"],
        "zero_carrying_triple_rank": cert_c["triple_rank_claim_survives"],
        "nonsingular_minor_rebuilt_at_worlds":
            cert_c["primary_minor_survives"],
        "coefficient_identity_and_residual_set":
            cert_c["residual_claim_survives"],
        "zero_counts": gate_zero_counts(zero_counts),
        "zero_set_identities_incl_M5": cert_d["identities_survive"],
        "everywhere_positive_min_mass": cert_d["min_mass_survives"],
        "min_event_numerators_rebuilt": cert_d["min_numerators_survive"],
        "totals_rebuilt": cert_f["totals_survive"],
        "total_factorizations_rebuilt":
            cert_f["total_factorizations_survive"],
        "mass_lattices": cert_f["lattices_survive"],
        "lattice_factorizations": cert_f["lattice_factorizations_survive"],
        "difference_support_cardinalities": cert_e["cardinalities_survive"],
        "difference_support_sets": cert_e["support_digests_survive"],
        "zero_carrying_supports_identical": cert_e["identity_claim_survives"],
        "per_family_differing_cells": cert_e["per_family_counts_survive"],
        "per_family_differing_cell_sets": cert_e["per_family_digests_survive"],
        "certified_statements_text": cert_stmt["statements_survive"],
    }
    verdict = "CORROBORATES" if all(claim_survival.values()) else "REFUTES"

    receipt = {
        "cycle": 905,
        "role": "independent check, specified to refute",
        "checker_verdict": verdict,
        "claim_survival": claim_survival,
        "claim_survival_rows": len(claim_survival),
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "independence": (
            "independently transcribed census / dead-wire rig / composed"
            " scan (no AST lift, no import of the primary); plain Fraction"
            " weightings plus an independently reconstructed"
            " integer-numerator convention against the primary's"
            " arithmetic; integer multiply-only elimination and modular"
            " rank against the primary's Fraction elimination and"
            " Gram/Laplace minors; event-level brute-force difference"
            " supports against the primary's world-level route; totals,"
            " factorizations, minimum numerators, the minor matrix, and"
            " the certified-statement texts REBUILT from the model, never"
            " read from the claim"
        ),
        "event_space_digest": event_digest,
        "base_rank_routes": {
            "integer_multiply_only": rank_1,
            "modular": {str(p): r for p, r in modular.items()},
        },
        "totals_rebuilt_from_model": totals_rebuilt,
        "min_event_numerators_rebuilt": min_numerators_rebuilt,
        "mass_lattices": lattices,
        "teeth": teeth,
        "elapsed_sec": elapsed,
        "firewall_hits": len(CHECKER_FIREWALL.hits),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_receipt_sha256": sha256(payloads[PRIMARY_RECEIPT]).hexdigest(),
        "label_on_every_fraction": FRACTION_LABEL,
        "boundary": (
            "conditional finite-model support only: no probability, no"
            " occurrence rule, no update law, no selection, no"
            " elimination, no interface or bridge claim, no negative"
            " universal claim"
        ),
    }
    out_path = (
        ROOT / "outputs"
        / "weighting_exact_algebra_independent_check_cycle905_receipt_2026_08_08.json"
    )
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")

    lines = [
        "CYCLE905_WEIGHTING_EXACT_ALGEBRA_INDEPENDENT_CHECK",
        "SPECIFIED_TO_REFUTE_FAIL_CLOSED_EXIT_NONZERO_ON_ANY_REFUTATION",
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
        "pass": all(checks.values()) and verdict == "CORROBORATES",
    }))
    lines.append("CYCLE905_SALVAGE_INDEPENDENT_CHECK_" + verdict)
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if (all(checks.values()) and verdict == "CORROBORATES") else 1


if __name__ == "__main__":
    sys.exit(main())
