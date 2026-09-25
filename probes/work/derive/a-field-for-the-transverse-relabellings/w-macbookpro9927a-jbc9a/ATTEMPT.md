# Can any object of the clauses absorb relabellings in time across the wave?

Unit `J:derive:a-field-for-the-transverse-relabellings:a1`, worker `w-macbookpro9927a-jbc9a` (Claude Opus 5.5), 2026-09-25. No prior attempts were printed at claim time.

**Related work by this worker (disclosed).** `relabelling-blindness-in-the-cube-kinetic-family` a2 (#9225, same day) reproduced block 124 T3–T5 and found the transverse relabellings drifting. The present question starts where it stopped. Block 124 (PR #9178, open) is by the supervisor's model family, which is also this worker's.

## 1. Setting
**Block 62 as landed, at one wave vector.**
- The fields are the strain h (symmetric), the rates' multiplier u, and the symbols p_j = 2 sin(k_j/2).
- R₁ = p² tr h − p·h·p and R₂ = −(p²/4)tr h² + |hp|²/2 − (p·h·p) tr h/2 + (p²/4)(tr h)².
- The Lagrangian is L = α ḣ_ijḣ_ij + β(tr ḣ)² + K(uR₁ + R₂).

**Relabellings in time.** h → h + (pξᵀ + ξpᵀ)ζ(t).
- *Transverse:* p·ξ = 0.
- *Gradient:* ξ ∥ p.

**A symmetry** is a transformation that changes L by a total time derivative. "Only if" is shown by the Euler operator, which annihilates total derivatives; "if" by an explicit construction.

**Objects of the landed clauses.**
- **Records and their contents.** "A site never carries more than one record; records are permanent."
- **Site rates w_x** (blocks 53, 60): one number per site, a multiplier in the ledger.
- **Bond rates c_b and lengths ℓ_b = √(w_xw_y)/c_b** (block 59): one number per bond each.
  - They multiply the walker's hops: H = Σ c_b h_b + Σ w_x m_x.
  - The bond rates obey block 59's linear nearest-bond law, a quadratic energy with matrix M(k). The coefficients are those restated in block 84.
- **Bond strains B_a^j and plaquette curls F** (block 64).
  - B is the walk's coupling to the frame; to first order the frame's strain is −B.
  - It relabels as B → B + d_aξ_j.
  - The curls are unchanged by relabellings.
- **The twist** (block 65).
  - It is a site field ϑ (three per site), and the twist along a bond is d_aϑ_a (one per bond).
  - It enters the blind walk H[ϑ] = H + ½Σ_j{(ϑ × e_j)·σ, S_j} + ½Σ_a C_a[d_aϑ_a].
  - It shifts together with a rotation of the coin axes.
- **The walker's currents** (block 63; block 65's densities): the momentum density π_j (three per site), the bond current J_a^j, the site response Θ_a^j and the bond density b_c (one per bond). All are functionals of the walker's state.

## 2. Statement
- **(a)** A transverse relabelling in time changes L by 4αζ′ ξ·ḣ·p + 2αp²|ξ|²ζ′², at every (α, β) (block 124 T3).
  - It is absorbed only by a field X that shifts by ξ′.
  - The most general local second-order coupling that absorbs it is T(D) − T(ḣ), with D = ḣ − pXᵀ − Xpᵀ, plus terms that vanish when p·X = 0.
  - None of the candidates' own clauses permits X → X + ξ′.
- **(b)** Nothing built from these objects at nearest-neighbour reach absorbs it. The minimal new object is a bond vector N_j, one number per bond, with no law of its own (a multiplier), entering as ḣ_ij − (d_iN_j + d_jN_i).
- **(c)** With that N, the (h, u, N) system has 10 components.
  - The three relabellings, (pξᵀ + ξpᵀ, u = 0, N = ξ′), are symmetries at every (α, β).
  - After fixing them, the only finite frequencies are the transverse traceless pair, Ω² = Kp²/(4α), each twice. There are no zero-frequency drifts: the transverse trace, u and N are fixed by constraints.
  - At β = −α there is one more symmetry: u and N absorb the gradient relabelling separately, so their difference is null at every frequency.

## 3. Steps
1. **The change to absorb. CHECKED A1** (block 124 T3 reproduced). Its Euler derivative in ζ is not zero, so without a compensating field the transverse relabelling is not a symmetry.

2. **The form of any absorbing coupling. PROVED; CHECKED B4.**
   - Let X be a field transforming as X → X + ξζ′, and let the Lagrangian be T(ḣ) + ḣ·K·X + X·Q·X.
   - The transformation acts on the 9 variables (ḣ, X) along 2 directions (ξ ⊥ p). The invariant linear combinations are D (6) and p·X (1).
   - A quadratic form invariant up to total derivatives must be a form in (D, p·X). Its ḣḣ part must equal T.
   - So it is T(D) + ℓ(D)(p·X) + c(p·X)², with 6 + 1 free numbers.
   - B4 solves all Euler-derivative conditions at p = (1,2,2) for the 24 unknowns of K and Q. It finds one family with exactly 7 free numbers. The residual beyond T(D) − T(ḣ) is invariant under the joint shift and vanishes when p·X = 0.

3. **Candidates, one by one. PROVED; CHECKED B1, B2.**
   - *Bond rates (one per bond)* have their own law.
     - Their quadratic energy ½cᵀM(k)c changes under c → c + vζ′ (v ⊥ p) by −ζ′vᵀMc − ½vᵀMvζ′². Its Euler derivative is nonzero at generic (α, β, γ, k) (B1).
     - The rates also multiply the walker's hops, so the walker's generator would change by ζ′Σv_bh_b.
     - The law does not permit the shift. The lengths are functions of the rates and inherit this.
   - *Block 64's strains* are the frame itself. They shift by dξ, not ξ′; the curls do not shift at all.
   - *The twist.*
     - Shifting ϑ by vζ′ without rotating the coin adds ζ′ times a nonzero hermitian operator to the walker's generator (B2, on a 4³ torus). Its clause pairs a shift of ϑ with a coin rotation ψ → U(x)ψ.
     - A coin rotation is not a relabelling. A relabelling of the walker is the unitary e^{−iG_ξ}, with G_ξ = ½Σ{ξ_j, S_j} (block 63), a different operator.
   - *The walker's currents and densities* are expectations in the walker's state. A time-dependent relabelling moves that state by e^{−iG_ξ(t)}, so these expectations change by amounts linear in ξ(t), not ξ′.
     - The walker's own Lagrangian picks up ζ′⟨G_ξ⟩, which couples to the momentum density, not to ḣ.
   - *Site rates* are one scalar per site. At most they absorb the gradient part, through u → u − (2α/K)ζ″ at β = −α (block 124; #9225).
   - *Records and contents* are permanent.

4. **No local construction. PROVED; CHECKED B3.**
   - Let X = A(k)[ḣ, …] be any local combination of nearest-neighbour reach. Its symbol is bounded near k = 0, and its h-dependent part shifts by A(pξ′ᵀ + ξ′pᵀ), whose size is at most 2‖A‖|p||ξ′|.
   - Shifting by ξ′ requires A(pξ′ᵀ + ξ′pᵀ) = ξ′ for every transverse ξ′. As k → 0 the left side tends to 0 and the right side does not.
   - The other objects' shifts contain no ξ′ at all (step 3).
   - So no local combination of the landed objects shifts by ξ′. A shift built from ḣ would need 1/p, which is nonlocal.
   - B3 checks the finite instance: no A with entries of degree ≤ 1 in p exists.

5. **The minimal new object. PROVED.**
   - A bond vector N with no law of its own, transforming as N → N + ξ′, and coupled only through D. D is then exactly invariant.
   - One number per bond is the minimum: two transverse components (and the gradient) at every bond must be absorbed.
   - This is the comparator's shift vector; it is named as a comparator only.

6. **The 10×10 system. CHECKED C1** (β = 0, 1/2, −1; p = (1,2,2) and (2/5, 1/3, −3/7); α = K = 1).
   - The modes solve (Ω²A + iΩ(B − Bᵀ) + C)q = 0, for q ∝ e^{−iΩt}.
   - The three relabelling vectors are null at every Ω.
   - Keeping the transverse traceless pair, the transverse trace, u and N gives the 7×7 reduced determinant. At β = 0 and p = (1,2,2) it is −30233088(2Ω − 3)²(2Ω + 3)²: only Ω² = p²/4, twice.
   - At β = −α the reduced determinant vanishes identically. The extra null vector (h = 0, u = 2Ω², N = iΩp/2) is the u-absorption of the gradient minus its N-absorption.

## 4. ASSUMED
None beyond standard linear algebra and calculus.

## 5. What would finish it
- A law for N (the momentum constraint's partner) and its source, the walker's momentum.
- Orders beyond the second.
- Whether a composite of landed objects at larger reach could act as N. Step 4 excludes every local one.
