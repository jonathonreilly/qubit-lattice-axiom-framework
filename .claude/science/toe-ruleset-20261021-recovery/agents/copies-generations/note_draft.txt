---
claim_id: block_of_eight_band_copies_and_a_per_axis_flip_that_splits_them_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied block-of-eight tick and a supplied per-axis chirality-flip variant: exact copy degeneracy and coset decoupling of the base tick, the exact corner spectrum mu = m + theta(3 - 2n) of the variant, the S4 copy symmetry forcing a mass matrix diag(m_s, m_t, m_t, m_t), and finite numerical masses; no generation, species, chirality or physical mass reading, and no exact cubic covariance of the variant, is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_of_eight_band_copies_and_a_per_axis_flip_that_splits_them_2026_10_21.py
---

# Copies of the block-of-eight band and a per-axis flip that splits them

Claim type: bounded_theorem.
Primary runner: `scripts/block_of_eight_band_copies_and_a_per_axis_flip_that_splits_them_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its current tick candidate puts four two-component fields on the eight sites of a 2^3 block, and its light band comes in four copies. This note shows why the copies do not mix and tests a per-axis flip that splits them. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither tick.

## Why the base copies do not mix

Each axis substep is exp(-i K_i A_i) with A_i of eigenvalues +-1, so a shift by pi e_i flips its sign. Shifts by pi(1,1,0), pi(1,0,1) and pi(0,1,1) leave U unchanged and pi(1,1,1) negates it, to 5.3e-16. Equivalently, all 8 block steps are (+-1,+-1,+-1) and lie in the lattice x = y = z mod 2, so the four cosets of that lattice never exchange amplitude: the copies are four identical decoupled systems. Translations and rotations act on the four copies as S4 (order 24). Its permutation representation is 1 + 3, so the most general covariant copy mass matrix is diag(m_s, m_t, m_t, m_t). The commutant dimensions are 2 for translations with rotations, 2 with C3 about (1,1,1), 4 with the two-fold rotations, 5 for rotations alone and 6 for C3 alone. A one-block-translation-invariant term is diagonal in crystal momentum and cannot couple copies, so splitting them needs block steps outside that lattice.

## The per-axis flip

In each axis substep, move L and L', apply exp(-i theta X_LR) within the block, then move R and R'. At theta = 0 this is the base tick exactly. At a zone corner with n components equal to pi, each half-move is a signed projector sum, and (P_L - P_R) e^{-i theta X} (P_R - P_L) = -e^{+i theta X}. So the corner spectrum is {+-mu, pi +- mu}, each twice, with mu = m + theta(3 - 2n), for every M and every axis order, to 1.1e-15.

With m = 0 and theta = 0.09, the masses are 0.09 six times and 0.27 twice, with zone minimum 0.0900. Each four-copy sector has one copy at 3 theta and three at theta, so the ratio is exactly 3 and there are six light copies. With m = 0.1 and theta = 0.09, the masses are 0.01 three times, 0.17, 0.19 three times and 0.37, with zone minimum 0.0100: three light copies, on the tuned branch theta close to m. Axis-dependent angles split the n = 2 triplet as m - sum(theta) + 2 theta_k, to 8.3e-17. Near the light corners the mean block step per axis equals the group velocity to 8.4e-10. The n = 1 triplet carries the translation characters (-1,1,1), (1,-1,1) and (1,1,-1).

## What the variant costs

The variant is unitary with block steps in {-1,0,1}^3, and 18 of its 27 steps cross cosets. It has a rest step of operator norm sin^3 theta (7.261e-4 at theta = 0.09), which the law that a relay steps every tick does not cover as written. It is spectrally covariant under 8 of the 24 rotations, the D4 about the middle axis of the substep order; the base tick is spectrally covariant under all 24.

Covariant rules give equal triplet masses, so a Koide-type ratio from a C3 circulant would need a coset-privileging term and loss of the two-fold axes.

## Scope

Supplied: one fermion mode per site, the mode assignment, the substep order, M, m and theta, and the flip acting on both families. The three-light-copy branch is a tuning. No generation, species, chirality or physical mass reading is established, and exact cubic covariance of the variant is not.
