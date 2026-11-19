---
claim_id: a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free light bands of FREEZE (twist-local-single; W_F = (-2,1,1), the family-class tick of tick-winding-origin) on CL-1's 2x2x2 cell. (1) FREEZE's on-cell magnetic point group (node-faithful K-independent intertwiners among CL-1's 24 rotations x inversion x chiral x antiunitary) has order 96, half of CL-1's 192: an element is kept iff [R not tetrahedral] = inversion + chiral + antiunitary (mod 2). (2) On the 4-state node space (L q = 2 plus R q = 1) at K = 0 and at R the group allows 0 constant, 1 linear and 1 quadratic real coupling, each FREEZE's own: no b-type term, an isotropic cone with equal L and R speed 1/sqrt3, and one L-R term m(K) = (sqrt2/6)(Kx^2 + w Ky^2 + w^2 Kz^2). (3) m(K) is the only structure to order K^2 that is odd under C2', T and inversion. (4) FREEZE's light dispersion is exactly cos theta = mean cos K, so every level is 2-fold, even in K, with cubic anisotropy -(1/36)(Ka)^2; at order K^3 the group also allows a T-odd k_x k_y k_z term, which is 0 in FREEZE. (5) Each node keeps one protected L (q = 2). Not covered: interactions, gauge fields, the copy mass, K-dependent intertwiners, photon bands, which physical species these Weyls are."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - no_principle_tested_forces_a_nonzero_turn_graded_tick_winding_because_chiral_walls_exist_at_zero_winding_time_reversal_forbids_the_family_class_and_fewest_changes_selects_zero_bounded_theorem_note_2026-10-24
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_2026_10_24.py
---

# A family-class tick keeps a 96-element magnetic group that forbids every low-energy rotation- or Lorentz-violating dispersion term below dimension six, and leaves its time-reversal breaking in one chirality-flip term

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] estimate or reading.
Runner: runner.py, TOTAL: PASS=9 FAIL=0, 14 s, 72 MB peak, 3.8 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/t_breaking_tick_lowenergy_test_run.py). Axioms unchanged. No rule adopted.

## Question

tick-winding-origin showed that a family-class tick (W with all three components nonzero, for example FREEZE's
W_F = (-2, 1, 1)) has to break Floquet T and the axis-reversing part of CL-1's 24-rotation covariance. Before adopting
"the update tick is family-class", we need to know whether that breaking reaches low energy. Three checks:
(1) Is the light cone isotropic at O(K)? At which order does anisotropy appear? Is there a dimension-3 or dimension-4
    term that is T-odd or breaks rotations?
(2) How do the coefficients compare with SME-type bounds for a Planck-scale step?
(3) Does the light L stay one protected node with q = 2, and where does the T breaking show?

Repo first: a git grep of origin/main for "magnetic point group", "kx ky kz" and "chirality-flip term" found only
generic lattice-anisotropy runners (for example frontier_emergent_lorentz_spatial_bz_power_mixing_boundary), which are
not about this tick. Open PR #10065 is tick-winding-origin, which this note builds on. Criteria were written before any
code (criteria_pre_run.txt) and used unchanged.

## 1. The exact symmetry group [T]/[F]

- We searched every element (R in CL-1's 24 rotations; K -> +-RK; U or U^+; unitary or antiunitary) for an on-cell
  intertwiner that is invertible on the light node space. The search used 12 random momenta; with fewer momenta it
  found spurious null vectors, so 12 is needed.
- FREEZE keeps exactly 96 of the 192 elements that CL-1's tick has (the 192 is re-checked in the runner). The rule is:
  element kept <=> [R is not one of the 12 tetrahedral rotations] = inversion + chiral + antiunitary (mod 2).
  - Kept: the 12 tetrahedral rotations T; the T_d mirrors and S4 (inversion x C2', C4); the campaign's CPT-type map
    (chiral x inversion); particle-hole (U(K) -> U(-K), antiunitary); PT; T x C2' and T x C4.
  - Broken when taken alone: C2', C4, Floquet T, inversion and chiral.
- So "only the 12 proper rotations" undercounts what is left. The group is a full 96-element magnetic group. Each broken
  operation survives once composed with a C2' or C4. (This is the same pattern as the register's copy-mass statement:
  "breaking ... T ... but keeping both composed with a fourfold turn".)

## 2. Allowed low-energy terms on the light node space [T]

Effective H (U = exp(-iH)) on the 4 light states (L q = 2 plus R q = 1, degenerate at quasienergy 0 at K = 0 and at
pi at R). We projected generic Hermitian polynomials onto the group and counted the real couplings that survive.

  order        K = 0   R    content
  K^0 (dim 3)    0     0    no b_mu, no L-R offset (b_0), the node cannot move or split
  K^1 (dim 4)    1     1    FREEZE's own tau3 sigma.K / sqrt3: isotropic, equal L and R speed, no L-R linear mix
  K^2 (dim 5)    1     1    FREEZE's own m(K): purely L-R, (sqrt2/6)(Kx^2 + w Ky^2 + w^2 Kz^2), no cross terms

- Dimension 4. The cone is isotropic. The only free number is the overall speed (1/sqrt3 sites per tick), so there are
  no c_jk, no c_0j and no species-dependent speed between L and R.
- Dimension 3. Nothing is allowed.
- Dimension 5. One term, m(K): a chirality-flip (L-R) coupling with the turn-phase pattern 1 : w : w^2. It is a pure
  E (quadrupole) pattern that vanishes along (111).

## 3. Where the T breaking sits [T]

- The linear cone on its own has partner intertwiners for C2', T and inversion (each space is 2-dimensional).
- Once m(K) is added, none of the three survives, while T.C2' still does.
- So up to order K^2, m(K) is the only structure at low energy that is T-odd and rotation-odd. It is the family/CP
  phase of the tick, carried as an L-R coupling.

## 4. Dispersion [T]/[F]

- Exact: on the light sector, cos theta = (cos Kx + cos Ky + cos Kz)/3. This follows because CTWIST's generators are
  Clifford, so U = f + iX with X^2 a scalar, and the spectrum depends only on f. Consequences:
  - every level is 2-fold, so there is no helicity or L-R split at any order;
  - theta(K) = theta(-K);
  - m(K) enters the spectrum only as |m|^2 ~ K^4.
- Isotropic at O(K). The spread of the speed over directions scales as K^2 (the ratio is 4.000 when K is halved).
  v(axis) - v(111) = -(1/36)(Ka)^2 v, a cubic term of dimension 6.
- Class statement at order K^3. The group allows 3 real couplings: two T-even cubic ones, and one T-odd, rotation-odd
  k_x k_y k_z term. That term gives v(n) != v(-n) proportional to n_x n_y n_z (Ka)^2, which is dimension 6. Its
  coefficient is 0 in FREEZE but is not forbidden for deformations of the class.

## 5. Protected nodes and the bound comparison

- [T] Each node (K = 0 and R) keeps exactly one 2-fold L Weyl with q = 2, plus the R mirror with q = 1. No allowed
  constant can move, split or gap them.
- [S] Bounds. With a Planck-scale step, Ka = (E/E_P)(a/l_P), using the campaign map eta = 2(c/v)(a/l_P).

    term                     FREEZE value      bound                    result
    b (dim 3)                0 (forbidden)     ~1e-31 GeV               PASS
    c_jk, c_0j (dim 4)       0 (forbidden)     ~1e-21                   PASS
    dim-5 dispersion eta     0 (no K^2 in E)   Crab |eta| < ~1e-7       PASS
    dim-6 cubic              (1/36)(Ka)^2      at 1e20 eV: 2e-18 (a = l_P) to 2e-16 (10 l_P); GRB/UHECR dim-6
                                               limits are far weaker                   PASS
  - The T-odd m(K) does not change the dispersion. It shows only as a chirality admixture of amplitude
    ~0.41 |P(n)| Ka, where P(n) = nx^2 + w ny^2 + w^2 nz^2. That is 3e-17 to 3e-16 at 1 TeV.
  - [S, conditional] If a Dirac mass M were ever formed from this L-R pair, interference with m(K) would give an
    E-pattern c_jk ~ 0.71 (M/E_P)(a/l_P). For an electron that is 3e-23 to 3e-22, below ~1e-21. The R here is the
    mirror, not an identified Dirac partner, so this is a reading, not a prediction.

## Answer

PASS on the pre-set criterion. In FREEZE's light bands there is no rotation- or Lorentz-violating term of dimension
<= 4; the 96-element group forbids all of them, including b and c. The dimension-5 dispersion term is zero and the
leading anisotropy is (Ka)^2, two powers of Ka, more than the one power the criterion asked for.
- The T breaking does reach low energy, but only through one structure up to K^2: the chirality-flip term m(K), which
  carries the turn phase (the family/CP structure).
- It is invisible in every spectrum at dimension <= 5.
- At dimension 6 the class also permits an n_x n_y n_z reciprocity-odd term, which FREEZE itself does not have.
- The light L (q = 2) is a single protected 2-fold node at each node point.

Cost of adoption, for the gate entry: the bends are the ones already listed (Floquet T, C2'/C4 alone, fewest changes).
Low-energy measurement adds no new failure at this level.

## Smuggling review

- Supplied:
  - FREEZE and CTWIST (with the Pi split and the i tau3 quarter phase);
  - free fields;
  - the restriction to K-independent on-cell intertwiners;
  - the node-space truncation;
  - the SME/Crab/GRB bound values (order of magnitude);
  - the step a = 1 to 10 l_P.
- Forced:
  - the 96-element group and its Z2 grading rule;
  - the allowed-term counts 0/1/1 at both nodes and 3 at K^3;
  - FREEZE's terms lie in those spaces;
  - m(K)'s pattern, size and its oddness under C2', T and inversion;
  - the exact dispersion cos theta = mean cos K and its consequences;
  - the node charges and handedness.
- Not shown:
  - interactions and link dressing, which could generate the allowed k_x k_y k_z term (dimension 6, harmless at this
    size);
  - photon bands;
  - the copy mass on top of FREEZE;
  - K-dependent symmetries.
