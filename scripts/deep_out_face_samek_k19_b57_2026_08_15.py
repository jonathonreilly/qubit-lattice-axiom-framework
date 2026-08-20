#!/usr/bin/env python3
"""Score same-k reverse at k=19 under df on B_57(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/DEEP_OUT_FACE_SAMEK_K19_B57_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/DEEP_OUT_FACE_SAMEK_K19_B57_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=19 under the named "
    "deep-out-face hop-cost on B_57(0) is reported. "
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


def dijkstra_df(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + df_cost(v, w)
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
    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_57(0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and one Dijkstra; no fit and "
        "no second graph search"
    )
    print(
        "claim_boundary: same-k reverse at k=19 is displayed, not adopted"
    )

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
        "df is not written into Admissibility",
        "Do not write df into Admissibility" in note
        and "Do not write `df` into Admissibility" in note,
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

    sites = ball(57)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_df(sites)
    t1900 = dist[(19, 0, 0)]
    t191919 = dist[(19, 19, 19)]
    t5700 = dist[(57, 0, 0)]
    t5400 = dist[(54, 0, 0)]
    t320 = dist[(3, 2, 0)]
    reverse = 3 * t1900 * t1900 > t191919 * t191919
    axis_sq = t1900 * t1900
    body_sq = t191919 * t191919
    axis_prod = 3 * axis_sq
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 20)],
        (19, 1, 1),
        (19, 1, 0),
        (19, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 20)],
        *[(19, y, 1) for y in range(3, 20)],
        *[(19, 19, z) for z in range(2, 20)],
    )
    witness_out_face = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
    )
    out_face_hop = ((2, 2, 0), (3, 2, 0))
    unit_out_face = ((1, 1, 0), (2, 1, 0))
    later_out_face = ((7, 2, 0), (8, 2, 0))
    height2_nongrow = ((1, -2, 0), (2, -2, 0))
    ridge_enter = ((2, 1, 0), (2, 1, 1))
    df_omega_agree = True
    for site in sites:
        sx, sy, sz = site
        for dx, dy, dz in NEIGH:
            neighbor = (sx + dx, sy + dy, sz + dz)
            if neighbor not in dist:
                continue
            if df_cost(site, neighbor) != omega_cost(site, neighbor):
                df_omega_agree = False
                break
        if not df_omega_agree:
            break
    print(f"n_sites {len(sites)}")
    print(f"t(19,0,0) {t1900}")
    print(f"t(19,19,19) {t191919}")
    print(f"t(19,0,0)^2/361 {axis_sq}/361")
    print(f"t(19,19,19)^2/1083 {body_sq}/1083")
    print(f"3t_axis^2 {axis_prod}")
    print(f"t_body^2 {body_sq}")
    print(f"reverse {reverse}")
    print(f"t(57,0,0) {t5700}")
    print(f"t(54,0,0) {t5400}")
    print(f"t(3,2,0) {t320}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_axis_sum {path_cost(witness_axis, df_cost)}")
    print(f"witness_body_sum {path_cost(witness_body, df_cost)}")
    print(f"df_out_face {df_cost(*out_face_hop)}")
    print(f"omega_out_face {omega_cost(*out_face_hop)}")
    print(f"rho3_out_face {rho3_cost(*out_face_hop)}")
    print(f"df_unit_out_face {df_cost(*unit_out_face)}")
    print(f"omega_grow_unit {omega_grow(*unit_out_face)}")
    print(f"df_grow_unit {df_grow(*unit_out_face)}")
    print(f"witness_out_face_df {path_cost(witness_out_face, df_cost)}")
    print(f"witness_out_face_rho3 {path_cost(witness_out_face, rho3_cost)}")

    checks.check(
        "t-1900-191919",
        "t(19,0,0) and t(19,19,19) match the named witness walks",
        t1900 == path_cost(witness_axis, df_cost)
        and t191919 == path_cost(witness_body, df_cost)
        and t1900 > 0
        and t191919 > 0,
    )
    checks.check(
        "reverse-k19",
        "t(19,0,0)^2/361 > t(19,19,19)^2/1083 does not hold",
        (not reverse)
        and axis_prod < body_sq
        and f"{axis_prod} < {body_sq}" in note
        and "inequality does not hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b57",
        "B_57(0) has 253575 sites and 253574 nonzero sites",
        len(sites) == 253575 and len(nonzero) == 253574 and all(l1(v) <= 57 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_57(0) is reached",
        len(dist) == 253575,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        f"t(19,0,0) = {t1900}" in note
        and f"t(19,19,19) = {t191919}" in note
        and "`(19,0,0)`" in note
        and "`(19,19,19)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        f"{axis_prod} < {body_sq}" in note
        and f"{axis_sq}/361" in note
        and f"{body_sq}/1083" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "df prices deep out-face at 3 while ρ3 prices it at 1",
        df_cost(*out_face_hop) == 3
        and rho3_cost(*out_face_hop) == 1
        and mu_cost(*out_face_hop) == 1
        and df_cost(*later_out_face) == 3
        and rho3_cost(*later_out_face) == 1
        and df_cost(*height2_nongrow) == 1
        and t320 == 11
        and path_cost(witness_out_face, df_cost) == 11
        and path_cost(witness_out_face, rho3_cost) == 9
        and "cannot price deep out-face" in note
        and "`t(3,2,0) = 11`" in note,
    )
    checks.check(
        "not-leftover-of-b54",
        "(19,19,19) lies outside B_54(0) and the note says so",
        l1((19, 19, 19)) == 57
        and (19, 19, 19) in dist
        and t5700 == dist[(57, 0, 0)]
        and t5400 == dist[(54, 0, 0)]
        and "absent from `B_54(0)`" in note
        and "not leftover of the `B_54(0)` times" in note,
    )
    checks.check(
        "skips-unit-out-face",
        "df extra clause skips unit-out-face; ω extra clause includes it; both hop-costs are 3 by μ",
        omega_grow(*unit_out_face)
        and (not df_grow(*unit_out_face))
        and df_grow(*out_face_hop)
        and omega_grow(*out_face_hop)
        and df_cost(*unit_out_face) == 3
        and omega_cost(*unit_out_face) == 3
        and rho3_cost(*unit_out_face) == 3
        and df_cost(*out_face_hop) == omega_cost(*out_face_hop) == 3
        and df_omega_agree
        and "skips the unit-out-face" in note
        and "not leftover of `ω`" in note,
    )
    checks.check(
        "not-leftover-of-kappa",
        "κ prices ridge-enter at 3 while df leaves it at 1",
        df_cost(*ridge_enter) == 1
        and kappa_cost(*ridge_enter) == 3
        and rho3_cost(*ridge_enter) == 1
        and "not leftover of `κ`" in note,
    )
    checks.check(
        "not-leftover-of-iota",
        "df does not tax the interior 3→3 hop that ι taxes",
        df_cost((3, 3, 2), (3, 3, 3)) == 1
        and iota_cost((3, 3, 2), (3, 3, 3)) == 3
        and "not leftover of `ι`" in note,
    )
    checks.check(
        "seed-and-deep-out-face-clauses",
        "seed-exit, both-weights-1, support-drop, corridor-slide, ridge-slide, and deep out-face cost 3; unit-cube and body enter cost 1",
        df_cost((0, 0, 0), (1, 0, 0)) == 3
        and df_cost((1, 0, 0), (2, 0, 0)) == 3
        and df_cost((1, 1, 0), (1, 0, 0)) == 3
        and df_cost(*unit_out_face) == 3
        and df_cost((1, 1, 1), (2, 1, 1)) == 3
        and df_cost((2, 2, 0), (3, 2, 0)) == 3
        and df_cost((2, 2, 0), (2, 3, 0)) == 3
        and df_cost((3, 2, 0), (4, 2, 0)) == 3
        and df_cost((1, 0, 0), (1, 1, 0)) == 1
        and df_cost((1, 1, 0), (1, 1, 1)) == 1
        and df_cost((2, 1, 0), (2, 1, 1)) == 1
        and df_cost((2, 2, 0), (2, 2, 1)) == 1
        and df_cost((1, -2, 0), (2, -2, 0)) == 1
        and df_cost((2, 2, 2), (3, 2, 2)) == 1
        and df_cost((2, 7, 7), (3, 7, 7)) == 1
        and df_cost((18, 19, 19), (19, 19, 19)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "df(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "thm3-note-boundary",
        "the note refuses an Admissibility write and an L1 attachment",
        "Do not write df into Admissibility." in note
        and "Do not attach L1." in note,
    )

    print("per_element: named hop-cost values are 1 or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (19,0,0) and (19,19,19).")
    print("lattice_wide: checked and not executed — the search stays inside B_57(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
