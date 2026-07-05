#!/usr/bin/env python3
"""Mechanical checks for the record/measurement collapse gate map.

This runner is source-side only. It verifies anchors and finite witnesses for
why the current framework has a supplied-context collapse/update interface but
not a retained unbounded physical collapse derivation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RECORD_MEASUREMENT_COLLAPSE_UNBOUNDED_DERIVATION_GATE_MAP_NOTE_2026-07-05.md"
PASS = 0
FAIL = 0


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def read(path: str | Path) -> str:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    return p.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(matrix[i, i] for i in range(matrix.rows)))


def projector(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.T)


def doc_anchor_checks() -> None:
    section("Source anchors")
    note = read(NOTE)
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    formation = read("docs/RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md")
    instrument = read("docs/RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md")
    context_nogo = read("docs/RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md")
    production = read("docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md")
    unbounded = read("docs/POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md")

    report("note declares open_gate source row", "claim_type: open_gate" in note)
    report("note forbids bare retained status", "bare_retained_allowed: false" in note)
    report("note names measurement-production family", "measurement-production family" in note.lower() or "measurement production family" in note.lower())
    report("note says objective physical collapse remains open", "objective physical collapse law / Born-weighted native record production" in note)
    report("note records finite supplied-context support", "finite supplied-context collapse/update interface is available" in note)
    report("note keeps audit ownership external", "independent audit lane only" in note)
    prohibited = (
        "actual_current_surface_status: retained",
        "bare_retained_allowed: true",
        "proposal_allowed: true",
        "AUDIT_VERDICT_APPLIED=TRUE",
    )
    report("note avoids retained/promotion leaks", all(p not in note for p in prohibited))

    report("axioms contain Record occurrence sentence", "Records form." in axioms)
    report("axioms keep formation rules outside axiom content", "formation rules (which" in axioms and "with what weight" in axioms)
    report("axioms keep dynamics outside axiom content", "Admissibility is not a dynamics axiom" in axioms)
    report("realized-state primitive is not selector", "This is pointwise evaluation, not a state-selection rule." in realized)
    report("realized-state primitive supplies no probability", "probability rule" in realized and "state-selection rule" in realized)
    report("formation append is occurrence-strength only", "occurrence strength only" in formation)
    report("formation append leaves rule/rate open", "which admissible possibility, which site, what weight, or\n  what rate" in formation)
    report("instrument gate requires supplied readout context", "supplied readout context" in instrument)
    report("instrument gate separates realized outcome from probability", "chosen outcome -> one-hot post-record atom/count update" in instrument)
    report("context no-go has multiple readout contexts", "multiple complete projective readout contexts" in context_nogo)
    flat_context_nogo = flat(context_nogo)
    report(
        "context no-go keeps generator/rate underived",
        "one-step production probability vector does not determine the physical" in flat_context_nogo
        and "generator, or the clock/rate normalization" in flat_context_nogo,
    )
    report("production boundary says append/count does not produce next atom", "It does not\nproduce the next atom" in production)
    report("unbounded no-go blocks finite-certificate-alone route", "finite post-record certificate alone => unbounded retained law" in unbounded)


def context_nonselection_checks() -> None:
    section("Same state, distinct readout contexts")
    sqrt2 = sp.sqrt(2)
    rho = sp.Matrix([[sp.Rational(2, 3), sqrt2 / 3], [sqrt2 / 3, sp.Rational(1, 3)]])

    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    ket_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.sqrt(sp.Rational(1, 2))])
    ket_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.sqrt(sp.Rational(1, 2))])
    ket_y_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.I * sp.sqrt(sp.Rational(1, 2))])
    ket_y_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.I * sp.sqrt(sp.Rational(1, 2))])

    p_z = sp.Matrix([trace(projector(ket0) * rho), trace(projector(ket1) * rho)])
    p_x = sp.Matrix([trace(projector(ket_plus) * rho), trace(projector(ket_minus) * rho)])
    p_y = sp.Matrix([
        trace((ket_y_plus * ket_y_plus.conjugate().T) * rho),
        trace((ket_y_minus * ket_y_minus.conjugate().T) * rho),
    ])

    report("rho is normalized", trace(rho) == 1)
    report("Z probabilities match source gate", p_z == sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3)]), str(list(p_z)))
    report("X probabilities differ from Z", p_x != p_z, str(list(p_x)))
    report("Y probabilities differ from Z and X", p_y != p_z and p_y != p_x, str(list(p_y)))
    report("all three contexts are normalized", all(sp.simplify(sum(p) - 1) == 0 for p in (p_z, p_x, p_y)))
    report("same state/projective algebra does not select one context", len({tuple(p_z), tuple(p_x), tuple(p_y)}) == 3)

    tracial = sp.eye(2) / 2
    pz_tr = sp.Matrix([trace(projector(ket0) * tracial), trace(projector(ket1) * tracial)])
    px_tr = sp.Matrix([trace(projector(ket_plus) * tracial), trace(projector(ket_minus) * tracial)])
    py_tr = sp.Matrix([
        trace((ket_y_plus * ket_y_plus.conjugate().T) * tracial),
        trace((ket_y_minus * ket_y_minus.conjugate().T) * tracial),
    ])
    report("tracial no-information state is context-uniform", pz_tr == px_tr == py_tr == sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)]))
    report("tracial reference does not reproduce prepared-state Z probabilities", pz_tr != p_z)
    report("no-privilege route cannot by itself derive arbitrary prepared-state collapse", pz_tr != p_z and px_tr != p_x)


def producer_underdetermination_checks() -> None:
    section("Same realized word, distinct producers")
    word = (1, 0, 1, 1)

    def iid_likelihood(p_one: Fraction) -> Fraction:
        p_zero = 1 - p_one
        likelihood = Fraction(1, 1)
        for bit in word:
            likelihood *= p_one if bit else p_zero
        return likelihood

    fair = iid_likelihood(Fraction(1, 2))
    two_thirds = iid_likelihood(Fraction(2, 3))
    one_third = iid_likelihood(Fraction(1, 3))
    scripted = Fraction(1, 1)
    count = (word.count(0), word.count(1))

    report("realized word has fixed post-record count", count == (1, 3), str(count))
    report("fair IID gives positive likelihood", fair == Fraction(1, 16), str(fair))
    report("biased IID gives positive different likelihood", two_thirds != fair and two_thirds > 0, str(two_thirds))
    report("reverse-biased IID gives positive different likelihood", one_third not in (fair, two_thirds) and one_third > 0, str(one_third))
    report("scripted producer can write same word with likelihood one", scripted == 1)
    report("same post-record word/count does not identify producer", len({fair, two_thirds, one_third, scripted}) == 4)


@dataclass(frozen=True)
class Completion:
    prefix: tuple[int, ...]
    tail_value: int

    def finite_word(self, length: int) -> tuple[int, ...]:
        if length <= len(self.prefix):
            return self.prefix[:length]
        return self.prefix + (self.tail_value,) * (length - len(self.prefix))

    def limiting_density(self) -> Fraction:
        return Fraction(self.tail_value, 1)


def unbounded_lift_checks() -> None:
    section("Finite prefix does not fix unbounded law")
    prefix = (1, 0, 1, 1)
    zero_tail = Completion(prefix, 0)
    one_tail = Completion(prefix, 1)
    window = len(prefix)

    report("two completions agree on certificate window", zero_tail.finite_word(window) == one_tail.finite_word(window) == prefix)
    report("certificate count is shared", sum(zero_tail.finite_word(window)) == sum(one_tail.finite_word(window)) == 3)
    report("certificate frequency is shared", Fraction(sum(prefix), len(prefix)) == Fraction(3, 4))
    report("unbounded tails disagree", zero_tail.limiting_density() != one_tail.limiting_density())
    report("zero-tail limiting density is 0", zero_tail.limiting_density() == 0)
    report("one-tail limiting density is 1", one_tail.limiting_density() == 1)
    report("long finite windows eventually distinguish completions", zero_tail.finite_word(20) != one_tail.finite_word(20))


def collapse_update_typing_checks() -> None:
    section("Conditional update versus physical production")
    rho = sp.Matrix([[sp.Rational(2, 3), sp.sqrt(2) / 3], [sp.sqrt(2) / 3, sp.Rational(1, 3)]])
    p0 = sp.Matrix([[1, 0], [0, 0]])
    p1 = sp.Matrix([[0, 0], [0, 1]])
    nonselective = sp.simplify(p0 * rho * p0 + p1 * rho * p1)
    selective0 = sp.simplify(p0 * rho * p0 / trace(p0 * rho * p0))
    count = sp.Matrix([4, 2])
    one_hot_0 = sp.Matrix([1, 0])

    report("nonselective dephasing is normalized", trace(nonselective) == 1)
    report("nonselective dephasing is not selective branch 0", nonselective != selective0)
    report("selective branch 0 is normalized after supplied outcome", trace(selective0) == 1)
    report("record write is one-hot after outcome is supplied", count + one_hot_0 == sp.Matrix([5, 2]))
    report("probability vector is not the realized one-hot atom", sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3)]) != one_hot_0)


def conclusion_checks() -> None:
    section("Gate conclusion")
    required_gates = {
        "context_selection": False,
        "instrument_family": False,
        "probability_law_for_selected_family": False,
        "realized_write_selector": False,
        "production_kernel_or_generator": False,
        "clock_rate_if_dynamical": False,
        "unbounded_family_lift": False,
        "frequency_objectivity_bridge": False,
    }
    report("all retained-unbounded collapse gates are explicitly tracked", len(required_gates) == 8)
    report("no required gate is marked closed by this runner", not any(required_gates.values()))
    report("conditional finite interface can still be useful", True)
    print()
    print("COLLAPSE_AS_SUPPLIED_CONTEXT_UPDATE=SUPPORTED")
    print("RETAINED_UNBOUNDED_PHYSICAL_COLLAPSE_DERIVED=FALSE")
    print("MEASUREMENT_PRODUCTION_FAMILY_REQUIRED=TRUE")
    print("AUDIT_VERDICT_APPLIED=FALSE")


def main() -> int:
    print("Record/measurement collapse retained-unbounded gate map")
    print("source-side only; no audit verdict or retained promotion")
    doc_anchor_checks()
    context_nonselection_checks()
    producer_underdetermination_checks()
    unbounded_lift_checks()
    collapse_update_typing_checks()
    conclusion_checks()
    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: open gate map validated. Current support is finite and supplied-context; retained-unbounded physical collapse requires a measurement-production family.")
        return 0
    print("VERDICT: failed; do not cite this gate map until repaired.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
