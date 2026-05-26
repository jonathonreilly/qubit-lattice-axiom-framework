#!/usr/bin/env python3
"""Finite record-writing isometry certificate for Kraus instrument structure."""

from __future__ import annotations

import numpy as np


SEED = 20260526
SYSTEM_DIM = 4
RECORD_COUNT = 3
SAMPLES = 8
TOL = 1e-11


def _random_isometry(rows: int, cols: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(rows, cols)) + 1j * rng.normal(size=(rows, cols))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r) / np.maximum(np.abs(np.diag(r)), 1e-30)
    return q[:, :cols] * phases.conj()


def _kraus_blocks(isometry: np.ndarray) -> list[np.ndarray]:
    return [
        isometry[r * SYSTEM_DIM : (r + 1) * SYSTEM_DIM, :]
        for r in range(RECORD_COUNT)
    ]


def _random_density(rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(SYSTEM_DIM, SYSTEM_DIM)) + 1j * rng.normal(size=(SYSTEM_DIM, SYSTEM_DIM))
    rho = raw @ raw.conj().T
    return rho / np.trace(rho)


def _apply_channel(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conj().T for k in kraus)


def _choi_matrix(kraus: list[np.ndarray]) -> np.ndarray:
    blocks = []
    basis = []
    for i in range(SYSTEM_DIM):
        for j in range(SYSTEM_DIM):
            eij = np.zeros((SYSTEM_DIM, SYSTEM_DIM), dtype=complex)
            eij[i, j] = 1.0
            basis.append(_apply_channel(kraus, eij))
    for i in range(SYSTEM_DIM):
        row = []
        for j in range(SYSTEM_DIM):
            row.append(basis[i * SYSTEM_DIM + j])
        blocks.append(row)
    return np.block(blocks)


def main() -> None:
    rng = np.random.default_rng(SEED)
    isometry = _random_isometry(RECORD_COUNT * SYSTEM_DIM, SYSTEM_DIM, rng)
    kraus = _kraus_blocks(isometry)

    identity = np.eye(SYSTEM_DIM, dtype=complex)
    resolution = sum(k.conj().T @ k for k in kraus)
    resolution_error = np.linalg.norm(resolution - identity)
    isometry_error = np.linalg.norm(isometry.conj().T @ isometry - identity)
    assert resolution_error < TOL, resolution_error
    assert isometry_error < TOL, isometry_error
    print(f"isometry_error={isometry_error:.3e}")
    print(f"kraus_resolution_error={resolution_error:.3e}")

    choi = _choi_matrix(kraus)
    choi_eigs = np.linalg.eigvalsh(0.5 * (choi + choi.conj().T))
    assert float(np.min(choi_eigs)) > -TOL, float(np.min(choi_eigs))
    print(f"choi_min_eigenvalue={float(np.min(choi_eigs)):.3e}")

    for sample in range(SAMPLES):
        rho = _random_density(rng)
        probs = np.array([np.real(np.trace(k @ rho @ k.conj().T)) for k in kraus])
        channel_rho = _apply_channel(kraus, rho)
        trace_error = abs(np.trace(channel_rho) - 1.0)
        min_eig = float(np.min(np.linalg.eigvalsh(0.5 * (channel_rho + channel_rho.conj().T))))
        prob_sum_error = abs(float(np.sum(probs)) - 1.0)
        assert trace_error < TOL, (sample, trace_error)
        assert prob_sum_error < TOL, (sample, prob_sum_error)
        assert min_eig > -TOL, (sample, min_eig)
        for outcome, (k, p) in enumerate(zip(kraus, probs)):
            if p > 1e-14:
                selective = k @ rho @ k.conj().T / p
                selective_trace_error = abs(np.trace(selective) - 1.0)
                selective_min_eig = float(
                    np.min(np.linalg.eigvalsh(0.5 * (selective + selective.conj().T)))
                )
                assert selective_trace_error < TOL, (sample, outcome, selective_trace_error)
                assert selective_min_eig > -TOL, (sample, outcome, selective_min_eig)
        print(
            f"sample={sample} prob_sum_error={prob_sum_error:.3e} "
            f"trace_error={trace_error:.3e} channel_min_eig={min_eig:.3e}"
        )

    print("CERTIFICATE PASS: normalized finite record-writing map defines a Kraus CPTP instrument")


if __name__ == "__main__":
    main()
