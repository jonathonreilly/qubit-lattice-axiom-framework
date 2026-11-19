---
claim_id: a_definite_start_gives_the_record_arrow_but_no_initial_odds_give_the_spectral_tilt_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied staggered Margolus tick on small tori, odds stationary under a half-tick freeze the register's transport rule, so the empty start, the half-filled sea and any tick-eigenstate start give no moving records; a Haar-typical start has near-maximal odds entropy and no growth; a definite start (odds on one configuration) has zero odds entropy and rises to a volume law, giving an arrow; the only definite starts that favour no site are all-empty and all-full, both frozen; the support of a local operator grows exactly one site per half-tick in L-infinity distance; finite-range starts give an analytic structure factor with small-q index 0 or 2, and a doped Fermi sea gives index near 1. Comparisons with the measured tilt, baryon asymmetry and dark-matter ratio are estimates. No initial-odds law beyond the arrow, and no value of n_s, eta or the dark-matter ratio, is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_definite_start_gives_the_record_arrow_but_no_initial_odds_give_the_spectral_tilt_2026_10_21.py
---

# A definite start gives the record arrow, but no initial odds tested give the spectral tilt

Claim type: bounded_theorem.
Primary runner: `scripts/a_definite_start_gives_the_record_arrow_but_no_initial_odds_give_the_spectral_tilt_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and has no law for the initial odds. This note asks which initial odds the register's rules make natural, and what each candidate gives for the arrow, the large-scale fluctuation spectrum and relic abundances. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose a start. The candidates are:
- (a) all sites empty;
- (b) the half-filled sea;
- (c) Haar-typical odds;
- (d) any tick-stationary odds;
- (e) a definite start, with the odds on one configuration. This is either drawn uniformly (e1) or taken as the configuration the first records would read from the sea (e2).

## Statement

1. Stationary odds freeze transport. If the odds do not change over a half-tick, the register's transport rule keeps all the mass in place, so every configuration stays and records only repeat. Candidates (a) and (b) are frozen. A tick-eigenstate start (d) returns every tick, so its configuration at most oscillates with period one tick. In every case the probability of a move is at least the total-variation change of the odds.
2. Strict cone. The support of a local operator grows by exactly one site per half-tick in L-infinity distance. Along a body diagonal that is up to three times the light speed.
3. Spectrum fixed by the start. Number is conserved and the cone is finite. So if the start has finite-range or exponentially decaying correlations, S(q) stays analytic and even, and its small-q index is 0 or at least 2. A non-integer index such as 0.965 would need power-law correlations in the start itself. A Fermi surface is not finite range and gives a dominant |q| term, with index near 1.
4. The arrow. A Haar-typical start (c) has near-maximal odds entropy and no growth, so it has no arrow. A definite start (e) has zero odds entropy, which then grows. It reaches a volume law in block entropy, and its configuration keeps moving.
5. Symmetric definite starts. The only definite starts that favour no site are all-empty and all-full, and both are frozen. A definite start must therefore leave the choice of configuration to a measure.

## Derivation

Item 1: the transport rule moves mass only where the odds change. With unchanged odds the identity transport is optimal, and it forces every configuration to stay. Item 2: each half-tick is a product of commuting 2^3 cube unitaries, so one half-tick enlarges a support by at most one cube layer, and the bound is attained. Item 3: under a number-conserving circuit with a finite cone, finite-range correlations stay finite-range at every finite time. Their Fourier transform is then analytic, and number conservation and reflection symmetry remove the constant and linear terms unless the start has a nonzero q -> 0 limit. Item 5: the eight corners fall into four classes modulo (1,1,1), and the rotations permute these classes transitively. A site-blind definite start must therefore be uniform, that is, all-empty or all-full.

## Checks

The runner prints 17 PASS lines, and its output ends `TOTAL: PASS=17 FAIL=0` (19.7 s). Items 1 to 3 are stated in the runner's section A and checked numerically in sections B to D.

- Section B, a 16-site 4x2x2 torus with exact odds in the 2^16 Fock space at (mu, b) = (0.4, 0.3):
  - the Fock-space cube operators reproduce the exact Slater odds (1.5e-16 over 6 half-ticks and 12870 configurations);
  - (a) and (b) are frozen (largest total variation 2.5e-15);
  - (d) has half-tick total variation 0.669 and return error 7.1e-13;
  - (c) has odds entropy 0.955 ln D, unchanged;
  - (e1) and (e2) rise from 0 to late means of 0.670 and 0.725 ln D, with late move rates of at least 0.788 and 0.803;
  - the symmetric-start statement of item 5.
- Section C, exact Gaussian evolution:
  - the support reach after T = 1, 2, 3 half-ticks on an 8^3 torus is exactly T;
  - on a 12^3 torus the 4^3-block entropy per site rises from 0 to a mean of 0.634 (e1) and 0.637 (e2) after t >= 4, against 0.397 for the sea;
  - (e2) has exactly half filling (N = 864);
  - (e1) occupies the tick modes uniformly (mean 0.541, standard deviation 0.024, correlation with quasi-energy -0.000).
- Section D:
  - the Bloch construction matches the 512-site real-space tick (S(q) 0.091754 in both);
  - on 80^3 sites the local index is 1.991 for the gapped sea and 1.969 for the massless sea, with no linear term;
  - the uniform start is exactly white (index 0);
  - a doped sea at filling 0.560 gives index 1.177 with linear share 0.854.
- Section E, estimates against measurement. Every PASS here records that a candidate fails.
  - No candidate gives the measured tilt n_s = 0.9649 +- 0.0042. Index 1 is 8.4 sigma off, index 0 is 230 sigma off and index 2 is 246 sigma off.
  - Every rule conserves each species number, so eta is fixed by the start. (e1) gives |eta| of about 4e-92, with sign domains at lattice scale, which the absence of antimatter domains excludes; (e2) gives exactly 0. Both are against a measured 6.1e-10.
  - Under (e1) a never-thermalised link-free species needs m_c of about 0.55 eV/f. That is hot dark matter, which Lyman-alpha bounds exclude unless f is about 1e-4 or less.
  - Counting fractions inside 1 sigma of the dark-matter ratio 5.364 +- 0.065 (16/3, 27/5, 38/7, 43/8) occur at about the rate chance gives (2.8 expected), so they are not evidence.

## What is supplied and the boundary

Supplied:
- the tick at (mu, b) = (0.4, 0.3) and (0, 0.3);
- the negative-quasi-energy branch as "the sea";
- the reading of matter density as site occupation, with the fixed-time spectrum P(k) ~ k^n_s;
- the unit map a = sqrt(8 pi) l_P and standard adiabatic expansion;
- the uniform measure over starting configurations in (e1). The axiom that no possibility is privileged motivates this measure but does not force it;
- all measured numbers.

Established: a definite start gives the arrow within this family.

Not established:
- any initial-odds law beyond the arrow;
- the measured tilt, which would need correlations in the start at all ranges or a cone that grows;
- the baryon asymmetry, which would need B- and CP-violating terms;
- the dark-matter ratio;
- record statistics for the vacuum under a definite start, which were not computed.
