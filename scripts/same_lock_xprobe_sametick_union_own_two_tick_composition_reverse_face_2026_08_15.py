#!/usr/bin/env python3
"""Two-tick S^+ reverse/face composition on four nssame x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and +e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters. L(q) is q's own unique incoming lock;
if several earliest incoming steps exist, L(q) is UNDEFINED. At cut tau,
S^+(q, tau) is the set of locks of 6-NN of q that formed at tick <= tau and
are not q, union {L(q)} when L(q) is defined and t(q) <= tau. No global T.
tau0(q)=t(q), tau1(q)=t(q)+1. Reverse at a cut holds iff some a in S^+(A, .)
and some b in S^+(B, .) have a+b=(0,0,0). Face likewise on C, D. Empty =>
UNDEFINED. Composition HOLD iff the t+1 reverse/face bits equal the t bits.
Same process and x-probes as nssamxinc #7181. Uniqueness of incoming locks
is not required. Occupancy n is not used. Named-sign lettering is not used.
No unique P_+. No Dijkstra. No Gram. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SAME_LOCK_XPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SAME_LOCK_XPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
PROBES = {
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
    "16-census",
)
CLAIM_SCOPE = (
    "Reverse/face from S⁺ at t versus t+1 on the four #7181 "
    "x-probes, and composition, are reported. Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


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


def unique_own_incoming_letter(incoming: tuple[Point, ...] | set[Point]) -> Letter:
    unique = set(incoming)
    if len(unique) != 1:
        return UNDEFINED
    vector = next(iter(unique))
    if vector not in NN:
        return UNDEFINED
    return vector


def own_lock_in_set(neighbors: frozenset[Point], letter: Letter) -> frozenset[Point]:
    if letter == UNDEFINED:
        return neighbors
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return neighbors | {letter}


def neighbor_lock_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> frozenset[Point]:
    """Locks of 6-NN formed at tick <= tau; site excluded."""
    collected: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        collected.update(locks[neighbor])
    return frozenset(collected)


def plus_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> frozenset[Point]:
    """S^+(q, tau): 6-NN locks formed by tau, union L(q) when defined and t(q)<=tau."""
    neighbors = neighbor_lock_set(site, ticks, locks, tau)
    if site not in ticks or ticks[site] > tau:
        return neighbors
    letter = unique_own_incoming_letter(locks[site])
    return own_lock_in_set(neighbors, letter)


def incoming_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> frozenset[Point] | str:
    """Leftover contrast: earliest incoming steps, or UNDEFINED if unformed."""
    if site not in ticks:
        return UNDEFINED
    return frozenset(locks[site])


def existential_opposite(left: frozenset[Point], right: frozenset[Point]) -> str:
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: frozenset[Point], set_b: frozenset[Point]) -> str:
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point], set_d: frozenset[Point]) -> str:
    return existential_opposite(set_c, set_d)


def composition_report(rev0: str, rev1: str, face0: str, face1: str) -> str:
    """HOLD iff t+1 bits equal t bits; UNDEFINED pairs are allowed only jointly."""
    if rev0 != rev1 or face0 != face1:
        return "fail"
    return "HOLD"


def new_records_meeting_six_nn(
    site: Point,
    ticks: dict[Point, int],
) -> tuple[Point, ...]:
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

    print("two-tick S^+ reverse/face composition on nssame x-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
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
        and add(NEG_E3, E3) == ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    plus_a0 = frozenset({E1, NEG_E2, E3, NEG_E3})
    plus_b0 = frozenset({E1, E3})
    plus_c0 = frozenset({E1, E2, E3, NEG_E3})
    plus_d0 = frozenset({E1, E2, E3, NEG_E3})
    plus_a1 = plus_a0
    plus_b1 = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    plus_c1 = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    plus_d1 = plus_d0
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(frozenset({E3}), frozenset()) == UNDEFINED
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(plus_a0, plus_b0) == "hold"
        and existential_opposite(plus_c0, plus_d0) == "hold"
        and existential_opposite(plus_a1, plus_b1) == "hold"
        and existential_opposite(plus_c1, plus_d1) == "hold",
    )
    checks.check(
        "composition-identity",
        composition_report("hold", "hold", "hold", "hold") == "HOLD"
        and composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and composition_report(UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED) == "HOLD"
        and composition_report("hold", UNDEFINED, "hold", "hold") == "fail"
        and composition_report("hold", "hold", "fail", "hold") == "fail",
    )

    ticks, locks = form()
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    plus0: dict[str, frozenset[Point]] = {}
    plus1: dict[str, frozenset[Point]] = {}
    letters: dict[str, Letter] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    incoming: dict[str, frozenset[Point] | str] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        letters[name] = unique_own_incoming_letter(locks[site])
        plus0[name] = plus_set(site, tau0[name], ticks, locks)
        plus1[name] = plus_set(site, tau1[name], ticks, locks)
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        incoming[name] = incoming_set(site, ticks, locks)
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
    own_reverse = reverse_report(
        own_lock_in_set(frozenset(), letters["A"]),
        own_lock_in_set(frozenset(), letters["B"]),
    )
    own_face = face_report(
        own_lock_in_set(frozenset(), letters["C"]),
        own_lock_in_set(frozenset(), letters["D"]),
    )
    m_reverse = reverse_report(
        incoming["A"] if isinstance(incoming["A"], frozenset) else frozenset(),
        incoming["B"] if isinstance(incoming["B"], frozenset) else frozenset(),
    )
    m_face = face_report(
        incoming["C"] if isinstance(incoming["C"], frozenset) else frozenset(),
        incoming["D"] if isinstance(incoming["D"], frozenset) else frozenset(),
    )
    later_common = max(ticks[PROBES[name]] for name in ("A", "B", "C", "D"))
    later_plus = {
        name: plus_set(PROBES[name], later_common, ticks, locks)
        for name in ("A", "B", "C", "D")
    }
    print(f"reverse tau0={reverse0} tau1={reverse1}")
    print(f"face tau0={face0} tau1={face1}")
    print(f"composition={composition}")
    print(
        "per_element: each lock vector in S^+ at a probe's t and at t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
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
        and ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-at-tau0",
        plus0["A"] == plus_a0
        and plus0["B"] == plus_b0
        and plus0["C"] == plus_c0
        and plus0["D"] == plus_d0
        and letters["A"] == UNDEFINED
        and letters["B"] == E1
        and letters["C"] == E1
        and letters["D"] == UNDEFINED,
        str({name: set_display(plus0[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-at-tau1",
        plus1["A"] == plus_a1
        and plus1["B"] == plus_b1
        and plus1["C"] == plus_c1
        and plus1["D"] == plus_d1
        and plus1["B"] != plus0["B"]
        and plus1["C"] != plus0["C"]
        and plus1["A"] == plus0["A"]
        and plus1["D"] == plus0["D"],
        str({name: set_display(plus1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0),)
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
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
        and E2 in plus1["B"]
        and E2 not in plus0["B"]
        and NEG_E2 in plus1["C"]
        and NEG_E2 not in plus0["C"],
    )
    checks.check(
        "theorem2-reverse-tau0-and-tau1-hold",
        reverse0 == "hold"
        and reverse1 == "hold"
        and NEG_E3 in plus0["A"]
        and E3 in plus0["B"]
        and NEG_E3 in plus1["A"]
        and E3 in plus1["B"],
    )
    checks.check(
        "theorem2-face-tau0-and-tau1-hold",
        face0 == "hold"
        and face1 == "hold"
        and E3 in plus0["C"]
        and NEG_E3 in plus0["D"]
        and E3 in plus1["C"]
        and NEG_E3 in plus1["D"],
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
        "not-leftover-of-own-t-only-7181",
        plus0["B"] == plus_b0
        and plus1["B"] == plus_b1
        and plus0["B"] != plus1["B"]
        and reverse0 == "hold"
        and reverse1 == "hold",
    )
    checks.check(
        "not-leftover-of-later-tick-global-T",
        later_common == 4
        and later_plus["C"] == plus_c0
        and plus1["C"] == plus_c1
        and later_plus["C"] != plus1["C"]
        and NEG_E2 not in later_plus["C"]
        and NEG_E2 in plus1["C"]
        and later_plus["B"] == plus1["B"],
    )
    checks.check(
        "not-leftover-of-own-incoming-set-M",
        incoming["A"] == frozenset({E2, E3, NEG_E3})
        and incoming["B"] == frozenset({E1})
        and incoming["C"] == frozenset({E1})
        and incoming["D"] == frozenset({NEG_E2, E3, NEG_E3})
        and m_reverse == "fail"
        and m_face == "fail"
        and reverse0 == "hold"
        and face0 == "hold"
        and plus0["A"] != incoming["A"],
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        letters["A"] == UNDEFINED
        and letters["D"] == UNDEFINED
        and own_reverse == UNDEFINED
        and own_face == UNDEFINED
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["A"]]) == 3
        and len(locks[PROBES["D"]]) == 3
        and letters["A"] == UNDEFINED
        and letters["D"] == UNDEFINED
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(plus0["A"]) == (1, -1, 0)
        and sum_of_set(plus0["B"]) == (1, 0, 1)
        and add(sum_of_set(plus0["A"]), sum_of_set(plus0["B"])) != ZERO
        and reverse0 == "hold",
    )
    checks.check(
        "two-site-nssame-locks",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E1},
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks) and set(ticks) <= host,
    )
    checks.check(
        "mutation-empty-plus-undefined",
        reverse_report(frozenset(), plus0["B"]) == UNDEFINED
        and face_report(plus0["C"], frozenset()) == UNDEFINED,
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-plus-sets-ticks-and-new-neighbors",
        "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=3" in note
        and "S^+(A, τ0) = {+e_1, −e_2, +e_3, −e_3}" in note
        and "S^+(B, τ0) = {+e_1, +e_3}" in note
        and "S^+(C, τ0) = {+e_1, +e_2, +e_3, −e_3}" in note
        and "S^+(D, τ0) = {+e_1, +e_2, +e_3, −e_3}" in note
        and "S^+(A, τ1) = {+e_1, −e_2, +e_3, −e_3}" in note
        and "S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(C, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(D, τ1) = {+e_1, +e_2, +e_3, −e_3}" in note
        and "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)" in note
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
        "note-not-leftovers",
        "not leftover of same-tick union own at each probe's own t alone" in normalized_note
        and "not leftover of later-tick union own" in normalized_note
        and "not leftover of own incoming set" in normalized_note
        and "not leftover of unique own-incoming letters" in normalized_note
        and "not the two-tick lock-count clock" in normalized_note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ0(q)=t(q)" in note.replace(" ", "")
        and "τ1(q)=t(q)+1" in note.replace(" ", ""),
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "Uniqueness of incoming locks is not required." in note,
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
        '    "docs/SAME_LOCK_XPROBE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "plus_set" in defined_fns
        and "existential_opposite" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_report" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 3
        and set(ticks) <= host,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
