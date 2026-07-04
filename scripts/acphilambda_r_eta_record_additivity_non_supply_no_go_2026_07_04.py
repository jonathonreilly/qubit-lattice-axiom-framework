#!/usr/bin/env python3
"""Verifier for AC R-eta Record-additivity non-supply no-go."""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_RECORD_ADDITIVITY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
ANGLE_NOGO = DOCS / "ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md"
DELTA_CHAIN = DOCS / "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md"
FIXED = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def powerset(items: tuple[str, ...]) -> list[frozenset[str]]:
    out: list[frozenset[str]] = []
    for size in range(len(items) + 1):
        for combo in itertools.combinations(items, size):
            out.append(frozenset(combo))
    return out


def additive_total(values: dict[str, sp.Expr], records: frozenset[str]) -> sp.Expr:
    return sp.simplify(sum(values[item] for item in records))


def is_additive(values: dict[str, sp.Expr], records: tuple[str, ...]) -> bool:
    subsets = powerset(records)
    for left in subsets:
        for right in subsets:
            if left & right:
                continue
            lhs = additive_total(values, left | right)
            rhs = additive_total(values, left) + additive_total(values, right)
            if sp.simplify(lhs - rhs) != 0:
                return False
    return additive_total(values, frozenset()) == 0


def ledger_row_by_note_path(note_path: str) -> dict:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == note_path]
    if len(matches) != 1:
        raise AssertionError(f"{note_path}: expected 1 row, got {len(matches)}")
    return matches[0]


def main() -> int:
    print("AC_phi_lambda R-eta Record-additivity non-supply no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    tier = json.loads(TIER_A.read_text(encoding="utf-8"))
    angle = ANGLE_NOGO.read_text(encoding="utf-8")
    delta = DELTA_CHAIN.read_text(encoding="utf-8")
    fixed = FIXED.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)
    delta_flat = flat(delta)
    angle_flat = flat(angle)
    fixed_flat = flat(fixed)

    section("A - source and registry boundaries")

    for path in [NOTE, MINIMAL, TIER_A, LEDGER, ANGLE_NOGO, DELTA_CHAIN, FIXED, REGISTRY]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition retains R-eta",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("registry prose names density-read-as-angle", "density-read-as-angle" in registry_flat)
    check("note denies AC retirement", "AC_phi_lambda is not retired" in note)
    check("note denies registry edits", "does not edit any Tier-A registry" in note_flat)
    check("note keeps future readout-context routes open", "future readout-context theorem is not ruled out" in note)

    section("B - Record axiom surface")

    record_needles = [
        "Only records are readable",
        "A readout value is determined by record content alone",
        "scalar readout `I` is additive",
        "I(empty)=0",
    ]
    for needle in record_needles:
        check(f"minimal axioms contain Record clause: {needle}", needle in minimal_flat)

    excluded_needles = [
        "readout-context selection",
        "P2/modulus",
        "log-det",
        "source/action",
        "physical-observable identification",
        "formation rules",
    ]
    for needle in excluded_needles:
        check(f"minimal axioms keep outside content outside: {needle}", needle in minimal_flat)

    check("minimal axioms explicitly leave AC outside", "AC_phi_lambda" in minimal)
    check("minimal axioms explicitly leave theta outside", "strong-CP theta admission" in minimal)

    section("C - fixed-locus arithmetic witness")

    omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    denominator_1 = sp.simplify((1 - omega) * (1 - omega**2))
    denominator_2 = sp.simplify((1 - omega**2) * (1 - omega**4))
    term_1 = sp.simplify(1 / denominator_1)
    term_2 = sp.simplify(1 / denominator_2)
    density = sp.simplify((term_1 + term_2) / 3)
    check("(1 - omega)(1 - omega^2) = 3", sp.simplify(denominator_1 - 3) == 0, denominator_1)
    check("second summand denominator also equals 3", sp.simplify(denominator_2 - 3) == 0, denominator_2)
    check("each raw fixed-locus summand is 1/3", term_1 == sp.Rational(1, 3) and term_2 == sp.Rational(1, 3))
    check("averaged fixed-locus density is 2/9", density == sp.Rational(2, 9), density)
    check(
        "delta chain isolates R-eta as conditional input",
        (
            "R-eta is a dimensionless readout-class" in delta_flat
            or "R-eta is the named conditional input" in delta_flat
            or "R-\u03b7 is a dimensionless readout-class" in delta_flat
            or "R-\u03b7 is the named conditional" in delta_flat
        ),
    )
    check(
        "fixed-locus note carries 2/9 arithmetic",
        "2/9" in fixed_flat and ("fixed-locus" in fixed_flat or "fixed locus" in fixed_flat),
    )

    section("D - additive readout model family")

    records = ("j1", "j2")
    readouts: dict[str, dict[str, sp.Expr]] = {
        "direct_density": {"j1": sp.Rational(1, 9), "j2": sp.Rational(1, 9)},
        "cycle_angle_sum": {"j1": sp.Rational(1, 3), "j2": sp.Rational(1, 3)},
        "two_pi_packaging": {"j1": 2 * sp.pi / 9, "j2": 2 * sp.pi / 9},
        "count": {"j1": sp.Integer(1), "j2": sp.Integer(1)},
        "zero": {"j1": sp.Integer(0), "j2": sp.Integer(0)},
    }
    totals = {name: additive_total(values, frozenset(records)) for name, values in readouts.items()}
    expected = {
        "direct_density": sp.Rational(2, 9),
        "cycle_angle_sum": sp.Rational(2, 3),
        "two_pi_packaging": 4 * sp.pi / 9,
        "count": sp.Integer(2),
        "zero": sp.Integer(0),
    }
    for name, values in readouts.items():
        check(f"{name} is additive over disjoint record collections", is_additive(values, records))
        check(f"{name} total is expected", sp.simplify(totals[name] - expected[name]) == 0, totals[name])

    pairwise_different = True
    for left, right in itertools.combinations(totals, 2):
        pairwise_different = pairwise_different and sp.simplify(totals[left] - totals[right]) != 0
    check("same record collection supports mutually different additive readouts", pairwise_different, totals)
    check("direct density and cycle-angle readings disagree", totals["direct_density"] != totals["cycle_angle_sum"])
    check("direct density and 2*pi packaging disagree", sp.simplify(totals["direct_density"] - totals["two_pi_packaging"]) != 0)
    check("cycle-angle and count readings disagree", totals["cycle_angle_sum"] != totals["count"])
    check("zero reading satisfies additivity but misses R-eta", totals["zero"] == 0 and totals["zero"] != totals["direct_density"])

    section("E - non-supply conclusion")

    check("Record additivity only fixes form after map is fixed", "once the record-content-to-scalar map is fixed" in note)
    check("note states Record does not select map", "It does not select the map" in note)
    check("note states separate bridge is required", "requires a separate readout-context theorem" in note_flat)
    check("Block05 leaves Record-facing theorem live", "Record-facing inhomogeneous readout theorem" in angle)
    check("Block05 says Phi=S_sum is live only as license target", "live R-eta license" in angle)
    check("new note is a source-side bounded no-go", "**Claim type:** no_go" in note and "source-side bounded no-go" in note)

    banned = [
        "R-eta is derived",
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "Tier-A registry is edited",
        "Record derives R-eta",
        "all future readout-context routes are closed",
        "audited_clean",
        "retained_no_go",
    ]
    found = [phrase for phrase in banned if phrase in note]
    check("banned overclaim phrases are absent", not found, found)

    section("F - ledger dependency sanity")

    dependency_expectations = {
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md": "retained_bounded",
        "docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md": "unaudited",
        "docs/KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md": "unaudited",
    }
    for note_path, effective_status in dependency_expectations.items():
        row = ledger_row_by_note_path(note_path)
        check(f"{note_path} effective status is {effective_status}", row.get("effective_status") == effective_status, row.get("effective_status"))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
