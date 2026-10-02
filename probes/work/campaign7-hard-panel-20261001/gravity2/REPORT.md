**Gravity round 2: a corrected route for the sea-induced graviton (derivation only)**

Nothing was run and no files were written. I read main at origin/main. Block 183 is not on main; I read it on its pushed branch `physics-loop/admissibility-induced-law-block183-under-the-two-step-coupling-the-sea-under-shear-20260927`. Blocks 176 and 182 are also pushed, not landed. I also read issue #9198, REPORT.md and REVIEW.md.

**Short answer.** The linear, normal-ordered coupling the review asked for is guaranteed to fail the Ward test, so running it would decide nothing. Ward is restored by a sum rule on the coupling's second-order contact term, not by Decision R. The decisive test is whether a q-independent contact term can satisfy that sum rule; Decision V at quadratic order is one candidate. No route here reaches a linear graviton from finite-qubit composites plus the sea alone.

**Setting.**
- The walk: H_μ = Σσ_aS_a + με(x), with block 139's staggered mass and μ > 0. The two-step momentum is P_j = S_jC_j.
- The relabelling generator is G_ξ = ½Σ{ξ_j, P_j}.
- The coupling is V(B) = Σσ_a½{C_a[B_a^j], P_j}, which is block 69 T3a with dξ replaced by a bond field B.
- The placement is B = Rh, using block 120's B_i^j = −½φ_j h_ij.
- The member's relabelling is h → h + G_mξ, with G_mξ = −(d_iξ_j + d_jξ_i).
- The completed coupling is H(h) = H_μ + V(Rh) + ½S(h,h) + O(h³), where S is the second-order (contact) term.
- The sea energy is E_sea(X) = Tr[Xθ(−X)]; the induced action is W = E_sea(H(h)) − E_sea(H_μ) = W₁ + W₂ + …
- ⟨·⟩ is the sea expectation, and χ(q) is the Fourier form of W₂.

## 1. Is the O(k²) response relabelling-invariant?

**S1 [LANDED, block 69 T3].** i[H₀, G_ξ] = V(dξ), and K is the Noether current of the conserved two-step momentum. So block 69's coupling is exactly the gauged two-step translation.

**S2 [EXACT].** This holds unchanged for μ > 0. T_j^{±2} preserves the sublattice sign, so [ε, P_j] = 0; also [ε, ξ_j] = 0. Hence [με, G_ξ] = 0, i[H_μ, G_ξ] = V(dξ), and [P_j, H_μ] = 0. The massive sea is exactly invariant under uniform two-step translations.

**S3 [LANDED + ARGUED].**
- R·G_mξ = d(½φξ) + τ_ξ, where τ_i^j = ½φ_j d_jξ_i.
- In block 120 T4(a)'s proof, every plane-wave pair of the transposed combination carries the factor |s(k)|² − |s(k′)|². That is the symbol of a commutator with the scalar ΣS_a² = H_μ² − μ² [EXACT: the σ's anticommute and {S_a, ε} = 0].
- Read this way, V(τ_ξ) = [X_ξ, H_μ²] = i[H_μ, Y_ξ] with Y_ξ = i{H_μ, X_ξ} local [ARGUED].
- So V(RG_mξ) = i[H_μ, Z_ξ] with the local generator Z_ξ = G_{½φξ} + Y_ξ. Every member gauge direction is tangent to H_μ's unitary orbit. This is the operator content of block 120's compatibility.

**Theorem W [EXACT, given S3].** For all h and ξ:
- (i) W₁(G_mξ) = 0;
- (ii) 2W₂(h, G_mξ) = ⟨i[Z_ξ, V(Rh)]⟩ + ⟨S(h, G_mξ)⟩;
- (iii) W₂(G_mξ, G_mξ) = ½⟨S(G_mξ, G_mξ)⟩ − Σ_{p,h}(E_p − E_h)|(Z_ξ)_ph|².

*Proof.*
- E_sea is unitarily invariant, so E_sea(H(h)) = E_sea(e^{−iZ}H(h)e^{iZ}).
- Expanding: e^{−iZ}H(h)e^{iZ} = H_μ + V(Rh) + ½S(h,h) + V(RG_mξ) − i[Z, V(Rh)] − ½[Z,[Z,H_μ]] + O(3).
- Compare with H(h + G_mξ), and use E_sea(A + δ) − E_sea(A) = ⟨δ⟩ + O(3) for δ of second order.
- The orders ξ, hξ and ξ² give (i)–(iii), using ⟨[Z,[Z,H]]⟩ = −2Σ(E_p − E_h)|Z_ph|². ∎

**Consequences.**
- **(a) The linear coupling (S = 0) fails Ward [EXACT].** W₂(G_mξ, G_mξ) = −Σ(E_p − E_h)|Z_ph|² ≤ 0, with equality iff V(RG_mξ) has no particle–hole matrix elements.
  - It is strictly negative for walker gauge directions at generic q, because the spinors of σ·s at k and k+q are not parallel.
  - So the linear coupling fails Ward structurally: it is a paramagnetic response with no diamagnetic partner, not a lattice accident. #9198's failure is of this kind.
- **(b) Normal ordering cannot help [EXACT].** Normal ordering subtracts a c-number. It changes W₁, but neither W₂ nor the commutator in (ii). Normal-ordering S deletes ⟨S⟩ and reverts to (a). So the review's "linear, or normal-ordered" re-specification already has its Ward outcome fixed: it fails.
- **(c) Sign corollary [EXACT; the inversion step is ARGUED].**
  - A linear coupling gives χ(q) ≤ 0 at every q.
  - Ward would force χ(0) = 0, because the gauge directions at q → 0 span Sym(3).
  - The combined operation (inversion)∘ε maps H_μ to itself and V(B) to V(Bᴵ), so χ₁ = 0 [ARGUED].
  - Ward would then force χ₂ = cF (the review's uniqueness result), and F is indefinite, so c = 0.
  - So a linear coupling cannot produce an Einstein–Hilbert term. The stiffness has to come from the contact term.
- **(d) What restores Ward [EXACT].** The sea already has the symmetry (S2 and unitary covariance). What is missing is the **sum rule (Σ)**: ⟨S(h, G_mξ)⟩ = −⟨i[Z_ξ, V(Rh)]⟩ for all h, ξ.
  - (Σ) is consistent on gauge × gauge pairs: the Jacobi identity plus ⟨[H_μ, ·]⟩ = 0 make the right side symmetric in (ξ, η).
  - Solutions exist order by order, for example s = −2·Taylor(χ_para) plus any invariant form. Any two solutions differ by a relabelling-invariant form, which at O(k²) is c_s·F: one free constant.
- **(e) The uniform (k⁰) part [EXACT].**
  - Ward forces the whole uniform Hessian to vanish: bulk, E_g and T₂g.
  - It still allows the pressure tadpole W₁ = (κ₀/2)Σ tr h, with κ₀ = ⟨s₁²c₁²/R⟩.
  - Block 183 T6 (pushed) finds that long TT waves tend to ½E₂(q₂) ≠ 0 under block 69's coupling with a site-local completion. That is a concrete failure at this order.
  - Its threshold q₂* is exactly the E_g sum-rule point. Block 182's covariant value q₂ = −1/2 misses it.
- **(f) Tadpole caveat [EXACT].** Giving the member's relabelling a nonlinear part N adds −W₁(N) to (ii). With nonzero pressure, a suitable N can absorb any residual, so that version of the test is empty unless N is fixed on independent grounds. Block 62's member relabels linearly, so the strict form applies.

**Answer to 1.**
- There is a structural Ward identity (Theorem W), and the two-step current is the Noether current of an exact lattice relabelling.
- The linear or normal-ordered coupling violates it by the exactly computable amount ½⟨i[Z, V]⟩.
- Restoring it needs the sum rule (Σ), not a further symmetry of the sea.

## 2. Minimal supplied ingredient

- **Decision R does not enforce Ward [EXACT].**
  - A functional passes to the quotient iff it is already invariant.
  - For a quadratic form, invariance under a spanning discrete set of shifts already implies continuous invariance (W₂(h + Gv) = W₂(h) for all h forces W₂(·, Gv) = 0).
  - So R is a consistency demand, and the linear coupling's W already violates it.
- **Decision V at quadratic order is a site-local counterterm [ARGUED identification].** Expanding Σ_x e₀(h(x)) gives completion C3 below.
  - It satisfies (Σ) at k⁰.
  - It passes at O(k²) iff the paramagnetic O(q²) part is already Fierz–Pauli.
  - #9198 found the analogous test fails for block 62's coupling (float result, not landed).
- **Better: Decision S** (recorded, NOT adopted): "the walker–member coupling's second-order contact term obeys the relabelling sum rule (Σ)."
  - It is the lattice analogue of minimal coupling, the diamagnetic sum rule.
  - It is a covariance requirement on the supplied coupling, not a choice of the vacuum's zero. Block 147's reading question (V₀, the pressure tadpole) stays separate.
  - At quadratic order it needs no group closure. Closure does fail beyond that order: {G_ξ, G_η} carries cos 2k_l weights [ARGUED, from the Poisson symbol]. That matters for graviton self-interaction, not for the linear graviton.
- **What it costs [EXACT].**
  - (Σ) fixes the contact term on gauge rows, but leaves its invariant part c_s·F free. So the Einstein–Hilbert coefficient is c = c_sea + c_s unless the completion is pinned.
  - The natural pin is ultralocality, the Peierls analogue: a q-independent contact term that contributes only at k⁰.
  - Whether an ultralocal solution of (Σ) exists is the decisive question.

## 3. Decisive computation spec (not run)

**Setting.**
- μ ∈ {0.25, 0.5, 1}; μ = 0 is reported only as a limit.
- q = 2πn/L with n = 1…4, along (100), (110), (111) and (123).
- L ∈ {48, 64, 96, 128}, or zone quadrature.
- One worker, BLAS = 1.

**Coupling.**
- V(Rh): block 69's bond operator with block 120's φ placement, in block 62's site convention with block 120's phase reindexing.
- Normal-order V (subtract ⟨V(Rh)⟩) and report W₁ separately as the pressure.
- Never normal-order S.

**Completions.** W₂ depends on S only through s(q) = ⟨S⟩.
- **C0:** S = 0. This is the control.
- **C1:** block 69's linear or block 176's per-axis completion, site by site (q₂ = −1/2). This is the control.
- **C2:** bond-ultralocal, s_B ≡ −2M₀ on all nine bond components.
- **C3:** ultralocal on the member's sites, s_h ≡ −2R(0)†M₀R(0). This is Decision V at quadratic order.

Here M₀(B,B) = −⟨(μ²|w_B|² + |s×w_B|²)/(2R³)⟩, with w_{B,a} = c_aΣ_jB_a^j s_jc_j and R = (|s|² + μ²)^{1/2}. This is the exact second-order expansion of −(|s+w|² + μ²)^{1/2}, using block 69 T4's uniform symbol [EXACT]. Its diagonal entries reproduce block 183 T5's I_μ term. C2 and C3 differ at O(q²) through R(q).

**Positive controls.**
- **PC1:** the q → 0 limit of χ_para(q) equals M₀. This is the unconstrained Hessian, not 09-26 T2's fixed-volume Q.
- **PC2:** 2χ_para(q)D(q)ξ = Λ_G(q)ξ, with Λ_G = ⟨i[G_ξ, V(·)]⟩, where D(q) is the gradient ξ → dξ. This is exact on every finite torus, so it must hold to machine precision. The bubble has energy denominators; Λ_G has none.
- **PC3:** W₁(RG_mξ) = 0 (block 120).
- **PC4:** C1's diagonal uniform Hessian reproduces block 183 T5's E₂(q₂).

**Primary read-out: the Ward residual.**
- For each completion, compute ρ_C(q) = ‖χ_C(q)G_m(q)‖ / (‖χ_C^TT(q)‖·|q|), and extrapolate in L, then |q| → 0.
- By (ii), ρ_C = ½R†[Λ_Z + s_C·RG_m], which has no energy denominators.
- For C3 this reduces to a closed-form zone-average check at O(q³): ½Λ₃ = M₀G₃.
- Compute ρ_C both from the bubble and from Λ_Z; agreement is an extra control. C0 must return exactly ½Λ_Z.

**Secondary read-out (only after a pass).**
- c from a single TT entry; Ward implies isotropy and the Fierz–Pauli form.
- The TT inertia m_TT from the O(ω²) bubble of the same coupling, which is positive semidefinite [EXACT].
- The transverse-trace stiffness and inertia.

**Outcomes.**

| Result | Meaning |
|---|---|
| A positive control fails | Code bug. |
| C3 passes | Decision V's site-local counterterm is enough and the sea fixes c. If c > 0: ω² = c k²/m_TT, two linear TT modes. If c < 0: wrong-sign Einstein–Hilbert term; the route fails. |
| C2 passes, C3 fails | The counterterm must be bond-local (Peierls-like); V is the wrong counterterm. c comes from C2. |
| Both pass | They differ by an invariant c_s·F. Report the spread; a conclusion holds only if the signs agree. |
| Both fail at O(q³) | No ultralocal completion is Ward-compatible. Any compatible one carries a free c_s, so the Einstein–Hilbert coefficient becomes a supplied constant. The sea still fixes the inertia and the gauge rows. |

**Prior [ARGUED, unverified].** Λ(q) = −Σ_k[n(k+q) − n(k)]·ḡ·v̄, where n is the band direction and ḡ, v̄ are the endpoint-averaged symbols of G_ξ and V. It involves third derivatives of n weighted by P-functions, and I see no reason for it to be proportional to D(q) at O(q³). So I expect "both fail".

## 4. Is a linear graviton reachable from finite-qubit composites plus the sea?

**Spectral trichotomy [EXACT].** A relabelling redundancy that shifts h(x) by every real amount can be implemented by a unitary iff h(x)'s spectrum is invariant under those shifts. That leaves three cases; bounded spins fit none.
- **ℝ (noncompact):** this is the (ℝ, ℝ) supply of R1 as specified and of R2.
- **A periodic variable (rotor):** W(h) is then periodic and invariant, so its characters must be gauge-invariant with m = O(k²) [LANDED moment bound; review Step 3b]. That rules out h·R(h) and any k² stiffness, giving ω ∝ k² at best. The sea cannot get around this: a periodic coupling induces a periodic functional.
- **ℤ_N (finite-dimensional):** relabellings are then discrete. Aliased characters (R3) might carry an Einstein–Hilbert-like moment up to a length ℓ*(N); this is untested.

**The scalar sector [EXACT, plus ARGUED].**
- The Ward-invariant O(k²) form is Fierz–Pauli, which is negative on the transverse trace (review Step 7).
- The sea's adiabatic inertia is positive semidefinite and nonzero there: #9198's form gives A′/16 > 0 for k̂ = e₃ (EXACT algebra on an unlanded formula); for block 69's coupling this is ARGUED.
- So even a pass with c > 0 gives two linear TT modes plus a tachyonic transverse-trace mode, unless a re-timing constraint is supplied.
- The landed 09-25 note shows no positive inertia lies on β = −α, so the clock/rate sector would have to carry that constraint as a separate supply.

**Composite graviton from an interacting sea [ARGUED].** With a supplied four-fermion coupling g, a massless RPA pole at q → 0 needs 1 = gχ(0). Ward forces χ(0) = 0, so no finite g works. Without Ward, it is a tuned critical point.

**Honest answer.** No route examined here gives two linear TT modes from finite-qubit composites plus the sea. Each one needs:
- an (ℝ, ℝ) tensor variable, or the N → ∞ limit, or the untested finite-N aliasing route R3;
- plus a re-timing constraint for the scalar.

In the corrected route (R1′), the sea supplies inertia for that supplied field, and in a C2- or C3-pass outcome its Einstein–Hilbert coefficient. It does not replace the field.

## Summary
1. **[LANDED + EXACT]** Block 69's coupling is the gauged two-step translation, and this extends to μ > 0 because [ε, P_j] = 0.
2. **[LANDED + ARGUED]** Block 120's placement makes every member gauge direction tangent to the unitary orbit, through the local generator Z_ξ.
3. **[EXACT]** Theorem W: 2W₂(h, Gξ) = ⟨i[Z_ξ, V(Rh)]⟩ + ⟨S(h, Gξ)⟩. The linear coupling fails strictly, and normal ordering cannot fix it.
4. **[EXACT]** A linear coupling cannot produce an Einstein–Hilbert term: χ ≤ 0 and Ward together force c = 0.
5. **[EXACT]** Restoring Ward takes the sum rule (Σ), not a further sea symmetry. Decision R cannot enforce it.
6. **[EXACT]** Decision S (not adopted) fixes the gauge rows and leaves one free constant c_s.
7. **[pushed, not landed]** Block 183's q₂* is the E_g sum-rule point, and the covariant q₂ = −1/2 misses it.
8. **Spec:** C0–C3 completions; positive controls PC1 = M₀ and PC2 = the exact finite-torus identity; the Ward residual is primary and has no energy denominators. Prior [ARGUED]: both ultralocal completions fail.
9. **[EXACT]** The spectral trichotomy: exact relabelling needs ℝ, a periodic variable, or ℤ_N, and periodic variables forbid h·R(h).
10. **[EXACT + ARGUED]** Even with c > 0, the transverse-trace mode is tachyonic without a supplied re-timing constraint.