#!/usr/bin/env python3
"""Interval s^2 space/null/time census on formed nonzero sites of B_3(0).

Same opposite-lock two-site process as the B_3(0) seed {0,(0,1,0)} with locks
+e_1 and -e_1: a 6-NN step is allowed iff it is perpendicular to the parent
lock axis, and a newly formed site locks the incoming step. Uniqueness is not
required. Q is Euclidean |x|_2^2. No runner cache is written.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (1, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
ONE_SITE_SEEDS: tuple[tuple[Point, Point], ...] = ((ORIGIN, E1),)
SPACE_SITES = frozenset(
    {
        E2,
        (0, 1, 1),
        (0, 1, -1),
        (0, 2, 0),
        (1, 2, 0),
        (-1, 2, 0),
        (0, 2, 1),
        (0, 2, -1),
    }
)
NULL_SITES = frozenset({(0, -1, 0), E3, (0, 0, -1)})
UNFORMED_SITES = frozenset({(3, 0, 0), (-3, 0, 0), (0, 3, 0)})
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "B_12",
    "L1",
    "hop-cost",
    "parnn",
    "k20",
    "B_57",
)
CLAIM_SCOPE = (
    "Interval s^2 space/null/time counts on formed nonzero sites of "
    "B_3(0) under the nsopp two-site opposite-lock process are reported. "
    "Displayed, not adopted."
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Point, set[Point]] = {site: {lock} for site, lock in seeds}
    queue: deque[tuple[Point, int]] = deque((site, 0) for site, _lock in seeds)
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


def interval_class(s2: int) -> str:
    if s2 < 0:
        return "space"
    if s2 == 0:
        return "null"
    return "time"


def census(
    ticks: dict[Point, int],
) -> tuple[int, dict[str, int], dict[Point, tuple[int, int, int, str]]]:
    """Counts and per-site (t, Q, s^2, class) on formed nonzero sites."""
    counts = {"space": 0, "null": 0, "time": 0}
    rows: dict[Point, tuple[int, int, int, str]] = {}
    for site, tick in ticks.items():
        if site == ORIGIN:
            continue
        quad = dot(site, site)
        s2 = tick * tick - quad
        cls = interval_class(s2)
        counts[cls] += 1
        rows[site] = (tick, quad, s2, cls)
    return len(rows), counts, rows


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

    print("opposite-lock interval class census on formed B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

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
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OPPOSITE_LOCK_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    host = ball_sites()
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check("two-site-seed-in-host", {ORIGIN, E2} <= host)
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ORIGIN
        and add(ORIGIN, E2) == E2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(NEG_E1, E2)
        and not perpendicular(E1, E1)
        and not perpendicular(NEG_E1, E1)
        and in_ball(AXIS)
        and not in_ball((4, 0, 0)),
    )

    ticks, locks = form()
    n_formed, counts, rows = census(ticks)
    n_space = counts["space"]
    n_null = counts["null"]
    n_time = counts["time"]
    axis_row = rows.get(AXIS)
    axis_formed = AXIS in rows
    axis_class = axis_row[3] if axis_row is not None else "unformed"

    print(f"N_formed_nonzero={n_formed}")
    print(f"N_space={n_space} N_null={n_null} N_time={n_time}")
    if axis_row is not None:
        tick, quad, s2, cls = axis_row
        print(f"(1,0,0) t={tick} Q={quad} s^2={s2} class={cls}")
    else:
        print("(1,0,0) unformed")
    print(f"locks(1,0,0)={sorted(locks.get(AXIS, ()))}")
    print(f"seed ticks: t(0,0,0)={ticks[ORIGIN]} t(0,1,0)={ticks[E2]}")
    print(f"unformed={sorted(host - set(ticks))}")

    checks.check(
        "seed-ticks-zero-locks-plus-e1-minus-e1",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ORIGIN
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "unformed-axis-and-plus-y-end",
        set(host) - set(ticks) == UNFORMED_SITES,
        str(sorted(set(host) - set(ticks))),
    )
    checks.check(
        "uniqueness-not-required",
        AXIS in locks and len(locks[AXIS]) > 1,
        str(sorted(locks.get(AXIS, ()))),
    )
    checks.check(
        "perp-consistent-seed-locks",
        perpendicular(E1, E2) and perpendicular(NEG_E1, E2) and add(ORIGIN, E2) == E2,
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[(0, -1, 0)] == 1
        and ticks[E3] == 1
        and ticks[(0, 0, -1)] == 1
        and ticks[(0, 2, 0)] == 1
        and locks[(0, 2, 0)] == {E2}
        and "s·e_i=0" in note.replace(" ", ""),
    )
    plus_y_end = (0, 3, 0)
    plus_y_neighbors = tuple(add(plus_y_end, step) for step in NN)
    checks.check(
        "plus-y-end-unformed-from-perp-lock-at-02",
        plus_y_end not in ticks
        and plus_y_end in host
        and ticks[(0, 2, 0)] == 1
        and locks[(0, 2, 0)] == {E2}
        and not perpendicular(E2, E2)
        and sum(in_ball(site) for site in plus_y_neighbors) == 1
        and add((0, 2, 0), E2) == plus_y_end,
    )

    checks.check(
        "theorem1-n-formed-nonzero",
        n_formed == 119,
        str(n_formed),
    )
    checks.check(
        "theorem1-origin-excluded",
        ORIGIN not in rows and ORIGIN in ticks,
    )
    checks.check(
        "theorem1-second-seed-included",
        E2 in rows and rows[E2] == (0, 1, -1, "space"),
    )
    checks.check(
        "theorem1-census-set-is-formed-nonzero",
        set(rows) == set(ticks) - {ORIGIN},
    )
    checks.check(
        "theorem1-formed-plus-unformed-is-host",
        len(ticks) + len(UNFORMED_SITES) == len(host) == 123,
    )

    checks.check("theorem2-n-space", n_space == 8, str(n_space))
    checks.check("theorem2-n-null", n_null == 3, str(n_null))
    checks.check("theorem2-n-time", n_time == 108, str(n_time))
    checks.check(
        "theorem2-counts-partition-formed-nonzero",
        n_space + n_null + n_time == n_formed == 119,
    )
    space_sites = frozenset(site for site, row in rows.items() if row[3] == "space")
    null_sites = frozenset(site for site, row in rows.items() if row[3] == "null")
    checks.check(
        "theorem2-space-sites",
        space_sites == SPACE_SITES
        and rows[(0, 2, 0)] == (1, 4, -3, "space")
        and all(rows[site][2] < 0 for site in space_sites)
        and sum(rows[site][2] == -1 for site in space_sites) == 7,
        str(sorted(space_sites)),
    )
    checks.check(
        "theorem2-null-sites-are-tick1-origin-perp-neighbors-minus-seed",
        null_sites == NULL_SITES
        and all(rows[site][0] == 1 and rows[site][1] == 1 for site in null_sites),
        str(sorted(null_sites)),
    )

    checks.check("theorem3-axis-formed", axis_formed)
    checks.check(
        "theorem3-axis-class-time",
        axis_row == (3, 1, 8, "time"),
        str(axis_row),
    )
    hop_s2 = 1 * 1 - 1
    checks.check(
        "theorem3-not-hop-count-class",
        interval_class(hop_s2) == "null" and axis_class == "time",
        f"hop s^2={hop_s2}",
    )

    one_ticks, _ = form(seeds=ONE_SITE_SEEDS)
    one_n, one_counts, _ = census(one_ticks)
    checks.check(
        "cardinality-not-one-site-clone",
        one_n == 120
        and one_counts == {"space": 0, "null": 4, "time": 116}
        and (n_space, n_null, n_time) != (0, 4, 116)
        and n_formed != one_n,
        f"two=({n_space},{n_null},{n_time}) one={one_counts}",
    )

    perp_ticks, _ = form(seeds=PERP_SEEDS)
    perp_n, perp_counts, perp_rows = census(perp_ticks)
    checks.check(
        "not-perp-seed-interval-reprint",
        perp_n == 120
        and perp_counts == {"space": 9, "null": 3, "time": 108}
        and perp_rows[AXIS] == (2, 1, 3, "time")
        and (n_formed, n_space, n_null, n_time) != (120, 9, 3, 108)
        and axis_row != (2, 1, 3, "time"),
        f"opp=({n_formed},{n_space},{n_null},{n_time}) perp={perp_counts}",
    )

    free_ticks, _ = form(require_perp=False)
    free_n, _free_counts, _ = census(free_ticks)
    checks.check(
        "mutation-drop-perp-changes-formed-count",
        free_n != n_formed,
        f"free N_formed_nonzero={free_n}",
    )
    q_210 = dot((2, 1, 0), (2, 1, 0))
    checks.check(
        "q-is-euclidean-square-not-abs-sum",
        q_210 == 5 and (2, 1, 0) in rows and rows[(2, 1, 0)][1] == 5,
        str(q_210),
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-census-counts",
        "N_formed nonzero = 119" in note
        and "N_space = 8" in note
        and "N_null = 3" in note
        and "N_time = 108" in note,
    )
    checks.check(
        "note-reports-axis-class",
        "t(1,0,0)=3" in note
        and "s^2(1,0,0)=8" in note
        and "class time" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note,
    )
    checks.check(
        "note-cardinality-not-clone",
        "Cardinality-of-seed, not a 1-site clone" in note
        and "not a 1-site clone" in note,
    )
    checks.check(
        "note-not-perp-seed-reprint",
        "not a reprint of the perp two-site interval census" in note
        and "t(1,0,0)=3" in note
        and "N_formed nonzero = 120" not in note,
    )
    checks.check(
        "note-not-four-event-reprint",
        "3 t(1,0,0)^2" not in note
        and "t(2,0,0)^2 > 2 t(1,1,0)^2" not in note
        and "k=1 reverse" not in note
        and "k=1 face" not in note
        and "variance" not in note.lower()
        and "not a four-event table" in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "No runner cache is written." in note,
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

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
