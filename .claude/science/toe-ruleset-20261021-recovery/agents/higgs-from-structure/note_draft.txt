---
claim_id: the_zone_corner_pairing_is_electroweak_neutral_and_its_only_doublets_carry_two_units_of_b_minus_l_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For one 16 per family and its mirror on the CL-1 cube band and its step-pi/2 generator H', the edge registers and the tick's two copies: (A) exact weights: every colour-singlet SU(2)_L-doublet component of 16bar x 16 (a Dirac light-mirror bilinear) is lepton x lepton with B-L = +-2 (Y = +-1/2 or +-3/2); every one of 16 x 16 (a pair) has B-L = 0 and Y = +-1/2; no root of so(10) is a colour-singlet doublet. (B) At R = pi(1,1,1) each (eps, s) block is one Weyl of chirality -eps*s, so a light-mirror Lorentz scalar inside one eps sector is Dirac (16bar x 16) and a same-chirality one is an eps-odd pair (16 x 16). The eps-preserving corner masses (dim 4) are all light-mirror and their eigenmodes are exactly half mirror. The copy sign is not conserved off the nodes and the cell-local commutant of H' is span(1, eps), so no update rotates light and mirror separately; a gauge-invariant corner pairing is EW-neutral and the Spin(10)-singlet one breaks no continuous symmetry. (C) Conditional on separate light and mirror rotations at R (not in the laws): the Lbar n^c direction gives an exact colour- and charge-safe angle with v = f sin(theta/2); every term with an odd number of these doublets has Z4 = i^(B-L) charge 2, so they give no fermion a mass at any order; gauge loops align at theta = 0. (D) Edge dressing leaves the bilinear's quantum numbers unchanged; the copy factor's commutant is u(1) + u(1); the B-L = 0 doublets sit in the 10, whose S^9 angle forces v = f. Estimates (f at the corner gap, v/f ~ 1e-16) are separate. No structure of the laws gives a light B-L = 0 doublet; the tested rule fails the gate."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
  - the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_bounded_theorem_note_2026-10-22
  - transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_bounded_theorem_note_2026-10-22
  - a_light_pseudo_goldstone_higgs_needs_inserted_content_and_its_rule_moves_the_hierarchy_to_the_top_coupling_bounded_theorem_note_2026-10-22
  - supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_bounded_theorem_note_2026-10-22
runner: scripts/the_zone_corner_pairing_is_electroweak_neutral_and_its_only_doublets_carry_two_units_of_b_minus_l_2026_10_22.py
---

# The zone-corner pairing is electroweak-neutral, and its only doublets carry two units of B - L

Claim type: bounded_theorem.
Primary runner: `scripts/the_zone_corner_pairing_is_electroweak_neutral_and_its_only_doublets_carry_two_units_of_b_minus_l_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its owner decision 3 is open: a light Higgs seemed to need 8 new Weyl modes per cell, and the [AX-6 note](A_LIGHT_PSEUDO_GOLDSTONE_HIGGS_NEEDS_INSERTED_CONTENT_AND_ITS_RULE_MOVES_THE_HIERARCHY_TO_THE_TOP_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) found that supplying them fails the anti-smuggling gate. This note asks whether a structure the laws already contain gives a scalar Y = 1/2, colour-singlet doublet as a composite or collective mode, with no content named. Three candidates are tested:
- (a) a colour-singlet light-mirror bilinear at the zone corner R = pi(1,1,1). The [light-partner-gap note](THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md) shows chirality needs this pairing anyway. If its condensate were the weak doublet, chirality and electroweak breaking would be one mechanism;
- (b) a matter bilinear dressed by an edge register;
- (c) a pair across the tick's two copies.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Statement

A. Weights (exact rationals; 16 = (+-1/2)^5 with an odd number of minus signs, B-L = (2/3)(w1 + w2 + w3), T3L,R = (w4 +- w5)/2, Y = T3R + (B-L)/2).

1. Exact. These weights give q, u^c, d^c, L, e^c, n^c with their hypercharges.
2. Exact. No root of so(10) has zero colour weight and T3L = +-1/2. So no Goldstone of any Spin(10)-breaking vacuum is a colour-singlet doublet (mirror-condensate B2, rederived).
3. Exact. In 16bar x 16 (Dirac bilinears psi^dag chi), every colour-zero component with T3L = +-1/2 comes from lepton x lepton, so it is a colour singlet. Its (Y, B-L) is (+1/2, +2), (+3/2, +2) or their negatives. The Y = 1/2 doublet is Lbar n^c, with B-L = 2. No Dirac bilinear is a B-L = 0 doublet.
4. Exact. In 16 x 16 (pairs psi chi), the colour-singlet doublets are L e^c, L n^c, q u^c and q d^c, all with B-L = 0 and Y = +-1/2. These are the Higgs-type doublets.

B. The band at R (CL-1 cube hops; H' = (i/2)[R_o, R_e]).

1. Exact. H'(R) = 0, and each (eps, s) block at R is one Weyl of chirality -eps*s. Within one eps sector, the light (s = +1) and mirror (s = -1) corner modes have opposite chirality. So their Lorentz-scalar bilinear is Dirac, with internal content 16bar x 16 (A3). A same-chirality light-mirror scalar pairs opposite eps sectors: it is an eps-odd pair, with internal content 16 x 16 (A4).
2. Exact. The eps-preserving masses at R span dimension 4, and every one is purely s = + to s = -. This rederives light-partner-gap B1: the corner pairing that chirality needs is a light-mirror Dirac term. Its eigenmodes are exactly half mirror, so the corner modes feel the mirror term at full strength.
3. Exact. The commutator of s with H'(K) is up to 1.53 off the nodes and vanishes at the nodes. The cell-local commutant of H' is span(1, eps), and the CL-1 hops anticommute with eps. So no update rotates light and mirror separately. The internal symmetry of the free generator is at most U(16N)_eps+ x U(16N)_eps- (for H') or U(16N) (for the CL-1 tick), and either one rotates the light and mirror corner modes together. Hence:
   - a gauge-invariant corner pairing is a sum over the six SM multiplets of w_f f^dag f', with Y = 0 and T = 0, so it is electroweak-neutral (answer to (a): no);
   - the Spin(10)-singlet pairing commutes with every internal rotation and breaks no continuous symmetry, so its doublet fluctuations (A3) are not Goldstones.

C. Conditional coset (assumes separate light and mirror rotations at R, i.e. a conserved copy sign, which the laws lack by B3).

1. Exact. Take Sigma = exp(i theta X) with X = |n^c><nu| + h.c., the neutral Lbar n^c direction. Colour and charge stay unbroken at every theta, and m_W^2(theta)/m_W^2(pi) = sin^2(theta/2). So v = f sin(theta/2), and B-L is broken. Unlike the 10's S^9, this coset does have a colour-safe misalignment angle.
2. Exact. A Yukawa-type term needs an odd number of doublets times a light pair with half-integer isospin, which by A4 has B-L = 0. Each corner doublet carries Z4 = i^(B-L) charge 2, so every such term has charge 2 and is forbidden at every order. There are 16 weight pairings for a B-L = 0 doublet and 0 for the corner doublet. The corner doublet gives no fermion a mass, and its vev breaks the Z4 to Z2 (two vacua).
3. Exact algebra; the sign is supplied. The gauge-loop invariant is a sin^2(theta/2) + b sin^2 theta, with a = 1.70 and b = 0.28. With the standard positive vector-like sign, the vacuum aligns at theta = 0. Misalignment needs a Z4-odd source, and the laws have none.

D. Edges and copies.

1. Exact. Edge registers are gauge singlets with no B-L. On matter x edge the gauge generators are T x 1, so an edge-dressed bilinear has its matter bilinear's Casimir, Y and B-L. Candidate (b) reduces to A3/A4, as weak-scale B1 found for links and rishons.
2. Exact. In the copy factor, the commutant of the copy mass diag(0, M) is u(1) + u(1), which is abelian and has no doublet generator (ax6-higgs A3, rederived). Both copies carry the same 16, so copy-pair bilinears are 16bar x 16 or 16 x 16, with the s = -1 member at M. Candidate (c) reduces to A3/A4 and to the copy mass scale.
3. Exact. The B-L = 0 doublets (A4) sit in the pair-square 10. On n = cos(theta) t + sin(theta) h, the W sum is sin^2(theta)/2 and the colour-breaking sum is (4/3) cos^2(theta), so unbroken colour forces v = f (mirror-condensate C3, rederived).

## The dichotomy

The laws' light-mirror bilinears split two ways:
- Dirac type (eps-even): this is the type chirality needs at R. Its doublets carry B-L = +-2, so they can never give a Yukawa-type mass.
- Pair type (eps-odd): this type has the right B-L = 0 doublet. But the only continuous symmetry the laws give it is Spin(10), whose 10-vacuum angle runs to colour breaking (v = f).

The larger rotations that would make a pair-type doublet a pseudo-Goldstone (u(16)/so(10)) are broken at the cell scale. The mirror term breaks them, and by B2 the corner modes are half mirror. So the corner pairing cannot unify chirality with electroweak breaking.

## Estimates against measurement

| quantity | result | comparison |
|---|---|---|
| corner gap (the scale f of any corner condensate) | 2 eps0 per tick, i.e. the cell scale, M = 2.44e18 GeV | v = 246 GeV |
| v/f the conditional coset needs | sin(theta/2) of about 1e-16, FITTED and Z4-odd | no source in the laws |
| fermion masses from the corner doublet | 0 at every order (C2) | m_t = 172.6 GeV: contradicted |
| m_H, v/f | not computed: no input without a fitted number exists | 125.1 GeV |

## Candidate rule text (tested; FAILS the gate; not adopted)

> "AX-7 (corner copy charge). At each zone-corner node the copy sign is conserved, so light and mirror corner modes rotate separately; the corner pairing is their spontaneous condensate, and the weak doublet is its pseudo-Goldstone."

Gate report.
1. Measured numbers chosen: sin(theta/2) of about 1e-16 (FITTED).
2. Observed structure inserted by name: none. The rule constrains only an update label, so it passes this criterion.
3. Prediction it was not built for: no Yukawa-type mass from the doublet (C2), which contradicts every measured fermion mass. Also Z4 breaking, which allows Majorana-type terms and makes domain walls. The rule is FALSIFIED.
4. Axiom bent: Admissibility, through CL-1's hops (the copy sign is not conserved off the nodes, B3, consistent with PR #9963 "the copy sign is exact only at rest").

Result: FAIL.

Smuggling check.
- Supplied: the vector-like vacuum-alignment sign; the H' generator, used for the eps bookkeeping (not adopted; the CL-1 tick breaks eps); eps0 = 0.3 for the gap estimate.
- Forced: A1 to A4, the B1 chirality table, B2 and B3, the C1 angle function, the C2 selection rule, D1 to D3.

## Notes used or contradicted

- light-partner-gap (PR #9993): B1 and B2 rederive its census and its light-mirror corner masses. New here: the corner pairing's internal content and its EW neutrality.
- mirror-condensate-ew (PR #9974): B2 and C3 are rederived (A2, D3). Its B3 (B-L-neutral doublet generators only in light-mirror mixing) is sharpened: in Lorentz-scalar terms they are the eps-odd pair, not the corner Dirac pairing.
- weak-scale (PR #9969): B1 (registers centre-blind) is extended to edge dressing (D1).
- ax6-higgs (PR #9999): A3 (the copy commutant) is rederived (D2). Its conclusion stands: a light doublet needs content or a new symmetry.
- proton-theta (PR #9925) and neutrino-mass (PR #9981): the Z4 = i^(B-L) is used in C2.
- main: HIGGS_MASS_FROM_AXIOM_NOTE (legacy, a staggered taste-curvature scale with v supplied): not used, not contradicted.

## What a light-Higgs law must now do

1. Supply a continuous symmetry with a B-L = 0, colour-singlet doublet generator (light-mirror pair mixing, eps-odd) that stays exact or nearly exact below the cell scale, even though the mirror term breaks u(16) to so(10) and the corner modes are half mirror.
2. Or break the Z4 = i^(B-L) by a lepton-number-2 condensate, so that a B-L = +-2 doublet can couple, while keeping the measured neutrino bounds.
3. In either case, fix v/f without a fitted angle.

## Boundary

A, B, C1, C2 and D are exact weight algebra or exact linear algebra on the stated bands. C3 is exact algebra with the alignment sign supplied. Not computed: interacting corner dynamics, any binder in the eps-odd pair channel, 3D lattice phases, and links. Nothing here excludes a doublet that some future rule derives from site structure.
