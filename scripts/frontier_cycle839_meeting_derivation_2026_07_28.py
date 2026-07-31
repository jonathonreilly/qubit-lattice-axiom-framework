#!/usr/bin/env python3
"""Cycle 839: exact two-arc meeting theorem and causal-derivation attempt.

The graph-wavefront construction is kept distinct from the landed controller:
the former expands in both directions on C11, while the latter common-
translates every live A-rail token.  Later certificates test the proposed
bridge without executing either the Cycle-837 or Cycle-830 primary.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle837_why_sep5_2026_07_28.py",
)

from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
SEPARATIONS = tuple(range(1, RING_STATIONS // 2 + 1))

Pair = tuple[int, int]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def arc_vertices(
    start: int,
    direction: int,
    length: int,
) -> tuple[int, ...]:
    return tuple(
        (start + direction * offset) % RING_STATIONS
        for offset in range(length + 1)
    )


def enumerated_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    for tick in range(length + 1):
        from_left = {
            vertices[index] for index in range(length + 1)
            if index <= tick
        }
        from_right = {
            vertices[index] for index in range(length + 1)
            if length - index <= tick
        }
        overlap = from_left & from_right
        if overlap:
            return tick, tuple(
                station for station in vertices if station in overlap
            )
    raise AssertionError(("arc wavefronts did not meet", vertices))


def theorem_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    tick = (length + 1) // 2
    return tick, tuple(vertices[length - tick:tick + 1])


def source_swap_reflection(
    station: int,
    left: int,
    right: int,
) -> int:
    return (left + right - station) % RING_STATIONS


def oriented_pairs(separation: int) -> tuple[Pair, ...]:
    return tuple(
        (left, (left + separation) % RING_STATIONS)
        for left in range(RING_STATIONS)
    )


def pair_meeting_row(left: int, separation: int) -> dict[str, object]:
    right = (left + separation) % RING_STATIONS
    short_arc = arc_vertices(left, +1, separation)
    long_arc = arc_vertices(left, -1, RING_STATIONS - separation)
    short_formula = theorem_arc_meeting(short_arc)
    long_formula = theorem_arc_meeting(long_arc)
    short_enumerated = enumerated_arc_meeting(short_arc)
    long_enumerated = enumerated_arc_meeting(long_arc)
    short_centers = short_formula[1]
    long_centers = long_formula[1]
    reflection = {
        station: source_swap_reflection(station, left, right)
        for station in short_centers + long_centers
    }
    return {
        "oriented_pair": (left, right),
        "arc_lengths": (separation, RING_STATIONS - separation),
        "meeting_times": (short_formula[0], long_formula[0]),
        "short_arc_meeting_stations": short_centers,
        "long_arc_meeting_stations": long_centers,
        "meeting_station_union": tuple(sorted(
            set(short_centers) | set(long_centers)
        )),
        "two_arc_time_tie": short_formula[0] == long_formula[0],
        "source_swap_reflection_on_meeting_stations": tuple(
            sorted(reflection.items())
        ),
        "short_meeting_set_reflection_invariant": {
            source_swap_reflection(station, left, right)
            for station in short_centers
        } == set(short_centers),
        "long_meeting_set_reflection_invariant": {
            source_swap_reflection(station, left, right)
            for station in long_centers
        } == set(long_centers),
        "formula_equals_enumeration": (
            short_formula == short_enumerated
            and long_formula == long_enumerated
        ),
    }


def meeting_theorem_certificate() -> dict[str, object]:
    rows = []
    all_pair_rows = {}
    for separation in SEPARATIONS:
        pair_rows = tuple(
            pair_meeting_row(left, separation)
            for left in range(RING_STATIONS)
        )
        all_pair_rows[separation] = pair_rows
        representative = pair_rows[0]
        rotation_exact = all(
            row["meeting_times"] == representative["meeting_times"]
            and row["short_arc_meeting_stations"] == tuple(
                (station + left) % RING_STATIONS
                for station in representative[
                    "short_arc_meeting_stations"
                ]
            )
            and row["long_arc_meeting_stations"] == tuple(
                (station + left) % RING_STATIONS
                for station in representative[
                    "long_arc_meeting_stations"
                ]
            )
            for left, row in enumerate(pair_rows)
        )
        rows.append({
            "separation": separation,
            "arc_lengths": representative["arc_lengths"],
            "meeting_times_short_long":
                representative["meeting_times"],
            "representative_oriented_pair":
                representative["oriented_pair"],
            "representative_short_meeting_stations":
                representative["short_arc_meeting_stations"],
            "representative_long_meeting_stations":
                representative["long_arc_meeting_stations"],
            "representative_meeting_station_union":
                representative["meeting_station_union"],
            "short_center_type": (
                "MIDPOINT_FIXED"
                if separation % 2 == 0
                else "CENTRAL_EDGE_EXCHANGED"
            ),
            "long_center_type": (
                "MIDPOINT_FIXED"
                if (RING_STATIONS - separation) % 2 == 0
                else "CENTRAL_EDGE_EXCHANGED"
            ),
            "two_arc_time_tie": representative["two_arc_time_tie"],
            "all_11_rotations_exact": rotation_exact,
            "all_11_formula_equal_enumeration": all(
                row["formula_equals_enumeration"] for row in pair_rows
            ),
            "all_11_source_swap_reflection_symmetric": all(
                row["short_meeting_set_reflection_invariant"]
                and row["long_meeting_set_reflection_invariant"]
                for row in pair_rows
            ),
        })
    expected = (
        (1, (1, 5), (0, 1), (6,)),
        (2, (1, 5), (1,), (7, 6)),
        (3, (2, 4), (1, 2), (7,)),
        (4, (2, 4), (2,), (8, 7)),
        (5, (3, 3), (2, 3), (8,)),
    )
    observed = tuple(
        (
            row["separation"],
            row["meeting_times_short_long"],
            row["representative_short_meeting_stations"],
            row["representative_long_meeting_stations"],
        )
        for row in rows
    )
    tie_separations = tuple(
        row["separation"] for row in rows if row["two_arc_time_tie"]
    )
    exact = (
        observed == expected
        and tie_separations == (5,)
        and all(row["all_11_rotations_exact"] for row in rows)
        and all(
            row["all_11_formula_equal_enumeration"] for row in rows
        )
        and all(
            row["all_11_source_swap_reflection_symmetric"]
            for row in rows
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "model":
            "two counterpropagating radius-one graph wavefronts, treated "
            "separately on the two simple arcs joining each source pair",
        "rule_chain": (
            "On an arc v_0,...,v_L, tick t reaches indices k<=t from "
            "v_0 and L-k<=t from v_L.  Intersection therefore first "
            "occurs at t=ceil(L/2), with L-t<=k<=t.  The source-swap "
            "reflection k->L-k fixes an even-arc midpoint or exchanges "
            "an odd-arc central edge.  C11 supplies arc lengths s and "
            "11-s, so their first-meeting times are "
            "(ceil(s/2),ceil((11-s)/2))."
        ),
        "per_separation_table": tuple(rows),
        "simultaneous_two_arc_meeting_separations": tie_separations,
        "theorem":
            "For every unordered pair on C11 at separation s=1..5, the "
            "two arc-wise meetings have the displayed rotation-uniform, "
            "source-swap-symmetric center sets; their times tie at (3,3) "
            "if and only if s=5.",
        "pass": exact,
    }


def render(certificates: dict[str, object], report: dict[str, object]) -> str:
    return "\n".join((
        *(
            f"CERTIFICATE {name} {compact(value)}"
            for name, value in certificates.items()
        ),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )) + "\n"


def run() -> int:
    started = monotonic()
    certificate_a = meeting_theorem_certificate()
    replay_a = meeting_theorem_certificate()
    deterministic = (
        certificate_a == replay_a
        and digest(certificate_a) == digest(replay_a)
    )
    elapsed = monotonic() - started
    certificates = {"A_MEETING_THEOREM": certificate_a}
    report = {
        "cycle": 839,
        "stage": "certificate-A",
        "meeting_times_by_separation": tuple(
            (
                row["separation"],
                row["meeting_times_short_long"],
            )
            for row in certificate_a["per_separation_table"]
        ),
        "unique_tie": certificate_a[
            "simultaneous_two_arc_meeting_separations"
        ],
        "deterministic_replay": deterministic,
        "runtime_seconds": round(elapsed, 6),
        "pass": bool(certificate_a["pass"]) and deterministic,
        "terminal": "CYCLE839_CERTIFICATE_A_HONEST_FAIL",
    }
    if report["pass"]:
        report["terminal"] = "CYCLE839_CERTIFICATE_A_EXACT_PASS"
    output = render(certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE839_CERTIFICATE_A_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
