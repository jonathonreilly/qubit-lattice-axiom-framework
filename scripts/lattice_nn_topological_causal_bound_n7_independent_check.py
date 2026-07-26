#!/usr/bin/env python3
"""Independent shared-randomness steelman for the causal-bound theorem.

This helper deliberately does not import the primary certificate.  It builds a
time-dependent family of Boolean local maps on a three-vertex chain directly,
uses each seed-selected map schedule in both histories, and checks the claimed
forward-reachability containment after every tick.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


State = tuple[bool, bool, bool]
SCHEDULE_COUNT = 256
HORIZON = 3
WALL = "outside-reachability influence under shared extensional R-local updates"


@dataclass(frozen=True)
class SteelmanEvidence:
    schedules_checked: int
    initial_pairs_checked: int
    tick_assertions: int
    resolved: bool


def truth_table_output(mask: int, inputs: tuple[bool, ...]) -> bool:
    index = sum(int(bit) << position for position, bit in enumerate(inputs))
    return bool(mask & (1 << index))


def schedule_mask(seed: int, tick: int, vertex: int, arity: int) -> int:
    """Return a deterministic tick-dependent table selected by ``seed``."""
    mixed = (
        seed * 1103515245
        + (tick + 1) * 12345
        + (vertex + 1) * 2654435761
    ) & 0xFFFFFFFF
    return mixed % (1 << (1 << arity))


def update(state: State, seed: int, tick: int) -> State:
    predecessor_lists = ((0,), (0, 1), (1, 2))
    return tuple(
        truth_table_output(
            schedule_mask(seed, tick, vertex, len(predecessors)),
            tuple(state[u] for u in predecessors),
        )
        for vertex, predecessors in enumerate(predecessor_lists)
    )  # type: ignore[return-value]


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
    """Test changing realized maps without changing them between histories."""
    configurations = tuple(product((False, True), repeat=3))
    initial_pairs = 0
    tick_assertions = 0
    resolved = True
    for seed in range(SCHEDULE_COUNT):
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
                left_state = left_initial
                right_state = right_initial
                for tick in range(HORIZON + 1):
                    differences = {
                        vertex
                        for vertex, (left, right) in enumerate(
                            zip(left_state, right_state)
                        )
                        if left != right
                    }
                    tick_assertions += 1
                    resolved = resolved and differences <= reachable[tick]
                    if tick < HORIZON:
                        # The same seed and tick select the same realized local
                        # maps pathwise in both histories.
                        left_state = update(left_state, seed, tick)
                        right_state = update(right_state, seed, tick)
    return SteelmanEvidence(
        schedules_checked=SCHEDULE_COUNT,
        initial_pairs_checked=initial_pairs,
        tick_assertions=tick_assertions,
        resolved=resolved,
    )


def steelman_resolution_line(evidence: SteelmanEvidence) -> str:
    return (
        f"N7_STEELMAN_RESOLUTION {WALL} wall resolved independently: "
        f"{evidence.schedules_checked} deterministic seed schedules vary every "
        "local truth table by tick while remaining shared across the two "
        f"histories, and all {evidence.tick_assertions} tick comparisons obey "
        "D_t subset C_t(S); changing shared randomness cannot create an exterior "
        "difference."
    )


def main() -> int:
    evidence = compute_steelman_evidence()
    status = "PASS" if evidence.resolved else "FAIL"
    print("NN CAUSAL BOUND N7 -- INDEPENDENT TIME-DEPENDENT MAP MODE")
    print(
        f"[{status}] shared schedule steelman: "
        f"schedules={evidence.schedules_checked} "
        f"initial_pairs={evidence.initial_pairs_checked} "
        f"tick_assertions={evidence.tick_assertions}"
    )
    if evidence.resolved:
        print(steelman_resolution_line(evidence))
    print(f"TOTAL: PASS={int(evidence.resolved)} FAIL={int(not evidence.resolved)}")
    return 0 if evidence.resolved else 1


if __name__ == "__main__":
    raise SystemExit(main())
