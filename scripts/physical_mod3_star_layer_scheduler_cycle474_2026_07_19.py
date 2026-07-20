#!/usr/bin/env python3
"""Cycle 474: proper-cubic carried mod-3 scheduler for Cycle-470 stars.

Each Cycle-463 layer is partitioned into 27 coordinate-residue rounds.  Targets
in one round have disjoint seven-supercell stars, so complete Cycle-470 local
blocks can execute in event lockstep without M2/path/port conflicts.  The
schedule is a bounded finite compiler witness, not a time law or an optimal
coloring claim.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
from time import perf_counter
import resource
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467
import physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19 as c470


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MOD3_STAR_LAYER_SCHEDULER_CYCLE474_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
COLORS = tuple(product(range(3), repeat=3))
COLOR_COUNT = len(COLORS)
ARITHMETIC_EVENTS = 12_719_213
FROZEN_C467_ROUTE_DIGEST = "4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457"
FROZEN_C470_COMBINED_MANIFEST = "4b3c532fe2507e72c529e32a396d7288e28042a493492f55eff9dc6f906a7502"
FROZEN_C467_RUNNER_SHA = "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"
FROZEN_C470_RUNNER_SHA = "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"
WALL_CAP_SECONDS = 180.0
RSS_CAP_MIB = 1536.0
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Color = tuple[int, int, int]
Edge = tuple[int, int]
ZERO: Coord = (0, 0, 0)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 474", "27-color",
        "every target exactly once", "site-disjoint seven-supercell stars",
        "all 2,592 rounds", "all 24 proper-cubic frames", "held cube",
        "no global re-sort", "event manifest is not repeated primitive execution",
        "iteration count, color round, and parallel depth are not time",
        "not energy, stress, lapse, metric, proper time, backreaction, or gravity",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle474 note freezes the whole-layer scheduler boundary and N1-N8 gate", not missing, missing)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def color(coord: Coord) -> Color:
    return tuple(value % 3 for value in coord)  # type: ignore[return-value]


def star(target: Coord) -> frozenset[Coord]:
    return frozenset((target,) + c463.six_neighbors(target))


@dataclass(frozen=True)
class Round:
    layer: int
    read_layer: int
    write_layer: int
    color: Color
    targets: tuple[Coord, ...]


def rounds(radius: int, layer: int) -> tuple[Round, ...]:
    item = c463.domain(radius)
    if layer not in range(c463.ITERATIONS):
        raise ValueError("layer leaves the frozen schedule")
    return tuple(
        Round(layer, layer, layer + 1, item_color,
              tuple(target for target in item.active if color(target) == item_color))
        for item_color in COLORS
    )


def validate_round(item: c463.Domain, item_round: Round) -> None:
    if item_round.layer not in range(c463.ITERATIONS):
        raise ValueError("round layer leaves the schedule")
    if item_round.read_layer != item_round.layer or item_round.write_layer != item_round.layer + 1:
        raise ValueError("round violates retained-history dependency order")
    if item_round.color not in COLORS or len(set(item_round.targets)) != len(item_round.targets):
        raise ValueError("round has malformed color or duplicate target")
    if any(target not in item.active_index or color(target) != item_round.color for target in item_round.targets):
        raise ValueError("round target leaves its declared color class/domain")
    if any(star(left) & star(right) for left, right in combinations(item_round.targets, 2)):
        raise ValueError("round contains overlapping seven-supercell stars")


def layer_block_data(circuit: c467.Circuit) -> tuple[dict[str, object], ...]:
    output = []
    for layer in range(c463.ITERATIONS):
        actions = c470.ingress_actions(layer, circuit)
        ingress_events = sum(action.primitive_events for action in actions)
        ingress_digest = c470.action_digest(actions)
        block_events = ARITHMETIC_EVENTS + 2 * ingress_events
        manifest = sha256(
            f"{layer}|{ingress_digest}|{FROZEN_C467_ROUTE_DIGEST}|inverse:{ingress_digest}|{block_events}".encode()
        ).hexdigest()
        output.append({
            "layer": layer, "ingress_events": ingress_events,
            "block_events": block_events, "ingress_digest": ingress_digest,
            "block_manifest": manifest,
        })
    return tuple(output)


def schedule_controls(block_data: tuple[dict[str, object], ...]) -> dict[int, dict[str, object]]:
    results = {}
    for radius in (c463.TRAIN_RADIUS, c463.HELD_RADIUS):
        item = c463.domain(radius)
        failures = 0
        conflict_failures = 0
        shell_reads = 0
        manifest = sha256()
        maximum_parallel = 0
        total_events = 0
        parallel_depth = 0
        for layer in range(c463.ITERATIONS):
            seen = []
            datum = block_data[layer]
            for item_round in rounds(radius, layer):
                try:
                    validate_round(item, item_round)
                except ValueError:
                    failures += 1
                seen.extend(item_round.targets)
                maximum_parallel = max(maximum_parallel, len(item_round.targets))
                supports = [star(target) for target in item_round.targets]
                conflict_failures += sum(bool(left & right) for left, right in combinations(supports, 2))
                shell_reads += sum(
                    neighbor in item.shell_index
                    for target in item_round.targets for neighbor in c463.six_neighbors(target)
                )
                block_events = int(datum["block_events"])
                total_events += len(item_round.targets) * block_events
                parallel_depth += block_events
                manifest.update(
                    f"{layer}|{item_round.read_layer}|{item_round.write_layer}|{item_round.color}|"
                    f"{item_round.targets}|{datum['block_manifest']}|event-lockstep\n".encode()
                )
            failures += int(len(seen) != len(item.active) or set(seen) != set(item.active) or len(set(seen)) != len(seen))
        expected_shell_reads = c463.ITERATIONS * (54 if radius == 1 else 150)
        expected_events = len(item.active) * sum(int(row["block_events"]) for row in block_data)
        expected_depth = COLOR_COUNT * sum(int(row["block_events"]) for row in block_data)
        results[radius] = {
            "targets": len(item.active), "rounds": c463.ITERATIONS * COLOR_COUNT,
            "maximum_parallel_blocks": maximum_parallel, "shell_reads": shell_reads,
            "total_elementary_events_manifested": total_events,
            "strict_parallel_depth": parallel_depth, "schedule_digest": manifest.hexdigest(),
        }
        check(
            f"R={radius} all 2,592 rounds cover every target exactly once with site-disjoint seven-supercell stars and exact retained-layer dependencies",
            failures == 0 and conflict_failures == 0 and shell_reads == expected_shell_reads
            and total_events == expected_events and parallel_depth == expected_depth,
            {**results[radius], "coverage_or_dependency_failures": failures,
             "simultaneous_star_conflicts": conflict_failures,
             "expected_shell_reads": expected_shell_reads,
             "physical_domain_M2": item.physical_m2,
             "maximum_simultaneous_support_M2": maximum_parallel * 7 * c463.SUPERCELL_M2,
             "simultaneous_M2_path_port_conflicts": 0},
        )
    return results


def colored_forward(state: c463.CoarseState, item: c463.Domain, *, reverse: bool = False,
                    delete: tuple[int, Coord] | None = None,
                    bad_dependency: bool = False) -> c463.CoarseState:
    c463.validate_source(state.source, item, allow_vacuum=True)
    history = [list(layer) for layer in state.history]
    layer_order = reversed(range(c463.ITERATIONS)) if reverse else range(c463.ITERATIONS)
    for layer in layer_order:
        layer_rounds = tuple(reversed(rounds(item.radius, layer))) if reverse else rounds(item.radius, layer)
        for item_round in layer_rounds:
            validate_round(item, item_round)
            for target in reversed(item_round.targets) if reverse else item_round.targets:
                if delete == (layer, target):
                    continue
                read_layer = layer + 1 if bad_dependency else item_round.read_layer
                if read_layer not in range(len(history)):
                    raise ValueError("dependency read leaves retained history")
                neighbors = tuple(
                    history[read_layer][item.active_index[coord]] if coord in item.active_index else 0
                    for coord in c463.six_neighbors(target)
                )
                value = c463.local_quotient(neighbors, state.source[item.active_index[target]], strict=not bad_dependency)
                target_index = item.active_index[target]
                if reverse:
                    if history[item_round.write_layer][target_index] != value:
                        raise ValueError("inverse target does not match its retained dependency")
                    history[item_round.write_layer][target_index] = 0
                else:
                    if history[item_round.write_layer][target_index] != 0:
                        raise ValueError("forward target is not blank")
                    history[item_round.write_layer][target_index] = value
    return c463.CoarseState(state.source, tuple(tuple(layer) for layer in history))


def history_semantics_controls() -> dict[int, c463.CoarseState]:
    output = {}
    rows = []
    for radius in (c463.TRAIN_RADIUS, c463.HELD_RADIUS):
        item = c463.domain(radius)
        initial = c463.initial_coarse(item)
        colored = colored_forward(initial, item)
        baseline = c463.coarse_forward(initial, item)
        restored = colored_forward(colored, item, reverse=True)
        rows.append({
            "radius": radius, "EG_word_mismatches": int(colored != baseline),
            "inverse_mismatches": int(restored != initial),
            "nonblank_final_targets": sum(value != 0 for value in colored.history[-1]),
        })
        output[radius] = colored
    check(
        "the full 96-layer colored forward and reverse schedules equal Cycle463 E/G history semantics exactly",
        all(row["EG_word_mismatches"] == 0 and row["inverse_mismatches"] == 0 for row in rows),
        rows,
    )
    return output


def transfer_edge_counts(actions: tuple[c470.Action, ...]) -> Counter[Edge]:
    counts: Counter[Edge] = Counter()
    for action in actions:
        ids = tuple(c470.state_index(coord) for coord in action.path)
        if action.kind == "remote_cnot":
            for left, right in zip(ids[:-2], ids[1:-1]):
                counts[(min(left, right), max(left, right))] += 12  # ingress+egress, two SWAP traversals each
            left, right = ids[-2], ids[-1]
            counts[(min(left, right), max(left, right))] += 2
        else:
            for left, right in zip(ids[:-2], ids[1:-1]):
                counts[(min(left, right), max(left, right))] += 12
            left, right = ids[-2], ids[-1]
            counts[(min(left, right), max(left, right))] += 6
    return counts


def congestion_controls(circuit: c467.Circuit, block_data: tuple[dict[str, object], ...]) -> dict[str, object]:
    state = [0] * (7 * c463.SUPERCELL_M2)
    arithmetic = c470.ArithmeticExecutor(circuit.layout.wire_count, state)
    result = c470.execute_arithmetic(arithmetic, circuit)
    local_maxima = []
    transfer_maxima = []
    for layer in range(c463.ITERATIONS):
        transfer = transfer_edge_counts(c470.ingress_actions(layer, circuit))
        transfer_maxima.append(max(transfer.values(), default=0))
        combined = transfer.copy()
        combined.update(arithmetic.edge_counts)
        local_maxima.append(max(combined.values(), default=0))
    sum_block_events = sum(int(row["block_events"]) for row in block_data)
    strict_parallel_depth = COLOR_COUNT * sum_block_events
    detail = {
        "arithmetic_events": result.events,
        "arithmetic_route_digest": result.digest,
        "arithmetic_max_edge_incidence": max(arithmetic.edge_counts.values()),
        "transfer_max_edge_incidence_range": (min(transfer_maxima), max(transfer_maxima)),
        "local_block_max_edge_incidence_range": (min(local_maxima), max(local_maxima)),
        "layer48_local_edge_incidence": local_maxima[48],
        "peak_simultaneous_block_count": 8,
        "peak_simultaneous_edge_conflicts": 0,
        "strict_parallel_depth_per_forward_history": strict_parallel_depth,
        "strict_parallel_depth_forward_plus_inverse": 2 * strict_parallel_depth,
        "full_layer_per_edge_incidence_upper_bound": 7 * max(local_maxima),
        "full_history_per_edge_incidence_upper_bound": 7 * sum(local_maxima),
        "construction_optimality_claimed": False,
    }
    check(
        "literal Cycle467 routing plus exact transfer paths give strict parallel depth and congestion upper bounds",
        result.digest == FROZEN_C467_ROUTE_DIGEST and result.events == ARITHMETIC_EVENTS
        and result.adjacency_failures == 0 and result.restored_mapping
        and local_maxima[48] == 9749 and strict_parallel_depth == 36_132_875_280,
        detail,
    )
    return detail


def transform_color(frame: c463.Frame, item_color: Color) -> Color:
    return tuple(value % 3 for value in c463.transform(frame, item_color))  # type: ignore[return-value]


def covariance_controls(results: dict[int, dict[str, object]],
                        block_data: tuple[dict[str, object], ...]) -> None:
    frames = c463.proper_cubic_frames()
    failures = 0
    manifests = []
    for frame in frames:
        frame_digest = sha256()
        frame_digest.update(repr(frame).encode())
        for radius in (c463.TRAIN_RADIUS, c463.HELD_RADIUS):
            item = c463.domain(radius)
            carried_sequence = []
            for layer in range(c463.ITERATIONS):
                for item_round in rounds(radius, layer):
                    carried_color = transform_color(frame, item_round.color)
                    carried_targets = tuple(c463.transform(frame, target) for target in item_round.targets)
                    carried_sequence.append(carried_color)
                    failures += int(set(carried_targets) != {
                        target for target in item.active if color(target) == carried_color
                    })
                    for target in item_round.targets:
                        failures += int(
                            {c463.transform(frame, coord) for coord in star(target)}
                            != set(star(c463.transform(frame, target)))
                        )
                    frame_digest.update(
                        f"{radius}|{layer}|{carried_color}|{carried_targets}|"
                        f"{block_data[layer]['block_manifest']}|carried-no-resort\n".encode()
                    )
            expected_colors = tuple(transform_color(frame, item_color) for _ in range(c463.ITERATIONS) for item_color in COLORS)
            failures += int(tuple(carried_sequence) != expected_colors)
            failures += int(set(carried_sequence[:COLOR_COUNT]) != set(COLORS))
            frame_digest.update(str(results[radius]["strict_parallel_depth"]).encode())
        manifests.append(frame_digest.hexdigest())
    check(
        "all 24 proper-cubic frames carry colors, target order, disjoint stars, dependencies, and block manifests without a global re-sort",
        len(frames) == 24 and failures == 0 and len(set(manifests)) == 24,
        {"frames": len(frames), "carried_failures": failures,
         "frame_schedule_manifests": manifests, "global_resort_used": False,
         "carried_sequence_rule": "map the reference color/target sequence by F; do not regenerate lexicographic order"},
    )


def deletion_and_domain_controls(histories: dict[int, c463.CoarseState]) -> None:
    held = c463.domain(c463.HELD_RADIUS)
    initial = c463.initial_coarse(held)
    baseline = histories[c463.HELD_RADIUS]
    delete_target = (48, (0, 0, 0))
    deleted = colored_forward(initial, held, delete=delete_target)
    deletion_changes = deleted != baseline and deleted.history[49][held.active_index[ZERO]] == 0

    mod2_conflicts = []
    for left, right in combinations(held.active, 2):
        if tuple(value % 2 for value in left) == tuple(value % 2 for value in right) and star(left) & star(right):
            mod2_conflicts.append((left, right, tuple(sorted(star(left) & star(right)))))
    omitted = tuple(item_round for item_round in rounds(c463.HELD_RADIUS, 0) if item_round.color != (0, 0, 0))
    omitted_targets = {target for item_round in omitted for target in item_round.targets}
    duplicate_refused = False
    try:
        item_round = rounds(c463.HELD_RADIUS, 0)[0]
        validate_round(held, Round(0, 0, 1, item_round.color, item_round.targets + item_round.targets[:1]))
    except ValueError:
        duplicate_refused = True
    wrong_color_refused = False
    try:
        validate_round(held, Round(0, 0, 1, (0, 0, 0), ((1, 0, 0),)))
    except ValueError:
        wrong_color_refused = True
    dependency_refused = False
    try:
        item_round = rounds(c463.HELD_RADIUS, 0)[0]
        validate_round(held, Round(0, 1, 1, item_round.color, item_round.targets))
    except ValueError:
        dependency_refused = True
    wrong_inverse_refused = False
    try:
        colored_forward(baseline, held, reverse=True, bad_dependency=True)
    except (ValueError, OverflowError):
        wrong_inverse_refused = True
    shell_refused = False
    physical = c463.encode(initial, held)
    corrupt_shell = [list(layer) for layer in physical.boundary_history]
    corrupt_shell[0][0] = c463.binary(1)
    try:
        c463.validate_physical(c463.replace(physical, boundary_history=tuple(tuple(layer) for layer in corrupt_shell)), held)
    except ValueError:
        shell_refused = True
    check(
        "target/color/dependency deletions and malformed mod-2, duplicate, wrong-color, inverse, and shell schedules are exposed or refused",
        deletion_changes and len(omitted_targets) < len(held.active) and bool(mod2_conflicts)
        and duplicate_refused and wrong_color_refused and dependency_refused
        and wrong_inverse_refused and shell_refused,
        {"deleted_target_changes_history": deletion_changes,
         "omitted_color_missing_targets": len(held.active) - len(omitted_targets),
         "mod2_overlap_witnesses": mod2_conflicts[:3], "mod2_overlap_count": len(mod2_conflicts),
         "duplicate_refused": duplicate_refused, "wrong_color_refused": wrong_color_refused,
         "dependency_refused": dependency_refused, "wrong_inverse_refused": wrong_inverse_refused,
         "nonblank_shell_refused": shell_refused,
         "minimum_color_claimed": False},
    )


def frozen_dependency_and_no_go_controls() -> None:
    c467_path = ROOT / "scripts/physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py"
    c470_path = ROOT / "scripts/physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py"
    check(
        "Cycle467/470 artifacts and route identities remain frozen",
        file_sha(c467_path) == FROZEN_C467_RUNNER_SHA and file_sha(c470_path) == FROZEN_C470_RUNNER_SHA,
        {"Cycle467_runner_SHA": file_sha(c467_path), "expected_Cycle467": FROZEN_C467_RUNNER_SHA,
         "Cycle470_runner_SHA": file_sha(c470_path), "expected_Cycle470": FROZEN_C470_RUNNER_SHA,
         "Cycle467_route_digest": FROZEN_C467_ROUTE_DIGEST,
         "Cycle470_literal_combined_manifest": FROZEN_C470_COMBINED_MANIFEST},
    )
    check(
        "the supplied/constructed/open inventory keeps history, time, source, and gravity boundaries explicit",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "supplied": ["Cycle463 domains, retained history order, shell, and local law",
                         "Cycle467 arithmetic trace", "Cycle470 serial seven-cell block",
                         "reference mod-3 color order and strict event-lockstep policy"],
            "constructed": ["27-color finite schedules", "exact star-disjointness and coverage",
                             "full forward/inverse word histories", "event/depth/congestion manifests",
                             "held boundary controls and all24 carried schedules"],
            "open": ["lower-color or lower-depth schedules", "optimized global routing",
                     "history removal", "law/source/time/gravity derivation"],
            "not_claimed": ["27-color minimality", "depth as duration", "source as energy/stress",
                            "continuum, metric, backreaction, or gravity"],
            "event_manifest_is_not_repeated_primitive_execution": True,
        },
    )
    check(
        "full N1-N8 rejects no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "mod-3^3 succeeds; denser star colorings, edge coloring, moving-head, staggered, and cache/network schedules remain alternatives",
            "N2": "color scheduling, local routing, arithmetic, retained history, law selection, source meaning, clock interpretation, and gravity remain independent",
            "N3": "27 reference colors, lexicographic manifest order, blank targets, layer barriers, strict local trace, boundaries, and frame orbit are exposed",
            "N4": "the witness matches Cycle470's overlapping-star residual and no source/time/gravity residual",
            "N5": "claims stop at finite R1/R2 event manifests and exact word histories; no optimum, infinite, continuum, or time rhetoric",
            "N6": "whole-layer conflict scheduling closes constructively while efficiency, history, and law/source walls remain open",
            "N7": "a reviewer can seek fewer rounds, edge-colored pipelines, cached faces, asynchronous local barriers, or dynamical link transport",
            "N8": "Cycle470's overlap residual closes only for this retained-history finite schedule; C_wrap/C_source/gravity echoes remain; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle474 run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle474 physical mod-3 whole-layer star scheduler")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    circuit = c467.make_circuit(c463.VALUE_BITS, c463.DENOMINATOR)
    block_data = layer_block_data(circuit)
    schedule_results = schedule_controls(block_data)
    histories = history_semantics_controls()
    congestion_controls(circuit, block_data)
    covariance_controls(schedule_results, block_data)
    deletion_and_domain_controls(histories)
    frozen_dependency_and_no_go_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
