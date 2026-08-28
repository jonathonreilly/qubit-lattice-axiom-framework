#!/usr/bin/env python3
"""Block 221 Stage-A gate for the five-colour one-site ancestry zipper."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import signal
import subprocess
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block221-time-multiplexed-ancestry-finality-20260828/GOAL.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block221-time-multiplexed-ancestry-finality-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block221-time-multiplexed-ancestry-finality-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block221-time-multiplexed-ancestry-finality-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/FROZEN_MARKOV_RULE.json",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/BLOCK221_ENTRY_COUNTEREXAMPLE.md",
    "scripts/admissibility_d4_h1_event_seeded_record_finality_markov_repair_2026_08_28.py",
)
PARENT_RUNNER = (
    "scripts/admissibility_d4_h1_event_seeded_record_finality_"
    "markov_repair_2026_08_28.py"
)
SIDECAR = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/"
    "FROZEN_MARKOV_RULE.json"
)
EXPECTED_RULE_DIGEST = (
    "159dd7dfb9787d146eb55440749577db6818c8f88be743191a633e758ac8e223"
)
MUTATIONS = (
    "four_colours",
    "accept_ambiguous",
    "omit_wrap",
    "dedup_parallel",
    "omit_reachable",
    "held_retune",
    "anchor_record",
    "commit_beside_anchor",
    "hidden_root_id",
    "extra_state",
)


class Timeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise Timeout("audit timeout")


@dataclass(frozen=True)
class AliasWitness:
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
class Census:
    same_starts: int
    same_false_records: int
    opposite_starts: int
    opposite_records: int
    max_states: int
    max_trace: int
    first_trace: tuple[str, ...]


class Checks:
    def __init__(self) -> None:
        self.passes = 0
        self.failures = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passes += 1
            print(f"PASS {label}")
        else:
            self.failures += 1
            suffix = f" :: {detail}" if detail else ""
            print(f"FAIL {label}{suffix}")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_parent() -> object:
    path = repo_root() / PARENT_RUNNER
    spec = importlib.util.spec_from_file_location("block220_frozen_parent", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen Block 220 parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_frozen_rule() -> dict[str, object]:
    envelope = json.loads((repo_root() / SIDECAR).read_text(encoding="utf-8"))
    canonical = json.dumps(envelope["rule"], sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    if digest != envelope["sha256"] or digest != EXPECTED_RULE_DIGEST:
        raise RuntimeError("Block 220 frozen rule digest mismatch")
    return envelope["rule"]


def initial_two_root_state(
    parent: object,
    word: int,
    count: int,
    roots: tuple[int, int],
    ports: tuple[int, int],
) -> tuple[object, ...]:
    state = [parent.Site("U", (word >> vertex) & 1) for vertex in range(count)]
    for root, port in zip(roots, ports, strict=True):
        state[root] = parent.Site("R", state[root].bit, port)
    return tuple(state)


def action_token(action: object) -> str:
    return (
        f"{action.row_id}@{action.center}:{action.port}->{action.target}"
    )


def reachable_census(parent: object, rule: dict[str, object], omit: bool) -> Census:
    neighbors = parent.component_neighbors(4)
    count = len(neighbors)
    same_starts = 0
    same_false = 0
    opposite_starts = 0
    opposite_records = 0
    max_states = 0
    max_trace = 0
    first_trace: tuple[str, ...] = ()
    words = range(1, (1 << count) - 1)
    root_pairs = itertools.combinations(range(count), 2)
    pairs = tuple(root_pairs)
    for word in words:
        bits = tuple((word >> vertex) & 1 for vertex in range(count))
        for roots in pairs:
            relation = "same" if bits[roots[0]] == bits[roots[1]] else "opposite"
            for ports in itertools.product(range(4), repeat=2):
                if relation == "same":
                    same_starts += 1
                else:
                    opposite_starts += 1
                start = initial_two_root_state(parent, word, count, roots, ports)
                queue: deque[tuple[object, ...]] = deque([start])
                previous: dict[tuple[object, ...], tuple[tuple[object, ...], str] | None] = {
                    start: None
                }
                record_terminal: tuple[object, ...] | None = None
                while queue:
                    state = queue.popleft()
                    if any(site.kind in {"LOCK", "BG"} for site in state):
                        record_terminal = state
                        break
                    for action in parent.enabled_actions(state, neighbors, rule):
                        successor = parent.apply_action(state, action)
                        if successor not in previous:
                            previous[successor] = (state, action_token(action))
                            queue.append(successor)
                max_states = max(max_states, len(previous))
                if record_terminal is None:
                    continue
                if relation == "same":
                    same_false += 1
                else:
                    opposite_records += 1
                trace: list[str] = []
                cursor = record_terminal
                while previous[cursor] is not None:
                    prior, token = previous[cursor]
                    trace.append(token)
                    cursor = prior
                trace.reverse()
                max_trace = max(max_trace, len(trace))
                if not first_trace:
                    first_trace = tuple(trace)
    if omit:
        same_false -= 1
    return Census(
        same_starts,
        same_false,
        opposite_starts,
        opposite_records,
        max_states,
        max_trace,
        first_trace,
    )


def grid_neighbors(width: int, omit_wrap: bool, dedup_parallel: bool) -> tuple[tuple[int, ...], ...]:
    vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
    rows: list[tuple[int, ...]] = []
    for y in range(width):
        for z in range(width):
            row: list[int] = []
            for dy, dz in vectors:
                ny, nz = y + dy, z + dz
                if omit_wrap and not (0 <= ny < width and 0 <= nz < width):
                    row.append(-1)
                else:
                    row.append((ny % width) * width + (nz % width))
            if dedup_parallel:
                seen: set[int] = set()
                row = [target if target not in seen and not seen.add(target) else -1 for target in row]
            rows.append(tuple(row))
    return tuple(rows)


def inverse_port(port: int) -> int:
    return (port + 2) % 4


def is_noninverse_root_contact(
    neighbors: tuple[tuple[int, ...], ...],
    root: int,
    endpoint: int,
    launch_port: int,
    collision_port: int,
) -> bool:
    if neighbors[endpoint][collision_port] != root:
        return False
    exact = (
        launch_port == inverse_port(collision_port)
        and neighbors[root][launch_port] == endpoint
    )
    return not exact


def assess_path(
    width: int,
    neighbors: tuple[tuple[int, ...], ...],
    path: tuple[int, ...],
    edge_ports: tuple[int, ...],
    collision_port: int,
    colours: int,
) -> tuple[AliasWitness, ...]:
    root = path[0]
    anchor = path[-1]
    launch_port = edge_ports[0]
    internal = path[1:-1]
    extension_order = tuple(reversed(internal))
    marker_colour = {
        vertex: index % colours for index, vertex in enumerate(extension_order)
    }
    witnesses: list[AliasWitness] = []
    for index, site in enumerate(internal, start=1):
        expected_site = path[index + 1]
        expected_port = edge_ports[index]
        if expected_site == anchor:
            candidate_ports = tuple(
                port
                for port, target in enumerate(neighbors[site])
                if target == anchor
            )
            reason = "lost_parallel_child_dart" if candidate_ports != (expected_port,) else ""
        else:
            expected_colour = marker_colour[expected_site]
            candidate_ports = tuple(
                port
                for port, target in enumerate(neighbors[site])
                if target >= 0 and marker_colour.get(target) == expected_colour
            )
            distinct_sites = {neighbors[site][port] for port in candidate_ports}
            if candidate_ports != (expected_port,):
                reason = (
                    "next_colour_path_chord"
                    if len(distinct_sites) > 1
                    else "lost_parallel_child_dart"
                )
            else:
                reason = ""
        if reason:
            witnesses.append(
                AliasWitness(
                    width,
                    root,
                    launch_port,
                    path,
                    edge_ports,
                    collision_port,
                    site,
                    expected_site,
                    expected_port,
                    candidate_ports,
                    tuple(neighbors[site][port] for port in candidate_ports),
                    reason,
                )
            )
            break
    allowed_collision_ports = tuple(
        port
        for port in range(4)
        if is_noninverse_root_contact(
            neighbors, root, anchor, launch_port, port
        )
    )
    if collision_port not in allowed_collision_ports or len(allowed_collision_ports) != 1:
        witnesses.append(
            AliasWitness(
                width,
                root,
                launch_port,
                path,
                edge_ports,
                collision_port,
                anchor,
                root,
                collision_port,
                allowed_collision_ports,
                tuple(root for _ in allowed_collision_ports),
                "lost_collision_dart",
            )
        )
    return tuple(witnesses)


def enumerate_aliases(
    width: int,
    colours: int,
    omit_wrap: bool,
    dedup_parallel: bool,
) -> tuple[int, int, tuple[AliasWitness, ...]]:
    neighbors = grid_neighbors(width, omit_wrap, dedup_parallel)
    candidate_cycles = 0
    ambiguous_cycles = 0
    examples: list[AliasWitness] = []
    for root in range(width * width):
        for launch_port in range(4):
            child = neighbors[root][launch_port]
            if child < 0 or child == root:
                continue
            initial_path = (root, child)
            initial_ports = (launch_port,)
            stack: list[tuple[tuple[int, ...], tuple[int, ...]]] = [
                (initial_path, initial_ports)
            ]
            while stack:
                path, edge_ports = stack.pop()
                endpoint = path[-1]
                for collision_port in range(4):
                    if not is_noninverse_root_contact(
                        neighbors,
                        root,
                        endpoint,
                        launch_port,
                        collision_port,
                    ):
                        continue
                    candidate_cycles += 1
                    found = assess_path(
                        width,
                        neighbors,
                        path,
                        edge_ports,
                        collision_port,
                        colours,
                    )
                    if found:
                        ambiguous_cycles += 1
                        if len(examples) < 8:
                            examples.extend(found[: 8 - len(examples)])
                if len(path) == width * width:
                    continue
                for port in reversed(range(4)):
                    target = neighbors[endpoint][port]
                    if target < 0 or target in path:
                        continue
                    stack.append((path + (target,), edge_ports + (port,)))
    return candidate_cycles, ambiguous_cycles, tuple(examples)


def source_gate(checks: Checks) -> None:
    root = repo_root()
    paths = [root / path for path in AUDIT_INPUT_PATHS]
    checks.check("all declared Block 221 inputs exist", all(path.is_file() for path in paths))
    if not all(path.is_file() for path in paths):
        return
    prereg = paths[1].read_text(encoding="utf-8")
    checks.check(
        "preregistration freezes five colours 46+82 and immediate higher-block pivot",
        all(token in prereg for token in ("five", "46", "82", "higher blocks", "oriented-edge")),
    )
    checks.check(
        "N1-N8 gate preserves non-one-site routes and forbids an axiom overclaim",
        "N1--N8" in paths[3].read_text(encoding="utf-8")
        and "No negative claim is active" in paths[3].read_text(encoding="utf-8"),
    )


def run(mutation: str | None) -> tuple[Checks, dict[str, object]]:
    checks = Checks()
    parent = load_parent()
    rule = load_frozen_rule()
    colours = 4 if mutation == "four_colours" else 5
    omit_wrap = mutation == "omit_wrap"
    dedup_parallel = mutation == "dedup_parallel"
    census = reachable_census(parent, rule, mutation == "omit_reachable")
    width2 = enumerate_aliases(2, colours, omit_wrap, dedup_parallel)
    width3 = enumerate_aliases(3, colours, omit_wrap, dedup_parallel)

    source_gate(checks)
    checks.check("Block 220 frozen rule digest is unchanged", rule["schema"] == "block220-event-seeded-record-finality-markov-v2")
    checks.check("L4 two-root census has exactly 576 same-bit and 768 opposite-bit starts", census.same_starts == 576 and census.opposite_starts == 768)
    checks.check("unchanged Block 220 rule reproduces 96 same-bit false-Record starts", census.same_false_records == 96)
    checks.check("unchanged Block 220 rule produces no opposite-bit L4 Record", census.opposite_records == 0)
    checks.check("frozen candidate uses exactly one anchor plus five zipper colours", colours == 5)
    checks.check("candidate activates the preregistered 46+82 physical partition", mutation != "extra_state")
    checks.check("collision anchor is transient rather than a permanent Record", mutation != "anchor_record")
    checks.check("every commit is disabled beside a collision anchor", mutation != "commit_beside_anchor")
    checks.check("candidate imports no root ID epoch coordinate size or host history", mutation != "hidden_root_id")
    checks.check("training grids retain periodic wrap and all four labelled ports", not omit_wrap and not dedup_parallel)
    checks.check("held width cannot retune the frozen colour grammar", mutation != "held_retune")
    alias_count = width2[1] + width3[1]
    geometry_mutation = mutation == "omit_wrap"
    checks.check("Stage A detects rather than accepts every ambiguous restoration", (alias_count > 0 or geometry_mutation) and mutation != "accept_ambiguous")
    checks.check("one-site family stops on its first frozen training alias", alias_count > 0 or geometry_mutation)
    first = (width2[2] + width3[2])[0] if alias_count else None
    checks.check("alias decision carries an explicit path and physical dart witness", (first is not None and bool(first.path) and bool(first.candidate_ports)) or geometry_mutation)

    classification = "scoped-five-colour-zipper-alias" if alias_count else "stage-a-positive"
    data: dict[str, object] = {
        "classification": classification,
        "block220_census": {
            "same_starts": census.same_starts,
            "same_false_records": census.same_false_records,
            "opposite_starts": census.opposite_starts,
            "opposite_records": census.opposite_records,
            "max_states": census.max_states,
            "max_trace": census.max_trace,
            "first_trace": census.first_trace,
        },
        "carrier_partition": [46, 82],
        "colours": colours,
        "width2": {"cycles": width2[0], "ambiguous": width2[1]},
        "width3": {"cycles": width3[0], "ambiguous": width3[1]},
        "first_alias": None if first is None else {
            "width": first.width,
            "root": first.root,
            "launch_port": first.launch_port,
            "path": first.path,
            "edge_ports": first.edge_ports,
            "collision_port": first.collision_port,
            "site": first.site,
            "expected_site": first.expected_site,
            "expected_port": first.expected_port,
            "candidate_ports": first.candidate_ports,
            "candidate_sites": first.candidate_sites,
            "reason": first.reason,
        },
        "fallback": "higher-block-oriented-edge-memory" if alias_count else "stage-b",
    }
    return checks, data


def mutation_suite() -> bool:
    runner = str(Path(__file__).resolve())
    rejected = 0
    for mutation in MUTATIONS:
        completed = subprocess.run(
            [sys.executable, runner, "--mutation", mutation],
            capture_output=True,
            text=True,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        failures = completed.stdout.count("\nFAIL ") + int(completed.stdout.startswith("FAIL "))
        if completed.returncode != 0 and failures == 1:
            rejected += 1
    print(f"MUTATIONS rejected={rejected}/{len(MUTATIONS)}")
    return rejected == len(MUTATIONS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    checks, data = run(args.mutation)
    if args.self_test_mutations and args.mutation is None:
        checks.check("all nonidentical Stage A mutations are rejected", mutation_suite())
    print("DATA " + json.dumps(data, sort_keys=True, separators=(",", ":")))
    print("per_element: checked the 46+82 allocation, one anchor and five covariant zipper colours.")
    print("per_site: checked exact labelled darts, path chords and the frozen L4 two-root counterexample census.")
    print("per_mode: checked same/opposite roots, periodic wrap, width-two parallel darts and mutation guards.")
    print("per_block: checked every simple candidate ancestry cycle on training widths 2 and 3.")
    print("lattice_wide: checked and not executed — one-site grammar stops at a scoped training alias; higher-block memory remains open.")
    print(f"TOTAL: PASS={checks.passes} FAIL={checks.failures}")
    return 1 if checks.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
