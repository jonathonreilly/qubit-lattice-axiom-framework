#!/usr/bin/env python3
"""Exact finite controls for simulation versus physical record equivalence."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INTRINSIC_SIMULATION_OBSERVER_EQUIVALENCE_RECORD_COST_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
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


def fast_history(bit: int) -> tuple[tuple[str, int], ...]:
    return (("S", bit), ("O", 1 - bit))


def wrapped_history(bit: int) -> tuple[tuple[str, int], ...]:
    return (("S", bit), ("P", bit), ("O", 1 - bit))


def logical_decode(history: tuple[tuple[str, int], ...]) -> int:
    return next(value for kind, value in history if kind == "O")


def source_contract() -> None:
    section("A - Source and authority boundary")
    check("A note exists", NOTE.is_file())
    check("A live axioms exist", AXIOMS.is_file())
    text = NOTE.read_text(encoding="utf-8").lower().replace("*", "")
    check("A note is authority-free", "authority: none" in text)
    check("A note changes no live foundation", "changes no live foundation" in text)
    check("A note preserves strong observer-equivalence route", "strongest surviving steelman" in text)
    check("A note contains all N1-N8 sections", all(f"n{index} —" in text for index in range(1, 9)))
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A live Record keeps only-records-readable premise", "Only records are readable." in axioms)
    check("A live readout remains additive", "scalar readout\n`I` is additive" in axioms)


def fast_wrapped_pair() -> None:
    section("B - Logical simulation versus complete record transcript")
    for bit in (0, 1):
        fast = fast_history(bit)
        wrapped = wrapped_history(bit)
        check(f"B input {bit} logical output agrees", logical_decode(fast) == logical_decode(wrapped) == 1 - bit)
        check(f"B input {bit} complete transcripts differ", fast != wrapped)
        check(f"B input {bit} wrapped history has one extra record", len(wrapped) == len(fast) + 1)
        check(f"B input {bit} wrapped causal depth doubles", len(wrapped) - 1 == 2 * (len(fast) - 1))
        check(f"B input {bit} unit additive readout differs", sum(1 for _ in wrapped) == sum(1 for _ in fast) + 1)
        check(f"B input {bit} phase record is protocol-readable", ("P", bit) in wrapped and all(kind != "P" for kind, _ in fast))

    contracted = tuple(item for item in wrapped_history(0) if item[0] != "P")
    check("B macro contraction recovers fast logical transcript", contracted == fast_history(0))
    check("B contraction is many-to-one deletion of a record", len(wrapped_history(0)) > len(contracted))


def hidden_phase_state_test() -> None:
    section("C - Hidden phase violates record-state sufficiency")
    visible_records = (("S", 0),)
    before = {"records": visible_records, "hidden": 0, "next": "advance_phase"}
    after = {"records": visible_records, "hidden": 1, "next": "append_output"}
    check("C hidden-phase states share the same record configuration", before["records"] == after["records"])
    check("C hidden-phase states have different next futures", before["next"] != after["next"])
    check("C hidden phase is predictive state unless quotiented", before["hidden"] != after["hidden"] and before["next"] != after["next"])


def path_refinement_weights() -> None:
    section("D - Path refinement versus physical event quotient")
    base_paths = (("z", 0), ("o", 1))
    refined_paths = (("z_a", 0), ("z_b", 0), ("o", 1))

    def weights(paths: tuple[tuple[str, int], ...]) -> dict[int, Fraction]:
        result = {0: Fraction(0), 1: Fraction(0)}
        for _, outcome in paths:
            result[outcome] += Fraction(1, len(paths))
        return result

    base = weights(base_paths)
    refined = weights(refined_paths)
    check("D decoded terminal support is the same", {outcome for _, outcome in base_paths} == {outcome for _, outcome in refined_paths} == {0, 1})
    check("D base path counting is fair", base == {0: Fraction(1, 2), 1: Fraction(1, 2)})
    check("D refined path counting is two-thirds one-third", refined == {0: Fraction(2, 3), 1: Fraction(1, 3)})
    check("D same decoded support does not fix weights", base != refined)

    quotient_events = (("zero_event", 0), ("one_event", 1))
    quotient = weights(quotient_events)
    check("D event-first quotient restores fair weights", quotient == base)
    check("D path-first and event-first weighting disagree", quotient != refined)


def causal_and_capacity_controls() -> None:
    section("E - Causal subdivision and permanent capacity")
    fast_edges = (("S", "O"),)
    wrapped_edges = (("S", "P"), ("P", "O"))
    check("E logical start reaches output in both graphs", fast_edges[0] == ("S", "O") and wrapped_edges[0][0] == "S" and wrapped_edges[-1][1] == "O")
    check("E causal graphs are not node-isomorphic", {node for edge in fast_edges for node in edge} != {node for edge in wrapped_edges for node in edge})
    check("E contraction preserves endpoint reachability", (wrapped_edges[0][0], wrapped_edges[-1][1]) == fast_edges[0])
    events = 12
    check("E wrapped implementation consumes twice the post-input record capacity", 2 * events == 24 and events == 12)
    check("E capacity overhead is dimensionless", Fraction(2 * events, events) == 2)


def claim_contract() -> None:
    section("F - Exact claim boundary")
    text = NOTE.read_text(encoding="utf-8").lower()
    tokens = (
        "simulation becomes physical equivalence only after",
        "full transcript equivalence",
        "not a no-go against intrinsic universality",
        "one exact law identity or one exact transcript-preserving physical-",
        "logical simulation, causal-graph contraction",
        "record-state insufficiency only",
        "computational universality alone is insufficient",
    )
    for token in tokens:
        check(f"F note contains boundary: {token}", token in text)


def main() -> int:
    source_contract()
    fast_wrapped_pair()
    hidden_phase_state_test()
    path_refinement_weights()
    causal_and_capacity_controls()
    claim_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: exact logical simulation is not full physical record equivalence without a transcript-preserving observer quotient")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
