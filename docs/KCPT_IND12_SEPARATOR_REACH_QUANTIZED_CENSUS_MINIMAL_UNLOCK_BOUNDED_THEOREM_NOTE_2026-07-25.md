# KCPT — ind12 Separator Reach: a Numerically Resolved Census over 768 Ambient Single-Element Extensions and a 28-Dimensional Central Extension (Bounded Theorem)

**Type:** bounded_theorem
**Date:** 2026-07-25
**Lane:** KCPT (periodic L = 4, N = 64 staggered lattice on the 4³ torus)

## Opening

The bicommutant-dimension note found that the center Z(𝒜) = C⁵ of the Dirac-symmetry
algebra has one direction beyond C[M] = C⁴: the ind12 separator
sep = P_a − P_b, which splits shell m = 2 into two rank-12 H-constituents. This note
examines that separator within the family of single ambient-group-element extensions of

  𝒜_nat := ⟨D2, J_full, S_eps⟩.

On the fixed surface and at the stated tolerances, a census of all 768 extensions
numerically resolves four reach values {0, 1/9, 1/3, 1}. It also identifies a smallest
reaching H-class and an explicit 28-dimensional extension in which sep is numerically
represented as a difference of minimal central idempotents.

## Claim boundary

The surface is the periodic L = 4, N = 64 staggered lattice with integer antisymmetric
adjacency D2; M = D2²; shell eigenvalues λ_m = −4m and inherited shell dimensions
[8, 24, 24, 8]; J_full² = −I; S_eps = diag((−1)^(x₁+x₂+x₃)); the 768-element signed-
permutation group G_amb; and H = ⟨G_amb, S_eps⟩. It reuses the six multiplicity-free
H-constituents C⁶⁴ = 8 + 8 + 12 + 12 + 12⁺ + 12⁻ and defines P_a and P_b as the tagged
rank-12 pair on shell m = 2, with sep := P_a − P_b.

No new free parameter, dynamics, bulk sign-family member, external numerical value, or
literature input is introduced. The result is r-neutral and orientation-neutral. No
physical CP, chirality, measurement, readout, conservation, superselection, or Record
identification is asserted. Unless a singular value or another norm is named, matrix
norms are Frobenius norms.

For an orthonormal basis B, define

  resid(B, sep) := ‖sep/‖sep‖_F − Π_B(sep/‖sep‖_F)‖_F,
  overlap²(B, sep) := 1 − resid(B, sep)².

The companion runner recomputes and gates the new algebra dimensions, closure results,
class counts, reach values, character values, center dimensions, numerical separation
margins, idempotent ranks, and residuals used below. The order of H and the starting shell
dimensions are inherited construction checks, not claimed as newly re-gated results.

## Construction recap

The runner rebuilds the lattice, coordinates, staggered signs η_μ, D2, M, four shell
projectors Pf[m], the kernel complex structure, J_bulk, J_full, S_eps, G_amb, H generators,
the six constituent projectors, and the tagged ind12 pair. It is self-contained and does
not import or execute another runner. The separator is defined once as
`sep = Ps[i_ind12[0]] - Ps[i_ind12[1]]`.

The 768-element ambient-group order is re-gated by `CENSUS-ELEMENT-COUNT`. The order of H
and the shell dimensions are inherited from the Schur-forced fused-block construction.

## Native frame and resolution ladder

The word algebras numerically true-close below cap 350 at

- dim_C⟨D2⟩ = 7;
- dim_C⟨D2, J_full⟩ = 8; and
- dim_C 𝒜_nat = 16.

The relations J_full² = −I, S_eps² = I, and {J_full, S_eps} = 0 hold with residual below
1e-12. The per-shell restriction dimensions are [4, 4, 4, 4]. The commutant-in-𝒜_nat
nullspace has dimension 4, its largest dropped singular value is below 1e-8, its smallest
kept singular value exceeds 1e-4, and every Pf[m] has residual below 1e-10 against that
nullspace. Thus the finite computation numerically resolves

  𝒜_nat ≅ M₂(C)^⊕4,   Z(𝒜_nat) = C[M],

at the stated tolerances, and the following concrete word-algebra ladder:

  C[M] (dim 4) ⊂ C[D2] (dim 7) ⊂ ⟨D2, J_full⟩ (dim 8)
  ⊂ 𝒜_nat (dim 16) ⊂ 𝒜 (dim 992).

## Separator non-membership in the native frame

The computation gives |overlap²(𝒜_nat, sep)| ≤ 1e-10. Accordingly, sep is not represented
in 𝒜_nat at the stated tolerance. This is only a finite operator-algebra non-membership
statement. It does not imply that a physical split is unread, unrecorded, or impossible;
nor does it select a measurement or readout context.

## H-stability and reach census

Conjugation by the five H-generators preserves 𝒜_nat to residual below 1e-10, fixes sep to
residual below 1e-10, and normalizes G_amb by integer matrix equality. Therefore

  ω(g) := overlap²(⟨𝒜_nat, g⟩, sep)

is numerically invariant on the computed H-conjugacy classes. The 36 classes partition all
768 elements. Every representative true-closes below cap 350. At match tolerance 1e-9,
the observed reach labels are {0, 1/9, 1/3, 1}, with element counts
{528, 12, 96, 132}. The joint histogram is:

| closed dim | ω = 0 | ω = 1/9 | ω = 1/3 | ω = 1 |
|-----------:|------:|--------:|--------:|------:|
| 16 | 4 | · | · | · |
| 24 | 12 | · | · | · |
| 28 | · | 12 | · | 4 |
| 32 | 96 | · | · | · |
| 48 | 320 | · | · | · |
| 76 | · | · | · | 128 |
| 88 | 96 | · | · | · |
| 96 | · | · | 96 | · |
| **total** | **528** | **12** | **96** | **132** |

The ω = 1/3 tier consists of four size-24 classes whose representatives have order 8. The
ω = 1 tier consists of one size-4 class of order 4 and two size-64 classes of order 12.

## Character/reach relation

For Δχ(g) := Re(tr(P_a g) − tr(P_b g)), the computed class representatives match
{0, +4√2, −4√2} within 1e-9. At the same tolerance, the nonzero-Δχ classes are the four
ω = 1/3 classes, while every ω = 1 class has Δχ = 0. This is a numerical set match on the
fixed class census, not a symbolic theorem about other surfaces or extension families.

## The 28-dimensional central extension

Define

  g1 = diag((−1)^{x₂}) · T₍₁,₁,₁₎.

Integer matrix equality verifies g1 ∈ G_amb and g1⁴ = I. Its H-orbit is exactly
{g1, g1³, −g1, −g1³}; the other fully reaching classes have size 64. The extension

  A28 := ⟨𝒜_nat, g1⟩

numerically true-closes at dimension 28, has ω(g1) = 1 within 1e-9, and has per-shell
restriction dimensions [4, 8, 8, 8]. Its computed center has dimension 7, with largest
null singular value below 1e-8 and smallest kept singular value above 1e-4. Two
deterministic complex central samples each resolve seven eigenvalue clusters; their
maximum within-cluster gaps are below 1e-8 and their minimum between-cluster gaps exceed
1e-4.

The generators make A28 a finite-dimensional *-algebra:
D2* = −D2, J_full* = −J_full, S_eps* = S_eps, and g1* = g1³. The seven sampled central
idempotents have numerical corner dimensions 4, so the computation resolves

  A28 ≅ M₂(C)^⊕7

at the stated tolerances. Their ranks are {4, 4, 8, 12, 12, 12, 12}, with shell supports
8@0 | 12,12@1 | 12,12@2 | 4,4@3. The two shell-2 idempotents match {P_a, P_b} within
1e-8, and ‖sep − (e_a − e_b)‖_F < 1e-8. Thus sep is numerically represented as a
difference of minimal central idempotents in A28. No physical “charge” interpretation is
attached to this centrality statement.

## Shift-direction contrasts

With the sign field (−1)^{x₂} fixed, shift (1,1,1) gives ω = 1 at dimension 28;
shift (1,1,3) gives ω = 1/9 at dimension 28; and shift (1,1,2) gives
|ω| ≤ 1e-10 at dimension 48. Thus extension dimension alone does not determine the
observed reach. Two sign-dressed axis rotations give dimension 76, ω = 1, order 12, and
H-class size 64, showing a second full-reach route above the smallest class.

## No-Go Discipline for the bounded non-membership statement

The negative statement in scope is only: `sep` is not represented in the computed
16-dimensional 𝒜_nat at the stated finite-surface tolerance.

- **N1 — alternative routes:** five route families were stress-tested: true word-monoid
  closure; Hilbert–Schmidt projection residual; the Z(𝒜_nat) = C[M] characterization;
  shell-wise M₂ central-scalar structure; and an independent block-QR/right-multiplication
  span reconstruction with a tolerance sweep.
- **N2 — wall independence:** there is one operative numerical wall, the fixed finite
  matrix surface with explicit tolerances; no second physical impossibility wall is used.
- **N3 — hidden walls:** no registration, readout, Record, dynamics, continuum, or
  arbitrary-L premise is inferred from algebra membership.
- **N4 — residual matching:** the residual supports only numerical non-membership in
  𝒜_nat; the rhetoric is restricted to that residual.
- **N5 — rhetoric:** the claim is limited to this 64×64 representation and this generated
  algebra, not all sites, modes, surfaces, or physical contexts.
- **N6 — partial closure:** the 1/9 and 1/3 tiers and the fully reaching A28 extension are
  retained as explicit routes outside 𝒜_nat; no universal no-go is claimed.
- **N7 — steelman:** a tolerance-dependent rank misclassification is the strongest
  objection. Independent tolerance sweeps preserved dimensions 16 and 28 from 1e-7
  through 1e-11, while the live center gaps separate kept values near 2 from null values
  below 5e-15. This supports the numerical claim, not an exact symbolic one.
- **N8 — cross-cycle echo:** earlier KCPT reviews warn against promoting fixed-operator or
  algebra-exclusion results into universal physical no-go claims. This statement preserves
  that boundary.

**No-Go disposition:** PASS for the narrowed numerical operator-algebra statement.

## Boundary / honest-auditor read

This is a numerical class-A verification on one fixed L = 4 surface. The reach labels and
counts are measured to 1e-9, not symbolically proved. The census covers single-element
extensions only. Multi-element extensions, subgroup extensions, other surfaces, continuum
limits, dynamics, and physical identifications remain open. The observation
1/9 = (1/3)² is an unexplained numerical coincidence here. The periodic boundary, the
g = I counting metric, and the chosen J_full sign-family representative are inherited
finite-surface inputs. Both direct dependencies are unaudited; this note asserts no audit
grade or publication-usable status and requires an independent audit.

## Two paths this opens

- Test whether the four reach labels and nine-cell histogram persist or refine at
  L = 6 and L = 8.
- Classify multi-element and subgroup extensions between 𝒜_nat and 𝒜, keeping algebraic
  containment separate from any physical interpretation.

## Runner evidence

The companion runner
`scripts/kcpt_ind12_separator_reach_quantized_census_minimal_unlock_2026_07_25.py`
reports `TOTAL: PASS=49 FAIL=0`. Each gate uses a descriptive scientific name:

| Gate | Expected value |
|------|----------------|
| `NATIVE-D2-ALGEBRA` | dim⟨D2⟩ = 7 at true closure. |
| `NATIVE-DIRAC-PAIR` | dim⟨D2,J_full⟩ = 8 at true closure. |
| `NATIVE-FRAME-DIM` | dim 𝒜_nat = 16 at true closure. |
| `NATIVE-COMPLEX-STRUCTURE`, `NATIVE-PARITY-INVOLUTION`, `NATIVE-GRADING-ANTICOMMUTATION` | defining relation residuals below 1e-12. |
| `NATIVE-SHELL-BLOCKS` | shell dimensions [4,4,4,4]. |
| `NATIVE-CENTER-DIM`, `NATIVE-CENTER-GAP`, `NATIVE-CENTER-CM` | center dimension 4, live null/kept gap, shell projectors in the center span. |
| `NATIVE-SEPARATOR-ORTHOGONALITY` | Absolute overlap²(𝒜_nat,sep) ≤ 1e-10. |
| `STABILITY-PARITY-OUTSIDE-AMBIENT`, `STABILITY-AMBIENT-NORMALITY` | H extension and normalization checks. |
| `STABILITY-NATIVE-FRAME`, `STABILITY-SEPARATOR` | H preserves 𝒜_nat and sep below 1e-10. |
| `CENSUS-CLASS-COUNT`, `CENSUS-ELEMENT-COUNT` | 36 classes and 768 elements. |
| `CENSUS-TRUE-CLOSURE`, `CENSUS-REACH-SPECTRUM`, `CENSUS-REACH-COUNTS`, `CENSUS-DIM-REACH-HISTOGRAM` | closure and four-tier/nine-cell census. |
| `CENSUS-THIRD-ORDERS`, `CENSUS-FULL-REACH-ORDERS` | order structure of nonzero tiers. |
| `CHARACTER-SPECTRUM`, `CHARACTER-THIRD-INVERSION`, `CHARACTER-FULL-BLINDNESS` | character/reach numerical set relations. |
| `UNLOCK-MINIMAL-ELEMENT-MEMBERSHIP`, `UNLOCK-MINIMAL-ELEMENT-ORDER`, `UNLOCK-MINIMAL-ELEMENT-ORBIT`, `UNLOCK-MINIMAL-CLASS` | g1 and its smallest reaching class. |
| `UNLOCK-ALGEBRA-DIM`, `UNLOCK-FULL-REACH`, `UNLOCK-SHELL-DIMS` | A28 closure, reach, and shell dimensions. |
| `UNLOCK-CENTER-DIM`, `UNLOCK-CENTER-GAP` | center dimension 7 and live null/kept gap. |
| `UNLOCK-CENTER-CLUSTERS-PRIMARY`, `UNLOCK-CENTER-CLUSTERS-CONTRAST` | seven well-separated clusters for both seeds. |
| `UNLOCK-WEDDERBURN-BLOCKS`, `UNLOCK-IDEMPOTENT-RANKS`, `UNLOCK-SHELL-SUPPORTS` | seven numerical M₂ corners, ranks, and shell supports. |
| `UNLOCK-SHELL2-IDEMPOTENTS`, `UNLOCK-SEPARATOR-IDEMPOTENTS` | shell-2 and separator matches below 1e-8. |
| `SHIFT-REACH-NINTH`, `SHIFT-REACH-ZERO`, `SHIFT-DIMENSION-CONTRAST`, `ROTATION-FULL-REACH` | shift and rotation contrasts. |
| `REACH-IN-FRAME-CONTROL`, `REACH-DIAL-CONTRAST`, `REACH-SIGNFIELD-PERTURBATION` | independent discriminating controls. |

## Dependencies

- [the bicommutant-dimension note](KCPT_DIRAC_SYMMETRY_ALGEBRA_BICOMMUTANT_DIMENSION_992_BOUNDED_THEOREM_NOTE_2026-07-24.md) — supplies 𝒜, its center, and the ind12 separator.
- [the Schur-forced fused-block superstructure note](KCPT_DIRAC_CHISGN_COVARIANCE_SCHUR_FORCED_FUSED_BLOCK_SUPERSTRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-24.md) — supplies the finite lattice, operators, groups, and constituent projectors reused by the runner.

Earlier notes enter transitively through these two direct dependencies. No non-KCPT document
is a load-bearing dependency.
