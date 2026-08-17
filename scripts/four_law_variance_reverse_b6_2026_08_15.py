#!/usr/bin/env python3
"""Score ρ, α, ν, and ℓ¹ on the same B_6(0) sites.

Four origin Dijkstras. ℓ¹ hops cost 1, so t_ℓ¹(v) = |v|_1.
No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
import math
from collections.abc import Callable
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/FOUR_LAW_VARIANCE_REVERSE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/FOUR_LAW_VARIANCE_REVERSE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "On B_6(0), ρ, α, ν, and ℓ¹ are scored for diamond reverse "
    "and for var(|v|_2/t). Displayed, not adopted."
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
CostFn = Callable[[tuple[int, int, int], tuple[int, int, int]], int]


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
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or sigma_v == sigma_w:
        return 3
    return 1


def alpha_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1):
        return 3
    return 1


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def l1_cost(_v: tuple[int, int, int], _w: tuple[int, int, int]) -> int:
    return 1


def dijkstra(
    sites: list[tuple[int, int, int]], cost: CostFn
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
            nd = d + cost(v, w)
            if nd < dist.get(w, 10**9):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist


def population_variance(values: list[float]) -> float:
    n = len(values)
    mean = math.fsum(values) / n
    return math.fsum((x - mean) ** 2 for x in values) / n


def fmt_var(value: float) -> str:
    return f"{value:.14f}"


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
        "note claim_scope matches the displayed four-law scoring statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the four laws are displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "no law is written into Admissibility",
        "not written into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "no displayed law is attached to L1",
        "not attached to L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "not-leftover",
        "the scores are joint on the same 376 sites, not leftover of one-law scores",
        "not leftover of one-law scores" in note,
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

    sites = ball(6)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    laws: list[tuple[str, CostFn]] = [
        ("rho", rho_cost),
        ("alpha", alpha_cost),
        ("nu", nu_cost),
        ("l1", l1_cost),
    ]
    arrivals: dict[str, dict[tuple[int, int, int], int]] = {}
    times: dict[str, tuple[int, int]] = {}
    reverses: dict[str, bool] = {}
    variances: dict[str, float] = {}
    for name, cost in laws:
        dist = dijkstra(sites, cost)
        arrivals[name] = dist
        t_axis = dist[(4, 0, 0)]
        t_diag = dist[(2, 2, 2)]
        times[name] = (t_axis, t_diag)
        reverses[name] = 12 * t_axis * t_axis > 16 * t_diag * t_diag
        variances[name] = population_variance([l2(v) / dist[v] for v in nonzero])

    print(f"n_sites {len(sites)}")
    print(f"n_nonzero {len(nonzero)}")
    for name in ("rho", "alpha", "nu", "l1"):
        t_axis, t_diag = times[name]
        print(
            f"{name} t(4,0,0) {t_axis} t(2,2,2) {t_diag} "
            f"12 t_axis^2 {12 * t_axis * t_axis} "
            f"16 t_diag^2 {16 * t_diag * t_diag} "
            f"reverse {reverses[name]} var {fmt_var(variances[name])}"
        )
    order = sorted(variances, key=lambda name: variances[name])
    print("var_order " + " < ".join(order))
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "four-dijkstras",
        "exactly four Dijkstras ran, one per named law",
        DIJKSTRA_CALLS == 4,
    )
    checks.check(
        "ball-b6",
        "B_6(0) has 377 sites and 376 nonzero sites",
        len(sites) == 377 and len(nonzero) == 376 and all(l1(v) <= 6 for v in sites),
    )
    checks.check(
        "same-376-sites",
        "every law is scored on the same 376 nonzero sites",
        all(len(arrivals[name]) == 377 for name in arrivals)
        and all(arrivals[name][v] > 0 for name in arrivals for v in nonzero),
    )
    checks.check(
        "l1-is-norm",
        "ℓ¹ Dijkstra arrivals equal |v|_1",
        all(arrivals["l1"][v] == l1(v) for v in sites),
    )
    checks.check(
        "rho-times",
        "ρ arrivals are t(4,0,0)=12 and t(2,2,2)=14",
        times["rho"] == (12, 14),
    )
    checks.check(
        "alpha-times",
        "α arrivals are t(4,0,0)=8 and t(2,2,2)=8",
        times["alpha"] == (8, 8),
    )
    checks.check(
        "nu-times",
        "ν arrivals are t(4,0,0)=10 and t(2,2,2)=8",
        times["nu"] == (10, 8),
    )
    checks.check(
        "l1-times",
        "ℓ¹ arrivals are t(4,0,0)=4 and t(2,2,2)=6",
        times["l1"] == (4, 6),
    )
    checks.check(
        "reverse-bits",
        "only ν reverses 12 t_axis^2 > 16 t_diag^2",
        reverses == {"rho": False, "alpha": False, "nu": True, "l1": False},
    )
    checks.check(
        "note-records-times",
        "note records all four (4,0,0) and (2,2,2) arrivals and reverse bits",
        "t_ρ(4,0,0) = 12" in note
        and "t_ρ(2,2,2) = 14" in note
        and "t_α(4,0,0) = 8" in note
        and "t_α(2,2,2) = 8" in note
        and "t_ν(4,0,0) = 10" in note
        and "t_ν(2,2,2) = 8" in note
        and "t_ℓ¹(4,0,0) = 4" in note
        and "t_ℓ¹(2,2,2) = 6" in note
        and "only ν reverses" in note,
    )
    var_strings = {name: fmt_var(variances[name]) for name in variances}
    checks.check(
        "note-records-variances",
        "note records all four population variances and the order",
        var_strings["rho"] in note
        and var_strings["alpha"] in note
        and var_strings["nu"] in note
        and var_strings["l1"] in note
        and "var_ρ < var_α < var_ν < var_ℓ¹" in note,
    )
    checks.check(
        "var-order",
        "computed variance order is ρ < α < ν < ℓ¹",
        order == ["rho", "alpha", "nu", "l1"]
        and variances["rho"] < variances["alpha"] < variances["nu"] < variances["l1"],
    )
    checks.check(
        "nu-beats-l1",
        "ν reverses and has variance strictly below ℓ¹",
        reverses["nu"] and variances["nu"] < variances["l1"],
    )
    checks.check(
        "rho-rounder-no-reverse",
        "ρ has the smallest variance and does not reverse",
        not reverses["rho"] and order[0] == "rho",
    )
    checks.check(
        "named-clauses",
        "ρ, α, and ν clauses match the displayed algebra on seed, axis, and drop hops",
        rho_cost((0, 0, 0), (1, 0, 0)) == 3
        and rho_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho_cost((1, 0, 0), (1, 1, 0)) == 1
        and alpha_cost((0, 0, 0), (1, 0, 0)) == 3
        and alpha_cost((1, 0, 0), (2, 0, 0)) == 3
        and alpha_cost((1, 1, 0), (2, 1, 0)) == 1
        and nu_cost((1, 1, 0), (1, 0, 0)) == 3
        and alpha_cost((1, 1, 0), (1, 0, 0)) == 1
        and l1_cost((1, 1, 0), (1, 0, 0)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom
        and "ρ(v→w)" not in axiom
        and "α(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
