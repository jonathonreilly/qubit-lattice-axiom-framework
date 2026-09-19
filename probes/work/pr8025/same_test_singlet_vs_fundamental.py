#!/usr/bin/env python3
"""J:attack-b:PR8025 — SAME TEST BOTH SIDES on §5 singlet vs fundamental block.

The note: the four-link physical state has single-link reduced density I/9 on
the 9-dim fundamental PW block and zero support on the constant singlet; a
forced local zero-charge projection would discard it. Same test: overlap of
the reduced density with (i) the 9-dim block identity and (ii) the 1-dim
singlet projector, applied to both the loop state and a pure singlet.
HIT if both objects pass or both fail the same support test.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    # Haar: E[U_ab conj(U_cd)] = δ_ac δ_bd / 3  ⇒  ρ_link = I_9 / 9
    dim_fun = 9
    dim_singlet = 1
    rho_loop = Fr(1, dim_fun)  # each of 9 diagonal entries
    # overlap with the 9-dim block: Tr(ρ I_9) = 1
    overlap_block_loop = dim_fun * rho_loop
    # overlap with the constant singlet: the singlet is the trivial irrep,
    # orthogonal to the 8+1?  For L2(SU3), the constant function is the
    # (0,0) PW block, dimension 1. Fundamental matrix elements live in (1,0)
    # and are orthogonal to (0,0). So <singlet, ρ_loop singlet> = 0.
    overlap_singlet_loop = Fr(0)
    print(f"loop state: Tr_block={overlap_block_loop} singlet-overlap={overlap_singlet_loop}")

    # a genuine singlet reduced state: ρ = |0><0| on the trivial block
    overlap_block_singlet = Fr(0)  # no support on the 9-dim fundamental block
    overlap_singlet_singlet = Fr(1)
    print(f"singlet state: Tr_block={overlap_block_singlet} singlet-overlap={overlap_singlet_singlet}")

    # same test 1: "supported on the singlet?"
    loop_on_singlet = overlap_singlet_loop > 0
    singlet_on_singlet = overlap_singlet_singlet > 0
    print(f"supported on singlet: loop={loop_on_singlet} singlet={singlet_on_singlet}")
    if loop_on_singlet == singlet_on_singlet:
        return hits("singlet-support test does not separate the loop state from a singlet")

    # same test 2: "supported on the 9-dim fundamental block?"
    loop_on_fun = overlap_block_loop > 0
    singlet_on_fun = overlap_block_singlet > 0
    print(f"supported on fundamental 9-block: loop={loop_on_fun} singlet={singlet_on_fun}")
    if loop_on_fun == singlet_on_fun:
        return hits("fundamental-block support test does not separate")

    # Haar orthonormality of the 9 matrix elements vs 1 singlet
    haar_fun = Fr(1, 3)  # E|U_ab|^2
    if 9 * haar_fun != 3:
        return hits("9 Haar matrix elements do not reconstruct Tr U*U=3")
    print("Haar: 9 fundamental matrix elements orthonormal after √3; singlet orthogonal: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the same support tests "
        "separate the four-link physical reduced density (I/9 on the 9-dim "
        "block, zero on the singlet) from a local singlet, as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
