#!/usr/bin/env python3
"""Score face reverse versus k under s2 on B_16(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/C2D4_SOFT_RIDGE_COST2_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/C2D4_SOFT_RIDGE_COST2_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Face reverse under the named c2d4-plus-soft-ridge hop-cost on B_16(0) "
    "at k=1..8 is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
SCALES = (1, 2, 3, 4, 5, 6, 7, 8)
EXPECTED_AXIS = {
    1: 6,
    2: 12,
    3: 18,
    4: 22,
    5: 24,
    6: 26,
    7: 29,
    8: 35,
}
EXPECTED_FACE = {
    1: 4,
    2: 8,
    3: 10,
    4: 12,
    5: 15,
    6: 18,
    7: 21,
    8: 23,
}
EXPECTED_REVERSE = {
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: False,
    8: True,
}
UNIT_OUT_SRC = (1, 1, 0)
UNIT_OUT_DST = (2, 1, 0)
EARLY_OUT_SRC = (2, 2, 0)
EARLY_OUT_DST = (3, 2, 0)
SKIP3_OUT_SRC = (3, 2, 0)
SKIP3_OUT_DST = (4, 2, 0)
MAX4_OUT_SRC = (4, 2, 0)
MAX4_OUT_DST = (5, 2, 0)
INTERIOR_SRC = (2, 2, 2)
INTERIOR_DST = (3, 2, 2)
RIDGE_SRC = (1, 1, 1)
RIDGE_DST = (2, 1, 1)
INTERIOR_DROP_SRC = (2, 2, 2)
INTERIOR_DROP_DST = (2, 2, 1)
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


def c2d4_extra(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    if support_size(v) != 2 or support_size(w) != 2:
        return False
    return max(abs(coord) for coord in w) > max(abs(coord) for coord in v) and max(
        abs(coord) for coord in v
    ) >= 4


def c2d4_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if c2d4_extra(v, w):
        return 2
    return 1


def s2_ridge(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    if support_size(v) != 3 or support_size(w) != 3:
        return False
    return sum(abs(coord) == 1 for coord in w) == 2


def s2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if s2_ridge(v, w) or c2d4_extra(v, w):
        return 2
    return 1


def dijkstra_s2(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + s2_cost(v, w)
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


def axis_site(k: int) -> tuple[int, int, int]:
    return (2 * k, 0, 0)


def face_site(k: int) -> tuple[int, int, int]:
    return (k, k, 0)


def available(k: int, radius: int) -> bool:
    return l1(axis_site(k)) <= radius and l1(face_site(k)) <= radius


def is_reverse(t_axis: int, t_face: int) -> bool:
    return t_axis * t_axis > 2 * t_face * t_face


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
        "s2 is not written into Admissibility",
        "Do not write `s2` into Admissibility" in note,
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

    sites = ball(16)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    available_ks = [k for k in SCALES if available(k, 16)]
    dist = dijkstra_s2(sites)
    print(f"n_sites {len(sites)}")
    print(f"available_k {available_ks}")
    bits: dict[int, bool] = {}
    for k in available_ks:
        axis = axis_site(k)
        face = face_site(k)
        t_axis = dist[axis]
        t_face = dist[face]
        bit = is_reverse(t_axis, t_face)
        bits[k] = bit
        print(
            f"k={k} t{axis}={t_axis} t{face}={t_face} "
            f"axis_dens {t_axis * t_axis}/{4 * k * k} "
            f"face_dens {t_face * t_face}/{2 * k * k} "
            f"cmp {t_axis * t_axis} ? {2 * t_face * t_face} reverse {bit}"
        )
    pattern = ",".join("yes" if bits[k] else "no" for k in available_ks)
    print(f"hold_fail_pattern {pattern}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"s2_ridge {s2_cost(RIDGE_SRC, RIDGE_DST)}")
    print(f"c2d4_ridge {c2d4_cost(RIDGE_SRC, RIDGE_DST)}")
    print(f"rho3_ridge {rho3_cost(RIDGE_SRC, RIDGE_DST)}")
    print(f"mu_ridge {mu_cost(RIDGE_SRC, RIDGE_DST)}")
    print(f"s2_ridge_extra {s2_ridge(RIDGE_SRC, RIDGE_DST)}")
    print(f"s2_interior {s2_cost(INTERIOR_SRC, INTERIOR_DST)}")
    print(f"c2d4_interior {c2d4_cost(INTERIOR_SRC, INTERIOR_DST)}")
    print(f"rho3_interior {rho3_cost(INTERIOR_SRC, INTERIOR_DST)}")
    print(f"s2_ridge_interior {s2_ridge(INTERIOR_SRC, INTERIOR_DST)}")
    print(f"s2_interior_drop {s2_cost(INTERIOR_DROP_SRC, INTERIOR_DROP_DST)}")
    print(f"s2_ridge_interior_drop {s2_ridge(INTERIOR_DROP_SRC, INTERIOR_DROP_DST)}")
    print(f"s2_max4_out {s2_cost(MAX4_OUT_SRC, MAX4_OUT_DST)}")
    print(f"c2d4_max4_out {c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)}")
    print(f"s2_skip3_out {s2_cost(SKIP3_OUT_SRC, SKIP3_OUT_DST)}")
    print(f"s2_early_out {s2_cost(EARLY_OUT_SRC, EARLY_OUT_DST)}")
    print(f"s2_unit_out {s2_cost(UNIT_OUT_SRC, UNIT_OUT_DST)}")

    times_ok = all(
        dist[axis_site(k)] == EXPECTED_AXIS[k] and dist[face_site(k)] == EXPECTED_FACE[k]
        for k in available_ks
    )
    checks.check(
        "theorem-1",
        "computed arrivals match the displayed B_16(0) table",
        times_ok
        and all(f"`t({2 * k},0,0) = {EXPECTED_AXIS[k]}`" in note for k in SCALES)
        and all(f"`t({k},{k},0) = {EXPECTED_FACE[k]}`" in note for k in SCALES),
    )
    checks.check(
        "reverse-bits",
        "displayed reverse bits match t(2k,0,0)^2 > 2 t(k,k,0)^2",
        bits == {k: EXPECTED_REVERSE[k] for k in available_ks}
        and "36 > 32" in note
        and "144 > 128" in note
        and "324 > 200" in note
        and "484 > 288" in note
        and "576 > 450" in note
        and "676 > 648" in note
        and "841 > 882" in note
        and "1225 > 1058" in note,
    )
    checks.check(
        "hold-fail-pattern",
        "the eight bits are yes,yes,yes,yes,yes,yes,no,yes",
        bits == {k: EXPECTED_REVERSE[k] for k in available_ks}
        and "yes, yes, yes, yes, yes, yes, no, yes" in note
        and "fails at `k=7`" in note
        and "holds at `k=1..6` and `k=8`" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b16",
        "B_16(0) has 6017 sites and 6016 nonzero sites",
        len(sites) == 6017 and len(nonzero) == 6016 and all(l1(v) <= 16 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_16(0) is reached",
        len(dist) == 6017,
    )
    checks.check(
        "available-k-1-8",
        "every k=1..8 pair lies in B_16(0); none omitted",
        available_ks == list(SCALES)
        and all(axis_site(k) in dist and face_site(k) in dist for k in SCALES)
        and "No scale is omitted" in note,
    )
    site_set = set(sites)
    ridge_live = (
        RIDGE_SRC in site_set
        and RIDGE_DST in site_set
        and s2_cost(RIDGE_SRC, RIDGE_DST) == 2
        and c2d4_cost(RIDGE_SRC, RIDGE_DST) == 3
        and rho3_cost(RIDGE_SRC, RIDGE_DST) == 3
        and mu_cost(RIDGE_SRC, RIDGE_DST) == 1
        and s2_ridge(RIDGE_SRC, RIDGE_DST)
        and support_size(RIDGE_SRC) == 3
        and support_size(RIDGE_DST) == 3
        and sum(abs(c) == 1 for c in RIDGE_DST) == 2
    )
    checks.check(
        "soft-ridge-hop",
        "the named ridge-stay 3->3 hop (1,1,1)->(2,1,1) has s2=2 and rho3=3",
        ridge_live and "(1,1,1) → (2,1,1)" in note,
    )
    interior_idle = (
        INTERIOR_SRC in site_set
        and INTERIOR_DST in site_set
        and s2_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and c2d4_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and rho3_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and not s2_ridge(INTERIOR_SRC, INTERIOR_DST)
        and support_size(INTERIOR_SRC) == 3
        and support_size(INTERIOR_DST) == 3
        and min(abs(c) for c in INTERIOR_DST) >= 2
    )
    checks.check(
        "interior-body-idle",
        "3->3 (2,2,2)->(3,2,2) is idle for the soft-ridge clause",
        interior_idle and "(2,2,2) → (3,2,2)" in note,
    )
    interior_drop = (
        INTERIOR_DROP_SRC in site_set
        and INTERIOR_DROP_DST in site_set
        and not s2_ridge(INTERIOR_DROP_SRC, INTERIOR_DROP_DST)
        and s2_cost(INTERIOR_DROP_SRC, INTERIOR_DROP_DST) == 1
        and rho3_cost(INTERIOR_DROP_SRC, INTERIOR_DROP_DST) == 1
        and sum(abs(c) == 1 for c in INTERIOR_DROP_DST) == 1
        and support_size(INTERIOR_DROP_SRC) == 3
        and support_size(INTERIOR_DROP_DST) == 3
    )
    checks.check(
        "interior-dest-one-unit-idle",
        "3->3 (2,2,2)->(2,2,1) is idle for the soft-ridge clause",
        interior_drop and "(2,2,2) → (2,2,1)" in note,
    )
    extra_live = (
        MAX4_OUT_SRC in site_set
        and MAX4_OUT_DST in site_set
        and s2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and c2d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and not s2_ridge(MAX4_OUT_SRC, MAX4_OUT_DST)
    )
    checks.check(
        "max4-out-face-hop",
        "the inherited max>=4 out-face hop (4,2,0)->(5,2,0) has s2=2",
        extra_live and "(4,2,0) → (5,2,0)" in note,
    )
    skip3 = (
        SKIP3_OUT_SRC in site_set
        and SKIP3_OUT_DST in site_set
        and not c2d4_extra(SKIP3_OUT_SRC, SKIP3_OUT_DST)
        and s2_cost(SKIP3_OUT_SRC, SKIP3_OUT_DST) == 1
        and max(abs(c) for c in SKIP3_OUT_SRC) == 3
    )
    checks.check(
        "source-max-3-skipped",
        "out-face (3,2,0)->(4,2,0) is skipped by the inherited extra clause",
        skip3 and "(3,2,0) → (4,2,0)" in note and "source max" in note,
    )
    early_skip = (
        EARLY_OUT_SRC in site_set
        and EARLY_OUT_DST in site_set
        and not c2d4_extra(EARLY_OUT_SRC, EARLY_OUT_DST)
        and s2_cost(EARLY_OUT_SRC, EARLY_OUT_DST) == 1
        and max(abs(c) for c in EARLY_OUT_SRC) == 2
    )
    checks.check(
        "early-out-face-skipped",
        "early-out-face (2,2,0)->(3,2,0) is skipped by the inherited extra clause",
        early_skip and "(2,2,0) → (3,2,0)" in note,
    )
    unit_skip = (
        UNIT_OUT_SRC in site_set
        and UNIT_OUT_DST in site_set
        and not c2d4_extra(UNIT_OUT_SRC, UNIT_OUT_DST)
        and mu_cost(UNIT_OUT_SRC, UNIT_OUT_DST) == 3
        and s2_cost(UNIT_OUT_SRC, UNIT_OUT_DST) == 3
        and max(abs(c) for c in UNIT_OUT_SRC) == 1
    )
    checks.check(
        "unit-out-face-skipped",
        "unit-out-face (1,1,0)->(2,1,0) is skipped by the inherited extra clause",
        unit_skip and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "cost-2-not-3",
        "ridge-stay 3->3 is cost 2, not 3",
        s2_cost(RIDGE_SRC, RIDGE_DST) == 2
        and s2_cost(INTERIOR_SRC, INTERIOR_DST) == 1
        and s2_cost(INTERIOR_DROP_SRC, INTERIOR_DROP_DST) == 1
        and s2_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and "cost `2`" in note
        and "not `3`" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        s2_cost((0, 0, 0), (1, 0, 0)) == 3
        and s2_cost((1, 0, 0), (2, 0, 0)) == 3
        and s2_cost((1, 0, 0), (1, 1, 0)) == 1
        and s2_cost((1, 1, 0), (1, 1, 1)) == 1
        and s2_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "s2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
