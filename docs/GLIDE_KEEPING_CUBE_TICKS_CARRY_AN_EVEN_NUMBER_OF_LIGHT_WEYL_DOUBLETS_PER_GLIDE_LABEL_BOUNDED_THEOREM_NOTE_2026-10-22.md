---
claim_id: glide_keeping_cube_ticks_carry_an_even_number_of_light_weyl_doublets_per_glide_label_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Free one-mode-per-site CL-1-type cube ticks on the 2^3 cell, any range. Exact: (i) a tick keeps the one-site (1,1,1) glide G = A^-1 D T exactly when its odd half-step is the glide image of its even half-step, U = (DT) A (DT)^-1 A, and then U = T^2 G^-2. (ii) The glide label Lam = e^{-i th.1/2} G U^{1/2} is an involution commuting with U that is antiperiodic in the cell Bloch angle, so it is balanced in every gapped quasienergy window. (iii) At K = 0 and at the zone corner pi(1,1,1) the 12 tetrahedral rotations (indeed the three 2-fold ones alone) commute with Lam and act spinorially, so each label sector there is a sum of doublets. Theorem: if such a tick keeps the glide and the three 2-fold rotations and has no quasienergy-0 or -pi states except Weyl doublets at K = 0, the number of light Weyl doublets carrying each glide label is even. Hence no glide-keeping, cube-covariant deformation leaves exactly L(q=2, glide +) + R(q=2, glide -) light: every placement of the q = 1 copy doublets is excluded, and they can never be mass-paired (they stay T-doublets at K = 0 with opposite glide labels). Finite diagnostics: the natural glide-symmetric copy terms (copy inversion, glide Dirac mass, copy shift) and a 12-start search over copy unitaries on both tilings all leave extra quasienergy-0 or -pi states, as the theorem requires; AX-3 evades only by breaking the glide; keeping a single turn without the 2-fold rotations lifts the doublet constraint. Not covered: composite or multi-mode cells, coarser rungs, interactions, links."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - no_tested_band_carries_both_the_light_turn_charge_and_the_momentum_separated_mirror_bounded_theorem_note_2026-10-22
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
runner: scripts/glide_keeping_cube_ticks_carry_an_even_number_of_light_weyl_doublets_per_glide_label_2026_10_22.py
---

# Glide-keeping cube ticks carry an even number of light Weyl doublets per glide label

Claim type: bounded_theorem (exact counting theorem plus finite diagnostics). Runner: runner.py (TOTAL: PASS=15
FAIL=0, about 1.6 s, about 80 MB peak, stdout about 3.4 k characters). Run through scripts/runner_cache.execute_runner
under a unique filename: status ok, exit 0, 1.75 s. Axioms unchanged.

## Question

one-band-check found that the massless CL-1 cube tick has a one-site (1,1,1) glide G equal to chirality at K = 0,
that the range-one filter (1 - G)/2 separates light from mirror, and that the AX-3 copy mass breaks the glide. It set
a target: keep the glide and leave only L(q=2, G=+1) + R(q=2, G=-1), so the mod-3 family theorem and the glide
filter would hold on one band (candidate GLIDE-KEEP). This note searches the glide-keeping, cube-covariant term
space for such a band. Result: it does not exist, at any range, and the obstruction is a parity.

## Setting (supplied)

- CL-1 cell: one mode per site, face phase -1, the cube tick on both tilings, step eps (eps = 0.6 in the runner's
  band checks; the theorem does not depend on eps), Bloch over 2Z^3 with twist th = 2k.
- The 12 tetrahedral rotations (the ones the copy sign s keeps), with the site gauges of the massless tick.
- Seeded random terms (seed 20261022): every hop of fine range |d|_inf <= 2, averaged over the 12 rotations, plus a
  random copy-sector unitary on the even cube.

## A. What "keeps the glide" means (exact)

- A1. The massless tick is U = T^2 G^-2 with G = Ue^-1 D T, where T is the (1,1,1) shift, D = (-1)^(x1+x3) and
  T^2 is a cell translation. The glide determines the tick.
- A2. For any local even half-step A, the tick U = (DT) A (DT)^-1 A keeps G = A^-1 D T, and U = T^2 G^-2. Conversely,
  a glide G of this form fixes U. So GLIDE-KEEP is exactly: "the odd half-step is the glide image of the even
  half-step." Any glide-keeping deformation is a choice of the local unitary A.
- A3. The random range-2 deformation keeps all 12 rotations (error 4e-16).

## B. The glide label (exact)

- B1. Define Lam = e^{-i th.1/2} G U^{1/2}, using the principal square root (defined wherever U has no eigenvalue
  -1). Then Lam^2 = G^2 e^{-i th.1} U = 1 and [Lam, U] = 0. And Lam(th + 2 pi e_i) = -Lam(th): the label is
  antiperiodic, so going round any cycle of the zone exchanges + and -. Each tick eigenstate carries a label
  +-1. At K = 0 it is the old G = chirality.
- B2. At K = 0 the massless doublets are, as (label, s, q): L2 (+,+,2), L1 (+,-,1), R2 (-,+,2), R1 (-,-,1). So the
  target L2 + R2 is ONE light doublet per label, and the massless tick has two per label.
- B3. At K = 0 and at the corner th_c = pi(1,1,1), all 12 rotations commute with Lam, for the random deformation
  too. The reason is that a rotation maps the (1,1,1) glide to another body-diagonal glide. That glide differs by a
  cell translation, and at these two points the translation's Bloch phase cancels against e^{-i th.1/2}. At
  (pi,0,0) two of the four 2-fold elements anticommute, so there is no constraint there.
- B4. At K = 0 and th_c the rotations act spinorially, as the register's double-cover theorem says. Every operator
  that commutes with the 12 rotations and with Lam, and the tick itself, is doubly degenerate there (to 3e-14). So
  each label sector is a sum of doublets. The three 2-fold rotations alone already force this: their spinorial irrep
  is 2-dimensional, and they commute with Lam at th_c.
- B5. One kept turn alone (C3 about (1,1,1), without the 2-fold rotations) forces no doublets: a symmetrised random
  operator is non-degenerate.

## C. Theorem (glide parity)

Hypotheses: the tick keeps the glide (A2) and the three 2-fold rotations, and it has no quasienergy-0 or -pi states
except Weyl doublets at K = 0. Each such doublet splits into one branch above 0 and one below.

Claim: for each glide label, the number of light Weyl doublets at K = 0 is even.

Proof:
1. Let n(W, l) be the number of states in the window W = (-pi, 0) that carry label l. Off the light nodes,
   P_W (1 +- Lam)/2 is continuous on the doubled zone. The doubled zone minus isolated points is connected, so
   n(W, l) is constant.
2. Antiperiodicity (B1) maps the + sector to the - sector, so n(W, +) = n(W, -).
3. At th_c, every label sector is a sum of doublets (B3, B4), so n(W, l) is even.
4. Take a small k != 0 near K = 0. Each light Weyl doublet with label l contributes one state to W, its lower
   branch. Every other K = 0 doublet lying in W contributes 2. So n(W, l) = N_light(l) mod 2.
5. Hence N_light(l) is even. QED.

Corollaries:
- C1. Every placement of the two q = 1 copy doublets, over label choices and sides of 0 (12 cases), violates
  either the balance in step 2 or the evenness in step 3.
  - Opposite sides: a mass-paired pattern at +-E is unbalanced in W.
  - Same side with opposite labels: balanced, but n(W) = 2 or 6, not a multiple of 4.
  - So no clean glide-keeping band has exactly one light doublet per label.
  - The copy doublets also cannot be mass-paired at all. They stay T-doublets pinned at K = 0 with opposite
    labels, and so they have different glide eigenvalues.
- C2 (control). The massless tick has two light doublets per label. Its n(W) = 4 on the whole grid, with (2, 2)
  per label at the corner. This is consistent.

Consequence: any glide-keeping, 2-fold-covariant band that keeps one light pair at K = 0 must carry further
quasienergy-0 or -pi states somewhere in the zone, an odd number per label in the sense of step 4. This answers
one-band-check's open question 3 in the negative. Its "existence not excluded" is now excluded for this setting.

## D. Finite diagnostics: the natural attempts fail exactly as C predicts

All at eps = 0.6. "E = 0 points off K = 0" counts seeded Nelder-Mead searches that converge to a zero away from K = 0.
- D1. Copy inversion, A = Ue (PS + DI PC). DI is the gauged cube inversion, and PS and PC are the s = +-1
  projectors.
  - Copy levels: +-1.2, both label +.
  - tr Lam = 4 at K = 0, so the band cannot be gapped at pi (B1). It has quasienergy-pi states (min distance 0.018
    on the grid; exact pi modes at pi(0,0,1)-type and pi(1,1,1) points at eps = 0.3) and E = 0 points (8/8
    searches).
- D2. Glide Dirac mass, A = Ue (PS + i DI PC).
  - Copy levels: +-1.94 with opposite labels. This is the mass-paired pattern.
  - It is unbalanced in W, and E = 0 surfaces follow (8/8 searches).
- D3. Copy shift, A = Ue (PS + e^{i pi/4} PC).
  - Both copy doublets sit at +pi/2 with opposite labels. This is balanced, but n(W) = 2.
  - The light branches are dragged across 0 near the zone faces (7/8 searches).
- D4. A 12-start Nelder-Mead search over copy-sector unitaries on both tilings (8 angles; scratch/opt1.py and
  opt2.py, eps 0.6, seeds 1 and 2) never reached a positive gap margin. The best margin was -3e-6. At that optimum
  an E = 0 doublet sits on the 4-orbit pi(1/2,1/2,1/2) of the turn axes. This is a search diagnostic, not a theorem;
  the theorem is C.
- D5. AX-3 evades the theorem by breaking the glide (|[G, U]| = 0.52). It gives one light pair, a constant
  n(W) = 4, no E = 0 points off K = 0, and an open pi gap.

## Answer to the task

1. Removing the q = 1 tastes in a glide-keeping band.
   - Pair annihilation is impossible: the copy doublets are T-irreducible at K = 0 and carry opposite labels.
   - Displacing them in quasienergy is allowed at K = 0, but C forces extra light states elsewhere.
   - Going to longer range does not help. The theorem uses only the glide, the 2-fold rotations and the gaps.
2. Exactly q = 2 light content with the glide kept: impossible, as above.
3. The glide filter would work on such a band, but no such band exists.

So no GLIDE-KEEP rule text and no glide-symmetric copy-mass form is offered.

## Candidate rule and gate

> GLIDE-KEEP (candidate from one-band-check). "Every term of the update respects the one-site diagonal glide of the
> cube tick." Equivalent form (A2): "the odd half-step is the glide image of the even half-step."

1. Numbers chosen: none. Pass.
2. Observed structure by name: none. Pass.
3. Prediction it was not built for: TESTED and FAILED internally. With the 2-fold rotations kept, it forces an even
   number of light doublets per glide label, so the one-light-pair band that the family count needs cannot coexist
   with it. It fails against measurement in the following sense: either it brings extra massless species (light
   doublets beyond one pair) or it loses the family count.
4. Axiom bent: none (it would restrict AX-3).

Gate result: not a smuggling failure; a consistency FAILURE. **Not adopted.** The R10/R11 inconsistency of
one-band-check cannot be repaired by keeping the glide inside one-mode CL-1 with the 12 rotations.

## Escapes (open, not constructed)

- Extra light doublets: an odd number per label (for example a pair at the corner pi(1,1,1)). That means extra light
  species. Their turn charges and whether they could serve as the gapped mirror are not computed.
- Keep one turn without the 2-fold rotations (B5). The light Weyl velocity is then uniaxial at linear order (two
  speeds allowed by C3 alone). That needs a reason or a tuning against fermion isotropy bounds (an estimate, not
  computed here).
- Composite cells (several sites or modes per role, as in TWO_QUBIT_SITE..._2026-10-16 on main) or a coarser rung,
  where the glide and the doublet structure differ. Not tested. These fit the composite-before-atomic principle.
- Break the glide (as AX-3 does) and separate the mirror by another mechanism (rung separation), keeping R10.

## Theorems vs diagnostics vs estimates

- Exact (runner): A1-A3; B1-B5; C1-C2 (the counting); the K = 0 labels and copy levels of D1-D3.
- Proof (in text, from exact ingredients): the parity theorem of section C.
- Finite diagnostics: the zero searches in D1-D3 and the optimisation optimum in D4.
- Estimate, not computed: the isotropy cost of the single-turn escape.
- Speculation: none relied on.

## Smuggling review

- Supplied: the CL-1 tick, the copy sign s, the 12 rotations, eps, the seeds, and the random term amplitudes (0.05
  scale).
- Forced (exact): the half-step form of GLIDE-KEEP; the label's antiperiodicity; the commutation of the label with
  the rotations at K = 0 and the corner; spinorial doublets; the parity theorem; the exclusion of all 12 placements.
- Nothing measured enters.

## Boundary

Free bands, one mode per site, the 2^3 cell, Bloch over 2Z^3. Not computed: interactions, links, Spin(10) (band x
1_16), coarser rungs, multi-mode or composite cells, and the turn charges of any extra light doublets.

## Used / narrowed

- Used: one-band-check (the glide, the target, AX-3 glide breaking), family-count-5mode (tick, s, q),
  families-from-tastes (E + E), register CL-1 (double cover).
- Narrows one-band-check question 3: from "not excluded" to excluded with the 2-fold rotations kept.
- Narrows GLIDE-KEEP: from untested to failed.
