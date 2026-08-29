#!/usr/bin/env python3
"""Independent exact projector controls for the adjacent product-vector entry."""

from __future__ import annotations

from fractions import Fraction as F

import sympy as sp


AUDIT_TIMEOUT_SEC = 120


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[tuple[int, int], tuple[int, int]] = {}

    def add(self, item: tuple[int, int]) -> None:
        self.parent.setdefault(item, item)

    def find(self, item: tuple[int, int]) -> tuple[int, int]:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: tuple[int, int], right: tuple[int, int]) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def original_link_open_kernel(orientation: int) -> dict[str, object]:
    """Derive the cross-history 1/27 kernel before any channel projection.

    The five traces are p0*C1 against p1*C0*C1 for orientation 0 and
    p1*C1 against p0*C0*C1 for orientation 1.  Every link except h2 occurs
    exactly twice and is integrated with int R_ab R_cd=d_ac d_bd/3.  The four
    h2 occurrences are deliberately left open.
    """

    if orientation not in (0, 1):
        raise ValueError("orientation must be 0 or 1")
    p0 = (("u0", 1), ("h1", 1), ("v0", -1), ("h0", -1))
    p1 = (("u1", 1), ("h2", 1), ("v1", -1), ("h1", -1))
    c0 = (("u0", 1), ("u1", 1), ("h2", 1), ("v1", -1), ("v0", -1), ("h0", -1))
    c1 = (("u2", 1), ("u3", 1), ("h4", 1), ("v3", -1), ("v2", -1), ("h2", -1))
    loops = (p0, c1, p1, c0, c1) if orientation == 0 else (p1, c1, p0, c0, c1)
    union_find = UnionFind()
    occurrences: dict[str, list[tuple[tuple[int, int], tuple[int, int]]]] = {}
    for loop_index, loop in enumerate(loops):
        indices = tuple((loop_index, position) for position in range(len(loop)))
        for index in indices:
            union_find.add(index)
        for position, (link, direction) in enumerate(loop):
            left = indices[position]
            right = indices[(position + 1) % len(loop)]
            matrix_indices = (left, right) if direction == 1 else (right, left)
            occurrences.setdefault(link, []).append(matrix_indices)

    open_nodes: list[tuple[int, int]] = []
    for link, pair in occurrences.items():
        if link == "h2":
            open_nodes.extend(index for occurrence in pair for index in occurrence)
            continue
        assert len(pair) == 2
        (a, b), (c, d) = pair
        union_find.union(a, c)
        union_find.union(b, d)

    roots = {union_find.find(index) for index in union_find.parent}
    open_roots = {union_find.find(index) for index in open_nodes}
    open_occurrences = tuple(
        tuple(union_find.find(index) for index in occurrence)
        for occurrence in occurrences["h2"]
    )
    same_order_identity = (
        open_occurrences[0] == open_occurrences[3]
        and open_occurrences[1] == open_occurrences[2]
        if orientation == 0 else
        open_occurrences[0] == open_occurrences[2]
        and open_occurrences[1] == open_occurrences[3]
    )
    return {
        "external_links": len(occurrences) - 1,
        "closed_classes": len(roots - open_roots),
        "open_classes": len(open_roots),
        "open_occurrences": open_occurrences,
        "kernel_coefficient": F(3 ** len(roots - open_roots), 3 ** (len(occurrences) - 1)),
        "same_order_identity": (
            same_order_identity
            and open_occurrences[0][0] != open_occurrences[0][1]
            and open_occurrences[1][0] != open_occurrences[1][1]
        ),
    }


def delta(left: int, right: int) -> int:
    return int(left == right)


def pair_index(first: int, second: int) -> int:
    return 3 * first + second


def projectors() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    p0 = sp.zeros(9, 9)
    p1 = sp.zeros(9, 9)
    p2 = sp.zeros(9, 9)
    for a in range(3):
        for c in range(3):
            for e in range(3):
                for g in range(3):
                    row = pair_index(a, c)
                    column = pair_index(e, g)
                    identity = F(delta(a, e) * delta(c, g), 1)
                    swap = F(delta(a, g) * delta(c, e), 1)
                    trace = F(delta(a, c) * delta(e, g), 1)
                    p0[row, column] = sp.Rational(trace.numerator, 3 * trace.denominator)
                    p1[row, column] = sp.Rational((identity - swap).numerator, 2 * (identity - swap).denominator)
                    symmetric = (identity + swap) / 2 - trace / 3
                    p2[row, column] = sp.Rational(symmetric.numerator, symmetric.denominator)
    return p0, p1, p2


def projector_certificate() -> dict[str, object]:
    ps = projectors()
    identity = sp.eye(9)
    open_kernels = tuple(original_link_open_kernel(orientation) for orientation in (0, 1))
    coefficient = open_kernels[0]["kernel_coefficient"]
    return {
        "traces": tuple(int(sp.trace(projector)) for projector in ps),
        "idempotent": all(projector * projector == projector for projector in ps),
        "orthogonal": all(
            ps[left] * ps[right] == sp.zeros(9, 9)
            for left in range(3) for right in range(3) if left != right
        ),
        "complete": sum(ps, sp.zeros(9, 9)) == identity,
        "open_kernel": open_kernels[0],
        "open_kernels": open_kernels,
        "overlaps": tuple(coefficient * int(sp.trace(projector)) for projector in ps),
    }


def response_sum(t, u):
    dimensions = (1, 3, 5)
    multipliers = (sp.Integer(1), t, u)
    total = 0
    for dimension, x_value in zip(dimensions, multipliers):
        first_orientation = (t**6 + t**10) * t**10 * (1 + x_value)
        second_orientation = (t**6 + t**8 * x_value) * x_value * (t**10 + t**8)
        total += dimension * (first_orientation + second_orientation)
    return sp.expand(total)


def closed_sum(t, u):
    first_moment = 1 + 3 * t + 5 * u
    second_moment = 1 + 3 * t**2 + 5 * u**2
    return sp.expand(
        t**14 * first_moment
        + t**16 * (9 + 2 * first_moment + second_moment)
        + t**18 * second_moment
        + t**20 * (9 + first_moment)
    )


def exterior_n1_survivors():
    vector = (1, -1)
    menu = (vector, (1, 1), (0, -1))
    survivors = []
    for left in menu:
        for right in menu:
            parity_match = left[1] == -1 and right[1] == -1
            exclusive_match = left == vector
            scalar_partner = abs(1 - right[0]) == 0 and -right[1] == 1
            if parity_match and exclusive_match and scalar_partner:
                survivors.append((left, right))
    return tuple(survivors)


def fixture() -> dict[str, object]:
    t, u = sp.symbols("t u", positive=True)
    certificate = projector_certificate()
    direct = response_sum(t, u)
    closed = closed_sum(t, u)
    derivative_u = sp.expand(sp.diff(closed, u))
    rational_value = F(
        int(sp.numer(closed.subs({t: sp.Rational(1, 2), u: sp.Rational(1, 4)}))),
        108 * int(sp.denom(closed.subs({t: sp.Rational(1, 2), u: sp.Rational(1, 4)}))),
    )
    return {
        "projectors": certificate,
        "direct": direct,
        "closed": closed,
        "identity_limit": sp.Rational(1, 108) * closed.subs({t: 1, u: 1}),
        "u_derivative": derivative_u,
        "u_is_load_bearing": derivative_u != 0,
        "rational_value": rational_value,
        "action_survivors": exterior_n1_survivors(),
    }


def main() -> int:
    data = fixture()
    checks = (
        ("both original-link orientations have eleven external Haar pairs",
         all(kernel["external_links"] == 11 for kernel in data["projectors"]["open_kernels"])),
        ("both contractions leave eight closed and four open index classes",
         all(kernel["closed_classes"] == 8 and kernel["open_classes"] == 4
             for kernel in data["projectors"]["open_kernels"])),
        ("both open shared-rung kernels are positive I on V tensor V divided by 27",
         all(kernel["kernel_coefficient"] == F(1, 27) and kernel["same_order_identity"]
             for kernel in data["projectors"]["open_kernels"])),
        ("O(3) vector-pair projectors have ranks 1,3,5",
         data["projectors"]["traces"] == (1, 3, 5)),
        ("projectors are complete orthogonal idempotents",
         data["projectors"]["idempotent"]
         and data["projectors"]["orthogonal"]
         and data["projectors"]["complete"]),
        ("channel-resolved Haar overlaps are d_L/27",
         data["projectors"]["overlaps"] == (F(1, 27), F(1, 9), F(5, 27))),
        ("direct history sum equals the closed two-multiplier polynomial",
         data["direct"] == data["closed"]),
        ("identity crossing recovers the spectator one-cell coefficient",
         data["identity_limit"] == sp.Rational(2, 3)),
        ("spin-two multiplier is load-bearing", data["u_is_load_bearing"]),
        ("the explicit exterior action menu leaves only V,V",
         data["action_survivors"] == (((1, -1), (1, -1)),)),
        ("finite t=1/2 u=1/4 fixture is positive",
         data["rational_value"] > 0),
    )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
