# KCPT: L = 6 Surface Change — Module Structure and Natural-Algebra Invariance (Bounded Theorem)

**Type:** bounded_theorem
**Date:** 2026-07-25
**Lane:** KCPT (periodic L = 6, N = 216 staggered lattice on the 6³ torus, compared against the landed L = 4, N = 64 lane)
**Runner:** `scripts/kcpt_l6_surface_change_module_structure_natural_algebra_invariance_2026_07_25.py`

## Opening

The landed L = 4 lane resolved a compact picture: on the 4³ torus the ambient module
C⁶⁴ splits into six multiplicity-free H-constituents, the Dirac-symmetry algebra
𝒜 = ⟨D2, J_full, ρ(H)⟩ has dimension 992 with abelian center C⁵, and the natural core
𝒜_nat = ⟨D2, J_full, S_eps⟩ is M₂(C)^⊕4 with center C[M]. The single direction of the
center beyond C[M] is the ind12 separator, and 𝒜_nat is numerically blind to it.

This note ports that structure map to the L = 6, N = 216 surface and records what changes
and what does not. The finding is a **surface-change / surface-stability dichotomy**. The
ambient module and the ambient algebra grow and lose multiplicity-freeness: the H-endomorphism
algebra rises from an abelian C⁶ to a 19-dimensional non-abelian algebra, the ambient algebra 𝒜 rises from
dimension 992 to 4224, and the separator space (the center of 𝒜 modulo C[M]) rises from
dimension 1 to dimension 9. The natural core is unmoved: 𝒜_nat keeps the same abstract type
M₂(C)^⊕4 with center C[M], and stays numerically blind to the now nine-dimensional separator
space at the stated tolerances.

## 1. Setup

The surface is the periodic L = 6, N = 216 staggered lattice on the 6³ torus with integer
antisymmetric adjacency D2 built from staggered phases η_μ (η₀ = 1, η₁ = (−1)^{x₀},
η₂ = (−1)^{x₀+x₁}). Write M = D2². Its shell eigenvalues are λ_m = −3m for
m = 0, 1, 2, 3 with inherited dimensions

  [8, 48, 96, 64],   dim_m = C(3, m)·2^{3−m}·4^m,   Σ dim_m = 216,

and shell projectors Pf[m] taken as integer Lagrange interpolants of M. The kernel shell
carries the eight ±1 sign vectors; the complex structure

  J_full = J_ker + J_bulk,   J_bulk = Σ_{λ_m ≠ 0} D2·Pf[m]/√|λ_m|,

is real antisymmetric with J_full² = −I. The parity involution is
S_eps = diag((−1)^{x₀+x₁+x₂}), with S_eps·D2·S_eps = −D2.

The Dirac sign character χ_sgn on signed permutations is defined by h·D2·hᵀ = χ_sgn(h)·D2.
The ambient group G_amb is the ported L = 4 lane construction: the closure of all signed
permutations of the form (base coordinate map) ∘ (quadratic sign field) ∘ (translation)
that commute with D2, where the base maps are the identity, U2: x ↦ (−x₁, −x₀, −x₂), and
UR: x ↦ (x₁, x₂, x₀), and the sign fields are the 64 quadratic characters
(−1)^{a·x + Σ b_{ij} x_i x_j}. It has order 2592 = 6³·12, and H = ⟨G_amb, S_eps⟩ has order
5184 with [H : G_amb] = 2. The kernel of χ_sgn on H is exactly G_amb, and χ_sgn(S_eps) = −1.

H is a symmetry group of D2, not the maximal one: an explicit dressed four-fold rotation
g_r4 = diag((−1)^{x₀x₁ + x₀}) R4, with R4 implementing
r4: x ↦ (x₁, −x₀, x₂), commutes with D2 exactly (χ_sgn = +1) yet lies outside H, on the
L = 6 and the L = 4 surface alike (gates B8, E4b). Under the runner's dense column-vector
convention, R4 acts first and the sign field acts second. All group-level counts in this
note are therefore statements about this H, the lane's fixed comparison group, not about
the full symmetry group of D2.

The runner is self-contained: it rebuilds every L = 6 object above from scratch, and also
rebuilds the entire L = 4, N = 64 surface (adjacency, shells, complex structure, group,
per-shell H-endomorphism algebras) from scratch for the direct comparison. It loads no saved
data and executes no other runner.

Unless a singular value or another norm is named, matrix norms are Frobenius norms. For an
orthonormal Frobenius basis B and a matrix X, define overlap²(B, X) = ‖B̄·(vec X / ‖vec X‖)‖²
and resid²(B, X) = 1 − overlap²(B, X).

## 2. Theorem (numerically resolved at the stated tolerances)

**T1 — Surface (A).** On the 6³ torus, D2 is integer with D2ᵀ = −D2; M has spectrum
{0, −3, −6, −9} with well-separated integer clusters (max |ev − round| ≤ 2e-14) and
dimensions [8, 48, 96, 64] matching the combinatorial formula; the kernel is eight-dimensional
with an exact ±1 sign basis annihilated by D2; and J_full is real, antisymmetric, with
‖J_full² + I‖ ≤ 5e-16 (max-entry norm).

**T2 — Symmetry group and Dirac sign character (B).** |G_amb| = 2592, |H| = 5184,
[H : G_amb] = 2, and S_eps ∉ G_amb. H has 137 conjugacy classes with size multiset
{1:2, 2:5, 3:4, 4:3, 6:24, 12:57, 54:6, 72:6, 108:21, 144:9}, and G_amb decomposes into 75
orbits under H-conjugation with size multiset
{1:2, 2:3, 3:4, 4:1, 6:14, 12:27, 54:6, 72:6, 108:9, 144:3}. The character χ_sgn takes value
+1 on exactly 2592 elements and −1 on exactly 2592 elements (none neither), its +1 kernel
equals G_amb as a set, it is multiplicative on seeded products, and χ_sgn(S_eps) = −1 with
S_eps·D2·S_eps = −D2.

**T3 — The ambient module gains multiplicity (C).** The H-endomorphism algebra End_H(C²¹⁶)
has dimension 19, computed two independent ways that agree: as the Frobenius-independent count
of H-averaged operators, and as the character inner product c_H = ⟨χ, χ⟩_H = 19. The per-shell
commutant dimensions are c_m = [1, 4, 8, 6] (character and dimension counts agree), the
cross-shell homomorphism spaces vanish (≤ 2e-16), and 19 = 1 + 4 + 8 + 6. The
per-shell isotypic decomposition, computed by the H-averaged-commutant method and clustered at
two independent seeds (7 and 1234) with identical, seed-stable results, is

  m = 0: one irrep of dimension 8, multiplicity 1;
  m = 1: one irrep of dimension 24, multiplicity 2;
  m = 2: four irreps of dimension 12, multiplicity 1, and one of dimension 24, multiplicity 2;
  m = 3: two irreps of dimension 8, multiplicity 1, and one of dimension 24, multiplicity 2.

For every shell Σ mult² = c_m and Σ mult·dim = dim_m. End_H is non-abelian: two commutant
elements have ‖[X, Y]‖ ≈ 0.28. This is the surface change — the L = 4 module is
multiplicity-free with abelian End_H = C⁶ (re-verified from scratch, gate E4b), whereas the L = 6 module carries multiplicity-2
constituents and a 19-dimensional non-abelian endomorphism algebra.

**T4 — The natural core is invariant (D).** The word algebra 𝒜_nat = ⟨D2, J_full, S_eps⟩
true-closes at dimension 16 with center of dimension 4 spanned by the shell projectors
(overlap²(Z, Pf[m]) = 1 to 1e-12). Its Wedderburn decomposition, resolved at two seeds
(7 and 1234), has four blocks of block-algebra dimension 4 and block-center dimension 1 (each
an M₂(C)), with block idempotents equal to the shell projectors (‖P_block − P_shell‖ ≤ 2e-13)
and ranks {8, 48, 64, 96}. Thus 𝒜_nat ≅ M₂(C)^⊕4 with Z(𝒜_nat) = C[M], the same abstract
type carried on the L = 4 surface. The abstract natural core does not change under the surface
change.

**T5 — The ambient algebra grows (E1–E4).** The ambient commutant
𝒜′ = End_H ∩ {D2}′ ∩ {J_full}′ (the center of 𝒜 = ⟨D2, J_full, ρ(H)⟩) has dimension 13,
resolved by a clean Gram spectral gap (null block ≤ 3e-14, first non-null value 16.0 against
scale 40.0), and is abelian (≤ 2e-15). Its minimal idempotent ranks, resolved identically at
two seeds (11 and 2024), are [8, 8, 8, 12, 12, 12, 12, 24, 24, 24, 24, 24, 24], summing to 216,
so dim 𝒜 = Σ rᵢ² = 4224. Run through the identical machinery, the L = 4 surface (|H| = 1536)
reproduces its landed values dim 𝒜′ = 5, ranks [8, 8, 12, 12, 24], dim 𝒜 = 992. The ambient
algebra grows from 992 to 4224 across the surface change.

**T6 — The separator space grows while the core stays blind (E5–E8).** Inside 𝒜′, the
orthogonal complement of C[M] has dimension 9 at L = 6, against dimension 1 at L = 4 through
the same construction. A named representative sep6 = P₈ₐ − P₈ᵦ, the difference of the two
multiplicity-1 rank-8 isotypic projectors on shell m = 3, has rank sum 16 and ‖sep6‖ = 4,
and commutes with D2, J_full, and 400 seeded ρ(h) (all ≤ 6e-14). The natural core is
numerically blind to the entire separator space: the gate threshold is
overlap²(𝒜_nat, ·) ≤ 1e-10, and the observed values are ≲ 1e-30 (seed-dependent in the
trailing digits) for all nine
complement directions, for sep6, and for the six pairwise differences of the four
multiplicity-1 rank-12 isotypic projectors on shell m = 2. A wrong-value control confirms the
test discriminates: augmenting the 𝒜_nat Frobenius basis with sep6/‖sep6‖ raises the overlap²
against sep6 from ≈ 1e-31 to 1 (to 1e-12). Thus the separator space grows nine-fold across the
surface change while remaining outside the natural core at the stated tolerances.

## 3. Record numbers

The runner reports `TOTAL: PASS=34 FAIL=0`. Representative resolved values:

| Quantity | Value |
|----------|-------|
| M spectrum integrality (max \|ev − round\|) | 2.0e-14 |
| ‖J_full² + I‖ (max-entry) | 4.4e-16 |
| cross-shell homomorphism (max) | 1.8e-16 |
| End_H non-abelian witness ‖[X, Y]‖ | 0.28 |
| c_H (character = dimension) | 19 = 1 + 4 + 8 + 6 |
| dressed-r4 witness (L = 6 and L = 4) | commutes with D2, outside H |
| 𝒜_nat Wedderburn idempotent alignment (max over seeds) | 1.4e-13 |
| Z(𝒜_nat) shell-projector overlap² | 1.0 (≥ 1 − 1e-10) |
| 𝒜′ Gram spectral gap (null vs first kept) | 2.9e-14 vs 16.0 |
| 𝒜′ abelian residual (max) | 1.6e-15 |
| dim 𝒜 (L = 6 vs L = 4) | 4224 vs 992 |
| separator complement dimension (L = 6 vs L = 4) | 9 vs 1 |
| sep6 norm; [sep6, D2]; [sep6, J_full]; max[sep6, ρ(h)] | 4.0; 5.2e-14; 1.8e-14; 2.0e-14 |
| blindness overlap² — 9 complement directions (max) | 8.2e-31 |
| blindness overlap² — sep6 + 6 quartet differences (max) | 5.9e-32 |
| wrong-value control — augmented overlap²(·, sep6) | 1.0 |

All isotypic tables, Wedderburn blocks, and idempotent ranks are reported at two independent
seeds with identical outcomes. The order of H, the starting shell dimensions, and the L = 4
comparison values are rebuilt from scratch as construction and self-calibration checks.

## 4. What this does not show — claim boundary

This is a numerical operator-algebra verification on two fixed finite surfaces (L = 6 and
L = 4). The dimensions, isotypic tables, idempotent ranks, and residuals are resolved to the
stated tolerances, not established as exact symbolic theorems. The statements are about
finite-dimensional \*-algebras generated by explicit matrices; the numerical blindness of
𝒜_nat to the separator space is a finite operator-algebra non-membership statement and does
not imply that any physical split is unread, unrecorded, or impossible, nor does it select a
measurement or readout context.

No new free parameter, dynamics, bulk sign-family member, external numerical value, or
literature input is introduced. The result is r-neutral and orientation-neutral. No physical
CP, chirality, measurement, readout, conservation, superselection, or Record identification is
asserted.

The reach / ω census that quantified the L = 4 separator across single-element extensions of
𝒜_nat is **not** computed here. Whether the four reach labels {0, 1/9, 1/3, 1} and the
extension histogram persist, refine, or reorganize once the separator space is nine-dimensional
is exactly the next path this opens. Re-deriving that census on the
enlarged separator space, and classifying the multiplicity-2 constituents that first appear
at L = 6, are the paths this note opens. Separately, gates B8 and E4b exhibit a dressed
four-fold rotation commuting with D2 outside H on both surfaces: characterizing the full
signed-permutation symmetry group of D2, and how the module structure and the separator
space refine under it, is a further path this note opens.

All three direct dependencies are unaudited; this note asserts no audit
grade or publication-usable status and requires an independent audit.

## 5. Dependencies

- [the bicommutant-dimension note](KCPT_DIRAC_SYMMETRY_ALGEBRA_BICOMMUTANT_DIMENSION_992_BOUNDED_THEOREM_NOTE_2026-07-24.md) — supplies the L = 4 algebra 𝒜, its dimension 992, its center C⁵, and the ind12 separator that this note ports to L = 6.
- [the Schur-forced fused-block superstructure note](KCPT_DIRAC_CHISGN_COVARIANCE_SCHUR_FORCED_FUSED_BLOCK_SUPERSTRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-24.md) — supplies the Dirac sign character χ_sgn, the ambient group construction, and the constituent-projector method reused at L = 6.
- [the ind12 separator reach census note](KCPT_IND12_SEPARATOR_REACH_QUANTIZED_CENSUS_MINIMAL_UNLOCK_BOUNDED_THEOREM_NOTE_2026-07-25.md) — supplies the L = 4 one-dimensional separator complement and the reach census whose L = 6 analogue this note leaves open.

Earlier notes enter transitively through these three direct dependencies. No non-KCPT document
is a load-bearing dependency.
