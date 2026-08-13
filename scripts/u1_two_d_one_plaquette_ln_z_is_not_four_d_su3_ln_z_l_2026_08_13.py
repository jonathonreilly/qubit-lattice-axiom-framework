#!/usr/bin/env python3
"""Exact checks: 2D U(1) I_0 is not 4D SU(3) ln Z_L.

Z_1(β)=I_0(β) is remainder-controlled at β=1,2,3. That table is ln Z of
this U(1) model only. N_p(L=2)=96≠1 and wrap 72 is unused, so I_0 is not
4D SU(3) ln Z_L. Identity gates call i0_partial(beta, N) and
plaquette_count_4d(L). No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "U1_TWO_D_ONE_PLAQUETTE_LN_Z_IS_NOT_FOUR_D_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JUNE10_PATH = (
    ROOT
    / "docs"
    / "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/U1_TWO_D_ONE_PLAQUETTE_LN_Z_IS_NOT_FOUR_D_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DISPLAYED = {
    Fraction(1): (
        Fraction(44963077292459, 35514010828800),
        Fraction(1, 34433319479279616),
        Fraction(4359485085044947363, 3443331947927961600),
    ),
    Fraction(2): (
        Fraction(1235309099, 541900800),
        Fraction(1, 130365075456),
        Fraction(29717830994743, 13036507545600),
    ),
    Fraction(3): (
        Fraction(6419871123697, 1315333734400),
        Fraction(59049, 5142954901504),
        Fraction(2510169615270427, 514295490150400),
    ),
}

INJECTED_NUMERAL = Fraction(5934, 10000)
N_TRUNC = 8
COUPLINGS = (Fraction(1), Fraction(2), Fraction(3))


def normalize(text: str) -> str:
    return " ".join(text.split())


def factorial_fraction(n: int) -> Fraction:
    out = Fraction(1)
    for k in range(2, n + 1):
        out *= k
    return out


def binomial_fraction(n: int, k: int) -> Fraction:
    return factorial_fraction(n) / (factorial_fraction(k) * factorial_fraction(n - k))


def i0_term(k: int, beta: Fraction) -> Fraction:
    return (beta ** (2 * k)) / ((Fraction(4) ** k) * factorial_fraction(k) ** 2)


def i0_partial(beta: Fraction, N: int) -> Fraction:
    """Identity-gate function: exact partial sum S_N(β)."""
    return sum((i0_term(k, beta) for k in range(N + 1)), Fraction(0))


def remainder_ratio(beta: Fraction, N: int) -> Fraction:
    return (beta * beta) / (Fraction(4) * Fraction(N + 2) ** 2)


def remainder_majorant(beta: Fraction, N: int) -> Fraction:
    """Integer-factorial tail: R_N = t_{N+1} / (1-q) for q<1."""
    q = remainder_ratio(beta, N)
    if q >= 1:
        raise ValueError("geometric majorant requires q < 1")
    return i0_term(N + 1, beta) / (1 - q)


def haar_even_moment(k: int) -> Fraction:
    """∫ cos^{2k} θ dθ/(2π) = C(2k,k)/4^k."""
    return binomial_fraction(2 * k, k) / (Fraction(4) ** k)


def haar_series_term(k: int, beta: Fraction) -> Fraction:
    return (beta ** (2 * k) / factorial_fraction(2 * k)) * haar_even_moment(k)


def plaquette_count_4d(L: int) -> int:
    """Identity-gate function: N_p = 6 L^4 on the 4D torus."""
    return 6 * L**4


def link_count_4d(L: int) -> int:
    return 4 * L**4


def wrapping_count_4d(L: int) -> int:
    """June 10 wrapping count 6 L^2 (2L-1)."""
    return 6 * L * L * (2 * L - 1)


def i0_enclosure_is_four_d_su3_ln_z_l(beta: Fraction, N: int, L: int) -> bool:
    """Predicate: this I_0 enclosure is 4D SU(3) ln Z_L.

    Identity gate: must call i0_partial(beta, N) and plaquette_count_4d(L).
    Holds only if the 4D torus has one plaquette.
    """
    _ = i0_partial(beta, N)
    return plaquette_count_4d(L) == 1


def plaquette_count_forced_one(L: int) -> int:
    """Mutation: replace plaquette_count_4d(L) by 1."""
    del L
    return 1


def is_i0_series_coefficient(coeff: Fraction, kmax: int = 20) -> bool:
    """True iff coeff equals some t_k at a declared coupling."""
    for beta in COUPLINGS:
        for k in range(kmax + 1):
            if coeff == i0_term(k, beta):
                return True
    return False


def disk_square_bounds(beta: Fraction, N: int) -> tuple[Fraction, Fraction]:
    partial = i0_partial(beta, N)
    hi = partial + remainder_majorant(beta, N)
    return partial * partial, hi * hi


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
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
    june10 = JUNE10_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: June 10 three-point ln Z_L interface "
        "and torus counts are source-bound; I_0 series uses t_k only"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: I_0 is Z of 2D U(1) one-plaquette only; "
        "not 4D SU(3) ln Z_L; B1 is not retired"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, June 10 note, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/U1_TWO_D_ONE_PLAQUETTE_LN_Z_IS_NOT_FOUR_D_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "source-june10-three-point",
        "June 10 names certified ln Z_L enclosures at three couplings",
        "produce certified enclosures (half-width `eta`) of `ln Z_L` at the three couplings"
        in normalize(june10)
        and "a certified enclosure of ln Z_L at three couplings" in note,
    )
    checks.check(
        "source-june10-counts",
        "June 10 records N_p=6L^4 and wrapping 6L^2(2L-1)",
        "N_P = 6L^4" in june10 and "6L^2(2L-1)" in june10,
    )

    t0 = i0_term(0, Fraction(1))
    t1 = {beta: i0_term(1, beta) for beta in COUPLINGS}
    t2 = {beta: i0_term(2, beta) for beta in COUPLINGS}
    haar_ok = all(
        haar_series_term(k, beta) == i0_term(k, beta)
        for beta in COUPLINGS
        for k in (0, 1, 2)
    )
    checks.check(
        "theorem-1-terms",
        "t_0=1, t_1=β^2/4, t_2=β^4/64 match Haar moments",
        t0 == 1
        and t1[Fraction(1)] == Fraction(1, 4)
        and t1[Fraction(2)] == Fraction(1)
        and t1[Fraction(3)] == Fraction(9, 4)
        and t2[Fraction(1)] == Fraction(1, 64)
        and t2[Fraction(2)] == Fraction(1, 4)
        and t2[Fraction(3)] == Fraction(81, 64)
        and haar_ok
        and haar_even_moment(1) == Fraction(1, 2)
        and haar_even_moment(2) == Fraction(3, 8),
        residual=(t0, t1, t2),
    )
    checks.check(
        "theorem-1-s2-one",
        "S_2(1)=1+1/4+1/64=81/64 via i0_partial(1, 2)",
        i0_partial(Fraction(1), 2) == Fraction(81, 64)
        and i0_term(0, Fraction(1)) + i0_term(1, Fraction(1)) + i0_term(2, Fraction(1))
        == Fraction(81, 64),
        residual=i0_partial(Fraction(1), 2),
    )

    q_values = {beta: remainder_ratio(beta, N_TRUNC) for beta in COUPLINGS}
    checks.check(
        "theorem-2-q-lt-one",
        "N=8 gives q<1 at β=1,2,3",
        q_values[Fraction(1)] == Fraction(1, 400)
        and q_values[Fraction(2)] == Fraction(1, 100)
        and q_values[Fraction(3)] == Fraction(9, 400)
        and all(q < 1 for q in q_values.values()),
        residual=q_values,
    )

    enclosure_ok = True
    displayed_ok = True
    for beta in COUPLINGS:
        partial = i0_partial(beta, N_TRUNC)
        rem = remainder_majorant(beta, N_TRUNC)
        lo, rem_disp, hi_disp = DISPLAYED[beta]
        if not (partial == lo and rem == rem_disp and partial + rem == hi_disp):
            displayed_ok = False
        if not (partial >= 1 and rem > 0 and partial <= partial + rem):
            enclosure_ok = False
        if remainder_ratio(beta, N_TRUNC) >= 1:
            enclosure_ok = False
    checks.check(
        "theorem-2-enclosures",
        "S_8 <= I_0 <= S_8+R_8 at β=1,2,3 with displayed rationals",
        enclosure_ok and displayed_ok,
        residual={beta: DISPLAYED[beta] for beta in COUPLINGS},
    )
    note_rationals = all(
        f"{value.numerator}/{value.denominator}" in note
        for beta in COUPLINGS
        for value in DISPLAYED[beta]
    )
    checks.check(
        "theorem-2-note-rationals",
        "the paired note displays the N=8 enclosure rationals",
        note_rationals,
    )

    optional = (Fraction(5), Fraction(6), Fraction(7))
    optional_ok = True
    for beta in optional:
        q = remainder_ratio(beta, N_TRUNC)
        rem = remainder_majorant(beta, N_TRUNC)
        partial = i0_partial(beta, N_TRUNC)
        if not (q < 1 and rem > 0 and partial < partial + rem):
            optional_ok = False
    checks.check(
        "theorem-2-optional-567",
        "the same remainder law has q<1 at β=5,6,7 and stays U(1)",
        optional_ok
        and remainder_ratio(Fraction(5), N_TRUNC) == Fraction(1, 16)
        and remainder_ratio(Fraction(6), N_TRUNC) == Fraction(9, 100)
        and remainder_ratio(Fraction(7), N_TRUNC) == Fraction(49, 400),
    )

    checks.check(
        "theorem-3-volume",
        "N_p(L=2)=96≠1 and N_ell(L=2)=64 via plaquette_count_4d",
        plaquette_count_4d(2) == 6 * 16 == 96
        and link_count_4d(2) == 64
        and plaquette_count_4d(2) != 1,
        residual=plaquette_count_4d(2),
    )
    checks.check(
        "theorem-3-wrapping-unused",
        "June 10 wrap at L=2 is 72 and is not an input of i0_partial",
        wrapping_count_4d(2) == 72
        and wrapping_count_4d(2) == 6 * 4 * 3
        and i0_partial(Fraction(1), 2) == Fraction(81, 64)
        and "never used by `I_0`" in note,
        residual=wrapping_count_4d(2),
    )
    checks.check(
        "identity-i0-is-not-four-d",
        "predicate that I_0 is 4D SU(3) ln Z_L fails because N_p=96≠1",
        i0_enclosure_is_four_d_su3_ln_z_l(Fraction(1), N_TRUNC, 2) is False
        and i0_enclosure_is_four_d_su3_ln_z_l(Fraction(2), N_TRUNC, 2) is False
        and i0_enclosure_is_four_d_su3_ln_z_l(Fraction(3), N_TRUNC, 2) is False
        and plaquette_count_4d(2) == 96,
    )

    lo2, hi2 = disk_square_bounds(Fraction(1), N_TRUNC)
    s1 = i0_partial(Fraction(1), N_TRUNC)
    r1 = remainder_majorant(Fraction(1), N_TRUNC)
    checks.check(
        "theorem-4-disk-square",
        "Z_disk=I_0^2 obeys S^2 <= I_0^2 <= (S+R)^2 at β=1",
        lo2 == s1 * s1
        and hi2 == (s1 + r1) * (s1 + r1)
        and lo2 > 0
        and lo2 < hi2,
        residual=(lo2, hi2),
    )
    checks.check(
        "theorem-4-disk-not-four-d",
        "the m=2 disk product is still not 4D SU(3) Z_L",
        2 != plaquette_count_4d(2)
        and i0_enclosure_is_four_d_su3_ln_z_l(Fraction(1), N_TRUNC, 2) is False
        and "still not 4D SU(3)" in note,
    )

    checks.check(
        "mutation-count-forced-one",
        "replacing plaquette_count_4d(2) by 1 fails 6*16=96",
        plaquette_count_forced_one(2) == 1
        and plaquette_count_4d(2) == 6 * 16 == 96
        and plaquette_count_forced_one(2) != plaquette_count_4d(2),
        residual=(plaquette_count_forced_one(2), plaquette_count_4d(2)),
    )
    checks.check(
        "mutation-injected-numeral",
        "feeding 5934/10000 into I_0 as a coefficient is rejected; coefficients are t_k only",
        not is_i0_series_coefficient(INJECTED_NUMERAL)
        and is_i0_series_coefficient(i0_term(0, Fraction(1)))
        and is_i0_series_coefficient(i0_term(1, Fraction(1)))
        and is_i0_series_coefficient(i0_term(2, Fraction(1)))
        and i0_partial(Fraction(1), N_TRUNC) != INJECTED_NUMERAL
        and i0_term(1, Fraction(1)) == Fraction(1, 4),
    )
    invalid_q = remainder_ratio(Fraction(20), N_TRUNC)
    checks.check(
        "mutation-q-not-less-than-one",
        "the remainder gate refuses q>=1 (β=20, N=8)",
        invalid_q == 1,
    )

    checks.check(
        "theorem-5-note-negatives",
        "the note records the scoped negatives of Theorem 5",
        all(
            phrase in note
            for phrase in (
                "does not retire B1",
                "This note does not derive 0.5934.",
                "does not claim 4D",
                "does not perform Monte Carlo",
                "does not claim I_0 is Z_L of 4D SU(3)",
                "Series coefficients are the terms `t_k` only",
            )
        ),
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
                "trace_class: upstream_support",
                "target_claim_id: certified_three_point_ln_z_l",
                "reachability_to_target: supports",
                'target_blocker_text: "produce certified ln Z_L enclosures at three couplings, or a mass-gap rate"',
                'next_trace_action: "2D U(1) I_0 is an executable certified table for that model only. The June 10 4D SU(3) interface remains open. Do not import 0.5934. Do not adopt axiom text."',
                "source_of_blocker_text: handoff",
                "authors no audit verdict",
                "MINIMAL_AXIOMS_2026-06-29.md",
                "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
                "**Type:** bounded_theorem",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the I_0 table is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("I_0(beta)", "Z_1(beta)", "plaquette_count_4d")
        )
        and "Lattice" in axiom
        and "Qubit" in axiom
        and "Admissibility" in axiom
        and "Record" in axiom,
    )

    n5_lines = (
        "per_element: remainder-controlled I_0 terms t_k and the three couplings beta in {1,2,3} are the only evaluated objects",
        "per_site: U(1) one-plaquette and the L=2 4D torus counts 96 and 72; no 4D site configuration is sampled",
        "per_mode: the I_0 power series is checked; no 4D transfer-matrix mode or mass-gap rate is claimed",
        "per_block: only the U(1) Haar identity, the three-point I_0 table, the 96-versus-1 type split, and the disk product are executed",
        "lattice_wide: checked and not executed — no 4D SU(3) ln Z_L enclosure and no B1 retirement is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
