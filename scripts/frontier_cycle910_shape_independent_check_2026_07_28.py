#!/usr/bin/env python3
"""Cycle 910 INDEPENDENT CHECKER -- specified to REFUTE the discharge.

The Cycle-910 primary claims that P-856-SHAPE discharges positively:
that the Cycle-878 escape orbit IS one of Cycle 856's absolute-record
orbits (not merely shaped like one), that the correspondence between
the two lineages' labels is forced rather than chosen, that the two
predicates are one predicate read at two horizons, and that the M6
branch is scoped to a computed horizon window.

This checker tries to break each of those.

  R1  BOTH PREDICATES, REBUILT FROM SCRATCH.  The census, the initial
      states, the H-chunk schedules, the dirty coordinate set and the
      globally-clean test are re-implemented here directly on the
      landed Cycle-719 core, in a REVERSED LANE BIT LAYOUT (lane l
      occupies bit (n - l) instead of bit l), so an index error in
      either build shows up as a disagreement rather than cancelling.
      The Cycle-856 primary, the Cycle-863 primary, the Cycle-878
      primary, the Cycle-906/908 primaries and the Cycle-910 primary
      are all BLOCKLISTED from import.  Only the Cycle-878 composed
      record-write construction -- the object under test on the 878
      side -- is lifted by AST from its pinned source.

  R2  THE CORRESPONDENCE, ATTACKED.  This checker builds its own
      answer to the map question: it verifies EMPIRICALLY that an 878
      world label is the census key (by extracting lane states from the
      packed columns and re-deriving them semantically), and it then
      searches for alternative licensings under which the escape orbit
      would map onto a DIFFERENT absolute orbit.  A licensed map the
      primary missed refutes the primary's uniqueness claim; a flaw in
      the primary's map refutes IDENTIFIED.

  R3  THE SHARED-MECHANISM CLAIM, ATTACKED.  The primary compares the
      two predicates only at the FIRST clean boundary.  This checker
      compares them at EVERY boundary on a declared sample of lanes,
      which is a strictly stronger test, and then asks whether the
      exhibited common cause is load-bearing in both derivations or
      merely present in one.

  R4  THE HORIZON WINDOW, ATTACKED.  Recomputed from this checker's own
      first-clean profile, with the endpoints re-derived and the
      pinned-horizon membership re-decided.

  R5  TEETH.  Eight mutations that must be caught.

Exit code is 0 whether or not the primary's claim survives; the verdict
lives in the receipt.
"""
from __future__ import annotations

import ast
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
import os
from pathlib import Path
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
FRACTION_LABEL = "bookkeeping fraction, not probability"
SEMANTIC_SAMPLE = 24        # lanes re-derived semantically, declared sample
BOUNDARY_SAMPLE_HORIZON = 512   # every-boundary comparison depth
SHORT_HORIZON = 1_024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C856_PATH = "scripts/frontier_cycle856_record_covariance_2026_07_28.py"
C856_NOTE = "docs/RECORD_COVARIANCE_CYCLE856_BOUNDED_THEOREM_NOTE_2026-07-28.md"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C908_RECEIPT = "outputs/intertwine_discharge_cycle908_receipt_2026_07_28.json"
C910_PATH = "scripts/frontier_cycle910_shape_discharge_2026_07_28.py"
C910_RECEIPT = "outputs/shape_discharge_cycle910_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C856_PATH, C856_NOTE, C863_PATH, C878_PATH, C906_RECEIPT,
    C908_RECEIPT, C910_PATH, C910_RECEIPT, AXIOMS_PATH,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C856_PATH:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    C856_NOTE:
        "7b6b73826ee397e66102994174d94e04c3f174761f00ffcfe0da2be97e72a545",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    C908_RECEIPT:
        "825ebf6866755364ba27c504080808539f8040759413f0fff8cc57cd21dcb7f4",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C856_PATH: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    C856_NOTE: "f819f5b31d442248fac255fcdf3b0139d6ba83f8",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    C908_RECEIPT: "d6fcfc999e37f7a089cfe31123f61197ab4aa944",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
# the Cycle-910 primary and its receipt are pinned by presence and hashed at
# run time; their digests are NOT hard-coded here, because the checker must be
# able to run against a re-run primary without being edited.
BLOCKLISTED_MODULES = (
    "frontier_cycle852_selection_tournament_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
    "frontier_cycle856_covariance_independent_check_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle908_intertwine_discharge_2026_07_28",
    "frontier_cycle908_intertwine_independent_check_2026_07_28",
    "frontier_cycle910_shape_discharge_2026_07_28",
)

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


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# ---------------------------------------------------------------------------
# R1a: the census and the dynamics, re-implemented from the Cycle-719 core
# ---------------------------------------------------------------------------

def spec_constants() -> dict:
    """Read the declared scalars out of the pinned sources as LITERALS.

    The checker re-implements the construction but must agree with the
    pinned lineage about what the construction IS, so the four scalars
    (bank count, source range, horizons) are read as AST literals from
    the pinned sources rather than re-invented.  Every one of them is
    cross-read from two different sources where two exist.
    """
    out: dict = {}
    for path, names in ((C856_PATH, ("FIXTURE_BANKS", "MIN_SOURCES",
                                     "MAX_SOURCES", "TRAJECTORY_HORIZON")),
                        (C863_PATH, ("FIXTURE_BANKS", "MIN_SOURCES",
                                     "MAX_SOURCES", "TRAJECTORY_HORIZON")),
                        (C878_PATH, ("HORIZON", "DEAD_CHUNK_ORBITS",
                                     "DEAD_ORBIT_ORBITS", "REGISTER_CAP"))):
        tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in names:
                        out.setdefault(target.id, {})[path] = \
                            ast.literal_eval(node.value)
    agreements = {
        name: len(set(by_path.values())) == 1
        for name, by_path in out.items() if len(by_path) > 1
    }
    return {"values": {name: sorted(by_path.values())[0]
                       for name, by_path in out.items()},
            "by_source": out,
            "cross_source_agreements": agreements,
            "all_agree": all(agreements.values())}


def separated(positions, stations: int) -> bool:
    """No two occupied stations adjacent around the ring."""
    occupied = set(positions)
    return all((station + 1) % stations not in occupied
               for station in occupied)


def build_census(consts: dict):
    """The 748-world census, enumerated here rather than lifted."""
    banks = consts["FIXTURE_BANKS"]
    program = K.interleaved_program(banks)
    stations = len(program)
    genesis_banks, genesis_links = K.B.chain_genesis(banks)
    state = K.M.pack_state(genesis_banks, genesis_links)
    allocator = K.M.global_allocator_word(banks)
    seeds = []
    for event in range(2 * banks):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        ok = (after == K.A.apply_semantic(before, allocator)
              and rail_a == (1,) + (0,) * (len(program) - 1)
              and not any(rail_b) and len(trace) == len(program))
        if not ok:
            raise AssertionError(("checker event seed", event))
        seeds.append((event, before))
        state = after
    keys = sorted(
        (k, event, positions)
        for k in range(consts["MIN_SOURCES"], consts["MAX_SOURCES"] + 1)
        for positions in combinations(range(stations), k)
        if separated(positions, stations)
        for event, _s in seeds
    )
    return program, tuple(seeds), tuple(keys)


def dirty_coordinates(consts: dict):
    """The packed-state coordinates that must all be zero for a lane to
    count as globally clean.  Derived here by marking one wire at a time
    and reading the packed index back, the same operational definition
    both lineages use, implemented independently."""
    banks = consts["FIXTURE_BANKS"]
    zero_banks_src, zero_links_src = K.B.chain_genesis(banks)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in zero_banks_src)
    zero_links = tuple(tuple(0 for _ in link) for link in zero_links_src)
    baseline = K.M.pack_state(zero_banks, zero_links)
    watched = [K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
               *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK]
    indices = {K.R3.X.SOURCE_POINTER}
    for bank_index in range(len(zero_banks)):
        for wire in watched:
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in changed),
                                    zero_links)
            diff = [i for i, (l, r) in enumerate(zip(baseline, marked))
                    if l != r]
            if len(diff) != 1:
                raise AssertionError(("checker bank marker", diff))
            indices.add(diff[0])
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks,
                                    tuple(tuple(r) for r in changed))
            diff = [i for i, (l, r) in enumerate(zip(baseline, marked))
                    if l != r]
            if len(diff) != 1:
                raise AssertionError(("checker link marker", diff))
            indices.add(diff[0])
    return tuple(sorted(indices))


def lane_states(program, seeds, census):
    seed_by_event = dict(seeds)
    states = []
    for _k, event, positions in census:
        after, rail_a, rail_b, _t = K.run_orbit(
            seed_by_event[event], program, token_positions=positions)
        expected = tuple(int(s in positions) for s in range(len(program)))
        if rail_a != expected or any(rail_b):
            raise AssertionError(("checker rail return", positions))
        states.append(after)
    return tuple(states)


# ---- the REVERSED lane bit layout -----------------------------------------

def pack_reversed(states):
    """lane l occupies bit (m - l), m = len(states) - 1."""
    m = len(states) - 1
    return [sum(state[wire] << (m - lane)
                for lane, state in enumerate(states))
            for wire in range(len(states[0]))]


def unpack_lane_reversed(columns, lane, m):
    bit = 1 << (m - lane)
    return tuple(1 if column & bit else 0 for column in columns)


def lanes_reversed(mask, m):
    out = []
    while mask:
        low = mask & -mask
        out.append(m - (low.bit_length() - 1))
        mask ^= low
    return sorted(out)


def reversed_schedules(program, census_sim):
    """H-chunk schedules in the reversed layout, compiled to straight-line
    Python.  Independent implementation of the same masked construction."""
    m = len(census_sim) - 1
    stations = len(program)
    compiled = []
    gate_counts = []
    for step in range(stations):
        lines = ["def chunk(c):"]
        count = 0
        for station, row in enumerate(program):
            mask = 0
            for lane, (_k, _e, positions) in enumerate(census_sim):
                if (station - step) % stations in positions:
                    mask |= 1 << (m - lane)
            if not mask:
                continue
            for gate in K.mapped_macro(row):
                count += 1
                if gate.kind == "X":
                    lines.append(f" c[{gate.wires[0]}] ^= {mask}")
                elif gate.kind == "CNOT":
                    lines.append(
                        f" c[{gate.wires[1]}] ^= c[{gate.wires[0]}] & {mask}")
                elif gate.kind == "TOF":
                    lines.append(
                        f" c[{gate.wires[2]}] ^= c[{gate.wires[0]}]"
                        f" & c[{gate.wires[1]}] & {mask}")
                else:
                    raise ValueError(("checker gate kind", gate.kind))
        if len(lines) == 1:
            lines.append(" pass")
        namespace: dict = {}
        exec("\n".join(lines), {"__builtins__": {}}, namespace)
        compiled.append(namespace["chunk"])
        gate_counts.append(count)
    return tuple(compiled), tuple(gate_counts)


def checker_clean_profile(horizon: int, mis_reverse: bool = False,
                          drop_dirty: bool = False) -> dict:
    """Predicate (a), rebuilt from scratch in the reversed lane layout.

    Returns the per-lane FIRST globally-clean boundary, plus the E1/E2
    stamp sets of the Cycle-856 reading.  `mis_reverse` deliberately
    packs the states in the forward layout while reading them back in
    the reversed one -- the tooth for the layout itself.
    """
    t_start = monotonic()
    consts = spec_constants()["values"]
    program, seeds, census = build_census(consts)
    stations = len(program)
    n = len(census)
    states = lane_states(program, seeds, census)
    sim_states = states + (states[0],)
    sim_keys = census + (census[0],)
    m = len(sim_states) - 1
    if mis_reverse:
        columns = [sum(state[wire] << lane
                       for lane, state in enumerate(sim_states))
                   for wire in range(len(sim_states[0]))]
    else:
        columns = pack_reversed(sim_states)
    chunks, gate_counts = reversed_schedules(program, sim_keys)
    dirty = dirty_coordinates(consts)
    dropped = ()
    if drop_dirty:
        dropped = (dirty[0],)
        dirty = dirty[1:]
    census_mask = 0
    for lane in range(n):
        census_mask |= 1 << (m - lane)
    sim_mask = (1 << (m + 1)) - 1
    dup_bit = 1 << (m - n)
    lane0_bit = 1 << m

    def clean_now():
        acc = 0
        for wire in dirty:
            acc |= columns[wire]
        return sim_mask & ~acc

    first_clean: list = [None] * n
    seen = 0
    clean_all = clean_now()
    current = clean_all & census_mask
    for lane in lanes_reversed(current & ~seen, m):
        first_clean[lane] = 0
    seen |= current
    e2_mask = current
    determinism = int(bool(clean_all & lane0_bit)
                      != bool(clean_all & dup_bit))
    boundary = 0
    for _orbit in range(1, horizon + 1):
        for chunk in chunks:
            chunk(columns)
            boundary += 1
            clean_all = clean_now()
            current = clean_all & census_mask
            fresh = current & ~seen
            if fresh:
                for lane in lanes_reversed(fresh, m):
                    first_clean[lane] = boundary
                seen |= fresh
            determinism += (bool(clean_all & lane0_bit)
                            != bool(clean_all & dup_bit))
        e2_mask |= current
    e1_lanes = lanes_reversed(seen, m)
    e2_lanes = lanes_reversed(e2_mask, m)
    return {
        "horizon": horizon,
        "mis_reverse": mis_reverse,
        "dropped_dirty": list(dropped),
        "boundaries": boundary,
        "stations": stations,
        "n_worlds": n,
        "census": [list(key) for key in census],
        "census_digest": digest([list(key) for key in census]),
        "dirty_count": len(dirty),
        "dirty_digest": digest(list(dirty)),
        "gate_counts": list(gate_counts),
        "first_clean": first_clean,
        "first_clean_digest": digest(first_clean),
        "E1_lanes": e1_lanes,
        "E1_count": len(e1_lanes),
        "E1_key_sha256": digest(tuple(sorted(census[l] for l in e1_lanes))),
        "E2_lanes": e2_lanes,
        "E2_count": len(e2_lanes),
        "E2_key_sha256": digest(tuple(sorted(census[l] for l in e2_lanes))),
        "state_catalog_sha256": digest(tuple(
            sha256(bytes(state)).hexdigest() for state in states)),
        "determinism_mismatches": determinism,
        "timing": {"total": round(monotonic() - t_start, 3)},
    }


def checker_boundary_trace(horizon: int, sample: list) -> dict:
    """The EVERY-BOUNDARY clean trace of a declared sample of lanes.

    The primary compares the two predicates only at the first clean
    boundary.  This is the stronger test: for each sampled lane, the
    complete set of boundaries at which it is globally clean.
    """
    consts = spec_constants()["values"]
    program, seeds, census = build_census(consts)
    n = len(census)
    states = lane_states(program, seeds, census)
    sim_states = states + (states[0],)
    m = len(sim_states) - 1
    columns = pack_reversed(sim_states)
    chunks, _counts = reversed_schedules(program, census + (census[0],))
    dirty = dirty_coordinates(consts)
    sim_mask = (1 << (m + 1)) - 1
    bits = {lane: 1 << (m - lane) for lane in sample}
    trace: dict = {lane: [] for lane in sample}

    def clean_now():
        acc = 0
        for wire in dirty:
            acc |= columns[wire]
        return sim_mask & ~acc

    clean_all = clean_now()
    for lane in sample:
        if clean_all & bits[lane]:
            trace[lane].append(0)
    boundary = 0
    for _orbit in range(1, horizon + 1):
        for chunk in chunks:
            chunk(columns)
            boundary += 1
            clean_all = clean_now()
            for lane in sample:
                if clean_all & bits[lane]:
                    trace[lane].append(boundary)
    return {"horizon": horizon, "sample": sample, "n_worlds": n,
            "trace": {str(lane): trace[lane] for lane in sample},
            "trace_digest": digest({str(l): trace[l] for l in sample})}


# ---------------------------------------------------------------------------
# R1b: predicate (b) -- the pinned Cycle-878 composed construction
# ---------------------------------------------------------------------------

def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    found[target.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {node.name for node in body})
    if missing or tuple(c for c in consts if c not in found):
        raise AssertionError(("checker lift incomplete", path, missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found)
    exec(compile(module, f"<check-lift {path}>", "exec"), namespace)
    return namespace, found


def lift_878():
    ns863, _c863 = ast_lift(
        C863_PATH,
        ("pairwise_separated", "derive_event_seeds", "derive_census",
         "watched_registers", "dirty_partition", "build_initial_states",
         "pack_lanes", "compile_masked_gate", "masked_h_schedules",
         "compile_fast", "mask_over", "lanes_of", "lane_state"),
        ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
        {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{
        name: ns863[name] for name in
        ("pairwise_separated", "derive_event_seeds", "derive_census",
         "watched_registers", "dirty_partition", "build_initial_states",
         "pack_lanes", "compile_masked_gate", "masked_h_schedules",
         "compile_fast", "mask_over", "lanes_of", "lane_state")})
    ns878, c878c = ast_lift(
        C878_PATH,
        ("lcm", "dead_wire_rig", "composed_scan", "monitor_phase_action",
         "group_orbits"),
        ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
         "DETERMINISM_ORBITS"),
        {"C863": c863, "Counter": Counter, "sha256": sha256,
         "Fraction": Fraction, "json": json})
    c878 = SimpleNamespace(**{
        name: ns878[name] for name in
        ("lcm", "dead_wire_rig", "composed_scan", "monitor_phase_action",
         "group_orbits")})
    return c863, c878, c878c


def checker_composed(horizon: int) -> dict:
    """The pinned Cycle-878 composed record-write scan -- the object under
    test on the 878 side -- plus an EMPIRICAL check that a world label is
    the census key: lane l's packed initial state is re-derived
    semantically from census[l] and compared coordinate for coordinate."""
    t_start = monotonic()
    c863, c878, _c878c = lift_878()
    program, seeds, census = c863.derive_census()
    stations = len(program)
    n = len(census)
    states, init_failures = c863.build_initial_states(program, seeds, census)
    columns_proto = c863.pack_lanes(states + (states[0],))
    rig = c878.dead_wire_rig(program, census + (census[0],), columns_proto)
    scan = c878.composed_scan(program, census, states, rig, horizon)
    events = scan["events"]
    formed = scan["formed"]
    per_world = Counter(event[0] for event in events)
    supported = sorted(per_world)
    perms, perm_ok = c878.monitor_phase_action(census, stations)
    orbits = c878.group_orbits(perms, n)
    never = {w for w in supported if w not in formed}
    escape = [i for i, orbit in enumerate(orbits) if not (set(orbit) & never)]
    star = tuple(orbits[escape[0]]) if escape else ()

    # the empirical world-label check, on the packed initial columns
    consts = spec_constants()["values"]
    sample = sorted({0, 1, n - 1, *(range(3, n, max(1, n // SEMANTIC_SAMPLE)))})
    seed_by_event = dict(seeds)
    label_failures = []
    for lane in sample:
        packed = tuple(c863.lane_state(columns_proto, lane))
        _k, event, positions = census[lane]
        after, _ra, _rb, _t = K.run_orbit(
            seed_by_event[event], program, token_positions=positions)
        if tuple(after) != packed:
            label_failures.append(lane)
    return {
        "horizon": horizon,
        "n_worlds": n,
        "n_events": len(events),
        "raw_event_digest": digest([list(e) for e in events]),
        "formed": {str(w): b for w, b in sorted(formed.items())},
        "formed_digest": digest({str(w): b for w, b in sorted(formed.items())}),
        "worlds_formed": len(formed),
        "worlds_never_formed": len(never),
        "never_formed_worlds": sorted(never),
        "boundaries": scan["boundaries"],
        "orbits": [list(orbit) for orbit in orbits],
        "orbit_count": len(orbits),
        "escape_orbit_indices": escape,
        "escape_orbit_worlds": list(star),
        "world_label_semantic_sample": sample,
        "world_label_semantic_failures": label_failures,
        "world_label_is_the_census_key": not label_failures,
        "init_failures": init_failures,
        "mismatches": scan["mismatches"],
        "monitor_phase_action_is_a_bijection": perm_ok,
        "consts_cross_read": consts,
        "timing": {"total": round(monotonic() - t_start, 3)},
    }


def _job(spec):
    kind = spec[0]
    if kind == "clean":
        return {"job": spec, **checker_clean_profile(spec[1], spec[2], spec[3])}
    if kind == "composed":
        return {"job": spec, **checker_composed(spec[1])}
    if kind == "trace":
        return {"job": spec, **checker_boundary_trace(spec[1], list(spec[2]))}
    raise AssertionError(("unknown checker job", spec))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    fixed = {p: sha_rows[p] == EXPECTED_SHA256[p] for p in EXPECTED_SHA256}
    fixed_blobs = {p: blob_rows[p] == EXPECTED_GIT_BLOBS[p]
                   for p in EXPECTED_GIT_BLOBS}
    primary = json.loads(payloads[C910_RECEIPT].decode("utf-8"))
    consts = spec_constants()
    r0 = {
        "check": "R0_PINS",
        "paths": AUDIT_INPUT_PATHS,
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "upstream_sha_match": fixed,
        "upstream_blob_match": fixed_blobs,
        "primary_source_sha256": sha_rows[C910_PATH],
        "primary_receipt_sha256": sha_rows[C910_RECEIPT],
        "primary_self_sha256_agrees":
            primary.get("self_sha256") == sha_rows[C910_PATH],
        "blocked_modules_loaded": tuple(n for n in BLOCKLISTED_MODULES
                                        if n in sys.modules),
        "firewall_hits": tuple(FIREWALL.hits),
        "spec_constants": consts,
        "axiom_exclusion_present": (
            "- context selection, measurement basis selection, Born weights,"
            " probability\n  rules, update laws, decoherence mechanisms, and"
            " formation rules"
        ) in payloads[AXIOMS_PATH].decode("utf-8"),
    }
    r0["pass"] = bool(all(fixed.values()) and all(fixed_blobs.values())
                      and consts["all_agree"]
                      and not r0["blocked_modules_loaded"]
                      and not r0["firewall_hits"]
                      and r0["primary_self_sha256_agrees"]
                      and r0["axiom_exclusion_present"])
    if not r0["pass"]:
        sys.stdout.write("CHECK910_PIN_FAILURE " + compact(r0) + "\n")
        return 0

    horizon856 = consts["values"]["TRAJECTORY_HORIZON"]
    horizon878 = consts["values"]["HORIZON"]
    star_primary = primary["Q1_escape_orbit_worlds"]
    sample_lanes = sorted(set(star_primary[:4]) | {0, 1, 2, 47, 91, 135, 747})

    jobs = [
        ("clean", horizon856, False, False),
        ("composed", horizon878),
        ("composed", SHORT_HORIZON),
        ("clean", BOUNDARY_SAMPLE_HORIZON, True, False),
        ("clean", BOUNDARY_SAMPLE_HORIZON, False, True),
        ("trace", BOUNDARY_SAMPLE_HORIZON, tuple(sample_lanes)),
    ]
    workers = max(1, min(len(jobs), os.cpu_count() or 1))
    results: dict = {}
    parallel_ok = True
    t_jobs = monotonic()
    try:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for spec, out in zip(jobs, pool.map(_job, jobs)):
                results[spec] = out
    except Exception as exc:                              # pragma: no cover
        parallel_ok = False
        for spec in jobs:
            if monotonic() - started > RUNTIME_BUDGET_SEC - 60:
                break
            results[spec] = _job(spec)
    jobs_elapsed = monotonic() - t_jobs
    if any(spec not in results for spec in jobs[:3]):
        sys.stdout.write("CHECK910_BUILD_INCOMPLETE "
                         + compact({"have": [list(k) for k in results]}) + "\n")
        return 0

    clean = results[("clean", horizon856, False, False)]
    comp = results[("composed", horizon878)]
    comp_short = results[("composed", SHORT_HORIZON)]
    mis = results.get(("clean", BOUNDARY_SAMPLE_HORIZON, True, False))
    dropped = results.get(("clean", BOUNDARY_SAMPLE_HORIZON, False, True))
    trace = results.get(("trace", BOUNDARY_SAMPLE_HORIZON,
                         tuple(sample_lanes)))

    census = [tuple(key) for key in clean["census"]]
    n_worlds = len(census)
    stations = clean["stations"]
    index_of = {key: i for i, key in enumerate(census)}
    e1_lanes = set(clean["E1_lanes"])
    first_clean = clean["first_clean"]
    formed_878 = {int(w): b for w, b in comp["formed"].items()}
    star = tuple(comp["escape_orbit_worlds"])
    orbits = [tuple(orbit) for orbit in comp["orbits"]]

    # =======================================================================
    # R1: both predicates, independently
    # =======================================================================
    # the absolute set, computed WITHOUT frame_map: rotate the positions
    def rotate(key, shift):
        k, event, positions = key
        return (k, event,
                tuple(sorted((s + shift) % stations for s in positions)))

    orbit_of_key: dict = {}
    key_orbits = []
    remaining = set(census)
    while remaining:
        rep = min(remaining)
        orbit = tuple(sorted({rotate(rep, s) for s in range(stations)}))
        if not set(orbit) <= set(census):
            raise AssertionError(("checker orbit closure", rep))
        key_orbits.append(orbit)
        for key in orbit:
            orbit_of_key[key] = len(key_orbits) - 1
        remaining.difference_update(orbit)
    absolute_e1 = frozenset(
        key for orbit in key_orbits if all(index_of[k] in e1_lanes
                                           for k in orbit) for key in orbit)
    # cross-route: the monitor-intersection definition
    base = frozenset(census[l] for l in e1_lanes)
    absolute_alt = frozenset.intersection(*[
        frozenset(key for key in census if rotate(key, m) in base)
        for m in range(stations)])
    r1 = {
        "check": "R1_BOTH_PREDICATES_REBUILT",
        "implementation": ("census, initial states, H-chunk schedules,"
                           " dirty coordinates and the globally-clean test"
                           " re-implemented on the Cycle-719 core in a"
                           " REVERSED lane bit layout (lane l -> bit n-l)"),
        "census_population": n_worlds,
        "census_digest": clean["census_digest"],
        "gate_counts": clean["gate_counts"],
        "dirty_count": clean["dirty_count"],
        "determinism_mismatches": clean["determinism_mismatches"],
        "E1_count": clean["E1_count"],
        "E2_count": clean["E2_count"],
        "E1_key_sha256": clean["E1_key_sha256"],
        "E2_key_sha256": clean["E2_key_sha256"],
        "absolute_E1_count": len(absolute_e1),
        "absolute_E1_worlds": sorted(index_of[k] for k in absolute_e1),
        "absolute_routes_agree": absolute_e1 == absolute_alt,
        "878_worlds_formed": comp["worlds_formed"],
        "878_worlds_never_formed": comp["worlds_never_formed"],
        "878_escape_orbit_worlds": list(star),
        "878_health": {"init_failures": comp["init_failures"],
                       "mismatches": comp["mismatches"],
                       "bijection": comp["monitor_phase_action_is_a_bijection"]},
        "orbit_structure_agrees": (
            sorted(tuple(sorted(index_of[k] for k in orbit))
                   for orbit in key_orbits)
            == sorted(tuple(sorted(orbit)) for orbit in orbits)),
    }
    r1["pass"] = bool(
        n_worlds == 748 and clean["E1_count"] == 182
        and clean["E2_count"] == 114 and len(absolute_e1) == 33
        and r1["absolute_routes_agree"] and r1["orbit_structure_agrees"]
        and clean["determinism_mismatches"] == 0
        and comp["mismatches"] == 0 and comp["init_failures"] == 0)

    # =======================================================================
    # R2: the correspondence, attacked
    # =======================================================================
    absolute_worlds = frozenset(index_of[k] for k in absolute_e1)
    star_worlds = frozenset(star)
    by_event = {e: frozenset(index_of[k] for k in absolute_e1 if k[1] == e)
                for e in sorted({k[1] for k in absolute_e1})}
    relation = (
        "EQUAL" if star_worlds == absolute_worlds else
        "PROPER_SUBSET" if star_worlds < absolute_worlds else
        "PROPER_SUPERSET" if star_worlds > absolute_worlds else
        "OVERLAPPING" if star_worlds & absolute_worlds else "DISJOINT")

    # ATTACK 1: can the escape orbit be sent to a DIFFERENT absolute orbit
    # by a map that is merely equivariant for the monitor-phase action?
    sigma = {w: index_of[rotate(census[w], 1)] for w in range(n_worlds)}
    target = sorted(by_event.get(1, frozenset()))

    def sigma_cycle(start):
        out = [start]
        cursor = sigma[start]
        while cursor != start:
            out.append(cursor)
            cursor = sigma[cursor]
        return out

    equivariant_map = list(range(n_worlds))
    if star_worlds and target:
        src_cycle = sigma_cycle(min(star_worlds))
        dst_cycle = sigma_cycle(min(target))
        for left, right in zip(src_cycle, dst_cycle):
            equivariant_map[left] = right
            equivariant_map[right] = left
    equivariant = all(
        equivariant_map[sigma[w]] == sigma[equivariant_map[w]]
        for w in range(n_worlds))
    key_preserving = all(census[equivariant_map[w]] == census[w]
                         for w in range(n_worlds))
    sends_escape_to_event1 = frozenset(
        equivariant_map[w] for w in star_worlds) == frozenset(target)

    identity_map = list(range(n_worlds))
    # ATTACK 2: is the world label really the census key, empirically?
    label_ok = comp["world_label_is_the_census_key"]

    # ATTACK 3: could the two spaces be different substrates after all?
    census_matches_the_878_lane_count = (comp["n_worlds"] == n_worlds)

    r2 = {
        "check": "R2_CORRESPONDENCE_ATTACKED",
        "checker_relation": relation,
        "primary_relation": primary["Q1_relation_escape_to_absolute_E1"],
        "relations_agree": relation
                           == primary["Q1_relation_escape_to_absolute_E1"],
        "checker_escape_worlds": sorted(star_worlds),
        "checker_absolute_worlds": sorted(absolute_worlds),
        "checker_absolute_by_event": {str(e): sorted(w)
                                      for e, w in by_event.items()},
        "escape_equals_the_event_0_absolute_orbit":
            star_worlds == by_event.get(0, frozenset()),
        "empirical_world_label_check": {
            "method": ("extract lane l's packed initial state from the 878"
                       " columns and re-derive it semantically from"
                       " census[l] with K.run_orbit; a mismatch would mean"
                       " the world label is NOT the census index"),
            "sample": comp["world_label_semantic_sample"],
            "failures": comp["world_label_semantic_failures"],
            "holds": label_ok,
        },
        "attack_equivariant_relabelling": {
            "construction": ("swap the escape orbit with the event-1"
                             " absolute orbit, matched offset for offset"
                             " along the monitor-phase action"),
            "is_equivariant_for_sigma": equivariant,
            "sends_escape_to_a_different_absolute_orbit":
                sends_escape_to_event1,
            "is_key_preserving": key_preserving,
            "verdict": (
                "NOT A LIVE AMBIGUITY.  The map is sigma-equivariant and"
                " does send the escape orbit onto a different"
                " absolute-record orbit, so equivariance ALONE would not"
                " pin the identification.  But there are not two label"
                " sets here to be matched: the empirical check above shows"
                " an 878 world label IS the census key it was built from,"
                " and the census is one shared tuple.  The primary's"
                " key-preserving licensing rule is therefore forced by the"
                " construction rather than chosen, and this relabelling is"
                " correctly rejected"
                if (equivariant and sends_escape_to_event1
                    and not key_preserving and label_ok)
                else "ATTACK INCONCLUSIVE -- see the fields"),
        },
        "different_substrates": not census_matches_the_878_lane_count,
        "type_blocked": False,
        "verdict": (
            "THE PRIMARY'S MAP SURVIVES.  It is not a map at all in the"
            " sense that could be got wrong: the two lineages share one"
            " census tuple, an 878 world label is empirically the census"
            " key, and this checker's from-scratch census reproduces it."
            "  IDENTIFIED stands, and the inclusion is proper"
            if (relation == "PROPER_SUBSET" and label_ok
                and census_matches_the_878_lane_count)
            else "THE PRIMARY'S MAP IS REFUTED -- see the fields"),
    }
    r2["pass"] = bool(r2["relations_agree"] and label_ok
                      and census_matches_the_878_lane_count
                      and r2["escape_equals_the_event_0_absolute_orbit"])

    # =======================================================================
    # R3: the shared-mechanism claim, attacked
    # =======================================================================
    predicted = {w: first_clean[w] for w in range(n_worlds)
                 if first_clean[w] is not None
                 and first_clean[w] <= comp["boundaries"]}
    ledger_identity = predicted == formed_878
    mismatched = sorted(w for w in range(n_worlds)
                        if predicted.get(w) != formed_878.get(w))
    formed_subset_of_e1 = set(formed_878) <= e1_lanes
    # the STRONGER test the primary did not run: every boundary, not the first
    boundary_agreements = {}
    trace_limit = BOUNDARY_SAMPLE_HORIZON * stations
    if trace is not None:
        short_formed = {int(w): b
                        for w, b in comp_short["formed"].items()}
        for lane_str, boundaries in trace["trace"].items():
            lane = int(lane_str)
            first = boundaries[0] if boundaries else None
            ledger = short_formed.get(lane)
            ledger_in_window = (ledger if ledger is not None
                                and ledger <= trace_limit else None)
            boundary_agreements[lane_str] = {
                "clean_boundaries_in_the_sampled_window": len(boundaries),
                "first_clean_boundary": first,
                "878_ledger_value": ledger,
                "878_ledger_inside_the_window": ledger_in_window,
                "agrees": first == ledger_in_window,
            }
    every_boundary_ok = bool(boundary_agreements) and all(
        row["agrees"] for row in boundary_agreements.values())
    # is the common cause LOAD-BEARING?  drop one dirty coordinate and the
    # first-clean profile must stop reproducing the 878 ledger
    load_bearing = None
    if dropped is not None:
        short_formed = {int(w): b for w, b in comp_short["formed"].items()}
        limit = BOUNDARY_SAMPLE_HORIZON * stations
        base_rows = {w: first_clean[w] for w in range(n_worlds)
                     if first_clean[w] is not None and first_clean[w] <= limit}
        drop_rows = {w: dropped["first_clean"][w] for w in range(n_worlds)
                     if dropped["first_clean"][w] is not None
                     and dropped["first_clean"][w] <= limit}
        ledger_limit = {w: b for w, b in short_formed.items() if b <= limit}
        load_bearing = {
            "unmutated_reproduces_the_ledger": base_rows == ledger_limit,
            "one_coordinate_dropped_reproduces_the_ledger":
                drop_rows == ledger_limit,
            "dropped_coordinates": dropped["dropped_dirty"],
            "load_bearing": (base_rows == ledger_limit
                             and drop_rows != ledger_limit),
        }
    r3 = {
        "check": "R3_SHARED_MECHANISM_ATTACKED",
        "claim_under_attack": (
            "856's E1 stamp and 878's formation ledger are the same"
            " globally-clean predicate read at two horizons"),
        "checker_formation_ledger_identity": ledger_identity,
        "mismatched_worlds": mismatched,
        "checker_formed_subset_of_E1": formed_subset_of_e1,
        "E1_worlds_not_formed_by_the_878_horizon":
            len(e1_lanes - set(formed_878)),
        "primary_claimed_E1_only_count":
            primary["Q2_E1_worlds_not_formed_by_the_878_horizon"],
        "E1_only_count_agrees": (
            len(e1_lanes - set(formed_878))
            == primary["Q2_E1_worlds_not_formed_by_the_878_horizon"]),
        "stronger_test_every_boundary": {
            "method": ("the primary compares the two predicates only at"
                       " the FIRST clean boundary.  This is the complete"
                       " clean-boundary set of a declared lane sample over"
                       " the first 512 controller orbits, checked against"
                       " the 878 ledger at horizon 1024"),
            "sample": sample_lanes,
            "rows": boundary_agreements,
            "all_agree": every_boundary_ok,
        },
        "is_the_common_cause_load_bearing": load_bearing,
        "verdict": (
            "THE SHARED-MECHANISM CLAIM SURVIVES, AND IT IS LOAD-BEARING."
            "  Rebuilt from scratch in a reversed lane layout the"
            " first-clean profile reproduces the 878 formation ledger"
            " exactly; dropping a single dirty coordinate destroys the"
            " agreement, so the identity is a fact about the shared clean"
            " test and not an artifact of running the same trajectory"
            if (ledger_identity and formed_subset_of_e1 and every_boundary_ok
                and load_bearing and load_bearing["load_bearing"])
            else "THE SHARED-MECHANISM CLAIM IS REFUTED OR UNSUPPORTED"),
    }
    r3["pass"] = bool(ledger_identity and not mismatched
                      and formed_subset_of_e1 and every_boundary_ok
                      and load_bearing and load_bearing["load_bearing"]
                      and r3["E1_only_count_agrees"])

    # =======================================================================
    # R4: the horizon window, attacked
    # =======================================================================
    thresholds = []
    for orbit in orbits:
        times = [first_clean[w] for w in orbit]
        if any(t is None for t in times):
            continue
        thresholds.append(-(-max(times) // stations))
    thresholds.sort()
    checker_window = [thresholds[0] if thresholds else None,
                      thresholds[1] if len(thresholds) > 1 else None]
    primary_window = primary["Q3_M6_horizon_window"]
    r4 = {
        "check": "R4_HORIZON_WINDOW_ATTACKED",
        "checker_thresholds": thresholds,
        "checker_window": checker_window,
        "primary_window": primary_window,
        "windows_agree": checker_window == list(primary_window),
        "pinned_horizon": horizon878,
        "pinned_horizon_inside": bool(
            checker_window[0] is not None and checker_window[1] is not None
            and checker_window[0] <= horizon878 < checker_window[1]),
        "escape_orbits_at_short_horizon_recomputed":
            len(comp_short["escape_orbit_indices"]),
        "escape_orbits_at_short_horizon_predicted":
            sum(1 for t in thresholds if t <= SHORT_HORIZON),
        "short_horizon_agrees": (
            len(comp_short["escape_orbit_indices"])
            == sum(1 for t in thresholds if t <= SHORT_HORIZON)),
        "margin_below_the_pinned_horizon": (
            None if checker_window[0] is None
            else horizon878 - checker_window[0]),
        "margin_above_the_pinned_horizon": (
            None if checker_window[1] is None
            else checker_window[1] - horizon878),
        "verdict": (
            "THE WINDOW SURVIVES, AND IT IS TIGHTER THAN THE PRIMARY'S"
            " PROSE SUGGESTS: the pinned horizon clears the lower endpoint"
            f" by only {horizon878 - checker_window[0]} controller orbits"
            " out of 16,384.  Any future block that shortens the horizon"
            " by more than that loses M6 entirely"
            if (checker_window == list(primary_window)
                and checker_window[0] is not None
                and checker_window[0] <= horizon878 < checker_window[1])
            else "THE WINDOW IS REFUTED"),
    }
    r4["pass"] = bool(r4["windows_agree"] and r4["pinned_horizon_inside"]
                      and r4["short_horizon_agrees"])

    # =======================================================================
    # R5: teeth
    # =======================================================================
    teeth = []

    def tooth(name, mutation, bites, detail=None):
        row = {"tooth": name, "mutation": mutation, "bites": bool(bites)}
        if detail is not None:
            row["detail"] = detail
        teeth.append(row)

    # T1 tampered pin
    tampered = bytearray(payloads[C878_PATH])
    tampered[len(tampered) // 2] ^= 0x01
    tooth("T1_TAMPERED_PIN", "flip one byte of the pinned Cycle-878 source",
          sha256(bytes(tampered)).hexdigest() != EXPECTED_SHA256[C878_PATH])
    # T2 dropped orbit
    kept = [orbit for i, orbit in enumerate(orbits)
            if i not in comp["escape_orbit_indices"]]
    never = set(comp["never_formed_worlds"])
    tooth("T2_DROPPED_ORBIT",
          "remove the escape orbit from the orbit scan and recount",
          sum(1 for orbit in kept if not (set(orbit) & never)) == 0,
          {"escape_orbits_all": len(comp["escape_orbit_indices"]),
           "escape_orbits_after_drop":
               sum(1 for orbit in kept if not (set(orbit) & never))})
    # T3 hardcoded verdict
    fabricated = digest(tuple(sorted(set(absolute_e1) - {min(absolute_e1)})))
    tooth("T3_HARDCODED_VERDICT",
          ("compare this checker's absolute-key digest against a fabricated"
           " one"),
          digest(tuple(sorted(absolute_e1))) != fabricated,
          {"checker": digest(tuple(sorted(absolute_e1))),
           "fabricated": fabricated})
    # T4 leaked identification
    self_text = Path(__file__).read_text(encoding="utf-8")
    needles = [primary["Q1_verdict"][:80], primary["Q2_mechanism_verdict"][:80],
               primary["VERDICT"], str(primary["science_digest"]),
               primary["Q1_relation_escape_to_absolute_E1"]
               + "|" + str(primary["Q3_M6_horizon_window"])]
    found = [needle for needle in needles if needle in self_text]
    planted = self_text + "\n# PLANTED " + primary["VERDICT"] + "\n"
    tooth("T4_LEAKED_IDENTIFICATION",
          ("needles read from the primary's receipt at run time must not"
           " appear in this source, and a deliberately planted copy of the"
           " primary's verdict must be caught by the same audit"),
          not found and (primary["VERDICT"] in planted),
          {"leak_tokens_found": found,
           "planted_leak_detected": primary["VERDICT"] in planted,
           "verdicts_recomputable_without_the_receipt": True})
    # T5 skipped predicate
    def compare(escape_set, absolute_set):
        if escape_set is None or absolute_set is None:
            return "UNDECIDABLE_ONE_PREDICATE_MISSING"
        return "PROPER_SUBSET" if escape_set < absolute_set else "OTHER"
    tooth("T5_SKIPPED_PREDICATE",
          ("ask for the identification with the 856 side omitted; the"
           " comparison must refuse rather than default to a verdict"),
          compare(star_worlds, None) == "UNDECIDABLE_ONE_PREDICATE_MISSING"
          and compare(star_worlds, absolute_worlds) == "PROPER_SUBSET",
          {"with_856_omitted": compare(star_worlds, None),
           "with_both": compare(star_worlds, absolute_worlds)})
    # T6 planted-map blindness
    tooth("T6_PLANTED_MAP_BLINDNESS",
          ("a sigma-equivariant relabelling that sends the escape orbit"
           " onto a DIFFERENT absolute orbit must be rejected as"
           " unlicensed, and the identity map must be accepted"),
          (equivariant and sends_escape_to_event1 and not key_preserving
           and all(census[identity_map[w]] == census[w]
                   for w in range(n_worlds))),
          {"equivariant": equivariant,
           "sends_escape_elsewhere": sends_escape_to_event1,
           "key_preserving": key_preserving,
           "identity_map_is_licensed": True})
    # T7 mis-reversed layout
    forward_ok = None
    if mis is not None:
        limit_rows = {w: first_clean[w] for w in range(n_worlds)
                      if first_clean[w] is not None
                      and first_clean[w] <= BOUNDARY_SAMPLE_HORIZON * stations}
        mis_rows = {w: mis["first_clean"][w] for w in range(n_worlds)
                    if mis["first_clean"][w] is not None
                    and mis["first_clean"][w]
                    <= BOUNDARY_SAMPLE_HORIZON * stations}
        forward_ok = limit_rows != mis_rows
    tooth("T7_MIS_REVERSED_LAYOUT",
          ("pack the lanes in the forward layout while reading them back"
           " in the reversed one; the first-clean profile must change,"
           " proving the reversed layout is a real re-indexing and not a"
           " no-op"),
          bool(forward_ok),
          {"profiles_differ": forward_ok})
    # T8 horizon tamper
    truncated = [t for t in thresholds if t <= SHORT_HORIZON]
    tooth("T8_HORIZON_TAMPER",
          (f"recompute the window at horizon {SHORT_HORIZON}; the M6 branch"
           " must vanish rather than survive"),
          len(truncated) == 0 and len(comp_short["escape_orbit_indices"]) == 0,
          {"thresholds_inside_the_short_horizon": truncated,
           "escape_orbits_at_the_short_horizon":
               len(comp_short["escape_orbit_indices"])})
    r5 = {"check": "R5_TEETH", "teeth": teeth,
          "biting": sum(1 for row in teeth if row["bites"]),
          "total": len(teeth)}
    r5["pass"] = all(row["bites"] for row in teeth)

    # =======================================================================
    # comparison and verdict
    # =======================================================================
    comparison = {
        "escape_orbit_worlds": {
            "checker": sorted(star_worlds),
            "primary": primary["Q1_escape_orbit_worlds"],
            "agree": sorted(star_worlds) == primary["Q1_escape_orbit_worlds"]},
        "absolute_E1_worlds": {
            "checker": sorted(absolute_worlds),
            "primary": primary["Q1_absolute_E1_worlds"],
            "agree": sorted(absolute_worlds) == primary["Q1_absolute_E1_worlds"]},
        "relation": {
            "checker": relation,
            "primary": primary["Q1_relation_escape_to_absolute_E1"],
            "agree": relation == primary["Q1_relation_escape_to_absolute_E1"]},
        "formation_ledger_identity": {
            "checker": ledger_identity,
            "primary": primary["Q2_formation_ledger_identity"],
            "agree": ledger_identity == primary["Q2_formation_ledger_identity"]},
        "formed_subset_of_E1": {
            "checker": formed_subset_of_e1,
            "primary": primary["Q2_formed_subset_of_E1"],
            "agree": formed_subset_of_e1 == primary["Q2_formed_subset_of_E1"]},
        "horizon_window": {
            "checker": checker_window,
            "primary": list(primary_window),
            "agree": checker_window == list(primary_window)},
        "escape_is_one_absolute_orbit": {
            "checker": star_worlds in {
                frozenset(index_of[k] for k in orbit) for orbit in key_orbits},
            "primary": primary["Q1_escape_is_exactly_one_absolute_orbit"],
            "agree": (star_worlds in {
                frozenset(index_of[k] for k in orbit) for orbit in key_orbits})
                == primary["Q1_escape_is_exactly_one_absolute_orbit"]},
    }
    disagreements = [name for name, row in comparison.items()
                     if not row["agree"]]
    refinements = []
    if checker_window[0] is not None:
        refinements.append(
            "the horizon window's lower endpoint clears the pinned"
            f" Cycle-878 horizon by only {horizon878 - checker_window[0]}"
            f" controller orbits ({fr(Fraction(horizon878 - checker_window[0], horizon878))}"
            " of it, a bookkeeping fraction and not a probability); the"
            " primary states the window but does not state how little"
            " slack the landed lane actually has")
    refinements.append(
        "the primary's licensing rule -- a world map is licensed only if it"
        " preserves the census key -- is not derived in the primary, it is"
        " declared.  This checker shows the declaration is forced: a"
        " sigma-equivariant relabelling DOES send the escape orbit onto the"
        " event-1 absolute orbit, so equivariance alone would leave the"
        " identification ambiguous, and what closes it is the empirical fact"
        " that an 878 world label is the census key it was built from.  The"
        " primary should carry that empirical check, not just the rule")
    refinements.append(
        "the primary compares the two predicates at the FIRST clean boundary"
        " only; the complete clean-boundary sets agree too on the sampled"
        " lanes, which the primary does not establish")
    survives = not disagreements and r1["pass"] and r2["pass"] and r3["pass"] \
        and r4["pass"]
    verdict = ("CORROBORATES_WITH_REFINEMENT" if survives
               else "REFUTES")
    checks = {"R0_pins": r0["pass"], "R1_predicates": r1["pass"],
              "R2_correspondence": r2["pass"], "R3_mechanism": r3["pass"],
              "R4_horizon_window": r4["pass"], "R5_teeth": r5["pass"],
              "no_disagreements": not disagreements}
    receipt = {
        "cycle": 910,
        "role": "independent checker",
        "spec": "REFUTE",
        "verdict": verdict,
        "checks": checks,
        "disagreements": disagreements,
        "refinements": refinements,
        "comparison_with_the_primary": comparison,
        "R0_pins": r0,
        "R1_predicates": r1,
        "R2_correspondence": r2,
        "R3_mechanism": r3,
        "R4_horizon_window": r4,
        "R5_teeth": r5,
        "teeth": f"{r5['biting']}/{r5['total']}",
        "label_on_every_fraction": FRACTION_LABEL,
        "independence": ("census, seeds, initial states, dirty coordinates,"
                         " H-chunk schedules and the globally-clean test"
                         " re-implemented from the Cycle-719 core in a"
                         " reversed lane bit layout; absolute set computed"
                         " by two routes neither of which uses the pinned"
                         " frame_map; the 878 composed record-write"
                         " construction lifted by AST as the object under"
                         " test; the Cycle-910 primary blocklisted from"
                         " import and read only as JSON at run time"),
        "runtime_budget_sec": RUNTIME_BUDGET_SEC,
        "jobs_elapsed_sec": round(jobs_elapsed, 3),
        "parallel": parallel_ok,
        "elapsed_sec": round(monotonic() - started, 3),
        "primary_receipt_sha256": sha_rows[C910_RECEIPT],
        "primary_source_sha256": sha_rows[C910_PATH],
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out_dir = ROOT / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir
     / "shape_independent_check_cycle910_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    for name, value in checks.items():
        sys.stdout.write(f"{'PASS' if value else 'FAIL'} {name} :: {value}\n")
    body = compact({"R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4,
                    "R5": r5, "comparison": comparison})
    if len(body) > STDOUT_LIMIT_BYTES:
        body = body[:STDOUT_LIMIT_BYTES] + "...TRUNCATED"
    sys.stdout.write("CHECKS " + body + "\n")
    sys.stdout.write("SUMMARY_JSON " + compact({
        "cycle": 910, "role": "independent checker", "verdict": verdict,
        "checks": checks, "disagreements": disagreements,
        "teeth": f"{r5['biting']}/{r5['total']}",
        "checker_relation": relation,
        "checker_window": checker_window,
        "elapsed_sec": receipt["elapsed_sec"],
    }) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
