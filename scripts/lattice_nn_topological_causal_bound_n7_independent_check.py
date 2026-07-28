#!/usr/bin/env python3
"""Independent shared-map steelman for the causal-bound theorem.

This helper deliberately does not import the primary certificate.  It builds a
universal adversarial transition closure for Boolean local maps on a
three-vertex chain.  At each tick it permits every output pair compatible with
one shared local truth table, so the resulting state-pair set overapproximates
every time-dependent shared-map schedule without sampling schedules.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


State = tuple[bool, bool, bool]
StatePair = tuple[State, State]
HORIZON = 3
WALL = "outside-reachability influence under shared extensional R-local updates"
PREDECESSOR_LISTS = ((0,), (0, 1), (1, 2))


@dataclass(frozen=True)
class SteelmanEvidence:
    initial_pairs_checked: int
    tick_state_pairs_checked: int
    successor_pairs_generated: int
    resolved: bool


def possible_shared_outputs(
    left_inputs: tuple[bool, ...],
    right_inputs: tuple[bool, ...],
) -> tuple[tuple[bool, bool], ...]:
    """All output pairs allowed by one truth table on the two input tuples."""
    if left_inputs == right_inputs:
        return ((False, False), (True, True))
    return tuple(product((False, True), repeat=2))


def adversarial_successors(left_state: State, right_state: State) -> set[StatePair]:
    """Enumerate all next pairs under arbitrary shared local truth tables."""
    output_options = []
    for predecessors in PREDECESSOR_LISTS:
        left_inputs = tuple(left_state[source] for source in predecessors)
        right_inputs = tuple(right_state[source] for source in predecessors)
        output_options.append(possible_shared_outputs(left_inputs, right_inputs))
    return {
        (
            tuple(outputs[0] for outputs in per_vertex),  # type: ignore[misc]
            tuple(outputs[1] for outputs in per_vertex),  # type: ignore[misc]
        )
        for per_vertex in product(*output_options)
    }


def cumulative_reachability(sources: frozenset[int]) -> list[set[int]]:
    successors = ({0, 1}, {1, 2}, {2})
    reached = set(sources)
    by_tick = [set(reached)]
    for _ in range(HORIZON):
        reached.update(
            vertex
            for source in tuple(reached)
            for vertex in successors[source]
        )
        by_tick.append(set(reached))
    return by_tick


def compute_steelman_evidence() -> SteelmanEvidence:
    """Exhaust every pair transition allowed by pathwise-shared local maps."""
    configurations = tuple(product((False, True), repeat=3))
    initial_pairs = 0
    tick_state_pairs = 0
    successor_pairs = 0
    resolved = True
    for left_initial in configurations:
        for right_initial in configurations:
            initial_pairs += 1
            sources = frozenset(
                vertex
                for vertex, (left, right) in enumerate(
                    zip(left_initial, right_initial)
                )
                if left != right
            )
            reachable = cumulative_reachability(sources)
            state_pairs: set[StatePair] = {(left_initial, right_initial)}
            for tick in range(HORIZON + 1):
                for left_state, right_state in state_pairs:
                    differences = {
                        vertex
                        for vertex, (left, right) in enumerate(
                            zip(left_state, right_state)
                        )
                        if left != right
                    }
                    tick_state_pairs += 1
                    resolved = resolved and differences <= reachable[tick]
                if tick < HORIZON:
                    next_pairs: set[StatePair] = set()
                    for left_state, right_state in state_pairs:
                        successors = adversarial_successors(
                            left_state, right_state
                        )
                        successor_pairs += len(successors)
                        next_pairs.update(successors)
                    state_pairs = next_pairs
    return SteelmanEvidence(
        initial_pairs_checked=initial_pairs,
        tick_state_pairs_checked=tick_state_pairs,
        successor_pairs_generated=successor_pairs,
        resolved=resolved,
    )


def steelman_resolution_line(evidence: SteelmanEvidence) -> str:
    return (
        f"N7_STEELMAN_RESOLUTION {WALL} wall resolved independently: "
        "an exhaustive adversarial Boolean transition closure covered "
        f"{evidence.initial_pairs_checked} initial pairs, "
        f"{evidence.tick_state_pairs_checked} reachable state-pair checks, and "
        f"{evidence.successor_pairs_generated} locally shared-map successor "
        "choices; equal predecessor tuples were restricted to equal outputs, "
        "different tuples allowed all four output pairs, and every resulting "
        "state pair obeyed D_t subset C_t(S)."
    )


def main() -> int:
    evidence = compute_steelman_evidence()
    status = "PASS" if evidence.resolved else "FAIL"
    print("NN CAUSAL BOUND N7 -- INDEPENDENT TIME-DEPENDENT MAP MODE")
    print(
        f"[{status}] universal shared-map steelman: "
        f"initial_pairs={evidence.initial_pairs_checked} "
        f"tick_state_pairs={evidence.tick_state_pairs_checked} "
        f"successor_pairs={evidence.successor_pairs_generated}"
    )
    if evidence.resolved:
        print(steelman_resolution_line(evidence))
    print(f"TOTAL: PASS={int(evidence.resolved)} FAIL={int(not evidence.resolved)}")
    return 0 if evidence.resolved else 1


if __name__ == "__main__":
    raise SystemExit(main())
