#!/usr/bin/env python3
"""Existential opposite neighbor-lock reverse/face on four nnseed x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each probe's formation tick, S is the set of locks of already-
recorded six-neighbors. Reverse holds iff some a in S(A) and some b in S(B)
have a+b=(0,0,0). Face holds iff some c in S(C) and some d in S(D) have
c+d=(0,0,0). Empty S on either side is UNDEFINED; nonempty with no opposite
pair fails. Not unique-vector leftover. Not sum leftover. Not named-sign
lettering. Occupancy n is not used. The probe's own incoming lock is not
used. Uniqueness of incoming locks is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_NEIGHBOR_LOCK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_NEIGHBOR_LOCK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
LOCK_NAME = {
    E1: "+e_1",
    NEG_E1: "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
    E3: "+e_3",
    NEG_E3: "−e_3",
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
    "f(n)",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse and face from existential opposite already-recorded 6-NN "
    "locks on the four nnseed x-probes are reported. Displayed, not adopted."
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
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def recorded_lock_set(pairs: tuple[tuple[Point, Point], ...]) -> frozenset[Point]:
    """Set of already-recorded six-neighbor locks. Duplicates collapse."""
    return frozenset(lock for _neighbor, lock in pairs)


def existential_opposite(left: frozenset[Point], right: frozenset[Point]) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right.

    Empty set on either side is UNDEFINED. Nonempty with no opposite pair fails.
    Does not sum. Does not require a singleton.
    """
    if not left or not right:
        return "UNDEFINED"
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: frozenset[Point], set_b: frozenset[Point]) -> str:
    """Reverse iff some a in S(A) and some b in S(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point], set_d: frozenset[Point]) -> str:
    """Face iff some c in S(C) and some d in S(D) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


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

    print("existential opposite neighbor-lock reverse/face on nnseed x-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E2, E2) == ZERO
        and add(E1, E1) == (2, 0, 0)
        and add(E1, E3) == (1, 0, 1)
        and add(E1, E1) != ZERO
        and add(E1, E3) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold"
        and existential_opposite(frozenset({E2}), frozenset({NEG_E2})) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({NEG_E2})) == "fail"
        and existential_opposite(frozenset({E1, E2}), frozenset({NEG_E1, E3}))
        == "hold",
    )
    checks.check(
        "duplicates-collapse-in-set",
        recorded_lock_set(((ORIGIN, E1), (PROBES["D"], E1))) == frozenset({E1})
        and recorded_lock_set(((ORIGIN, E1), ((0, 1, 1), E3))) == frozenset({E1, E3}),
    )
    checks.check(
        "mixed-remains-a-set",
        recorded_lock_set((((0, 1, 1), E3), (PROBES["D"], E1))) == frozenset({E1, E3})
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and len(frozenset({E1, E3})) != 1,
    )
    checks.check(
        "not-named-sign-reduction",
        named_sign(E1) == named_sign(E3) == "+"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and named_sign(NEG_E2) != named_sign(E2)
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "not-unique-vector-leftover",
        existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(frozenset({E1, E2}), frozenset({NEG_E1, E3}))
        == "hold"
        and len(frozenset({E1, E3})) != 1
        and len(frozenset({E1, E2})) != 1,
    )
    checks.check(
        "not-sum-leftover",
        add(E1, E1) == (2, 0, 0)
        and add(E1, E3) == (1, 0, 1)
        and add((2, 0, 0), (1, 0, 1)) != ZERO
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(frozenset({E1, E2}), frozenset({NEG_E1, E3}))
        == "hold"
        and add(add(E1, E2), add(NEG_E1, E3)) != ZERO,
    )
    checks.check(
        "reverse-face-identity",
        reverse_report(frozenset(), frozenset({NEG_E2})) == "UNDEFINED"
        and reverse_report(frozenset({E1}), frozenset()) == "UNDEFINED"
        and reverse_report(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and reverse_report(frozenset({E1}), frozenset({E1})) == "fail"
        and reverse_report(frozenset({E1}), frozenset({E2})) == "fail"
        and reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and face_report(frozenset({NEG_E2}), frozenset({E2})) == "hold"
        and face_report(frozenset({E2}), frozenset({NEG_E2})) == "hold"
        and face_report(frozenset({NEG_E2}), frozenset({NEG_E2})) == "fail"
        and face_report(frozenset(), frozenset({E2})) == "UNDEFINED"
        and face_report(frozenset({NEG_E2}), frozenset()) == "UNDEFINED",
    )

    ticks, locks = form()
    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    lock_sets: dict[str, frozenset[Point]] = {}
    for name, site in PROBES.items():
        pairs = recorded_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        lock_sets[name] = recorded_lock_set(pairs)
        lock_text = ", ".join(
            f"{lock_display(lock)} at {neighbor}" for neighbor, lock in pairs
        )
        incoming = ",".join(lock_display(step) for step in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} recorded-neighbor-locks=[{lock_text}] "
            f"S={set_display(lock_sets[name])} incoming={incoming}"
        )

    reverse_status = reverse_report(lock_sets["A"], lock_sets["B"])
    face_status = face_report(lock_sets["C"], lock_sets["D"])
    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "theorem1-A-neighbor-lock-set",
        neighbor_lists["A"] == ((ORIGIN, E1), (PROBES["D"], E1))
        and lock_sets["A"] == frozenset({E1}),
        str((neighbor_lists["A"], lock_sets["A"])),
    )
    checks.check(
        "theorem1-B-neighbor-lock-set",
        neighbor_lists["B"] == (((0, 1, 1), E3), (PROBES["D"], E1))
        and lock_sets["B"] == frozenset({E1, E3}),
        str((neighbor_lists["B"], lock_sets["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-set",
        neighbor_lists["C"] == ((PROBES["A"], NEG_E2),)
        and lock_sets["C"] == frozenset({NEG_E2}),
        str((neighbor_lists["C"], lock_sets["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-set",
        neighbor_lists["D"] == ((E2, E2),) and lock_sets["D"] == frozenset({E2}),
        str((neighbor_lists["D"], lock_sets["D"])),
    )
    checks.check(
        "theorem1-B-mixed-vectors-remain-a-set",
        lock_sets["B"] == frozenset({E1, E3})
        and {lock for _n, lock in neighbor_lists["B"]} == {E1, E3}
        and named_sign(E1) == named_sign(E3) == "+",
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and lock_sets["A"] == frozenset({E1})
        and lock_sets["B"] == frozenset({E1, E3})
        and add(E1, E1) != ZERO
        and add(E1, E3) != ZERO
        and lock_sets["A"]
        and lock_sets["B"],
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and lock_sets["C"] == frozenset({NEG_E2})
        and lock_sets["D"] == frozenset({E2})
        and add(NEG_E2, E2) == ZERO,
        face_status,
    )
    checks.check(
        "sign-lettering-loses-axis-and-fails-face",
        named_sign(NEG_E2) == "-"
        and named_sign(E2) == "+"
        and not (named_sign(NEG_E2) == "+" and named_sign(E2) == "-")
        and face_status == "hold",
    )
    checks.check(
        "not-self-incoming-nnlock",
        locks[PROBES["C"]] == {E1}
        and locks[PROBES["D"]] == {E1}
        and lock_sets["C"] == frozenset({NEG_E2})
        and lock_sets["D"] == frozenset({E2}),
    )
    checks.check(
        "not-probe-own-incoming-lock",
        locks[PROBES["A"]] == {NEG_E2}
        and lock_sets["A"] == frozenset({E1})
        and NEG_E2 not in lock_sets["A"],
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2 and lock_sets["B"] == frozenset({E1, E3}),
        str(sorted(locks[PROBES["B"]])),
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
        "mutation-empty-neighbor-locks-undefined",
        recorded_lock_set(()) == frozenset()
        and reverse_report(frozenset(), lock_sets["B"]) == "UNDEFINED"
        and face_report(lock_sets["C"], frozenset()) == "UNDEFINED",
    )
    checks.check(
        "mutation-mixed-neighbor-vectors-fail-without-opposite",
        recorded_lock_set((((0, 1, 1), E3), (PROBES["D"], E1))) == frozenset({E1, E3})
        and reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-sets",
        "S(A) = {+e_1}" in note
        and "S(B) = {+e_1, +e_3}" in note
        and "S(C) = {−e_2}" in note
        and "S(D) = {+e_2}" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_1 at (1, 1, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "−e_2 at (1, 0, 0)" in note
        and "+e_2 at (0, 1, 0)" in note,
    )
    checks.check(
        "note-reports-fail-hold",
        "Reverse: fail" in note
        and "Face: hold" in note
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
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note
        and "C−/D+" in note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "incoming step" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-not-unique-or-sum-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "No aggregation of `B`'s `{+e_1,+e_3}` is opposite `A`'s" in note,
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
        '    "docs/NNSEED_NEIGHBOR_LOCK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
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
        "source-letter-from-existential-opposite-only",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "recorded_neighbor_locks" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
