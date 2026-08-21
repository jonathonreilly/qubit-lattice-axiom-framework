#!/usr/bin/env python3
"""Interval s^2 space/null/time census on formed nonzero sites of B_3(0).

Same perp-step incoming-lock process as the B_3(0) seed-lock +e_1 formation
ticks: a 6-NN step is allowed iff it is perpendicular to the parent lock
axis, and a newly formed site locks the incoming step. Uniqueness is not
required. Q is Euclidean |x|_2^2. No runner cache is written.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "B_12",
    "L1",
)
CLAIM_SCOPE = (
    "Interval s^2 space/null/time counts on formed nonzero sites of "
    "B_3(0) under perpnn formation-ticks are reported. Displayed, not adopted."
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

    print("perpnn interval class census on formed B_3(0)")
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
        '    "docs/PERPNN_INTERVAL_CLASS_CENSUS_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    host = ball_sites()
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)

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

    checks.check(
        "seed-origin-tick-zero-lock-plus-e1",
        ticks[ORIGIN] == 0 and locks[ORIGIN] == {E1},
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "uniqueness-not-required",
        AXIS in locks and len(locks[AXIS]) > 1,
        str(sorted(locks.get(AXIS, ()))),
    )

    checks.check(
        "theorem1-n-formed-nonzero",
        n_formed == 120,
        str(n_formed),
    )
    checks.check(
        "theorem1-origin-excluded",
        ORIGIN not in rows and ORIGIN in ticks,
    )
    checks.check(
        "theorem1-census-set-is-formed-nonzero",
        set(rows) == set(ticks) - {ORIGIN},
    )

    checks.check("theorem2-n-space", n_space == 0, str(n_space))
    checks.check("theorem2-n-null", n_null == 4, str(n_null))
    checks.check("theorem2-n-time", n_time == 116, str(n_time))
    checks.check(
        "theorem2-counts-partition-formed-nonzero",
        n_space + n_null + n_time == n_formed == 120,
    )
    null_sites = frozenset(site for site, row in rows.items() if row[3] == "null")
    checks.check(
        "theorem2-null-sites-are-tick1-perp-neighbors",
        null_sites == frozenset({E2, (0, -1, 0), E3, (0, 0, -1)})
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

    free_ticks, _ = form(require_perp=False)
    free_n, free_counts, _ = census(free_ticks)
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

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-census-counts",
        "N_formed nonzero = 120" in note
        and "N_space = 0" in note
        and "N_null = 4" in note
        and "N_time = 116" in note,
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
        "note-not-four-event-reprint",
        "(1,1,0)" not in note
        and "(1,1,1)" not in note
        and "variance" not in note.lower(),
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
