#!/usr/bin/env python3
"""Sum of already-recorded 6-NN locks on four nnseed y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each y-probe's formation tick, S is the list of incoming locks of
already-recorded six-neighbors. A is a seed: same-tick partner is not
already-recorded. If S is empty the letter is UNDEFINED; else the letter is
the vector sum of S in Z^3. Reverse iff L(A)+L(B)=(0,0,0). Face iff
L(C)+L(D)=(0,0,0). Uniqueness is not required. Not leftover unique vector.
Not occupancy-kernel n. Not named {+,−} PVM letters.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_YPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_YPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
ZERO: Point = (0, 0, 0)
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
PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
X_PROBES = {
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
    "Gram",
    "L1",
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


def vector_sum(locks: list[Point]) -> Point:
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


def letter_from_S(locks: list[Point]) -> Point | None:
    if not locks:
        return None
    return vector_sum(locks)


def letter_report(letter: Point | None) -> str:
    if letter is None:
        return "UNDEFINED"
    return str(letter)


def comparison_report(left: Point | None, right: Point | None) -> str:
    if left is None or right is None:
        return "UNDEFINED"
    if add(left, right) == ZERO:
        return "hold"
    return "fail"


def leftover_unique_vector(site: Point, ticks: dict[Point, int]) -> Point | None:
    """Refused unique leftover: the unique unrecorded 6-NN step."""
    formation = ticks[site]
    unrecorded: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] >= formation:
            unrecorded.append(step)
    if len(unrecorded) != 1:
        return None
    return unrecorded[0]


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
    """Earliest formation ticks and incoming locks on B_3(0)."""
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


def already_recorded(site: Point, ticks: dict[Point, int]) -> frozenset[Point]:
    formation = ticks[site]
    return frozenset(other for other, tick in ticks.items() if tick < formation)


def neighbor_lock_list(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> list[Point]:
    """Incoming locks of already-recorded 6-NN, walked in NN order."""
    recorded = already_recorded(site, ticks)
    collected: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in recorded:
            collected.extend(sorted(locks[neighbor]))
    return collected


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

    print("already-recorded 6-NN lock-sum reverse/face on four nnseed y-probes")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: Reverse and face from the sum of already-recorded 6-NN "
        "locks on the four nnseed y-probes are reported. Displayed, not adopted."
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
    checks.check(
        "host-is-euclidean-b3",
        ORIGIN in host and len(host) == 123 and BALL_SQ == 9,
    )
    checks.check(
        "y-probes-in-host",
        {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]} <= host,
    )
    checks.check(
        "perp-step-blocks-parallel",
        perpendicular(E1, E2)
        and not perpendicular(E2, E2)
        and in_ball(PROBES["C"])
        and not in_ball((0, 4, 0)),
    )

    ticks, locks = form()
    lists: dict[str, list[Point]] = {}
    letters: dict[str, Point | None] = {}
    leftovers: dict[str, Point | None] = {}
    for name, site in PROBES.items():
        collected = neighbor_lock_list(site, ticks, locks)
        lists[name] = collected
        letters[name] = letter_from_S(collected)
        leftovers[name] = leftover_unique_vector(site, ticks)
        print(
            f"{name} S={collected} L={letter_report(letters[name])} "
            f"t={ticks[site]} incoming={sorted(locks.get(site, ()))} "
            f"leftover={leftovers[name]}"
        )

    checks.check(
        "theorem1-A-undefined",
        lists["A"] == []
        and letters["A"] is None
        and letter_report(letters["A"]) == "UNDEFINED"
        and ticks[PROBES["A"]] == 0,
        letter_report(letters["A"]),
    )
    checks.check(
        "theorem1-B-sum",
        lists["B"] == [E3, E1]
        and letters["B"] == (1, 0, 1)
        and letters["B"] == vector_sum(lists["B"])
        and ticks[PROBES["B"]] == 2,
        str(letters["B"]),
    )
    checks.check(
        "theorem1-C-sum",
        lists["C"] == [E2, E2, E2, E2, E2]
        and letters["C"] == (0, 5, 0)
        and letters["C"] == vector_sum(lists["C"])
        and ticks[PROBES["C"]] == 3,
        str(letters["C"]),
    )
    checks.check(
        "theorem1-D-sum",
        lists["D"] == [E2]
        and letters["D"] == (0, 1, 0)
        and letters["D"] == vector_sum(lists["D"])
        and ticks[PROBES["D"]] == 1,
        str(letters["D"]),
    )
    checks.check(
        "theorem1-y-ticks-match-nsiso",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 1,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 4
        and len(locks[PROBES["D"]]) == 1,
        f"B={sorted(locks[PROBES['B']])} C={sorted(locks[PROBES['C']])}",
    )
    checks.check(
        "two-site-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2}
        and PROBES["A"] == E2,
    )

    formed_before_a = already_recorded(PROBES["A"], ticks)
    checks.check(
        "seed-excludes-same-tick-partner",
        ORIGIN not in formed_before_a
        and formed_before_a == frozenset()
        and ticks[ORIGIN] == ticks[PROBES["A"]] == 0
        and lists["A"] == [],
    )

    reverse_status = comparison_report(letters["A"], letters["B"])
    face_status = comparison_report(letters["C"], letters["D"])
    face_sum = (
        add(letters["C"], letters["D"])
        if letters["C"] is not None and letters["D"] is not None
        else None
    )
    print(f"reverse={reverse_status} face={face_status} face_sum={face_sum}")

    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and letters["A"] is None
        and letters["B"] == (1, 0, 1),
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and letters["C"] == (0, 5, 0)
        and letters["D"] == (0, 1, 0)
        and face_sum == (0, 6, 0)
        and face_sum != ZERO,
        face_status,
    )
    checks.check(
        "not-leftover-unique-vector",
        leftovers["A"] is None
        and leftovers["B"] is None
        and leftovers["C"] == E2
        and leftovers["D"] is None
        and leftovers["C"] != letters["C"]
        and letters["C"] == (0, 5, 0),
        str(leftovers["C"]),
    )
    checks.check(
        "letter-is-not-probe-incoming",
        letters["B"] not in locks[PROBES["B"]]
        and letters["C"] not in locks[PROBES["C"]]
        and letters["D"] not in locks[PROBES["D"]]
        and letters["A"] is None,
    )
    checks.check(
        "empty-S-is-undefined",
        letter_from_S([]) is None
        and letter_from_S([E2]) == E2
        and vector_sum([E2, E2, E2, E2, E2]) == (0, 5, 0),
    )

    same_tick_lists = lists["A"] + sorted(locks[ORIGIN])
    same_tick_letter = letter_from_S(same_tick_lists)
    checks.check(
        "mutation-same-tick-partner-defines-A",
        same_tick_letter == E1
        and letters["A"] is None
        and comparison_report(same_tick_letter, letters["B"]) == "fail"
        and reverse_status == "UNDEFINED",
        str(same_tick_letter),
    )
    leftover_face = comparison_report(leftovers["C"], letters["D"])
    leftover_sum = (
        add(leftovers["C"], letters["D"])
        if leftovers["C"] is not None and letters["D"] is not None
        else None
    )
    checks.check(
        "mutation-leftover-changes-letter",
        leftovers["C"] == E2
        and leftovers["C"] != letters["C"]
        and leftover_sum == (0, 2, 0)
        and leftover_sum != face_sum
        and leftover_face == "fail"
        and face_status == "fail",
        f"leftover_sum={leftover_sum} face_sum={face_sum}",
    )
    one_site_ticks, one_site_locks = form(seeds=((ORIGIN, E1),))
    one_site_lists = {
        name: neighbor_lock_list(PROBES[name], one_site_ticks, one_site_locks)
        for name in ("A", "B", "C", "D")
        if PROBES[name] in one_site_ticks
    }
    checks.check(
        "mutation-one-site-seed-changes-S",
        one_site_ticks[PROBES["A"]] != 0
        and one_site_lists["A"] != lists["A"]
        and letter_from_S(one_site_lists["A"]) is not None,
        str(one_site_lists.get("A")),
    )

    x_letters = {
        name: letter_from_S(neighbor_lock_list(site, ticks, locks))
        for name, site in X_PROBES.items()
    }
    x_reverse = comparison_report(x_letters["A"], x_letters["B"])
    x_face = comparison_report(x_letters["C"], x_letters["D"])
    checks.check(
        "x-probe-nfsum-is-fail-hold-not-this-display",
        x_reverse == "fail"
        and x_face == "hold"
        and add(x_letters["C"], x_letters["D"]) == ZERO
        and reverse_status == "UNDEFINED"
        and face_status == "fail"
        and x_letters["C"] != letters["C"],
        f"x_reverse={x_reverse} x_face={x_face}",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "not-t-as-comparator",
        reverse_status == "UNDEFINED"
        and face_status == "fail"
        and "3 t(" not in note,
    )
    checks.check(
        "a-is-seed-not-grown-incoming",
        ticks[PROBES["A"]] == 0
        and locks[PROBES["A"]] == {E2}
        and letters["A"] is None,
    )

    claim_scope = (
        "Reverse and face from the sum of already-recorded 6-NN "
        "locks on the four nnseed y-probes are reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-S-and-letters",
        "S(A_y) = empty" in note
        and "L(A_y) = UNDEFINED" in note
        and "L(B)   = (1, 0, 1)" in note
        and "L(C_y) = (0, 5, 0)" in note
        and "L(D_y) = (0, 1, 0)" in note
        and "S(B)   = (+e_3, +e_1)" in note
        and "S(D_y) = (+e_2)" in note,
    )
    checks.check(
        "note-reports-undefined-fail",
        note.count("Report: `UNDEFINED`.") == 1
        and note.count("Report: `fail`.") == 1
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-face-sum-not-zero",
        "L(C_y)+L(D_y) = (0, 6, 0) ≠ (0, 0, 0)." in note,
    )
    checks.check(
        "note-not-leftover-or-occupancy-or-pvm",
        "not a unique leftover vector" in normalized_note
        and "not occupancy-kernel `n`" in normalized_note
        and "not a named `{+,−}` PVM letter" in normalized_note,
    )
    checks.check(
        "note-y-ticks-nsiso",
        "t(A_y)=t(0,1,0)=0" in note
        and "t(B)=t(1,1,1)=2" in note
        and "t(C_y)=t(0,2,0)=3" in note
        and "t(D_y)=t(1,1,0)=1" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-same-tick-partner-rule",
        "same-tick partner is not already-recorded" in normalized_note
        and "Already-recorded means strictly earlier" in normalized_note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS)
        and "Do not attach" not in note,
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "does not supply the formation site, probability, or rate"
        in normalized_axiom,
    )
    checks.check(
        "note-quotes-current-premises",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
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
        '    "docs/NNSEED_YPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def form(" in source
        and "def already_recorded(" in source
        and "def neighbor_lock_list(" in source
        and "def vector_sum(" in source
        and "def letter_from_S(" in source
        and "def leftover_unique_vector(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
