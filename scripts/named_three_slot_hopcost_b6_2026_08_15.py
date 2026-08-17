#!/usr/bin/env python3
"""Census of 27 named (seed, equal, unequal) hop-costs on B_6(0)."""

from __future__ import annotations

import heapq
from itertools import product
from math import sqrt
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/NAMED_THREE_SLOT_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NAMED_THREE_SLOT_HOPCOST_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
COSTS = (1, 2, 3)
AXIS = (4, 0, 0)
BODY = (2, 2, 2)
RADIUS = 6


def normalize(text: str) -> str:
    return " ".join(text.split())


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_card(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def l2(v: tuple[int, int, int]) -> float:
    return sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def hop_cost(
    src: tuple[int, int, int],
    dst: tuple[int, int, int],
    c_seed: int,
    c_eq: int,
    c_uneq: int,
) -> int:
    weight_src = support_card(src)
    if weight_src == 0:
        return c_seed
    if weight_src == support_card(dst):
        return c_eq
    return c_uneq


def dijkstra(
    sites: list[tuple[int, int, int]],
    c_seed: int,
    c_eq: int,
    c_uneq: int,
) -> dict[tuple[int, int, int], int]:
    site_set = set(sites)
    dist = {(0, 0, 0): 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, (0, 0, 0))]
    seen: set[tuple[int, int, int]] = set()
    while heap:
        time, src = heapq.heappop(heap)
        if src in seen:
            continue
        seen.add(src)
        sx, sy, sz = src
        for dx, dy, dz in NEIGH:
            dst = (sx + dx, sy + dy, sz + dz)
            if dst not in site_set:
                continue
            nxt = time + hop_cost(src, dst, c_seed, c_eq, c_uneq)
            if nxt < dist.get(dst, 10**9):
                dist[dst] = nxt
                heapq.heappush(heap, (nxt, dst))
    return dist


def population_variance(values: list[float]) -> float:
    count = len(values)
    mean = sum(values) / count
    return sum((value - mean) ** 2 for value in values) / count


def reverses_diamond(t_axis: int, t_body: int) -> bool:
    return 12 * t_axis * t_axis > 16 * t_body * t_body


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
    note = (ROOT / NOTE_REL).read_text(encoding="utf-8")
    axiom = (ROOT / AXIOM_REL).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; the 27 triples, B_6(0), and the diamond/variance comparators are declared finite inputs")
    print("framework_role: displayed finite hop-cost census; no Admissibility edit and no L1 attachment")
    print("claim_scope: Among 27 named (seed, equal, unequal) hop-costs on B_6(0), those that reverse diamond at (4,0,0) vs (2,2,2) and beat l1 variance are counted. Displayed, not adopted.")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )

    sites = ball(RADIUS)
    nonzero = [site for site in sites if site != (0, 0, 0)]
    checks.check(
        "ball-cardinality",
        "B_6(0) has exactly 377 sites and contains both probes",
        len(sites) == 377
        and AXIS in sites
        and BODY in sites
        and l1(AXIS) == 4
        and l1(BODY) == 6,
        len(sites),
    )
    checks.check(
        "nonzero-count",
        "variance domain is the 376 nonzero sites",
        len(nonzero) == 376,
        len(nonzero),
    )

    triples = tuple(product(COSTS, repeat=3))
    checks.check(
        "named-family-size",
        "the named family is the lex-ordered 27 triples in {1,2,3}^3",
        len(triples) == 27 and triples[0] == (1, 1, 1) and triples[-1] == (3, 3, 3),
        len(triples),
    )

    l1_times = {site: l1(site) for site in sites}
    var_l1 = population_variance([l2(site) / l1_times[site] for site in nonzero])
    unit_dist = dijkstra(sites, 1, 1, 1)
    checks.check(
        "unit-rule-is-l1",
        "the (1,1,1) rule reproduces the l1 arrival table on B_6(0)",
        all(unit_dist[site] == l1_times[site] for site in sites),
    )

    rows = []
    for c_seed, c_eq, c_uneq in triples:
        dist = dijkstra(sites, c_seed, c_eq, c_uneq)
        t_axis = dist[AXIS]
        t_body = dist[BODY]
        variance = population_variance([l2(site) / dist[site] for site in nonzero])
        rows.append(
            {
                "triple": (c_seed, c_eq, c_uneq),
                "complete": len(dist) == 377,
                "t_axis": t_axis,
                "t_body": t_body,
                "reverse": reverses_diamond(t_axis, t_body),
                "variance": variance,
                "beat": variance < var_l1,
            }
        )

    checks.check(
        "twenty-seven-dijkstras",
        "exactly 27 complete arrival tables were computed on B_6(0)",
        len(rows) == 27 and all(row["complete"] for row in rows),
        len(rows),
    )
    checks.check(
        "no-eight-tuple-scan",
        "the runner enumerates 27 named triples and does not scan 6561 occupancy 8-tuples",
        len(triples) == 27 and len(rows) == 27,
    )

    reversals = [row for row in rows if row["reverse"]]
    beaters = [row for row in reversals if row["beat"]]
    n_rev = len(reversals)
    n_beat = len(beaters)
    print(f"N_rev={n_rev}")
    print(f"N_beat={n_beat}")
    print(f"var_l1={var_l1:.12f}")

    investment = next(row for row in rows if row["triple"] == (3, 3, 1))
    unit_row = next(row for row in rows if row["triple"] == (1, 1, 1))
    print(
        "investment_(3,3,1) "
        f"t(4,0,0)={investment['t_axis']} t(2,2,2)={investment['t_body']} "
        f"reverse={investment['reverse']}"
    )

    checks.check(
        "theorem-1-n-rev",
        "N_rev=0: none of the 27 reverse 12 t(4,0,0)^2 > 16 t(2,2,2)^2",
        n_rev == 0,
        n_rev,
    )
    checks.check(
        "theorem-2-n-beat",
        "N_beat=0 because the reversal set is empty",
        n_beat == 0,
        n_beat,
    )
    checks.check(
        "investment-nonreversal",
        "the seed-exit 3, equal 3, unequal 1 investment stays strictly below the diamond cut",
        investment["t_axis"] == 12
        and investment["t_body"] == 14
        and 12 * 12 * 12 < 16 * 14 * 14
        and not investment["reverse"],
        (investment["t_axis"], investment["t_body"]),
    )
    checks.check(
        "unit-nonreversal",
        "the unit l1 comparator itself does not reverse the diamond",
        unit_row["t_axis"] == 4
        and unit_row["t_body"] == 6
        and 12 * 16 < 16 * 36
        and not unit_row["reverse"],
    )
    checks.check(
        "best-ratio-still-short",
        "the largest t(4,0,0)/t(2,2,2) among the 27 is 12/14, below 2/sqrt(3)",
        max(row["t_axis"] / row["t_body"] for row in rows) == 12 / 14
        and (12 / 14) ** 2 < 4 / 3,
    )
    checks.check(
        "axiom-unedited",
        "current Admissibility names no hop-cost triple and is not edited here",
        "c_seed" not in axiom
        and "c_eq" not in axiom
        and "c_uneq" not in axiom
        and "(3, 3, 1)" not in axiom
        and "hop-cost" not in axiom
        and "There is one fixed nearest-neighbor admissibility rule" in axiom,
    )

    forbidden_note = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    required = (
        "N_rev = 0",
        "N_beat = 0",
        "Displayed, not adopted",
        "Uniqueness is not claimed",
        "Do not attach L1",
        "authors no audit verdict",
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "Among 27 named (seed, equal, unequal) hop-costs on B_6(0), those that reverse diamond at (4,0,0) vs (2,2,2) and beat ℓ¹ variance are counted. Displayed, not adopted.",
    )
    checks.check(
        "note-census",
        "the note reports N_rev=0, N_beat=0, and the displayed-not-adopted boundary",
        all(item in note for item in required)
        and "lex-first reversing triple does not exist" in normalized_note
        and "t(4,0,0)=12" in note
        and "t(2,2,2)=14" in note,
    )
    checks.check(
        "note-hygiene",
        "forbidden phrases, uniqueness, L1 attachment, and axiom-edit language are absent",
        all(phrase not in note for phrase in forbidden_note)
        and all(phrase not in axiom for phrase in forbidden_note)
        and "new axiom" not in note.lower()
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and all(f"### N{index}" in note for index in range(1, 9)),
        [phrase for phrase in forbidden_note if phrase in note],
    )
    checks.check(
        "claim-scope-literal",
        "claim_scope matches the declared census wording",
        "Among 27 named (seed, equal, unequal) hop-costs on B_6(0)" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "source-axiom-boundary",
        "the current axiom memo still types one covariant nearest-neighbor rule and no named three-slot cost",
        "one fixed nearest-neighbor admissibility rule" in normalized_axiom
        and "covariant under lattice translations and proper cubic rotations" in normalized_axiom
        and "named three-slot" not in normalized_axiom,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine fields and retained-language hygiene hold",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "FAIL / DO NOT SHIP" in note
        and "27 Dijkstras" in note,
    )

    print("per_element: each of the 27 named triples is one Dijkstra arrival table")
    print("per_site: times are compared only at (4,0,0) and (2,2,2); variance uses B_6(0) minus the origin")
    print("per_mode: seed-exit, equal-support, and unequal-support are the only named cost slots")
    print("per_block: diamond reversal and l1-variance beating are counted, not adopted")
    print("lattice_wide: checked and not executed — no infinite-lattice or 6561 8-tuple scan")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
