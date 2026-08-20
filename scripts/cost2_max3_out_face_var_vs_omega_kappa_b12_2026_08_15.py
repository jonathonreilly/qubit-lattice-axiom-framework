#!/usr/bin/env python3
"""Exact B_12(0) arrival-speed variance comparison of c2d3, ω, and κ."""

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
NOTE_REL = "docs/COST2_MAX3_OUT_FACE_VAR_VS_OMEGA_KAPPA_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/COST2_MAX3_OUT_FACE_VAR_VS_OMEGA_KAPPA_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Arrival-speed variance under cost-2 max≥3 out-face, out-face, and "
    "ridge-enter on B_12(0) is reported. Displayed, not adopted."
)

RADIUS = 12
ORIGIN = (0, 0, 0)
SHIFTS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
NONZERO_COUNT = 2624
SITE_COUNT = 2625
DIJKSTRA_CALLS = 0

Q_C2D3 = Fraction(2273856763058868971, 11694144292871040000)
Q_OMEGA = Fraction(2697928722329275408991, 14234892042902154624000)
Q_KAPPA = Fraction(8065845471432407489, 37031456927424960000)
VAR_DIGITS = {
    "c2d3": "0.003682635284982629",
    "omega": "0.004242786759120176",
    "kappa": "0.005030477616848010",
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


def kappa_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if support_size(source) == 2 and support_size(target) == 3 and unit_abs_count(target) == 2:
        return 3
    return 1


def omega_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if (
        support_size(source) == 2
        and support_size(target) == 2
        and max_abs_coord(target) > max_abs_coord(source)
    ):
        return 3
    return 1


def c2d3_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if (
        support_size(source) == 2
        and support_size(target) == 2
        and max_abs_coord(target) > max_abs_coord(source)
        and max_abs_coord(source) >= 3
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
    print("construction: three directed Dijkstras on the induced B_12(0) graph")
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

    dist_c2d3 = dijkstra(sites, c2d3_cost)
    dist_omega = dijkstra(sites, omega_cost)
    dist_kappa = dijkstra(sites, kappa_cost)
    checks.check(
        "three-dijkstras",
        "exactly three Dijkstras run and each named cost reaches every ball site",
        DIJKSTRA_CALLS == 3
        and len(dist_c2d3) == SITE_COUNT
        and len(dist_omega) == SITE_COUNT
        and len(dist_kappa) == SITE_COUNT,
        residual=(DIJKSTRA_CALLS, len(dist_c2d3), len(dist_omega), len(dist_kappa)),
    )
    checks.check(
        "named-clauses",
        "c2d3 prices max≥3 out-face at 2; ω prices all out-face at 3; κ prices ridge-enter at 3",
        rho3_cost((0, 0, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (2, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (1, 1, 0)) == 1
        and rho3_cost((1, 1, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and rho3_cost((3, 2, 0), (4, 2, 0)) == 1
        and rho3_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho3_cost((2, 2, 1), (3, 2, 1)) == 1
        and rho3_cost((2, 1, 0), (2, 1, 1)) == 1
        and rho3_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d3_cost((3, 2, 0), (4, 2, 0)) == 2
        and c2d3_cost((2, 2, 0), (3, 2, 0)) == 1
        and c2d3_cost((1, 1, 0), (2, 1, 0)) == 3
        and c2d3_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d3_cost((2, 1, 0), (2, 1, 1)) == 1
        and c2d3_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d3_cost((2, 2, 1), (3, 2, 1)) == 1
        and c2d3_cost((0, -1, 0), (1, -1, 0)) == 1
        and omega_cost((3, 2, 0), (4, 2, 0)) == 3
        and omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and omega_cost((1, 1, 0), (2, 1, 0)) == 3
        and omega_cost((1, 1, 1), (2, 1, 1)) == 3
        and omega_cost((2, 2, 1), (3, 2, 1)) == 1
        and omega_cost((2, 1, 0), (2, 1, 1)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((0, -1, 0), (1, -1, 0)) == 1
        and kappa_cost((1, 1, 0), (2, 1, 0)) == 3
        and kappa_cost((1, 1, 1), (2, 1, 1)) == 3
        and kappa_cost((2, 2, 0), (3, 2, 0)) == 1
        and kappa_cost((3, 2, 0), (4, 2, 0)) == 1
        and kappa_cost((2, 1, 0), (2, 1, 1)) == 3
        and kappa_cost((1, 1, 0), (1, 1, 1)) == 1
        and kappa_cost((0, -1, 0), (1, -1, 0)) == 1,
    )

    moment_c2d3, var_c2d3_coeff = second_moment_and_var_coeff(dist_c2d3, sites)
    moment_omega, var_omega_coeff = second_moment_and_var_coeff(dist_omega, sites)
    moment_kappa, var_kappa_coeff = second_moment_and_var_coeff(dist_kappa, sites)
    var_c2d3 = eval_coeff(var_c2d3_coeff)
    var_omega = eval_coeff(var_omega_coeff)
    var_kappa = eval_coeff(var_kappa_coeff)

    print(f"Q_c2d3 = {moment_c2d3}")
    print(f"Q_omega = {moment_omega}")
    print(f"Q_kappa = {moment_kappa}")
    print(f"var_c2d3 = {truncated_decimal(var_c2d3)}")
    print(f"var_omega = {truncated_decimal(var_omega)}")
    print(f"var_kappa = {truncated_decimal(var_kappa)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "second-moments",
        "the three exact second moments match the note",
        moment_c2d3 == Q_C2D3
        and moment_omega == Q_OMEGA
        and moment_kappa == Q_KAPPA
        and "2273856763058868971/11694144292871040000" in note
        and "2697928722329275408991/14234892042902154624000" in note
        and "8065845471432407489/37031456927424960000" in note,
    )
    checks.check(
        "reported-variances",
        "the note reports the three truncated population variances",
        VAR_DIGITS["c2d3"] in note
        and VAR_DIGITS["omega"] in note
        and VAR_DIGITS["kappa"] in note
        and truncated_decimal(var_c2d3) == VAR_DIGITS["c2d3"]
        and truncated_decimal(var_omega) == VAR_DIGITS["omega"]
        and truncated_decimal(var_kappa) == VAR_DIGITS["kappa"],
    )
    checks.check(
        "variance-order",
        "c2d3 is strictly rounder than ω, which is strictly rounder than κ",
        var_c2d3 < var_omega < var_kappa,
        residual=(str(var_c2d3), str(var_omega), str(var_kappa)),
    )

    named = {
        "c2d3": var_c2d3,
        "kappa": var_kappa,
        "omega": var_omega,
    }
    lex_first = min(named, key=lambda name: (named[name], name))
    print(f"lex_first_minimizer = {lex_first}")
    checks.check(
        "lex-first-minimizer",
        "the lex-first minimizer among the three names is c2d3",
        lex_first == "c2d3",
    )

    forbidden = ("G_" "N", "1/" "r", "1/" "r^2", "Lattice-" "named", "not a " "TOE")
    checks.check(
        "forbidden-phrases",
        "note and runner omit the forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
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
        "the note refuses to write c2d3, ω, or κ into Admissibility",
        "Do not write `c2d3`, `ω`, or `κ` into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "c2d3(v→w)" not in axiom
        and "ω(v→w)" not in axiom
        and "κ(v→w)" not in axiom,
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
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note or "uniqueness" in note.lower() and "not claimed" in normalized_note,
    )
    checks.check(
        "mutation-c2d3-as-omega-or-kappa",
        "pricing all out-face at 3 or omitting the max≥3 clause would erase c2d3 being rounder than both",
        var_c2d3 < var_omega < var_kappa,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d3(v→w)" not in axiom
        and "ω(v→w)" not in axiom
        and "κ(v→w)" not in axiom,
    )

    print("per_element: checked exactly — each of the 2624 nonzero B_12(0) sites receives three arrival times")
    print("per_site: checked exactly — population variance uses |v|_2/t at every nonzero site")
    print("per_mode: checked exactly — three named hop-costs only; no other clause triple is scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
