#!/usr/bin/env python3
"""Cycle 195: exact finite-context versus effect-complete Born seam.

The runner constructs a normalized, parity-correct, no-disturbance
Peres-Mermin box that has no positive two-qubit density representation.  It
thereby isolates the full-effect/full-frame completion condition used by the
Cycle-20 operational representation theorem.  No axiom or authority surface
is changed.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PERES_MERMIN_EFFECT_COMPLETION_SEAM_CYCLE195_NOTE_2026-07-16.md"
)
CYCLE189_RUNNER = ROOT / "scripts/preterminal_context_quantum_process_cycle189_2026_07_16.py"
CYCLE189_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md"
)
CYCLE20_RUNNER = ROOT / "scripts/operational_quotient_born_affinity_cycle20_2026_07_14.py"
CYCLE20_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
CYCLE194_RUNNER = ROOT / "scripts/cycle189_record_corpus_frequency_bridge_cycle194_2026_07_16.py"
CYCLE194_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CYCLE189_RECORD_CORPUS_FREQUENCY_BRIDGE_CYCLE194_NOTE_2026-07-16.md"
)

FROZEN = {
    CYCLE189_RUNNER: "a06853a529723332c774112d5aad8e53d9a91ad486de70de201cfcb8b501fe34",
    CYCLE189_NOTE: "97c2e98f90cef08063a3589d31555fbe76a18cbbbd3b8fb677c3b03603c54ded",
    CYCLE20_RUNNER: "d5cc88a558b769d1291d4c8da629b2038078d41ca9ad0e0c91542e0a34440724",
    CYCLE20_NOTE: "dfb44a519055f5099ff03f571271ba2e416da705976899ac877e7121551047b4",
    CYCLE194_RUNNER: "10cbf5029bff31dd7977f1529774f550445c6df5ec98724c3610fdd1a9fb9b25",
    CYCLE194_NOTE: "55ff10103b6cbf2f884897af938d36c67fbcb8982a95c8c8492ec831bb8e1ca7",
}

PASS = 0
FAIL = 0

Outcome = tuple[int, int, int]
Distribution = dict[Outcome, Fraction]

BOX_EXPECTATIONS = {
    "IX": Fraction(1),
    "IZ": Fraction(0),
    "XI": Fraction(0),
    "XX": Fraction(0),
    "XZ": Fraction(-1),
    "YY": Fraction(0),
    "ZI": Fraction(0),
    "ZX": Fraction(0),
    "ZZ": Fraction(-1),
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail != "" else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_cycle189():
    spec = spec_from_file_location("cycle189_effect_source", CYCLE189_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Cycle 189")
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def box_distribution(context) -> Distribution:
    first, second, third = context.observables
    distribution: Distribution = {}
    for a in (-1, 1):
        for b in (-1, 1):
            c = context.product_sign * a * b
            weight = (
                Fraction(1)
                + a * BOX_EXPECTATIONS[first]
                + b * BOX_EXPECTATIONS[second]
                + a * b * context.product_sign * BOX_EXPECTATIONS[third]
            ) / 4
            distribution[(a, b, c)] = weight
    return distribution


def occurrence_expectation(
    context,
    distribution: Distribution,
    observable: str,
) -> Fraction:
    index = context.observables.index(observable)
    return sum(
        (Fraction(outcome[index]) * weight for outcome, weight in distribution.items()),
        Fraction(0),
    )


def exact_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN PREDECESSORS")
    observed = {path: digest(path) for path in FROZEN}
    check(
        "Cycle 20, Cycle 189, and Cycle 194 remain frozen",
        observed == FROZEN,
        {path.name: value for path, value in observed.items()},
    )

    cycle189 = load_cycle189()
    boxes = {
        context.label: box_distribution(context)
        for context in cycle189.CONTEXTS
    }

    print("\nFINITE PERES-MERMIN BOX")
    normalization_failures = []
    parity_failures = []
    negativity_failures = []
    for context in cycle189.CONTEXTS:
        distribution = boxes[context.label]
        if sum(distribution.values(), Fraction(0)) != 1:
            normalization_failures.append(context.label)
        for outcome, weight in distribution.items():
            if weight < 0:
                negativity_failures.append((context.label, outcome, weight))
            if outcome[0] * outcome[1] * outcome[2] != context.product_sign:
                parity_failures.append((context.label, outcome))
    check(
        "all six context tables are exact normalized nonnegative distributions",
        not normalization_failures and not negativity_failures,
        {"normalization": normalization_failures, "negative": negativity_failures},
    )
    check(
        "every supported triple obeys the Peres-Mermin signed product",
        not parity_failures,
        parity_failures,
    )

    occurrence_values: dict[str, list[Fraction]] = defaultdict(list)
    for context in cycle189.CONTEXTS:
        for observable in context.observables:
            occurrence_values[observable].append(
                occurrence_expectation(
                    context,
                    boxes[context.label],
                    observable,
                )
            )
    check(
        "both occurrences of every shared observable have one common marginal",
        set(occurrence_values) == set(BOX_EXPECTATIONS)
        and all(
            len(values) == 2
            and values[0] == values[1] == BOX_EXPECTATIONS[observable]
            for observable, values in occurrence_values.items()
        ),
        dict(occurrence_values),
    )

    support_histogram: dict[int, int] = defaultdict(int)
    for distribution in boxes.values():
        support_histogram[sum(weight > 0 for weight in distribution.values())] += 1
    check(
        "the countermodel uses only exact zero and half weights",
        {
            weight
            for distribution in boxes.values()
            for weight in distribution.values()
        }
        == {Fraction(0), Fraction(1, 2)}
        and dict(support_histogram) == {2: 6},
        dict(support_histogram),
    )

    print("\nNO POSITIVE TWO-QUBIT REPRESENTATIVE")
    A = cycle189.OBSERVABLES["IX"]
    B = cycle189.OBSERVABLES["ZZ"]
    C = cycle189.OBSERVABLES["XZ"]
    I4 = cycle189.I4
    plus_A = sp.simplify((I4 + A) / 2)
    check(
        "IX anticommutes with both demanded negative observables",
        exact_zero(A * B + B * A) and exact_zero(A * C + C * A),
        "",
    )
    check(
        "the IX=+1 support projector kills both anticommuting expectations",
        exact_zero(plus_A * B * plus_A)
        and exact_zero(plus_A * C * plus_A),
        "",
    )
    check(
        "the box demands IX=1 together with ZZ=XZ=-1",
        BOX_EXPECTATIONS["IX"] == 1
        and BOX_EXPECTATIONS["ZZ"] == -1
        and BOX_EXPECTATIONS["XZ"] == -1,
        "",
    )

    rho_zero_completion = sp.simplify(
        (
            I4
            + sum(
                (
                    sp.Rational(value.numerator, value.denominator)
                    * cycle189.OBSERVABLES[name]
                    for name, value in BOX_EXPECTATIONS.items()
                ),
                sp.zeros(4),
            )
        )
        / 4
    )
    eigenvalues = rho_zero_completion.eigenvals()
    expected_eigenvalues = {
        (1 - sp.sqrt(3)) / 4: 2,
        (1 + sp.sqrt(3)) / 4: 2,
    }
    check(
        "the canonical Pauli completion is Hermitian trace one but not positive",
        rho_zero_completion.H == rho_zero_completion
        and sp.trace(rho_zero_completion) == 1
        and eigenvalues == expected_eigenvalues
        and (1 - sp.sqrt(3)) / 4 < 0,
        eigenvalues,
    )
    check(
        "no omitted Pauli component can repair the IX-support contradiction",
        exact_zero(plus_A * B * plus_A)
        and BOX_EXPECTATIONS["ZZ"] != 0,
        "",
    )

    print("\nCYCLE-189 POSITIVE CONTROLS")
    positive_failures = []
    table_failures = []
    for preparation, rho in cycle189.PREPARATIONS.items():
        eigen = rho.eigenvals()
        if rho.H != rho or sp.trace(rho) != 1 or any(value < 0 for value in eigen):
            positive_failures.append((preparation, eigen))
        for context in cycle189.CONTEXTS:
            distribution = cycle189.context_outcome_distribution(
                preparation,
                context.label,
            )
            if (
                sp.simplify(sum(distribution.values()) - 1) != 0
                or any(weight.is_nonnegative is not True for weight in distribution.values())
            ):
                table_failures.append((preparation, context.label))
    check(
        "both Cycle-189 preparations are positive trace-one density operators",
        not positive_failures,
        positive_failures,
    )
    check(
        "their twelve Cycle-189 context tables remain normalized and positive",
        not table_failures,
        table_failures,
    )

    print("\nSCOPE AND THEOREM FIREWALL")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required = (
        "finite context consistency is not effect completeness",
        "normalized numerical law remains exact-law content",
        "trace form is mathematical after completion",
        "born trace pairing is reduced, not derived from support",
        "fixed peres–mermin scope",
        "no axiom conclusion follows",
        "## n1",
        "## n2",
        "## n3",
        "## n4",
        "## n5",
        "## n6",
        "## n7",
        "## n8",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check(
        "the note preserves the exact completion boundary and N1-N8 scope",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("CONTEXTS", len(boxes))
    print("SHARED_OBSERVABLES", len(occurrence_values))
    print("SUPPORT_HISTOGRAM", dict(sorted(support_histogram.items())))
    print("BOX_EXPECTATIONS", BOX_EXPECTATIONS)
    print("ZERO_COMPLETION_EIGENVALUES", eigenvalues)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE195_EFFECT_COMPLETION_SEAM_GREEN"
        if FAIL == 0
        else "CYCLE195_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
