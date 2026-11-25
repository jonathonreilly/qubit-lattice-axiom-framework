lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T18:31Z

# Check of row 1508 (Lean Stage 1d, Trace.lean), queue row 1524

Started 2026-11-25T06:31Z (date -u) on Mac mini worker 2, at commit 0a994ddb0, branch claude/ym4d-hard-route.
Checker: Claude Opus 5.5 high. Author of the checked work: gpt-6.2-astra max (row 1508).
Method: by reading only; no build (the lead replays the build and prints axioms).

## Plan

1. Read lean/gapchain/RECEIPT-1d.md and GapChain/Trace.lean in full.
2. Q1: compare Trace.cyclic with Periodic.cyclic (Periodic.lean, row 1509) symbol by symbol.
3. Q2: Kernel.cyclic_eq_tsum statement, hypotheses, route vs check 1507 Q4.
4. Q3: operator_compose and hasSum_hs_pairing statements.
5. Q4: eigenvalue enumeration vs PositiveSlot / transfer_boxSpectrum.
6. Q5: Trace.cyclic_eq_tsum vs hypothesis of Periodic.torusData_of_trace.
7. Verdict.

## Sources read (in full)

- `lean/gapchain/GapChain/Trace.lean` (547 lines; SHA-256 dc9cc02c3cf3f0ea15004901a014430bdafa6b6fc8344c4650f4cbf245aea8a1, which matches RECEIPT-1d).
- `lean/gapchain/RECEIPT-1d.md` (112 lines).
- `lean/gapchain/GapChain/Periodic.lean` (299 lines, row 1509).
- Relied-on parts of `Transfer.lean` (Space, row, operator, adjKernel, operator_adjoint, realOperator, realOperator_eq, transfer, transferKernel_memLp, transfer_positive, transfer_boxSpectrum), `Wilson.lean` 375-385 and 471-505 (nonzero_eigenblock_basis, PositiveSlot, nonzero_eigenvalue_has_slot, boxSpectrum_of_operator statement), `TheoremS.lean` 315-331 and 430-437 (BoxSpectrum, weight, Box, Box.Valid).
- Check 1507 Q4 (`library/lean-gap-chain-stage1c-check-opus.md` lines 98-120), for the route comparison.

Scan of Trace.lean for `sorry|admit|axiom |native_decide|implemented_by|opaque|unsafe|extern|set_option|macro|elab|@[`: 0 hits. The file has 32 `#print axioms` lines, one per theorem, matching the 32 receipt reports. I did not build and did not see the build logs (they are under the author's /private/tmp folder). The axiom lists are taken from the receipt; the lead's replay is the check on them.

## Q1. Is Trace.cyclic symbol for symbol Periodic.cyclic?

Yes. `diff` of Trace.lean 488-490 against Periodic.lean 21-23 is empty: both are
`def cyclic (β : ℝ) (R : Box) (a : ℕ) : ℝ := ∫ u : Fin a → Slice R, ∏ t : Fin a, transferKernel β R (u t, u (finRotate a t)) ∂(Measure.pi fun _ => sliceHaar R)`.

Name resolution. The namespaces are GapChain.Wilson.Trace and GapChain.Wilson.Periodic. Box is GapChain.Box (TheoremS 430). Slice, sliceHaar and transferKernel are GapChain.Wilson declarations (Transfer 502, 504, 548). finRotate and Fin are root names, and Measure.pi is MeasureTheory.Measure.pi; both files open MeasureTheory. Trace opens Set and InnerProductSpace in addition, and Periodic opens Topology. None of these namespaces declares Box, Slice, sliceHaar, transferKernel, finRotate or Measure.pi, so every identifier resolves to the same constant in both files. The two definitions differ only in their own names. The bodies are the same source text with the same resolved constants, so `Trace.cyclic β R a = Periodic.cyclic β R a` holds by `rfl` after delta-unfolding both. I did not verify one point by reading: the two modules import different extra Mathlib files (VectorMeasure.WithDensity versus Probability.ProductMeasure), so instance arguments could elaborate along different paths. Such paths are definitionally equal, and `rfl` checks definitional equality. The receipt says the author's consumer checked the body by `rfl`, and the lead's `cyclic_agree` build is the decisive check. **Q1: yes.**

## Q2. Kernel.cyclic_eq_tsum: statement, hidden hypotheses, route

Statement (Trace 474-478). The context is X with a MeasurableSpace, μ with `[IsProbabilityMeasure μ]`, and k : X × X → ℂ. Hypotheses: `hk : MemLp k 2 (μ.prod μ)`, `hp : (operator k hk).IsPositive`, `ha : 2 ≤ a`. Conclusion: `∫ u : Fin a → X, ∏ t, k (u t, u (finRotate a t)) ∂copies μ a = ((∑' i : PositiveSlot (operator k hk), i.1.val ^ a : ℝ) : ℂ) ∧ Summable (fun i : PositiveSlot (operator k hk) => i.1.val ^ a)`. Here `copies μ a` is the abbrev `Measure.pi fun _ : Fin a => μ` (Trace 217).

- Hidden hypotheses: none. The `variable {H ...}` block at Trace 383 is not used by this theorem, so it is not included. No separability, countable generation, topology, boundedness or realness of k is assumed. `operator k hk` is the Transfer.lean L² integral operator: `row k x` is the conjugate of the section k(x,·), so (operator k hk f)(x) = ∫ k(x,y) f(y) dμ(y) a.e. (operator_apply). So the integrand ∏_t k(u_t, u_{t+1}), with indices mod a, is the kernel of Tr T^a.
- "Positive eigenvalues with multiplicity": `PositiveSlot T = Σ r : {r : ℝ // 0 < r}, Fin (finrank ℂ (eigenspace T r))` (Wilson 477). It gives one slot per orthonormal direction of each positive eigenspace. Non-eigenvalues get Fin 0. For self-adjoint T, geometric multiplicity equals the multiplicity in the spectral sum. Since T is positive, `nonzero_eigenvalue_has_slot` shows that every nonzero eigenvalue is a positive slot value. So the sum runs over the whole nonzero point spectrum.
- "Summable": the second conjunct gives summability of the real a-th powers. The first conjunct is then a genuine sum, not the zero value of `tsum` on a non-summable family.
- So the receipt's claim holds as stated: for any square-integrable complex kernel whose operator is positive, on a probability space, for every a ≥ 2, the cyclic integral equals the summable sum of the positive eigenvalues' a-th powers, counted with multiplicity.

Route. This is **not** check 1507 Q4's route. That route expanded T^{a-2} spectrally on kernel columns and used monotone convergence, valid for a ≥ 3. Row 1508 takes the alternative that 1507 Q4 step 3 names ("or the HS equality of A0(e)"), which is row 667 A0(e): Hilbert–Schmidt pairing plus kernel composition. I checked each step's statement and the logic between steps:
1. `ae_eq_of_operator_eq`: equal operators imply equal kernels μ⊗μ-a.e. Pairing against indicator functions makes the vector measures k·d(μ⊗μ) and l·d(μ⊗μ) agree on measurable rectangles. Rectangles form a generating π-system, so the measures agree, and `Integrable.ae_eq_of_withDensityᵥ_eq` gives k = l a.e. This is valid with no separability.
2. `exists_kernel_basis`: the rank-one kernels (x,y) ↦ b_j(x) conj(b_i(y)) form a Hilbert basis of L²(μ⊗μ), for any Hilbert basis b of L²(μ). Orthonormality follows from `inner_rankKernel_rankKernel`. Completeness: if q is orthogonal to all of them, then ⟪b_j, T_q b_i⟫ = 0 for all i, j, so T_q b_i = 0, so T_q = 0, so q = 0 a.e. by step 1. This answers 1507's caution (i) at a = 2 without separability.
3. `hasSum_loopProduct`: for any Hilbert basis b and L² kernels k, l, ∑_i ⟪b_i, T_l T_k^{n+1} b_i⟫ = ∫ loopProduct k l n. The base case n = 0 is `hasSum_hs_pairing` with the kernels adjKernel l and k, since T_{adj l} = T_l^* (operator_adjoint), and ∫ conj(adj l) k = ∫ k(x,y) l(y,x). The step integrates out vertex 0 (`integral_loopProduct_succ`, `integral_vertex`). This replaces the closing kernel l by compose l k, and T_{l∘k} = T_l T_k (`operator_compose`). The Fubini justification is `integrable_loopProduct`, which proves the integrand integrable for any L² kernels. It runs an induction with the norm kernels |k| and compose |l| |k|, which answers 1507's caution (ii).
4. `exists_positive_slot_basis`: an orthonormal family of eigenvectors indexed injectively by PositiveSlot T is extended to a Hilbert basis, and T kills every added vector. Proof: T(b p) is orthogonal to every eigenspace, using symmetry and the fact that each nonzero eigenspace is spanned by its slot vectors, which are orthogonal to b p. The compact self-adjoint spectral theorem then makes the orthogonal complement of the eigenspaces zero. The proof uses `.choose` of `nonzero_eigenblock_basis`, as 1507 (K3) asked. The sum depends only on the index type and i.1.val, not on the choice.
5. `hasSum_cyclic`: the trace terms vanish off the slots (T^{n+2} = T^{n+1}·T, and T kills the added vectors) and equal λ^{n+2} on the slots. `Function.Injective.hasSum_iff` moves the sum to PositiveSlot, and `loopProduct_rotate` converts loopProduct k k n into the finRotate product.

The route is valid, and it is stronger than 1507 recommended: arbitrary L² complex kernels, a ≥ 2, no separability. **Q2: yes.**

## Q3. operator_compose and hasSum_hs_pairing

- `compose μ k l (x,z) = ∫ k(x,y) l(y,z) dμ(y)` (Trace 153). `operator_compose`: `operator (compose μ k l) (compose_memLp hk hl) = operator k hk * operator l hl`. By Fubini, (T_k T_l f)(x) = ∫ k(x,y) ∫ l(y,z) f(z) dz dy = ∫ (∫ k(x,y) l(y,z) dy) f(z) dz, so the composed kernel represents T_k T_l in this order. In Mathlib, `*` on CLMs is composition with the right factor applied first. The statement is correct. The pointwise Bochner integral defaults to 0 where the y-integrand is not integrable. That happens only on a null set (`compose_eq_inner` a.e.), and the operator depends only on the a.e. class, so the default is harmless. `compose_memLp` gives the L² bound |c(x,z)| ≤ ‖k(x,·)‖ ‖l(·,z)‖ (Cauchy–Schwarz on rows).
- `hasSum_hs_pairing`: `HasSum (fun i => ⟪T_k b_i, T_l b_i⟫) ⟪k, l⟫_{L²(μ⊗μ)}` for every Hilbert basis b, with Mathlib's inner product conjugate-linear in the first slot. Both sides equal Tr(T_k^* T_l) = ∫ conj(k) l, so the conjugations match. The convergence is unconditional (`HasSum`) over an arbitrary index type. It comes from Parseval on the product basis and `HasSum.prod_fiberwise`. **Q3: yes, both stated correctly.**

## Q4. Is the eigenvalue enumeration the BoxSpectrum one?

Yes. There is one `PositiveSlot`, GapChain.Wilson.PositiveSlot (Wilson 477); grep finds no other declaration. Trace refers to it through `open Module.End Wilson` inside `namespace GapChain` (Trace 381), which covers `exists_positive_slot_basis`, `hasSum_cyclic` and `cyclic_eq_tsum`. The Wilson-level `Trace.cyclic_eq_tsum` sums over `PositiveSlot (transfer β R)`. That is the index type and summand (`i.1.val ^ a`) of the weight clause of `transfer_boxSpectrum` (Transfer 757-761): `B.weight a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a` for a ≥ 3. The step from the general operator to `transfer` is `transfer β R = Kernel.operator _ (transferKernel_memLp β R)` by `rfl` (Trace 501). It holds because `transfer` is `realOperator (sliceHaar R) (transferKernel β R)` and `realOperator_eq` is itself `rfl` (Transfer 323-324); the MemLp proofs agree by proof irrelevance. The real part is taken through `Complex.hasSum_ofReal` after rewriting the complex product of real kernel values as a real product (`Complex.ofReal_prod`, `integral_complex_ofReal`). So the sum is the BoxSpectrum weight of the witness chosen in `transfer_boxSpectrum`. **Q4: yes.**

## Q5. Does Trace.cyclic_eq_tsum match the trace hypothesis of torusData_of_trace?

The hypothesis (Periodic 268-269) is `trace : ∀ R : Box, R.Valid → ∀ a : ℕ, 3 ≤ a → Periodic.cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a`, for β with hβ : 0 < β.
The theorem (Trace 506-508) is `Trace.cyclic_eq_tsum {β} (hβ : 0 < β) (R : Box) (_hR : R.Valid) {a : ℕ} (ha : 3 ≤ a) : Trace.cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a`.
The right sides are the same text. The left sides agree by Q1 (delta). The hypotheses match: β > 0, R valid, a ≥ 3. Two binder differences are not mismatches:
- a is implicit in the theorem and explicit in the hypothesis, so the instance is `fun R hR a ha => Trace.cyclic_eq_tsum hβ R hR ha`, elaborated against the expected type, where `Trace.cyclic` unfolds to `Periodic.cyclic`.
- `_hR` is unused, so the identity holds on every box, and `cyclic_hasSum` holds for β ≥ 0 and a ≥ 2.
**Q5: yes, exact match up to binder explicitness.**

## Remarks (none breaking)

1. The receipt's prose says "the two incident norm kernels supplies the Fubini bound", which describes `integrable_loopProduct` correctly. The receipt's "Proof" paragraph on the positive specialization matches `exists_positive_slot_basis`.
2. `Trace.cyclic` is a second copy of `Periodic.cyclic`. The join could later delete one copy and point the other at it. That is the lead's choice and not needed for correctness.
3. Not verified here: that the build passes and the axiom lists are as printed (receipt only; the lead replays them), and that `GapChain/Assembly.lean` exists. It is not in this checkout at 0a994ddb0 (`ls` fails), so I could not check its 20-line join.

Prior-statement check: `grep -i -E 'cyclic|hilbert.schmidt|power sum|trace identity' library/open-core.md` gives no match. FINISH rows 1508/1509/1524 carry the identity. Row 667 A0(e) and row 698 Lemma 1.1 (ii) give it by hand (Claude Opus 5.5). The design credit (GL8 of Sussman–Alpoge, outline lines 2315-2335 at 31a47c543775) is as in the receipt. Nothing here is claimed new.

## Verdict

**FAITHFUL.** No changes required.
- Trace.cyclic is symbol for symbol Periodic.cyclic, with the same resolved constants, so the two agree by rfl (Q1).
- Kernel.cyclic_eq_tsum states exactly the receipt's claim: any MemLp-2 complex kernel with positive operator on a probability space, a ≥ 2, the sum over PositiveSlot (positive eigenvalues with multiplicity), summable. It has no hidden hypothesis. It follows the Hilbert–Schmidt-pairing route (row 667 A0(e)), not check 1507 Q4's column-expansion route, and the route is valid (Q2).
- operator_compose and hasSum_hs_pairing are stated correctly (Q3).
- The enumeration is the same GapChain.Wilson.PositiveSlot (transfer β R) as transfer_boxSpectrum's weight clause (Q4).
- Trace.cyclic_eq_tsum discharges the trace hypothesis of Periodic.torusData_of_trace exactly, up to binder explicitness (Q5).

Open: the lead's build replay and axiom print, the Assembly join (not in this checkout), and the physical seed (T.seed N < 1/5041).

Done 2026-11-25T06:35Z (date -u). Reading only; no numeric job and no build were run.
