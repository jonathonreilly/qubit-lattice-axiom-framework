---
claim_id: light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied block Hamiltonian H' with a supplied copy-selective symmetric mirror term, the light-copy states at K = 0 and K = R are exact zero modes at any coupling and the second-order induced light mass vanishes at K = 0, but with the mirror gapped the light copy has 8 Weyl nodes per sublattice (4 left, 4 right), a vector-like spectrum; a 1+1D chain shows the same release; no chiral light spectrum is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.py
---

# The light copy stays exactly massless, yet gapping the mirror releases vector-like doublers

Claim type: bounded_theorem.
Primary runner: `scripts/light_copy_exactly_massless_yet_mirror_gapping_releases_vector_like_doublers_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its chirality route gaps one copy (the mirror) symmetrically and keeps the other (the light copy). This note asks whether the light copy stays massless and whether it stays chiral. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither H' nor the mirror term.

## Statement

1. At K = 0 and K = R the light copy is decoupled exactly: its states commute with every term built from mirror modes, for any coupling, so its Green function there is 1/z. The second-order induced light mass is zero at K = 0, and no mirror condensate can give the light copy a mass at K = 0.
2. Anomaly matching protects the light copy exactly for N = 1, 2, 4, 5, 7, 8 families, the N at which the rest cannot be gapped. At N = 0 mod 3 every listed anomaly vanishes and anomaly matching protects nothing.
3. Negative result. Once the mirror is frozen or gapped by a copy-selective term, the light copy has Weyl nodes at all 8 block-zone corners, 4 left-handed and 4 right-handed per sublattice. The spectrum is vector-like in each SU(2)_e sector. A 1+1D chain shows the same release at p = pi.

## Derivation

H'(0) = H'(R) = 0, and s3 splits each sublattice 2 + 2 with [s3, H'(K)] = O(K^2). Near Gamma the light-mirror block has two equal singular values (sqrt2/6)|Kx^2 + w Ky^2 + w^2 Kz^2|, a d-wave form that vanishes on the body diagonals. On a 4^3 torus, in both tilings, the light states at K = 0 and K = R are killed by H' and orthogonal to the mirror combinations of all 16 cubes. By the canonical anticommutation relations they commute with every mirror term, so they are exact zero modes.

The mirror cell chains of the single-cell pair-square theorem give E0 = -2g sqrt(11088 + 48 sqrt 21081), gap 19.0715 g and fermion gap 33.5804 g. Reversal of the ground chain and particle-hole conjugation (16 <-> 16bar) give equal hole weights, so the isolated cell's mirror Green function is odd in z and vanishes at z = 0. The second-order self-energy h G_b h^dag is then a Z factor plus a static part from the mirror's own band of order K^5/Delta_f^2, which is zero at K = 0. Any mirror condensate reaches the light copy only through h(K) ~ K^2, so its induced light mass term goes as K^4/M and is zero at K = 0. Masses for the light copy therefore need fields coupled to it directly, as an explicit new term.

Per family, the light content carries twisted-Z3_k x SU(2)_e^2 = 4(q_a + k), which is 16 = 1 mod 3 at k = 2; the set still to be gapped (the mirror plus the light R-point partner) carries the opposite. The protection that holds at N = 0 mod 3 is crystalline: the copy label is exact at K = 0.

At the 8 corners the light-light and mirror-mirror blocks of H' vanish. The mixing is 0 at Gamma and R and 2sqrt2/3, the whole free gap, at the six X and M corners: H' gaps X and M only through copy mixing. With the mirror frozen, the light Hamiltonian P_l H' P_l is traceless with zeros only at the 8 corners, chirality (-1)^(r+1): Gamma and the three M points left-handed, the three X points and R right-handed, net zero. A gapped mirror with a propagator zero removes the partner that the X and M doublers were paired with. Any endpoint that freezes local light combinations leaves a finite-range free Hamiltonian, whose nodes have net chirality zero per sector by Nielsen-Ninomiya; with Gamma kept, a right-handed node survives. Golterman and Shamir (arXiv:2505.20436) extend this away from the endpoint under their assumptions; that is cited, not rederived.

## Checks

The runner ends with `TOTAL: PASS=20 FAIL=0`. Among its lines:

- `[PASS] A1 [T] H'(0) = H'(R) = 0; s3 splits each sublattice 2+2; [s3,H'(K)] = O(K^2)`.
- `[PASS] A2 [T] near Gamma the light-mirror block has 2 equal singular values (sqrt2/6)|Kx^2 + w Ky^2 + w^2 Kz^2|`.
- `[PASS] A3 [T] at the 8 corners the light-light and mirror-mirror blocks vanish; the mixing is 0 at Gamma, R and 2sqrt2/3 = the whole free gap at the 6 X/M corners`.
- `[PASS] A4 [T] the light projected band P_l H' P_l is traceless with zeros only at the 8 corners, chirality (-1)^(r+1) (Gamma, 3M left; 3X, R right): net 0`.
- `[PASS] B1 [T] 4^3 torus, both tilings: light K=0 and K=R states are killed by H' and orthogonal to the mirror combos of all 16 cubes ... exact zero modes, G_l(z,0) = 1/z at any coupling`.
- `[PASS] B2 [T] one block, mirror top form: at Gamma and R the 16 light states stay exactly degenerate, mirror gap exactly g (g = .5, 4, 32) | splitting 5e-14`.
- `[PASS] C1 [T] cell chains: E0 = -2g sqrt(11088+48 sqrt21081), Delta = 19.0715 g, Delta_f = 33.5804 g`.
- `[PASS] C2 [T/F] second order Sigma = h G_b h^+ ... O(K^5), zero at K = 0, never a mass`. The one-block diagonalisation gives 0.170579652 against a predicted 0.170579724 at g = 2.
- `[PASS] D1 [T] ... anomaly protection holds exactly for the N at which S cannot be gapped | k=2: N [1, 2, 4, 5, 7, 8]`.
- `[PASS] D2 [T] at N = 0 mod 3 all listed light anomalies vanish ... anomaly matching gives no protection there`.
- `[PASS] E2 [T] endpoint (mirror frozen, P f P = 0): light H_eff = P_l H' P_l, 8 Weyl nodes per sublattice per family, 4L + 4R: vector-like in each SU(2)_e sector`.
- `[PASS] E3 [F] one block at X ... light weight 0.9991 = Z = g^2/(g^2+8/9): doublers released | gap 0.9428, 0.8093, 0.0329, 0.0005` at g = 0, 2, 8, 32.
- `[PASS] E5 [T] zoom repair of X/M: a light-copy term mu(1 - S(K)^2) linking K and K+R ... the 6 X/M doublers get gap mu 8/9, Gamma and R stay`.
- `[PASS] F1 [T]` to `[PASS] F5 [T]`: the 1+1D chain (16 modes on a twisted ring, copy mixing mu(1 - cos p), mu = 0.5). The light p = 0 mode commutes with the generator to 4e-17 and stays gapless and right-moving (+0.1494, weight 1.0000 at theta = 0.3, g = 16). The p = pi doubler is released as a left-mover (-1.006, -0.210, -0.1497 with weights 0.57, 0.90, 0.9961 for free, g = 4, g = 16), so the light copy becomes R + L. A pair hop on both copies instead moves the light Gamma quasiparticle to -22.35 (weight 0.32). Freezing the staggered light pair leaves H_eff = sin(K)/2, a new left-mover at K = pi.

Estimate lines: `[PASS] E1 [E]` (no light composites: odd cell levels >= 33.58 g, even >= 19.07 g, mirror-only composites carry twisted charge 0 against the light's 1) and `[PASS] E4 [E]` (condensation wins over hybridisation for g > 0.066, below the second-order bound g > 0.102 for the gapped mirror phase, so wherever the mirror is gapped the doublers are released).

Against measurement, as an estimate: at least 4 left- and 4 right-handed weak-doublet tastes per family gives N_nu >= 12 at N = 3, against 2.984 +- 0.008, plus full-strength right-handed charged currents. The induced change of the light velocity at 1 TeV is below 6e-64.

## Repair candidate, not adopted

A light-copy term mu(1 - S(K)^2) linking K and K + R, staggered over blocks and so read one rung up, gaps exactly the six X and M doublers with gap mu 8/9 and keeps Gamma, R and the decoupling theorem. After it the light content is Gamma plus the R-point partner. Gapping that partner remains open; the anomaly-allowed N = 0 mod 3 is necessary but not sufficient for it.

## Boundary

Supplied: H', which copy is the mirror, the mirror terms (the pair square and the stand-ins used here, the one-block top form and the 1+1D pair hop, all copy-selective with a unique symmetric ground state and no bilinear condensate), g and mu, the 1+1D Wilson-type mixing (chosen to mimic the block corners, not derived), the (4,2) content, SU(2)_e as the weak group, the twist k = 2 and a = 3 Planck lengths. Cited: Nielsen-Ninomiya, anomaly matching and Golterman-Shamir, whose assumptions were not checked for this candidate beyond the endpoint. Notes that assume two light tastes per family after mirror gapping are narrowed: without the repair term there are eight. The register's claims of exact chirality and V - A are not supported here. No chiral light spectrum is established.
