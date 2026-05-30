#!/usr/bin/env python3
"""
First-Jacobi / first-Hankel equivalence on the canonical Wilson-side packet
(load-bearing claim, post-2026-05-24 narrowing).

Scope (narrowed 2026-05-24):
  This runner is the algorithmic check of the load-bearing claim in
  docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_FIRST_HANKEL_TO_DM_BOUNDARY_NOTE_2026-04-19.md
  after that note's 2026-05-24 narrowing. The load-bearing claim is the
  algebraic equivalence on the canonical minimal-bulk-completion packet:

    on the selected canonical Wilson-side packet from the sibling
    minimal-bulk-completion packet theorem, the first Jacobi layer
    (alpha0, beta1) and the first Hankel packet (m1, m2) satisfy
    alpha0 = m1, beta1^2 = m2 - m1^2, with beta1 > 0.

  This is exact linear algebra on the realized packet and is checked here
  to machine precision.

What this runner no longer asserts:

  The 2026-05-03 audit on this row flagged the prior version for using text
  checks against the source note to assert a contested seam-localization
  premise (that the first Hankel packet is the earliest Wilson-side scalar
  packet feeding the DM boundary). Per the note's 2026-05-24 narrowing,
  the seam-localization statement is explicitly demoted to a non-load-
  bearing conditional corollary, and this runner drops the text checks that
  asserted it. The only checks below are algorithmic identity checks on the
  canonical realized packet.
"""

from __future__ import annotations

from pathlib import Path
import math
import sys

import numpy as np

from frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_packet_theorem_2026_04_19 import (
    selected_transfer_and_packet,
)


ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def main() -> int:
    print("=" * 118)
    print("FIRST-JACOBI / FIRST-HANKEL EQUIVALENCE ON CANONICAL WILSON-SIDE PACKET")
    print("(load-bearing checks only, post-2026-05-24 narrowing)")
    print("=" * 118)
    print()
    print("Question (load-bearing):")
    print("  On the canonical Wilson-side packet selected by the minimal-bulk-completion")
    print("  packet theorem, does the first Jacobi layer (alpha0, beta1) coincide with the")
    print("  first Hankel packet (m1, m2) via alpha0 = m1 and beta1^2 = m2 - m1^2?")

    pkg = selected_transfer_and_packet()
    alpha0 = float(pkg["alpha0"])
    beta1 = float(pkg["beta1"])
    m1 = float(pkg["m1"])
    m2 = float(pkg["m2"])
    eig = float(pkg["eig"])
    psi = np.asarray(pkg["psi"], dtype=float)
    swap = np.asarray(pkg["swap"], dtype=float)
    transfer = np.asarray(pkg["transfer"], dtype=float)

    psi_swap_err = float(np.linalg.norm(swap @ psi - psi))
    sym_err = float(np.max(np.abs(transfer - transfer.T)))
    eig_min = float(np.min(np.linalg.eigvalsh(transfer)))

    moment_alpha_gap = abs(alpha0 - m1)
    beta1_from_moments = math.sqrt(max(m2 - m1 * m1, 0.0))
    moment_beta_gap = abs(beta1 - beta1_from_moments)

    print()
    print(f"  selected (m1, m2)                           = ({m1:.12f}, {m2:.12f})")
    print(f"  selected (alpha0, beta1)                    = ({alpha0:.12f}, {beta1:.12f})")
    print(f"  beta1 from moments sqrt(m2 - m1^2)           = {beta1_from_moments:.12f}")
    print(f"  Perron eigenvalue                           = {eig:.12f}")
    print(f"  transfer symmetry / Perron-swap errors      = ({sym_err:.3e}, {psi_swap_err:.3e})")
    print(f"  min eigenvalue(T_sel)                       = {eig_min:.6e}")
    print()

    # Algorithmic load-bearing checks only. No text checks of the source note.

    # (1) The canonical realization is finite and well-defined.
    check(
        "Canonical Wilson-side packet is finite and well-defined (m1, m2 finite, m2 > m1^2)",
        math.isfinite(m1)
        and math.isfinite(m2)
        and (m2 - m1 * m1) > 1.0e-15,
        f"(m1,m2)=({m1:.6f},{m2:.6f}), m2 - m1^2 = {(m2 - m1 * m1):.3e}",
    )

    # (2) The packet comes from a positive conjugation-symmetric factorized
    # transfer operator with a strictly positive Perron eigenvalue.
    check(
        "Selected packet has positive Perron eigenvalue, symmetric transfer operator, conjugation-symmetric Perron state, and beta1 > 0",
        eig > 0.0
        and sym_err < 1.0e-10
        and psi_swap_err < 1.0e-10
        and eig_min > -1.0e-10
        and beta1 > 0.0,
        f"(eig,sym,psi_swap,eig_min,beta1)=({eig:.3e},{sym_err:.3e},{psi_swap_err:.3e},{eig_min:.3e},{beta1:.3e})",
    )

    # (3) Algebraic equivalence alpha0 = m1.
    check(
        "First Jacobi alpha0 equals first Hankel m1 to machine precision",
        moment_alpha_gap < 1.0e-12,
        f"|alpha0 - m1| = {moment_alpha_gap:.3e}",
    )

    # (4) Algebraic equivalence beta1^2 = m2 - m1^2.
    check(
        "First Jacobi beta1 equals sqrt(m2 - m1^2) to machine precision",
        moment_beta_gap < 1.0e-12,
        f"|beta1 - sqrt(m2 - m1^2)| = {moment_beta_gap:.3e}",
    )

    print("\n" + "=" * 118)
    print("RESULT")
    print("=" * 118)
    print("  Algebraic equivalence on the canonical Wilson-side packet:")
    print(f"    (m1, m2)         = ({m1:.12f}, {m2:.12f})")
    print(f"    (alpha0, beta1)  = ({alpha0:.12f}, {beta1:.12f})")
    print(f"    alpha0 = m1                          : exact ({moment_alpha_gap:.1e})")
    print(f"    beta1  = sqrt(m2 - m1^2)             : exact ({moment_beta_gap:.1e})")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
