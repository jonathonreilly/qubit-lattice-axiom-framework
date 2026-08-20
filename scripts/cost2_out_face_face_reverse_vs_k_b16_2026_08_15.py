#!/usr/bin/env python3
"""Score face reverse versus k under w2 on B_16(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST2_OUT_FACE_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_OUT_FACE_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Face reverse under the named cost-2 out-face hop-cost on B_16(0) "
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
    4: 24,
    5: 26,
    6: 28,
    7: 31,
    8: 37,
}
EXPECTED_FACE = {
    1: 4,
    2: 8,
    3: 11,
    4: 14,
    5: 17,
    6: 20,
    7: 22,
    8: 24,
}
EXPECTED_REVERSE = {
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: False,
    7: False,
    8: True,
}
OUT_FACE_SRC = (2, 2, 0)
OUT_FACE_DST = (3, 2, 0)
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


def w2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
            return 2
    return 1


def dijkstra_w2(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + w2_cost(v, w)
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
        "w2 is not written into Admissibility",
        "Do not write `w2` into Admissibility" in note,
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
    dist = dijkstra_w2(sites)
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
    print(f"w2_out_face {w2_cost(OUT_FACE_SRC, OUT_FACE_DST)}")
    print(f"rho3_out_face {rho3_cost(OUT_FACE_SRC, OUT_FACE_DST)}")

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
        and "324 > 242" in note
        and "576 > 392" in note
        and "676 > 578" in note
        and "784 > 800" in note
        and "961 > 968" in note
        and "1369 > 1152" in note,
    )
    checks.check(
        "hold-fail-pattern",
        "the eight bits are yes,yes,yes,yes,yes,no,no,yes",
        bits == {k: EXPECTED_REVERSE[k] for k in available_ks}
        and "yes, yes, yes, yes, yes, no, no, yes" in note
        and "fails at `k=6` and `k=7`" in note
        and "holds at `k=1..5` and `k=8`" in note,
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
    extra_live = (
        OUT_FACE_SRC in site_set
        and OUT_FACE_DST in site_set
        and w2_cost(OUT_FACE_SRC, OUT_FACE_DST) == 2
        and rho3_cost(OUT_FACE_SRC, OUT_FACE_DST) == 1
        and support_size(OUT_FACE_SRC) == 2
        and support_size(OUT_FACE_DST) == 2
        and max(abs(c) for c in OUT_FACE_DST) > max(abs(c) for c in OUT_FACE_SRC)
    )
    checks.check(
        "out-face-hop",
        "the named out-face hop (2,2,0)->(3,2,0) has w2=2",
        extra_live and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "cost-2-not-3",
        "face-growth is cost 2, not 3",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and w2_cost((1, 1, 0), (2, 1, 0)) == 3
        and "cost `2`" in note
        and "not `3`" in note,
    )
    checks.check(
        "w2-not-leftover-of-rho3",
        "face-growth (2,2,0)->(3,2,0) is w2=2 and ρ3=1",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        w2_cost((0, 0, 0), (1, 0, 0)) == 3
        and w2_cost((1, 0, 0), (2, 0, 0)) == 3
        and w2_cost((1, 0, 0), (1, 1, 0)) == 1
        and w2_cost((1, 1, 0), (1, 1, 1)) == 1
        and w2_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "w2(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
