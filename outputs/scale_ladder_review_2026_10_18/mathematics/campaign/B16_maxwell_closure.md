> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B16 findings: lattice U(1) Maxwell field in the curvature-member constraint algebra



During development, wrong expected values in four tests were fixed: T3b sign, M0 printed factor, M2b hypothesis, M6 r₂ sign. The M2b hypothesis (no Gauss term in {P_A, C}) was refuted by the computation.

## Setup (supplied)

- **Fields.** A and E on links, F on plaquettes. Noncompact in the main runs; the compact case is T7.
- **Hamiltonian.** H_EM(N) = Σ_l N_l (g²/2)E² + Σ_p N_p (c_B/2g²)F².
- **Timing.** Link: u_tail N_x + u_head N_{x+j}. Plaquette: a weighted sum over its corners.
- **Gauss constraint.** Gauss_x = div E, taken as first class.
- **Gauge relabelling generator.** G_A[ξ] = Σ ξ E F, normalised by a unit lattice translation (T3b).
- **Gravity.** As in B14.
- **Continuum ansatz.** 126 coefficients: a general quadratic in (E, F) for each strain component.

## Results

1. **Translation-invariant endpoint/corner timing classification (T2, symbolic lapses).**
   - Exactly 8 smearing classes close: each axis timed at its tail or its head, and each plaquette at the matching corner.
   - The reflection-symmetric translation-invariant timing fails, leaving 162 non-bond lapse pairs (384 at L=4 in the check). No generator Σ ξ_b O_b paired with gravity's bond ξ rescues it.
   - **Exact local rule (check).** {H, H} is bond-supported iff each plaquette weights only corners whose opposite corner its links' timings do not cover.
   - **Scope correction (check).** Reflection-symmetric closing timings exist only if unit translations are broken. The staggered example (links at their even endpoints, plaquettes at their odd corners) closes with the same cone. But its generator carries an O(1) doubler component, and it appears to fail {G, C} at O(1) (one configuration).
   - Gauss cannot rescue any timing (T2d).
   - The compact theory gives the same algebra with F → sin F (T7).
   - The scalar (B14) closes with symmetric timing; Maxwell does not, because both E and B live on extended cells.
2. **Same cone as the scalar.**
   - {H_EM(N), H_EM(M)} = G_A[−c_B ξ̃] exactly, and g cancels.
   - Closure with gravity holds iff c_B = −sK/(4α) = K/(4α).
   - Scalar + Maxwell + gravity closes iff c_φ = c_B.
   - **Generator normalisation.** Doubling G_A moves closure to c_B = 2κ (T3c). The subsequent B19 calculation qualifies this: matter normalizations coincide under the common lapse rule, but the linear gravity shift normalization is not fixed by {G,G} alone. G_A is the generator the bracket induces, and it acts as the unit L_ξ on smooth fields (C2h). Sector generators λ_s L_ξ close on themselves only if all λ_s are equal. So given {G, G} closure and δ_ξh = L_ξg, the cone is derived. The same applies to G_m and G_f. Open: the lattice {G, G}, since the argument is nonlinear-order.
3. **Universal stress coupling (continuum, leading order).**
   - Closure gives the Maxwell metric stress plus λ·tr h·H_EM.
   - With the scalar-lapse rule the coupling is unique, and the structure function is g^ij = δ − h.
   - The two species share one λ. M3–M6 have not been independently checked.
4. **Gauss enters as a first-class constraint with field-dependent multipliers.**
   - With the gauge-covariant generator, {P_A, C} and {P_A, P_A} pick up Gauss terms.
   - With the pure Lie-derivative generator, {C, C} needs Gauss[ξ₀·A] (T5c). On the lattice T5b is true by definition.
5. **Lattice {G, C} obstruction (T6), coupling-independent.**
   - Under a uniform shift, G_g ≡ 0, and {G_A[e₀], H_EM(1)} = (g²/2)Σ(ΔE)² − (c_B/2g²)Σ(ΔF)² + g²Σ E·Gauss.
   - It is O(a), measured by the check: D/H(∂N) ~ L^-1.03. The scalar gives D = 0 and R ~ L^-2.06, so O(a²).
   - **Cause (check):** the one-sided timing forces a non-antisymmetric G_A, δA = (1 − T⁻¹)A. The scalar's central G_m is antisymmetric. So the O(a) comes from the timing, not from Maxwell as such.
   - The B14 scalar obstruction also appears at uniform shift (T6d). So B14's E5 does not depend on its coupling ansatz.

## Derived vs supplied

- **Derived:**
  - the eight translation-invariant timing classes within the specified endpoint/corner support;
  - the gauge generator form, up to normalisation;
  - the cone c_γ² = K/(4α), independent of g and equal to the scalar's;
  - the universal stress with one shared λ;
  - the structure function;
  - where Gauss enters;
  - the exact O(a) obstruction.
- **Supplied:**
  - the H_EM form and field placement;
  - endpoint/corner smearing support;
  - {G, G} closure, which fixes the normalisation of G_A;
  - δ_ξh = 2∂ξ, the scalar-lapse rule, the ansatz, and c_B > 0.
- **Not fixed:** g and Newton's constant.

## Caveats

- Linearised at flat strain, order-ε brackets only.
- Wider timing stencils are not classified.
- The one-sided ("upwind") timing breaks lattice reflection symmetry. Whether that is acceptable is open.

## Prior art

- Schwinger's energy-density commutator condition (1962–63); Loll 1997 (gr-qc/9708025); arXiv:2305.10097. Cubical cell ownership is the forward timing, so it is common.
- Teitelboim 1973; Hojman–Kuchař–Teitelboim 1976; Isham–Kuchař 1985 (gauge fields and the Gauss constraint in the deformation algebra); Kuchař 1974–76; Deser 1970.
- Lattice breaking of the algebra: Renteln–Smolin, Gambini–Pullin, Bahr–Dittrich.
- New and narrow: the one-sided timing classification, the symmetric-timing impossibility mod Gauss, and the exact uniform-shift defect identity.
