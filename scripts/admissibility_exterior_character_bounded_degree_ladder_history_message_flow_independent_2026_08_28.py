#!/usr/bin/env python3
"""Independent exact finite checks for the bounded-degree ladder history message.

This helper uses only integers, Fraction, finite enumeration, and a direct
polynomial determinant.  It does not import the primary runner or SymPy.
"""

from __future__ import annotations

from fractions import Fraction
import itertools


AUDIT_TIMEOUT_SEC = 120

G = (1, -1)


def poly_add(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_scale(a: tuple[Fraction, ...], scalar: Fraction) -> tuple[Fraction, ...]:
    return tuple(scalar * value for value in a)


def poly_mul(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def determinant_polynomial(
    matrix: tuple[tuple[tuple[Fraction, ...], ...], ...]
) -> tuple[Fraction, ...]:
    size = len(matrix)
    total = (Fraction(0),)
    for perm in itertools.permutations(range(size)):
        term = (Fraction(permutation_sign(perm)),)
        for row, column in enumerate(perm):
            term = poly_mul(term, matrix[row][column])
        total = poly_add(total, term)
    return total


def matmul(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def diagonal(values: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(value if i == j else Fraction(0) for j in range(len(values)))
        for i, value in enumerate(values)
    )


def transpose(matrix: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def matrix_power(
    matrix: tuple[tuple[Fraction, ...], ...], exponent: int
) -> tuple[tuple[Fraction, ...], ...]:
    size = len(matrix)
    result = tuple(
        tuple(Fraction(int(i == j)) for j in range(size)) for i in range(size)
    )
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def ladder_edges(length: int) -> tuple[tuple[str, int, int], ...]:
    edges: list[tuple[str, int, int]] = []
    for i in range(length):
        edges.append(("u", i, i + 1))
    for i in range(length):
        edges.append(("v", length + 1 + i, length + 1 + i + 1))
    for i in range(length + 1):
        edges.append(("h", i, length + 1 + i))
    return tuple(edges)


def coarsen_length_two(config: tuple[int, ...]) -> tuple[int, int, int, int]:
    u0, u1, v0, v1, h0, _h1, h2 = config
    return (u1 * u0, v1 * v0, h0, h2)


def gauge_action(
    config: tuple[int, ...], gauges: tuple[int, ...], length: int
) -> tuple[int, ...]:
    edges = ladder_edges(length)
    return tuple(gauges[target] * value * gauges[source] for value, (_, source, target) in zip(config, edges))


def coarse_gauge_action(
    config: tuple[int, int, int, int], retained: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    bottom_rail, top_rail, left_rung, right_rung = config
    gb0, gt0, gb2, gt2 = retained
    return (
        gb2 * bottom_rail * gb0,
        gt2 * top_rail * gt0,
        gt0 * left_rung * gb0,
        gt2 * right_rung * gb2,
    )


def rail_forest_rungs(config: tuple[int, ...]) -> tuple[int, int, int]:
    u0, u1, v0, v1, h0, h1, h2 = config
    tau_b = (1, u0, u1 * u0)
    tau_t = (1, v0, v1 * v0)
    return tuple(tau_t[i] * h * tau_b[i] for i, h in enumerate((h0, h1, h2)))


def perimeter_polynomial_one(w_prime: int, w_value: int) -> tuple[Fraction, ...]:
    x = (1, w_value)
    xp = (1, w_prime)
    total = (Fraction(0),)
    for gb0, gt0, gb1, gt1 in itertools.product(G, repeat=4):
        signs = (
            xp[0] * gt0 * x[0] * gb0,
            xp[1] * gt1 * x[1] * gb1,
            gb1 * gb0,
            gt1 * gt0,
        )
        term = (Fraction(1),)
        for sign in signs:
            term = poly_mul(term, (Fraction(1), Fraction(sign)))
        total = poly_add(total, term)
    return poly_scale(total, Fraction(1, 16))


def perimeter_polynomial_two() -> tuple[Fraction, ...]:
    """Fourier coefficient of the outer two-cell cycle in the temporal kernel."""

    total = (Fraction(0),)
    normalizer = Fraction(1, 2 ** 12)
    for x in itertools.product(G, repeat=3):
        for xp in itertools.product(G, repeat=3):
            outer_character = x[0] * x[2] * xp[0] * xp[2]
            for gb in itertools.product(G, repeat=3):
                for gt in itertools.product(G, repeat=3):
                    signs = [xp[i] * gt[i] * x[i] * gb[i] for i in range(3)]
                    signs.extend(gb[i + 1] * gb[i] for i in range(2))
                    signs.extend(gt[i + 1] * gt[i] for i in range(2))
                    term = (Fraction(outer_character),)
                    for sign in signs:
                        term = poly_mul(term, (Fraction(1), Fraction(sign)))
                    total = poly_add(total, term)
    return poly_scale(total, normalizer)


def connector_deleted_matrix() -> tuple[tuple[Fraction, ...], ...]:
    states = tuple(itertools.product(G, repeat=2))

    def rho(state: tuple[int, int]) -> Fraction:
        xp, x = state
        return Fraction(1) + Fraction(xp * x, 2)

    def m(value: int) -> Fraction:
        return Fraction(1) if value == 1 else Fraction(1, 2)

    return tuple(
        tuple(
            m(y[0] * z[0]) * m(y[1] * z[1]) * rho(y) / 4
            for y in states
        )
        for z in states
    )


def characteristic_polynomial(matrix: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, ...]:
    size = len(matrix)
    polynomial_matrix: list[list[tuple[Fraction, ...]]] = []
    for i in range(size):
        row: list[tuple[Fraction, ...]] = []
        for j in range(size):
            constant = -matrix[i][j]
            row.append((constant, Fraction(int(i == j))))
        polynomial_matrix.append(row)
    return determinant_polynomial(tuple(tuple(row) for row in polynomial_matrix))


def actual_history_components() -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[Fraction, ...],
    tuple[tuple[Fraction, ...], ...],
    tuple[tuple[Fraction, ...], ...],
]:
    states = tuple(itertools.product(G, repeat=4))
    half = Fraction(1, 2)

    def w(value: int) -> Fraction:
        return Fraction(1) + half * value

    def m(value: int) -> Fraction:
        return Fraction(1) if value == 1 else half

    densities = tuple(w(xp * gt * x * gb) for gb, gt, xp, x in states)
    bond = tuple(
        tuple(
            w(y[0] * z[0])
            * w(y[1] * z[1])
            * m(y[2] * z[2])
            * m(y[3] * z[3])
            for y in states
        )
        for z in states
    )
    measure = diagonal(tuple(value / 16 for value in densities))
    return states, densities, bond, matmul(bond, measure)


def kernel_power(
    bond: tuple[tuple[Fraction, ...], ...],
    measure: tuple[tuple[Fraction, ...], ...],
    exponent: int,
) -> tuple[tuple[Fraction, ...], ...]:
    result = bond
    for _ in range(1, exponent):
        result = matmul(matmul(result, measure), bond)
    return result


def physical_three_column_weights(*, duplicate_middle: bool = False) -> tuple[Fraction, ...]:
    states, densities, bond, _operator = actual_history_components()
    measure = diagonal(tuple(value / 16 for value in densities))
    bond_two = kernel_power(bond, measure, 2)
    bond_four = kernel_power(bond, measure, 4)

    def endpoint(pair: tuple[int, int]) -> tuple[tuple[Fraction, ...], ...]:
        return tuple(
            (densities[index] / 4,) if state[2:] == pair else (Fraction(0),)
            for index, state in enumerate(states)
        )

    values: list[Fraction] = []
    for pair0, pair1, pair2 in itertools.product(itertools.product(G, repeat=2), repeat=3):
        e0 = endpoint(pair0)
        e1_column = endpoint(pair1)
        e2 = endpoint(pair2)
        e1_values = tuple(row[0] for row in e1_column)
        middle = diagonal(e1_values)
        staged_middle = middle
        if duplicate_middle:
            staged_middle = matmul(middle, middle)
        direct = matmul(
            matmul(matmul(matmul(transpose(e0), bond_four), middle), bond_four),
            e2,
        )[0][0]
        staged = matmul(
            matmul(
                matmul(
                    matmul(
                        matmul(
                            matmul(
                                matmul(
                                    matmul(transpose(e0), bond_two),
                                    measure,
                                ),
                                bond_two,
                            ),
                            staged_middle,
                        ),
                        bond_two,
                    ),
                    measure,
                ),
                bond_two,
            ),
            e2,
        )[0][0]
        values.append(direct - staged)
    return tuple(values)


def raw_two_bond_shared_frame_check() -> tuple[bool, bool]:
    """Compare an independent raw Haar sum with the shared-frame matrix marginal."""

    states, densities, bond, _operator = actual_history_components()
    physical_pairs = tuple(itertools.product(G, repeat=2))

    def raw_weight(
        pair0: tuple[int, int], pair1: tuple[int, int], pair2: tuple[int, int],
        *, duplicate_middle: bool,
    ) -> Fraction:
        total = Fraction(0)
        for i, z0 in enumerate(states):
            if z0[2:] != pair0:
                continue
            for j, z1 in enumerate(states):
                if z1[2:] != pair1:
                    continue
                for k, z2 in enumerate(states):
                    if z2[2:] != pair2:
                        continue
                    middle_density = densities[j]
                    if duplicate_middle:
                        middle_density *= densities[j]
                    total += (
                        densities[i]
                        * bond[i][j]
                        * middle_density
                        * bond[j][k]
                        * densities[k]
                        / Fraction(4**3)
                    )
        return total

    matrix_values: list[Fraction] = []
    duplicated_values: list[Fraction] = []
    raw_values: list[Fraction] = []
    for pair0, pair1, pair2 in itertools.product(physical_pairs, repeat=3):
        endpoint0 = tuple(
            (densities[i] / 4,) if state[2:] == pair0 else (Fraction(0),)
            for i, state in enumerate(states)
        )
        endpoint2 = tuple(
            (densities[i] / 4,) if state[2:] == pair2 else (Fraction(0),)
            for i, state in enumerate(states)
        )
        middle_values = tuple(
            densities[i] / 4 if state[2:] == pair1 else Fraction(0)
            for i, state in enumerate(states)
        )
        middle = diagonal(middle_values)
        matrix_value = matmul(
            matmul(matmul(matmul(transpose(endpoint0), bond), middle), bond),
            endpoint2,
        )[0][0]
        matrix_values.append(matrix_value)
        raw_values.append(raw_weight(pair0, pair1, pair2, duplicate_middle=False))
        duplicated_values.append(
            raw_weight(pair0, pair1, pair2, duplicate_middle=True)
        )

    return tuple(matrix_values) == tuple(raw_values), tuple(duplicated_values) != tuple(raw_values)


def compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(left)))


def s3_ordered_direct_staged() -> bool:
    group = tuple(itertools.permutations(range(3)))
    for links in itertools.product(group, repeat=4):
        direct = compose_permutations(
            links[3],
            compose_permutations(links[2], compose_permutations(links[1], links[0])),
        )
        first = compose_permutations(links[1], links[0])
        second = compose_permutations(links[3], links[2])
        if direct != compose_permutations(second, first):
            return False
    return True


def scalar_merge(x: Fraction, y: Fraction, q_value: Fraction) -> Fraction:
    return (x + q_value * y) / (1 + q_value * x * y)


def independent_facts() -> dict[str, object]:
    length = 4
    edges = ladder_edges(length)
    degrees = [0 for _ in range(2 * length + 2)]
    for _, source, target in edges:
        degrees[source] += 1
        degrees[target] += 1

    pushforward: dict[tuple[int, int, int, int], int] = {}
    equivariant = True
    orbit_signatures: set[tuple[int, int]] = set()
    for config in itertools.product(G, repeat=7):
        coarse = coarsen_length_two(config)
        pushforward[coarse] = pushforward.get(coarse, 0) + 1
        x0, x1, x2 = rail_forest_rungs(config)
        orbit_signatures.add((x1 * x0, x2 * x1))
        for gauges in itertools.product(G, repeat=6):
            transformed = gauge_action(config, gauges, 2)
            retained = (gauges[0], gauges[3], gauges[2], gauges[5])
            if coarsen_length_two(transformed) != coarse_gauge_action(coarse, retained):
                equivariant = False

    one_cell = {
        (wp, wv): perimeter_polynomial_one(wp, wv)
        for wp, wv in itertools.product(G, repeat=2)
    }
    connector_matrix = connector_deleted_matrix()
    _history_states, _history_densities, _history_bond, actual_matrix = actual_history_components()
    actual_four_direct = matrix_power(actual_matrix, 4)
    actual_two_staged = matmul(matrix_power(actual_matrix, 2), matrix_power(actual_matrix, 2))
    raw_shared_matches, raw_shared_duplicate_fails = raw_two_bond_shared_frame_check()

    q_value = Fraction(1, 9)
    r_value = Fraction(1, 2)
    left = scalar_merge(scalar_merge(r_value, r_value, q_value), r_value, q_value)
    right = scalar_merge(r_value, scalar_merge(r_value, r_value, q_value), q_value)

    return {
        "vertices": 2 * length + 2,
        "edges": len(edges),
        "max_degree": max(degrees),
        "degree_multiset": tuple(sorted(degrees)),
        "pushforward_counts": tuple(sorted(pushforward.values())),
        "coarsening_equivariant": equivariant,
        "residual_orbit_count": len(orbit_signatures),
        "one_cell_perimeter": one_cell,
        "two_cell_outer": perimeter_polynomial_two(),
        "connector_charpoly": characteristic_polynomial(connector_matrix),
        "history_direct_staged": actual_four_direct == actual_two_staged,
        "physical_shared_direct_staged": all(value == 0 for value in physical_three_column_weights()),
        "physical_duplicate_middle_fails": any(value != 0 for value in physical_three_column_weights(duplicate_middle=True)),
        "raw_shared_frame_matches": raw_shared_matches,
        "raw_shared_frame_duplicate_fails": raw_shared_duplicate_fails,
        "s3_ordered_direct_staged": s3_ordered_direct_staged(),
        "history_trace": sum(actual_matrix[i][i] for i in range(len(actual_matrix))),
        "scalar_left": left,
        "scalar_right": right,
        "scalar_defect": left - right,
    }


def main() -> int:
    facts = independent_facts()
    expected_one = {
        (wp, wv): (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(wp * wv))
        for wp, wv in itertools.product(G, repeat=2)
    }
    checks = (
        ("bounded ladder", facts["vertices"] == 10 and facts["edges"] == 13 and facts["max_degree"] == 3),
        ("product-Haar pushforward", set(facts["pushforward_counts"]) == {8}),
        ("coarsening equivariance", facts["coarsening_equivariant"]),
        ("rail-forest residual quotient", facts["residual_orbit_count"] == 4),
        ("one-cell actual perimeter", facts["one_cell_perimeter"] == expected_one),
        ("two-cell outer perimeter", facts["two_cell_outer"] == (Fraction(0),) * 6 + (Fraction(1),)),
        (
            "connector-deleted characteristic polynomial",
            facts["connector_charpoly"]
            == (
                Fraction(729, 1048576),
                Fraction(-27, 1024),
                Fraction(147, 512),
                Fraction(-1),
                Fraction(1),
            ),
        ),
        ("direct/staged actual history", facts["history_direct_staged"]),
        ("shared-frame physical marginal", facts["physical_shared_direct_staged"] and facts["physical_duplicate_middle_fails"]),
        ("raw shared-frame Haar sum", facts["raw_shared_frame_matches"] and facts["raw_shared_frame_duplicate_fails"]),
        ("nonabelian ordered coarsening", facts["s3_ordered_direct_staged"]),
        ("scalar associator", facts["scalar_defect"] == Fraction(12, 343)),
    )
    failed = 0
    for name, condition in checks:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        failed += int(not ok)
    print(f"TOTAL: PASS={len(checks) - failed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
