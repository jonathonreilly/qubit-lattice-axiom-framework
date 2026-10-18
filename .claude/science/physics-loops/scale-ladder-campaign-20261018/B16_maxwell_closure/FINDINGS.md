# B16 findings: lattice U(1) Maxwell field in the curvature-member constraint algebra

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back, because the worker's .md write was blocked. Runners:
- `b16_lattice_closure.py`: exact rational arithmetic, importing B14's lattice code. PASS=19 FAIL=0 on 3³ and 4³.
- `b16_continuum_leading_order.py`: exact sympy. PASS=12 FAIL=0.

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

1. **Timing must be one-sided (T2, symbolic lapses).**
   - Exactly 8 smearing classes close: each axis timed at its tail or its head, and each plaquette at the matching corner.
   - The reflection-symmetric timing fails, leaving 162 non-bond lapse pairs.
   - Gauss cannot rescue any timing (T2d).
   - The compact theory gives the same algebra with F → sin F (T7).
   - The scalar (B14) closes with symmetric timing; Maxwell does not, because both E and B live on extended cells.
2. **Same cone as the scalar.**
   - {H_EM(N), H_EM(M)} = G_A[−c_B ξ̃] exactly, and g cancels.
   - Closure with gravity holds iff c_B = −sK/(4α) = K/(4α).
   - Scalar + Maxwell + gravity closes iff c_φ = c_B.
   - **This is conditional on the generator normalisation:** doubling G_A moves closure to c_B = 2κ (T3c). The unit-translation normalisation is supplied, exactly as for G_m (B14) and G_f (B15).
3. **Universal stress coupling (continuum, leading order).**
   - Closure gives the Maxwell metric stress plus λ·tr h·H_EM.
   - With the scalar-lapse rule the coupling is unique, and the structure function is g^ij = δ − h.
   - The two species share one λ.
4. **Gauss enters as a first-class constraint with field-dependent multipliers.**
   - With the gauge-covariant generator, {P_A, C} and {P_A, P_A} pick up Gauss terms.
   - With the pure Lie-derivative generator, {C, C} needs Gauss[ξ₀·A], which is exact on the lattice (T5b, T5c).
5. **Lattice {G, C} obstruction (T6), coupling-independent.**
   - Under a uniform shift, G_g ≡ 0, and {G_A[e₀], H_EM(1)} = (g²/2)Σ(ΔE)² − (c_B/2g²)Σ(ΔF)² + g²Σ E·Gauss.
   - This is O(a) by analytic counting, one order worse than the scalar's O(a²). No float scaling study was run.
   - The B14 scalar obstruction also appears at uniform shift (T6d). So B14's E5 does not depend on its coupling ansatz.

## Derived vs supplied

- **Derived:**
  - the one-sided timing;
  - the gauge generator form, up to normalisation;
  - the cone c_γ² = K/(4α), independent of g and equal to the scalar's;
  - the universal stress with one shared λ;
  - the structure function;
  - where Gauss enters;
  - the exact O(a) obstruction.
- **Supplied:**
  - the H_EM form and field placement;
  - endpoint/corner smearing support;
  - the unit-translation normalisation of G_A;
  - δ_ξh = 2∂ξ, the scalar-lapse rule, the ansatz, and c_B > 0.
- **Not fixed:** g and Newton's constant.

## Caveats

- Linearised at flat strain, order-ε brackets only.
- Wider timing stencils are not classified.
- The one-sided ("upwind") timing breaks lattice reflection symmetry. Whether that is acceptable is open.

## Prior art

- Teitelboim 1973; Hojman–Kuchař–Teitelboim 1976; Isham–Kuchař 1985 (gauge fields and the Gauss constraint in the deformation algebra); Kuchař 1974–76; Deser 1970.
- Lattice breaking of the algebra: Renteln–Smolin, Gambini–Pullin, Bahr–Dittrich.
- New and narrow: the one-sided timing classification, the symmetric-timing impossibility mod Gauss, and the exact uniform-shift defect identity.
