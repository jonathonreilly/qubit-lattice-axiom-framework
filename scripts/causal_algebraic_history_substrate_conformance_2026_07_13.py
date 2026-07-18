#!/usr/bin/env python3
"""Executable common comparison surface for six substrate families."""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Hashable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CAUSAL_ALGEBRAIC_HISTORY_SUBSTRATE_SPECIFICATION_NOTE_2026-07-13.md"

State = Hashable
Context = str
Record = tuple[Hashable, Hashable]

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FiniteSubstrate:
    name: str
    family: str
    states: tuple[State, ...]
    contexts: tuple[Context, ...]
    successors: dict[tuple[State, Context], tuple[State, ...]]
    records: dict[State, frozenset[Record]]
    joint_dimension: int | None = None
    generated_local_rank: int | None = None
    weights: dict[tuple[State, Context], dict[State, Fraction]] = field(default_factory=dict)
    selection_mode: str = "none"
    availability: dict[tuple[State, Context], frozenset[Hashable]] = field(default_factory=dict)
    formed_content: dict[tuple[State, State, Context], Hashable] = field(default_factory=dict)
    frequency_counts: dict[Hashable, int] = field(default_factory=dict)
    state_type: str = "records"


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def total(model: FiniteSubstrate) -> bool:
    return all(model.successors.get((state, context)) for state in model.states for context in model.contexts)


def declared_generated_composition(model: FiniteSubstrate) -> bool:
    return (
        model.joint_dimension is not None
        and model.generated_local_rank is not None
        and model.joint_dimension == model.generated_local_rank
    )


def record_invariant(model: FiniteSubstrate) -> bool:
    return all(
        model.records[state].issubset(model.records[successor])
        for (state, _), successors in model.successors.items()
        for successor in successors
    )


def future_signature(model: FiniteSubstrate, state: State, horizon: int) -> tuple:
    if horizon == 0:
        return tuple(sorted(model.records[state], key=repr))
    context_rows = []
    for context in model.contexts:
        successors = model.successors[(state, context)]
        weights = model.weights.get((state, context), {})
        successor_rows = []
        for successor in successors:
            successor_rows.append(
                (
                    weights.get(successor),
                    future_signature(model, successor, horizon - 1),
                )
            )
        context_rows.append((context, tuple(sorted(successor_rows, key=repr))))
    return (tuple(sorted(model.records[state], key=repr)), tuple(context_rows))


def record_state_sufficient(model: FiniteSubstrate, horizon: int = 2) -> bool:
    for index, left in enumerate(model.states):
        for right in model.states[index + 1 :]:
            if model.records[left] != model.records[right]:
                continue
            if future_signature(model, left, horizon) != future_signature(model, right, horizon):
                return False
    return True


def menu_complete(model: FiniteSubstrate) -> bool | None:
    if not model.availability:
        return None
    for (state, context), menu in model.availability.items():
        realized = frozenset(
            model.formed_content[(state, successor, context)]
            for successor in model.successors[(state, context)]
            if (state, successor, context) in model.formed_content
        )
        if realized != menu:
            return False
    return True


def normalized_statistics(model: FiniteSubstrate) -> bool:
    if model.frequency_counts:
        values = tuple(model.frequency_counts.values())
        return bool(values) and min(values) == max(values)
    branching = [
        (key, successors)
        for key, successors in model.successors.items()
        if len(successors) > 1
    ]
    if not branching:
        return False
    for key, successors in branching:
        if key not in model.weights:
            return False
        weights = model.weights[key]
        if set(weights) != set(successors) or sum(weights.values()) != 1:
            return False
    return True


def actuality(model: FiniteSubstrate) -> bool:
    if model.selection_mode == "stochastic":
        return normalized_statistics(model)
    if model.selection_mode == "deterministic":
        return all(len(successors) == 1 for successors in model.successors.values())
    return False


def append_model() -> FiniteSubstrate:
    states = ("empty", "r0", "r1")
    context = "write_x"
    successors = {
        ("empty", context): ("r0", "r1"),
        ("r0", context): ("r0",),
        ("r1", context): ("r1",),
    }
    records = {
        "empty": frozenset(),
        "r0": frozenset({("x", 0)}),
        "r1": frozenset({("x", 1)}),
    }
    return FiniteSubstrate(
        "append", "monotone append closure", states, (context,), successors, records,
        availability={("empty", context): frozenset({0, 1})},
        formed_content={
            ("empty", "r0", context): 0,
            ("empty", "r1", context): 1,
        },
    )


def qca_model() -> FiniteSubstrate:
    states = ("00", "01", "10", "11")
    context = "cnot_step"
    mapping = {"00": "00", "01": "01", "10": "11", "11": "10"}
    successors = {(state, context): (future,) for state, future in mapping.items()}
    records = {
        state: (frozenset({("target", 1)}) if state[1] == "1" else frozenset())
        for state in states
    }
    return FiniteSubstrate(
        "qca", "reversible QCA/CNOT", states, (context,), successors, records,
        joint_dimension=16, generated_local_rank=16,
        selection_mode="deterministic", state_type="quantum_enriched",
    )


def refinement_model() -> FiniteSubstrate:
    states = ("plus", "mixed", "xp", "xm")
    contexts = ("refine", "x_test")
    successors = {
        ("plus", "refine"): ("mixed",),
        ("mixed", "refine"): ("mixed",),
        ("xp", "refine"): ("xp",),
        ("xm", "refine"): ("xm",),
        ("plus", "x_test"): ("xp",),
        ("mixed", "x_test"): ("xp", "xm"),
        ("xp", "x_test"): ("xp",),
        ("xm", "x_test"): ("xm",),
    }
    records = {
        "plus": frozenset(),
        "mixed": frozenset(),
        "xp": frozenset({("x", "+")}),
        "xm": frozenset({("x", "-")}),
    }
    return FiniteSubstrate(
        "refinement", "record-generated refinement", states, contexts,
        successors, records, joint_dimension=16, generated_local_rank=16,
        state_type="quantum_enriched",
    )


def instrument_model() -> FiniteSubstrate:
    states = ("plus", "minus", "z0", "z1", "xp", "xm")
    contexts = ("z_test", "x_test")
    successors: dict[tuple[State, Context], tuple[State, ...]] = {}
    for state in states:
        for context in contexts:
            successors[(state, context)] = (state,)
    successors[("plus", "z_test")] = ("z0", "z1")
    successors[("minus", "z_test")] = ("z0", "z1")
    successors[("plus", "x_test")] = ("xp",)
    successors[("minus", "x_test")] = ("xm",)
    records = {
        "plus": frozenset(),
        "minus": frozenset(),
        "z0": frozenset({("z", 0)}),
        "z1": frozenset({("z", 1)}),
        "xp": frozenset({("x", "+")}),
        "xm": frozenset({("x", "-")}),
    }
    weights = {
        ("plus", "z_test"): {"z0": Fraction(1, 2), "z1": Fraction(1, 2)},
        ("minus", "z_test"): {"z0": Fraction(1, 2), "z1": Fraction(1, 2)},
    }
    return FiniteSubstrate(
        "instrument", "quantum instrument", states, contexts, successors,
        records, joint_dimension=16, generated_local_rank=16, weights=weights,
        selection_mode="stochastic", state_type="density_plus_records",
    )


def measured_history_model() -> FiniteSubstrate:
    states = ("root", "h0", "h1")
    context = "append"
    successors = {
        ("root", context): ("h0", "h1"),
        ("h0", context): ("h0",),
        ("h1", context): ("h1",),
    }
    records = {
        "root": frozenset(),
        "h0": frozenset({(0, 0)}),
        "h1": frozenset({(0, 1)}),
    }
    weights = {
        ("root", context): {"h0": Fraction(1, 2), "h1": Fraction(1, 2)},
    }
    return FiniteSubstrate(
        "history", "measured history tree", states, (context,), successors,
        records, weights=weights,
    )


def deterministic_history_model() -> FiniteSubstrate:
    values = tuple(index % 3 for index in range(12))
    states = tuple(f"p{index}" for index in range(13))
    context = "step"
    successors = {
        (states[index], context): (states[index + 1],)
        for index in range(12)
    }
    successors[(states[-1], context)] = (states[-1],)
    records = {
        states[length]: frozenset((index, values[index]) for index in range(length))
        for length in range(13)
    }
    counts = {value: values.count(value) for value in set(values)}
    return FiniteSubstrate(
        "det_history", "deterministic periodic history", states, (context,),
        successors, records, selection_mode="deterministic",
        frequency_counts=counts,
    )


def source_contract() -> None:
    section("A - Common-language source contract")
    raw = NOTE.read_text()
    note = " ".join(raw.lower().replace("**", "").split())
    check("A note is authority-free", "authority: none" in note)
    for symbol in ("lambda", "`a`", "`iota`", "`sigma`", "`r(s)`", "`kappa`", "`l(s,k)`", "`k(s)`", "`mu`", "`h`", "`q`"):
        check(f"A typed symbol present: {symbol}", symbol in note)
    check("A syntax/physics boundary is explicit", "syntax versus physics" in note)
    check("A six reference families are named", "six reference families" in note)
    check("A no axiom recommendation is made", "makes no axiom recommendation" in note)


def run_model(model: FiniteSubstrate) -> dict[str, bool | None]:
    return {
        "L": total(model),
        "C": declared_generated_composition(model),
        "S": record_state_sufficient(model),
        "V": record_invariant(model),
        "F": menu_complete(model),
        "X": actuality(model),
        "W": normalized_statistics(model),
    }


def family_conformance() -> None:
    section("B - Six-family executable conformance")
    models = (
        append_model(),
        qca_model(),
        refinement_model(),
        instrument_model(),
        measured_history_model(),
        deterministic_history_model(),
    )
    results = {model.name: run_model(model) for model in models}

    check("B all six family witnesses are present", len(models) == 6)
    check("B every declared finite law is total", all(result["L"] for result in results.values()))

    append = results["append"]
    check("B append closes record state, support, and invariance", append["S"] and append["F"] and append["V"])
    check("B append does not supply composition, actuality, or weights", not append["C"] and not append["X"] and not append["W"])

    qca = results["qca"]
    check("B QCA declares generated-composition metadata and deterministic update", qca["C"] and qca["X"])
    check("B reversible copy fails record-only state and permanence", not qca["S"] and not qca["V"])

    refinement = results["refinement"]
    check("B refinement preserves records on its declared transitions", refinement["V"])
    check("B refinement retains an enriched state and lacks X/W", not refinement["S"] and not refinement["X"] and not refinement["W"])

    instrument = results["instrument"]
    check("B instrument declares generated-carrier metadata and normalized stochastic branch law", instrument["C"] and instrument["X"] and instrument["W"])
    check("B instrument state is not exhausted by records", not instrument["S"])

    history = results["history"]
    check("B measured history closes S/V/W", history["S"] and history["V"] and history["W"])
    check("B measured history has no generated quantum carrier or actual selector", not history["C"] and not history["X"])

    deterministic = results["det_history"]
    check("B deterministic history closes finite S/V/X/frequency controls", deterministic["S"] and deterministic["V"] and deterministic["X"] and deterministic["W"])
    check("B deterministic history has no generated quantum carrier", not deterministic["C"])

    check("B no reference family closes C/S/L/V/X/W together", not any(all(result[key] for key in ("C", "S", "L", "V", "X", "W")) for result in results.values()))


def exact_context_and_provenance_guards() -> None:
    section("C - Context and provenance guards")
    instrument = instrument_model()
    check("C incompatible X and Z tests remain distinct contexts", set(instrument.contexts) == {"x_test", "z_test"})
    check("C plus/minus have one record map but different contextual futures", instrument.records["plus"] == instrument.records["minus"] and not record_state_sufficient(instrument))
    check("C stochastic actuality requires an explicit normalized kernel", instrument.selection_mode == "stochastic" and normalized_statistics(instrument))

    qca = qca_model()
    check("C generated-composition metadata is separately declared from local evolution", qca.joint_dimension == qca.generated_local_rank == 16)
    check("C deterministic evolution alone supplies no frequency certificate", actuality(qca) and not normalized_statistics(qca))

    history = measured_history_model()
    check("C a normalized history measure need not select an actual history", normalized_statistics(history) and not actuality(history))


def main() -> None:
    source_contract()
    family_conformance()
    exact_context_and_provenance_guards()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: finite conformance language only; family names grant no physical premise")


if __name__ == "__main__":
    main()
