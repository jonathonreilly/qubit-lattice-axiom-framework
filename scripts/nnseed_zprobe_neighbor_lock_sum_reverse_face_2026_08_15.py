#!/usr/bin/env python3
"""Sum of already-recorded 6-NN locks on four nnseed z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's formation tick, S is the list of locks of
already-recorded six-neighbors. If S is empty, the letter is UNDEFINED; else
the letter is the vector sum of S in Z^3. Reverse holds iff L(A) and L(B) are
defined and L(A)+L(B)=(0,0,0). Face holds iff L(C) and L(D) are defined and
L(C)+L(D)=(0,0,0). Occupancy n is not used. The probe's own incoming lock is
not used. Uniqueness of incoming locks is not required. Not unique f(n).
Not ndot. Not named sign. Not the unique-vector singleton leftover.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_ZPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_ZPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
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
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (0, 1, 1),
}
X_PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
LOCK_NAME = {
    E1: "+e_1",
    (-1, 0, 0): "−e_1",
    E2: "+e_2",
    (0, -1, 0): "−e_2",
    E3: "+e_3",
    (0, 0, -1): "−e_3",
}
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "16-census",
    "16-letter",
    "L1",
    "Runner cache",
)
CLAIM_SCOPE = (
    "Reverse and face from the sum of already-recorded 6-NN "
    "locks on the four nnseed z-probes are reported. Displayed, not adopted."
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


def sum_from_neighbor_locks(locks: tuple[Point, ...]) -> Letter:
    """Vector sum of recorded-neighbor locks, or UNDEFINED if the list is empty."""
    if not locks:
        return "UNDEFINED"
    total = ORIGIN
    for lock in locks:
        total = add(total, lock)
    return total


def reverse_report(letter_a: Letter, letter_b: Letter) -> str:
    """Reverse iff L(A)+L(B)=(0,0,0). UNDEFINED if a needed vector is UNDEFINED."""
    if letter_a == "UNDEFINED" or letter_b == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter_a, tuple) or not isinstance(letter_b, tuple):
        return "UNDEFINED"
    holds = add(letter_a, letter_b) == ORIGIN
    return "hold" if holds else "fail"


def face_report(letter_c: Letter, letter_d: Letter) -> str:
    """Face iff L(C)+L(D)=(0,0,0). UNDEFINED if a needed vector is UNDEFINED."""
    if letter_c == "UNDEFINED" or letter_d == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter_c, tuple) or not isinstance(letter_d, tuple):
        return "UNDEFINED"
    holds = add(letter_c, letter_d) == ORIGIN
    return "hold" if holds else "fail"


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if isinstance(letter, tuple):
        return str(letter)
    return str(letter)


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


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


def recorded_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Locks of already-recorded six-neighbors at the formation tick of site."""
    formation = ticks[site]
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        if ticks[neighbor] >= formation:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


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

    print("sum of already-recorded 6-NN locks on nnseed z-probes")
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

    host = ball_sites()
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )
    checks.check(
        "z-probes-are-not-x-probes",
        probe_sites != x_probe_sites
        and x_probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0)),
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "sum-identity-from-neighbor-locks",
        sum_from_neighbor_locks((E1,)) == E1
        and sum_from_neighbor_locks((E1, E1)) == (2, 0, 0)
        and sum_from_neighbor_locks(((0, -1, 0),)) == (0, -1, 0)
        and sum_from_neighbor_locks((E1, E2)) == (1, 1, 0)
        and sum_from_neighbor_locks((E1, E3)) == (1, 0, 1)
        and sum_from_neighbor_locks((E1, (-1, 0, 0))) == ORIGIN
        and sum_from_neighbor_locks((E3, E3, E3, E3)) == (0, 0, 4)
        and sum_from_neighbor_locks(()) == "UNDEFINED",
    )
    checks.check(
        "mixed-locks-have-a-sum-not-undefined",
        sum_from_neighbor_locks((E1, E3)) == (1, 0, 1)
        and sum_from_neighbor_locks((E1, E2)) == (1, 1, 0)
        and sum_from_neighbor_locks((E1, E3)) != "UNDEFINED",
    )
    checks.check(
        "multiplicity-is-kept-in-the-sum",
        sum_from_neighbor_locks((E3, E3, E3, E3)) == (0, 0, 4)
        and sum_from_neighbor_locks((E3,)) == E3
        and sum_from_neighbor_locks((E3, E3, E3, E3)) != E3,
    )
    checks.check(
        "reverse-face-undefined-when-sum-undefined",
        reverse_report("UNDEFINED", (-1, 0, 0)) == "UNDEFINED"
        and reverse_report(E1, "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", (0, -1, 0)) == "UNDEFINED"
        and face_report(E3, "UNDEFINED") == "UNDEFINED"
        and reverse_report(E1, (-1, 0, 0)) == "hold"
        and reverse_report(E1, E2) == "fail"
        and reverse_report(E1, E1) == "fail"
        and reverse_report(E1, (1, 0, 1)) == "fail"
        and face_report(E3, (0, 0, -1)) == "hold"
        and face_report((0, 0, 4), E2) == "fail"
        and face_report(E3, E3) == "fail",
    )

    ticks, locks = form()
    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    letters: dict[str, Letter] = {}
    for name, site in PROBES.items():
        pairs = recorded_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        letter = sum_from_neighbor_locks(tuple(lock for _n, lock in pairs))
        letters[name] = letter
        lock_text = ", ".join(
            f"{lock_display(lock)} at {neighbor}" for neighbor, lock in pairs
        )
        incoming = ",".join(lock_display(step) for step in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} recorded-neighbor-locks=[{lock_text}] "
            f"L={letter_display(letter)} incoming={incoming}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    print(f"reverse={reverse_status} face={face_status}")

    incoming_c_sum = sum_from_neighbor_locks(tuple(sorted(locks[PROBES["C"]])))
    checks.check(
        "theorem1-A-neighbor-lock-list-and-sum",
        neighbor_lists["A"] == ((ORIGIN, E1),) and letters["A"] == E1,
        str((neighbor_lists["A"], letters["A"])),
    )
    checks.check(
        "theorem1-B-neighbor-lock-list-and-sum",
        neighbor_lists["B"] == ((PROBES["D"], E3), (X_PROBES["D"], E1))
        and letters["B"] == (1, 0, 1),
        str((neighbor_lists["B"], letters["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-list-and-sum",
        neighbor_lists["C"]
        == (
            ((1, 0, 2), E3),
            ((-1, 0, 2), E3),
            ((0, -1, 2), E3),
            (PROBES["A"], E3),
        )
        and letters["C"] == (0, 0, 4),
        str((neighbor_lists["C"], letters["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-list-and-sum",
        neighbor_lists["D"] == ((E2, E2),) and letters["D"] == E2,
        str((neighbor_lists["D"], letters["D"])),
    )
    checks.check(
        "theorem1-sums-e1-mixed-four-e3-e2",
        letters["A"] == E1
        and letters["B"] == (1, 0, 1)
        and letters["C"] == (0, 0, 4)
        and letters["D"] == E2,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 1,
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and letters["A"] == E1
        and letters["B"] == (1, 0, 1)
        and add(E1, (1, 0, 1)) == (2, 0, 1)
        and add(E1, (1, 0, 1)) != ORIGIN,
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and letters["C"] == (0, 0, 4)
        and letters["D"] == E2
        and add((0, 0, 4), E2) == (0, 1, 4)
        and add((0, 0, 4), E2) != ORIGIN,
        face_status,
    )
    checks.check(
        "not-self-incoming-at-C",
        locks[PROBES["C"]] == {(-1, 0, 0), E2, E1}
        and incoming_c_sum == E2
        and letters["C"] == (0, 0, 4)
        and incoming_c_sum != letters["C"],
        incoming_c_sum,
    )
    checks.check(
        "not-probe-own-incoming-as-sum-source",
        locks[PROBES["A"]] == {E3}
        and letters["A"] == E1
        and letters["A"] != next(iter(locks[PROBES["A"]]))
        and incoming_c_sum != letters["C"],
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-sign-letters",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 3
        and letters["B"] == (1, 0, 1)
        and letters["C"] == (0, 0, 4),
        str((sorted(locks[PROBES["B"]]), sorted(locks[PROBES["C"]]))),
    )
    checks.check(
        "two-site-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2},
    )
    checks.check(
        "already-recorded-not-self-or-later",
        all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
        and all(
            ticks[neighbor] < ticks[PROBES[name]]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        ),
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "no-sixteen-combo-census",
        reverse_status == "fail"
        and face_status == "fail"
        and reverse_status != "some"
        and face_status != "some",
    )
    checks.check(
        "not-unique-vector-leftover",
        letters["B"] == (1, 0, 1)
        and letters["B"] != "UNDEFINED"
        and letters["C"] == (0, 0, 4)
        and letters["C"] != E3
        and reverse_status == "fail"
        and reverse_status != "UNDEFINED",
    )
    checks.check(
        "not-named-sign-leftover-all-plus",
        letters["B"] == (1, 0, 1)
        and letters["A"] == E1
        and letters["C"] == (0, 0, 4)
        and letters["D"] == E2,
    )
    checks.check(
        "mutation-empty-neighbor-locks-undefined",
        sum_from_neighbor_locks(()) == "UNDEFINED"
        and reverse_report("UNDEFINED", letters["D"] if isinstance(letters["D"], tuple) else E2)
        == "UNDEFINED"
        and face_report(letters["C"], "UNDEFINED") == "UNDEFINED",
    )
    checks.check(
        "mutation-mixed-neighbor-vectors-still-sum",
        sum_from_neighbor_locks((E1, E3)) == (1, 0, 1)
        and reverse_report((1, 0, 1), E1) == "fail",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-lists-and-sums",
        "L(A) = (1, 0, 0)" in note
        and "L(B) = (1, 0, 1)" in note
        and "L(C) = (0, 0, 4)" in note
        and "L(D) = (0, 1, 0)" in note
        and "S = (+e_1)" in note
        and "S = (+e_3, +e_1)" in note
        and "S = (+e_3, +e_3, +e_3, +e_3)" in note
        and "S = (+e_2)" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "+e_1 at (1, 1, 0)" in note
        and "+e_3 at (1, 0, 2)" in note
        and "+e_3 at (-1, 0, 2)" in note
        and "+e_3 at (0, -1, 2)" in note
        and "+e_3 at (0, 0, 1)" in note
        and "+e_2 at (0, 1, 0)" in note,
    )
    checks.check(
        "note-reports-fail-fail",
        note.count("Report: `fail`.") == 2
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-does-not-use-occupancy-or-incoming",
        "does not use occupancy" in normalized_note
        and "does not use the probe" in normalized_note
        and "own incoming lock" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "incoming step" in normalized_note,
    )
    checks.check(
        "note-not-unique-fn-or-ndot",
        "not unique `f(n)`" in note and "not ndot" in note,
    )
    checks.check(
        "note-not-unique-vector-leftover",
        "not the unique-vector singleton leftover" in normalized_note
        and "L(B)=(1,0,1)" in note.replace(" ", "")
        and "L(C)=(0,0,4)" in note.replace(" ", ""),
    )
    checks.check(
        "note-not-named-sign",
        "not named sign" in normalized_note
        and "Named signs" in note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor lock sums"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-not-sixteen-free-letters",
        "not a sixteen-combination free lettering" in normalized_note
        and "16-census" not in note
        and "16-letter" not in note,
    )
    checks.check(
        "note-not-occupancy-letter-or-self-incoming",
        "not a unique letter of occupancy" in normalized_note
        and "self-incoming" in normalized_note,
    )
    checks.check(
        "note-not-x-probe-reprint",
        "not the x-probes" in normalized_note
        and "A = (0,0,1)" in note,
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
        '    "docs/NNSEED_ZPROBE_NEIGHBOR_LOCK_SUM_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def sum_from_neighbor_locks(" in source
        and "def recorded_neighbor_locks(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] >= 1
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-sum-from-neighbor-locks-only",
        "sum_from_neighbor_locks" in defined_fns
        and "recorded_neighbor_locks" in defined_fns
        and "named_sign" not in defined_fns
        and "unique_vector_from_neighbor_locks" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and not any("ndot" in name for name in defined_fns),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
