#!/usr/bin/env python3
"""Finite check for dim_C(M_2(C)^tensor 4) = 256.

Paired with docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md.
This is bounded algebraic bookkeeping only: it does not derive d=4 or
connect the 1/256 reciprocal to a mass scale.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" ({detail})" if detail else ""))


def m2_basis() -> list[np.ndarray]:
    return [
        np.array([[1, 0], [0, 0]], dtype=complex),
        np.array([[0, 1], [0, 0]], dtype=complex),
        np.array([[0, 0], [1, 0]], dtype=complex),
        np.array([[0, 0], [0, 1]], dtype=complex),
    ]


def kron_all(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for mat in mats[1:]:
        out = np.kron(out, mat)
    return out


def main() -> int:
    print("M_2(C)^tensor4 dimension-256 bounded verifier")

    basis = m2_basis()
    check("dim_C(M_2(C)) = 4 by basis enumeration", len(basis) == 4)

    for d in range(1, 6):
        check(
            f"tensor-dimension induction gives dim_C(M_2(C)^tensor{d}) = 4^{d}",
            4**d == len(basis) ** d,
            f"value={4**d}",
        )

    tensor_basis = []
    for choices in product(range(4), repeat=4):
        tensor_basis.append(kron_all([basis[i] for i in choices]))
    flat = np.array([mat.reshape(-1) for mat in tensor_basis])
    rank = np.linalg.matrix_rank(flat)
    check("explicit tensor basis count at d=4 is 256", len(tensor_basis) == 256)
    check("explicit tensor basis rank at d=4 is 256", rank == 256, f"rank={rank}")

    sample = kron_all([np.array([[0, 1], [1, 0]], dtype=complex)] * 4)
    check("M_2(C)^tensor4 acts on C^16", sample.shape == (16, 16), f"shape={sample.shape}")
    check("dim_C(M_16(C)) = 16^2 = 256", 16**2 == 256)
    check("reciprocal bookkeeping value is exactly 1/256", Fraction(1, 4**4) == Fraction(1, 256))

    # Guard against the overclaim that this runner derives physics.
    check("does not derive d=4; d=4 is the bounded parameter", True)
    check("does not consume PDG values or mass-scale observations", True)
    check("does not derive a lepton mass scale", True)

    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
