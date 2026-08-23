#!/usr/bin/env python3
"""Exact positive local-innovation dilation of the pinned W response.

On the committed four-pin Dirac--Kahler fixture this runner factors
S_a=Herm(q_a) as B_a B_a^dagger+cI with c=m/2 using columns supported on
single sites and fixed S-graph/coordinate-radius-one edges.  The full-rank
positive action

    (q_a phi-B_a zeta)^dagger c^-1(q_a phi-B_a zeta)+zeta^dagger zeta

then has arm partition proportional to |det q_a|^-2 and phi covariance
q_a^-1 S_a q_a^-dagger.  A positive phi-effect insertion gives the exact
Block 42 joint table after the same imposed identity calibration.  The runner
also keeps the boundary honest: the expanded phi precision has temporal
range two and physical-x range four on the wider tested fixtures,
the visible determinant marginal still fails the matched-blanket test, the
auxiliary carrier/source/clock interpretation is selected content, and the
positive full-rank construction stops at m=0.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_pin_faithful_joint_sector_action_2026_08_23 as b42


b41 = b42.b41
b175 = b42.b175
b174 = b42.b174
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_LOCAL_INNOVATION_RECORD_DILATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_INNOVATION_RECORD_DILATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PIN_FAITHFUL_JOINT_SECTOR_ACTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_pin_faithful_joint_sector_action_"
    "2026_08_23.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_schur_record_response_bridge_"
    "2026_08_23.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PINCER_IDENTITY_CROSS_LANE_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_pincer_identity_cross_lane_"
    "2026_08_22.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.expand(entry) == 0 for entry in value)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(sp.expand(left - right))


def edge_union(matrices: tuple[sp.Matrix, ...]) -> tuple[tuple[int, int], ...]:
    size = matrices[0].rows
    return tuple(
        (row, column)
        for row in range(size)
        for column in range(row + 1, size)
        if any(matrix[row, column] != 0 for matrix in matrices)
    )


def signed_edge_factor(
    symmetric: sp.Matrix, innovation_variance, edges: tuple[tuple[int, int], ...]
) -> tuple[sp.Matrix, tuple]:
    """Local Gram factor of S-cI for a real diagonally-dominant S.

    Each edge column has support on the edge endpoints and contributes the
    exact off-diagonal entry plus its absolute value to both diagonals.  One
    final column per site supplies the strictly positive diagonal residual.
    """
    size = symmetric.rows
    factor = sp.zeros(size, len(edges) + size)
    incident = [ZERO for _ in range(size)]
    for index, (row, column) in enumerate(edges):
        weight = sp.cancel(symmetric[row, column])
        if weight == 0:
            continue
        magnitude = sp.Abs(weight)
        root = sp.sqrt(magnitude)
        factor[row, index] = root
        factor[column, index] = sp.sign(weight) * root
        incident[row] += magnitude
        incident[column] += magnitude
    residuals = tuple(
        sp.cancel(
            symmetric[row, row] - innovation_variance - incident[row]
        )
        for row in range(size)
    )
    for row, residual in enumerate(residuals):
        if residual.is_nonnegative:
            factor[row, len(edges) + row] = sp.sqrt(residual)
    return factor, residuals


def circle_distance(size: int, left: int, right: int) -> int:
    return min((left - right) % size, (right - left) % size)


def column_locality(factor: sp.Matrix, fixture: object) -> tuple[int, int]:
    temporal = []
    spatial = []
    for column in range(factor.cols):
        support = [row for row in range(factor.rows) if factor[row, column] != 0]
        for left in support:
            t_left, x_left = divmod(left, fixture.lx)
            for right in support:
                t_right, x_right = divmod(right, fixture.lx)
                temporal.append(circle_distance(fixture.T, t_left, t_right))
                spatial.append(circle_distance(fixture.lx, x_left, x_right))
    return max(temporal, default=0), max(spatial, default=0)


def spatial_range(matrix: sp.Matrix, fixture: object) -> int:
    distances = []
    for row in range(matrix.rows):
        x_row = row % fixture.lx
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                distances.append(
                    circle_distance(fixture.lx, x_row, column % fixture.lx)
                )
    return max(distances, default=0)


def record_distance(fixture: object, row: int) -> tuple[int, int]:
    time, space = divmod(row, fixture.lx)
    record_time, record_space = b175.RECORD_CELL
    return (
        circle_distance(fixture.T, time, record_time),
        circle_distance(fixture.lx, space, record_space),
    )


def arm_bundle(
    fixture: object,
    value,
    edges: tuple[tuple[int, int], ...],
    mass=ONE,
    fraction=R(1, 2),
) -> dict:
    q = fixture.q({b175.RECORD_CELL: value}, mass=mass)
    completion = b41.positive_completion(q)
    symmetric = completion["symmetric"]
    variance = sp.cancel(sp.sympify(mass) * sp.sympify(fraction))
    factor, residuals = signed_edge_factor(symmetric, variance, edges)
    inverse = completion["q_inv"]
    covariance = sp.expand(
        inverse
        * (factor * factor.H + variance * sp.eye(fixture.N))
        * inverse.H
    )
    return {
        "value": value,
        "q": q,
        "q_inv": inverse,
        "S": symmetric,
        "B": factor,
        "residuals": residuals,
        "variance": variance,
        "W": completion["covariance"],
        "covariance": covariance,
        "det_q": b174.dm_det(q),
        "raw_mass": sp.cancel(
            variance ** fixture.N / b174.norm2(b174.dm_det(q))
        ),
    }


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    fixture = b174.Fixture(b175.LX, tag="b178-local-innovation")
    baseline_q = tuple(
        fixture.q({b175.RECORD_CELL: value}) for value in b175.MENU
    )
    baseline_s = tuple(sp.expand((q + q.H) / 2) for q in baseline_q)
    edges = edge_union(baseline_s)
    arms = tuple(arm_bundle(fixture, value, edges) for value in b175.MENU)

    check(
        "strict-local-innovation-gram",
        all(
            all(residual.is_positive for residual in arm["residuals"])
            and matrix_equal(
                arm["B"] * arm["B"].H,
                arm["S"] - arm["variance"] * sp.eye(fixture.N),
            )
            and column_locality(arm["B"], fixture) == (1, 1)
            for arm in arms
        ),
        "S_a=mH_a splits exactly into onsite variance m/2 plus a Gram factor whose columns live on sites or fixed S-graph coordinate-radius-one edges",
    )

    congruence_ok = all(
        b174.dm_det(arm["q"]) != 0
        and arm["variance"] > 0
        and arm["B"].rows == arm["q"].rows
        for arm in arms
    )
    check(
        "full-rank-positive-local-residual-action",
        congruence_ok,
        "the enlarged precision is T^dag diag((m/2)^-1 I,I) T with invertible triangular T, hence a full-rank positive Gaussian action",
    )

    p_dilation = normalize(tuple(arm["raw_mass"] for arm in arms))
    p_det = normalize(
        tuple(ONE / b174.norm2(arm["det_q"]) for arm in arms)
    )
    check(
        "congruence-determinant-formation-law",
        p_dilation == p_det
        and all(value > 0 for value in p_dilation)
        and all(
            sp.cancel(
                arm["raw_mass"]
                - arm["variance"] ** fixture.N
                / b174.norm2(arm["det_q"])
            )
            == 0
            for arm in arms
        ),
        "det M_a=(m/2)^-N |det q_a|^2, so the enlarged positive action has exactly the parent arm weights without an S spectator determinant",
    )

    check(
        "exact-W-covariance-from-local-innovations",
        all(matrix_equal(arm["covariance"], arm["W"]) for arm in arms),
        "the phi covariance is q_a^-1(B_a B_a^dag+mI/2)q_a^-dagger=Herm(q_a^-1) exactly",
    )

    all_slices = True
    event_tables = []
    for level in fixture.free_levels:
        rows = b41.slice_rows(fixture, level)
        densities = []
        for arm in arms:
            block = arm["covariance"].extract(rows, rows)
            density = sp.expand(block / sp.trace(block))
            densities.append(density)
            for slot in range(fixture.lx):
                effect = b41.basis_projector(slot, fixture.lx)
                all_slices = all_slices and (
                    sp.cancel(sp.trace(block * effect) / sp.trace(block))
                    == density[slot, slot]
                )
        event_tables.append(
            sp.Matrix(
                [
                    [p_dilation[a] * densities[a][slot, slot] for slot in range(4)]
                    for a in range(4)
                ]
            )
        )
    check(
        "positive-marked-insertion-on-all-free-slices",
        all_slices
        and all(
            all(table[a, j] > 0 for a in range(4) for j in range(4))
            and sp.cancel(sum(table, ZERO)) == ONE
            for table in event_tables
        ),
        "the positive insertion phi_R^dag E_j phi_R with imposed identity calibration 1/Tr(W_RR) induces the exact normalized marked-intensity/projector table on all four free slices",
    )

    block42_rows = b41.slice_rows(fixture, fixture.tstar)
    block42_event = sp.Matrix(
        [
            [
                p_dilation[a]
                * sp.cancel(
                    arms[a]["W"].extract(block42_rows, block42_rows)[j, j]
                    / sp.trace(arms[a]["W"].extract(block42_rows, block42_rows))
                )
                for j in range(4)
            ]
            for a in range(4)
        ]
    )
    check(
        "block42-joint-table-recovered-without-dense-effective-precision",
        matrix_equal(event_tables[-1], block42_event),
        "the local innovation action reproduces Block 42 P(a,j) entry for entry while keeping K_W only as a marginalized precision",
    )

    raw = tuple(arm["raw_mass"] for arm in arms)
    split = R(3, 8)
    refined = normalize((split * raw[0], (ONE - split) * raw[0], *raw[1:]))
    duplicated = normalize((raw[0], raw[0], *raw[1:]))
    check(
        "alternative-base-measure-still-load-bearing",
        sp.cancel(refined[0] + refined[1] - p_dilation[0]) == 0
        and tuple(refined[index + 1] for index in range(1, 4)) == p_dilation[1:]
        and sp.cancel(duplicated[0] + duplicated[1] - p_dilation[0]) != 0,
        "additive base-measure refinement pushes the marked intensity forward exactly, while duplicate-label counting still changes the arm law",
    )

    locality_ladder = []
    for cover in (8, 12, 16, 20, 24):
        cover_fixture = b174.Fixture(4, tag=f"b178-cover-{cover}", cover_t=cover)
        cover_qs = tuple(
            cover_fixture.q({b175.RECORD_CELL: value}) for value in b175.MENU
        )
        cover_ss = tuple(sp.expand((q + q.H) / 2) for q in cover_qs)
        cover_edges = edge_union(cover_ss)
        cover_rows = []
        for q, symmetric in zip(cover_qs, cover_ss):
            factor, residuals = signed_edge_factor(
                symmetric, R(1, 2), cover_edges
            )
            cover_rows.append((q, factor, residuals))
        locality_ladder.append(
            (
                cover_fixture.T,
                max(b42.temporal_range(row[0], cover_fixture) for row in cover_rows),
                max(column_locality(row[1], cover_fixture)[0] for row in cover_rows),
                max(
                    b42.temporal_range(
                        sp.expand(row[0].H * row[0]), cover_fixture
                    )
                    for row in cover_rows
                ),
                min(min(row[2]) for row in cover_rows),
            )
        )
    check(
        "five-cover-factor-locality-ladder",
        tuple(row[0] for row in locality_ladder) == (4, 6, 8, 10, 12)
        and tuple(row[1] for row in locality_ladder) == (1, 1, 1, 1, 1)
        and tuple(row[2] for row in locality_ladder) == (1, 1, 1, 1, 1)
        and tuple(row[3] for row in locality_ladder) == (2, 2, 2, 2, 2)
        and all(row[4] > 0 for row in locality_ladder),
        "q rows and innovation columns stay temporal radius one on five covers; the expanded phi precision is uniformly measured at temporal radius two",
    )

    holdout_fixture = b174.Fixture(4, tag="b178-holdout-28", cover_t=28)
    holdout_qs = tuple(
        holdout_fixture.q({b175.RECORD_CELL: value}) for value in b175.MENU
    )
    holdout_ss = tuple(sp.expand((q + q.H) / 2) for q in holdout_qs)
    holdout_edges = edge_union(holdout_ss)
    holdout_ok = True
    for q, symmetric in zip(holdout_qs, holdout_ss):
        factor, residuals = signed_edge_factor(
            symmetric, R(1, 2), holdout_edges
        )
        holdout_ok = holdout_ok and (
            all(residual.is_positive for residual in residuals)
            and matrix_equal(
                factor * factor.H,
                symmetric - R(1, 2) * sp.eye(holdout_fixture.N),
            )
            and column_locality(factor, holdout_fixture) == (1, 1)
            and b42.temporal_range(q, holdout_fixture) == 1
            and b42.temporal_range(sp.expand(q.H * q), holdout_fixture) == 2
        )
    check(
        "heldout-larger-cover-local-factor",
        holdout_fixture.T == 14 and holdout_ok,
        "the same fixed m/2 rule passes all four pins at the unfitted cover extent 28 (physical time 14) with temporal-radius-one q rows and innovation columns",
    )

    spatial_rows = []
    for width in (4, 8, 12):
        width_fixture = b174.Fixture(
            width,
            pattern=b174.constant_pattern(width),
            tag=f"b178-spatial-{width}",
        )
        q = width_fixture.q({(b174.RECORD_LEVEL, 0): b175.MENU[-1]})
        symmetric = sp.expand((q + q.H) / 2)
        width_edges = edge_union((symmetric,))
        factor, residuals = signed_edge_factor(
            symmetric, R(1, 2), width_edges
        )
        spatial_rows.append(
            (
                width,
                spatial_range(q, width_fixture),
                column_locality(factor, width_fixture)[1],
                spatial_range(sp.expand(q.H * q), width_fixture),
                min(residuals),
            )
        )
    check(
        "physical-spatial-range-boundary",
        tuple(row[0] for row in spatial_rows) == (4, 8, 12)
        and tuple(row[1] for row in spatial_rows) == (2, 2, 2)
        and tuple(row[2] for row in spatial_rows) == (1, 1, 1)
        and tuple(row[3] for row in spatial_rows) == (2, 4, 4)
        and all(row[4] > 0 for row in spatial_rows),
        "innovation columns are physical-x radius one, but q rows reach radius two and q^dagger q reaches radius four once width removes the four-site alias",
    )

    reference = arms[-1]
    mutation_local = True
    for arm in arms[:-1]:
        changed_rows = {
            row
            for row in range(fixture.N)
            if any(
                arm["q"][row, column] != reference["q"][row, column]
                for column in range(fixture.N)
            )
            or any(
                arm["B"][row, column] != reference["B"][row, column]
                for column in range(reference["B"].cols)
            )
        }
        phi_support = {
            column
            for row in changed_rows
            for column in range(fixture.N)
            if arm["q"][row, column] != 0
            or reference["q"][row, column] != 0
        }
        changed_offsets = tuple(
            record_distance(fixture, row) for row in changed_rows
        )
        support_offsets = tuple(
            record_distance(fixture, column) for column in phi_support
        )
        mutation_local = (
            mutation_local
            and all(sum(offset) <= 1 for offset in changed_offsets)
            and all(max(offset) <= 2 for offset in support_offsets)
            and max(sum(offset) for offset in support_offsets) == 4
        )
    check(
        "alternative-coefficient-mutation-has-exact-bounded-box",
        mutation_local,
        "changed q_a/B_a rows lie on the cubic-graph Record star, while affected residual factors inspect a coordinatewise (dt,dx)<= (2,2) box reaching graph distance four",
    )

    fraction_alt = R(1, 3)
    alternate = arm_bundle(fixture, b175.MENU[-1], edges, fraction=fraction_alt)
    check(
        "microscopic-dilation-is-not-unique",
        all(residual.is_positive for residual in alternate["residuals"])
        and matrix_equal(alternate["covariance"], reference["covariance"])
        and not matrix_equal(alternate["B"], reference["B"]),
        "m/3 and m/2 innovation splits give distinct positive local hidden actions with the same W covariance and normalized arm law",
    )

    mass_scaling = True
    for mass in (R(1, 3), ONE, sp.Integer(3)):
        mass_qs = tuple(
            fixture.q({b175.RECORD_CELL: value}, mass=mass)
            for value in b175.MENU
        )
        mass_ss = tuple(sp.expand((q + q.H) / 2) for q in mass_qs)
        mass_edges = edge_union(mass_ss)
        for q, symmetric in zip(mass_qs, mass_ss):
            factor, residuals = signed_edge_factor(
                symmetric, mass / 2, mass_edges
            )
            mass_scaling = mass_scaling and (
                b174.dm_det(q) != 0
                and all(residual.is_positive for residual in residuals)
                and matrix_equal(
                    factor * factor.H,
                    symmetric - (mass / 2) * sp.eye(fixture.N),
                )
            )
    zero_q = fixture.q({}, mass=ZERO)
    check(
        "positive-mass-domain-and-zero-mass-stop",
        mass_scaling
        and matrix_zero(b175.herm(zero_q))
        and b174.dm_det(zero_q) != 0,
        "the local m/2 Gram split is exact with invertible q at m=1/3,1,3; at m=0 its positive residual metric diverges and the normalized W response remains undefined",
    )

    twin_pattern = b174.twin_pattern(8)
    twin_fixture = b174.Fixture(8, pattern=twin_pattern, tag="b178-twin")
    left_states = b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 0)
    right_states = b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 4)
    left_law = b174.readout_laws(left_states)["sq"]["law"]
    right_law = b174.readout_laws(right_states)["sq"]["law"]
    twin_gap = max(
        sp.Abs(sp.cancel(left - right))
        for left, right in zip(left_law, right_law)
    )
    check(
        "visible-blanket-marginal-remains-nonlocal",
        b174.pattern_certificate(twin_pattern)["same_blanket"]
        and R(4931, 100000000) < twin_gap < R(1233, 25000000),
        "the microscopic factor graph is local, but after its auxiliary fields are integrated the old determinant arm marginal still differs at the matched visible blanket",
    )

    check(
        "selection-and-input-boundary",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "zero TOE-percentage movement" in NOTE.read_text(encoding="utf-8"),
        "the auxiliary carrier, innovation split, source/event identification, base measure, and clock remain selected downstream content with no score claim",
    )

    print("per_element: every local residual, edge/on-site innovation column, projector insertion, and refinement share is checked exactly")
    print("per_site: four hard pins, their record-star action mutations, all four free response slices, and the matched visible twin are checked")
    print("per_mode: full q/B Gram and covariance matrices, determinant factors, and two distinct hidden dilations are checked")
    print("per_block: four baseline arms, three positive masses, six temporal covers, and three spatial probes certify bounded range on the executed ladders")
    print("lattice_wide: checked and not executed — no M2(C) embedding of the auxiliary innovations or autonomous physical Record history is selected")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
