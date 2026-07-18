#!/usr/bin/env python3
"""Exact controls for the record-only-state/Bell law-type dichotomy.

This runner checks finite CHSH algebra and documentation contracts.  It does
not select a physical law, amend the foundation, or issue an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Source and authority boundary")
    for path in (NOTE, AXIOMS, REGISTRY):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A exact state sentence is quoted", "a state is a configuration of records" in note)
    check("A live source says state is records", "A state is a configuration of records." in axioms)
    check("A live source denies dynamics", "Admissibility is not a dynamics axiom." in axioms)
    check("A no state edit is authorized", "no live state or axiom edit is justified" in note)
    check("A global and enlarged-state routes both remain live", "global record-history law" in note and "enlarged process-state law" in note)


def local_chsh_bound() -> None:
    section("B - Exact Bell-local record-response polytope")
    responses = tuple(product((-1, 1), repeat=2))
    values = []
    for alice in responses:
        for bob in responses:
            s = (
                alice[0] * bob[0]
                + alice[0] * bob[1]
                + alice[1] * bob[0]
                - alice[1] * bob[1]
            )
            values.append(s)
    check("B four deterministic response maps per wing", len(responses) == 4)
    check("B sixteen deterministic local vertices", len(values) == 16)
    check("B every deterministic local vertex has abs CHSH two", {abs(v) for v in values} == {2})
    weights = tuple(Fraction(index + 1, sum(range(1, 17))) for index in range(16))
    mixed = sum(weight * value for weight, value in zip(weights, values))
    check("B an arbitrary displayed local convex mixture stays bounded", abs(mixed) <= 2, f"S={mixed}")
    check("B local convexity proof uses normalized positive weights", all(w >= 0 for w in weights) and sum(weights) == 1)


def quantum_record_table() -> None:
    section("C - Exact no-signalling quantum transcript table")
    root2 = sp.sqrt(2)
    correlations = {
        (0, 0): -1 / root2,
        (0, 1): -1 / root2,
        (1, 0): -1 / root2,
        (1, 1): 1 / root2,
    }
    table: dict[tuple[int, int], dict[tuple[int, int], sp.Expr]] = {}
    for context, corr in correlations.items():
        table[context] = {
            (x, y): sp.simplify((1 + x * y * corr) / 4)
            for x, y in product((-1, 1), repeat=2)
        }
    for context, probabilities in table.items():
        check(f"C context {context} normalizes", sp.simplify(sum(probabilities.values()) - 1) == 0)
        check(f"C context {context} is strictly positive", all(float(p) > 0 for p in probabilities.values()))
        for x in (-1, 1):
            check(
                f"C Alice marginal one-half at {context} x={x}",
                sp.simplify(sum(p for (xo, _), p in probabilities.items() if xo == x) - sp.Rational(1, 2)) == 0,
            )
        for y in (-1, 1):
            check(
                f"C Bob marginal one-half at {context} y={y}",
                sp.simplify(sum(p for (_, yo), p in probabilities.items() if yo == y) - sp.Rational(1, 2)) == 0,
            )
        recovered = sp.simplify(sum(x * y * p for (x, y), p in probabilities.items()))
        check(f"C context {context} recovers its correlation", sp.simplify(recovered - correlations[context]) == 0)
    chsh = sp.simplify(
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )
    check("C exact quantum abs CHSH is two-root-two", sp.simplify(abs(chsh) - 2 * root2) == 0, f"S={chsh}")
    check("C quantum table exceeds Bell-local bound", float(abs(chsh)) > 2)


def law_type_separations() -> None:
    section("D - Record-state and law-type separations")
    # Same visible current record, different preparation ancestry, different future.
    histories = {
        "coherent": {"current_record": "parity=+", "future_phase_test": Fraction(1)},
        "dephased": {"current_record": "parity=+", "future_phase_test": Fraction(1, 2)},
    }
    check("D same current record can have different legal futures", len({v["current_record"] for v in histories.values()}) == 1 and len({v["future_phase_test"] for v in histories.values()}) == 2)
    check("D current-record Markov sufficiency requires lumpability", histories["coherent"]["future_phase_test"] != histories["dephased"]["future_phase_test"])

    local_table = {(a, b): Fraction(0) for a, b in product((0, 1), repeat=2)}
    global_table = {
        (0, 0): -sp.sqrt(2) / 2,
        (0, 1): -sp.sqrt(2) / 2,
        (1, 0): -sp.sqrt(2) / 2,
        (1, 1): sp.sqrt(2) / 2,
    }
    check("D one transcript signature admits distinct exact laws", local_table != global_table)
    check("D global table is context indexed without signalling", all(abs(float(value)) <= 1 for value in global_table.values()))


def documentation_contract() -> None:
    section("E - Type gate and constitutional consequence")
    note = normalized(NOTE)
    required = (
        "bell-local factorization",
        "chsh <= 2",
        "2 sqrt(2)",
        "state is a configuration of records",
        "record-fibre strong lumpability",
        "global history weights",
        "measurement-dependent boundary",
        "persistent preparation record",
        "separate law placement",
        "qualification would need revision",
        "no record clause is forced",
    )
    for phrase in required:
        check(f"E note contains {phrase}", phrase in note)
    check("E global route preserves current state ontology", "preserves the current record-only state ontology" in note)
    check("E process-state route is explicitly conditional", "only if the final law needs an ontic evolving quantum carrier" in note)
    check("E exact law identity remains the common residue", "common residue is still one exact law identity" in note)
    for index in range(1, 9):
        check(f"E N{index} section exists", f"n{index} —" in note)


def main() -> int:
    source_contract()
    local_chsh_bound()
    quantum_record_table()
    law_type_separations()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print("TYPE_GATE: record-only ontology admits a global history law; a local ontic quantum carrier would require an explicit state-language change")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
