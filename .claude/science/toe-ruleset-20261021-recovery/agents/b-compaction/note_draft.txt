---
claim_id: the_staggered_margolus_term_is_a_universal_time_step_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied staggered Margolus tick with half-tick unitaries V(mu/2 +- b), the bands are cos w = A S - (cos2b - cos mu)/2 with c = cos(b)/sqrt3 as mu -> 0; the tick is exactly exp(+i(eps+mu/2)W_o) exp(-i(eps-mu/2)W_e) with eps = pi/2 - b, so b sets a time step and bandwidth; a supplied Yee link leapfrog matches the massless b-band at every K exactly when its Courant number is cos(b)/sqrt3, is a Jordan block at R when b = 0, and with one shared b keeps photon decay closed on the sampled grid while a per-species b opens it; a pi-cone particle-hole pair sits at -4b mod 2pi and two band-top pairs wrap the quasi-energy circle iff b <= pi/4; three structural clauses of the register follow as theorems. Rates and bounds from measured numbers are order-of-magnitude estimates. The value of eps, the vacuum filling and any adopted register text are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_staggered_margolus_term_is_a_universal_time_step_2026_10_21.py
---

# The staggered Margolus term is a universal time step

Claim type: bounded_theorem.
Primary runner: `scripts/the_staggered_margolus_term_is_a_universal_time_step_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its supplied Margolus tick on Z^3 places one fermion mode per site, uses the spin-3/2 edge hop W on 2x2x2 cubes, and runs two partitions offset by (1,1,1). Species apply V(a) = cos a W + i sin a with a = mu/2 +- b. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose b. This note asks what b is for. The answer is that b is exactly a time step, and that it works when one value is shared by every species. Its role is to narrow the band so that no small group of excitations wraps the quasi-energy circle. Gapping the pi-cone alone is not enough.

## Statement

1. Bands and speed. All eight bands obey cos w = A S - (cos 2b - cos mu)/2, with A = (cos 2b + cos mu)/2 and S the mean of cos K_a. The exact speed at K = 0 is c^2 = (A/3)(mu/sin mu), which gives c = cos b / sqrt 3 as mu goes to 0.
2. Exact rewrite. V(mu/2 + b) = i exp(-i(eps - mu/2)W) and V(mu/2 - b) = -i exp(+i(eps + mu/2)W), with eps = pi/2 - b. The tick is therefore exp(+i delta_o W_o) exp(-i delta_e W_e). The limit b -> pi/2 is continuous time with H = eps(W_e - W_o) - (mu/2)(W_e + W_o). The band top at R is pi - 2b = 2 eps.
3. Links. The Yee leapfrog band of a supplied link update is sin^2(w/2) = (3C^2/2)(1 - S). It equals the massless b-band at every K exactly when the Courant number is C = cos b / sqrt 3. At b = 0 (C = 1/sqrt 3) the photon is a Jordan block at R, with norm growing linearly in ticks; any b > 0 makes it diagonalisable and bounded. At equal K, 1 - cos w_f = (1 - cos w_gamma) + (1 - cos mu)(1 + S)/2, so mass is the only difference between the fermion and photon bands.
4. One b for all species. With a universal b, photon decay into a fermion pair stays closed on the sampled grid. With a per-species b (fermion 0.3, photon 0) it opens. A per-species b also leaves the register's symmetric-stress clause with no common metric. With a universal b the only spread is mu^2 (1/6 - 1/(4 cos^2 b)) + O(mu^4), so the clause is exact only for massless sources.
5. Arcs. At b = 0 all eight states at R sit at quasi-energy pi for every mu, a massless pi-cone. For b > 0 the upper band fills [mu, pi - 2b], with its top at R. A particle-hole pair at R then sits at -4b mod 2 pi, on the opposite side of 0 from the 0-cone excitations at +2 mu and above. Quasi-energy is conserved only modulo 2 pi, so a small b does not decouple the pi-cone. Two band-top pairs wrap the circle exactly when b <= pi/4.
6. Structural clauses. Three clauses follow as theorems. Every nearest-neighbour bond lies in exactly one cube of exactly one partition. The translations preserving the pair of tilings are 2Z^3 and (1,1,1) + 2Z^3; a 90 degree turn about a cube centre preserves it, while one about a site does not. An equal-edge Hermitian hop squares to 1 exactly when every face carries phase -1, and the spin-3/2 W has this.

## Derivation

Each half-tick is cos a W + i sin a = W e^{iaW}, since W^2 = 1. Substituting a = mu/2 +- b and eps = pi/2 - b turns the prefactors into +-i and leaves single exponentials in W, which gives item 2. The Bloch tick reduces to 2x2 blocks built from two reflections with determinant 1; their trace gives item 1. Item 3 compares two closed-form bands in S. Item 5 counts on the circle: the gaps at 0 and pi bound the same two arcs. If the vacuum fills one arc, the excitation range is [2 mu, 2 pi - 4b] mod 2 pi, and m band-top pairs at zero total momentum wrap the circle when 2m(pi - 2b) >= 2 pi.

## Checks

The runner prints 19 PASS lines, and its output ends `TOTAL: PASS=19 FAIL=0` (0.3 s).

- `1a` the band formula (2.2e-15).
- `1b` the speed on axis, face and body directions (relative deviation 2.5e-9), with c(0.3)/c(0) = 0.955336.
- `2a` the exponential rewrite (2.2e-15).
- `2b` the continuous-time limit (8.7e-13 at eps = 0.001).
- `2c` the band top equals 2 eps (1.8e-15).
- `3a` the Yee band (5.3e-15).
- `3b` an exact band match over 800 K at three values of b (1.2e-14).
- `3c` at b = 0 the norm ratio |M^1000|/|M^100| is 10.00; at b = 0.3 the largest |M^n|/|M| is 1.352.
- `3d` the equal-K identity (8.9e-16).
- `3e` for a universal b the smallest relative decay margins over 60k K are 1.5e-4, 6.3e-4 and 1.8e-3 at b = 0.3, 0.9 and 1.3. These are positive on a finite grid.
- `3f` for a per-species b the margin is -0.045.
- `4a` the spread of the metric alpha is 0.0291 for b = 0 against 0.3.
- `4b` the mu^2 offset, -5.009e-4 against the formula's -5.009e-4.
- `5a` the b = 0 pi-cone.
- `5b` the pi-pair equals -4b at b = 0.3, 1.0 and 0.0073.
- `5c` the smallest number of wrapping pairs: 2 for b up to pi/4 and 3 just above, rising to 43 at b = 1.53.
- `6a` the bond count on a 6^3 torus.
- `6b` the translations mod 2 are (0,0,0) and (1,1,1).
- `6c` the face-flux condition (6.7e-15), consistent on 300 random hops.

Section 7 of the runner prints arithmetic with measured numbers, labelled as estimates. It makes no checks.
- With per-species b, the survival of 1.4 PeV photons gives b_e < 7.30e-10; the same argument gives b_mu < 1.5e-7 and b_p < 1.3e-6.
- With per-species small b, a solar-core rate of about 9e45 erg/s compares with L_sun = 3.8e33 erg/s. This needs quantised links.
- Wrap events inject 1.33e19 GeV each. A crude vacuum-stability bound asks for eps of about 0.037 or less. The setting b = (pi - 1/2)/2 (eps = 0.25) gives about alpha^13 per cell-tick and fails that crude bound.
- With universal small eps, the pi-cone states sit near 4.2e18 GeV, with thermal production of order exp(-264) at 1.6e16 GeV.

## What is supplied and the boundary

Supplied:
- the tick, b and mu;
- the Yee placement of links;
- the Fock filling of one arc;
- the identification of quasi-energy with energy times tau, and the unit map a = sqrt(8 pi) l_P;
- quantised links for every rate estimate, and all measured numbers.

That the reflection W is forced by covariance is taken from the register, not rederived here; only the face-flux condition is rederived.

Not established:
- the value of eps. It is one supplied number, and no law fixes it;
- the vacuum filling;
- any adopted register text, including dropping clauses that item 6 shows to be theorems;
- charged, stable band-top relics, which remain an untested prediction.

If links are only classical responses, the vacuum wrap channel estimated above is absent.
