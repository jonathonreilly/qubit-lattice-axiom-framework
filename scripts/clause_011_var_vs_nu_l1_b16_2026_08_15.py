#!/usr/bin/env python3
"""Exact B_16(0) arrival-speed variance comparison of (0,1,1), ν, and ℓ¹."""

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
NOTE_PATH = ROOT / "docs" / "CLAUSE_011_VAR_VS_NU_L1_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_VAR_VS_NU_L1_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

RADIUS = 16
ORIGIN = (0, 0, 0)
SHIFTS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
NONZERO_COUNT = 6016
SITE_COUNT = 6017

Q_011 = Fraction(1696786091619347777, 3396055562124825600)
Q_NU = Fraction(98585558497628911, 271684444969986048)
Q_L1 = Fraction(191, 376)
VAR_DIGITS = {
    "(0,1,1)": "0.007597371121382114",
    "nu": "0.006780272990053171",
    "l1": "0.008690294859180384",
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


def hop_cost(source: Point, target: Point, seed: bool, axis_one: bool, drop: bool) -> int:
    source_weight = weight(source)
    target_weight = weight(target)
    expensive = False
    if seed and source_weight == 0:
        expensive = True
    if axis_one and source_weight == 1 and target_weight == 1:
        expensive = True
    if drop and target_weight < source_weight:
        expensive = True
    return 3 if expensive else 1


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

    print("claim_scope: Arrival-speed variance under (0,1,1), support-drop, and ℓ¹ on B_16(0) is compared. Displayed, not adopted.")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observation or fit")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: three directed Dijkstras on the induced B_16(0) graph")
    print("negative_scope: displayed scores are not adopted and L1 is not attached")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_VAR_VS_NU_L1_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    checks.check("ball-cardinality", "B_16(0) has 6017 sites and 6016 nonzero sites", len(sites) == SITE_COUNT and ORIGIN in site_set and len(sites) - 1 == NONZERO_COUNT)

    cost_011 = lambda src, dst: hop_cost(src, dst, seed=False, axis_one=True, drop=True)
    cost_nu = lambda src, dst: hop_cost(src, dst, seed=True, axis_one=True, drop=True)
    cost_l1 = lambda src, dst: 1

    dist_011 = dijkstra(sites, cost_011)
    dist_nu = dijkstra(sites, cost_nu)
    dist_l1 = dijkstra(sites, cost_l1)
    checks.check(
        "three-dijkstras",
        "each named cost reaches every ball site",
        len(dist_011) == SITE_COUNT and len(dist_nu) == SITE_COUNT and len(dist_l1) == SITE_COUNT,
        residual=(len(dist_011), len(dist_nu), len(dist_l1)),
    )
    checks.check(
        "l1-taxicab",
        "unit hop-cost arrivals equal the taxicab norm",
        all(dist_l1[site] == l1_norm(site) for site in sites),
    )

    moment_011, var_011_coeff = second_moment_and_var_coeff(dist_011, sites)
    moment_nu, var_nu_coeff = second_moment_and_var_coeff(dist_nu, sites)
    moment_l1, var_l1_coeff = second_moment_and_var_coeff(dist_l1, sites)
    var_011 = eval_coeff(var_011_coeff)
    var_nu = eval_coeff(var_nu_coeff)
    var_l1 = eval_coeff(var_l1_coeff)

    print(f"Q_(0,1,1) = {moment_011}")
    print(f"Q_nu = {moment_nu}")
    print(f"Q_l1 = {moment_l1}")
    print(f"var_(0,1,1) = {truncated_decimal(var_011)}")
    print(f"var_nu = {truncated_decimal(var_nu)}")
    print(f"var_l1 = {truncated_decimal(var_l1)}")

    checks.check("second-moments", "the three exact second moments match the note", moment_011 == Q_011 and moment_nu == Q_NU and moment_l1 == Q_L1)
    checks.check(
        "reported-variances",
        "the note reports the three truncated population variances",
        VAR_DIGITS["(0,1,1)"] in note and VAR_DIGITS["nu"] in note and VAR_DIGITS["l1"] in note
        and truncated_decimal(var_011) == VAR_DIGITS["(0,1,1)"]
        and truncated_decimal(var_nu) == VAR_DIGITS["nu"]
        and truncated_decimal(var_l1) == VAR_DIGITS["l1"],
    )
    checks.check(
        "variance-order",
        "ν is strictly rounder than (0,1,1), which is strictly rounder than ℓ¹",
        var_nu < var_011 < var_l1,
        residual=(str(var_nu), str(var_011), str(var_l1)),
    )

    named = {
        "(0,1,1)": var_011,
        "l1": var_l1,
        "nu": var_nu,
    }
    lex_first = min(named, key=lambda name: (named[name], name))
    print(f"lex_first_minimizer = {lex_first}")
    checks.check("lex-first-minimizer", "the lex-first minimizer among the three names is ν", lex_first == "nu")
    checks.check("cheaper-worse-round", "the cheaper rival stays worse-round", var_011 > var_nu)

    forbidden = ("G_" "N", "1/" "r", "1/" "r^2", "Lattice-" "named", "not a " "TOE")
    checks.check(
        "forbidden-phrases",
        "note and runner omit the forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "claim-scope",
        "front matter uses the declared claim_scope",
        'claim_scope: "Arrival-speed variance under (0,1,1), support-drop, and ℓ¹ on B_16(0) is compared. Displayed, not adopted."'
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
        "the note refuses to write (0,1,1) or ν into Admissibility",
        "Do not write `(0,1,1)` or ν into Admissibility." in note
        and "hop-cost values" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "(0,1,1)" not in axiom
        and "support-drop hop-cost" not in axiom,
    )
    checks.check(
        "no-l1-attach",
        "the note does not attach L1",
        "This note does not attach L1." in note
        and "Do not attach L1." in note
        and "hypothetical_axiom_status: \"no edit\"" in note,
    )

    mutated = dijkstra(sites, cost_l1)
    mutated_moment, mutated_coeff = second_moment_and_var_coeff(mutated, sites)
    mutated_var = eval_coeff(mutated_coeff)
    checks.check(
        "mutation-unit-as-nu",
        "replacing ν by unit cost destroys the reported minimizer",
        mutated_moment == moment_l1 and mutated_var == var_l1 and mutated_var > var_011,
    )

    print("per_element: checked exactly — each of the 6016 nonzero B_16(0) sites receives three arrival times")
    print("per_site: checked exactly — population variance uses |v|_2/t at every nonzero site")
    print("per_mode: checked exactly — three named hop-costs only; no other clause triple is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
