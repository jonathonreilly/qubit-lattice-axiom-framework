---
claim_id: the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Free-band census and removal tests for the light copy's zone-corner partners. Exact: on the CL-1 cube tick with copy mass (eps = 0.3, M = 0.2), the light copy's low content is one Dirac at K = 0 and the R = pi(1,1,1) partner sits at quasi-energy 2 eps, but the sublattice sign eps is not conserved and the copy mass is an eps-odd mass. On the step-pi/2 conserved generator H' = (i/2)[R_o, R_e], eps is conserved and there are 8 Weyl per flavour at K = 0 and R; each (eps, copy sign s) block at a node is one Weyl with chirality eps*s at K = 0 and -eps*s at R. The light copy (s = +1) holds, per eps sector, the zone-centre Weyl and one corner partner of the opposite chirality. Every eps-preserving mass at R pairs s = +1 with s = -1 (light with mirror). The only cell-local masses that anticommute with H' everywhere are eps-odd: with a 2-hop form factor (1 - B)/2 they gap the corner partners in light-light pairs and leave K = 0 untouched, but they break the charge that protects the light chirality. On one SU(4) block atom, the composite Phi = eps m^+m^+m^+/6 re-gaps a light level only through the anomalous G_(m,Phi), at 2 w lam/g; in a band that self-energy is a spin-blind node shift (Fermi pocket), not a mass. Composite spectra of extended mirrors, interacting 3D phases and Spin(10) are not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
runner: scripts/the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.py
---

# The light copy's zone-corner partners are vector-like only through the sublattice charge

Claim type: bounded_theorem.
Primary runner: `scripts/the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_2026_10_22.py`.

The [block-quartic note](THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md) showed that a block-local quartic gaps a Dirac mirror symmetrically. The cost is that the symmetric gap releases every light mode that was gapped only by pairing with the mirror. The [candidate-law register](CANDIDATE_LAWS.md) therefore asks for a rule that removes the light copy's zone-corner partners without the mirror. This note counts those partners exactly and tests three removals:
- the copy mass;
- a light-only corner mass;
- pairing with the mirror's three-fermion composites.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Statement

1. (CL-1 tick.) The tick has eps = 0.3, mu = 0 and copy mass M = 0.2. At K = 0, 4 modes are at zero: the light copy s = +1, one Dirac (1 L + 1 R per flavour). The other copy sits at +-M. At R = pi(1,1,1) the light copy is at +-2 eps and the heavy copy at +-(2 eps - M). The X point is at 0.198 and 0.398, the M point at 0.311 and 0.511. No zero lies off K = 0 (16^3 grid). The sublattice sign eps anticommutes with R_e, R_o and the copy-mass generator (1 - s)R_e = R_e - iR1R2R3, and it commutes with s. So the tick removes the corner partner by itself, with no mirror, and it conserves no chiral charge. The copy mass is an eps-odd Dirac mass on the s = -1 copy.
2. (Chiral generator.) H' = (i/2)[R_o, R_e] commutes with eps. Its only zeros are at K = 0 and R, with 8 modes each and Clifford velocities of speed 1/sqrt3. Its cell-local commutant is span{1, eps}, and tr(g5 X) = 0 on that commutant at both nodes. At the nodes the copy sign s commutes with the velocities. Each (eps, s) block is one Weyl, with chirality eps*s at K = 0 and -eps*s at R.
3. (Census.) Per flavour:
   - Light copy: G_L(eps+) and G_R(eps-) at K = 0, with corner partners R_R(eps+) and R_L(eps-) at pi(1,1,1).
   - Mirror: G_R(eps+), G_L(eps-), R_L(eps+), R_R(eps-).
   - When the mirror gaps, the released light modes are one Weyl per eps sector at pi(1,1,1), of the opposite chirality to that sector's light Weyl: 2 per flavour.
   - If instead every light mode is paired to the mirror, as in the block-quartic test, all 8 are released.
4. (Copy mass.) It gaps the mirror copy's Dirac at K = 0 and moves only the heavy copy at R. It gaps no light partner, and it is eps-odd. It is not enough.
5. (Light-only corner mass.) The eps-preserving masses at R span 4 dimensions, and every one of them pairs s = +1 with s = -1, so they are light-mirror pairings (Golterman-Shamir). The cell-local masses that anticommute with H' at every K span 2 dimensions, and all of them are eps-odd. One of them, X, has X^2 = 1 and [X, B] = 0, where B = (R_oR_e + R_eR_o)/2 is a 2-hop term with [B, H'] = 0. Then H' + lam (1 - B)/2 X squares exactly to H'^2 + lam^2 (1 - B)^2/4:
   - every R mode is gapped by lam, the light partners R_R(eps+) pairing with R_L(eps-), which is opposite chirality and light-light;
   - K = 0 keeps its 8 zeros.

   But the same X with no form factor gaps K = 0 by lam, pairing G_L(eps+) with G_R(eps-) of the light copy. The partners are vector-like among themselves only under the breaking of the charge that also makes the zone-centre pair vector-like. This is Nielsen-Ninomiya in exact form.
6. (Composites, one SU(4) block.) The block term is -g(Q + Q^+). At w = 0, G_m = G_Phi = 0 and |G_(m,Phi)| = 1/g. With a light l_a coupled by w l^+m + lam l^+Phi (exact diagonalisation, 256 states, w = lam = 0.05), the light level is:
   - with w alone: 1.2e-4 (released);
   - with lam alone: 9e-6 (released);
   - with both: 0.00498 g, against 2 w lam/g = 0.00500.

   In a band this self-energy is a number, not a matrix in spin. On a Weyl node it is a shift mu, with a zero of sigma.k + mu at |k| = mu: a Fermi pocket, not a gap. A Weyl gaps only with an opposite-chirality partner in its own eps sector (the mirror's R_L), or by a Majorana pair, and 16 x 16 has no Spin(10) singlet. Spin(10), Z4, eps and spin act alike on G_L and on its partner, so only momentum separates them.

## Derivation

- (1) The tick is computed at the eight inversion-symmetric points and on a grid. The eps relations hold because each hop and the three-hop product join opposite sublattices, while s is a product of four hops.
- (2) The velocities are finite differences of H' at the node, and g5 = i a1 a2 a3 / v^3. The commutant is the null space of [., H'(K)] over five random K. The chirality per block is tr(g5 P_(eps,s))/2.
- (5) The masses at R are the null space of {., a_i} together with [., eps]. The global masses are the null space of {., H'(K)}. Because B is a function of U = R_oR_e that commutes with H' and with X, the square follows.
- (6) Lehmann sums on the 16-state atom, plus exact diagonalisation of the 8-mode block.

## Checks

A1-A6 (census), B1-B4 (corner mass), C1-C4 (composites). TOTAL: PASS=14 FAIL=0.

## Clause count and law text

Tested candidate (law text, NOT proposed for adoption):

> "Corner term. Each species' generator carries lam (1 - B)/2 X, with B the symmetrised product of the two tilings' reflections and X the cell-local term anticommuting with the generator at every momentum; lam is a constant in proper units."

Smuggling check:
- Supplied: lam, and the choice of X within its 2-dimensional space.
- Chosen, not forced: the form factor (1 - B)/2, a 2-hop function of U that is 0 at K = 0 and 1 at R; uniqueness is not checked. Forced: X is eps-odd (B2).
- Hidden cost: X breaks eps, the only cell-local conserved label (A5). That label is what makes the light copy chiral (A6). So the term reopens the K = 0 Dirac mass. It would trade the corner doubler for a vector-like light copy.

Verdict:
- (a) The copy mass is insufficient.
- (b) A light-only corner removal exists exactly, but it necessarily breaks the light chirality.
- (c) Composite pairing is spin-blind on a Weyl. It moves the partner to a Fermi pocket and does not gap it.

No rule is adopted. The requirement now has an exact form. The light corner partner R_R(eps+) can be gapped only by an L Weyl of the same eps sector at R. On these bands, the only such Weyl is the mirror's R_L(eps+). So the mirror term must gap the mirror symmetrically at K = 0 while it stays Dirac-paired with the light copy at R. That needs a mirror interaction whose symmetric zero vanishes at R, an intermediate, momentum-selective phase: the register's open SMG route, and not a cell-local term.

## Boundary

- Free bands only: the CL-1 tick at one (eps, M) point and its step-pi/2 generator.
- The composite test is on one SU(4) block, with no dispersion. The spin-blindness argument assumes that G_(m,Phi) is spin-scalar at w = 0, as it is on the block.
- Not computed: the composite spectra of an extended symmetric mirror, any 3D interacting phase, Spin(10), twelve-turn covariance of X (the register states that no eps-preserving mass at R is turn-invariant), and links.
