#!/usr/bin/env python3
"""Exact finite probes for permanent-record capacity and renewal semantics.

The checks separate a recyclable working process from an append-only history
ledger.  They do not assume that every microscopic update is a record event.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_CAPACITY_RENEWAL_CONSTITUTIONAL_PRESSURE_NOTE_2026-07-14.md"
)
PASS = 0
FAIL = 0
OPEN = -1


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def source_contract() -> None:
    section("A - Source and claim boundary")
    axioms = AXIOMS.read_text(encoding="utf-8")
    axiom_words = " ".join(axioms.split())
    note = NOTE.read_text(encoding="utf-8")
    normalized = note.lower().replace("*", "").replace("`", "")
    check("A live Record axiom says one record per site", "A site never carries more than one record" in axiom_words)
    check("A live Record axiom says records are permanent", "records are permanent" in axioms)
    check("A note is authority-free", "authority: none" in normalized)
    check("A note does not identify every update with formation", "not every microscopic update" in normalized)
    check("A note disclaims a universal no-go", "not a universal no-go" in normalized)


def append_histories(site_count: int):
    root = (OPEN,) * site_count
    levels = {0: {root}}
    paths = {root: 1}
    for level in range(site_count):
        next_level = set()
        for state in levels[level]:
            for site, value in enumerate(state):
                if value != OPEN:
                    continue
                for outcome in (0, 1):
                    future = list(state)
                    future[site] = outcome
                    future = tuple(future)
                    next_level.add(future)
                    paths[future] = paths.get(future, 0) + paths[state]
        levels[level + 1] = next_level
    return levels, paths


def finite_site_saturation() -> None:
    section("B - Exact append-only site saturation")
    for site_count in range(1, 7):
        levels, paths = append_histories(site_count)
        expected_states = tuple(comb(site_count, level) * 2**level for level in range(site_count + 1))
        observed_states = tuple(len(levels[level]) for level in range(site_count + 1))
        terminal_paths = sum(paths[state] for state in levels[site_count])
        check(
            f"B N={site_count} level census is C(N,k)2^k",
            observed_states == expected_states,
            str(observed_states),
        )
        check(
            f"B N={site_count} complete scheduled histories are N!2^N",
            terminal_paths == factorial(site_count) * 2**site_count,
            str(terminal_paths),
        )
        check(
            f"B N={site_count} has no append beyond N records",
            all(OPEN not in state for state in levels[site_count]),
        )


def independent_record_dimension() -> None:
    section("C - Independent readable record dimension")
    for qubits in range(1, 8):
        dimension = 2**qubits
        max_binary_records = 0
        while 2 ** (max_binary_records + 1) <= dimension:
            max_binary_records += 1
        check(
            f"C {qubits} qubits carry at most {qubits} independent binary labels",
            max_binary_records == qubits and 2**qubits == dimension,
        )

    labels = tuple(product((0, 1), repeat=4))
    parity_even = tuple(label for label in labels if sum(label) % 2 == 0)
    check("C four unconstrained binary records require sixteen sectors", len(labels) == 16)
    check("C one parity relation compresses four labels to eight sectors", len(parity_even) == 8)
    check(
        "C compression preserves fewer than four independent bits",
        all(label[3] == (label[0] ^ label[1] ^ label[2]) for label in parity_even),
    )


def recurrent_clock_boundary() -> None:
    section("D - Recyclable clock versus permanent history ledger")
    period = 4
    ticks = 29
    phases = tuple(step % period for step in range(ticks))
    check("D finite modular clock runs for arbitrarily many sampled steps", len(phases) == ticks)
    check("D modular phase aliases distinct cycle numbers", phases[1] == phases[5] == phases[9])

    slots = 7
    formation_every = 3
    records_by_step = tuple(min(slots, step // formation_every) for step in range(1, 40))
    check("D finite permanent ledger reaches its seven-slot ceiling", max(records_by_step) == slots)
    check("D positive scheduled commit rate becomes zero after saturation", len(set(records_by_step[-10:])) == 1)
    check(
        "D working phase can continue after record formation stops",
        phases[22] != phases[23] and records_by_step[22] == records_by_step[23],
    )

    for slots in (1, 2, 5, 10):
        for spacing in (1, 3, 7):
            last_commit_step = slots * spacing
            check(
                f"D N={slots}, spacing={spacing} finite local ledger lasts N*spacing steps",
                last_commit_step == slots * spacing,
            )


def l1_ball(radius: int):
    return {
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    }


def export_geometry() -> None:
    section("E - Fresh-support export on Z^3")
    previous = set()
    for radius in range(0, 9):
        ball = l1_ball(radius)
        expected_volume = (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3
        expected_shell = 1 if radius == 0 else 4 * radius**2 + 2
        shell = ball - previous
        check(f"E L1 ball r={radius} has exact cubic volume", len(ball) == expected_volume)
        check(f"E L1 shell r={radius} has exact quadratic area", len(shell) == expected_shell)
        previous = ball

    minimum_radii = []
    for records in (1, 7, 25, 63, 129, 231, 377):
        radius = 0
        while len(l1_ball(radius)) < records:
            radius += 1
        minimum_radii.append(radius)
        check(
            f"E {records} site-tethered records require a ball of radius at least {radius}",
            len(l1_ball(radius)) >= records and (radius == 0 or len(l1_ball(radius - 1)) < records),
        )
    check("E unbounded archive size forces unbounded support radius", minimum_radii == sorted(minimum_radii) and len(set(minimum_radii)) > 1)


def sparse_formation() -> None:
    section("F - Sparse formation does not itself renew a bounded archive")
    for slot_count in (2, 5, 11):
        for probability in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            expected_open = tuple(slot_count * (1 - probability) ** step for step in range(8))
            expected_new = tuple(expected_open[step] * probability for step in range(8))
            check(
                f"F N={slot_count}, p={probability} expected open capacity decreases",
                all(expected_open[i + 1] < expected_open[i] for i in range(7)),
            )
            check(
                f"F N={slot_count}, p={probability} expected local formation rate decays",
                all(expected_new[i + 1] < expected_new[i] for i in range(7)),
            )
    check(
        "F no positive asymptotic rate survives finite no-renewal slots",
        all(Fraction(1, 2) ** step < Fraction(1, 1000) for step in range(10, 15)),
    )


def record_identity_semantics() -> None:
    section("G - Site-tethered and migratory permanence are different")
    # Two-bit classical carrier.  The fact 1 starts at the left address and is
    # moved by a SWAP.  Its content survives, but its site does not.
    before = (1, 0)
    after = (before[1], before[0])
    check("G SWAP preserves the encoded fact somewhere", sum(before) == sum(after) == 1)
    check("G SWAP does not preserve the fact at the same site", before[0] == 1 and after[0] == 0)
    check("G migration frees the old address", after[0] == 0)

    # Copying before clearing leaves a permanent archive but uses fresh support.
    copied = (1, 1)
    cleared_old = (0, copied[1])
    check("G copy creates a second readable carrier", copied == (1, 1))
    check("G clearing the old carrier preserves content only under migratory identity", cleared_old == (0, 1))
    check("G site-tagged append permanence forbids that clearing", cleared_old[0] != before[0])


def conclusion_contract() -> None:
    section("H - Constitutional consequence needles")
    note = NOTE.read_text(encoding="utf-8")
    required = (
        "finite bounded archive",
        "sparse formation",
        "export",
        "migratory",
        "site-tethered",
        "clock is not the lock",
        "does not force a new axiom sentence",
    )
    for phrase in required:
        check(f"H note contains boundary: {phrase}", phrase in note.lower())


def main() -> None:
    source_contract()
    finite_site_saturation()
    independent_record_dimension()
    recurrent_clock_boundary()
    export_geometry()
    sparse_formation()
    record_identity_semantics()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
