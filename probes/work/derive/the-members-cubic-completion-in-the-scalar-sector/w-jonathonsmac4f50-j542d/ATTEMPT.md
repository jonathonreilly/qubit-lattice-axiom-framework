# The member's first-order cubic completion: the scalar sector does not select the comparator

Task `J:derive:the-members-cubic-completion-in-the-scalar-sector:a2` · worker `w-jonathonsmac4f50-j542d` · model
`claude-opus-5-5` · origin/main `78db61c32a` · checker `check.py` (exact over Q; about 15 min).

**Provenance.** The pre-registration is the supervisor's (Claude, this machine's campaign). Block 112's T1, which this
task uses as its setting, came from this machine's earlier probe #8711. This attempt is by the same model family, so
it is not independent of the supervisor. A referee from another family is needed.

## 1. Exact statement attempted

**Setting.** The member at α = K/4, β = −α, with the bond shift, in the landed long-wave form (block 144 T1; blocks
62, 101, 124 and 136 as landed). Take K = w̄ = 1 and write the lapse as n:

    S2 = ∫ ¼[tr(Ḣ²) − (tr Ḣ)²] + n R₁ + R₂,   Ḣ = ḣ − ∂N − ∂Nᵀ,
    R₁ = ∂ᵢ∂ⱼhᵢⱼ − ∇²tr h,
    R₂ = −¼(∂ₖhᵢⱼ)² + ½(∂ᵢhᵢₖ)(∂ⱼhⱼₖ) − ½(∂ᵢhᵢⱼ)∂ⱼtr h + ¼(∂ₖtr h)².

Its linear gauge symmetries are:
- spatial relabellings: δh = ∂ξ + ∂ξᵀ, δN = ξ̇;
- relabellings in time: δn = ξ̇⁰ (this is δu = (4α/K)ξ̇⁰ at α = K/4), δN = −∇ξ⁰.

**Scalar sector** (the task's restriction):
- the fields are n, N = ∇B and h = 2ψδ + 2∂∂E;
- the parameters are ξ⁰ = ζ and ξ = ∇χ.

**Problem.** Find all local cubic vertices V3 and local first-order deformations δ1 with

    δ0V3 + δ1S2 = 0.

- V3 has two derivatives, is T-even, has at most one time derivative per field, and is rotation-invariant (B, C)
  or cubic-symmetric (D, E).
- The identity holds for all field configurations of the sector.

Count the solutions modulo local field redefinitions and δ0-exact δ1. Compare with the comparator's cubic vertex, the
third-order part of N√γ(KᵢⱼKⁱʲ − K² + R).

**Why this is the leading order of the lattice problem.** Every difference of the member has symbol p_j → k_j at long
wavelength. So the leading symbols of any exact lattice solution (V3, δ1) with two derivatives at leading order solve
this problem. Exact lattice triviality reduces to triviality here. A cubic-symmetric lattice vertex has a leading
symbol built from hyperoctahedral-invariant tensors, which are products of δ-blocks of even size.

## 2. Steps

1. **PROVED (grading).** The identity is homogeneous in the number of derivatives: δ0 adds one, and S2 has two.
   - Only the one-derivative part of δ1 meets a two-derivative V3. Its other parts must satisfy E·δ1 = 0 by
     themselves and are invisible.
   - A redefinition φ → φ + F(φ,φ) changes V3 by E(φ)·F. On two-derivative vertices only zero-derivative F
     contribute, and they come with the solution δ1 = 2F(δ0φ, φ).
   - Redefinitions of the gauge parameters add δ0-exact terms to δ1 and leave V3 unchanged.
   - Hence: classes = (consistent V3) / span{E·F}. check.py verifies that span{E·F} lies in the consistent space.
2. **CHECKED A1–A3.**
   - S2 is invariant under both relabellings for every field component.
   - The comparator's quadratic part equals S2 on all ten components (block 144 T1 re-derived independently).
3. **CHECKED B, scalar sector, rotation-invariant.**
   - 1122 vertex monomials reduce to 67 independent symbols.
   - The consistent space is 21-dimensional, and redefinitions span 17 of it.
   - **So there are 4 classes.** The comparator's vertex is consistent and nontrivial. No class is strictly gauge
     invariant: each needs δ1 ≠ 0.
4. **CHECKED B6–B8, explicit classes that are not the comparator's.**
   - `V_n = n |∂ᵢhᵢⱼ − ∂ⱼ tr h|²`. On scalar configurations ∂ᵢhᵢⱼ − ∂ⱼtr h = −4∂ⱼψ, so V_n = 16 n(∇ψ)². That vector is
     invariant under longitudinal relabellings only.
   - The static lengths-only cubic, with the second derivatives acting on the third factor:

         V_h = 3 hᵢᵢ hⱼⱼ ∂ₗ∂ₗhₖₖ − 4 hᵢᵢ hⱼⱼ ∂ₖ∂ₗhₖₗ − 10 hᵢᵢ hⱼₖ ∂ₗ∂ₗhⱼₖ + 12 hᵢᵢ hⱼₖ ∂ₖ∂ₗhⱼₗ
             − 3 hᵢⱼ hᵢⱼ ∂ₗ∂ₗhₖₖ + 4 hᵢⱼ hᵢⱼ ∂ₖ∂ₗhₖₗ + 12 hᵢⱼ hᵢₖ ∂ₗ∂ₗhⱼₖ − 14 hᵢⱼ hᵢₖ ∂ₖ∂ₗhⱼₗ

   - Both are consistent and nontrivial. The comparator, V_n and V_h are independent classes.
   - A fourth class needs the shift or time derivatives. It has a 25-monomial representative (lapse², lapse ×
     kinetic and shift terms).
   - Sector counts: vertices without the shift carry 2 classes; without the lapse, 1; lengths only, 1; static, 2.
5. **CHECKED C and C5, full configurations, rotation-invariant.**
   - 87 independent symbols; consistent space 18; redefinitions 17.
   - **Exactly 1 class, the comparator's.** This reproduces the known uniqueness of the Einstein cubic vertex, which
     is named here as a comparator and not used.
   - V_n and V_h are not consistent there.
6. **CHECKED D and D5, scalar sector, cubic-symmetric, general momenta.**
   - 3186 monomials reduce to 130 independent symbols; consistent space 30; redefinitions 26.
   - **Still 4 classes.** The rotation-invariant classes span them, so anisotropic leading symbols add none.
7. **CHECKED E, full configurations, cubic-symmetric, general momenta.**
   - 183 independent symbols; consistent space 27; redefinitions 26.
   - **Exactly 1 class, the comparator's.**
8. **PROVED from 3–7, comparison with the pre-registration.**
   - In the scalar sector the comparator's own continuum theory sits in a 4-dimensional solution space. The rule
     "dimension two or more … is a departure" would therefore classify the comparator itself as a departure. The
     rule "a one-dimensional continuum part equal to the comparator's" cannot occur in this restriction.
   - The restriction is not selective: the three extra classes exist because only longitudinal relabellings remain,
     so ∂ᵢhᵢⱼ − ∂ⱼtr h becomes invariant. The transverse relabellings are what select the comparator.
   - In the unrestricted problem the leading-order answer is exactly the comparator, with or without cubic
     anisotropy. There the pre-registered test is meaningful.

## 3. First step that is not done

**The exact lattice lift.** It is not computed whether the comparator's class, unique in the full sector at leading
order (E), lifts to an exact range-1 or range-2 lattice solution. The alternative would be an obstruction at a stated
order in the spacing. The tie to the walker's coupling is also not addressed.

## 4. What would finish it

1. Re-pose A1 in the full sector, or at least scalar plus vector. At leading order the answer there is one class, the
   comparator's (E), so the pre-registered decision rule becomes meaningful.
2. Enumerate lattice vertices and deformations with placements (sites, bonds, faces) at range 1 and then 2. Solve the
   exact Laurent identity in z_a^{1/2} with leading symbol in the comparator's class. Record the first order in the
   spacing at which no local δ1 exists, or give the exact solution. The machinery here (grading, quotient,
   comparator) carries over. Only the symbol ring changes, from polynomials in k to Laurent polynomials in z.

## ASSUMED

- The member, its shift, the two relabellings and the scalar-sector restriction, as supplied by the landed blocks.
  They are not framework premises.
- The locality class: polynomial symbols, T-even, reflection-even (δ tensors only), two-derivative vertices.
- The comparator: used for comparison only.
