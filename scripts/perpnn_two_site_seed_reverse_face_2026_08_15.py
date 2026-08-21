#!/usr/bin/env python3
"""Perp-step two-site seed reverse and face on B_3(0).

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is the two-record set {0, (0,1,0)} with perp-consistent locks +e_1 and +e_2.
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Uniqueness is not required: all
earliest incoming steps are kept. Cardinality-of-seed, not a 1-site clone.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_TWO_SITE_SEED_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_TWO_SITE_SEED_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
ONE_SITE_SEEDS: tuple[tuple[Point, Point], ...] = ((ORIGIN, E1),)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "hop-cost",
    "parnn",
    "k20",
    "B_57",
    "L1",
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

    print("perp-step two-site seed reverse/face on B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Perp-step incoming-lock formation-tick reverse and face "
        "at k=1 on B_3(0) with two-site seed {0,(0,1,0)} and locks +e_1/+e_2 "
        "are reported. Displayed, not adopted."
    )

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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "k1-probes-in-host",
        {(1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0)} <= host,
    )
    checks.check(
        "two-site-seed-in-host",
        {ORIGIN, E2} <= host,
    )

    ticks, locks = form()
    mask = tuple(int(ticks.get(step) == 1) for step in NN)
    t100 = ticks.get((1, 0, 0))
    t111 = ticks.get((1, 1, 1))
    t200 = ticks.get((2, 0, 0))
    t110 = ticks.get((1, 1, 0))

    print(f"tick-1 6-mask: {mask}")
    print(f"t(1,0,0)={t100} t(1,1,1)={t111} t(2,0,0)={t200} t(1,1,0)={t110}")
    print(f"locks(1,0,0)={sorted(locks.get((1, 0, 0), ()))}")
    print(f"locks(1,1,1)={sorted(locks.get((1, 1, 1), ()))}")
    print(f"seed ticks: t(0,0,0)={ticks[ORIGIN]} t(0,1,0)={ticks[E2]}")

    checks.check(
        "theorem1-tick1-mask",
        mask == (0, 0, 0, 1, 1, 1),
        str(mask),
    )
    checks.check(
        "theorem1-seed-and-tick1-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2}
        and locks[(0, -1, 0)] == {(0, -1, 0)}
        and locks[E3] == {E3}
        and locks[(0, 0, -1)] == {(0, 0, -1)},
    )
    checks.check(
        "theorem1-plus-e2-neighbor-is-seed-not-tick1",
        ticks[E2] == 0 and mask[2] == 0,
    )
    checks.check(
        "theorem1-defined-ticks",
        t100 == 2 and t111 == 2 and t200 == 3 and t110 == 1,
        f"{t100},{t111},{t200},{t110}",
    )
    checks.check(
        "theorem1-uniqueness-not-required",
        t111 is not None and len(locks[(1, 1, 1)]) == 2,
        str(sorted(locks.get((1, 1, 1), ()))),
    )
    checks.check(
        "theorem1-not-six-neighbor-distance",
        t100 != 1 and t200 != 2,
    )

    one_ticks, _one_locks = form(seeds=ONE_SITE_SEEDS)
    one_mask = tuple(int(one_ticks.get(step) == 1) for step in NN)
    checks.check(
        "cardinality-not-one-site-clone",
        one_mask == (0, 0, 1, 1, 1, 1)
        and mask != one_mask
        and (
            one_ticks.get((1, 0, 0)),
            one_ticks.get((1, 1, 1)),
            one_ticks.get((2, 0, 0)),
            one_ticks.get((1, 1, 0)),
        )
        == (3, 3, 4, 2)
        and (t100, t111, t200, t110) != (3, 3, 4, 2),
        f"two={mask} one={one_mask}",
    )

    reverse_defined = t100 is not None and t111 is not None
    face_defined = t200 is not None and t110 is not None
    reverse_holds = reverse_defined and 3 * t100 * t100 > t111 * t111
    face_holds = face_defined and t200 * t200 > 2 * t110 * t110
    checks.check(
        "theorem2-reverse-defined-and-holds",
        reverse_holds,
        f"3*{t100}^2={3 * t100 * t100 if reverse_defined else 'undef'} vs {t111 * t111 if reverse_defined else 'undef'}",
    )
    checks.check(
        "theorem3-face-defined-and-holds",
        face_holds,
        f"{t200}^2={t200 * t200 if face_defined else 'undef'} vs 2*{t110}^2={2 * t110 * t110 if face_defined else 'undef'}",
    )

    free_ticks, _ = form(require_perp=False)
    free_mask = tuple(int(free_ticks.get(step) == 1) for step in NN)
    checks.check(
        "mutation-drop-perp-changes-origin-mask",
        free_mask == (1, 1, 0, 1, 1, 1) and free_mask != mask,
        str(free_mask),
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "perp-consistent-seed-locks",
        perpendicular(E1, E2) and add(ORIGIN, E2) == E2,
    )

    claim_scope = (
        "Perp-step incoming-lock formation-tick reverse and face at k=1 "
        "on B_3(0) with two-site seed {0,(0,1,0)} and locks +e_1/+e_2 are "
        "reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-mask-and-ticks",
        "tick-1 6-mask, order (+e_1,-e_1,+e_2,-e_2,+e_3,-e_3): (0,0,0,1,1,1)"
        in note
        and "t(1,0,0)=2" in note
        and "t(1,1,1)=2" in note
        and "t(2,0,0)=3" in note
        and "t(1,1,0)=1" in note,
    )
    checks.check(
        "note-reverse-and-face-hold",
        "3 t(1,0,0)^2 > t(1,1,1)^2" in note
        and "t(2,0,0)^2 > 2 t(1,1,0)^2" in note
        and "Status: hold." in note,
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
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/PERPNN_TWO_SITE_SEED_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
