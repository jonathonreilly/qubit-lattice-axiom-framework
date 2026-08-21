#!/usr/bin/env python3
"""Same-tick-inclusive 6-NN locks union own incoming reverse/face on x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,0,1), (0,0,-1)} with locks +e_1, -e_1, and -e_1. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters. L(q) is q's own unique
incoming lock; if several earliest incoming steps exist, L(q) is UNDEFINED.
At each x-probe's own formation tick t(q), S^+(q) is the set of locks of
6-NN of q that formed at tick <= t(q) and are not q, union {L(q)} when L(q)
is defined. No global T. Reverse holds iff some a in S^+(A) and some b in
S^+(B) have a+b=(0,0,0). Face holds iff some c in S^+(C) and some d in
S^+(D) have c+d=(0,0,0). Empty S^+ on either side is UNDEFINED; nonempty
with no opposite pair fails. Reverse HOLD does not use L(A): L(A) is
UNDEFINED. Same process as the z-symmetric three-site unique-vector display.
Same x-probes as the opposite-lock two-site unique-vector display. Cubic of
same-tick union own HOLDING on the y-symmetric x-probes. Not leftover of
two-site opposite-lock same-tick union own. Not leftover of z-symmetric
three-site y-probe same-tick union own (unlaunched; reverse fails there).
Not leftover of y-symmetric three-site x-probe same-tick union own. Not
leftover of y-symmetric three-site y-probe same-tick union own (reverse
HOLD uses L(A) there). Not leftover of strictly-earlier own-lock-in. Not
leftover of later-tick union own. Uniqueness of incoming locks is not
required. Occupancy n is not used. Named-sign lettering is not used. No
unique P_+. No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Z_SYMMETRIC_THREE_SITE_XPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Z_SYMMETRIC_THREE_SITE_XPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E1, E2),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
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
    "Reverse and face from same-tick ∪ own incoming lock on the "
    "four z-symmetric three-site x-probes are reported. Displayed, not adopted."
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
    """Set of same-tick-inclusive six-neighbor locks. Duplicates collapse."""
    return frozenset(lock for _neighbor, lock in pairs)


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point]) -> Letter:
    """Unique letter if the probe's own earliest incoming locks are a singleton in NN."""
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def own_lock_in_set(neighbors: frozenset[Point], letter: Letter) -> frozenset[Point]:
    """Union of same-tick-inclusive 6-NN locks with L(q) when L(q) is defined."""
    if letter == "UNDEFINED":
        return neighbors
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return neighbors | {letter}


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
    """Reverse iff some a in S^+(A) and some b in S^+(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point], set_d: frozenset[Point]) -> str:
    """Face iff some c in S^+(C) and some d in S^+(D) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def set_display(locks: frozenset[Point]) -> str:
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
    seeds: tuple[tuple[Point, Point], ...] = Z_SYMMETRIC_SEEDS,
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
    """Locks of 6-NN of site formed at tick <= t(site); site excluded."""
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


def strictly_earlier_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Leftover: locks of 6-NN of site formed at tick < t(site); site excluded."""
    formation = ticks[site]
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] >= formation:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def later_tick_T(
    ticks: dict[Point, int],
    probes: dict[str, Point] = PROBES,
) -> int | None:
    """Leftover global T: max formation tick of the four named probes."""
    defined = [ticks[probes[name]] for name in ("A", "B", "C", "D") if probes[name] in ticks]
    if len(defined) != 4:
        return None
    return max(defined)


def later_tick_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    common_tick: int,
) -> tuple[tuple[Point, Point], ...]:
    """Leftover: locks of 6-NN of site formed at tick <= common_tick, site excluded."""
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > common_tick:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def sum_of_set(locks: frozenset[Point]) -> Point:
    """Z^3 sum leftover of a lock set. Contrast only; not this letter."""
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

    print("same-tick-inclusive union own incoming reverse/face on z-symmetric x-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites,
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
        and add(E1, E1) == (2, 0, 0)
        and add(E2, E2) == (0, 2, 0)
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    star_a = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    star_b = frozenset({E1, E2})
    star_c = frozenset({E1, E2, NEG_E2})
    star_d = frozenset({E1, E2})
    plus_a = star_a
    plus_b = star_b
    plus_c = star_c
    plus_d = star_d
    form_a = frozenset({E1})
    form_b = frozenset({E2})
    form_c = frozenset({E2, NEG_E2})
    form_d = frozenset({E2})
    ownin_a = form_a
    ownin_b = frozenset({E1, E2})
    ownin_c = frozenset({E1, E2, NEG_E2})
    ownin_d = frozenset({E1, E2})
    later_b = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    two_site_a = frozenset({E1, E2, NEG_E2, NEG_E3})
    two_site_d = frozenset({E1, E2})
    y_star_a = frozenset({E1, E2})
    y_plus_a = frozenset({E1, E2})
    y_plus_c = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    ysym_plus_a = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    ysym_plus_b = frozenset({E1, E3})
    ysym_plus_d = frozenset({E1, NEG_E1, E3, NEG_E3})
    ysym_y_plus_a = frozenset({E1, NEG_E1})
    ysym_y_plus_c = frozenset({NEG_E1, E2})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(star_a, star_b) == "hold"
        and existential_opposite(star_c, star_d) == "hold"
        and existential_opposite(ownin_a, ownin_b) == "fail"
        and existential_opposite(ownin_c, ownin_d) == "hold"
        and existential_opposite(frozenset({NEG_E3}), frozenset({E3})) == "hold",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E3, E3)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )
    checks.check(
        "own-lock-in-set-identity",
        own_lock_in_set(star_a, "UNDEFINED") == star_a
        and own_lock_in_set(star_b, E1) == star_b
        and own_lock_in_set(star_c, E1) == star_c
        and own_lock_in_set(star_d, E1) == star_d
        and own_lock_in_set(y_star_a, E2) == y_plus_a
        and own_lock_in_set(frozenset({E1}), NEG_E1) == ysym_y_plus_a
        and own_lock_in_set(frozenset({E1}), NEG_E1) != frozenset({E1})
        and own_lock_in_set(frozenset(), NEG_E1) == frozenset({NEG_E1})
        and own_lock_in_set(frozenset(), "UNDEFINED") == frozenset(),
    )

    ticks, locks = form()
    leftover_T = later_tick_T(ticks)
    two_ticks, two_locks = form(TWO_SITE_SEEDS)
    ysym_ticks, ysym_locks = form(Y_SYMMETRIC_SEEDS)
    nstri_ticks, nstri_locks = form(NSTRI_SEEDS)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and leftover_T is not None,
    )
    assert leftover_T is not None

    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    star_sets: dict[str, frozenset[Point]] = {}
    letters: dict[str, Letter] = {}
    plus_sets: dict[str, frozenset[Point]] = {}
    form_sets: dict[str, frozenset[Point]] = {}
    ownin_sets: dict[str, frozenset[Point]] = {}
    later_star: dict[str, frozenset[Point]] = {}
    later_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        star_sets[name] = recorded_lock_set(pairs)
        letter = unique_own_incoming_letter(locks[site])
        letters[name] = letter
        plus_sets[name] = own_lock_in_set(star_sets[name], letter)
        earlier = strictly_earlier_neighbor_locks(site, ticks, locks)
        form_sets[name] = recorded_lock_set(earlier)
        ownin_sets[name] = own_lock_in_set(form_sets[name], letter)
        later_pairs = later_tick_neighbor_locks(site, ticks, locks, leftover_T)
        later_star[name] = recorded_lock_set(later_pairs)
        later_plus[name] = own_lock_in_set(later_star[name], letter)
        incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} L={letter_display(letter)} "
            f"S={set_display(star_sets[name])} "
            f"S+={set_display(plus_sets[name])} incoming={incoming}"
        )

    print(
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]} "
        f"leftover_T={leftover_T}"
    )
    reverse_status = reverse_report(plus_sets["A"], plus_sets["B"])
    face_status = face_report(plus_sets["C"], plus_sets["D"])
    star_reverse = reverse_report(star_sets["A"], star_sets["B"])
    star_face = face_report(star_sets["C"], star_sets["D"])
    ownin_reverse = reverse_report(ownin_sets["A"], ownin_sets["B"])
    ownin_face = face_report(ownin_sets["C"], ownin_sets["D"])
    later_reverse = reverse_report(later_plus["A"], later_plus["B"])
    later_face = face_report(later_plus["C"], later_plus["D"])
    own_reverse = reverse_report(
        own_lock_in_set(frozenset(), letters["A"]),
        own_lock_in_set(frozenset(), letters["B"]),
    )
    own_face = face_report(
        own_lock_in_set(frozenset(), letters["C"]),
        own_lock_in_set(frozenset(), letters["D"]),
    )
    reverse_uses_la = (
        letters["A"] != "UNDEFINED"
        and isinstance(letters["A"], tuple)
        and reverse_status == "hold"
        and reverse_report(plus_sets["A"] - {letters["A"]}, plus_sets["B"]) != "hold"
    )
    print(f"reverse={reverse_status} face={face_status} reverse_uses_L(A)={reverse_uses_la}")
    print(
        "per_element: each lock vector in same-tick-inclusive six-neighbor "
        "locks union L(q) when L(q) is defined"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four S^+ lock sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    y_star: dict[str, frozenset[Point]] = {}
    y_plus: dict[str, frozenset[Point]] = {}
    y_letters: dict[str, Letter] = {}
    for name in ("A", "B", "C", "D"):
        site = Y_PROBES[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        y_star[name] = recorded_lock_set(pairs)
        y_letters[name] = unique_own_incoming_letter(locks[site])
        y_plus[name] = own_lock_in_set(y_star[name], y_letters[name])
    y_reverse = reverse_report(y_plus["A"], y_plus["B"])
    y_face = face_report(y_plus["C"], y_plus["D"])
    y_star_reverse = reverse_report(y_star["A"], y_star["B"])
    y_reverse_uses_la = (
        y_letters["A"] != "UNDEFINED"
        and isinstance(y_letters["A"], tuple)
        and y_reverse == "hold"
        and reverse_report(y_plus["A"] - {y_letters["A"]}, y_plus["B"]) != "hold"
    )

    two_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, two_ticks, two_locks)
        letter = unique_own_incoming_letter(two_locks[site])
        two_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    two_reverse = reverse_report(two_plus["A"], two_plus["B"])
    two_face = face_report(two_plus["C"], two_plus["D"])

    nstri_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, nstri_ticks, nstri_locks)
        letter = unique_own_incoming_letter(nstri_locks[site])
        nstri_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    nstri_reverse = reverse_report(nstri_plus["A"], nstri_plus["B"])

    nfexist_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, perp_ticks, perp_locks)
        letter = unique_own_incoming_letter(perp_locks[site])
        nfexist_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    nfexist_reverse = reverse_report(nfexist_plus["A"], nfexist_plus["B"])
    nfexist_face = face_report(nfexist_plus["C"], nfexist_plus["D"])

    ysym_plus: dict[str, frozenset[Point]] = {}
    ysym_letters: dict[str, Letter] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, ysym_ticks, ysym_locks)
        letter = unique_own_incoming_letter(ysym_locks[site])
        ysym_letters[name] = letter
        ysym_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    ysym_reverse = reverse_report(ysym_plus["A"], ysym_plus["B"])
    ysym_face = face_report(ysym_plus["C"], ysym_plus["D"])

    ysym_y_plus: dict[str, frozenset[Point]] = {}
    ysym_y_letters: dict[str, Letter] = {}
    for name in ("A", "B", "C", "D"):
        site = Y_PROBES[name]
        pairs = own_tick_neighbor_locks(site, ysym_ticks, ysym_locks)
        letter = unique_own_incoming_letter(ysym_locks[site])
        ysym_y_letters[name] = letter
        ysym_y_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    ysym_y_reverse = reverse_report(ysym_y_plus["A"], ysym_y_plus["B"])
    ysym_y_face = face_report(ysym_y_plus["C"], ysym_y_plus["D"])
    ysym_y_reverse_uses_la = (
        ysym_y_letters["A"] != "UNDEFINED"
        and isinstance(ysym_y_letters["A"], tuple)
        and ysym_y_reverse == "hold"
        and reverse_report(ysym_y_plus["A"] - {ysym_y_letters["A"]}, ysym_y_plus["B"])
        != "hold"
    )

    z_plus: dict[str, frozenset[Point]] = {}
    z_letters: dict[str, Letter] = {}
    for name in ("A", "B", "C", "D"):
        site = Z_PROBES[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        letter = unique_own_incoming_letter(locks[site])
        z_letters[name] = letter
        z_plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    z_reverse = reverse_report(z_plus["A"], z_plus["B"])
    z_reverse_uses_la = (
        z_letters["A"] != "UNDEFINED"
        and isinstance(z_letters["A"], tuple)
        and z_reverse == "hold"
        and reverse_report(z_plus["A"] - {z_letters["A"]}, z_plus["B"]) != "hold"
    )

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-own-letter-and-plus-set",
        letters["A"] == "UNDEFINED"
        and neighbor_lists["A"]
        == (
            (ORIGIN, E1),
            (PROBES["D"], E1),
            ((1, -1, 0), E1),
            ((1, 0, 1), NEG_E2),
            ((1, 0, 1), NEG_E3),
            ((1, 0, 1), E2),
            ((1, 0, -1), NEG_E2),
            ((1, 0, -1), E3),
            ((1, 0, -1), E2),
        )
        and star_sets["A"] == star_a
        and plus_sets["A"] == plus_a
        and plus_sets["A"] == star_sets["A"],
        str((letters["A"], plus_sets["A"])),
    )
    checks.check(
        "theorem1-B-own-letter-and-plus-set",
        letters["B"] == E1
        and neighbor_lists["B"]
        == (
            ((0, 1, 1), E2),
            (PROBES["D"], E1),
        )
        and star_sets["B"] == star_b
        and plus_sets["B"] == plus_b
        and E1 in star_sets["B"],
        str((letters["B"], plus_sets["B"])),
    )
    checks.check(
        "theorem1-C-own-letter-and-plus-set",
        letters["C"] == E1
        and neighbor_lists["C"]
        == (
            (PROBES["A"], NEG_E2),
            (PROBES["A"], E2),
            ((2, 0, 1), E1),
            ((2, 0, -1), E1),
        )
        and star_sets["C"] == star_c
        and plus_sets["C"] == plus_c
        and E1 in star_sets["C"],
        str((letters["C"], plus_sets["C"])),
    )
    checks.check(
        "theorem1-D-own-letter-and-plus-set",
        letters["D"] == E1
        and neighbor_lists["D"]
        == (
            (Y_PROBES["A"], E2),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and star_sets["D"] == star_d
        and plus_sets["D"] == plus_d
        and plus_sets["D"] == star_sets["D"]
        and E1 in plus_sets["D"],
        str((letters["D"], plus_sets["D"])),
    )
    checks.check(
        "theorem1-union-is-noop-on-x-probes",
        plus_sets["A"] == star_sets["A"]
        and plus_sets["B"] == star_sets["B"]
        and plus_sets["C"] == star_sets["C"]
        and plus_sets["D"] == star_sets["D"]
        and letters["A"] == "UNDEFINED"
        and letters["D"] == E1
        and letters["B"] == E1
        and letters["C"] == E1
        and E1 in star_sets["B"]
        and E1 in star_sets["C"]
        and E1 in star_sets["D"],
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 3
        and locks[E1] == {NEG_E2, E2}
        and letters["A"] == "UNDEFINED"
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-reverse-hold-does-not-use-L-A",
        reverse_uses_la is False
        and letters["A"] == "UNDEFINED"
        and reverse_status == "hold"
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and NEG_E2 in plus_sets["A"]
        and E2 in plus_sets["B"]
        and add(NEG_E2, E2) == ZERO,
        str((reverse_status, letters["A"], plus_sets["A"], plus_sets["B"])),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and NEG_E2 in plus_sets["A"]
        and E2 in plus_sets["B"]
        and add(NEG_E2, E2) == ZERO
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and NEG_E2 in plus_sets["C"]
        and E2 in plus_sets["D"]
        and add(NEG_E2, E2) == ZERO
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-leftover-of-sametick-exclude-q",
        star_sets["A"] == plus_sets["A"]
        and star_reverse == "hold"
        and star_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and letters["A"] == "UNDEFINED"
        and letters["B"] == E1
        and letters["C"] == E1
        and letters["D"] == E1
        and y_plus["A"] == y_star["A"]
        and y_letters["A"] == E2
        and y_reverse == "fail",
    )
    checks.check(
        "not-leftover-of-strictly-earlier-own-lock-in",
        form_sets["A"] == form_a
        and form_sets["B"] == form_b
        and form_sets["C"] == form_c
        and form_sets["D"] == form_d
        and ownin_sets["A"] == ownin_a
        and ownin_sets["B"] == ownin_b
        and ownin_sets["C"] == ownin_c
        and ownin_sets["D"] == ownin_d
        and ownin_reverse == "fail"
        and ownin_face == "hold"
        and reverse_status == "hold"
        and reverse_status != ownin_reverse
        and plus_sets["A"] != ownin_sets["A"]
        and plus_sets["D"] == ownin_sets["D"],
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        letters["A"] == "UNDEFINED"
        and letters["B"] == E1
        and letters["C"] == E1
        and letters["D"] == E1
        and own_reverse == "UNDEFINED"
        and own_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and reverse_status != own_reverse
        and face_status != own_face
        and plus_sets["A"] != frozenset()
        and plus_sets["D"] != frozenset(),
    )
    checks.check(
        "not-leftover-of-later-tick-union-own",
        leftover_T == 4
        and later_plus["B"] == later_b
        and plus_sets["B"] == plus_b
        and plus_sets["B"] != later_plus["B"]
        and E2 in later_plus["B"]
        and E2 in plus_sets["B"]
        and NEG_E2 in later_plus["B"]
        and NEG_E2 not in plus_sets["B"]
        and E3 in later_plus["B"]
        and E3 not in plus_sets["B"]
        and later_reverse == "hold"
        and later_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and leftover_T != ticks[PROBES["A"]]
        and leftover_T != ticks[PROBES["B"]],
    )
    checks.check(
        "no-global-later-T-in-letter",
        leftover_T == 4
        and leftover_T != ticks[PROBES["A"]]
        and leftover_T != ticks[PROBES["B"]]
        and leftover_T != ticks[PROBES["D"]]
        and leftover_T == ticks[PROBES["C"]]
        and plus_sets["B"] != later_plus["B"]
        and all(
            ticks[neighbor] <= ticks[PROBES[name]]
            for name in ("A", "B", "C", "D")
            for neighbor, _lock in neighbor_lists[name]
        ),
    )
    checks.check(
        "not-leftover-of-two-site-opposite-lock-sametick-union-own",
        Z_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and two_plus["A"] == two_site_a
        and two_plus["D"] == two_site_d
        and plus_sets["A"] == plus_a
        and plus_sets["D"] == plus_d
        and plus_sets["A"] != two_plus["A"]
        and plus_sets["D"] == two_plus["D"]
        and E3 in plus_sets["A"]
        and E3 not in two_plus["A"]
        and NEG_E3 in plus_sets["A"]
        and NEG_E3 in two_plus["A"]
        and two_reverse == "hold"
        and two_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
        str((two_plus["A"], plus_sets["A"], two_plus["D"], plus_sets["D"])),
    )
    checks.check(
        "not-leftover-of-z-symmetric-y-probe-union",
        probe_sites != y_probe_sites
        and y_letters["A"] == E2
        and y_star["A"] == y_star_a
        and y_plus["A"] == y_plus_a
        and y_plus["C"] == y_plus_c
        and y_plus["A"] == y_star["A"]
        and plus_sets["A"] == star_sets["A"]
        and y_reverse == "fail"
        and y_face == "hold"
        and y_star_reverse == "fail"
        and y_reverse_uses_la is False
        and reverse_uses_la is False
        and reverse_status == "hold"
        and face_status == "hold"
        and plus_sets["A"] != y_plus["A"]
        and plus_sets["C"] != y_plus["C"]
        and ticks[Y_PROBES["A"]] == 1
        and ticks[PROBES["A"]] == 3,
    )
    checks.check(
        "not-leftover-of-y-symmetric-xprobe-union",
        Z_SYMMETRIC_SEEDS != Y_SYMMETRIC_SEEDS
        and ysym_plus["A"] == ysym_plus_a
        and ysym_plus["B"] == ysym_plus_b
        and ysym_plus["D"] == ysym_plus_d
        and plus_sets["B"] != ysym_plus["B"]
        and plus_sets["D"] != ysym_plus["D"]
        and ysym_ticks[PROBES["D"]] == 3
        and ticks[PROBES["D"]] == 2
        and ysym_letters["D"] == "UNDEFINED"
        and letters["D"] == E1
        and ysym_reverse == "hold"
        and ysym_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
        str((ysym_plus["B"], plus_sets["B"], ysym_plus["D"], plus_sets["D"])),
    )
    checks.check(
        "not-leftover-of-y-symmetric-y-probe-union",
        ysym_y_letters["A"] == NEG_E1
        and ysym_y_plus["A"] == ysym_y_plus_a
        and ysym_y_plus["C"] == ysym_y_plus_c
        and ysym_y_reverse == "hold"
        and ysym_y_face == "hold"
        and ysym_y_reverse_uses_la is True
        and reverse_uses_la is False
        and plus_sets["A"] != ysym_y_plus["A"]
        and ysym_ticks[Y_PROBES["A"]] == 0
        and ticks[Y_PROBES["A"]] == 1,
    )
    checks.check(
        "not-leftover-of-z-symmetric-z-probe-union",
        z_letters["A"] == NEG_E1
        and z_reverse == "hold"
        and z_reverse_uses_la is True
        and reverse_uses_la is False
        and ticks[Z_PROBES["A"]] == 0
        and ticks[PROBES["A"]] == 3
        and plus_sets["A"] != z_plus["A"],
    )
    checks.check(
        "not-leftover-of-nstri-third-site",
        Z_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and nstri_ticks[E1] == 0
        and ticks[E1] != 0
        and plus_sets["A"] != nstri_plus["A"]
        and nstri_reverse == "fail"
        and reverse_status == "hold",
        str(nstri_plus["A"]),
    )
    checks.check(
        "not-leftover-of-nfexist-nnseed-x-probes",
        Z_SYMMETRIC_SEEDS != PERP_SEEDS
        and reverse_status == "hold"
        and face_status == "hold"
        and plus_sets["A"] != nfexist_plus["A"]
        and nfexist_reverse == "fail"
        and reverse_status != nfexist_reverse,
        str((nfexist_reverse, nfexist_face, nfexist_plus["A"])),
    )
    checks.check(
        "sign-lettering-loses-axis",
        named_sign(NEG_E3) == "-"
        and named_sign(E3) == "+"
        and named_sign(E1) == "+"
        and named_sign(NEG_E2) == "-"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus_sets["A"]) == E1
        and sum_of_set(plus_sets["B"]) == add(E1, E2)
        and sum_of_set(plus_sets["C"]) == E1
        and sum_of_set(plus_sets["D"]) == add(E1, E2)
        and add(sum_of_set(plus_sets["A"]), sum_of_set(plus_sets["B"])) != ZERO
        and add(sum_of_set(plus_sets["C"]), sum_of_set(plus_sets["D"])) != ZERO
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-unique-vector-leftover",
        len(plus_sets["A"]) > 1
        and len(plus_sets["B"]) > 1
        and len(plus_sets["C"]) > 1
        and len(plus_sets["D"]) > 1
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["A"]]) == 2
        and len(locks[PROBES["D"]]) == 1
        and letters["A"] == "UNDEFINED"
        and letters["D"] == E1
        and plus_sets["A"] == plus_a
        and plus_sets["D"] == plus_d
        and reverse_status == "hold"
        and face_status == "hold",
        str((sorted(locks[PROBES["A"]]), sorted(locks[PROBES["D"]]))),
    )
    checks.check(
        "z-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E3] == 0
        and locks[E3] == {NEG_E1}
        and ticks[NEG_E3] == 0
        and locks[NEG_E3] == {NEG_E1}
        and ticks[E2] == 1
        and ticks[NEG_E2] == 1
        and add(E1, NEG_E1) == ZERO
        and E1 not in {site for site, _lock in Z_SYMMETRIC_SEEDS}
        and Z_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Z_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and Z_SYMMETRIC_SEEDS != PERP_SEEDS
        and Z_SYMMETRIC_SEEDS != Y_SYMMETRIC_SEEDS
        and PROBES["A"] != E3,
    )
    checks.check(
        "same-tick-includes-same-tick-neighbors",
        any(ticks[neighbor] == ticks[PROBES["A"]] for neighbor, _lock in neighbor_lists["A"])
        and any(ticks[neighbor] == ticks[PROBES["B"]] for neighbor, _lock in neighbor_lists["B"])
        and any(ticks[neighbor] == ticks[PROBES["C"]] for neighbor, _lock in neighbor_lists["C"])
        and any(ticks[neighbor] == ticks[PROBES["D"]] for neighbor, _lock in neighbor_lists["D"])
        and all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
        and all(
            ticks[neighbor] <= ticks[PROBES[name]]
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
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E1, NEG_E1)
    )
    z_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E3, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and z_mirror_parallel_blocked
        and ticks[NEG_E3] == 0
        and ticks[E2] == 1
        and ticks[NEG_E2] == 1
        and ticks[(0, 0, 2)] == 1
        and ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-plus-set-undefined",
        recorded_lock_set(()) == frozenset()
        and reverse_report(frozenset(), plus_sets["B"]) == "UNDEFINED"
        and face_report(plus_sets["C"], frozenset()) == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and ownin_reverse == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-own-incoming-reverse-undefined",
        own_reverse == "UNDEFINED"
        and own_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-formation-own-lock-in-reverse-fails",
        ownin_reverse == "fail" and reverse_status == "hold",
    )
    checks.check(
        "mutation-sum-would-fail",
        add(sum_of_set(plus_sets["A"]), sum_of_set(plus_sets["B"])) != ZERO
        and add(sum_of_set(plus_sets["C"]), sum_of_set(plus_sets["D"])) != ZERO
        and reverse_status == "hold"
        and face_status == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-plus-sets",
        "S^+(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(B) = {+e_1, +e_2}" in note
        and "S^+(C) = {+e_1, +e_2, −e_2}" in note
        and "S^+(D) = {+e_1, +e_2}" in note
        and "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "L(A) = UNDEFINED" in note
        and "L(B) = +e_1" in note
        and "L(C) = +e_1" in note
        and "L(D) = +e_1" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_1 at (1, 1, 0)" in note
        and "+e_2 at (0, 1, 1)" in note
        and "−e_2 at (1, 0, 0)" in note
        and "+e_2 at (0, 1, 0)" in note
        and "+e_1 at (1, -1, 0)" in note,
    )
    checks.check(
        "note-reports-hold-hold-and-does-not-use-L-A",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "Reverse HOLD does not use L(A)." in note
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
        and "own incoming lock" in normalized_note
        and "same-tick-inclusive" in normalized_note,
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
        "note-not-unique-or-sum-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "Face holds." in note
        and "Reverse holds." in note,
    )
    checks.check(
        "note-not-leftover-of-own-incoming",
        "not leftover of the unique own-incoming lock-vector letters"
        in normalized_note
        and "face fail" in normalized_note
        and "Face: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-sametick-exclude-q",
        "not leftover of same-tick-inclusive existential opposite that excludes"
        in normalized_note
        and "Reverse: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-strictly-earlier-own-lock-in",
        "not leftover of strictly-earlier own-lock-in"
        in normalized_note
        and "S^+(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick-union-own",
        "not leftover of later-tick union own"
        in normalized_note
        and "does not wait for a global later T" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-two-site-or-y-probes",
        "not leftover of two-site opposite-lock" in normalized_note
        and "not leftover of z-symmetric three-site y-probe" in normalized_note
        and "not leftover of y-symmetric three-site x-probe" in normalized_note
        and "reverse HOLD uses L(A)" in note
        and "S^+(D) = {+e_1, +e_2}" in note,
    )
    checks.check(
        "note-sametick-union-own",
        "union" in normalized_note
        and "S^+(q)" in note
        and "own incoming lock" in normalized_note
        and "same-tick-inclusive" in normalized_note
        and "no global T" in normalized_note,
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
        '    "docs/Z_SYMMETRIC_THREE_SITE_XPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
        and "def own_tick_neighbor_locks(" in source
        and "def unique_own_incoming_letter(" in source
        and "def own_lock_in_set(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 3
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-sametick-union-own-existential-opposite",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "own_tick_neighbor_locks" in defined_fns
        and "unique_own_incoming_letter" in defined_fns
        and "own_lock_in_set" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
