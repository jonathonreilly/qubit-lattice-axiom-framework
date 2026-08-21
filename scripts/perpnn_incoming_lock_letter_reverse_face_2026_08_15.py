#!/usr/bin/env python3
"""Named-sign reverse/face hold reports from perp-step incoming locks.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed lock at
the origin is +e_1. A 6-NN step is allowed iff it is perpendicular to the
parent lock axis. Newly formed sites lock the incoming step. Uniqueness is
not required: reverse and face are scored on every earliest combination.
"""

from __future__ import annotations

import ast
from collections import deque
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_INCOMING_LOCK_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_INCOMING_LOCK_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
PLUS_LOCKS = frozenset({E1, E2, E3})
BALL_SQ = 9
PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
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


def normalize(text: str) -> str:
    return " ".join(text.split())


def named_sign(lock: Point) -> str:
    return "+" if lock in PLUS_LOCKS else "-"


def hold_report(n_true: int, n_total: int) -> str:
    if n_total == 0 or n_true == 0:
        return "none"
    if n_true == n_total:
        return "hold-on-all"
    return "some"


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
    """Earliest formation order and possible incoming locks on B_3(0)."""
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
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("incoming-lock named-sign reverse/face on B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face content-bits from perpnn earliest "
        "incoming locks on four probes are reported as all/some/none. "
        "Displayed, not adopted."
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
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )

    _ticks, locks = form()
    lock_a = frozenset(locks.get(PROBES["A"], ()))
    lock_b = frozenset(locks.get(PROBES["B"], ()))
    lock_c = frozenset(locks.get(PROBES["C"], ()))
    lock_d = frozenset(locks.get(PROBES["D"], ()))
    expected_a = frozenset({E2, (0, -1, 0), E3, (0, 0, -1)})
    expected_b = frozenset({E1, E2, E3})
    expected_c = frozenset({E1})
    expected_d = frozenset({E1})

    print(f"locks(A)={sorted(lock_a)}")
    print(f"locks(B)={sorted(lock_b)}")
    print(f"locks(C)={sorted(lock_c)}")
    print(f"locks(D)={sorted(lock_d)}")

    checks.check("theorem1-locks-A", lock_a == expected_a, str(sorted(lock_a)))
    checks.check("theorem1-locks-B", lock_b == expected_b, str(sorted(lock_b)))
    checks.check("theorem1-locks-C", lock_c == expected_c, str(sorted(lock_c)))
    checks.check("theorem1-locks-D", lock_d == expected_d, str(sorted(lock_d)))
    checks.check(
        "theorem1-uniqueness-not-required",
        len(lock_a) == 4 and len(lock_b) == 3,
        f"A={len(lock_a)} B={len(lock_b)}",
    )
    checks.check(
        "named-sign-definition",
        named_sign(E1) == named_sign(E2) == named_sign(E3) == "+"
        and named_sign((-1, 0, 0))
        == named_sign((0, -1, 0))
        == named_sign((0, 0, -1))
        == "-",
    )
    checks.check(
        "named-sign-sets",
        {named_sign(lock) for lock in lock_a} == {"+", "-"}
        and {named_sign(lock) for lock in lock_b} == {"+"}
        and {named_sign(lock) for lock in lock_c} == {"+"}
        and {named_sign(lock) for lock in lock_d} == {"+"},
    )

    combos = tuple(product(sorted(lock_a), sorted(lock_b), sorted(lock_c), sorted(lock_d)))
    n_combos = len(combos)
    reverse_hits = 0
    face_hits = 0
    for lock_tuple in combos:
        signs = tuple(named_sign(lock) for lock in lock_tuple)
        reverse_hits += int(signs[0] == "+" and signs[1] == "-")
        face_hits += int(signs[2] == "+" and signs[3] == "-")
    reverse_status = hold_report(reverse_hits, n_combos)
    face_status = hold_report(face_hits, n_combos)
    drop_b_hits = sum(1 for lock_tuple in combos if named_sign(lock_tuple[0]) == "+")
    drop_d_hits = sum(1 for lock_tuple in combos if named_sign(lock_tuple[2]) == "+")

    print(f"n_combos={n_combos} reverse_hits={reverse_hits} face_hits={face_hits}")
    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "combinations-are-earliest-product",
        n_combos == 12 == len(lock_a) * len(lock_b) * len(lock_c) * len(lock_d)
        and n_combos != 2**4,
        str(n_combos),
    )
    checks.check(
        "theorem2-reverse-none",
        reverse_status == "none" and reverse_hits == 0,
        reverse_status,
    )
    checks.check(
        "theorem3-face-none",
        face_status == "none" and face_hits == 0,
        face_status,
    )
    checks.check(
        "mutation-drop-b-minus-is-some",
        hold_report(drop_b_hits, n_combos) == "some" and drop_b_hits == 6,
        str(drop_b_hits),
    )
    checks.check(
        "mutation-drop-d-minus-is-hold-on-all",
        hold_report(drop_d_hits, n_combos) == "hold-on-all" and drop_d_hits == n_combos,
        str(drop_d_hits),
    )
    checks.check(
        "seed-origin-lock-plus-e1",
        locks[ORIGIN] == {E1},
    )
    checks.check(
        "formation-stays-in-host",
        set(locks) <= host,
    )

    claim_scope = (
        "Reverse and face content-bits from perpnn earliest incoming locks "
        "on four probes are reported as all/some/none. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-lock-sets",
        "locks(A) = {+e_2,-e_2,+e_3,-e_3}" in note
        and "locks(B) = {+e_1,+e_2,+e_3}" in note
        and "locks(C) = {+e_1}" in note
        and "locks(D) = {+e_1}" in note,
    )
    checks.check(
        "note-reports-none-none",
        "Report: `none`." in note
        and note.count("Report: `none`.") == 2
        and "hold-on-all" in note
        and "some" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-no-clock-scoring",
        "t(1,0,0)" not in note
        and "3 t(" not in note
        and "not scored from a clock parameter" in normalized_note,
    )
    checks.check(
        "note-not-free-lettering-space",
        "free lettering space" in note
        and "16 letterings" not in note
        and "16-letter" not in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
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
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "does not supply the formation site, probability, or rate"
        in normalized_axiom,
    )
    checks.check(
        "note-quotes-current-premises",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "does not supply the formation site, probability, or rate"
        in normalized_note,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "claim_type: bounded_theorem" in note
        and "authors no audit verdict" in normalized_note
        and "FAIL / DO NOT SHIP" in note,
    )
    checks.check(
        "note-n-gates-present",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-no-author-retained-verdict",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/PERPNN_INCOMING_LOCK_LETTER_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
