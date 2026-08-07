#!/usr/bin/env python3
"""
Universal-Yukawa no-go for the leptogenesis CP kernel.

Question:
  If the Dirac neutrino Yukawa really remains the exact universal matrix
  Y = y_0 I, can the fixed Majorana Z_3 texture plus unitary basis rotations
  alone produce a nonzero leptogenesis asymmetry?

Answer:
  No. For any unitary left/right basis changes U_L, U_R,

      Y' = U_L^dag (y_0 I) U_R

  still satisfies

      H' = Y'^dag Y' = y_0^2 I.

  So every off-diagonal entry H'_{1j} vanishes and therefore
  Im[(H'_{1j})^2] = 0. The standard CP-asymmetry tensor is identically zero.

Boundary:
  This does not rule out leptogenesis in principle. It proves that the current
  exact universal-Yukawa bridge is not enough by itself; a non-universal Dirac
  flavor texture or equivalent extra structure is still required.
"""

from __future__ import annotations

import math
import sys

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def z3_bridge() -> np.ndarray:
    omega = np.exp(2j * np.pi / 3.0)
    return (1.0 / np.sqrt(3.0)) * np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, omega, omega * omega],
            [1.0, omega * omega, omega],
        ],
        dtype=complex,
    )


def majorana_doublet_rotation() -> np.ndarray:
    """Diagonalizes the 2x2 Z3 doublet block by a real orthogonal rotation."""
    return np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
            [0.0, -1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
        ],
        dtype=complex,
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS: UNIVERSAL-YUKAWA NO-GO")
    print("=" * 88)
    print()
    print("Authority stack:")
    print("  - docs/DM_NEUTRINO_SCHUR_SUPPRESSION_THEOREM_NOTE_2026-04-15.md")
    print("  - docs/DM_Z3_TEXTURE_FACTOR_THEOREM_NOTE_2026-04-15.md")
    print()
    print("Question:")
    print("  Can the exact universal Dirac bridge Y = y_0 I produce leptogenesis")
    print("  after only unitary basis changes on the fixed Z_3 Majorana texture?")

    y0 = 0.006662640625
    y_universal = y0 * np.eye(3, dtype=complex)
    uz3 = z3_bridge()
    ur = majorana_doublet_rotation()

    # Two representative unitary basis changes:
    # 1. left flavor/site <-> Z3 bridge
    # 2. right-handed Majorana mass diagonalization in the doublet block
    y_prime = uz3.conj().T @ y_universal @ ur
    h_prime = y_prime.conj().T @ y_prime

    # Also verify the basis-independent statement directly on a generic unitary
    theta = 0.37
    ul_generic = np.array(
        [
            [np.cos(theta), np.sin(theta), 0.0],
            [-np.sin(theta), np.cos(theta), 0.0],
            [0.0, 0.0, 1.0],
        ],
        dtype=complex,
    )
    ur_generic = uz3 @ ur
    y_generic = ul_generic.conj().T @ y_universal @ ur_generic
    h_generic = y_generic.conj().T @ y_generic

    offdiag = h_prime - np.diag(np.diag(h_prime))
    cp_entries = [np.imag(h_prime[0, j] ** 2) for j in (1, 2)]

    print()
    print("Representative transformed Yukawa matrix Y':")
    print(y_prime)
    print()
    print("Representative H' = Y'^dag Y':")
    print(h_prime)

    check(
        "The retained exact Dirac bridge is universal: Y = y_0 I",
        np.allclose(y_universal, y0 * np.eye(3), atol=1e-15),
        f"y0={y0:.12f}",
    )
    check(
        "The canonical Z_3 bridge and doublet diagonalization are unitary",
        np.allclose(uz3.conj().T @ uz3, np.eye(3), atol=1e-12)
        and np.allclose(ur.conj().T @ ur, np.eye(3), atol=1e-12),
        "U_Z3^dag U_Z3 = I and U_R^dag U_R = I",
    )
    check(
        "Under those unitary rotations, H' remains y_0^2 I",
        np.allclose(h_prime, (y0 * y0) * np.eye(3), atol=1e-12),
        "Y'^dag Y' = y0^2 I",
    )
    check(
        "The statement is basis-independent for generic unitary U_L, U_R",
        np.allclose(h_generic, (y0 * y0) * np.eye(3), atol=1e-12),
        "generic U_L/U_R still give H = y0^2 I",
    )
    check(
        "All off-diagonal entries vanish, so the CP tensor is exactly zero",
        np.max(np.abs(offdiag)) < 1e-12 and max(abs(x) for x in cp_entries) < 1e-12,
        f"max offdiag={np.max(np.abs(offdiag)):.2e}",
    )

    print()
    print("N5 execution certificate -- what this runner resolves per class:")
    print(
        "  per_element: checked -- the vanishing is established entry by entry "
        "on the 3x3 kernel: every off-diagonal entry of H' is inspected with "
        f"max |H'_offdiag| = {np.max(np.abs(offdiag)):.2e}, the diagonal entries "
        f"all equal y_0^2 = {y0 * y0:.9e}, and the two CP entries "
        f"Im[(H'_1j)^2] for j = 2, 3 come out as {cp_entries[0]:.2e} and "
        f"{cp_entries[1]:.2e} individually."
    )
    print(
        "  per_site: checked and not executed -- although the source comment "
        "labels the left rotation a flavor/site basis change, every matrix here "
        "acts on the internal three-generation index of a single fixed factor; "
        "no Z^3 lattice site is instantiated and no quantity is indexed by "
        "position, so the no-go is not resolved site by site."
    )
    print(
        "  per_mode: checked -- the three Z_3 character modes carried by "
        "U_Z3 with omega = exp(2 pi i / 3) are the resolved objects, and the "
        "finding is exact degeneracy across them: H' assigns the identical "
        f"value {y0 * y0:.9e} to all three character modes, so no mode pair "
        "carries the relative phase the CP tensor would need."
    )
    print(
        "  per_block: checked -- the Z_3 grading splits the factor into a "
        "1-dimensional singlet block and a 2-dimensional doublet block, and "
        "the Majorana rotation U_R acts as the identity on the singlet while "
        "rotating only the doublet block by pi/4; H' is unchanged on both "
        "blocks, so neither block supplies a nonzero CP kernel."
    )
    print(
        "  lattice_wide: checked and not executed -- the entire argument is "
        "finite linear algebra on one fixed 3x3 internal factor with no "
        "volume, no site sum and no limit taken; the centrality of Y = y_0 I "
        f"= {y0:.12f} I is what kills the kernel, and that statement is never "
        "extended to a lattice-scale object anywhere in this runner."
    )
    print()
    print("Result:")
    print("  The exact universal Dirac bridge by itself cannot generate a nonzero")
    print("  leptogenesis asymmetry on the fixed Z_3 Majorana texture. A non-")
    print("  universal Dirac flavor texture or equivalent extra structure is still")
    print("  required before the CP kernel can be nonzero.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
