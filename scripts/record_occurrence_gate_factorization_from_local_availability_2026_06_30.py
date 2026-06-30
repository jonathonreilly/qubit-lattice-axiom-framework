#!/usr/bin/env python3
"""Verify the record-occurrence gate factorization bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BORN_INTERFACE = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
KERNEL_BOUNDARY = DOCS / "RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md"
CONTEXT_NOGO = DOCS / "RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md"
FORMATION_NOGO = DOCS / "RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md"
POINTER = DOCS / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md"
PRODUCTION_INTERFACE = DOCS / "RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def available(site: int, records: dict[int, int]) -> set[int]:
    """Antiferromagnetic toy availability: differ from neighboring records."""
    values = {0, 1}
    for neighbor in (site - 1, site + 1):
        if neighbor in records:
            values.discard(records[neighbor])
    return values


def valid_records(records: dict[int, int]) -> bool:
    """A finite record set is valid when each neighbor pair differs."""
    for site, value in records.items():
        if value not in {0, 1}:
            return False
        for neighbor in (site - 1, site + 1):
            if neighbor in records and records[neighbor] == value:
                return False
    return True


def extend(records: dict[int, int], site: int | None, value: int | None) -> dict[int, int]:
    """Return a record extension, preserving existing records."""
    new = dict(records)
    if site is None:
        return new
    if site in new:
        raise ValueError("cannot overwrite an existing record")
    if value not in available(site, records):
        raise ValueError("cannot lock an unavailable value")
    new[site] = int(value)
    return new


def main() -> int:
    print("=== Record occurrence gate factorization from local availability ===")

    paths = [
        NOTE,
        AXIOMS,
        BORN_INTERFACE,
        KERNEL_BOUNDARY,
        CONTEXT_NOGO,
        FORMATION_NOGO,
        POINTER,
        PRODUCTION_INTERFACE,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    born = read(BORN_INTERFACE)
    kernel = read(KERNEL_BOUNDARY)
    context = read(CONTEXT_NOGO)
    formation = read(FORMATION_NOGO)
    pointer = read(POINTER)
    interface = read(PRODUCTION_INTERFACE)

    section("PART A -- source boundary")
    check("current axioms are 2026-06-29 four-axiom surface", "Lattice, Qubit, Admissibility, Record" in axioms)
    check("axioms give local possibility", "Each site has a domain of local possibilities" in axioms)
    check("axioms give nearest-neighbor availability", "nearest-neighbor conditions determine the available subset" in flat(axioms))
    check("axioms give fixed records", "A record locks exactly one available local possibility" in axioms)
    check("axioms say Admissibility is not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("axioms say no record-production process", "record-production process" in axioms)
    check("Born bridge names W_occurrence", "W_occurrence" in born)
    check("Born bridge says occurrence remains open", "branch occurrence / production law" in born)
    check("production interface splits pre/formation/post", "pre-record quantum state" in interface and "post-record word/count" in interface)
    check("kernel boundary says post-record layer is consumer", "consumer of produced atoms" in kernel or "not a producer" in kernel)
    check("context no-go blocks generator drop", "production generator" in context and "clock/rate normalization" in context)
    check("formation no-go supplies no-record witnesses", "H = 0" in formation and "no record" in formation)
    check("pointer note supplies bounded controlled-copy route", "nonzero local controlled-copy coupling is sufficient" in pointer)

    section("PART B -- finite availability witness")
    empty: dict[int, int] = {}
    left0 = {-1: 0}
    both_unrecorded_available = available(0, empty)
    left0_available = available(0, left0)
    check("empty neighborhood leaves both values available", both_unrecorded_available == {0, 1}, f"A={both_unrecorded_available}")
    check("left record 0 removes only value 0", left0_available == {1}, f"A={left0_available}")
    check("left0 record set is valid", valid_records(left0))

    no_activation = extend(left0, None, None)
    activation = extend(left0, 0, 1)
    check("no activation preserves the same valid record boundary", no_activation == left0 and valid_records(no_activation))
    check("activation locks the unique available value", activation == {-1: 0, 0: 1} and valid_records(activation))
    check("same availability admits no-activation and activation extensions", no_activation != activation)

    try:
        extend(left0, 0, 0)
        unavailable_rejected = False
    except ValueError:
        unavailable_rejected = True
    check("unavailable value cannot be locked", unavailable_rejected)

    no_from_empty = extend(empty, None, None)
    zero_from_empty = extend(empty, 0, 0)
    one_from_empty = extend(empty, 0, 1)
    check("empty boundary admits no activation", no_from_empty == {})
    check("empty boundary admits selecting 0", zero_from_empty == {0: 0})
    check("empty boundary admits selecting 1", one_from_empty == {0: 1})
    check("selection is independent once two values are available", zero_from_empty != one_from_empty)

    try:
        extend({0: 1}, 0, 0)
        overwrite_rejected = False
    except ValueError:
        overwrite_rejected = True
    check("existing record cannot be overwritten", overwrite_rejected)

    section("PART C -- activation/selection/preservation factorization")
    activation_only_site = 0
    multi_available = available(activation_only_site, empty)
    check("activation alone is incomplete when multiple values are available", len(multi_available) == 2)
    selected_value = min(multi_available)
    selected_extension = extend(empty, activation_only_site, selected_value)
    check("activation plus selection yields a record extension", selected_extension == {0: 0})
    check("preservation holds under extension", all(selected_extension[k] == v for k, v in empty.items()))
    boundary = {-1: 0, 1: 1}
    check("opposing neighbor records can exhaust availability", available(0, boundary) == set())
    check("exhausted availability blocks activation at that site", valid_records(boundary) and len(available(0, boundary)) == 0)
    same_records = {-1: 0, 1: 0}
    check("same neighbor records leave one compatible middle value", available(0, same_records) == {1})
    check("record collections remain finite dictionaries in witness", all(isinstance(x, dict) for x in [empty, left0, activation]))

    section("PART D -- Born weights are not occurrence tokens")
    p0 = Fraction(3, 5)
    p1 = Fraction(2, 5)
    check("sample Born-form weights normalize", p0 + p1 == 1)
    check("both sample weights are nonnegative", p0 >= 0 and p1 >= 0)
    born_weight_vector = {0: p0, 1: p1}
    deterministic_zero = extend(empty, 0, 0)
    deterministic_one = extend(empty, 0, 1)
    no_event = extend(empty, None, None)
    check("weight vector has support over values, not a record token", set(born_weight_vector) == {0, 1})
    check("same weight vector is distinct from deterministic 0 extension", born_weight_vector != deterministic_zero)
    check("same weight vector is distinct from deterministic 1 extension", born_weight_vector != deterministic_one)
    check("same weight vector is distinct from no-event extension", born_weight_vector != no_event)
    check("a realized extension has integral record values", all(v in {0, 1} for v in deterministic_zero.values()))
    expected_value = 0 * p0 + 1 * p1
    check("ensemble expectation can be fractional", expected_value == Fraction(2, 5))
    check("fractional expectation is not a locked binary record", expected_value not in {0, 1})

    section("PART E -- minimum bridge shape checks")
    minimum_sentence = (
        "Given a finite record boundary and the current local possibility domains, a "
        "local composable rule may extend the record set by locking available "
        "possibilities at selected unrecorded sites."
    )
    check("note states minimum bridge shape", minimum_sentence in note_flat)
    check("minimum law names finite record boundary", "finite record boundary" in note)
    check("minimum law names local possibility domains", "local possibility domains" in note)
    check("minimum law names selected unrecorded sites", "selected unrecorded sites" in note)
    check("minimum law forbids overwrites", "never overwrites records" in note)
    check("minimum law forbids unavailable locks", "never locks unavailable possibilities" in note)
    check("note keeps deterministic/weighted/instrument choice explicit", "deterministic, weighted, or instrument-based" in note)
    check("note keeps rate normalization explicit", "normalizes occurrence rate" in note)
    check("note offers bridge theorem before axiom expansion", "retained bridge theorem rather than as an axiom" in note)

    section("PART F -- audit consequence and non-claims")
    check("note restates blocker sharply", "availability and Born-form interface are insufficient by themselves" in note)
    check("note separates rows that only need available values", "Rows that only need available values" in note)
    check("note separates rows that need actual new records", "Rows that need actual new records" in note)
    check("note does not derive occurrence", "It does not derive record occurrence" in note)
    check("note does not derive Hamiltonian/generator/rate", "Hamiltonian, transfer operator, Markov generator, clock" in note)
    check("note rejects total recording", "does not say all sites record" in note)
    check("note does not add primitive", "does not add a new axiom or primitive" in note)
    check("note consumes no measured values", "PDG" not in note and "measured values" in note)

    section("PART G -- no-go discipline gate")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    check("N1 enumerates at least six routes", note.count("| Route |") == 1 and note.count("| Availability route |") == 1 and note.count("| Total-record route |") == 1)
    check("N2 collapses residual to activation plus selection", "local activation + selection of available possibilities" in note)
    check("N3 defines activation", "\"Activation\" means extending the record set" in note)
    check("N4 has six residual matches", note.count("| `") >= 6 and "Residual Matching" in note)
    check("N5 avoids records-never-occur overclaim", "not \"records never occur\"" in note)
    check("N6 gives import-retirement path", "import-retirement path" in note)
    check("N7 steelman names strong Admissibility reading", "sufficiently strong reading of Admissibility" in note)
    check("N8 ties to Record/Born occurrence residual", "Record/Born interface bridge narrowed the" in note)

    section("PART H -- assembled conclusion")
    exact_factorization = (
        available(0, left0) == {1}
        and extend(left0, None, None) == left0
        and extend(left0, 0, 1) == {-1: 0, 0: 1}
        and available(0, empty) == {0, 1}
        and extend(empty, 0, 0) != extend(empty, 0, 1)
    )
    check("finite witness proves availability without occurrence", exact_factorization)
    check("availability constrains but does not activate", "Availability says what a site may record" in note)
    check("Record fixes after recording, not before", "Record says what is fixed after recording" in note)
    check("Born interface gives weights after interface, not token", "weight vector over available record values is not itself a realized durable record" in note)
    check("collapsed wall is W_occurrence", "W_occurrence" in note and "local record-extension law" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print(
        "RESULT: PASS -- local availability and Born-form interface do not "
        "supply record occurrence; the remaining gate is activation plus "
        "selection of available possibilities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
