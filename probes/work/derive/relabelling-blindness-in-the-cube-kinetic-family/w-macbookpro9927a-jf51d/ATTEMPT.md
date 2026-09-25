# Which kinetic terms with only the cube's symmetry are blind to relabellings in time?

Unit `J:derive:relabelling-blindness-in-the-cube-kinetic-family:a2` (independent attempt 2 of 2), worker `w-macbookpro9927a-jf51d` (Claude Opus 5.5), 2026-09-25. No prior attempts were printed at claim time.

**Provenance.**
- Part (a) was derived here, from block 62 as landed, before block 124's runner or its T5 proof text was read. It agrees with block 124 T5 (PR #9178, open) step by step.
- T5 is the supervisor's own addition, by the same model family as this worker and not refereed by another family. This attempt is therefore not cross-family evidence for T5.
- Parts (b) and (c) go beyond block 124.
- This worker has no prior attempt on block 124's problems. `the-kinetic-term-under-the-two-blindness-demands` (#8734) belongs to another worker.

## 1. Setting (block 62 as landed; block 124's demands)
- **Fields at one lattice wave vector.** The metric strain is h = −(ε + εᵀ) around the frame E = 1 + ε. Here E[j, a] carries the bond index j and the coin index a, the coin index being soldered to the bond directions (block 54). The other fields are the rotation part ω = antisym(ε), 3 components, and the rates' multiplier u. The symbols are p_j = 2 sin(k_j/2), all real.
- **The member (block 62).**
  - R₁ = p² tr h − p·h·p.
  - R₂ = −(p²/4) tr h² + |hp|²/2 − (p·h·p) tr h/2 + (p²/4)(tr h)².
  - The Lagrangian is L = T + K(uR₁ + R₂), with w̄ = 1 and potential −F₂ = K(uR₁ + R₂).
- **Cube kinetic family (block 62).** T = M₁Σ_j ḣ_jj² + M₂Σ_{i<j} ḣ_iiḣ_jj + M₃Σ_{i<j} ḣ_ij². The rotation-invariant members α ḣ_ijḣ_ij + β(tr ḣ)² are M₁ = α + β, M₂ = 2β, M₃ = 2α.
- **Relabellings.** ξ acts on the frame by pullback, δε = −ξpᵀ (row j, column a). So δh = pξᵀ + ξpᵀ, which is block 62 T3's, and δω = (pξᵀ − ξpᵀ)/2.
  - *Gradient:* ξ ∥ p. Block 124 writes it as h → h + ppᵀζ(t).
  - *Transverse:* p·ξ = 0, e.g. ξ = (p × b)ζ(t).
- **Coin rotations in time** (block 124 T1): ω → ω + Ω(t), with Ω antisymmetric and arbitrary at each tick.
- **Symmetry.** A transformation is a symmetry when the change of L is a total time derivative for every history of every field.

## 2. Statement
**(a) Relabellings in h′.**
- *Gradient.* The relabelling in time is a symmetry, with a multiplier shift u → u + Σ_{n≤3} c_nζ^{(n)}, iff (M₁, M₂, M₃) = (0, c, −c) and the shift is exactly u → u + (c/K)ζ″. That is the rotation-invariant member at β = −α, with α = −c/2.
- *Transverse.* It is a symmetry iff (M₁, M₂, M₃) = (M, 2M, 0), with no shift: the pure trace term.
- *Both.* Only for the zero term. This agrees with block 124 T5(a)–(c).

**(b) The frame's full rate.**
- At first order the rate V = ĖE⁻¹/w is ε̇. It is a tensor with two bond indices, on which the cube group acts as V → RVRᵀ.
- The cube-invariant quadratic forms in V have exactly four numbers: Σ V_jj², Σ_{i<j} V_iiV_jj, Σ sym(V)_ij² and Σ antisym(V)_ij². Call the last one's coefficient N.
- *Rotation blindness alone* forces N = 0 and leaves three numbers, block 62's cube family. So T1's "exactly two" needs its metric premise.
- *The gradient demand alone* forces (M₁, M₂, M₃) = (0, c, −c) and leaves N free.
- *The transverse demand* forces (M, 2M, 0) together with N = 0.
- *Rotation blindness with the gradient demand* leaves exactly block 62's member at β = −α.

**(c) Modes of the survivor (0, c, −c)**, with c = −2α < 0.
- There is exactly one travelling pair. It is transverse traceless, with u = 0 and no rotation, and X = Ω² = Kp²/(4α), where p² = Σ 4 sin²(k_j/2).
- Every other direction is one of:
  - the gradient gauge direction (ppᵀ, u = 2αX/K), null at every X;
  - one of the two transverse relabellings, which drift (X = 0);
  - one of the three rotations, which drift if N ≠ 0 and are pure gauge if N = 0.

## 3. Steps
1. **The total-derivative criterion. PROVED.**
   - *Only if:* the Euler operator Σ_n (−d/dt)^n ∂/∂f^{(n)} annihilates every total derivative dΛ/dt. So a nonzero Euler derivative in any field rules out a symmetry.
   - *If:* an explicit Λ is exhibited: for the gradient survivor, δL = d(cζ′R₁)/dt; for the transverse survivor, δL = 0.
2. **Gradient. PROVED; CHECKED A1.**
   - With δh = ppᵀζ, R₁ and R₂ are unchanged (block 62 T3). So δL = 2B(ḣ, ppᵀ)ζ̇ + T(ppᵀ)ζ̇² + KΣc_nζ^{(n)}R₁(h), where B is T's bilinear form.
   - Integrate by parts: Kc_nζ^{(n)}R₁ ≡ (−1)^{n−1}Kc_nζ̇R₁^{(n−1)} modulo total derivatives. Only n = 2 produces ζ̇ times a first derivative of h, so matching forces c₀ = c₁ = c₃ = 0 and 2B(ḣ, ppᵀ) = Kc₂Ṙ₁(ḣ) for all ḣ and p.
   - Comparing coefficients: A_jj gives 2M₁p_j² + M₂Σ_{l≠j}p_l² = Kc₂Σ_{l≠j}p_l², and A_ij gives 2M₃p_ip_j = −2Kc₂p_ip_j. So M₁ = 0, M₂ = −M₃ = Kc₂ = c.
   - Then T(ppᵀ) = 0 identically.
   - A1 solves every Euler-derivative coefficient in symbolic p, with c₀ … c₃ free. It finds exactly this and verifies the Λ.
3. **Transverse. PROVED; CHECKED A2.**
   - R₁ and R₂ are unchanged, so no multiplier term can absorb the change.
   - The ζ̇ḣ coefficient must vanish identically. Its A_ij parts, M₃(p_iξ_j + p_jξ_i), vanish for generic ξ ⊥ p only if M₃ = 0.
   - Its A_jj parts, (2M₁ − M₂)p_jξ_j after using p·ξ = 0, force M₂ = 2M₁.
   - The rotation part changes by δω ≠ 0, which forces N = 0.
   - The survivor M(tr ḣ)² is exactly unchanged, since tr δh = 2p·ξ = 0.
4. **Both demands. CHECKED A3.** Solving the union of the conditions gives only zero.
5. **The four cube numbers. PROVED; CHECKED B1.**
   - Under the proper cube group O, R³⊗R³ = A₁ ⊕ E ⊕ T₁ ⊕ T₂. These are the trace, the traceless diagonal, the antisymmetric part and the symmetric off-diagonal part, each occurring once.
   - T₁ and T₂ are inequivalent: the quarter turn has character +1 on T₁ and −1 on T₂. So there are no cross terms.
   - The invariant symmetric bilinear forms therefore number 1 + 1 + 1 + 1 = 4. Inversion acts trivially on the tensor.
   - B1 solves Q(RVRᵀ) = Q(V) for the quarter turn, the third turn about (1,1,1) and inversion, over all 45 entries of Q: exactly 4 free numbers, matching the stated basis.
6. **Rotation blindness and the relabellings' rotation parts. PROVED; CHECKED B2, B3.**
   - Q(V + Ω) − Q(V) = 2N⟨A, Ω⟩ + N|Ω|², which vanishes for all Ω iff N = 0.
   - A gradient relabelling has δε = −ζppᵀ, which is symmetric, so δω = 0 and N is free.
   - A transverse relabelling has δω ≠ 0 (step 3).
7. **Modes. PROVED; CHECKED C1, C2.**
   - Decompose h at p ≠ 0 into transverse traceless (2), vector parts pξᵀ + ξpᵀ with ξ ⊥ p (2), the longitudinal part ppᵀ, and the transverse trace t(1 − p̂p̂ᵀ).
   - For α|ḣ|² − α(tr ḣ)²:
     - *TT sector:* L = α|ḣ|² − (Kp²/4)|h|², so X = Kp²/(4α).
     - *Vector sector:* L = α|ḣ|², with R₁ = R₂ = 0, so ḧ = 0: a drift.
     - *Scalar sector:* L = −2α(ṫ² + 2ḣ_Lṫ) + K(2p²ut + (p²/2)t²). The u equation forces t = 0; h_L is then arbitrary, with u = −(2α/K)ḧ_L; there is no mode.
     - *Rotation sector:* L = N|ω̇|², a drift, decoupled.
   - C1 and C2 check this at p = (1,2,2) and p = (2/5, 1/3, −3/7), with K = α = 1:
     - the (h, u) pencil XA + C has normal rank 6;
     - the gcd of its 6×6 minors is 16X²(4X − 9)² at the first p, and the roots are p²/4 twice and 0 at the second;
     - the rotation block decouples, with det (2NX)³;
     - at X = p²/4 the null space is the TT pair plus the gauge vector.

## 4. ASSUMED
None beyond standard linear algebra. The representation count in step 5 is also verified by direct computation in B1.

## 5. What would finish it / open
- Orders beyond the second in the strains.
- A field that couples to the transverse relabellings, which remain drifting directions for every survivor (block 124's open item).
- Nothing here fixes α/K, the member's existence, or K.
- The cube members that fail the gradient demand keep block 62 T4(c)'s direction-dependent dispersion. They are not classified here.
