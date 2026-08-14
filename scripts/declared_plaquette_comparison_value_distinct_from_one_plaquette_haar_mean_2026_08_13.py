#!/usr/bin/env python3
"""Exact separation of a declared plaquette datum from the bare Haar mean.

Paired note:
  docs/DECLARED_PLAQUETTE_COMPARISON_VALUE_DISTINCT_FROM_ONE_PLAQUETTE_HAAR_MEAN_BOUNDED_THEOREM_NOTE_2026-08-13.md

The SU(3) one-plaquette series is recomputed from the June 10 recurrence.
The declared datum 5934/10000 enters only after the independent half-ceiling
for p_1(6) is closed. This runner writes no audit status or cache itself.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/DECLARED_PLAQUETTE_COMPARISON_VALUE_DISTINCT_FROM_ONE_PLAQUETTE_HAAR_MEAN_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JUNE10_REL = (
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_"
    "NARROW_THEOREM_NOTE_2026-06-10.md"
)
ALPHA_REL = "docs/ALPHA_S_DERIVED_NOTE.md"
SELF_REL = "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/DECLARED_PLAQUETTE_COMPARISON_VALUE_DISTINCT_FROM_ONE_PLAQUETTE_HAAR_MEAN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/ALPHA_S_DERIVED_NOTE.md",
    "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
)
AUDIT_TIMEOUT_SEC = 180

NOTE_PATH = ROOT / NOTE_REL
JUNE10_PATH = ROOT / JUNE10_REL
ALPHA_PATH = ROOT / ALPHA_REL
SELF_PATH = ROOT / SELF_REL

N_C = 3
G_BARE = Fraction(1)
BETA = Fraction(6)
HALF = Fraction(1, 2)
DECLARED_COMPARATOR = Fraction(5934, 10000)


def recurrence_coeffs(nmax: int, *, lag2_sign: int = 1) -> list[Fraction]:
    """Return a_0,...,a_(nmax-1); lag2_sign supports a mutation gate."""
    if nmax < 3:
        raise ValueError("nmax must include the three recurrence seeds")
    coeffs = [Fraction(1), Fraction(0), Fraction(1, 36)]
    for n in range(2, nmax - 1):
        numerator = (
            n * (n + 1) * coeffs[n]
            + 2 * (2 * n + 3) * coeffs[n - 1]
            + lag2_sign * coeffs[n - 2]
        )
        denominator = 6 * (n + 1) * (n + 4) * (n + 5)
        coeffs.append(numerator / denominator)
    return coeffs


def exp_tail_majorant(start: int, beta: Fraction) -> Fraction:
    """Bound sum_{k=start}^infinity beta^k/k! for exact beta>=0, start>beta."""
    if beta < 0 or Fraction(start) <= beta:
        raise ValueError("geometric majorant requires 0 <= beta < start")
    first = beta**start / factorial(start)
    return first * Fraction(start, 1) / (Fraction(start, 1) - beta)


def one_plaquette_enclosures(
    n_trunc: int, beta: Fraction
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return exact (J_lo, J_hi, Jprime_lo, Jprime_hi)."""
    coeffs = recurrence_coeffs(n_trunc + 1)
    j_lo = sum(
        (coeffs[n] * beta**n for n in range(n_trunc + 1)), Fraction(0)
    )
    jp_lo = sum(
        (n * coeffs[n] * beta ** (n - 1) for n in range(1, n_trunc + 1)),
        Fraction(0),
    )
    return (
        j_lo,
        j_lo + exp_tail_majorant(n_trunc + 1, beta),
        jp_lo,
        jp_lo + exp_tail_majorant(n_trunc, beta),
    )


def declared_matching(n_c: int, g_bare: Fraction) -> Fraction:
    if g_bare == 0:
        raise ZeroDivisionError("g_bare must be nonzero")
    return Fraction(2 * n_c, 1) / (g_bare * g_bare)


def matching_gate(matching_fn: Callable[[int, Fraction], Fraction]) -> bool:
    return (
        matching_fn(3, Fraction(1)) == Fraction(6)
        and matching_fn(3, Fraction(2)) == Fraction(3, 2)
        and matching_fn(2, Fraction(1)) == Fraction(4)
    )


def separation_gate(p1_upper: Fraction, comparator: Fraction) -> bool:
    return p1_upper < HALF < comparator


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    print("Declared plaquette comparator versus bare one-plaquette Haar mean")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: June 10 exact recurrence; alpha_s declared "
        "comparator; finite-diagnostic non-derivation boundary"
    )

    note = NOTE_PATH.read_text(encoding="utf-8")
    june10 = JUNE10_PATH.read_text(encoding="utf-8")
    alpha = ALPHA_PATH.read_text(encoding="utf-8")
    self_note = SELF_PATH.read_text(encoding="utf-8")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        f"{len(AUDIT_INPUT_PATHS)} paths",
    )
    checks.check(
        "audit-input-paths-unique-and-normalized",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(path).is_absolute() and ".." not in Path(path).parts for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 180)

    # Matching family and two explicit mutations.
    checks.check(
        "declared-matching-three-point-gate",
        matching_gate(declared_matching),
        "(N_c,g)=(3,1),(3,2),(2,1)",
    )
    checks.check(
        "declared-point-is-beta-six",
        declared_matching(N_C, G_BARE) == BETA,
    )
    checks.check(
        "mutation-product-matching-rejected",
        not matching_gate(lambda n_c, g: Fraction(2 * n_c, 1) * g * g),
    )
    checks.check(
        "mutation-missing-factor-two-rejected",
        not matching_gate(lambda n_c, g: Fraction(n_c, 1) / (g * g)),
    )

    # Exact recurrence family.
    coeffs = recurrence_coeffs(25)
    mutated = recurrence_coeffs(25, lag2_sign=-1)
    checks.check("recurrence-seed-a0", coeffs[0] == 1)
    checks.check("recurrence-seed-a1", coeffs[1] == 0)
    checks.check("recurrence-seed-a2", coeffs[2] == Fraction(1, 36))
    checks.check("recurrence-a3", coeffs[3] == Fraction(1, 648))
    checks.check("recurrence-a4", coeffs[4] == Fraction(1, 2592))
    checks.check(
        "recurrence-nonnegative-through-proof-truncation",
        all(value >= 0 for value in coeffs),
    )
    checks.check(
        "haar-moment-majorant-through-proof-truncation",
        all(value <= Fraction(1, factorial(n)) for n, value in enumerate(coeffs)),
    )
    checks.check(
        "mutation-recurrence-lag2-sign-rejected",
        mutated[3] != Fraction(1, 648) and mutated[3] != coeffs[3],
    )

    # Exact tail family and submitted off-by-one regression.
    tail_j16 = exp_tail_majorant(17, BETA)
    tail_jp16 = exp_tail_majorant(16, BETA)
    submitted_bad_tail_j16 = (
        Fraction(6**17, factorial(17)) * Fraction(18, 12)
    )
    checks.check(
        "tail-j16-correct-first-omitted-index",
        tail_j16 == Fraction(708588, 9634625),
    )
    checks.check(
        "tail-jprime16-exact",
        tail_jp16 == Fraction(944784, 4379375),
    )
    checks.check(
        "mutation-submitted-off-by-one-tail-rejected",
        submitted_bad_tail_j16 < tail_j16,
        "draft factor (N+2)/(N-4) is too small at N=16",
    )
    checks.check(
        "tail-generic-rational-beta",
        exp_tail_majorant(3, Fraction(3, 2))
        == Fraction(3, 2) ** 3 / factorial(3) * Fraction(3, 1) / Fraction(3, 2),
    )

    # Order-16 theorem.
    j16, j16_hi, jp16, jp16_hi = one_plaquette_enclosures(16, BETA)
    p16_lo = jp16 / j16_hi
    p16_hi = jp16_hi / j16
    exact_gap16 = j16 - 2 * jp16_hi
    checks.check(
        "n16-displayed-partial-sums",
        j16 == Fraction(251763633587, 73156608000)
        and jp16 == Fraction(443237359, 304819200),
    )
    checks.check(
        "n16-displayed-upper-envelope",
        jp16_hi == Fraction(259952292959, 155675520000),
    )
    checks.check(
        "n16-displayed-positive-gap",
        exact_gap16 == Fraction(5323057146257, 52306974720000)
        and exact_gap16 > 0,
    )
    checks.check(
        "n16-certified-half-ceiling",
        Fraction(0) < p16_lo < p16_hi < HALF,
        f"interval=({float(p16_lo):.12f},{float(p16_hi):.12f})",
    )

    # Order-20 independent truncation and final rational comparison.
    j20, j20_hi, jp20, jp20_hi = one_plaquette_enclosures(20, BETA)
    p20_lo = jp20 / j20_hi
    p20_hi = jp20_hi / j20
    checks.check(
        "n20-certified-interval-contained-in-n16",
        p16_lo < p20_lo < p20_hi < p16_hi,
        f"interval=({float(p20_lo):.12f},{float(p20_hi):.12f})",
    )
    checks.check("n20-independent-half-ceiling", 2 * jp20_hi < j20)
    checks.check(
        "declared-comparator-exact-rational",
        DECLARED_COMPARATOR == Fraction(2967, 5000),
    )
    checks.check(
        "strict-object-value-separation-n16",
        separation_gate(p16_hi, DECLARED_COMPARATOR),
    )
    checks.check(
        "strict-object-value-separation-n20",
        separation_gate(p20_hi, DECLARED_COMPARATOR),
    )
    checks.check(
        "mutation-comparator-as-haar-mean-rejected",
        not separation_gate(DECLARED_COMPARATOR, DECLARED_COMPARATOR),
    )
    checks.check(
        "comparator-not-used-by-haar-enclosure",
        one_plaquette_enclosures(16, BETA) == (j16, j16_hi, jp16, jp16_hi),
    )

    # Source provenance and current no-live-admission boundary.
    checks.check(
        "june10-recurrence-source-present",
        "6(N+1)(N+4)(N+5) a_{N+1}" in june10
        and "0 <= a_n <= 1/n!" in june10,
    )
    checks.check(
        "june10-withholds-comparator-derivation",
        "does not derive `0.5934`" in june10,
    )
    checks.check(
        "alpha-source-declares-comparison-input",
        "Declared boundary inputs" in alpha
        and "<P> = 0.5934" in alpha
        and "None of them is" in alpha
        and "claimed as derived by this note" in alpha,
    )
    checks.check(
        "finite-diagnostic-withholds-value-derivation",
        "0.5934" in self_note
        and "not a value derived" in self_note
        and "does not claim" in self_note,
    )

    # Audit-compatible note and trace surface.
    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "target_claim_id: alpha_s_derived_note",
        "target_blocker_text:",
        "source_of_blocker_text: handoff",
        "reachability_to_target: prunes",
        "artifact_role: theorem",
        "next_trace_action:",
        "conditional_surface_status:",
        "hypothetical_axiom_status: no edit",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-machine-status-complete",
        all(marker in note for marker in machine_markers),
    )
    checks.check(
        "note-dependency-links-complete",
        all(
            filename in note
            for filename in (
                "ALPHA_S_DERIVED_NOTE.md",
                "PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
                "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
            )
        ),
    )
    checks.check(
        "note-primary-name-is-explicit",
        note.startswith("---")
        and "# Declared Plaquette Comparison Value Is Distinct" in note
        and "# Plaquette B1" not in note,
    )
    checks.check(
        "note-correct-tail-formula",
        "(N+1)/(N-5)" in note and "(N+2) / (N-4)" not in note,
    )
    checks.check(
        "note-coupling-specific-boundary",
        "coupling-independent ceiling" in note
        and "coupling-specific at the declared `beta=6` point" in note,
    )
    checks.check(
        "note-object-separation-boundary",
        "object-separation" in note
        and "It is not the interacting 4D object" in note
        and "No 4D" in note,
    )

    # No-Go Discipline N1-N8 and route preservation.
    checks.check(
        "no-go-n1-through-n8-present",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "no-go-n1-route-count-and-markers",
        note.count("**ATTEMPTED**") >= 5
        and "correlated 4D Wilson/Haar measure" in note
        and "finite-volume `ln Z_L`" in note,
    )
    checks.check(
        "no-go-steelman-accepted",
        "The objection is" in note
        and "correct. The theorem is retained only" in note
        and "4D correlations can change the mean" in note,
    )
    checks.check(
        "no-go-live-routes-preserved",
        "preserved as the June 10 certification route" in note
        and "remains open" in note,
    )

    # Machine-readable N5 certificate lines are also emitted to cache stdout.
    n5_lines = (
        "per-element: executed — exact recurrence coefficient arithmetic",
        "per-site: not applicable — the proved object has no lattice sites",
        "per-mode: not applicable — no mode decomposition is used",
        "per-block: executed — the one-plaquette Haar block is fully bounded",
        "lattice-wide: not executed — no correlated 4D lattice is evaluated",
    )
    checks.check("n5-certificate-five-lines-in-note", all(line in note for line in n5_lines))
    print("N5_CERTIFICATE:")
    for line in n5_lines:
        print(line)

    checks.check(
        "explicit-nonclaims-visible",
        "No axiom edit" in note
        and "No 4D" in note
        and "not a derived or admitted theorem" in note,
    )
    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
