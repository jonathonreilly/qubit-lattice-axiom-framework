#!/usr/bin/env python3
"""Score same-k reverse at k=17 under c2d4 on B_51(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST2_MAX4_OUT_FACE_SAMEK_K17_B51_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_MAX4_OUT_FACE_SAMEK_K17_B51_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=17 under the named cost-2 max≥4 "
    "out-face hop-cost on B_51(0) is reported. "
    "Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
DIJKSTRA_CALLS = 0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def least_nonzero_abs(v: tuple[int, int, int]) -> int | None:
    nonzero = [abs(c) for c in v if c != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_height_count(v: tuple[int, int, int]) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if nu_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2 and least_nonzero_abs(w) == 1:
        return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3 and unit_height_count(w) == 2:
        return 3
    return 1


def kappa_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if (
        support_size(v) == 2
        and support_size(w) == 3
        and unit_height_count(w) == 2
    ):
        return 3
    return 1


def iota_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 3 and sigma_w == 3:
        m = min(abs(c) for c in w)
        if m >= 2 and sum(1 for c in w if abs(c) == m) != 2:
            return 3
    return 1


def omega_grow(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 2
        and support_size(w) == 2
        and max(abs(c) for c in w) > max(abs(c) for c in v)
    )


def df_grow(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return omega_grow(v, w) and max(abs(c) for c in v) >= 2


def d3_grow(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return omega_grow(v, w) and max(abs(c) for c in v) >= 3


def d4_grow(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return omega_grow(v, w) and max(abs(c) for c in v) >= 4


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if omega_grow(v, w):
        return 3
    return 1


def df_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if df_grow(v, w):
        return 3
    return 1


def d3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if d3_grow(v, w):
        return 3
    return 1


def d4_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if d4_grow(v, w):
        return 3
    return 1


def c2d4_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if d4_grow(v, w):
        return 2
    return 1


def dijkstra_c2d4(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist: dict[tuple[int, int, int], int] = {(0, 0, 0): 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, (0, 0, 0))]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        d, v = heapq.heappop(heap)
        if v in seen:
            continue
        seen.add(v)
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w not in site_set:
                continue
            nd = d + c2d4_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        out: list[str] = []
        for elt in node.value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, str):
                return None
            out.append(elt.value)
        return tuple(out)
    return None


def path_cost(
    walk: tuple[tuple[int, int, int], ...],
    cost_fn,
) -> int:
    return sum(cost_fn(a, b) for a, b in zip(walk, walk[1:]))


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths",
        "declared inputs are the source note and the current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "note claim_scope matches the displayed scoring statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "c2d4 is not written into Admissibility",
        "Do not write c2d4 into Admissibility" in note
        and "Do not write `c2d4` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note or "no uniqueness" in note.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note",
        forbidden_hits == [],
    )

    sites = ball(51)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_c2d4(sites)
    t1700 = dist[(17, 0, 0)]
    t171717 = dist[(17, 17, 17)]
    t5100 = dist[(51, 0, 0)]
    t4800 = dist[(48, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    t520 = dist[(5, 2, 0)]
    reverse = 3 * t1700 * t1700 > t171717 * t171717
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 18)],
        (17, 1, 1),
        (17, 1, 0),
        (17, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 18)],
        *[(17, y, 1) for y in range(3, 18)],
        *[(17, 17, z) for z in range(2, 18)],
    )
    witness_skip = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
        (4, 2, 0),
    )
    witness_later = witness_skip + ((5, 2, 0),)
    skip_hop = ((3, 2, 0), (4, 2, 0))
    later_hop = ((4, 2, 0), (5, 2, 0))
    height_two = ((2, 2, 0), (3, 2, 0))
    unit_out_face = ((1, 1, 0), (2, 1, 0))
    later_out_face = ((7, 2, 0), (8, 2, 0))
    height2_nongrow = ((1, -2, 0), (2, -2, 0))
    ridge_enter = ((2, 1, 0), (2, 1, 1))
    print(f"n_sites {len(sites)}")
    print(f"t(17,0,0) {t1700}")
    print(f"t(17,17,17) {t171717}")
    print(f"t(17,0,0)^2/289 {t1700 * t1700}/289")
    print(f"t(17,17,17)^2/867 {t171717 * t171717}/867")
    print(f"3t_axis^2 {3 * t1700 * t1700}")
    print(f"t_body^2 {t171717 * t171717}")
    print(f"reverse {reverse}")
    print(f"t(51,0,0) {t5100}")
    print(f"t(48,0,0) {t4800}")
    print(f"t(3,2,0) {t320}")
    print(f"t(4,2,0) {t420}")
    print(f"t(5,2,0) {t520}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_axis_sum {path_cost(witness_axis, c2d4_cost)}")
    print(f"witness_body_sum {path_cost(witness_body, c2d4_cost)}")
    print(f"c2d4_skip {c2d4_cost(*skip_hop)}")
    print(f"d4_skip {d4_cost(*skip_hop)}")
    print(f"d3_skip {d3_cost(*skip_hop)}")
    print(f"df_skip {df_cost(*skip_hop)}")
    print(f"omega_skip {omega_cost(*skip_hop)}")
    print(f"rho3_skip {rho3_cost(*skip_hop)}")
    print(f"c2d4_later {c2d4_cost(*later_hop)}")
    print(f"d4_later {d4_cost(*later_hop)}")
    print(f"rho3_later {rho3_cost(*later_hop)}")
    print(f"d4_grow_skip {d4_grow(*skip_hop)}")
    print(f"d3_grow_skip {d3_grow(*skip_hop)}")
    print(f"d4_grow_later {d4_grow(*later_hop)}")
    print(f"witness_skip_c2d4 {path_cost(witness_skip, c2d4_cost)}")
    print(f"witness_skip_d3 {path_cost(witness_skip, d3_cost)}")
    print(f"witness_later_c2d4 {path_cost(witness_later, c2d4_cost)}")
    print(f"witness_later_d4 {path_cost(witness_later, d4_cost)}")
    print(f"witness_later_rho3 {path_cost(witness_later, rho3_cost)}")

    checks.check(
        "t-1700-171717",
        "t(17,0,0)=33 and t(17,17,17)=55",
        t1700 == 33
        and t171717 == 55
        and t1700 == path_cost(witness_axis, c2d4_cost)
        and t171717 == path_cost(witness_body, c2d4_cost),
    )
    checks.check(
        "reverse-k17",
        "t(17,0,0)^2/289 > t(17,17,17)^2/867 holds",
        reverse
        and 3 * t1700 * t1700 == 3267
        and t171717 * t171717 == 3025
        and "3267 > 3025" in note
        and "inequality holds" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b51",
        "B_51(0) has 182207 sites and 182206 nonzero sites",
        len(sites) == 182207 and len(nonzero) == 182206 and all(l1(v) <= 51 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_51(0) is reached",
        len(dist) == 182207,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`33`" in note
        and "`55`" in note
        and "`(17,0,0)`" in note
        and "`(17,17,17)`" in note
        and "t(17,0,0) = 33" in note
        and "t(17,17,17) = 55" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "3267 > 3025" in note and "1089/289" in note and "3025/867" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "c2d4 prices max≥4 out-face at 2 while ρ3 prices it at 1",
        c2d4_cost(*later_hop) == 2
        and rho3_cost(*later_hop) == 1
        and mu_cost(*later_hop) == 1
        and c2d4_cost(*later_out_face) == 2
        and rho3_cost(*later_out_face) == 1
        and c2d4_cost(*height2_nongrow) == 1
        and t1700 == 33
        and t171717 == 55
        and t520 == 12
        and path_cost(witness_later, c2d4_cost) == 12
        and path_cost(witness_later, rho3_cost) == 11
        and "cannot price max≥4 out-face" in note
        and "`t(5,2,0) = 12`" in note,
    )
    checks.check(
        "not-leftover-of-d4",
        "d4 prices max≥4 out-face at 3 while c2d4 prices it at 2",
        c2d4_cost(*later_hop) == 2
        and d4_cost(*later_hop) == 3
        and path_cost(witness_later, d4_cost) == 13
        and path_cost(witness_later, c2d4_cost) == 12
        and t520 == 12
        and t5100 == 72
        and "not leftover of `d4`" in note
        and "`t(51,0,0) = 72`" in note,
    )
    checks.check(
        "not-leftover-of-b48",
        "(17,17,17) lies outside B_48(0) and the note says so",
        l1((17, 17, 17)) == 51
        and (17, 17, 17) in dist
        and t5100 == 72
        and t4800 == 64
        and "absent from `B_48(0)`" in note
        and "not leftover of the `B_48(0)` times" in note,
    )
    checks.check(
        "skips-height-three-out-face",
        "c2d4 extra clause skips (3,2,0)→(4,2,0); d3, df, and ω extra clauses include it",
        (not d4_grow(*skip_hop))
        and d3_grow(*skip_hop)
        and df_grow(*skip_hop)
        and omega_grow(*skip_hop)
        and d4_grow(*later_hop)
        and d3_grow(*later_hop)
        and df_grow(*later_hop)
        and omega_grow(*later_hop)
        and c2d4_cost(*skip_hop) == 1
        and d3_cost(*skip_hop) == 3
        and df_cost(*skip_hop) == 3
        and omega_cost(*skip_hop) == 3
        and rho3_cost(*skip_hop) == 1
        and c2d4_cost(*later_hop) == 2
        and c2d4_cost(*unit_out_face) == 3
        and c2d4_cost(*height_two) == 1
        and df_cost(*height_two) == 3
        and t420 == 10
        and t320 == 9
        and path_cost(witness_skip, c2d4_cost) == 10
        and path_cost(witness_skip, d3_cost) == 12
        and "skips the height-three out-face" in note
        and "not leftover of `d3`" in note
        and "not leftover of `df`" in note,
    )
    checks.check(
        "not-leftover-of-kappa",
        "κ prices ridge-enter at 3 while c2d4 leaves it at 1",
        c2d4_cost(*ridge_enter) == 1
        and kappa_cost(*ridge_enter) == 3
        and rho3_cost(*ridge_enter) == 1
        and "not leftover of `κ`" in note,
    )
    checks.check(
        "not-leftover-of-iota",
        "c2d4 does not tax the interior 3→3 hop that ι taxes",
        c2d4_cost((3, 3, 2), (3, 3, 3)) == 1
        and iota_cost((3, 3, 2), (3, 3, 3)) == 3
        and t171717 == 55
        and t171717 != 87
        and "not leftover of `ι`" in note,
    )
    checks.check(
        "seed-and-max4-out-face-clauses",
        "seed-exit, both-weights-1, support-drop, corridor-slide, ridge-slide cost 3; max≥4 out-face costs 2; skipped height-two and height-three grow, unit-cube, and body enter cost 1",
        c2d4_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d4_cost((1, 1, 0), (1, 0, 0)) == 3
        and c2d4_cost(*unit_out_face) == 3
        and c2d4_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d4_cost((2, 2, 0), (3, 2, 0)) == 1
        and c2d4_cost((3, 2, 0), (4, 2, 0)) == 1
        and c2d4_cost((4, 2, 0), (5, 2, 0)) == 2
        and c2d4_cost((3, 2, 0), (3, 3, 0)) == 1
        and c2d4_cost((3, 3, 0), (4, 3, 0)) == 1
        and c2d4_cost((4, 3, 0), (5, 3, 0)) == 2
        and c2d4_cost((1, 0, 0), (1, 1, 0)) == 1
        and c2d4_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((2, 1, 0), (2, 1, 1)) == 1
        and c2d4_cost((2, 2, 0), (2, 2, 1)) == 1
        and c2d4_cost((1, -2, 0), (2, -2, 0)) == 1
        and c2d4_cost((2, 2, 2), (3, 2, 2)) == 1
        and c2d4_cost((2, 7, 7), (3, 7, 7)) == 1
        and c2d4_cost((16, 17, 17), (17, 17, 17)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
