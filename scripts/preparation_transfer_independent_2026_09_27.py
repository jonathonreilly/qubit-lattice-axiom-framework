#!/usr/bin/env python3
"""Independent numerical helper for conditional population transfer.

Uses SI-second matrix exponentials and augmented affine QR readout, independently
of the publication runner's closed-form propagation. This checks arithmetic
under supplied Markov/pulse/readout assumptions, not their physical validity.
No optimizer, source data, fitted constants, file reads or audit verdicts.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ()


def propagate(rates_per_us, times_s, initial=(0.0, 0.5, 0.5), swap=False):
    """Return (nt,3) populations; rates order k10,k21,k20, times total seconds.

    swap=True applies an ideal instantaneous 1/2 permutation at half the delay.
    The returned populations precede the final within12 rotation; their sum in
    states 1 and 2 is invariant under any such final unitary.
    """
    rates = np.asarray(rates_per_us, dtype=float)
    times = np.asarray(times_s, dtype=float)
    state = np.asarray(initial, dtype=float)
    if rates.shape != (3,) or not np.all(np.isfinite(rates)) or np.any(rates < 0):
        raise ValueError('three finite nonnegative rates required')
    if times.ndim != 1 or not np.all(np.isfinite(times)) or np.any(times < 0):
        raise ValueError('one-dimensional finite nonnegative times required')
    if (state.shape != (3,) or not np.all(np.isfinite(state))
            or np.any(state < 0) or not np.isclose(state.sum(), 1, rtol=0, atol=1e-12)):
        raise ValueError('normalized nonnegative initial population required')
    if not isinstance(swap, (bool, np.bool_)):
        raise ValueError('swap must be boolean')
    k10, k21, k20 = rates * 1e6
    generator = np.array([[0, k10, k20], [0, -k10, k21], [0, 0, -k21-k20]])
    result = np.empty((times.size, 3))
    for i, t in enumerate(times):
        if swap:
            half = expm(generator * (t / 2))
            mid = half @ state
            result[i] = half @ mid[[0, 2, 1]]
        else:
            result[i] = expm(generator * t) @ state
    return result


def reconstruct(raw_iq):
    """Affine populations for (...,nt,2) IQ; final three samples are refs 0/1/2.

    Returns the same leading/sample shape with last dimension 3, including the
    reference samples. Does not clip or silently discard observations. Caller
    supplies and verifies reference membership; this routine cannot infer it.
    """
    raw = np.asarray(raw_iq, dtype=float)
    if raw.ndim < 2 or raw.shape[-1] != 2 or raw.shape[-2] < 3 or not np.all(np.isfinite(raw)):
        raise ValueError('finite IQ array with at least three reference samples required')
    flat = raw.reshape((-1, raw.shape[-2], 2))
    result = np.empty((len(flat), raw.shape[-2], 3))
    for i, trace in enumerate(flat):
        affine = np.vstack([trace[-3:].T, np.ones(3)])
        if np.linalg.matrix_rank(affine) != 3:
            raise ValueError('reference centroids must be affinely independent')
        q, r = np.linalg.qr(affine)
        result[i] = np.linalg.solve(r, q.T @ np.vstack([trace.T, np.ones(len(trace))])).T
    return result.reshape(raw.shape[:-1] + (3,))


def main():
    # Exact elementary cases exercise units, midpoint swapping and IQ inversion.
    tests = []
    tests.append(np.allclose(propagate([0, 0, 0], [0, 1], [0, 1, 0], True), [0, 0, 1]))
    t = np.array([0, 1e-6, 2e-6])
    decay = np.exp(-t * 1e6)
    tests.append(np.allclose(propagate([1, 0, 0], t, [0, 1, 0]), np.column_stack([1-decay, decay, t*0]), atol=1e-14))
    tests.append(np.allclose(reconstruct(np.array([[0, 0], [1, 0], [0, 1]])), np.eye(3), atol=1e-14))
    print(f'TOTAL: PASS={sum(bool(v) for v in tests)} FAIL={sum(not bool(v) for v in tests)}')
    return 0 if all(tests) else 1


if __name__ == '__main__':
    raise SystemExit(main())
