#!/usr/bin/env python3
"""PMNS hw=1 carrier nonselection and scalar source/transfer boundary.

This runner replaces the old definition-shaped calculation

    sum_i P_i I_3 P_i = I_3

with the complete finite result on the named carrier:

1. the joint commutant of the three hw=1 translation involutions and the
   proper-cubic three-cycle is C I_3;
2. the four framework axioms do not supply a carrier operator or select the
   scalar normalization; two formal expansions of the same premise signature
   witness the non-entailment;
3. every nonsingular scalar active/passive pair produces only scalar basis
   columns and cycle-frame support under the implemented response interface,
   and is rejected by the explicitly defined one-sided-minimal support
   interface.

No PMNS helper module, observed value, fitted coordinate, or target PMNS
matrix is imported.
"""

from __future__ import annotations

import itertools
import inspect
import pathlib
import sys

import numpy as np

np.set_printoptions(precision=8, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1.0e-11
I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
TARGET_ACTIVE_SUPPORT = (np.abs(I3 + CYCLE) > 0).astype(int)


def permutation_matrices() -> tuple[np.ndarray, ...]:
    matrices: list[np.ndarray] = []
    for permutation in itertools.permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=complex)
        for row, column in enumerate(permutation):
            matrix[row, column] = 1.0
        matrices.append(matrix)
    return tuple(matrices)


PERMUTATION_MATRICES = permutation_matrices()
CYCLIC_MONOMIAL_SUPPORTS = tuple(
    (np.abs(np.linalg.matrix_power(CYCLE, power)) > TOL).astype(int)
    for power in range(3)
)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    message = f"  [{status}] {name}"
    if detail:
        message += f"  ({detail})"
    print(message)
    return condition


def matrix_unit(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i, j] = 1.0
    return out


E11 = matrix_unit(0, 0)
E22 = matrix_unit(1, 1)
E33 = matrix_unit(2, 2)


def pauli_cl3_generators() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def max_clifford_residual(gammas: tuple[np.ndarray, ...]) -> float:
    residual = 0.0
    for i, gamma_i in enumerate(gammas):
        for j, gamma_j in enumerate(gammas):
            target = 2.0 * I2 if i == j else np.zeros_like(I2)
            residual = max(
                residual,
                float(np.linalg.norm(gamma_i @ gamma_j + gamma_j @ gamma_i - target)),
            )
    return residual


def hw1_characters() -> tuple[tuple[int, int, int], ...]:
    return (-1, 1, 1), (1, -1, 1), (1, 1, -1)


def hw1_translations() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    characters = np.asarray(hw1_characters(), dtype=int)
    return tuple(
        np.diag(characters[:, axis]).astype(complex) for axis in range(3)
    )  # type: ignore[return-value]


def joint_character_projector(
    translations: tuple[np.ndarray, ...], character: tuple[int, int, int]
) -> np.ndarray:
    projector = I3.copy()
    for translation, sign in zip(translations, character, strict=True):
        projector = projector @ (I3 + sign * translation) / 2.0
    return projector


def hw1_projectors() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    translations = hw1_translations()
    return tuple(
        joint_character_projector(translations, character)
        for character in hw1_characters()
    )  # type: ignore[return-value]


def commutant_constraint_matrix(operators: tuple[np.ndarray, ...]) -> np.ndarray:
    """Return L with L vec(X)=0 iff X commutes with every operator.

    Column-major vectorization gives
    vec(XA-AX) = (A^T tensor I - I tensor A) vec(X).
    """

    identity = np.eye(3, dtype=complex)
    return np.vstack(
        [np.kron(operator.T, identity) - np.kron(identity, operator) for operator in operators]
    )


def numerical_rank(matrix: np.ndarray, tol: float = TOL) -> int:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return int(np.count_nonzero(singular_values > tol))


def nullspace_basis(matrix: np.ndarray, tol: float = TOL) -> list[np.ndarray]:
    _u, singular_values, vh = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.count_nonzero(singular_values > tol))
    return [vector.reshape((3, 3), order="F") for vector in vh[rank:].conj()]


def projector_resolve(seed: np.ndarray, projectors: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(
        (projector @ seed @ projector for projector in projectors),
        np.zeros((3, 3), dtype=complex),
    )


def group_average(seed: np.ndarray, projectors: tuple[np.ndarray, ...]) -> np.ndarray:
    dephased = projector_resolve(seed, projectors)
    return sum(
        (
            np.linalg.matrix_power(CYCLE, power)
            @ dephased
            @ np.linalg.matrix_power(CYCLE.conj().T, power)
            for power in range(3)
        ),
        np.zeros((3, 3), dtype=complex),
    ) / 3.0


def is_equivariant(block: np.ndarray, operators: tuple[np.ndarray, ...]) -> bool:
    return all(np.linalg.norm(block @ operator - operator @ block) < TOL for operator in operators)


def active_resolvent(alpha: float, lam: float) -> np.ndarray:
    denominator = 1.0 - lam * (alpha - 1.0)
    if abs(denominator) < TOL:
        raise np.linalg.LinAlgError("active scalar resolvent pole")
    return I3 / denominator


def passive_resolvent(beta: float, lam: float) -> np.ndarray:
    denominator = 1.0 - lam * beta
    if abs(denominator) < TOL:
        raise np.linalg.LinAlgError("passive scalar resolvent pole")
    return I3 / denominator


def response_columns(resolvent: np.ndarray) -> list[np.ndarray]:
    return [resolvent[:, column].copy() for column in range(3)]


def reconstruct_active_block(columns: list[np.ndarray], lam: float) -> np.ndarray:
    kernel = np.column_stack(columns)
    delta = (I3 - np.linalg.inv(kernel)) / lam
    return I3 + delta


def reconstruct_passive_block(columns: list[np.ndarray], lam: float) -> np.ndarray:
    kernel = np.column_stack(columns)
    return (I3 - np.linalg.inv(kernel)) / lam


def support_mask(block: np.ndarray, tol: float = TOL) -> np.ndarray:
    return (np.abs(block) > tol).astype(int)


def has_active_pmns_support(block: np.ndarray) -> bool:
    return any(
        np.array_equal(
            support_mask(permutation @ block @ permutation.conj().T),
            TARGET_ACTIVE_SUPPORT,
        )
        for permutation in PERMUTATION_MATRICES
    )


def has_monomial_support(block: np.ndarray) -> bool:
    mask = support_mask(block)
    return any(np.array_equal(mask, cyclic_mask) for cyclic_mask in CYCLIC_MONOMIAL_SUPPORTS)


def locally_rejected(active_block: np.ndarray, passive_block: np.ndarray) -> bool:
    active_support = has_active_pmns_support(active_block)
    passive_support = has_active_pmns_support(passive_block)
    active_monomial = has_monomial_support(active_block)
    passive_monomial = has_monomial_support(passive_block)
    one_sided_minimal = (
        active_support and passive_monomial and not passive_support
    ) or (
        passive_support and active_monomial and not active_support
    )
    return not one_sided_minimal


def conditional_unit_hw1_source_transfer_pack(lam_act: float, lam_pass: float) -> dict[str, object]:
    """Return the explicit conditional ``alpha=beta=1`` family member."""
    projectors = hw1_projectors()
    active_block = I3.copy()
    passive_block = I3.copy()
    active_r = active_resolvent(1.0, lam_act)
    passive_r = passive_resolvent(1.0, lam_pass)
    return {
        "active_block": active_block,
        "passive_block": passive_block,
        "active_resolvent": active_r,
        "passive_resolvent": passive_r,
        "active_columns": response_columns(active_r),
        "passive_columns": response_columns(passive_r),
        "source_projectors": projectors,
        "edge_basis": tuple(projector @ CYCLE for projector in projectors),
        "normalization_status": "conditional_unit_member_not_axiom_selected",
        "cl3_z3_packet": {
            "gammas": pauli_cl3_generators(),
            "translations": hw1_translations(),
            "characters": hw1_characters(),
            "projectors": projectors,
            "hw1_identity": I3.copy(),
            "free_sector": I3.copy(),
        },
    }


def sole_axiom_hw1_source_transfer_pack(lam_act: float, lam_pass: float) -> dict[str, object]:
    """Compatibility alias for :func:`conditional_unit_hw1_source_transfer_pack`.

    The historical name is retained only because five downstream diagnostic
    runners import it. Returned metadata makes the conditional normalization
    machine-visible. This function is not called by the revised derivation.
    """

    return conditional_unit_hw1_source_transfer_pack(lam_act, lam_pass)


def expect_pole(callable_) -> bool:
    try:
        callable_()
    except np.linalg.LinAlgError:
        return True
    return False


def part1_framework_and_hw1_packet() -> None:
    print("\n" + "=" * 92)
    print("PART 1: FRAMEWORK SURFACE AND HW=1 CHARACTER PACKET")
    print("=" * 92)

    axiom_path = pathlib.Path(__file__).resolve().parents[1] / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_text = axiom_path.read_text(encoding="utf-8")
    required_axiom_needles = (
        "### Lattice / Physical Locality",
        "### Qubit / Site Possibility",
        "### Admissibility / Local Constraint",
        "### Record / Fixed Reality",
        "choose a Hamiltonian or transfer operator",
        "source/action and physical-observable identification",
    )
    check(
        "The current premise source names all four axioms and excludes transfer/source-action supply",
        all(needle in axiom_text for needle in required_axiom_needles),
        f"source={axiom_path.relative_to(axiom_path.parents[1])}",
    )

    gammas = pauli_cl3_generators()
    check(
        "The one-site packet realizes M_2(C) ~= Cl(3,0)",
        max_clifford_residual(gammas) < TOL,
        f"max_residual={max_clifford_residual(gammas):.2e}",
    )

    translations = hw1_translations()
    projectors = hw1_projectors()
    check(
        "The restricted hw=1 translations are commuting involutions",
        all(np.linalg.norm(translation @ translation - I3) < TOL for translation in translations)
        and all(
            np.linalg.norm(left @ right - right @ left) < TOL
            for left, right in itertools.product(translations, repeat=2)
        ),
    )
    check(
        "The joint character projectors are rank-one orthogonal idempotents",
        all(np.linalg.norm(projector @ projector - projector) < TOL for projector in projectors)
        and all(round(float(np.trace(projector).real)) == 1 for projector in projectors)
        and all(
            np.linalg.norm(projectors[i] @ projectors[j]) < TOL
            for i in range(3)
            for j in range(3)
            if i != j
        ),
    )
    check(
        "The projectors are E11,E22,E33 and resolve I_3",
        all(
            np.linalg.norm(actual - expected) < TOL
            for actual, expected in zip(projectors, (E11, E22, E33), strict=True)
        )
        and np.linalg.norm(sum(projectors, np.zeros((3, 3), dtype=complex)) - I3) < TOL,
    )
    check(
        "The proper-cubic three-cycle permutes the three character lines transitively",
        all(
            any(
                np.linalg.norm(CYCLE @ projector @ CYCLE.conj().T - other) < TOL
                for other in projectors
            )
            for projector in projectors
        )
        and np.linalg.norm(np.linalg.matrix_power(CYCLE, 3) - I3) < TOL,
    )
    edge_frame = tuple(projector @ CYCLE for projector in projectors)
    check(
        "Projector transport gives exactly the ordered cycle matrix-unit frame",
        all(
            np.linalg.norm(actual - expected) < TOL
            for actual, expected in zip(
                edge_frame,
                (matrix_unit(0, 1), matrix_unit(1, 2), matrix_unit(2, 0)),
                strict=True,
            )
        ),
    )


def part2_joint_commutant_classification() -> None:
    print("\n" + "=" * 92)
    print("PART 2: COMPLETE JOINT-COMMUTANT CLASSIFICATION")
    print("=" * 92)

    translations = hw1_translations()
    translation_constraints = commutant_constraint_matrix(translations)
    cycle_constraints = commutant_constraint_matrix((CYCLE,))
    joint_constraints = commutant_constraint_matrix((*translations, CYCLE))

    translation_nullity = 9 - numerical_rank(translation_constraints)
    cycle_nullity = 9 - numerical_rank(cycle_constraints)
    joint_nullity = 9 - numerical_rank(joint_constraints)
    check(
        "The translation commutant has complex dimension 3 (the diagonal algebra)",
        translation_nullity == 3,
        f"nullity={translation_nullity}",
    )
    check(
        "The cycle commutant has complex dimension 3 (the circulant algebra)",
        cycle_nullity == 3,
        f"nullity={cycle_nullity}",
    )
    check(
        "The joint translation/cycle commutant has complex dimension 1",
        joint_nullity == 1,
        f"constraint_rank={numerical_rank(joint_constraints)}, nullity={joint_nullity}",
    )

    joint_basis = nullspace_basis(joint_constraints)
    scalar_residuals = [
        np.linalg.norm(basis - (np.trace(basis) / 3.0) * I3) for basis in joint_basis
    ]
    check(
        "The joint nullspace is exactly C I_3",
        len(joint_basis) == 1 and max(scalar_residuals, default=np.inf) < TOL,
        f"max_scalar_residual={max(scalar_residuals, default=np.inf):.2e}",
    )

    diagonal_control = np.diag([0.5, 1.0, 1.5]).astype(complex)
    circulant_control = I3 + 0.2 * (CYCLE + CYCLE.conj().T)
    check(
        "Negative control: a nonscalar diagonal commutes with translations but not C_3",
        is_equivariant(diagonal_control, translations)
        and not is_equivariant(diagonal_control, (CYCLE,)),
    )
    check(
        "Negative control: a nonscalar circulant commutes with C_3 but not all translations",
        is_equivariant(circulant_control, (CYCLE,))
        and not is_equivariant(circulant_control, translations),
    )


def part3_projector_map_and_normalization_nonselection() -> None:
    print("\n" + "=" * 92)
    print("PART 3: PROJECTOR MAP AND UNIT-NORMALIZATION NONSELECTION")
    print("=" * 92)

    axiom_path = pathlib.Path(__file__).resolve().parents[1] / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_text = axiom_path.read_text(encoding="utf-8")
    projectors = hw1_projectors()
    scalar_samples = (0.0, 0.5, 1.0, 1.75)
    check(
        "Projector resolution preserves every scalar seed alpha I_3, not only alpha=1",
        all(
            np.linalg.norm(projector_resolve(alpha * I3, projectors) - alpha * I3) < TOL
            for alpha in scalar_samples
        ),
    )

    generic_seed = np.array(
        [[0.4, 0.2 + 0.1j, -0.3j], [0.2 - 0.1j, 1.1, 0.15], [0.3j, 0.15, 1.7]],
        dtype=complex,
    )
    expected_average = (np.trace(generic_seed) / 3.0) * I3
    check(
        "Translation dephasing followed by C_3 averaging fixes shape but preserves input trace",
        np.linalg.norm(group_average(generic_seed, projectors) - expected_average) < TOL,
        f"alpha=Tr(X)/3={np.trace(generic_seed)/3.0}",
    )

    check(
        "The axiom source contains no active/passive carrier symbol or unit-normalization clause",
        all(token not in axiom_text for token in ("D_act", "D_pass", "alpha I_3", "beta I_3")),
    )

    carrier_operators = (*hw1_translations(), CYCLE)
    model_unit = I3
    model_half = 0.5 * I3
    check(
        "Two formal carrier expansions are positive Hermitian contractions",
        all(
            np.linalg.norm(block - block.conj().T) < TOL
            and np.linalg.eigvalsh(block).min() >= -TOL
            and np.linalg.eigvalsh(block).max() <= 1.0 + TOL
            for block in (model_unit, model_half)
        ),
    )
    check(
        "Both formal expansions obey every explicit translation/C_3 invariance",
        is_equivariant(model_unit, carrier_operators)
        and is_equivariant(model_half, carrier_operators),
    )
    check(
        "The two expansions have distinct normalizations on the same axiom/carrier signature",
        np.linalg.norm(model_unit - model_half) > 0.5,
        f"Tr(D_1)={np.trace(model_unit).real:.1f}, Tr(D_1/2)={np.trace(model_half).real:.1f}",
    )


def part4_scalar_family_response_and_reconstruction() -> None:
    print("\n" + "=" * 92)
    print("PART 4: COMPLETE SCALAR-FAMILY RESPONSE AND RECONSTRUCTION")
    print("=" * 92)

    lam_act = 0.25
    lam_pass = 0.25
    alpha_values = (0.0, 0.5, 1.0, 1.75)
    beta_values = (0.0, 0.5, 1.0, 2.0)

    response_ok = True
    reconstruction_ok = True
    rejection_ok = True
    frame_ok = True
    for alpha, beta in itertools.product(alpha_values, beta_values):
        active_r = active_resolvent(alpha, lam_act)
        passive_r = passive_resolvent(beta, lam_pass)
        active_columns = response_columns(active_r)
        passive_columns = response_columns(passive_r)

        active_scalar = np.trace(active_r) / 3.0
        passive_scalar = np.trace(passive_r) / 3.0
        response_ok &= np.linalg.norm(np.column_stack(active_columns) - active_scalar * I3) < TOL
        response_ok &= np.linalg.norm(np.column_stack(passive_columns) - passive_scalar * I3) < TOL

        active_block = reconstruct_active_block(active_columns, lam_act)
        passive_block = reconstruct_passive_block(passive_columns, lam_pass)
        reconstruction_ok &= np.linalg.norm(active_block - alpha * I3) < TOL
        reconstruction_ok &= np.linalg.norm(passive_block - beta * I3) < TOL
        rejection_ok &= locally_rejected(active_block, passive_block)

        transported = CYCLE @ np.column_stack(active_columns)
        frame_ok &= np.linalg.norm(transported - active_scalar * CYCLE) < TOL

    check(
        "Every scalar pair on the deterministic nonsingular grid gives only scalar basis-source columns",
        response_ok,
        f"pairs_tested={len(alpha_values) * len(beta_values)}",
    )
    check(
        "Response inversion reconstructs alpha I_3 and beta I_3 over the grid",
        reconstruction_ok,
    )
    check(
        "Forward transfer adds only a common scalar times the cycle frame",
        frame_ok,
    )
    check(
        "The defined one-sided-minimal support interface rejects every tested scalar pair",
        rejection_ok,
    )

    unit_active = active_resolvent(1.0, lam_act)
    unit_passive = passive_resolvent(1.0, lam_pass)
    half_active = active_resolvent(0.5, lam_act)
    half_passive = passive_resolvent(0.5, lam_pass)
    check(
        "The two same-premise normalizations produce different exact resolvents",
        np.linalg.norm(unit_active - I3) < TOL
        and np.linalg.norm(unit_passive - (4.0 / 3.0) * I3) < TOL
        and np.linalg.norm(half_active - (8.0 / 9.0) * I3) < TOL
        and np.linalg.norm(half_passive - (8.0 / 7.0) * I3) < TOL,
    )

    check(
        "The active scalar pole is rejected as an undefined response pack",
        expect_pole(lambda: active_resolvent(1.0 + 1.0 / lam_act, lam_act)),
    )
    check(
        "The passive scalar pole is rejected as an undefined response pack",
        expect_pole(lambda: passive_resolvent(1.0 / lam_pass, lam_pass)),
    )


def part5_escape_falsifier_and_input_firewall() -> None:
    print("\n" + "=" * 92)
    print("PART 5: NONSCALAR ESCAPE FALSIFIER AND INPUT FIREWALL")
    print("=" * 92)

    epsilon = 0.2
    active_escape = I3 + epsilon * CYCLE
    check(
        "A nonscalar I_3+epsilon C block has the active PMNS support shape",
        has_active_pmns_support(active_escape),
    )
    check(
        "The same nonscalar escape fails the zero-input translation invariance hypothesis",
        not is_equivariant(active_escape, hw1_translations())
        and is_equivariant(active_escape, (CYCLE,)),
    )

    swap_23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    orbit_active = swap_23 @ (I3 + CYCLE) @ swap_23.conj().T
    check(
        "The active-support interface recognizes permutation-conjugate I_3+C support",
        has_active_pmns_support(orbit_active),
    )
    check(
        "The passive interface accepts only the three cyclic monomial masks",
        has_monomial_support(I3)
        and has_monomial_support(CYCLE)
        and has_monomial_support(CYCLE @ CYCLE)
        and not has_monomial_support(swap_23),
    )

    forbidden_target_inputs = {
        "theta12",
        "theta13",
        "theta23",
        "delta_cp",
        "target_pmns",
        "observed_pmns",
    }
    module_functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    parameter_names = {
        parameter
        for _name, function in module_functions
        for parameter in inspect.signature(function).parameters
    }
    check(
        "No runner function accepts an observed/fitted PMNS target input",
        forbidden_target_inputs.isdisjoint(parameter_names),
        f"function_parameters={sorted(parameter_names)}",
    )


def main() -> int:
    print("=" * 92)
    print("PMNS HW=1 CARRIER NONSELECTION AND SCALAR SOURCE/TRANSFER BOUNDARY")
    print("=" * 92)
    print()
    print("Question:")
    print("  Within the explicit translation/C3-invariant hw=1 candidate class,")
    print("  what block shape follows, do the current axioms select its unit")
    print("  normalization, and does the conditional rejection depend on it?")

    part1_framework_and_hw1_packet()
    part2_joint_commutant_classification()
    part3_projector_map_and_normalization_nonselection()
    part4_scalar_family_response_and_reconstruction()
    part5_escape_falsifier_and_input_firewall()

    print("\n" + "=" * 92)
    print("RESULT")
    print("=" * 92)
    print("  Exact bounded result:")
    print("    - explicit joint translation/C3 invariance forces D = alpha I_3")
    print("    - the current axioms do not select alpha=1 or equate two sectors")
    print("    - projector resolution preserves, rather than selects, alpha")
    print("    - the analytic formulas give only scalar basis-source columns and")
    print("      cycle-frame support; the deterministic grid verifies reconstruction")
    print("    - the defined one-sided-minimal support interface rejects the scalar grid")
    print("  The unit pair (I_3,I_3) is one implementation point, not an")
    print("  axiom-derived normalization.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
