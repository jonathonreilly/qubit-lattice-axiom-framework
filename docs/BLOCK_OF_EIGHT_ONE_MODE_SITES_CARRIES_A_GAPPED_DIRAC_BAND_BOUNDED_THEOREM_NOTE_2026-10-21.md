---
claim_id: block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite checks that a supplied block-local update on the eight one-mode sites of a 2^3 block reproduces the two-mass gapped Dirac band and that its light band's mean block step equals the group velocity; no matter content, exact cubic covariance, removal of sublattice copies or physical masses."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_2026_10_21.py
---

# A block of eight one-mode sites carries a gapped Dirac band

Claim type: bounded_theorem.
Primary runner: `scripts/block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) give one qubit per site. In the fermionic reading that is one mode per site. A field with two spin components at a site therefore needs two modes, which is more than one site holds. The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, states its relay rules per block. This note puts the two-mass Dirac cell of the companion two-chirality note into the eight modes of a 2^3 block.

## Construction

The block's eight modes are taken as four two-component fields L, R, L' and R'. On the block lattice they run, respectively,

    U_L(K), U_L(-K), -U_L(K), -U_L(-K),

where U_L(K) = S_z S_y S_x. The sign reproduces the momentum shift by Q = pi(1,1,1): each factor changes sign under k -> k + pi, so U_L(K+Q) = -U_L(K). The masses are block-local:

- **m** couples L with R and L' with R';
- **M** couples L with R' and L' with R.

The whole tick therefore factors into a block-local mass coin, three block substeps and a block-local sign. Each piece is a single-particle unitary on the block's modes, i.e. a fermionic Gaussian operation.

## Results

- **Spectrum:** at 50 random block momenta it equals that of the momentum-shifted form to 1e-12 or better.
- **Gap:** the minimum |quasi-energy| on a 25^3 zone grid equals m, at m = .05 and M = .5.
- **Mean step:** for the light band at three momenta away from the axes, the mean block step per axis equals the group velocity. The record-source identity of the register therefore applies. On the axes the band is spin-degenerate, and the identity needs the velocity-diagonal spin state.

## Scope

The assignment of block modes, the substep order and the two masses are supplied. Exact cubic covariance holds for 4 of 24 rotations, as for the split-step update. The four sublattice copies of the light band remain. No matter content or physical mass values are established.
