#!/usr/bin/env python3
"""Same-tick-inclusive 6-NN locks union own incoming reverse/face on z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_3 and +e_3 (same lock, perpendicular to the
seed edge). A 6-NN step is allowed iff it is perpendicular to the parent
lock axis. Newly formed sites lock the incoming step. Seeds keep their seed
letters. L(q) is q's own unique incoming lock; if several earliest incoming
steps exist, L(q) is UNDEFINED. At each z-probe's own formation tick t(q),
S^+(q) is the set of locks of 6-NN of q that formed at tick <= t(q) and are
not q, union {L(q)} when L(q) is defined. No global T. Reverse holds iff
some a in S^+(A) and some b in S^+(B) have a+b=(0,0,0). Face holds iff some
c in S^+(C) and some d in S^+(D) have c+d=(0,0,0). Empty S^+ on either side
is UNDEFINED; nonempty with no opposite pair fails. Reverse HOLD does not
use L(A): L(A) is UNDEFINED from three earliest incoming steps, and reverse
holds by neighbor-neighbor from -e_1 at A against +e_1 at B. Face holds from
-e_1 at C against +e_1 at D. Not leftover of strictly-earlier own-lock-in
(reverse fail). Not leftover of same-tick exclude-q (letter still the
union; L(A) UNDEFINED). Not leftover of later-tick union own (five-lock
sets at B and D after a global T). Not leftover of y-axis opposite ±e_3
z-probes (z-probe S^+ coincides because perp-step sees only the lock axis;
seed L(0,1,0)=+e_3 not -e_3; y-probes fail/fail vs hold/fail). Not leftover
of y-axis same-lock +e_3 y-probes (fail/fail, A is a seed). Not leftover of
y-axis same-lock +e_3 x-probes (fail/hold). Not leftover of y-axis opposite
±e_2 z-probes (reverse fail). Uniqueness of incoming locks is not required.
Occupancy n is not used. Named-sign lettering is not used. No unique P_+.
No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    (E2, E3),
)
OPPOSITE_E3_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E2, NEG_E3),
)
Y_AXIS_E2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E2, NEG_E2),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
X_PROBES = {
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
    "four y-axis same-lock +e_3 z-probes are reported. Displayed, not adopted."
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


def reverse_hold_uses_own_letter_a(
    neighbor_a: frozenset[Point],
    neighbor_b: frozenset[Point],
    letter_a: Letter,
    letter_b: Letter,
    plus_a: frozenset[Point],
    plus_b: frozenset[Point],
) -> str:
    """Classify reverse HOLD as using L(A), only neighbor-neighbor, or not hold."""
    status = reverse_report(plus_a, plus_b)
    if status != "hold":
        return "does_not_hold"
    uses_la = False
    if letter_a != "UNDEFINED" and isinstance(letter_a, tuple):
        for b in plus_b:
            if add(letter_a, b) == ZERO:
                uses_la = True
    if uses_la:
        return "uses_L_A"
    if reverse_report(neighbor_a, neighbor_b) == "hold":
        return "only_neighbor_neighbor"
    if letter_b != "UNDEFINED" and isinstance(letter_b, tuple):
        for a in neighbor_a:
            if add(a, letter_b) == ZERO:
                return "uses_L_B_not_L_A"
    return "hold_unclassified"


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


def plus_maps(
    probes: dict[str, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> dict[str, frozenset[Point]]:
    plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        letter = unique_own_incoming_letter(locks[site])
        plus[name] = own_lock_in_set(recorded_lock_set(pairs), letter)
    return plus


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("same-tick-inclusive union own incoming reverse/face on y-axis same-lock +e_3 z-probes")
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
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites
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
        and add(NEG_E3, E3) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(E1, E1) == (2, 0, 0)
        and add(E3, E3) == (0, 0, 2)
        and add(E1, E1) != ZERO
        and add(E3, E3) != ZERO
        and dot(E1, E3) == 0
        and perpendicular(E3, E1)
        and perpendicular(E3, E2)
        and not perpendicular(E3, E3)
        and in_ball(PROBES["C"])
        and not in_ball((0, 0, 4)),
    )
    plus_a = frozenset({E1, NEG_E1, NEG_E2, E3})
    plus_b = frozenset({E1, E3})
    plus_c = frozenset({E1, NEG_E1, E2, E3})
    plus_d = frozenset({E1, E3})
    later_union_a = plus_a
    later_mixed_b = frozenset({E1, NEG_E1, E2, NEG_E2, E3})
    later_mixed_c = plus_c
    later_mixed_d = frozenset({E1, NEG_E1, E2, NEG_E2, E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(plus_a, plus_b) == "hold"
        and existential_opposite(plus_c, plus_d) == "hold"
        and existential_opposite(frozenset({E3}), plus_b) == "fail"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold"
        and existential_opposite(frozenset({E3}), frozenset({E3})) == "fail",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E3,)) == E3
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E3)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E1, E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )
    checks.check(
        "own-lock-in-set-identity",
        own_lock_in_set(plus_a, "UNDEFINED") == plus_a
        and own_lock_in_set(plus_b, E3) == plus_b
        and own_lock_in_set(frozenset({E1}), E3) == plus_d
        and own_lock_in_set(frozenset({E3}), "UNDEFINED") == frozenset({E3})
        and own_lock_in_set(frozenset(), "UNDEFINED") == frozenset(),
    )

    ticks, locks = form()
    later_common = later_tick_T(ticks)
    nnseed_ticks, nnseed_locks = form(NNSEED_SEEDS)
    opp_ticks, opp_locks = form(NSOPP_SEEDS)
    y_axis_e2_ticks, y_axis_e2_locks = form(Y_AXIS_E2_SEEDS)
    opposite_e3_ticks, opposite_e3_locks = form(OPPOSITE_E3_SEEDS)
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
    reverse_channel = reverse_hold_uses_own_letter_a(
        neighbor_sets["A"],
        neighbor_sets["B"],
        letters["A"],
        letters["B"],
        plus_sets["A"],
        plus_sets["B"],
    )
    reverse_uses_la = reverse_channel == "uses_L_A"
    print(f"reverse={reverse_status} face={face_status}")
    print(f"reverse_hold_channel={reverse_channel} reverse_uses_L(A)={reverse_uses_la}")
    print(
        "per_element: each lock vector in same-tick-inclusive six-neighbor "
        "locks union L(q) when L(q) is defined"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
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

    x_plus = plus_maps(X_PROBES, ticks, locks)
    x_reverse = reverse_report(x_plus["A"], x_plus["B"])
    x_face = face_report(x_plus["C"], x_plus["D"])

    y_plus = plus_maps(Y_PROBES, ticks, locks)
    y_reverse = reverse_report(y_plus["A"], y_plus["B"])
    y_face = face_report(y_plus["C"], y_plus["D"])

    nnseed_plus = plus_maps(PROBES, nnseed_ticks, nnseed_locks)
    nnseed_reverse = reverse_report(nnseed_plus["A"], nnseed_plus["B"])
    nnseed_face = face_report(nnseed_plus["C"], nnseed_plus["D"])

    opp_plus = plus_maps(PROBES, opp_ticks, opp_locks)
    opp_reverse = reverse_report(opp_plus["A"], opp_plus["B"])
    opp_face = face_report(opp_plus["C"], opp_plus["D"])

    y_axis_e2_plus = plus_maps(PROBES, y_axis_e2_ticks, y_axis_e2_locks)
    y_axis_e2_reverse = reverse_report(y_axis_e2_plus["A"], y_axis_e2_plus["B"])
    y_axis_e2_face = face_report(y_axis_e2_plus["C"], y_axis_e2_plus["D"])

    opposite_e3_plus = plus_maps(PROBES, opposite_e3_ticks, opposite_e3_locks)
    opposite_e3_reverse = reverse_report(opposite_e3_plus["A"], opposite_e3_plus["B"])
    opposite_e3_face = face_report(opposite_e3_plus["C"], opposite_e3_plus["D"])
    opposite_e3_y = plus_maps(Y_PROBES, opposite_e3_ticks, opposite_e3_locks)
    opposite_e3_y_reverse = reverse_report(opposite_e3_y["A"], opposite_e3_y["B"])
    opposite_e3_y_face = face_report(opposite_e3_y["C"], opposite_e3_y["D"])
    opposite_e3_x = plus_maps(X_PROBES, opposite_e3_ticks, opposite_e3_locks)
    opposite_e3_x_reverse = reverse_report(opposite_e3_x["A"], opposite_e3_x["B"])
    opposite_e3_x_face = face_report(opposite_e3_x["C"], opposite_e3_x["D"])

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
            ((1, 0, 1), E3),
            ((-1, 0, 1), E3),
            ((0, 1, 1), NEG_E1),
            ((0, 1, 1), NEG_E2),
            ((0, 1, 1), E1),
            ((0, -1, 1), E3),
            (ORIGIN, E3),
        )
        and neighbor_sets["A"] == plus_a
        and plus_sets["A"] == plus_a,
        str((letters["A"], plus_sets["A"])),
    )
    checks.check(
        "theorem1-B-own-letter-and-plus-set",
        letters["B"] == E3
        and neighbor_lists["B"]
        == (
            (PROBES["D"], E3),
            ((1, 1, 0), E1),
        )
        and neighbor_sets["B"] == plus_b
        and plus_sets["B"] == plus_b,
        str((letters["B"], plus_sets["B"])),
    )
    checks.check(
        "theorem1-C-own-letter-and-plus-set",
        letters["C"] == E3
        and neighbor_lists["C"]
        == (
            ((0, 1, 2), E3),
            (PROBES["A"], NEG_E1),
            (PROBES["A"], E2),
            (PROBES["A"], E1),
        )
        and neighbor_sets["C"] == plus_c
        and plus_sets["C"] == plus_c,
        str((letters["C"], plus_sets["C"])),
    )
    checks.check(
        "theorem1-D-own-letter-and-plus-set",
        letters["D"] == E3
        and neighbor_lists["D"]
        == (
            (PROBES["B"], E3),
            ((1, 0, 0), E1),
        )
        and neighbor_sets["D"] == plus_d
        and plus_sets["D"] == plus_d,
        str((letters["D"], plus_sets["D"])),
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E3
        and ticks[E3] == 3
        and locks[E3] == {E1, NEG_E1, E2}
        and letters["A"] == "UNDEFINED"
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and locks[ORIGIN] == {E3}
        and locks[E2] == {E3},
    )
    checks.check(
        "theorem1-A-mixed-incoming-B-C-D-unique",
        letters["A"] == "UNDEFINED"
        and letters["B"] == E3
        and letters["C"] == E3
        and letters["D"] == E3
        and locks[PROBES["A"]] == {E1, NEG_E1, E2}
        and locks[PROBES["B"]] == {E3}
        and locks[PROBES["C"]] == {E3}
        and locks[PROBES["D"]] == {E3}
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d,
    )
    checks.check(
        "theorem1-reverse-hold-does-not-use-L-A",
        reverse_status == "hold"
        and reverse_channel == "only_neighbor_neighbor"
        and reverse_uses_la is False
        and letters["A"] == "UNDEFINED"
        and exclude_reverse == "hold"
        and own_reverse == "UNDEFINED"
        and NEG_E1 in plus_sets["A"]
        and E1 in plus_sets["B"]
        and add(NEG_E1, E1) == ZERO,
        reverse_channel,
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and NEG_E1 in plus_sets["A"]
        and E1 in plus_sets["B"]
        and add(NEG_E1, E1) == ZERO
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and add(NEG_E1, E1) == ZERO
        and NEG_E1 in plus_sets["C"]
        and E1 in plus_sets["D"]
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-leftover-of-sametick-exclude-q",
        neighbor_sets["A"] == plus_a
        and neighbor_sets["B"] == plus_b
        and neighbor_sets["C"] == plus_c
        and neighbor_sets["D"] == plus_d
        and plus_sets["A"] == neighbor_sets["A"]
        and plus_sets["D"] == neighbor_sets["D"]
        and letters["A"] == "UNDEFINED"
        and letters["B"] == E3
        and E3 in neighbor_sets["B"]
        and exclude_reverse == "hold"
        and exclude_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-leftover-of-strictly-earlier-own-lock-in",
        earlier_plus["A"] == frozenset({E3})
        and earlier_plus["B"] == plus_b
        and earlier_plus["C"] == plus_c
        and earlier_plus["D"] == plus_d
        and earlier_reverse == "fail"
        and earlier_face == "hold"
        and plus_sets["A"] != earlier_plus["A"]
        and reverse_status != earlier_reverse
        and reverse_status == "hold",
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        letters["A"] == "UNDEFINED"
        and letters["B"] == E3
        and letters["C"] == E3
        and letters["D"] == E3
        and own_reverse == "UNDEFINED"
        and own_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and reverse_status != own_reverse
        and face_status != own_face
        and plus_sets["A"] != frozenset()
        and plus_sets["B"] != frozenset({E3})
        and plus_sets["C"] != frozenset({E3})
        and plus_sets["D"] != frozenset({E3}),
    )
    checks.check(
        "not-leftover-of-later-tick-union-own",
        later_union_sets["A"] == later_union_a
        and later_union_sets["B"] == later_mixed_b
        and later_union_sets["C"] == later_mixed_c
        and later_union_sets["D"] == later_mixed_d
        and later_union_reverse == "hold"
        and later_union_face == "hold"
        and plus_sets["B"] != later_union_sets["B"]
        and plus_sets["D"] != later_union_sets["D"]
        and NEG_E1 in later_union_sets["B"]
        and NEG_E1 not in plus_sets["B"]
        and later_common == 4
        and later_common != ticks[PROBES["A"]],
    )
    checks.check(
        "holding-reverse-does-not-wait-for-later-T",
        reverse_status == "hold"
        and later_union_reverse == "hold"
        and exclude_reverse == "hold"
        and reverse_uses_la is False
        and later_common == 4
        and ticks[PROBES["A"]] == 3
        and plus_sets["B"] != later_union_sets["B"]
        and face_status == "hold",
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
        "not-leftover-of-this-process-xprobe-sametick-union-own",
        probe_sites != x_probe_sites
        and reverse_status == "hold"
        and face_status == "hold"
        and x_reverse == "fail"
        and x_face == "hold"
        and reverse_status != x_reverse
        and plus_sets["A"] != x_plus["A"]
        and E3 in plus_sets["A"]
        and E1 in x_plus["A"],
        str((x_reverse, x_face, x_plus["A"])),
    )
    checks.check(
        "not-leftover-of-this-process-yprobe-sametick-union-own",
        probe_sites != y_probe_sites
        and reverse_status == "hold"
        and face_status == "hold"
        and y_reverse == "fail"
        and y_face == "fail"
        and reverse_status != y_reverse
        and face_status != y_face
        and plus_sets["A"] != y_plus["A"]
        and y_plus["A"] == frozenset({E3})
        and Y_PROBES["A"] == E2
        and ticks[Y_PROBES["A"]] == 0
        and letters["A"] == "UNDEFINED"
        and unique_own_incoming_letter(locks[Y_PROBES["A"]]) == E3,
        str((y_reverse, y_face, y_plus["A"])),
    )
    checks.check(
        "not-leftover-of-y-axis-opposite-e3-zprobes",
        TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and locks[E2] == {E3}
        and opposite_e3_locks[E2] == {NEG_E3}
        and add(E3, NEG_E3) == ZERO
        and plus_sets["A"] == opposite_e3_plus["A"]
        and plus_sets["B"] == opposite_e3_plus["B"]
        and plus_sets["C"] == opposite_e3_plus["C"]
        and plus_sets["D"] == opposite_e3_plus["D"]
        and opposite_e3_reverse == "hold"
        and opposite_e3_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and y_reverse == "fail"
        and y_face == "fail"
        and opposite_e3_y_reverse == "hold"
        and opposite_e3_y_face == "fail"
        and y_plus["A"] != opposite_e3_y["A"]
        and opposite_e3_y["A"] == frozenset({E3, NEG_E3})
        and y_plus["A"] == frozenset({E3}),
        str((opposite_e3_locks[E2], opposite_e3_y["A"])),
    )
    checks.check(
        "not-leftover-of-y-axis-opposite-e3-yprobes",
        TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and probe_sites != y_probe_sites
        and reverse_status == "hold"
        and face_status == "hold"
        and opposite_e3_y_reverse == "hold"
        and opposite_e3_y_face == "fail"
        and face_status != opposite_e3_y_face
        and plus_sets["A"] != opposite_e3_y["A"]
        and NEG_E3 in opposite_e3_y["A"]
        and E3 in opposite_e3_y["A"],
        str((opposite_e3_y_reverse, opposite_e3_y_face, opposite_e3_y["A"])),
    )
    checks.check(
        "not-leftover-of-y-axis-opposite-e3-xprobes",
        TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and probe_sites != x_probe_sites
        and reverse_status == "hold"
        and face_status == "hold"
        and opposite_e3_x_reverse == "fail"
        and opposite_e3_x_face == "hold"
        and reverse_status != opposite_e3_x_reverse
        and plus_sets["D"] != opposite_e3_x["D"]
        and NEG_E3 in opposite_e3_x["D"]
        and NEG_E3 not in plus_sets["D"],
        str((opposite_e3_x_reverse, opposite_e3_x_face, opposite_e3_x["D"])),
    )
    checks.check(
        "not-leftover-of-nnseed-zprobe-sametick-union-own",
        TWO_SITE_SEEDS != NNSEED_SEEDS
        and nnseed_reverse == "fail"
        and nnseed_face == "hold"
        and reverse_status == "hold"
        and reverse_status != nnseed_reverse
        and plus_sets["A"] != nnseed_plus["A"]
        and NEG_E1 in plus_sets["A"]
        and E1 in nnseed_plus["A"]
        and plus_sets["D"] != nnseed_plus["D"]
        and NEG_E2 in nnseed_plus["D"]
        and NEG_E2 not in plus_sets["D"],
        str((nnseed_reverse, nnseed_face, nnseed_plus["A"], nnseed_plus["D"])),
    )
    checks.check(
        "not-leftover-of-nsopp-zprobe-sametick-union-own",
        TWO_SITE_SEEDS != NSOPP_SEEDS
        and opp_reverse == "fail"
        and opp_face == "hold"
        and reverse_status == "hold"
        and reverse_status != opp_reverse
        and plus_sets["A"] != opp_plus["A"]
        and NEG_E1 in plus_sets["A"]
        and E1 in opp_plus["A"],
        str((opp_reverse, opp_face, opp_plus["A"])),
    )
    checks.check(
        "not-leftover-of-y-axis-opposite-e2-zprobes",
        TWO_SITE_SEEDS != Y_AXIS_E2_SEEDS
        and y_axis_e2_reverse == "fail"
        and y_axis_e2_face == "hold"
        and reverse_status == "hold"
        and reverse_status != y_axis_e2_reverse
        and plus_sets["A"] != y_axis_e2_plus["A"]
        and y_axis_e2_plus["A"] == frozenset({E2, E3})
        and E2 in y_axis_e2_plus["A"]
        and E2 not in plus_sets["A"],
        str((y_axis_e2_reverse, y_axis_e2_face, y_axis_e2_plus["A"])),
    )
    checks.check(
        "sign-lettering-loses-axis",
        named_sign(E3) == "+"
        and named_sign(E1) == "+"
        and named_sign(NEG_E1) == "-"
        and named_sign(NEG_E2) == "-"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus_sets["A"]) == add(NEG_E2, E3)
        and sum_of_set(plus_sets["B"]) == add(E1, E3)
        and sum_of_set(plus_sets["C"]) == add(E2, E3)
        and sum_of_set(plus_sets["D"]) == add(E1, E3)
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
        len(locks[PROBES["A"]]) == 3
        and locks[PROBES["A"]] == {E1, NEG_E1, E2}
        and letters["A"] == "UNDEFINED"
        and letters["B"] == E3
        and letters["C"] == E3
        and letters["D"] == E3
        and plus_sets["A"] == plus_a
        and plus_sets["C"] == plus_c
        and reverse_status == "hold"
        and face_status == "hold"
        and len(locks[(1, 2, 0)]) == 2
        and locks[(1, 2, 0)] == {E1, E2},
        str((sorted(locks[PROBES["A"]]), sorted(locks[(1, 2, 0)]))),
    )
    checks.check(
        "y-axis-same-lock-e3-seed-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E3}
        and ticks[E2] == 0
        and locks[E2] == {E3}
        and add(E3, E3) != ZERO
        and add(E3, NEG_E3) == ZERO
        and dot(E3, E2) == 0
        and PROBES["A"] != E2
        and TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and TWO_SITE_SEEDS != NNSEED_SEEDS
        and TWO_SITE_SEEDS != NSOPP_SEEDS
        and TWO_SITE_SEEDS != Y_AXIS_E2_SEEDS,
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
        ticks.get(add(E2, step)) != 1 for step in (E3, NEG_E3)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[(1, 0, 0)] == 1
        and ticks[(-1, 0, 0)] == 1
        and ticks[(0, -1, 0)] == 1
        and ticks[E3] == 3
        and ticks[(0, 0, -1)] == 3
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
        reverse_report(frozenset({E3}), plus_b) == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-exclude-q-sets-coincide-because-L-A-undefined",
        exclude_reverse == "hold"
        and reverse_status == "hold"
        and letters["A"] == "UNDEFINED"
        and plus_sets["A"] == neighbor_sets["A"],
    )
    checks.check(
        "mutation-own-incoming-reverse-undefined",
        own_reverse == "UNDEFINED"
        and own_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-earlier-would-fail-reverse",
        earlier_reverse == "fail" and reverse_status == "hold",
    )
    checks.check(
        "mutation-later-tick-changes-B-and-D-sets",
        later_union_reverse == "hold"
        and later_union_face == "hold"
        and plus_sets["B"] != later_union_sets["B"]
        and plus_sets["D"] != later_union_sets["D"],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-plus-sets",
        "S^+(A) = {+e_1, −e_1, −e_2, +e_3}" in note
        and "S^+(B) = {+e_1, +e_3}" in note
        and "S^+(C) = {+e_1, −e_1, +e_2, +e_3}" in note
        and "S^+(D) = {+e_1, +e_3}" in note
        and "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "L(A) = UNDEFINED" in note
        and "L(B) = +e_3" in note
        and "L(C) = +e_3" in note
        and "L(D) = +e_3" in note
        and "+e_3 at (1, 0, 1)" in note
        and "+e_3 at (-1, 0, 1)" in note
        and "−e_1 at (0, 1, 1)" in note
        and "−e_2 at (0, 1, 1)" in note
        and "+e_1 at (0, 1, 1)" in note
        and "+e_3 at (0, -1, 1)" in note
        and "+e_3 at (0, 0, 0)" in note
        and "+e_1 at (1, 1, 0)" in note
        and "+e_3 at (0, 1, 2)" in note
        and "−e_1 at (0, 0, 1)" in note
        and "+e_2 at (0, 0, 1)" in note
        and "+e_1 at (0, 0, 1)" in note
        and "+e_3 at (1, 1, 1)" in note
        and "+e_1 at (1, 0, 0)" in note,
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
        "note-reports-reverse-hold-channel",
        "does not use L(A)" in normalized_note
        and "own–neighbor" in note
        and "own–own" in note
        and "neighbor–neighbor" in note
        and "UNDEFINED" in note,
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
        and "Reverse holds." in note,
    )
    checks.check(
        "note-not-leftover-of-own-incoming",
        "not leftover of the unique own-incoming lock-vector letters"
        in normalized_note
        and "reverse `UNDEFINED`" in note
        and "Reverse: hold" in note,
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
        and "S^+(A) = {+e_1, −e_1, −e_2, +e_3}" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick-union-own",
        "not leftover of later-tick union own"
        in normalized_note
        and "does not wait for a global later T" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-nnseed-zprobe-own-lock-in",
        "not leftover of same-tick-inclusive union own on the four nnseed z-probes"
        in normalized_note
        and "Reverse: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-y-axis-e2",
        "not leftover of y-axis opposite ±e_2" in normalized_note
        or "not leftover of the y-axis opposite `±e_2`" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-y-axis-opposite-e3-zprobes",
        "not leftover of y-axis opposite ±e_3 z-probes" in normalized_note
        or "not leftover of y-axis opposite `±e_3` z-probes" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-same-lock-yprobes",
        "not leftover of same-tick-inclusive union own on the four y-axis same-lock `+e_3` y-probes"
        in normalized_note
        or "not leftover of this process on the four y-probes" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-same-lock-xprobes",
        "not leftover of same-tick-inclusive union own on the four y-axis same-lock `+e_3` x-probes"
        in normalized_note
        or "not leftover of this process on the four x-probes" in normalized_note,
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
        "note-a-is-not-seed",
        "A is not a seed" in note
        and "perpendicular to the seed edge" in normalized_note,
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
        '    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_SAMETICK_UNION_OWN_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
