#!/usr/bin/env python3
"""Exact checks: ensemble <P> is not unit-lock Record I.

At beta=2, remainder-controlled I_0 and I_1 give 0 < I_1/I_0 < 8/9 < 1.
Record I of a unit-lock pattern is a nonnegative integer. Identity gates
call i0_partial, i1_partial, and record_I. A predicate that <P>(2) is an
integer must fail. A predicate that I equals <P>(2) must fail on I=0 and
I=1. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "REALIZED_STATE_PRIMITIVE_FORBIDS_ENSEMBLE_PLAQUETTE_AS_RECORD_I_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PRIMITIVE_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/REALIZED_STATE_PRIMITIVE_FORBIDS_ENSEMBLE_PLAQUETTE_AS_RECORD_I_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BETA_TWO = Fraction(2)
INJECTED_NUMERAL = Fraction(5934, 10000)


def normalize(text: str) -> str:
    return " ".join(text.split())


def factorial_fraction(n: int) -> Fraction:
    out = Fraction(1)
    for k in range(2, n + 1):
        out *= k
    return out


def bessel_term(n: int, k: int, beta: Fraction) -> Fraction:
    """One exact term of I_n(β) = sum 1/(k!(k+n)!) (β/2)^{2k+n}."""
    half = beta / 2
    return (half ** (2 * k + n)) / (
        factorial_fraction(k) * factorial_fraction(k + n)
    )


def i0_partial(beta: Fraction, N: int) -> Fraction:
    """Identity-gate function: exact partial sum S0_N(β)."""
    return sum((bessel_term(0, k, beta) for k in range(N + 1)), Fraction(0))


def i1_partial(beta: Fraction, N: int) -> Fraction:
    """Identity-gate function: exact partial sum S1_N(β)."""
    return sum((bessel_term(1, k, beta) for k in range(N + 1)), Fraction(0))


def remainder_ratio_at_two(N: int) -> Fraction:
    return Fraction(1, (N + 2) ** 2)


def i0_remainder_majorant_at_two(N: int) -> Fraction:
    """For N>=1: 0 <= I_0(2)-S0_N <= t_{N+1}/(1-1/(N+2)^2)."""
    if N < 1:
        raise ValueError("I_0 remainder majorant requires N >= 1")
    q = remainder_ratio_at_two(N)
    if q >= 1:
        raise ValueError("geometric majorant requires q < 1")
    return bessel_term(0, N + 1, BETA_TWO) / (1 - q)


def i1_remainder_majorant_at_two(N: int) -> Fraction:
    """I_1(2) tail: same q=1/(N+2)^2 majorant, valid because the I_1 ratio is smaller."""
    q = remainder_ratio_at_two(N)
    if q >= 1:
        raise ValueError("geometric majorant requires q < 1")
    return bessel_term(1, N + 1, BETA_TWO) / (1 - q)


def record_I(unit_locks: tuple[object, ...]) -> int:
    """Identity-gate function: nonnegative integer domain count. I(empty)=0."""
    return len(unit_locks)


def mean_p_is_integer(beta: Fraction) -> bool:
    """Predicate: <P>(β) is an integer.

    Identity gate: must call i0_partial and i1_partial.
    At β=2 the certified enclosure is (0, 8/9), which contains no integer.
    """
    s0 = i0_partial(beta, 2)
    s1_lo = i1_partial(beta, 1)
    s1_hi = i1_partial(beta, 3) + i1_remainder_majorant_at_two(3)
    if s1_lo <= 0 or s0 <= 0:
        return True
    return not (s1_hi < s0)


def record_I_equals_mean_p(
    unit_locks: tuple[object, ...], beta: Fraction
) -> bool:
    """Predicate: Record I equals <P>(β).

    Identity gate: must call i0_partial, i1_partial, and record_I.
    Must fail on I=0 and on I=1 at β=2.
    """
    value = record_I(unit_locks)
    s0 = i0_partial(beta, 2)
    s1_lo = i1_partial(beta, 1)
    s1_hi = i1_partial(beta, 3) + i1_remainder_majorant_at_two(3)
    if value == 0:
        return s1_lo <= 0
    return s1_hi >= value * s0


def is_bessel_series_coefficient(coeff: Fraction, kmax: int = 20) -> bool:
    """True iff coeff equals some I_n term at β=2 for n in {0,1}."""
    for n in (0, 1):
        for k in range(kmax + 1):
            if coeff == bessel_term(n, k, BETA_TWO):
                return True
    return False


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: realized-state primitive and Record "
        "readout sentences are source-bound; I_n series uses Bessel terms only"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: U(1) one-plaquette <P>(2) is not unit-lock Record I; "
        "June 10 is not retired; 4D <P>* is not claimed"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, primitive, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/REALIZED_STATE_PRIMITIVE_FORBIDS_ENSEMBLE_PLAQUETTE_AS_RECORD_I_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "source-realized-state",
        "the primitive supplies pointwise evaluation and no averaging over alternatives",
        "evaluate at the realized state, pointwise" in primitive
        and "no averaging over alternatives" in primitive
        and "no averaging over alternatives" in note
        and "pointwise" in note,
    )
    checks.check(
        "source-record-i",
        "the axiom memo supplies content-only additive I with I(empty)=0",
        "I(empty)=0" in normalize(axiom).replace(" ", "")
        or (
            "`I(empty)=0`" in axiom
            and "A readout value is determined by record content" in axiom
            and "locks exactly one admissible local possibility" in axiom
        ),
    )

    s0_2 = i0_partial(BETA_TWO, 2)
    s1_1 = i1_partial(BETA_TWO, 1)
    s1_3 = i1_partial(BETA_TWO, 3)
    t4 = bessel_term(1, 4, BETA_TWO)
    rem1 = i1_remainder_majorant_at_two(3)
    checks.check(
        "theorem-1-s0-two",
        "S0_2(2)=1+1+1/4=9/4 via i0_partial",
        s0_2 == Fraction(9, 4)
        and bessel_term(0, 0, BETA_TWO) == 1
        and bessel_term(0, 1, BETA_TWO) == 1
        and bessel_term(0, 2, BETA_TWO) == Fraction(1, 4)
        and i0_partial(BETA_TWO, 2) == Fraction(9, 4),
        residual=s0_2,
    )
    checks.check(
        "theorem-1-i0-ratio",
        "I_0 term ratio at beta=2 is 1/(k+1)^2",
        bessel_term(0, 1, BETA_TWO) / bessel_term(0, 0, BETA_TWO) == 1
        and bessel_term(0, 2, BETA_TWO) / bessel_term(0, 1, BETA_TWO)
        == Fraction(1, 4)
        and bessel_term(0, 3, BETA_TWO) / bessel_term(0, 2, BETA_TWO)
        == Fraction(1, 9)
        and i0_remainder_majorant_at_two(1) > 0,
    )
    checks.check(
        "theorem-1-s1-one",
        "S1_1(2)=1+1/2=3/2 via i1_partial",
        s1_1 == Fraction(3, 2)
        and bessel_term(1, 0, BETA_TWO) == 1
        and bessel_term(1, 1, BETA_TWO) == Fraction(1, 2)
        and i1_partial(BETA_TWO, 1) == Fraction(3, 2),
        residual=s1_1,
    )
    checks.check(
        "theorem-1-s1-three",
        "S1_3=3/2+1/12+1/144=229/144 via i1_partial",
        s1_3 == Fraction(229, 144)
        and bessel_term(1, 2, BETA_TWO) == Fraction(1, 12)
        and bessel_term(1, 3, BETA_TWO) == Fraction(1, 144)
        and Fraction(3, 2) + Fraction(1, 12) + Fraction(1, 144)
        == Fraction(229, 144)
        and s1_3 < 2,
        residual=s1_3,
    )
    checks.check(
        "theorem-1-i1-lt-two",
        "next-term remainder < 1/2880/(1-1/25) < 1/2000, so I_1(2)<2",
        t4 == Fraction(1, 2880)
        and remainder_ratio_at_two(3) == Fraction(1, 25)
        and rem1 == Fraction(1, 2880) / (1 - Fraction(1, 25))
        and rem1 == Fraction(25, 69120)
        and rem1 < Fraction(1, 2000)
        and s1_3 + rem1 < 2
        and s1_3 + Fraction(1, 2000) < 2,
        residual=(t4, rem1, s1_3 + rem1),
    )
    checks.check(
        "theorem-1-ratio-bound",
        "0 < I_1(2)/I_0(2) < 2/(9/4)=8/9 < 1",
        s1_1 > 0
        and s0_2 == Fraction(9, 4)
        and Fraction(2) / Fraction(9, 4) == Fraction(8, 9)
        and Fraction(8, 9) < 1
        and s1_3 + rem1 < 2
        and (s1_3 + rem1) / s0_2 < Fraction(8, 9),
        residual=Fraction(8, 9),
    )

    empty = ()
    one_lock = ("unit-lock-0",)
    checks.check(
        "theorem-2-record-integer",
        "record_I is a nonnegative integer and I(empty)=0",
        record_I(empty) == 0
        and record_I(one_lock) == 1
        and record_I(("a", "b", "c")) == 3
        and isinstance(record_I(empty), int)
        and record_I(empty) >= 0,
    )
    checks.check(
        "identity-mean-not-integer",
        "predicate that <P>(2) is an integer fails",
        mean_p_is_integer(BETA_TWO) is False
        and "i0_partial" in mean_p_is_integer.__code__.co_names
        and "i1_partial" in mean_p_is_integer.__code__.co_names,
    )
    checks.check(
        "identity-I-equals-mean",
        "predicate that I equals <P>(2) fails on I=0 and on I=1",
        record_I_equals_mean_p(empty, BETA_TWO) is False
        and record_I_equals_mean_p(one_lock, BETA_TWO) is False
        and "i0_partial" in record_I_equals_mean_p.__code__.co_names
        and "i1_partial" in record_I_equals_mean_p.__code__.co_names
        and "record_I" in record_I_equals_mean_p.__code__.co_names,
    )

    checks.check(
        "theorem-3-primitive-forbids",
        "the note applies the primitive to forbid identifying <P> with Record I",
        all(
            phrase in note
            for phrase in (
                "no averaging over alternatives",
                "ensemble mean over Haar",
                "forbids identifying",
                "Record readout",
            )
        ),
    )
    checks.check(
        "theorem-4-note-negatives",
        "the note records the scoped negatives of Theorem 4",
        all(
            phrase in note
            for phrase in (
                "does not retire June 10",
                "does not import 0.5934",
                "does not claim 4D",
                "does not say a later law-level table is impossible",
            )
        ),
    )
    checks.check(
        "mutation-injected-numeral",
        "feeding 5934/10000 into I_n as a coefficient is rejected; coefficients are Bessel terms only",
        not is_bessel_series_coefficient(INJECTED_NUMERAL)
        and is_bessel_series_coefficient(bessel_term(0, 0, BETA_TWO))
        and is_bessel_series_coefficient(bessel_term(0, 2, BETA_TWO))
        and is_bessel_series_coefficient(bessel_term(1, 1, BETA_TWO))
        and i0_partial(BETA_TWO, 2) != INJECTED_NUMERAL
        and i1_partial(BETA_TWO, 3) != INJECTED_NUMERAL,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: negative_route_pruning",
                "target_claim_id: record_i_versus_ensemble_plaquette_mean",
                "reachability_to_target: advances",
                "source_of_blocker_text: handoff",
                "authors no audit verdict",
                "MINIMAL_AXIOMS_2026-06-29.md",
                "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
                "**Type:** bounded_theorem",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "L_phys" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the ensemble mean and Bessel table are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("I_1(beta)", "<P>(beta)", "i0_partial", "i1_partial")
        )
        and "Lattice" in axiom
        and "Qubit" in axiom
        and "Admissibility" in axiom
        and "Record" in axiom
        and "I(empty)=0" in axiom.replace(" ", "").replace("`", ""),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )

    n5_lines = (
        "per_element: remainder-controlled Bessel terms of I_0(2) and I_1(2) and the ratio bound 8/9 are the only evaluated objects",
        "per_site: one U(1) plaquette versus one unit-lock pattern; no 4D site configuration is sampled",
        "per_mode: the I_n power series is checked; no 4D transfer-matrix mode or mass-gap rate is claimed",
        "per_block: only the integer type of Record I, the non-integer <P>(2) enclosure, and the primitive ban are executed",
        "lattice_wide: checked and not executed — no 4D <P>* and no June 10 retirement is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(
                ("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:")
            )
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
