#!/usr/bin/env python3
"""One-plaquette J is not a certified 4D ln Z_L enclosure.

Paired note:
  docs/ONE_PLAQUETTE_FREE_ENERGY_IS_NOT_FOUR_D_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md

Recomputes the SU(3) single-link series from the June 10 recurrence with an
explicit Haar remainder. A remainder-controlled table of J and p_1 at
b in {5, 6, 7} is a proxy only. The numeral 0.5934 is not an input to J
or p_1.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/ONE_PLAQUETTE_FREE_ENERGY_IS_NOT_FOUR_D_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JUNE10_REL = (
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONE_PLAQUETTE_FREE_ENERGY_IS_NOT_FOUR_D_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
JUNE10_PATH = ROOT / JUNE10_REL
AXIOM_PATH = ROOT / AXIOM_REL

HALF = Fraction(1, 2)
TWO_FIFTHS = Fraction(2, 5)
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


def J_series(nmax: int) -> list[Fraction]:
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


def one_plaquette_J(b: Fraction, n_trunc: int) -> tuple[Fraction, Fraction]:
    """Remainder-controlled enclosure (J_lo, J_hi). Coupling only; no L."""
    coeffs = J_series(n_trunc + 2)
    j_lo = sum((coeffs[n] * b**n for n in range(n_trunc + 1)), Fraction(0))
    return j_lo, j_lo + exp_tail_majorant(n_trunc + 1, b)


def one_plaquette_enclosures(
    n_trunc: int, beta: Fraction
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return (J_lo, J_hi, Jprime_lo, Jprime_hi). No admitted numeral."""
    coeffs = J_series(n_trunc + 2)
    j_lo = sum((coeffs[n] * beta**n for n in range(n_trunc + 1)), Fraction(0))
    jp_lo = sum((n * coeffs[n] * beta ** (n - 1) for n in range(1, n_trunc + 1)), Fraction(0))
    rem_j = exp_tail_majorant(n_trunc + 1, beta)
    rem_jp = exp_tail_majorant(n_trunc, beta)
    return j_lo, j_lo + rem_j, jp_lo, jp_lo + rem_jp


def plaquette_count(L: int) -> int:
    return 6 * L**4


def link_count(L: int) -> int:
    return 4 * L**4


def wrapping_count(L: int) -> int:
    return 6 * L**2 * (2 * L - 1)


def enumerate_torus_counts(L: int) -> tuple[int, int]:
    """Exact (N_p, wrapping) by listing torus plaquettes."""
    total = 0
    wrap = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    site = (x0, x1, x2, x3)
                    for mu in range(4):
                        for nu in range(mu + 1, 4):
                            total += 1
                            if site[mu] == L - 1 or site[nu] == L - 1:
                                wrap += 1
    return total, wrap


def is_four_d_ln_z_l_enclosure(factor_count: int, L: int) -> bool:
    """True only if the enclosed object uses the 4D plaquette count."""
    return factor_count == plaquette_count(L)


def mutated_plaquette_count(_L: int) -> int:
    return 1


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
    print("AUDIT_TIMEOUT_SEC:", AUDIT_TIMEOUT_SEC)
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: June 10 recurrence, Haar majorant, L2 wrapping count; "
        "0.5934 is not an input to J or p_1"
    )

    note = NOTE_PATH.read_text(encoding="utf-8")
    june10 = JUNE10_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    checks.check(
        "audit-input-paths-exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/ONE_PLAQUETTE_FREE_ENERGY_IS_NOT_FOUR_D_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        f"{len(AUDIT_INPUT_PATHS)} paths",
    )

    coeffs = J_series(24)
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

    checks.check(
        "counting-L2-plaquettes-links-wrap",
        plaquette_count(2) == 96
        and link_count(2) == 64
        and wrapping_count(2) == 72
        and wrapping_count(2) == 6 * 4 * 3,
    )
    enum_p, enum_w = enumerate_torus_counts(2)
    checks.check(
        "L2-wrapping-enumerated",
        enum_p == plaquette_count(2) == 6 * 16 == 96 and enum_w == wrapping_count(2) == 72,
    )
    checks.check(
        "N-p-neq-1-for-L-ge-2",
        all(plaquette_count(L) != 1 for L in range(2, 8)),
    )

    j6_lo, j6_hi = one_plaquette_J(Fraction(6), 20)
    checks.check(
        "identity-j-is-not-ln-z-l",
        j6_lo > 0
        and j6_hi > j6_lo
        and not is_four_d_ln_z_l_enclosure(1, 2)
        and plaquette_count(2) == 96
        and plaquette_count(2) != 1,
        "N_p(2)=96 != 1",
    )
    checks.check(
        "identity-plaquette-count-not-one",
        plaquette_count(2) == 6 * 16 == 96 and mutated_plaquette_count(2) != 6 * 16,
    )
    checks.check(
        "wrapping-unused-by-one-plaquette-J",
        wrapping_count(2) == 72
        and one_plaquette_J.__code__.co_argcount == 2
        and one_plaquette_J(Fraction(6), 20) == (j6_lo, j6_hi),
    )

    table_ok = True
    p1_hi = {}
    for beta, j_floor, p_ceil in (
        (Fraction(5), Fraction(2), TWO_FIFTHS),
        (Fraction(6), Fraction(3), HALF),
        (Fraction(7), Fraction(5), HALF),
    ):
        j_lo, j_hi, jp_lo, jp_hi = one_plaquette_enclosures(20, beta)
        p_lo = jp_lo / j_hi
        p_up = jp_hi / j_lo
        p1_hi[int(beta)] = p_up
        table_ok = table_ok and j_lo > j_floor and p_up < p_ceil and p_lo > 0 and j_hi > j_lo
    checks.check(
        "theorem-2-three-point-J-and-p1",
        table_ok
        and p1_hi[5] < TWO_FIFTHS
        and p1_hi[6] < HALF
        and p1_hi[7] < HALF,
        "p1(5)<2/5, p1(6)<1/2, p1(7)<1/2",
    )

    j_lo16, _j_hi16, jp_lo16, jp_hi16 = one_plaquette_enclosures(16, Fraction(6))
    gap16 = j_lo16 - 2 * jp_hi16
    checks.check(
        "n16-b6-partial-sums-and-half-ceiling",
        j_lo16 == Fraction(251763633587, 73156608000)
        and jp_lo16 == Fraction(443237359, 304819200)
        and exp_tail_majorant(16, Fraction(6)) == Fraction(944784, 4379375)
        and gap16 == Fraction(5323057146257, 52306974720000)
        and gap16 > 0
        and jp_hi16 / j_lo16 < HALF,
    )

    admitted = Fraction(5934, 10000)
    checks.check(
        "mutation-forced-p1-rejected-by-remainder",
        p1_hi[6] < HALF < admitted and admitted != p1_hi[6],
        "p_1(6)<1/2<5934/10000",
    )

    checks.check(
        "note-does-not-derive-05934",
        "This note does not derive 0.5934." in note,
    )
    checks.check(
        "note-does-not-claim-ln-J-is-ln-Z-L",
        "does not claim ln J is ln Z_L" in note
        and "J` is not `Z_L" in note,
    )
    checks.check(
        "note-quotes-june10-interface",
        "a certified enclosure of `ln Z_L` at three couplings" in note
        and "a certified enclosure of `ln Z_L` at three couplings" in june10
        and "does not derive `0.5934`" in june10,
    )
    checks.check(
        "note-machine-status-contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "target_claim_id: certified_three_point_ln_z_l",
                'target_blocker_text: "produce certified ln Z_L enclosures at three couplings, or a mass-gap rate"',
                "reachability_to_target: prunes",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                'hypothetical_axiom_status: "no edit"',
            )
        ),
    )
    n5_lines = (
        "N5-1. \"Not a certified ln Z_L enclosure\"",
        "N5-2. \"Illegal substitution\"",
        "N5-3. \"Does not retire B1\"",
        "N5-4. \"Does not derive 0.5934\"",
        "N5-5. \"Mass-gap rate still open\"",
    )
    checks.check("n5-scoped-negative-lines", all(line in note for line in n5_lines))
    checks.check(
        "note-theorems-and-witnesses",
        all(
            phrase in note
            for phrase in (
                "N_p = 96",
                "N_ℓ = 64",
                "6 * 4 * 3 = 72",
                "a_3 = 1/648",
                "a_4 = 1/2592",
                "does not retire B1",
                "mass-gap",
            )
        ),
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN if phrase in note]
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "note-forbidden-phrases-absent",
        not forbidden_hits and retained_hits == [],
        ",".join(forbidden_hits + retained_hits),
    )
    checks.check(
        "june10-recurrence-and-wrapping-formula",
        "6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}" in june10
        and "0 <= a_n <= 1/n!" in june10
        and "6L^2(2L-1)" in june10,
    )
    checks.check(
        "axiom-memo-unedited-surface",
        "Lattice" in axiom and "Qubit" in axiom and "Admissibility" in axiom and "Record" in axiom,
    )
    checks.check(
        "note-links-required-sources",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
        in note,
    )
    checks.check(
        "non-claims-visible",
        "No 4D" in note and "no Monte Carlo" in note and "no axiom necessity" in note and "no new primitive" in note,
    )
    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
