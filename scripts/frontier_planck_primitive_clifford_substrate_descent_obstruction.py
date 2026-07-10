#!/usr/bin/env python3
"""Exact/numerical certificate for the Planck Clifford carrier descent gate.

This runner tests the bridge that the older construction runner did not test:
whether the spatial action already carried by the event-cell one-form packet
is the spatial-bivector action induced by an irreducible complex Cl_4 module.

The decisive intertwiner and Casimir calculations are exact SymPy linear
algebra.  The larger full-cell algebra/commutant ranks use NumPy on matrices
whose entries are Gaussian integers or half-integers, with reported singular
value gaps.

Exit code: 0 when every obstruction/cross-check is reproduced, 1 otherwise.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

import frontier_planck_primitive_clifford_majorana_edge_derivation as conditional_helper


PASS_BLOCKS = 0
FAIL_BLOCKS = 0
TOL = 1.0e-10


def block(name: str, passed: bool, detail: str) -> bool:
    global PASS_BLOCKS, FAIL_BLOCKS
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_BLOCKS += 1
    else:
        FAIL_BLOCKS += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def numerical_rank_and_gap(matrix: np.ndarray) -> tuple[int, float, float]:
    singular = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular > TOL))
    smallest_nonzero = float(singular[rank - 1]) if rank else 0.0
    largest_zero = float(singular[rank]) if rank < len(singular) else 0.0
    return rank, smallest_nonzero, largest_zero


def commutant_dimension(generators: list[np.ndarray]) -> tuple[int, float, float]:
    dim = generators[0].shape[0]
    ident = np.eye(dim, dtype=complex)
    system = np.vstack(
        [np.kron(ident, gen) - np.kron(gen.T, ident) for gen in generators]
    )
    rank, smallest_nonzero, largest_zero = numerical_rank_and_gap(system)
    return dim * dim - rank, smallest_nonzero, largest_zero


def center_dimension(
    algebra_basis: list[np.ndarray], generators: list[np.ndarray]
) -> tuple[int, float, float]:
    """Dimension of algebra elements commuting with all generators."""
    columns = []
    for basis_element in algebra_basis:
        columns.append(
            np.concatenate(
                [commutator(basis_element, generator).reshape(-1) for generator in generators]
            )
        )
    system = np.column_stack(columns)
    rank, smallest_nonzero, largest_zero = numerical_rank_and_gap(system)
    return len(algebra_basis) - rank, smallest_nonzero, largest_zero


def algebra_span(generators: list[np.ndarray]) -> list[np.ndarray]:
    dim = generators[0].shape[0]
    basis: list[np.ndarray] = []
    flat_basis = np.empty((dim * dim, 0), dtype=complex)

    def add(candidate: np.ndarray) -> bool:
        nonlocal flat_basis
        trial = np.column_stack((flat_basis, candidate.reshape(-1)))
        rank = np.linalg.matrix_rank(trial, tol=TOL)
        if rank > flat_basis.shape[1]:
            basis.append(candidate)
            flat_basis = trial
            return True
        return False

    add(np.eye(dim, dtype=complex))
    for generator in generators:
        add(generator)
    changed = True
    while changed:
        changed = False
        for existing in list(basis):
            for generator in generators:
                changed = add(existing @ generator) or changed
    return basis


def clifford_generators_4() -> list[sp.Matrix]:
    ident2 = sp.eye(2)
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.diag(1, -1)
    return [
        sp.kronecker_product(x, ident2),
        sp.kronecker_product(y, ident2),
        sp.kronecker_product(z, x),
        sp.kronecker_product(z, y),
    ]


def substrate_spin_one_plus_scalar() -> list[sp.Matrix]:
    """Hermitian su(2) generators on (t,x,y,z) = 1 + 3."""
    out: list[sp.Matrix] = []
    for axis in range(3):
        matrix = sp.zeros(4)
        for j in range(3):
            for k in range(3):
                matrix[1 + j, 1 + k] = -sp.I * sp.LeviCivita(axis, j, k)
        out.append(matrix)
    return out


def induced_clifford_spin_half_doublet(gamma: list[sp.Matrix]) -> list[sp.Matrix]:
    # Spatial coframe order is (n,tau_1,tau_2) = gamma[1:4].
    return [
        -sp.I * gamma[2] * gamma[3] / 2,
        -sp.I * gamma[3] * gamma[1] / 2,
        -sp.I * gamma[1] * gamma[2] / 2,
    ]


def exact_intertwiner_nullity(
    substrate: list[sp.Matrix], clifford_spin: list[sp.Matrix]
) -> tuple[int, int]:
    # Column-major vec(J A - A T) = (I kron J - T^T kron I) vec(A).
    system = sp.Matrix.vstack(
        *[
            sp.kronecker_product(sp.eye(4), j)
            - sp.kronecker_product(t.T, sp.eye(4))
            for j, t in zip(substrate, clifford_spin, strict=True)
        ]
    )
    rank = system.rank()
    return rank, 16 - rank


def exterior_cell_operators() -> tuple[
    list[tuple[int, ...]], list[np.ndarray], list[np.ndarray], np.ndarray
]:
    subsets = [
        subset
        for degree in range(5)
        for subset in itertools.combinations(range(4), degree)
    ]
    index = {subset: i for i, subset in enumerate(subsets)}
    creators: list[np.ndarray] = []
    for axis in range(4):
        wedge = np.zeros((16, 16), dtype=complex)
        for subset in subsets:
            if axis in subset:
                continue
            sign = (-1) ** sum(item < axis for item in subset)
            target = tuple(sorted((axis, *subset)))
            wedge[index[target], index[subset]] = sign
        creators.append(wedge)
    annihilators = [creator.conj().T for creator in creators]
    gamma = [
        creator + annihilator
        for creator, annihilator in zip(creators, annihilators, strict=True)
    ]
    p_one = np.diag([1.0 if len(subset) == 1 else 0.0 for subset in subsets])
    return subsets, creators, gamma, p_one


def native_cubic_clifford() -> tuple[list[np.ndarray], dict[str, np.ndarray]]:
    ident2 = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1.0, -1.0]).astype(complex)
    pauli = {"I": ident2, "X": x, "Y": y, "Z": z}

    def word(label: str) -> np.ndarray:
        out = pauli[label[0]]
        for letter in label[1:]:
            out = np.kron(out, pauli[letter])
        return out

    return [word("XII"), word("YXI"), word("YYX")], {
        label: word(label)
        for label in map("".join, itertools.product("IXYZ", repeat=3))
    }


def main() -> int:
    print("=" * 78)
    print("PLANCK PRIMITIVE CLIFFORD SUBSTRATE-DESCENT OBSTRUCTION")
    print("=" * 78)
    print()
    print("Question:")
    print("  Even granting P_A = Lambda^1 W, does its supplied exterior")
    print("  substrate action agree with the spatial bivector action induced")
    print("  by an irreducible Cl_4(C) module, and does the canonical full-cell")
    print("  Clifford action restrict to P_A?")
    print()

    gamma4 = clifford_generators_4()
    helper_gamma = conditional_helper.clifford_generators()
    helper_gamma_match = all(
        np.linalg.norm(
            np.array(exact.tolist(), dtype=complex) - numeric
        )
        < TOL
        for exact, numeric in zip(gamma4, helper_gamma.values(), strict=True)
    )
    substrate = substrate_spin_one_plus_scalar()
    clifford_spin = induced_clifford_spin_half_doublet(gamma4)

    su2_substrate = all(
        substrate[i] * substrate[j]
        - substrate[j] * substrate[i]
        == sp.I * sum(
            (sp.LeviCivita(i, j, k) * substrate[k] for k in range(3)),
            sp.zeros(4),
        )
        for i in range(3)
        for j in range(3)
    )
    substrate_casimir = sum((j * j for j in substrate), sp.zeros(4))
    block(
        "1. supplied exterior P_A action is the scalar-plus-vector module",
        su2_substrate
        and substrate_casimir.eigenvals() == {sp.Integer(0): 1, sp.Integer(2): 3},
        f"exact Casimir spectrum={substrate_casimir.eigenvals()} (1 + 3)",
    )

    su2_clifford = all(
        clifford_spin[i] * clifford_spin[j]
        - clifford_spin[j] * clifford_spin[i]
        == sp.I * sum(
            (sp.LeviCivita(i, j, k) * clifford_spin[k] for k in range(3)),
            sp.zeros(4),
        )
        for i in range(3)
        for j in range(3)
    )
    clifford_casimir = sum((t * t for t in clifford_spin), sp.zeros(4))
    block(
        "2. irreducible Cl_4 spatial bivectors are two spin-half doublets",
        su2_clifford
        and clifford_casimir == sp.Rational(3, 4) * sp.eye(4)
        and helper_gamma_match,
        (
            f"exact Casimir={sp.Rational(3, 4)} I_4 (2 + 2); "
            "conditional-helper matrices match"
        ),
    )

    rank, nullity = exact_intertwiner_nullity(substrate, clifford_spin)
    block(
        "3. no substrate-to-Clifford spatial intertwiner exists on P_A",
        rank == 16 and nullity == 0,
        f"exact simultaneous-intertwiner system rank={rank}, nullity={nullity}",
    )

    _, creators, gamma_cell, p_one = exterior_cell_operators()
    ident16 = np.eye(16, dtype=complex)
    clifford_error = max(
        np.linalg.norm(
            anticommutator(gamma_cell[i], gamma_cell[j])
            - (2.0 if i == j else 0.0) * ident16
        )
        for i in range(4)
        for j in range(4)
    )
    block(
        "4. canonical wedge-plus-contraction operators realize Cl_4 on H_cell",
        clifford_error < TOL,
        f"max Clifford error={clifford_error:.2e} on Lambda^* W (dim 16)",
    )

    compressed_norm = max(np.linalg.norm(p_one @ g @ p_one) for g in gamma_cell)
    leakage_norm = max(np.linalg.norm((ident16 - p_one) @ g @ p_one) for g in gamma_cell)
    invariant_error = max(np.linalg.norm(g @ p_one - p_one @ g) for g in gamma_cell)
    block(
        "5. the canonical full-cell Clifford generators do not preserve P_A",
        compressed_norm < TOL and leakage_norm > 1.0 and invariant_error > 1.0,
        (
            f"max ||P_A gamma P_A||={compressed_norm:.2e}; "
            f"leakage={leakage_norm:.6g}; commutator={invariant_error:.6g}"
        ),
    )

    gamma_commutant, gamma_gap, gamma_zero = commutant_dimension(gamma_cell)
    gamma_algebra_dim = len(algebra_span(gamma_cell))
    block(
        "6. numerical companion: full-cell Cl_4 multiplicity is four",
        gamma_algebra_dim == 16 and gamma_commutant == 16 and gamma_gap > 1.0,
        (
            f"generated algebra dim={gamma_algebra_dim}; commutant dim="
            f"{gamma_commutant}; singular gap={gamma_gap:.3g}/{gamma_zero:.3g}"
        ),
    )

    odd_one_link = creators + [creator.conj().T for creator in creators]
    odd_compressions = [p_one @ operator @ p_one for operator in odd_one_link]
    odd_compression_rank = np.linalg.matrix_rank(
        np.column_stack([operator.reshape(-1) for operator in odd_compressions]),
        tol=TOL,
    )
    block(
        "7. no fundamental one-link odd operator descends within P_A",
        odd_compression_rank == 0,
        f"span rank of P_A(a_a + a_a^dagger)P_A building blocks={odd_compression_rank}",
    )

    # Compare the natural exterior rotation action with the Clifford spin
    # action on the full event cell.  Their difference is a commuting right
    # spin-half action.  Hence the jointly generated algebra is M_8(C) with
    # multiplicity two: its irreducible joint blocks have dimension eight,
    # not four.
    substrate_np = [np.array(matrix.tolist(), dtype=complex) for matrix in substrate]
    annihilators = [creator.conj().T for creator in creators]
    exterior_spin = [
        sum(
            (
                one_particle[a, b] * creators[a] @ annihilators[b]
                for a in range(4)
                for b in range(4)
            ),
            np.zeros((16, 16), dtype=complex),
        )
        for one_particle in substrate_np
    ]
    clifford_spin_cell = [
        -0.5j * gamma_cell[2] @ gamma_cell[3],
        -0.5j * gamma_cell[3] @ gamma_cell[1],
        -0.5j * gamma_cell[1] @ gamma_cell[2],
    ]
    right_spin = [
        j - s for j, s in zip(exterior_spin, clifford_spin_cell, strict=True)
    ]
    right_gamma_error = max(
        np.linalg.norm(commutator(r, g)) for r in right_spin for g in gamma_cell
    )
    right_su2_error = max(
        np.linalg.norm(
            commutator(right_spin[i], right_spin[j])
            - 1j
            * sum(
                (
                    float(sp.LeviCivita(i, j, k)) * right_spin[k]
                    for k in range(3)
                ),
                np.zeros((16, 16), dtype=complex),
            )
        )
        for i in range(3)
        for j in range(3)
    )
    right_casimir = sum((r @ r for r in right_spin), np.zeros((16, 16), complex))
    right_casimir_error = np.linalg.norm(right_casimir - 0.75 * ident16)
    right_algebra_dim = len(algebra_span(right_spin))
    joint_generators = gamma_cell + exterior_spin
    joint_algebra_basis = algebra_span(joint_generators)
    joint_algebra_dim = len(joint_algebra_basis)
    joint_commutant, joint_gap, joint_zero = commutant_dimension(
        joint_generators
    )
    joint_center, center_gap, center_zero = center_dimension(
        joint_algebra_basis, joint_generators
    )
    block(
        "8. numerical companion: smallest joint Clifford-plus-spin block is dimension eight",
        (
            right_gamma_error < TOL
            and right_su2_error < TOL
            and right_casimir_error < TOL
            and right_algebra_dim == 4
            and joint_algebra_dim == 64
            and joint_commutant == 4
            and joint_center == 1
            and joint_gap > 1.0
            and center_gap > 1.0
        ),
        (
            f"commuting right-spin error={right_gamma_error:.2e}; "
            f"su2 error={right_su2_error:.2e}; right Casimir error="
            f"{right_casimir_error:.2e}; right algebra dim={right_algebra_dim}; joint algebra "
            f"dim={joint_algebra_dim}=dim M_8(C); joint commutant dim="
            f"{joint_commutant}; center dim={joint_center}; singular gaps="
            f"{joint_gap:.3g}/{joint_zero:.3g}, {center_gap:.3g}/{center_zero:.3g}"
        ),
    )

    # Independent atlas-reuse frame: start from the actual retained native
    # cubic C^8 taste matrices rather than the exterior-cell rotation model.
    # They do supply spin-half Clifford bivectors, but neither an operator for
    # the new time axis nor a unique rank-four copy.
    native_spatial, pauli_words = native_cubic_clifford()
    native_bivectors = [
        -0.5j * native_spatial[1] @ native_spatial[2],
        -0.5j * native_spatial[2] @ native_spatial[0],
        -0.5j * native_spatial[0] @ native_spatial[1],
    ]
    native_casimir = sum(
        (b @ b for b in native_bivectors), np.zeros((8, 8), dtype=complex)
    )
    native_algebra_dim = len(algebra_span(native_spatial))
    native_commutant, native_gap, native_zero = commutant_dimension(native_spatial)
    block(
        "9. numerical companion: retained native Cl_3 has unresolved multiplicity",
        (
            np.linalg.norm(native_casimir - 0.75 * np.eye(8)) < TOL
            and native_algebra_dim == 8
            and native_commutant == 8
            and native_gap > 1.0
        ),
        (
            f"Casimir=3/4 I_8; algebra dim={native_algebra_dim}; commutant "
            f"dim={native_commutant}; singular gap={native_gap:.3g}/{native_zero:.3g}"
        ),
    )

    time_candidates = {
        label: matrix
        for label, matrix in pauli_words.items()
        if all(
            np.linalg.norm(anticommutator(matrix, spatial)) < TOL
            for spatial in native_spatial
        )
    }
    extension_data = []
    for label, time_operator in sorted(time_candidates.items()):
        extended = [time_operator, *native_spatial]
        extension_algebra_dim = len(algebra_span(extended))
        extension_commutant, _, _ = commutant_dimension(extended)
        extension_data.append((label, extension_algebra_dim, extension_commutant))
    block(
        "10. numerical companion: time-axis label fixes neither operator nor copy",
        (
            len(time_candidates) == 8
            and all(
                algebra_dim == 16 and commutant_dim == 4
                for _, algebra_dim, commutant_dim in extension_data
            )
        ),
        (
            f"Hermitian Pauli-string time candidates={sorted(time_candidates)}; "
            "each extension generates M_4(C) with commutant M_2(C) on C^8"
        ),
    )

    print()
    print(f"Summary: PASS={PASS_BLOCKS}  FAIL={FAIL_BLOCKS}")
    if FAIL_BLOCKS:
        return 1
    print()
    print("Exact verdict: OBSTRUCTION ON THE GRANTED EVENT-CELL SURFACE.")
    print("Even after P_A is granted, its supplied exterior module 1+3 is not")
    print("the 2+2 spatial module induced by an irreducible Cl_4(C) carrier;")
    print("the intertwiner space is zero.  The canonical Cl_4 action on the")
    print("full exterior cell does exist, but it does not preserve P_A.")
    print("Numerical companions: the smallest joint Clifford-plus-substrate-")
    print("spin block has dimension eight; the retained native C^8 taste route")
    print("leaves eight displayed Pauli-string time operators and a two-copy")
    print("Cl_4 multiplicity in the tested finite-matrix realization.")
    print("Thus the existing C^4 gamma assignment is consistent but is not a")
    print("descent of the stated event-cell action.  A positive repair requires")
    print("a changed representation premise, not only a P_A selector.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
