#!/usr/bin/env python3
"""Quadratic proper-cubic scalars of one bond correlation, exact and finite.

The carrier is a real 3x3 matrix, not a traceless symmetric block and not a
CHSH score. Invariants are computed by row reduction over the rationals.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 120


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def zeros(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def eye(n: int) -> list[list[Fraction]]:
    out = zeros(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = len(b[0])
    p = len(b)
    out = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if a[i][k] == 0:
                continue
            for j in range(m):
                out[i][j] += a[i][k] * b[k][j]
    return out


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = len(a[0])
    return [[a[r][c] for r in range(n)] for c in range(m)]


def det3(a: list[list[Fraction]]) -> Fraction:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def mat_key(a: list[list[Fraction]]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(row) for row in a)


def conj(g: list[list[Fraction]], t: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(matmul(g, t), transpose(g))


def signed_permutations() -> list[list[list[Fraction]]]:
    out: list[list[list[Fraction]]] = []
    for perm in permutations(range(3)):
        for signs in product((Fraction(-1), Fraction(1)), repeat=3):
            m = zeros(3)
            for i, col in enumerate(perm):
                m[i][col] = signs[i]
            out.append(m)
    return out


def closure(generators: list[list[list[Fraction]]]) -> list[list[list[Fraction]]]:
    found = {mat_key(g): g for g in generators}
    queue = list(found.keys())
    while queue:
        key = queue.pop()
        for gen in generators:
            prod = matmul(found[key], gen)
            pk = mat_key(prod)
            if pk not in found:
                found[pk] = prod
                queue.append(pk)
    return list(found.values())


PAIRS: list[tuple[int, int]] = [(a, b) for a in range(9) for b in range(a, 9)]
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


def add_term(poly: dict[tuple[int, int], Fraction], a: int, b: int, coeff: Fraction) -> None:
    if coeff == 0:
        return
    if a > b:
        a, b = b, a
    key = (a, b)
    poly[key] = poly.get(key, Fraction(0)) + coeff
    if poly[key] == 0:
        del poly[key]


def square_of_linear(coeffs: list[Fraction]) -> dict[tuple[int, int], Fraction]:
    poly: dict[tuple[int, int], Fraction] = {}
    for i, ci in enumerate(coeffs):
        if ci == 0:
            continue
        for j, cj in enumerate(coeffs):
            if cj == 0:
                continue
            add_term(poly, i, j, ci * cj)
    return poly


def add_poly(
    lhs: dict[tuple[int, int], Fraction],
    rhs: dict[tuple[int, int], Fraction],
    scale: Fraction = Fraction(1),
) -> None:
    for key, coeff in rhs.items():
        add_term(lhs, key[0], key[1], scale * coeff)


def entry_map(g: list[list[Fraction]]) -> list[tuple[Fraction, int]]:
    images: list[tuple[Fraction, int]] = [(Fraction(0), -1) for _ in range(9)]
    for src in range(9):
        basis = zeros(3)
        basis[src // 3][src % 3] = Fraction(1)
        image = conj(g, basis)
        nz = [
            (image[i][j], i * 3 + j)
            for i in range(3)
            for j in range(3)
            if image[i][j] != 0
        ]
        if len(nz) != 1 or nz[0][0] not in (Fraction(-1), Fraction(1)):
            raise RuntimeError(f"conjugation is not a signed permutation at {src}")
        images[src] = nz[0]
    return images


def apply_poly(
    poly: dict[tuple[int, int], Fraction],
    images: list[tuple[Fraction, int]],
) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for (a, b), coeff in poly.items():
        sa, na = images[a]
        sb, nb = images[b]
        add_term(out, na, nb, coeff * sa * sb)
    return out


def poly_vector(poly: dict[tuple[int, int], Fraction]) -> list[Fraction]:
    vec = [Fraction(0) for _ in PAIRS]
    for key, coeff in poly.items():
        vec[PAIR_INDEX[key]] = coeff
    return vec


def nullspace(equations: list[list[Fraction]]) -> list[list[Fraction]]:
    if not equations:
        return []
    n = len(equations[0])
    a = [row[:] for row in equations]
    m = len(a)
    row = 0
    pivots: list[int] = []
    for col in range(n):
        sel = None
        for i in range(row, m):
            if a[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        a[row], a[sel] = a[sel], a[row]
        pivot = a[row][col]
        a[row] = [value / pivot for value in a[row]]
        for i in range(m):
            if i == row or a[i][col] == 0:
                continue
            factor = a[i][col]
            a[i] = [a[i][j] - factor * a[row][j] for j in range(n)]
        pivots.append(col)
        row += 1
    pivot_row = {col: i for i, col in enumerate(pivots)}
    basis: list[list[Fraction]] = []
    for free in range(n):
        if free in pivot_row:
            continue
        vec = [Fraction(0) for _ in range(n)]
        vec[free] = Fraction(1)
        for col, prow in pivot_row.items():
            vec[col] = -a[prow][free]
        basis.append(vec)
    return basis


def invariant_equations(
    group: list[list[list[Fraction]]],
) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    width = len(PAIRS)
    for g in group:
        images = entry_map(g)
        for index, (left, right) in enumerate(PAIRS):
            image = apply_poly({(left, right): Fraction(1)}, images)
            row = poly_vector(image)
            row[index] -= 1
            if any(value != 0 for value in row):
                rows.append(row)
            if len(row) != width:
                raise RuntimeError("bad equation width")
    return rows


def eval_poly(poly: dict[tuple[int, int], Fraction], values: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for (a, b), coeff in poly.items():
        total += coeff * values[a] * values[b]
    return total


def matrix_values(t: list[list[Fraction]]) -> list[Fraction]:
    return [t[i][j] for i in range(3) for j in range(3)]


def channels() -> dict[str, dict[tuple[int, int], Fraction]]:
    tr = [Fraction(0) for _ in range(9)]
    tr[0] = tr[4] = tr[8] = Fraction(1)
    q_tr = square_of_linear(tr)
    q_e: dict[tuple[int, int], Fraction] = {}
    for slot in (0, 4, 8):
        form = [-tr[i] for i in range(9)]
        form[slot] += 3
        add_poly(q_e, square_of_linear(form))
    q_t2: dict[tuple[int, int], Fraction] = {}
    q_a: dict[tuple[int, int], Fraction] = {}
    for left, right in ((1, 3), (2, 6), (5, 7)):
        sym = [Fraction(0) for _ in range(9)]
        sym[left] = Fraction(1)
        sym[right] = Fraction(1)
        anti = [Fraction(0) for _ in range(9)]
        anti[left] = Fraction(1)
        anti[right] = Fraction(-1)
        add_poly(q_t2, square_of_linear(sym))
        add_poly(q_a, square_of_linear(anti))
    return {
        "trace": q_tr,
        "traceless-diagonal": q_e,
        "symmetric-off-diagonal": q_t2,
        "antisymmetric": q_a,
    }


def substitute(
    poly: dict[tuple[int, int], Fraction],
    forms: list[dict[int, Fraction]],
) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for (a, b), coeff in poly.items():
        for i, ci in forms[a].items():
            for j, cj in forms[b].items():
                add_term(out, i, j, coeff * ci * cj)
    return out


def directed_forms() -> list[dict[int, Fraction]]:
    # variables: 0 = u, 1 = t, 2 = v
    forms: list[dict[int, Fraction]] = [{} for _ in range(9)]
    forms[0] = {0: Fraction(1)}
    forms[1] = {1: Fraction(-1)}
    forms[3] = {1: Fraction(1)}
    forms[4] = {0: Fraction(1)}
    forms[8] = {2: Fraction(1)}
    return forms


def monom(i: int, j: int, coeff: Fraction) -> dict[tuple[int, int], Fraction]:
    poly: dict[tuple[int, int], Fraction] = {}
    add_term(poly, i, j, coeff)
    return poly


def main() -> int:
    checks = Checks()
    rz = [
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    rx = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(1), Fraction(0)],
    ]
    improper = eye(3)
    improper[1][1] = Fraction(-1)
    group = closure([rz, rx, eye(3)])
    every = signed_permutations()
    proper = [m for m in every if det3(m) == 1]
    full_keys = {mat_key(m) for m in every}
    proper_keys = {mat_key(m) for m in proper}
    group_keys = {mat_key(m) for m in group}

    checks.check("generated closure has order 24", len(group) == 24)
    checks.check("closure equals the determinant-+1 signed permutations", group_keys == proper_keys)
    checks.check("all signed permutations have order 48", len(every) == 48 and len(full_keys) == 48)
    checks.check("both generators lie in the closure", mat_key(rz) in group_keys and mat_key(rx) in group_keys)
    checks.check("diag(1,-1,1) has determinant -1 and is outside the closure", det3(improper) == -1 and mat_key(improper) not in group_keys)

    linear_rows: list[list[Fraction]] = []
    for g in group:
        images = entry_map(g)
        for src in range(9):
            sign, dest = images[src]
            row = [Fraction(0) for _ in range(9)]
            row[src] -= 1
            row[dest] += sign
            if any(value != 0 for value in row):
                linear_rows.append(row)
    linear_basis = nullspace(linear_rows)
    checks.check("linear invariant dimension is 1", len(linear_basis) == 1)
    if linear_basis:
        scale = linear_basis[0][0]
        checks.check(
            "the linear invariant is the trace",
            scale != 0 and linear_basis[0] == [scale if i in (0, 4, 8) else Fraction(0) for i in range(9)],
        )
    else:
        checks.check("the linear invariant is the trace", False)

    quad = channels()
    names = ("trace", "traceless-diagonal", "symmetric-off-diagonal", "antisymmetric")
    for name in names:
        invariant = all(apply_poly(quad[name], entry_map(g)) == quad[name] for g in every)
        checks.check(f"{name} channel is invariant under all 48 signed permutations", invariant)

    samples = {
        "trace": matrix_values(eye(3)),
        "traceless-diagonal": matrix_values(
            [
                [Fraction(1), Fraction(0), Fraction(0)],
                [Fraction(0), Fraction(-1), Fraction(0)],
                [Fraction(0), Fraction(0), Fraction(0)],
            ]
        ),
        "symmetric-off-diagonal": matrix_values(
            [
                [Fraction(0), Fraction(1), Fraction(0)],
                [Fraction(1), Fraction(0), Fraction(0)],
                [Fraction(0), Fraction(0), Fraction(0)],
            ]
        ),
        "antisymmetric": matrix_values(
            [
                [Fraction(0), Fraction(1), Fraction(0)],
                [Fraction(-1), Fraction(0), Fraction(0)],
                [Fraction(0), Fraction(0), Fraction(0)],
            ]
        ),
    }
    expected = {
        "trace": {"trace": Fraction(9), "traceless-diagonal": Fraction(0), "symmetric-off-diagonal": Fraction(0), "antisymmetric": Fraction(0)},
        "traceless-diagonal": {"trace": Fraction(0), "traceless-diagonal": Fraction(18), "symmetric-off-diagonal": Fraction(0), "antisymmetric": Fraction(0)},
        "symmetric-off-diagonal": {"trace": Fraction(0), "traceless-diagonal": Fraction(0), "symmetric-off-diagonal": Fraction(4), "antisymmetric": Fraction(0)},
        "antisymmetric": {"trace": Fraction(0), "traceless-diagonal": Fraction(0), "symmetric-off-diagonal": Fraction(0), "antisymmetric": Fraction(4)},
    }
    for sample_name, values in samples.items():
        for channel_name in names:
            checks.check(
                f"sample {sample_name} on channel {channel_name}",
                eval_poly(quad[channel_name], values) == expected[sample_name][channel_name],
            )

    diagonal_square = square_of_linear([Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)])
    checks.check(
        "T_xx squared is not a cubic invariant",
        apply_poly(diagonal_square, entry_map(rz)) != diagonal_square,
    )

    proper_dim = len(nullspace(invariant_equations(group)))
    full_dim = len(nullspace(invariant_equations(every)))
    checks.check("proper-cubic quadratic invariant dimension is 4", proper_dim == 4)
    checks.check("full signed-permutation quadratic invariant dimension is 4", full_dim == 4)

    rotation = [
        [Fraction(3, 5), Fraction(-4, 5), Fraction(0)],
        [Fraction(4, 5), Fraction(3, 5), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    checks.check("the 3-4-5 matrix is a rotation", det3(rotation) == 1 and matmul(rotation, transpose(rotation)) == eye(3))
    checks.check(
        "the 3-4-5 matrix is not a signed permutation",
        any(entry not in (Fraction(-1), Fraction(0), Fraction(1)) for row in rotation for entry in row),
    )
    seed = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    moved = conj(rotation, seed)
    q_e_seed = eval_poly(quad["traceless-diagonal"], matrix_values(seed))
    q_t_seed = eval_poly(quad["symmetric-off-diagonal"], matrix_values(seed))
    q_e_moved = eval_poly(quad["traceless-diagonal"], matrix_values(moved))
    q_t_moved = eval_poly(quad["symmetric-off-diagonal"], matrix_values(moved))
    hand_moved = [
        [Fraction(-7, 25), Fraction(24, 25), Fraction(0)],
        [Fraction(24, 25), Fraction(7, 25), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    checks.check("rotated diagonal matrix equals the hand product", moved == hand_moved)
    checks.check("traceless-diagonal square moves under the 3-4-5 rotation", q_e_seed == 18 and q_e_moved == Fraction(882, 625))
    checks.check("symmetric-off-diagonal square moves under the 3-4-5 rotation", q_t_seed == 0 and q_t_moved == Fraction(2304, 625))
    ratio = (q_e_seed - q_e_moved) / q_t_moved
    checks.check("the rotation forces beta/alpha = 9/2", ratio == Fraction(9, 2))
    def frobenius(values: list[Fraction]) -> Fraction:
        return eval_poly(quad["traceless-diagonal"], values) / 9 + eval_poly(quad["symmetric-off-diagonal"], values) / 2
    checks.check(
        "the Frobenius ratio agrees on the rotated pair and equals 2",
        frobenius(matrix_values(seed)) == 2 and frobenius(matrix_values(moved)) == 2,
    )

    forms = directed_forms()
    restricted = {name: substitute(quad[name], forms) for name in names}
    checks.check("directed trace channel is (2u+v)^2", restricted["trace"] == add_merge(monom(0, 0, 4), monom(2, 2, 1), monom(0, 2, 4)))
    checks.check("directed traceless-diagonal channel is 6(u-v)^2", restricted["traceless-diagonal"] == add_merge(monom(0, 0, 6), monom(2, 2, 6), monom(0, 2, -12)))
    checks.check("directed symmetric-off-diagonal channel is identically zero", restricted["symmetric-off-diagonal"] == {})
    checks.check("directed antisymmetric channel is 4 t^2", restricted["antisymmetric"] == monom(1, 1, 4))
    flipped = [dict(form) for form in forms]
    flipped[1] = {1: Fraction(1)}
    flipped[3] = {1: Fraction(-1)}
    flipped_values = {name: substitute(quad[name], flipped) for name in names}
    checks.check("every basis channel is even under t to -t", flipped_values == restricted)

    pure = [Fraction(0), Fraction(-1), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1)]
    pure_minus = [Fraction(0), Fraction(1), Fraction(0), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1)]
    pure_values = {name: eval_poly(quad[name], pure) for name in names}
    checks.check(
        "the two pure twists give the same four channel values",
        pure_values == {name: eval_poly(quad[name], pure_minus) for name in names}
        and pure_values == {
            "trace": Fraction(1),
            "traceless-diagonal": Fraction(6),
            "symmetric-off-diagonal": Fraction(0),
            "antisymmetric": Fraction(4),
        },
    )
    shear = samples["symmetric-off-diagonal"]
    checks.check(
        "the symmetric-off-diagonal coefficient is visible off the directed pattern",
        eval_poly(quad["symmetric-off-diagonal"], shear) == 4 and eval_poly(quad["symmetric-off-diagonal"], pure) == 0,
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


def add_merge(*polys: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for poly in polys:
        add_poly(out, poly)
    return out


if __name__ == "__main__":
    raise SystemExit(main())
