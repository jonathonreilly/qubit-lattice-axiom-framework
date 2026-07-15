#!/usr/bin/env python3
"""Executable certificate for the NN topological causal-bound note.

This runner checks the finite graph dependency-support recurrence used in
docs/LATTICE_NN_LIGHT_CONE_NOTE.md. It intentionally checks only graph
reachability, not a physical spacetime light cone or distance law.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable


Vertex = int
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class GraphCase:
    name: str
    vertex_count: int
    edges: tuple[Edge, ...]
    horizon: int
    include_self_edges: bool


def require(condition: bool, *context: object) -> None:
    """Raise on a failed certificate check even when Python uses -O."""
    if not condition:
        raise AssertionError(context)


def dependency_edges(case: GraphCase) -> tuple[Edge, ...]:
    edges = set(case.edges)
    if case.include_self_edges:
        edges.update((v, v) for v in range(case.vertex_count))
    return tuple(sorted(edges))


def predecessors(vertex_count: int, edges: Iterable[Edge]) -> list[set[Vertex]]:
    pred = [set() for _ in range(vertex_count)]
    for u, v in edges:
        pred[v].add(u)
    return pred


def successors(vertex_count: int, edges: Iterable[Edge]) -> list[set[Vertex]]:
    succ = [set() for _ in range(vertex_count)]
    for u, v in edges:
        succ[u].add(v)
    return succ


def dependency_supports(
    vertex_count: int, pred: list[set[Vertex]], horizon: int
) -> list[list[set[Vertex]]]:
    """deps[t][v] is the set of initial vertices that can affect v at tick t."""
    deps = [[{v} for v in range(vertex_count)]]
    for _ in range(horizon):
        previous = deps[-1]
        current = []
        for v in range(vertex_count):
            support = set()
            for u in pred[v]:
                support.update(previous[u])
            current.append(support)
        deps.append(current)
    return deps


def forward_reachability(
    succ: list[set[Vertex]], sources: frozenset[Vertex], horizon: int
) -> list[set[Vertex]]:
    reached_by_tick = [set(sources)]
    frontier = set(sources)
    reached = set(sources)
    for _ in range(horizon):
        next_frontier = set()
        for u in frontier:
            next_frontier.update(succ[u])
        reached.update(next_frontier)
        reached_by_tick.append(set(reached))
        frontier = next_frontier
    return reached_by_tick


def tested_source_sets(vertex_count: int) -> tuple[frozenset[Vertex], ...]:
    """Singleton coverage plus deterministic empty and multi-source cases."""
    if vertex_count == 0:
        return (frozenset(),)
    candidates = [frozenset()]
    candidates.extend(frozenset({source}) for source in range(vertex_count))
    candidates.extend(
        (
            frozenset(range(0, vertex_count, 2)),
            frozenset(range(1, vertex_count, 2)),
            frozenset({0, vertex_count - 1}),
            frozenset(range(vertex_count)),
        )
    )
    return tuple(dict.fromkeys(candidates))


def check_case(case: GraphCase) -> tuple[int, int]:
    edges = dependency_edges(case)
    pred = predecessors(case.vertex_count, edges)
    succ = successors(case.vertex_count, edges)
    deps = dependency_supports(case.vertex_count, pred, case.horizon)

    checks = 0
    for sources in tested_source_sets(case.vertex_count):
        reachable = forward_reachability(succ, sources, case.horizon)
        previous_affected: set[Vertex] | None = None
        for tick in range(case.horizon + 1):
            affected = {
                vertex
                for vertex in range(case.vertex_count)
                if deps[tick][vertex] & sources
            }
            require(
                affected <= reachable[tick],
                case.name,
                sorted(sources),
                tick,
                sorted(affected),
                sorted(reachable[tick]),
            )
            outside = set(range(case.vertex_count)) - reachable[tick]
            require(
                all(not (deps[tick][v] & sources) for v in outside),
                case.name,
                sorted(sources),
                tick,
                sorted(outside),
            )
            checks += 2
            if previous_affected is not None:
                one_step_support = {
                    vertex
                    for source in previous_affected
                    for vertex in succ[source]
                }
                require(
                    affected == one_step_support,
                    case.name,
                    sorted(sources),
                    tick,
                    sorted(affected),
                    sorted(one_step_support),
                )
                checks += 1
            if case.include_self_edges:
                require(
                    affected == reachable[tick],
                    case.name,
                    sorted(sources),
                    tick,
                    sorted(affected),
                    sorted(reachable[tick]),
                )
                checks += 1
            previous_affected = affected
    return len(edges), checks


def truth_table_output(table_mask: int, inputs: tuple[bool, ...]) -> bool:
    input_index = sum(int(bit) << index for index, bit in enumerate(inputs))
    return bool(table_mask & (1 << input_index))


def check_realized_difference_lemma(
    max_predecessors: int = 3,
) -> tuple[int, int, tuple[int, ...]]:
    """Check the one-step lemma and complete Boolean-function coverage."""
    cases = 0
    output_difference_cases = 0
    distinct_signature_counts = []
    for predecessor_count in range(max_predecessors + 1):
        input_tuples = tuple(product((False, True), repeat=predecessor_count))
        signatures = set()
        for table_mask in range(1 << len(input_tuples)):
            signature = tuple(
                truth_table_output(table_mask, inputs) for inputs in input_tuples
            )
            reconstructed_mask = sum(
                int(output)
                << sum(int(bit) << index for index, bit in enumerate(inputs))
                for inputs, output in zip(input_tuples, signature)
            )
            require(
                reconstructed_mask == table_mask,
                predecessor_count,
                table_mask,
                signature,
            )
            signatures.add(signature)
            for left_inputs in input_tuples:
                for right_inputs in input_tuples:
                    left_output = truth_table_output(table_mask, left_inputs)
                    right_output = truth_table_output(table_mask, right_inputs)
                    differing_inputs = {
                        index
                        for index, (left, right) in enumerate(
                            zip(left_inputs, right_inputs)
                        )
                        if left != right
                    }
                    require(
                        left_output == right_output or bool(differing_inputs),
                        predecessor_count,
                        table_mask,
                        left_inputs,
                        right_inputs,
                    )
                    output_difference_cases += int(left_output != right_output)
                    cases += 1
        expected_signature_count = 1 << len(input_tuples)
        require(
            len(signatures) == expected_signature_count,
            predecessor_count,
            len(signatures),
            expected_signature_count,
        )
        distinct_signature_counts.append(len(signatures))
    return cases, output_difference_cases, tuple(distinct_signature_counts)


def boolean_update(
    state: tuple[bool, ...],
    ordered_predecessors: tuple[tuple[Vertex, ...], ...],
    table_masks: tuple[int, ...],
) -> tuple[bool, ...]:
    return tuple(
        truth_table_output(
            table_mask,
            tuple(state[u] for u in predecessor_vertices),
        )
        for predecessor_vertices, table_mask in zip(
            ordered_predecessors, table_masks
        )
    )


def check_realized_history_bound(horizon: int = 3) -> tuple[int, int]:
    """Exhaustively instantiate two small multi-tick Boolean update systems."""
    graph_edges = (
        ((0, 1),),
        ((0, 0), (0, 1), (1, 1)),
    )
    configurations = tuple(product((False, True), repeat=2))
    checks = 0
    for edges in graph_edges:
        pred = predecessors(2, edges)
        succ = successors(2, edges)
        ordered_pred = tuple(tuple(sorted(vertices)) for vertices in pred)
        table_mask_ranges = tuple(
            range(1 << (1 << len(vertices))) for vertices in ordered_pred
        )
        for table_masks in product(*table_mask_ranges):
            for left_initial in configurations:
                for right_initial in configurations:
                    sources = frozenset(
                        vertex
                        for vertex, (left, right) in enumerate(
                            zip(left_initial, right_initial)
                        )
                        if left != right
                    )
                    reachable = forward_reachability(succ, sources, horizon)
                    left_state = left_initial
                    right_state = right_initial
                    for tick in range(horizon + 1):
                        realized_differences = {
                            vertex
                            for vertex, (left, right) in enumerate(
                                zip(left_state, right_state)
                            )
                            if left != right
                        }
                        require(
                            realized_differences <= reachable[tick],
                            edges,
                            table_masks,
                            left_initial,
                            right_initial,
                            tick,
                            sorted(realized_differences),
                            sorted(reachable[tick]),
                        )
                        checks += 1
                        if tick < horizon:
                            left_state = boolean_update(
                                left_state, ordered_pred, table_masks
                            )
                            right_state = boolean_update(
                                right_state, ordered_pred, table_masks
                            )
    return len(graph_edges), checks


def line_case(length: int, horizon: int) -> GraphCase:
    edges = []
    for i in range(length - 1):
        edges.append((i, i + 1))
        edges.append((i + 1, i))
    return GraphCase("undirected_nn_line", length, tuple(edges), horizon, True)


def grid_case(width: int, height: int, horizon: int) -> GraphCase:
    def idx(x: int, y: int) -> int:
        return y * width + x

    edges = []
    for y in range(height):
        for x in range(width):
            if x + 1 < width:
                edges.append((idx(x, y), idx(x + 1, y)))
                edges.append((idx(x + 1, y), idx(x, y)))
            if y + 1 < height:
                edges.append((idx(x, y), idx(x, y + 1)))
                edges.append((idx(x, y + 1), idx(x, y)))
    return GraphCase(
        "undirected_nn_grid", width * height, tuple(edges), horizon, True
    )


def branching_dag_case() -> GraphCase:
    edges = (
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 5),
        (5, 6),
        (3, 7),
    )
    return GraphCase("branching_dag", 8, edges, 5, False)


def layered_dag_case() -> GraphCase:
    layers = [range(0, 2), range(2, 5), range(5, 9), range(9, 12)]
    edges = []
    for left_layer, right_layer in zip(layers, layers[1:]):
        for u in left_layer:
            for v in right_layer:
                if (u + 2 * v) % 3 != 1:
                    edges.append((u, v))
    return GraphCase("layered_dag", 12, tuple(edges), 4, False)


def main() -> None:
    cases = (
        line_case(length=9, horizon=5),
        grid_case(width=5, height=4, horizon=4),
        branching_dag_case(),
        layered_dag_case(),
    )

    total_checks = 0
    (
        realized_cases,
        output_difference_cases,
        signature_counts,
    ) = check_realized_difference_lemma()
    history_graphs, history_checks = check_realized_history_bound()
    print("NN topological causal-bound certificate")
    print("claim: finite graph/DAG forward reachability for source sets")
    print()

    print(
        "PASS realized_difference_one_step: max_predecessors=3 "
        f"boolean_cases={realized_cases} "
        f"output_difference_cases={output_difference_cases} "
        f"signatures={','.join(map(str, signature_counts))}"
    )
    print(
        "PASS realized_history_multitick: "
        f"graphs={history_graphs} horizon=3 assertions={history_checks}"
    )

    for case in cases:
        edge_count, checks = check_case(case)
        total_checks += checks
        print(
            f"PASS {case.name}: vertices={case.vertex_count} "
            f"dependency_edges={edge_count} horizon={case.horizon} "
            f"mode={'exact' if case.include_self_edges else 'bound'} "
            f"source_sets={len(tested_source_sets(case.vertex_count))} "
            f"assertions={checks}"
        )

    print()
    print(
        f"TOTAL PASS: {len(cases)} graph families, {total_checks} support "
        f"assertions, {realized_cases} realized-difference cases, "
        f"{history_checks} realized-history assertions"
    )
    print("NON-CLAIMS:")
    print("  - no emergent relativity check")
    print("  - no Lorentz-invariance check")
    print("  - no physical-spacetime light-cone check")
    print("  - no universal-speed-law check")
    print("  - no causal-field distance-law check")
    print("  - no mass-response or Newtonian falloff check")


if __name__ == "__main__":
    main()
