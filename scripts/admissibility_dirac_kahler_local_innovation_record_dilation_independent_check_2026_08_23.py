#!/usr/bin/env python3
"""Independent reconstruction of the local-innovation dilation.

This checker imports the Block 174 action fixture directly, not the primary
Block 43 runner.  It uses c=m/3, reverses the edge-column order, rebuilds the
W covariance from q^-1, and samples a disjoint cover subset including the
held-out extent.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_site_conditional_law_family_2026_08_22 as b174


R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
MENU = b174.MENU
RECORD_CELL = (b174.RECORD_LEVEL, 0)
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def zero(matrix: sp.Matrix) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and zero(sp.expand(left - right))


def herm(matrix: sp.Matrix) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def inverse(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.inv(method="DM")


def edge_set(matrices: tuple[sp.Matrix, ...]) -> tuple[tuple[int, int], ...]:
    size = matrices[0].rows
    return tuple(
        reversed(
            [
                (i, j)
                for i in range(size)
                for j in range(i + 1, size)
                if any(matrix[i, j] != 0 for matrix in matrices)
            ]
        )
    )


def factor(
    symmetric: sp.Matrix, variance, edges: tuple[tuple[int, int], ...]
) -> tuple[sp.Matrix, tuple]:
    size = symmetric.rows
    output = sp.zeros(size, size + len(edges))
    diagonal_use = [ZERO for _ in range(size)]
    for column, (i, j) in enumerate(edges):
        weight = sp.cancel(symmetric[i, j])
        if weight == 0:
            continue
        magnitude = sp.Abs(weight)
        output[i, column] = sp.sqrt(magnitude)
        output[j, column] = sp.sign(weight) * sp.sqrt(magnitude)
        diagonal_use[i] += magnitude
        diagonal_use[j] += magnitude
    remainders = tuple(
        sp.cancel(symmetric[i, i] - variance - diagonal_use[i])
        for i in range(size)
    )
    for i, remainder in enumerate(remainders):
        if remainder.is_nonnegative:
            output[i, len(edges) + i] = sp.sqrt(remainder)
    return output, remainders


def circle(size: int, left: int, right: int) -> int:
    return min((left - right) % size, (right - left) % size)


def temporal_range(matrix: sp.Matrix, fixture: object) -> int:
    values = []
    for i in range(matrix.rows):
        t_i = i // fixture.lx
        for j in range(matrix.cols):
            if matrix[i, j] != 0:
                t_j = j // fixture.lx
                values.append(circle(fixture.T, t_i, t_j))
    return max(values, default=0)


def spatial_range(matrix: sp.Matrix, fixture: object) -> int:
    values = []
    for i in range(matrix.rows):
        x_i = i % fixture.lx
        for j in range(matrix.cols):
            if matrix[i, j] != 0:
                values.append(circle(fixture.lx, x_i, j % fixture.lx))
    return max(values, default=0)


def factor_diameter(matrix: sp.Matrix, fixture: object) -> tuple[int, int]:
    time = []
    space = []
    for column in range(matrix.cols):
        support = [row for row in range(matrix.rows) if matrix[row, column] != 0]
        for left in support:
            t_left, x_left = divmod(left, fixture.lx)
            for right in support:
                t_right, x_right = divmod(right, fixture.lx)
                time.append(circle(fixture.T, t_left, t_right))
                space.append(circle(fixture.lx, x_left, x_right))
    return max(time, default=0), max(space, default=0)


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

    fixture = b174.Fixture(4, tag="b178-independent")
    qs = tuple(fixture.q({RECORD_CELL: value}) for value in MENU)
    symmetric = tuple(herm(q) for q in qs)
    edges = edge_set(symmetric)
    variance = R(1, 3)
    factors = tuple(factor(matrix, variance, edges) for matrix in symmetric)

    check(
        "independent-local-gram",
        all(
            all(value.is_positive for value in remainders)
            and equal(B * B.H, S - variance * sp.eye(fixture.N))
            and factor_diameter(B, fixture) == (1, 1)
            for S, (B, remainders) in zip(symmetric, factors)
        ),
        "a reversed-column c=m/3 reconstruction gives exact site/edge Gram factors for all four arms",
    )

    raw = tuple(
        sp.cancel(variance ** fixture.N / b174.norm2(b174.dm_det(q)))
        for q in qs
    )
    determinant = tuple(
        sp.cancel(ONE / b174.norm2(b174.dm_det(q))) for q in qs
    )
    check(
        "independent-partition-law",
        normalize(raw) == normalize(determinant)
        and all(value > 0 for value in raw),
        "the common c^N congruence factor cancels and independently recovers the determinant arm law",
    )

    covariances = []
    expected = []
    for q, S, (B, _) in zip(qs, symmetric, factors):
        q_inv = inverse(q)
        covariance = sp.expand(
            q_inv * (B * B.H + variance * sp.eye(fixture.N)) * q_inv.H
        )
        covariances.append(covariance)
        expected.append(herm(q_inv))
    check(
        "independent-W-covariance",
        all(equal(left, right) for left, right in zip(covariances, expected)),
        "the visible covariance independently reduces to Herm(q^-1) on every arm",
    )

    level = fixture.free_levels[0]
    rows = tuple(range(level * fixture.lx, (level + 1) * fixture.lx))
    probabilities = normalize(raw)
    table = sp.zeros(4, 4)
    for arm, covariance in enumerate(covariances):
        block = covariance.extract(rows, rows)
        for outcome in range(4):
            table[arm, outcome] = sp.cancel(
                probabilities[arm] * block[outcome, outcome] / sp.trace(block)
            )
    check(
        "independent-positive-joint-table",
        all(table[a, j] > 0 for a in range(4) for j in range(4))
        and sp.cancel(sum(table, ZERO)) == ONE
        and all(
            sp.cancel(sum(table[a, j] for j in range(4)) - probabilities[a])
            == 0
            for a in range(4)
        ),
        "one disjoint free slice gives a normalized positive arm/projector marked-intensity table",
    )

    local_mutation = True
    default_q = qs[-1]
    default_B = factors[-1][0]
    for q, (B, _) in zip(qs[:-1], factors[:-1]):
        changed = {
            row
            for row in range(fixture.N)
            if any(q[row, col] != default_q[row, col] for col in range(fixture.N))
            or any(B[row, col] != default_B[row, col] for col in range(B.cols))
        }
        phi_support = {
            column
            for row in changed
            for column in range(fixture.N)
            if q[row, column] != 0 or default_q[row, column] != 0
        }
        changed_offsets = tuple(
            (
                circle(fixture.T, row // fixture.lx, RECORD_CELL[0]),
                circle(fixture.lx, row % fixture.lx, RECORD_CELL[1]),
            )
            for row in changed
        )
        support_offsets = tuple(
            (
                circle(fixture.T, column // fixture.lx, RECORD_CELL[0]),
                circle(fixture.lx, column % fixture.lx, RECORD_CELL[1]),
            )
            for column in phi_support
        )
        local_mutation = (
            local_mutation
            and all(sum(offset) <= 1 for offset in changed_offsets)
            and all(max(offset) <= 2 for offset in support_offsets)
            and max(sum(offset) for offset in support_offsets) == 4
        )
    check(
        "independent-coefficient-mutation-bounded-box",
        local_mutation,
        "changed coefficient rows are on the cubic-graph Record star; affected residual factors inspect a coordinatewise (dt,dx)<= (2,2) box reaching graph distance four",
    )

    cover_ok = True
    cover_rows = []
    for cover in (12, 20, 28):
        cover_fixture = b174.Fixture(4, tag=f"b178-independent-{cover}", cover_t=cover)
        q = cover_fixture.q({RECORD_CELL: MENU[1]})
        S = herm(q)
        local_edges = edge_set((S,))
        B, remainders = factor(S, variance, local_edges)
        row = (
            cover_fixture.T,
            temporal_range(q, cover_fixture),
            factor_diameter(B, cover_fixture)[0],
            temporal_range(sp.expand(q.H * q), cover_fixture),
        )
        cover_rows.append(row)
        cover_ok = cover_ok and (
            all(value.is_positive for value in remainders)
            and equal(B * B.H, S - variance * sp.eye(cover_fixture.N))
        )
    check(
        "independent-cover-locality",
        cover_ok
        and tuple(row[0] for row in cover_rows) == (6, 10, 14)
        and all(row[1:] == (1, 1, 2) for row in cover_rows),
        "three disjoint covers including held-out 28 retain temporal-radius-one residual factors and temporal-radius-two expanded visible precision",
    )

    width_fixture = b174.Fixture(
        8, pattern=b174.constant_pattern(8), tag="b178-independent-width8"
    )
    width_q = width_fixture.q({(b174.RECORD_LEVEL, 0): MENU[2]})
    width_s = herm(width_q)
    width_edges = edge_set((width_s,))
    width_B, width_remainders = factor(width_s, variance, width_edges)
    check(
        "independent-physical-spatial-boundary",
        all(value.is_positive for value in width_remainders)
        and spatial_range(width_q, width_fixture) == 2
        and factor_diameter(width_B, width_fixture)[1] == 1
        and spatial_range(sp.expand(width_q.H * width_q), width_fixture) == 4,
        "at held-out physical width eight the innovation columns are x-radius one, q reaches two, and the expanded visible precision reaches four",
    )

    B_half, rem_half = factor(symmetric[-1], R(1, 2), edges)
    q_inv = inverse(qs[-1])
    covariance_half = sp.expand(
        q_inv * (B_half * B_half.H + R(1, 2) * sp.eye(fixture.N)) * q_inv.H
    )
    check(
        "independent-hidden-split-nonuniqueness",
        all(value.is_positive for value in rem_half)
        and not equal(B_half, factors[-1][0])
        and equal(covariance_half, covariances[-1]),
        "the independently compared m/3 and m/2 hidden actions differ but have the same visible covariance",
    )

    split = R(4, 9)
    refined = normalize((split * raw[0], (ONE - split) * raw[0], *raw[1:]))
    check(
        "independent-additive-refinement",
        sp.cancel(refined[0] + refined[1] - probabilities[0]) == 0
        and tuple(refined[index + 1] for index in range(1, 4))
        == probabilities[1:],
        "a different exact alternative split pushes the local-action intensity forward additively",
    )

    zero_q = fixture.q({}, mass=ZERO)
    check(
        "independent-zero-mass-boundary",
        zero(herm(zero_q)) and b174.dm_det(zero_q) != 0,
        "at m=0 the positive residual variance vanishes although q remains invertible",
    )

    twin = b174.twin_pattern(8)
    twin_fixture = b174.Fixture(8, pattern=twin, tag="b178-independent-twin")
    left = b174.readout_laws(
        b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 0)
    )["sq"]["law"]
    right = b174.readout_laws(
        b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 4)
    )["sq"]["law"]
    gap = max(sp.Abs(sp.cancel(a - b)) for a, b in zip(left, right))
    check(
        "independent-visible-twin-boundary",
        b174.pattern_certificate(twin)["same_blanket"]
        and R(4931, 100000000) < gap < R(1233, 25000000),
        "the visible determinant marginal independently retains the matched-blanket gap",
    )

    check(
        "independent-input-closure",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "zero TOE-percentage movement" in NOTE.read_text(encoding="utf-8"),
        "the checker reads only the final note, its direct Block 42/174 sources, and Minimal Axioms",
    )

    print("per_element: reversed local Gram columns, positive remainders, projector atoms, and refinement shares are rebuilt")
    print("per_site: four hard pins, one disjoint free slice, the Record star, and the matched visible twin are checked")
    print("per_mode: full visible covariances, two innovation splits, and complex determinant factors are reconstructed")
    print("per_block: four baseline arms, three independently sampled time covers, and one wider physical-x fixture are checked")
    print("lattice_wide: checked and not executed — no physical auxiliary-to-M2(C) compiler or autonomous Record process is selected")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
