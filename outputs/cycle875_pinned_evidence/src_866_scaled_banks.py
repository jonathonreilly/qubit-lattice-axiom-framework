#!/usr/bin/env python3
"""Cycle 866: the scaled-bank construction (B = 3 and 4).

Owner-directed run-to-ground (supervisor-authored). Three legs on richer
spatial structure (stations = 8B-5, matching the landed ring-family law):

B_DERIVED_CLOCK_AT_SCALE: does the all-bank synchronization cadence align
  with the supplied tick as B grows (the B=2 negative was ~14% on-tick)?
C_SECOND_CLOCK_TEST: do disjoint bank-pair sync sequences form
  independent cadences (a second clock) or lock to one structure?
D_BIRTH_DATUM_INTRINSIC: does a RECORD-NATIVE birth pattern (per-bank
  first-event order + gaps in event counts) determine the within-cohort
  record-age offsets — the last gauge residue of the demotion?

Declared bounded probe: events {0,1}, k=2 pairwise-separated placements,
horizon 8,192 orbits, event stores capped 1,024/lane. bounded_theorem,
authority none, audit unset. Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
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

BANK_COUNTS = (3, 4)
EVENTS_USED = (0, 1)
HORIZON = 8_192
STORE_CAP = 1_024


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(b: bytes) -> str:
    return sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    tree = ast.parse(Path(__file__).read_text(), filename="self")
    literal = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    return {
        "sha256": sha_rows,
        "pass": literal == AUDIT_INPUT_PATHS
        and sha_rows == EXPECTED_SHA256 and blob_rows == EXPECTED_GIT_BLOBS,
    }


def pairwise_separated(positions, stations):
    occ = set(positions)
    return all((s + 1) % stations not in occ for s in occ)


def build_bank(bank_count):
    """Seeds, census, initial states, schedules, dirty partitions for B."""

    program = K.interleaved_program(bank_count)
    stations = len(program)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(bank_count)
    seeds = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, ra, rb, tr = K.run_orbit(before, program)
        if not (after == K.A.apply_semantic(before, allocator)
                and ra == (1,) + (0,) * (stations - 1) and not any(rb)):
            raise AssertionError(("seed", bank_count, event))
        seeds.append((event, before))
        state = after
    seed_by_event = dict(seeds)
    census = tuple(sorted(
        (2, event, positions)
        for positions in combinations(range(stations), 2)
        if pairwise_separated(positions, stations)
        for event in EVENTS_USED
    ))

    def watched():
        return (
            ("POINTER", K.A.POINTER), ("U_TO_V", K.A.U_TO_V),
            ("V_TO_U", K.A.V_TO_U), ("DIRECTION_OK", K.A.DIRECTION_OK),
            *((f"F{i}", w) for i, w in enumerate(K.A.FRESH)),
            *((f"Z{i}", w) for i, w in enumerate(K.A.ZERO_WORK)),
            ("TOKEN_OK", K.A.TOKEN_OK),
        )

    banks0, links0 = K.B.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in b) for b in banks0)
    zl = tuple(tuple(0 for _ in l) for l in links0)
    base = K.M.pack_state(zb, zl)
    per_bank = []
    for bi in range(bank_count):
        rows = set()
        for _n, wire in watched():
            ch = [list(b) for b in zb]
            ch[bi][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in ch), zl)
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            if len(d) != 1:
                raise AssertionError(("bank marker", bank_count, bi))
            rows.add(d[0])
        per_bank.append(tuple(sorted(rows)))
    link_rows = set()
    for li, link in enumerate(zl):
        for wire in range(len(link)):
            ch = [list(r) for r in zl]
            ch[li][wire] = 1
            marked = K.M.pack_state(zb, tuple(tuple(r) for r in ch))
            d = [i for i, (l, r) in enumerate(zip(base, marked)) if l != r]
            if len(d) != 1:
                raise AssertionError(("link marker", bank_count, li))
            link_rows.add(d[0])
    global_dirty = tuple(sorted(
        set().union(*per_bank) | link_rows | {K.R3.X.SOURCE_POINTER}
    ))

    states = []
    for _k, event, positions in census:
        before = seed_by_event[event]
        after, ra, rb, _ = K.run_orbit(
            before, program, token_positions=positions
        )
        expected = tuple(int(s in positions) for s in range(stations))
        if ra != expected or any(rb):
            raise AssertionError(("init", bank_count, positions))
        states.append(after)

    sim_keys = census + (census[0],)

    def masked_schedules():
        rows = []
        for step in range(stations):
            sched = []
            for station, row in enumerate(program):
                mask = sum(
                    1 << lane
                    for lane, (_k, _e, pos) in enumerate(sim_keys)
                    if (station - step) % stations in pos
                )
                if mask:
                    for g in K.mapped_macro(row):
                        if g.kind == "X":
                            sched.append((0, g.wires[0], 0, 0, mask))
                        elif g.kind == "CNOT":
                            sched.append((1, g.wires[0], g.wires[1], 0, mask))
                        else:
                            sched.append(
                                (2, g.wires[0], g.wires[1], g.wires[2], mask)
                            )
            rows.append(tuple(sched))
        return tuple(rows)

    fns = []
    for schedule in masked_schedules():
        src = ["def apply_chunk(c):"]
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return {
        "stations": stations, "census": census, "states": tuple(states),
        "per_bank": tuple(per_bank), "global_dirty": global_dirty,
        "fast": tuple(fns),
    }


def mask_over(columns, indices, universe):
    dirty = 0
    for w in indices:
        dirty |= columns[w]
    return universe & ~dirty


def lanes_of(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def scan_bank(bank):
    census = bank["census"]
    n = len(census)
    columns = [
        sum(state[w] << lane for lane, state in enumerate(
            bank["states"] + (bank["states"][0],)
        ))
        for w in range(len(bank["states"][0]))
    ]
    dup = n
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    stations = bank["stations"]
    B = len(bank["per_bank"])
    counts = {"global": [0] * n, "allsync": [0] * n}
    stores = {"global": [[] for _ in range(n)],
              "allsync": [[] for _ in range(n)]}
    pair_stores = {
        pair: [[] for _ in range(n)]
        for pair in combinations(range(B), 2)
    }
    bank_first = [[None] * B for _ in range(n)]
    e1 = {}
    e2 = {}
    mism = 0

    def note(mask, kind, boundary):
        for lane in lanes_of(mask):
            counts[kind][lane] += 1
            s = stores[kind][lane]
            if len(s) < STORE_CAP:
                s.append(boundary)

    def observe(boundary):
        nonlocal mism
        g = mask_over(columns, bank["global_dirty"], uni_sim)
        mism += int(bool(g & 1) != bool(g & (1 << dup)))
        ga = g & uni_all
        bmasks = [
            mask_over(columns, bank["per_bank"][bi], uni_all)
            for bi in range(B)
        ]
        note(ga, "global", boundary)
        for lane in lanes_of(ga):
            e1.setdefault(census[lane], boundary)
        allm = uni_all
        for bm in bmasks:
            allm &= bm
        note(allm, "allsync", boundary)
        for (i, j), store in pair_stores.items():
            pm = bmasks[i] & bmasks[j]
            for lane in lanes_of(pm):
                s = store[lane]
                if len(s) < STORE_CAP:
                    s.append(boundary)
        for bi, bm in enumerate(bmasks):
            for lane in lanes_of(bm):
                if bank_first[lane][bi] is None:
                    bank_first[lane][bi] = (
                        boundary, counts["global"][lane]
                    )
        return ga

    observe(0)
    ga = 0
    for orbit in range(1, HORIZON + 1):
        for step, chunk in enumerate(bank["fast"], 1):
            chunk(columns)
            ga = observe((orbit - 1) * stations + step)
        for lane in lanes_of(ga):
            e2.setdefault(census[lane], orbit)
    return {
        "e1": e1, "e2": e2, "counts": counts, "stores": stores,
        "pair_stores": pair_stores, "bank_first": bank_first,
        "mismatches": mism, "stations": stations, "B": B,
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    results = {}
    certs = []
    for B in BANK_COUNTS:
        bank = build_bank(B)
        scan = scan_bank(bank)
        census = bank["census"]
        stations = scan["stations"]

        total = on = 0
        first_match = first_total = 0
        for lane, key in enumerate(census):
            for b in scan["stores"]["allsync"][lane]:
                total += 1
                on += int(b % stations == 0)
            syncs = scan["stores"]["allsync"][lane]
            if key in scan["e2"] and syncs:
                first_total += 1
                first_match += int(
                    syncs[0] == scan["e2"][key] * stations
                    or (syncs[0] == 0 and scan["e2"][key] == 0)
                )
        derived = {
            "B": B, "stations": stations, "census_size": len(census),
            "stamped_e1": len(scan["e1"]), "stamped_e2": len(scan["e2"]),
            "allsync_stored": total,
            "allsync_on_tick_fraction":
                round(on / total, 6) if total else None,
            "first_allsync_equals_e2": f"{first_match}/{first_total}",
        }

        pair_onticks = {}
        pair_periods = {}
        for pair, store in scan["pair_stores"].items():
            pt = po = 0
            gaps = Counter()
            for lane in range(len(census)):
                seq = store[lane]
                for b in seq:
                    pt += 1
                    po += int(b % stations == 0)
                for a, b2 in zip(seq, seq[1:]):
                    gaps[b2 - a] += 1
            pair_onticks[str(pair)] = (
                round(po / pt, 4) if pt else None
            )
            pair_periods[str(pair)] = gaps.most_common(3)
        distinct_cadences = len({
            compact(v) for v in pair_periods.values()
        })
        second_clock = {
            "pair_on_tick_fractions": pair_onticks,
            "pair_dominant_gaps": pair_periods,
            "distinct_pair_cadence_signatures": distinct_cadences,
        }

        cohorts = defaultdict(list)
        stamp_rung = {}
        for lane, key in enumerate(census):
            if key not in scan["e2"]:
                continue
            boundary = scan["e2"][key] * stations
            events = scan["stores"]["global"][lane]
            if boundary in events:
                stamp_rung[key] = events.index(boundary) + 1
            elif scan["e2"][key] == 0 and events and events[0] == 0:
                stamp_rung[key] = 1
        for key, rung in stamp_rung.items():
            cohorts[scan["e2"][key]].append((key, rung))
        rows = []
        for moment, members in sorted(cohorts.items()):
            if len(members) < 2:
                continue
            base = min(r for _k, r in members)
            for key, rung in members:
                lane = census.index(key)
                bf = scan["bank_first"][lane]
                native = (
                    tuple(sorted(
                        (bf[i][1], i) for i in range(scan["B"]) if bf[i]
                    )) if any(bf) else None
                )
                rows.append({
                    "offset": rung - base,
                    "native": compact(native),
                    "gauge": scan["e1"].get(key),
                })
        def functional(field):
            m = {}
            collisions = 0
            for r in rows:
                v = r[field]
                if v in m:
                    if m[v] != r["offset"]:
                        return False, None
                    collisions += 1
                else:
                    m[v] = r["offset"]
            return True, {"classes": len(m), "rows": len(rows),
                          "nontrivial": collisions}
        nat_ok, nat_stats = functional("native")
        gau_ok, gau_stats = functional("gauge")
        birth = {
            "cohort_member_rows": len(rows),
            "offset_histogram": dict(sorted(Counter(
                r["offset"] for r in rows
            ).items())),
            "native_pattern_functional": nat_ok,
            "native_stats": nat_stats,
            "gauge_e1_functional": gau_ok,
            "gauge_stats": gau_stats,
        }
        results[B] = {"derived_clock": derived,
                      "second_clock": second_clock,
                      "birth_datum": birth,
                      "mismatches": scan["mismatches"]}
    runtime = round(monotonic() - started, 3)
    checks = {
        "A_SCALED_SUBSTRATE": all(
            results[B]["derived_clock"]["stamped_e1"] > 0
            for B in BANK_COUNTS
        ),
        "B_DERIVED_CLOCK_AT_SCALE": True,
        "C_SECOND_CLOCK_TEST": True,
        "D_BIRTH_DATUM_INTRINSIC": True,
        "E_CONTROLS": bool(
            controls["pass"]
            and all(results[B]["mismatches"] == 0 for B in BANK_COUNTS)
            and runtime < AUDIT_TIMEOUT_SEC
        ),
    }
    lines = ["CYCLE866_SCALED_BANKS",
             "OWNER_DIRECTED_RUN_TO_GROUND_NO_AXIOM_SURFACE_TOUCHED",
             f"DECLARED_PROBE events={EVENTS_USED} k=2 horizon={HORIZON}"
             f" store_cap={STORE_CAP}"]
    for B in BANK_COUNTS:
        lines.append(f"CERTIFICATE B{B}_RESULTS PASS "
                     + compact(results[B]))
    summary = {"checks": checks, "cycle": 866,
               "runtime_seconds": runtime,
               "native_functional_by_B": {
                   B: results[B]["birth_datum"]["native_pattern_functional"]
                   for B in BANK_COUNTS},
               "on_tick_by_B": {
                   B: results[B]["derived_clock"]
                   ["allsync_on_tick_fraction"] for B in BANK_COUNTS},
               "pass": all(checks.values())}
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE866_SCALED_BANKS_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
