#!/usr/bin/env python3
"""Own unique incoming lock vector reverse/face on four opposite-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1 (the opposite-lock two-site seed).
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters.
A is a seed site and uses its seed letter -e_1. The unique letter at a formed
probe is that probe's own unique earliest incoming lock in {±e_i}; if several
earliest incoming steps exist, the letter is UNDEFINED. Reverse holds iff
L(A) and L(B) are defined and L(A)+L(B)=(0,0,0). Face holds iff L(C) and
L(D) are defined and L(C)+L(D)=(0,0,0). Already-recorded six-neighbor locks
are not the letter. Occupancy n is not used. Named-sign lettering is not
used. A six-neighbor star is not used. Uniqueness of incoming locks is not
required. This is not leftover of the y-probe neighbor-lock lists. This is
not the four opposite-lock x-probes. This seed is not the perp two-site seed
+e_1/+e_2.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
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
    "Reverse and face from the probe's own unique incoming lock "
    "vector on the four opposite-lock y-probes are reported. Displayed, not adopted."
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
    """Named sign of a lock vector. Contrast only; not the unique letter."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point]) -> Letter:
    """Unique letter if the probe's own earliest incoming locks are a singleton in NN."""
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def comparison_report(left: Letter, right: Letter) -> str:
    """Hold iff both letters are defined lock vectors that sum to zero."""
    if left == "UNDEFINED" or right == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(left, tuple) or not isinstance(right, tuple):
        return "UNDEFINED"
    if add(left, right) == ZERO:
        return "hold"
    return "fail"


def reverse_report(letter_a: Letter, letter_b: Letter) -> str:
    """Reverse iff L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)."""
    return comparison_report(letter_a, letter_b)


def face_report(letter_c: Letter, letter_d: Letter) -> str:
    """Face iff L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)."""
    return comparison_report(letter_c, letter_d)


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


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

    print("own unique incoming lock vector reverse/face on opposite-lock y-probes")
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
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(NEG_E1, E2)
        and not perpendicular(E1, E1)
        and not perpendicular(NEG_E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((NEG_E2,)) == NEG_E2
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((E1, E3)) == "UNDEFINED"
        and unique_own_incoming_letter((E2, NEG_E2)) == "UNDEFINED"
        and unique_own_incoming_letter((E2, E3, NEG_E3)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )
    checks.check(
        "reverse-face-identity",
        reverse_report(NEG_E1, E1) == "hold"
        and reverse_report(E1, E1) == "fail"
        and reverse_report("UNDEFINED", E1) == "UNDEFINED"
        and reverse_report(E1, "UNDEFINED") == "UNDEFINED"
        and face_report(E1, E1) == "fail"
        and face_report(NEG_E2, E2) == "hold"
        and face_report("UNDEFINED", E1) == "UNDEFINED"
        and face_report(E1, "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "UNDEFINED") == "UNDEFINED",
    )

    ticks, locks = form()
    perp_ticks, perp_locks = form(PERP_SEEDS)
    letters: dict[str, Letter] = {}
    incoming_sets: dict[str, frozenset[Point]] = {}
    for name, site in PROBES.items():
        incoming = frozenset(locks[site])
        incoming_sets[name] = incoming
        letter = unique_own_incoming_letter(incoming)
        letters[name] = letter
        incoming_text = ",".join(lock_display(step) for step in sorted(incoming))
        print(
            f"{name} t={ticks[site]} incoming=[{incoming_text}] "
            f"L={letter_display(letter)}"
        )

    x_letters = {
        name: unique_own_incoming_letter(locks[site])
        for name, site in X_PROBES.items()
    }
    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    x_reverse = reverse_report(x_letters["A"], x_letters["B"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: unique letter is the probe's own singleton earliest "
        "incoming lock vector in {±e_i}, else UNDEFINED"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four unique lock vectors plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    checks.check(
        "theorem1-A-own-incoming-letter",
        incoming_sets["A"] == frozenset({NEG_E1}) and letters["A"] == NEG_E1,
        str((sorted(incoming_sets["A"]), letters["A"])),
    )
    checks.check(
        "theorem1-B-own-incoming-letter",
        incoming_sets["B"] == frozenset({E1}) and letters["B"] == E1,
        str((sorted(incoming_sets["B"]), letters["B"])),
    )
    checks.check(
        "theorem1-C-own-incoming-letter",
        incoming_sets["C"] == frozenset({E2}) and letters["C"] == E2,
        str((sorted(incoming_sets["C"]), letters["C"])),
    )
    checks.check(
        "theorem1-D-own-incoming-letter",
        incoming_sets["D"] == frozenset({NEG_E2, NEG_E3, E3})
        and letters["D"] == "UNDEFINED",
        str((sorted(incoming_sets["D"]), letters["D"])),
    )
    checks.check(
        "theorem1-A-is-seed-letter",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and letters["A"] == NEG_E1,
    )
    checks.check(
        "theorem1-D-mixed-incoming-not-singleton",
        letters["D"] == "UNDEFINED"
        and incoming_sets["D"] == frozenset({NEG_E2, NEG_E3, E3}),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and letters["A"] == NEG_E1
        and letters["B"] == E1
        and add(NEG_E1, E1) == ZERO
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and letters["C"] == E2
        and letters["D"] == "UNDEFINED"
        and face_status != "hold"
        and face_status != "fail",
        face_status,
    )
    checks.check(
        "not-nsopy-neighbor-lock-leftover",
        letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and reverse_status == "hold"
        and reverse_status != "UNDEFINED"
        and letters["A"] != "UNDEFINED"
        and letters["B"] != E3
        and letters["C"] != NEG_E1,
    )
    checks.check(
        "not-nsopown-x-probes",
        PROBES["A"] != X_PROBES["A"]
        and PROBES["C"] != X_PROBES["C"]
        and x_letters["A"] == "UNDEFINED"
        and x_letters["B"] == E1
        and x_letters["C"] == E1
        and x_letters["D"] == "UNDEFINED"
        and x_reverse == "UNDEFINED"
        and reverse_status == "hold"
        and reverse_status != "UNDEFINED",
    )
    checks.check(
        "not-ownvec-nnseed",
        TWO_SITE_SEEDS != PERP_SEEDS
        and locks[E2] == {NEG_E1}
        and perp_locks[E2] == {E2}
        and ticks[PROBES["A"]] == 0
        and perp_ticks[PROBES["A"]] == 0
        and letters["A"] != E2
        and letters["D"] != E1
        and face_status != "fail",
    )
    checks.check(
        "not-nnlock-named-sign",
        letters["A"] == NEG_E1
        and named_sign(NEG_E1) == "-"
        and letters["B"] == E1
        and named_sign(E1) == "+"
        and letters["A"] != named_sign(NEG_E1)
        and letters["C"] != named_sign(E2),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(incoming_sets[name] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(incoming_sets["A"]) == 1
        and len(incoming_sets["D"]) == 3
        and letters["A"] == NEG_E1
        and letters["D"] == "UNDEFINED",
        str((sorted(incoming_sets["A"]), sorted(incoming_sets["D"]))),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and unique_own_incoming_letter(locks[ORIGIN]) == E1
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and unique_own_incoming_letter(locks[E2]) == NEG_E1
        and add(E1, NEG_E1) == ZERO
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
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
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-incoming-undefined",
        unique_own_incoming_letter(()) == "UNDEFINED"
        and reverse_report("UNDEFINED", letters["B"]) == "UNDEFINED"
        and face_report(letters["C"], "UNDEFINED") == "UNDEFINED",
    )
    checks.check(
        "mutation-mixed-incoming-undefined",
        unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == "UNDEFINED"
        and face_report(E2, "UNDEFINED") == "UNDEFINED"
        and reverse_report("UNDEFINED", E1) == "UNDEFINED",
    )
    checks.check(
        "mutation-nsopy-leftover-reverse-would-be-undefined",
        reverse_report("UNDEFINED", E3) == "UNDEFINED" and reverse_status == "hold",
    )
    checks.check(
        "mutation-nsopown-reverse-would-be-undefined",
        reverse_report("UNDEFINED", E1) == "UNDEFINED" and reverse_status == "hold",
    )
    checks.check(
        "mutation-ownvec-face-would-fail",
        face_report(E2, E2) == "fail" and face_status == "UNDEFINED",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-own-incoming-letters",
        "L(A) = −e_1" in note
        and "L(B) = +e_1" in note
        and "L(C) = +e_2" in note
        and "L(D) = UNDEFINED" in note
        and "seed letter −e_1" in note
        and "incoming +e_1" in note
        and "incoming +e_2" in note
        and "incoming −e_2, −e_3, +e_3" in note,
    )
    checks.check(
        "note-reports-hold-undefined",
        "Reverse: hold" in note
        and "Face: UNDEFINED" in note
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
        "note-does-not-use-occupancy-or-neighbor-locks",
        "does not use occupancy" in normalized_note
        and "does not use already-recorded six-neighbor locks as the unique letter"
        in normalized_note
        and "own unique incoming lock" in normalized_note,
    )
    checks.check(
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-nsopy-leftover",
        "not leftover of the unique already-recorded six-neighbor lock-vector lists"
        in normalized_note
        and "these same y-probes" in normalized_note
        and "Record readout at C is C's own incoming lock" in note,
    )
    checks.check(
        "note-not-nsopown-x-probes",
        "not the four opposite-lock x-probes" in normalized_note
        and "A=(1,0,0)" in note.replace(" ", ""),
    )
    checks.check(
        "note-not-ownvec-different-seed",
        "not the perp two-site seed" in normalized_note
        and "different seed" in normalized_note
        and "+e_1/+e_2" in note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
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
        "note-no-star-dijkstra-gram-occupancy",
        "six-neighbor star" in normalized_note
        and "does not use a six-neighbor star" in normalized_note
        and "does not use occupancy" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_OWN_INCOMING_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def unique_own_incoming_letter(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["C"]] >= 1
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-own-incoming-only",
        "unique_own_incoming_letter" in defined_fns
        and "recorded_neighbor_locks" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
