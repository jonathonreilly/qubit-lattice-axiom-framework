#!/usr/bin/env python3
"""Own incoming set exist-opposite reverse/face on four #7185 x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (1,0,0), (-1,0,0)} with locks +e_2, -e_2, and -e_2 (nsxopinx #7185).
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. M(q) is the set of earliest incoming NN steps at q. Mixed stays
a set. Unformed is UNDEFINED. Reverse holds iff some a in M(A) and some b
in M(B) have a+b=(0,0,0). Face holds iff some c in M(C) and some d in M(D)
have c+d=(0,0,0). Empty or UNDEFINED on either side is UNDEFINED; nonempty
with no opposite pair fails. Unique L is not the object. The 6-NN star S^+
is not the letter; #7185 S^+(A) is a leftover comparator that HOLDs using
L(A). Reverse HOLD uses singleton M(A)={-e_2}. Unique-L leftover reports
face UNDEFINED when mixed. nszmenu #7188 mixed M reverse-fails and
face-fails; this is not a reprint of that fail/fail. Occupancy n is not
used. Named-sign lettering is not used. No unique P_+. Uniqueness of
incoming locks is not required. No larger ball.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Incoming = frozenset[Point] | str
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
X_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (NEG_E1, NEG_E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (E2, E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E1),
)
PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
Y_PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
Z_PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
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
    "Runner cache",
    "f(n)",
    "ndot",
    "P_+",
)
CLAIM_SCOPE = (
    "Reverse and face from own incoming set on the four "
    "#7185 x-probes are reported. No S⁺. Displayed, not adopted."
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


def own_incoming_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Incoming:
    """Earliest incoming NN steps at site. Seeds are a singleton. Unformed is UNDEFINED."""
    if site not in ticks:
        return "UNDEFINED"
    return frozenset(locks[site])


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point] | Incoming) -> Letter:
    """Unique-L leftover: UNDEFINED when mixed. Not this letter."""
    if incoming == "UNDEFINED":
        return "UNDEFINED"
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def recorded_lock_set(pairs: tuple[tuple[Point, Point], ...]) -> frozenset[Point]:
    """Set of six-neighbor locks. Leftover comparator only."""
    return frozenset(lock for _neighbor, lock in pairs)


def own_lock_in_set(neighbors: frozenset[Point], letter: Letter) -> Incoming:
    """S^+ leftover: neighbor locks union L(q) when defined. Not this letter."""
    if letter == "UNDEFINED":
        return neighbors
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return neighbors | {letter}


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right.

    UNDEFINED or empty on either side is UNDEFINED. Nonempty with no opposite
    pair fails. Mixed stays a set. Does not sum. Does not require a singleton.
    """
    if left == "UNDEFINED" or right == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return "UNDEFINED"
    if not left or not right:
        return "UNDEFINED"
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    """Reverse iff some a in M(A) and some b in M(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in M(C) and some d in M(D) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def set_display(locks: Incoming) -> str:
    if locks == "UNDEFINED":
        return "UNDEFINED"
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


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
    seeds: tuple[tuple[Point, Point], ...] = X_SYMMETRIC_SEEDS,
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


def own_tick_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Leftover #7185 S^+ neighbor list: 6-NN locks formed at tick <= t(site)."""
    formation = ticks[site]
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > formation:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def sum_of_set(locks: Incoming) -> Point | str:
    """Z^3 sum leftover of a lock set. Contrast only; not this letter."""
    if locks == "UNDEFINED":
        return "UNDEFINED"
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


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

    print("own incoming set exist-opposite reverse/face on #7185 x-probes")
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
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites,
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
        and add(E2, NEG_E2) == ZERO
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a = frozenset({E2, NEG_E2})
    plus_b = frozenset({E2, E3})
    plus_c = frozenset({E1, NEG_E2})
    plus_d = frozenset({E2, NEG_E2, E3, NEG_E3})
    set_a = frozenset({NEG_E2})
    set_b = frozenset({E2})
    set_c = frozenset({E1})
    set_d = frozenset({NEG_E1, E3, NEG_E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite("UNDEFINED", frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), "UNDEFINED") == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_a, set_b) == "hold"
        and existential_opposite(set_c, set_d) == "hold"
        and existential_opposite(plus_a, plus_b) == "hold"
        and existential_opposite(plus_c, plus_d) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "own-incoming-set-identity",
        unique_own_incoming_letter(frozenset({NEG_E2})) == NEG_E2
        and unique_own_incoming_letter(frozenset({E2, NEG_E2})) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E1, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED"
        and unique_own_incoming_letter("UNDEFINED") == "UNDEFINED",
    )

    ticks, locks = form()
    two_ticks, two_locks = form(TWO_SITE_SEEDS)
    ysym_ticks, ysym_locks = form(Y_SYMMETRIC_SEEDS)
    zsym_ticks, zsym_locks = form(Z_SYMMETRIC_SEEDS)
    nstri_ticks, nstri_locks = form(NSTRI_SEEDS)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D")),
    )

    incoming_sets: dict[str, Incoming] = {}
    letters: dict[str, Letter] = {}
    plus_sets: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        incoming_sets[name] = own_incoming_set(site, ticks, locks)
        letters[name] = unique_own_incoming_letter(incoming_sets[name])
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        plus_sets[name] = own_lock_in_set(recorded_lock_set(pairs), letters[name])
        print(
            f"{name} t={ticks[site]} M={set_display(incoming_sets[name])} "
            f"L={letter_display(letters[name])} "
            f"S+={set_display(plus_sets[name])}"
        )

    reverse_status = reverse_report(incoming_sets["A"], incoming_sets["B"])
    face_status = face_report(incoming_sets["C"], incoming_sets["D"])
    plus_reverse = reverse_report(plus_sets["A"], plus_sets["B"])
    plus_face = face_report(plus_sets["C"], plus_sets["D"])
    unique_reverse = reverse_report(
        own_lock_in_set(frozenset(), letters["A"]),
        own_lock_in_set(frozenset(), letters["B"]),
    )
    unique_face = face_report(
        own_lock_in_set(frozenset(), letters["C"]),
        own_lock_in_set(frozenset(), letters["D"]),
    )
    reverse_uses_la = (
        letters["A"] != "UNDEFINED"
        and isinstance(letters["A"], tuple)
        and plus_reverse == "hold"
        and reverse_report(plus_sets["A"] - {letters["A"]}, plus_sets["B"]) != "hold"
        if isinstance(plus_sets["A"], frozenset) and isinstance(plus_sets["B"], frozenset)
        else False
    )
    reverse_uses_singleton_m_a = (
        reverse_status == "hold"
        and incoming_sets["A"] == set_a
        and isinstance(incoming_sets["A"], frozenset)
        and len(incoming_sets["A"]) == 1
        and NEG_E2 in incoming_sets["A"]
        and incoming_sets["B"] == set_b
        and add(NEG_E2, E2) == ZERO
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"S+_reverse={plus_reverse} S+_face={plus_face} "
        f"reverse_uses_L(A)={reverse_uses_la} "
        f"reverse_uses_singleton_M(A)={reverse_uses_singleton_m_a}"
    )
    print(f"unique_L_reverse={unique_reverse} unique_L_face={unique_face}")
    print(
        "per_element: each lock vector in the probe's own incoming set M(q)"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four incoming sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    two_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        two_incoming[name] = own_incoming_set(PROBES[name], two_ticks, two_locks)

    ysym_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        ysym_incoming[name] = own_incoming_set(PROBES[name], ysym_ticks, ysym_locks)
    ysym_reverse = reverse_report(ysym_incoming["A"], ysym_incoming["B"])
    ysym_face = face_report(ysym_incoming["C"], ysym_incoming["D"])

    zsym_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        zsym_incoming[name] = own_incoming_set(PROBES[name], zsym_ticks, zsym_locks)
    zsym_reverse = reverse_report(zsym_incoming["A"], zsym_incoming["B"])
    zsym_face = face_report(zsym_incoming["C"], zsym_incoming["D"])

    nstri_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        nstri_incoming[name] = own_incoming_set(PROBES[name], nstri_ticks, nstri_locks)

    perp_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        perp_incoming[name] = own_incoming_set(PROBES[name], perp_ticks, perp_locks)
    perp_reverse = reverse_report(perp_incoming["A"], perp_incoming["B"])
    perp_face = face_report(perp_incoming["C"], perp_incoming["D"])

    y_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        y_incoming[name] = own_incoming_set(Y_PROBES[name], ticks, locks)
    y_reverse = reverse_report(y_incoming["A"], y_incoming["B"])
    y_face = face_report(y_incoming["C"], y_incoming["D"])

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-incoming-sets",
        incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and incoming_sets["C"] == set_c
        and incoming_sets["D"] == set_d
        and incoming_sets["A"] != "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED"
        and len(incoming_sets["A"]) == 1
        and len(incoming_sets["D"]) == 3,
        str({name: set_display(incoming_sets[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-compare-7185-S-plus-A",
        plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and incoming_sets["A"] != plus_sets["A"]
        and E2 in plus_sets["A"]
        and E2 not in incoming_sets["A"]
        and NEG_E2 in incoming_sets["A"]
        and NEG_E2 in plus_sets["A"]
        and NEG_E1 in incoming_sets["D"]
        and NEG_E1 not in plus_sets["D"],
        str((set_display(incoming_sets["A"]), set_display(plus_sets["A"]))),
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E1
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and incoming_sets["A"] == frozenset({NEG_E2})
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(incoming_sets["D"]) == 3
        and letters["D"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED"
        and unique_own_incoming_letter(incoming_sets["D"]) == "UNDEFINED"
        and NEG_E1 in incoming_sets["D"]
        and E3 in incoming_sets["D"]
        and NEG_E3 in incoming_sets["D"],
    )
    checks.check(
        "theorem1-reverse-hold-uses-singleton-M-A",
        reverse_uses_singleton_m_a
        and letters["A"] == NEG_E2
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b,
        str((reverse_status, set_display(incoming_sets["A"]))),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and add(NEG_E2, E2) == ZERO
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and incoming_sets["C"] == set_c
        and incoming_sets["D"] == set_d
        and add(E1, NEG_E1) == ZERO
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "discriminator-hold-from-singleton-M-not-S-plus",
        reverse_status == "hold"
        and face_status == "hold"
        and plus_reverse == "hold"
        and plus_face == "hold"
        and reverse_uses_singleton_m_a
        and reverse_uses_la
        and incoming_sets["A"] != plus_sets["A"]
        and incoming_sets["C"] != plus_sets["C"]
        and incoming_sets["D"] != plus_sets["D"]
        and len(incoming_sets["A"]) == 1
        and len(plus_sets["A"]) == 2
        and letters["A"] == NEG_E2
        and NEG_E2 in plus_sets["C"]
        and NEG_E2 not in incoming_sets["C"],
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "hold"
        and unique_face == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold"
        and face_status != unique_face
        and letters["A"] == NEG_E2
        and letters["B"] == E2
        and letters["C"] == E1
        and letters["D"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-S-plus-7185",
        plus_sets["A"] == plus_a
        and plus_reverse == "hold"
        and plus_face == "hold"
        and reverse_uses_la
        and incoming_sets["A"] != plus_sets["A"]
        and incoming_sets["B"] != plus_sets["B"]
        and incoming_sets["C"] != plus_sets["C"]
        and incoming_sets["D"] != plus_sets["D"]
        and E2 not in incoming_sets["A"]
        and E2 in plus_sets["A"]
        and NEG_E1 in incoming_sets["D"]
        and NEG_E1 not in plus_sets["D"],
    )
    checks.check(
        "not-reprint-of-nszmenu-7188",
        zsym_incoming["A"] != incoming_sets["A"]
        and zsym_incoming["A"] == frozenset({E2, NEG_E2})
        and zsym_reverse == "fail"
        and zsym_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and ticks[PROBES["A"]] == 0
        and zsym_ticks[PROBES["A"]] == 3,
    )
    checks.check(
        "not-y-probes-or-two-site-or-nstri-or-perp",
        X_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and X_SYMMETRIC_SEEDS != Y_SYMMETRIC_SEEDS
        and X_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and X_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and X_SYMMETRIC_SEEDS != PERP_SEEDS
        and ticks[NEG_E1] == 0
        and two_ticks.get(NEG_E1) != 0
        and probe_sites != y_probe_sites
        and y_incoming["A"] != incoming_sets["A"]
        and y_reverse == "fail"
        and y_face == "fail"
        and nstri_incoming["B"] != incoming_sets["B"]
        and E1 in nstri_incoming["B"]
        and E1 not in incoming_sets["B"]
        and perp_incoming["A"] != incoming_sets["A"]
        and perp_reverse == "fail"
        and perp_face == "hold"
        and ysym_reverse == "fail"
        and ysym_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-nnlock-named-sign",
        incoming_sets["A"] == frozenset({NEG_E2})
        and named_sign(NEG_E2) == "-"
        and named_sign(E2) == "+"
        and incoming_sets["C"] == frozenset({E1})
        and named_sign(E1) == "+"
        and incoming_sets["A"] != named_sign(NEG_E2)
        and incoming_sets["C"] != named_sign(E1),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(
            incoming_sets[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        len(incoming_sets["A"]) == 1
        and len(incoming_sets["B"]) == 1
        and len(incoming_sets["C"]) == 1
        and len(incoming_sets["D"]) == 3
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "x-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E2}
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and ticks[NEG_E1] == 0
        and locks[NEG_E1] == {NEG_E2}
        and add(E2, NEG_E2) == ZERO
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E2, NEG_E2)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E1, step)) != 1 for step in (E2, NEG_E2)
    )
    x_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E1, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and x_mirror_parallel_blocked
        and ticks[NEG_E1] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), incoming_sets["B"]) == "UNDEFINED"
        and face_report(incoming_sets["C"], frozenset()) == "UNDEFINED"
        and reverse_report("UNDEFINED", incoming_sets["B"]) == "UNDEFINED"
        and face_report(incoming_sets["C"], "UNDEFINED") == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-unique-L-face-would-be-undefined",
        unique_face == "UNDEFINED"
        and unique_reverse == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-S-plus-would-hold-on-larger-A",
        plus_reverse == "hold"
        and plus_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and incoming_sets["A"] != plus_sets["A"],
    )
    checks.check(
        "mutation-sum-cancels-mixed-D",
        sum_of_set(incoming_sets["A"]) == NEG_E2
        and sum_of_set(incoming_sets["B"]) == E2
        and sum_of_set(incoming_sets["C"]) == E1
        and sum_of_set(incoming_sets["D"]) == NEG_E1
        and incoming_sets["D"] != frozenset({NEG_E1})
        and len(incoming_sets["D"]) == 3
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "face-pair-not-S-plus-pair",
        add(E1, NEG_E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and E1 in incoming_sets["C"]
        and NEG_E1 in incoming_sets["D"]
        and NEG_E2 in plus_sets["C"]
        and E2 in plus_sets["D"]
        and NEG_E2 not in incoming_sets["C"]
        and E2 not in incoming_sets["D"],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-incoming-sets",
        "M(A) = {−e_2}" in note
        and "M(B) = {+e_2}" in note
        and "M(C) = {+e_1}" in note
        and "M(D) = {−e_1, +e_3, −e_3}" in note
        and "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "incoming +e_2" in note
        and "incoming +e_1" in note
        and "incoming −e_1, −e_3, +e_3" in note,
    )
    checks.check(
        "note-reports-7185-S-plus-A",
        "S^+(A) = {+e_2, −e_2}" in note
        and "Reverse HOLD uses a singleton M(A)." in note
        and "L(A) = −e_2" in note
        and "Reverse HOLD uses L(A)." in note,
    )
    checks.check(
        "note-reports-hold-hold",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own incoming set" in normalized_note
        and "mixed stays a set" in normalized_note,
    )
    checks.check(
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-unique-or-sum-or-star-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "not leftover of #7185" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "not leftover of nszmenu" in normalized_note
        and "Face holds." in note
        and "Reverse holds." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "own incoming set" in normalized_note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", "")
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
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def own_incoming_set(" in source
        and "def existential_opposite(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-own-incoming-set-existential-opposite",
        "own_incoming_set" in defined_fns
        and "existential_opposite" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
