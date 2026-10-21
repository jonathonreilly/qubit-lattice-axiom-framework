---
claim_id: anomaly_free_conserved_currents_fix_hypercharge_on_supplied_chiral_content_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "A photon coupled to relay value (fermion number) gives q_n = q_p = 3 and unbound hydrogen, and massless baryon-number or B-L links are compared with MICROSCOPE as estimates. On the supplied lattice tick an on-site sublattice symmetry survives random link phases and Wilson doublers cancel the index. On the supplied chiral three-generation content with supplied Yukawa structure, the U(1)s conserved classically and left anomaly-free by the colour and weak links are span{Y} without a right-handed neutrino and span{Y, B-L} with Dirac neutrinos; Y comes out in the ratios 1:-4:2:-3:6, q_e + q_p = 0 and q_n = -q_nu identically, and a neutral vacuum gives the measured charges. No chiral content, link law, electric-charge rule or fermion-number-breaking mechanism is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/anomaly_free_conserved_currents_fix_hypercharge_on_supplied_chiral_content_2026_10_21.py
---

# Anomaly-free conserved currents fix hypercharge on supplied chiral content

Claim type: bounded_theorem.
Primary runner: `scripts/anomaly_free_conserved_currents_fix_hypercharge_on_supplied_chiral_content_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It conserves relay value in every event and reads that value as charge. This note measures how far that reading is from data and checks which conserved currents survive once supplied links act. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the content used.

## Relay value as charge

Relay value counts fermion number, F = 3A + Z for a nucleus. A photon coupled to it gives q_n = q_p = 3 and q_H = +4: electron and proton repel and atoms are unbound. The measured |q_n| < 1.5e-21 excludes this by a factor of 2e21. As estimates against MICROSCOPE (|eta| < 4.2e-15, titanium against platinum alloy, alpha_G(u) = 5.821e-39), a massless link at coupling e = 0.303 on F, B or B-L gives eta of 2.6e35, 1.0e33 and 3.6e34. The couplings must be below 3.9e-26, 6.2e-25 and 1.0e-25.

## On-site symmetries on the lattice

The block hop W is Hermitian with W^2 = 1. With random link phases at mu = 0 the tick is unitary and the sublattice sign eps = (-1)^(x+y+z) commutes with it exactly (2.4e-15 and 6.2e-15). At mu = 0.4 the mass breaks it (|[eps, U]| = 0.33). The anomaly weight of eps over the copy doublet is proportional to tr sigma3 = 0. For a Wilson fermion with one light species (m0 = 1), |index| equals the flux for flux 1, 2 and 3. Two doublers (m0 = 3) give minus the index of one, and all four (m0 = 5) or the naive operator (r = 0) give 0. So on a finite-range lattice an exact on-site number carries no net anomaly.

## Spectral flow

One flux quantum moves chi q levels of a chiral branch of charge q. Times the lowest-level degeneracy q n_B, the anomaly weight is the sum of chi X q^2; the runner checks (chi, q) = (1, 1), (1, 2), (1, -1) and (1, 3). The abelian count is rederived here; the non-abelian weights are cited.

## Supplied chiral content

On supplied left-handed Weyl content with three generations:

| current | SU(3)^2 X | SU(2)^2 X | X^3 | grav | Y^2 X |
|---|---|---|---|---|---|
| F (relay value) | 0 | 6 | 0 | 0 | -6 |
| B | 0 | 3/2 | 0 | 0 | -3/2 |
| L | 0 | 3/2 | 0 | 0 | -3/2 |
| B+L | 0 | 3 | 0 | 0 | -3 |
| B-L | 0 | 0 | 0 | 0 | 0 |
| L_mu - L_tau | 0 | 0 | 0 | 0 | 0 |
| Y | 0 | 0 | 0 | 0 | 0 |

- With Dirac neutrinos the classical conserved U(1)s are span{Y, B, L}, and the subspace that stays conserved once SU(3)^2 and SU(2)^2 act is span{Y, B-L}, with all trilinears 0.
- Without a right-handed neutrino (Weinberg operator) the classical U(1)s are span{Y, B} and the surviving subspace is span{Y}, with ratios Q:u:d:L:e = 1:-4:2:-3:6.
- With Yukawas and SU(2)^2, X^3 per generation factors as (h - 3q)^3, so h = 3q and Y is fixed up to scale with no gravitational input.
- L_mu - L_tau has no anomaly, so the anomaly condition alone does not remove it.

## Electric charge

Write Q = T3 + lambda Y + epsilon (B - L). Then q_e + q_p = 0 identically in lambda and epsilon, and q_n = -q_nu identically (q_n = epsilon + lambda/2 - 1/2). A neutral vacuum (T3 = -1/2, Y = 1/2) gives e, p, n, u, d, nu = -1, 1, 0, 2/3, -1/3, 0. With a B-L admixture q_n = epsilon, so as an estimate |epsilon| < 1.5e-21. An SU(2) instanton has one zero mode per doublet, so Delta B = Delta L = 3, Delta(B-L) = 0 and Delta F = 12. Its rate is about exp(-4 pi/alpha_W) = 10^-161.5 and needs three baryons, so one proton cannot decay this way.

## Checks

The runner prints `TOTAL: PASS=18 FAIL=0`. Its PASS lines cover the MICROSCOPE and neutron-charge bounds, the block hop, survival of eps under link phases, its breaking by mass, the Wilson index and doubler cancellation, the spectral-flow count, the anomaly weights, the Dirac and Weinberg conserved subspaces, the cubic factorisation, the two charge identities, the neutral-vacuum charges and the instanton selection rule.

## Supplied and boundary

Supplied: the chiral SU(3) x SU(2) links and Standard Model content, the Higgs and Yukawa structure, and any fermion-number-breaking gap for mirror fermions; 't Hooft anomaly matching for that step is cited, not rederived. A rule that gives links only to currents the full update conserves would remove fermion number only if the full update breaks it. Measured comparisons are estimates. No chiral content, link law, electric-charge rule or fermion-number-breaking mechanism is established.
