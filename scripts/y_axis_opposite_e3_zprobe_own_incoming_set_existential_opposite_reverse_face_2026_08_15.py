#!/usr/bin/env python3
"""Own incoming set exist-opposite reverse/face on four #7192 z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_3 and -e_3 (y-axis opposite ±e_3; same
process and z-probes as nsye3zinc #7192). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q) is the set of
earliest incoming NN steps at q. Mixed stays a set. Unformed is UNDEFINED.
Unique L is not the object. Reverse holds iff some a in M(A) and some b in
M(B) have a+b=(0,0,0). Face holds iff some c in M(C) and some d in M(D) have
c+d=(0,0,0). Empty or UNDEFINED on either side is UNDEFINED; nonempty with
no opposite pair fails. The 6-NN star S^+ is not the letter; #7192 S^+ is a
leftover comparator that HOLDs reverse and face. Reverse on this display
fails from mixed M(A)={+e_1, -e_1, +e_2} against singleton M(B)={+e_3}.
Face fails from singleton M(C)={+e_3} against singleton M(D)={+e_3}.
Unique-L leftover reports reverse UNDEFINED when mixed. Occupancy n is
not used. Named-sign lettering is not used. No unique P_+. Uniqueness of
incoming locks is not required. No larger ball. No S^+.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_AXIS_OPPOSITE_E3_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_AXIS_OPPOSITE_E3_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E2, NEG_E3),
)
SAME_E3_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E2, E3),
)
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
)
NSSAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
X_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E1, NEG_E3),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
OPPOSITE_E2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E2, NEG_E2),
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
    "Runner cache",
    "f(n)",
    "ndot",
    "P_+",
)
CLAIM_SCOPE = (
    "Reverse and face from the own incoming *set* on the four #7192 z-probes "
    "are reported. No S⁺. Displayed, not adopted."
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
    """Set of six-neighbor locks. Leftover #7192 S^+ comparator only."""
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
    """Leftover #7192 S^+ neighbor list: 6-NN locks formed at tick <= t(site)."""
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

    print("own incoming set exist-opposite reverse/face on #7192 z-probes")
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
        and add(NEG_E2, E2) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(NEG_E3, E3) == ZERO
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and add(E3, E3) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E3, E1)
        and perpendicular(E3, E2)
        and not perpendicular(E3, E3)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a = frozenset({E1, NEG_E1, NEG_E2, E3})
    plus_b = frozenset({E1, E3})
    plus_c = frozenset({E1, NEG_E1, E2, E3})
    plus_d = frozenset({E1, E3})
    set_a = frozenset({E1, NEG_E1, E2})
    set_b = frozenset({E3})
    set_c = frozenset({E3})
    set_d = frozenset({E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite("UNDEFINED", frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), "UNDEFINED") == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_a, set_b) == "fail"
        and existential_opposite(set_c, set_d) == "fail"
        and existential_opposite(plus_a, plus_b) == "hold"
        and existential_opposite(plus_c, plus_d) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold"
        and existential_opposite(frozenset({E3}), frozenset({E3})) == "fail",
    )
    checks.check(
        "own-incoming-set-identity",
        unique_own_incoming_letter(frozenset({E3})) == E3
        and unique_own_incoming_letter(frozenset({E1, NEG_E1, E2})) == "UNDEFINED"
        and unique_own_incoming_letter((E1, E2)) == "UNDEFINED"
        and unique_own_incoming_letter(()) == "UNDEFINED"
        and unique_own_incoming_letter("UNDEFINED") == "UNDEFINED",
    )

    ticks, locks = form()
    same_ticks, same_locks = form(SAME_E3_SEEDS)
    nspar_ticks, nspar_locks = form(NSPAR_SEEDS)
    nssame_ticks, nssame_locks = form(NSSAME_SEEDS)
    xopp_ticks, xopp_locks = form(X_AXIS_OPPOSITE_SEEDS)
    nsopp_ticks, nsopp_locks = form(NSOPP_SEEDS)
    opp_e2_ticks, opp_e2_locks = form(OPPOSITE_E2_SEEDS)
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
        and isinstance(incoming_sets["A"], frozenset)
        and len(incoming_sets["A"]) == 1
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
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
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

    same_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        same_incoming[name] = own_incoming_set(site, same_ticks, same_locks)
    same_reverse = reverse_report(same_incoming["A"], same_incoming["B"])
    same_face = face_report(same_incoming["C"], same_incoming["D"])
    same_y: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        same_y[name] = own_incoming_set(Y_PROBES[name], same_ticks, same_locks)
    same_y_reverse = reverse_report(same_y["A"], same_y["B"])
    same_y_face = face_report(same_y["C"], same_y["D"])

    nspar_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        nspar_incoming[name] = own_incoming_set(
            PROBES[name], nspar_ticks, nspar_locks
        )
    nspar_reverse = reverse_report(nspar_incoming["A"], nspar_incoming["B"])
    nspar_face = face_report(nspar_incoming["C"], nspar_incoming["D"])

    nssame_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        nssame_incoming[name] = own_incoming_set(
            PROBES[name], nssame_ticks, nssame_locks
        )
    nssame_reverse = reverse_report(nssame_incoming["A"], nssame_incoming["B"])
    nssame_face = face_report(nssame_incoming["C"], nssame_incoming["D"])

    xopp_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        xopp_incoming[name] = own_incoming_set(
            PROBES[name], xopp_ticks, xopp_locks
        )
    xopp_reverse = reverse_report(xopp_incoming["A"], xopp_incoming["B"])
    xopp_face = face_report(xopp_incoming["C"], xopp_incoming["D"])

    nsopp_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        nsopp_incoming[name] = own_incoming_set(
            Y_PROBES[name], nsopp_ticks, nsopp_locks
        )
    nsopp_reverse = reverse_report(nsopp_incoming["A"], nsopp_incoming["B"])
    nsopp_face = face_report(nsopp_incoming["C"], nsopp_incoming["D"])

    opp_e2_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        opp_e2_incoming[name] = own_incoming_set(
            PROBES[name], opp_e2_ticks, opp_e2_locks
        )
    opp_e2_reverse = reverse_report(opp_e2_incoming["A"], opp_e2_incoming["B"])
    opp_e2_face = face_report(opp_e2_incoming["C"], opp_e2_incoming["D"])

    y_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        y_incoming[name] = own_incoming_set(Y_PROBES[name], ticks, locks)
    y_reverse = reverse_report(y_incoming["A"], y_incoming["B"])
    y_face = face_report(y_incoming["C"], y_incoming["D"])

    x_incoming: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        x_incoming[name] = own_incoming_set(X_PROBES[name], ticks, locks)
    x_reverse = reverse_report(x_incoming["A"], x_incoming["B"])
    x_face = face_report(x_incoming["C"], x_incoming["D"])

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2,
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
        and len(incoming_sets["A"]) == 3
        and len(incoming_sets["B"]) == 1
        and len(incoming_sets["C"]) == 1
        and len(incoming_sets["D"]) == 1,
        str({name: set_display(incoming_sets[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-compare-7192-S-plus",
        plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and incoming_sets["A"] != plus_sets["A"]
        and incoming_sets["B"] != plus_sets["B"]
        and incoming_sets["C"] != plus_sets["C"]
        and incoming_sets["D"] != plus_sets["D"]
        and E2 in incoming_sets["A"]
        and E2 not in plus_sets["A"]
        and NEG_E2 not in incoming_sets["A"]
        and NEG_E2 in plus_sets["A"]
        and E3 not in incoming_sets["A"]
        and E3 in plus_sets["A"]
        and E1 in plus_sets["B"]
        and E1 not in incoming_sets["B"]
        and E1 in plus_sets["D"]
        and E1 not in incoming_sets["D"],
        str((set_display(incoming_sets["A"]), set_display(plus_sets["A"]))),
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E3
        and ticks[E3] == 3
        and locks[E3] == {E1, NEG_E1, E2}
        and incoming_sets["A"] == set_a
        and letters["A"] == "UNDEFINED"
        and X_PROBES["A"] != PROBES["A"]
        and Y_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(incoming_sets["A"]) == 3
        and letters["A"] == "UNDEFINED"
        and incoming_sets["A"] != "UNDEFINED"
        and unique_own_incoming_letter(incoming_sets["A"]) == "UNDEFINED"
        and E1 in incoming_sets["A"]
        and NEG_E1 in incoming_sets["A"]
        and E2 in incoming_sets["A"]
        and letters["D"] == E3
        and incoming_sets["D"] == frozenset({E3}),
    )
    checks.check(
        "theorem1-reverse-does-not-use-singleton-M-A",
        not reverse_uses_singleton_m_a
        and reverse_status == "fail"
        and letters["A"] == "UNDEFINED"
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and len(incoming_sets["A"]) == 3,
        str((reverse_status, set_display(incoming_sets["A"]))),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and E3 in incoming_sets["B"]
        and E3 not in incoming_sets["A"]
        and NEG_E3 not in incoming_sets["A"]
        and reverse_status != "hold"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and incoming_sets["C"] == set_c
        and incoming_sets["D"] == set_d
        and E3 in incoming_sets["C"]
        and E3 in incoming_sets["D"]
        and add(E3, E3) != ZERO
        and face_status != "hold"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "discriminator-fail-from-own-incoming-not-S-plus",
        reverse_status == "fail"
        and face_status == "fail"
        and plus_reverse == "hold"
        and plus_face == "hold"
        and not reverse_uses_la
        and not reverse_uses_singleton_m_a
        and incoming_sets["A"] != plus_sets["A"]
        and incoming_sets["B"] != plus_sets["B"]
        and incoming_sets["C"] != plus_sets["C"]
        and incoming_sets["D"] != plus_sets["D"]
        and E2 in incoming_sets["A"]
        and E2 not in plus_sets["A"]
        and E1 in plus_sets["D"]
        and E1 not in incoming_sets["D"],
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "UNDEFINED"
        and unique_face == "fail"
        and reverse_status == "fail"
        and face_status == "fail"
        and reverse_status != unique_reverse
        and letters["A"] == "UNDEFINED"
        and letters["B"] == E3
        and letters["C"] == E3
        and letters["D"] == E3
        and incoming_sets["A"] != "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-S-plus-7192",
        plus_sets["A"] == plus_a
        and plus_sets["D"] == plus_d
        and plus_reverse == "hold"
        and plus_face == "hold"
        and not reverse_uses_la
        and reverse_status == "fail"
        and face_status == "fail"
        and incoming_sets["A"] != plus_sets["A"]
        and incoming_sets["B"] != plus_sets["B"]
        and incoming_sets["C"] != plus_sets["C"]
        and incoming_sets["D"] != plus_sets["D"]
        and E2 in incoming_sets["A"]
        and E2 not in plus_sets["A"]
        and E3 in plus_sets["A"]
        and E3 not in incoming_sets["A"]
        and E1 in plus_sets["D"]
        and E1 not in incoming_sets["D"],
    )
    checks.check(
        "not-x-or-y-probes-or-nsopp",
        TWO_SITE_SEEDS != NSOPP_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and x_incoming["A"] != incoming_sets["A"]
        and y_incoming["A"] != incoming_sets["A"]
        and nsopp_incoming["A"] != incoming_sets["A"]
        and x_incoming["A"] == frozenset({E1})
        and x_reverse == "fail"
        and x_face == "fail"
        and y_incoming["A"] == frozenset({NEG_E3})
        and ticks[Y_PROBES["A"]] == 0
        and y_reverse == "hold"
        and y_face == "fail"
        and nsopp_reverse == "hold"
        and nsopp_face == "hold"
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "not-same-lock-or-nspar-or-nssame-or-x-axis-or-opp-e2",
        TWO_SITE_SEEDS != SAME_E3_SEEDS
        and TWO_SITE_SEEDS != NSPAR_SEEDS
        and TWO_SITE_SEEDS != NSSAME_SEEDS
        and TWO_SITE_SEEDS != X_AXIS_OPPOSITE_SEEDS
        and TWO_SITE_SEEDS != OPPOSITE_E2_SEEDS
        and locks[E2] == {NEG_E3}
        and same_locks[E2] == {E3}
        and same_incoming["A"] == incoming_sets["A"]
        and same_incoming["D"] == incoming_sets["D"]
        and same_reverse == "fail"
        and same_face == "fail"
        and same_y["A"] == frozenset({E3})
        and same_y_reverse == "fail"
        and same_y_face == "fail"
        and y_incoming["A"] == frozenset({NEG_E3})
        and y_reverse == "hold"
        and nspar_incoming["A"] == frozenset({E3})
        and nspar_incoming["A"] != incoming_sets["A"]
        and nspar_ticks[PROBES["A"]] == 1
        and nspar_reverse == "fail"
        and nspar_face == "fail"
        and nssame_incoming["A"] == frozenset({E3})
        and nssame_incoming["A"] != incoming_sets["A"]
        and nssame_reverse == "fail"
        and nssame_face == "hold"
        and xopp_incoming["A"] == frozenset({E1, E2, NEG_E2})
        and xopp_incoming["A"] != incoming_sets["A"]
        and xopp_incoming["D"] == frozenset({NEG_E1, E2, NEG_E2})
        and xopp_reverse == "fail"
        and xopp_face == "fail"
        and opp_e2_incoming["A"] == frozenset({E3})
        and opp_e2_incoming["A"] != incoming_sets["A"]
        and opp_e2_ticks[PROBES["A"]] == 1
        and opp_e2_reverse == "fail"
        and opp_e2_face == "hold"
        and reverse_status == "fail"
        and face_status == "fail",
        str((same_reverse, nspar_reverse, set_display(xopp_incoming["A"]))),
    )
    checks.check(
        "not-nnlock-named-sign",
        incoming_sets["B"] == frozenset({E3})
        and named_sign(E3) == "+"
        and named_sign(E1) == "+"
        and named_sign(NEG_E1) == "-"
        and incoming_sets["A"] != named_sign(E1)
        and incoming_sets["C"] != named_sign(E3)
        and reverse_status == "fail"
        and face_status == "fail",
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
        len(incoming_sets["A"]) == 3
        and len(incoming_sets["B"]) == 1
        and len(incoming_sets["C"]) == 1
        and len(incoming_sets["D"]) == 1
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "two-site-y-axis-opposite-e3",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E3}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E3}
        and add(E3, NEG_E3) == ZERO
        and PROBES["A"] != E2
        and TWO_SITE_SEEDS != SAME_E3_SEEDS
        and TWO_SITE_SEEDS != NSPAR_SEEDS
        and TWO_SITE_SEEDS != NSSAME_SEEDS
        and TWO_SITE_SEEDS != X_AXIS_OPPOSITE_SEEDS
        and TWO_SITE_SEEDS != NSOPP_SEEDS
        and TWO_SITE_SEEDS != OPPOSITE_E2_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
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
        and ticks[NEG_E1] == 1
        and ticks[E1] == 1
        and ticks[NEG_E2] == 1
        and ticks[(0, 2, 0)] == 1
        and ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
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
        reverse_report(frozenset({E3}), frozenset({E3})) == "fail"
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "mutation-unique-L-would-be-undefined",
        unique_reverse == "UNDEFINED"
        and unique_face == "fail"
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "mutation-S-plus-would-hold",
        plus_reverse == "hold"
        and plus_face == "hold"
        and reverse_status == "fail"
        and face_status == "fail"
        and incoming_sets["A"] != plus_sets["A"],
    )
    checks.check(
        "mutation-sum-collapses-mixed-pairs",
        sum_of_set(incoming_sets["A"]) == E2
        and sum_of_set(incoming_sets["B"]) == E3
        and sum_of_set(incoming_sets["C"]) == E3
        and sum_of_set(incoming_sets["D"]) == E3
        and incoming_sets["A"] != frozenset({E2})
        and len(incoming_sets["A"]) == 3
        and add(sum_of_set(incoming_sets["A"]), sum_of_set(incoming_sets["B"])) != ZERO
        and add(sum_of_set(incoming_sets["C"]), sum_of_set(incoming_sets["D"])) != ZERO
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "mutation-internal-opposite-at-A-is-not-reverse",
        E1 in incoming_sets["A"]
        and NEG_E1 in incoming_sets["A"]
        and add(E1, NEG_E1) == ZERO
        and reverse_status == "fail"
        and E3 in incoming_sets["B"]
        and NEG_E3 not in incoming_sets["A"],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-incoming-sets",
        "M(A) = {+e_1, −e_1, +e_2}" in note
        and "M(B) = {+e_3}" in note
        and "M(C) = {+e_3}" in note
        and "M(D) = {+e_3}" in note
        and "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "incoming −e_1, +e_2, +e_1" in note
        and "incoming +e_3" in note,
    )
    checks.check(
        "note-reports-7192-S-plus",
        "S^+(A) = {+e_1, −e_1, −e_2, +e_3}" in note
        and "S^+(B) = {+e_1, +e_3}" in note
        and "S^+(C) = {+e_1, −e_1, +e_2, +e_3}" in note
        and "S^+(D) = {+e_1, +e_3}" in note
        and "Reverse HOLD does not use L(A)" in note
        and "L(A) = UNDEFINED" in note,
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
        and "not leftover of #7192" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "Face fails." in note
        and "Reverse fails." in note,
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
        '    "docs/Y_AXIS_OPPOSITE_E3_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and ticks[PROBES["A"]] == 3
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
