**Hostile review: Lane F (gravity) REPORT**

I read the brief, the full REPORT and the landed notes it relies on, all at `origin/main` 0485dc0738. Those notes are the 09-26 sea-shear note, the tensor parent (09-14), the oscillator-slot note (09-24), block 62, block 147's scope and T3, and the scopes of block 120, the 09-21 three-responses note and the 09-25 one-light-cone and relabelling notes. I also read open probe issue #9198, which is not landed. No code was run and no files were written.

## Verdicts

| Claim | Verdict |
|---|---|
| O1 placement lemma (Steps 1–2) | HOLDS WITH NARROWED SCOPE |
| O2 range | HOLDS (nearest-neighbour on the fine lattice) |
| O3 / Step 3 compactness table | HOLDS (EXACT within the regular local class); two caveats |
| Step 1, ⟨Θ_a^j⟩ = −θ₀δ_a^j | The identity HOLDS; reading it as a "composite tetrad" is WRONG (overreach) |
| Step 5, one term gives two effects | HOLDS (EXACT within the comparator) |
| Step 7, Fierz–Pauli algebra and signs | HOLDS |
| Step 7, "cubic-anisotropic admixtures not excluded" | WRONG (too weak: they are excluded) |
| Step 2 counting; Step 4 "R1 escapes O3/O4" | GAP |
| Decisive computation spec (§5) | GAP (several errors; its μ = 0 case was already run in float) |
| O7 reading of the 09-26 note | HOLDS WITH NARROWED SCOPE |
| Decision V | Fine as a recorded, non-adopted decision. NOT minimal, and the fine-tuning is under-flagged |

## 1. Placement lemma (re-derived)

**Step 1 (EXACT).** Row j sits on class r_j and reads E_ij at r_j + {a, a−m}e_i. Take a C₂ that maps component j to ±j. With one class per row, it must map class r_j to itself, even for non-symmorphic operations. It sends the offsets to {−a, m−a}. Equality of the two sets forces a = m/2. Two side notes:
- m must be even; for odd m the hypothesis set is empty.
- The i = j case uses a C₂ about e_k.

**Step 2 (EXACT).**
- Centring gives o_ij ≡ r_j + (m/2)e_i.
- Storing E_ij and E_ji as one field on one class gives r_i − (m/2)e_i ≡ r_j − (m/2)e_j =: σ. Hence o_ii ≡ σ for every i.
- So "one class for the diagonal" follows from symmetric storage plus centring alone. C₂ and C₃ are not needed for that; they serve only to fix σ:
  - C₂ gives 2σ ≡ 0;
  - C₃ then gives σ ∈ {0, (m/2)(1,1,1)}, measured from the rotation centre.
- The two placements are one placement up to the fine-lattice translation (m/2)(1,1,1), which swaps V↔C and L↔P. The REPORT lists them as two.

**Can a component be split over classes?** Not usefully, within the span-m hypothesis:
- *Non-symmetric storage* (E_ij and E_ji as separate fields). Rows on one class put three components on each link. Rows on links put three slots at V and two on each face. Composites are still needed.
- *Splitting by irrep* (the E_g pair apart from the trace). The E_g pair still needs two commuting slots on one class. The trace on another class cannot be reached by a span-m two-point stencil.

**The real loophole is the stencil-span assumption, which the REPORT leaves implicit.**
- Use a wide centred difference for the diagonal entries (offsets ±m, so a = 0 is allowed) and the short one for the off-diagonal entries.
- Then o_ii ≡ σ + (m/2)e_i: E_ii sits on link class L_i, off-diagonal components on faces, rows on L_j.
- That is one slot per site. A single qubit works for ℤ₂.
- The costs:
  - the row reads E_jj two fine steps away, so it is not nearest-neighbour on the fine lattice;
  - the symbol of the diagonal difference vanishes at the class zone boundary, a doubler where the Gauss row loses rank.

The lemma should be stated with all three hypotheses: one class per component and per row, span-m two-point differences, and symmetric E stored once. The "≥ 3-qubit composite" consequence is really a trade against fine-lattice nearest-neighbour range.

**O2 (EXACT).** A stencil built from axis-displaced nearest neighbours has a symbol that is a sum of one-variable functions. It therefore has no k_i k_j term, so no mixed derivative is possible. That settles the scalar law and Pretko's law.

## 2. Step 3

**(a) The identity.**
- T(E + sβ) = T(E) + Re(β̄ sᵀME) + |β|² sᵀMs/2.
- Since Ms = GᵀK, the cross term is Re(β̄ KᵀGE).
- Since Gs = 0, sᵀMs = KᵀGs = 0.
- So the identity is exact for every β, finite and integer included.
- With the half-step phases, F commutes with M (F is trivial on the diagonal slots, and M's vvᵀ part lives there), so the identity carries over.

**Rotor sector (E ∈ ℤ, h ∈ U(1)).**
- U_x = e^{i(Sq)(x)} is well defined because S has integer stencils. It shifts E by Sᵀe_x.
- GSᵀ = 0, so U_x preserves ker G.
- H_E is diagonal in E, so it commutes with the G-projector. On ker G it commutes with U_x.

The logic holds: a quadratic T is a valid operator on integer E, whereas on periodic E a nonconstant quadratic cannot be single-valued (09-24). The obstruction was compactness, not integrality.

**(b) The h side.**
- A continuous α plus Fourier uniqueness forces Gm = 0 for every character. Weak invariance equals strong here, because e^{im·h} moves ker G into the sector GE = Gm, which is orthogonal.
- Moment bound, re-derived:
  - Gm = 0 for all k̂ gives m(0) = 0;
  - the O(k) term T_ijl, symmetric in (ij), must be antisymmetric in (il), so it vanishes;
  - hence m = O(k²) and H_hh = O(k⁴).
- This matches the parent: H_hh = O(k⁴), H_EE = O(k²), H_hE = O(k³).

**Caveats.**
1. *The compact/integer row.* The O(k) solutions of sᵀr = 0 are of two kinds: three gauge-type ones, r₁ = Gᵀc, and five curl-type ones, r₁ = sym(ε(k)e) with e symmetric and traceless.
   - The gauge-type ones carry zero transverse-traceless (TT) weight, because Gᵀc paired with E_TT gives c·(G E_TT) = 0.
   - The k² result therefore rests on the curl-type characters, which do carry TT weight. Example: for k ∥ z, the xx−yy entry is −4e_xy.
   - The row survives, but the REPORT should name this mechanism.
2. *What the k² rows mean.* ℤ-valued slots are infinite-dimensional (O4), so neither k² row is a finite-qubit construction. Each entry is an upper bound, attained by cos(R-row) or curl characters. A compact rank-2 phase with ω ∝ k² already exists in the literature (Xu), so "new" means new to this repo.

## 3. Step 7 (re-derived)

Take δh = k⊗ξ + ξ⊗k. The first-order variations are:
- δ tr h² = 4 ξ·hk
- δ|hk|² = 2k²(ξ·hk) + 2(ξ·k)(kᵀhk)
- δ[(kᵀhk) tr h] = 2(ξ·k)(kᵀhk) + 2k²(ξ·k) tr h
- δ[k²(tr h)²] = 4k²(ξ·k) tr h

Collecting terms gives exactly 4a + 2b = 0, 2b + 2c = 0 and 2c + 4d = 0.
- The three structures are independent: ξ ⊥ k isolates the first; ξ = k with h varied separates the other two.
- The solution is b = −2a, c = 2a, d = −a. The second-order invariance then follows automatically.
- This equals −4R₂, with R₂ checked against block 62. It also equals −h·inc(k)h.

Signs: on TT, F = a k² tr h² > 0. On the transverse trace φ(1 − k̂k̂), F = −2a k²φ² < 0. Both claims HOLD.

**Correction: the hedge is wrong.** Relabelling invariance alone forces the Fierz–Pauli form at O(k²), with no rotation symmetry assumed. (EXACT as a pen-and-paper proof; not machine-checked.)
1. Each row ℓ of a gauge-annihilating degree-2 L satisfies ℓk = 0.
2. The map from degree-2 symmetric polynomials (36-dimensional) to degree-3 vector polynomials (30-dimensional) is onto; there is a constructive monomial argument. Its kernel is therefore 6-dimensional and equals {inc(k)m : m constant}.
3. So L = M·inc(k). Hermiticity gives M·inc = inc·Mᵀ, so M preserves T(k) = {h : hk = 0} for every k.
4. For orthonormal k, k′, n, the intersection T(k) ∩ T(k′) is span(nnᵀ). So every nnᵀ is an eigenvector of M, which forces M = λ·1.

Consequences:
- If the Ward test passes at O(k³), c_TT is automatically isotropic and the same for both polarisations, and the transverse-trace sign is fixed.
- Read-outs (b)–(d) are implied by (a).
- The direction- and polarisation-dependent K that #9198 found is itself a Ward-failure signature.

## 4. O7 against the landed 09-26 note

**Accurate:**
- T2: negative definite on traceless uniform strain at fixed volume, for every μ ≥ 0.
- T3: lower at every size for unequal diagonal lengths.
- T4(c): R₁ and R₂ vanish on uniform strain.

**Narrowings required:**
1. *"TT" is wrong at k = 0.* There is no transversality at k = 0. All five traceless directions are unstable, with two separate cubic coefficients: diagonal ≤ −(B + 5A)/8 and off-diagonal ≤ −(A + B)/2.
2. *Conditional on block 147's first reading.* The note says that, measured above the sea, "none of this arises". O7 drops this conditional.
3. *Coupling scope.* The result is for block 62's frame coupling.
   - The note's 09-27 addendum says block 120 excludes the frame response as a source for the member's non-uniform modes.
   - Under block 69's two-step coupling, the instability's sign depends on a completion number q₂. That is block 183, which is pushed but not on main.
4. *"Tachyonic" is the REPORT's gloss, not the note's.* The note says the lattice is "forced to shear" within block 148's action. The gloss is correct conditionally: both supplied inertias are positive on traceless strain.
   - Block 148: for Σλ̇ = 0, L_kin = +4αVΣλ̇².
   - #9198 (c): 3A′ on the diagonal, B′ off it.
5. *"Relabelling broken at k = 0" is ARGUED, not landed.* On a torus, uniform strains are shape moduli. The defensible form: a long-wavelength pure-gauge strain costs bulk energy that no local relabelling-invariant density can produce.

## 5. Decision V

It does hide a fine-tuning, and it is worse than a cosmological-constant tuning.
1. **Not new.** It is block 147's second reading made frame-wise. Block 147 T3 (landed) already says a frame-dependent subtraction is "an additional coupling/counterterm choice". It changes source and pressure, and its inhomogeneous completion is open.
2. **Many constants, not one.** At quadratic order it tunes five cubic-invariant constants: the constant, the pressure, the bulk modulus, the E_g shear and the T₂g shear. Beyond quadratic order it tunes a whole function e₀(g).
3. **Not a cosmological constant.** A dilation gives −I(det g)^{−1/6}, which no multiple of √det g matches (09-26 T1, #9198). The traceless part is a graviton-mass counterterm that no symmetry protects.
4. **Cutoff-scale.** On #9198's float numbers, the cancelled off-diagonal coefficient B/4 ≈ 0.047 is about 10–14 times the TT q² stiffness K/4 ≈ 0.003–0.005. Without Decision V the whole TT branch would be unstable, not just its uniform end. (ARGUED: this assumes the two share a normalisation and that the O(q²) truncation holds to the zone edge.)
5. **"Every ledger" is ambiguous.** It must say the sea's inertia is kept, or Step 8 has no m_TT.
6. **Not minimal.** The graviton question needs V_T alone (the two traceless constants). V₀ (vacuum energy and pressure) is block 147's separate decision.

## Additional gaps the questions surfaced

**R1 relocates the noncompact variable rather than escaping it.** An "independent real frame field with zero bare action" is an (ℝ,ℝ)-type supply, the same import class as R2. Making it composite instead would need a supplied interaction and a collective-mode calculation, not §5's external-source linear response.

**The Step 1 "solder" is the vacuum tadpole.** ⟨Θ⟩ = −θ₀δ, with θ₀ = I/3 ≈ 0.40, is the expectation of the supplied soldered Hamiltonian's own terms. It is not a spontaneous condensate. Because this tadpole is nonzero, the O(k²) response depends on the nonlinear completion. The spec's E = (1+h)^{−1/2} on bond-averaged h adds a seagull residual of about +(3/32)θ₀ Σ_j k_j²(hh†)_jj ≈ 0.037 k² (ARGUED). That is:
- zero along the axes;
- of order 0.08–0.10 in K-units along (110) and (111);
- several times #9198's stiffness, against which the computation reads its sign.

**Step 2's count assumes re-timing closes.** Closure needs β = −α. The 09-25 note shows that line contains no positive-semidefinite form, while the sea's inertia is positive-semidefinite with zero dilation part. #9198 states "β = −α is impossible" for the sea.

## Required corrections

1. State O1's three hypotheses explicitly, add the mixed-span counterexample, and merge the two placements into one.
2. Replace Step 7's hedge with the general uniqueness result. Make the Ward test the single primary read-out, with (b)–(d) as consistency checks.
3. Cite #9198. At μ = 0 with block 62's coupling, its float results already show:
   - Ward fails, with relabelling-mode energies 0.00228 and 0.00395;
   - K = 0.013–0.019, anisotropic;
   - α/K = 0.29–0.39, which is not the one-light-cone value 1/4.
4. Re-specify §5:
   - use block 69's two-step current with block 120's φ-placement, not block 62's frame coupling;
   - use the linear coupling, or normal-order it bond by bond against the uniform sea, so the result does not depend on the completion;
   - fix the positive control to the unconstrained Hessian (#9198's formula, or the expansion inside 09-26 T2's proof), not T2's fixed-volume Q. As specified, the parametrisation alone shifts it by −(I_μ/8) tr h², so the check would fail;
   - report the spread across at least two completions.
5. Narrow O7 as listed in §4.
6. Re-label Decision V as block 147's counterterm made anisotropic. State that it is a cutoff-scale, multi-constant graviton-mass tuning, and split it into V₀ and V_T.
7. Mark Step 2 and Step 4 as GAP.

## Bottom line

The algebra in O1, O2, Step 3, Step 5 and Step 7 survives; Step 7 actually comes out stronger than claimed. The R1 route does not stand as written:
- its decisive computation uses the coupling that landed block 120 excludes;
- its μ = 0 case has a float precedent (#9198) that already falls in the "Ward fails" outcome;
- its O(k²) read-out depends on the completion at a size larger than the signal;
- its "escape" relocates the noncompact variable into a supplied real frame field.

Decision V should be flagged as a tuning that no symmetry protects and that is larger than the induced stiffness, not as a minimal clause.