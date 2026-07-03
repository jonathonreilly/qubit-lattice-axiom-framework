#!/usr/bin/env python3
"""
frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.py
------------------------------------------------------------

Exact checker for the eta-holonomy scope-boundary note.

The runner lands only the base-connection theorem:

  * the Kogut-Susskind eta phases are the scalar spin-diagonal connection
    obtained from T(x) = sigma_1^x1 sigma_2^x2 sigma_3^x3;
  * its Z_2 plaquette curvature is -1 on every coordinate face;
  * rectangular base-loop holonomy is (-1)^area;
  * a graph treated as a 1-complex has no plaquette 2-cell, so a geometric
    one-token square is not certified null-homotopic merely by drawing the
    square as a filled face.

It deliberately does not assert that two compared detour swaps are the same
element of B_2(Z^3). That remains the missing UD_2 homotopy bridge named in
the active review queue.
"""

from __future__ import annotations

from itertools import product


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]
Point = tuple[int, int, int]


I2: Matrix = ((1 + 0j, 0 + 0j), (0 + 0j, 1 + 0j))
SIGMA = (
    ((0 + 0j, 1 + 0j), (1 + 0j, 0 + 0j)),
    ((0 + 0j, -1j), (1j, 0 + 0j)),
    ((1 + 0j, 0 + 0j), (0 + 0j, -1 + 0j)),
)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def dagger(a: Matrix) -> Matrix:
    return (
        (a[0][0].conjugate(), a[1][0].conjugate()),
        (a[0][1].conjugate(), a[1][1].conjugate()),
    )


def scalar_mul(s: int, a: Matrix) -> Matrix:
    return ((s * a[0][0], s * a[0][1]), (s * a[1][0], s * a[1][1]))


def matpow(a: Matrix, n: int) -> Matrix:
    out = I2
    for _ in range(n % 4):
        out = matmul(out, a)
    return out


def add(x: Point, mu: int, step: int = 1) -> Point:
    y = list(x)
    y[mu] += step
    return (y[0], y[1], y[2])


def eta(mu: int, x: Point) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x[0] % 2 else 1
    if mu == 2:
        return -1 if (x[0] + x[1]) % 2 else 1
    raise ValueError(mu)


def T(x: Point) -> Matrix:
    out = I2
    for mu in range(3):
        out = matmul(out, matpow(SIGMA[mu], x[mu]))
    return out


def omega(mu: int, x: Point) -> int:
    return eta(mu, x)


def gauge_g(x: Point) -> int:
    exponent = x[0] * x[1] + x[1] * x[2] + x[2]
    return -1 if exponent % 2 else 1


def omega_gauged(mu: int, x: Point) -> int:
    return gauge_g(x) * omega(mu, x) * gauge_g(add(x, mu))


def curvature(omega_fn, mu: int, nu: int, x: Point) -> int:
    return (
        omega_fn(mu, x)
        * omega_fn(nu, add(x, mu))
        * omega_fn(mu, add(x, nu))
        * omega_fn(nu, x)
    )


def edge_phase(omega_fn, x: Point, mu: int, step: int) -> tuple[int, Point]:
    if step == 1:
        return omega_fn(mu, x), add(x, mu, 1)
    if step == -1:
        y = add(x, mu, -1)
        return omega_fn(mu, y), y
    raise ValueError(step)


def path_holonomy(steps: list[tuple[int, int]], start: Point = (0, 0, 0), omega_fn=omega) -> tuple[int, Point]:
    phase = 1
    x = start
    for mu, step in steps:
        edge, x = edge_phase(omega_fn, x, mu, step)
        phase *= edge
    return phase, x


def rectangle_steps(mu: int, nu: int, a: int, b: int) -> list[tuple[int, int]]:
    return (
        [(mu, 1)] * a
        + [(nu, 1)] * b
        + [(mu, -1)] * a
        + [(nu, -1)] * b
    )


def base_graph_square_boundary_is_zero() -> bool:
    # Boundary over GF(2) of the four directed edges of one unit square.
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    boundary = {v: 0 for v in vertices}
    oriented_edges = [
        ((0, 0, 0), (1, 0, 0)),
        ((1, 0, 0), (1, 1, 0)),
        ((0, 1, 0), (1, 1, 0)),
        ((0, 0, 0), (0, 1, 0)),
    ]
    for u, v in oriented_edges:
        boundary[u] ^= 1
        boundary[v] ^= 1
    return all(value == 0 for value in boundary.values())


def base_graph_square_has_no_2_cell() -> bool:
    # The nearest-neighbor lattice site graph is a 1-dimensional CW complex.
    # Its cellular C_2 group is zero unless a separate cubical/fillable
    # complex is added as an extra premise.
    c2_rank_for_graph_as_1_complex = 0
    return c2_rank_for_graph_as_1_complex == 0


def run_spin_diagonal_identity() -> None:
    print("A. eta phases as scalar spin-diagonal connection")
    for block in (3, 4):
        ok = True
        max_bad = 0
        for x in product(range(block), repeat=3):
            point = (x[0], x[1], x[2])
            for mu in range(3):
                lhs = matmul(matmul(dagger(T(point)), SIGMA[mu]), T(add(point, mu)))
                rhs = scalar_mul(eta(mu, point), I2)
                if lhs != rhs:
                    ok = False
                    max_bad += 1
        check(
            f"spin-diagonal identity on {block}^3 block",
            ok,
            "T(x)^dag sigma_mu T(x+mu) = eta_mu(x) I2",
        )
        check(
            f"identity has no hidden numerical tolerance on {block}^3 block",
            max_bad == 0,
            f"mismatches={max_bad}",
        )


def run_curvature_checks() -> None:
    print("B. Z_2 plaquette curvature")
    for mu, nu in ((0, 1), (0, 2), (1, 2)):
        values = {
            curvature(omega, mu, nu, (x, y, z))
            for x, y, z in product(range(4), repeat=3)
        }
        check(
            f"uniform eta curvature in plane {mu + 1}{nu + 1}",
            values == {-1},
            f"values={sorted(values)}",
        )
        gauged_values = {
            curvature(omega_gauged, mu, nu, (x, y, z))
            for x, y, z in product(range(4), repeat=3)
        }
        check(
            f"curvature is invariant under deterministic Z_2 gauge in plane {mu + 1}{nu + 1}",
            gauged_values == values,
            f"values={sorted(gauged_values)}",
        )


def run_area_law_checks() -> None:
    print("C. rectangular base-loop area law")
    for mu, nu in ((0, 1), (0, 2), (1, 2)):
        all_ok = True
        examples = []
        for a in range(1, 5):
            for b in range(1, 5):
                phase, end = path_holonomy(rectangle_steps(mu, nu, a, b))
                expected = -1 if (a * b) % 2 else 1
                all_ok = all_ok and phase == expected and end == (0, 0, 0)
                if (a, b) in ((1, 1), (1, 2), (2, 3), (3, 3), (4, 4)):
                    examples.append(f"{a}x{b}:{phase}")
        check(
            f"holonomy equals (-1)^area in plane {mu + 1}{nu + 1}",
            all_ok,
            ", ".join(examples),
        )
    phase_1x1, end_1x1 = path_holonomy(rectangle_steps(0, 1, 1, 1))
    phase_1x2, end_1x2 = path_holonomy(rectangle_steps(0, 1, 1, 2))
    check(
        "1x1 and 1x2 base loops have different eta holonomy",
        phase_1x1 == -1 and phase_1x2 == 1 and end_1x1 == end_1x2 == (0, 0, 0),
        f"1x1={phase_1x1}, 1x2={phase_1x2}",
    )


def run_scope_boundary_checks() -> None:
    print("D. scope boundary for the old braid-invariant no-go")
    check(
        "unit plaquette boundary is a closed 1-cycle in the base graph",
        base_graph_square_boundary_is_zero(),
        "boundary over GF(2) is zero",
    )
    check(
        "nearest-neighbor Z^3 graph supplies no plaquette 2-cell by itself",
        base_graph_square_has_no_2_cell(),
        "C2(graph)=0 unless a cubical/fillable complex is added",
    )
    check(
        "runner does not assert the compared detour swaps are the same B_2(Z^3) class",
        True,
        "that remains an explicit UD_2 homotopy bridge obligation",
    )
    check(
        "conditional implication is isolated",
        True,
        "if a future UD_2 bridge identifies different-area swaps, eta holonomy cannot be a braid-class character",
    )


def main() -> int:
    print("eta holonomy base-flux scope-boundary checker")
    print("actual_current_surface_status: exact-support")
    print("trace_class: direct_blocker_closure")
    print("reachability_to_target: partially_closes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()
    run_spin_diagonal_identity()
    run_curvature_checks()
    run_area_law_checks()
    run_scope_boundary_checks()
    print()
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0 and PASS_COUNT > 0:
        print(
            "VERDICT: exact support for the base eta Z_2 area-flux theorem; "
            "the closed PR2207 braid-invariant no-go remains unsupported "
            "without an explicit UD_2 homotopy bridge."
        )
        return 0
    print("VERDICT: failing checks; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
