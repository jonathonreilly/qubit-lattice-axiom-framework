#!/usr/bin/env python3
"""Perp-step incoming-lock formation ticks on B_3(0).

Finite host: Euclidean ball of radius 3 centered at the origin. Seed lock at
the origin is +e_1. A 6-NN step is allowed iff it is perpendicular to the
parent lock axis. Newly formed sites lock the incoming step. Uniqueness is
not required: all earliest incoming steps are kept.
"""

from __future__ import annotations

import ast
from collections import defaultdict, deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERP_STEP_INCOMING_LOCK_FORMATION_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERP_STEP_INCOMING_LOCK_FORMATION_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "hop-cost",
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
    seed_lock: Point = E1,
    *,
    require_perp: bool = True,
    parallel_only: bool = False,
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
                if parallel_only and perpendicular(lock, step):
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

    print("perp-step incoming-lock formation on B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("claim_scope: displayed k=1 reverse/face on B_3(0); not adopted")

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

    ticks, locks = form()
    mask = tuple(int(ticks.get(step) == 1) for step in NN)
    t100 = ticks.get((1, 0, 0))
    t111 = ticks.get((1, 1, 1))
    t200 = ticks.get((2, 0, 0))
    t110 = ticks.get((1, 1, 0))

    print(f"tick-1 6-mask: {mask}")
    print(f"t(1,0,0)={t100} t(1,1,1)={t111} t(2,0,0)={t200} t(1,1,0)={t110}")
    print(f"locks(1,0,0)={sorted(locks.get((1, 0, 0), ()))}")

    checks.check(
        "theorem1-tick1-mask",
        mask == (0, 0, 1, 1, 1, 1),
        str(mask),
    )
    checks.check(
        "theorem1-incoming-locks",
        locks[E2] == {E2}
        and locks[(0, -1, 0)] == {(0, -1, 0)}
        and locks[E3] == {E3}
        and locks[(0, 0, -1)] == {(0, 0, -1)},
    )
    checks.check(
        "theorem1-not-second-plus-e1-mask",
        mask != (1, 0, 0, 0, 0, 0)
        and mask != (1, 1, 0, 0, 0, 0)
        and set(step for step, bit in zip(NN, mask, strict=True) if bit)
        == {E2, (0, -1, 0), E3, (0, 0, -1)},
    )
    checks.check(
        "theorem2-defined-ticks",
        t100 == 3 and t111 == 3 and t200 == 4 and t110 == 2,
        f"{t100},{t111},{t200},{t110}",
    )
    checks.check(
        "theorem2-uniqueness-not-required",
        t100 is not None and len(locks[(1, 0, 0)]) == 4,
        str(sorted(locks.get((1, 0, 0), ()))),
    )
    checks.check(
        "theorem2-not-hop-count",
        t100 != 1 and t200 != 2,
    )
    reverse_defined = t100 is not None and t111 is not None
    face_defined = t200 is not None and t110 is not None
    reverse_holds = reverse_defined and 3 * t100 * t100 > t111 * t111
    face_holds = face_defined and t200 * t200 > 2 * t110 * t110
    checks.check(
        "theorem3-reverse-defined-and-holds",
        reverse_holds,
        f"3*{t100}^2={3 * t100 * t100 if reverse_defined else 'undef'} vs {t111 * t111 if reverse_defined else 'undef'}",
    )
    checks.check(
        "theorem3-face-defined-and-holds",
        face_holds,
        f"{t200}^2={t200 * t200 if face_defined else 'undef'} vs 2*{t110}^2={2 * t110 * t110 if face_defined else 'undef'}",
    )

    parallel_ticks, _ = form(require_perp=False, parallel_only=True)
    free_ticks, _ = form(require_perp=False, parallel_only=False)
    parallel_mask = tuple(int(parallel_ticks.get(step) == 1) for step in NN)
    free_mask = tuple(int(free_ticks.get(step) == 1) for step in NN)
    checks.check(
        "mutation-parallel-only-is-axial-mask",
        parallel_mask == (1, 1, 0, 0, 0, 0),
        str(parallel_mask),
    )
    checks.check(
        "mutation-drop-perp-forms-all-six",
        free_mask == (1, 1, 1, 1, 1, 1)
        and free_ticks.get((1, 0, 0)) == 1,
        str(free_mask),
    )
    checks.check(
        "seed-origin-tick-zero-lock-plus-e1",
        ticks[ORIGIN] == 0 and locks[ORIGIN] == {E1},
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )

    claim_scope = (
        "Perp-step incoming-lock formation-tick reverse and face at k=1 "
        "on B_3(0) with seed lock +e_1 are reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-mask-and-ticks",
        "tick-1 6-mask, order (+e_1,-e_1,+e_2,-e_2,+e_3,-e_3): (0,0,1,1,1,1)"
        in note
        and "t(1,0,0)=3" in note
        and "t(1,1,1)=3" in note
        and "t(2,0,0)=4" in note
        and "t(1,1,0)=2" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note,
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
        '    "docs/PERP_STEP_INCOMING_LOCK_FORMATION_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
