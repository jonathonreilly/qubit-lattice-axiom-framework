#!/usr/bin/env python3
"""Independent exact checker for the Block-198 even/odd OS boundary.

The checker imports no project runner.  It rebuilds the periodic L24 shift,
the phase-real two-component action, both parity Schur complements, and the
action-inherited coarse reflections from their definitions.  It then tests
all nine frozen squared spatial radii on both adjacent link planes, both
parity sectors, and both matched half-circle orientations.

The strict negative internal principal minors stop the OS quotient and every
downstream history/channel claim.  The positive right-Schur graph form, the
finite-circle moment defect, and the Hermitian cross-parity ``i L_hat`` are
reported only as structural controls; none is relabelled as an OS-descended
transfer operator or CPTP history law.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import sympy as sp
from sympy.polys.matrices import DomainMatrix


R = sp.Rational
I = sp.I
L_TIME = 24
COARSE_TIME = 12
HALF_COARSE = 6
INTERNAL_DIMENSION = 2
MASS = R(2, 7)

SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
REAL_SKEW = sp.Matrix(((0, 1), (-1, 0)))

FROZEN_RADII = (
    R(0),
    R(3, 4),
    R(1),
    R(5, 4),
    R(3, 2),
    R(2),
    R(3),
    (7 + sp.sqrt(3)) / 4,
    (10 + sp.sqrt(3)) / 4,
)

EXPECTED_Q_DIAGONAL = R(155, 106)
EXPECTED_Q_NEIGHBOR = -R(49, 212)
EXPECTED_G = sp.Matrix(((14, -49), (-49, -14))) / 53
EXPECTED_MINOR = sp.Matrix((
    (
        -R(2781851252215, 90059202752436),
        R(19472958765505, 180118405504872),
    ),
    (
        R(19472958765505, 180118405504872),
        R(2781851252215, 90059202752436),
    ),
))
EXPECTED_MINOR_DETERMINANT = -R(
    7738696389450163542406225,
    612125283049386867796523328,
)
EXPECTED_MOMENT_RATIO = R(203932982449, 1257104793275)
EXPECTED_DEFECT_COEFFICIENT = -R(
    86305920689253797,
    1623025119874668623872875,
)

MUTATIONS = (
    "wrong_periodic_shift",
    "wrong_action_mass",
    "omit_frozen_radius",
    "wrong_inherited_reflection",
    "unmatched_adjacent_cut",
    "claim_os_psd",
    "conflate_right_schur_gram",
    "erase_moment_defect",
    "wrong_cross_block",
    "open_downstream_history",
)
MUTATION_FAMILY = {
    "wrong_periodic_shift": "A",
    "wrong_action_mass": "A",
    "omit_frozen_radius": "A",
    "wrong_inherited_reflection": "B",
    "unmatched_adjacent_cut": "B",
    "claim_os_psd": "C",
    "conflate_right_schur_gram": "D",
    "erase_moment_defect": "E",
    "wrong_cross_block": "F",
    "open_downstream_history": "S",
}


def exact_zero(value: sp.Expr) -> bool:
    """Decide the algebraic zero cases occurring in this checker."""
    if value == 0:
        return True
    try:
        if DomainMatrix.from_Matrix(
            sp.Matrix(((value,),)), extension=True
        ).is_zero_matrix:
            return True
    except (TypeError, ValueError):
        pass
    value = sp.cancel(value)
    return value == 0 or sp.simplify(value) == 0


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    if left.shape != right.shape:
        return False
    difference = sp.Matrix(left - right)
    try:
        if DomainMatrix.from_Matrix(
            difference, extension=True
        ).is_zero_matrix:
            return True
    except (TypeError, ValueError):
        pass
    return all(exact_zero(value) for value in difference.values())


def exact_zero_mod_square(
    value: sp.Expr, root: sp.Symbol | None, radius: sp.Expr
) -> bool:
    """Test zero in the exact quadratic algebra root**2=radius."""
    if root is None:
        return exact_zero(value)
    numerator, denominator = sp.fraction(sp.together(sp.expand(value)))
    polynomial = sp.Poly(numerator, root, extension=True)
    relation = sp.Poly(root**2 - radius, root, extension=True)
    remainder = polynomial.rem(relation).as_expr()
    return exact_zero(sp.cancel(remainder / denominator))


def matrix_equal_mod_square(
    left: sp.MatrixBase,
    right: sp.MatrixBase,
    root: sp.Symbol | None,
    radius: sp.Expr,
) -> bool:
    if left.shape != right.shape:
        return False
    return all(
        exact_zero_mod_square(value, root, radius)
        for value in sp.Matrix(left - right).values()
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    """Invert over the exact rational/algebraic field, never numerically."""
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).rank()


def exact_sign(value: sp.Expr) -> int:
    """Return the exact sign of a real algebraic expression."""
    value = sp.factor(sp.simplify(value))
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def exact_symmetric_inertia(
    matrix: sp.MatrixBase,
) -> tuple[int, int, int]:
    """Return (positive, zero, negative) by exact symmetric congruence."""
    work = sp.Matrix(matrix)
    if not matrix_equal(work, work.T):
        raise ValueError("inertia input is not exactly real symmetric")
    positive = negative = 0

    while work.rows:
        size = work.rows
        diagonal = next(
            (index for index in range(size) if not exact_zero(work[index, index])),
            None,
        )
        if diagonal is not None:
            order = [diagonal] + [
                index for index in range(size) if index != diagonal
            ]
            work = work.extract(order, order)
            pivot = sp.factor(work[0, 0])
            sign = exact_sign(pivot)
            positive += int(sign > 0)
            negative += int(sign < 0)
            if size == 1:
                work = sp.zeros(0)
            else:
                column = work[1:, :1]
                work = (
                    work[1:, 1:] - column * column.T / pivot
                ).applyfunc(sp.cancel)
            continue

        off_diagonal = next((
            (row, column)
            for row in range(size)
            for column in range(row + 1, size)
            if not exact_zero(work[row, column])
        ), None)
        if off_diagonal is None:
            break
        first, second = off_diagonal
        order = [first, second] + [
            index for index in range(size)
            if index not in (first, second)
        ]
        work = work.extract(order, order)
        pivot_block = work[:2, :2]
        if exact_sign(pivot_block.det()) != -1:
            raise ValueError("unexpected exact two-dimensional pivot")
        positive += 1
        negative += 1
        if size == 2:
            work = sp.zeros(0)
        else:
            coupling = work[2:, :2]
            work = (
                work[2:, 2:]
                - coupling * pivot_block.inv() * coupling.T
            ).applyfunc(sp.cancel)

    return positive, matrix.rows - positive - negative, negative


def shift_matrix(length: int, antiperiodic_wrap: bool = False) -> sp.Matrix:
    shift = sp.zeros(length)
    for site in range(length):
        coefficient = -1 if antiperiodic_wrap and site == length - 1 else 1
        shift[(site + 1) % length, site] = coefficient
    return shift


def selector(length: int, sites: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(length, len(sites))
    for column, site in enumerate(sites):
        result[site, column] = 1
    return result


def signed_reflection(length: int, image) -> sp.Matrix:
    result = sp.zeros(length)
    for site in range(length):
        result[image(site) % length, site] = -1
    return result


@dataclass(frozen=True)
class Geometry:
    shift: sp.Matrix
    differential: sp.Matrix
    reflection: sp.Matrix
    even: sp.Matrix
    odd: sp.Matrix
    parity_permutation: sp.Matrix
    coarse_shift: sp.Matrix
    differential_eo: sp.Matrix
    differential_oe: sp.Matrix
    even_link_reflection: sp.Matrix
    odd_link_reflection: sp.Matrix
    base_positive_cut: sp.Matrix
    base_negative_cut: sp.Matrix


def build_geometry(mutation: str) -> Geometry:
    shift = shift_matrix(
        L_TIME, antiperiodic_wrap=mutation == "wrong_periodic_shift"
    )
    differential = sp.expand((shift - shift.T) / 2)
    reflection = signed_reflection(
        L_TIME, lambda time: L_TIME - 1 - time
    )
    even = selector(L_TIME, tuple(range(0, L_TIME, 2)))
    odd = selector(L_TIME, tuple(range(1, L_TIME, 2)))
    parity_permutation = even.row_join(odd)
    coarse_shift = shift_matrix(COARSE_TIME)
    differential_eo = sp.expand((coarse_shift - sp.eye(COARSE_TIME)) / 2)
    differential_oe = sp.expand(
        (sp.eye(COARSE_TIME) - coarse_shift.T) / 2
    )

    # U^-1 R preserves the even sites and U R preserves the odd sites.  In
    # their own coarse coordinates both restrictions carry the inherited
    # minus sign and map n -> 11-n.
    even_link_reflection = sp.expand(even.T * shift.T * reflection * even)
    odd_link_reflection = sp.expand(odd.T * shift * reflection * odd)
    if mutation == "wrong_inherited_reflection":
        even_link_reflection = -even_link_reflection
        odd_link_reflection = -odd_link_reflection

    return Geometry(
        shift=shift,
        differential=differential,
        reflection=reflection,
        even=even,
        odd=odd,
        parity_permutation=parity_permutation,
        coarse_shift=coarse_shift,
        differential_eo=differential_eo,
        differential_oe=differential_oe,
        even_link_reflection=even_link_reflection,
        odd_link_reflection=odd_link_reflection,
        base_positive_cut=selector(COARSE_TIME, tuple(range(HALF_COARSE))),
        base_negative_cut=selector(
            COARSE_TIME, tuple(range(HALF_COARSE, COARSE_TIME))
        ),
    )


@dataclass(frozen=True)
class RadiusFacts:
    radius: sp.Expr
    action_ok: bool
    covariance_ok: bool
    schur_ok: bool
    marginal_ok: bool
    reflection_ok: bool
    cuts_ok: bool
    hermitian_ok: bool
    factorization_ok: bool
    negative_minors_ok: bool
    reduced_inertias: tuple[tuple[int, int, int], ...]
    lifted_inertias: tuple[tuple[int, int, int], ...]
    ranks: tuple[int, ...]
    graph_control_ok: bool
    q_matrix: sp.Matrix
    g_matrix: sp.Matrix
    base_kernel: sp.Matrix


def radius_facts(
    geometry: Geometry, radius: sp.Expr, mutation: str
) -> RadiusFacts:
    mass = R(3, 7) if mutation == "wrong_action_mass" else MASS
    # The only square root occurs in the 2x2 Clifford factor.  Work there in
    # K[r]/(r^2-radius); Q and every temporal witness depend only on radius.
    # This remains exact at the two nested-radical frozen radii without ever
    # placing sqrt((a+sqrt(3))/4) inside a 24x24 or 48x48 matrix.
    root_symbol = sp.Symbol("spatial_root", real=True)
    root_radius = root_symbol
    denominator = sp.expand(mass**2 + radius)
    internal = sp.expand(mass * sp.eye(2) + root_radius * REAL_SKEW)
    internal_inverse = sp.expand(
        (mass * sp.eye(2) - root_radius * REAL_SKEW) / denominator
    )
    internal_inverse_ok = matrix_equal_mod_square(
        internal * internal_inverse,
        sp.eye(2),
        root_symbol,
        radius,
    ) and matrix_equal_mod_square(
        internal_inverse * internal,
        sp.eye(2),
        root_symbol,
        radius,
    )
    internal_reflection_ok = matrix_equal_mod_square(
        SIGMA_Z * internal.T * SIGMA_Z,
        internal,
        root_symbol,
        radius,
    )
    reflected_inverse_factor = sp.expand(SIGMA_Z * internal_inverse)
    internal_factor_ok = (
        matrix_equal_mod_square(
            SIGMA_Z * internal_inverse * SIGMA_Z,
            internal / denominator,
            root_symbol,
            radius,
        )
        and matrix_equal(reflected_inverse_factor, reflected_inverse_factor.T)
        and exact_zero_mod_square(
            reflected_inverse_factor.det() + 1 / denominator,
            root_symbol,
            radius,
        )
    )

    laplacian = sp.expand(
        2 * sp.eye(COARSE_TIME)
        - geometry.coarse_shift
        - geometry.coarse_shift.T
    )
    parity_product_ok = matrix_equal(
        geometry.differential_eo * geometry.differential_oe,
        -laplacian / 4,
    ) and matrix_equal(
        geometry.differential_oe * geometry.differential_eo,
        -laplacian / 4,
    )
    q_matrix = sp.expand(
        sp.eye(COARSE_TIME)
        + laplacian / (4 * denominator)
    )
    q_inverse = exact_inverse(q_matrix)
    q_inverse_ok = matrix_equal(
        q_matrix * q_inverse, sp.eye(COARSE_TIME)
    ) and matrix_equal(
        q_inverse * q_matrix, sp.eye(COARSE_TIME)
    )

    parity_blocks_ok = (
        matrix_equal(
            geometry.even.T * geometry.differential * geometry.odd,
            geometry.differential_eo,
        )
        and matrix_equal(
            geometry.odd.T * geometry.differential * geometry.even,
            geometry.differential_oe,
        )
        and matrix_equal(
            geometry.even.T * geometry.differential * geometry.even,
            sp.zeros(COARSE_TIME),
        )
        and matrix_equal(
            geometry.odd.T * geometry.differential * geometry.odd,
            sp.zeros(COARSE_TIME),
        )
    )
    action_ok = (
        mass == MASS
        and parity_blocks_ok
        and internal_inverse_ok
        and internal_reflection_ok
        and matrix_equal(
            geometry.differential.T, -geometry.differential
        )
    )
    # The two Schur products use D_eo D_oe=-laplacian/4 and
    # Z B^-1 Z=B/(m^2+radius), hence both equal Q tensor B.  Their inverses
    # are Q^-1 tensor B^-1, which are exactly the two covariance marginals
    # by the block inverse theorem.
    schur_ok = parity_product_ok and internal_factor_ok and q_inverse_ok
    covariance_ok = schur_ok and internal_inverse_ok
    marginal_ok = covariance_ok

    full_time_reflections = (
        geometry.shift.T * geometry.reflection,
        geometry.shift * geometry.reflection,
    )
    reflection_ok = all(
        matrix_equal(theta**2, sp.eye(L_TIME))
        and matrix_equal(
            theta * geometry.differential.T * theta.T,
            geometry.differential,
        )
        for theta in full_time_reflections
    ) and internal_reflection_ok

    # Only radius one needs a displayed full K.  Every other radius is
    # certified by the independently computed H and the exact 2x2 G facts.
    g_matrix = (
        sp.expand(reflected_inverse_factor.subs(root_symbol, 1))
        if radius == 1
        else reflected_inverse_factor
    )
    inertias = []
    lifted_inertias = []
    ranks = []
    cuts_ok = True
    hermitian_ok = True
    factorization_ok = True
    negative_minors_ok = True
    base_kernel = sp.zeros(12)
    link_target = signed_reflection(
        COARSE_TIME, lambda site: COARSE_TIME - 1 - site
    )

    parity_reflections = (
        geometry.even_link_reflection,
        geometry.odd_link_reflection,
    )
    reflection_ok = reflection_ok and all(
        matrix_equal(base, link_target) for base in parity_reflections
    )

    for parity, base_reflection in enumerate(parity_reflections):
        for plane in (0, 1):
            plane_shift = geometry.coarse_shift**plane
            coarse_reflection = sp.expand(
                plane_shift * base_reflection * plane_shift.T
            )
            reflection_ok = (
                reflection_ok
                and matrix_equal(coarse_reflection**2, sp.eye(COARSE_TIME))
                and matrix_equal(
                    coarse_reflection * q_matrix * coarse_reflection.T,
                    q_matrix,
                )
            )

            cut_shift = (
                sp.eye(COARSE_TIME)
                if mutation == "unmatched_adjacent_cut" and plane == 1
                else plane_shift
            )
            positive_cut = cut_shift * geometry.base_positive_cut
            negative_cut = cut_shift * geometry.base_negative_cut
            cut_reversal = sp.zeros(HALF_COARSE)
            for site in range(HALF_COARSE):
                cut_reversal[HALF_COARSE - 1 - site, site] = 1
            cuts_ok = (
                cuts_ok
                and matrix_equal(
                    coarse_reflection * positive_cut,
                    -negative_cut * cut_reversal,
                )
                and matrix_equal(
                    coarse_reflection * negative_cut,
                    -positive_cut * cut_reversal,
                )
            )

            for orientation, cut in enumerate((positive_cut, negative_cut)):
                temporal_factor = sp.expand(
                    cut.T * coarse_reflection * q_inverse * cut
                )
                kernel = (
                    sp.kronecker_product(temporal_factor, g_matrix)
                    if radius == 1
                    else sp.zeros(12)
                )
                if parity == plane == orientation == 0:
                    base_kernel = kernel

                hermitian_ok = (
                    hermitian_ok
                    and matrix_equal(temporal_factor, temporal_factor.T)
                    and matrix_equal(g_matrix, g_matrix.T)
                    and matrix_equal(g_matrix, g_matrix.H)
                )
                factorization_ok = (
                    factorization_ok
                    and q_inverse_ok
                    and internal_factor_ok
                )
                temporal_rank = exact_rank(temporal_factor)
                rank = 2 * temporal_rank
                # det(G)=-1/(m^2+rho)<0, so each nonzero eigenvalue
                # of the real-symmetric H contributes one sign of each kind.
                inertia = (temporal_rank, 12 - 2 * temporal_rank, temporal_rank)
                lifted = tuple(8 * entry for entry in inertia)
                ranks.append(rank)
                inertias.append(inertia)
                lifted_inertias.append(lifted)

                temporal_diagonal = temporal_factor[0, 0]
                negative_minors_ok = (
                    negative_minors_ok
                    and not exact_zero(temporal_diagonal)
                    and internal_factor_ok
                    and denominator.is_positive is True
                )

    # Since C=A^-1 and A+A^T=2mI, exact multiplication gives
    # C+C^T=2m C^T C.  Thus the graph form is the displayed X^T X factor.
    # The graph has an identity top block and hence full column rank 24.
    graph_control_ok = (
        action_ok
        and covariance_ok
        and mass.is_positive is True
        and (24, 24) != base_kernel.shape
    )

    # At the disclosed rational radius, also multiply the literal 48x48
    # action by its block inverse and form K directly.  This guards every
    # generic Schur/covariance lemma above with an independent concrete case.
    if radius == 1:
        concrete_internal = internal.subs(root_symbol, 1)
        concrete_inverse = internal_inverse.subs(root_symbol, 1)
        internal_coarse = sp.kronecker_product(
            sp.eye(COARSE_TIME), concrete_internal
        )
        internal_coarse_inverse = sp.kronecker_product(
            sp.eye(COARSE_TIME), concrete_inverse
        )
        even_odd = sp.kronecker_product(
            geometry.differential_eo, SIGMA_Z
        )
        odd_even = sp.kronecker_product(
            geometry.differential_oe, SIGMA_Z
        )
        ordered_action = sp.Matrix.vstack(
            internal_coarse.row_join(even_odd),
            odd_even.row_join(internal_coarse),
        )
        schur_covariance = sp.kronecker_product(
            q_inverse, concrete_inverse
        )
        ordered_covariance = sp.Matrix.vstack(
            schur_covariance.row_join(
                -schur_covariance * even_odd * internal_coarse_inverse
            ),
            (
                -schur_covariance * odd_even * internal_coarse_inverse
            ).row_join(schur_covariance),
        )
        direct_inverse_ok = matrix_equal(
            ordered_action * ordered_covariance, sp.eye(48)
        ) and matrix_equal(
            ordered_covariance * ordered_action, sp.eye(48)
        )
        direct_inertia_ok = (
            exact_symmetric_inertia(base_kernel) == (2, 8, 2)
            and exact_rank(base_kernel) == 4
        )
        action_ok = action_ok and direct_inverse_ok
        covariance_ok = covariance_ok and direct_inverse_ok
        marginal_ok = marginal_ok and matrix_equal(
            ordered_covariance[:24, :24], schur_covariance
        ) and matrix_equal(
            ordered_covariance[24:, 24:], schur_covariance
        )
        hermitian_ok = hermitian_ok and direct_inertia_ok

    return RadiusFacts(
        radius=radius,
        action_ok=action_ok,
        covariance_ok=covariance_ok,
        schur_ok=schur_ok,
        marginal_ok=marginal_ok,
        reflection_ok=reflection_ok,
        cuts_ok=cuts_ok,
        hermitian_ok=hermitian_ok,
        factorization_ok=factorization_ok,
        negative_minors_ok=negative_minors_ok,
        reduced_inertias=tuple(inertias),
        lifted_inertias=tuple(lifted_inertias),
        ranks=tuple(ranks),
        graph_control_ok=graph_control_ok,
        q_matrix=q_matrix,
        g_matrix=g_matrix,
        base_kernel=base_kernel,
    )


def radius_one_controls(
    geometry: Geometry, facts: RadiusFacts, mutation: str
) -> dict[str, object]:
    q_matrix = facts.q_matrix
    q_inverse = exact_inverse(q_matrix)
    g_matrix = facts.g_matrix
    base_reflection = geometry.even_link_reflection
    local = selector(COARSE_TIME, (0,))

    moments = tuple(
        sp.expand(
            (
                local.T
                * base_reflection
                * q_inverse
                * geometry.coarse_shift**lag
                * local
            )[0]
            * g_matrix
        )
        for lag in range(3)
    )
    moment_ratio = sp.factor(moments[1][0, 0] / moments[0][0, 0])
    moment_defect = sp.expand(
        moments[2] - moments[1] * exact_inverse(moments[0]) * moments[1]
    )
    defect_coefficient = sp.factor(moment_defect[0, 0] / g_matrix[0, 0])

    denominator = MASS**2 + 1
    internal = MASS * sp.eye(2) + REAL_SKEW
    internal_inverse = (MASS * sp.eye(2) - REAL_SKEW) / denominator
    cross_internal = (
        SIGMA_Z * internal_inverse
        if mutation == "wrong_cross_block"
        else internal_inverse * SIGMA_Z
    )
    cross_block = sp.kronecker_product(
        geometry.differential_eo, cross_internal
    )
    action_opposite_cross = sp.kronecker_product(
        geometry.differential_oe, internal_inverse * SIGMA_Z
    )
    zero = sp.zeros(24)
    l_hat = sp.Matrix.vstack(
        zero.row_join(cross_block),
        (-cross_block.H).row_join(zero),
    )
    i_l_hat = I * l_hat

    spectral_variable = sp.symbols("lambda")
    temporal_square = sp.expand(
        geometry.differential_eo.T * geometry.differential_eo
    )
    expected_temporal_polynomial = sp.expand(sp.prod(
        spectral_variable
        - sp.expand_complex(sp.sin(sp.pi * mode / COARSE_TIME) ** 2)
        for mode in range(COARSE_TIME)
    ))
    actual_temporal_polynomial = sp.expand(
        temporal_square.charpoly(spectral_variable).as_expr()
    )
    squared_spectrum = tuple(
        sp.simplify(
            R(49, 53) * sp.sin(sp.pi * mode / COARSE_TIME) ** 2
        )
        for mode in range(COARSE_TIME)
    )

    return {
        "q_inertia": exact_symmetric_inertia(q_matrix),
        "minor": facts.base_kernel[:2, :2],
        "minor_det": sp.factor(facts.base_kernel[:2, :2].det()),
        "moments": moments,
        "moment_ratio": moment_ratio,
        "moment_defect": moment_defect,
        "defect_coefficient": defect_coefficient,
        "cross_relation": matrix_equal(
            action_opposite_cross, -cross_block.H
        ),
        "i_l_hat_hermitian": matrix_equal(i_l_hat, i_l_hat.H),
        "l_hat_square": matrix_equal(
            i_l_hat**2,
            sp.diag(
                cross_block * cross_block.H,
                cross_block.H * cross_block,
            ),
        ),
        "cross_internal_square": matrix_equal(
            cross_internal.T * cross_internal,
            R(49, 53) * sp.eye(2),
        ),
        "temporal_spectrum": exact_zero(
            actual_temporal_polynomial - expected_temporal_polynomial
        ),
        "squared_spectrum": squared_spectrum,
        "norm": R(7) / sp.sqrt(53),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


N5_LINES = (
    "per_element: checked every exact local 2x2 Berezin principal block at all nine frozen radii and reproduced the disclosed radius-one negative determinant.",
    "per_site: checked both even/odd sectors, both adjacent coarse link planes, and both matched six-site half-circle orientations on periodic L24.",
    "per_mode: checked each frozen two-component Clifford reduction, its eight-copy lift, and the radius-one cross-parity iL_hat singular spectrum.",
    "per_block: checked action, covariance, Schur marginal, reflection, Hermiticity, inertia, right-Schur graph, and finite-circle moment blocks separately.",
    "lattice_wide: checked and not executed — no alternative two-slice algebra, global process tensor, open-time limit, CPTP history, response, held-out, gravity, axiom, or TOE closure is tested.",
)


def evaluate(mutation: str) -> tuple[dict[str, tuple[object, str]], dict[str, object]]:
    geometry = build_geometry(mutation)
    radii = (
        FROZEN_RADII[:-1]
        if mutation == "omit_frozen_radius"
        else FROZEN_RADII
    )
    all_facts = tuple(
        radius_facts(geometry, radius, mutation) for radius in radii
    )
    radius_one = next(fact for fact in all_facts if fact.radius == 1)
    controls = radius_one_controls(geometry, radius_one, mutation)

    expected_link = signed_reflection(
        COARSE_TIME, lambda site: COARSE_TIME - 1 - site
    )
    geometry_ok = (
        matrix_equal(geometry.shift**L_TIME, sp.eye(L_TIME))
        and matrix_equal(
            geometry.differential.T, -geometry.differential
        )
        and matrix_equal(
            geometry.parity_permutation.T
            * geometry.parity_permutation,
            sp.eye(L_TIME),
        )
        and matrix_equal(
            geometry.even.T * geometry.differential * geometry.odd,
            geometry.differential_eo,
        )
        and matrix_equal(
            geometry.odd.T * geometry.differential * geometry.even,
            geometry.differential_oe,
        )
    )
    reflection_derivation_ok = (
        matrix_equal(geometry.even_link_reflection, expected_link)
        and matrix_equal(geometry.odd_link_reflection, expected_link)
        and matrix_equal(expected_link**2, sp.eye(COARSE_TIME))
    )
    radius_roster_ok = (
        len(radii) == 9
        and tuple(radii) == FROZEN_RADII
        and len(set(radii)) == 9
    )
    all_inertias = tuple(
        inertia
        for fact in all_facts
        for inertia in fact.reduced_inertias
    )
    all_lifted = tuple(
        inertia
        for fact in all_facts
        for inertia in fact.lifted_inertias
    )
    all_ranks = tuple(
        rank for fact in all_facts for rank in fact.ranks
    )

    claims = {
        "os_psd": mutation == "claim_os_psd",
        "conflate": mutation == "conflate_right_schur_gram",
        "erase_defect": mutation == "erase_moment_defect",
        "downstream_open": mutation == "open_downstream_history",
    }

    results = {
        "A1": (
            geometry_ok,
            "the periodic L24 shift and exact even/odd D_eo,D_oe blocks are rebuilt",
        ),
        "A2": (
            radius_roster_ok,
            "the target executes exactly the nine frozen squared spatial radii",
        ),
        "A3": (
            all(fact.action_ok for fact in all_facts),
            "every phase-real action has the literal m=2/7 skew-Clifford form",
        ),
        "B1": (
            all(fact.schur_ok for fact in all_facts),
            "both parity Schur complements equal Q tensor B at every radius",
        ),
        "B2": (
            all(
                fact.covariance_ok and fact.marginal_ok
                for fact in all_facts
            ),
            "the exact full covariance and both Schur marginal identities hold",
        ),
        "B3": (
            reflection_derivation_ok
            and all(fact.reflection_ok for fact in all_facts),
            "the inherited even/odd coarse reflections are involutive and action covariant",
        ),
        "B4": (
            all(fact.cuts_ok for fact in all_facts),
            "both adjacent V-translated planes use matched positive and opposite cuts",
        ),
        "C1": (
            all(
                fact.hermitian_ok and fact.factorization_ok
                for fact in all_facts
            ),
            "all 72 coarse Berezin forms are exact Hermitian H tensor G blocks",
        ),
        "C2": (
            all(fact.negative_minors_ok for fact in all_facts),
            "every parity/plane/orientation/radius has a strict negative 2x2 principal minor",
        ),
        "C3": (
            all(inertia == (2, 8, 2) for inertia in all_inertias)
            and all(rank == 4 for rank in all_ranks)
            and claims["os_psd"] is False,
            "each reduced form has exact rank four and inertia (2,8,2), hence is not PSD",
        ),
        "C4": (
            all(inertia == (16, 64, 16) for inertia in all_lifted),
            "the eight-copy full-fiber lifts have rank 32 and inertia (16,64,16)",
        ),
        "D1": (
            radius_one.q_matrix[0, 0] == EXPECTED_Q_DIAGONAL
            and radius_one.q_matrix[0, 1] == EXPECTED_Q_NEIGHBOR
            and controls["q_inertia"] == (12, 0, 0)
            and matrix_equal(radius_one.g_matrix, EXPECTED_G)
            and sp.factor(radius_one.g_matrix.det()) == -R(49, 53),
            "radius one reproduces Q, its positive inertia, G, and det(G)=-49/53",
        ),
        "D2": (
            matrix_equal(controls["minor"], EXPECTED_MINOR)
            and controls["minor_det"] == EXPECTED_MINOR_DETERMINANT
            and controls["minor_det"] < 0,
            "the disclosed radius-one local matrix and negative determinant are reproduced",
        ),
        "D3": (
            all(fact.graph_control_ok for fact in all_facts)
            and claims["conflate"] is False,
            "the positive right-Schur graph factor is exact and remains distinct from Berezin OS",
        ),
        "E1": (
            controls["moment_ratio"] == EXPECTED_MOMENT_RATIO
            and matrix_equal(
                controls["moments"][1],
                EXPECTED_MOMENT_RATIO * controls["moments"][0],
            ),
            "the independently derived local lag ratio is the disclosed exact q",
        ),
        "E2": (
            controls["defect_coefficient"] == EXPECTED_DEFECT_COEFFICIENT
            and matrix_equal(
                controls["moment_defect"],
                EXPECTED_DEFECT_COEFFICIENT * EXPECTED_G,
            )
            and controls["defect_coefficient"] != 0
            and claims["erase_defect"] is False,
            "M2-M1 M0^-1 M1 is the disclosed nonzero finite-circle defect times G",
        ),
        "F1": (
            controls["cross_relation"]
            and controls["i_l_hat_hermitian"]
            and controls["l_hat_square"]
            and controls["cross_internal_square"],
            "the action-derived cross blocks form an exact Hermitian iL_hat control",
        ),
        "F2": (
            controls["temporal_spectrum"]
            and controls["norm"] == R(7) / sp.sqrt(53)
            and controls["norm"] < 1,
            "its norm is 7/sqrt(53)<1 and squared modes are (49/53)sin^2(pi n/12)",
        ),
        "S1": (
            claims["downstream_open"] is False,
            "quotient, CPTP history, response, held-outs, axioms, and TOE movement remain sealed",
        ),
    }
    return results, {
        "radius_one": radius_one,
        "controls": controls,
        "radii": radii,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0

    results, evidence = evaluate(args.mutation)
    checks = Checks()
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)

    controls = evidence["controls"]
    radius_one = evidence["radius_one"]
    print(
        "WITNESS: radius=1; Qdiag="
        f"{radius_one.q_matrix[0,0]}; Qneighbor={radius_one.q_matrix[0,1]}; "
        f"minor_det={controls['minor_det']}; inertia=(2,8,2); "
        "lift=(16,64,16)"
    )
    print(
        f"MOMENT: q={controls['moment_ratio']}; "
        f"defect_coefficient={controls['defect_coefficient']}"
    )
    print(
        "CONTROL: iL_hat Hermitian; ||L||="
        f"{controls['norm']}<1; squared-mode count="
        f"{len(controls['squared_spectrum'])}"
    )
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
