#!/usr/bin/env python3
"""Two-tick own-incoming-set reverse/face composition on #7213 x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (1,0,0), (-1,0,0)} with locks +e_2, -e_2, and -e_2 (x-symmetric
three-site, same process as #7185 / #7213). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q, tau) is the set of
earliest incoming nearest-neighbor steps at q using only records with tick
<= tau. Unformed at tau => UNDEFINED. Reverse at a cut uses M(A, .) and
M(B, .) at each probe's own t or t+1; face likewise on C, D. Empty or
UNDEFINED => UNDEFINED. Composition HOLD iff the t+1 reverse/face bits
equal the t bits (neither side UNDEFINED, or both UNDEFINED). Same process
and x-probes as the x-symmetric three-site own-incoming-set display.
No global T. No 6-NN star. Uniqueness of incoming locks is not required.
No unique P_+. Occupancy n is not used. Named-sign lettering is not used.
No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
X_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (NEG_E1, NEG_E2),
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
    "S^+",
    "S⁺",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse/face from M at t versus t+1 on the four #7213 "
    "x-probes, and composition, are reported. Displayed, not adopted."
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


def incoming_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"incoming is not a lock set: {value!r}")
    return set_display(value)


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
    seeds: tuple[tuple[Point, Point], ...] = X_SYMMETRIC_SEEDS,
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


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("incoming sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
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


def neighbor_lock_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> frozenset[Point]:
    """Leftover contrast: locks of 6-NN formed by tau, site excluded."""
    collected: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        collected.update(locks[neighbor])
    return frozenset(collected)


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

    print("two-tick own-incoming-set reverse/face composition on #7213 x-probes")
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
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold"
        and existential_opposite(frozenset({E1}), frozenset({NEG_E1, E3, NEG_E3}))
        == "hold",
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
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau0)={incoming_display(m0[name])} "
            f"M(tau1)={incoming_display(m1[name])} "
            f"new={','.join(site_display(site_n) for site_n in new_meet[name]) or '{}'}"
        )

    reverse0 = reverse_report(m0["A"], m0["B"])
    reverse1 = reverse_report(m1["A"], m1["B"])
    face0 = face_report(m0["C"], m0["D"])
    face1 = face_report(m1["C"], m1["D"])
    composition = composition_report(reverse0, reverse1, face0, face1)
    unique_reverse = reverse_report(unique_letter(m0["A"]), unique_letter(m0["B"]))
    unique_face = face_report(unique_letter(m0["C"]), unique_letter(m0["D"]))
    leftover_neighbor_reverse = reverse_report(
        neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]]),
        neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]]),
    )
    leftover_neighbor_face = face_report(
        neighbor_lock_set(PROBES["C"], ticks, locks, ticks[PROBES["C"]]),
        neighbor_lock_set(PROBES["D"], ticks, locks, ticks[PROBES["D"]]),
    )
    print(f"reverse tau0={reverse0} tau1={reverse1}")
    print(f"face tau0={face0} tau1={face1}")
    print(f"composition={composition}")
    print(
        "per_element: each earliest incoming nearest-neighbor step at a probe, "
        "read from the record prefix at that probe's t and at t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four incoming sets at two cuts plus reverse/face/composition bits"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E2, NEG_E2)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E1, step)) != 1 for step in (E2, NEG_E2)
    )
    x_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E1, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and x_mirror_parallel_blocked
        and ticks[NEG_E1] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "incoming-set-undefined-if-unformed",
        incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(E1, 0, ticks, locks, seed_map) == frozenset({NEG_E2})
        and incoming_set(E1, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and incoming_set(NEG_E1, 0, ticks, locks, seed_map) == frozenset({NEG_E2}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E1
        and ticks[E1] == 0
        and E1 in seed_map
        and seed_map[E1] == NEG_E2
        and m0["A"] == frozenset({NEG_E2}),
    )
    checks.check(
        "theorem1-M-at-tau0",
        m0["A"] == frozenset({NEG_E2})
        and m0["B"] == frozenset({E2})
        and m0["C"] == frozenset({E1})
        and m0["D"] == frozenset({NEG_E1, E3, NEG_E3})
        and m0["A"] == frozenset(locks[PROBES["A"]])
        and m0["B"] == frozenset(locks[PROBES["B"]])
        and m0["C"] == frozenset(locks[PROBES["C"]])
        and m0["D"] == frozenset(locks[PROBES["D"]]),
        str({name: incoming_display(m0[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau1-equals-tau0",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(m0["D"], frozenset)
        and len(m0["D"]) == 3
        and unique_letter(m0["D"]) == UNDEFINED
        and m0["D"] != UNDEFINED
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0), (1, 0, 1), (1, 0, -1))
        and new_meet["B"] == ((2, 1, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet["D"] == ((1, 2, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-new-neighbors-are-later-arrivals",
        all(
            ticks[neighbor] == ticks[PROBES[name]] + 1
            for name in ("A", "B", "C", "D")
            for neighbor in new_meet[name]
        )
        and PROBES["C"] in new_meet["A"]
        and PROBES["D"] in new_meet["B"],
    )
    checks.check(
        "theorem2-reverse-tau0-and-tau1-hold",
        reverse0 == "hold"
        and reverse1 == "hold"
        and add(NEG_E2, E2) == ZERO
        and reverse0 != "fail"
        and reverse0 != UNDEFINED,
    )
    checks.check(
        "theorem2-face-tau0-and-tau1-hold",
        face0 == "hold"
        and face1 == "hold"
        and add(E1, NEG_E1) == ZERO
        and face0 != "fail"
        and face0 != UNDEFINED,
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
        "mutation-unique-letter-face-undefined",
        unique_reverse == "hold"
        and unique_face == UNDEFINED
        and reverse0 == "hold"
        and face0 == "hold"
        and face0 != unique_face,
    )
    checks.check(
        "mutation-neighbor-lock-leftover-reverse-fails",
        leftover_neighbor_reverse == "fail"
        and leftover_neighbor_face == "hold"
        and reverse0 == "hold"
        and E2 in neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        and NEG_E2 not in neighbor_lock_set(
            PROBES["A"], ticks, locks, ticks[PROBES["A"]]
        ),
    )
    checks.check(
        "mutation-empty-plus-undefined",
        existential_opposite(frozenset(), m0["B"]) == UNDEFINED
        and reverse0 == "hold",
    )
    checks.check(
        "mutation-sum-is-not-the-letter",
        isinstance(m0["A"], frozenset)
        and isinstance(m0["B"], frozenset)
        and isinstance(m0["D"], frozenset)
        and add(sum_of_set(m0["A"]), sum_of_set(m0["B"])) == ZERO
        and sum_of_set(m0["D"]) == NEG_E1
        and m0["D"] != frozenset({NEG_E1})
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "M-is-not-neighbor-lock-set",
        isinstance(m0["A"], frozenset)
        and E2 in neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        and E2 not in m0["A"]
        and NEG_E2 in m0["A"]
        and m0["A"]
        != neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]]),
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(m0["A"], frozenset)
        and isinstance(m0["D"], frozenset)
        and len(m0["A"]) == 1
        and len(m0["D"]) == 3
        and reverse0 == "hold"
        and face0 == "hold",
    )
    checks.check(
        "x-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E2}
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and ticks[NEG_E1] == 0
        and locks[NEG_E1] == {NEG_E2}
        and add(E2, NEG_E2) == ZERO
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-ticks-and-new-neighbors",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "M(A, τ0) = {−e_2}" in note
        and "M(B, τ0) = {+e_2}" in note
        and "M(C, τ0) = {+e_1}" in note
        and "M(D, τ0) = {−e_1, +e_3, −e_3}" in note
        and "M(A, τ1) = {−e_2}" in note
        and "M(B, τ1) = {+e_2}" in note
        and "M(C, τ1) = {+e_1}" in note
        and "M(D, τ1) = {−e_1, +e_3, −e_3}" in note
        and "new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)" in note
        and "new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (1, 2, 0)" in note,
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
        "note-not-star-or-unique-letter-leftover",
        "not leftover of same-tick-inclusive six-neighbor lock union" in normalized_note
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
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own incoming set" in normalized_note,
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
        and "claim_type: bounded_theorem"
        in note
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
        '    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_INCOMING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "incoming_set" in defined_fns
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
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
