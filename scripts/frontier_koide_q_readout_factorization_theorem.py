#!/usr/bin/env python3
"""Exact rank/kernel quotient for the defined Koide-Q readout map.

The theorem proved here is finite-dimensional:

    L(u, v, w, z) = diag(u, v, w),
    rank(L) = 3,
    ker(L) = span(e_z),
    im(L) = Diag_3(R),
    R^4 / span(e_z) ~= Diag_3(R).

The 3 x 4 matrix is derived from the displayed 16 x 16 basis construction,
including both time/chirality copies.  A separate independent mode derives it
from basis-state transitions without multiplying the projector matrices.  A
hostile mode mutates the construction and requires recomputed theorem premises
to reject plausible axis, projector, time-copy, ordering, image, kernel,
fiber, rank, and C3-orientation errors.

For selectors, this runner checks only the definitional corollary for the
separately declared class S_L = {Phi composed with L}.  It does not claim that
locality, bosonic parity, species resolution, or C3 covariance classifies all
selectors into S_L, and it makes no physical charged-lepton identification.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Iterable

import sympy as sp


Spatial = tuple[int, int, int]
State = tuple[int, int, int, int]

FULL_STATES: tuple[State, ...] = tuple(
    (a, b, c, t)
    for a in range(2)
    for b in range(2)
    for c in range(2)
    for t in range(2)
)
INDEX = {state: i for i, state in enumerate(FULL_STATES)}

T1: tuple[Spatial, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SLOTS: tuple[Spatial, ...] = (
    (0, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
)
TIMES = (0, 1)

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])

EXPECTED_L = sp.Matrix.hstack(sp.eye(3), sp.zeros(3, 1))
E_Z = sp.Matrix([0, 0, 0, 1])
SECTION = sp.Matrix.vstack(sp.eye(3), sp.zeros(1, 3))
P_SPECIES = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
P_SLOTS = sp.diag(P_SPECIES, sp.ones(1, 1))

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, condition: object, detail: str = "") -> None:
    ok = bool(condition)
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def basis_column(state: State) -> sp.Matrix:
    out = sp.zeros(16, 1)
    out[INDEX[state], 0] = 1
    return out


def flip_spatial(state: State, axis: int) -> State:
    bits = list(state)
    bits[axis] = 1 - bits[axis]
    return tuple(bits)  # type: ignore[return-value]


def gamma_matrix(axis: int) -> sp.Matrix:
    out = sp.zeros(16)
    for state in FULL_STATES:
        out[INDEX[flip_spatial(state, axis)], INDEX[state]] = 1
    return out


def spatial_projector(
    spatial_states: Iterable[Spatial], times: tuple[int, ...] = TIMES
) -> sp.Matrix:
    out = sp.zeros(16)
    for spatial in spatial_states:
        for time in times:
            state = spatial + (time,)
            out[INDEX[state], INDEX[state]] = 1
    return out


def restriction_basis(
    spatial_states: tuple[Spatial, ...], time: int
) -> sp.Matrix:
    return sp.Matrix.hstack(
        *(basis_column(spatial + (time,)) for spatial in spatial_states)
    )


def full_restriction_basis(
    spatial_states: tuple[Spatial, ...] = T1,
) -> sp.Matrix:
    return sp.Matrix.hstack(
        *(
            basis_column(spatial + (time,))
            for time in TIMES
            for spatial in spatial_states
        )
    )


@dataclass(frozen=True)
class ConstructionSpec:
    gamma_axis: int = 0
    t1_projector_states: tuple[Spatial, ...] = T1
    slot_states: tuple[Spatial, ...] = SLOTS
    projector_times: tuple[int, ...] = TIMES
    slot_times: tuple[int, ...] = TIMES
    restriction_states: tuple[Spatial, ...] = T1


@dataclass
class Reconstruction:
    gamma: sp.Matrix
    p_t1: sp.Matrix
    p_slots: tuple[sp.Matrix, ...]
    restriction_bases: tuple[sp.Matrix, sp.Matrix]
    images: tuple[sp.Matrix, ...]
    restrictions: tuple[tuple[sp.Matrix, sp.Matrix], ...]
    l_matrix: sp.Matrix


def reconstruct(spec: ConstructionSpec = ConstructionSpec()) -> Reconstruction:
    gamma = gamma_matrix(spec.gamma_axis)
    p_t1 = spatial_projector(spec.t1_projector_states, spec.projector_times)
    p_slots = tuple(
        spatial_projector((slot,), spec.slot_times) for slot in spec.slot_states
    )
    bases = tuple(
        restriction_basis(spec.restriction_states, time) for time in TIMES
    )
    images = tuple(p_t1 * gamma * p_slot * gamma * p_t1 for p_slot in p_slots)
    restrictions = tuple(
        tuple(basis.T * image * basis for basis in bases) for image in images
    )
    columns = tuple(
        sp.Matrix(list(time_restrictions[0].diagonal()))
        for time_restrictions in restrictions
    )
    l_matrix = sp.Matrix.hstack(*columns)
    return Reconstruction(
        gamma=gamma,
        p_t1=p_t1,
        p_slots=p_slots,
        restriction_bases=bases,  # type: ignore[arg-type]
        images=images,
        restrictions=restrictions,  # type: ignore[arg-type]
        l_matrix=l_matrix,
    )


def expected_image_matrices() -> tuple[sp.Matrix, ...]:
    diagonals = (
        sp.diag(1, 0, 0),
        sp.diag(0, 1, 0),
        sp.diag(0, 0, 1),
        sp.zeros(3),
    )
    basis_full = full_restriction_basis()
    return tuple(
        basis_full * sp.diag(diagonal, diagonal) * basis_full.T
        for diagonal in diagonals
    )


def transition_l_matrix(spec: ConstructionSpec = ConstructionSpec()) -> sp.Matrix:
    """Derive L from state transitions, without multiplying 16 x 16 matrices."""
    out = sp.zeros(3, 4)
    for species_index, spatial in enumerate(spec.restriction_states):
        intermediate = flip_spatial(spatial + (0,), spec.gamma_axis)[:3]
        if intermediate in spec.slot_states:
            out[species_index, spec.slot_states.index(intermediate)] = 1
    return out


def algebra_checks(
    reconstruction: Reconstruction,
    input_cycle: sp.Matrix = P_SLOTS,
    output_cycle: sp.Matrix = P_SPECIES,
) -> dict[str, bool]:
    """Recompute canonical theorem premises for normal and hostile modes."""
    l_matrix = reconstruction.l_matrix
    expected_bases = tuple(restriction_basis(T1, time) for time in TIMES)
    expected_projectors = tuple(
        spatial_projector((slot,), TIMES) for slot in SLOTS
    )
    expected_images = expected_image_matrices()
    nullspace = l_matrix.nullspace()

    x_symbols = sp.symbols("x0:4", real=True)
    y_symbols = sp.symbols("y0:4", real=True)
    difference = sp.Matrix(x_symbols) - sp.Matrix(y_symbols)
    expected_difference_image = sp.Matrix(
        [x_symbols[i] - y_symbols[i] for i in range(3)]
    )

    checks = {
        "gamma_axis": reconstruction.gamma == gamma_matrix(0),
        "projector_slots": reconstruction.p_t1
        == spatial_projector(T1, TIMES)
        and all(
            actual == expected
            for actual, expected in zip(reconstruction.p_slots, expected_projectors)
        ),
        "restriction_map": reconstruction.restriction_bases == expected_bases,
        "time_copies": all(
            restricted[0] == restricted[1]
            for restricted in reconstruction.restrictions
        ),
        "slot_images": reconstruction.images == expected_images,
        "unreachable_zero": reconstruction.images[3] == sp.zeros(16),
        "l_exact": l_matrix == EXPECTED_L,
        "rank_image": l_matrix.rank() == 3 and l_matrix.T.nullspace() == [],
        "kernel": nullspace == [E_Z],
        "fiber": l_matrix * difference == expected_difference_image
        and nullspace == [E_Z],
        "quotient": l_matrix * SECTION == sp.eye(3)
        and sp.eye(4) - SECTION * l_matrix == E_Z * E_Z.T
        and l_matrix * E_Z == sp.zeros(3, 1),
        "c3": output_cycle * l_matrix == l_matrix * input_cycle,
    }
    return {name: bool(value) for name, value in checks.items()}


def run_normal() -> None:
    reconstruction = reconstruct()
    l_matrix = reconstruction.l_matrix
    expected_images = expected_image_matrices()
    basis_full = full_restriction_basis()

    section("A. Exact 16 x 16 basis/projector reconstruction")

    gamma_from_tensor = sp.kronecker_product(SX, I2, I2, I2)
    expected_gamma_actions = all(
        reconstruction.gamma * basis_column(state)
        == basis_column(flip_spatial(state, 0))
        for state in FULL_STATES
    )
    record(
        "A.1 Gamma_1 = X tensor I tensor I tensor I flips only the first spatial bit",
        reconstruction.gamma == gamma_from_tensor
        and reconstruction.gamma**2 == sp.eye(16)
        and expected_gamma_actions,
    )

    expected_p_t1 = spatial_projector(T1, TIMES)
    record(
        "A.2 every spatial projector contains both time copies and P_T1 has rank 6",
        reconstruction.p_t1 == expected_p_t1
        and reconstruction.p_t1.rank() == 6
        and all(projector.rank() == 2 for projector in reconstruction.p_slots),
        "t=0 and t=1 are included for each spatial basis state.",
    )
    record(
        "A.3 the six-column T1 embedding is an exact restriction map onto im(P_T1)",
        basis_full.T * basis_full == sp.eye(6)
        and basis_full * basis_full.T == reconstruction.p_t1,
    )

    transition_map = transition_l_matrix()
    record(
        "A.4 tuple transitions independently give 100->000, 010->110, 001->101",
        transition_map == EXPECTED_L,
        f"transition-derived L = {transition_map}",
    )

    slot_labels = ("000", "110", "101", "011")
    expected_diagonals = (
        sp.diag(1, 0, 0),
        sp.diag(0, 1, 0),
        sp.diag(0, 0, 1),
        sp.zeros(3),
    )
    for index, (label, expected_diagonal) in enumerate(
        zip(slot_labels, expected_diagonals), start=1
    ):
        restrictions = reconstruction.restrictions[index - 1]
        record(
            f"A.{index + 4} slot {label} has the exact displayed image on both time copies",
            reconstruction.images[index - 1] == expected_images[index - 1]
            and restrictions[0] == expected_diagonal
            and restrictions[1] == expected_diagonal,
            f"t=0: {restrictions[0]}; t=1: {restrictions[1]}",
        )

    section("B. Exact rank, kernel, image, fibers, and quotient")

    record(
        "B.1 the operator-derived coefficient matrix is exactly L = [I3 0]",
        l_matrix == EXPECTED_L and l_matrix == transition_map,
        f"L = {l_matrix}",
    )
    record(
        "B.2 rank(L)=3 and the column space is all of Diag_3(R)",
        l_matrix.rank() == 3
        and l_matrix.columnspace() == [sp.eye(3).col(i) for i in range(3)]
        and l_matrix * SECTION == sp.eye(3),
        f"rank(L) = {l_matrix.rank()}, right inverse J = {SECTION}",
    )
    record(
        "B.3 ker(L) is exactly span(e_z)",
        l_matrix.nullspace() == [E_Z] and l_matrix * E_Z == sp.zeros(3, 1),
        f"nullspace basis = {l_matrix.nullspace()}",
    )

    u, v, w, z = sp.symbols("u v w z", real=True)
    d1, d2, d3 = sp.symbols("d1 d2 d3", real=True)
    fiber = sp.linsolve(
        (l_matrix, sp.Matrix([d1, d2, d3])), (u, v, w, z)
    )
    record(
        "B.4 every diagonal has the exact affine fiber {(d1,d2,d3,z)}",
        fiber == sp.FiniteSet((d1, d2, d3, z)),
        f"fiber = {fiber}",
    )

    x_symbols = sp.symbols("x0:4", real=True)
    y_symbols = sp.symbols("y0:4", real=True)
    difference = sp.Matrix(x_symbols) - sp.Matrix(y_symbols)
    record(
        "B.5 L(x)=L(y) iff x-y is an e_z shift",
        l_matrix * difference
        == sp.Matrix([x_symbols[i] - y_symbols[i] for i in range(3)])
        and l_matrix.nullspace() == [E_Z],
        f"L(x-y) = {l_matrix * difference}",
    )
    record(
        "B.6 explicit section/defect identities construct R4/span(e_z) ~= Diag_3(R)",
        l_matrix * SECTION == sp.eye(3)
        and sp.eye(4) - SECTION * l_matrix == E_Z * E_Z.T
        and l_matrix * E_Z == sp.zeros(3, 1),
        f"LJ = {l_matrix * SECTION}; I4-JL = {sp.eye(4) - SECTION * l_matrix}",
    )

    section("C. C3 intertwining and invariant quadratics on the image")

    e1, e2, e3 = (sp.eye(3).col(i) for i in range(3))
    eu, ev, ew, ez = (sp.eye(4).col(i) for i in range(4))
    record(
        "C.1 the declared forward cycles have order 3 and the stated orientation",
        P_SPECIES**3 == sp.eye(3)
        and P_SLOTS**3 == sp.eye(4)
        and P_SPECIES * e1 == e2
        and P_SPECIES * e2 == e3
        and P_SPECIES * e3 == e1
        and P_SLOTS * eu == ev
        and P_SLOTS * ev == ew
        and P_SLOTS * ew == eu
        and P_SLOTS * ez == ez,
    )
    record(
        "C.2 L intertwines the declared forward coefficient and diagonal cycles",
        P_SPECIES * l_matrix == l_matrix * P_SLOTS,
        f"rho_3 L = {P_SPECIES * l_matrix}",
    )

    q11, q12, q13, q22, q23, q33 = sp.symbols(
        "q11 q12 q13 q22 q23 q33", real=True
    )
    unknowns = (q11, q12, q13, q22, q23, q33)
    q_matrix = sp.Matrix(
        [[q11, q12, q13], [q12, q22, q23], [q13, q23, q33]]
    )
    invariant_difference = P_SPECIES.T * q_matrix * P_SPECIES - q_matrix
    equations = [
        invariant_difference[i, j] for i in range(3) for j in range(i, 3)
    ]
    constraint_matrix, _ = sp.linear_eq_to_matrix(equations, unknowns)
    invariant_basis = constraint_matrix.nullspace()
    identity_coefficients = sp.Matrix([1, 0, 0, 1, 0, 1])
    off_diagonal_coefficients = sp.Matrix([0, 1, 1, 0, 1, 0])
    expected_invariant_span = sp.Matrix.hstack(
        identity_coefficients, off_diagonal_coefficients
    )
    actual_invariant_span = sp.Matrix.hstack(*invariant_basis)
    record(
        "C.3 the C3-invariant real quadratic space on Diag_3(R) is exactly two-dimensional",
        constraint_matrix.rank() == 4
        and len(invariant_basis) == 2
        and constraint_matrix * identity_coefficients == sp.zeros(6, 1)
        and constraint_matrix * off_diagonal_coefficients == sp.zeros(6, 1)
        and actual_invariant_span.row_join(expected_invariant_span).rank() == 2,
        "Q has one common diagonal coefficient and one common off-diagonal coefficient.",
    )

    section("D. Definition-driven selector corollary, not classification")

    eta = sp.symbols("eta", real=True)
    weight = sp.Matrix([u, v, w, z])
    shifted_weight = weight + eta * E_Z
    phi = sp.Function("Phi")
    selector = phi(*list(l_matrix * weight))
    shifted_selector = phi(*list(l_matrix * shifted_weight))
    record(
        "D.1 for the declared class S_L={Phi composed with L}, kernel invariance is definitional",
        l_matrix * shifted_weight == l_matrix * weight
        and shifted_selector == selector,
        f"Phi(L(W + eta e_z)) = {shifted_selector}",
    )

    generic_weight = sp.Matrix(sp.symbols("r0:4", real=True))
    z_scalar = (E_Z.T * generic_weight)[0]
    cycled_z_scalar = (E_Z.T * P_SLOTS * generic_weight)[0]
    shifted_z_difference = (
        E_Z.T * (generic_weight + eta * E_Z) - E_Z.T * generic_weight
    )[0]
    record(
        "D.2 the z scalar is C3-invariant but kernel-sensitive, so covariance alone does not force factorization",
        cycled_z_scalar == z_scalar
        and shifted_z_difference == eta
        and l_matrix * (generic_weight + eta * E_Z)
        == l_matrix * generic_weight,
        f"S_z(rho_4 W)-S_z(W)=0; S_z(W+eta e_z)-S_z(W)={shifted_z_difference}",
    )


def run_independent() -> None:
    section("I. Independent transition reconstruction")

    expected_transitions = (
        ((1, 0, 0), (0, 0, 0)),
        ((0, 1, 0), (1, 1, 0)),
        ((0, 0, 1), (1, 0, 1)),
    )
    computed_transitions = tuple(
        (spatial, flip_spatial(spatial + (0,), 0)[:3]) for spatial in T1
    )
    record(
        "I.1 state enumeration gives the three canonical intermediate transitions",
        computed_transitions == expected_transitions,
        f"transitions = {computed_transitions}",
    )

    time_preserved = all(
        flip_spatial(spatial + (time,), 0)[3] == time
        for spatial in T1
        for time in TIMES
    )
    record(
        "I.2 the independent transition rule preserves both time/chirality copies",
        time_preserved,
    )

    transition_l = transition_l_matrix()
    matrix_l = reconstruct().l_matrix
    record(
        "I.3 transition enumeration derives L=[I3 0] and matches the 16 x 16 route",
        transition_l == EXPECTED_L and transition_l == matrix_l,
        f"transition L = {transition_l}",
    )
    record(
        "I.4 independent L has rank 3, full image, and kernel span(e_z)",
        transition_l.rank() == 3
        and transition_l * SECTION == sp.eye(3)
        and transition_l.nullspace() == [E_Z],
    )
    record(
        "I.5 independent section identities establish the quotient isomorphism",
        transition_l * SECTION == sp.eye(3)
        and sp.eye(4) - SECTION * transition_l == E_Z * E_Z.T
        and transition_l * E_Z == sp.zeros(3, 1),
    )
    record(
        "I.6 independent L has the declared forward C3 intertwining orientation",
        P_SPECIES * transition_l == transition_l * P_SLOTS
        and P_SPECIES * transition_l != transition_l * P_SLOTS.T,
    )


def mutation_record(
    label: str,
    spec: ConstructionSpec,
    expected_failures: tuple[str, ...],
    *,
    input_cycle: sp.Matrix = P_SLOTS,
    output_cycle: sp.Matrix = P_SPECIES,
) -> None:
    reconstruction = reconstruct(spec)
    checks = algebra_checks(reconstruction, input_cycle, output_cycle)
    actual_failures = tuple(name for name, ok in checks.items() if not ok)
    record(
        label,
        all(not checks[name] for name in expected_failures),
        "recomputed failures = " + ", ".join(actual_failures),
    )


def run_hostile() -> None:
    section("H. Hostile mutations of recomputed premises")

    baseline_checks = algebra_checks(reconstruct())
    record(
        "H.0 the hostile validator accepts the independently reconstructed baseline",
        all(baseline_checks.values()),
        "validated premises = " + ", ".join(baseline_checks),
    )

    mutation_record(
        "H.1 a wrong Gamma axis is rejected",
        ConstructionSpec(gamma_axis=1),
        ("gamma_axis", "slot_images", "l_exact", "kernel", "fiber"),
    )
    mutation_record(
        "H.2 a wrong intermediate projector slot is rejected",
        ConstructionSpec(
            slot_states=((0, 0, 0), (1, 1, 1), (1, 0, 1), (0, 1, 1))
        ),
        ("projector_slots", "slot_images", "l_exact", "rank_image"),
    )
    mutation_record(
        "H.3 a missing time copy is rejected",
        ConstructionSpec(slot_times=(0,)),
        ("projector_slots", "time_copies", "slot_images"),
    )
    mutation_record(
        "H.4 a wrong coefficient-slot order is rejected",
        ConstructionSpec(
            slot_states=((0, 0, 0), (1, 0, 1), (1, 1, 0), (0, 1, 1))
        ),
        ("projector_slots", "slot_images", "l_exact", "c3"),
    )
    mutation_record(
        "H.5 a wrong species restriction order is rejected",
        ConstructionSpec(
            restriction_states=((1, 0, 0), (0, 0, 1), (0, 1, 0))
        ),
        ("restriction_map", "l_exact", "c3"),
    )
    mutation_record(
        "H.6 a nonzero unreachable image and its changed kernel/fibers are rejected",
        ConstructionSpec(
            slot_states=((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 0, 0))
        ),
        (
            "projector_slots",
            "slot_images",
            "unreachable_zero",
            "l_exact",
            "kernel",
            "fiber",
            "quotient",
        ),
    )
    mutation_record(
        "H.7 a duplicated reachable image that lowers rank is rejected",
        ConstructionSpec(
            slot_states=((0, 0, 0), (1, 1, 0), (1, 1, 0), (0, 1, 1))
        ),
        ("projector_slots", "slot_images", "l_exact", "rank_image", "kernel"),
    )

    canonical_l = reconstruct().l_matrix
    wrong_kernel_direction = sp.Matrix([0, 0, 1, 0])
    record(
        "H.8 the plausible wrong kernel span(e_w) is rejected by exact multiplication",
        canonical_l * wrong_kernel_direction != sp.zeros(3, 1)
        and wrong_kernel_direction not in canonical_l.nullspace(),
        f"L e_w = {canonical_l * wrong_kernel_direction}",
    )

    eta = sp.symbols("eta", nonzero=True, real=True)
    generic_weight = sp.Matrix(sp.symbols("h0:4", real=True))
    wrong_fiber_shift = eta * wrong_kernel_direction
    record(
        "H.9 a claimed e_w fiber shift is rejected by recomputed outputs",
        canonical_l * (generic_weight + wrong_fiber_shift)
        - canonical_l * generic_weight
        == sp.Matrix([0, 0, eta]),
        f"L(W+eta e_w)-L(W) = {canonical_l * wrong_fiber_shift}",
    )

    mutation_record(
        "H.10 an inverse input-cycle orientation is rejected",
        ConstructionSpec(),
        ("c3",),
        input_cycle=P_SLOTS.T,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "all"),
        default="normal",
        help="verification mode (default: normal)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    PASSES.clear()

    if args.mode in ("normal", "all"):
        run_normal()
    if args.mode in ("independent", "all"):
        run_independent()
    if args.mode in ("hostile", "all"):
        run_hostile()

    section("Summary")
    n_pass = sum(ok for _, ok, _ in PASSES)
    n_total = len(PASSES)
    print(f"MODE: {args.mode}")
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT (bounded): the defined 16 x 16 construction gives")
        print("L=[I3 0], rank 3, image Diag_3(R), kernel span(e_z), exact")
        print("fibers, and R^4/span(e_z) ~= Diag_3(R).  The declared forward")
        print("C3 actions intertwine.  Selector invariance is asserted only as")
        print("the definitional corollary for S_L={Phi composed with L}.")
        return 0

    print("VERDICT: exact quotient verification has FAILs.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
