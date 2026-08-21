#!/usr/bin/env python3
"""Formation-tick existential opposite 6-NN reverse/face on four opposite-lock z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's own formation tick t(q), S(q) is the set of locks of
6-NN of q that formed at tick < t(q) (strictly earlier; q excluded). Do not
wait for a global later T. Reverse holds iff some a in S(A) and some b in
S(B) have a+b=(0,0,0). Face holds iff some c in S(C) and some d in S(D) have
c+d=(0,0,0). Empty S on either side is UNDEFINED; nonempty with no opposite
pair fails. Not leftover of later-tick existential opposite on these z-probes
(global T=max t). Not leftover of unique own-incoming letters. Not leftover
of opposite-lock x-probe or y-probe formation-tick lists. Not unique-vector
leftover. Not sum leftover. Not named-sign lettering. Occupancy n is not
used. The probe's own incoming lock is not used. Uniqueness of incoming
locks is not required.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_ZPROBE_FORMATION_TICK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_ZPROBE_FORMATION_TICK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
Y_PROBES = {
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
    "Reverse and face from existential opposite 6-NN locks at "
    "each nsopp z-probe's own formation tick (no global later T) are "
    "reported. Displayed, not adopted."
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
    """Set of formation-tick six-neighbor locks. Duplicates collapse."""
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


def formation_tick_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Locks of 6-NN of site formed at tick < t(site); site excluded."""
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

    print("formation-tick existential opposite 6-NN reverse/face on opposite-lock z-probes")
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites
        and probe_sites != x_probe_sites
        and PROBES["D"] != (0, 1, 1),
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
        and add(E1, E3) != ZERO
        and add(E3, E3) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    form_a = frozenset({E1})
    form_b = frozenset({E3})
    form_c = frozenset({E3})
    form_d = frozenset({E3})
    later_a = frozenset({E1, NEG_E1, E2, NEG_E2, E3})
    later_b = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    later_c = frozenset({E1, NEG_E1, NEG_E2, E3})
    later_d = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    nfexist_a = frozenset({E1})
    nfexist_b = frozenset({E1, E3})
    nfexist_c = frozenset({NEG_E2})
    nfexist_d = frozenset({E2})
    xform_c = frozenset({E2, E3, NEG_E3})
    xform_d = frozenset({E1, NEG_E1})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(form_a, form_b) == "fail"
        and existential_opposite(form_c, form_d) == "fail"
        and existential_opposite(later_a, later_b) == "hold"
        and existential_opposite(later_c, later_d) == "hold"
        and existential_opposite(nfexist_c, nfexist_d) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold",
    )

    ticks, locks = form()
    common_tick = later_tick_T(ticks)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and common_tick is not None,
    )
    assert common_tick is not None

    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    lock_sets: dict[str, frozenset[Point]] = {}
    later_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    later_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        pairs = formation_tick_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        lock_sets[name] = recorded_lock_set(pairs)
        later_pairs = later_tick_neighbor_locks(site, ticks, locks, common_tick)
        later_lists[name] = later_pairs
        later_sets[name] = recorded_lock_set(later_pairs)
        incoming = ",".join(LOCK_NAME[lock] for lock in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} S={set_display(lock_sets[name])} "
            f"incoming={incoming}"
        )

    print(
        "no global T; "
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]}"
    )
    reverse_status = reverse_report(lock_sets["A"], lock_sets["B"])
    face_status = face_report(lock_sets["C"], lock_sets["D"])
    later_reverse = reverse_report(later_sets["A"], later_sets["B"])
    later_face = face_report(later_sets["C"], later_sets["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: lock vector in a formation-tick already-recorded six-neighbor set"
    )
    print(
        "per_site: scored only at probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four lock sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    nfexist_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = X_PROBES[name]
        pairs = formation_tick_neighbor_locks(site, perp_ticks, perp_locks)
        nfexist_sets[name] = recorded_lock_set(pairs)
    nfexist_reverse = reverse_report(nfexist_sets["A"], nfexist_sets["B"])
    nfexist_face = face_report(nfexist_sets["C"], nfexist_sets["D"])

    xform_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = X_PROBES[name]
        pairs = formation_tick_neighbor_locks(site, ticks, locks)
        xform_sets[name] = recorded_lock_set(pairs)
    xform_reverse = reverse_report(xform_sets["A"], xform_sets["B"])
    xform_face = face_report(xform_sets["C"], xform_sets["D"])

    yform_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = Y_PROBES[name]
        pairs = formation_tick_neighbor_locks(site, ticks, locks)
        yform_sets[name] = recorded_lock_set(pairs)
    yform_reverse = reverse_report(yform_sets["A"], yform_sets["B"])
    yform_face = face_report(yform_sets["C"], yform_sets["D"])

    checks.check(
        "theorem1-formation-ticks-not-global-T",
        ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
        and ticks[PROBES["A"]] != ticks[PROBES["B"]]
        and ticks[PROBES["B"]] != ticks[PROBES["C"]]
        and common_tick == 4
        and common_tick != ticks[PROBES["A"]]
        and common_tick != ticks[PROBES["B"]]
        and common_tick != ticks[PROBES["D"]],
        str(
            (
                ticks[PROBES["A"]],
                ticks[PROBES["B"]],
                ticks[PROBES["C"]],
                ticks[PROBES["D"]],
            )
        ),
    )
    checks.check(
        "theorem1-A-neighbor-lock-set",
        neighbor_lists["A"] == ((ORIGIN, E1),)
        and lock_sets["A"] == form_a
        and ticks[PROBES["A"]] == 1,
        str((neighbor_lists["A"], lock_sets["A"])),
    )
    checks.check(
        "theorem1-B-neighbor-lock-set",
        neighbor_lists["B"] == (((0, 1, 1), E3),)
        and lock_sets["B"] == form_b
        and ticks[PROBES["B"]] == 2,
        str((neighbor_lists["B"], lock_sets["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-set",
        neighbor_lists["C"]
        == (
            ((1, 0, 2), E3),
            ((-1, 0, 2), E3),
            ((0, -1, 2), E3),
            (PROBES["A"], E3),
        )
        and lock_sets["C"] == form_c
        and ticks[PROBES["C"]] == 4,
        str((neighbor_lists["C"], lock_sets["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-set",
        neighbor_lists["D"] == ((PROBES["A"], E3),)
        and lock_sets["D"] == form_d
        and ticks[PROBES["D"]] == 2,
        str((neighbor_lists["D"], lock_sets["D"])),
    )
    checks.check(
        "theorem1-sets-are-singletons-uniqueness-not-required",
        lock_sets["A"] == form_a
        and lock_sets["B"] == form_b
        and lock_sets["C"] == form_c
        and lock_sets["D"] == form_d
        and len(lock_sets["A"]) == 1
        and len(lock_sets["C"]) == 1
        and len(neighbor_lists["C"]) == 4,
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and lock_sets["A"] == form_a
        and lock_sets["B"] == form_b
        and add(E1, E3) != ZERO
        and reverse_status != "hold"
        and reverse_status != "UNDEFINED"
        and lock_sets["A"]
        and lock_sets["B"],
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and lock_sets["C"] == form_c
        and lock_sets["D"] == form_d
        and add(E3, E3) != ZERO
        and face_status != "hold"
        and face_status != "UNDEFINED"
        and lock_sets["C"]
        and lock_sets["D"],
        face_status,
    )
    checks.check(
        "holding-needs-the-later-tick",
        later_sets["A"] == later_a
        and later_sets["B"] == later_b
        and later_sets["C"] == later_c
        and later_sets["D"] == later_d
        and later_sets["A"] != lock_sets["A"]
        and later_sets["B"] != lock_sets["B"]
        and later_sets["C"] != lock_sets["C"]
        and later_sets["D"] != lock_sets["D"]
        and later_reverse == "hold"
        and later_face == "hold"
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "not-leftover-of-nsopzex-later-tick-lists",
        later_reverse == "hold"
        and later_face == "hold"
        and reverse_status != later_reverse
        and face_status != later_face
        and NEG_E1 not in lock_sets["A"]
        and NEG_E1 in later_sets["A"]
        and E1 not in lock_sets["D"]
        and E1 in later_sets["D"]
        and common_tick == 4,
    )
    checks.check(
        "not-leftover-of-nfexist-nnseed-x-probes",
        TWO_SITE_SEEDS != PERP_SEEDS
        and nfexist_sets["A"] == nfexist_a
        and nfexist_sets["B"] == nfexist_b
        and nfexist_sets["C"] == nfexist_c
        and nfexist_sets["D"] == nfexist_d
        and nfexist_reverse == "fail"
        and nfexist_face == "hold"
        and reverse_status == "fail"
        and face_status == "fail"
        and face_status != nfexist_face
        and lock_sets["B"] != nfexist_sets["B"]
        and lock_sets["C"] != nfexist_sets["C"]
        and lock_sets["D"] != nfexist_sets["D"],
    )
    checks.check(
        "not-leftover-of-nsopexft-x-probe-formation-tick",
        xform_sets["A"] == form_a
        and xform_sets["B"] == form_b
        and xform_sets["C"] == xform_c
        and xform_sets["D"] == xform_d
        and xform_reverse == "fail"
        and xform_face == "fail"
        and lock_sets["C"] != xform_sets["C"]
        and lock_sets["D"] != xform_sets["D"]
        and probe_sites != x_probe_sites
        and len(xform_sets["C"]) == 3
        and len(lock_sets["C"]) == 1,
    )
    checks.check(
        "not-leftover-of-nsopyft-y-probe-formation-tick",
        yform_sets["A"] == frozenset()
        and yform_sets["B"] == frozenset({E3})
        and yform_sets["C"] == frozenset({NEG_E1})
        and yform_sets["D"] == frozenset({E1, NEG_E1})
        and yform_reverse == "UNDEFINED"
        and yform_face == "hold"
        and reverse_status != yform_reverse
        and face_status != yform_face
        and probe_sites != y_probe_sites
        and ticks[PROBES["A"]] != 0,
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        locks[PROBES["A"]] == {E3}
        and locks[PROBES["B"]] == {E1}
        and locks[PROBES["C"]] == {E1, NEG_E1, E2}
        and locks[PROBES["D"]] == {E1}
        and lock_sets["A"] != frozenset({E3})
        and lock_sets["C"] != frozenset({E1, NEG_E1, E2})
        and reverse_status == "fail"
        and reverse_status != "UNDEFINED"
        and face_status == "fail"
        and face_status != "UNDEFINED",
    )
    checks.check(
        "formation-tick-excludes-same-tick-and-later",
        all(
            ticks[neighbor] < ticks[PROBES[name]]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        )
        and PROBES["D"] not in {neighbor for neighbor, _lock in neighbor_lists["A"]}
        and PROBES["C"] not in {neighbor for neighbor, _lock in neighbor_lists["A"]}
        and PROBES["B"] not in {neighbor for neighbor, _lock in neighbor_lists["D"]}
        and PROBES["A"] in {neighbor for neighbor, _lock in neighbor_lists["D"]},
    )
    checks.check(
        "sign-lettering-loses-axis",
        named_sign(E1) == named_sign(E3) == "+"
        and reverse_status == "fail"
        and named_sign(E3) == "+"
        and add(E1, E3) != ZERO,
    )
    checks.check(
        "not-probe-own-incoming-lock",
        locks[PROBES["A"]] == {E3}
        and lock_sets["A"] == form_a
        and E3 in locks[PROBES["A"]]
        and E3 not in lock_sets["A"]
        and E1 in lock_sets["A"]
        and E1 not in locks[PROBES["A"]]
        and locks[PROBES["D"]] == {E1}
        and lock_sets["D"] != frozenset({E1})
        and locks[PROBES["C"]] == {E1, NEG_E1, E2}
        and lock_sets["C"] != locks[PROBES["C"]],
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(lock_sets["A"]) == E1
        and sum_of_set(lock_sets["B"]) == E3
        and sum_of_set(lock_sets["C"]) == E3
        and sum_of_set(lock_sets["D"]) == E3
        and add(sum_of_set(lock_sets["A"]), sum_of_set(lock_sets["B"])) != ZERO
        and add(sum_of_set(lock_sets["C"]), sum_of_set(lock_sets["D"])) != ZERO
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "not-unique-vector-leftover",
        len(lock_sets["A"]) == 1
        and len(lock_sets["B"]) == 1
        and len(lock_sets["C"]) == 1
        and len(lock_sets["D"]) == 1
        and reverse_status == "fail"
        and face_status == "fail"
        and later_sets["A"]
        and len(later_sets["A"]) > 1
        and len(later_sets["C"]) > 1,
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["C"]]) == 3
        and lock_sets["C"] == form_c
        and reverse_status == "fail"
        and face_status == "fail",
        str(sorted(locks[PROBES["C"]])),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS
        and PROBES["A"] != E2
        and ticks[PROBES["A"]] != 0,
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
        and ticks[(0, 2, 0)] == 1
        and ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
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
        reverse_report(frozenset({E1}), frozenset({E3})) == "fail"
        and face_report(frozenset({E3}), frozenset({E3})) == "fail"
        and reverse_status == "fail"
        and face_status == "fail",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-sets",
        "S(A) = {+e_1}" in note
        and "S(B) = {+e_3}" in note
        and "S(C) = {+e_3}" in note
        and "S(D) = {+e_3}" in note
        and "t(A)=1" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "+e_3 at (1, 0, 2)" in note
        and "+e_3 at (-1, 0, 2)" in note
        and "+e_3 at (0, -1, 2)" in note
        and "+e_3 at (0, 0, 1)" in note,
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
        and "`+e_1` is in `S(A)` and is not incoming at `A`" in note,
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
        and "Reverse fails." in note,
    )
    checks.check(
        "note-not-leftover-of-own-incoming",
        "not leftover of unique own-incoming lock-vector letters"
        in normalized_note
        and "face `UNDEFINED`" in note
        and "Face: fail" in note,
    )
    checks.check(
        "note-not-leftover-of-later-tick",
        "not leftover of later-tick existential opposite" in normalized_note
        and "holding needs the later tick" in normalized_note
        and "global `T=4`" in note,
    )
    checks.check(
        "note-not-leftover-of-nfexist",
        "not leftover of formation-time existential opposite on the nnseed"
        in normalized_note
        and "perp two-site seed" in normalized_note
        and "face hold" in normalized_note,
    )
    checks.check(
        "note-not-leftover-of-x-or-y-formation-tick",
        "not leftover of formation-tick existential opposite on the opposite-lock x-probes"
        in normalized_note
        and "not leftover of formation-tick existential opposite on the opposite-lock y-probes"
        in normalized_note,
    )
    checks.check(
        "note-no-global-later-T",
        "no global later tick" in normalized_note.lower()
        or "There is no global later tick" in note,
    )
    checks.check(
        "note-no-global-later-T-strict",
        "There is no global later tick." in note
        and "strictly earlier" in normalized_note
        and "own formation tick" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_ZPROBE_FORMATION_TICK_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
        and "def formation_tick_neighbor_locks(" in source
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
        "source-letter-from-existential-opposite-only",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "formation_tick_neighbor_locks" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
