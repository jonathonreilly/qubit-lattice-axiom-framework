#!/usr/bin/env python3
"""Own outgoing set exist-opposite reverse/face on four #7211 y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process and y-probes as nmsyop #7211). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q) is the set of
earliest incoming NN steps at q. Mixed stays a set. Unformed is UNDEFINED.
O(q) is the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such that
q+e is formed in B_3(0) and e is in M(q+e). Unformed q is UNDEFINED. Empty O
is empty, not UNDEFINED. O is not M and is not S^+. Unique L is not the
object. Reverse holds iff some a in O(A) and some b in O(B) have
a+b=(0,0,0). Face holds iff some c in O(C) and some d in O(D) have
c+d=(0,0,0). Empty or UNDEFINED on either side is UNDEFINED; nonempty with
no opposite pair fails. Reverse HOLD of #7211 uses M(A)={-e_1} against
M(B)={+e_1} and does not use an incoming letter that is also outgoing.
Occupancy n is not used. Named-sign lettering is not used. No unique P_+.
Uniqueness of outgoing locks is not required. No larger ball.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Outgoing = frozenset[Point] | str
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
)
CLAIM_SCOPE = (
    "Reverse and face from the own outgoing *set* on the four "
    "#7211 y-probes are reported. No S⁺. Displayed, not adopted."
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


def own_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Outgoing:
    """Outgoing dual of M. Unformed is UNDEFINED. Empty O is empty, not UNDEFINED."""
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


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point] | Incoming) -> Letter:
    """Unique-L leftover of M: UNDEFINED when mixed. Not this letter."""
    if incoming == "UNDEFINED":
        return "UNDEFINED"
    unique = set(incoming)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def unique_own_outgoing_letter(outgoing: tuple[Point, ...] | set[Point] | Outgoing) -> Letter:
    """Unique-L leftover of O: UNDEFINED when mixed. Not this letter."""
    if outgoing == "UNDEFINED":
        return "UNDEFINED"
    unique = set(outgoing)
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
    """Reverse iff some a in O(A) and some b in O(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in O(C) and some d in O(D) have c+d=(0,0,0)."""
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


def reverse_hold_uses_incoming_also_outgoing(
    incoming_a: Incoming,
    incoming_b: Incoming,
    outgoing_a: Outgoing,
    outgoing_b: Outgoing,
) -> bool:
    """True iff a #7211 reverse HOLD pair uses a letter that is also outgoing."""
    if incoming_a == "UNDEFINED" or incoming_b == "UNDEFINED":
        return False
    if outgoing_a == "UNDEFINED" or outgoing_b == "UNDEFINED":
        return False
    if not isinstance(incoming_a, frozenset) or not isinstance(incoming_b, frozenset):
        return False
    if not isinstance(outgoing_a, frozenset) or not isinstance(outgoing_b, frozenset):
        return False
    for a in incoming_a:
        for b in incoming_b:
            if add(a, b) != ZERO:
                continue
            if a in outgoing_a or b in outgoing_b:
                return True
    return False


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

    print("own outgoing set exist-opposite reverse/face on #7211 y-probes")
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
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and add(E3, NEG_E3) == ZERO
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
        and existential_opposite(out_c, out_d) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold"
        and existential_opposite(plus_a, plus_b) == "hold"
        and existential_opposite(plus_c, plus_d) == "hold",
    )
    checks.check(
        "own-outgoing-set-identity",
        unique_own_outgoing_letter(frozenset({NEG_E1})) == NEG_E1
        and unique_own_outgoing_letter(frozenset({E2, NEG_E2})) == "UNDEFINED"
        and unique_own_outgoing_letter(frozenset({E2, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_outgoing_letter(frozenset({E1, NEG_E1})) == "UNDEFINED"
        and unique_own_outgoing_letter((E1, E2)) == "UNDEFINED"
        and unique_own_outgoing_letter(()) == "UNDEFINED"
        and unique_own_outgoing_letter("UNDEFINED") == "UNDEFINED"
        and unique_own_incoming_letter(frozenset({NEG_E1})) == NEG_E1
        and unique_own_incoming_letter(frozenset({NEG_E2, E3, NEG_E3})) == "UNDEFINED",
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
    outgoing_sets: dict[str, Outgoing] = {}
    letters: dict[str, Letter] = {}
    out_letters: dict[str, Letter] = {}
    plus_sets: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        incoming_sets[name] = own_incoming_set(site, ticks, locks)
        outgoing_sets[name] = own_outgoing_set(site, ticks, locks)
        letters[name] = unique_own_incoming_letter(incoming_sets[name])
        out_letters[name] = unique_own_outgoing_letter(outgoing_sets[name])
        pairs = own_tick_neighbor_locks(site, ticks, locks)
        plus_sets[name] = own_lock_in_set(recorded_lock_set(pairs), letters[name])
        print(
            f"{name} t={ticks[site]} M={set_display(incoming_sets[name])} "
            f"O={set_display(outgoing_sets[name])} "
            f"L={letter_display(letters[name])} "
            f"S+={set_display(plus_sets[name])}"
        )

    reverse_status = reverse_report(outgoing_sets["A"], outgoing_sets["B"])
    face_status = face_report(outgoing_sets["C"], outgoing_sets["D"])
    reverse_m = reverse_report(incoming_sets["A"], incoming_sets["B"])
    face_m = face_report(incoming_sets["C"], incoming_sets["D"])
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
    unique_out_reverse = reverse_report(
        own_lock_in_set(frozenset(), out_letters["A"]),
        own_lock_in_set(frozenset(), out_letters["B"]),
    )
    unique_out_face = face_report(
        own_lock_in_set(frozenset(), out_letters["C"]),
        own_lock_in_set(frozenset(), out_letters["D"]),
    )
    reverse_7211_uses_incoming_also_outgoing = reverse_hold_uses_incoming_also_outgoing(
        incoming_sets["A"],
        incoming_sets["B"],
        outgoing_sets["A"],
        outgoing_sets["B"],
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"M_reverse={reverse_m} M_face={face_m} "
        f"S+_reverse={plus_reverse} S+_face={plus_face} "
        f"reverse_7211_uses_incoming_also_outgoing="
        f"{reverse_7211_uses_incoming_also_outgoing}"
    )
    print(f"unique_L_reverse={unique_reverse} unique_L_face={unique_face}")
    print(
        f"unique_O_reverse={unique_out_reverse} unique_O_face={unique_out_face}"
    )
    print(
        "per_element: each lock vector in the probe's own outgoing set O(q)"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four outgoing sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    perp_outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        perp_outgoing[name] = own_outgoing_set(PROBES[name], perp_ticks, perp_locks)
    perp_face = face_report(perp_outgoing["C"], perp_outgoing["D"])

    zsym_outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        zsym_outgoing[name] = own_outgoing_set(PROBES[name], zsym_ticks, zsym_locks)
    zsym_reverse = reverse_report(zsym_outgoing["A"], zsym_outgoing["B"])

    twosite_outgoing: dict[str, Outgoing] = {}
    twosite_plus: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        twosite_outgoing[name] = own_outgoing_set(site, twosite_ticks, twosite_locks)
        twosite_incoming = own_incoming_set(site, twosite_ticks, twosite_locks)
        twosite_letter = unique_own_incoming_letter(twosite_incoming)
        twosite_pairs = own_tick_neighbor_locks(site, twosite_ticks, twosite_locks)
        twosite_plus[name] = own_lock_in_set(
            recorded_lock_set(twosite_pairs), twosite_letter
        )

    nstri_outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        nstri_outgoing[name] = own_outgoing_set(PROBES[name], nstri_ticks, nstri_locks)

    x_outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        x_outgoing[name] = own_outgoing_set(X_PROBES[name], ticks, locks)
    x_reverse = reverse_report(x_outgoing["A"], x_outgoing["B"])
    x_face = face_report(x_outgoing["C"], x_outgoing["D"])

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
        "theorem1-outgoing-sets",
        outgoing_sets["A"] == out_a
        and outgoing_sets["B"] == out_b
        and outgoing_sets["C"] == out_c
        and outgoing_sets["D"] == out_d
        and outgoing_sets["A"] != "UNDEFINED"
        and outgoing_sets["D"] != "UNDEFINED"
        and len(outgoing_sets["A"]) == 3
        and len(outgoing_sets["B"]) == 3
        and len(outgoing_sets["C"]) == 4
        and len(outgoing_sets["D"]) == 2,
        str({name: set_display(outgoing_sets[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-compare-O-to-M-of-7211",
        outgoing_sets["A"] != incoming_sets["A"]
        and outgoing_sets["B"] != incoming_sets["B"]
        and outgoing_sets["C"] != incoming_sets["C"]
        and outgoing_sets["D"] != incoming_sets["D"]
        and incoming_sets["A"].isdisjoint(outgoing_sets["A"])
        and incoming_sets["B"].isdisjoint(outgoing_sets["B"])
        and incoming_sets["C"].isdisjoint(outgoing_sets["C"])
        and incoming_sets["D"].isdisjoint(outgoing_sets["D"])
        and NEG_E1 in incoming_sets["A"]
        and NEG_E1 not in outgoing_sets["A"]
        and E1 in incoming_sets["B"]
        and E1 not in outgoing_sets["B"],
        str(
            (
                set_display(incoming_sets["A"]),
                set_display(outgoing_sets["A"]),
                set_display(incoming_sets["B"]),
                set_display(outgoing_sets["B"]),
            )
        ),
    )
    checks.check(
        "theorem1-O-is-not-S-plus",
        outgoing_sets["A"] != plus_sets["A"]
        and outgoing_sets["B"] != plus_sets["B"]
        and outgoing_sets["C"] != plus_sets["C"]
        and outgoing_sets["D"] != plus_sets["D"]
        and plus_sets["A"] == plus_a
        and plus_sets["B"] == plus_b
        and plus_sets["C"] == plus_c
        and plus_sets["D"] == plus_d
        and E1 in plus_sets["A"]
        and E1 not in outgoing_sets["A"],
        str((set_display(outgoing_sets["A"]), set_display(plus_sets["A"]))),
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
        len(outgoing_sets["A"]) == 3
        and len(outgoing_sets["D"]) == 2
        and out_letters["A"] == "UNDEFINED"
        and out_letters["B"] == "UNDEFINED"
        and out_letters["C"] == "UNDEFINED"
        and out_letters["D"] == "UNDEFINED"
        and outgoing_sets["A"] != "UNDEFINED"
        and outgoing_sets["D"] != "UNDEFINED"
        and unique_own_outgoing_letter(outgoing_sets["D"]) == "UNDEFINED"
        and E1 in outgoing_sets["D"]
        and NEG_E1 in outgoing_sets["D"],
    )
    checks.check(
        "theorem1-reverse-7211-hold-does-not-use-outgoing-incoming",
        reverse_m == "hold"
        and incoming_sets["A"] == set_a
        and incoming_sets["B"] == set_b
        and add(NEG_E1, E1) == ZERO
        and not reverse_7211_uses_incoming_also_outgoing
        and NEG_E1 not in outgoing_sets["A"]
        and E1 not in outgoing_sets["B"],
        str((reverse_m, reverse_7211_uses_incoming_also_outgoing)),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and outgoing_sets["A"] == out_a
        and outgoing_sets["B"] == out_b
        and add(E3, NEG_E3) == ZERO
        and E3 in outgoing_sets["A"]
        and NEG_E3 in outgoing_sets["B"]
        and reverse_status != "fail"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and outgoing_sets["C"] == out_c
        and outgoing_sets["D"] == out_d
        and add(E1, NEG_E1) == ZERO
        and E1 in outgoing_sets["C"]
        and NEG_E1 in outgoing_sets["D"]
        and face_status != "fail"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "discriminator-hold-from-O-not-M-or-S-plus",
        reverse_status == "hold"
        and face_status == "hold"
        and reverse_m == "hold"
        and face_m == "hold"
        and plus_reverse == "hold"
        and plus_face == "hold"
        and outgoing_sets["A"] != incoming_sets["A"]
        and outgoing_sets["A"] != plus_sets["A"]
        and not reverse_7211_uses_incoming_also_outgoing
        and len(outgoing_sets["A"]) == 3
        and len(incoming_sets["A"]) == 1
        and letters["A"] == NEG_E1,
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "hold"
        and unique_face == "UNDEFINED"
        and unique_out_reverse == "UNDEFINED"
        and unique_out_face == "UNDEFINED"
        and reverse_status == "hold"
        and face_status == "hold"
        and face_status != unique_face
        and reverse_status != unique_out_reverse
        and letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and letters["D"] == "UNDEFINED"
        and out_letters["A"] == "UNDEFINED"
        and incoming_sets["D"] != "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-M-or-S-plus-7211",
        incoming_sets["A"] == set_a
        and plus_sets["A"] == plus_a
        and plus_reverse == "hold"
        and plus_face == "hold"
        and reverse_m == "hold"
        and outgoing_sets["A"] != incoming_sets["A"]
        and outgoing_sets["B"] != incoming_sets["B"]
        and outgoing_sets["C"] != incoming_sets["C"]
        and outgoing_sets["D"] != incoming_sets["D"]
        and outgoing_sets["A"] != plus_sets["A"]
        and E1 not in outgoing_sets["A"]
        and E1 in plus_sets["A"]
        and NEG_E1 in incoming_sets["A"]
        and NEG_E1 not in outgoing_sets["A"],
    )
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and x_outgoing["A"] != outgoing_sets["A"]
        and zsym_outgoing["A"] != outgoing_sets["A"]
        and perp_outgoing["A"] != outgoing_sets["A"]
        and perp_outgoing["C"] != outgoing_sets["C"]
        and zsym_outgoing["C"] != outgoing_sets["C"]
        and x_reverse == "fail"
        and x_face == "fail"
        and zsym_reverse == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and perp_face == "hold",
    )
    checks.check(
        "not-two-site-or-nstri-third-site",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and ticks[NEG_E2] == 0
        and twosite_ticks[NEG_E2] == 1
        and twosite_outgoing["A"] == outgoing_sets["A"]
        and twosite_outgoing["D"] == outgoing_sets["D"]
        and twosite_plus["D"] == twosite_plus_d
        and E2 in twosite_plus["D"]
        and E2 not in plus_sets["D"]
        and nstri_outgoing["B"] != outgoing_sets["B"]
        and nstri_outgoing["D"] != outgoing_sets["D"]
        and E1 in nstri_outgoing["B"]
        and NEG_E1 in nstri_outgoing["D"],
    )
    checks.check(
        "not-nnlock-named-sign",
        outgoing_sets["A"] == frozenset({E2, E3, NEG_E3})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and outgoing_sets["A"] != named_sign(E2)
        and incoming_sets["A"] != named_sign(NEG_E1),
    )
    checks.check(
        "outgoing-locks-are-nn-steps",
        all(
            outgoing_sets[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        len(outgoing_sets["A"]) == 3
        and len(outgoing_sets["B"]) == 3
        and len(outgoing_sets["C"]) == 4
        and len(outgoing_sets["D"]) == 2
        and reverse_status == "hold"
        and face_status == "hold",
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
        "empty-O-is-empty-not-undefined",
        own_outgoing_set(unformed, ticks, locks) == "UNDEFINED"
        and unformed not in ticks
        and isinstance(outgoing_sets["A"], frozenset)
        and outgoing_sets["A"]
        and existential_opposite(frozenset(), outgoing_sets["B"]) == "UNDEFINED"
        and own_outgoing_set(PROBES["A"], ticks, locks) != "UNDEFINED",
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), outgoing_sets["B"]) == "UNDEFINED"
        and face_report(outgoing_sets["C"], frozenset()) == "UNDEFINED"
        and reverse_report("UNDEFINED", outgoing_sets["B"]) == "UNDEFINED"
        and face_report(outgoing_sets["C"], "UNDEFINED") == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-unique-L-outgoing-would-be-undefined",
        unique_out_face == "UNDEFINED"
        and unique_out_reverse == "UNDEFINED"
        and unique_face == "UNDEFINED"
        and unique_reverse == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "mutation-M-hold-uses-letters-absent-from-O",
        reverse_m == "hold"
        and face_m == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and not reverse_7211_uses_incoming_also_outgoing
        and incoming_sets["A"] != outgoing_sets["A"],
    )
    checks.check(
        "mutation-sum-cancels-mixed-O",
        sum_of_set(outgoing_sets["A"]) == E2
        and sum_of_set(outgoing_sets["B"]) == E2
        and sum_of_set(outgoing_sets["C"]) == ZERO
        and sum_of_set(outgoing_sets["D"]) == ZERO
        and outgoing_sets["A"] != frozenset({E2})
        and outgoing_sets["C"] != frozenset()
        and len(outgoing_sets["A"]) == 3
        and reverse_status == "hold"
        and face_status == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-outgoing-sets",
        "O(A) = {+e_2, +e_3, −e_3}" in note
        and "O(B) = {+e_2, +e_3, −e_3}" in note
        and "O(C) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D) = {+e_1, −e_1}" in note
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
        "note-reports-7211-M-compare",
        "O is not M" in note
        and "Reverse HOLD of #7211 does not use an incoming letter that is also outgoing."
        in note
        and "L(A) = −e_1" in note,
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
        and "own outgoing set" in normalized_note
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
        and "Face holds." in note
        and "Reverse holds." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "O is not M" in note
        and "own outgoing set" in normalized_note,
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
        '    "docs/Y_SYMMETRIC_THREE_SITE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def own_outgoing_set(" in source
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
        "source-letter-from-own-outgoing-set-existential-opposite",
        "own_outgoing_set" in defined_fns
        and "existential_opposite" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
