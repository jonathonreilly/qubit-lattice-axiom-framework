"""Independent finite-dimensional algebra checks for TW-2."""

from __future__ import annotations

import math
import os

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
G4 = np.load(os.path.join(HERE, "scripts", "nf1_gammas.npy"))
MASS_OPS = np.load(os.path.join(HERE, "scripts", "tw2_mass_ops.npy"))
GAMMA, GEPS = G4[:3], G4[3]
I8 = np.eye(8)
BITS = [tuple((i >> j) & 1 for j in range(3)) for i in range(8)]


def index(bit):
    return bit[0] + 2 * bit[1] + 4 * bit[2]


def folding_permutation(bit):
    out = np.zeros((8, 8))
    for source in BITS:
        target = tuple(a ^ b for a, b in zip(source, bit))
        out[index(source), index(target)] = 1
    return out


def nullity_for_class(label):
    """Complex nullity using column-major vec identities, separate from worker code."""
    constraints = []
    for shift in BITS:
        p = folding_permutation(shift)
        sign = (-1) ** sum(a * b for a, b in zip(label, shift))
        constraints.append(np.kron(p.T, p) - sign * np.eye(64))
    for gamma in GAMMA:
        constraints.append(np.kron(I8, gamma) + np.kron(gamma.T, I8))
    constraints.append(np.kron(I8, GEPS) - np.kron(GEPS.T, I8))
    matrix = np.vstack(constraints)
    singular = np.linalg.svd(matrix, compute_uv=False)
    return 64 - int(np.sum(singular > 1e-9))


def representation_checks():
    # Basis (O23,O31,O12), read directly as the three coordinate axes.
    c4z = np.array(((0, -1, 0), (1, 0, 0), (0, 0, 1)), float)
    c2x = np.diag((1.0, -1.0, -1.0))
    c2edge = np.array(((0, 1, 0), (1, 0, 0), (0, 0, -1)), float)
    c3body = np.array(((0, 0, -1), (1, 0, 0), (0, -1, 0)), float)
    reps = (c4z, c2x, c2edge, c3body)
    stacked = np.vstack([rep - np.eye(3) for rep in reps])
    invariant_nullity = 3 - np.linalg.matrix_rank(stacked, tol=1e-12)
    chars = tuple(np.trace(rep) for rep in reps)
    return chars, invariant_nullity, tuple(np.linalg.det(rep) for rep in reps)


def main():
    dims = {"".join(map(str, label)): nullity_for_class(label) for label in BITS}
    print("mass-family complex nullities by folding class:", dims)
    print("nearest-neighbour nullities:", {key: dims[key] for key in ("100", "010", "001")})
    m110 = MASS_OPS[0]
    taste = GEPS @ m110
    pplus = (I8 + taste) / 2
    pminus = (I8 - taste) / 2
    print(
        "block projectors ranks=%d,%d idempotence=%.3e orthogonality=%.3e"
        % (
            round(np.trace(pplus).real),
            round(np.trace(pminus).real),
            max(np.max(np.abs(pplus @ pplus - pplus)), np.max(np.abs(pminus @ pminus - pminus))),
            np.max(np.abs(pplus @ pminus)),
        )
    )
    print(
        "projector commutators max: kinetic=%.3e singlet-mass=%.3e split-mass=%.3e"
        % (
            max(np.max(np.abs(pplus @ gamma - gamma @ pplus)) for gamma in GAMMA),
            np.max(np.abs(pplus @ GEPS - GEPS @ pplus)),
            np.max(np.abs(pplus @ m110 - m110 @ pplus)),
        )
    )
    fold_error = 0.0
    for shift in BITS:
        p = folding_permutation(shift)
        sign = (-1) ** (shift[0] + shift[1])
        fold_error = max(fold_error, np.max(np.abs(p @ m110 @ p - sign * m110)))
    print("M110 folding-character error=%.3e" % fold_error)
    chars, invdim, dets = representation_checks()
    print("triplet characters (C4axis,C2axis,C2edge,C3body)=%s determinants=%s" % (chars, dets))
    print("common invariant-vector dimension=%d (T1 vector triplet has none)" % invdim)
    me, mmu, planck = 0.000511, 0.10566, 1.22089e19
    realistic_lambda = (mmu - me) / (2 * planck)
    print("Hamming tree gap is 2*lambda/a; e-mu calibration would give lambda=%.6e, whereas lambda=0.1 is a supplied grid-scale sample" % realistic_lambda)


if __name__ == "__main__":
    main()
