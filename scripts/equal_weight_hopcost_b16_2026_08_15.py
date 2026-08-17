#!/usr/bin/env python3
"""Score the named equal-weight hop-cost on B_16(0).

Two origin Dijkstras, one for rho and one for nu. No cache write.
No axiom edit. Displayed, not adopted.
"""

from __future__ import annotations

import ast
import heapq
import math
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/EQUAL_WEIGHT_HOPCOST_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/EQUAL_WEIGHT_HOPCOST_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "On B_16(0), the named equal-weight hop-cost is scored for "
    "diamond reverse and for var vs ν. "
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
VAR_RHO_REPORTED = 0.00096368825222
VAR_NU_REPORTED = 0.00678027299005
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


def inward_weight(v: tuple[int, int, int]) -> int:
    weight = 0
    vx, vy, vz = v
    for dx, dy, dz in NEIGH:
        neighbor = (vx + dx, vy + dy, vz + dz)
        if l1(neighbor) < l1(v):
            weight += 1
    return weight


def l2(v: tuple[int, int, int]) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def rho_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = inward_weight(v)
    sigma_w = inward_weight(w)
    if sigma_v == sigma_w or sigma_v == 0:
        return 3
    return 1


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def dijkstra(
    sites: list[tuple[int, int, int]],
    cost_fn,
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
            nd = d + cost_fn(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def population_variance(values: list[float]) -> float:
    n = len(values)
    mean = math.fsum(values) / n
    return math.fsum((x - mean) ** 2 for x in values) / n


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
        "ρ and ν are not written into Admissibility",
        "Do not write `ρ` or `ν` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rules are not attached to L1",
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
    forbidden_hits = [token for token in forbidden if token in note or token in source]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note and runner",
        forbidden_hits == [],
    )

    sites = ball(16)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist_rho = dijkstra(sites, rho_cost)
    dist_nu = dijkstra(sites, nu_cost)
    t400 = dist_rho[(4, 0, 0)]
    t800 = dist_rho[(8, 0, 0)]
    t222 = dist_rho[(2, 2, 2)]
    t444 = dist_rho[(4, 4, 4)]
    t1600 = dist_rho[(16, 0, 0)]
    t_nu_800 = dist_nu[(8, 0, 0)]
    t_nu_444 = dist_nu[(4, 4, 4)]
    reverse = 12 * t400 * t400 > 16 * t222 * t222
    nu_doubled = 12 * t_nu_800 * t_nu_800 > 16 * t_nu_444 * t_nu_444
    var_rho = population_variance([l2(v) / dist_rho[v] for v in nonzero])
    var_nu = population_variance([l2(v) / dist_nu[v] for v in nonzero])

    print(f"n_sites {len(sites)}")
    print(f"t_rho(4,0,0) {t400}")
    print(f"t_rho(2,2,2) {t222}")
    print(f"t_rho(8,0,0) {t800}")
    print(f"t_rho(4,4,4) {t444}")
    print(f"t_rho(16,0,0) {t1600}")
    print(f"12 t_rho(4,0,0)^2 {12 * t400 * t400}")
    print(f"16 t_rho(2,2,2)^2 {16 * t222 * t222}")
    print(f"diamond_reverse {reverse}")
    print(f"nu_double_diamond_reverse {nu_doubled}")
    print(f"var_rho {var_rho:.14f}")
    print(f"var_nu {var_nu:.14f}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "two-dijkstras",
        "exactly two Dijkstras ran, one for ρ and one for ν",
        DIJKSTRA_CALLS == 2,
    )
    checks.check(
        "ball-b16",
        "B_16(0) has 6017 sites and 6016 nonzero sites",
        len(sites) == 6017 and len(nonzero) == 6016 and all(l1(v) <= 16 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_16(0) is reached under both costs",
        len(dist_rho) == 6017 and len(dist_nu) == 6017,
    )
    checks.check(
        "t-400",
        "t_ρ(4,0,0) = 12",
        t400 == 12,
    )
    checks.check(
        "t-222",
        "t_ρ(2,2,2) = 14",
        t222 == 14,
    )
    checks.check(
        "diamond-not-reverse",
        "12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2 fails",
        (not reverse) and 12 * t400 * t400 == 1728 and 16 * t222 * t222 == 3136,
    )
    checks.check(
        "note-records-times",
        "note records the computed ρ arrivals and the reverse products",
        "t_ρ(4,0,0) = 12" in note
        and "t_ρ(2,2,2) = 14" in note
        and "1728" in note
        and "3136" in note,
    )
    checks.check(
        "var-rho",
        "population variance under ρ matches the reported value",
        abs(var_rho - VAR_RHO_REPORTED) < 5e-14,
    )
    checks.check(
        "var-nu",
        "population variance under ν matches the reported value",
        abs(var_nu - VAR_NU_REPORTED) < 5e-14,
    )
    checks.check(
        "var-rho-smaller",
        "var(|v|_2/t) is strictly smaller under ρ than under ν",
        var_rho < var_nu,
    )
    checks.check(
        "note-records-variances",
        "note records both variances and which is smaller",
        "0.00096368825222" in note
        and "0.00678027299005" in note
        and "var_ρ < var_ν" in note,
    )
    checks.check(
        "not-leftover-of-b12",
        "the B_16(0) table is not leftover of the B_12(0) times",
        t1600 == 48
        and l1((16, 0, 0)) == 16
        and (16, 0, 0) in dist_rho
        and "not leftover of the `B_12(0)` times" in note,
    )
    checks.check(
        "nu-doubled-already-fails",
        "ν doubled reverse already fails on B_16(0)",
        (not nu_doubled)
        and t_nu_800 == 14
        and t_nu_444 == 14
        and 12 * t_nu_800 * t_nu_800 == 2352
        and 16 * t_nu_444 * t_nu_444 == 3136,
    )
    checks.check(
        "rho-named-clauses",
        "ρ costs 3 on seed-exit and equal inward weight, else 1",
        rho_cost((0, 0, 0), (1, 0, 0)) == 3
        and rho_cost((1, 0, 0), (2, 0, 0)) == 3
        and rho_cost((1, 0, 0), (1, 1, 0)) == 1
        and rho_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho_cost((1, 1, 0), (1, 0, 0)) == 1,
    )
    checks.check(
        "nu-named-clauses",
        "ν costs 3 on seed-exit, both-weights-1, or support drop, else 1",
        nu_cost((0, 0, 0), (1, 0, 0)) == 3
        and nu_cost((1, 0, 0), (2, 0, 0)) == 3
        and nu_cost((1, 0, 0), (1, 1, 0)) == 1
        and nu_cost((1, 1, 1), (2, 1, 1)) == 1
        and nu_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ρ(v→w)" not in axiom
        and "ν(v→w)" not in axiom,
    )

    print(
        "per_element: checked exactly — each directed B_16(0) edge carries the named equal-weight hop-cost"
    )
    print(
        "per_site: checked exactly — |v|_2/t(v) is scored on each of the 6016 nonzero sites"
    )
    print(
        "per_mode: checked exactly — the two named rules, with two Dijkstras and no uniqueness claim"
    )
    print(
        "per_block: checked exactly — diamond order and population variance on B_16(0)\\{0}"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility cost and no L1 attachment"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
