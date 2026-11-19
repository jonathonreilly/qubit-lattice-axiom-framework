---
claim_id: one_light_dirac_copy_on_four_cubed_blocks_and_the_protection_particle_hole_trade_off_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For covariant block unitaries with one mode per site, 2^3 cubes give a light Dirac only with two copies or a star of at least 3; on supplied 4^3 blocks with inversion a glide built from the register's reflection W makes the light pair massless without tuning, but a one-copy tick cannot have both that protection and an exact w -> -w symmetry; a supplied particle-hole-symmetric 4^3 tick has one light Dirac copy with c = 0 and its zero exact only in its form; no adopted tick, stability under link dressing or chirality is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_light_dirac_copy_on_four_cubed_blocks_and_the_protection_particle_hole_trade_off_2026_10_21.py
---

# One light Dirac copy on 4^3 blocks and the protection versus particle-hole trade-off

Claim type: bounded_theorem.
Primary runner: `scripts/one_light_dirac_copy_on_four_cubed_blocks_and_the_protection_particle_hole_trade_off_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update on 2^3 cubes gives two copies of each light Dirac species. This note checks why, what a 4^3 block can do, and what the mass zero of a one-copy tick costs. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the 4^3 ticks used, and give proper rotations only, so inversion is supplied.

## Statement

1. On 2^3 cubes with one mode per site, a site action that is a permutation with phases, the same unitary on every cube and exact covariance, every covariant block unitary gives a light Dirac only as two copies (at Gamma and R) or on a star of at least 3 momenta.
2. On a 4^3 block with inversion, a glide built from the register's reflection W makes the light g/u pair at Gamma massless for every covariant block, with no tuning.
3. A one-copy tick cannot have both that protection and an exact w -> -w symmetry. Without the second, the light cone generically has a particle-antiparticle asymmetry w+ + w- = 2 c k^2 with c nonzero.
4. A supplied particle-hole-symmetric tick S on 4^3 blocks has one light Dirac copy, c = 0 exactly, and speed sin(eps)/sqrt 3 blocks per tick. Its mass zero is exact in its form but not enforced by a symmetry.

## Derivation

2^3 cubes. With inversion, every spinorial site action gives G3/2g + G3/2u at both invariant momenta. With rotations only, the spin-3/2 corner gives 2 G3/2, and the m = +-1/2 corners give E1/2 + E5/2 + G3/2. E1/2 x E5/2 contains neither a mass nor a k-linear term, so one E1/2 cannot form a massive Dirac. Every non-invariant momentum of the 2Z^3 zone has a star of at least 3 points. Nothing is assumed about the block unitary itself; the result fails only if the 2Z^3 translations are broken.

Multiplicity. On an L^3 cell with inversion and L = 2m, the E1/2g multiplicity at Gamma is m(m-1) + 2 C(m,3), which is always even.

The register's W on 4^3. On the 2^3 cubes nested in a 4^3 block, W commutes with the rotations and the (2,2,2) translation. It is odd under exactly one of the two inversion site-action classes, which no site-diagonal operator can be.

Opposite-step structure. If the odd half-tick is the image of the inverse even one under a tiling-exchanging map, both such maps fix no site mod 4, every trace tr(g M) vanishes, and the two E1/2g levels at Gamma come as {w, -w}. One light copy then brings a second light copy or a copy at pi.

Glide. Let the odd half-tick be the (2,2,2)-translate of W V W. Then Sigma = T_(2,2,2) W V commutes with U(K) and Sigma^2 = exp(-4i K.(1,1,1)) U(K). Sigma(0) anticommutes with inversion, so every Gamma level is a g/u pair and the light pair is massless for every covariant V. A step asymmetry eps -+ mu/2 breaks Sigma and gives Gamma levels +-mu.

Doubling. If one symmetry makes the light g and u levels coincide and another maps w to -w, the E1/2g level set is closed under negation. Its size is even, so a second E1/2 pair sits at 0 or pi.

## Checks

The runner gives 27 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- The 2^3 representation content, tensor facts and star sizes [1, 3, 6, 8, 12, 24]; E1/2g multiplicities 0, 2, 8 for L = 2, 4, 6.
- On 4^3, the rotation lifts with a central inversion close into O_h' on 64 sites to 1.3e-14, and the content is E1/2g and E1/2u twice each.
- Opposite-step blocks: max |tr| 0, and the two E1/2g levels are {w, -w} to 4.4e-16.
- Glide: Sigma commutes with U(K) and squares correctly to 8.0e-16; g and u levels coincide to 8.9e-16 over 3 random blocks; with glide and a W-odd generator the light points sit at {w, -w} to 3.3e-16.
- Protected tick P (eps = 7 pi/12, phi = pi/12): 4 light states at Gamma, cone speed 2.230, c = -12.62. The cone bends back to w = 0 at |K| = 0.1758, against v/|c| = 0.1768. Tuning c to 0 within the glide class opens an exact zero at K = (0.708, 0.479, 0.216).
- Tick S: W U(K) W = U(K)^-1 to 6.1e-15; on an 8^3 torus it is unitary and covariant to 5.1e-15. Gamma holds 4 light states, 30 at +2 pi/3 and 30 at -2 pi/3. The cone is isotropic with speed 2.0000 sites per tick, c = 4.4e-11, and speed ratios to sin(eps)/sqrt 3 of 0.99999. A Lipschitz box cover of the O_h wedge (304 boxes, ||dU/dK_i|| <= 2.522) shows nothing within 0.35 of pi, nothing within 0.12 of 0 for |K|_inf >= pi/32, and exactly 4 states with |w| < 0.5 inside. A small covariant W-odd term keeps the symmetry but moves the light pair by 8.5e-3, so the zero is not protected.
- A previously tuned one-copy tick is massless at m0 = 0.29282 with speed 0.6666, and a box cover (336 boxes) confirms one light copy. All its other Gamma levels lie in [1.17, 1.98], so it has no w -> -w symmetry, and c = -0.0578.

A scan of about 5000 parameter points found no fully gapped protected one-copy tick. That every glide-protected one-copy tick recrosses the light level is a conjecture, not proved here.

## Against measurement (estimates)

With E = v|k| +- c k^2 and a supplied spacing a = 5 l_P, eta = 2 (c/v)(a/l_P), against Crab synchrotron and vacuum-Cherenkov bounds of roughly |eta| < 1e-7. The protected tick P gives eta = -57 and the previously tuned tick -0.87, both excluded. S has c = 0 by symmetry and no conflict. Measurement therefore favours the particle-hole-symmetric tick, whose remaining issue is that its mass zero is a tuning.

## Boundary

Supplied: the 4^3 zoom, inversion and its W-odd site-action class, the light-copy direction, the heavy phases, the projector form of the block generator (not nearest-neighbour inside the block) and eps. Not checked: stability of the zero under link dressing by the response law, and the link dressing of the block projectors. S is vector-like. No adopted tick, stability under link dressing or chirality is established.
