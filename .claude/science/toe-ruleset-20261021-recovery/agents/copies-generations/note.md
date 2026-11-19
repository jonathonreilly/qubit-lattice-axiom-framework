---
claim_type: bounded_theorem
claim_scope: "For the supplied block-of-eight tick and a supplied per-axis chirality-flip variant: exact copy degeneracy and coset decoupling of the base tick; exact corner spectrum mu = m + theta(3 - 2n) of the variant; S4 copy symmetry forcing diag(m_s, m_t, m_t, m_t); finite numerical masses. No generation, species, chirality or physical-mass reading."
---

# Copies of the block-of-eight light band: why they do not mix, and a per-axis flip that splits them

Claim type: bounded theorem. Draft (agent copies-generations, 2026-10-21). Runner: `runner.py` (13 checks).

## Setting (supplied)

The block candidate has modes L, R, L', R' (two spin components each) per block. Its tick is a block-local mass gate exp(-i(m X_LR + M X_LR'))
followed by three axis substeps S_i = exp(-i K_i A_i), A_i = sigma_i on L, L' and -sigma_i on R, R', and a sign on L', R'.
Everything here is in Bloch form over the block lattice, so one-block translations commute with the tick by construction.

## Theorems

**T1. The base copies are exact duplicates carried by cosets.** A_i has eigenvalues +-1, so S_i(K + pi e_i) = -S_i(K). A shift by
G in {pi(1,1,0), pi(1,0,1), pi(0,1,1)} flips two signs: U(K+G) = U(K). A shift by pi(1,1,1) flips three: U(K+pi(1,1,1)) = -U(K).
Equivalently, every block step is (+-1,+-1,+-1), inside the lattice B = {x = y = z mod 2}. The four cosets of B are invariant
under the tick, mass gate included, so the four copies are four identical, decoupled systems.

**T2. Copy symmetry.** Translations act on the four cosets as Z2 x Z2. Rotations about a site fix the coset of that site and
permute the other three. Together they generate S4 (order 24). The 4-point permutation representation of S4 is 1 + 3, so its
commutant is span{1, J}. In the corner basis, the most general covariant copy mass matrix is diag(m_s, m_t, m_t, m_t). There is no
singlet-triplet mixing and no triplet splitting. In coset language, with on-block term a and uniform inter-coset coupling d,
m_s = a + 3d and m_t = a - d. The commutant dimensions are 2 for translations and rotations, 2 for translations and C3[111], 4 for
translations and the two-fold rotations D2, 5 for rotations alone (S3) and 6 for C3 alone.
If one-block translations are kept, any symmetry that acts transitively on the three corners forces m_t to be common.
With rotations alone, i.e. if one coset is privileged, the matrix is [[a, beta, beta, beta], [beta*, b, d, d], ...].
Its spectrum is b - d (twice) and (a+b+2d)/2 +- sqrt(((a-b-2d)/2)^2 + 3|beta|^2).

**T3. No translation-covariant bilinear mixes the copies.** The copies sit at distinct crystal momenta, so a one-block-translation-invariant
term is diagonal in K and cannot couple G to G'. A tick change can only split copies, by making the corners inequivalent.
That requires a block step outside B: if every step lies in B, T1 holds and the copies stay degenerate.

**T4. Corner theorem for the per-axis flip.** Proposal: in each axis substep, move L and L' (exp(-i K_i sigma_i P_L)), apply
exp(-i theta X_LR) within the block, then move R and R'. At a corner G each half-move is P_R + (-1)^{n_i} P_L or its mirror.
Then (P_L - P_R) e^{-i theta X} (P_R - P_L) = -e^{+i theta X}, so axis i contributes (-1)^{n_i} exp(-i theta cos G_i X_LR).
All corner factors commute with X_LR. Hence U(G) = (-1)^n sgn e^{-iM X_LR'} e^{-i mu X_LR} with mu = m + theta(3 - 2n), where n is the number of pi
components. The spectrum is {+-mu, pi +- mu}, each twice, for every M and every axis order (checked to 1e-15).

## Results

- **P1 (theta replaces m, no new parameter; M = .5, theta = .09).** The singlets n = 0, 3 have mass 3 theta = 0.27. The triplets
  n = 1, 2 have mass theta = 0.09. The zone minimum is 0.0900. Each four-copy sector has one copy at 3 theta and three at theta,
  so the ratio is exactly 3. Overall there are six light copies, not three.
- **P2 (m and theta; m = .1, theta = .09).** The masses are 0.01 x3 (n = 2), 0.17 (n = 3), 0.19 x3 (n = 1) and 0.37 (n = 0),
  and the zone minimum is 0.0100. This is exactly three light copies. It needs the tuned branch theta = m + delta with |delta| << m
  (theta = -m selects n = 1 instead). The tuning is supplied.
- In both, the band minimum sits at the corner. The mean block step per axis equals the group velocity (8e-10).
- **Degeneracy breaking.** Axis-dependent angles give m_k = m - sum(theta) + 2 theta_k on the n = 2 triplet. That breaks the
  rotations. Otherwise it takes a coset-privileging term. Both privilege something: an axis or a site class.

## Koide, structural only

Covariant rules give b = 0 on the triplet: Q = 1/3, r = 0. A Hermitian C3 circulant, a + 2|c| cos(phi + 2 pi k/3), needs both
a coset-privileging term and the loss of the two-fold axes. Even then the tick's mass enters the quasi-energy linearly, so r = 1/2
would fix sum m^2/(sum m)^2 = 2/3, not Koide's Q, which needs the circulant on sqrt(m). This is a mismatch, not a fit.

The n = 1 triplet carries exactly the diag(-1,+1,+1) translation triple of THREE_GENERATION_OBSERVABLE_THEOREM_NOTE. Here those
translations are symmetries of the tick, unlike in the staggered case. The C3[111] cycle, however, is not a symmetry of the P1/P2 tick off the corners.

## Interactions between copies

- **Base tick.** Tick steps, burns (site-local), relay steps (assumed to be the tick's steps, (+-1)^3) and CL-6 switching (within a
  block) all stay in one coset. The copies share no block. They couple only through the shared responses to the CL-7 source and the
  value current, i.e. gravity and the vector field, with equal strength.
- **Proposal.** The free tick keeps each copy (a distinct crystal momentum). A burn is site-local and breaks translations: its matrix
  element between corners G and G' is e^{i(G-G').x}, of unit modulus. Burns therefore scatter copies into one another directly,
  in addition to gravity and gauge.

## Smuggling review and open dependencies

Supplied: the mode assignment, the substep order, L-before-R (R-before-L gives the same corners), M, theta, and the flip acting on
both families. P1 privileges no site, state or axis, and the ratio 3 follows from three axes. P2's three-light branch is a tuning.

The proposal is spectrally covariant under 8 of 24 rotations (the D4 about the middle axis). The base is covariant under 24 of 24 spectrally,
but only 4 of 24 at operator level. The corner theorem is order-independent.

The proposal also adds non-diagonal steps and a rest step of norm sin^3 theta. CL-4 ("relays always move one block per tick") does not cover the rest step.
