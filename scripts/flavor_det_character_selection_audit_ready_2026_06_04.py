"""Finite-patch repair runner for the determinant-character log-det packet.

This runner backs docs/FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04.md.
It verifies the bounded surface now being offered for re-audit:

* determinant is the composition-axis character; trace/power-trace/e_k are not;
* direct-sum additivity alone cannot select determinant, because trace adds too;
* supplied finite Grassmann/Berezin source patches give det(M) by the signed
  permutation formula;
* independent block-diagonal patches multiply, so log|det| adds on the
  real-positive branch;
* the finite positive branch has the usual analytic derivative of log det.

The runner does not claim that Lattice + Quantum + Record force the physical
cross-site Grassmann/CAR frame, and it does not close a coupled KS/Dirac
factorization surface with off-block source couplings.
"""

from __future__ import annotations

import itertools

import numpy as np


rng = np.random.default_rng(19)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def close(lhs: complex, rhs: complex, tol: float = 1e-8) -> bool:
    scale = max(1.0, abs(lhs), abs(rhs))
    return abs(lhs - rhs) <= tol * scale


def gl(n: int) -> np.ndarray:
    while True:
        m = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        if abs(np.linalg.det(m)) > 1e-3:
            return m


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    out = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        n = block.shape[0]
        out[offset : offset + n, offset : offset + n] = block
        offset += n
    return out


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = 0
    for i, left in enumerate(perm):
        for right in perm[i + 1 :]:
            if left > right:
                inversions += 1
    return -1 if inversions % 2 else 1


def berezin_det(matrix: np.ndarray) -> complex:
    """Signed permutation sum for the finite Berezin determinant identity."""
    n = matrix.shape[0]
    total = 0.0 + 0.0j
    for perm in itertools.permutations(range(n)):
        term = permutation_sign(perm)
        for row, col in enumerate(perm):
            term *= matrix[row, col]
        total += term
    return total


def e2(matrix: np.ndarray) -> complex:
    ev = np.linalg.eigvals(matrix)
    return sum(ev[i] * ev[j] for i in range(len(ev)) for j in range(i + 1, len(ev)))


def main() -> int:
    passed: list[bool] = []
    n = 4
    a, s = gl(n), gl(n)

    passed.append(
        check(
            "det is multiplicative under composition: det(A S)=det(A)det(S)",
            close(np.linalg.det(a @ s), np.linalg.det(a) * np.linalg.det(s)),
        )
    )

    passed.append(
        check(
            "tr fails composition-multiplicativity, so tr is excluded on this axis",
            abs(np.trace(a @ s) - np.trace(a) * np.trace(s)) > 1e-3,
        )
    )

    passed.append(
        check(
            "power-trace tr(M^2) fails composition-multiplicativity",
            abs(np.trace((a @ s) @ (a @ s)) - np.trace(a @ a) * np.trace(s @ s))
            > 1e-3,
        )
    )

    passed.append(
        check(
            "elementary symmetric e_2 fails composition-multiplicativity",
            abs(e2(a @ s) - e2(a) * e2(s)) > 1e-3,
        )
    )

    passed.append(
        check(
            "integer powers det^m obey composition-multiplicativity",
            all(
                close(
                    np.linalg.det(a @ s) ** k,
                    (np.linalg.det(a) ** k) * (np.linalg.det(s) ** k),
                    1e-7,
                )
                for k in (-2, -1, 0, 1, 2, 3)
            ),
        )
    )

    f = np.diag([-1, 1, 1, 1]).astype(complex)
    sqrt_lhs = complex(np.linalg.det(f @ f)) ** 0.5
    sqrt_rhs = complex(np.linalg.det(f)) ** 0.5 * complex(np.linalg.det(f)) ** 0.5
    passed.append(
        check(
            "fractional complex branches such as det^(1/2) are not global characters",
            abs(sqrt_lhs - sqrt_rhs) > 1e-6,
            f"sqrt(det(F F))={sqrt_lhs}, sqrt(det F)sqrt(det F)={sqrt_rhs}",
        )
    )

    direct_sum = block_diag(a, s)
    passed.append(
        check(
            "Pattern L: tr is additive over direct sums, so additivity alone cannot select det",
            abs(np.trace(direct_sum) - (np.trace(a) + np.trace(s))) < 1e-9,
        )
    )

    patch1 = np.array([[2.0, 0.4], [0.1, 1.7]], dtype=complex)
    patch2 = np.array(
        [[1.4, 0.2, 0.1], [0.3, 1.8, 0.2], [0.1, 0.4, 1.6]],
        dtype=complex,
    )
    passed.append(
        check(
            "finite Berezin signed-permutation sum gives det(M) on source patch 1",
            close(berezin_det(patch1), np.linalg.det(patch1)),
            f"berezin={berezin_det(patch1):.12g}, det={np.linalg.det(patch1):.12g}",
        )
    )
    passed.append(
        check(
            "finite Berezin signed-permutation sum gives det(M) on source patch 2",
            close(berezin_det(patch2), np.linalg.det(patch2)),
            f"berezin={berezin_det(patch2):.12g}, det={np.linalg.det(patch2):.12g}",
        )
    )

    patch_sum = block_diag(patch1, patch2)
    det1 = np.linalg.det(patch1)
    det2 = np.linalg.det(patch2)
    det_sum = np.linalg.det(patch_sum)
    passed.append(
        check(
            "independent block source patches multiply: det(M1 oplus M2)=det(M1)det(M2)",
            close(det_sum, det1 * det2),
            f"det_sum={det_sum:.12g}, product={det1 * det2:.12g}",
        )
    )

    passed.append(
        check(
            "positive branch log|det| adds, while raw powers remain multiplicative not additive",
            abs(np.log(abs(det_sum)) - (np.log(abs(det1)) + np.log(abs(det2)))) < 1e-10
            and abs(abs(det_sum) ** 2 - (abs(det1) ** 2 + abs(det2) ** 2)) > 1e-3,
        )
    )

    # Analytic regularity check on a real-positive determinant branch.
    m = np.array([[2.4, 0.2], [0.2, 1.9]], dtype=float)
    p = np.array([[0.3, 0.0], [0.0, -0.1]], dtype=float)
    eps = 1e-6
    finite_diff = (
        np.log(np.linalg.det(m + eps * p)) - np.log(np.linalg.det(m - eps * p))
    ) / (2.0 * eps)
    derivative = np.trace(np.linalg.inv(m) @ p)
    passed.append(
        check(
            "real-positive finite branch is regular: d log det(M+tP)=Tr(M^-1 P)",
            abs(finite_diff - derivative) < 1e-8,
            f"finite_diff={finite_diff:.12g}, trace={derivative:.12g}",
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("RE-AUDIT TARGET: supplied finite Grassmann/CAR independent source patches")
    print("give determinant amplitudes, determinant is the composition character,")
    print("and regular positive-branch additive readouts are c*log|det|.")
    print("BOUNDARY: this does not force FS/CAR from the baseline axioms and does")
    print("not factorize a coupled KS/Dirac surface with off-block couplings.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
