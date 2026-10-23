---
claim_id: a_rung_separated_mirror_protects_the_light_cone_but_a_rung_local_mirror_gap_releases_the_fine_partner_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Free two-rung model (a fine Z^3 rung and one coarse rung on 2^3 blocks), each rung carrying the same cone-rule band (Karsten-Wilczek type, nodes 0 (+1) and R = pi(1,1,1) (-1), coarse hop 1/2 so the cone speeds agree), coupled by a nested block reading. Exact: on one rung the mirror cone sits on the same rung (charges sum to zero; a random 0.05 change keeps both); nested block rows overlap by 2^(-3/2) per rung and weight a fine plane wave by prod cos^2(q/2) (uniform rows) or prod sin^2(q/2) (staggered rows). With the same rule on both rungs the uniform reading couples same-chirality cones (zeros remain, no pair removed); the staggered reading Dirac-pairs the fine R cone with the coarse zone-centre cone A (gap w, coupling matrix fixed by the SU(2) lift of the polar rotation between the cone frames; the identity leaves a nodal ring) and leaves the fine zone-centre cone exactly decoupled (H psi_L = 0, vertex ~ q1 q2 q3). The two remaining zeros are the light cone on the fine rung (coarse weight 0) and the mirror B near the coarse corner (coarse weight 0.879), opposite chirality. Light-B bilinears are forbidden by coarse crystal momentum for every coarse-translation-invariant term (2e-16), while light-fine-partner and light-A bilinears are allowed by that symmetry. A momentum-blind (rung-local) symmetric gap of the coarse rung releases the fine partner with weight D^2/(D^2+w^2) (0.500, 0.889, 0.985 at w/D = 1, 2^-1.5, 2^-3): overlap suppression makes the release more complete (ED SU(4) atom: partner gap/w = 0.186, 0.0071, 0.0003). Only a quartic on rung-2 staggered rows leaves A untouched at the node; that layout is the momentum-selective-mirror route one rung up. Free bands and one atom only; no interacting 3D phase, no Spin(10), no links."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - untuned_all_direction_massless_crossings_select_space_dimension_equal_to_the_bloch_ball_dimension_bounded_theorem_note_2026-10-22
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
  - the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_bounded_theorem_note_2026-10-22
runner: scripts/a_rung_separated_mirror_protects_the_light_cone_but_a_rung_local_mirror_gap_releases_the_fine_partner_2026_10_22.py
---

# A rung-separated mirror protects the light cone, but a rung-local mirror gap releases the fine partner

Claim type: bounded_theorem (exact free-band statements, one exact atom diagonalisation) with a gate verdict.
Runner: runner.py (14 PASS / 0 FAIL, about 1.4 s, peak 85 MB). Axioms unchanged; the register has zero premise weight.

## Question

The Spin(10)-breaking note found that with the family and the mirror both present, the Spin(10)-singlet family-mirror pairing is the most attractive channel and gaps both. Its repair (a) asks whether family and mirror can sit on different rungs, so that no local family-mirror bilinear exists. Then the mirror could be gapped by its own rung-local symmetric quartic (SMG) while the light family stays chiral. This note tests repair (a) in the smallest exact setting: two rungs, free bands, and one atom for the interacting step.

## Statement

1. (One rung; theorem plus finite check.) The cone-rule band d(p).sigma with k = A p (A unimodular), d = (sin k1, sin k2, sin k3 + 2 - cos k1 - cos k2) has nodes only at p = 0 (chirality +1) and R (-1), found on a 24^3 grid with Newton refinement (A1). A random nearest-neighbour change of size 0.05 moves them (by 0.07 and 0.10) and keeps them (A2). The update reflected through the inversion has the chiralities swapped (A3).
   - On a single rung the mirror cone sits on the same rung, at another momentum. "Rung" is not a label a single-rung cone carries; what a coarser reading sees is a momentum window.
   - Nested block rows overlap by 2^(-3/2) per rung (2^-3 over two rungs). A fine plane wave q has weight prod cos^2(q/2) on the uniform block rows and prod sin^2(q/2) on the staggered (eps-weighted) rows (A4, exact on 8^3).
   - So a coarse reading sees the zone-centre cone fully and the corner cone not at all (uniform rows), or the reverse (staggered rows). Which chirality sits at the visible momentum is one bit, and inversion swaps it.
2. (Two rungs, uniform reading; theorem.) Put the same rule on the coarse rung (coarse hop 1/2, so the cone speeds agree in fine units). The uniform row couples the fine zone-centre cone (+1) to the coarse zone-centre cone (+1). These have the same chirality, so the coupling moves the zeros to isolated points near |h| = w and gaps nothing (B2). The fine R cone stays exactly decoupled. No pair is removed.
3. (Two rungs, staggered reading; theorem.)
   - The staggered row's form factor is (1/8) prod(1 - e^(iq)). It is 1 at q = R and 0 at q = 0.
   - It Dirac-pairs the fine R cone (-1) with the coarse zone-centre cone A (+1): gap exactly w at the node (B3).
   - The coupling matrix is not free. Two opposite-chirality cones with frames J_a and J_b gap everywhere near the node with coupling w U, where U is the SU(2) lift of the orthogonal polar factor of -J_b J_a^-1. In the rotated frame det H = (u.Su + w^2)^2 + |u x Su|^2 > 0 for positive S (B1: min |E|/w = 0.496 over 2000 random frames and momenta). For this band U = i sigma_z. The identity coupling leaves a nodal ring (B1).
   - The fine zone-centre cone is an exact zero mode: H psi_L = 0 (B3). Its vertex to the coarse rows vanishes as q1 q2 q3 (B5), so near the node it is an irrelevant coupling.
   - The full two-rung spectrum has exactly two zeros (B4):
     - the light cone at P = 0, chirality +1, weight on the coarse rung 0;
     - the mirror B at P = 0.9465 pi (1,1,1), chirality -1, weight on the coarse rung 0.879. B is shifted off the corner by hybridising with gapped fine modes.
     - Elsewhere min |E| = 0.265.

   So question (1) is answered: yes. Given the same rule on both rungs, requiring that the cross-rung term remove a pair at all selects the staggered-character reading, and the mirror then sits on the coarse rung. Nothing lopsided is chosen beyond the one handedness bit (which chirality is light), and inversion maps the rule set onto itself.
4. (Crystal momentum; theorem.) The light cone folds to coarse momentum 0 and B sits at the coarse corner. On a 4^3 + 2^3 torus, a random bilinear averaged over the coarse translations gives a light-B element of 2e-16 (B6). The family-mirror singlet channel between the light and B is therefore FORBIDDEN, not merely suppressed by the overlap, for every term that keeps coarse translations. This holds at any order and with interactions, as long as no order breaks coarse translations.
   - The same random bilinear couples the light to the fine partner R (2.54) and to A (2.28). Both fold to coarse momentum 0.
   - So what protects the light from its own partner is fine translation symmetry on the fine rung plus the zero of the staggered row, not the rung split.
5. (Gapping the coarse mirror; exact algebra plus ED.) A rung-local symmetric quartic on the coarse rung (block-local, momentum-blind) acts on A as well as on B.
   - Once A has a propagator zero, G_A ~ -i omega/D^2, the fine partner's propagator at the node is [i omega - w^2 U G_A U^+]^-1. That has a pole at zero with weight Z = D^2/(D^2 + w^2) (C1): 0.500, 0.889 and 0.985 at w/D = 1, 2^-1.5 and 2^-3.
   - The fine R cone, of chirality opposite to the light cone, is released. The light family becomes vector-like on the fine rung.
   - The overlap suppression makes this worse, not better. Smaller cross-rung coupling means a cleaner released partner.
   - ED of one SU(4) atom (256 states) has a partner l_a hybridised by w with a block m_a carrying -g(m1 m2 m3 m4 + h.c.), g = 1. The partner gap/w is 1 when free. With g = 1 it is 0.186, 0.0071 and 0.0003 at w = 0.2, 0.2 x 2^-1.5 and 0.2 x 2^-3 (C2).
   - This answers questions (2) and (3). The light cone itself is protected (exact zero mode, irrelevant vertex, light-B forbidden). But gapping the coarse mirror with a rung-local term releases the fine partner: Golterman-Shamir in its exact block-quartic form, and the same partner as the light-partner census (one opposite-chirality Weyl at R per eps sector).
6. (Escape and where it leads; exact free statement.) Coarse modes on the rung-2 staggered rows see A (coarse P = 0) with weight 0 and B (coarse corner) with weight 1. On the uniform rows it is the reverse (C3). So a mirror quartic built only from the rung-2 staggered rows leaves A, and therefore the fine partner's pairing, untouched at the node.
   - This is exactly the momentum-selective-mirror layout: the light cone out of the interaction, the partner Dirac-paired with a mirror mode that the filter excludes at the node, the remaining mirror cone where the filter is 1. Here it is reached through the coarse rung, with the filter given by the next rung's reading instead of being supplied.
   - Its dynamics is that route's open question: a symmetric gap of B without order.
   - The anomaly count is favourable for the real content: B is one 16 of one chirality, Z16 index 0. It is unfavourable for SU(4) toys (index 4 or 8). Those cannot test this, as the momentum-selective-mirror note found (C4).
   - Iterating the same reading up the ladder pushes B one rung further each time. That is the register's rung ladder, "its mirror on no finite rung", with its magnetic and cone-rate objections.

## Verdict

Repair (a) works at the free level and for the light cone. The family-mirror singlet channel is removed exactly, by coarse crystal momentum, and the light cone is an exact zero mode of any Hamiltonian made of fine-rung translation-invariant terms, staggered cross rows and anything on the coarse rung.

It does NOT escape Golterman-Shamir by itself. The fine rung's own partner (Nielsen-Ninomiya per rung) must be gapped through the coarse rung, and a rung-local symmetric mirror gap releases it with weight approaching 1 as the cross-rung coupling is suppressed. The only version that keeps the partner paired needs a momentum-selective mirror quartic (rung-2 staggered rows). That reduces repair (a) to the open momentum-selective SMG route, which is not computed here. Status: free part exact; interacting part open; no rule adopted.

## Candidate rule and gate

> RUNG-READ (candidate, not adopted). "Every rung carries the same cone-rule update in its own units at the zoom rate. Each rung couples to its parent only through the parent's block row of the character that pairs opposite-chirality cones (the staggered row when the rule is the same), carrying the SU(2) lift of the polar rotation between the paired cone frames. The mirror term is built only from the top rung's rows of that character."

1. Measured numbers: none chosen. w and g are supplied constants. Pass.
2. Observed structure by name: none. Pass in form. The content (one 16) and the handedness bit are supplied by other clauses. The character choice is forced by requiring a cross-rung pair to be removed. The coupling matrix is forced by the bands.
3. Predictions it was not built for:
   - the light's leading coupling to the zoom structure is the cubic-harmonic vertex q1 q2 q3, which gives a self-energy of order w^2 (q1 q2 q3)^2 / D;
   - a vector-like fine partner at mass scale w;
   - the light-B channel is exactly zero.
   All are UNTESTED against measurement, and the dynamical premise (momentum-selective SMG of B) is unverified.
4. Axiom bent:
   - If the coarse rung carries its own modes: Lattice and Qubit (an extra layer of sites per block, as in the rung ladder; the owner allows an extra dimension if it works).
   - If the coarse modes are readings of the fine modes: no axiom is bent, but then every cone is a fine-rung cone and the rule IS the momentum-selective filter acting on fine modes.

Gate result: not a smuggling failure. It is UNTESTED on its load-bearing dynamical premise, so it is not adopted.

## Smuggling review

- Supplied:
  - the cone-rule band (Karsten-Wilczek form, a stand-in for a generic cone-rule update);
  - two modes per fine site, a two-level unit (composite-before-atomic would put it on a 2-site cluster; not built);
  - the coarse hop 1/2, the zoom rate (at the fine rate the coarse cones move at 2c; register);
  - w, D, g, the SU(4) atom and the lattice sizes.
- Forced (exact): per-rung charge sum; overlaps and form factors; the character selection; the coupling matrix up to phase; the light zero mode; the light-B momentum selection; the release weight; the rung-2 row weights.
- Cited, not rederived: Nielsen-Ninomiya beyond the finite check; Golterman-Shamir as context; the Z16 classification for the 16.

## Relation to repo work

Builds on and agrees with:
- why-three-dims: mirrors forced per rung.
- light-partner-gap: the released partner is the opposite-chirality R Weyl.
- block-quartic-smg: the release formula, here with the cross-rung w.
- momentum-selective-mirror: repair (a) reduces to it, one rung up.
- the register's rung ladder ("mirror on no finite rung") and the hybrid (gapping the top-rung mirror releases its doublers).
- neutrino-rule-2: the overlap theorem, and crystal-momentum zero from a corner-only coupling.

It narrows spin10-breaking's repair (a): the singlet channel is removed exactly, but the 45 and singlet channels are not the binding constraint. The binding constraint is the per-rung partner.

## Boundary

Free bands, two rungs, one atom. Not computed: the interacting 3D phase of B under the rung-2 staggered quartic, Spin(10), links, the tick (a Hamiltonian stand-in), the cone universality of the two rungs' metrics beyond this band, and coarse-translation order.
