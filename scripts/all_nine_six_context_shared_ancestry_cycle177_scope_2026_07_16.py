#!/usr/bin/env python3
"""Cycle 177 scope preflight: all-nine/six-context shared ancestry.

This runner fixes the exact finite target and its algebraic census.  It does
not claim that the physical six-context apparatus has been built.
"""

from __future__ import annotations

import ast
import hashlib
from collections import Counter
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CYCLE168 = ROOT / "scripts/peres_mermin_factorized_reference_census_2026_07_16.py"
CYCLE173 = (
    ROOT
    / "scripts/shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16.py"
)
CYCLE173_CHECK = (
    ROOT
    / "scripts/shared_ancestry_dual_context_cycle173_port_contract_check_2026_07_16.py"
)
CYCLE173_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SHARED_ANCESTRY_DUAL_CONTEXT_PERES_MERMIN_CYCLE173_NOTE_2026-07-16.md"
)
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ALL_NINE_SIX_CONTEXT_SHARED_ANCESTRY_CYCLE177_SCOPE_NOTE_2026-07-16.md"
)

FROZEN = {
    CYCLE173: "92afd28e4cf8b36b98b90b8cf919e13052716a056c64377396da304cb42acc11",
    CYCLE173_CHECK: "d1fcdd953fd9d6dc35e680b28fd7c1fda4eb542b6aae63521cb7f3a5d8d67c55",
    CYCLE173_NOTE: "6c241e3f19dace1c67ed48199c04627d446dff64c01f4dde0c8ae76be37d0cc4",
}

EXPECTED_CONTEXTS = (
    ("R1", (11, 2, 14), 0),
    ("R2", (0, 3, 4), 0),
    ("R3", (12, 6, 9), 0),
    ("C1", (11, 0, 12), 0),
    ("C2", (2, 3, 6), 0),
    ("C3", (14, 4, 9), 1),
)
PAULI_NAMES = tuple(
    left + right
    for left in "IXYZ"
    for right in "IXYZ"
    if left + right != "II"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contexts_from_cycle168() -> tuple[object, ...]:
    tree = ast.parse(CYCLE168.read_text(encoding="utf-8"))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "PM_CONTEXTS"
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise ValueError("PM_CONTEXTS not found")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN CYCLE-173 AUTHORITY")
    observed_hashes = {path: sha256(path) for path in FROZEN}
    check(
        "the Cycle-173 runner, contract verifier, and revised note are frozen",
        observed_hashes == FROZEN,
        {path.name: value for path, value in observed_hashes.items()},
    )

    print("\nEXACT SIX-CONTEXT TARGET")
    contexts = contexts_from_cycle168()
    check(
        "Cycle 168 supplies the exact declared Peres-Mermin square",
        contexts == EXPECTED_CONTEXTS,
        contexts,
    )
    incidence = Counter(
        measurement_id
        for _label, ids, _sign in contexts
        for measurement_id in ids
    )
    row_incidence = Counter(
        measurement_id
        for _label, ids, _sign in contexts[:3]
        for measurement_id in ids
    )
    column_incidence = Counter(
        measurement_id
        for _label, ids, _sign in contexts[3:]
        for measurement_id in ids
    )
    check(
        "nine observables occur exactly once in a row and once in a column",
        len(incidence) == 9
        and set(incidence.values()) == {2}
        and row_incidence == column_incidence
        and set(row_incidence.values()) == {1},
        {
            PAULI_NAMES[index]: incidence[index]
            for index in sorted(incidence)
        },
    )

    occurrences = {
        measurement_id: tuple(
            (label, port_role)
            for label, ids, _sign in contexts
            for port_role, candidate in zip(("g1", "g2", "p"), ids, strict=True)
            if candidate == measurement_id
        )
        for measurement_id in sorted(incidence)
    }
    check(
        "the physical target is exactly eighteen source-to-context branches",
        len(occurrences) == 9
        and all(len(value) == 2 for value in occurrences.values()),
        {
            PAULI_NAMES[index]: value
            for index, value in occurrences.items()
        },
    )

    print("\nFULLY PORTED MEMBERSHIP LOWER INVENTORY")
    leaves = {"g1": 6, "g2": 6, "p": 15}
    splitters = {label: count - 1 for label, count in leaves.items()}
    check(
        "one fully ported context needs 27 leaves and 24 comb splitters",
        sum(leaves.values()) == 27
        and sum(splitters.values()) == 24
        and 6 * sum(leaves.values()) == 162
        and 6 * sum(splitters.values()) == 144,
        {"leaves": leaves, "splitters": splitters},
    )
    check(
        "nine binary source forks add exactly nine upstream splitters",
        len(occurrences) == 9,
        {
            "context_comb_splitters": 144,
            "shared_source_splitters": 9,
            "architectural_total_before_output_join": 153,
        },
    )

    print("\nEXHAUSTIVE SHARED-SIGN CENSUS")
    observable_ids = tuple(sorted(incidence))
    support_histogram: Counter[int] = Counter()
    output_patterns: Counter[tuple[int, ...]] = Counter()
    for assignment in product((0, 1), repeat=len(observable_ids)):
        signs = dict(zip(observable_ids, assignment, strict=True))
        outputs = tuple(
            int(
                (
                    signs[ids[0]]
                    ^ signs[ids[1]]
                    ^ signs[ids[2]]
                )
                == expected_unsigned_sign
            )
            for _label, ids, expected_unsigned_sign in contexts
        )
        support_histogram[sum(outputs)] += 1
        output_patterns[outputs] += 1
    check(
        "all 512 shared sign assignments satisfy exactly one, three, or five contexts",
        support_histogram == Counter({1: 96, 3: 320, 5: 96}),
        support_histogram,
    )
    check(
        "no shared sign assignment satisfies all six context terminals",
        not any(sum(pattern) == 6 for pattern in output_patterns)
        and sum(output_patterns.values()) == 512,
        {
            "patterns": len(output_patterns),
            "all_six": sum(
                count
                for pattern, count in output_patterns.items()
                if sum(pattern) == 6
            ),
        },
    )

    print("\nSCOPE GATE")
    normalized = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "not yet a physical contextuality certificate",
        "not a no-classical-memory theorem",
        "not an instrument-equivalence theorem",
        "no axiom conclusion follows",
        "### n1",
        "### n2",
        "### n3",
        "### n4",
        "### n5",
        "### n6",
        "### n7",
        "### n8",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check(
        "the Cycle-177 scope keeps the operational contextuality seam open",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("CONTEXTS", contexts)
    print("OCCURRENCES", occurrences)
    print("SUPPORT_HISTOGRAM", support_histogram)
    print("OUTPUT_PATTERNS", len(output_patterns))
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CYCLE177_SCOPE_FIXED" if FAIL == 0 else "CYCLE177_SCOPE_OPEN")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
