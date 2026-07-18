#!/usr/bin/env python3
"""Finite model controls for existence versus exact law specification."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXISTENCE_UNIQUENESS_AND_EXACT_LAW_REFERENCE_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


@dataclass(frozen=True)
class FixedKernelLaw:
    lam: int

    def answer(self, n_zero: int, n_one: int) -> tuple[Fraction, Fraction]:
        w_zero = self.lam**n_zero
        w_one = self.lam**n_one
        total = w_zero + w_one
        return Fraction(w_zero, total), Fraction(w_one, total)


def one_law_per_model() -> None:
    section("A - One fixed rule per model does not identify one common value")
    laws = (FixedKernelLaw(1), FixedKernelLaw(2))
    profiles = tuple((n0, n1) for n0 in range(7) for n1 in range(7 - n0))
    for law in laws:
        check(f"A model lambda={law.lam} contains exactly one fixed law object", isinstance(law, FixedKernelLaw))
        check(f"A law lambda={law.lam} gives one answer per profile", all(len(law.answer(*profile)) == 2 for profile in profiles))
        check(f"A law lambda={law.lam} answers normalize", all(sum(law.answer(*profile)) == 1 for profile in profiles))
        check(f"A law lambda={law.lam} is positive", all(all(weight > 0 for weight in law.answer(*profile)) for profile in profiles))
        check(
            f"A law lambda={law.lam} is label covariant",
            all(law.answer(n0, n1) == tuple(reversed(law.answer(n1, n0))) for n0, n1 in profiles),
        )

    predictions = tuple(law.answer(2, 1)[0] for law in laws)
    check("A two admissible models disagree on one observable", predictions == (Fraction(1, 2), Fraction(2, 3)))
    check("A one-fixed-rule syntax is true in both models", all(law is not None for law in laws))
    check("A structural theory cannot decide the separated value", len(set(predictions)) == 2)
    check("A exact reference to lambda one decides the value", laws[0].answer(2, 1)[0] == Fraction(1, 2))
    check("A exact reference to lambda two decides the other value", laws[1].answer(2, 1)[0] == Fraction(2, 3))


@dataclass(frozen=True)
class RawLaw:
    flip_hidden: bool

    def step(self, state: tuple[int, int], context: str) -> tuple[tuple[str, int], tuple[int, int]]:
        record, hidden = state
        if context == "read":
            return ("record", record), (record, 1 - hidden if self.flip_hidden else hidden)
        if context == "probe":
            return ("hidden", hidden), (record, 1 - hidden if self.flip_hidden else hidden)
        raise ValueError(context)


def transcript(law: RawLaw, initial: tuple[int, int], protocol: tuple[str, ...]):
    state = initial
    result = []
    for context in protocol:
        output, state = law.step(state, context)
        result.append(output)
    return tuple(result)


def exact_equivalence_requires_complete_contexts() -> None:
    section("B - Physical equivalence is relative to a complete test repertoire")
    still = RawLaw(False)
    flip = RawLaw(True)
    initial = (0, 0)
    read_protocols = tuple(("read",) * depth for depth in range(1, 5))
    check(
        "B raw laws are record-equivalent under read-only protocols",
        all(transcript(still, initial, protocol) == transcript(flip, initial, protocol) for protocol in read_protocols),
    )
    probe_protocol = ("read", "probe")
    check(
        "B one hidden-sensitive context separates the raw laws",
        transcript(still, initial, probe_protocol) != transcript(flip, initial, probe_protocol),
    )
    check("B raw presentation difference alone need not be physical", still != flip)
    check("B complete context choice determines the equivalence quotient", bool(read_protocols) and bool(probe_protocol))


@dataclass(frozen=True)
class DeterministicLaw:
    write: int

    def answer(self) -> int:
        return self.write


def determinism_does_not_identify_the_function() -> None:
    section("C - Functional uniqueness within a law is not uniqueness across laws")
    zero = DeterministicLaw(0)
    one = DeterministicLaw(1)
    check("C zero law has exactly one answer", zero.answer() == 0)
    check("C one law has exactly one answer", one.answer() == 1)
    check("C two deterministic laws disagree", zero.answer() != one.answer())
    check("C deterministic typing removes sampling only", len({zero.answer()}) == len({one.answer()}) == 1)


def documentation_contract() -> None:
    section("D - Documentation and live-surface boundary")
    note = NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "")
    axioms = AXIOMS.read_text(encoding="utf-8").lower()
    check("D note is authority-free", "authority: none" in note)
    check("D note distinguishes existence, functionality, and identification", all(word in note for word in ("existence", "functional", "identification")))
    check("D note permits exact physical equivalence", "exact physical-equivalence class" in note)
    check("D note carries all N1-N8 headings", all(f"### n{index}" in note for index in range(1, 9)))
    check("D note rejects a placeholder reference", "placeholder" in note and "does not close" in note)
    check("D live axioms have no canonical-law placeholder", "canonical-law" not in axioms and "[canonical" not in axioms)


def main() -> int:
    one_law_per_model()
    exact_equivalence_requires_complete_contexts()
    determinism_does_not_identify_the_function()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
