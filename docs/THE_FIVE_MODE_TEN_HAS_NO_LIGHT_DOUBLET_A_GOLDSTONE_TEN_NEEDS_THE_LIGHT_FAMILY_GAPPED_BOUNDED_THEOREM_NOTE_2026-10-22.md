---
claim_id: the_five_mode_ten_has_no_light_doublet_a_goldstone_ten_needs_the_light_family_gapped_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Five fermion modes per site (Cl(10), Spin(10), U(5) frame from the number-conserving tick, cubic E + T1 labels),
  optionally the sixth A1 half-link mode (Cl(12), Spin(12), 32 = 16 + 16bar), one 16 per family read as Weyl species,
  3 families, mirror gapped symmetrically. Exact: (A) the 10 is the mode operators, 5_{+2} + 5bar_{-2} under U(5)_X;
  its doublet is E (Y = 1/2, B-L = 0), its triplet T1 (Y = -1/3, B-L = -2/3), so doublet-triplet splitting is the same
  parameter as omega_E != omega_T. On five modes every 10-tensor is odd under the Spin(10) element Omega = (-1)^F5, so it
  is fermionic; a bosonic 10 needs a Spin(10)-singlet fermion such as A1 (g_a g_A1). (B) The Lorentz-scalar pairs of the
  32 are 66 + 462; the 66 = 45_0 + 1_0 + 10_{+1} + 10_{-1}; the scalar 10s are light-light and mirror-mirror pairs; light-
  mirror scalars are 1 + 45 + 210 with no 10. (C) The only pair whose Goldstones are the 10s is the light-mirror singlet
  1_0 (stabiliser 46, 20 Goldstones = 10_{+1} + 10_{-1}), and it is a full-rank equal-mass Dirac term for the whole light
  16. A mirror-only gap breaks Spin(12) explicitly to the same 46 and leaves no Goldstone. (D) On the 6 link ends the
  covariant one-body terms are span(1, P, F); P groups A1 with E; the doublet coset frequency is -6b (face term), the
  triplet's -2a - 4b; the covariant site-A1 hop gives the doublet a seesaw gap sqrt(a^2/4 + 6h^2) - a/2. (E) 16 x 16 x 10
  has a symmetric family matrix; one neutral component couples (q u^c), (L n^c), the other (q d^c), (L e^c), with equal
  magnitudes; with N = 3 the turn anomaly forces uniform turn charges, so the turn gives no texture; Sym^2(3) has one
  SO(3) and no U(3) invariant. Estimates against measurement are separate. No candidate gives a light doublet without a
  fitted number; all tested rules fail the gate."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - five_modes_per_site_are_the_smallest_anomaly_free_protected_spin2n_content_bounded_theorem_note_2026-10-22
  - number_conserving_tick_fixes_the_u5_frame_but_half_link_2_plus_3_split_is_orbital_not_internal_bounded_theorem_note_2026-10-22
  - five_mode_cones_carry_the_spin10_vector_and_separated_sixteen_cones_evade_the_composite_partner_bounded_theorem_note_2026-10-22
  - the_zone_corner_pairing_is_electroweak_neutral_and_its_only_doublets_carry_two_units_of_b_minus_l_bounded_theorem_note_2026-10-22
  - a_light_pseudo_goldstone_higgs_needs_inserted_content_and_its_rule_moves_the_hierarchy_to_the_top_coupling_bounded_theorem_note_2026-10-22
  - the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_bounded_theorem_note_2026-10-22
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
runner: scripts/the_five_mode_ten_has_no_light_doublet_a_goldstone_ten_needs_the_light_family_gapped_2026_10_22.py
---

# The five-mode 10 has no light doublet; a Goldstone 10 needs the light family gapped

Claim type: bounded_theorem. Runner: runner.py (PASS=32, FAIL=0, about 1.1 s, peak about 215 MB, stdout 4951
characters). Tested through scripts/runner_cache.execute_runner under a unique filename: status ok, exit 0.

## Question

The current best framework has 5 fermion modes per site (why-five-modes), the U(5) frame from the tick (rule TJ,
time-complex-structure), Spin(10) protection, N_f = 3 (family-count-5mode, conditional), and a symmetrically gapped
mirror. Three walls are already recorded: higgs-from-structure, ax6-higgs and mirror-condensate-ew. This note asks
whether a light Y = 1/2 doublet scalar arises without inserting content, through three candidates:
- (1) the sixth half-link (A1) mode or the Spin(12) extension, as the source of a 10;
- (2) the doublet as a pseudo-Goldstone of the mirror's SMG transition;
- (3) a 16 x 16 x 10 Yukawa structure with the top largest.

Two readings are kept apart, following chirality-5mode-cones:
- R5 (five modes): the site's Fock space is 16 + 16bar, and single-particle operators and free cones carry the
  fermionic 10.
- R16 (species): a supplied 16-component field, where each 16 state is a Weyl species (the Wilczek-Zee reading).

## A. What the 10 is (exact)

- A1-A4.
  - The 10 is the 10 Majoranas, i.e. the mode operators: c^dag gives 5_{+2} and c gives 5bar_{-2} under U(5)_X,
    with X = 2N - 5.
  - With the cubic labels (Y = N_E/2 - N_T/3, B-L = 1 - (2/3) N_T):
    - c_E^dag = (1,2)_{1/2} with B-L = 0. This is the doublet.
    - c_T^dag = (3,1)_{-1/3} with B-L = -2/3. This is the triplet.
  - **The 10's doublet-triplet split is the E/T1 split of the mode labels: the same parameter, omega_E != omega_T,
    that gives SU(3) x SU(2).** The DT question and the SM-breaking question are therefore one question.
- A7 (new, sharpening the cone correction).
  - The Spin(10) element Omega = prod_j exp(i pi (n_j - 1/2)) acts as -1 on all 10 Majoranas and equals
    (-1)^F5 up to a phase.
  - So on five modes every operator in a 10, or in any odd tensor, is fermionic. Products of an even number of 10s
    never contain a 10.
  - **Within R5 there is no bosonic 10 at all**: not on a site, and not as a multi-site product of the cone 10s.
- A8. A bosonic 10 needs a Spin(10)-singlet fermion. With A1 kept, Phi_a = g_a g_A1 is even, Omega-odd and has
  Casimir 9. Candidate (1) is the only structural source of a scalar 10 in R5.

## B. Scalar pairs of the Spin(12) 32 (exact Casimirs, 528-dim symmetric space)

- Lorentz-scalar Weyl pairs are internally symmetric: (Grassmann) x (eps) is symmetric.
- B1. Sym^2(32) = 66 + 462. There is no Spin(12) singlet, so one 32 is protected (pseudoreal).
- B2. 66 = 45_0 + 1_0 + 10_{+1} + 10_{-1} under Spin(10) x U(1)_A1.
- B3. Light-light pairs (q6 = -1) are 10 + 126, with no singlet (the 16 is protected). Mirror-mirror pairs are
  10 + 126bar.
- B4. Light-mirror scalar pairs are 1 + 45 + 210. **There is no 10: a scalar 10 is never a light-mirror bilinear.**
  The light-mirror 10 is the vector current, i.e. the Spin(12) coset generators.

## C. The Goldstone dichotomy (answers candidate 2; exact)

- C1-C3.
  - Take the pair that breaks Spin(12) -> Spin(10) x U(1). Its stabiliser is 46 and its 20 Goldstones are exactly
    10_{+1} + 10_{-1}, which contain the B-L = 0, Y = +-1/2 doublets and the triplets.
  - That pair is the light-mirror singlet 1_0. Its coefficient matrix is purely light x mirror, full rank, with
    16 equal singular values.
  - It is a Dirac mass for the whole light 16. **A Goldstone 10 exists only if the light family is gapped at f.**
- C4.
  - A mirror-only term (spurion: the A1 occupation, the stand-in for any Spin(10)-invariant SMG interaction on the
    mirror) has the same commutant, 46. It breaks Spin(12) explicitly.
  - SMG is by definition a symmetric phase with no order parameter. So nothing is spontaneously broken, there is no
    Goldstone, and every light-mirror-mixing mode sits at the mirror gap.
  - "Pseudo-Goldstone of the SMG transition" therefore has spontaneous scale zero and explicit breaking of order the
    gap. That gives no PGB.
  - The broken-phase alternative is mirror-condensate-ew C3: v = f, which measurement excludes.
- Result for (2): **FAIL**. Chirality of the light family and a Goldstone 10 are mutually exclusive in the Spin(12)
  frame. This is the on-site analogue of higgs-from-structure's dichotomy. Spin(12) does supply the "B-L = 0,
  colour-singlet doublet generator" that note asked for, but it cannot be kept exact while the light stays chiral and
  the mirror is gapped.

## D. Does the cube split the 10's doublet from its triplet? (candidate 1; exact)

- D1. O_h on the 6 link ends has 3 orbits on pairs: same, antipode P, perpendicular (face) F. So the covariant
  one-body terms are span(1, P, F).
- D2-D3. P gives A1 +1, E +1, T1 -1, so the antipode term groups A1 with E (6 = 3_even + 3_odd). F gives A1 4,
  E -2, T1 0.
- D4. For H = aP + bF, the coset (c_a^dag c_A1) frequencies are -6b for the doublet and -2a - 4b for the triplet.
  **If the tick has no face term (b = 0, "straight-through link ends"), the doublet generator is exact and the
  triplet is split by 2a: doublet-triplet splitting at the one-body level, from inversion parity.** This is the
  E + T1 split again, with A1 joining E.
- D5-D6. The only covariant site-link hop couples the site to A1 (amplitude sqrt(6) h).
  - It gives the doublet a seesaw gap sqrt(a^2/4 + 6h^2) - a/2, about 6h^2/a, verified at h = 0.3, 0.03 and 0.003.
  - The commutant drops from 19 to 15, so the doublet generator is broken.
  - A light doublet needs h/a of about 3e-9 (FITTED).
- In any case the protected object at b = 0 is a generator (a conserved light-mirror current), not a scalar.
  Turning it into a scalar needs spontaneous breaking, which leads back to C.
- The E/T1 labels are orbital (time-complex-structure S5). The generic covariant cone mixes them, so the split does
  not survive covariance.

Scale (estimate): a bosonic 10 = g_a g_A1 has an invariant mass (Sym^2(10) contains 1), so it is unprotected and sits at
the cell, M = 2.44e18 GeV. A light doublet with a heavy triplet needs (m_D/M)^2 of about 2.6e-33 (FITTED).

## E. Yukawa 16 x 16 x 10 (candidate 3; R16 reading)

- E1-E2. B = the product of the 5 imaginary Majoranas is invariant. Y_a = B g_a on 16 x 16 is symmetric, so the
  family matrix Y_fg is symmetric.
- E3.
  - One neutral component (c_1^dag) couples (q u^c) and (L n^c). The other (c_1) couples (q d^c) and (L e^c).
    Every entry has magnitude 1.
  - A single 10 therefore gives m_u = m_nuD and m_d = m_e family by family, CKM = 1, and Y_u = Y_d.
  - A real 10 (H_d = H_u*) also gives m_t = m_b (tan beta = 1).
- E4. With N = 3 and turn charges q_f in {1, 2}, the anomaly condition 4 sum q = 0 mod 3 forces uniform q:
  (1,1,1) or (2,2,2). This sharpens family-count-5mode D7: its family-dependent loophole is closed at N = 3.
- E5. Every Y_fg then carries the same turn phase w^(2q + qH). All 9 entries are allowed, or none are, so there is
  no texture.
- E6. Family symmetry: Sym^2(3) has one SO(3) invariant (Y ~ 1, degenerate families) and no U(3) invariant (Y = 0).
  Neither gives "top largest".
- E7 (seeded diagnostic). For anarchic O(1) symmetric complex Y, 0 of 1e5 samples reach the up-type hierarchy
  (m_c/m_t = 3.2e-3, m_u/m_t = 6.5e-6). The median sigma2/sigma1 is 0.60.
- "Top largest" is trivial (some eigenvalue is largest), but the hierarchy is not produced. y_t of order 1 at the
  cell is natural; y_u of about 1e-5 is FITTED.
- In R5 the propagating fermions are the real 10, so 10 x 10 = 1 + 45 + 54 contains no 10. A 16 16 10 Yukawa
  exists only in R16.

## Estimates against measurement (approximate running values at about 2e16 GeV, cited, not checks of a rule)

| quantity | single-10 prediction | measured (approx.) |
|---|---|---|
| m_b/m_tau | 1 | 0.60 |
| m_s/m_mu | 1 | 0.21 |
| m_d/m_e | 1 | 2.3 |
| |V_us| | 0 | 0.225 |
| m_t/m_b (real 10) | 1 | 74 |
| doublet mass (unprotected 10) | M | 125 GeV, a 2.6e-33 tuning |

## Candidate rules tested (none adopted)

- **S12** (keep the A1 half-link mode; the doublet is a Spin(12)/Spin(10) x U(1) Goldstone).
  - (1) The scale f is not fixed, and v/f is unfixed.
  - (2) No structure is named, so it passes this clause. But it adds a sixth on-site mode, which goes against
    composite-before-atomic.
  - (3) Prediction it was not built for: the light 16 gets a Dirac mass f equal for all members (C1). This
    contradicts the light chiral family and the measured mass spread. FALSIFIED.
  - (4) Bends Qubit (a sixth mode per site).
  - Result: **FAIL**.
- **SMG-PGB** (the doublet is a pseudo-Goldstone of the mirror gap).
  - No spontaneous breaking exists in a symmetric phase (C4). The rule is empty.
  - In the broken phase, v = f (mirror-condensate-ew), which is excluded.
  - Result: **FAIL**.
- **DT** (straight-through link ends, b = 0, A1 kept).
  - (1) Needs h/a of about 3e-9 (FITTED), or the site decouples (an extra light singlet).
  - (2) Passes literally.
  - (3) Predicts the triplet heavy and the doublet seesaw-light, but the light object is a current, not a scalar.
    The orbital-label failure (S5) is inherited.
  - (4) Bends Qubit (modes on link ends).
  - Result: **FAIL**.
- **Y10** (Yukawa from one family-blind 10).
  - (3) Predicts Y_u = Y_d = Y_e and degenerate or vanishing family masses, both contradicted.
  - Result: **FAIL**.

## Smuggling review

- Supplied:
  - the Weyl-species reading R16, needed for B, C and E (R5 has no species 16, chirality-5mode-cones);
  - the A1 mode;
  - the one-body spurion as the stand-in for SMG (C4);
  - b = 0 (D);
  - the anarchic Gaussian prior (E7);
  - the approximate running masses.
- Forced (exact): A1-A8, B1-B4, C1-C4, D1-D6, E1-E6.
- No measured number is used in any rule. Measured values enter only the table.

## What a light-Higgs rule would now need

1. A bosonic 10 or doublet needs a Spin(10)-singlet fermion or a non-fermionic register that carries Omega-odd
   charge. Registers are centre-blind (ax6-higgs A2), so it has to be a singlet fermion. A singlet built from sites
   (composite) rather than a sixth on-site mode would satisfy composite-before-atomic. Not tested here.
2. A symmetry with a light-mirror doublet generator that is spontaneously broken WITHOUT gapping the light family.
   C shows that in Spin(12) the breaking pair is the light Dirac mass. A momentum-dependent (corner-only) breaking
   pair evades C, but higgs-from-structure B3 shows that the update gives no separate light/mirror rotations there.
3. Family hierarchy: with N = 3 the turn is texture-free (E4-E5), so the hierarchy needs a new family-distinguishing
   rule.

## Used / narrowed / contradicted

- why-five-modes: used (the 16, protection). Narrowed by A7: protection is Fock content, and no bosonic 10 exists in R5.
- time-complex-structure: used (rule TJ, E + T1, S5, S7). S7's "16 + 16bar" is extended: Spin(12)'s scalar 10s are
  light-light and mirror-mirror, and the Goldstone 10 needs the light Dirac mass.
- chirality-5mode-cones: used (cones carry the 10). A7 adds that every 10 in R5 is fermionic.
- higgs-from-structure: its dichotomy is rederived in the on-site Spin(12) frame (C).
- mirror-condensate-ew: B1 and C3 are used. ax6-higgs: A2 is used, and its conclusion stands.
- family-count-5mode: its D7 loophole is closed at N = 3 (E4).
- Repo search on main ("doublet-triplet", "Spin(12)"): nothing found. Open PRs: none on these topics.

## Boundary

The theorems are exact representation theory, weight algebra and finite linear algebra on one site's Fock space
(64 states) and its pair space (1024). The SMG interaction is represented by its one-body spurion. Not computed:
interacting mirror dynamics, momentum-dependent condensates, 3D lattice phases, RG of the seesaw ratio, and Yukawa
running. Nothing here excludes a doublet built from a composite singlet fermion.
