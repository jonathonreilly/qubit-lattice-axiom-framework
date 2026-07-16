#!/usr/bin/env python3
"""Independent verifier for the Cycle-168 factorized Peres--Mermin census.

The independent side uses named Pauli strings and an explicit one-qubit
multiplication table.  It does not import the tableau implementation used by
the primary census.  The primary census is then run in a subprocess so its
firewall and exact executable evidence are checked without sharing mutable
module state with this verifier.
"""

from __future__ import annotations

import ast
import os
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts/peres_mermin_factorized_reference_census_2026_07_16.py"
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PERES_MERMIN_FACTORIZED_REFERENCE_CENSUS_CYCLE168_NOTE_2026-07-16.md"
)

PAULIS = tuple(
    left + right
    for left in "IXYZ"
    for right in "IXYZ"
    if left + right != "II"
)
CONTEXTS = (
    ("R1", ("ZI", "IZ", "ZZ"), 1),
    ("R2", ("IX", "XI", "XX"), 1),
    ("R3", ("ZX", "XZ", "YY"), 1),
    ("C1", ("ZI", "IX", "ZX"), 1),
    ("C2", ("IZ", "XI", "XZ"), 1),
    ("C3", ("ZZ", "XX", "YY"), -1),
)
ONE_QUBIT_PRODUCT = {
    ("I", "I"): (0, "I"),
    ("I", "X"): (0, "X"),
    ("I", "Y"): (0, "Y"),
    ("I", "Z"): (0, "Z"),
    ("X", "I"): (0, "X"),
    ("Y", "I"): (0, "Y"),
    ("Z", "I"): (0, "Z"),
    ("X", "X"): (0, "I"),
    ("Y", "Y"): (0, "I"),
    ("Z", "Z"): (0, "I"),
    ("X", "Y"): (1, "Z"),
    ("Y", "X"): (3, "Z"),
    ("Y", "Z"): (1, "X"),
    ("Z", "Y"): (3, "X"),
    ("Z", "X"): (1, "Y"),
    ("X", "Z"): (3, "Y"),
}

SignedPauli = tuple[int, str]
StabilizerGroup = frozenset[SignedPauli]

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


def commute(left: str, right: str) -> bool:
    local_anticommutations = sum(
        a != "I" and b != "I" and a != b
        for a, b in zip(left, right, strict=True)
    )
    return local_anticommutations % 2 == 0


def multiply(left: SignedPauli, right: SignedPauli) -> SignedPauli:
    left_sign, left_name = left
    right_sign, right_name = right
    exponent = (0 if left_sign == 1 else 2) + (
        0 if right_sign == 1 else 2
    )
    letters = []
    for left_letter, right_letter in zip(
        left_name,
        right_name,
        strict=True,
    ):
        phase, letter = ONE_QUBIT_PRODUCT[(left_letter, right_letter)]
        exponent += phase
        letters.append(letter)
    exponent %= 4
    if exponent not in (0, 2):
        raise AssertionError(("non-Hermitian product", left, right, exponent))
    return (1 if exponent == 0 else -1, "".join(letters))


def opposite(record: SignedPauli) -> SignedPauli:
    return -record[0], record[1]


def enumerate_stabilizer_groups() -> tuple[StabilizerGroup, ...]:
    groups = set()
    for first_name, second_name in combinations(PAULIS, 2):
        if not commute(first_name, second_name):
            continue
        for first_sign, second_sign in product((1, -1), repeat=2):
            first = (first_sign, first_name)
            second = (second_sign, second_name)
            third = multiply(first, second)
            if third[1] == "II":
                raise AssertionError(("dependent generators", first, second))
            groups.add(frozenset((first, second, third)))
    return tuple(
        sorted(
            groups,
            key=lambda group: tuple(sorted(group)),
        )
    )


def measure(
    group: StabilizerGroup,
    measured: SignedPauli,
) -> tuple[str, StabilizerGroup | None]:
    if measured in group:
        return "D+", group
    if opposite(measured) in group:
        return "D-", None
    commuting = tuple(
        record for record in group if commute(record[1], measured[1])
    )
    if len(commuting) != 1:
        raise AssertionError(("bad centralizer intersection", group, measured))
    retained = commuting[0]
    updated = frozenset(
        (measured, retained, multiply(measured, retained))
    )
    if len(updated) != 3:
        raise AssertionError(("bad update", group, measured, updated))
    return "A", updated


def independent_stage_census(
    groups: tuple[StabilizerGroup, ...],
) -> Counter[str]:
    census: Counter[str] = Counter()
    for group in groups:
        for name in PAULIS:
            for sign in (1, -1):
                measured = (sign, name)
                kind, _updated = measure(group, measured)
                multiplicity = 6
                census["attempt"] += multiplicity
                if kind == "D+":
                    census["support"] += multiplicity
                    census["commuting"] += multiplicity
                    census["member"] += multiplicity
                elif kind == "D-":
                    census["reject"] += multiplicity
                    census["commuting"] += multiplicity
                    census["opposite"] += multiplicity
                else:
                    census["support"] += multiplicity
                    census["anticommuting"] += multiplicity
    return census


def independent_checker_census() -> Counter[str]:
    census: Counter[str] = Counter()
    unsigned_products: Counter[int] = Counter()
    for _label, names, unsigned_sign in CONTEXTS:
        product_record = multiply(
            multiply((1, names[0]), (1, names[1])),
            (1, names[2]),
        )
        if product_record != (unsigned_sign, "II"):
            raise AssertionError(("bad context product", names, product_record))
        for _order in permutations(range(3)):
            unsigned_products[unsigned_sign] += 1
            for bits in product((0, 1), repeat=3):
                scalar_sign = -1 if sum(bit == 0 for bit in bits) % 2 else 1
                full_sign = scalar_sign * unsigned_sign
                census["attempt"] += 1
                census[
                    "parity_equal"
                    if scalar_sign == unsigned_sign
                    else "parity_different"
                ] += 1
                census[
                    "full_plus" if full_sign == 1 else "full_minus"
                ] += 1
    census["unsigned_plus"] = unsigned_products[1]
    census["unsigned_minus"] = unsigned_products[-1]
    return census


def independent_transcript_census(
    groups: tuple[StabilizerGroup, ...],
) -> tuple[
    Counter[object],
    dict[str, Counter[object]],
    dict[tuple[str, int], Counter[str]],
]:
    global_census: Counter[object] = Counter()
    context_census: dict[str, Counter[object]] = defaultdict(Counter)
    context_order_census: dict[tuple[str, int], Counter[str]] = defaultdict(
        Counter
    )
    for group in groups:
        for label, names, unsigned_sign in CONTEXTS:
            for order_index, order in enumerate(permutations(range(3))):
                for bits in product((0, 1), repeat=3):
                    signed_rows = tuple(
                        (1 if bits[index] else -1, names[index])
                        for index in range(3)
                    )
                    ordered = tuple(signed_rows[index] for index in order)
                    current = group
                    first_reject = None
                    random_steps = 0
                    stage_types = []
                    for step_index, measured in enumerate(ordered, 1):
                        stage_type, updated = measure(current, measured)
                        stage_types.append(stage_type)
                        if stage_type == "D-":
                            first_reject = step_index
                            break
                        if stage_type == "A":
                            random_steps += 1
                        if updated is None:
                            raise AssertionError(("missing update", measured))
                        current = updated

                    supported = first_reject is None
                    scalar_sign = (
                        -1 if sum(bit == 0 for bit in bits) % 2 else 1
                    )
                    relation = (
                        "q_equal_u"
                        if scalar_sign == unsigned_sign
                        else "q_different_u"
                    )
                    multiplicity = 6
                    support_key = "supported" if supported else "rejected"
                    for census in (
                        global_census,
                        context_census[label],
                        context_order_census[(label, order_index)],
                    ):
                        census["attempt"] += multiplicity
                        census[support_key] += multiplicity
                    global_census[relation] += multiplicity
                    context_census[label][relation] += multiplicity
                    if first_reject is not None:
                        global_census[
                            ("first_reject", first_reject)
                        ] += multiplicity
                    if relation == "q_equal_u" and supported:
                        global_census["q_equal_u_supported"] += multiplicity
                        context_census[label][
                            "q_equal_u_supported"
                        ] += multiplicity
                    if relation == "q_equal_u" and not supported:
                        global_census["q_equal_u_rejected"] += multiplicity
                        context_census[label][
                            "q_equal_u_rejected"
                        ] += multiplicity
                    if relation == "q_different_u" and supported:
                        global_census[
                            "q_different_u_supported"
                        ] += multiplicity
                    global_census[
                        "unsigned_plus"
                        if unsigned_sign == 1
                        else "unsigned_minus"
                    ] += multiplicity
                    full_sign = scalar_sign * unsigned_sign
                    global_census[
                        "full_plus" if full_sign == 1 else "full_minus"
                    ] += multiplicity
                    if supported:
                        global_census["terminal_h1"] += multiplicity
                        global_census[
                            "supported_unsigned_plus"
                            if unsigned_sign == 1
                            else "supported_unsigned_minus"
                        ] += multiplicity
                        global_census[
                            "supported_full_plus"
                            if full_sign == 1
                            else "supported_full_minus"
                        ] += multiplicity
                        if len(stage_types) == 3 and stage_types[2] == "D+":
                            global_census[
                                "third_deterministic"
                            ] += multiplicity
                        weight = Fraction(1, 2**random_steps)
                        global_census[("weight", weight)] += multiplicity
                        context_census[label][
                            ("weight", weight)
                        ] += multiplicity
    return global_census, dict(context_census), dict(context_order_census)


def primary_source_failures() -> tuple[object, ...]:
    tree = ast.parse(PRIMARY.read_text(encoding="utf-8"))
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    expected_signature = (
        "initial_basis",
        "ordered_unsigned_rows",
        "ordered_signed_rows",
        "tables",
    )
    transcript = functions.get("factorized_transcript")
    failures: list[object] = []
    if transcript is None:
        failures.append(("missing", "factorized_transcript"))
        return tuple(failures)
    actual_signature = tuple(argument.arg for argument in transcript.args.args)
    if actual_signature != expected_signature:
        failures.append(("signature", actual_signature))

    forbidden = {
        "symplectic",
        "multiply_commuting",
        "tableau_measure",
        "pivot_rows",
        "membership_bits",
        "group_key",
        "STATE_GENERATORS",
        "BRANCH",
    }
    for name, node in functions.items():
        if not (name.startswith("physical_") or name == "factorized_transcript"):
            continue
        for child in ast.walk(node):
            if isinstance(child, ast.Name) and child.id in forbidden:
                failures.append((name, "forbidden-name", child.id))
            if isinstance(child, ast.Attribute) and child.attr in forbidden:
                failures.append((name, "forbidden-attribute", child.attr))
            if isinstance(child, ast.BinOp) and isinstance(
                child.op,
                (ast.BitXor, ast.BitAnd, ast.BitOr),
            ):
                failures.append((name, "direct-host-bit-operator"))
    return tuple(failures)


def run_primary() -> tuple[int, str, str]:
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(ROOT / "scripts")
    completed = subprocess.run(
        [sys.executable, str(PRIMARY)],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    return completed.returncode, completed.stdout, completed.stderr


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    groups = enumerate_stabilizer_groups()
    check(
        "independent named-Pauli construction has exactly 60 states",
        len(groups) == 60,
        len(groups),
    )

    stage = independent_stage_census(groups)
    expected_stage = {
        "attempt": 10_800,
        "support": 9_720,
        "reject": 1_080,
        "anticommuting": 8_640,
        "commuting": 2_160,
        "member": 1_080,
        "opposite": 1_080,
    }
    check(
        "independent 10,800-stage census is exact",
        all(stage[key] == value for key, value in expected_stage.items()),
        dict(stage),
    )

    checker = independent_checker_census()
    expected_checker = {
        "attempt": 288,
        "parity_equal": 144,
        "parity_different": 144,
        "full_plus": 144,
        "full_minus": 144,
        "unsigned_plus": 30,
        "unsigned_minus": 6,
    }
    check(
        "independent 288-case checker census is exact",
        all(checker[key] == value for key, value in expected_checker.items()),
        dict(checker),
    )

    global_census, context_census, context_order_census = (
        independent_transcript_census(groups)
    )
    expected_global = {
        "attempt": 103_680,
        "supported": 38_880,
        "rejected": 64_800,
        ("first_reject", 1): 10_368,
        ("first_reject", 2): 15_552,
        ("first_reject", 3): 38_880,
        "q_equal_u": 51_840,
        "q_different_u": 51_840,
        "q_equal_u_supported": 38_880,
        "q_equal_u_rejected": 12_960,
        "q_different_u_supported": 0,
        "unsigned_plus": 86_400,
        "unsigned_minus": 17_280,
        "full_plus": 51_840,
        "full_minus": 51_840,
        "terminal_h1": 38_880,
        "supported_unsigned_plus": 32_400,
        "supported_unsigned_minus": 6_480,
        "supported_full_plus": 38_880,
        "supported_full_minus": 0,
        "third_deterministic": 38_880,
        ("weight", Fraction(1, 4)): 27_648,
        ("weight", Fraction(1, 2)): 10_368,
        ("weight", Fraction(1, 1)): 864,
    }
    check(
        "independent 103,680-transcript global census is exact",
        all(
            global_census[key] == value
            for key, value in expected_global.items()
        ),
        {str(key): global_census[key] for key in expected_global},
    )

    expected_context = {
        "attempt": 17_280,
        "supported": 6_480,
        "rejected": 10_800,
        "q_equal_u": 8_640,
        "q_different_u": 8_640,
        "q_equal_u_supported": 6_480,
        "q_equal_u_rejected": 2_160,
        ("weight", Fraction(1, 4)): 4_608,
        ("weight", Fraction(1, 2)): 1_728,
        ("weight", Fraction(1, 1)): 144,
    }
    context_failures = {
        label: {
            str(key): observed[key]
            for key in expected_context
            if observed[key] != expected_context[key]
        }
        for label, observed in context_census.items()
        if any(
            observed[key] != value
            for key, value in expected_context.items()
        )
    }
    check(
        "all six independent context cells have the exact same census",
        not context_failures and len(context_census) == 6,
        context_failures,
    )

    order_failures = {
        str(key): dict(observed)
        for key, observed in context_order_census.items()
        if (
            observed["attempt"],
            observed["supported"],
            observed["rejected"],
        )
        != (2_880, 1_080, 1_800)
    }
    check(
        "all 36 independent context-order cells are 2,880/1,080/1,800",
        not order_failures and len(context_order_census) == 36,
        order_failures,
    )

    source_failures = primary_source_failures()
    check(
        "primary factorized path has the narrow direct-call firewall contract",
        not source_failures,
        source_failures,
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    normalized_note = " ".join(note_text.split())
    required_disclosures = (
        "not a routed row-native physical-membership theorem",
        "not a probability or Born-rule derivation",
        "No axiom conclusion follows",
        "before the dynamic firewall is installed",
        "not an oracle-free synthesis of those tables",
    )
    missing_disclosures = tuple(
        phrase
        for phrase in required_disclosures
        if phrase not in normalized_note
    )
    check(
        "Cycle-168 note states every required scope and provenance boundary",
        not missing_disclosures,
        missing_disclosures,
    )

    returncode, stdout, stderr = run_primary()
    expected_primary_lines = (
        "PASS factorized cache sizes are exact",
        "PASS all 10,800 factorized stages match the tableau oracle",
        "PASS all 288 independent checker cases have corrected semantics",
        "PASS global support, parity, product, and weight census is exact",
        "PASS each of six contexts has the exact same support census",
        "PASS all 36 context-order cells have 2,880/1,080/1,800",
        "PASS basis invariance has 17,280 classes and 86,400 comparisons",
        "PASS order invariance has 17,280 classes and 86,400 comparisons",
        "PASS 38 stage shapes and 76 future-geometry representative keys",
        "PASS 16 FAIL 0",
        "RESULT PERES_MERMIN_FACTORIZED_REFERENCE_CENSUS",
    )
    missing_primary_lines = tuple(
        phrase for phrase in expected_primary_lines if phrase not in stdout
    )
    check(
        "primary exhaustive runner passes with the exact evidence surface",
        returncode == 0 and not missing_primary_lines and not stderr,
        {
            "returncode": returncode,
            "missing": missing_primary_lines,
            "stderr": stderr[-1_000:],
            "stdout_tail": stdout[-1_000:],
        },
    )

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE168_PERES_MERMIN_FACTORIZED_REFERENCE_CENSUS_VERIFIED"
        if FAIL == 0
        else "OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
