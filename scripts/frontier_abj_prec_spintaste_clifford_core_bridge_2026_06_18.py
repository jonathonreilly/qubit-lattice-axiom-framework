#!/usr/bin/env python3
"""ABJ P-REC spin/taste Clifford-core bridge.

This runner isolates the algebraic part of the ABJ P-REC blocker:
the canonical blocked free staggered hypercube carries a 4D Clifford
spin factor with a taste-singlet volume-element gamma5. It also checks
the honest boundary: the site-parity epsilon grading is not that
taste-singlet spin gamma5; epsilon is a taste-dressed chirality-like
operator and cannot close physical anomaly chirality by itself.

No audit status is set here.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md"
ABJ_NOTE = (
    ROOT
    / "docs"
    / "ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def bits_from_index(i: int, d: int = 4) -> tuple[int, ...]:
    return tuple((i >> mu) & 1 for mu in range(d))


def index_from_bits(bits: tuple[int, ...] | list[int]) -> int:
    out = 0
    for mu, bit in enumerate(bits):
        out |= (int(bit) & 1) << mu
    return out


BITS4 = [bits_from_index(i) for i in range(16)]


def eta_phase(mu: int, bits: tuple[int, ...]) -> float:
    return -1.0 if (sum(bits[:mu]) % 2) else 1.0


def alpha_matrices() -> list[np.ndarray]:
    """Hypercube flip matrices induced by the canonical staggered phases."""
    alphas: list[np.ndarray] = []
    for mu in range(4):
        mat = np.zeros((16, 16), dtype=complex)
        for col, bits in enumerate(BITS4):
            flipped = list(bits)
            flipped[mu] ^= 1
            row = index_from_bits(flipped)
            mat[row, col] = eta_phase(mu, bits)
        alphas.append(mat)
    return alphas


def generated_clifford_rank(mats: list[np.ndarray]) -> int:
    basis = []
    ident = np.eye(mats[0].shape[0], dtype=complex)
    for mask in range(1 << len(mats)):
        word = ident.copy()
        for mu, mat in enumerate(mats):
            if mask & (1 << mu):
                word = word @ mat
        basis.append(word.reshape(-1))
    svals = np.linalg.svd(np.stack(basis, axis=1), compute_uv=False)
    return int(np.sum(svals > 1e-10))


def generated_basis(mats: list[np.ndarray]) -> np.ndarray:
    cols = []
    ident = np.eye(mats[0].shape[0], dtype=complex)
    for mask in range(1 << len(mats)):
        word = ident.copy()
        for mu, mat in enumerate(mats):
            if mask & (1 << mu):
                word = word @ mat
        cols.append(word.reshape(-1))
    return np.stack(cols, axis=1)


def commutant_basis(mats: list[np.ndarray]) -> list[np.ndarray]:
    """Return a numerical basis for matrices commuting with every alpha_mu."""
    n = mats[0].shape[0]
    ident = np.eye(n, dtype=complex)
    blocks = [np.kron(ident, mat) - np.kron(mat.T, ident) for mat in mats]
    system = np.vstack(blocks)
    _, svals, vh = np.linalg.svd(system)
    rank = int(np.sum(svals > 1e-10))
    null_vectors = vh[rank:].conj()
    return [vec.reshape((n, n), order="F") for vec in null_vectors]


def max_commutator(mat: np.ndarray, basis: list[np.ndarray]) -> float:
    return max(float(np.max(np.abs(mat @ other - other @ mat))) for other in basis)


def projector_rank(proj: np.ndarray) -> int:
    vals = np.linalg.eigvalsh((proj + proj.conj().T) / 2.0)
    return int(np.sum(vals > 0.5))


def main() -> int:
    print("ABJ P-REC spin/taste Clifford-core bridge")
    print("=" * 72)

    alphas = alpha_matrices()
    ident16 = np.eye(16, dtype=complex)

    max_herm = max(float(np.max(np.abs(mat - mat.conj().T))) for mat in alphas)
    max_square = max(float(np.max(np.abs(mat @ mat - ident16))) for mat in alphas)
    max_anti = 0.0
    for mu, a_mu in enumerate(alphas):
        for nu, a_nu in enumerate(alphas):
            target = 2.0 * ident16 if mu == nu else np.zeros((16, 16), dtype=complex)
            max_anti = max(max_anti, float(np.max(np.abs(a_mu @ a_nu + a_nu @ a_mu - target))))
    check(
        "canonical blocked staggered alpha_mu form Cl4",
        max_herm < 1e-13 and max_square < 1e-13 and max_anti < 1e-13,
        f"herm={max_herm:.1e}, square={max_square:.1e}, anti={max_anti:.1e}",
    )

    alg_rank = generated_clifford_rank(alphas)
    comm_basis = commutant_basis(alphas)
    check(
        "generated spin Clifford algebra has rank 16 and taste commutant has dimension 16",
        alg_rank == 16 and len(comm_basis) == 16,
        f"rank={alg_rank}, commutant_dim={len(comm_basis)}",
    )

    gamma5_spin = alphas[0] @ alphas[1] @ alphas[2] @ alphas[3]
    gamma5_anti = max(float(np.max(np.abs(gamma5_spin @ mat + mat @ gamma5_spin))) for mat in alphas)
    gamma5_square = float(np.max(np.abs(gamma5_spin @ gamma5_spin - ident16)))
    gamma5_herm = float(np.max(np.abs(gamma5_spin - gamma5_spin.conj().T)))
    check(
        "spin volume gamma5 squares to I, is Hermitian, and anticommutes with every alpha_mu",
        gamma5_square < 1e-13 and gamma5_herm < 1e-13 and gamma5_anti < 1e-13,
        f"square={gamma5_square:.1e}, herm={gamma5_herm:.1e}, anti={gamma5_anti:.1e}",
    )

    p_plus = (ident16 + gamma5_spin) / 2.0
    p_minus = (ident16 - gamma5_spin) / 2.0
    p_resid = max(
        float(np.max(np.abs(p_plus @ p_plus - p_plus))),
        float(np.max(np.abs(p_minus @ p_minus - p_minus))),
        float(np.max(np.abs(p_plus @ p_minus))),
    )
    check(
        "spin gamma5 gives complementary rank-8 chirality projectors",
        p_resid < 1e-13 and projector_rank(p_plus) == 8 and projector_rank(p_minus) == 8,
        f"projector_resid={p_resid:.1e}, ranks=({projector_rank(p_plus)}, {projector_rank(p_minus)})",
    )

    gamma5_comm = max_commutator(gamma5_spin, comm_basis)
    check(
        "spin gamma5 is taste-singlet: it commutes with the full taste commutant",
        gamma5_comm < 1e-10,
        f"max_commutator_with_commutant={gamma5_comm:.1e}",
    )

    epsilon = np.diag([(-1.0) ** sum(bits) for bits in BITS4]).astype(complex)
    epsilon_square = float(np.max(np.abs(epsilon @ epsilon - ident16)))
    epsilon_anti = max(float(np.max(np.abs(epsilon @ mat + mat @ epsilon))) for mat in alphas)
    check(
        "site-parity epsilon is also an involution anticommuting with alpha_mu",
        epsilon_square < 1e-13 and epsilon_anti < 1e-13,
        f"square={epsilon_square:.1e}, anti={epsilon_anti:.1e}",
    )

    diff_plus = float(np.max(np.abs(epsilon - gamma5_spin)))
    diff_minus = float(np.max(np.abs(epsilon + gamma5_spin)))
    check(
        "epsilon is not plus or minus the taste-singlet spin gamma5",
        diff_plus > 0.5 and diff_minus > 0.5,
        f"max|eps-g5|={diff_plus:.1f}, max|eps+g5|={diff_minus:.1f}",
    )

    basis = generated_basis(alphas)
    coeffs, *_ = np.linalg.lstsq(basis, epsilon.reshape(-1), rcond=None)
    epsilon_spin_resid = float(np.linalg.norm(basis @ coeffs - epsilon.reshape(-1)))
    check(
        "epsilon is not in the generated spin Clifford algebra",
        epsilon_spin_resid > 1.0,
        f"least_squares_residual={epsilon_spin_resid:.3f}",
    )

    epsilon_comm = max_commutator(epsilon, comm_basis)
    check(
        "epsilon is taste-dressed: it fails to commute with the full taste commutant",
        epsilon_comm > 0.25,
        f"max_commutator_with_commutant={epsilon_comm:.3f}",
    )

    check(
        "spin gamma5 and epsilon commute but are independent trace-orthogonal involutions",
        float(np.max(np.abs(gamma5_spin @ epsilon - epsilon @ gamma5_spin))) < 1e-13
        and abs(np.trace(gamma5_spin @ epsilon)) < 1e-13,
        f"tr(g5 eps)={np.trace(gamma5_spin @ epsilon):.1e}",
    )

    note = NOTE.read_text(encoding="utf-8")
    abj = ABJ_NOTE.read_text(encoding="utf-8")
    check(
        "source note states the closed algebraic core and the remaining physical P-REC residual",
        "closed algebraic core" in note
        and "remaining P-REC residual" in note
        and "anomaly-carrying physical chirality" in note,
    )
    check(
        "ABJ bridge points to this P-REC split without claiming full P-REC closure",
        "ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md" in abj
        and "does not close full P-REC" in abj,
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
