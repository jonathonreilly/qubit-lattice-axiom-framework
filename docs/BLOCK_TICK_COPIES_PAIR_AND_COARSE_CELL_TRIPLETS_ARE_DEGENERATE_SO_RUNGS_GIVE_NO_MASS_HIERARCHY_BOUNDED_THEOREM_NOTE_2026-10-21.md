---
claim_id: block_tick_copies_pair_and_coarse_cell_triplets_are_degenerate_so_rungs_give_no_mass_hierarchy_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For supplied rotation-covariant block ticks with the spin-3/2 corner action: levels at K = 0 and K = pi(1,1,1) have multiplicity 4k in 30 random multi-step ticks; in a coarse cell of 2^3 blocks the fine corners fold to coarse K = 0 in orbits 1, 3, 3, 1 with exactly degenerate triplets; one zoom step doubles the gap per coarse tick so the physical mass is rung-invariant; the family cos w = A S - B cannot carry the lepton ratios with one copy per orbit; an S3 copy symmetry allows at most two distinct masses and a C3 circulant fits any three with no prediction. Comparisons of Koide ratios, rung ladders, a universal rung map and shared-basis mixing with measured masses and mixings are estimates. No tick-level mechanism for three non-degenerate light copies, Koide parameters or mixing is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_tick_copies_pair_and_coarse_cell_triplets_are_degenerate_so_rungs_give_no_mass_hierarchy_2026_10_21.py
---

# Block-tick copies pair and coarse-cell triplets are degenerate, so rungs give no mass hierarchy

Claim type: bounded_theorem.
Primary runner: `scripts/block_tick_copies_pair_and_coarse_cell_triplets_are_degenerate_so_rungs_give_no_mass_hierarchy_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether zooming out the register's block tick, one block or one coarse cell of 2^3 blocks at a time, can supply three light copies with distinct masses. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the ticks used, and the assignment of one copy per rung or orbit is supplied.

## Copies at one block

The commutant of the 24 spin-3/2 corner actions has dimension 4, so covariant block unitaries are exp(i sum x_j H_j). In 30 random covariant multi-step ticks every level at K = 0 and K = pi(1,1,1) has multiplicity 4k (only 4 was seen), so copies come in pairs and an odd count cannot occur at this rung.

## A coarse cell of 2^3 blocks

The fine corners {0, pi}^3 fold to coarse K = 0 in rotation orbits of sizes 1, 3, 3, 1 (by the number of pi entries), and corners in one orbit have identical spectra, so each triplet is exactly degenerate. With the W(mu) tick the coarse levels are |w_n| = arccos(cos^2(mu/2)(3 - 2n)/3 - sin^2(mu/2)); at mu = 0.1 this gives 0.1000, 1.2345, 1.9124 and 3.1416 (deviation 1.3e-15), so the triplets sit at the cutoff. One zoom step uses 2 fine ticks per coarse tick and K_c = 2 K_f, so the coarse gap is 2 x the fine gap (0.20000 against 2 mu = 0.2). The physical mass is rung-invariant and zooming makes no new light copy.

For the family cos w = A S - B (block ticks with any even and odd masses), one copy per orbit n = 0, 1, 2 obeys cos w0 - 2 cos w1 + cos w2 = 0. This has no root with w1/w0 = 206.77 and w2/w1 = 16.817 with w2 <= pi: the left side is negative on (0, pi/16.817], about -140 w1^2 near 0. In the small-w limit w_n^2 is affine in n, so w2/w1 tends to sqrt(2) = 1.414. This covers only this family, not every covariant tick.

## What a copy symmetry allows

- S3 (permutation representation A1 + E): the commutant is span{1, J}, with spectrum {a + 2d, a - d, a - d}, so at most two distinct masses.
- C3 alone: the commutant is the 3-dimensional circulants a + bP + b* P^2, and (a, |b|, phase) fit any three masses: 3 parameters for 3 data, no prediction. For the leptons |b|/a = 0.707100 and the phase is 0.222230 rad mod 2 pi/3.
- C3 with a real structure (b real, from an axis reflection or antiunitary symmetry) forces a degenerate pair, so three distinct masses need a complex phase off multiples of pi/3.
- On the square-root-mass circulant the Koide ratio is Q = 1/3 + (2/3)|b|^2/a^2, independent of the phase.

## Estimates against measured masses and mixing

- Koide: leptons give Q = 0.666661 +- 0.000007, 0.9 sigma from 2/3. Up quarks give 0.8490 and down quarks 0.7314, so no species-blind Q = 2/3 mechanism fits.
- A rung-independent rule makes m_(n+1)/m_n constant, but the lepton ratios 206.77 and 16.817 differ by a factor 12.2952. A geometric ladder obeys Koide only at (23 + 5 sqrt(21))/2 = 22.9564 per rung, giving 1 : 22.96 : 527 against measured 1 : 206.8 : 3477.
- Suppression m_n ~ exp(-c 2^n) predicts ln(m2/m1)/ln(m3/m2) = 2. Measured: leptons 1.8890, up 1.2981, down 0.7881. Fitting c to mu/e predicts tau/mu = 14.38 against 16.817.
- A universal two-parameter rung map fitted to the leptons (c = 0.5294, m* = 42.5 GeV) misses every quark step by more than a factor 2 (0.18, 0.04, 3.65 and 0.40 times).
- Up and down both circulant in one copy basis make the CKM matrix a permutation, so |V_us| = 0 against 0.22500 +- 0.00067 (336 sigma). Circulant charged leptons with diagonal neutrinos give |U|^2 = 1/3 everywhere, so sin^2 theta13 = 1/3 and sin^2 theta12 = 1/2 against 0.0220 and 0.307.
- For reference only, the Brannen form with r = 1/2 and delta = 2/9 supplied gives mu/e = 206.770 and tau/mu = 16.8180, and Koide gives m_tau = 1776.97 MeV against 1776.86 +- 0.12: two supplied constants for two ratios, produced by no tick here.

## Checks

The runner prints `TOTAL: PASS=18 FAIL=0`. Several PASS lines record that a candidate mechanism fails against measurement. They cover the block commutant, the pair multiplicities, the orbit folding and degeneracy, the coarse levels, rung invariance of the mass, the no-root result, the S3 and C3 commutants, the real-structure degeneracy, the Koide formula, the measured Koide values, the four ladder and rung-map tests, the two mixing tests, and the Brannen reference.

## Supplied and boundary

Supplied: the tick, the j = 3/2 action, the partitions, the masses, the rung-to-copy assignments and the measured PDG and NuFIT values. Quark masses mix renormalisation schemes, but each failure is at a factor of 2 or more. Measured comparisons are estimates. No tick-level mechanism for three non-degenerate light copies, Koide parameters or mixing is established.
