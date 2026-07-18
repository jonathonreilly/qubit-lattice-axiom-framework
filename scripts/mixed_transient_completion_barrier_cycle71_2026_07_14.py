#!/usr/bin/env python3
"""Cycle 71: mixed Cycle-60/Cycle-67 causal-composition audit.

Cycle 67 proves the completion-barrier phase transducer after the Cycle-60
comb is complete.  This runner projects every one of the 242,033 reachable
Cycle-60 states into every locally relevant Cycle-67 context.  The projection
is deliberately an over-approximation: a phase record may be called feasible
without forcing all of its mandatory ancestors to appear in the same local
view.  Every apparent bad write is therefore passed through Cycle 67's exact
must-ancestor certificate.  Safety follows only if the over-approximation has
no conflict/blocker and every reported wrong write carries that contradiction.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import mixed_transient_pair_barrier_phase_cycle68_2026_07_14 as c68
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MIXED_TRANSIENT_COMPLETION_BARRIER_CYCLE71_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def role_neighbours(phase: dict[Coord, str], site: Coord, role: str) -> frozenset[Coord]:
    return frozenset(
        neighbour
        for direction in c53.DIRECTIONS
        if (neighbour := c53.add(site, direction)) in phase
        and phase[neighbour] == role
    )


def requirements67(
    phase: dict[Coord, str], _repaired: bool,
) -> dict[Coord, tuple[frozenset[Coord], ...]]:
    """Return the exact AND-of-OR dependency DAG for Cycle 67.

    In this geometry every `one` group is a singleton.  `all` is written as
    one singleton group per parent, making mandatory ancestry explicit.
    """

    specification: dict[str, tuple[tuple[str, str], ...]] = {
        "F": (),
        "FP": (("F", "all"),),
        "I1": (("FP", "one"),),
        "I2": (("I1", "one"),),
        "DONE": (("I2", "all"),),
        "L1": (("DONE", "one"),),
        "L2": (("I2", "one"), ("L1", "one")),
        "L3": (("L2", "all"),),
        "L4": (("L3", "one"),),
        "L5": (("F", "one"), ("L4", "one")),
        "L6": (("L5", "one"),),
        "L7": (("F", "one"), ("L6", "one")),
        "L8": (("L7", "all"),),
        "L9": (("L8", "one"),),
        "L10": (("L9", "one"),),
        "L11": (("L10", "all"),),
        "L12": (("L11", "one"),),
        "C_Q": (("L12", "one"),),
        "P0": (("C_Q", "one"),),
        "P1": (("P0", "one"), ("L8", "one"), ("L10", "one")),
        "P2": (("C_Q", "one"), ("P1", "one"), ("L11", "one")),
        "P3": (("P2", "one"), ("L8", "one"), ("L10", "one")),
        "X_B": (("P3", "one"),),
        "Z_A": (("X_B", "one"), ("P2", "one")),
        "Z_C": (("X_B", "one"),),
    }

    result: dict[Coord, tuple[frozenset[Coord], ...]] = {}
    for site, role in phase.items():
        groups: list[frozenset[Coord]] = []
        for parent_role, mode in specification[role]:
            parents = role_neighbours(phase, site, parent_role)
            if not parents:
                raise ValueError(f"missing {parent_role} parent for {role}@{site}")
            if mode == "all":
                groups.extend(frozenset((parent,)) for parent in sorted(parents))
            else:
                groups.append(parents)
        result[site] = tuple(groups)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 Cycle-67 conditional runner is green", c67.main() == 0)
    check("A03 Cycle-67 table has 99 canonical rows", len(c67.RULES) == 99)
    check("A04 Cycle-67 declares 91 additions", len(c67.ALLOWED) == 91)

    comb_raw = c68.raw_outputs(c60.CONSTRUCTION.table)
    phase_raw = c68.raw_outputs(c67.RULES)
    check("B01 Cycle-60 and Cycle-67 raw input domains are disjoint", set(comb_raw).isdisjoint(phase_raw))
    check("B02 Cycle-60 raw census is 376", len(comb_raw) == 376, str(len(comb_raw)))
    check("B03 Cycle-67 raw census is 2,218", len(phase_raw) == 2_218, str(len(phase_raw)))

    seen, cycle60_sites = c68.reachable_cycle60_states()
    check("C01 every reachable Cycle-60 state is retained", len(seen) == 242_033, f"{len(seen):,}")

    prior_requirements = c68.requirements
    c68.requirements = requirements67
    try:
        mixed = c68.mixed_scan(
            seen, cycle60_sites, c67.ALLOWED, c67.RULES, repaired=True,
        )
    finally:
        c68.requirements = prior_requirements

    check("C02 mixed over-approximation scans 1,204,205 contexts", mixed.contexts == 1_204_205, f"{mixed.contexts:,}")
    check("C03 207,550 contexts pass the first parent-feasibility gate", mixed.feasible_contexts == 207_550, f"{mixed.feasible_contexts:,}")
    check("C04 mixed union has no output conflict", mixed.conflicts == 0)
    check("C05 permanent phase records cannot block an unfinished comb target", mixed.blockers == 0)

    conditions = c67.compile_conditions()
    bad, witnesses, _, _, _ = c67.causal_safety_certificate(conditions)
    off_footprint = {
        (target, output): condition
        for condition in bad
        for _, _, target_bit, output, target in (condition,)
        if not target_bit
    }
    mixed_wrong = frozenset(mixed.wrong_writes)
    expected_wrong = frozenset(
        (target, "PHASE", (output,), None)
        for target, output in off_footprint
    )
    check("D01 over-approximation reports exactly 15 wrong-write classes", len(mixed_wrong) == 15, str(sorted(mixed_wrong)))
    check("D02 no new partial-comb wrong-write class appears", mixed_wrong == expected_wrong)
    check("D03 all 15 classes are off-footprint aliases", all(expected is None and source == "PHASE" for _, source, _, expected in mixed_wrong))
    check("D04 every mixed alias has a must-ancestor contradiction", all(off_footprint[(target, outputs[0])] in witnesses for target, _, outputs, _ in mixed_wrong))
    check("D05 every Cycle-67 bad condition remains causally certified", len(witnesses) == len(bad) == 47)

    # The mixed scan includes every reachable comb projection and more phase
    # subsets than can coexist.  With no conflict/blocker and every apparent
    # wrong write removed by an exact necessary-ancestor contradiction, no
    # first bad append exists.  Cycle 67's rank closure then supplies progress.
    check("E01 mixed safety induction closes", mixed.conflicts == mixed.blockers == 0 and mixed_wrong == expected_wrong and all(off_footprint[(target, outputs[0])] in witnesses for target, _, outputs, _ in mixed_wrong))
    check("E02 composition retains Cycle-67 complete-terminal proof", c67.rank_prefix_closure()[1] == 0)

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
