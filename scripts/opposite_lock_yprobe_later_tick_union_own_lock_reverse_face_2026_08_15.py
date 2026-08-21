#!/usr/bin/env python3
"""Later-tick 6-NN locks union own incoming reverse/face on four nsopp y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters. L(q) is q's own unique incoming lock;
if several earliest incoming steps exist, L(q) is UNDEFINED. Let T be the
max of t(A), t(B), t(C), t(D) among those defined in B_3(0): the first later
tick at which all four y-probes are recorded. At tick T, S_*(q) is the set
of locks of 6-NN of q that formed at tick <= T and are not q. S^T_+(q) is
S_*(q) union {L(q)} when L(q) is defined. Reverse holds iff some a in
S^T_+(A) and some b in S^T_+(B) have a+b=(0,0,0). Face holds iff some c in
S^T_+(C) and some d in S^T_+(D) have c+d=(0,0,0). Empty S^T_+ on either
side is UNDEFINED; nonempty with no opposite pair fails. Not leftover of
formation-tick own-lock-in (formation t, not T). Not leftover of later-tick
existential opposite that excludes q (no own). Uniqueness of incoming
locks is not required. Occupancy n is not used. Named-sign lettering is not
used. No unique P_+. No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_LATER_TICK_UNION_OWN_LOCK_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_LATER_TICK_UNION_OWN_LOCK_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "P_+",
)
CLAIM_SCOPE = (
    "Reverse and face from existential opposite in later-tick "
    "6-NN locks union the probe's own incoming lock on the four nsopp "
    "y-probes are reported. Displayed, not adopted."
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
    """Set of later-tick six-neighbor locks. Duplicates collapse."""
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


def later_tick_union_own_lock_set(
    star: frozenset[Point], letter: Letter
) -> frozenset[Point]:
    """S^T_+(q) = S_*(q) union {L(q)} when L(q) is defined."""
    if letter == "UNDEFINED":
        return star
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return star | {letter}


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
    """Reverse iff some a in S^T_+(A) and some b in S^T_+(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point], set_d: frozenset[Point]) -> str:
    """Face iff some c in S^T_+(C) and some d in S^T_+(D) have c+d=(0,0,0)."""
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


def later_tick_T(
    ticks: dict[Point, int],
    probes: dict[str, Point] = PROBES,
) -> int | None:
    """First later tick at which all named probes are recorded, or None."""
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
    """Locks of 6-NN of site formed at tick <= common_tick, site excluded."""
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


def formation_tick_neighbor_locks(
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

    print("later-tick 6-NN union own incoming reverse/face on opposite-lock y-probes")
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    mixed_ab = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    mixed_cd = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    all_six = frozenset(NN)
    formation_plus_a = frozenset({NEG_E1})
    formation_plus_b = frozenset({E1, E3})
    formation_plus_c = frozenset({NEG_E1, E2})
    formation_plus_d = frozenset({E1, NEG_E1})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E2, E3})) == "fail"
        and existential_opposite(all_six, mixed_ab) == "hold"
        and existential_opposite(mixed_cd, mixed_cd) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((E1,)) == E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED",
    )
    checks.check(
        "later-tick-union-own-lock-identity",
        later_tick_union_own_lock_set(mixed_ab, NEG_E1) == all_six
        and later_tick_union_own_lock_set(mixed_ab, E1) == mixed_ab
        and later_tick_union_own_lock_set(mixed_cd, E2) == mixed_cd
        and later_tick_union_own_lock_set(mixed_cd, "UNDEFINED") == mixed_cd
        and later_tick_union_own_lock_set(frozenset(), NEG_E1) == frozenset({NEG_E1}),
    )

    ticks, locks = form()
    common_tick = later_tick_T(ticks)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    perp_common = later_tick_T(perp_ticks, X_PROBES)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and common_tick is not None,
    )
    assert common_tick is not None
    assert perp_common is not None

    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    star_sets: dict[str, frozenset[Point]] = {}
    letters: dict[str, Letter] = {}
    plus_sets: dict[str, frozenset[Point]] = {}
    formation_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = later_tick_neighbor_locks(site, ticks, locks, common_tick)
        neighbor_lists[name] = pairs
        star_sets[name] = recorded_lock_set(pairs)
        letter = unique_own_incoming_letter(locks[site])
        letters[name] = letter
        plus_sets[name] = later_tick_union_own_lock_set(star_sets[name], letter)
        earlier = recorded_lock_set(formation_tick_neighbor_locks(site, ticks, locks))
        formation_plus[name] = later_tick_union_own_lock_set(earlier, letter)
        incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} L={letter_display(letter)} "
            f"S_*={set_display(star_sets[name])} "
            f"S^T_+={set_display(plus_sets[name])} incoming={incoming}"
        )

    print(
        f"T={common_tick} "
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]}"
    )
    reverse_status = reverse_report(plus_sets["A"], plus_sets["B"])
    face_status = face_report(plus_sets["C"], plus_sets["D"])
    star_reverse = reverse_report(star_sets["A"], star_sets["B"])
    star_face = face_report(star_sets["C"], star_sets["D"])
    formation_reverse = reverse_report(formation_plus["A"], formation_plus["B"])
    formation_face = face_report(formation_plus["C"], formation_plus["D"])
    own_reverse = reverse_report(
        later_tick_union_own_lock_set(frozenset(), letters["A"]),
        later_tick_union_own_lock_set(frozenset(), letters["B"]),
    )
    own_face = face_report(
        later_tick_union_own_lock_set(frozenset(), letters["C"]),
        later_tick_union_own_lock_set(frozenset(), letters["D"]),
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: each lock vector in the union of later-tick "
        "six-neighbor locks with L(q) when L(q) is defined"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four S^T_+ lock sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    nslate_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    nslate_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = X_PROBES[name]
        pairs = later_tick_neighbor_locks(site, perp_ticks, perp_locks, perp_common)
        nslate_lists[name] = pairs
        nslate_sets[name] = recorded_lock_set(pairs)
    nslate_reverse = reverse_report(nslate_sets["A"], nslate_sets["B"])
    nslate_face = face_report(nslate_sets["C"], nslate_sets["D"])

    checks.check(
        "theorem1-later-tick-T",
        common_tick == 3
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and common_tick
        == max(
            ticks[PROBES["A"]],
            ticks[PROBES["B"]],
            ticks[PROBES["C"]],
            ticks[PROBES["D"]],
        ),
        str(common_tick),
    )
    checks.check(
        "theorem1-A-letter-star-plus",
        letters["A"] == NEG_E1
        and neighbor_lists["A"]
        == (
            (PROBES["D"], NEG_E2),
            (PROBES["D"], NEG_E3),
            (PROBES["D"], E3),
            ((-1, 1, 0), NEG_E2),
            ((-1, 1, 0), NEG_E3),
            ((-1, 1, 0), E3),
            (PROBES["C"], E2),
            (ORIGIN, E1),
            ((0, 1, 1), E3),
            ((0, 1, -1), NEG_E3),
        )
        and star_sets["A"] == mixed_ab
        and plus_sets["A"] == all_six
        and NEG_E1 not in star_sets["A"]
        and NEG_E1 in plus_sets["A"],
        str((letters["A"], star_sets["A"], plus_sets["A"])),
    )
    checks.check(
        "theorem1-B-letter-star-plus",
        letters["B"] == E1
        and neighbor_lists["B"]
        == (
            ((0, 1, 1), E3),
            ((1, 2, 1), E3),
            ((1, 2, 1), E2),
            ((1, 2, 1), E1),
            ((1, 0, 1), E1),
            ((1, 1, 2), E3),
            (PROBES["D"], NEG_E2),
            (PROBES["D"], NEG_E3),
            (PROBES["D"], E3),
        )
        and star_sets["B"] == mixed_ab
        and plus_sets["B"] == mixed_ab,
        str((letters["B"], star_sets["B"], plus_sets["B"])),
    )
    checks.check(
        "theorem1-C-letter-star-plus",
        letters["C"] == E2
        and neighbor_lists["C"]
        == (
            ((1, 2, 0), E1),
            ((-1, 2, 0), NEG_E1),
            (PROBES["A"], NEG_E1),
            ((0, 2, 1), E3),
            ((0, 2, 1), E2),
            ((0, 2, -1), NEG_E3),
            ((0, 2, -1), E2),
        )
        and star_sets["C"] == mixed_cd
        and plus_sets["C"] == mixed_cd,
        str((letters["C"], star_sets["C"], plus_sets["C"])),
    )
    checks.check(
        "theorem1-D-letter-star-plus",
        letters["D"] == "UNDEFINED"
        and neighbor_lists["D"]
        == (
            (PROBES["A"], NEG_E1),
            ((1, 2, 0), E1),
            ((1, 0, 0), NEG_E3),
            ((1, 0, 0), E3),
            ((1, 0, 0), E2),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and star_sets["D"] == mixed_cd
        and plus_sets["D"] == mixed_cd,
        str((letters["D"], star_sets["D"], plus_sets["D"])),
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
        and locks[PROBES["D"]] == {NEG_E2, NEG_E3, E3}
        and plus_sets["D"] == mixed_cd,
    )
    checks.check(
        "theorem1-A-B-mixed-vectors-remain-a-set",
        plus_sets["A"] == all_six
        and plus_sets["B"] == mixed_ab
        and len(plus_sets["A"]) == 6
        and len(plus_sets["B"]) == 5,
    )
    checks.check(
        "theorem1-C-D-mixed-vectors-remain-a-set",
        plus_sets["C"] == mixed_cd
        and plus_sets["D"] == mixed_cd
        and len(plus_sets["C"]) == 5
        and len(plus_sets["D"]) == 5,
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and plus_sets["A"] == all_six
        and plus_sets["B"] == mixed_ab
        and NEG_E1 in plus_sets["A"]
        and E1 in plus_sets["B"]
        and add(NEG_E1, E1) == ZERO
        and add(E2, NEG_E2) == ZERO
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and plus_sets["C"] == mixed_cd
        and plus_sets["D"] == mixed_cd
        and NEG_E1 in plus_sets["C"]
        and E1 in plus_sets["D"]
        and add(NEG_E1, E1) == ZERO
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-leftover-of-formation-tick-own-lock-in",
        formation_plus["A"] == formation_plus_a
        and formation_plus["B"] == formation_plus_b
        and formation_plus["C"] == formation_plus_c
        and formation_plus["D"] == formation_plus_d
        and formation_reverse == "hold"
        and formation_face == "hold"
        and plus_sets["A"] != formation_plus["A"]
        and plus_sets["B"] != formation_plus["B"]
        and plus_sets["C"] != formation_plus["C"]
        and plus_sets["D"] != formation_plus["D"]
        and common_tick != ticks[PROBES["A"]]
        and common_tick != ticks[PROBES["C"]],
    )
    checks.check(
        "not-leftover-of-later-tick-exclude-q",
        star_sets["A"] == mixed_ab
        and star_sets["B"] == mixed_ab
        and star_sets["C"] == mixed_cd
        and star_sets["D"] == mixed_cd
        and star_reverse == "hold"
        and star_face == "hold"
        and plus_sets["A"] != star_sets["A"]
        and NEG_E1 not in star_sets["A"]
        and NEG_E1 in plus_sets["A"]
        and plus_sets["B"] == star_sets["B"]
        and plus_sets["C"] == star_sets["C"]
        and plus_sets["D"] == star_sets["D"],
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and letters["D"] == "UNDEFINED"
        and own_reverse == "hold"
        and own_face == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold"
        and face_status != own_face
        and plus_sets["A"] != frozenset({NEG_E1})
        and plus_sets["C"] != frozenset({E2})
        and plus_sets["D"] != frozenset(),
    )
    checks.check(
        "not-leftover-of-nslate-nnseed-x-probes",
        TWO_SITE_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and nslate_sets["A"] == frozenset({E1})
        and nslate_sets["B"] == frozenset({E1, E2, E3})
        and nslate_sets["C"] == frozenset({NEG_E2})
        and nslate_sets["D"] == frozenset({E1, E2, NEG_E2, E3, NEG_E3})
        and nslate_reverse == "fail"
        and nslate_face == "hold"
        and reverse_status == "hold"
        and reverse_status != nslate_reverse
        and plus_sets["A"] != nslate_sets["A"],
    )
    checks.check(
        "later-tick-includes-post-formation-neighbors",
        any(ticks[neighbor] > ticks[PROBES["A"]] for neighbor, _lock in neighbor_lists["A"])
        and any(ticks[neighbor] > ticks[PROBES["B"]] for neighbor, _lock in neighbor_lists["B"])
        and any(ticks[neighbor] > ticks[PROBES["C"]] for neighbor, _lock in neighbor_lists["C"])
        and all(
            ticks[neighbor] <= ticks[PROBES["D"]] for neighbor, _lock in neighbor_lists["D"]
        ),
    )
    checks.check(
        "sign-lettering-loses-axis",
        named_sign(E2) == "+"
        and named_sign(NEG_E2) == "-"
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "own-lock-enters-A-plus-set",
        star_sets["A"] == mixed_ab
        and plus_sets["A"] == all_six
        and letters["A"] == NEG_E1
        and NEG_E1 not in star_sets["A"]
        and NEG_E1 in plus_sets["A"],
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus_sets["A"]) == ZERO
        and sum_of_set(plus_sets["B"]) == E1
        and sum_of_set(plus_sets["C"]) == E2
        and sum_of_set(plus_sets["D"]) == E2
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
        len(locks[PROBES["D"]]) == 3
        and letters["D"] == "UNDEFINED"
        and plus_sets["D"] == mixed_cd
        and face_status == "hold",
        str(sorted(locks[PROBES["D"]])),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS,
    )
    checks.check(
        "later-tick-not-self-and-formed-by-T",
        all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
        and all(
            ticks[neighbor] <= common_tick
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
        "mutation-empty-plus-set-undefined",
        recorded_lock_set(()) == frozenset()
        and reverse_report(frozenset(), plus_sets["B"]) == "UNDEFINED"
        and face_report(plus_sets["C"], frozenset()) == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E2, E3})) == "fail"
        and reverse_status == "hold",
    )
    checks.check(
        "mutation-exclude-q-would-omit-own-at-A",
        star_reverse == "hold"
        and reverse_status == "hold"
        and NEG_E1 not in star_sets["A"]
        and plus_sets["A"] != star_sets["A"],
    )
    checks.check(
        "mutation-formation-own-lock-in-different-sets",
        formation_plus["A"] == formation_plus_a
        and plus_sets["A"] == all_six
        and formation_plus["A"] != plus_sets["A"],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-star-and-plus-sets",
        "S_*(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S_*(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S_*(C) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S_*(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S^T_+(A) = {+e_1, −e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^T_+(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^T_+(C) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S^T_+(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "T = max{t(A), t(B), t(C), t(D)} = 3." in note
        and "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "L(A) = −e_1" in note
        and "L(B) = +e_1" in note
        and "L(C) = +e_2" in note
        and "L(D) = UNDEFINED" in note
        and "−e_2 at (1, 1, 0)" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_2 at (0, 2, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "−e_1 at (0, 1, 0)" in note
        and "+e_1 at (1, 2, 0)" in note
        and "−e_3 at (1, 0, 0)" in note,
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
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own incoming lock" in normalized_note
        and "later tick" in normalized_note,
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
        "note-star-excludes-own-and-plus-unions-own",
        "S_*(A)` has no `−e_1`" in note
        and "S^T_+(A)` includes `L(A)=−e_1`" in note
        and "union" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from later-tick six-neighbor locks"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-not-unique-or-sum-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "Reverse holds." in note
        and "Face holds." in note,
    )
    checks.check(
        "note-not-leftover-of-own-incoming",
        "not leftover of the unique own-incoming lock-vector letters"
        in normalized_note
        and "face `UNDEFINED`" in note
        and "Face: hold" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick-exclude-q",
        "not leftover of later-tick existential opposite"
        in normalized_note
        and "excludes `q`" in note
        and "S_*(A)` has no `−e_1`" in note,
    )
    checks.check(
        "note-not-leftover-of-formation-own-lock-in",
        "not leftover of formation-tick own-lock-in"
        in normalized_note
        and "formation t, not T" in normalized_note
        and "S^T_+(A) = {+e_1, −e_1, +e_2, −e_2, +e_3, −e_3}" in note,
    )
    checks.check(
        "note-later-tick-T-defined",
        "first later tick" in normalized_note
        and "all four" in normalized_note
        and "tick `≤ T`" in note,
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
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OPPOSITE_LOCK_YPROBE_LATER_TICK_UNION_OWN_LOCK_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
        and "def later_tick_neighbor_locks(" in source
        and "def later_tick_T(" in source
        and "def unique_own_incoming_letter(" in source
        and "def later_tick_union_own_lock_set(" in source
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
        "source-letter-from-later-tick-union-own-lock",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "later_tick_neighbor_locks" in defined_fns
        and "unique_own_incoming_letter" in defined_fns
        and "later_tick_union_own_lock_set" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
