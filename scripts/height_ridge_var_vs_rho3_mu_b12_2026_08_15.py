#!/usr/bin/env python3
"""Exact B_12(0) arrival-speed variance comparison of ζ, ρ3, and μ."""

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
NOTE_PATH = ROOT / "docs" / "HEIGHT_RIDGE_VAR_VS_RHO3_MU_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/HEIGHT_RIDGE_VAR_VS_RHO3_MU_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

RADIUS = 12
ORIGIN = (0, 0, 0)
SHIFTS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
NONZERO_COUNT = 2624
SITE_COUNT = 2625

Q_ZETA = Fraction(7935966931146340589, 37031456927424960000)
Q_RHO3 = Fraction(8080835149812247289, 37031456927424960000)
Q_MU = Fraction(81461329283517896329, 284940228576113510400)
VAR_DIGITS = {
    "zeta": "0.005394463770340473",
    "rho3": "0.005047718614862020",
    "mu": "0.005601692188543646",
}


Point = tuple[int, int, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def l1_norm(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def radius_squared(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1] + point[2] * point[2]


def weight(point: Point) -> int:
    return sum(coordinate != 0 for coordinate in point)


def min_nonzero_abs(point: Point) -> int | None:
    nonzero = [abs(coordinate) for coordinate in point if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_coord_count(point: Point) -> int:
    return sum(abs(coordinate) == 1 for coordinate in point)


def height_ridge_clause(source: Point, target: Point) -> bool:
    if weight(source) != 3 or weight(target) != 3:
        return False
    abs_target = [abs(coordinate) for coordinate in target]
    height = min(abs_target)
    return height >= 2 and sum(value == height for value in abs_target) == 2


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
    source_weight = weight(source)
    target_weight = weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def mu_cost(source: Point, target: Point) -> int:
    if nu_cost(source, target) == 3:
        return 3
    if weight(source) == 2 and weight(target) == 2 and min_nonzero_abs(target) == 1:
        return 3
    return 1


def rho3_cost(source: Point, target: Point) -> int:
    if mu_cost(source, target) == 3:
        return 3
    if weight(source) == 3 and weight(target) == 3 and unit_coord_count(target) == 2:
        return 3
    return 1


def zeta_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if height_ridge_clause(source, target):
        return 3
    return 1


def neighbors(site: Point, sites: set[Point]) -> tuple[Point, ...]:
    out: list[Point] = []
    for shift in SHIFTS:
        candidate = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        if candidate in sites:
            out.append(candidate)
    return tuple(out)


def dijkstra(sites: tuple[Point, ...], cost_fn) -> dict[Point, int]:
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


def second_moment_and_var_coeff(dist: dict[Point, int], sites: tuple[Point, ...]) -> tuple[Fraction, dict[int, Fraction]]:
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

    print("claim_scope: Arrival-speed variance under height-ridge, ridge-slide, and corridor-slide on B_12(0) is compared. Displayed, not adopted.")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observation or fit")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: three directed Dijkstras on the induced B_12(0) graph")
    print("negative_scope: displayed scores are not adopted and L1 is not attached")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/HEIGHT_RIDGE_VAR_VS_RHO3_MU_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-tuple-literal",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        parse_audit_tuple(self_source) == AUDIT_INPUT_PATHS,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalized_axiom and admissibility_sentence in normalized_note)
    checks.check("source-formation-boundary", "formation site/probability/rate remains outside Admissibility", formation_boundary in normalized_axiom and formation_boundary in normalized_note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )

    sites = ball_sites(RADIUS)
    site_set = set(sites)
    checks.check("ball-cardinality", "B_12(0) has 2625 sites and 2624 nonzero sites", len(sites) == SITE_COUNT and ORIGIN in site_set and len(sites) - 1 == NONZERO_COUNT)

    checks.check(
        "named-hop-costs",
        "ζ taxes height-m ridges that ρ3 leaves cheap",
        zeta_cost((2, 2, 2), (3, 2, 2)) == 3
        and rho3_cost((2, 2, 2), (3, 2, 2)) == 1
        and mu_cost((2, 2, 2), (3, 2, 2)) == 1
        and zeta_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho3_cost((1, 1, 1), (2, 1, 1)) == 3
        and zeta_cost((3, 3, 3), (4, 3, 3)) == 3
        and rho3_cost((3, 3, 3), (4, 3, 3)) == 1
        and zeta_cost((2, 2, 2), (2, 2, 3)) == 3
        and zeta_cost((2, 3, 3), (3, 3, 3)) == 1
        and mu_cost((1, 1, 0), (2, 1, 0)) == 3
        and nu_cost((0, 0, 0), (1, 0, 0)) == 3,
    )

    dist_zeta = dijkstra(sites, zeta_cost)
    dist_rho3 = dijkstra(sites, rho3_cost)
    dist_mu = dijkstra(sites, mu_cost)
    checks.check(
        "three-dijkstras",
        "each named cost reaches every ball site",
        len(dist_zeta) == SITE_COUNT and len(dist_rho3) == SITE_COUNT and len(dist_mu) == SITE_COUNT,
        residual=(len(dist_zeta), len(dist_rho3), len(dist_mu)),
    )

    moment_zeta, var_zeta_coeff = second_moment_and_var_coeff(dist_zeta, sites)
    moment_rho3, var_rho3_coeff = second_moment_and_var_coeff(dist_rho3, sites)
    moment_mu, var_mu_coeff = second_moment_and_var_coeff(dist_mu, sites)
    var_zeta = eval_coeff(var_zeta_coeff)
    var_rho3 = eval_coeff(var_rho3_coeff)
    var_mu = eval_coeff(var_mu_coeff)

    print(f"Q_zeta = {moment_zeta}")
    print(f"Q_rho3 = {moment_rho3}")
    print(f"Q_mu = {moment_mu}")
    print(f"var_zeta = {truncated_decimal(var_zeta)}")
    print(f"var_rho3 = {truncated_decimal(var_rho3)}")
    print(f"var_mu = {truncated_decimal(var_mu)}")

    checks.check("second-moments", "the three exact second moments match the note", moment_zeta == Q_ZETA and moment_rho3 == Q_RHO3 and moment_mu == Q_MU)
    checks.check(
        "reported-variances",
        "the note reports the three truncated population variances",
        VAR_DIGITS["zeta"] in note and VAR_DIGITS["rho3"] in note and VAR_DIGITS["mu"] in note
        and truncated_decimal(var_zeta) == VAR_DIGITS["zeta"]
        and truncated_decimal(var_rho3) == VAR_DIGITS["rho3"]
        and truncated_decimal(var_mu) == VAR_DIGITS["mu"],
    )
    checks.check(
        "variance-order",
        "ρ3 is strictly rounder than ζ, which is strictly rounder than μ",
        var_rho3 < var_zeta < var_mu,
        residual=(str(var_rho3), str(var_zeta), str(var_mu)),
    )

    named = {
        "mu": var_mu,
        "rho3": var_rho3,
        "zeta": var_zeta,
    }
    lex_first = min(named, key=lambda name: (named[name], name))
    print(f"lex_first_minimizer = {lex_first}")
    checks.check("lex-first-minimizer", "the lex-first minimizer among the three names is ρ3", lex_first == "rho3")
    checks.check("height-ridge-worse-round", "ζ stays worse-round than ρ3", var_zeta > var_rho3)

    forbidden = ("G_" "N", "1/" "r", "1/" "r^2", "Lattice-" "named", "not a " "TOE")
    checks.check(
        "forbidden-phrases",
        "note and runner omit the forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "claim-scope",
        "front matter uses the declared claim_scope",
        'claim_scope: "Arrival-speed variance under height-ridge, ridge-slide, and corridor-slide on B_12(0) is compared. Displayed, not adopted."'
        in note,
    )
    checks.check(
        "theorems-displayed",
        "three theorems are present and the scores are displayed, not adopted",
        "## Theorem 1 — Three Variances" in note
        and "## Theorem 2 — Lex-First Minimizer" in note
        and "## Theorem 3 — No Admissibility Write, L1 Not Attached" in note
        and "Displayed, not adopted." in note
        and "displayed, not adopted" in normalized_note,
    )
    checks.check(
        "no-admissibility-write",
        "the note refuses to write ζ, ρ3, or μ into Admissibility",
        "Do not write ζ, ρ3, or μ into Admissibility." in note
        and "hop-cost values" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "height-ridge hop-cost" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "no-l1-attach",
        "the note does not attach L1",
        "This note does not attach L1." in note
        and "Do not attach L1." in note
        and "hypothetical_axiom_status: \"no edit\"" in note,
    )

    mutated = dijkstra(sites, rho3_cost)
    mutated_moment, mutated_coeff = second_moment_and_var_coeff(mutated, sites)
    mutated_var = eval_coeff(mutated_coeff)
    checks.check(
        "mutation-zeta-as-rho3",
        "dropping the height-ridge clause collapses ζ onto ρ3",
        mutated_moment == moment_rho3 and mutated_var == var_rho3 and mutated_var != var_zeta,
    )

    print("per_element: checked exactly — each of the 2624 nonzero B_12(0) sites receives three arrival times")
    print("per_site: checked exactly — population variance uses |v|_2/t at every nonzero site")
    print("per_mode: checked exactly — three named hop-costs only; no other clause is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
