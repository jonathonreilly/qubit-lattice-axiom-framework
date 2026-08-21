#!/usr/bin/env python3
"""Plaquette opposite-vertex holonomy reverse/face on nnseed Q and R.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_2. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. The letter at a recorded site is that site's own incoming lock in
{±e_i}; seeds use their seed letters. Face is scored on the seed-square
Q={0,(1,0,0),(1,1,0),(0,1,0)} at the first tick all four sites are recorded.
Reverse is scored on the 4-cycle R containing A=(1,0,0) and B=(1,1,1) at
T_R=min(t(A),t(B)). Face and reverse hold iff opposite vertices have opposite
locks. Uniqueness of incoming locks is not required. Not a leftover of star
aggregation of six-neighbor lock lists. Occupancy n is not used.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_PLAQUETTE_HOLONOMY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_PLAQUETTE_HOLONOMY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E2: Point = (0, -1, 0)
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    NEG_E2,
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
PROBE_A: Point = (1, 0, 0)
PROBE_B: Point = (1, 1, 1)
Q_CYCLE: tuple[Point, ...] = (ORIGIN, E1, (1, 1, 0), E2)
R_CYCLE: tuple[Point, ...] = (PROBE_A, (1, 1, 0), PROBE_B, (1, 0, 1))
LOCK_NAME = {
    E1: "+e_1",
    (-1, 0, 0): "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
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
    "unique P_+",
    "6-NN star",
)
CLAIM_SCOPE = (
    "Reverse and face from plaquette opposite-vertex holonomy "
    "on the nnseed seed-square Q and on the 4-cycle R containing "
    "A and B are reported. Displayed, not adopted."
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


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def incoming_display(incoming: frozenset[Point]) -> str:
    return ", ".join(lock_display(lock) for lock in sorted(incoming))


def own_incoming_letter(incoming: frozenset[Point] | None) -> Letter:
    """Letter is the site's unique incoming lock, or NONUNIQUE/MISSING."""
    if incoming is None:
        return "MISSING"
    if len(incoming) == 1:
        return next(iter(incoming))
    return "NONUNIQUE"


def letter_display(letter: Letter) -> str:
    if letter in {"MISSING", "NONUNIQUE", "UNDEFINED"}:
        return str(letter)
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not an incoming lock: {letter!r}")
    return LOCK_NAME.get(letter, str(letter))


def cycle_holonomy(letters: tuple[Letter, ...]) -> Letter:
    """Cycle sum of unique incoming locks, else UNDEFINED."""
    total = ZERO
    for letter in letters:
        if not isinstance(letter, tuple):
            return "UNDEFINED"
        total = add(total, letter)
    return total


def opposite_vertex_status(letters: tuple[Letter, ...]) -> str:
    """Hold iff both opposite pairs of unique locks sum to zero."""
    if len(letters) != 4:
        raise ValueError("cycle must have four letters")
    if any(letter == "MISSING" for letter in letters):
        return "UNDEFINED"
    first = letters[0]
    second = letters[1]
    third = letters[2]
    fourth = letters[3]
    if not all(isinstance(item, tuple) for item in (first, second, third, fourth)):
        return "fail"
    if add(first, third) == ZERO and add(second, fourth) == ZERO:
        return "hold"
    return "fail"


def reverse_report(letters: tuple[Letter, ...]) -> str:
    """Reverse on R: opposite vertices have opposite unique incoming locks."""
    return opposite_vertex_status(letters)


def face_report(letters: tuple[Letter, ...]) -> str:
    """Face on Q: opposite vertices have opposite unique incoming locks."""
    return opposite_vertex_status(letters)


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


def cycle_letters(
    cycle: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    *,
    deadline: int | None,
) -> tuple[Letter, ...]:
    """Own-incoming letters on a 4-cycle, MISSING if unrecorded by deadline."""
    letters: list[Letter] = []
    for site in cycle:
        if site not in ticks:
            letters.append("MISSING")
            continue
        if deadline is not None and ticks[site] > deadline:
            letters.append("MISSING")
            continue
        letters.append(own_incoming_letter(frozenset(locks[site])))
    return tuple(letters)


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

    print("plaquette opposite-vertex holonomy reverse/face on nnseed Q and R")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "q-and-r-in-host",
        Q_CYCLE == (ORIGIN, E1, (1, 1, 0), E2)
        and R_CYCLE == (PROBE_A, (1, 1, 0), PROBE_B, (1, 0, 1))
        and set(Q_CYCLE) <= host
        and set(R_CYCLE) <= host
        and PROBE_A in Q_CYCLE
        and PROBE_A in R_CYCLE
        and PROBE_B in R_CYCLE
        and PROBE_B not in Q_CYCLE,
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
        and (2, 0, 0) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBE_B)
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "own-incoming-letter-identity",
        own_incoming_letter(frozenset({E1})) == E1
        and own_incoming_letter(frozenset({NEG_E2})) == NEG_E2
        and own_incoming_letter(frozenset({E1, E3})) == "NONUNIQUE"
        and own_incoming_letter(None) == "MISSING",
    )
    checks.check(
        "holonomy-identity",
        cycle_holonomy((E1, NEG_E2, E1, E2)) == (2, 0, 0)
        and cycle_holonomy((E1, E2, (-1, 0, 0), NEG_E2)) == ZERO
        and cycle_holonomy((E1, NEG_E2, "NONUNIQUE", E2)) == "UNDEFINED"
        and cycle_holonomy((E1, "MISSING", E1, E2)) == "UNDEFINED",
    )
    checks.check(
        "reverse-face-identity",
        reverse_report((NEG_E2, E1, E2, (-1, 0, 0))) == "hold"
        and reverse_report((NEG_E2, E1, "NONUNIQUE", E1)) == "fail"
        and reverse_report(("MISSING", E1, E1, E1)) == "UNDEFINED"
        and face_report((E1, NEG_E2, E1, E2)) == "fail"
        and face_report((E1, NEG_E2, (-1, 0, 0), E2)) == "hold"
        and face_report(("MISSING", NEG_E2, E1, E2)) == "UNDEFINED"
        and add(E1, E1) == (2, 0, 0)
        and add(NEG_E2, E2) == ZERO,
    )

    ticks, locks = form()
    t_a = ticks[PROBE_A]
    t_b = ticks[PROBE_B]
    t_q = max(ticks[site] for site in Q_CYCLE)
    t_r = min(t_a, t_b)
    q_incoming = tuple(frozenset(locks[site]) for site in Q_CYCLE)
    r_incoming = tuple(
        frozenset(locks[site]) if site in ticks and ticks[site] <= t_r else None
        for site in R_CYCLE
    )
    q_letters = cycle_letters(Q_CYCLE, ticks, locks, deadline=t_q)
    r_letters = cycle_letters(R_CYCLE, ticks, locks, deadline=t_r)
    holonomy = cycle_holonomy(q_letters)
    reverse_status = reverse_report(r_letters)
    face_status = face_report(q_letters)

    print(f"T_Q={t_q} T_R={t_r} t(A)={t_a} t(B)={t_b}")
    for name, site, incoming, letter in zip(
        ("0", "e_1", "e_1+e_2", "e_2"), Q_CYCLE, q_incoming, q_letters, strict=True
    ):
        print(
            f"Q {name} {site} t={ticks[site]} "
            f"incoming=[{incoming_display(incoming)}] L={letter_display(letter)}"
        )
    print(f"H={holonomy}")
    for name, site, incoming, letter in zip(
        ("A", "(1,1,0)", "B", "(1,0,1)"),
        R_CYCLE,
        r_incoming,
        r_letters,
        strict=True,
    ):
        if incoming is None:
            incoming_text = "MISSING"
        else:
            incoming_text = incoming_display(incoming)
        print(
            f"R {name} {site} t={ticks.get(site, 'MISSING')} "
            f"incoming=[{incoming_text}] L={letter_display(letter)}"
        )
    print(f"reverse={reverse_status} face={face_status}")

    checks.check(
        "theorem1-TQ-four-locks-on-Q-and-H",
        t_q == 2
        and q_letters == (E1, NEG_E2, E1, E2)
        and q_incoming == (
            frozenset({E1}),
            frozenset({NEG_E2}),
            frozenset({E1}),
            frozenset({E2}),
        )
        and holonomy == (2, 0, 0),
        str((t_q, q_letters, holonomy)),
    )
    checks.check(
        "theorem1-TR-four-locks-on-R",
        t_r == 2
        and t_r == min(t_a, t_b)
        and r_letters == (NEG_E2, E1, "NONUNIQUE", E1)
        and r_incoming == (
            frozenset({NEG_E2}),
            frozenset({E1}),
            frozenset({E1, E3}),
            frozenset({E1}),
        )
        and all(site in ticks and ticks[site] <= t_r for site in R_CYCLE),
        str((t_r, r_letters, tuple(sorted(locks[PROBE_B])))),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and r_letters[0] == NEG_E2
        and r_letters[2] == "NONUNIQUE"
        and add(E1, E1) != ZERO
        and all(site in ticks for site in R_CYCLE),
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and q_letters == (E1, NEG_E2, E1, E2)
        and add(E1, E1) == (2, 0, 0)
        and add(NEG_E2, E2) == ZERO
        and holonomy == (2, 0, 0)
        and all(site in ticks for site in Q_CYCLE),
        face_status,
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBE_B]) == 2
        and r_letters[2] == "NONUNIQUE"
        and reverse_status == "fail",
        str(sorted(locks[PROBE_B])),
    )
    checks.check(
        "two-site-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E2}
        and q_letters[0] == E1
        and q_letters[3] == E2,
    )
    checks.check(
        "letter-is-own-incoming-not-star-sum",
        q_letters[1] == NEG_E2
        and locks[PROBE_A] == {NEG_E2}
        and q_letters[1] == next(iter(locks[PROBE_A]))
        and holonomy != (5, 0, 0)
        and holonomy == (2, 0, 0),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[site] <= set(NN) for site in Q_CYCLE)
        and all(locks[site] <= set(NN) for site in R_CYCLE),
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
        "mutation-unrecorded-undefined",
        reverse_report(("MISSING", E1, E1, E1)) == "UNDEFINED"
        and face_report((E1, NEG_E2, "MISSING", E2)) == "UNDEFINED"
        and opposite_vertex_status(("MISSING", NEG_E2, E1, E2)) == "UNDEFINED",
    )
    checks.check(
        "mutation-nonunique-recorded-fails",
        reverse_report((NEG_E2, E1, "NONUNIQUE", E1)) == "fail"
        and reverse_status == "fail",
    )
    checks.check(
        "first-tick-all-Q-recorded",
        t_q == 2
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and ticks[(1, 1, 0)] == 1
        and ticks[E1] == 2
        and max(ticks[site] for site in Q_CYCLE if ticks[site] < t_q) == 1,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and t_a >= 1
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-own-incoming-only",
        "own_incoming_letter" in defined_fns
        and "cycle_holonomy" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "neighbor_lock_pairs" not in defined_fns
        and "sum_letter" not in defined_fns,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-TQ-locks-H",
        "T_Q = 2" in note
        and "L(0) = +e_1" in note
        and "L(e_1) = −e_2" in note
        and "L(e_1+e_2) = +e_1" in note
        and "L(e_2) = +e_2" in note
        and "H = (2, 0, 0)" in note,
    )
    checks.check(
        "note-reports-TR-R-locks",
        "T_R = 2" in note
        and "L(A) = −e_2" in note
        and "L(1,1,0) = +e_1" in note
        and "L(B) = +e_1, +e_3" in note
        and "L(1,0,1) = +e_1" in note,
    )
    checks.check(
        "note-reports-fail-fail",
        "Reverse: fail" in note
        and "Face: fail" in note
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
        "note-not-star-aggregation",
        "not a leftover of star aggregation of six-neighbor lock lists"
        in normalized_note
        and "own incoming lock" in normalized_note
        and "seed-square" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation",
        "does not attach a formation member from plaquette opposite-vertex holonomy"
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
        '    "docs/NNSEED_PLAQUETTE_HOLONOMY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def own_incoming_letter(" in source
        and "def cycle_holonomy(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
