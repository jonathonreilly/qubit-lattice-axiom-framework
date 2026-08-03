#!/usr/bin/env python3
"""Cycle 867: the composed record-write model (records as state content).

Owner-directed run-to-ground (supervisor-authored). The 863-865 arc's
stamps were interpretive annotations over record-free trajectories (the
reversibility seam named by the literature search). This cycle composes
the model: record writes fire DYNAMICALLY at bank clean-edges, written
into BOUNDARY-DEAD wires (the Cycle-854 never-active gauge freedom used
as the record medium) — records become genuine, readable, permanent
state content while the active dynamics is provably unperturbed.

A. DEAD_WIRE_REGISTER: derive boundary-dead wires; verify the composed
   writes never collide with active dynamics and are write-once through
   the declared horizon.
B. REGISTER_REPRODUCES_ANNOTATION: the register's first-write structure
   equals the annotation-machinery's event structure at the same
   horizon (the phantom-stamp seam closed).
C. FORMATION_LOCALITY (the honest saturation reformulation): at
   formation edges, probe DECLARED perturbation classes (one_flip,
   late_acting, untouched_in_chunk, flip_and_restore) on payload wires
   with TRUE bank membership (kernel pack-state marking), near
   (recording-bank) versus far (other-bank); firing and content
   invariance are reported as data whichever way they fall.
D. CONTROLS.

Declared scope: B=2, the 852 census, horizon 16,384 orbits;
dead-wire derivation window 512 orbits at chunk granularity then
orbit granularity to 4,096; locality sample 32 early-formation keys,
up to 4 payload wires per side, register cap 64 wire-visible ordinals
per (tag, lane) — all caps disclosed in the emitted certificates.
bounded_theorem, authority none, audit unset. Independent audit still
required.

v3 (2026-08-03): the finale checker refuted the v2 probe's
implementation — uniform chunk slicing was off-trajectory (true
per-step gate counts are non-uniform) and the index-half bank split
left the far arm empty — and found REGISTER_CAP undisclosed. v3
reconstructs trajectories from true per-step chunks, derives bank
membership by kernel pack-state marking, runs the four declared
perturbation classes on both sides, and discloses every cap.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle863_time_from_records_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]: "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
}
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle863_time_from_records_2026_07_28 as C863

HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
LOCALITY_SAMPLE = 32
LOCALITY_BOUNDARY_CAP = 1_100
REGISTER_CAP = 64
PAYLOAD_WIRES_PER_SIDE = 4
PERTURBATION_CLASSES = (
    "one_flip", "late_acting", "untouched_in_chunk", "flip_and_restore"
)


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


def true_step_chunks(program, positions):
    """Per-step gate lists on the true trajectory (variable length,
    station order) — replaces the v2 uniform slicing the checker refuted."""
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
    """TRUE bank membership of packed state rows via single-bit
    pack-state marking — replaces the v2 index-half split the checker
    refuted (it left the far arm empty)."""
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


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = C863.derive_census()
    stations = len(program)
    n = len(census)
    states, init_fail = C863.build_initial_states(
        program, event_seeds, census
    )
    sim = census + (census[0],)
    dup = n
    columns = C863.pack_lanes(states + (states[0],))
    fast = C863.compile_fast(C863.masked_h_schedules(program, sim))
    per_bank, links, source_ptr = C863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1

    # --- Certificate A part 1: derive boundary-dead wires -----------------
    acc = [0] * len(columns)
    work = [c for c in columns]
    for w, c in enumerate(work):
        acc[w] |= c
    boundary = 0
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            boundary += 1
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    mask_lanes = uni_sim
    dead_wires = tuple(
        w for w in range(len(acc)) if (acc[w] & mask_lanes) == 0
    )
    dead_set = set(dead_wires)

    # Safe register slots: dead wires that no gate ever READS (inputs) or
    # WRITES (targets) — mutation is then STRUCTURALLY inert: the active
    # dynamics cannot see or touch them. Derived from the raw schedules.
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
    slot_tags = [("G", 0)] + [
        (f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    if len(safe_slots_pool) < len(slot_tags):
        raise AssertionError(("insufficient safe slots",
                              len(safe_slots_pool), len(slot_tags)))
    slot_of = {tag: safe_slots_pool[i] for i, tag in enumerate(slot_tags)}
    slot_wires = set(slot_of.values())

    # --- The composed scan: base dynamics + REAL register writes ----------
    columns = C863.pack_lanes(states + (states[0],))
    register: list[list[tuple]] = [[] for _ in range(n)]
    register_counts = [0] * n
    bank_write_ordinal = [[0, 0] for _ in range(n)]
    write_once_violations = 0
    dead_activation_conflicts = 0
    wire_visible_writes = 0

    def wire_write(tag, lane):
        nonlocal write_once_violations, wire_visible_writes
        wire = slot_of[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit
        wire_visible_writes += 1
    prev_bank = [
        C863.mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    e1_first_composed: dict = {}
    prev_global = C863.mask_over(columns, global_dirty, uni_sim)
    mism = int(bool(prev_global & 1) != bool(prev_global & (1 << dup)))
    for lane in C863.lanes_of(prev_global & uni_all):
        e1_first_composed.setdefault(census[lane], 0)
        wire_write(("G", 0), lane)
        if register_counts[lane] < REGISTER_CAP:
            register[lane].append((0, "G", sha256(bytes(
                C863.lane_state(columns, lane))).hexdigest()[:16]))
        register_counts[lane] += 1

    boundary = 0
    written_marks: set = set()
    for orbit in range(1, HORIZON + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = C863.mask_over(columns, global_dirty, uni_sim)
            mism += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            new_e1 = 0
            for lane in C863.lanes_of(ga):
                if census[lane] not in e1_first_composed:
                    e1_first_composed[census[lane]] = boundary
                    new_e1 |= 1 << lane
            for b in (0, 1):
                bm = C863.mask_over(columns, bank_dirty[b], uni_all)
                edge = bm & ~prev_bank[b]
                for lane in C863.lanes_of(edge):
                    ordinal = bank_write_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                        register[lane].append(
                            (boundary, f"B{b}", sha256(bytes(
                                C863.lane_state(columns, lane)
                            )).hexdigest()[:16])
                        )
                    bank_write_ordinal[lane][b] = ordinal + 1
                    register_counts[lane] += 1
                prev_bank[b] = bm
            for w in dead_wires:
                if w in slot_wires:
                    continue
                if columns[w] & uni_sim:
                    dead_activation_conflicts += 1
                    break

    slot_population = {
        compact(tag): bin(columns[wire]).count("1")
        for tag, wire in sorted(slot_of.items())
    }
    cert_a = {
        "certificate": "A_DEAD_WIRE_REGISTER",
        "dead_wire_count": len(dead_wires),
        "safe_slot_pool": len(safe_slots_pool),
        "slots_allocated": len(slot_of),
        "structural_inertness": {
            "slots_in_gate_inputs": len(slot_wires & gate_inputs),
            "slots_in_gate_targets": len(slot_wires & gate_targets),
            "statement": (
                "register slots are dead wires no gate reads or writes;"
                " mutation cannot influence or be influenced by the"
                " active dynamics — inertness is structural, and the"
                " writes REALLY mutate the state columns"
            ),
        },
        "derivation_window": {
            "chunk_granularity_orbits": DEAD_CHUNK_ORBITS,
            "orbit_granularity_orbits": DEAD_ORBIT_ORBITS,
        },
        "dead_activation_conflicts_through_horizon":
            dead_activation_conflicts,
        "write_once_violations_on_wires": write_once_violations,
        "write_once_semantics": (
            "zero violations certifies the fresh-slot allocation"
            " discipline (strictly increasing per-(tag,lane) ordinal)"
            " plus non-interference; content immutability under slot"
            " reuse is out of scope by construction"
        ),
        "register_cap_per_tag_lane": REGISTER_CAP,
        "wire_visible_write_events": wire_visible_writes,
        "write_events_beyond_cap_not_wire_visible":
            sum(register_counts) - wire_visible_writes,
        "total_register_write_events": sum(register_counts),
        "wire_bits_set_total": sum(slot_population.values()),
        "slot_population_sample": dict(list(slot_population.items())[:6]),
    }
    cert_a["pass"] = (
        len(dead_wires) > 0
        and len(slot_wires & gate_inputs) == 0
        and len(slot_wires & gate_targets) == 0
        and dead_activation_conflicts == 0
        and write_once_violations == 0
        and sum(slot_population.values()) > 0
    )

    # --- Certificate B: register reproduces annotation at same horizon ----
    old_h = C863.TRAJECTORY_HORIZON
    C863.TRAJECTORY_HORIZON = HORIZON
    try:
        rep = C863.replay(program, event_seeds, census)
    finally:
        C863.TRAJECTORY_HORIZON = old_h
    anno_e1 = rep["e1_moment"]
    match = sum(
        1 for key, b in e1_first_composed.items()
        if anno_e1.get(key) == b
    )
    g_wire_lanes = set(C863.lanes_of(columns[slot_of[("G", 0)]] & uni_all))
    b0_first_lanes = set(
        C863.lanes_of(columns[slot_of[("B0", 0)]] & uni_all)
    )
    wire_existence_count = len(
        g_wire_lanes | b0_first_lanes | set(
            C863.lanes_of(columns[slot_of[("B1", 0)]] & uni_all)
        )
    )
    cert_b = {
        "certificate": "B_REGISTER_REPRODUCES_ANNOTATION",
        "declared_horizon": HORIZON,
        "composed_first_writes": len(e1_first_composed),
        "annotation_stamps_at_horizon": len(anno_e1),
        "moment_exact_matches": match,
        "wire_level_existence": {
            "lanes_with_any_first_slot_bit": wire_existence_count,
            "statement": (
                "record EXISTENCE is read back from the mutated state"
                " wires; moments/contents are measurement metadata (host"
                " log), disclosed as such"
            ),
        },
        "finding": (
            "the phantom-stamp seam is closed iff every annotation stamp"
            " has a moment-exact composed register write and vice versa,"
            " with existence readable from the state itself"
        ),
    }
    cert_b["pass"] = (
        match == len(anno_e1) == len(e1_first_composed)
        and rep["mismatches"] == 0
        and wire_existence_count >= len(e1_first_composed)
    )

    # --- Certificate C: formation locality probe (v3, corrected) ----------
    seeds = dict(C863.derive_event_seeds(program))
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

    tally = {
        cls: {side: {"probes": 0, "fired": 0, "content_equal": 0}
              for side in ("near", "far")}
        for cls in PERTURBATION_CLASSES
    }
    sampled = 0
    base_not_clean = 0
    degenerate_restore_skips = 0
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
        if not all(base_after[w] == 0 for w in global_dirty):
            base_not_clean += 1
            continue
        sampled += 1
        base_content = sha256(bytes(base_after)).hexdigest()
        rec_bank = 0 if all(
            base_after[w] == 0 for w in bank_dirty[0]
        ) else 1
        first_touch: dict = {}
        for idx, gate in enumerate(last_chunk):
            for w in gate.wires:
                first_touch.setdefault(w, idx)
        for side, bank in (("near", rec_bank), ("far", 1 - rec_bank)):
            pool = bank_payload[bank]
            picks = {"one_flip": pool[0], "flip_and_restore": pool[0]}
            touched = [w for w in pool if w in first_touch]
            picks["late_acting"] = (
                max(touched, key=lambda w: first_touch[w])
                if touched else None
            )
            untouched = [w for w in pool if w not in first_touch]
            picks["untouched_in_chunk"] = (
                untouched[0] if untouched else None
            )
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
                fired = all(after[w] == 0 for w in global_dirty)
                cell = tally[cls][side]
                cell["probes"] += 1
                cell["fired"] += int(fired)
                if fired:
                    cell["content_equal"] += int(
                        sha256(bytes(after)).hexdigest() == base_content
                    )

    def rate(cls, side, field):
        cell = tally[cls][side]
        return (cell[field] / cell["probes"]) if cell["probes"] else None

    restore_contrast = (
        rate("flip_and_restore", "near", "content_equal") is not None
        and rate("flip_and_restore", "far", "content_equal") is not None
        and rate("flip_and_restore", "near", "content_equal")
        != rate("flip_and_restore", "far", "content_equal")
    )
    cert_c = {
        "certificate": "C_FORMATION_LOCALITY",
        "declared_sample": {
            "lanes": sampled,
            "boundary_cap": LOCALITY_BOUNDARY_CAP,
            "lane_cap": LOCALITY_SAMPLE,
            "wires_per_side": PAYLOAD_WIRES_PER_SIDE,
            "classes": PERTURBATION_CLASSES,
            "base_not_clean_skips": base_not_clean,
            "degenerate_restore_skips": degenerate_restore_skips,
        },
        "payload_derivation": {
            "pool_size": len(payload_pool),
            "bank_pool_sizes": [len(bank_payload[0]), len(bank_payload[1])],
            "membership": "kernel pack-state single-bit marking",
        },
        "per_class": tally,
        "computed_reading": {
            "one_flip_fires_near": rate("one_flip", "near", "fired"),
            "one_flip_fires_far": rate("one_flip", "far", "fired"),
            "direct_flip_content_equal_near":
                rate("one_flip", "near", "content_equal"),
            "direct_flip_content_equal_far":
                rate("one_flip", "far", "content_equal"),
            "restore_content_equal_near":
                rate("flip_and_restore", "near", "content_equal"),
            "restore_content_equal_far":
                rate("flip_and_restore", "far", "content_equal"),
            "restore_class_near_far_contrast": restore_contrast,
        },
        "finding": (
            "per-class firing and content-invariance counts are the"
            " exact verdict at the declared sample, classes, and pools;"
            " the near/far contrast question is answered by the"
            " computed_reading rates, whichever way they fall"
        ),
    }
    # Integrity gate only — bookkeeping consistency, never the outcome.
    cells_ok = all(
        0 <= cell["content_equal"] <= cell["fired"] <= cell["probes"]
        <= sampled
        for cls in PERTURBATION_CLASSES for cell in (tally[cls]["near"],
                                                     tally[cls]["far"])
    )
    cert_c["pass"] = (
        sampled > 0
        and cells_ok
        and sampled + base_not_clean == len(candidates)
        and len(bank_payload[0]) > 0 and len(bank_payload[1]) > 0
    )

    runtime = round(monotonic() - started, 3)
    checks = {
        "A_DEAD_WIRE_REGISTER": cert_a["pass"],
        "B_REGISTER_REPRODUCES_ANNOTATION": cert_b["pass"],
        "C_FORMATION_LOCALITY": cert_c["pass"],
        "D_CONTROLS": bool(
            controls["pass"] and init_fail == 0 and mism == 0
            and runtime < AUDIT_TIMEOUT_SEC
        ),
    }
    lines = ["CYCLE867_COMPOSED_RECORD_WRITE",
             "OWNER_DIRECTED_RUN_TO_GROUND_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("A_DEAD_WIRE_REGISTER", cert_a),
                          ("B_REGISTER_REPRODUCES_ANNOTATION", cert_b),
                          ("C_FORMATION_LOCALITY", cert_c)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {"checks": checks, "cycle": 867,
               "runtime_seconds": runtime,
               "pass": all(checks.values())}
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE867_COMPOSED_RECORD_WRITE_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
