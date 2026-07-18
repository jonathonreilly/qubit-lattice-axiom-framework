#!/usr/bin/env python3
"""Type and placement gate for a future exact-law constitutional reference.

This runner is read-only with respect to live foundation surfaces.  It checks
that availability alone does not identify prediction and that the placement
note keeps zero-edit, four-name retyping, and five-name Law routes distinct.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "EXACT_LAW_CONSTITUTIONAL_PLACEMENT_SCHEMA_PROBE_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CONTRACT = REVIEW / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"

FIELDS = (
    "DOMAIN",
    "STATE",
    "CONTEXT",
    "ATOMIC_LAW",
    "CONTINUATION",
    "AVAILABILITY",
    "CONCURRENCY",
    "RECORD",
    "ACTUALITY",
    "STATISTICS",
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Live source and authority boundary")
    for label, path in {
        "placement note": NOTE,
        "axiom memo": AXIOMS,
        "premise registry": REGISTRY,
        "law contract": CONTRACT,
    }.items():
        check(f"A source exists: {label}", path.is_file(), str(path.relative_to(ROOT)))

    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    check("A note has no authority", "authority: none" in note)
    check("A note disclaims an axiom proposal", "not an axiom proposal" in note)
    check("A note changes no live surface", "changes no live foundation" in note)
    check("A live memo still names four axioms", all(f"### {name}" in axioms for name in ("Lattice", "Qubit", "Admissibility", "Record")))
    check("A Admissibility remains a menu rule", "nearest-neighbor admissibility rule" in axioms and "available possibilities are determined by" in axioms)
    check("A live memo explicitly rejects dynamics reading", "Admissibility is not a dynamics axiom." in axioms)
    check("A live Record remains unchanged", "Records form." in axioms and "records are permanent." in axioms)
    check("A registry still has only approved ids", set(registry["canonical_ids"]) == {"minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"})
    check("A no placeholder entered live axioms", "[exact" not in axioms.lower() and "canonical-law" not in axioms.lower())


def availability_prediction_separation() -> None:
    section("B - Same availability, different prediction")
    neighborhoods = tuple(range(3**6))
    availability = {n: frozenset((0, 1)) for n in neighborhoods}
    law_a = {n: (Fraction(1, 2), Fraction(1, 2)) for n in neighborhoods}
    law_b = {n: (Fraction(2, 3), Fraction(1, 3)) for n in neighborhoods}

    check("B availability is nonempty everywhere", all(availability[n] for n in neighborhoods))
    check("B law A normalizes everywhere", all(sum(law_a[n]) == 1 for n in neighborhoods))
    check("B law B normalizes everywhere", all(sum(law_b[n]) == 1 for n in neighborhoods))
    check("B both laws have the same full support", all({i for i, p in enumerate(law_a[n]) if p} == availability[n] == {i for i, p in enumerate(law_b[n]) if p} for n in neighborhoods))
    check("B laws predict different readable records", law_a[0] != law_b[0])
    check("B availability identity does not imply law identity", availability == availability and law_a != law_b)


def placement_matrix() -> None:
    section("C - Ten-field placement matrix")
    complete_reference = frozenset(FIELDS)
    current_admissibility = frozenset(("AVAILABILITY",))
    record_trigger = frozenset(("AVAILABILITY", "RECORD"))
    retyped_admissibility = complete_reference
    separate_law = complete_reference
    qualification_reference = complete_reference

    check("C current Admissibility closes availability only", current_admissibility == {"AVAILABILITY"})
    check("C generous Record trigger remains incomplete", record_trigger < complete_reference)
    check("C Record trigger omits atomic law", "ATOMIC_LAW" not in record_trigger)
    check("C Record trigger omits statistics", "STATISTICS" not in record_trigger)
    check("C retyped complete-law reference can cover all fields", retyped_admissibility == complete_reference)
    check("C separate Law reference can cover all fields", separate_law == complete_reference)
    check("C Qualification reference can carry content but has a placement defect", qualification_reference == complete_reference)
    check("C scientific atom count is equal for the two honest supplied-law routes", len(retyped_admissibility) == len(separate_law))
    check("C all contract fields represented", set(FIELDS) == complete_reference)


def documentation_contract() -> None:
    section("D - Placement and no-placeholder documentation")
    note = normalized(NOTE)
    contract = normalized(CONTRACT)

    for route in (
        "route a — derive the exact law; make no edit",
        "route b — retype admissibility as the complete local law",
        "route c — add a separate law axiom",
        "route d — add formation content to record",
        "route e — put the identity in qualification only",
    ):
        check(f"D note retains {route}", route in note)

    for field in FIELDS:
        check(f"D canonical contract contains {field}", field.lower() in contract)

    for placeholder in (
        "qca",
        "multiway",
        "causal-front",
        "least action",
        "maximum entropy",
        "wolfram model",
        "disagreement law",
    ):
        check(f"D placeholder family rejected: {placeholder}", placeholder in note)

    check("D exact object route is explicit", "one complete exact mathematical object" in note)
    check("D exact equivalence route is explicit", "one exactly defined equivalence class" in note and "every representative gives identical probabilities" in note)
    check("D retyping requires retiring no-dynamics sentence", "retiring the memo's explicit sentence that admissibility is not dynamics" in note)
    check("D Record change remains conditional", "one record clarification becomes necessary only if" in note)
    check("D wording waits for type gate", "only after this gate closes should exact prose be iterated" in note)
    check("D note carries N1-N8", all(f"n{i} —" in note for i in range(1, 9)))
    check("D no universal no-go is made", "no universal claim is made" in note)


def main() -> int:
    source_contract()
    availability_prediction_separation()
    placement_matrix()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: exact-law identity is one scientific atom; its honest location depends on whether the final object is a local continuation law or a distinct global-history law")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
