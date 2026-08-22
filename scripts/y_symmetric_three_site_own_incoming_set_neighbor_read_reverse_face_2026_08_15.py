#!/usr/bin/env python3
"""Neighbor-read of own incoming reverse/face on four #7211 y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process and y-probes as nmsyop #7211). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q) is the set of
earliest incoming NN steps at q. Mixed stays a set. Unformed is UNDEFINED.
For formed q, Nbr(q) is the set of 6-NN of q that are formed in B_3(0) and
are not q. R(q) is the neighbor-read of own incoming:

    R(q) = { e in {±e_1,±e_2,±e_3} | q+e in Nbr(q) and (-e) in M(q+e) }.

Unformed q is UNDEFINED. Empty R is empty, not UNDEFINED. R is not M and is
not O. Unique L is not the object. Read-HOLD at q iff R(q)=M(q) as sets
(both defined, possibly mixed). Read-fail if both defined and unequal.
UNDEFINED if either is UNDEFINED. Reverse holds iff some a in R(A) and some
b in R(B) have a+b=(0,0,0). Face holds iff some c in R(C) and some d in
R(D) have c+d=(0,0,0). Empty or UNDEFINED on either side is UNDEFINED;
nonempty with no opposite pair fails. This is not leftover of #7211 M bits:
the letter is neighbor-read, not own incoming. This is not leftover of
#7208 neighbor-read: R(D) is empty here while #7208 has R(D)={-e_2}.
Occupancy n is not used. Named-sign lettering is not used. No unique P_+.
Uniqueness of neighbor-read locks is not required. No larger ball. No
sister kernel. No Cl. No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_NEIGHBOR_READ_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_NEIGHBOR_READ_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Incoming = frozenset[Point] | str
NeighborRead = frozenset[Point] | str
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
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E1, E2),
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
    "CHSH",
    "W9",
    "mu*",
    "Dirac-Kähler",
    "Cl(3,0)",
)
CLAIM_SCOPE = (
    "Neighbor-read R of own incoming on the four #7211 y-probes, "
    "equality to M, and reverse/face from R are reported. "
    "Displayed, not adopted."
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def neg(step: Point) -> Point:
    return (-step[0], -step[1], -step[2])


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


def own_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Incoming:
    """Outgoing dual of M. Leftover comparator only. Empty O is empty, not UNDEFINED."""
    if site not in ticks:
        return "UNDEFINED"
    outgoing: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        if step in locks[neighbor]:
            outgoing.add(step)
    return frozenset(outgoing)


def formed_neighbors(
    site: Point,
    ticks: dict[Point, int],
) -> frozenset[Point] | str:
    """6-NN of site that are formed in B_3(0) and are not site. Unformed is UNDEFINED."""
    if site not in ticks:
        return "UNDEFINED"
    neighbors: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if not in_ball(neighbor):
            continue
        neighbors.add(neighbor)
    return frozenset(neighbors)


def neighbor_read_own_incoming(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> NeighborRead:
    """Neighbor-read R of own incoming. Unformed is UNDEFINED. Empty R is empty."""
    if site not in ticks:
        return "UNDEFINED"
    neighbors = formed_neighbors(site, ticks)
    if neighbors == "UNDEFINED":
        return "UNDEFINED"
    assert isinstance(neighbors, frozenset)
    result: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in neighbors:
            continue
        if neg(step) in locks[neighbor]:
            result.add(step)
    return frozenset(result)


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point] | Incoming) -> Letter:
    """Unique-L leftover: UNDEFINED when mixed or empty. Not this letter."""
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
    """Reverse iff some a in R(A) and some b in R(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in R(C) and some d in R(D) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def read_report(neighbor_read: NeighborRead, incoming: Incoming) -> str:
    """Read-HOLD iff R=M as sets. Read-fail if both defined and unequal."""
    if neighbor_read == "UNDEFINED" or incoming == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(neighbor_read, frozenset) or not isinstance(incoming, frozenset):
        return "UNDEFINED"
    if neighbor_read == incoming:
        return "hold"
    return "fail"


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
    seeds: tuple[tuple[Point, Point], ...] = Y_SYMMETRIC_SEEDS,
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
    """Leftover S^+ neighbor list: 6-NN locks formed at tick <= t(site)."""
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

    print("neighbor-read of own incoming reverse/face on #7211 y-probes")
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and neg(E1) == NEG_E1
        and neg(NEG_E3) == E3
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a = frozenset({E1, NEG_E1})
    plus_b = frozenset({E1, E3})
    plus_c = frozenset({NEG_E1, E2})
    plus_d = frozenset({E1, NEG_E1, E3, NEG_E3})
    twosite_plus_d = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    set_a = frozenset({NEG_E1})
    set_b = frozenset({E1})
    set_c = frozenset({E2})
    set_d = frozenset({NEG_E2, E3, NEG_E3})
    out_a = frozenset({E2, E3, NEG_E3})
    out_b = frozenset({E2, E3, NEG_E3})
    out_c = frozenset({E1, NEG_E1, E3, NEG_E3})
    out_d = frozenset({E1, NEG_E1})
    read_a = frozenset()
    read_b = frozenset({NEG_E3})
    read_c = frozenset()
    read_d = frozenset()
    twosite_read_d = frozenset({NEG_E2})
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
        and existential_opposite(out_a, out_b) == "hold"
        and existential_opposite(read_a, read_b) == "UNDEFINED"
        and existential_opposite(read_c, read_d) == "UNDEFINED"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "neighbor-read-identity",
        unique_own_incoming_letter(frozenset({NEG_E1})) == NEG_E1
        and unique_own_incoming_letter(frozenset()) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E2, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E3})) == NEG_E3
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED"
        and unique_own_incoming_letter("UNDEFINED") == "UNDEFINED"
        and read_report("UNDEFINED", set_a) == "UNDEFINED"
        and read_report(read_a, "UNDEFINED") == "UNDEFINED"
        and read_report(read_a, set_a) == "fail"
        and read_report(set_a, set_a) == "hold"
        and read_report(read_d, set_d) == "fail",
    )

    ticks, locks = form()
    perp_ticks, perp_locks = form(PERP_SEEDS)
    zsym_ticks, zsym_locks = form(Z_SYMMETRIC_SEEDS)
    twosite_ticks, twosite_locks = form(TWO_SITE_SEEDS)
    nstri_ticks, nstri_locks = form(NSTRI_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D")),
    )

    incoming_sets: dict[str, Incoming] = {}
    outgoing_sets: dict[str, Incoming] = {}
    neighbor_reads: dict[str, NeighborRead] = {}
    neighbor_sets: dict[str, frozenset[Point] | str] = {}
    letters: dict[str, Letter] = {}
    read_letters: dict[str, Letter] = {}
    plus_sets: dict[str, Incoming] = {}
    read_status: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        incoming_sets[name] = own_incoming_set(site, ticks, locks)
        outgoing_sets[name] = own_outgoing_set(site, ticks, locks)
        neighbor_reads[name] = neighbor_read_own_incoming(site, ticks, locks)
        neighbor_sets[name] = formed_neighbors(site, ticks)
        letters[name] = unique_own_incoming_letter(incoming_sets[name])
        read_letters[name] = unique_own_incoming_letter(neighbor_reads[name])
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        plus_sets[name] = own_lock_in_set(recorded_lock_set(pairs), letters[name])
        read_status[name] = read_report(neighbor_reads[name], incoming_sets[name])
        print(
            f"{name} t={ticks[site]} M={set_display(incoming_sets[name])} "
            f"R={set_display(neighbor_reads[name])} "
            f"O={set_display(outgoing_sets[name])} "
            f"read={read_status[name]} "
            f"L={letter_display(letters[name])} "
            f"S+={set_display(plus_sets[name])}"
        )

    reverse_status = reverse_report(neighbor_reads["A"], neighbor_reads["B"])
    face_status = face_report(neighbor_reads["C"], neighbor_reads["D"])
    reverse_m = reverse_report(incoming_sets["A"], incoming_sets["B"])
    face_m = face_report(incoming_sets["C"], incoming_sets["D"])
    reverse_o = reverse_report(outgoing_sets["A"], outgoing_sets["B"])
    face_o = face_report(outgoing_sets["C"], outgoing_sets["D"])
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
    unique_read_reverse = reverse_report(
        own_lock_in_set(frozenset(), read_letters["A"]),
        own_lock_in_set(frozenset(), read_letters["B"]),
    )
    unique_read_face = face_report(
        own_lock_in_set(frozenset(), read_letters["C"]),
        own_lock_in_set(frozenset(), read_letters["D"]),
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"M_reverse={reverse_m} M_face={face_m} "
        f"O_reverse={reverse_o} O_face={face_o} "
        f"S+_reverse={plus_reverse} S+_face={plus_face}"
    )
    print(f"unique_L_reverse={unique_reverse} unique_L_face={unique_face}")
    print(
        f"unique_R_reverse={unique_read_reverse} unique_R_face={unique_read_face}"
    )
    print(
        "per_element: each lock vector in the neighbor-read R(q) of own incoming"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four neighbor-reads plus equality to M and reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    perp_reads: dict[str, NeighborRead] = {}
    for name in ("A", "B", "C", "D"):
        perp_reads[name] = neighbor_read_own_incoming(PROBES[name], perp_ticks, perp_locks)
    perp_reverse = reverse_report(perp_reads["A"], perp_reads["B"])
    perp_face = face_report(perp_reads["C"], perp_reads["D"])

    zsym_reads: dict[str, NeighborRead] = {}
    for name in ("A", "B", "C", "D"):
        zsym_reads[name] = neighbor_read_own_incoming(PROBES[name], zsym_ticks, zsym_locks)
    zsym_reverse = reverse_report(zsym_reads["A"], zsym_reads["B"])
    zsym_face = face_report(zsym_reads["C"], zsym_reads["D"])

    twosite_reads: dict[str, NeighborRead] = {}
    twosite_incoming: dict[str, Incoming] = {}
    twosite_plus: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        twosite_reads[name] = neighbor_read_own_incoming(site, twosite_ticks, twosite_locks)
        twosite_incoming[name] = own_incoming_set(site, twosite_ticks, twosite_locks)
        twosite_letter = unique_own_incoming_letter(twosite_incoming[name])
        twosite_pairs = own_tick_neighbor_locks(site, twosite_ticks, twosite_locks)
        twosite_plus[name] = own_lock_in_set(recorded_lock_set(twosite_pairs), twosite_letter)
    twosite_reverse = reverse_report(twosite_reads["A"], twosite_reads["B"])
    twosite_face = face_report(twosite_reads["C"], twosite_reads["D"])

    nstri_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        nstri_incoming[name] = own_incoming_set(PROBES[name], nstri_ticks, nstri_locks)

    x_reads: dict[str, NeighborRead] = {}
    x_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        x_reads[name] = neighbor_read_own_incoming(X_PROBES[name], ticks, locks)
        x_incoming[name] = own_incoming_set(X_PROBES[name], ticks, locks)
    x_reverse = reverse_report(x_reads["A"], x_reads["B"])
    x_face = face_report(x_reads["C"], x_reads["D"])

    unformed = (0, 3, 0)
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-incoming-sets-of-7211",
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
        "theorem1-neighbor-reads",
        neighbor_reads["A"] == read_a
        and neighbor_reads["B"] == read_b
        and neighbor_reads["C"] == read_c
        and neighbor_reads["D"] == read_d
        and neighbor_reads["A"] != "UNDEFINED"
        and neighbor_reads["C"] != "UNDEFINED"
        and neighbor_reads["D"] != "UNDEFINED"
        and isinstance(neighbor_reads["A"], frozenset)
        and len(neighbor_reads["A"]) == 0
        and len(neighbor_reads["B"]) == 1
        and len(neighbor_reads["C"]) == 0
        and len(neighbor_reads["D"]) == 0,
        str({name: set_display(neighbor_reads[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-equality-R-to-M-is-read-fail",
        read_status["A"] == "fail"
        and read_status["B"] == "fail"
        and read_status["C"] == "fail"
        and read_status["D"] == "fail"
        and neighbor_reads["A"] != incoming_sets["A"]
        and neighbor_reads["B"] != incoming_sets["B"]
        and neighbor_reads["C"] != incoming_sets["C"]
        and neighbor_reads["D"] != incoming_sets["D"]
        and all(status != "UNDEFINED" for status in read_status.values())
        and all(status != "hold" for status in read_status.values()),
        str(read_status),
    )
    checks.check(
        "theorem1-R-is-not-M-and-not-O",
        neighbor_reads["A"] != incoming_sets["A"]
        and neighbor_reads["B"] != incoming_sets["B"]
        and neighbor_reads["C"] != incoming_sets["C"]
        and neighbor_reads["D"] != incoming_sets["D"]
        and neighbor_reads["A"] != outgoing_sets["A"]
        and neighbor_reads["B"] != outgoing_sets["B"]
        and neighbor_reads["C"] != outgoing_sets["C"]
        and neighbor_reads["D"] != outgoing_sets["D"]
        and outgoing_sets["A"] == out_a
        and outgoing_sets["B"] == out_b
        and outgoing_sets["C"] == out_c
        and outgoing_sets["D"] == out_d
        and NEG_E1 in incoming_sets["A"]
        and NEG_E1 not in neighbor_reads["A"],
        str(
            (
                set_display(neighbor_reads["A"]),
                set_display(incoming_sets["A"]),
                set_display(outgoing_sets["A"]),
            )
        ),
    )
    checks.check(
        "theorem1-star-excluding-A-does-not-recover-M-A",
        PROBES["A"] not in neighbor_sets["A"]
        and isinstance(neighbor_sets["A"], frozenset)
        and len(neighbor_sets["A"]) == 6
        and neighbor_reads["A"] != incoming_sets["A"]
        and incoming_sets["A"] == set_a
        and NEG_E1 not in neighbor_reads["A"]
        and unique_own_incoming_letter(neighbor_reads["A"]) == "UNDEFINED",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and incoming_sets["A"] == frozenset({NEG_E1})
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(incoming_sets["D"]) == 3
        and letters["D"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED"
        and neighbor_reads["D"] != "UNDEFINED"
        and unique_own_incoming_letter(incoming_sets["D"]) == "UNDEFINED"
        and NEG_E2 in incoming_sets["D"]
        and NEG_E2 not in neighbor_reads["D"]
        and neighbor_reads["D"] != incoming_sets["D"],
    )
    checks.check(
        "theorem1-empty-R-is-empty",
        neighbor_reads["A"] == frozenset()
        and neighbor_reads["C"] == frozenset()
        and neighbor_reads["D"] == frozenset()
        and neighbor_reads["A"] != "UNDEFINED"
        and neighbor_reads["D"] != "UNDEFINED"
        and neighbor_read_own_incoming(unformed, ticks, locks) == "UNDEFINED"
        and unformed not in ticks,
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and neighbor_reads["A"] == read_a
        and neighbor_reads["B"] == read_b
        and reverse_status != "hold"
        and reverse_status != "fail"
        and reverse_m == "hold",
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and neighbor_reads["C"] == read_c
        and neighbor_reads["D"] == read_d
        and face_status != "hold"
        and face_status != "fail"
        and face_m == "hold",
        face_status,
    )
    checks.check(
        "discriminator-undefined-from-R-not-M-or-O-or-S-plus",
        reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and reverse_m == "hold"
        and face_m == "hold"
        and reverse_o == "hold"
        and face_o == "hold"
        and plus_reverse == "hold"
        and plus_face == "hold"
        and neighbor_reads["A"] != incoming_sets["A"]
        and neighbor_reads["A"] != outgoing_sets["A"]
        and neighbor_reads["A"] != plus_sets["A"]
        and letters["A"] == NEG_E1,
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "hold"
        and unique_face == "UNDEFINED"
        and unique_read_reverse == "UNDEFINED"
        and unique_read_face == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and reverse_status != unique_reverse
        and letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and letters["D"] == "UNDEFINED"
        and read_letters["A"] == "UNDEFINED"
        and read_letters["B"] == NEG_E3
        and read_letters["C"] == "UNDEFINED"
        and read_letters["D"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-M-or-O-or-S-plus-7211",
        incoming_sets["A"] == set_a
        and outgoing_sets["A"] == out_a
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and reverse_m == "hold"
        and face_m == "hold"
        and reverse_o == "hold"
        and plus_reverse == "hold"
        and neighbor_reads["A"] != incoming_sets["A"]
        and neighbor_reads["B"] != incoming_sets["B"]
        and neighbor_reads["C"] != incoming_sets["C"]
        and neighbor_reads["D"] != incoming_sets["D"]
        and neighbor_reads["A"] != outgoing_sets["A"]
        and neighbor_reads["A"] != plus_sets["A"]
        and NEG_E1 not in neighbor_reads["A"]
        and NEG_E1 in incoming_sets["A"]
        and E1 in plus_sets["A"],
    )
    checks.check(
        "not-leftover-of-7208-neighbor-read",
        twosite_reads["A"] == read_a
        and twosite_reads["B"] == read_b
        and twosite_reads["C"] == read_c
        and twosite_reads["D"] == twosite_read_d
        and neighbor_reads["D"] != twosite_reads["D"]
        and neighbor_reads["D"] == read_d
        and NEG_E2 in twosite_reads["D"]
        and NEG_E2 not in neighbor_reads["D"]
        and twosite_reverse == "UNDEFINED"
        and twosite_face == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and twosite_plus["D"] == twosite_plus_d
        and E2 in twosite_plus["D"]
        and E2 not in plus_sets["D"],
    )
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and x_incoming["A"] != incoming_sets["A"]
        and zsym_reads["B"] != neighbor_reads["B"]
        and perp_reads["C"] != neighbor_reads["C"]
        and zsym_reads["C"] != neighbor_reads["C"]
        and x_reverse == "fail"
        and x_face == "UNDEFINED"
        and zsym_reverse == "UNDEFINED"
        and zsym_face == "fail"
        and perp_reverse == "UNDEFINED"
        and perp_face == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "not-two-site-or-nstri-third-site",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and ticks[NEG_E2] == 0
        and twosite_ticks[NEG_E2] == 1
        and twosite_incoming["A"] == incoming_sets["A"]
        and twosite_incoming["D"] == incoming_sets["D"]
        and nstri_incoming["B"] != incoming_sets["B"]
        and nstri_incoming["D"] != incoming_sets["D"]
        and E2 in nstri_incoming["B"]
        and NEG_E1 in nstri_incoming["D"],
    )
    checks.check(
        "not-nnlock-named-sign",
        incoming_sets["A"] == frozenset({NEG_E1})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(NEG_E3) == "-"
        and neighbor_reads["B"] != named_sign(NEG_E3)
        and incoming_sets["A"] != named_sign(NEG_E1),
    )
    checks.check(
        "neighbor-read-locks-are-nn-steps",
        all(
            neighbor_reads[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        len(neighbor_reads["A"]) == 0
        and len(neighbor_reads["B"]) == 1
        and len(neighbor_reads["C"]) == 0
        and len(neighbor_reads["D"]) == 0
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and read_status["A"] == "fail"
        and read_status["D"] == "fail",
    )
    checks.check(
        "y-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[NEG_E2] == 0
        and locks[NEG_E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
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
    y_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and y_mirror_parallel_blocked
        and ticks[NEG_E2] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), neighbor_reads["B"]) == "UNDEFINED"
        and face_report(neighbor_reads["C"], frozenset()) == "UNDEFINED"
        and reverse_report("UNDEFINED", neighbor_reads["B"]) == "UNDEFINED"
        and face_report(neighbor_reads["C"], "UNDEFINED") == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "mutation-unique-L-of-R-would-be-undefined",
        unique_read_reverse == "UNDEFINED"
        and unique_read_face == "UNDEFINED"
        and unique_face == "UNDEFINED"
        and unique_reverse == "hold"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )
    checks.check(
        "mutation-M-and-O-hold-while-R-is-undefined",
        reverse_m == "hold"
        and face_m == "hold"
        and reverse_o == "hold"
        and face_o == "hold"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and incoming_sets["A"] != neighbor_reads["A"]
        and outgoing_sets["A"] != neighbor_reads["A"],
    )
    checks.check(
        "mutation-sum-of-R-is-not-the-letter",
        sum_of_set(neighbor_reads["A"]) == ZERO
        and sum_of_set(neighbor_reads["B"]) == NEG_E3
        and sum_of_set(neighbor_reads["C"]) == ZERO
        and sum_of_set(neighbor_reads["D"]) == ZERO
        and neighbor_reads["A"] != frozenset({ZERO})
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-neighbor-reads",
        "R(A) = {}" in note
        and "R(B) = {−e_3}" in note
        and "R(C) = {}" in note
        and "R(D) = {}" in note
        and "M(A) = {−e_1}" in note
        and "M(B) = {+e_1}" in note
        and "M(C) = {+e_2}" in note
        and "M(D) = {−e_2, +e_3, −e_3}" in note
        and "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note,
    )
    checks.check(
        "note-reports-equality-read-fail",
        "Read-fail" in note
        and "R is not M" in note
        and "R is not O" in note
        and "does not uniquely recover M(A)" in note,
    )
    checks.check(
        "note-reports-undefined-undefined",
        "Reverse: UNDEFINED" in note
        and "Face: UNDEFINED" in note
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
        and "neighbor-read" in normalized_note
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
        and "not leftover of #7211" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "Face is UNDEFINED." in note
        and "Reverse is UNDEFINED." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "R is not M" in note
        and "neighbor-read" in normalized_note,
    )
    checks.check(
        "note-not-sister-kernel-or-outgoing-or-7208",
        "not the sister kernel" in normalized_note
        and "R is not O" in note
        and "not leftover of #7208" in normalized_note
        and "Uniqueness is not required." in note,
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
        '    "docs/Y_SYMMETRIC_THREE_SITE_OWN_INCOMING_SET_NEIGHBOR_READ_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def neighbor_read_own_incoming(" in source
        and "def formed_neighbors(" in source
        and "def read_report(" in source
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
        "source-letter-from-neighbor-read-existential-opposite",
        "neighbor_read_own_incoming" in defined_fns
        and "formed_neighbors" in defined_fns
        and "read_report" in defined_fns
        and "existential_opposite" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
