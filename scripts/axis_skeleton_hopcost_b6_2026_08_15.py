#!/usr/bin/env python3
"""Score the named axis-skeleton hop-cost on B_6(0).

One Dijkstra computes α-arrival times on the closed nearest-neighbor graph
ball of radius 6. The runner reports diamond reverse at (4,0,0) versus
(2,2,2) and the population variance of |v|_2/t against ℓ¹. α is displayed,
not adopted. No cache or governance surface is written.
"""

from __future__ import annotations

import heapq
import math
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "AXIS_SKELETON_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/AXIS_SKELETON_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
RADIUS = 6
VAR_ALPHA_TEXT = "0.005489876321"
VAR_L1_TEXT = "0.013502037619"


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def weight(point: Point) -> int:
    return sum(coord != 0 for coord in point)


def l1_norm(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def l2_norm(point: Point) -> float:
    return math.sqrt(point[0] * point[0] + point[1] * point[1] + point[2] * point[2])


def alpha(source: Point, target: Point) -> int:
    source_weight = weight(source)
    target_weight = weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1):
        return 3
    return 1


def graph_ball(radius: int) -> frozenset[Point]:
    span = range(-radius, radius + 1)
    return frozenset(point for point in product(span, repeat=3) if l1_norm(point) <= radius)


def dijkstra_alpha(ball: frozenset[Point]) -> dict[Point, int]:
    dist = {ORIGIN: 0}
    heap: list[tuple[int, Point]] = [(0, ORIGIN)]
    while heap:
        cost, site = heapq.heappop(heap)
        if cost != dist[site]:
            continue
        for shift in SHIFTS:
            neighbor = add(site, shift)
            if neighbor not in ball:
                continue
            new_cost = cost + alpha(site, neighbor)
            if new_cost < dist.get(neighbor, 10**9):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist


def population_variance(values: list[float]) -> float:
    count = len(values)
    mean = sum(values) / count
    return sum((value - mean) ** 2 for value in values) / count


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Lattice nearest-neighbor graph "
        "and Admissibility non-adoption boundary are source-bound; no observation or fit"
    )
    print(
        "integrity_reads: this runner, its note, and the current axiom memo; "
        "no cache or governance surface is written"
    )
    print(
        "construction: one Dijkstra for the named axis-skeleton hop-cost on B_6(0)"
    )
    print(
        "negative_scope: displayed score only; alpha is not adopted, not written "
        "into Admissibility, and does not attach L1"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and the current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/AXIS_SKELETON_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_one = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    checks.check(
        "source-lattice",
        "the cubic nearest-neighbor graph is the current Lattice premise",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility-unedited",
        "the axiom still names one fixed nearest-neighbor admissibility rule",
        admissibility_one in axiom and admissibility_one in note,
    )
    checks.check(
        "axiom-has-no-alpha",
        "the axiom memo does not contain the named hop-cost",
        "axis-skeleton" not in axiom and "α(v→w)" not in axiom and "alpha hop" not in axiom,
    )
    checks.check(
        "source-record-unused",
        "lock, content-only readout, and unreadability at absence are quoted as unused",
        all(
            phrase in normalized_axiom and phrase in normalized_note
            for phrase in (record_lock, record_content, record_absence)
        )
        and "Record supplies no hop-cost" in note,
    )

    claim_scope = (
        "On B_6(0), the named axis-skeleton hop-cost is scored for diamond "
        "reverse at (4,0,0) vs (2,2,2) and for var(|v|_2/t) vs ℓ¹. "
        "Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "the note carries the declared displayed claim_scope",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note states displayed, not adopted, and uniqueness is not claimed",
        "Displayed, not adopted" in note
        and "displayed, not adopted" in note
        and "Uniqueness is not required" in note
        and "not written into Admissibility" in note,
    )
    checks.check(
        "no-l1-attachment",
        "the note refuses L1 attachment",
        "This note does not attach L1." in note
        and "L1 attachment | refused" in normalize(note).replace(" | ", " | "),
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-phrases",
        "the note omits the forbidden tokens",
        all(token not in note for token in forbidden),
        [token for token in forbidden if token in note],
    )

    checks.check(
        "alpha-seed-exit",
        "seed exit costs 3",
        alpha(ORIGIN, (1, 0, 0)) == 3 and alpha(ORIGIN, (0, -1, 0)) == 3,
    )
    checks.check(
        "alpha-axis-skeleton",
        "both-weight-one hops cost 3",
        alpha((1, 0, 0), (2, 0, 0)) == 3
        and alpha((2, 0, 0), (3, 0, 0)) == 3
        and alpha((0, 4, 0), (0, 3, 0)) == 3,
    )
    checks.check(
        "alpha-off-skeleton",
        "leaving the axis 1-skeleton costs 1",
        alpha((1, 0, 0), (1, 1, 0)) == 1
        and alpha((1, 1, 0), (2, 1, 0)) == 1
        and alpha((1, 1, 0), (1, 1, 1)) == 1
        and alpha((4, 1, 0), (4, 0, 0)) == 1,
    )

    ball = graph_ball(RADIUS)
    dijkstra_runs = 0
    dijkstra_runs += 1
    dist = dijkstra_alpha(ball)
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra run covers B_6(0)",
        dijkstra_runs == 1
        and len(ball) == 377
        and set(dist) == set(ball)
        and dist[ORIGIN] == 0,
        (dijkstra_runs, len(ball), len(dist)),
    )

    t400 = dist[(4, 0, 0)]
    t222 = dist[(2, 2, 2)]
    t110 = dist[(1, 1, 0)]
    t220 = dist[(2, 2, 0)]
    t330 = dist[(3, 3, 0)]
    reverse_left = 12 * t400 * t400
    reverse_right = 16 * t222 * t222
    reverse = reverse_left > reverse_right
    checks.check(
        "theorem-1-times",
        "t(4,0,0)=8 and t(2,2,2)=8",
        t400 == 8 and t222 == 8,
        (t400, t222),
    )
    checks.check(
        "theorem-1-reverse",
        "12 t(4,0,0)^2 > 16 t(2,2,2)^2 is false",
        reverse_left == 768 and reverse_right == 1024 and reverse is False,
        (reverse_left, reverse_right, reverse),
    )
    checks.check(
        "face-split",
        "(1,1,0) and (2,2,0) split, and (2,2),(3,3) are cheaper than 3 |v|_1",
        t110 == 4
        and t220 == 6
        and t330 == 8
        and t220 < 3 * l1_norm((2, 2, 0))
        and t330 < 3 * l1_norm((3, 3, 0)),
        (t110, t220, t330),
    )

    nonzero = sorted(point for point in ball if point != ORIGIN)
    ratios_alpha = [l2_norm(point) / dist[point] for point in nonzero]
    ratios_l1 = [l2_norm(point) / l1_norm(point) for point in nonzero]
    var_alpha = population_variance(ratios_alpha)
    var_l1 = population_variance(ratios_l1)
    checks.check(
        "theorem-2-variance",
        "var_α is smaller than var_ℓ¹ on B_6(0)\\{0}",
        len(nonzero) == 376
        and f"{var_alpha:.12f}" == VAR_ALPHA_TEXT
        and f"{var_l1:.12f}" == VAR_L1_TEXT
        and var_alpha < var_l1,
        (len(nonzero), f"{var_alpha:.12f}", f"{var_l1:.12f}"),
    )

    checks.check(
        "note-reports-score",
        "the note reports the computed times, reverse integers, and variances",
        "t(4,0,0)=8" in note
        and "t(2,2,2)=8" in note
        and "768 > 1024" in note
        and VAR_ALPHA_TEXT in note
        and VAR_L1_TEXT in note
        and "t(1,1,0)=4" in note
        and "t(2,2,0)=6" in note,
    )
    checks.check(
        "ball-membership",
        "(4,0,0) and (2,2,2) lie in the declared graph ball and not beyond it",
        (4, 0, 0) in ball
        and (2, 2, 2) in ball
        and l1_norm((2, 2, 2)) == RADIUS
        and (7, 0, 0) not in ball,
    )

    print(f"t(4,0,0)={t400}")
    print(f"t(2,2,2)={t222}")
    print(f"reverse_left={reverse_left} reverse_right={reverse_right} reverse={reverse}")
    print(f"var_alpha={var_alpha:.12f} var_l1={var_l1:.12f}")
    print(f"sites={len(ball)} nonzero={len(nonzero)} dijkstra_runs={dijkstra_runs}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
