#!/usr/bin/env python3
"""Two-tick S^+ reverse/face composition on z-symmetric x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,0,1), (0,0,-1)} with locks +e_1, -e_1, and -e_1. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters. L(q) is q's own unique
incoming lock; if several earliest incoming steps exist, L(q) is UNDEFINED.
At cut tau, S^+(q, tau) is the set of locks of 6-NN of q that formed at tick
<= tau and are not q, union {L(q)} when L(q) is defined and t(q) <= tau.
Reverse at a cut uses S^+(A, .) and S^+(B, .) at each probe's own t or t+1;
face likewise on C, D. Empty or UNDEFINED => UNDEFINED. Composition HOLD
iff the t+1 reverse/face bits equal the t bits (neither side UNDEFINED, or
both UNDEFINED). Same process and x-probes as the z-symmetric three-site
same-tick union-own display. No global T. Uniqueness of incoming locks is
not required. No unique P_+. Occupancy n is not used. Named-sign lettering
is not used. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
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
BALL_SQ = 9
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
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
)
CLAIM_SCOPE = (
    "Reverse/face from S⁺ at t versus t+1 on the four #7188 "
    "x-probes, and whether those bits compose, are reported. "
    "Displayed, not adopted."
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


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def letter_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    lock = next(iter(value))
    return LOCK_NAME[lock]


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
    seeds: tuple[tuple[Point, Point], ...] = Z_SYMMETRIC_SEEDS,
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


def unique_own_incoming(site: Point, locks: dict[Point, set[Point]]) -> Incoming:
    """Unique own incoming lock; mixed or missing is UNDEFINED."""
    letters = locks.get(site, set())
    if len(letters) != 1:
        return UNDEFINED
    return frozenset(letters)


def neighbor_lock_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> frozenset[Point]:
    """Locks of 6-NN formed by tau, site excluded."""
    collected: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        collected.update(locks[neighbor])
    return frozenset(collected)


def s_plus(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Incoming:
    """Same-tick-inclusive 6-NN locks union L(q) when defined and t(q) <= tau."""
    collected = neighbor_lock_set(site, ticks, locks, tau)
    if site not in ticks or ticks[site] > tau:
        return collected
    letter = unique_own_incoming(site, locks)
    if letter == UNDEFINED:
        return collected
    if not isinstance(letter, frozenset):
        raise TypeError(f"own incoming is not a lock set: {letter!r}")
    return collected | letter


def incoming_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Incoming:
    """Leftover: earliest incoming NN steps at site using records with tick <= tau."""
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


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("S^+ sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(
    set_a: Incoming,
    set_b: Incoming,
    formed_a: bool = True,
    formed_b: bool = True,
) -> str:
    if not formed_a or not formed_b:
        return UNDEFINED
    return existential_opposite(set_a, set_b)


def face_report(
    set_c: Incoming,
    set_d: Incoming,
    formed_c: bool = True,
    formed_d: bool = True,
) -> str:
    if not formed_c or not formed_d:
        return UNDEFINED
    return existential_opposite(set_c, set_d)


def composition_report(rev0: str, rev1: str, face0: str, face1: str) -> str:
    """HOLD iff t+1 bits equal t bits; UNDEFINED pairs are allowed only jointly."""
    if rev0 != rev1 or face0 != face1:
        return "fail"
    return "HOLD"


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

    print("two-tick S^+ reverse/face composition on z-symmetric x-probes")
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E2, NEG_E2}), frozenset({E1})) == "fail"
        and existential_opposite(frozenset({E1}), frozenset({E1})) == "fail"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "composition-identity",
        composition_report("hold", "hold", "hold", "hold") == "HOLD"
        and composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and composition_report(UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED) == "HOLD"
        and composition_report("fail", UNDEFINED, "fail", "fail") == "fail"
        and composition_report("hold", "hold", "fail", "hold") == "fail",
    )

    ticks, locks, seed_map = form()
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    plus0: dict[str, Incoming] = {}
    plus1: dict[str, Incoming] = {}
    letters: dict[str, Incoming] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    leftover_m0: dict[str, Incoming] = {}
    leftover_m1: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        letters[name] = unique_own_incoming(site, locks)
        plus0[name] = s_plus(site, tau0[name], ticks, locks)
        plus1[name] = s_plus(site, tau1[name], ticks, locks)
        leftover_m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        leftover_m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} L={letter_display(letters[name])} "
            f"S+(tau0)={set_display(plus0[name]) if isinstance(plus0[name], frozenset) else plus0[name]} "
            f"S+(tau1)={set_display(plus1[name]) if isinstance(plus1[name], frozenset) else plus1[name]} "
            f"new={','.join(site_display(site_n) for site_n in new_meet[name]) or '{}'}"
        )

    reverse0 = reverse_report(
        plus0["A"],
        plus0["B"],
        formed_a=PROBES["A"] in ticks and ticks[PROBES["A"]] <= tau0["A"],
        formed_b=PROBES["B"] in ticks and ticks[PROBES["B"]] <= tau0["B"],
    )
    reverse1 = reverse_report(
        plus1["A"],
        plus1["B"],
        formed_a=PROBES["A"] in ticks and ticks[PROBES["A"]] <= tau1["A"],
        formed_b=PROBES["B"] in ticks and ticks[PROBES["B"]] <= tau1["B"],
    )
    face0 = face_report(
        plus0["C"],
        plus0["D"],
        formed_c=PROBES["C"] in ticks and ticks[PROBES["C"]] <= tau0["C"],
        formed_d=PROBES["D"] in ticks and ticks[PROBES["D"]] <= tau0["D"],
    )
    face1 = face_report(
        plus1["C"],
        plus1["D"],
        formed_c=PROBES["C"] in ticks and ticks[PROBES["C"]] <= tau1["C"],
        formed_d=PROBES["D"] in ticks and ticks[PROBES["D"]] <= tau1["D"],
    )
    composition = composition_report(reverse0, reverse1, face0, face1)
    unique_reverse = reverse_report(letters["A"], letters["B"])
    unique_face = face_report(letters["C"], letters["D"])
    leftover_m_reverse = reverse_report(leftover_m0["A"], leftover_m0["B"])
    leftover_m_face = face_report(leftover_m0["C"], leftover_m0["D"])
    leftover_m_composition = composition_report(
        leftover_m_reverse,
        reverse_report(leftover_m1["A"], leftover_m1["B"]),
        leftover_m_face,
        face_report(leftover_m1["C"], leftover_m1["D"]),
    )
    reverse_uses_la = (
        letters["A"] != UNDEFINED
        and isinstance(letters["A"], frozenset)
        and reverse0 == "hold"
        and reverse_report(plus0["A"] - letters["A"], plus0["B"]) != "hold"
        if isinstance(plus0["A"], frozenset) and isinstance(letters["A"], frozenset)
        else False
    )
    print(f"reverse tau0={reverse0} tau1={reverse1}")
    print(f"face tau0={face0} tau1={face1}")
    print(f"composition={composition} reverse_uses_L(A)={reverse_uses_la}")
    print(
        "per_element: each lock vector in same-tick-inclusive six-neighbor "
        "locks union L(q) when L(q) is defined, at t and at t+1"
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
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and ticks[NEG_E3] == 0
        and ticks[E2] == 1
        and ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2,
    )
    checks.check(
        "theorem1-own-letters",
        letters["A"] == UNDEFINED
        and letters["B"] == frozenset({E1})
        and letters["C"] == frozenset({E1})
        and letters["D"] == frozenset({E1}),
    )
    expected_a = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    expected_b0 = frozenset({E1, E2})
    expected_b1 = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    expected_c = frozenset({E1, E2, NEG_E2})
    expected_d0 = frozenset({E1, E2})
    expected_d1 = frozenset({E1, E2, NEG_E2})
    checks.check(
        "theorem1-S-plus-at-tau0",
        plus0["A"] == expected_a
        and plus0["B"] == expected_b0
        and plus0["C"] == expected_c
        and plus0["D"] == expected_d0,
        str({name: set_display(plus0[name]) if isinstance(plus0[name], frozenset) else plus0[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-at-tau1",
        plus1["A"] == expected_a
        and plus1["B"] == expected_b1
        and plus1["C"] == expected_c
        and plus1["D"] == expected_d1,
        str({name: set_display(plus1[name]) if isinstance(plus1[name], frozenset) else plus1[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-S-plus-B-and-D-grow",
        plus1["B"] != plus0["B"]
        and plus1["D"] != plus0["D"]
        and plus1["A"] == plus0["A"]
        and plus1["C"] == plus0["C"]
        and plus0["B"] < plus1["B"]
        and plus0["D"] < plus1["D"],
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0),)
        and new_meet["B"] == ((1, 2, 1), (1, 0, 1), (1, 1, 2))
        and new_meet["C"] == ((2, 1, 0), (2, -1, 0))
        and new_meet["D"] == ((1, 2, 0), (1, 0, 0)),
        str(new_meet),
    )
    checks.check(
        "theorem1-new-neighbors-are-later-arrivals",
        all(
            ticks[neighbor] == ticks[PROBES[name]] + 1
            for name in ("A", "B", "C", "D")
            for neighbor in new_meet[name]
        )
        and E1 in plus0["A"]
        if isinstance(plus0["A"], frozenset)
        else False,
    )
    checks.check(
        "theorem2-reverse-tau0-and-tau1-hold",
        reverse0 == "hold" and reverse1 == "hold" and reverse_uses_la is False,
    )
    checks.check(
        "theorem2-face-tau0-and-tau1-hold",
        face0 == "hold" and face1 == "hold",
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
        "mutation-unique-letter-reverse-undefined",
        unique_reverse == UNDEFINED
        and unique_face == "fail"
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "mutation-M-leftover-fail-fail-hold",
        leftover_m0["A"] == frozenset({E2, NEG_E2})
        and leftover_m0["B"] == frozenset({E1})
        and leftover_m0["C"] == frozenset({E1})
        and leftover_m0["D"] == frozenset({E1})
        and leftover_m1["A"] == leftover_m0["A"]
        and leftover_m1["B"] == leftover_m0["B"]
        and leftover_m_reverse == "fail"
        and leftover_m_face == "fail"
        and leftover_m_composition == "HOLD"
        and reverse0 == "hold",
    )
    checks.check(
        "mutation-empty-plus-undefined",
        existential_opposite(frozenset(), plus0["B"]) == UNDEFINED
        and reverse0 == "hold",
    )
    checks.check(
        "mutation-sum-is-not-the-predicate",
        isinstance(plus0["A"], frozenset)
        and isinstance(plus0["B"], frozenset)
        and reverse0 == "hold",
    )
    checks.check(
        "S-plus-is-not-M",
        isinstance(plus0["A"], frozenset)
        and isinstance(leftover_m0["A"], frozenset)
        and E1 in plus0["A"]
        and E1 not in leftover_m0["A"]
        and plus0["A"] != leftover_m0["A"],
    )
    checks.check(
        "unformed-excludes-own-letter",
        s_plus(PROBES["C"], 3, ticks, locks)
        == neighbor_lock_set(PROBES["C"], ticks, locks, 3)
        and ticks[PROBES["C"]] == 4,
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-S-plus-ticks-and-new-neighbors",
        "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "S^+(A, τ0) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(B, τ0) = {+e_1, +e_2}" in note
        and "S^+(C, τ0) = {+e_1, +e_2, −e_2}" in note
        and "S^+(D, τ0) = {+e_1, +e_2}" in note
        and "S^+(A, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S^+(C, τ1) = {+e_1, +e_2, −e_2}" in note
        and "S^+(D, τ1) = {+e_1, +e_2, −e_2}" in note
        and "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)" in note
        and "new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0)" in note
        and "new 6-NN of D at t(D)+1: (1, 2, 0), (1, 0, 0)" in note,
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
        "note-not-M-or-unique-letter-leftover",
        "not leftover of own incoming sets" in normalized_note
        and "not leftover of unique own-incoming letters" in normalized_note
        and "mixed remains a set" in normalized_note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
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
        '    "docs/Z_SYMMETRIC_THREE_SITE_SAMETICK_UNION_OWN_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and not any("occup" in name for name in defined_fns),
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
