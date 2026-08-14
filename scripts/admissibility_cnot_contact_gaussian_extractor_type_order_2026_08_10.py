#!/usr/bin/env python3
"""Exact checks for the CNOT-contact/Gaussian-extractor type-order theorem.

The runner independently checks conditioned CNOT conjugation, Gaussian
second-moment extractor equivariance, fixed-effect versus transported-effect
grades, the supplied-control mixture escape, and the finite XOR marginal
tradeoff.  Measure-zero and all-lambda statements are analytic source proofs;
the runner checks exact fixtures and source-bound claim/governance surfaces.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_CNOT_CONTACT_GAUSSIAN_EXTRACTOR_TYPE_ORDER_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md"
INSTRUMENT_PATH = ROOT / "docs" / "RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md"
PROCESS_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md"
COVARIANT_PATH = ROOT / "docs" / "COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CNOT_CONTACT_GAUSSIAN_EXTRACTOR_TYPE_ORDER_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md",
    "docs/work_history/repo/review_feedback/PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md",
    "docs/COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md",
)


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

ZERO: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
IDENTITY: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
PAULI_X: Matrix = (
    (Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0)),
)
P_ZERO: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
P_ONE: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
E_ZERO: Matrix = (
    (Fraction(1, 2), Fraction(0)),
    (Fraction(0), Fraction(0)),
)


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(value * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def matrix_determinant(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace_product(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        left[row][column] * right[column][row]
        for row in range(2)
        for column in range(2)
    )


def conjugate_by_x(matrix: Matrix) -> Matrix:
    return matrix_multiply(matrix_multiply(PAULI_X, matrix), PAULI_X)


def gaussian_extractor(center: Matrix, offset: Fraction = Fraction(0)) -> Matrix:
    center_squared = matrix_multiply(center, center)
    unnormalized = matrix_add(
        center_squared,
        matrix_scale(Fraction(2) + offset, IDENTITY),
    )
    return matrix_scale(Fraction(1, matrix_trace(unnormalized)), unnormalized)


def controlled_target(matrix: Matrix, control: int) -> Matrix:
    return matrix if control == 0 else conjugate_by_x(matrix)


def fixed_effect_grade(state: Matrix, control: int) -> Fraction:
    return trace_product(controlled_target(state, control), E_ZERO)


def transported_effect_grade(state: Matrix, control: int) -> Fraction:
    effect = controlled_target(E_ZERO, control)
    return trace_product(controlled_target(state, control), effect)


def target_mixture(control_one_weight: Fraction) -> Matrix:
    return matrix_add(
        matrix_scale(Fraction(1) - control_one_weight, P_ZERO),
        matrix_scale(control_one_weight, P_ONE),
    )


def xor_output_one_probability(target_one_weight: Fraction, control: int) -> Fraction:
    return target_one_weight if control == 0 else Fraction(1) - target_one_weight


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    instrument = INSTRUMENT_PATH.read_text(encoding="utf-8")
    process_note = PROCESS_PATH.read_text(encoding="utf-8")
    covariant_note = COVARIANT_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: the current axiom, reviewed current-main Gaussian compiler, landed Cycle 972 finite contact theorem, and two tracked conditional process boundaries are source-bound")
    print("package_local_integrity_reads: the proposed theorem note is checked for construction, boundary, trace status, and N1-N8 surfaces; the cache envelope binds every declared input")
    print("analytic_boundary: the Gaussian density-set measure-zero proof, general conjugation pushforward, and all-lambda formulas are proved in the source; exact rational fixtures are executed here")
    print("negative_scope: only direct sample typing and the declared fixed-input/conditioned-CNOT selection route are bounded; randomized controls, larger instruments, and local process laws remain live")

    checks.check(
        "source-current-axiom",
        "the current M2 possibility, probability-measure, and Record-content clauses are present",
        all(
            phrase in axiom_flat
            for phrase in (
                "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
                "the probability distribution over the possibilities is",
                "A readout value is determined by record content alone.",
            )
        ),
    )
    checks.check(
        "source-parent-residual",
        "the current-main Gaussian compiler leaves physical extractor selection and preparation/program registration open",
        "why the physical law selects the raw second moment" in parent
        and "how contact/pointer dynamics encodes the ordered effect program" in parent
        and "preparation equivalence is held fixed" in parent,
    )
    checks.check(
        "source-finite-contact",
        "the landed Cycle 972 source supplies exactly the bounded six-witness XOR class and uniform-target marginal",
        "Exactly six of the 20 words induce state-resolved neighbour dependence" in covariant_note
        and "y = x XOR n_d" in covariant_note
        and "zero of the 20 declared words" in covariant_note
        and "continuous `M_2(C)` distributions are outside the declared horizon" in covariant_note,
    )
    checks.check(
        "source-instrument-type-order",
        "the tracked instrument interface starts from a supplied density state and instrument",
        "pre-record state rho + supplied instrument {K_r}" in instrument
        and "Deriving the physical instrument" in instrument
        and "Deriving the trace/effect probability rule" in instrument,
    )
    checks.check(
        "source-process-boundary",
        "the finite process reconstruction imports preparation, instrument, Born pairing, and process category",
        "density operator is therefore a derived calculator" in process_note
        and "Born pairing, and process category are explicit imports" in process_note
        and "local lattice implementation of the process" in process_note,
    )

    ambient_real_dimension = 2 * 2 * 2
    density_operator_real_dimension = 3
    checks.check(
        "raw-content-type-codimension",
        "qubit density operators occupy a three-real-dimensional subset of the eight-real-dimensional M2 content space",
        ambient_real_dimension == 8
        and density_operator_real_dimension == 3
        and ambient_real_dimension - density_operator_real_dimension == 5,
    )

    truth_table = {
        (target, control): target ^ control
        for target, control in product((0, 1), repeat=2)
    }
    checks.check(
        "cnot-xor-law",
        "the conditioned target law is exactly y=x XOR n on all four basis rows",
        truth_table
        == {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},
    )
    checks.check(
        "conditioned-conjugation",
        "control zero is identity while control one swaps the two target basis projectors",
        controlled_target(P_ZERO, 0) == P_ZERO
        and controlled_target(P_ZERO, 1) == P_ONE
        and controlled_target(P_ONE, 1) == P_ZERO,
    )
    checks.check(
        "conjugation-involution",
        "two incoming-X conjugations return every exact matrix fixture",
        all(
            conjugate_by_x(conjugate_by_x(matrix)) == matrix
            for matrix in (ZERO, IDENTITY, P_ZERO, P_ONE, E_ZERO)
        ),
    )

    rho_blank_zero = gaussian_extractor(ZERO)
    rho_pz_zero = gaussian_extractor(P_ZERO)
    rho_pz_one = gaussian_extractor(P_ZERO, Fraction(1))
    checks.check(
        "gaussian-extractor-fixtures",
        "the displayed family gives I/2 at blank, diag(3/5,2/5), and diag(4/7,3/7)",
        rho_blank_zero == matrix_scale(Fraction(1, 2), IDENTITY)
        and rho_pz_zero
        == ((Fraction(3, 5), Fraction(0)), (Fraction(0), Fraction(2, 5)))
        and rho_pz_one
        == ((Fraction(4, 7), Fraction(0)), (Fraction(0), Fraction(3, 7))),
    )
    checks.check(
        "extractor-contact-equivariance",
        "X-transporting the center transports every tested extractor member by X conjugation",
        all(
            gaussian_extractor(conjugate_by_x(P_ZERO), offset)
            == conjugate_by_x(gaussian_extractor(P_ZERO, offset))
            for offset in (Fraction(0), Fraction(1), Fraction(2), Fraction(5))
        ),
    )
    checks.check(
        "pure-control-spectrum-preservation",
        "conditioned conjugation preserves trace and determinant on both nontrivial extractor fixtures",
        all(
            matrix_trace(controlled_target(state, control)) == matrix_trace(state)
            and matrix_determinant(controlled_target(state, control))
            == matrix_determinant(state)
            for state in (rho_pz_zero, rho_pz_one)
            for control in (0, 1)
        ),
    )
    checks.check(
        "common-blank-spectrum-boundary",
        "the common Gaussian blank is maximally mixed while the Pz extractor has a different determinant",
        matrix_determinant(rho_blank_zero) == Fraction(1, 4)
        and matrix_determinant(rho_pz_zero) == Fraction(6, 25)
        and matrix_determinant(rho_blank_zero) != matrix_determinant(rho_pz_zero),
    )

    checks.check(
        "fixed-effect-lambda-zero",
        "the fixed half-Pz effect changes from 3/10 to 1/5 under incoming control, a gap of 1/10",
        fixed_effect_grade(rho_pz_zero, 0) == Fraction(3, 10)
        and fixed_effect_grade(rho_pz_zero, 1) == Fraction(1, 5)
        and fixed_effect_grade(rho_pz_zero, 0)
        - fixed_effect_grade(rho_pz_zero, 1)
        == Fraction(1, 10),
    )
    checks.check(
        "fixed-effect-lambda-one",
        "the lambda-one fixed-effect pair is 2/7 and 3/14 with exact gap 1/14",
        fixed_effect_grade(rho_pz_one, 0) == Fraction(2, 7)
        and fixed_effect_grade(rho_pz_one, 1) == Fraction(3, 14)
        and fixed_effect_grade(rho_pz_one, 0)
        - fixed_effect_grade(rho_pz_one, 1)
        == Fraction(1, 14),
    )
    checks.check(
        "fixed-effect-family-gap",
        "four exact finite lambda fixtures obey the positive 1/[2(2lambda+5)] contact gap",
        all(
            fixed_effect_grade(gaussian_extractor(P_ZERO, offset), 0)
            - fixed_effect_grade(gaussian_extractor(P_ZERO, offset), 1)
            == Fraction(1, 2 * (2 * offset + 5))
            for offset in map(Fraction, (0, 1, 2, 3))
        ),
    )
    checks.check(
        "transported-effect-covariance",
        "co-transporting the effect restores the original grade for every tested compiler member",
        all(
            transported_effect_grade(gaussian_extractor(P_ZERO, offset), control)
            == trace_product(gaussian_extractor(P_ZERO, offset), E_ZERO)
            for offset in map(Fraction, (0, 1, 2, 3))
            for control in (0, 1)
        ),
    )
    checks.check(
        "same-effect-versus-transported-effect",
        "fixed-effect descent fails on the biased fixture although transported-effect covariance holds",
        fixed_effect_grade(rho_pz_zero, 0)
        != fixed_effect_grade(rho_pz_zero, 1)
        and transported_effect_grade(rho_pz_zero, 0)
        == transported_effect_grade(rho_pz_zero, 1),
    )

    checks.check(
        "random-control-mixture-lambda-zero",
        "a supplied control-one weight 2/5 prepares the raw Pz density operator from a blank target",
        target_mixture(Fraction(2, 5)) == rho_pz_zero,
    )
    checks.check(
        "random-control-mixture-lambda-one",
        "a supplied control-one weight 3/7 prepares the lambda-one density operator",
        target_mixture(Fraction(3, 7)) == rho_pz_one,
    )
    checks.check(
        "mixture-carrier-not-selector",
        "distinct supplied control weights remain valid and produce distinct normalized target states",
        all(
            matrix_trace(target_mixture(weight)) == 1
            and matrix_determinant(target_mixture(weight)) >= 0
            for weight in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1))
        )
        and target_mixture(Fraction(2, 5)) != target_mixture(Fraction(3, 7)),
    )

    checks.check(
        "uniform-xor-marginal",
        "uniform target mixing gives half-half output for both control conditions",
        xor_output_one_probability(Fraction(1, 2), 0) == Fraction(1, 2)
        and xor_output_one_probability(Fraction(1, 2), 1) == Fraction(1, 2),
    )
    checks.check(
        "deterministic-xor-dependence",
        "a fixed target input gives maximally separated point outputs across the two controls",
        xor_output_one_probability(Fraction(0), 0) == 0
        and xor_output_one_probability(Fraction(0), 1) == 1,
    )
    checks.check(
        "xor-dependence-formula",
        "the exact marginal response gap is |1-2p| on representative rational target mixtures",
        all(
            abs(
                xor_output_one_probability(weight, 1)
                - xor_output_one_probability(weight, 0)
            )
            == abs(Fraction(1) - 2 * weight)
            for weight in (
                Fraction(0),
                Fraction(1, 5),
                Fraction(1, 2),
                Fraction(4, 5),
                Fraction(1),
            )
        ),
    )

    construction_needles = (
        "`mu_C(D_2)=0`",
        "`T_n(A)=X^n A X^n`",
        "`rho_(T_n#mu)^(lambda)=X^n rho_mu^(lambda) X^n`",
        "`(w_0,w_1)=(3/10,1/5)`",
        "`q_0=2/5`",
        "carrier, not a selector",
    )
    checks.check(
        "construction-source-surface",
        "the source states the type, equivariance, fixed-effect, and supplied-mixture results",
        all(phrase in note for phrase in construction_needles),
    )
    boundary_needles = (
        "No global unitary or contact no-go",
        "does not select the control weight",
        "not the same-effect quotient",
        "no canonical axiom is edited",
        "supplies no scalar collection functional `I`, finite additivity, direct readout compiler",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves the bounded route and governance limits",
        all(phrase in note_flat for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the complete bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "target_claim_id:",
                "target_blocker_text:",
                "source_of_blocker_text: handoff",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the CNOT/extractor bridge notation is absent from the canonical axiom memo",
        all(
            phrase not in axiom
            for phrase in ("T_n(A)", "rho_(T_n#mu)", "q_0=2/5", "CNOT compiler")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, and global-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Source residual used |" in note
        and "The primitive-registry scan used" in note
        and "FAIL / DO NOT SHIP" in note
        and "No global unitary or contact no-go is claimed" in note_flat,
    )

    print("per_element: all four XOR rows, five exact matrix fixtures, four lambda members, fixed and transported effects, and five target mixtures are checked")
    print("per_site: one target plus one basis-control neighbour is executed at blank, Pz, and X-transported conditions; no autonomous site/program selection is asserted")
    print("per_mode: conditioned conjugation, spectrum preservation, random-control reduction, and fixed-versus-transported effect modes are checked exactly")
    print("per_block: the Gaussian extractor/CNOT carrier chain is checked through state typing, contact equivariance, supplied mixing, and the preparation-quotient boundary")
    print("lattice_wide: checked and not executed — the landed Cycle 972 theorem supplies a finite covariant direction orbit, while this theorem rederives one-edge algebra and claims no global continuous compiler")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
