#!/usr/bin/env python3
"""Simultaneous M and O at t+1 reverse/face on four #7211 y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process and y-probes as nmsyop #7211). A 6-NN step is allowed iff it
is perpendicular to the parent lock axis. Newly formed sites lock the
incoming step. Seeds keep their seed letters as a singleton. t(q) is the
formation tick. tau = t+1 is that probe's own next tick, not a global later
T. M(q,tau) is the set of earliest incoming NN steps at q from records with
tick <= tau. Mixed stays a set. Unformed at tau is UNDEFINED. O(q,tau) is
the outgoing dual: the set of e in {±e_1,±e_2,±e_3} such that q+e is formed
and e is in M(q+e,tau). Unformed at tau is UNDEFINED. Empty O is empty, not
UNDEFINED. Reverse of M at tau holds iff some a in M(A,tau) and some b in
M(B,tau) have a+b=(0,0,0). Face of M likewise on C,D. Reverse/face of O at
tau are the same predicate on the outgoing sets. Empty or UNDEFINED on
either side is UNDEFINED; nonempty with no opposite pair fails. Unique L is
not the object. The 6-NN star S^+ is not the letter. Occupancy n is not
used. Named-sign lettering is not used. No unique P_+. Uniqueness of
incoming or outgoing locks is not required. No larger ball.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
LockSet = frozenset[Point] | str
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
    "Simultaneous M and O at t+1 on the four "
    "#7211 y-probes, intersection, and reverse/face of each are reported. "
    "Displayed, not adopted."
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


def incoming_at(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> LockSet:
    """M(q,tau): earliest incoming from records with tick <= tau.

    Seeds are a singleton. Unformed at tau is UNDEFINED.
    """
    if site not in ticks or ticks[site] > tau:
        return "UNDEFINED"
    return frozenset(locks[site])


def outgoing_at(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> LockSet:
    """O(q,tau): e in NN with q+e formed and e in M(q+e,tau).

    Unformed at tau is UNDEFINED. Empty O is empty, not UNDEFINED.
    """
    if site not in ticks or ticks[site] > tau:
        return "UNDEFINED"
    outgoing: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        incoming = incoming_at(neighbor, tau, ticks, locks)
        if incoming != "UNDEFINED" and isinstance(incoming, frozenset) and step in incoming:
            outgoing.add(step)
    return frozenset(outgoing)


def intersection_at(incoming: LockSet, outgoing: LockSet) -> LockSet:
    """M ∩ O when both defined. If either UNDEFINED then UNDEFINED."""
    if incoming == "UNDEFINED" or outgoing == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return "UNDEFINED"
    return incoming & outgoing


def unique_own_letter(locks: tuple[Point, ...] | set[Point] | LockSet) -> Letter:
    """Unique-L leftover: UNDEFINED when mixed. Not this letter."""
    if locks == "UNDEFINED":
        return "UNDEFINED"
    unique = set(locks)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def existential_opposite(left: LockSet, right: LockSet) -> str:
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


def reverse_report(set_a: LockSet, set_b: LockSet) -> str:
    """Reverse iff some a in the A-set and some b in the B-set have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: LockSet, set_d: LockSet) -> str:
    """Face iff some c in the C-set and some d in the D-set have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def set_display(locks: LockSet) -> str:
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


def timed_probe_sets(
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    probes: dict[str, Point] = PROBES,
) -> tuple[dict[str, LockSet], dict[str, LockSet], dict[str, LockSet]]:
    """M, O, and M∩O at each probe's own tau=t+1."""
    incoming: dict[str, LockSet] = {}
    outgoing: dict[str, LockSet] = {}
    inter: dict[str, LockSet] = {}
    for name, site in probes.items():
        if site not in ticks:
            incoming[name] = "UNDEFINED"
            outgoing[name] = "UNDEFINED"
            inter[name] = "UNDEFINED"
            continue
        tau = ticks[site] + 1
        incoming[name] = incoming_at(site, tau, ticks, locks)
        outgoing[name] = outgoing_at(site, tau, ticks, locks)
        inter[name] = intersection_at(incoming[name], outgoing[name])
    return incoming, outgoing, inter


def sum_of_set(locks: LockSet) -> Point | str:
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

    print("simultaneous M and O at t+1 reverse/face on #7211 y-probes")
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
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    set_m_a = frozenset({NEG_E1})
    set_m_b = frozenset({E1})
    set_m_c = frozenset({E2})
    set_m_d = frozenset({NEG_E2, E3, NEG_E3})
    set_o_a = frozenset({E2, E3, NEG_E3})
    set_o_b = frozenset({E2, E3, NEG_E3})
    set_o_c = frozenset({E1, NEG_E1, E3, NEG_E3})
    set_o_d = frozenset({E1, NEG_E1})
    empty: frozenset[Point] = frozenset()
    checks.check(
        "existential-opposite-identity",
        existential_opposite("UNDEFINED", frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), "UNDEFINED") == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset({E3})) == "UNDEFINED"
        and existential_opposite(frozenset({E3}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_m_a, set_m_b) == "hold"
        and existential_opposite(set_m_c, set_m_d) == "hold"
        and existential_opposite(set_o_a, set_o_b) == "hold"
        and existential_opposite(set_o_c, set_o_d) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "timed-set-identity",
        unique_own_letter(frozenset({NEG_E1})) == NEG_E1
        and unique_own_letter(frozenset({E2, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_letter(frozenset({NEG_E2, E3, NEG_E3})) == "UNDEFINED"
        and unique_own_letter((E1, E2)) == "UNDEFINED"
        and unique_own_letter(()) == "UNDEFINED"
        and unique_own_letter("UNDEFINED") == "UNDEFINED"
        and intersection_at(set_m_a, set_o_a) == empty
        and intersection_at("UNDEFINED", set_o_a) == "UNDEFINED",
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

    incoming, outgoing, inter = timed_probe_sets(ticks, locks)
    incoming_t: dict[str, LockSet] = {}
    outgoing_t: dict[str, LockSet] = {}
    outgoing_inf: dict[str, LockSet] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        formation = ticks[site]
        incoming_t[name] = incoming_at(site, formation, ticks, locks)
        outgoing_t[name] = outgoing_at(site, formation, ticks, locks)
        outgoing_inf[name] = outgoing_at(site, formation + 32, ticks, locks)
        print(
            f"{name} t={formation} tau={formation + 1} "
            f"M={set_display(incoming[name])} "
            f"O={set_display(outgoing[name])} "
            f"M∩O={set_display(inter[name])}"
        )

    reverse_m = reverse_report(incoming["A"], incoming["B"])
    face_m = face_report(incoming["C"], incoming["D"])
    reverse_o = reverse_report(outgoing["A"], outgoing["B"])
    face_o = face_report(outgoing["C"], outgoing["D"])
    unique_m_reverse = reverse_report(
        frozenset({unique_own_letter(incoming["A"])})
        if unique_own_letter(incoming["A"]) != "UNDEFINED"
        else "UNDEFINED",
        frozenset({unique_own_letter(incoming["B"])})
        if unique_own_letter(incoming["B"]) != "UNDEFINED"
        else "UNDEFINED",
    )
    unique_m_face = face_report(
        frozenset({unique_own_letter(incoming["C"])})
        if unique_own_letter(incoming["C"]) != "UNDEFINED"
        else "UNDEFINED",
        frozenset({unique_own_letter(incoming["D"])})
        if unique_own_letter(incoming["D"]) != "UNDEFINED"
        else "UNDEFINED",
    )
    unique_o_reverse = reverse_report(
        frozenset({unique_own_letter(outgoing["A"])})
        if unique_own_letter(outgoing["A"]) != "UNDEFINED"
        else "UNDEFINED",
        frozenset({unique_own_letter(outgoing["B"])})
        if unique_own_letter(outgoing["B"]) != "UNDEFINED"
        else "UNDEFINED",
    )
    unique_o_face = face_report(
        frozenset({unique_own_letter(outgoing["C"])})
        if unique_own_letter(outgoing["C"]) != "UNDEFINED"
        else "UNDEFINED",
        frozenset({unique_own_letter(outgoing["D"])})
        if unique_own_letter(outgoing["D"]) != "UNDEFINED"
        else "UNDEFINED",
    )
    reverse_o_at_t = reverse_report(outgoing_t["A"], outgoing_t["B"])
    print(f"M_reverse={reverse_m} M_face={face_m}")
    print(f"O_reverse={reverse_o} O_face={face_o}")
    print(
        f"unique_L_M_reverse={unique_m_reverse} unique_L_M_face={unique_m_face} "
        f"unique_L_O_reverse={unique_o_reverse} unique_L_O_face={unique_o_face}"
    )
    print(
        "per_element: each lock vector in timed M(q,tau) or timed O(q,tau)"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four incoming sets, four outgoing sets, four intersections, "
        "and reverse/face of M and of O as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    perp_in, perp_out, _perp_inter = timed_probe_sets(perp_ticks, perp_locks)
    zsym_in, zsym_out, _zsym_inter = timed_probe_sets(zsym_ticks, zsym_locks)
    twosite_in, twosite_out, twosite_inter = timed_probe_sets(
        twosite_ticks, twosite_locks
    )
    nstri_in, nstri_out, nstri_inter = timed_probe_sets(nstri_ticks, nstri_locks)
    x_in, x_out, _x_inter = timed_probe_sets(ticks, locks, X_PROBES)
    x_reverse_m = reverse_report(x_in["A"], x_in["B"])
    x_face_m = face_report(x_in["C"], x_in["D"])
    x_reverse_o = reverse_report(x_out["A"], x_out["B"])
    x_face_o = face_report(x_out["C"], x_out["D"])

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-timed-incoming",
        incoming["A"] == set_m_a
        and incoming["B"] == set_m_b
        and incoming["C"] == set_m_c
        and incoming["D"] == set_m_d
        and incoming["A"] != "UNDEFINED"
        and incoming["D"] != "UNDEFINED"
        and len(incoming["A"]) == 1
        and len(incoming["D"]) == 3,
        str({name: set_display(incoming[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-timed-outgoing",
        outgoing["A"] == set_o_a
        and outgoing["B"] == set_o_b
        and outgoing["C"] == set_o_c
        and outgoing["D"] == set_o_d
        and outgoing["A"] != "UNDEFINED"
        and outgoing["D"] != "UNDEFINED"
        and len(outgoing["A"]) == 3
        and len(outgoing["D"]) == 2,
        str({name: set_display(outgoing[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-intersection-empty",
        inter["A"] == empty
        and inter["B"] == empty
        and inter["C"] == empty
        and inter["D"] == empty
        and all(inter[name] != "UNDEFINED" for name in ("A", "B", "C", "D"))
        and NEG_E1 not in outgoing["A"]
        and E1 not in outgoing["B"]
        and E2 not in outgoing["C"]
        and NEG_E2 not in outgoing["D"],
        str({name: set_display(inter[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-is-seed-and-M-frozen",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and incoming["A"] == frozenset({NEG_E1})
        and incoming_t["A"] == incoming["A"]
        and incoming_t["B"] == incoming["B"]
        and incoming_t["C"] == incoming["C"]
        and incoming_t["D"] == incoming["D"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-O-nonempty-at-tplus1-empty-at-t-for-ABC",
        outgoing_t["A"] == empty
        and outgoing_t["B"] == empty
        and outgoing_t["C"] == empty
        and outgoing["A"] != empty
        and outgoing["B"] != empty
        and outgoing["C"] != empty
        and outgoing["D"] == outgoing_inf["D"]
        and reverse_o_at_t == "UNDEFINED",
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(incoming["D"]) == 3
        and unique_own_letter(incoming["D"]) == "UNDEFINED"
        and incoming["D"] != "UNDEFINED"
        and unique_own_letter(outgoing["A"]) == "UNDEFINED"
        and outgoing["A"] != "UNDEFINED"
        and NEG_E2 in incoming["D"]
        and E3 in incoming["D"]
        and NEG_E3 in incoming["D"],
    )
    checks.check(
        "theorem1-compare-7211-M",
        incoming["A"] == set_m_a
        and incoming["B"] == set_m_b
        and incoming["C"] == set_m_c
        and incoming["D"] == set_m_d
        and incoming["A"] != outgoing["A"]
        and reverse_m == "hold"
        and face_m == "hold"
        and NEG_E1 in incoming["A"]
        and NEG_E1 not in outgoing["A"],
        str((set_display(incoming["A"]), set_display(outgoing["A"]))),
    )
    checks.check(
        "theorem2-reverse-face-from-M",
        reverse_m == "hold"
        and face_m == "hold"
        and incoming["A"] == set_m_a
        and incoming["B"] == set_m_b
        and incoming["C"] == set_m_c
        and incoming["D"] == set_m_d
        and add(NEG_E1, E1) == ZERO
        and add(E2, NEG_E2) == ZERO
        and reverse_m != "fail"
        and reverse_m != "UNDEFINED"
        and face_m != "fail"
        and face_m != "UNDEFINED",
        str((reverse_m, face_m)),
    )
    checks.check(
        "theorem3-reverse-face-from-O",
        reverse_o == "hold"
        and face_o == "hold"
        and outgoing["A"] == set_o_a
        and outgoing["B"] == set_o_b
        and outgoing["C"] == set_o_c
        and outgoing["D"] == set_o_d
        and add(E3, NEG_E3) == ZERO
        and add(E1, NEG_E1) == ZERO
        and reverse_o != "fail"
        and reverse_o != "UNDEFINED"
        and face_o != "fail"
        and face_o != "UNDEFINED",
        str((reverse_o, face_o)),
    )
    checks.check(
        "not-unique-L-leftover",
        unique_m_reverse == "hold"
        and unique_m_face == "UNDEFINED"
        and unique_o_reverse == "UNDEFINED"
        and unique_o_face == "UNDEFINED"
        and reverse_m == "hold"
        and face_m == "hold"
        and reverse_o == "hold"
        and face_o == "hold"
        and face_m != unique_m_face
        and reverse_o != unique_o_reverse
        and unique_own_letter(incoming["A"]) == NEG_E1
        and unique_own_letter(incoming["D"]) == "UNDEFINED"
        and unique_own_letter(outgoing["A"]) == "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-7211-M-alone",
        incoming["A"] == set_m_a
        and reverse_m == "hold"
        and face_m == "hold"
        and outgoing["A"] != incoming["A"]
        and outgoing["A"] != empty
        and inter["A"] == empty
        and reverse_o == "hold"
        and face_o == "hold",
    )
    checks.check(
        "not-leftover-of-untimed-O-alone",
        outgoing["A"] == outgoing_inf["A"]
        and outgoing["B"] == outgoing_inf["B"]
        and outgoing["C"] == outgoing_inf["C"]
        and outgoing["D"] == outgoing_inf["D"]
        and incoming["A"] != outgoing["A"]
        and reverse_m == "hold"
        and reverse_o == "hold"
        and inter["A"] == empty,
    )
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and x_in["A"] != incoming["A"]
        and zsym_in["A"] != incoming["A"]
        and perp_in["A"] != incoming["A"]
        and perp_out["A"] != outgoing["A"]
        and zsym_out["A"] != outgoing["A"]
        and x_reverse_m == "fail"
        and x_face_m == "fail"
        and x_reverse_o == "fail"
        and x_face_o == "fail"
        and reverse_m == "hold"
        and reverse_o == "hold",
    )
    checks.check(
        "not-two-site-or-nstri-third-site",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and ticks[NEG_E2] == 0
        and twosite_ticks[NEG_E2] == 1
        and twosite_in["A"] == incoming["A"]
        and twosite_out["A"] == outgoing["A"]
        and twosite_inter["A"] == inter["A"]
        and nstri_in["B"] != incoming["B"]
        and nstri_in["D"] != incoming["D"]
        and E2 in nstri_in["B"]
        and NEG_E1 in nstri_in["D"]
        and nstri_inter["B"] != empty
        and nstri_inter["D"] != empty,
    )
    checks.check(
        "not-nnlock-named-sign",
        incoming["A"] == frozenset({NEG_E1})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and incoming["C"] == frozenset({E2})
        and named_sign(E2) == "+"
        and incoming["A"] != named_sign(NEG_E1)
        and outgoing["A"] != named_sign(E3),
    )
    checks.check(
        "incoming-and-outgoing-are-nn-steps",
        all(incoming[name] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(outgoing[name] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(incoming["A"]) == 1
        and len(incoming["D"]) == 3
        and len(outgoing["A"]) == 3
        and len(outgoing["D"]) == 2
        and reverse_m == "hold"
        and face_m == "hold"
        and reverse_o == "hold"
        and face_o == "hold",
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
        "unformed-at-tau-is-undefined",
        incoming_at((4, 0, 0), 1, ticks, locks) == "UNDEFINED"
        and outgoing_at((4, 0, 0), 1, ticks, locks) == "UNDEFINED"
        and incoming_at(PROBES["D"], 0, ticks, locks) == "UNDEFINED"
        and outgoing_at(PROBES["D"], 0, ticks, locks) == "UNDEFINED",
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), incoming["B"]) == "UNDEFINED"
        and face_report(incoming["C"], frozenset()) == "UNDEFINED"
        and reverse_report("UNDEFINED", incoming["B"]) == "UNDEFINED"
        and face_report(outgoing["C"], "UNDEFINED") == "UNDEFINED"
        and reverse_o_at_t == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_m == "hold"
        and reverse_o == "hold"
        and face_m == "hold"
        and face_o == "hold",
    )
    checks.check(
        "mutation-unique-L-O-would-be-undefined",
        unique_o_reverse == "UNDEFINED"
        and unique_o_face == "UNDEFINED"
        and unique_m_face == "UNDEFINED"
        and reverse_o == "hold"
        and face_o == "hold"
        and face_m == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed-D",
        sum_of_set(incoming["A"]) == NEG_E1
        and sum_of_set(incoming["B"]) == E1
        and sum_of_set(incoming["C"]) == E2
        and sum_of_set(incoming["D"]) == NEG_E2
        and incoming["D"] != frozenset({NEG_E2})
        and len(incoming["D"]) == 3
        and reverse_m == "hold"
        and face_m == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-intersection",
        "M(A,τ) = {−e_1}" in note
        and "M(B,τ) = {+e_1}" in note
        and "M(C,τ) = {+e_2}" in note
        and "M(D,τ) = {−e_2, +e_3, −e_3}" in note
        and "O(A,τ) = {+e_2, +e_3, −e_3}" in note
        and "O(B,τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C,τ) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D,τ) = {+e_1, −e_1}" in note
        and "M(A,τ)∩O(A,τ) = {}" in note
        and "M(B,τ)∩O(B,τ) = {}" in note
        and "M(C,τ)∩O(C,τ) = {}" in note
        and "M(D,τ)∩O(D,τ) = {}" in note
        and "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "incoming +e_1" in note
        and "incoming +e_2" in note
        and "incoming −e_2, −e_3, +e_3" in note,
    )
    checks.check(
        "note-reports-hold-hold-of-M-and-O",
        "Reverse of M: hold" in note
        and "Face of M: hold" in note
        and "Reverse of O: hold" in note
        and "Face of O: hold" in note
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
        and "own incoming" in normalized_note
        and "own outgoing" in normalized_note
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
        and "not leftover of untimed" in normalized_note
        and "Reverse of M holds." in note
        and "Face of M holds." in note
        and "Reverse of O holds." in note
        and "Face of O holds." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "No S⁺." in note
        and "own incoming" in normalized_note
        and "own outgoing" in normalized_note,
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
        '    "docs/Y_SYMMETRIC_THREE_SITE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def incoming_at(" in source
        and "def outgoing_at(" in source
        and "def intersection_at(" in source
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
        "source-letter-from-timed-incoming-outgoing-existential-opposite",
        "incoming_at" in defined_fns
        and "outgoing_at" in defined_fns
        and "intersection_at" in defined_fns
        and "existential_opposite" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
