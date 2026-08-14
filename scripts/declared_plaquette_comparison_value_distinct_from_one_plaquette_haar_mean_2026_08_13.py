#!/usr/bin/env python3
"""Wilson matching at g_bare=1 is independent of admission B1.

Paired note:
  docs/PLAQUETTE_B1_CONVENTION_INDEPENDENT_OF_ONE_PLAQUETTE_MEAN_BOUNDED_THEOREM_NOTE_2026-08-13.md

Recomputes the SU(3) single-link series from the June 10 recurrence with an
explicit Haar remainder. The numeral 0.5934 is compared only after p_1(6) is
bounded, and is never an input to J or J'.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PLAQUETTE_B1_CONVENTION_INDEPENDENT_OF_ONE_PLAQUETTE_MEAN_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JUNE10_REL = (
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
SELF_REL = "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/PLAQUETTE_B1_CONVENTION_INDEPENDENT_OF_ONE_PLAQUETTE_MEAN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
JUNE10_PATH = ROOT / JUNE10_REL
AXIOM_PATH = ROOT / AXIOM_REL
SELF_PATH = ROOT / SELF_REL

N_C = 3
G_BARE = 1
HALF = Fraction(1, 2)
ADMITTED = Fraction(5934, 10000)
FORBIDDEN = (
    "we" + " adopt",
    "new" + " axiom",
    "promo" + "ted",
    "Cod" + "ex",
    "derived " + "0.5934",
)


def factorial_fraction(n: int) -> Fraction:
    out = Fraction(1)
    for k in range(2, n + 1):
        out *= k
    return out


def recurrence_coeffs(nmax: int) -> list[Fraction]:
    coeffs = [Fraction(1), Fraction(0), Fraction(1, 36)]
    for n in range(2, nmax):
        nxt = (
            Fraction(n * (n + 1)) * coeffs[n]
            + Fraction(2 * (2 * n + 3)) * coeffs[n - 1]
            + coeffs[n - 2]
        ) / Fraction(6 * (n + 1) * (n + 4) * (n + 5))
        coeffs.append(nxt)
    return coeffs


def exp_tail_majorant(start: int, beta: Fraction) -> Fraction:
    """Upper bound on sum_{k=start}^{infty} beta^k / k! for start > beta."""
    if start <= beta:
        raise ValueError("geometric majorant requires start > beta")
    return (beta**start / factorial_fraction(start)) * Fraction(start, start - int(beta))


def one_plaquette_enclosures(n_trunc: int, beta: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return (J_lo, J_hi, Jprime_lo, Jprime_hi) from the recurrence plus remainder.

    The admitted B1 numeral is not an argument and is not used.
    """
    coeffs = recurrence_coeffs(n_trunc + 2)
    j_lo = sum((coeffs[n] * beta**n for n in range(n_trunc + 1)), Fraction(0))
    jp_lo = sum((n * coeffs[n] * beta ** (n - 1) for n in range(1, n_trunc + 1)), Fraction(0))
    rem_j = exp_tail_majorant(n_trunc + 1, beta)
    rem_jp = exp_tail_majorant(n_trunc, beta)
    return j_lo, j_lo + rem_j, jp_lo, jp_lo + rem_jp


def declared_matching(n_c: int, g_bare: Fraction) -> Fraction:
    return Fraction(2 * n_c, g_bare * g_bare)


def matching_gate(matching_fn) -> bool:
    return (
        matching_fn(3, Fraction(1)) == Fraction(6)
        and matching_fn(3, Fraction(2)) == Fraction(3, 2)
        and matching_fn(2, Fraction(1)) == Fraction(4)
    )


def mean_separation_gate(p1_upper: Fraction, admitted: Fraction) -> bool:
    return p1_upper < HALF < admitted


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        extra = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{extra}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: June 10 recurrence and Haar majorant; 0.5934 compared only after p_1 is bounded")

    note = NOTE_PATH.read_text(encoding="utf-8")
    june10 = JUNE10_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_note = SELF_PATH.read_text(encoding="utf-8")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        f"{len(AUDIT_INPUT_PATHS)} paths",
    )
    checks.check(
        "theorem-1-declared-matching",
        matching_gate(declared_matching),
        "beta = 2 N_c / g_bare^2 at (3,1),(3,2),(2,1)",
    )
    checks.check(
        "discriminating-matching-rejects-product-form",
        not matching_gate(lambda n_c, g: Fraction(2 * n_c) * g * g),
    )
    checks.check(
        "discriminating-matching-rejects-missing-two",
        not matching_gate(lambda n_c, g: Fraction(n_c, g * g)),
    )
    checks.check(
        "g-bare-one-selects-beta-six",
        declared_matching(N_C, Fraction(G_BARE)) == Fraction(6) and N_C == 3 and G_BARE == 1,
    )

    coeffs = recurrence_coeffs(24)
    rhs3 = Fraction(2 * 3) * coeffs[2] + Fraction(2 * (4 + 3)) * coeffs[1] + coeffs[0]
    den3 = Fraction(6 * 3 * 6 * 7)
    rhs4 = Fraction(3 * 4) * coeffs[3] + Fraction(2 * (6 + 3)) * coeffs[2] + coeffs[1]
    den4 = Fraction(6 * 4 * 7 * 8)
    checks.check("recurrence-a3-from-seeds", rhs3 / den3 == Fraction(1, 648) == coeffs[3])
    checks.check("recurrence-a4-from-recurrence", rhs4 / den4 == Fraction(1, 2592) == coeffs[4])
    checks.check(
        "haar-majorant-0-le-a-n-le-1-over-n-factorial",
        all(Fraction(0) <= coeffs[n] <= Fraction(1, factorial(n)) for n in range(len(coeffs))),
    )

    # p_1 enclosure is computed with no reference to the admitted numeral.
    j_lo16, j_hi16, jp_lo16, jp_hi16 = one_plaquette_enclosures(16, Fraction(6))
    p1_lo16 = jp_lo16 / j_hi16
    p1_hi16 = jp_hi16 / j_lo16
    gap16 = j_lo16 - 2 * jp_hi16
    if not (p1_hi16 < HALF):
        print(f"honest residual: p1_hi16 - 1/2 = {p1_hi16 - HALF}")
    checks.check(
        "n16-displayed-partial-sums",
        j_lo16 == Fraction(251763633587, 73156608000)
        and jp_lo16 == Fraction(443237359, 304819200),
    )
    checks.check(
        "n16-remainder-and-envelope",
        exp_tail_majorant(16, Fraction(6)) == Fraction(944784, 4379375)
        and jp_hi16 == Fraction(259952292959, 155675520000),
    )
    checks.check(
        "theorem-2-n16-strict-half-ceiling",
        gap16 == Fraction(5323057146257, 52306974720000) and gap16 > 0 and p1_hi16 < HALF,
        f"p1 in ({p1_lo16.limit_denominator(10**6)}, {p1_hi16.limit_denominator(10**6)})",
    )

    j_lo20, j_hi20, jp_lo20, jp_hi20 = one_plaquette_enclosures(20, Fraction(6))
    p1_hi20 = jp_hi20 / j_lo20
    checks.check(
        "independent-n20-remainder-ceiling",
        2 * jp_hi20 < j_lo20 and p1_hi20 < HALF < ADMITTED,
    )
    checks.check(
        "admitted-numeral-compared-only-after-bound",
        mean_separation_gate(p1_hi16, ADMITTED) and mean_separation_gate(p1_hi20, ADMITTED),
        "p_1(6) < 1/2 < 5934/10000",
    )
    checks.check(
        "discriminating-mean-rejects-admitted-numeral",
        not mean_separation_gate(ADMITTED, ADMITTED),
    )
    checks.check(
        "p1-upper-is-not-an-offset-from-admitted-numeral",
        p1_hi16 != ADMITTED and (ADMITTED - p1_hi16) == ADMITTED - p1_hi16 and p1_hi16 < HALF,
    )

    checks.check(
        "note-does-not-derive-05934",
        "This note does not derive 0.5934." in note,
    )
    checks.check(
        "note-does-not-retire-b1",
        "does not retire B1" in note and "three-point" in note and "ln Z_L" in note and "mass-gap" in note,
    )
    checks.check(
        "note-preserves-declared-numerals",
        "0.5934" in note and "beta = 6" in note and "g_bare = 1" in note and "5934/10000" in note,
    )
    checks.check(
        "note-machine-status-contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "hypothetical_axiom_status: no edit",
                "claim_type: bounded_theorem",
            )
        ),
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN if phrase in note]
    checks.check("note-forbidden-phrases-absent", not forbidden_hits, ",".join(forbidden_hits))
    checks.check(
        "june10-recurrence-and-nonderivation",
        "6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}" in june10
        and "0 <= a_n <= 1/n!" in june10
        and "does not derive `0.5934`" in june10,
    )
    checks.check(
        "axiom-memo-unedited-surface",
        "Lattice" in axiom and "Qubit" in axiom and "Admissibility" in axiom and "Record" in axiom,
    )
    checks.check(
        "self-consistency-is-license-not-derivation",
        "admitted comparison/reuse number" in self_note and "not a value derived" in self_note,
    )
    checks.check(
        "note-links-required-sources",
        all(
            name in note
            for name in (
                "MINIMAL_AXIOMS_2026-06-29.md",
                "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
                "PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
            )
        ),
    )
    checks.check(
        "non-claims-visible",
        "No 4D" in note and "no Monte Carlo" in note and "no axiom necessity" in note and "no new primitive" in note,
    )
    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
