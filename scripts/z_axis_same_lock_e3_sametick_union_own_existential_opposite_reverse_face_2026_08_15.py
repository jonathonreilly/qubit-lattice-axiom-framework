#!/usr/bin/env python3
"""Same-tick-inclusive 6-NN locks union own incoming reverse/face on y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,0,1)} with locks +e_3 and +e_3 (same letter, perpendicular to the
seed edge). This is not nsze2sam (+e_2/+e_2) and not nszsaminc (+e_1/+e_1).
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters.
L(q) is q's own unique incoming lock; if several earliest incoming steps
exist, L(q) is UNDEFINED. At each y-probe's own formation tick t(q), S^+(q)
is the set of locks of 6-NN of q that formed at tick <= t(q) and are not q,
union {L(q)} when L(q) is defined. No global T. Reverse holds iff some a in
S^+(A) and some b in S^+(B) have a+b=(0,0,0). Face holds iff some c in
S^+(C) and some d in S^+(D) have c+d=(0,0,0). Empty S^+ on either side is
UNDEFINED; nonempty with no opposite pair fails. Reverse HOLD does not use
L(A): reverse fails, and L(A)=+e_2 has no opposite in S^+(B). A is not a
seed site. Face holds from -e_1 at C against +e_1 at D. Not leftover of
strictly-earlier own-lock-in (face fail). Not leftover of same-tick
exclude-q. Not leftover of later-tick union own (hold/hold after a global T
from a five-lock set at A). Not leftover of nsze2sam (hold/hold on same-lock
+e_2). Not leftover of nsze3inc (fail/hold on opposite +/-e_3; seed partner
lock is -e_3). Not leftover of nszsaminc (fail/hold on same-lock +e_1). Not
leftover of nszparinc (fail/hold). Not leftover of nspar x-probes (fail/hold
on a different seed). Not leftover of nsopp y-probes (hold/hold with seed
site A). Uniqueness of incoming locks is not required. Occupancy n is not
used. Named-sign lettering is not used. No unique P_+. No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Z_AXIS_SAME_LOCK_E3_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Z_AXIS_SAME_LOCK_E3_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E3, E3),
)
NSZE2SAM_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E3, E2),
)
NSZE2INC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E3, NEG_E2),
)
NSZE3INC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E3, NEG_E3),
)
NSZSAMINC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, E1),
)
NSZPARINC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
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
    "P_+",
)
CLAIM_SCOPE = (
    "Reverse and face from same-tick ∪ own incoming lock on the "
    "four z-axis same-lock +e_3 y-probes are reported. Displayed, not adopted."
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


def reverse_hold_uses_own_letter(
    plus_a: frozenset[Point],
    plus_b: frozenset[Point],
    letter_a: Letter,
) -> bool:
    """True iff reverse holds and some holding pair uses L(A)."""
    if letter_a == "UNDEFINED" or not isinstance(letter_a, tuple):
        return False
    if letter_a not in plus_a:
        return False
    if reverse_report(plus_a, plus_b) != "hold":
        return False
    return any(add(letter_a, b) == ZERO for b in plus_b)


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

    print("same-tick-inclusive union own incoming reverse/face on z-axis same-lock +e_3 y-probes")
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
        and add(E1, E1) == (2, 0, 0)
        and add(E2, E2) == (0, 2, 0)
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and add(E3, E3) != ZERO
        and dot(E1, E3) == 0
        and perpendicular(E3, E1)
        and perpendicular(E3, E2)
        and not perpendicular(E3, E3)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a = frozenset({E2, E3})
    mixed_b = frozenset({E1, E2})
    mixed_c = frozenset({E1, NEG_E1, E2, NEG_E3})
    mixed_d = frozenset({E1, E2})
    later_union_a = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    later_union_b = frozenset({E1, E2, E3})
    later_union_d = frozenset({E1, E2, NEG_E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(plus_a, mixed_b) == "fail"
        and existential_opposite(mixed_c, mixed_d) == "hold"
        and existential_opposite(frozenset({E2}), mixed_b) == "fail"
        and existential_opposite(frozenset({E1}), mixed_b) == "fail"
        and existential_opposite(frozenset({NEG_E1}), mixed_d) == "hold",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((E2, E3)) == "UNDEFINED"
        and unique_own_incoming_letter((E1, E3, NEG_E1)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )
    checks.check(
        "own-lock-in-set-identity",
        own_lock_in_set(frozenset({E3}), E2) == plus_a
        and own_lock_in_set(mixed_b, E2) == mixed_b
        and own_lock_in_set(plus_a, "UNDEFINED") == plus_a
        and own_lock_in_set(frozenset({E2}), E1) == mixed_d
        and own_lock_in_set(frozenset(), "UNDEFINED") == frozenset(),
    )

    ticks, locks = form()
    later_common = later_tick_T(ticks)
    nsze2sam_ticks, nsze2sam_locks = form(NSZE2SAM_SEEDS)
    nsze2_ticks, nsze2_locks = form(NSZE2INC_SEEDS)
    nsze3inc_ticks, nsze3inc_locks = form(NSZE3INC_SEEDS)
    nszsam_ticks, nszsam_locks = form(NSZSAMINC_SEEDS)
    nszpar_ticks, nszpar_locks = form(NSZPARINC_SEEDS)
    nsopp_ticks, nsopp_locks = form(NSOPP_SEEDS)
    nspar_ticks, nspar_locks = form(NSPAR_SEEDS)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and later_common is not None,
    )
    assert later_common is not None

    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    neighbor_sets: dict[str, frozenset[Point]] = {}
    earlier_sets: dict[str, frozenset[Point]] = {}
    letters: dict[str, Letter] = {}
    plus_sets: dict[str, frozenset[Point]] = {}
    later_sets: dict[str, frozenset[Point]] = {}
    later_union_sets: dict[str, frozenset[Point]] = {}
    earlier_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        neighbor_sets[name] = recorded_lock_set(pairs)
        earlier_pairs = strictly_earlier_neighbor_locks(site, ticks, locks)
        earlier_sets[name] = recorded_lock_set(earlier_pairs)
        letter = unique_own_incoming_letter(locks[site])
        letters[name] = letter
        plus_sets[name] = own_lock_in_set(neighbor_sets[name], letter)
        earlier_plus[name] = own_lock_in_set(earlier_sets[name], letter)
        later_pairs = later_tick_neighbor_locks(site, ticks, locks, later_common)
        later_sets[name] = recorded_lock_set(later_pairs)
        later_union_sets[name] = own_lock_in_set(later_sets[name], letter)
        incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} L={letter_display(letter)} "
            f"S+={set_display(plus_sets[name])} incoming={incoming}"
        )

    print(
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]} "
        f"leftover_T={later_common}"
    )
    reverse_status = reverse_report(plus_sets["A"], plus_sets["B"])
    face_status = face_report(plus_sets["C"], plus_sets["D"])
    exclude_reverse = reverse_report(neighbor_sets["A"], neighbor_sets["B"])
    exclude_face = face_report(neighbor_sets["C"], neighbor_sets["D"])
    earlier_reverse = reverse_report(earlier_plus["A"], earlier_plus["B"])
    earlier_face = face_report(earlier_plus["C"], earlier_plus["D"])
    later_union_reverse = reverse_report(later_union_sets["A"], later_union_sets["B"])
    later_union_face = face_report(later_union_sets["C"], later_union_sets["D"])
    own_reverse = reverse_report(
        own_lock_in_set(frozenset(), letters["A"]),
        own_lock_in_set(frozenset(), letters["B"]),
    )
    own_face = face_report(
        own_lock_in_set(frozenset(), letters["C"]),
        own_lock_in_set(frozenset(), letters["D"]),
    )
    uses_la = reverse_hold_uses_own_letter(plus_sets["A"], plus_sets["B"], letters["A"])
    reverse_uses_la = (
        letters["A"] != "UNDEFINED"
        and reverse_status == "hold"
        and isinstance(letters["A"], tuple)
        and any(add(letters["A"], b) == ZERO for b in plus_sets["B"])
        and not any(
            add(a, b) == ZERO
            for a in neighbor_sets["A"]
            for b in plus_sets["B"]
        )
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(f"reverse_HOLD_uses_L(A)={uses_la}")
    print(
        "per_element: each lock vector in same-tick-inclusive six-neighbor "
        "locks union L(q) when L(q) is defined"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
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

    def plus_from(ticks_map, locks_map, probes=PROBES):
        out: dict[str, frozenset[Point]] = {}
        for name in ("A", "B", "C", "D"):
            site = probes[name]
            pairs = own_tick_neighbor_locks(site, ticks_map, locks_map)
            letter = unique_own_incoming_letter(locks_map[site])
            out[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
        return out

    nsze2sam_plus = plus_from(nsze2sam_ticks, nsze2sam_locks)
    nsze2sam_reverse = reverse_report(nsze2sam_plus["A"], nsze2sam_plus["B"])
    nsze2sam_face = face_report(nsze2sam_plus["C"], nsze2sam_plus["D"])

    nsze2_plus = plus_from(nsze2_ticks, nsze2_locks)
    nsze2_reverse = reverse_report(nsze2_plus["A"], nsze2_plus["B"])
    nsze2_face = face_report(nsze2_plus["C"], nsze2_plus["D"])

    nsze3inc_plus = plus_from(nsze3inc_ticks, nsze3inc_locks)
    nsze3inc_reverse = reverse_report(nsze3inc_plus["A"], nsze3inc_plus["B"])
    nsze3inc_face = face_report(nsze3inc_plus["C"], nsze3inc_plus["D"])

    nszsam_plus = plus_from(nszsam_ticks, nszsam_locks)
    nszsam_reverse = reverse_report(nszsam_plus["A"], nszsam_plus["B"])
    nszsam_face = face_report(nszsam_plus["C"], nszsam_plus["D"])

    this_x_plus = plus_from(ticks, locks, X_PROBES)
    this_x_reverse = reverse_report(this_x_plus["A"], this_x_plus["B"])
    this_x_face = face_report(this_x_plus["C"], this_x_plus["D"])

    nszpar_plus = plus_from(nszpar_ticks, nszpar_locks)
    nszpar_reverse = reverse_report(nszpar_plus["A"], nszpar_plus["B"])
    nszpar_face = face_report(nszpar_plus["C"], nszpar_plus["D"])

    nsparx_plus = plus_from(nspar_ticks, nspar_locks, X_PROBES)
    nsparx_reverse = reverse_report(nsparx_plus["A"], nsparx_plus["B"])
    nsparx_face = face_report(nsparx_plus["C"], nsparx_plus["D"])

    nspary_plus = plus_from(nspar_ticks, nspar_locks)
    nspary_reverse = reverse_report(nspary_plus["A"], nspary_plus["B"])
    nspary_face = face_report(nspary_plus["C"], nspary_plus["D"])

    nsopin_plus = plus_from(nsopp_ticks, nsopp_locks)
    nsopin_reverse = reverse_report(nsopin_plus["A"], nsopin_plus["B"])
    nsopin_face = face_report(nsopin_plus["C"], nsopin_plus["D"])

    nfexist_plus = plus_from(perp_ticks, perp_locks)
    nfexist_reverse = reverse_report(nfexist_plus["A"], nfexist_plus["B"])
    nfexist_face = face_report(nfexist_plus["C"], nfexist_plus["D"])

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-own-letter-and-plus-set",
        letters["A"] == E2
        and neighbor_lists["A"]
        == (
            (ORIGIN, E3),
            ((0, 1, 1), E2),
        )
        and neighbor_sets["A"] == plus_a
        and plus_sets["A"] == plus_a,
        str((letters["A"], plus_sets["A"])),
    )
    checks.check(
        "theorem1-B-own-letter-and-plus-set",
        letters["B"] == "UNDEFINED"
        and neighbor_lists["B"]
        == (
            ((0, 1, 1), E2),
            ((1, 0, 1), E1),
            (PROBES["D"], E2),
            (PROBES["D"], E1),
        )
        and neighbor_sets["B"] == mixed_b
        and plus_sets["B"] == mixed_b,
        str((letters["B"], plus_sets["B"])),
    )
    checks.check(
        "theorem1-C-own-letter-and-plus-set",
        letters["C"] == "UNDEFINED"
        and neighbor_lists["C"]
        == (
            ((1, 2, 0), E2),
            ((-1, 2, 0), E2),
            (PROBES["A"], E2),
            ((0, 2, 1), NEG_E1),
            ((0, 2, 1), NEG_E3),
            ((0, 2, 1), E1),
            ((0, 2, -1), E2),
        )
        and neighbor_sets["C"] == mixed_c
        and plus_sets["C"] == mixed_c,
        str((letters["C"], plus_sets["C"])),
    )
    checks.check(
        "theorem1-D-own-letter-and-plus-set",
        letters["D"] == "UNDEFINED"
        and neighbor_lists["D"]
        == (
            (PROBES["A"], E2),
            ((1, 0, 0), E1),
            (PROBES["B"], E2),
            (PROBES["B"], E1),
        )
        and neighbor_sets["D"] == mixed_d
        and plus_sets["D"] == mixed_d,
        str((letters["D"], plus_sets["D"])),
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E2
        and ticks[E2] == 1
        and locks[E2] == {E2}
        and letters["A"] == E2
        and ORIGIN in ticks
        and ticks[ORIGIN] == 0
        and E2 not in {site for site, _lock in TWO_SITE_SEEDS}
        and E3 in {site for site, _lock in TWO_SITE_SEEDS},
    )
    checks.check(
        "theorem1-A-unique-incoming",
        letters["A"] == E2
        and locks[PROBES["A"]] == {E2}
        and plus_sets["A"] == plus_a,
    )
    checks.check(
        "theorem1-B-mixed-incoming-not-singleton",
        letters["B"] == "UNDEFINED"
        and locks[PROBES["B"]] == {E1, E2}
        and plus_sets["B"] == mixed_b,
    )
    checks.check(
        "theorem1-reverse-hold-does-not-use-L-A",
        uses_la is False
        and reverse_uses_la is False
        and reverse_status == "fail"
        and letters["A"] == E2
        and plus_sets["A"] == plus_a
        and E2 in plus_sets["A"]
        and E2 in plus_sets["B"]
        and add(E2, E2) != ZERO,
        str((uses_la, reverse_status)),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == mixed_b
        and add(E2, E1) != ZERO
        and add(E2, E2) != ZERO
        and add(E3, E1) != ZERO
        and add(E3, E2) != ZERO
        and reverse_status != "hold"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and plus_sets["C"] == mixed_c
        and plus_sets["D"] == mixed_d
        and NEG_E1 in plus_sets["C"]
        and E1 in plus_sets["D"]
        and add(NEG_E1, E1) == ZERO
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-leftover-of-sametick-exclude-q",
        neighbor_sets["A"] == plus_a
        and neighbor_sets["B"] == mixed_b
        and neighbor_sets["C"] == mixed_c
        and neighbor_sets["D"] == mixed_d
        and plus_sets["A"] == neighbor_sets["A"]
        and plus_sets["D"] == neighbor_sets["D"]
        and letters["A"] == E2
        and letters["D"] == "UNDEFINED"
        and E2 in neighbor_sets["A"]
        and exclude_reverse == "fail"
        and exclude_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "not-leftover-of-strictly-earlier-own-lock-in",
        earlier_plus["A"] == plus_a
        and earlier_plus["B"] == mixed_b
        and earlier_plus["C"] == frozenset({E2})
        and earlier_plus["D"] == mixed_d
        and earlier_reverse == "fail"
        and earlier_face == "fail"
        and plus_sets["C"] != earlier_plus["C"]
        and neighbor_sets["C"] != earlier_sets["C"]
        and reverse_status == "fail"
        and face_status == "hold"
        and face_status != earlier_face,
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        letters["A"] == E2
        and letters["B"] == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED"
        and own_reverse == "UNDEFINED"
        and own_face == "UNDEFINED"
        and reverse_status == "fail"
        and face_status == "hold"
        and reverse_status != own_reverse
        and face_status != own_face
        and plus_sets["A"] != frozenset({E2})
        and plus_sets["B"] != frozenset()
        and plus_sets["C"] != frozenset()
        and plus_sets["D"] != frozenset(),
    )
    checks.check(
        "not-leftover-of-later-tick-union-own",
        later_union_sets["A"] == later_union_a
        and later_union_sets["B"] == later_union_b
        and later_union_sets["C"] == mixed_c
        and later_union_sets["D"] == later_union_d
        and later_union_reverse == "hold"
        and later_union_face == "hold"
        and reverse_status == "fail"
        and plus_sets["A"] != later_union_sets["A"]
        and plus_sets["B"] != later_union_sets["B"]
        and plus_sets["D"] != later_union_sets["D"]
        and NEG_E1 in later_union_sets["A"]
        and NEG_E1 not in plus_sets["A"]
        and later_common == 4
        and later_common != ticks[PROBES["A"]],
    )
    checks.check(
        "same-tick-union-fails-reverse-without-later-T",
        reverse_status == "fail"
        and later_union_reverse == "hold"
        and NEG_E1 not in plus_sets["A"]
        and NEG_E1 in later_union_sets["A"]
        and uses_la is False
        and later_common == 4
        and ticks[PROBES["A"]] == 1,
    )
    checks.check(
        "no-global-later-T-in-letter",
        all(
            ticks[neighbor] <= ticks[PROBES[name]]
            for name in ("A", "B", "C", "D")
            for neighbor, _lock in neighbor_lists[name]
        )
        and any(
            ticks[neighbor] == ticks[PROBES[name]]
            for name in ("A", "B", "C", "D")
            for neighbor, _lock in neighbor_lists[name]
        )
        and later_common
        == max(
            ticks[PROBES["A"]],
            ticks[PROBES["B"]],
            ticks[PROBES["C"]],
            ticks[PROBES["D"]],
        )
        and ticks[PROBES["A"]] != later_common,
    )
    checks.check(
        "not-leftover-of-this-process-x-probes",
        probe_sites != x_probe_sites
        and this_x_reverse == "fail"
        and this_x_face == "hold"
        and reverse_status == "fail"
        and plus_sets["A"] != this_x_plus["A"]
        and plus_sets["C"] != this_x_plus["C"]
        and this_x_plus["A"] == frozenset({E1, E3}),
        str((this_x_reverse, this_x_face, this_x_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nsze2sam-plus-e2",
        TWO_SITE_SEEDS != NSZE2SAM_SEEDS
        and locks[ORIGIN] == {E3}
        and nsze2sam_locks[ORIGIN] == {E2}
        and nsze2sam_reverse == "hold"
        and nsze2sam_face == "hold"
        and reverse_status == "fail"
        and reverse_status != nsze2sam_reverse
        and ticks[PROBES["A"]] == 1
        and nsze2sam_ticks[PROBES["A"]] == 3
        and plus_sets["A"] != nsze2sam_plus["A"],
        str((nsze2sam_reverse, nsze2sam_face, nsze2sam_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nsze3inc-pm-e3",
        TWO_SITE_SEEDS != NSZE3INC_SEEDS
        and locks[E3] == {E3}
        and nsze3inc_locks[E3] == {NEG_E3}
        and add(E3, E3) != ZERO
        and add(E3, NEG_E3) == ZERO
        and nsze3inc_reverse == "fail"
        and nsze3inc_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold"
        and plus_sets["A"] == nsze3inc_plus["A"]
        and plus_sets["B"] == nsze3inc_plus["B"]
        and plus_sets["C"] == nsze3inc_plus["C"]
        and plus_sets["D"] == nsze3inc_plus["D"]
        and ticks[E3] == 0
        and nsze3inc_ticks[E3] == 0,
        str((locks[E3], nsze3inc_locks[E3], nsze3inc_reverse, nsze3inc_face)),
    )
    checks.check(
        "not-leftover-of-nsze2inc-pm-e2",
        TWO_SITE_SEEDS != NSZE2INC_SEEDS
        and nsze2_reverse == "hold"
        and nsze2_face == "hold"
        and reverse_status == "fail"
        and reverse_status != nsze2_reverse
        and plus_sets["A"] != nsze2_plus["A"],
        str((nsze2_reverse, nsze2_face, nsze2_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nszsaminc-plus-e1",
        TWO_SITE_SEEDS != NSZSAMINC_SEEDS
        and nszsam_reverse == "fail"
        and nszsam_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold"
        and ticks[PROBES["A"]] == 1
        and nszsam_ticks[PROBES["A"]] == 1
        and plus_sets["A"] != nszsam_plus["A"]
        and plus_sets["A"] == plus_a
        and nszsam_plus["A"] == frozenset({E1, E2})
        and locks[ORIGIN] == {E3}
        and nszsam_locks[ORIGIN] == {E1},
        str((nszsam_reverse, nszsam_face, nszsam_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nszparinc-pm-e1",
        TWO_SITE_SEEDS != NSZPARINC_SEEDS
        and nszpar_reverse == "fail"
        and nszpar_face == "hold"
        and reverse_status == "fail"
        and plus_sets["A"] != nszpar_plus["A"]
        and nszpar_plus["A"] == frozenset({E1, E2}),
        str((nszpar_reverse, nszpar_face, nszpar_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nspar-x-probes",
        TWO_SITE_SEEDS != NSPAR_SEEDS
        and probe_sites != x_probe_sites
        and nsparx_reverse == "fail"
        and nsparx_face == "hold"
        and reverse_status == "fail"
        and plus_sets["A"] != nsparx_plus["A"]
        and ticks[PROBES["A"]] != 0
        and nspar_ticks[X_PROBES["A"]] == 0,
        str((nsparx_reverse, nsparx_face, nsparx_plus["A"])),
    )
    checks.check(
        "not-leftover-of-nspar-y-probes",
        TWO_SITE_SEEDS != NSPAR_SEEDS
        and nspary_reverse == "fail"
        and nspary_face == "fail"
        and reverse_status == "fail"
        and face_status == "hold"
        and face_status != nspary_face
        and plus_sets["B"] != nspary_plus["B"]
        and plus_sets["C"] != nspary_plus["C"],
        str((nspary_reverse, nspary_face, nspary_plus["C"])),
    )
    checks.check(
        "not-leftover-of-nsopin-y-probes",
        TWO_SITE_SEEDS != NSOPP_SEEDS
        and nsopin_reverse == "hold"
        and nsopin_face == "hold"
        and reverse_status == "fail"
        and plus_sets["A"] != nsopin_plus["A"]
        and plus_sets["B"] != nsopin_plus["B"]
        and ticks[PROBES["A"]] != 0
        and nsopp_ticks[PROBES["A"]] == 0,
        str((nsopin_reverse, nsopin_face, nsopin_plus["B"])),
    )
    checks.check(
        "not-leftover-of-nfexist-nnseed-y-probes",
        TWO_SITE_SEEDS != PERP_SEEDS
        and reverse_status == "fail"
        and face_status == "hold"
        and nfexist_reverse == "fail"
        and nfexist_face == "fail"
        and plus_sets["A"] != nfexist_plus["A"]
        and plus_sets["B"] != nfexist_plus["B"]
        and plus_sets["C"] != nfexist_plus["C"]
        and ticks[PROBES["A"]] != 0
        and perp_ticks[PROBES["A"]] == 0,
        str((nfexist_reverse, nfexist_face, nfexist_plus["B"])),
    )
    checks.check(
        "sign-lettering-loses-axis",
        named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and named_sign(E3) == "+"
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus_sets["A"]) == add(E2, E3)
        and sum_of_set(plus_sets["B"]) == add(E1, E2)
        and sum_of_set(plus_sets["C"]) == add(E2, NEG_E3)
        and sum_of_set(plus_sets["D"]) == add(E1, E2)
        and add(sum_of_set(plus_sets["A"]), sum_of_set(plus_sets["B"])) != ZERO
        and add(sum_of_set(plus_sets["C"]), sum_of_set(plus_sets["D"])) != ZERO
        and reverse_status == "fail"
        and face_status == "hold"
        and plus_sets["A"] != frozenset({add(E2, E3)})
        and plus_sets["C"] != frozenset({add(E2, NEG_E3)}),
    )
    checks.check(
        "not-unique-vector-leftover",
        len(plus_sets["A"]) > 1
        and len(plus_sets["B"]) > 1
        and len(plus_sets["C"]) > 1
        and len(plus_sets["D"]) > 1
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["B"]]) == 2
        and len(locks[PROBES["C"]]) == 3
        and len(locks[PROBES["D"]]) == 2
        and letters["B"] == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED"
        and plus_sets["C"] == mixed_c
        and reverse_status == "fail",
        str(sorted(locks[PROBES["C"]])),
    )
    checks.check(
        "two-site-z-axis-same-lock-e3-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E3}
        and ticks[E3] == 0
        and locks[E3] == {E3}
        and add(E3, E3) != ZERO
        and dot(E3, E3) == 1
        and PROBES["A"] == E2
        and ticks[PROBES["A"]] == 1
        and TWO_SITE_SEEDS != NSZE2SAM_SEEDS
        and TWO_SITE_SEEDS != NSZE2INC_SEEDS
        and TWO_SITE_SEEDS != NSZE3INC_SEEDS
        and TWO_SITE_SEEDS != NSZSAMINC_SEEDS
        and TWO_SITE_SEEDS != NSZPARINC_SEEDS
        and TWO_SITE_SEEDS != NSOPP_SEEDS
        and TWO_SITE_SEEDS != NSPAR_SEEDS
        and TWO_SITE_SEEDS != PERP_SEEDS,
    )
    checks.check(
        "same-tick-neighbors-at-or-before-own-t",
        all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
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
        ticks.get(add(ORIGIN, step)) != 1 for step in (E3, NEG_E3)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E3, NEG_E3)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[(1, 0, 0)] == 1
        and ticks[(-1, 0, 0)] == 1
        and ticks[E2] == 1
        and ticks[NEG_E2] == 1
        and ticks.get((0, 0, 2)) != 1
        and ticks.get(NEG_E3) != 1
        and ticks[PROBES["A"]] == 1
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
        reverse_report(frozenset({E2}), mixed_b) == "fail"
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "mutation-exclude-q-coincides-on-y-because-undefined-or-already-neighbor",
        neighbor_sets["A"] == plus_sets["A"]
        and neighbor_sets["B"] == plus_sets["B"]
        and neighbor_sets["C"] == plus_sets["C"]
        and neighbor_sets["D"] == plus_sets["D"]
        and letters["A"] == E2
        and letters["A"] in neighbor_sets["A"]
        and letters["D"] == "UNDEFINED"
        and exclude_reverse == reverse_status
        and exclude_face == face_status,
    )
    checks.check(
        "mutation-own-incoming-reverse-would-be-undefined",
        own_reverse == "UNDEFINED"
        and own_face == "UNDEFINED"
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "mutation-sum-would-fail-both-bits",
        add(sum_of_set(plus_sets["A"]), sum_of_set(plus_sets["B"])) != ZERO
        and add(sum_of_set(plus_sets["C"]), sum_of_set(plus_sets["D"])) != ZERO
        and reverse_status == "fail"
        and face_status == "hold",
    )
    checks.check(
        "mutation-later-tick-would-hold-from-different-A",
        later_union_reverse == "hold"
        and later_union_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold"
        and later_union_sets["A"] != plus_sets["A"],
    )
    checks.check(
        "mutation-nsze3inc-y-probes-coincide-seed-partner-differs",
        nsze3inc_reverse == reverse_status
        and nsze3inc_face == face_status
        and plus_sets["A"] == nsze3inc_plus["A"]
        and locks[E3] != nsze3inc_locks[E3]
        and locks[E3] == {E3}
        and nsze3inc_locks[E3] == {NEG_E3},
    )
    checks.check(
        "mutation-nszsaminc-would-use-different-A",
        nszsam_reverse == "fail"
        and nszsam_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold"
        and plus_sets["A"] != nszsam_plus["A"],
    )
    checks.check(
        "mutation-nsze2sam-would-hold-reverse",
        nsze2sam_reverse == "hold"
        and nsze2sam_face == "hold"
        and reverse_status == "fail"
        and face_status == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-plus-sets",
        "S^+(A) = {+e_2, +e_3}" in note
        and "S^+(B) = {+e_1, +e_2}" in note
        and "S^+(C) = {+e_1, −e_1, +e_2, −e_3}" in note
        and "S^+(D) = {+e_1, +e_2}" in note
        and "t(A)=1" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "L(A) = +e_2" in note
        and "L(B) = UNDEFINED" in note
        and "L(C) = UNDEFINED" in note
        and "L(D) = UNDEFINED" in note
        and "+e_3 at (0, 0, 0)" in note
        and "+e_2 at (0, 1, 1)" in note
        and "+e_1 at (1, 0, 1)" in note
        and "+e_2 at (1, 1, 0)" in note
        and "+e_1 at (1, 1, 0)" in note
        and "+e_2 at (1, 2, 0)" in note
        and "+e_2 at (-1, 2, 0)" in note
        and "+e_2 at (0, 1, 0)" in note
        and "−e_1 at (0, 2, 1)" in note
        and "−e_3 at (0, 2, 1)" in note
        and "+e_1 at (0, 2, 1)" in note
        and "+e_2 at (0, 2, -1)" in note
        and "+e_1 at (1, 0, 0)" in note
        and "+e_2 at (1, 1, 1)" in note
        and "+e_1 at (1, 1, 1)" in note,
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
        "note-reverse-hold-does-not-use-L-A",
        "Reverse HOLD uses L(A): no" in note
        and uses_la is False
        and reverse_status == "fail",
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
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
        and "Do not attach" not in note,
    )
    checks.check(
        "note-not-unique-or-sum-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "Face holds." in note
        and "Reverse fails." in note,
    )
    checks.check(
        "note-not-leftover-of-own-incoming",
        "not leftover of the unique own-incoming lock-vector letters"
        in normalized_note
        and "reverse `UNDEFINED`" in note
        and "Reverse: fail" in note,
    )
    checks.check(
        "note-not-leftover-of-sametick-exclude-q",
        "not leftover of same-tick-inclusive existential opposite that excludes"
        in normalized_note
        and "Reverse: fail" in note,
    )
    checks.check(
        "note-not-leftover-of-strictly-earlier-own-lock-in",
        "not leftover of strictly-earlier own-lock-in"
        in normalized_note
        and "S^+(C) = {+e_1, −e_1, +e_2, −e_3}" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick-union-own",
        "not leftover of later-tick union own"
        in normalized_note
        and "does not wait for a global later T" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-nsze2sam",
        "not leftover of nsze2sam z-axis same-lock"
        in normalized_note
        and "L(0,0,1)=+e_3" in note.replace(" ", "")
        and "Reverse: fail" in note
        and "Face: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-nsze3inc",
        "not leftover of nsze3inc z-axis opposite"
        in normalized_note
        and "Reverse: fail" in note
        and "Face: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-nszsaminc",
        "not leftover of nszsaminc z-axis same-lock"
        in normalized_note
        and "Reverse: fail" in note
        and "Face: hold" in note,
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
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-a-is-not-seed-site",
        "A is not a seed site" in note
        and "perpendicular to the seed edge" in normalized_note
        and "y-probes" in normalized_note,
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
        other_retained = other_retained.replace(line, "", 1)
    checks.check(
        "note-no-author-retained-verdict",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/Z_AXIS_SAME_LOCK_E3_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and ticks[PROBES["A"]] == 1
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
