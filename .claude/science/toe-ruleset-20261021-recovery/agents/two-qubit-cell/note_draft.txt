---
claim_id: two_qubit_site_dirac_walk_is_vector_like_and_a_tetrahedral_twist_gives_a_chiral_turn_charge_with_a_pinned_pi_doubler_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Free bands on a supplied two-qubit site C^2 (flavor tau) (x) C^2 (spin sigma), Clifford walks U = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma. (A) The landed O-covariant doubler-free member (coin 1 (x) D(R), b*) does not resolve the R10/R11 clash: every band is doubly degenerate, its single light node at k = 0 is a vector-like Dirac point (one L and one R Weyl at the same momentum), an O-invariant mass is allowed, and both chiralities carry turn charge q = 0. (B) New exact member: twisting the flavor qubit by the Z3 character of the tetrahedral group T, rho = diag(wbar, w), gives the nearest-neighbour unitary T-covariant walk f = sum c/3, h1 - i h2 = (sqrt2/3)(c1 + w c2 + wbar c3), g = s/sqrt3. The turn then acts chirally: every L Weyl has q = 2 and every R Weyl q = 1 (relabel by the conjugate twist), so mass at k = 0 is forbidden, but h vanishes on the body diagonals and a second pinned Dirac node sits at R = pi(1,1,1) at quasienergy pi with the same per-chirality charges. Light content 2 L + 2 R; no momentum separation of light from mirror; label separation by an on-site filter with O(k^2) leak. Not covered: walks outside the Clifford class, interactions, links, composite realisations."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - two_qubit_site_unfreezes_the_cubic_tick_doubler_free_dirac_walk_bounded_theorem_note_2026-10-16
  - glide_keeping_cube_ticks_carry_an_even_number_of_light_weyl_doublets_per_glide_label_bounded_theorem_note_2026-10-22
  - no_tested_band_carries_both_the_light_turn_charge_and_the_momentum_separated_mirror_bounded_theorem_note_2026-10-22
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
runner: scripts/two_qubit_site_dirac_walk_is_vector_like_and_a_tetrahedral_twist_gives_a_chiral_turn_charge_with_a_pinned_pi_doubler_2026_10_22.py
---

# The two-qubit-site Dirac walk is vector-like; a tetrahedral twist gives a chiral turn charge but a pinned pi doubler

Claim type: bounded_theorem (exact free-band statements). Runner: runner.py, TOTAL: PASS=20 FAIL=0, 0.26 s,
negligible memory, stdout 2.3 k characters; run through scripts/runner_cache.execute_runner under a unique
filename: status ok, exit 0. Axioms unchanged; the site is a supplied hypothesis (bends Qubit, see Cost).

## Question

one-band-check: R10 (family count) needs the light copy to carry a nonzero turn charge q; R11 (mirror
separation) needs light and mirror at different momenta. glide-band: one-mode CL-1 with the 12 rotations cannot
keep the glide and leave one light pair; escapes include a multi-mode cell. Does the landed two-qubit-site
doubler-free walk (main: TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK, 2026-10-16) do both jobs?

## A. The landed O-covariant member: does not resolve the clash (exact)

- A1-A3. Rebuilt b* = (11/30, sqrt u*, 3/20), u* = 0.0395524; G(b*) PSD rank 3; unitary, O-covariant.
- A2 (exact, all Clifford walks). X = h1 tau1 + h2 tau2 + tau3 g.sigma squares to a scalar, so every band is
  doubly degenerate at every k and every node is a 4-fold Dirac point. No band of this class can host a lone
  Weyl node: a light L and its mirror R always sit at the same momentum.
- A4-A5. The only node is k = 0 (24^3 grid); its linear part s tau3 sigma.k (s = 0.914) is one L (tau3 = +1) and
  one R (tau3 = -1) Weyl at the same momentum. A momentum filter vanishing on one vanishes on the other.
- A6. h1 is O-invariant, so rotating F(0) off the f axis is an O-covariant Dirac mass (gap = m exactly). The
  masslessness of the landed member is a choice of the internal O(3) frame, not protected. The doubler-free walk
  is a Wilson-type vector-like fermion.
- A7. The turn acts on each tau3 block as D(R), det 1: q_L = q_R = 0. A fermion-number twist shifts both
  equally. The only 1-dimensional representations of O have turn character 1, so no flavor twist is available
  within O; the E twist is the irreducible spin-3/2 coin, where the landed note found no moving walk.
- A8. The Z3-twisted turn is not a symmetry of this member (residual 1.40).

Answers for the landed walk: (1) one Dirac cone at k = 0; L and R share it; no quarter-point or other momentum
separation. (2) q = 0. (3) The glide-parity theorem does not apply (no glide, multi-mode site), and the walk
evades the doubler count by the chirality-breaking Wilson term h. That is the Nielsen-Ninomiya-allowed vector-like
route, so it removes the chiral content the clash is about. (4) It bends the Qubit axiom.

## B. A tetrahedral twist on the flavor qubit (new, exact)

Rule tested (TWIST): the flavor qubit carries the Z3 character of the 12 tetrahedral rotations (the ones the
copy mass keeps). The turn about (1,1,1) acts as rho (x) D(R), rho = diag(wbar, w); the 2-folds act as 1 (x) D(R).
Then h = (h1, h2) must lie in the E-valued cell functions, not the invariants.

- B1-B2. Exact nearest-neighbour member: f = (c1+c2+c3)/3, h1 - i h2 = (sqrt2/3)(c1 + w c2 + wbar c3),
  g = (s1,s2,s3)/sqrt3. Unitarity is the identity f^2 + |h|^2 + |g|^2 = 1 (the c^2 and cc coefficients cancel:
  1/9 + 2/9 - 1/3 = 0 and 2/9 - 2/9 = 0). It is exactly T-covariant. Contrast: the O family needs corner hops.
- B3. Not O-covariant: a 4-fold would have to exchange the tau3 blocks and flip tau3 g.sigma, i.e. act as a
  parity. Neither the untwisted turn nor any tested 4-fold coin is a symmetry.
- B4. 1 + w + wbar = 0, so h = 0 on every body diagonal (the turn axes). The Dirac mass at k = 0 is forbidden by
  the turn, and a second node is forced where g also vanishes, at R = pi(1,1,1).
- B5. Nodes: exactly k = 0 (f = +1, quasienergy 0) and R (f = -1, quasienergy pi). Speed 1/sqrt3, isotropic at
  both.
- B6. The chirality of each tau3 block is the same at both nodes: tau3 = +1 is L at 0 and at R, tau3 = -1 is R at
  both. The f sign flip at R compensates the s sign flip.
- B7. Turn charges (det = w^{2q}): L (tau3 = +1) has q = 2, R has q = 1. The turn is a chiral Z3, like an axial
  taste phase; the conjugate twist gives q_L = 1, q_R = 2.
- B8. Every T-invariant on-site bilinear is tau3-diagonal and a scalar on each block (Schur, 24-element 2T
  average). No L-R mass exists at either node, and small T-keeping terms only shift node energies.
- B9. The on-site projector (1 + tau3)/2 selects the L Weyls with leak O(k^2), from h ~ k^2. The glide filter
  leaked O(k).
- B10-B11. Census: L at 0 and L at R (both q = 2); R at 0 and R at R (both q = 1). The R node is a pi-mode
  Dirac doubler pinned at a T-fixed momentum with q_L != q_R. No turn-keeping bilinear gaps it: within the node,
  B8 forbids it; across nodes, it fails both on charge (L@R with R@0 differ in q) and on quasienergy (0 versus pi).

Scratch diagnostic (not in runner): least-squares searches over the general twisted family (f, h in E1, E2, g in
v0..v3; 60 starts at three speeds) found exact members only with f(R) = -f(0). A doubled-tick variant (U^2)
puts R at quasienergy 0 but creates quasienergy-pi surfaces at f = 0, so it was not pursued.

## Verdict on the clash

- R10 premise (light L with q != 0): MET by TWIST. Moreover every light L carries the same q, so the vertex
  phase is w^{4 n_L N q} with n_L = 2, and N = 0 mod 3 survives (4*2*N*2 = 0 mod 3 iff N = 0 mod 3).
- R11 premise (light and mirror at different momenta): NOT MET. Both nodes carry one L and one R. Separation is
  by turn label instead, and it is exact at the nodes. This is the glide-label analogue, with a better leak
  (O(k^2)), but a momentum-filtered charge-4 term cannot gap only the mirror.
- Extra content: one protected pi-mode Dirac doubler at R. Removing it needs interactions (SMG of the R-node
  pair), which is outside free bands.
- So TWIST trades the R10/R11 clash for a chiral turn charge with a doubled light content. It does not deliver
  "one band does both jobs" as R11 is stated. It does show that R11's mechanism can be replaced by a label
  mechanism if the charge-4 mirror term is built from (1 - tau3)/2 fields (open; the single-family phase
  w^{4q} != 1 means the term must be multi-family, consistent with N = 0 mod 3).
- Glide parity (3): evaded because TWIST is a multi-mode site with no antiperiodic glide label. Its tau3 label is
  periodic, and the light count per label (2 at q = 2, 2 at q = 1) is even anyway. Not a counterexample to
  glide-band.

## Cost (4)

- The two-qubit site bends the Qubit axiom (M_4(C) site algebra, the parked fork 4). TWIST also keeps T, not O:
  the 4-fold rotations would have to act as a parity.
- Composite alternative (design principle "composite before atomic"): under T, the CL-1 cell's taste E splits
  into w + wbar. This is exactly the flavor twist rho. So the natural composite realisation is the 2^3 cell
  with the taste doublet as tau. Whether an E-valued Wilson term exists there without the glide obstruction is
  not computed here; that is the next probe.

## Gate (TWIST)

1. Numbers chosen: none. The coefficients 1/3, sqrt2/3, 1/sqrt3 are forced by unitarity of the NN member. Pass.
2. Observed structure by name: none. It uses the Z3 character of the kept rotation group on a site qubit. Pass.
3. Prediction not built for: a pinned pi-mode doubler at R and a chiral (axial) turn charge; isotropic NN speed
   1/sqrt3. Internally tested; untested against measurement, and the extra doubler is a liability unless it is
   gapped by interactions. UNTESTED.
4. Axiom bent: Qubit (two qubits per site). Composite version open.

Result: gate passes 1, 2 and 4, and 3 is UNTESTED. TWIST is not a resolution as stated. Report it as a
bounded candidate (q != 0 with label separation, one protected pi doubler); not adopted.

## Smuggling review

- Supplied: the two-qubit site; the Clifford ansatz; the choice of the nontrivial T character (versus the trivial
  one in A); the cell range (nearest neighbour).
- Forced: degeneracy of every band (A2); vector-like content and the allowed mass in A; h(0) = 0 and the R node
  in B; the chiralities and charges; the bilinear selection rules.
- Not used: any measured number or named gauge group.
