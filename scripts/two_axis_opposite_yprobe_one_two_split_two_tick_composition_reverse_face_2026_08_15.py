#!/usr/bin/env python3
"""1-in 2-out split at t versus t+1 reverse/face composition on two-axis opposite.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is four sites: origin locks +e_1, (0,1,0) locks -e_1, (0,0,1) locks +e_2,
and (0,1,1) locks -e_2. Two disjoint opposite pairs. Same process and
y-probes as nm2ax. M, O, and split as nm2ax12. The second pair is a new
seed, not a formed child of the first pair. A 6-NN step is allowed iff it
is perpendicular to the parent lock axis. Newly formed sites lock the
incoming step. Seeds keep their seed letters as a singleton. M(q, tau) is
the set of earliest incoming nearest-neighbor steps at q using only records
with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is the outgoing
dual of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is formed and e
is in M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is empty, not
UNDEFINED. Empty O at t fails split. Axis(S) is the unsigned lattice
directions of signed locks in S. Cover HOLDs at q iff Axis(M) intersect
Axis(O) is empty and Axis(M) union Axis(O) equals {e_1,e_2,e_3}. UNDEFINED
if M or O UNDEFINED. Else fail. Split HOLDs at q iff cover HOLDs and
|Axis(M)|=1 (hence |Axis(O)|=2). 2-in 1-out is fail of this object, not
UNDEFINED. tau0=t, tau1=t+1. Reverse HOLDs iff split at A and at B at that
cut. Face likewise on C, D. Composition HOLD iff split at tau0 equals split
at tau1 at A, B, C, and D. Uniqueness is not required. Occupancy of sites
is not used. Named-sign lettering is not used. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_YPROBE_ONE_TWO_SPLIT_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_YPROBE_ONE_TWO_SPLIT_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
PAIR2: Point = (0, 1, 1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
AXES: tuple[Point, ...] = (E1, E2, E3)
BALL_SQ = 9
TWO_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
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
AXIS_NAME = {
    E1: "e_1",
    E2: "e_2",
    E3: "e_3",
}
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "P_+",
    "S^+",
    "S⁺",
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "1-in 2-out split at t versus t+1 on the four y-probes of the "
    "two-axis opposite seed, reverse/face at each cut, and composition, "
    "are reported. Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


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


def axis_of_letter(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def axis_display(value: AxisSet) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"axis set is not an axis set: {value!r}")
    if not value:
        return "{}"
    names = ", ".join(AXIS_NAME[axis] for axis in AXES if axis in value)
    return "{" + names + "}"


def lockset_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    return set_display(value)


def axis_card(value: AxisSet) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"axis set is not an axis set: {value!r}")
    return str(len(value))


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]], dict[Point, Point]]:
    """Earliest formation ticks and incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Point, set[Point]] = {site: {lock} for site, lock in seeds}
    seed_map: dict[Point, Point] = {site: lock for site, lock in seeds}
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
    return ticks, locks, seed_map


def incoming_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Incoming:
    """Earliest incoming NN steps at site using only records with tick <= tau."""
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    if site in seed_map:
        return frozenset({seed_map[site]})
    arrivals: dict[int, set[Point]] = {}
    for step in NN:
        parent = sub(site, step)
        if parent not in ticks or ticks[parent] > tau:
            continue
        if any(perpendicular(lock, step) for lock in locks[parent]):
            arrivals.setdefault(ticks[parent] + 1, set()).add(step)
    if not arrivals:
        return frozenset()
    earliest = min(arrivals)
    return frozenset(arrivals[earliest])


def outgoing_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Outgoing:
    """Outgoing dual of M. Unformed at tau => UNDEFINED. Empty O is empty."""
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    outgoing: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if not in_ball(neighbor):
            continue
        incoming = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if incoming == UNDEFINED:
            continue
        if not isinstance(incoming, frozenset):
            raise TypeError(f"incoming is not a lock set: {incoming!r}")
        if step in incoming:
            outgoing.add(step)
    return frozenset(outgoing)


def axis_set(value: Incoming) -> AxisSet:
    """Unsigned lattice axes occupied by signed locks. UNDEFINED if unformed."""
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    occupied: set[Point] = set()
    for lock in value:
        axis = axis_of_letter(lock)
        if axis not in AXES:
            raise ValueError(f"lock is not a six-neighbor step: {lock!r}")
        occupied.add(axis)
    return frozenset(occupied)


def leftover_axis(incoming: Incoming, outgoing: Outgoing) -> AxisSet:
    """Leftover-empty contrast: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def leftover_of_one(value: Incoming) -> AxisSet:
    """One-sided leftover contrast: {e_1,e_2,e_3} minus Axis(S). Not this letter."""
    occupied = axis_set(value)
    if occupied == UNDEFINED:
        return UNDEFINED
    if not isinstance(occupied, frozenset):
        raise TypeError("one-sided leftover needs an axis set")
    return frozenset(AXES) - occupied


def leftover_match(left: AxisSet, right: AxisSet) -> str:
    """Leftover-empty fail contrast. Empty leftover => fail, not UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("leftover sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    if left == right:
        return "hold"
    return "fail"


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff axes disjoint and union is {e_1,e_2,e_3}. UNDEFINED if unformed."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    if axes_m & axes_o:
        return "fail"
    if axes_m | axes_o != frozenset(AXES):
        return "fail"
    return "hold"


def axis_split(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff cover HOLD and |Axis(M)|=1 (hence |Axis(O)|=2).

    2-in 1-out (cover HOLD with |Axis(M)|=2) is fail of this object, not
    UNDEFINED. Empty O fails cover and therefore fails split.
    """
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if len(axes_m) != 1:
        return "fail"
    if len(axes_o) != 2:
        return "fail"
    return "hold"


def two_in_one_out(incoming: Incoming, outgoing: Outgoing) -> str:
    """Cover HOLD with |Axis(M)|=2, hence |Axis(O)|=1. Not UNDEFINED."""
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if len(axes_m) == 2 and len(axes_o) == 1:
        return "hold"
    return "fail"


def pair_bit(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(split_a: str, split_b: str) -> str:
    """Reverse HOLDs iff split at A and split at B."""
    return pair_bit(split_a, split_b)


def face_report(split_c: str, split_d: str) -> str:
    """Face HOLDs iff split at C and split at D."""
    return pair_bit(split_c, split_d)


def composition_report(
    split0: dict[str, str],
    split1: dict[str, str],
) -> str:
    """HOLD iff split at t equals split at t+1 at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if split0[name] == UNDEFINED or split1[name] == UNDEFINED:
            return UNDEFINED
        if split0[name] != split1[name]:
            return "fail"
    return "HOLD"


def m_composition_report(
    m0: dict[str, Incoming],
    m1: dict[str, Incoming],
) -> str:
    """Leftover: HOLD iff M(t)=M(t+1) at A,B,C,D. Not this letter."""
    for name in ("A", "B", "C", "D"):
        if m0[name] == UNDEFINED or m1[name] == UNDEFINED:
            return UNDEFINED
        if m0[name] != m1[name]:
            return "fail"
    return "HOLD"


def bit_composition_report(rev0: str, rev1: str, face0: str, face1: str) -> str:
    """Leftover: HOLD iff reverse/face bits match. Not this letter."""
    if rev0 == UNDEFINED or rev1 == UNDEFINED or face0 == UNDEFINED or face1 == UNDEFINED:
        return UNDEFINED
    if rev0 != rev1 or face0 != face1:
        return "fail"
    return "HOLD"


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Signed exist-opposite leftover contrast. Not this reverse."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def new_records_meeting_six_nn(
    site: Point,
    ticks: dict[Point, int],
) -> tuple[Point, ...]:
    """Records in B_3(0) that form at t(site)+1 and are 6-NN of site."""
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + 1:
            found.append(neighbor)
    return tuple(found)


def sum_of_set(locks: frozenset[Point]) -> Point:
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

    print("1-in 2-out axis split of M and O at t versus t+1 reverse/face composition")
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
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites
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
        and add(E3, NEG_E3) == ZERO
        and add(E2, E3) == PAIR2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "axis-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset({NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E1, NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E2, E3, NEG_E3})) == frozenset({E2, E3})
        and axis_set(frozenset({E1, NEG_E1, E3, NEG_E3})) == frozenset({E1, E3}),
    )
    checks.check(
        "cover-identity",
        axis_cover(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_cover(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_cover(frozenset(), frozenset({E2, E3})) == "fail"
        and axis_cover(frozenset({NEG_E1}), frozenset()) == "fail"
        and axis_cover(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and axis_cover(frozenset({E2}), frozenset({E1, NEG_E1, E3, NEG_E3})) == "hold"
        and axis_cover(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "hold"
        and axis_cover(frozenset({E1}), frozenset({E2})) == "fail"
        and axis_cover(frozenset({E1}), frozenset({E1, E2, E3})) == "fail"
        and axis_cover(frozenset({E1}), frozenset({E1})) == "fail",
    )
    checks.check(
        "split-identity",
        axis_split(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_split(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_split(frozenset(), frozenset({E2, E3})) == "fail"
        and axis_split(frozenset({NEG_E1}), frozenset()) == "fail"
        and axis_split(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and axis_split(frozenset({E2}), frozenset({E1, NEG_E1, E3, NEG_E3})) == "hold"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E1}), frozenset({E2})) == "fail"
        and axis_split(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and two_in_one_out(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3})) == "fail"
        and two_in_one_out(UNDEFINED, frozenset({E1})) == UNDEFINED,
    )
    checks.check(
        "pair-bit-identity",
        pair_bit(UNDEFINED, "hold") == UNDEFINED
        and pair_bit("hold", UNDEFINED) == UNDEFINED
        and pair_bit("hold", "hold") == "hold"
        and pair_bit("hold", "fail") == "fail"
        and pair_bit("fail", "hold") == "fail"
        and pair_bit("fail", "fail") == "fail",
    )
    frozen_split = {"A": "fail", "B": "fail", "C": "fail", "D": "fail"}
    changed_split = {"A": "hold", "B": "hold", "C": "hold", "D": "fail"}
    checks.check(
        "composition-identity",
        composition_report(frozen_split, frozen_split) == "HOLD"
        and composition_report(frozen_split, changed_split) == "fail"
        and composition_report(
            {"A": UNDEFINED, "B": "fail", "C": "fail", "D": "fail"},
            frozen_split,
        )
        == UNDEFINED
        and bit_composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and bit_composition_report("fail", "hold", "fail", "fail") == "fail",
    )
    checks.check(
        "leftover-empty-fail-contrast",
        leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(UNDEFINED, frozenset({E1})) == UNDEFINED
        and leftover_axis(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3}))
        == frozenset()
        and leftover_axis(frozenset({NEG_E3}), frozenset({E1, NEG_E1}))
        == frozenset({E2})
        and leftover_axis(frozenset({E2}), frozenset({E1})) == frozenset({E3}),
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    axis_m0: dict[str, AxisSet] = {}
    axis_o0: dict[str, AxisSet] = {}
    axis_m1: dict[str, AxisSet] = {}
    axis_o1: dict[str, AxisSet] = {}
    cover0: dict[str, str] = {}
    cover1: dict[str, str] = {}
    split0: dict[str, str] = {}
    split1: dict[str, str] = {}
    two_one0: dict[str, str] = {}
    two_one1: dict[str, str] = {}
    lx1: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        axis_m0[name] = axis_set(m0[name])
        axis_o0[name] = axis_set(o0[name])
        axis_m1[name] = axis_set(m1[name])
        axis_o1[name] = axis_set(o1[name])
        cover0[name] = axis_cover(m0[name], o0[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        split0[name] = axis_split(m0[name], o0[name])
        split1[name] = axis_split(m1[name], o1[name])
        two_one0[name] = two_in_one_out(m0[name], o0[name])
        two_one1[name] = two_in_one_out(m1[name], o1[name])
        lx1[name] = leftover_axis(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M(t)={lockset_display(m0[name])} "
            f"O(t)={lockset_display(o0[name])} "
            f"split(t)={split0[name]} "
            f"M(t+1)={lockset_display(m1[name])} "
            f"O(t+1)={lockset_display(o1[name])} "
            f"split(t+1)={split1[name]}"
        )

    reverse0 = reverse_report(split0["A"], split0["B"])
    reverse1 = reverse_report(split1["A"], split1["B"])
    face0 = face_report(split0["C"], split0["D"])
    face1 = face_report(split1["C"], split1["D"])
    composition = composition_report(split0, split1)
    m_composition = m_composition_report(m0, m1)
    bit_composition = bit_composition_report(reverse0, reverse1, face0, face1)
    cover_reverse0 = pair_bit(cover0["A"], cover0["B"])
    cover_reverse1 = pair_bit(cover1["A"], cover1["B"])
    cover_face0 = pair_bit(cover0["C"], cover0["D"])
    cover_face1 = pair_bit(cover1["C"], cover1["D"])
    leftover_reverse1 = leftover_match(lx1["A"], lx1["B"])
    leftover_face1 = leftover_match(lx1["C"], lx1["D"])
    m_exist_reverse0 = existential_opposite(m0["A"], m0["B"])
    m_exist_reverse1 = existential_opposite(m1["A"], m1["B"])
    m_exist_face0 = existential_opposite(m0["C"], m0["D"])
    m_exist_face1 = existential_opposite(m1["C"], m1["D"])
    o_exist_reverse0 = existential_opposite(o0["A"], o0["B"])
    o_exist_reverse1 = existential_opposite(o1["A"], o1["B"])
    o_exist_face0 = existential_opposite(o0["C"], o0["D"])
    o_exist_face1 = existential_opposite(o1["C"], o1["D"])
    unique_split_a1 = axis_split(unique_letter(m1["A"]), unique_letter(o1["A"]))
    one_m1 = {
        name: incoming_set(
            PROBES[name],
            one_ticks[PROBES[name]] + 1,
            one_ticks,
            one_locks,
            one_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    one_o1 = {
        name: outgoing_set(
            PROBES[name],
            one_ticks[PROBES[name]] + 1,
            one_ticks,
            one_locks,
            one_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    one_cover = {name: axis_cover(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_split = {name: axis_split(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_cover_face = pair_bit(one_cover["C"], one_cover["D"])
    one_split_face = pair_bit(one_split["C"], one_split["D"])
    print(f"split reverse t={reverse0} t+1={reverse1}")
    print(f"split face t={face0} t+1={face1}")
    print(f"composition={composition}")
    print(f"frozen-M composition leftover={m_composition}")
    print(f"bit-composition leftover={bit_composition}")
    print(
        "per_element: each unsigned lattice axis among {e_1,e_2,e_3} "
        "occupied by M or by O at a probe's t and t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four split reports at two cuts, reverse/face at each cut, and composition"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and axis_split(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and axis_split(
            incoming_set(PROBES["D"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(PAIR2, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and m0["A"] == frozenset({NEG_E1})
        and m1["A"] == frozenset({NEG_E1}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-t-and-t-plus-1",
        m0["A"] == frozenset({NEG_E1})
        and m0["B"] == frozenset({E1})
        and m0["C"] == frozenset({E2})
        and m0["D"] == frozenset({NEG_E3})
        and m1["A"] == frozenset({NEG_E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E3}),
        str(
            {
                name: (lockset_display(m0[name]), lockset_display(m1[name]))
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-O-at-t-and-t-plus-1",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E1})
        and o1["A"] == frozenset({E2, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str(
            {
                name: (lockset_display(o0[name]), lockset_display(o1[name]))
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-split-at-t-and-t-plus-1",
        split0["A"] == "fail"
        and split0["B"] == "fail"
        and split0["C"] == "fail"
        and split0["D"] == "fail"
        and split1["A"] == "hold"
        and split1["B"] == "hold"
        and split1["C"] == "hold"
        and split1["D"] == "fail"
        and cover0["A"] == "fail"
        and cover0["B"] == "fail"
        and cover0["C"] == "fail"
        and cover0["D"] == "fail"
        and cover1["A"] == "hold"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and two_one0["A"] == "fail"
        and two_one1["D"] == "fail"
        and split0["A"] != UNDEFINED
        and split1["D"] != UNDEFINED,
        str(
            {
                name: (split0[name], split1[name])
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-empty-O-at-t-fails-split",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and axis_split(m0["A"], o0["A"]) == "fail"
        and axis_split(frozenset({NEG_E1}), frozenset()) == "fail"
        and o0["A"] != UNDEFINED,
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((0, 2, 0), (0, 1, -1))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1))
        and new_meet["D"] == ((2, 1, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and isinstance(m1["D"], frozenset)
        and len(m1["D"]) == 1
        and split1["D"] == "fail"
        and split1["A"] == "hold"
        and cover1["D"] == "fail",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and m0["A"] == frozenset({NEG_E1})
        and m1["A"] == frozenset({NEG_E1}),
    )
    checks.check(
        "theorem2-reverse-at-t-fail-and-t-plus-1-hold",
        reverse0 == "fail"
        and reverse1 == "hold"
        and split0["A"] == "fail"
        and split0["B"] == "fail"
        and split1["A"] == "hold"
        and split1["B"] == "hold"
        and reverse0 != UNDEFINED
        and reverse1 != "fail",
    )
    checks.check(
        "theorem2-face-at-t-and-t-plus-1-fail",
        face0 == "fail"
        and face1 == "fail"
        and split0["C"] == "fail"
        and split0["D"] == "fail"
        and split1["C"] == "hold"
        and split1["D"] == "fail"
        and face0 != UNDEFINED
        and face1 != "hold",
    )
    checks.check(
        "theorem3-composition-fail",
        composition == "fail"
        and split0["A"] != split1["A"]
        and split0["B"] != split1["B"]
        and split0["C"] != split1["C"]
        and split0["D"] == split1["D"]
        and split0["A"] != UNDEFINED
        and split1["D"] != UNDEFINED,
    )
    checks.check(
        "composition-is-split-equality-not-M-sets",
        composition == "fail"
        and m_composition == "HOLD"
        and m0["A"] == m1["A"]
        and m0["D"] == m1["D"]
        and composition != m_composition
        and composition_report(frozen_split, changed_split) == "fail"
        and m_composition_report(m0, m1) == "HOLD",
    )
    checks.check(
        "composition-is-not-reverse-face-bits",
        composition == "fail"
        and bit_composition == "fail"
        and reverse0 != reverse1
        and face0 == face1
        and bit_composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and bit_composition_report("fail", "hold", "fail", "fail") == "fail",
    )
    checks.check(
        "two-in-one-out-is-fail-not-undefined",
        two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail"
        and two_one1["D"] == "fail"
        and cover1["D"] == "fail"
        and split1["D"] == "fail"
        and split1["D"] != UNDEFINED
        and face1 == "fail"
        and face1 != UNDEFINED,
    )
    checks.check(
        "d-is-one-in-one-out-not-cover",
        cover1["D"] == "fail"
        and two_one1["D"] == "fail"
        and split1["D"] == "fail"
        and axis_card(axis_m1["D"]) == "1"
        and axis_card(axis_o1["D"]) == "1"
        and lx1["D"] == frozenset({E2}),
    )
    checks.check(
        "not-leftover-of-1-axis-cover-face-hold",
        one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["D"]] == 3
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["D"]] == 2
        and one_cover["D"] == "hold"
        and one_cover_face == "hold"
        and one_split["D"] == "fail"
        and one_split_face == "fail"
        and cover1["D"] == "fail"
        and cover_face1 == "fail"
        and face1 == "fail"
        and one_cover_face != cover_face1
        and one_m1["D"] != m1["D"]
        and one_o1["A"] != o1["A"],
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse1 == "fail"
        and leftover_face1 == "fail"
        and lx1["A"] == frozenset()
        and lx1["B"] == frozenset()
        and lx1["C"] == frozenset()
        and lx1["D"] == frozenset({E2})
        and reverse1 == "hold"
        and face1 == "fail"
        and leftover_reverse1 != reverse1,
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse0 == "hold"
        and m_exist_reverse1 == "hold"
        and m_exist_face0 == "fail"
        and m_exist_face1 == "fail"
        and o_exist_reverse0 == UNDEFINED
        and o_exist_face0 == UNDEFINED
        and o_exist_reverse1 == "hold"
        and o_exist_face1 == "hold"
        and reverse0 == "fail"
        and reverse1 == "hold"
        and face0 == "fail"
        and face1 == "fail"
        and m_exist_reverse0 != reverse0
        and o_exist_face1 != face1,
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({NEG_E1})
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["D"]) == frozenset({NEG_E3})
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_split_a1 == UNDEFINED
        and split1["A"] == "hold"
        and split1["D"] == "fail",
    )
    checks.check(
        "mutation-empty-plus-undefined",
        axis_split(frozenset(), frozenset({E2, E3})) == "fail"
        and axis_split(UNDEFINED, frozenset({E1})) == UNDEFINED
        and reverse0 == "fail"
        and reverse1 == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(m1["D"], frozenset)
        and isinstance(o1["A"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E1
        and sum_of_set(m1["D"]) == NEG_E3
        and sum_of_set(o1["A"]) == add(E2, NEG_E3)
        and sum_of_set(o1["D"]) == ZERO
        and axis_m1["D"] == frozenset({E3}),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E1 in m1["A"]
        and NEG_E1 not in o1["A"]
        and o1["A"] != m1["A"]
        and o0["A"] != m0["A"]
        and axis_m1["A"] != axis_o1["A"],
    )
    checks.check(
        "second-pair-is-seed-not-formed-child",
        PAIR2 in seed_map
        and seed_map[PAIR2] == NEG_E2
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {NEG_E2}
        and PAIR2 not in one_seeds
        and one_ticks[PAIR2] == 1
        and one_locks[PAIR2] == {E3}
        and E3 in seed_map
        and seed_map[E3] == E2
        and ticks[E3] == 0
        and one_ticks[E3] == 1
        and PAIR2 not in new_meet["A"],
    )
    x_m1 = {
        name: incoming_set(
            X_PROBES[name],
            ticks[X_PROBES[name]] + 1,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if X_PROBES[name] in ticks
    }
    perp_m1 = {
        name: incoming_set(
            PROBES[name],
            perp_ticks[PROBES[name]] + 1,
            perp_ticks,
            perp_locks,
            perp_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in perp_ticks
    }
    same_m_a = incoming_set(
        PROBES["A"],
        same_ticks[PROBES["A"]] + 1,
        same_ticks,
        same_locks,
        same_seeds,
    )
    zsym_m1 = {
        name: incoming_set(
            PROBES[name],
            zsym_ticks[PROBES[name]] + 1,
            zsym_ticks,
            zsym_locks,
            zsym_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in zsym_ticks
    }
    ysym_ticks_count0 = sum(time == 0 for time in ysym_ticks.values())
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != z_probe_sites
        and x_m1["A"] != m1["A"]
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse1 == "hold",
    )
    checks.check(
        "not-same-lock-two-site-seed",
        TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and same_m_a == frozenset({E1})
        and m1["A"] == frozenset({NEG_E1})
        and same_m_a != m1["A"],
    )
    checks.check(
        "not-one-axis-or-y-symmetric-seed",
        TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and ysym_ticks_count0 == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-split-at-two-cuts",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=2" in note
        and "M(A, τ0) = {−e_1}" in note
        and "M(B, τ0) = {+e_1}" in note
        and "M(C, τ0) = {+e_2}" in note
        and "M(D, τ0) = {−e_3}" in note
        and "M(A, τ1) = {−e_1}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_2}" in note
        and "M(D, τ1) = {−e_3}" in note
        and "O(A, τ0) = {}" in note
        and "O(B, τ0) = {}" in note
        and "O(C, τ0) = {}" in note
        and "O(D, τ0) = {−e_1}" in note
        and "O(A, τ1) = {+e_2, −e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ1) = {+e_1, −e_1}" in note
        and "split(A, τ0) = fail" in note
        and "split(B, τ0) = fail" in note
        and "split(C, τ0) = fail" in note
        and "split(D, τ0) = fail" in note
        and "split(A, τ1) = hold" in note
        and "split(B, τ1) = hold" in note
        and "split(C, τ1) = hold" in note
        and "split(D, τ1) = fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-split-reverse-face",
        "Reverse 1-in 2-out at τ0: fail" in note
        and "Reverse 1-in 2-out at τ1: hold" in note
        and "Face 1-in 2-out at τ0: fail" in note
        and "Face 1-in 2-out at τ1: fail" in note
        and "Reverse fails at τ0." in note
        and "Reverse holds at τ1." in note
        and "Face fails at τ0." in note
        and "Face fails at τ1." in note,
    )
    checks.check(
        "note-reports-composition-fail",
        "Composition of split at t versus t+1: fail" in note
        and "Composition fails." in note
        and "equality of the four split reports" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-exist-opposite",
        "not leftover of nmcover axis-cover" in normalized_note
        and "not leftover of the 1-axis opposite two-site seed" in normalized_note
        and "2-in 1-out is fail of this object, not UNDEFINED" in normalized_note
        and "O is not M" in note
        and "second pair is a new seed, not a formed child" in normalized_note
        and "Empty O at t fails split" in normalized_note,
    )
    checks.check(
        "note-not-one-sided-or-leftover-empty",
        "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "not leftover-empty fail" in normalized_note,
    )
    checks.check(
        "note-not-frozen-M-or-bit-composition",
        "not leftover of frozen-`M` two-tick set equality" in normalized_note
        and "not leftover of reverse/face-bit composition" in normalized_note
        and "not leftover of nm2ax12 `t+1`-only split reverse hold" in normalized_note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not leftover of the two-tick lock-count clock composition"
        in normalized_note
        or "not reprint the two-tick lock-count clock composition" in normalized_note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse 1-in 2-out at τ1: hold" in note
        and "Face 1-in 2-out at τ1: fail" in note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ0(q)=t(q)" in note.replace(" ", "")
        and "τ1(q)=t(q)+1" in note.replace(" ", ""),
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
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/TWO_AXIS_OPPOSITE_YPROBE_ONE_TWO_SPLIT_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "incoming_set" in defined_fns
        and "outgoing_set" in defined_fns
        and "axis_set" in defined_fns
        and "axis_cover" in defined_fns
        and "axis_split" in defined_fns
        and "two_in_one_out" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_report" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    checks.check(
        "split-two-tick-composition-fail",
        reverse0 == "fail"
        and reverse1 == "hold"
        and face0 == "fail"
        and face1 == "fail"
        and composition == "fail"
        and m_composition == "HOLD"
        and cover_reverse0 == "fail"
        and cover_reverse1 == "hold"
        and cover_face0 == "fail"
        and cover_face1 == "fail"
        and leftover_reverse1 == "fail"
        and leftover_face1 == "fail"
        and split0["A"] == "fail"
        and split1["A"] == "hold"
        and split1["D"] == "fail"
        and two_one1["D"] == "fail"
        and o_exist_face1 == "hold"
        and o_exist_reverse0 == UNDEFINED,
    )
    _ = (
        axis_m0,
        axis_o0,
        two_one0,
        unique_split_a1,
        one_cover_face,
        one_split_face,
        tau1,
        cover_reverse0,
        cover_face0,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
