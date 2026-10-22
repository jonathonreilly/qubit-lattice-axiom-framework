---
claim_id: five_mode_cones_carry_the_spin10_vector_and_separated_sixteen_cones_evade_the_composite_partner_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Re-poses the chirality wall with the cone rule (isolated Weyl cones, chirality sign det J, charges summing to zero) and five fermion modes per site. (A, exact) On a five-mode site every fermionic operator is a Spin(10) tensor (adjoint Casimir p(10-p) = 9, 21, 25, never the spinor 45/4), the only Spin(10)-invariant hop is the Majorana-vector identity, so any invariant free band is H_orb(k) x 1_10 and its cones carry the real vector 10, which has an invariant mass; such a Majorana band has zero-energy SURFACES (det H real), not cones. The 16 is the site's Fock space, not a propagating multiplet, so 'a 16 per cone' is false for the five-mode reading. (B) In the 16-component reading (one band h(k) x 1_16, a supplied spinor-index field): Spin(10) on the 16 is free of the perturbative and Z16 anomalies and has exactly one charge-4 invariant with the two-component cone slot; with low-energy constituents, a light-mirror hybridisation with any mirror composite is allowed by crystal momentum plus the centre Z4 iff the two cones share a quarter point; a range-one cube-averaged field has form factor exactly 0 at R and maximal at K, so a charge-4 mirror term on a band with cones at K and R never touches the light R cone at any order. Generic cones sit O(1) from quarter points, so the charge-4 term's first-order projection averages out; a small local change moves pinned cones by O(eps), an open (not tuned) condition. Dynamics of the Spin(10) mirror (whether it gaps symmetrically) is not computed. Supplied models; free-band and symmetry level."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - untuned_all_direction_massless_crossings_select_space_dimension_equal_to_the_bloch_ball_dimension_bounded_theorem_note_2026-10-22
  - five_modes_per_site_are_the_smallest_anomaly_free_protected_spin2n_content_bounded_theorem_note_2026-10-22
  - rung_one_cell_register_carries_the_one_generation_multiplet_pattern_bounded_theorem_note_2026-10-21
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
  - the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_bounded_theorem_note_2026-10-22
  - the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_bounded_theorem_note_2026-10-22
runner: scripts/five_mode_cones_carry_the_spin10_vector_and_separated_sixteen_cones_evade_the_composite_partner_2026_10_22.py
---

# Five-mode cones carry the Spin(10) vector; separated 16 cones evade the composite partner

Claim type: bounded_theorem. Runner: runner.py (TOTAL: PASS=11 FAIL=0, 2.7 s, peak 210 MB; stdout 4682
characters). It was run through scripts/runner_cache.execute_runner under a unique filename (status ok).
The minimal axioms are unchanged, and the register carries no premise weight.

## Question

Two new structural results are in play:
- The cone rule (agents/why-three-dims): untuned cones at d = 3 are Weyl cones with chirality sign det J.
  Their charges sum to zero, so mirrors are forced.
- Five modes per site (agents/why-five-modes) are the smallest anomaly-free protected content: Spin(10) and
  its 16.

The proposed escape is that the forced mirror cones carry 16bar and can be gapped by the Spin(10)-symmetric
charge-4 term (symmetric mass generation, SMG). The light 16 cones would stay gapless because the cone rule
places them at other momenta, so a momentum-local term can tell the two apart. This note asks four questions:
- (0) Does a five-mode cone carry a 16 at all?
- (1) Can a local term act on the mirror cones only?
- (2) Does momentum separation avoid the Golterman-Shamir release of light partners?
- (3) Is the escape consistent with the cone rule's genericity?

## A. Five modes per site: what a cone carries (exact)

- A1. One site's Fock space (32 states) is the spinor 16 + 16bar. The Casimir is 45/4 on every state.
- A2. Every fermionic operator on a site (degree 1, 3, 5 in the 10 Majoranas) is an SO(10) tensor. The adjoint
  Casimirs are exactly 9, 21, 25 = p(10 - p), and never 45/4. **No single-particle excitation, at a cone or
  anywhere, transforms as the 16.** This rederives site-so10 item 8 ("Spin(10) moves single fermions as its
  vector 10; its 16 lives in a register's Fock space") in sharper form, covering every odd operator.
- A3. By Schur:
  - the Spin(10)-invariant hops form a commutant of dimension 1, sum_a g_a(x) g_a(y);
  - every invariant free band is H_orb(k) x 1_10;
  - each cone carries the vector 10;
  - the 10 has an invariant symmetric bilinear (it is real, so a Majorana mass is allowed);
  - the 16 has none.

  The "protection" in why-five-modes is a statement about the Fock content. It does not transfer to cone
  content.
- A4. The invariant band is a Majorana band, H(-k) = -H(k)*. Its determinant is real, so zero-energy sets have
  codimension 1. In 4 of 4 random four-orbital bands, sign-change counts scale as n^2 (ratio 4.0-4.2 from
  n = 12 to 24), which is the signature of a surface. A five-mode Spin(10)-invariant band gives Majorana Fermi
  surfaces, not cones. Cones sit only at codimension-3 crossings away from zero energy.

**Verdict on (0): NO.** With five modes per site, the cone rule and Spin(10) protection do not combine: the
cones carry a real 10. "A full 16 per cone" needs a spinor-index fermion field, 16 complex components per
orbital (32 per site with the two-component cone slot). That is a different and larger bend of the Qubit
axiom, and why-five-modes does not derive it. Its Z16 selection (2^(N-1) = 0 mod 16) counts Fock states. A
field-content analogue would have to be a separate theorem. The composite-before-atomic principle makes this
worse: 32 modes on one site is the opposite of composite.

## B. Granting a 16-component field: the momentum route

Model (supplied): one band h(k) x 1_16, with Spin(10) acting on the spinor index. By Schur the invariant hops
are psi^+ psi x 1_16 (16bar x 16 contains a singlet and 16 x 16 does not), so the free band conserves number.

- B1. Generic cone band (cone rule: random nearest-neighbour h, no symmetry; seed 20261022):
  - 8 isolated cones at separated momenta, with chiralities summing to 0.
  - Distances to the nearest quarter point Q (4Q in 2 pi Z^3): 0.25-1.09.
  - First-order projection of a translation-invariant charge-4 term onto a cone,
    ell^-3 sum_x exp(4i(k - Q).x) at ell = 16: <= 0.08, and mostly < 1e-3.

  So **separation is generic, but a generic cone is not where the SMG term acts.** At weak and intermediate
  coupling, the charge-4 term oscillates away on any cone far from a quarter point. At strong coupling (g >> t)
  the band no longer matters, but the overlapping filtered term was seen to pair-order there (qmc-face-gapped,
  toy-qmc).
- B2. Pinned two-cone band (Karsten-Wilczek form on the unimodular map, as in momentum-selective-mirror; one
  band, not two copies): its only zeros are K = 0 (chi +1) and R = pi(1,1,1) (chi -1), and both are quarter
  points. Times 1_16 this gives one 16 per cone. Light = R, mirror = K.
- B3. Selection rule (exact; crystal momentum plus the centre Z4, constituents near their cones):
  - A hybridisation psi_L O or psi_L^+ O with O built from mirror fields of net number n needs n = 3 or 1 mod 4.
  - Its momentum is +-Q_L + n Q_M.
  - Over all 64 x 64 quarter-point pairs and |n| <= 7, it is allowed iff Q_L = Q_M.

  The Golterman-Shamir composite partner (psi_L paired with the mirror's psi^3) therefore needs the light cone
  at the mirror's own quarter point. That was the earlier failure: light and mirror paired at the same corner
  in block-quartic-smg and light-partner-gap. Light-mirror bilinears are also forbidden: psi_L^+ psi_M by
  momentum, psi_L psi_M by Spin(10).
- B4. Spin(10) on the 16:
  - tr X^3 = 0, so there is no perturbative anomaly.
  - The centre Z4 acts as a uniform +-i, giving Z16 index 16 = 0.
  - Charge-4 invariants: 0 with one orbital and exactly 1 with the two-component slot (the pair square; zero-weight
    dimensions 40 and 640, as in site-so10 A4).

  So the K mirror alone is anomaly-free, and its SMG term exists and is unique. Translation acts trivially on it.
- B5. Locality: the cube-averaged field (one 2x2x2 cube, the zoom kernel) has form factor
  prod(1 + e^{ip_i})/sqrt8. That is exactly 0 at R (overlap 7e-33) and maximal at K. A charge-4 term in
  filtered fields therefore never contains a light R mode, at any order and any volume. The light cone at R
  is exactly free. This is the exactness that B3 alone lacks: B3 assumes the composite's constituents sit near
  their cones, and strongly bound composites spread over the zone. For a generic light node kL the range-one
  complex filter prod(1 - e^{i(p - kL)})/2 vanishes at kL and is nonzero at the mirror (0.016 here). Momentum
  selection never needs non-locality.
- B6. Genericity: a random local change of maximum size 0.05 to the pinned band, including the identity part,
  keeps both chiralities and moves the cones by 0.049 (mirror) and 0.065 (light).
  - The SMG term is detuned only by 4|dk_M|. A gapped phase survives a small perturbation, so the condition is
    4 v |dk_M| << Delta_mirror: an open set, not a tuned point.
  - The light cone gets filter weight 2.3e-6 (about prod |dk_i|): highly irrelevant.
  - The node energies split by 0.030. A Spin(10)-singlet psi_L^+ psi_L chemical potential is allowed, so the
    light cone carries a Fermi pocket. That is not a mass, but it is a relevant term that nothing pins.
- B7. Contrast (exact algebra): with same-momentum pairing w, a symmetric mirror whose propagator has a zero
  releases the light mode it was gapping (|G_l(i 1e-3)| 0.016 -> 1067). With separated cones, translation sets
  w(k_L) = 0, so nothing was paired and nothing is released. The light cone is the isolated Weyl node itself.

**Verdicts.**
- (1) YES at the symmetry and anomaly level, for the 16-component field. A range-one filtered charge-4 term acts
  on the K mirror and exactly not on the R light cone, and the K mirror alone is anomaly-free.
- (2) YES, at the free and selection-rule level. Separation in momentum by a nonzero quarter-point difference
  removes the composite-partner channel (B3), and the zero of the filter makes the decoupling exact (B5). The
  earlier failures were same-momentum pairings. With one band there is no separate "light partner": the
  opposite-chirality partner of the light cone is the mirror.
- (3) The cone rule's generic cones sit away from quarter points, so the escape needs the mirror cone near a
  quarter point. That is an open condition of size about Delta/(4v), but a random band meets it only with
  probability set by that volume fraction. Pinning it (as KW does) needs a reason the rules do not yet supply.
  A possible route is Kramers-Weyl pinning at the TRIM under an antiunitary symmetry; it is not checked.
- Not established: that the Spin(10) K mirror actually gaps symmetrically. ax7-chirality-16weyl is the closest
  test (an SU(4) 16-Weyl toy), and it is inconclusive at L <= 6.

## Tested candidate rule (NOT adopted)

> "Mirror term at the zone centre. The charge-4 term invariant under every mode rotation the update keeps acts
> on the cube-averaged field; the cones the average passes are gapped, the cones it annihilates stay light."

Gate:
1. Numbers chosen: none. The coupling is a supplied constant.
2. Observed structure by name: it fails as stated. The rule needs a 16-component spinor-index field, which is
   not derived. The five-mode derivation gives a 10 at a cone (A2-A3). The cube filter, and which cone is K, are
   structural, not observed. The handedness bit is one sign, a parity convention.
3. Predictions it was not built for (UNTESTED):
   - the light species sits at the zone corner (staggered phase);
   - a light-cone chemical potential is generic (a Fermi pocket);
   - a gauge-singlet member is needed (16, not 15, inherited from Z16).
4. Axioms bent: Qubit (32 modes per site), and nearest-neighbour admissibility (the vertex spans a 2x2x2 cube).

Result: **FAIL on (2)**, so the rule is not adopted. The momentum mechanism itself (B3, B5, B7) passes (1) and
(4) and is reusable once the content question is solved.

## Smuggling review

- Supplied: the 16-component field in part B, the KW band, r = 1, the unimodular map, the cube filter, eps, L,
  ell and the seeds.
- Forced: A1-A4 (exact representation theory), B3 (selection rule), B4 (counts and indices), B5 (filter zero).

## Re-posed wall (for the register)

Chirality wall, after CONE + 5 modes:
- (i) Content: the propagating multiplet at a cone must be the 16. Five modes give the 10, so either a
  spinor-index field or an emergent fermionic 16 is needed; the second is not shown.
- (ii) Placement: the mirror cone must sit near a quarter point and the light cone away from it.
- (iii) Dynamics: a symmetric gap for the 16 mirror at K. This is open.

Separation itself is not the obstruction any more.

## Boundary

Free bands plus exact representation theory only. Not computed:
- the interacting Spin(10) dynamics;
- gauge links (a covariant filter smears the zero at R when the gauge field is rough);
- antiunitary symmetries;
- the light-cone chemical potential.

Golterman-Shamir is engaged at the selection-rule level. The propagator-zero question is left to zeros-ghosts.
Literature (Wang-Wen on the 16, Golterman-Shamir) is cited, not rederived.

## Used / narrowed

- Used: why-three-dims (CONE), why-five-modes, site-so10 (items 8 and 9, A4), light-partner-gap,
  block-quartic-smg, momentum-selective-mirror, ax7-chirality-16weyl, qmc-face-gapped.
- Narrows why-five-modes: its Spin(10) protection applies to Fock content and not to cone content.
- Supports the PR #9994 and #10004 momentum-selective route at the selection-rule level.
- Related, not checked: PR #10022 (family-count-5mode).
