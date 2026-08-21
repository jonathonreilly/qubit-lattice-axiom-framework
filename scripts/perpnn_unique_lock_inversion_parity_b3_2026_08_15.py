#!/usr/bin/env python3
"""Unique-lock inversion parity on B_3(0) under perpnn.

Same perp-step incoming-lock process as the B_3(0) formation-tick display:
seed lock(0)=+e_1, a 6-NN step is allowed iff it is perpendicular to the
parent lock axis, and a newly formed site locks the incoming step.
Uniqueness is not required of the process. This runner reports inversion
parity only on formed pairs whose earliest incoming-lock sets both have
size 1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_UNIQUE_LOCK_INVERSION_PARITY_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_UNIQUE_LOCK_INVERSION_PARITY_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "L1",
    "16-letter",
    "16 letterings",
    "hop-cost",
    "B_57",
    "Runner cache",
    "64 occupancy",
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def neg(site: Point) -> Point:
    return (-site[0], -site[1], -site[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def in_ball(site: Point) -> bool:
    return dot(site, site) <= BALL_SQ


def ball_sites() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if in_ball((x, y, z))
    )


def perpendicular(lock: Point, step: Point) -> bool:
    return dot(lock, step) == 0


def hemisphere_rep(site: Point) -> bool:
    """Count each {x,-x} once: x_1>0, or x_1=0 and x_2>0, or x_1=x_2=0 and x_3>0."""
    return (
        site[0] > 0
        or (site[0] == 0 and site[1] > 0)
        or (site[0] == 0 and site[1] == 0 and site[2] > 0)
    )


def assignment_string_tuple(tree: ast.AST, name: str) -> tuple[str, ...] | None:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    return None
                if isinstance(value, tuple) and all(
                    isinstance(item, str) for item in value
                ):
                    return value
                return None
    return None


def form(
    seed_lock: Point = E1,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {ORIGIN: 0}
    locks: dict[Point, set[Point]] = {ORIGIN: {seed_lock}}
    queue: deque[tuple[Point, int]] = deque([(ORIGIN, 0)])
    while queue:
        parent, parent_tick = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if require_perp and not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_tick = parent_tick + 1
                if child not in ticks:
                    ticks[child] = next_tick
                    locks[child] = {step}
                    queue.append((child, next_tick))
                elif ticks[child] == next_tick:
                    locks[child].add(step)
    return ticks, locks


def unique_lock(locks: dict[Point, set[Point]], site: Point) -> Point | None:
    letters = locks.get(site)
    if letters is None or len(letters) != 1:
        return None
    return next(iter(letters))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    claim_scope = (
        "Inversion parity of unique earliest incoming locks on formed "
        "pairs {x,−x} in B_3(0) under perpnn is reported. Displayed, not "
        "adopted."
    )

    print("perpnn unique-lock inversion parity on B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {claim_scope}")

    checks.check(
        "audit-input-paths-literal",
        literal_paths == AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
        str(literal_paths),
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    host = ball_sites()
    ticks, locks = form()
    formed = frozenset(ticks)
    unformed = sorted(host - formed)

    pair_reps: list[Point] = []
    unique_reps: list[Point] = []
    n_odd = 0
    n_even = 0
    n_other = 0
    for site in sorted(formed):
        if site == ORIGIN or not hemisphere_rep(site):
            continue
        antipode = neg(site)
        if antipode not in formed:
            continue
        pair_reps.append(site)
        lock_x = unique_lock(locks, site)
        lock_mx = unique_lock(locks, antipode)
        if lock_x is None or lock_mx is None:
            continue
        unique_reps.append(site)
        if lock_mx == neg(lock_x):
            n_odd += 1
        elif lock_mx == lock_x:
            n_even += 1
        else:
            n_other += 1

    n_pairs = len(pair_reps)
    n_unique = len(unique_reps)
    if n_unique == 0:
        sample_class = "empty"
    elif n_odd == n_unique and n_even == 0 and n_other == 0:
        sample_class = "all-odd"
    elif n_even == n_unique and n_odd == 0 and n_other == 0:
        sample_class = "all-even"
    else:
        sample_class = "mixed"

    print(f"host={len(host)} formed={len(formed)} unformed={unformed}")
    print(f"N_pairs={n_pairs} N_unique={n_unique}")
    print(f"N_odd={n_odd} N_even={n_even} N_other={n_other}")
    print(f"unique_sample={sample_class}")
    lock_010 = unique_lock(locks, (0, 1, 0))
    lock_0m10 = unique_lock(locks, (0, -1, 0))
    print(f"witness L(0,1,0)={lock_010} L(0,-1,0)={lock_0m10}")
    print(f"locks(1,0,0)={sorted(locks.get((1, 0, 0), ()))}")

    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "theorem1-n-pairs-both-formed",
        n_pairs == 60,
        str(n_pairs),
    )
    checks.check(
        "theorem1-n-unique-both-ends",
        n_unique == 25,
        str(n_unique),
    )
    checks.check(
        "theorem1-uniqueness-not-required",
        n_unique < n_pairs and len(locks[(1, 0, 0)]) == 4,
        f"unique={n_unique} pairs={n_pairs} locks(1,0,0)={len(locks[(1, 0, 0)])}",
    )
    checks.check(
        "theorem2-odd-even-other",
        n_odd == 25 and n_even == 0 and n_other == 0,
        f"{n_odd},{n_even},{n_other}",
    )
    checks.check(
        "theorem2-partition-of-unique",
        n_odd + n_even + n_other == n_unique,
    )
    checks.check(
        "theorem3-unique-sample-all-odd",
        sample_class == "all-odd",
        sample_class,
    )
    checks.check(
        "hemisphere-counts-each-pair-once",
        2 * n_pairs
        == sum(
            1
            for site in formed
            if site != ORIGIN and neg(site) in formed
        ),
    )
    checks.check(
        "unformed-axial-triple",
        unformed == [(-3, 0, 0), (3, 0, 0)],
        str(unformed),
    )
    checks.check(
        "witness-unique-odd-pair",
        lock_010 == E2 and lock_0m10 == (0, -1, 0) == neg(lock_010),
        f"{lock_010} vs {lock_0m10}",
    )
    checks.check(
        "seed-origin-tick-zero-lock-plus-e1",
        ticks[ORIGIN] == 0 and locks[ORIGIN] == {E1},
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)

    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-counts",
        "N_pairs=60" in note
        and "N_unique=25" in note
        and "N_odd=25" in note
        and "N_even=0" in note
        and "N_other=0" in note
        and "all-odd" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note,
    )
    checks.check(
        "note-forbids-enlargement-cache-and-occupancy-census",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "No runner cache is written." in note
        and "not a 64-row occupancy census" in note.lower(),
    )
    checks.check(
        "note-does-not-write-P-or-VA-into-admissibility",
        "Do not write P or V−A into Admissibility." in note
        and "not written into Admissibility" in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        and "claim_type: bounded_theorem" in note,
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/PERPNN_UNIQUE_LOCK_INVERSION_PARITY_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check("formation-uses-earliest-tick-queue", "queue.popleft()" in source)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
