"""Independent checks for the I2 referee report.

These checks deliberately do not import the worker scripts.  They test:

1. the exact three-dimensional cell-divergence improvement using rational
   arithmetic;
2. the three-dimensional folding spectrum, making the L^3 band count
   explicit;
3. the exact fine-translation symmetry of the specific C1 two-band matrix;
4. representative loop ratios with a plain midpoint quadrature; and
5. the elementary flat-measure umklapp fractions.
"""

from fractions import Fraction
from itertools import product

import numpy as np


def exact_improvement_3d(L: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return K'_coarse-K_fine/L in all directions, exactly.

    The energy values are arbitrary rationals with compact coarse-cell
    support.  The identity therefore tests the coefficient algebra rather
    than a particular Hamiltonian or trajectory.
    """

    active_cells = list(product(range(-1, 2), repeat=3))
    deltas = list(product(range(L), repeat=3))
    t = {}
    for q, (X, delta) in enumerate(product(active_cells, deltas), start=1):
        t[X, delta] = Fraction((17 * q) % 29 - 14, 31)

    cells = list(product(range(-2, 3), repeat=3))
    T = {X: sum((t.get((X, d), Fraction(0)) for d in deltas), Fraction(0)) for X in cells}
    B = {}
    for X in cells:
        for axis in range(3):
            B[X, axis] = sum(
                (Fraction(d[axis], L) * t.get((X, d), Fraction(0)) for d in deltas),
                Fraction(0),
            )

    Tp = {}
    for X in cells:
        divergence = Fraction(0)
        for axis in range(3):
            Xm = list(X)
            Xm[axis] -= 1
            divergence += B[X, axis] - B.get((tuple(Xm), axis), Fraction(0))
        Tp[X] = T[X] - divergence

    residuals = []
    for axis in range(3):
        Kp = sum((Fraction(X[axis]) * Tp[X] for X in cells), Fraction(0))
        Kfine_over_L = sum(
            (
                Fraction(L * X[axis] + d[axis], L) * value
                for (X, d), value in t.items()
            ),
            Fraction(0),
        )
        residuals.append(Kp - Kfine_over_L)
    return tuple(residuals)


def folding_3d_error(L: int) -> float:
    """Maximum normalized spectral error for an L^3-site cubic supercell."""

    m = 0.7
    sites = list(product(range(L), repeat=3))
    index = {site: j for j, site in enumerate(sites)}
    maximum = 0.0
    sample_ks = (
        np.array([-2.1, -0.7, 0.4]),
        np.array([-np.pi, 0.3, np.pi]),
        np.array([1.9, -2.7, 2.2]),
    )
    for k in sample_ks:
        W = np.eye(L**3, dtype=complex) * (m * m + 6 * L * L)
        for site in sites:
            row = index[site]
            for axis in range(3):
                nxt = list(site)
                phase = 1.0 + 0.0j
                if nxt[axis] == L - 1:
                    nxt[axis] = 0
                    phase = np.exp(1j * k[axis])
                else:
                    nxt[axis] += 1
                col = index[tuple(nxt)]
                W[row, col] += -(L * L) * phase
                W[col, row] += -(L * L) * phase.conjugate()

        observed = np.sort(np.linalg.eigvalsh(W))
        expected = []
        for n in product(range(L), repeat=3):
            K = k + 2 * np.pi * np.asarray(n)
            expected.append(m * m + 4 * L * L * np.sum(np.sin(K / (2 * L)) ** 2))
        expected = np.sort(np.asarray(expected))
        maximum = max(maximum, np.max(np.abs(observed - expected)) / (12 * L * L))
    return maximum


def c1_translation_commutator() -> tuple[float, float]:
    """Check [h,T_f]=0 and T_f^2=e^{-ik} for the C1 matrix form."""

    maximum_commutator = 0.0
    maximum_square = 0.0
    for k in np.linspace(-np.pi, np.pi, 101):
        alpha = 1.1 + 0.07 * np.cos(k) + 0.03 * np.cos(2 * k)
        D0 = 2.3 + 0.2 * np.cos(k)
        Tf = np.array([[0.0, np.exp(-1j * k)], [1.0, 0.0]], dtype=complex)
        h = np.array(
            [
                [D0, (1 + np.exp(-1j * k)) * alpha],
                [(1 + np.exp(1j * k)) * alpha, D0],
            ],
            dtype=complex,
        )
        maximum_commutator = max(maximum_commutator, np.linalg.norm(h @ Tf - Tf @ h, ord=np.inf))
        maximum_square = max(
            maximum_square,
            np.linalg.norm(Tf @ Tf - np.exp(-1j * k) * np.eye(2), ord=np.inf),
        )
    return maximum_commutator, maximum_square


def loop_ratios_midpoint(N: int, G: int = 128) -> tuple[float, float, float]:
    """Independent uniform-grid d=3 check of R_1, R_-1 and abs/N^4."""

    x = -np.pi + (np.arange(G) + 0.5) * (2 * np.pi / G)
    sx = 4 * N * N * np.sin(x / 2) ** 2
    w = np.sqrt(1.0 + sx[:, None, None] + sx[None, :, None] + sx[None, None, :])
    anomaly = np.broadcast_to((np.cos(x) - 1)[:, None, None], w.shape)
    r1 = np.sum(anomaly * w) / np.sum(w)
    rm1 = np.sum(anomaly / w) / np.sum(1 / w)
    # dK/(2pi) = N dx/(2pi); midpoint dx=2pi/G.
    absolute = np.sum(anomaly * w / 2) * (N / G) ** 3 / N**4
    return r1, rm1, absolute


def main() -> None:
    lines = []

    def emit(line: str) -> None:
        print(line)
        lines.append(line)

    emit("Exact 3D improvement (L is refinement per axis; sites/bands per cell = L^3):")
    for L in (2, 3, 4):
        emit(f"  L={L}, bands={L**3}: residuals={exact_improvement_3d(L)}")

    emit("3D folding spectrum:")
    for L in (2, 3):
        emit(f"  L={L}, bands={L**3}: normalized max error={folding_3d_error(L):.3e}")

    comm, square = c1_translation_commutator()
    emit("C1 two-band matrix fine-translation test:")
    emit(f"  max ||[h,T_f]||_inf={comm:.3e}; max ||T_f^2-e^(-ik)I||_inf={square:.3e}")

    emit("Independent d=3 midpoint loop quadrature:")
    for N in (4, 16, 64):
        r1, rm1, absolute = loop_ratios_midpoint(N)
        emit(f"  N={N}: R_1={r1:+.6f}, R_-1={rm1:+.6f}, abs/N^4={absolute:+.6f}")

    emit("Flat four-point umklapp fractions 1-(2/3)^d:")
    for d in (1, 2, 3):
        emit(f"  d={d}: {1 - (2 / 3) ** d:.12f}")

    with open("referee_independent_checks.out", "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
