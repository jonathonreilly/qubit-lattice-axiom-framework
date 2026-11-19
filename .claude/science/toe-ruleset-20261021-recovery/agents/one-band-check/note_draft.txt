---
claim_id: no_tested_band_carries_both_the_light_turn_charge_and_the_momentum_separated_mirror_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Free-band consistency check of two conditional results that use different bands. The family count (N = 0 mod 3) needs the light copy to carry a nonzero three-fold-turn charge q; the mirror separation needs light and mirror at different exact momentum labels so a filtered charge-4 term vanishes on the light cone. Exact: (A) the massless CL-1 cube tick has an exact one-site (1,1,1) glide G, and at K = 0 G equals the chirality operator, so all left tastes carry G = +1 and all right tastes G = -1 (a Karsten-Wilczek-like split by the glide label); a glide-symmetric number-conserving bilinear therefore has no L-R block at K = 0, and the copy mass on both tilings gaps nothing there. (B) The AX-3 copy mass (even cubes) breaks the glide for every site gauge; its light copy (1 L + 1 R Weyl) has q in {1,2} but both sit at cell momentum 0 with weight 1/4 on every fine corner, and a term keeping cell translations and all 12 kept rotations opens a light-mirror Dirac gap linearly. (C) The glide-symmetric massless tick separates (the range-one filter (1 - G)/2 is exactly 0 on the light states, 1 on the mirror, leak linear in k) but its light content is E with q = 1 and 2, total turn phase 1, so every N is allowed. (D) The Karsten-Wilczek-type band keeps no three-fold cube turn; for any on-site-spinor band with cones at K and R the turn acts on both cones by one on-site phase, which the charge-4 term fixes to +-1, so q = 0. No tested band does both jobs. A glide-symmetric band reached by moving the q = 1 tastes off K = 0 and annihilating them is not excluded and not constructed. Free bands only; no interactions, links or Spin(10) dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
  - five_mode_cones_carry_the_spin10_vector_and_separated_sixteen_cones_evade_the_composite_partner_bounded_theorem_note_2026-10-22
  - a_rung_separated_mirror_protects_the_light_cone_but_a_rung_local_mirror_gap_releases_the_fine_partner_bounded_theorem_note_2026-10-22
  - the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_bounded_theorem_note_2026-10-22
runner: scripts/no_tested_band_carries_both_the_light_turn_charge_and_the_momentum_separated_mirror_2026_10_22.py
---

# No tested band carries both the light turn charge and the momentum-separated mirror

Claim type: bounded_theorem (exact free-band statements and one consistency verdict). Runner: runner.py (TOTAL:
PASS=20 FAIL=0, about 1.5 s, about 60 MB, stdout about 3.9 k characters). It was run through
scripts/runner_cache.execute_runner under a unique filename: status ok, exit 0. Axioms unchanged.

## Question

Two conditional results in the best ruleset use different bands:
- R10, the family count (family-count-5mode), uses CL-1's cube tick with the copy mass (AX-3). It needs the light
  copy to carry a nonzero charge q under a kept three-fold cube turn.
- R11, the mirror separation (chirality-5mode-cones B2-B5, rung-separated-mirror), uses a Karsten-Wilczek-type band
  with cones at K = 0 and R = pi(1,1,1). It needs light and mirror at different exact momentum labels, so that the
  cube-filtered charge-4 term (zero at R) gaps only the mirror.

This note asks whether one band does both jobs.

## Setting (supplied)

- CL-1 cell: one mode per site, face phase -1, the Margolus cube tick on both tilings (step eps), Bloch over 2Z^3.
- The copy mass (M/4)(1 - s) Re on the even step (AX-3), with M = 0.7.
- The KW band d(p).sigma on the unimodular map (as in chirality-5mode-cones).
- Seeded random perturbations (seed 20261022).

## A. The CL-1 tick has a hidden glide, and on it the glide is the chirality (exact)

- A1. Let T be the one-site shift by (1,1,1), D = (-1)^(x1 + x3) a site gauge, and Ue the even half-step. Then
  G = Ue^-1 D T commutes with the massless tick U(k) at every k. The reason: D T maps the even links to the odd
  links with the sign flipped, and back, so it exchanges the two half-steps. G^2 is a cell translation times U^-1,
  so G acts as a fine translation that the cell hides.
- A2. The AX-3 copy mass (even cubes only) breaks G, and no site gauge restores it (best residual 0.30).
- A3. A copy mass placed on both tilings keeps G.
- A4. **Theorem.** In the massless tick at K = 0, G equals the chirality operator i A1 A2 A3 as an 8 x 8 matrix
  (residual 4e-16, at eps = 0.3 and 0.6). So both left tastes carry G = +1 and both right tastes carry G = -1. The
  massless tick is already split by the glide label, like K versus R in the KW band.
- A5 and A6. Consequences:
  - A glide-symmetric term commutes with chirality at K = 0, so its L-R block vanishes identically (Schur; random
    check).
  - A Dirac mass at K = 0 would need L and R with equal G, and there are none.
  - So a glide-symmetric copy mass gaps nothing at K = 0: with the copy mass on both tilings, all 8 states stay
    light.
  - The AX-3 copy mass reduces 2 + 2 to 1 + 1 only because it breaks the glide. It pairs one L taste (G = +1) with
    one R taste (G = -1).

## B. The AX-3 band (R10's band): q != 0, no separation

- B1. The light copy is 1 L Weyl + 1 R Weyl, and both sit at cell momentum K = 0.
- B2. Each light chirality block spreads exactly 1/4 over every one of the 8 fine corners. The cube average (the
  corner 000 at K = 0) has weight 1/4 on the light copy and on the mirror alike. There is no fine-momentum split.
- B3. R10 holds: 12 rotations are kept, q is in {1, 2} on every turn, and q_L = q_R. This reproduces
  family-count-5mode B3-B4.
- B4. A random cell-local term that keeps cell translations and all 12 kept rotations has an L-R block of norm
  0.75. It opens a Dirac gap at K = 0 that grows linearly with the term's size (levels -0.0021 and +0.0094 at size
  0.01; doubled at 0.02).
- B5. The light-mirror Dirac mass is therefore allowed in this band. R11's selection rule (pairing allowed iff
  Q_L = Q_M) is met here with Q_L = Q_M, so the Golterman-Shamir composite channel psi_L (mirror^3) is open. Any
  cube or cell filter at K = 0 also contains the light legs.

**Answer to question 1.** In the copy-mass tick, light and mirror share one momentum (cell K = 0) and one fine-corner
profile. Neither sits at R, and the cube filter cannot gap only the mirror. The glide could have told them apart,
but the copy mass breaks it.

## C. The glide-symmetric tick: separation, but no count

- C1. The range-one glide filter F = (1 - G)/2 is exactly 0 on every light L state at K = 0 and 1 on every R state.
  It is the analogue of the cube filter's zero at R, with the glide label in place of the fine momentum.
- C2. Its leak onto the light branch grows linearly in k (2.2e-3, 4.4e-3). The KW cube filter's leak grows as k^3.
- C3. F is cube-covariant: all 24 rotations are kept, and each maps G to G.
- C4. The light L content here is E (q = 1 and q = 2). The total turn phase on the L block is w^(2(1+2)) = 1, so
  the light vertex phase is 1 for every N. The family count is silent, which agrees with family-count-5mode's
  remark that the massless tick allows every N.

## D. The KW band (R11's band): separation, no turn charge

- D1. Its zeros are only K (+1) and R (-1).
- D2. No three-fold cube turn preserves its spectrum: none, unitary or antiunitary, with any translation or
  pi-momentum shift (minimum residual 2.37). So the family theorem's premise, a kept turn, is absent.
- D3. Covariance alone does not rescue this. For any cube-covariant on-site-spinor band with cones at K and R, every
  rotation's Bloch phase is 1 at both cones, because Rx - x has an even coordinate sum. The turn then acts on each
  cone as spinor x one on-site phase mu.
- D4. The spin-singlet charge-4 mirror term keeps the turn only if mu^4 = 1. With mu^6 = 1 that leaves mu = +-1,
  so q = 0 on both cones. The choice mu = w is the fermion-number Z3, and the term breaks it (w^4 = w). That is
  family-count-5mode's D4 exclusion.

**Answer to question 2.** No. Spin is on-site in the KW band, so the turn cannot carry the taste phase w that makes q
nonzero in CL-1. That phase comes from spin being a composite of the cell's tastes (the E representation).

## Verdict

| Band | R10: q != 0 on the light copy | R11: exact light-mirror separation |
|---|---|---|
| AX-3 copy-mass tick | yes | no (same K; glide broken; Dirac mass allowed) |
| Glide-symmetric massless tick | no (E, phase sum 0) | yes (glide filter) |
| KW two-cone band | no (no turn; q = 0 on-site) | yes (cube filter) |

**Inconsistent as the ruleset stands.** R10 and R11 cannot both be cited for the same light family. R11's
"light at R, mirror at K" does not hold in the band R10 uses. On that band the light-mirror mass and the composite
partner channel are allowed by every symmetry the band keeps. R10 is the result that survives on its own band;
R11 falls there. Equally, R10 falls on R11's band.

**Answer to question 3 (partial).** There is a precise target. In the massless tick the tastes are L(q=2, G=+1),
L(q=1, G=+1), R(q=2, G=-1) and R(q=1, G=-1) (labelled for one turn; the even-cube copy mass keeps the q = 2
pair). A band that does both jobs must keep G and remove one L and one R taste with equal q, leaving
L(q=2, G=+1) and R(q=2, G=-1). By A5-A6 no glide-symmetric bilinear does this at K = 0; it needs the q = 1 L and R
tastes to move off K = 0 and annihilate in the glide-unfolded zone (a finite band deformation, as KW does from
the naive band). The kept rotations constrain this: a K = 0 spin doublet cannot split while the 12 rotations are
kept. Existence is not excluded and not constructed here.

## Candidate rule and gate

> GLIDE-KEEP (candidate, UNTESTED). "Every term of the update respects the one-site diagonal glide of the cube
> tick (the shift that exchanges the two tilings)."

1. Numbers chosen: none. Pass.
2. Observed structure by name: none. The glide is a symmetry of the bare tick. Pass.
3. Predictions it was not built for: the light copy is glide-even and the mirror glide-odd, so a range-one glide
   filter exists. UNTESTED, and it is unproductive until a band of the section 3 type is shown to exist. Under
   GLIDE-KEEP, AX-3 as written is forbidden (A2), so the family count would need a new copy-mass form.
4. Axiom bent: none beyond the existing ones (it restricts AX-3).

Gate result: not a smuggling failure, but UNTESTED with no working band. **Not adopted.**

## Smuggling review

- Supplied: the CL-1 tick and copy mass (register and AX-3), the KW band, M, eps, the seeds and the random
  perturbations.
- Forced (exact):
  - the glide and its gauge (found by search);
  - G = chirality (A4) and the absence of an L-R block (A6);
  - the glide breaking by AX-3 under every gauge;
  - the corner weights, the q values, the linear Dirac gap;
  - the KW turn absence;
  - the on-site phase argument.
- Cited, not rederived: Golterman-Shamir (the composite partner channel), and the 't Hooft vertex logic of
  family-count-5mode.

## Boundary

Free bands only. Not computed:
- interacting effects;
- whether symmetries beyond translations, the 12 rotations and the glide protect the AX-3 light pair (B4 shows that
  these three do not);
- gauge links;
- the Spin(10) label, carried as band x 1_16;
- the node-motion construction of question 3.

## Used / narrowed

- Used: family-count-5mode (tick, copy mass, q), chirality-5mode-cones (KW band, cube filter, selection rule),
  rung-separated-mirror, families-from-tastes (PR #10016; E + E and the copy mass).
- Narrows synthesis-7 R11 ("light at R, mirror at K") to bands without a kept turn charge. It also narrows R10's
  sufficiency premise: symmetric mirror gapping in the AX-3 band has no momentum protection for the light copy.
- New exact fact: the CL-1 massless tick's chirality equals a one-site glide at K = 0.
