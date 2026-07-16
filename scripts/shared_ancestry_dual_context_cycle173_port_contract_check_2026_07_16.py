#!/usr/bin/env python3
"""Focused verifier for the frozen Cycle-173 measured-row port contract."""

from __future__ import annotations

import hashlib
from pathlib import Path

import shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16 as c173


ROOT = Path(__file__).resolve().parents[1]
FROZEN_RUNNER = (
    ROOT
    / "scripts/shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16.py"
)
FROZEN_RUNNER_SHA = (
    "92afd28e4cf8b36b98b90b8cf919e13052716a056c64377396da304cb42acc11"
)


def main() -> int:
    assert hashlib.sha256(FROZEN_RUNNER.read_bytes()).hexdigest() == FROZEN_RUNNER_SHA

    plan = c173.ported_plan()
    scaffold, _ports, removable_cage = c173.ported_scaffold()
    root = c173.add(plan.p_input, c173.EX)
    assert root == (-240, 0, 0)
    assert plan.p_input == (-241, 0, 0)

    group = plan.path_groups[2]
    paths = tuple(path for spec, path in group if spec == ("row", "p"))
    assert tuple((path[0], path[-1], len(path)) for path in paths) == (
        (root, (-240, 10, 0), 11),
        (root, (-225, 0, 0), 28),
    )

    controls = (
        (c173.add(root, c173.EY), c173.add(plan.p_input, c173.EY)),
        (c173.add(root, c173.NEG_EY), c173.add(plan.p_input, c173.NEG_EY)),
    )
    assert all(scaffold[mark] == "MARK" for _target, mark in controls)
    assert all(mark not in plan.fixed for _target, mark in controls)
    assert all(mark not in removable_cage for _target, mark in controls)

    context = c173.context_instance(
        "probe",
        (c173.IZ, c173.ZZ),
        c173.ZI,
        (0, 0, 0),
    )
    deletion_results = []
    for target, mark in controls:
        premise = c173.formation_records(
            context.initial,
            context.expected,
            context.dependencies,
            target,
        )
        wanted = context.expected[target]
        baseline = c173.c169.UNIFIED_RAW.get(
            c173.c169.c53.local_signature(premise, target),
            frozenset(),
        )
        shortened = dict(premise)
        del shortened[mark]
        after_deletion = c173.c169.UNIFIED_RAW.get(
            c173.c169.c53.local_signature(shortened, target),
            frozenset(),
        )
        assert baseline == frozenset((wanted,))
        assert wanted not in after_deletion
        deletion_results.append((target, mark, wanted, after_deletion))

    print("PASS frozen Cycle-173 runner hash", FROZEN_RUNNER_SHA)
    print("PASS cable-fed input/root", plan.p_input, root)
    print("PASS first-comb path group", tuple(map(len, paths)))
    print(
        "PASS functional nonremovable MARK guards",
        tuple((mark, scaffold[mark]) for _target, mark in controls),
    )
    print("PASS guard deletions stall first branch formations", deletion_results)
    print("RESULT CYCLE173_CABLE_FED_PORT_CONTRACT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
