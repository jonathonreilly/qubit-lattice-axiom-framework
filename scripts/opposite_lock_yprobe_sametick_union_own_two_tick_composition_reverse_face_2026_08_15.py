#!/usr/bin/env python3
"""Two-tick S⁺ reverse/face composition on opposite-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters. L(q) is q's own unique incoming lock;
if several earliest incoming steps exist, L(q) is UNDEFINED. At cut tau,
S^+(q, tau) is the set of locks of 6-NN of q that formed at tick <= tau and
are not q, union {L(q)} when L(q) is defined and t(q) <= tau. No global T.
tau0(q)=t(q) and tau1(q)=t(q)+1. Reverse at a cut is exist-opposite of
S^+(A, .) and S^+(B, .); face likewise on C, D. Empty S^+ on either side is
UNDEFINED. Composition HOLD iff the t+1 reverse/face bits equal the t bits.
Same process and y-probes as the #7167 same-tick union-own display.
Uniqueness of incoming locks is not required. Occupancy n is not used.
Named-sign lettering is not used. No unique P_+. No Dijkstra. No Gram.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
Plus = frozenset[Point]
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
    "P_+",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse/face from S⁺ at t versus t+1 on the four #7167 "
    "y-probes, and composition, are reported. Displayed, not adopted."
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


def named_sign(lock: Point) -> str:
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def recorded_lock_set(pairs: tuple[tuple[Point, Point], ...]) -> frozenset[Point]:
    """Set of six-neighbor locks. Duplicates collapse."""
    return frozenset(lock for _neighbor, lock in pairs)


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point]) -> Letter:
    """Unique letter if the probe's own earliest incoming locks are a singleton in NN."""
    unique = set(incoming)
    if len(unique) != 1:
        return UNDEFINED
    vector = next(iter(unique))
    if vector not in NN:
        return UNDEFINED
    return vector


def own_lock_in_set(neighbors: frozenset[Point], letter: Letter) -> frozenset[Point]:
    """Union of neighbor locks with L(q) when L(q) is defined."""
    if letter == UNDEFINED:
        return neighbors
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return neighbors | {letter}


def neighbor_locks_at_tau(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> tuple[tuple[Point, Point], ...]:
    """Locks of 6-NN of site formed at tick <= tau; site excluded."""
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > tau:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def s_plus(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> frozenset[Point]:
    """S^+(q, tau): 6-NN locks at tick <= tau, q excluded, union L(q) if defined and t(q)<=tau."""
    neighbors = recorded_lock_set(neighbor_locks_at_tau(site, ticks, locks, tau))
    if site not in ticks or ticks[site] > tau:
        return neighbors
    letter = unique_own_incoming_letter(locks[site])
    return own_lock_in_set(neighbors, letter)


def incoming_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Plus | str:
    """Leftover M: earliest incoming NN steps using only records with tick <= tau."""
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


def later_tick_T(
    ticks: dict[Point, int],
    probes: dict[str, Point] = PROBES,
) -> int | None:
    """Leftover global T: max formation tick of the four named probes."""
    defined = [ticks[probes[name]] for name in ("A", "B", "C", "D") if probes[name] in ticks]
    if len(defined) != 4:
        return None
    return max(defined)


def existential_opposite(left: frozenset[Point] | str, right: frozenset[Point] | str) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right."""
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


def reverse_report(set_a: frozenset[Point] | str, set_b: frozenset[Point] | str) -> str:
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point] | str, set_d: frozenset[Point] | str) -> str:
    return existential_opposite(set_c, set_d)


def composition_report(rev0: str, rev1: str, face0: str, face1: str) -> str:
    """HOLD iff t+1 bits equal t bits."""
    if rev0 != rev1 or face0 != face1:
        return "fail"
    return "HOLD"


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


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def letter_display(letter: Letter) -> str:
    if letter == UNDEFINED:
        return UNDEFINED
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


def site_display(site: Point) -> str:
    return f"({site[0]}, {site[1]}, {site[2]})"


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

    print("two-tick S+ reverse/face composition on opposite-lock y-probes")
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a0 = frozenset({E1, NEG_E1})
    plus_b0 = frozenset({E1, E3})
    plus_c0 = frozenset({NEG_E1, E2})
    plus_d0 = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    plus_a1 = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    plus_b1 = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    plus_c1 = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    plus_d1 = plus_d0
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(plus_a0, plus_b0) == "hold"
        and existential_opposite(plus_c0, plus_d0) == "hold"
        and existential_opposite(plus_a1, plus_b1) == "hold"
        and existential_opposite(frozenset({E1}), plus_b0) == "fail",
    )
    checks.check(
        "composition-identity",
        composition_report("hold", "hold", "hold", "hold") == "HOLD"
        and composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and composition_report(UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED) == "HOLD"
        and composition_report("hold", "fail", "hold", "hold") == "fail"
        and composition_report("hold", "hold", "hold", UNDEFINED) == "fail",
    )
    checks.check(
        "unique-own-incoming-letter-identity",
        unique_own_incoming_letter((NEG_E1,)) == NEG_E1
        and unique_own_incoming_letter((E1, E1)) == E1
        and unique_own_incoming_letter((NEG_E2, NEG_E3, E3)) == UNDEFINED
        and unique_own_incoming_letter(()) == UNDEFINED,
    )

    ticks, locks, seed_map = form()
    later_common = later_tick_T(ticks)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    letters: dict[str, Letter] = {}
    plus0: dict[str, frozenset[Point]] = {}
    plus1: dict[str, frozenset[Point]] = {}
    m0: dict[str, Plus | str] = {}
    m1: dict[str, Plus | str] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    exclude0: dict[str, frozenset[Point]] = {}
    later_plus: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        letters[name] = unique_own_incoming_letter(locks[site])
        plus0[name] = s_plus(site, tau0[name], ticks, locks)
        plus1[name] = s_plus(site, tau1[name], ticks, locks)
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        exclude0[name] = recorded_lock_set(
            neighbor_locks_at_tau(site, ticks, locks, tau0[name])
        )
        later_plus[name] = s_plus(site, later_common or 0, ticks, locks)
        print(
            f"{name} t={ticks[site]} L={letter_display(letters[name])} "
            f"S+(tau0)={set_display(plus0[name])} "
            f"S+(tau1)={set_display(plus1[name])} "
            f"new={','.join(site_display(site_n) for site_n in new_meet[name]) or '{}'}"
        )

    reverse0 = reverse_report(plus0["A"], plus0["B"])
    reverse1 = reverse_report(plus1["A"], plus1["B"])
    face0 = face_report(plus0["C"], plus0["D"])
    face1 = face_report(plus1["C"], plus1["D"])
    composition = composition_report(reverse0, reverse1, face0, face1)
    m_reverse0 = reverse_report(m0["A"], m0["B"])
    m_face0 = face_report(m0["C"], m0["D"])
    exclude_reverse = reverse_report(exclude0["A"], exclude0["B"])
    exclude_face = face_report(exclude0["C"], exclude0["D"])
    later_reverse = reverse_report(later_plus["A"], later_plus["B"])
    later_face = face_report(later_plus["C"], later_plus["D"])
    own_reverse = reverse_report(
        own_lock_in_set(frozenset(), letters["A"]),
        own_lock_in_set(frozenset(), letters["B"]),
    )
    own_face = face_report(
        own_lock_in_set(frozenset(), letters["C"]),
        own_lock_in_set(frozenset(), letters["D"]),
    )
    print(f"reverse tau0={reverse0} tau1={reverse1}")
    print(f"face tau0={face0} tau1={face1}")
    print(f"composition={composition}")
    print(
        "per_element: each lock vector in S^+ at a probe's t and at t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four S^+ lock sets at two cuts plus reverse/face/composition bits"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and tau0["A"] == 0
        and tau1["A"] == 1
        and tau0["B"] == 2
        and tau1["B"] == 3
        and tau0["C"] == 1
        and tau1["C"] == 2
        and tau0["D"] == 3
        and tau1["D"] == 4,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-own-letters",
        letters["A"] == NEG_E1
        and letters["B"] == E1
        and letters["C"] == E2
        and letters["D"] == UNDEFINED,
        str({name: letter_display(letters[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-at-tau0",
        plus0["A"] == plus_a0
        and plus0["B"] == plus_b0
        and plus0["C"] == plus_c0
        and plus0["D"] == plus_d0,
        str({name: set_display(plus0[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-at-tau1",
        plus1["A"] == plus_a1
        and plus1["B"] == plus_b1
        and plus1["C"] == plus_c1
        and plus1["D"] == plus_d1
        and plus1["A"] != plus0["A"]
        and plus1["B"] != plus0["B"]
        and plus1["C"] != plus0["C"]
        and plus1["D"] == plus0["D"],
        str({name: set_display(plus1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((0, 2, 0), (0, 1, 1), (0, 1, -1))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1))
        and new_meet["D"] == ((2, 1, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-new-neighbors-are-later-arrivals",
        all(
            ticks[neighbor] == ticks[PROBES[name]] + 1
            for name in ("A", "B", "C", "D")
            for neighbor in new_meet[name]
        )
        and E2 in locks[(0, 2, 0)]
        and E3 in locks[(0, 1, 1)]
        and NEG_E3 in locks[(0, 1, -1)],
    )
    checks.check(
        "theorem2-reverse-tau0-and-tau1-hold",
        reverse0 == "hold"
        and reverse1 == "hold"
        and reverse0 != UNDEFINED
        and reverse1 != UNDEFINED,
    )
    checks.check(
        "theorem2-face-tau0-and-tau1-hold",
        face0 == "hold"
        and face1 == "hold"
        and face0 != UNDEFINED
        and face1 != UNDEFINED,
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "HOLD"
        and reverse1 == reverse0
        and face1 == face0
        and reverse0 != UNDEFINED
        and face0 != UNDEFINED,
    )
    checks.check(
        "S-plus-grows-bits-freeze",
        plus1["A"] != plus0["A"]
        and plus1["B"] != plus0["B"]
        and plus1["C"] != plus0["C"]
        and reverse1 == reverse0 == "hold"
        and face1 == face0 == "hold",
    )
    checks.check(
        "not-leftover-of-own-incoming-M",
        m0["A"] == frozenset({NEG_E1})
        and m0["B"] == frozenset({E1})
        and m0["C"] == frozenset({E2})
        and m0["D"] == frozenset({NEG_E2, NEG_E3, E3})
        and m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and plus0["A"] != m0["A"]
        and plus1["A"] != m1["A"]
        and plus1["A"] != plus0["A"],
    )
    checks.check(
        "not-leftover-of-sametick-exclude-q",
        exclude0["A"] == frozenset({E1})
        and exclude_reverse == "fail"
        and reverse0 == "hold"
        and plus0["A"] != exclude0["A"]
        and exclude_face == "hold",
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        own_reverse == "hold"
        and own_face == UNDEFINED
        and face0 == "hold"
        and face0 != own_face
        and letters["D"] == UNDEFINED,
    )
    checks.check(
        "not-leftover-of-later-tick-union-own",
        later_common == 3
        and later_plus["A"] != plus0["A"]
        and later_reverse == "hold"
        and later_face == "hold"
        and tau0["A"] != later_common
        and tau1["A"] != later_common,
    )
    checks.check(
        "no-global-later-T-in-letter",
        later_common
        == max(
            ticks[PROBES["A"]],
            ticks[PROBES["B"]],
            ticks[PROBES["C"]],
            ticks[PROBES["D"]],
        )
        and tau0["A"] == ticks[PROBES["A"]]
        and tau1["D"] == ticks[PROBES["D"]] + 1
        and ticks[PROBES["A"]] != later_common,
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS
        and PROBES["A"] == E2,
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
        "sign-lettering-loses-axis",
        named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus0["A"]) == ZERO
        and add(sum_of_set(plus0["A"]), sum_of_set(plus0["B"])) != ZERO
        and add(sum_of_set(plus0["C"]), sum_of_set(plus0["D"])) != ZERO
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["D"]]) == 3
        and letters["D"] == UNDEFINED
        and plus0["D"] == plus_d0
        and face0 == "hold",
        str(sorted(locks[PROBES["D"]])),
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "mutation-empty-plus-undefined",
        reverse_report(frozenset(), plus0["B"]) == UNDEFINED
        and reverse0 == "hold",
    )
    checks.check(
        "mutation-exclude-q-reverse-would-fail",
        exclude_reverse == "fail" and reverse0 == "hold",
    )
    checks.check(
        "mutation-own-incoming-face-would-be-undefined",
        own_face == UNDEFINED and face0 == "hold",
    )
    checks.check(
        "mutation-M-frozen-while-S-plus-grows",
        m1["A"] == m0["A"]
        and plus1["A"] != plus0["A"]
        and composition == "HOLD",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-S-plus",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "S^+(A, τ0) = {+e_1, −e_1}" in note
        and "S^+(B, τ0) = {+e_1, +e_3}" in note
        and "S^+(C, τ0) = {−e_1, +e_2}" in note
        and "S^+(D, τ0) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S^+(A, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(C, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S^+(D, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "L(A) = −e_1" in note
        and "L(B) = +e_1" in note
        and "L(C) = +e_2" in note
        and "L(D) = UNDEFINED" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)" in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-hold-hold-composition-hold",
        "Reverse at τ0: hold" in note
        and "Reverse at τ1: hold" in note
        and "Face at τ0: hold" in note
        and "Face at τ1: hold" in note
        and "Composition: HOLD" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-M-leftover",
        "not leftover of own incoming sets M" in normalized_note
        and "S^+ grows" in note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "s_plus" in defined_fns
        and "existential_opposite" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_report" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
        and "form" in defined_fns
        and "unique_own_incoming_letter" in defined_fns
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
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
