---
claim_id: relays_on_the_spin_three_halves_margolus_tick_follow_born_odds_but_burn_and_turn_misses_the_stress_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied spin-3/2 Margolus tick (one mode per site, W(mu) on even then odd 2^3 blocks), an independent construction confirms unitarity, 24/24 rotation covariance, the band formula and two Dirac copies with c = 1/sqrt3; relays step n/2 block per half-tick, the group velocity is the odds-weighted mean step, and only the straight and reversal pairings are rotation covariant; minimal switching on the straight pairing keeps single-relay odds and joint two-relay odds exactly, while own-block marginal switching does not; the burn-and-turn record source fails to give eps v v on plane waves and changes on standing waves, while the canonical state-bilinear stress is linear and approaches eps v v at small K and mu; the pi-cone is massless for every mu. Finite diagnostics of a supplied model. No record source, adopted relay rule or physical reading of the pi-cone is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/relays_on_the_spin_three_halves_margolus_tick_follow_born_odds_but_burn_and_turn_misses_the_stress_2026_10_21.py
---

# Relays on the spin-3/2 Margolus tick follow the Born odds, but burn-and-turn deposits miss the stress

Claim type: bounded_theorem.
Primary runner: `scripts/relays_on_the_spin_three_halves_margolus_tick_follow_born_odds_but_burn_and_turn_misses_the_stress_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its relay, switching and record-source readings are tested here on one supplied tick. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the readings. The tick puts one mode on each site of Z^3 and applies W(mu) = cos(mu/2) W + i sin(mu/2) on even blocks {0,1}^3 + 2Z^3 and then on odd blocks shifted by (1,1,1). Here W is the edge hop of amplitude 1/sqrt 3, carrying the phase of the spin-3/2 coherent-state overlap of the two sites. Units: K is per block, w is per tick (two half-ticks), and velocities are in blocks per tick.

## Statement

1. The tick. W is Hermitian with W^2 = 1 and {W_a, W_b} = (2/3) delta_ab. The face holonomy is -1, and the 2 pi rotation acts as -1. Both half-ticks commute with all 24 rotations about an even and an odd block centre. Site inversion maps the even half-tick onto the odd one, so U = (I U_e)^2. The bands are cos w = cos^2(mu/2)(cos K_x + cos K_y + cos K_z)/3 - sin^2(mu/2), and each of +w and -w is fourfold. At low energy the eight states form an 8x8 Clifford set with a 4-dimensional commutant, so there are exactly two Dirac copies with c = 1/sqrt 3. No block-local copy symmetry exists: the common commutant of U(K) over K has dimension 2 at mu = 0 and 1 at mu > 0. The fourfold degeneracy therefore comes from U + U^dag being proportional to 1, not from a symmetry. The four rest states at w = +mu carry the cube-group representation E_(1/2) x E, so a 90 degree rotation mixes the two copies.
2. Relay geometry. Each site is a shared corner of one even and one odd block, whose centres differ by n(x) in {+-1}^3, so each half-step moves a relay n/2 block. The group velocity equals the odds-weighted mean step over the two half-ticks (Hellmann-Feynman). The step speed is sqrt 3 blocks per tick, which is 3c; the ratio of net distance to path length is at most 1/3, and the rest is zigzag that cancels. The only rotation-covariant pairings of incoming and outgoing directions are straight on (to the opposite corner) and reversal.
3. Born following. Minimal switching on the straight pairing keeps the single-relay occupation equal to the odds at every half-tick. For two entangled fermion relays, joint minimal switching keeps the joint odds exactly, while switching each relay on its own block's marginal odds does not. The price is that relays switch on most half-ticks: on plane waves the straight-pairing total variation is 0.79 to 0.98.
4. Record source, negative. Steps together with redraws give eps (mA mA + mB mB)/2 rather than eps v v, because the zigzag between half-ticks stays in the stress. Adding the switching chords with the best single coefficient leaves a 30 percent residual. No stress linear in the direction odds fits eps v v. On standing waves the burn-and-turn source changes, and for K along (1,1,0) its off-diagonal part flips sign, while the target does not.
5. Canonical stress. T^ij = c^2 sym(step^i x Re psi^* (-i grad_j) psi), averaged over the two half-ticks, is exactly linear in the state. It gives standing waves their plane-wave value and approaches eps v v as K and mu go to 0, with an O(K^2, mu^2) lattice error. It reads phase gradients, not relay records.
6. The pi-cone. All eight states at K = pi(1,1,1) sit at w = pi for every mu. The cone is massless and isotropic with speed c cos(mu/2). The energy reading in the candidate laws register assigns it about pi rad per tick, outside the domain of the switching law (at most 1/2). Different masses m1 and m2 on the two half-ticks give a K = 0 gap of (m1+m2)/2 and a pi-cone gap of |m1-m2|/2. A massive band has top group speed c cos(mu/2), on the body diagonals.

## Derivation

Item 1 is a direct construction: the coherent-state overlaps give the hop phases, and the Bloch reduction psi(2n+c) = e^{iK.n} phi(c) gives the even half-tick We and the odd half-tick D Wo D^dag, with D = diag e^{iK.c}. Item 2 follows from the block geometry and from the Hellmann-Feynman identity applied to the two legs a1 = W phi and a2 = D W D^dag a1. A covariant pairing must commute with the corner permutations of all 24 rotations, and only the identity and the corner inversion do. Item 3 holds because minimal switching (keep min(p_in, p_out) on each paired label and send the excess to the shortfalls in proportion) maps the incoming odds onto the outgoing odds by construction. Applied to the joint odds of two relays, it preserves them; applied to the product of marginals, it does not. Item 5 holds because the canonical stress is a sesquilinear form in psi whose cross terms between distinct momenta cancel in the sum over sites.

## Checks

The runner prints 32 PASS lines, and its output ends `TOTAL: PASS=32 FAIL=0`.

- `A1` to `A11` verify item 1:
  - the anticommutator holds to 2.2e-16;
  - holonomy and the 2 pi sign;
  - covariance of the 24 corner actions and of both half-ticks on 4^3 sites (1.2e-15);
  - U = (I U_e)^2;
  - the Bloch form against an 8^3 lattice (3.4e-15);
  - the band formula over 1600 K at four values of mu (2.2e-15);
  - no spatial doublers near w = 0 at mu = 0, with gap mu at mu > 0;
  - the Clifford set with commutant 4 (1.7e-9, from finite differences);
  - commutant dimensions 2 and 1;
  - the rest-state characters: C3 gives -1.00, and C4 and both C2 classes give 0.
- `B1` to `B9` verify items 2 and 3:
  - the n/2 step;
  - group velocity equal to the mean step on 40 modes (1.0e-9);
  - a zone-maximum speed of 0.577346;
  - the 109.47 degree turn of each edge hop;
  - exactly 2 covariant pairings;
  - for a single relay, total variation 2.2e-15 and chi2/dof 1.10 over 465 sites from 40000 samples;
  - for two relays, joint total variation 3.1e-15 against marginal 0.358;
  - straight-pairing total variation of 0.788, 0.967, 0.978 and 0.885 on four plane waves;
  - forward odds of 0.789 on both legs along an axis.
- `C1`, `C2` and `C3` are labelled FAILURE in the runner and print PASS. A PASS there means the failure of the burn-and-turn source was confirmed:
  - `C1` steps and redraws miss eps v v by a relative error up to 20.0;
  - `C2` the best chord coefficient is -0.1009 with residual 0.30;
  - `C3` the best stress linear in the odds leaves residual 0.72 over 300 plane waves.
- `C4` (two lines, for K = 2 pi(1,0,0)/12 and 2 pi(1,1,0)/12) checks that the standing waves are eigenstates (errors 1e-17 and 2e-17). For K along (1,1,0) the relay source's xx, yy and xy components are 0.189, 0.189 and 0.189 on the plane wave and 0.086, 0.086 and -0.086 on the standing wave. The canonical stress is 0.0607 for each component against a target of 0.0624.
- `C5` canonical linearity on a 6-mode superposition (6.9e-18).
- `C6` the canonical stress against eps v v: relative error 1.4e-4 at |K| = 0.05 and 2.2e-3 at |K| = 0.2 for mu = 0, and up to 1.4e-3 for mu = 0.1.
- `D1` pi-cone speed ratio 1.00000 at mu = 0, 0.3 and 1.0.
- `D2` the staggered-mass formula (8.9e-16), with K = 0 gap 0.200 and pi gap 0.700 for m1 = 0.9 and m2 = -0.5.
- `D3` checks only that each W(m) commutes with the 24 corner actions. The loss of U = (I U_e)^2 for unequal masses is stated in its label, not computed.
- `D5` top group speed ratio 1.000000 at mu = 0.1, 0.3 and 1.0.
- `D4` the pi-cone quasi-energy |w| = 3.1128 at mu = 0.1, a distance of 0.05 from the cone.

## What is supplied and the boundary

Supplied: the two partitions, the spin-3/2 polarisation and its orientation convention, mu, the Born reading of relay odds, and the register's same-site energy reading over a full tick. Forced, given the tick: the pairing, up to reversal. The canonical stress imports a momentum operator built from phase gradients and c^2 as a conversion factor. It is then a bilinear in the state and no longer a sum of relay records.

Not established: a record source built from relay deposits that reproduces eps v v; any adopted relay, switching or stress rule; and any physical reading of the pi-cone. The pi-cone is a massless species at quasi-energy pi for every mu. Since quasi-energy is conserved only modulo 2 pi, interactions could convert low-energy states into pairs of pi-cone states. Measured bounds on extra light species, on massless charged fermions and on electron stability are the relevant untested comparisons. They are not evaluated here.
