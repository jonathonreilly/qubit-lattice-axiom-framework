# The member's velocity-dependent pull: an independent check of block 144

Unit `J:derive:the-members-velocity-dependent-pull:a1`, worker `w-macbookpro9927a-j4748` (Claude Opus 5.5), 2026-09-25.

**Provenance.**
- Block 144 was landed on main on 2026-09-25 (`docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS_..._2026-09-25.md`). It is the supervisor's derivation, same model family (Claude), and is not refereed by another family.
- Attempt a2 (`w-jonathonsmac4f50-j24ce`, also Claude Opus 5.5) checked T2 along one axis, T3 by the exchange, T4 with the virial step, and a boost generator.
- **This attempt takes other routes:**
  - T1 for arbitrary fields, which neither block 144's runner (plane waves) nor a2 did;
  - T2 at non-axis wave vectors;
  - T4 from a Legendre transform derived here, evaluated on explicit bound states without the virial step;
  - T5(b)–(d).
- **Related work by this worker (disclosed):** #9214 (the member and a spin-polarised walker, on blocks 136/138), #9225 and #9226 (relabellings in time and the shift field). A referee of another model family should check this attempt.

## 1. Setting (block 144 as landed; blocks 62, 101 and 136)
- **The Lagrangian.** L = α[tr(Ḣ²) − (tr Ḣ)²] + K(uR₁ + R₂) − eu + N·P + ½Σ Θ_ij h_ij.
  - Ḣ = ∂_t h − ∂N − (∂N)ᵀ, with β = −α and w̄ = 1, at long wavelength.
  - R₁ = ∂_i∂_j h_ij − ∇² tr h.
  - R₂ = −¼(∂_k h_ij)² + ½(∂_i h_ik)² − ½(∂_i h_ij)∂_j tr h + ¼(∂_k tr h)².
- **Sources that keep the books:** ∂_t e = −∇·P and ∂_t P_j = −∂_iΘ_ij.
- **The pull** L_int = (k/r)[1 + a(v₁² + v₂²) + b v₁·v₂ + c(n·v₁)(n·v₂)] between bodies with free Lagrangian −m_a(1 − v_a²)^{1/2}.
- **The weight** is W(P̂) = E₀ ∂²E/∂P² at rest.

## 2. Statement attempted
An independent confirmation, or refutation, of block 144:
- **T1:** the member equals K times the comparator's second-order lapse-and-shift action iff α = K/4 and β = −α.
- **T2:** the exchange between book-keeping sources is (1/(2K))[T′·T − ½T′T]/(p² − ω²), with or without the shift, and there is no moving solution at α ≠ K/4.
- **T4:** W = 1 + [(1 + 2(2a + b))⟨U⟩ + (1 + 2c)⟨U_P̂⟩]/M. W = 1 for the member's (3/2, −7/2, −½), and W = 1 on every state forces 2a + b = −½ and c = −½.
- **T5(b)–(d):** the drifting lengths without the shift.

T3, the reduction of T2 to the order-v² Lagrangian, is not re-derived here. It rests on block 144's own derivation and on a2's check.

## 3. Steps
1. **T1 for every field. PROVED; CHECKED T1.**
   - **Scalar curvature.** With γ = 1 + εh(x), the scalar-curvature density √γR has first-order part R₁ exactly.
   - **Second order.** The second-order part minus R₂ is a quadratic form, with constant coefficients, in the first and second derivatives of h. Its Euler–Lagrange derivatives with respect to all six h_ij vanish identically (sympy, for arbitrary functions h_ij(x, y, z)).
   - **Why that means a divergence.** For a constant-coefficient quadratic form Q in derivatives of h, zero Euler derivatives means that the hermitian part of its Fourier symbol vanishes. Integrating by parts then turns Q into a total divergence. The argument is elementary: move the derivatives of each monomial onto one factor, with a divergence as remainder.
   - **Kinetic part.** The first-order extrinsic curvature is Ḣ/2, which gives ¼[tr(Ḣ²) − (tr Ḣ)²]. Matching α tr(Ḣ²) + β(tr Ḣ)² to K times this forces α = K/4 and β = −K/4.
   - **Lapse term.** (1 + u)√γR contributes uR₁ at second order.
   - This covers every field, not only plane waves along one axis.

2. **T2 at generic wave vectors. CHECKED T2.**
   - **Setup.** The Euler–Lagrange equations of L for all ten fields (sympy) are evaluated on plane waves at p = (1,2,2), ω = 7/3 and at p = (2/5, 1/3, −3/7), ω = 5/11. Neither p lies along an axis.
   - **Sources.** They keep the books, built from random rational symmetric Θ with P_j = p_iΘ_ij/ω and e = p·P/ω.
   - **With and without the shift:**
     - at α = K/4 the system is solvable;
     - the pairing −e′u + N·P′ + ½Θ′·h is free of the relabelling parameters and equals (1/(2K))[T′·T − ½T′T]/(p² − ω²), with η = diag(−1, 1, 1, 1);
     - at α = K/3 there is no solution.

3. **T4 on explicit bound states. PROVED; CHECKED T4 and T4c.**
   - **(a) The Legendre transform, derived here.** Scale v ~ λ and k ~ λ². Inverting p = ∂L/∂v to O(λ³) and forming H = p·v − L to O(λ⁴) gives H = Σ[m + p²/2m − p⁴/8m³] − (k/r)[1 + a(p₁²/m₁² + p₂²/m₂²) + b p₁·p₂/(m₁m₂) + c(n·p₁)(n·p₂)/(m₁m₂)] exactly at that order.
   - **(b) The centre of mass.** Put p₁ = (m₁/M)P ê + q and p₂ = (m₂/M)P ê − q. The coefficient C of P² is a polynomial of degree 2 in q, plus k/r and k n_in_j/r terms (sympy).
   - **(c) First-order perturbation.** For a parity eigenstate ψ of H₀ = q²/(2μ) − k/r, the terms odd in P have zero first-order average. Their second-order contribution lies beyond first order in the binding, by power counting (v⁴, kv²). So E(P) = E₀ + P²(1/(2M) + ⟨C − 1/(2M)⟩), and W − 1 = [⟨q²/(2μ) − k/r⟩ + 2M²⟨C − 1/(2M)⟩]/M at first order.
   - **(d) The states.** The hydrogenic states 1s, 2p₀ and 2p_x, with Bohr radius 1/(μk), are evaluated by exact integration of ⟨∂_iψ ∂_jψ⟩, ⟨n_in_j/r⟩ and ⟨1/r⟩, along ê = x and ê = z.
   - **Results.**
     - W = 1 exactly for (3/2, −7/2, −½) on every state and direction.
     - For the clock alone, W − 1 = (⟨U⟩ + ⟨U_P̂⟩)/M, with ratios to ⟨U⟩/M of 4/3 (1s), 8/5 (2p₀ along its axis) and 6/5 (across it).
     - The directional virial 2⟨T_P̂⟩ = −⟨U_P̂⟩ holds state by state, as a computed fact rather than an assumed step.
   - **(e) Necessity.** Requiring W = 1 on 1s along z and on 2p₀ along and across its axis gives exactly 2a + b = −½ and c = −½ (T4c). These three state-and-direction pairs have different ⟨U_P̂⟩/⟨U⟩.

4. **T5(b)–(d) without the shift. CHECKED T5.**
   - At α = K/4, h = t(∂ξ + ∂ξᵀ) with u = 0 solves the source-free Euler–Lagrange equations for every ξ(x).
   - Its momentum-constraint residual, 4α∂_i(ḣ_ij − δ_ij tr ḣ), equals K(∇²ξ − ∇∇·ξ). It vanishes only for longitudinal ξ.
   - ½Θ·h = d(tξ·P)/dt − ξ·P + ∂_i(tΘ_ijξ_j), using the books.

## 4. ASSUMED
- First-order perturbation theory for a bound state's energy, and the power counting of the odd-in-P terms. Block 144 and a2 use the same counting.
- Standard linear algebra and calculus.

## 5. What would finish it
- An independent route for T3, for example the boosted static field of a uniformly moving body, reduced modulo total derivatives.
- Nonlinear (order k²) terms.
- The lattice (finite-p) exchange away from long wavelength.
