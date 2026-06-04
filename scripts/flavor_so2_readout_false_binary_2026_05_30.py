#!/usr/bin/env python3
"""Finite determinant/readout algebra for the SO(2) flavor scope repair.

The runner checks only the bounded S1-S4 algebra:

* the continuous rephase C -> exp(i alpha) C is compatible with C^3=I only
  at cube-root phases;
* delta moves the supplied circulant spectrum but leaves the Koide trace ratio
  invariant;
* real determinant and singlet/doublet block-counting products differ on
  alpha P_s + beta P_d;
* the degeneracy locus is delta=m*pi/3.

It deliberately does not claim an exhaustive theorem over all admissible
readout/measure normalizations, nor that either counting is selected or
unselected by the framework.
"""

import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    c = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    i3 = np.eye(3, dtype=complex)
    j = np.ones((3, 3), dtype=complex)
    ps = j / 3.0
    pd = i3 - ps
    a = 1.0
    bmag = np.sqrt(0.5)
    passed = []

    allowed = [0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0]
    allowed_ok = all(np.allclose(np.linalg.matrix_power(np.exp(1j * t) * c, 3), i3) for t in allowed)
    generic_fails = not np.allclose(np.linalg.matrix_power(np.exp(0.4j) * c, 3), i3)
    passed.append(check(
        "S1 continuous C rephase obstruction: C->exp(i alpha)C preserves C^3=I only at cube-root phases",
        allowed_ok and generic_fails,
        "this checks the finite C3 obstruction; it is not a global readout-selector theorem",
    ))

    def lam(delta):
        return np.array([a + 2 * bmag * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)])

    def q(delta):
        values = lam(delta)
        return np.sum(values ** 2) / (np.sum(values) ** 2)

    spec_dep = not np.allclose(np.sort(lam(0.3)), np.sort(lam(1.1)))
    q_blind = abs(q(0.3) - q(1.1)) < 1e-12
    passed.append(check(
        "S2 delta moves the spectrum but is blind in Q for the supplied circulant family",
        spec_dep and q_blind,
        f"Q(delta)={q(0.3):.5f}; sorted spectra at delta=0.3 and 1.1 differ",
    ))

    alpha = 2.0
    beta = 5.0
    op = alpha * ps + beta * pd
    det_r = np.linalg.det(op).real
    block_count_product = alpha * beta
    passed.append(check(
        "S3 real determinant and stipulated singlet/doublet block-counting product differ",
        abs(det_r - alpha * beta ** 2) < 1e-9 and abs(block_count_product - alpha * beta) < 1e-12,
        f"det_R={det_r:.1f}=alpha beta^2; block product={block_count_product:.1f}=alpha beta",
    ))

    degen = all(np.min(np.abs(np.diff(np.sort(lam(m * np.pi / 3.0))))) < 1e-9 for m in range(6))
    nondegen = np.min(np.abs(np.diff(np.sort(lam(0.7))))) > 1e-6
    passed.append(check(
        "S4 full degeneracy occurs at every delta=m*pi/3, not only sin(delta)=0",
        degen and nondegen,
        "nondegeneracy in this family is delta not a multiple of pi/3",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: BOUNDED-SUPPORT finite algebra only. The runner verifies the C3 rephase obstruction,")
    print("delta-blind Q for the supplied circulant family, the det_R versus block-product counting")
    print("formulas, and the delta=m*pi/3 degeneracy locus. It does not prove an exhaustive")
    print("readout-normalization theorem or decide which counting a framework rule selects.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
