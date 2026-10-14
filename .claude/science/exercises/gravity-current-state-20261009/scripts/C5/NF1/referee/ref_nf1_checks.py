"""Independent, moderate-grid checks for the NF-1 referee pass.

This implementation does not import the worker's gamma matrices, flow, or
self-energy evaluator.  It imports only the registered scalar box functions
from ``flat/sublum.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "flat"))
from sublum import SymG, SymS  # noqa: E402


BF = 0.909103708
CPH = 2.9435
SLAW = SymS(BF)
GLAW = SymG(CPH)


def gamma_matrices() -> tuple[list[np.ndarray], np.ndarray]:
    bits = [tuple((n >> j) & 1 for j in range(3)) for n in range(8)]
    index = {b: i for i, b in enumerate(bits)}
    shifts = ((0, 0, 0), (1, 0, 0), (1, 1, 0))
    gammas: list[np.ndarray] = []
    for j, shift in enumerate(shifts):
        g = np.zeros((8, 8), complex)
        for n in bits:
            target = tuple((n[a] + shift[a]) % 2 for a in range(3))
            g[index[n], index[target]] = (-1) ** n[j]
        gammas.append(g)
    eps = np.zeros((8, 8), complex)
    for n in bits:
        target = tuple((n[a] + 1) % 2 for a in range(3))
        eps[index[n], index[target]] = 1.0
    return gammas, eps


GAMMA, EPS = gamma_matrices()


def sf_flow(k: np.ndarray, strain: np.ndarray, amplitude: float, steps: int = 8) -> np.ndarray:
    """Time-one RK4 map of dk/du=(amplitude/2) strain.(s s')."""

    y = np.asarray(k, float).copy()

    def rhs(z: np.ndarray) -> np.ndarray:
        p = SLAW.s(z) * SLAW.ds(z)
        return 0.5 * amplitude * (strain @ p)

    du = 1.0 / steps
    for _ in range(steps):
        k1 = rhs(y)
        k2 = rhs(y + 0.5 * du * k1)
        k3 = rhs(y + 0.5 * du * k2)
        k4 = rhs(y + du * k3)
        y += (du / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


def hamiltonian(k: np.ndarray, strain: np.ndarray, amplitude: float) -> np.ndarray:
    flowed = sf_flow(k, strain, amplitude) if amplitude else np.asarray(k, float)
    coeff = SLAW.s(flowed)
    return sum(coeff[j] * GAMMA[j] for j in range(3))


def sigma_direct(n: int, strain: np.ndarray, amplitude: float) -> np.ndarray:
    """Direct full-BZ 8x8 one-loop matrix at external (omega,k)=(0,0).

    The photon is deliberately left unstrained.  This is sufficient to test
    the claimed fermionic symmetry for Eg, T2g, and trace strain, and keeps the
    check independent of the worker's octant/reduced formula.
    """

    grid = -np.pi + (np.arange(n) + 0.5) * (2 * np.pi / n)
    h0 = hamiltonian(np.zeros(3), strain, amplitude)
    total = np.zeros((8, 8), complex)
    for qx in grid:
        for qy in grid:
            for qz in grid:
                q = np.array([qx, qy, qz])
                d = GLAW.h(q)
                omega = float(np.linalg.norm(d))
                corners: dict[tuple[int, int, int], np.ndarray] = {}
                for bx in (0, 1):
                    for by in (0, 1):
                        for bz in (0, 1):
                            corners[(bx, by, bz)] = hamiltonian(
                                q * np.array([bx, by, bz]), strain, amplitude
                            )
                hq = corners[(1, 1, 1)]
                energy = float(np.sqrt(np.trace(hq @ hq).real / 8.0))
                xmat = hq / (energy * 2.0 * omega * (energy + omega))

                # Average the six axis orderings directly.  For a leg in
                # direction j, each subset of the other two axes occurs with
                # multiplicities 2,1,1,2.
                vertices: list[np.ndarray] = []
                for j in range(3):
                    others = [a for a in range(3) if a != j]
                    acc = np.zeros((8, 8), complex)
                    for mask, weight in ((0, 2), (1, 1), (2, 1), (3, 2)):
                        base = [0, 0, 0]
                        for p, axis in enumerate(others):
                            base[axis] = (mask >> p) & 1
                        after = base.copy()
                        after[j] = 1
                        acc += weight * (corners[tuple(after)] - corners[tuple(base)])
                    vertices.append(acc / (6.0 * d[j]))

                exchange = xmat - sum(v @ xmat @ v for v in vertices)
                tadpole = np.zeros((8, 8), complex)
                for j in range(3):
                    qp = np.zeros(3)
                    qm = np.zeros(3)
                    qp[j] = q[j]
                    qm[j] = -q[j]
                    second = (hamiltonian(qp, strain, amplitude)
                              + hamiltonian(qm, strain, amplitude) - 2 * h0)
                    tadpole += second / (2.0 * d[j] ** 2)
                total += exchange + tadpole / (2.0 * omega)
    return total / n**3


def conjugation_constraint_nullity() -> tuple[int, int]:
    """Rank/nullity for EPS M EPS=-M and EPS M EPS=+M on all 64 entries."""

    conjugation = np.kron(EPS.T, EPS)
    eye = np.eye(64)
    stacked = np.vstack((conjugation + eye, conjugation - eye))
    rank = int(np.linalg.matrix_rank(stacked, tol=1e-12))
    return rank, 64 - rank


def arbitrary_link_counterexample(seed: int = 20261013) -> tuple[float, float]:
    """Opposite-sublattice c-number hopping need not be inversion covariant."""

    length = 4
    coords = np.arange(length)
    eps = np.diag((-1.0) ** coords)
    inversion = np.zeros((length, length))
    inversion[np.arange(length), (-coords) % length] = 1.0
    pstag = eps @ inversion
    rng = np.random.default_rng(seed)
    h = np.zeros((length, length), complex)
    for x in range(length):
        for y in range(x + 1, length):
            if (x - y) % 2:
                h[x, y] = rng.normal() + 1j * rng.normal()
                h[y, x] = h[x, y].conjugate()
    theta_error = float(np.linalg.norm(eps @ h @ eps + h))
    inversion_error = float(np.linalg.norm(pstag @ h @ pstag.conj().T - h))
    return theta_error, inversion_error


def main() -> None:
    clifford = max(
        np.max(np.abs(a @ b + b @ a - 2 * (i == j) * np.eye(8)))
        for i, a in enumerate(GAMMA + [EPS])
        for j, b in enumerate(GAMMA + [EPS])
    )
    hprobe = hamiltonian(np.array([0.31, -0.72, 1.17]), np.eye(3), 0.0)
    u1_ratio = np.linalg.norm(EPS @ hprobe - hprobe @ EPS) / np.linalg.norm(hprobe)
    rank, nullity = conjugation_constraint_nullity()
    print(f"Clifford residual: {clifford:.3e}")
    print(f"continuous U(1)_eps commutator ratio: {u1_ratio:.12f}")
    print(f"combined 64-entry constraint: rank={rank}, nullity={nullity}")

    rng = np.random.default_rng(91)
    k = rng.uniform(-np.pi, np.pi, 3)
    generic = np.array([[0.7, -0.2, 0.11], [-0.2, -0.4, 0.09], [0.11, 0.09, 0.3]])
    f = sf_flow(k, generic, 0.23)
    fm = sf_flow(-k, generic, 0.23)
    shift_errors = []
    for j in range(3):
        shifted = sf_flow(k + np.pi * np.eye(3)[j], generic, 0.23)
        shift_errors.append(np.max(np.abs(shifted - f - np.pi * np.eye(3)[j])))
    print(f"generic-flow oddness residual: {np.max(np.abs(fm + f)):.3e}")
    print(f"generic-flow pi-shift residual: {max(shift_errors):.3e}")

    for label, strain in (
        ("Eg", np.diag([1.0, -1.0, 0.0])),
        ("T2g", np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])),
        ("A1", np.eye(3)),
    ):
        sigma = sigma_direct(10, strain, 0.13)
        anti = np.linalg.norm(EPS @ sigma @ EPS + sigma)
        comm = np.linalg.norm(EPS @ sigma @ EPS - sigma)
        print(
            f"direct Sigma {label}: max64={np.max(np.abs(sigma)):.3e}, "
            f"Theta-residual={anti:.3e}, P-residual={comm:.3e}"
        )

    theta_error, inversion_error = arbitrary_link_counterexample()
    print(
        "arbitrary c-number opposite-sublattice hopping: "
        f"Theta residual={theta_error:.3e}, fixed-law P_stag residual={inversion_error:.3e}"
    )


if __name__ == "__main__":
    main()
