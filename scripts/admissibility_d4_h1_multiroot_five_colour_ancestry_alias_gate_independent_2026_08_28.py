#!/usr/bin/env python3
"""Independent Block 221 Stage-A ancestry-alias audit."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import signal
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180
BLOCK221_PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block221-time-multiplexed-ancestry-finality-20260828"
)
BLOCK220_PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827"
)
SIDECAR = f"{BLOCK220_PACK}/FROZEN_MARKOV_RULE.json"
ENTRY_WITNESS = f"{BLOCK220_PACK}/BLOCK221_ENTRY_COUNTEREXAMPLE.md"
BOUNDARY_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_MULTIROOT_FIVE_COLOUR_ANCESTRY_"
    "DART_ALIAS_BOUNDARY_NOTE_2026-08-28.md"
)
DISCIPLINE = (
    "docs/ADMISSIBILITY_D4_H1_MULTIROOT_FIVE_COLOUR_ANCESTRY_"
    "DART_ALIAS_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (
    SIDECAR,
    ENTRY_WITNESS,
    f"{BLOCK221_PACK}/GOAL.md",
    f"{BLOCK221_PACK}/PREREGISTRATION.md",
    f"{BLOCK221_PACK}/MUTATION_PLAN.md",
    f"{BLOCK221_PACK}/NO_GO_LEDGER.md",
    BOUNDARY_NOTE,
    DISCIPLINE,
)
EXPECTED_RULE_SHA256 = (
    "159dd7dfb9787d146eb55440749577db6818c8f88be743191a633e758ac8e223"
)
PORT_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
MUTATIONS = (
    "rule_semantic_tamper",
    "open_training_grid",
    "merge_labelled_darts",
    "three_depth_colours",
    "permit_first_alias",
    "drop_one_false_record",
    "quarter_turn_inverse",
    "endpoint_is_dart",
    "inject_epoch_memory",
    "promote_broad_no_go",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Stage-A audit timed out")


class Checks:
    def __init__(self, verbose: bool = True) -> None:
        self.passed = 0
        self.failed = 0
        self.verbose = verbose

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            if self.verbose:
                print(f"PASS {label}")
        else:
            self.failed += 1
            if self.verbose:
                suffix = f" :: {detail}" if detail else ""
                print(f"FAIL {label}{suffix}")


@dataclass(frozen=True, order=True)
class Cell:
    kind: str
    bit: int = -1
    direction: int = -1


@dataclass(frozen=True, order=True)
class LocalAction:
    row_id: str
    actor: int
    port: int
    target: int
    writes: tuple[tuple[int, Cell], ...]


@dataclass(frozen=True)
class ReachabilityCensus:
    same_starts: int
    same_records: int
    opposite_starts: int
    opposite_records: int
    maximum_reached: int
    maximum_shortest_record_trace: int
    first_start: tuple[int, tuple[int, int], tuple[int, int]]
    first_trace: tuple[str, ...]


@dataclass(frozen=True, order=True)
class PortCycle:
    path: tuple[int, ...]
    edge_ports: tuple[int, ...]
    collision_port: int


@dataclass(frozen=True)
class AliasEvidence:
    width: int
    root: int
    launch_port: int
    path: tuple[int, ...]
    edge_ports: tuple[int, ...]
    collision_port: int
    site: int
    expected_site: int
    expected_port: int
    candidate_ports: tuple[int, ...]
    candidate_sites: tuple[int, ...]
    reason: str


@dataclass(frozen=True)
class CycleCensus:
    cycles: int
    ambiguous: int
    lost_parallel_dart: int
    next_colour_chord: int
    lost_collision_dart: int
    first_alias: AliasEvidence | None
    records: tuple[PortCycle, ...]


@dataclass(frozen=True)
class RecoveryCollision:
    visible_key: tuple[object, ...]
    obligations: tuple[tuple[int, int], ...]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def load_frozen_rule(
    mutation: str | None,
) -> tuple[dict[str, object], str, bool]:
    envelope = json.loads((repo_root() / SIDECAR).read_text(encoding="utf-8"))
    rule = json.loads(json.dumps(envelope["rule"]))
    if mutation == "rule_semantic_tamper":
        rule["semantic_binding"] = False
    digest = hashlib.sha256(canonical_json(rule).encode()).hexdigest()
    bound = digest == envelope["sha256"] == EXPECTED_RULE_SHA256
    return rule, digest, bound


def periodic_labelled_grid(
    width: int, open_boundary: bool = False, merge_parallel: bool = False
) -> tuple[tuple[int, ...], ...]:
    rows = []
    for y in range(width):
        for z in range(width):
            row = []
            seen: set[int] = set()
            for dy, dz in PORT_STEPS:
                next_y, next_z = y + dy, z + dz
                if open_boundary and not (
                    0 <= next_y < width and 0 <= next_z < width
                ):
                    target = -1
                else:
                    target = (next_y % width) * width + (next_z % width)
                if merge_parallel and target in seen:
                    target = -1
                elif target >= 0:
                    seen.add(target)
                row.append(target)
            rows.append(tuple(row))
    return tuple(rows)


def inverse_port(port: int, rule: dict[str, object]) -> int:
    ports = rule["ports"]
    return (port + int(ports["inverse_offset"])) % int(ports["count"])


def selected_ports(
    selector: str, actor: Cell, rule: dict[str, object]
) -> tuple[int, ...]:
    port_count = int(rule["ports"]["count"])
    if selector == "actor_direction":
        return (actor.direction,)
    if selector == "successor_direction":
        return (
            (actor.direction + int(rule["ports"]["successor_step"]))
            % port_count,
        )
    if selector == "each_port":
        return tuple(range(port_count))
    raise AssertionError(f"unknown frozen selector {selector}")


def bit_relation_holds(relation: str, actor: Cell, target: Cell) -> bool:
    if relation == "any":
        return True
    if relation == "same":
        return actor.bit == target.bit
    if relation == "opposite":
        return actor.bit in (0, 1) and target.bit == 1 - actor.bit
    raise AssertionError(f"unknown frozen bit relation {relation}")


def direction_relation_holds(
    relation: str,
    target: Cell,
    actor_index: int,
    target_index: int,
    selected_port: int,
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
) -> bool:
    if relation == "any":
        return True
    reverse = inverse_port(selected_port, rule)
    exact = (
        target.direction == reverse
        and target.direction in range(4)
        and grid[target_index][target.direction] == actor_index
    )
    if relation == "inverse_port":
        return exact
    if relation == "not_inverse_port":
        return not exact
    raise AssertionError(f"unknown frozen direction relation {relation}")


def resolve_write(
    template: dict[str, str],
    actor: Cell,
    target: Cell,
    current: Cell,
    selected_port: int,
    rule: dict[str, object],
) -> Cell:
    kind = current.kind if template["kind"] == "same" else template["kind"]
    bit = {
        "actor": actor.bit,
        "target": target.bit,
        "same": current.bit,
        "opposite_actor": 1 - actor.bit,
    }[template["bit"]]
    direction = {
        "same": current.direction,
        "none": -1,
        "selected_port": selected_port,
        "inverse_port": inverse_port(selected_port, rule),
    }[template["direction"]]
    return Cell(kind, bit, direction)


def enabled_actions(
    state: tuple[Cell, ...],
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
) -> tuple[LocalAction, ...]:
    candidates: dict[tuple[int, int], list[tuple[int, LocalAction]]] = defaultdict(list)
    for actor_index, actor in enumerate(state):
        for row in rule["transitions"]:
            if actor.kind not in row["actor_kinds"]:
                continue
            if row["support"] == "radius_two_star":
                reserved = set(row["reserved_kinds"])
                guard = not any(
                    state[target].kind in reserved for target in grid[actor_index]
                )
                if row["guard"] == "always":
                    guard = True
                if not guard:
                    continue
                output = resolve_write(
                    row["actor_write"], actor, actor, actor, -1, rule
                )
                action = LocalAction(
                    str(row["id"]), actor_index, -1, -1,
                    ((actor_index, output),),
                )
                candidates[(actor_index, -1)].append(
                    (int(row["priority"]), action)
                )
                continue
            for port in selected_ports(str(row["port_selector"]), actor, rule):
                if port not in range(4):
                    continue
                target_index = grid[actor_index][port]
                if target_index < 0:
                    continue
                target = state[target_index]
                if target.kind not in row["target_kinds"]:
                    continue
                if not bit_relation_holds(str(row["bit_relation"]), actor, target):
                    continue
                if not direction_relation_holds(
                    str(row["direction_relation"]), target, actor_index,
                    target_index, port, grid, rule
                ):
                    continue
                actor_output = resolve_write(
                    row["actor_write"], actor, target, actor, port, rule
                )
                target_output = resolve_write(
                    row["target_write"], actor, target, target, port, rule
                )
                action = LocalAction(
                    str(row["id"]), actor_index, port, target_index,
                    tuple(sorted(
                        ((actor_index, actor_output), (target_index, target_output))
                    )),
                )
                candidates[(actor_index, port)].append(
                    (int(row["priority"]), action)
                )
    winners: set[LocalAction] = set()
    for support, choices in candidates.items():
        priority = max(value for value, _ in choices)
        top = {action for value, action in choices if value == priority}
        if len(top) != 1:
            raise AssertionError(f"ambiguous frozen rows at {support}: {top}")
        winners.update(top)
    return tuple(sorted(winners))


def apply_action(
    state: tuple[Cell, ...], action: LocalAction
) -> tuple[Cell, ...]:
    result = list(state)
    for index, value in action.writes:
        result[index] = value
    return tuple(result)


def action_token(action: LocalAction) -> str:
    return f"{action.row_id}@{action.actor}:{action.port}->{action.target}"


def initial_two_root_state(
    word: int, roots: tuple[int, int], ports: tuple[int, int]
) -> tuple[Cell, ...]:
    state = [Cell("U", (word >> vertex) & 1) for vertex in range(4)]
    for root, port in zip(roots, ports, strict=True):
        state[root] = Cell("R", state[root].bit, port)
    return tuple(state)


def two_root_census(
    rule: dict[str, object], drop_one_record: bool
) -> ReachabilityCensus:
    grid = periodic_labelled_grid(2)
    same_starts = same_records = opposite_starts = opposite_records = 0
    maximum_reached = maximum_trace = 0
    first_start: tuple[int, tuple[int, int], tuple[int, int]] = ()
    first_trace: tuple[str, ...] = ()
    for word in range(1, 15):
        bits = tuple((word >> vertex) & 1 for vertex in range(4))
        for roots in itertools.combinations(range(4), 2):
            same = bits[roots[0]] == bits[roots[1]]
            for ports in itertools.product(range(4), repeat=2):
                if same:
                    same_starts += 1
                else:
                    opposite_starts += 1
                start = initial_two_root_state(word, roots, ports)
                queue = deque([start])
                parent: dict[
                    tuple[Cell, ...],
                    tuple[tuple[Cell, ...], str] | None,
                ] = {start: None}
                terminal: tuple[Cell, ...] | None = None
                while queue:
                    state = queue.popleft()
                    if any(site.kind in {"LOCK", "BG"} for site in state):
                        terminal = state
                        break
                    for action in enabled_actions(state, grid, rule):
                        successor = apply_action(state, action)
                        if successor not in parent:
                            parent[successor] = (state, action_token(action))
                            queue.append(successor)
                maximum_reached = max(maximum_reached, len(parent))
                if terminal is None:
                    continue
                if same:
                    same_records += 1
                else:
                    opposite_records += 1
                trace = []
                cursor = terminal
                while parent[cursor] is not None:
                    previous, token = parent[cursor]
                    trace.append(token)
                    cursor = previous
                trace.reverse()
                maximum_trace = max(maximum_trace, len(trace))
                if not first_trace:
                    first_start = (word, roots, ports)
                    first_trace = tuple(trace)
    if drop_one_record:
        same_records -= 1
    return ReachabilityCensus(
        same_starts,
        same_records,
        opposite_starts,
        opposite_records,
        maximum_reached,
        maximum_trace,
        first_start,
        first_trace,
    )


def stage_a_inverse(port: int, quarter_turn_inverse: bool) -> int:
    return (port + (1 if quarter_turn_inverse else 2)) % 4


def noninverse_root_contact(
    grid: tuple[tuple[int, ...], ...],
    root: int,
    endpoint: int,
    launch_port: int,
    collision_port: int,
    quarter_turn_inverse: bool,
) -> bool:
    if endpoint < 0 or grid[endpoint][collision_port] != root:
        return False
    exact_reverse = (
        launch_port == stage_a_inverse(collision_port, quarter_turn_inverse)
        and grid[root][launch_port] == endpoint
    )
    return not exact_reverse


def enumerate_port_cycles(
    width: int,
    open_boundary: bool,
    merge_parallel: bool,
    quarter_turn_inverse: bool,
) -> tuple[tuple[tuple[int, ...], ...], tuple[PortCycle, ...]]:
    grid = periodic_labelled_grid(width, open_boundary, merge_parallel)
    cycles: list[PortCycle] = []
    for root in range(width * width):
        for launch_port in range(4):
            child = grid[root][launch_port]
            if child < 0 or child == root:
                continue
            frontier = [((root, child), (launch_port,))]
            while frontier:
                path, edge_ports = frontier.pop()
                endpoint = path[-1]
                for collision_port in range(4):
                    if noninverse_root_contact(
                        grid, root, endpoint, launch_port, collision_port,
                        quarter_turn_inverse,
                    ):
                        cycles.append(
                            PortCycle(path, edge_ports, collision_port)
                        )
                if len(path) == width * width:
                    continue
                for port in range(3, -1, -1):
                    target = grid[endpoint][port]
                    if target < 0 or target in path:
                        continue
                    frontier.append(
                        (path + (target,), edge_ports + (port,))
                    )
    return grid, tuple(cycles)


def assess_cycle(
    width: int,
    grid: tuple[tuple[int, ...], ...],
    cycle: PortCycle,
    colours: int,
    endpoint_is_dart: bool,
    quarter_turn_inverse: bool,
) -> tuple[AliasEvidence, ...]:
    path = cycle.path
    root = path[0]
    anchor = path[-1]
    internal = path[1:-1]
    markers = {
        vertex: depth % colours
        for depth, vertex in enumerate(reversed(internal))
    }
    evidence: list[AliasEvidence] = []
    for index, site in enumerate(internal, start=1):
        expected_site = path[index + 1]
        expected_port = cycle.edge_ports[index]
        if expected_site == anchor:
            candidates = tuple(
                port for port, target in enumerate(grid[site])
                if target == anchor
            )
        else:
            expected_colour = markers[expected_site]
            candidates = tuple(
                port for port, target in enumerate(grid[site])
                if target >= 0 and markers.get(target) == expected_colour
            )
        candidate_sites = tuple(grid[site][port] for port in candidates)
        if endpoint_is_dart:
            valid = set(candidate_sites) == {expected_site}
        else:
            valid = candidates == (expected_port,)
        if not valid:
            reason = (
                "lost_parallel_child_dart"
                if len(set(candidate_sites)) <= 1
                else "next_colour_path_chord"
            )
            evidence.append(
                AliasEvidence(
                    width,
                    root,
                    cycle.edge_ports[0],
                    path,
                    cycle.edge_ports,
                    cycle.collision_port,
                    site,
                    expected_site,
                    expected_port,
                    candidates,
                    candidate_sites,
                    reason,
                )
            )
            break
    allowed_collision_ports = tuple(
        port for port in range(4)
        if noninverse_root_contact(
            grid,
            root,
            anchor,
            cycle.edge_ports[0],
            port,
            quarter_turn_inverse,
        )
    )
    if endpoint_is_dart:
        collision_valid = bool(allowed_collision_ports)
    else:
        collision_valid = allowed_collision_ports == (cycle.collision_port,)
    if not collision_valid:
        evidence.append(
            AliasEvidence(
                width,
                root,
                cycle.edge_ports[0],
                path,
                cycle.edge_ports,
                cycle.collision_port,
                anchor,
                root,
                cycle.collision_port,
                allowed_collision_ports,
                tuple(root for _ in allowed_collision_ports),
                "lost_collision_dart",
            )
        )
    return tuple(evidence)


def cycle_census(
    width: int,
    colours: int,
    open_boundary: bool,
    merge_parallel: bool,
    quarter_turn_inverse: bool,
    endpoint_is_dart: bool,
) -> CycleCensus:
    grid, records = enumerate_port_cycles(
        width, open_boundary, merge_parallel, quarter_turn_inverse
    )
    ambiguous = 0
    reasons = defaultdict(int)
    first_alias = None
    for cycle in records:
        evidence = assess_cycle(
            width,
            grid,
            cycle,
            colours,
            endpoint_is_dart,
            quarter_turn_inverse,
        )
        if not evidence:
            continue
        ambiguous += 1
        reasons[evidence[0].reason] += 1
        if first_alias is None:
            first_alias = evidence[0]
    return CycleCensus(
        len(records),
        ambiguous,
        reasons["lost_parallel_child_dart"],
        reasons["next_colour_path_chord"],
        reasons["lost_collision_dart"],
        first_alias,
        records,
    )


def recovery_collision_classes(
    width: int,
    cycles: tuple[PortCycle, ...],
    colours: int,
    quarter_turn_inverse: bool,
) -> tuple[RecoveryCollision, ...]:
    """Group histories by every datum visible to the frozen depth-only state."""
    obligations: dict[
        tuple[object, ...], set[tuple[int, int]]
    ] = defaultdict(set)
    for cycle in cycles:
        path = cycle.path
        internal = path[1:-1]
        markers = tuple(sorted(
            (vertex, depth % colours)
            for depth, vertex in enumerate(reversed(internal))
        ))
        for index, site in enumerate(internal, start=1):
            incoming_port = stage_a_inverse(
                cycle.edge_ports[index - 1], quarter_turn_inverse
            )
            visible_key = (
                width,
                path[0],
                cycle.edge_ports[0],
                path[-1],
                cycle.collision_port,
                markers,
                site,
                path[index - 1],
                incoming_port,
            )
            obligations[visible_key].add(
                (path[index + 1], cycle.edge_ports[index])
            )
    collisions = [
        RecoveryCollision(key, tuple(sorted(required)))
        for key, required in obligations.items()
        if len({port for _, port in required}) > 1
    ]
    return tuple(sorted(collisions, key=lambda item: repr(item.visible_key)))


def first_alias_dict(alias: AliasEvidence | None) -> dict[str, object] | None:
    if alias is None:
        return None
    return {
        "width": alias.width,
        "root": alias.root,
        "launch_port": alias.launch_port,
        "path": alias.path,
        "edge_ports": alias.edge_ports,
        "collision_port": alias.collision_port,
        "site": alias.site,
        "expected_site": alias.expected_site,
        "expected_port": alias.expected_port,
        "candidate_ports": alias.candidate_ports,
        "candidate_sites": alias.candidate_sites,
        "reason": alias.reason,
    }


def source_and_scope_checks(checks: Checks) -> None:
    paths = [repo_root() / path for path in AUDIT_INPUT_PATHS]
    exist = all(path.is_file() for path in paths)
    checks.check("independent Stage-A source packet is complete", exist)
    if not exist:
        return
    preregistration = paths[3].read_text(encoding="utf-8")
    boundary_note = paths[6].read_text(encoding="utf-8")
    discipline = paths[7].read_text(encoding="utf-8")
    checks.check(
        "preregistration fixes the depth-only five-colour 46+82 training gate",
        all(
            token in preregistration
            for token in (
                "46 named rays plus rank-82", "five as a cyclic zipper alphabet",
                "widths 2 and 3", "zero or more than one adjacent next-colour",
                "higher blocks", "No negative decision is a broad no-go",
            )
        ),
    )
    n1_routes = (
        "fixed five-colour onsite trail",
        "port-aware onsite recolouring",
        "radius-two paired onsite pattern",
        "higher-block oriented-edge carrier",
        "rollback-first coalescing forest",
        "coherent or continuous-time arbitration",
    )
    n1_ok = all(route in discipline for route in n1_routes)
    n2_ok = all(token in discipline for token in ("W_D", "W_C", "independent?", "yes"))
    n3_ok = "No hidden condition enlarges the exact claim" in discipline
    n4_ok = discipline.count("no; ") >= 2 and "dropped as proof of W_D" in discipline
    n5_ok = all(
        token in discipline
        for token in ("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:")
    )
    n6_ok = all(
        token in discipline
        for token in ("port-aware reuse", "two-site phase pattern", "rollback-first grammar")
    )
    n7_ok = (
        "The steelman succeeds" in discipline
        and "broad no-go is premature" in discipline
    )
    n8_ok = all(
        token in discipline
        for token in ("Block 220", "Block 218", "Block 219", "Block 212")
    )
    checks.check(
        "landed N1-N8 packet keeps five constructive families live and drops mismatched witnesses",
        n1_ok and n2_ok and n3_ok and n4_ok and n5_ok and n6_ok and n7_ok and n8_ok,
    )
    scope_ok = (
        "Broad one-site/finality gate status: FAIL" in discipline
        and "partial-narrowing" in discipline
        and "This is not a no-go for one-site time multiplexing" in boundary_note
        and "No axiom amendment" in boundary_note
        and "toe_percentage_movement: 0" in boundary_note
        and "obligation_retirement: 0" in boundary_note
    )
    checks.check(
        "source rhetoric is limited to the frozen mapping, not one-site finality or axioms",
        scope_ok,
    )


def frozen_semantics_ok(rule: dict[str, object]) -> bool:
    rows = {str(row["id"]): row for row in rule["transitions"]}
    required = {
        "root_launch_match",
        "root_launch_mismatch",
        "root_launch_record_or_malformed",
        "head_return_root_commit",
        "head_return_parent",
        "head_descend",
        "head_skip_root_cross_edge",
        "head_skip_parent_cross_edge",
        "head_skip_reserved_cross_edge",
        "head_fail_opposite_transient",
        "head_fail_opposite_reservation",
        "head_fail_record_eroder_or_malformed",
        "failure_spread",
        "failure_guarded_decay",
        "matching_record_flood",
    }
    return (
        rule["schema"] == "block220-event-seeded-record-finality-markov-v2"
        and rule["semantic_binding"] is True
        and rule["default_action"] == "identity"
        and rule["runtime_memory_fields"] == []
        and rule["ports"]
        == {
            "count": 4,
            "inverse_offset": 2,
            "successor_step": 1,
            "parallel_darts_are_distinct": True,
        }
        and required == set(rows)
        and rows["head_return_root_commit"]["direction_relation"]
        == "inverse_port"
        and rows["head_skip_root_cross_edge"]["direction_relation"]
        == "not_inverse_port"
        and rows["failure_guarded_decay"]["guard"]
        == "no_reserved_neighbor"
    )


def carrier_partition(rule: dict[str, object]) -> tuple[int, int, int]:
    signature = rule["kraus_schema"]["signature_partition"]
    old_named = int(signature["named_rays_per_normal"])
    old_x = int(signature["X_n_rank"])
    maps = rule["direction_encoding"]["context_port_maps"]
    inverse = rule["direction_encoding"]["physical_inverse"]
    available = 0
    for normal, tangent in enumerate(maps):
        normal_pair = {normal, int(inverse[normal])}
        if len(set(tangent)) != 4 or set(tangent) & normal_pair:
            return old_named, old_x, -1
        available += len(normal_pair) * 3 * 2
    # The same twelve physical rays are viewed in each transported normal context.
    reclaimed_per_context = available // 6
    return old_named + reclaimed_per_context, old_x - reclaimed_per_context, reclaimed_per_context


def mutation_suite() -> tuple[int, int]:
    rejected = 0
    runner = str(Path(__file__).resolve())
    for mutation in MUTATIONS:
        completed = subprocess.run(
            [sys.executable, runner, "--science-only", "--mutation", mutation],
            capture_output=True,
            text=True,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        if (
            completed.returncode == 1
            and "FAIL " in completed.stdout
            and "TOTAL: PASS=" in completed.stdout
            and "Traceback" not in completed.stderr
        ):
            rejected += 1
    print(f"MUTATIONS rejected={rejected}/{len(MUTATIONS)}")
    return rejected, len(MUTATIONS)


def run(
    mutation: str | None, science_only: bool, verbose: bool = True
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    rule, consumed_digest, digest_bound = load_frozen_rule(mutation)
    colours = 3 if mutation == "three_depth_colours" else 5
    open_boundary = mutation == "open_training_grid"
    merge_parallel = mutation == "merge_labelled_darts"
    quarter_turn_inverse = mutation == "quarter_turn_inverse"
    endpoint_is_dart = mutation == "endpoint_is_dart"

    checks.check(
        "independent consumer binds the canonical frozen Block220 sidecar digest",
        digest_bound,
        consumed_digest,
    )
    checks.check(
        "independent transition interpreter preserves the load-bearing frozen rows",
        frozen_semantics_ok(rule),
    )
    named, complement, reclaimed = carrier_partition(rule)
    checks.check(
        "six transported contexts independently give the frozen 46+82 partition",
        (named, complement, reclaimed) == (46, 82, 12),
        f"partition={named}+{complement} reclaimed={reclaimed}",
    )

    census = two_root_census(
        rule, mutation == "drop_one_false_record"
    )
    checks.check(
        "independent L4 census partitions all mixed two-root starts as 576 plus 768",
        (census.same_starts, census.opposite_starts) == (576, 768),
    )
    checks.check(
        "independent L4 reachability reproduces 96 same-bit and zero opposite-bit Records",
        (census.same_records, census.opposite_records) == (96, 0),
    )
    expected_trace = (
        "root_launch_match@1:0->3",
        "head_skip_root_cross_edge@3:3->2",
        "head_skip_root_cross_edge@3:0->1",
        "head_skip_root_cross_edge@3:1->2",
        "head_return_root_commit@3:2->1",
    )
    checks.check(
        "first false Record is the frozen five-action ownership trace",
        census.first_start == (1, (1, 2), (0, 0))
        and census.first_trace == expected_trace
        and census.maximum_reached == 51
        and census.maximum_shortest_record_trace == 5,
        f"start={census.first_start} trace={census.first_trace}",
    )

    width2 = cycle_census(
        2, colours, open_boundary, merge_parallel,
        quarter_turn_inverse, endpoint_is_dart,
    )
    width3 = cycle_census(
        3, colours, open_boundary, merge_parallel,
        quarter_turn_inverse, endpoint_is_dart,
    )
    checks.check(
        "all width-two port-labelled simple root-cross cycles give 144 total and 128 aliases",
        (width2.cycles, width2.ambiguous) == (144, 128),
    )
    checks.check(
        "all width-three port-labelled simple root-cross cycles give 4356 total and 1440 aliases",
        (width3.cycles, width3.ambiguous) == (4356, 1440),
    )
    first = width2.first_alias
    first_exact = (
        first is not None
        and first.path == (0, 2, 3, 1)
        and first.edge_ports == (0, 1, 0)
        and first.collision_port == 1
        and first.site == 2
        and first.expected_site == 3
        and first.expected_port == 1
        and first.candidate_ports == (1, 3)
        and first.candidate_sites == (3, 3)
        and first.reason == "lost_parallel_child_dart"
    )
    checks.check(
        "first alias retains the exact 0-2-3-1 path and lost physical ports 1 versus 3",
        first_exact,
        str(first_alias_dict(first)),
    )

    recovery = recovery_collision_classes(
        2, width2.records, colours, quarter_turn_inverse
    )
    first_recovery = recovery[0] if recovery else None
    expected_visible = (
        2, 0, 0, 1, 1, ((2, 1), (3, 0)), 2, 0, 2
    )
    checks.check(
        "full visible-state quotient has 96 histories that require incompatible restored darts",
        len(recovery) == 96
        and first_recovery is not None
        and first_recovery.visible_key == expected_visible
        and first_recovery.obligations == ((3, 1), (3, 3)),
        f"classes={len(recovery)} first={first_recovery}",
    )
    checks.check(
        "endpoint incoming dart root launch collision dart and complete marker layout do not recover the lost port",
        bool(recovery) and mutation != "permit_first_alias",
    )
    checks.check(
        "training grids preserve periodic wrap and all four labelled darts",
        not open_boundary and not merge_parallel,
    )
    checks.check(
        "frozen candidate uses exactly five depth colours without hidden epoch memory",
        colours == 5 and mutation != "inject_epoch_memory",
    )
    checks.check(
        "quarter-turn contact is not substituted for the frozen opposite dart",
        not quarter_turn_inverse,
    )
    checks.check(
        "an endpoint equality is not silently promoted to physical dart equality",
        not endpoint_is_dart,
    )
    checks.check(
        "scope remains partial narrowing and never promotes a broad one-site finality or axiom no-go",
        mutation != "promote_broad_no_go",
    )
    primary_mutation_names = {
        "four_colours", "accept_ambiguous", "omit_wrap", "dedup_parallel",
        "omit_reachable", "held_retune", "anchor_record",
        "commit_beside_anchor", "hidden_root_id", "extra_state",
    }
    checks.check(
        "independent hostile mutations are nonidentical to the Stage-A primary suite",
        not (set(MUTATIONS) & primary_mutation_names),
    )
    if not science_only and mutation is None:
        source_and_scope_checks(checks)

    data: dict[str, object] = {
        "verdict": "CLEAN" if checks.failed == 0 else "DEFECT",
        "classification": (
            "scoped-depth-only-five-colour-dart-alias"
            if checks.failed == 0
            else f"rejected-independent-mutation-{mutation or 'baseline'}"
        ),
        "sidecar_sha256": consumed_digest,
        "carrier_partition": [named, complement],
        "reclaimed_normal_rays": reclaimed,
        "block220_census": {
            "same_starts": census.same_starts,
            "same_records": census.same_records,
            "opposite_starts": census.opposite_starts,
            "opposite_records": census.opposite_records,
            "maximum_reached": census.maximum_reached,
            "maximum_shortest_record_trace": census.maximum_shortest_record_trace,
            "first_start": census.first_start,
            "first_trace": census.first_trace,
        },
        "width2": {
            "cycles": width2.cycles,
            "ambiguous": width2.ambiguous,
            "lost_parallel_dart": width2.lost_parallel_dart,
            "next_colour_chord": width2.next_colour_chord,
            "lost_collision_dart": width2.lost_collision_dart,
        },
        "width3": {
            "cycles": width3.cycles,
            "ambiguous": width3.ambiguous,
            "lost_parallel_dart": width3.lost_parallel_dart,
            "next_colour_chord": width3.next_colour_chord,
            "lost_collision_dart": width3.lost_collision_dart,
        },
        "first_alias": first_alias_dict(first),
        "visible_recovery_collision_classes": len(recovery),
        "first_recovery_obligations": (
            None if first_recovery is None else first_recovery.obligations
        ),
        "scope": "frozen-depth-only-mapping-partial-narrowing-only",
    }
    return checks, data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    checks, data = run(args.mutation, args.science_only)
    if args.self_test_mutations and args.mutation is None:
        rejected, total = mutation_suite()
        checks.check(
            "all nonidentical independent Stage-A mutations are rejected",
            rejected == total,
            f"{rejected}/{total}",
        )
    data["verdict"] = "CLEAN" if checks.failed == 0 else "DEFECT"
    print("DATA " + canonical_json(data))
    print(
        "per_element: checked the 12 reclaimed normal-direction rays, fixed "
        "anchor/five-colour roles, and resulting 46+82 partition."
    )
    print(
        "per_site: checked the complete visible depth-marker neighbourhood, "
        "incoming restoration dart, and incompatible ports 1 versus 3."
    )
    print(
        "per_mode: checked all 576 same-bit and 768 opposite-bit L4 starts, "
        "periodic parallel darts, inverse labels, and recovery attacks."
    )
    print(
        "per_block: checked every 144 width-two and 4,356 width-three simple "
        "port-labelled root-cross cycle and each restoration signature."
    )
    print(
        "lattice_wide: checked and not executed — the frozen depth-only map "
        "fails a training block; other one-site and higher-block routes remain live."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
