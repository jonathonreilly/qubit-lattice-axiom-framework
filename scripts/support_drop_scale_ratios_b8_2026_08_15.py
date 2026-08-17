#!/usr/bin/env python3
"""Score axis and body-diagonal ν ratios on B_8(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_SCALE_RATIOS_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_SCALE_RATIOS_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Axis and body-diagonal arrival ratios under the named "
    "support-drop hop-cost on B_8(0) are reported for k=1..4. "
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


def dijkstra_nu(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + nu_cost(v, w)
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
        "Displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ν is not written into Admissibility",
        "Do not write `ν` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note,
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

    sites = ball(8)
    site_set = set(sites)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_nu(sites)

    times: dict[int, dict[str, int | None]] = {}
    for k in (1, 2, 3, 4):
        axis = (k, 0, 0)
        diag = (k, k, k)
        t_axis = dist[axis] if axis in site_set else None
        t_diag = dist[diag] if diag in site_set else None
        times[k] = {"axis": t_axis, "diag": t_diag}

    reverse: dict[int, bool | None] = {}
    axis_sq: dict[int, Fraction] = {}
    diag_sq: dict[int, Fraction | None] = {}
    for k in (1, 2, 3, 4):
        t_axis = times[k]["axis"]
        t_diag = times[k]["diag"]
        assert t_axis is not None
        axis_sq[k] = Fraction(t_axis * t_axis, k * k)
        if t_diag is None:
            diag_sq[k] = None
            reverse[k] = None
        else:
            diag_sq[k] = Fraction(t_diag * t_diag, 3 * k * k)
            reverse[k] = axis_sq[k] > diag_sq[k]

    print(f"n_sites {len(sites)}")
    for k in (1, 2, 3, 4):
        print(f"t({k},0,0) {times[k]['axis']}")
        print(f"t({k},{k},{k}) {times[k]['diag']}")
        print(f"axis_ratio_sq[{k}] {axis_sq[k]}")
        print(f"diag_ratio_sq[{k}] {diag_sq[k]}")
        print(f"reverse[{k}] {reverse[k]}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b8",
        "B_8(0) has 833 sites and 832 nonzero sites",
        len(sites) == 833 and len(nonzero) == 832 and all(l1(v) <= 8 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_8(0) is reached",
        len(dist) == 833,
    )
    checks.check(
        "axis-arrivals",
        "t(k,0,0) is 3,6,9,10 for k=1,2,3,4",
        [times[k]["axis"] for k in (1, 2, 3, 4)] == [3, 6, 9, 10],
    )
    checks.check(
        "diag-arrivals",
        "t(k,k,k) is 5,8 for k=1,2 and omitted for k=3,4",
        times[1]["diag"] == 5
        and times[2]["diag"] == 8
        and times[3]["diag"] is None
        and times[4]["diag"] is None
        and (3, 3, 3) not in site_set
        and (4, 4, 4) not in site_set,
    )
    checks.check(
        "reverse-k1",
        "t(1,0,0)^2 / 1^2 > t(1,1,1)^2 / 3",
        reverse[1] is True and axis_sq[1] == 9 and diag_sq[1] == Fraction(25, 3),
    )
    checks.check(
        "reverse-k2",
        "t(2,0,0)^2 / 4 > t(2,2,2)^2 / 12",
        reverse[2] is True and axis_sq[2] == 9 and diag_sq[2] == Fraction(16, 3),
    )
    checks.check(
        "gap-open",
        "the same-k ratio gap stays open at both available scales",
        reverse[1] is True and reverse[2] is True,
    )
    checks.check(
        "note-records-times",
        "note records the computed arrivals and omitted sites",
        "t(1,0,0) = 3" in note
        and "t(1,1,1) = 5" in note
        and "t(2,0,0) = 6" in note
        and "t(2,2,2) = 8" in note
        and "t(3,0,0) = 9" in note
        and "t(4,0,0) = 10" in note
        and "`(3,3,3)` and `(4,4,4)`" in note,
    )
    checks.check(
        "note-records-reverse",
        "note records both same-k reverse inequalities",
        "9 > 25/3" in note and "9 > 16/3" in note and "27 > 25" in note and "108 > 64" in note,
    )
    checks.check(
        "not-leftover-of-one-pair",
        "the table is not leftover of the mixed-scale pair",
        "not leftover of that one pair" in note
        and "not a substitute for this" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (1, 0, 0)) == 3
        and nu_cost((1, 0, 0), (2, 0, 0)) == 3
        and nu_cost((1, 0, 0), (1, 1, 0)) == 1
        and nu_cost((1, 1, 0), (1, 1, 1)) == 1
        and nu_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
