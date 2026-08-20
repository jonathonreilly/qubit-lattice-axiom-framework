#!/usr/bin/env python3
"""Exact B_12(0) arrival-speed variance of unit ℓ¹ lock-support versus c2d4.

Two Dijkstras from the origin on the finite nearest-neighbor graph: first
unit ℓ¹ cost on every 6-NN hop, then named c2d4. Variances are displayed,
not adopted. Hop-costs are not written into Admissibility. L1 is not
attached. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/L1_LOCKSUPPORT_VS_C2D4_VAR_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/L1_LOCKSUPPORT_VS_C2D4_VAR_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Arrival-speed variance on B_12(0) under unit ℓ¹ versus named "
    "c2d4 is compared. Displayed, not adopted."
)

RADIUS = 12
ORIGIN = (0, 0, 0)
SHIFTS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
NONZERO_COUNT = 2624
SITE_COUNT = 2625
DIJKSTRA_CALLS = 0

Q_L1 = Fraction(337, 656)
Q_C2D4 = Fraction(12586016761121881939, 63482497589871360000)
VAR_DIGITS = {
    "l1": "0.009447425719061308",
    "c2d4": "0.003574941366936777",
}


Point = tuple[int, int, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def l1_norm(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def radius_squared(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def support_size(point: Point) -> int:
    return int(point[0] != 0) + int(point[1] != 0) + int(point[2] != 0)


def least_nonzero_abs(point: Point) -> int | None:
    nonzero = [abs(coord) for coord in point if coord != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_abs_count(point: Point) -> int:
    return int(abs(point[0]) == 1) + int(abs(point[1]) == 1) + int(abs(point[2]) == 1)


def max_abs_coord(point: Point) -> int:
    return max(abs(point[0]), abs(point[1]), abs(point[2]))


def ball_sites(radius: int) -> tuple[Point, ...]:
    extent = range(-radius, radius + 1)
    return tuple(point for point in product(extent, repeat=3) if l1_norm(point) <= radius)


def split_square(value: int) -> tuple[int, int]:
    square = 1
    square_free = 1
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            square *= prime ** (exponent // 2)
            if exponent % 2:
                square_free *= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        square_free *= remaining
    return square, square_free


def nu_cost(source: Point, target: Point) -> int:
    sigma_v = support_size(source)
    sigma_w = support_size(target)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(source: Point, target: Point) -> int:
    if nu_cost(source, target) == 3:
        return 3
    if support_size(source) == 2 and support_size(target) == 2 and least_nonzero_abs(target) == 1:
        return 3
    return 1


def rho3_cost(source: Point, target: Point) -> int:
    if mu_cost(source, target) == 3:
        return 3
    if support_size(source) == 3 and support_size(target) == 3 and unit_abs_count(target) == 2:
        return 3
    return 1


def l1_cost(_source: Point, _target: Point) -> int:
    return 1


def c2d4_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if (
        support_size(source) == 2
        and support_size(target) == 2
        and max_abs_coord(target) > max_abs_coord(source)
        and max_abs_coord(source) >= 4
    ):
        return 2
    return 1


def neighbors(site: Point, sites: set[Point]) -> tuple[Point, ...]:
    out: list[Point] = []
    for shift in SHIFTS:
        candidate = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        if candidate in sites:
            out.append(candidate)
    return tuple(out)


def dijkstra(sites: tuple[Point, ...], cost_fn) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist = {ORIGIN: 0}
    heap: list[tuple[int, Point]] = [(0, ORIGIN)]
    while heap:
        current, site = heappop(heap)
        if current != dist[site]:
            continue
        for nxt in neighbors(site, site_set):
            trial = current + cost_fn(site, nxt)
            prior = dist.get(nxt)
            if prior is None or trial < prior:
                dist[nxt] = trial
                heappush(heap, (trial, nxt))
    return dist


def second_moment_and_var_coeff(
    dist: dict[Point, int], sites: tuple[Point, ...]
) -> tuple[Fraction, dict[int, Fraction]]:
    nonzero = tuple(site for site in sites if site != ORIGIN)
    count = len(nonzero)
    moment = Fraction(0)
    linear: dict[int, Fraction] = defaultdict(Fraction)
    for site in nonzero:
        arrival = dist[site]
        squared = radius_squared(site)
        moment += Fraction(squared, arrival * arrival)
        square, square_free = split_square(squared)
        linear[square_free] += Fraction(square, arrival)
    moment /= count
    square_coeff: dict[int, Fraction] = defaultdict(Fraction)
    keys = tuple(linear)
    for left in keys:
        for right in keys:
            square, square_free = split_square(left * right)
            square_coeff[square_free] += linear[left] * linear[right] * square
    var_coeff: dict[int, Fraction] = defaultdict(Fraction)
    var_coeff[1] += moment
    denom = count * count
    for square_free, coeff in square_coeff.items():
        var_coeff[square_free] -= coeff / denom
    return moment, {key: value for key, value in var_coeff.items() if value != 0}


def eval_coeff(coeff: dict[int, Fraction], precision: int = 50) -> Decimal:
    getcontext().prec = precision
    total = Decimal(0)
    for square_free, value in coeff.items():
        total += (Decimal(value.numerator) / Decimal(value.denominator)) * Decimal(square_free).sqrt()
    return total


def truncated_decimal(value: Decimal, places: int = 18) -> str:
    quantized = value.quantize(Decimal(10) ** -places)
    text = format(quantized, "f")
    whole, frac = text.split(".")
    return whole + "." + frac[:places]


def parse_audit_tuple(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.Assign):
            names = [target.id for target in node.targets if isinstance(target, ast.Name)]
            if "AUDIT_INPUT_PATHS" in names and isinstance(node.value, ast.Tuple):
                values: list[str] = []
                for element in node.value.elts:
                    if not isinstance(element, ast.Constant) or not isinstance(element.value, str):
                        return None
                    values.append(element.value)
                return tuple(values)
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(f"claim_scope: {CLAIM_SCOPE}")
    print("cache_write: false")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observation or fit")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: two directed Dijkstras on the induced B_12(0) graph, unit ℓ¹ then c2d4")
    print("negative_scope: displayed scores are not adopted and L1 is not attached")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-tuple-literal",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        parse_audit_tuple(self_source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "front matter uses the declared claim_scope",
        f'claim_scope: "{CLAIM_SCOPE}"' in note.replace("\n", " ")
        or f'claim_scope: "{CLAIM_SCOPE}"' in note,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalized_axiom and admissibility_sentence in normalized_note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )

    sites = ball_sites(RADIUS)
    site_set = set(sites)
    checks.check(
        "ball-cardinality",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites) == SITE_COUNT and ORIGIN in site_set and len(sites) - 1 == NONZERO_COUNT,
    )

    dist_l1 = dijkstra(sites, l1_cost)
    dist_c2d4 = dijkstra(sites, c2d4_cost)
    checks.check(
        "two-dijkstras",
        "exactly two Dijkstras run, unit ℓ¹ then c2d4, and each cost reaches every ball site",
        DIJKSTRA_CALLS == 2
        and "dist_l1 = dijkstra(sites, l1_cost)" in self_source
        and "dist_c2d4 = dijkstra(sites, c2d4_cost)" in self_source
        and self_source.index("dist_l1 = dijkstra(sites, l1_cost)")
        < self_source.index("dist_c2d4 = dijkstra(sites, c2d4_cost)")
        and len(dist_l1) == SITE_COUNT
        and len(dist_c2d4) == SITE_COUNT,
        residual=(DIJKSTRA_CALLS, len(dist_l1), len(dist_c2d4)),
    )
    checks.check(
        "l1-equals-norm",
        "unit ℓ¹ Dijkstra arrivals equal coordinate-sum on every site",
        all(dist_l1[site] == l1_norm(site) for site in sites),
    )
    checks.check(
        "named-clauses",
        "ℓ¹ prices every 6-NN hop at 1; c2d4 prices ρ3 at 3 and max≥4 out-face at 2",
        l1_cost((0, 0, 0), (1, 0, 0)) == 1
        and l1_cost((1, 0, 0), (2, 0, 0)) == 1
        and l1_cost((1, 0, 0), (1, 1, 0)) == 1
        and l1_cost((1, 1, 0), (1, 0, 0)) == 1
        and l1_cost((1, 1, 0), (2, 1, 0)) == 1
        and l1_cost((4, 2, 0), (5, 2, 0)) == 1
        and l1_cost((3, 2, 0), (4, 2, 0)) == 1
        and l1_cost((1, 1, 1), (2, 1, 1)) == 1
        and l1_cost((1, 1, 0), (1, 1, 1)) == 1
        and l1_cost((0, -1, 0), (1, -1, 0)) == 1
        and rho3_cost((0, 0, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (2, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (1, 1, 0)) == 1
        and rho3_cost((1, 1, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and rho3_cost((3, 2, 0), (4, 2, 0)) == 1
        and rho3_cost((4, 2, 0), (5, 2, 0)) == 1
        and rho3_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho3_cost((2, 2, 1), (3, 2, 1)) == 1
        and rho3_cost((2, 1, 0), (2, 1, 1)) == 1
        and rho3_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((4, 2, 0), (5, 2, 0)) == 2
        and c2d4_cost((3, 2, 0), (4, 2, 0)) == 1
        and c2d4_cost((2, 2, 0), (3, 2, 0)) == 1
        and c2d4_cost((1, 1, 0), (2, 1, 0)) == 3
        and c2d4_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d4_cost((2, 1, 0), (2, 1, 1)) == 1
        and c2d4_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((2, 2, 1), (3, 2, 1)) == 1
        and c2d4_cost((0, -1, 0), (1, -1, 0)) == 1
        and c2d4_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d4_cost((4, 1, 0), (5, 1, 0)) == 3,
    )

    moment_l1, var_l1_coeff = second_moment_and_var_coeff(dist_l1, sites)
    moment_c2d4, var_c2d4_coeff = second_moment_and_var_coeff(dist_c2d4, sites)
    var_l1 = eval_coeff(var_l1_coeff)
    var_c2d4 = eval_coeff(var_c2d4_coeff)

    print(f"Q_l1 = {moment_l1}")
    print(f"Q_c2d4 = {moment_c2d4}")
    print(f"var_l1 = {truncated_decimal(var_l1)}")
    print(f"var_c2d4 = {truncated_decimal(var_c2d4)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(
        "order: var_l1 > var_c2d4"
        if var_l1 > var_c2d4
        else ("order: var_l1 == var_c2d4" if var_l1 == var_c2d4 else "order: var_l1 < var_c2d4")
    )

    checks.check(
        "second-moments",
        "the two exact second moments match the note",
        moment_l1 == Q_L1
        and moment_c2d4 == Q_C2D4
        and "337/656" in note
        and "12586016761121881939/63482497589871360000" in note,
    )
    checks.check(
        "reported-variances",
        "the note reports the two truncated population variances",
        VAR_DIGITS["l1"] in note
        and VAR_DIGITS["c2d4"] in note
        and truncated_decimal(var_l1) == VAR_DIGITS["l1"]
        and truncated_decimal(var_c2d4) == VAR_DIGITS["c2d4"],
    )
    checks.check(
        "variance-order",
        "unit ℓ¹ is strictly less round than named c2d4 on B_12(0)",
        var_l1 > var_c2d4,
        residual=(str(var_l1), str(var_c2d4)),
    )
    checks.check(
        "thm2-note-reports-greater",
        "the note reports var_ℓ¹ greater than var_c2d4",
        "var_ℓ¹ > var_c2d4" in note and "strictly less round" in normalized_note,
    )

    forbidden = ("G_" "N", "1/" "r", "1/" "r^2", "Lattice-" "named", "not a " "TOE")
    checks.check(
        "forbidden-phrases",
        "note and runner omit the forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "theorems-displayed",
        "two theorems are present and the scores are displayed, not adopted",
        "## Theorem 1 — Two Variances" in note
        and "## Theorem 2 — Variance Order; Displayed, Not Adopted" in note
        and "Displayed, not adopted." in note
        and "displayed, not adopted" in normalized_note,
    )
    checks.check(
        "no-admissibility-write",
        "the note refuses to write hop-costs into Admissibility",
        "Do not write hop-costs into Admissibility." in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "c2d4(v→w)" not in axiom
        and "ℓ¹" not in axiom,
    )
    checks.check(
        "no-l1-attach",
        "the note does not attach L1",
        "This note does not attach L1." in note
        and "Do not attach L1." in note
        and "Do not attach L1" not in axiom
        and 'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "uniqueness-not-required",
        "uniqueness among hop-costs is not required",
        "Uniqueness is not required" in note and "not claimed" in normalized_note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d4(v→w)" not in axiom
        and "ℓ¹" not in axiom,
    )
    checks.check(
        "no-path-dump",
        "the runner stores arrival costs only",
        ("pre" + "decessor") not in self_source.lower()
        and ("path " + "dump") not in self_source.lower()
        and ("path " + "dump") not in note.lower(),
    )
    checks.check(
        "scope-ball",
        "the theorem stays on B_12(0) and uses two Dijkstras",
        "B_12(0)" in note
        and "Two Dijkstras" in note
        and "B_12(0)" in self_source
        and "B_" + "57" not in note
        and "B_" + "57" not in self_source,
    )

    print("per_element: checked exactly — each of the 2624 nonzero B_12(0) sites receives two arrival times")
    print("per_site: checked exactly — population variance uses |v|_2/t at every nonzero site")
    print("per_mode: checked exactly — unit ℓ¹ and named c2d4 only; no other clause family is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
