---
claim_id: link_dressing_gives_the_one_copy_block_tick_an_unprotected_additive_mass_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied one-copy 4^3 block tick S, its particle-antiparticle symmetry W U W = U^-1 and its Ginsparg-Wilson-type relation hold for every mass and forbid none; with W-compatible cube-phase links and the filled sea, one-loop dressing in supplied photon laws shifts the light level by about -0.142 e^2 per tick with the same sign in every variant, while a protected control tick gives zero; an overlap tick built from S is exactly chiral in magnetic backgrounds but quasi-local, and electric backgrounds and dynamical links give it a mass of the same order; no protected light copy, photon law or adopted tick is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/link_dressing_gives_the_one_copy_block_tick_an_unprotected_additive_mass_2026_10_21.py
---

# Link dressing gives the one-copy block tick an unprotected additive mass

Claim type: bounded_theorem.
Primary runner: `scripts/link_dressing_gives_the_one_copy_block_tick_an_unprotected_additive_mass_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It records a one-copy tick S on 4^3 blocks whose massless point is exact in form, but whose stability under link dressing was not established. This note dresses S with the register's links at one loop and asks whether any symmetry forbids the resulting mass. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither S nor the photon law.

## Statement

1. W U W = U^-1 holds for every species mass; it acts as CT, not as a chirality.
2. Any tick with W U W = U^-1 factors as U = W eps with eps a Hermitian involution, so D = 1 - U obeys W D + D W = D W D. This holds for every mass and constrains none.
3. Links that keep W are one phase per nested 2^3 cube. W maps a magnetic configuration to itself and an electric one to its negative, so the dressed theory keeps W.
4. In supplied photon laws the one-loop shift of the light level is -0.0259 e^2 (Coulomb, fixed by Gauss's law) plus -0.116 e^2 (transverse), about -0.142 e^2 = -1.8 alpha per tick, with the same sign in every variant tried.
5. An overlap tick built from S keeps one copy and W, is exactly chiral in every magnetostatic background, but is quasi-local, and electric backgrounds and dynamical links give it a mass of the same order.

## Derivation

Statements 1 to 3 are algebra on S. The block pseudoscalar G5 = i W IP is a Hermitian involution commuting with the 48 rotation lifts and anticommuting with IP and W, and G5 U(K) G5 = U(-K)^-1 holds automatically; G5 would be a chirality only if U(K) = U(-K)^-1, which S misses at O(1).

No-go (derived in the report, not run). Suppose a tick's gauge charges are block occupations and X commutes with the tick in every static electric background. At first order [X, Pi_b] = 0 for every block, so X does not depend on K in the block Bloch basis. If X protects the light mass it acts as a + b gamma5 (b != 0) on the light pair, and its eigensectors split the light Dirac point into Weyl points. For invertible rotation-invariant X, X pairs each E1/2g level at Gamma with an E1/2u level at the same w and W sends w -> -w; every L^3 block has an even number of E1/2g copies, so a second pair sits at quasi-energy 0 or pi. For general X the quasi-energy chirality sum rule (cited, Higashikawa-Nakagawa-Ueda 2019) gives the same. So no such tick has one particle-antiparticle-symmetric light copy with a protected mass.

Overlap tick. For any kernel H with W H W = -H, H_GW = IP - i W sign(i W H) is Hermitian and W-odd, D = 1 + G5 sign obeys the Ginsparg-Wilson relation, and X = (G5 - sign)/2 commutes with H_GW. This needs only {W, H} = 0, which holds in magnetostatic backgrounds; an electric potential commutes with W, so it falls outside the construction. The chiral projectors do not commute with Gauss's law, so this route opens no chirality for a tick.

## Checks

The runner gives `TOTAL: PASS=19 FAIL=0` in 25.4 s.

- 1: S has 4 light states at Gamma with W U W = U^-1 and IP U(K) IP = U(-K); the overlap algebra holds at mu = 0 and 0.04 (4.9e-15); |[G5, U]| = 1.00; |[W, site phases]| = 0.92.
- 2: the second-order Floquet formula matches exact many-body diagonalisation of a toy to 3.3e-6; the Ward identity holds to 3.6e-18; a static transverse field on a 12x4x4 torus gives exact pair means +-0.4112, +-0.4095 against the formula +-0.41036 eps^2.
- 3: in single static backgrounds the mass part moves by +0.4103 eps^2 (magnetic) and -0.1192 eps^2 (electric).
- 4: real-space 8^3 Coulomb equals the momentum sum (+0.023438); Coulomb eps_u = -0.025566, -0.025726, -0.025784 at n = 8, 12, 16, extrapolating to -0.02586; transverse delta_u = -0.11473, -0.11510, -0.11540, extrapolating to -0.1161, with delta_g = -delta_u and no imaginary parts; linear dispersion gives -0.0443 and six dynamical cube modes -0.3386; heavy-phase sums pi/2, pi/3, pi/6 give -0.0295, -0.0284, -0.0221.
- 5: the W-glide control tick P gives mass parts 0 and 1e-17, with only a common shift of -0.0234, so the machinery detects protection where it exists.
- 6: H_GW has 4 light states at 0 and 60 at +-2 at Gamma, no light state off Gamma on a 12^3 grid, block amplitudes 2.4e-1, 9.5e-3, 2.7e-3, 2.3e-4 at 1, 2, 4, 6 blocks (tick 8.1e-5 at 6), [X, H_GW] = 0 in random magnetostatic phases but |[X, Pi_block]| = 0.294, magnetic mass part 2.3e-11 and electric -0.2500 eps^2, and one-loop Coulomb +0.0705 and dynamical transverse +0.0232 e^2 in H_GW units.

Estimate (not a check). With a supplied site spacing of 5 Planck lengths and light speed 2 sites per tick, the electron's rest level is 4.19e-22 per tick against |delta m| of about 1.3e-2 (range 6.4e-3 to 3.3e-2 over the photon laws). The bare mass must cancel the shift to about 1 part in 3e19. With a species mass supplied per species this is a tuning, not a measured conflict; it becomes one under any rule that fixes the mass.

## Boundary

Supplied: S (light-copy projector, step pi/3, heavy phases pi/2 and pi/6), the calibration of e^2 to alpha through the long-range Coulomb law, the transverse photon law, the sea branch, one-loop perturbation theory, the overlap kernel and the site spacing. Forced: the cube-phase coupling, the absence of a protecting symmetry for S, the W-symmetry of the dressing, the Coulomb coefficient given Gauss's law, the common sign, and the overlap chirality being exact in magnetic and broken in electric backgrounds. Cited: the quasi-energy chirality sum rule for the general case of the no-go. The negative result stands: no symmetry of S forbids the additive mass, and the overlap route does not survive electric fields. No protected light copy, photon law or adopted tick is established.
