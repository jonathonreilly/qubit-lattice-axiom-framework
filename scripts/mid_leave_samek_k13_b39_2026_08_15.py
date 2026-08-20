#!/usr/bin/env python3
"""Score same-k reverse at k=13 under μλ on B_39(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/MID_LEAVE_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/MID_LEAVE_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=13 under the named mid-leave "
    "hop-cost on B_39(0) is reported. Displayed, not adopted."
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
        nonzero_abs = [abs(coord) for coord in w if coord != 0]
        if nonzero_abs and min(nonzero_abs) == 1:
            return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3:
        abs_w = (abs(w[0]), abs(w[1]), abs(w[2]))
        if sum(1 for value in abs_w if value == 1) == 2:
            return 3
    return 1


def mu_lambda_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if (
        support_size(v) == 1
        and support_size(w) == 2
        and max(abs(coord) for coord in w) == 1
        and max(abs(coord) for coord in v) >= 2
    ):
        return 3
    return 1


def path_cost(path: list[tuple[int, int, int]]) -> int:
    return sum(mu_lambda_cost(path[i], path[i + 1]) for i in range(len(path) - 1))


def dijkstra_mu_lambda(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
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
            nd = d + mu_lambda_cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def extra_clause_fires(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 1
        and support_size(w) == 2
        and max(abs(coord) for coord in w) == 1
        and max(abs(coord) for coord in v) >= 2
    )


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
        "μλ is not written into Admissibility",
        "Do not write μλ into Admissibility." in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1." in note and "Do not attach L1." not in axiom,
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

    sites = ball(39)
    dist = dijkstra_mu_lambda(sites)
    t1300 = dist[(13, 0, 0)]
    t131313 = dist[(13, 13, 13)]
    reverse = 3 * t1300 * t1300 > t131313 * t131313
    axis_witness = (
        [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0)]
        + [(x, 2, 0) for x in range(3, 14)]
        + [(13, 1, 0), (13, 0, 0)]
    )
    body_witness = (
        [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0)]
        + [(x, 2, 0) for x in range(3, 14)]
        + [(13, y, 0) for y in range(3, 14)]
        + [(13, 13, z) for z in range(1, 14)]
    )
    extra_live = False
    for v in sites:
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if extra_clause_fires(v, w):
                extra_live = True
                break
        if extra_live:
            break
    print(f"n_sites {len(sites)}")
    print(f"t(13,0,0) {t1300}")
    print(f"t(13,13,13) {t131313}")
    print(f"t(13,0,0)^2/169 {t1300 * t1300}/169")
    print(f"t(13,13,13)^2/507 {t131313 * t131313}/507")
    print(f"3t_axis^2 {3 * t1300 * t1300}")
    print(f"t_body^2 {t131313 * t131313}")
    print(f"reverse {reverse}")
    print(f"extra_clause_nn {extra_live}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "t-1300-131313",
        "t(13,0,0) and t(13,13,13) match the witness walks",
        t1300 == path_cost(axis_witness) == 25
        and t131313 == path_cost(body_witness) == 43,
    )
    checks.check(
        "reverse-k13",
        "t(13,0,0)^2/169 > t(13,13,13)^2/507 holds",
        reverse
        and 3 * t1300 * t1300 == 1875
        and t131313 * t131313 == 1849
        and "1875 > 1849" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b39",
        "B_39(0) has 82239 sites and contains the same-k pair",
        len(sites) == 82239
        and (13, 0, 0) in dist
        and (13, 13, 13) in dist
        and abs(13) + abs(13) + abs(13) == 39,
    )
    checks.check(
        "reachable",
        "every site of B_39(0) is reached",
        len(dist) == 82239,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "t(13,0,0) = 25" in note and "t(13,13,13) = 43" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "1875 > 1849" in note,
    )
    checks.check(
        "extra-clause-vacant-on-nn",
        "the extra mid-leave clause does not fire on nearest-neighbor hops",
        extra_live is False
        and mu_lambda_cost((2, 0, 0), (2, 1, 0)) == 1
        and rho3_cost((2, 0, 0), (2, 1, 0)) == 1
        and "does not fire on nearest-neighbor hops" in note,
    )
    checks.check(
        "unit-cube-spared",
        "the unit-cube 1→2 hop stays cost 1 because source max is 1",
        mu_lambda_cost((1, 0, 0), (1, 1, 0)) == 1
        and extra_clause_fires((1, 0, 0), (1, 1, 0)) is False
        and "spares the unit-cube" in note,
    )
    checks.check(
        "seed-and-stacked-clauses",
        "seed-exit, both-weights-1, corridor-slide, and ridge-slide cost 3",
        mu_lambda_cost((0, 0, 0), (1, 0, 0)) == 3
        and mu_lambda_cost((1, 0, 0), (2, 0, 0)) == 3
        and mu_lambda_cost((1, 1, 0), (1, 0, 0)) == 3
        and mu_lambda_cost((1, 1, 1), (2, 1, 1)) == 3
        and mu_lambda_cost((2, 1, 0), (2, 2, 0)) == 1
        and mu_lambda_cost((13, 13, 0), (13, 13, 1)) == 1
        and mu_lambda_cost((2, 2, 2), (3, 2, 2)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "μλ(v→w)" not in axiom
        and "mid-leave" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
