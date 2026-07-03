#!/usr/bin/env python3
"""Exact checker for the staggered chirality/parity bridge.

This runner proves the narrow bridge needed by the Kawamoto-Smit rescoping
companion:

  * on the nearest-neighbor Z^3 graph, a scalar sign grading that flips on
    every coordinate edge is unique up to the global sign and is
    epsilon(x) = (-1)^(x1+x2+x3);
  * the A1 Cl(3) pseudoscalar Omega0 = sigma1 sigma2 sigma3 = i I is central,
    so Omega(x) = epsilon(x) Omega0 is the unique normalized local scalar
    chirality field for that edge-flip grading;
  * multiplication by epsilon anticommutes with every nearest-neighbor odd
    kinetic operator, independently of edge weights.

It does not prove the full staggered-Dirac realization gate, Grassmann
statistics, the physical species-label bridge, or any observed value.
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


Point = tuple[int, int, int]
Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]


I2: Matrix = ((1 + 0j, 0 + 0j), (0 + 0j, 1 + 0j))
SIGMA: tuple[Matrix, Matrix, Matrix] = (
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


def scalar_mul(s: complex, a: Matrix) -> Matrix:
    return ((s * a[0][0], s * a[0][1]), (s * a[1][0], s * a[1][1]))


def msub(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] - b[0][0], a[0][1] - b[0][1]),
        (a[1][0] - b[1][0], a[1][1] - b[1][1]),
    )


def max_abs(a: Matrix) -> float:
    return max(abs(a[i][j]) for i in range(2) for j in range(2))


def add(x: Point, mu: int, step: int = 1) -> Point:
    y = list(x)
    y[mu] += step
    return (y[0], y[1], y[2])


def epsilon(x: Point) -> int:
    return -1 if sum(x) % 2 else 1


def gf2_rank(rows: list[int]) -> int:
    rows = rows[:]
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        pbit = pivot.bit_length() - 1
        rank += 1
        new_rows = []
        for row in rows:
            if row == pivot:
                continue
            if (row >> pbit) & 1:
                row ^= pivot
            if row:
                new_rows.append(row)
        rows = new_rows
    return rank


def finite_box_vertices(dims: tuple[int, int, int]) -> list[Point]:
    return [(x, y, z) for x, y, z in product(*(range(d) for d in dims))]


def edge_constraint_rank(dims: tuple[int, int, int]) -> tuple[int, int, bool]:
    vertices = finite_box_vertices(dims)
    index = {v: i for i, v in enumerate(vertices)}
    rows: list[int] = []
    parity_is_solution = True
    for v in vertices:
        for mu, limit in enumerate(dims):
            if v[mu] + 1 >= limit:
                continue
            w = add(v, mu)
            rows.append((1 << index[v]) | (1 << index[w]))
            parity_is_solution = parity_is_solution and epsilon(v) * epsilon(w) == -1
    return len(vertices), gf2_rank(rows), parity_is_solution


def run_graph_parity_uniqueness() -> None:
    print("A. Z^3 nearest-neighbor scalar edge-flip grading")
    for dims in ((2, 2, 2), (2, 3, 4), (4, 4, 3)):
        n_vertices, rank, parity_ok = edge_constraint_rank(dims)
        check(
            f"epsilon solves every edge-flip equation on {dims} open box",
            parity_ok,
            "epsilon(x+e_mu)=-epsilon(x)",
        )
        check(
            f"edge-flip solution space on {dims} box is one global sign",
            rank == n_vertices - 1,
            f"rank={rank}, vertices={n_vertices}, affine_solutions=2",
        )

    square_ok = True
    for x in product(range(3), repeat=3):
        p = (x[0], x[1], x[2])
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            # Four flips around a coordinate square return to the starting sign.
            square_ok = square_ok and (
                epsilon(p)
                * epsilon(add(p, mu))
                * epsilon(add(add(p, mu), nu))
                * epsilon(add(p, nu))
                == 1
            )
    check(
        "coordinate-square consistency gives path-independent parity propagation",
        square_ok,
        "four edge flips around every checked square multiply to +1",
    )


def run_clifford_pseudoscalar_bridge() -> None:
    print("B. A1 central pseudoscalar -> local staggered chirality")
    omega0 = matmul(matmul(SIGMA[0], SIGMA[1]), SIGMA[2])
    check(
        "Pauli pseudoscalar sigma1 sigma2 sigma3 equals i I",
        max_abs(msub(omega0, scalar_mul(1j, I2))) < 1e-12,
    )
    central = True
    for sigma in SIGMA:
        central = central and max_abs(msub(matmul(omega0, sigma), matmul(sigma, omega0))) < 1e-12
    check("A1 pseudoscalar is central in the Pauli Cl(3) realization", central)

    ratio_ok = True
    square_ok = True
    for x in product(range(-2, 3), repeat=3):
        p = (x[0], x[1], x[2])
        omega_x = epsilon(p) * 1j
        square_ok = square_ok and abs(omega_x * omega_x + 1) < 1e-12
        for mu in range(3):
            omega_y = epsilon(add(p, mu)) * 1j
            ratio_ok = ratio_ok and abs(omega_x / omega_y + 1) < 1e-12
    check(
        "Omega(x)=epsilon(x) Omega0 flips by -1 on every coordinate edge",
        ratio_ok,
        "Omega(x)/Omega(x+e_mu)=-1",
    )
    check(
        "local chirality keeps the Cl(3) pseudoscalar square",
        square_ok,
        "Omega(x)^2=-1 for Omega0=iI",
    )


def run_nearest_neighbor_anticommutation() -> None:
    print("C. Anticommutation with every nearest-neighbor odd kinetic stencil")
    dims = (3, 3, 3)
    vertices = finite_box_vertices(dims)
    edge_ok = True
    nonzero_edges = 0
    for v in vertices:
        for mu, limit in enumerate(dims):
            if v[mu] + 1 >= limit:
                continue
            w = add(v, mu)
            # An arbitrary nonzero edge weight c cancels because epsilon flips.
            for c in (1, -3, 2 + 5j):
                edge_ok = edge_ok and epsilon(v) * c + c * epsilon(w) == 0
                edge_ok = edge_ok and epsilon(w) * c + c * epsilon(v) == 0
            nonzero_edges += 1
    check(
        "Gamma_epsilon D + D Gamma_epsilon vanishes edgewise for arbitrary weights",
        edge_ok,
        f"checked {nonzero_edges} undirected nearest-neighbor edges with three weights",
    )

    non_nn_ok = True
    for x in product(range(2), repeat=3):
        p = (x[0], x[1], x[2])
        w = add(p, 0, 2)
        # Same-sublattice two-step hops commute with epsilon, so they are not in
        # the odd first-order nearest-neighbor class.
        non_nn_ok = non_nn_ok and epsilon(p) == epsilon(w)
    check(
        "two-step same-axis hops are correctly excluded from the odd NN class",
        non_nn_ok,
        "epsilon(x+2e_mu)=epsilon(x)",
    )


def main() -> int:
    print("staggered_dirac_chirality_parity_bridge_2026_06_06.py")
    print("actual_current_surface_status: exact-support")
    print("trace_class: direct_blocker_closure")
    print("target_blocker: H_staggered_chirality was a conditional premise")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    run_graph_parity_uniqueness()
    run_clifford_pseudoscalar_bridge()
    run_nearest_neighbor_anticommutation()
    print(f"\nSCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: FAIL")
        return 1
    print(
        "VERDICT: exact support for the narrow H_staggered_chirality bridge; "
        "the full staggered-Dirac realization gate remains outside this scope."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
