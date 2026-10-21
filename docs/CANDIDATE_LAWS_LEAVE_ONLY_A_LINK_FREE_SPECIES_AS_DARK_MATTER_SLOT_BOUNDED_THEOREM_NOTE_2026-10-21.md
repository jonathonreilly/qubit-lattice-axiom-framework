---
claim_id: candidate_laws_leave_only_a_link_free_species_as_dark_matter_slot_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied staggered block tick and supplied (mu, b) settings: the two copies at one frequency carry equal values of any rotation-covariant charge at rungs 1 to 3; pi-cone states carry their species number, sit at the global band top and, in finite numerical searches, have no lower two- or three-body state; the record set has no source term; and a number-conserving species with no link is exactly stable. Measured-data comparisons (halo dynamics, CMB consistency, thermalisation, self-scattering, sterile-neutrino lifetime) are estimates. No dark-matter species, mass or relic abundance is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/candidate_laws_leave_only_a_link_free_species_as_dark_matter_slot_2026_10_21.py
---

# The candidate laws leave only a link-free species as a dark-matter slot

Claim type: bounded_theorem.
Primary runner: `scripts/candidate_laws_leave_only_a_link_free_species_as_dark_matter_slot_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note checks five places in the register's laws where a dark component could sit: the second copy at one frequency, the pi-cone sector, the record set, a species with no link, and coarse-rung collective modes. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## The second copy carries the same charge

The staggered rest tick is U(0) = cos mu + i sin mu W, and the rotations commute with W. Each 4-dimensional rest space (W = +1, the two copies of one frequency) is irreducible under the 24 rotations: the mean |chi|^2 is 1.000000. By Schur's lemma every operator commuting with U(0) and the rotations, local or not, is a scalar there; the commutant has dimension 2 and the non-scalar part is 2.5e-16. So the two copies carry the same value of any covariant charge. This holds at rungs 1, 2 and 3: the coarse rest eigenvalue comes only from fine K = 0, with minimum separations 0.935, 0.573 and 0.228 over folded points. For the massless U(1) Q = a + c eps the copies carry {a + c, a - c}, so a copy is neutral only if Q = 0. A 90-degree rotation sends the copy label sigma3 to -sigma3, so the copy is not a rotation-invariant label.

## The pi-cone sector

The only K-independent block-local commutant is the scalars, so the only link charge is the species number, which counts a pi-cone mode like a light one. At R = pi(1,1,1), w(R) = pi - 2b is the global top of the band, with maximum excess -1.4e-4 over 1e5 sampled K for each of three (mu, b) settings. In finite searches at total momentum R there is no lower two-body state, and the lowest three-body states lie above w(R): 2.5416 against 1.9416, 0.6000 against 0.5000 and 3.0416 against 2.9416. This stability is numerical, not a theorem.

Under the supplied lapse coupling H = w(K)(1 + phi) in a weak well, the light packet falls in and the pi-cone packet falls out, both at the semiclassical rate -w w'' grad phi:

| (mu, b) | light packet a | pi-cone packet a | ratio |
|---|---|---|---|
| (0.3, 0.600) | -4.087e-4 (pred. -4.177e-4) | +8.696e-4 (pred. +8.710e-4) | -2.128 |
| (0.3, 1.321) | -1.250e-4 (pred. -1.253e-4) | +1.286e-4 (pred. +1.289e-4) | -1.029 |

Read with quasi-energy measured from 0, a pi-cone state at rest can never enter lower phi. Read from pi, its energy w - pi = -2b is negative: it falls in but sources negative energy. As an estimate, its mass is 0.5 rad/tick = 1.05e18 GeV in the first reading. Both readings conflict with the positive, concentrated dark mass inferred from rotation curves and lensing.

## Records source nothing

The register's total phase has no record term, so the permanent record set sources nothing. If it did, record mass per comoving volume would grow as t, by 3.63e4 from recombination to today, against a few-percent consistency between CMB and late-time dark-matter densities (estimate). The Born mean of a conditional source equals tr(rho_A T_A) + <V>/2 (-0.462433 both ways), so it adds no hidden mean mass.

## A species with no link

A number-conserving tick keeps the species number exactly ([N, U] = 0.0), so the lightest state is absolutely stable and has no photon coupling. A pairing term breaks this ([N, U] = 0.22) while fermion parity survives. As estimates: gravity alone gives Gamma/H = 3.8e-5 even at T = 1.1e18 GeV, so the relic density is whatever the supplied initial odds say; gravitational self-scattering is 3.2e-50 cm^2/g at 1.1e18 GeV against a bound of order 1; and an empty-register singlet with a Yukawa coupling at 7 keV and sin^2 2theta = 1e-11 lives 4.4e28 s against an age of 4.35e17 s.

Coarse-rung collective modes are not computed separately. The gapped link branches are Planck-scale parts of the link field and decay to charged pairs.

## Checks

The runner prints `TOTAL: PASS=22 FAIL=0`. Its PASS lines cover the rest-space irreducibility, the Schur commutant, the rung-1 to rung-3 folding, the U(1) copy charges, the copy-label rotation, the species-number commutant, the band top, the finite decay searches and packet accelerations for each (mu, b), the two readings at R, exact number conservation and its pairing control, the conditional-source mean, the record-growth estimate, gravitational thermalisation and the singlet lifetime.

## Supplied and boundary

Supplied: the block tick, b and mu, the two readings of quasi-energy, the lapse coupling in the weak static limit, the photon band cos w = S, the unit map a = sqrt(8 pi) l_P, the register reading of the singlet, the sterile-neutrino decay formula and all measured numbers (Planck 2018 gives Omega_c = 0.2645). The surviving slot needs a law that fixes the link-free species' mass and abundance; none is proposed. No dark-matter species, mass or relic abundance is established.
