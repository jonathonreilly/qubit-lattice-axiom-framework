#!/usr/bin/env python3
"""Same-tick-inclusive existential opposite 6-NN reverse/face on four opposite-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each y-probe's own formation tick t(q), S(q) is the set of locks of
6-NN of q that formed at tick <= t(q) (same-tick-inclusive; q excluded). Do
not wait for a global later T. Reverse holds iff some a in S(A) and some b
in S(B) have a+b=(0,0,0). Face holds iff some c in S(C) and some d in S(D)
have c+d=(0,0,0). Empty S on either side is UNDEFINED; nonempty with no
opposite pair fails. Not leftover of strictly-earlier formation-tick
existential opposite on these y-probes (tick < t(q)). Not leftover of
later-tick existential opposite on these y-probes (global T=max t). Not
leftover of unique own-incoming letters. Not unique-vector leftover. Not
sum leftover. Not named-sign lettering. Occupancy n is not used. The probe's
own incoming lock is not used. Uniqueness of incoming locks is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_INCLUSIVE_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_INCLUSIVE_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Reverse and face from existential opposite 6-NN locks formed "
    "by each nsopp y-probe's own tick (same-tick-inclusive, q "
    "excluded, no global later T) are reported. Displayed, not adopted."
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

    print("same-tick-inclusive existential opposite 6-NN reverse/face on opposite-lock y-probes")
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
    mixed_d = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    mixed_b = frozenset({E1, E3})
    later_mixed_ab = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    later_mixed_cd = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(frozenset({NEG_E1}), mixed_d) == "hold"
        and existential_opposite(mixed_d, mixed_d) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold",
    )

    ticks, locks = form()
    later_common = later_tick_T(ticks)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    perp_common = later_tick_T(perp_ticks, X_PROBES)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and later_common is not None,
    )
    assert later_common is not None
    assert perp_common is not None

    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    lock_sets: dict[str, frozenset[Point]] = {}
    earlier_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    earlier_sets: dict[str, frozenset[Point]] = {}
    later_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    later_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        lock_sets[name] = recorded_lock_set(pairs)
        earlier_pairs = strictly_earlier_neighbor_locks(site, ticks, locks)
        earlier_lists[name] = earlier_pairs
        earlier_sets[name] = recorded_lock_set(earlier_pairs)
        later_pairs = later_tick_neighbor_locks(site, ticks, locks, later_common)
        later_lists[name] = later_pairs
        later_sets[name] = recorded_lock_set(later_pairs)
        incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} S={set_display(lock_sets[name])} "
            f"incoming={incoming}"
        )

    print(
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]} "
        f"leftover_T={later_common}"
    )
    reverse_status = reverse_report(lock_sets["A"], lock_sets["B"])
    face_status = face_report(lock_sets["C"], lock_sets["D"])
    earlier_reverse = reverse_report(earlier_sets["A"], earlier_sets["B"])
    earlier_face = face_report(earlier_sets["C"], earlier_sets["D"])
    later_reverse = reverse_report(later_sets["A"], later_sets["B"])
    later_face = face_report(later_sets["C"], later_sets["D"])
    print(f"reverse={reverse_status} face={face_status}")

    nfexist_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    nfexist_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = X_PROBES[name]
        pairs = strictly_earlier_neighbor_locks(site, perp_ticks, perp_locks)
        nfexist_lists[name] = pairs
        nfexist_sets[name] = recorded_lock_set(pairs)
    nfexist_reverse = reverse_report(nfexist_sets["A"], nfexist_sets["B"])
    nfexist_face = face_report(nfexist_sets["C"], nfexist_sets["D"])

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-neighbor-lock-set",
        neighbor_lists["A"] == ((ORIGIN, E1),)
        and lock_sets["A"] == frozenset({E1})
        and ticks[PROBES["A"]] == 0,
        str((neighbor_lists["A"], lock_sets["A"])),
    )
    checks.check(
        "theorem1-B-neighbor-lock-set",
        neighbor_lists["B"]
        == (
            ((0, 1, 1), E3),
            ((1, 0, 1), E1),
        )
        and lock_sets["B"] == mixed_b,
        str((neighbor_lists["B"], lock_sets["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-set",
        neighbor_lists["C"] == ((E2, NEG_E1),)
        and lock_sets["C"] == frozenset({NEG_E1}),
        str((neighbor_lists["C"], lock_sets["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-set",
        neighbor_lists["D"]
        == (
            (E2, NEG_E1),
            ((1, 2, 0), E1),
            ((1, 0, 0), NEG_E3),
            ((1, 0, 0), E3),
            ((1, 0, 0), E2),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and lock_sets["D"] == mixed_d,
        str((neighbor_lists["D"], lock_sets["D"])),
    )
    checks.check(
        "theorem1-D-mixed-vectors-remain-a-set",
        lock_sets["D"] == mixed_d
        and len(lock_sets["D"]) == 5
        and lock_sets["C"] == frozenset({NEG_E1}),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and lock_sets["A"] == frozenset({E1})
        and lock_sets["B"] == mixed_b
        and reverse_status != "hold"
        and reverse_status != "UNDEFINED"
        and add(E1, E1) != ZERO
        and add(E1, E3) != ZERO,
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and lock_sets["C"] == frozenset({NEG_E1})
        and lock_sets["D"] == mixed_d
        and NEG_E1 in lock_sets["C"]
        and E1 in lock_sets["D"]
        and add(NEG_E1, E1) == ZERO
        and lock_sets["C"]
        and lock_sets["D"],
        face_status,
    )
    checks.check(
        "not-leftover-of-strictly-earlier",
        earlier_sets["A"] == frozenset()
        and earlier_sets["B"] == frozenset({E3})
        and earlier_sets["C"] == frozenset({NEG_E1})
        and earlier_sets["D"] == frozenset({E1, NEG_E1})
        and earlier_reverse == "UNDEFINED"
        and earlier_face == "hold"
        and reverse_status == "fail"
        and reverse_status != earlier_reverse
        and lock_sets["A"] != earlier_sets["A"]
        and lock_sets["B"] != earlier_sets["B"]
        and lock_sets["D"] != earlier_sets["D"],
    )
    checks.check(
        "not-leftover-of-later-tick",
        later_sets["A"] == later_mixed_ab
        and later_sets["B"] == later_mixed_ab
        and later_sets["C"] == later_mixed_cd
        and later_sets["D"] == later_mixed_cd
        and later_reverse == "hold"
        and later_face == "hold"
        and reverse_status == "fail"
        and reverse_status != later_reverse
        and lock_sets["A"] != later_sets["A"]
        and lock_sets["B"] != later_sets["B"]
        and lock_sets["C"] != later_sets["C"]
        and lock_sets["D"] == later_sets["D"]
        and later_common == 3
        and later_common != ticks[PROBES["A"]]
        and later_common == ticks[PROBES["D"]],
    )
    checks.check(
        "holding-reverse-needs-later-tick",
        reverse_status == "fail"
        and later_reverse == "hold"
        and face_status == "hold"
        and later_face == "hold"
        and lock_sets["A"] == frozenset({E1})
        and later_sets["A"],
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
            for name in ("A", "B", "D")
            for neighbor, _lock in neighbor_lists[name]
        )
        and any(
            ticks[neighbor] > ticks[PROBES["A"]]
            for neighbor, _lock in later_lists["A"]
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
        "not-leftover-of-unique-own-incoming",
        locks[PROBES["A"]] == {NEG_E1}
        and locks[PROBES["B"]] == {E1}
        and locks[PROBES["C"]] == {E2}
        and locks[PROBES["D"]] == {NEG_E2, NEG_E3, E3}
        and lock_sets["A"] != frozenset({NEG_E1})
        and lock_sets["C"] != frozenset({E2})
        and lock_sets["D"] != frozenset()
        and face_status == "hold"
        and face_status != "UNDEFINED"
        and reverse_status == "fail"
        and reverse_status != "hold",
    )
    checks.check(
        "not-leftover-of-nfexist-nnseed-x-probes",
        TWO_SITE_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and nfexist_sets["A"] == frozenset({E1})
        and nfexist_sets["B"] == frozenset({E1, E3})
        and nfexist_sets["C"] == frozenset({NEG_E2})
        and nfexist_sets["D"] == frozenset({E2})
        and nfexist_reverse == "fail"
        and nfexist_face == "hold"
        and reverse_status == "fail"
        and lock_sets["A"] == nfexist_sets["A"]
        and lock_sets["C"] != nfexist_sets["C"]
        and probe_sites != x_probe_sites,
    )
    checks.check(
        "sign-lettering-loses-axis-and-would-hide-hold",
        named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E3) == "+"
        and face_status == "hold"
        and reverse_status == "fail",
    )
    checks.check(
        "not-probe-own-incoming-lock",
        locks[PROBES["A"]] == {NEG_E1}
        and lock_sets["A"] == frozenset({E1})
        and NEG_E1 not in lock_sets["A"]
        and locks[PROBES["C"]] == {E2}
        and lock_sets["C"] != frozenset({E2}),
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(lock_sets["A"]) == E1
        and sum_of_set(lock_sets["B"]) == add(E1, E3)
        and sum_of_set(lock_sets["C"]) == NEG_E1
        and sum_of_set(lock_sets["D"]) == E2
        and add(sum_of_set(lock_sets["C"]), sum_of_set(lock_sets["D"])) != ZERO
        and face_status == "hold"
        and reverse_status == "fail",
    )
    checks.check(
        "not-unique-vector-leftover",
        lock_sets["A"] == frozenset({E1})
        and len(lock_sets["B"]) > 1
        and len(lock_sets["D"]) > 1
        and reverse_status == "fail"
        and reverse_status != "UNDEFINED"
        and face_status == "hold",
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["D"]]) == 3
        and lock_sets["D"] == mixed_d
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
        "own-tick-not-self-and-same-tick-inclusive",
        all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
        and all(
            ticks[neighbor] <= ticks[PROBES[name]]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        )
        and any(
            ticks[neighbor] == ticks[PROBES["A"]]
            for neighbor, _lock in neighbor_lists["A"]
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
        "mutation-empty-neighbor-locks-undefined",
        recorded_lock_set(()) == frozenset()
        and reverse_report(frozenset(), lock_sets["B"]) == "UNDEFINED"
        and face_report(lock_sets["C"], frozenset()) == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_status == "fail"
        and face_status == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-sets",
        "S(A) = {+e_1}" in note
        and "S(B) = {+e_1, +e_3}" in note
        and "S(C) = {−e_1}" in note
        and "S(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "+e_1 at (1, 0, 1)" in note
        and "−e_1 at (0, 1, 0)" in note
        and "+e_1 at (1, 2, 0)" in note
        and "−e_3 at (1, 0, 0)" in note
        and "+e_3 at (1, 0, 0)" in note
        and "+e_2 at (1, 0, 0)" in note
        and "+e_1 at (1, 1, 1)" in note
        and "+e_1 at (1, 1, -1)" in note,
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
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "incoming step" in normalized_note
        and "S(A)` is `{+e_1}`" in note,
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
        "note-not-leftover-of-strictly-earlier",
        "not leftover of strictly-earlier formation-tick existential opposite"
        in normalized_note
        and "Reverse: fail" in note
        and "reverse `UNDEFINED`" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick",
        "not leftover of later-tick existential opposite"
        in normalized_note
        and "global later T" in normalized_note
        and "Reverse: fail" in note,
    )
    checks.check(
        "note-own-tick-no-global-T",
        "own formation tick" in normalized_note
        and "no global later T" in normalized_note
        and "same-tick-inclusive" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_INCLUSIVE_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
        and "def own_tick_neighbor_locks(" in source
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
        "source-letter-from-existential-opposite-only",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "own_tick_neighbor_locks" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
