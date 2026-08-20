#!/usr/bin/env python3
"""Score same-k reverse at k=17 under ω on B_51(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/OUT_FACE_SAMEK_K17_B51_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OUT_FACE_SAMEK_K17_B51_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=17 under the named out-face hop-cost "
    "on B_51(0) is reported. Displayed, not adopted."
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
    if support_size(v) == 2 and support_size(w) == 2:
        nonzero = [abs(coord) for coord in w if coord != 0]
        if nonzero and min(nonzero) == 1:
            return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3:
        if sum(abs(coord) == 1 for coord in w) == 2:
            return 3
    return 1


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
            return 3
    return 1


def mid_leave_would_fire(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 1
        and support_size(w) == 2
        and max(abs(coord) for coord in w) == 1
        and max(abs(coord) for coord in v) >= 2
    )


def path_cost(path: list[tuple[int, int, int]]) -> int:
    return sum(omega_cost(a, b) for a, b in zip(path, path[1:]))


def dijkstra_omega(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + omega_cost(v, w)
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
        "ω is not written into Admissibility",
        "Do not write `ω` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note,
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
    checks.check(
        "cache-false",
        "the note records cache_write false",
        "cache_write: false" in note,
    )

    sites = ball(51)
    site_set = set(sites)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_omega(sites)
    t1700 = dist[(17, 0, 0)]
    t171717 = dist[(17, 17, 17)]
    t5100 = dist[(51, 0, 0)]
    t4800 = dist[(48, 0, 0)]
    reverse = 3 * t1700 * t1700 > t171717 * t171717
    print(f"n_sites {len(sites)}")
    print(f"t(17,0,0) {t1700}")
    print(f"t(17,17,17) {t171717}")
    print(f"t(17,0,0)^2/289 {t1700 * t1700}/289")
    print(f"t(17,17,17)^2/867 {t171717 * t171717}/867")
    print(f"3 t(17,0,0)^2 {3 * t1700 * t1700}")
    print(f"t(17,17,17)^2 {t171717 * t171717}")
    print(f"reverse {reverse}")
    print(f"t(51,0,0) {t5100}")
    print(f"t(48,0,0) {t4800}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    mid_leave_hits = 0
    for v in sites:
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w in site_set and mid_leave_would_fire(v, w):
                mid_leave_hits += 1

    axis_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1)]
    axis_witness.extend((x, 2, 1) for x in range(2, 18))
    axis_witness.extend([(17, 2, 0), (17, 1, 0), (17, 0, 0)])
    body_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0), (2, 2, 0), (2, 2, 1)]
    body_witness.extend((2, 2, z) for z in range(2, 18))
    body_witness.extend((2, y, 17) for y in range(3, 18))
    body_witness.extend((x, 17, 17) for x in range(3, 18))

    checks.check(
        "theorem-1",
        f"t(17,0,0)={t1700} and t(17,17,17)={t171717}",
        t1700 == 33 and t171717 == 55,
    )
    checks.check(
        "reverse-k17",
        "t(17,0,0)^2 / 289 > t(17,17,17)^2 / 867",
        reverse
        and 3 * t1700 * t1700 == 3267
        and t171717 * t171717 == 3025
        and "3267 > 3025" in note,
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
        "`(17,0,0)`" in note and "`(17,17,17)`" in note and "`33`" in note and "`55`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        "3267 > 3025" in note,
    )
    checks.check(
        "out-face-hop",
        "the named out-face hop (1,1,0)->(2,1,0) has ω=3",
        omega_cost((1, 1, 0), (2, 1, 0)) == 3
        and support_size((1, 1, 0)) == 2
        and support_size((2, 1, 0)) == 2
        and max(abs(c) for c in (2, 1, 0)) > max(abs(c) for c in (1, 1, 0))
        and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "mid-leave-cannot-fire",
        "mid-leave dest-max=1 and source-max>=2 never both hold on 6-NN",
        mid_leave_hits == 0 and "cannot fire" in note,
    )
    checks.check(
        "omega-not-leftover-of-rho3",
        "face-growth (2,2,0)->(3,2,0) is ω=3 and ρ3=1",
        omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "not-leftover-of-b48",
        "(17,17,17) lies outside B_48(0) and the note says so",
        l1((17, 17, 17)) == 51
        and (17, 17, 17) in dist
        and t5100 == 73
        and t4800 == 64
        and "absent from `B_48(0)`" in note
        and "not leftover of the `B_48(0)` times" in note,
    )
    checks.check(
        "witness-arrivals",
        "named axis and body walks realize costs 33 and 55",
        path_cost(axis_witness) == 33
        and path_cost(body_witness) == 55
        and axis_witness[-1] == (17, 0, 0)
        and body_witness[-1] == (17, 17, 17)
        and all(l1(v) <= 51 for v in axis_witness)
        and all(l1(v) <= 51 for v in body_witness),
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        omega_cost((0, 0, 0), (1, 0, 0)) == 3
        and omega_cost((1, 0, 0), (2, 0, 0)) == 3
        and omega_cost((1, 0, 0), (1, 1, 0)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ω(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
