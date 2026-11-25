lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T14:36Z

# Check of row 1506 (Lean Stage 1c, Wilson transfer operator), row 1507

Started 2026-11-25T02:36Z (date -u) on Mac mini worker 2, Claude Opus 5.5 high. Cross-provider check by reading (author gpt-6.2-astra), no build; the lead replays and prints axioms. Pinned at 2ff9eeb6b.

## Plan

1. Read `lean/gapchain/GapChain/Transfer.lean`, `RECEIPT-1c.md`, `Wilson.lean` (action, sides, links), and the hand sources: row 667 (`library/gap-transfer.md` (1a)), row 698 (`library/gap-seed-check.md` Lemma 1.1).
2. Q1: faithfulness of Slice, sliceHaar, spatialAction, gaugeAction, temporalAction, transferKernel.
3. Q2: operator lemmas and transfer_boxSpectrum vs the receipt; hidden hypotheses.
4. Q3: by hand, Z beta a R = cyclic beta R a (argument order, orientation, off-by-one, measure).
5. Q4: cyclic = sum of a-th powers of eigenvalues for a >= 3; missing kernel-unit pieces.
6. Verdict.

## Sources read

`lean/gapchain/GapChain/Transfer.lean` (821 lines, read in full), `lean/gapchain/RECEIPT-1c.md` (in full), `lean/gapchain/GapChain/Wilson.lean` lines 1-290 (SU2, linkHaar, halfTrace, step, transport, action, action_eq_geometric, sides, Z) and 380-575 (BoxSpectrum consumer), `library/gap-transfer.md` (row 667) Notation N.1-N.8 and Section 1 (1a), 1.1-1.9, `library/gap-seed-check.md` (row 698) Lemma 1.1. Hand sources rest on the Sussman-Alpoge account (CA-I Definition 1.1 conventions at 31a47c543775, outline 240-278 and GL8 2315-2335, cited by the author; not re-fetched here since row 1505 already checked the convention against CA-I).

## Q1. Faithfulness of the definitions

Write v_x for the vertex x, e = (x, i) for a positive spatial edge, x + e_i for `spatialStep x i`.

| Lean | Definition (read off the source) | Hand object | Match |
| --- | --- | --- | --- |
| `spatialSides R` | `![R.x, R.y, R.z]` | sides N_1, N_2, N_3 of Lambda (row 698 L1.1) | yes |
| `Vertex R`, `Edge R` | `(i : Fin 3) → Fin (side i)`, `Vertex R × Fin 3` | V = Lambda, E = {(x,i)}, positive spatial links only (N.3) | yes, 3|V| edges |
| `Slice R`, `sliceHaar R` | `Edge R → SU2`, `Measure.pi (fun _ => linkHaar)` | X = G^E with product normalized Haar (N.3) | yes |
| `linkHaar` | `haarMeasure haarDomain`, haarDomain = univ, `IsProbabilityMeasure` instance from `haarMeasure_self` | normalized Haar dg (N.1) | yes: left Haar of mass 1 on univ; on the compact group it is also right and inversion invariant (not needed by any Stage 1c proof, which only uses left invariance) |
| `Gauges R`, `gaugeHaar R` | `Vertex R → SU2`, product linkHaar | G^V with dh, one variable per vertex (N.5, 1a) | yes |
| `spatialStep` | `finRotate` on coordinate i only | x + e_i, periodic | yes; same formula as Wilson `step` |
| `SpatialPlane` | `{p : Fin 3 × Fin 3 // p.1 < p.2}`, 3 elements | 1 <= i < j <= 3 (N.4) | yes |
| `spatialAction u` | sum over x and i<j of 1 - halfTrace(u(x,i) u(x+e_i,j) u(x+e_j,i)^-1 u(x,j)^-1) | V(u)/beta (N.4) | yes, same word as Wilson `transport` |
| `halfTrace` | `re (trace g) / 2` | (1/2) tr g, real on SU(2) (N.2) | yes |
| `halfWeight β R` | exp(-beta S_sp(u)/2) | e^{-V(u)/2} | yes, beta once |
| `gaugeAction R (u, g)` | e ↦ g(x) u(e) g(x+e_i)^-1 | (h·u)_(x,i) = h(x) u_(x,i) h(x+e_i)^-1 (N.5) | yes; left action (`gauge_mul`: g·(h·u) = (gh)·u) |
| `temporalAction (u, w)` | sum over e of 1 - halfTrace(w_e u_e^-1) | sum over e of (1 - (1/2) tr(w_e u_e^-1)), K_0(u,w) = prod c(w_e u_e^-1) (N.7, c(g^-1) = c(g)) | yes |
| `temporal β R` | exp(-beta temporalAction) | K_0 | yes |
| `transferKernel β R` | `gram (halfWeight) * average gaugeHaar ((u,v),g) ↦ (u, g·v)` of `temporal` | A_T(u,v) of (1a) | yes, see next line |

`transferKernel_apply` (proved) states K_R(u,v) = exp(-beta(S_sp(u)+S_sp(v))/2) ∫ prod_e exp(-beta(1 - halfTrace(g(x) v_e g(x+e_i)^-1 u_e^-1))) dg, which is symbol for symbol the displayed A_T of row 667 (1a) (with V = beta S_sp), extended to unequal sides as in row 698 Lemma 1.1, and the K_R of RECEIPT-1b (checked in row 1505 Q4). Half the spatial action sits at each end, beta is counted once in each of the spatial and temporal parts, and the gauge variable acts on the second argument, as in (1a).

Plaquette count and orientation against `Wilson.lean`. `action_eq_geometric` gives action = sum over sites x of Fin 4 and pairs p.1 < p.2 in Fin 4 of 1 - halfTrace(transport U x p.1 p.2), six planes per site. With time = coordinate 0 of `sides a R = ![a, R.x, R.y, R.z]`: the three planes (i+1, j+1), i<j, give at time t exactly the `spatialAction` word of slice t (both use U(x,i) U(x+e_i,j) U(x+e_j,i)^-1 U(x,j)^-1); the three planes (0, i+1) give transport U x 0 (i+1) = U(x,0) U(x+e_0, i+1) U(x+e_{i+1}, 0)^-1 U(x, i+1)^-1 = g_t(v) U(t+1)_(v,i) g_t(v+e_i)^-1 U(t)_(v,i)^-1, which is the summand of temporalAction(U(t), g_t·U(t+1)) with no use of trace cyclicity or inversion. So 3 spatial + 3 temporal plaquettes per site, matching the Lean action exactly.

**Q1 verdict: FAITHFUL.** No definition to change.

Remarks (none breaking). (a) The definitions are total in R (any sides, including 1 and 2); all consumers carry `R.Valid`. (b) Pointwise symmetry K_R(u,v) = K_R(v,u) (hand 1.4) is not stated in Lean; self-adjointness of `transfer` is part of `IsPositive`, and nothing in Q3 or Q4 below needs pointwise symmetry.

## Q2. Operator lemmas against the receipt

Read against the receipt table (RECEIPT-1c lines 13-20) and the Outcome paragraph.

| Lean statement (as written) | Receipt claim | Match, hypotheses |
| --- | --- | --- |
| `Kernel.operator k hk : Lp ℂ 2 μ →L[ℂ] Lp ℂ 2 μ`, `operator_apply`: output =ᵐ x ↦ ∫ k(x,y) f(y) | bounded operator, row integral a.e. | yes; only `MemLp k 2 (μ.prod μ)` and `IsProbabilityMeasure μ` |
| `operator_congr`: k =ᵐ[μ.prod μ] l ⇒ same operator | product a.e. changes preserve the operator | yes |
| `operator_norm_le`: ‖operator k‖ ≤ ‖k‖_{L²(μ⊗μ)} | norm at most product L² norm | yes |
| `operator_hs`: `HSNormLE (operator k hk) ‖hk.toLp k‖`, where `HSNormLE A δ` (LemmaM1.lean:21) is: every finite orthonormal family v has sum ‖A v_i‖² ≤ δ² | finite-family HS bound | yes; this is the inequality half of A0(e) (row 667), not the equality ‖S_k‖_HS = ‖k‖_2 |
| `HSNormLE.isCompact` for any complete complex inner product space | compactness, nonseparable allowed | yes; proof truncates in a Hilbert basis from `exists_hilbertBasis`, no separability |
| `operator_adjoint`: adjoint = operator of `adjKernel k`, (x,y) ↦ conj k(y,x); `operator_selfAdjoint` under adjKernel k =ᵐ k | adjoint is conjugate transpose | yes |
| `transfer β R := realOperator (sliceHaar R) (transferKernel β R)` on `Space (sliceHaar R) = Lp ℂ 2 (sliceHaar R)` | operator on the full complex L² of product Haar on positive spatial links | yes, full space, not the gauge-invariant subspace. By row 667 1.6 this operator S_{A_T} equals T P = P T P = T_P on the full H (zero on H_inv^⊥), which is exactly the operator of row 698 Lemma 1.1 whose traces are partition functions |
| `transfer_apply` | kernel formula | yes |
| `transfer_positive (hβ : 0 ≤ β)` : `IsPositive` | positive for β ≥ 0 | yes; Mathlib `IsPositive` contains self-adjointness (the consumer uses `hp.isSymmetric`) |
| `transfer_ne_zero (β : ℝ)` | nonzero for every real β | yes |
| `transfer_compact (β : ℝ)` | compact for every real β | yes |
| `transfer_hs (hβ : 0 ≤ β)` : `HSNormLE (transfer β R) 1` | bound 1 at β ≥ 0 | yes, from 0 < K_R ≤ 1 (`transferKernel_pos`, `transferKernel_le_one`) and mass 1 |
| `transfer_boxSpectrum (hβ : 0 < β) (_hR : R.Valid)` | spectral package for valid boxes, β > 0 | yes; conclusion is literally that of `boxSpectrum_of_operator` (checked in row 1505 Q3) at T = transfer β R. `_hR` is unused, so the statement is stronger than claimed, never weaker |

No hidden hypothesis: the only typeclass inputs are the Borel structure on SU2 (global instance `borel SU2` in Wilson.lean), the product σ-algebras, compactness and second countability of SU2 (proved instances), and `IsProbabilityMeasure linkHaar` (proved from `haarMeasure_self`). No `Fact`, no extra measure assumption, no sorry. The positivity proof (closure of finite Gram kernels under exp, sandwich = single gauge average by left invariance and `temporal_gauge`) is kernel-checked; I read it for the statement it proves, and the two reductions it relies on (`transferKernel_eq_sandwich`, `temporal_eq_exp`) state true identities: (g·v)_e (g·u)_e^{-1} = g(x) v_e u_e^{-1} g(x)^{-1}, and Re tr(v u^*) = sum over entries of (Re u Re v + Im u Im v).

**Q2 verdict: the statements say what the receipt claims, on the full complex L² space, with no hidden hypothesis.**

## Q3. Z β a R = cyclic β R a, by hand

Definition fixed for rows 1508-1509: cyclic β R a = ∫ over u : Fin a → Slice R, under `Measure.pi (fun _ => sliceHaar R)`, of prod_{t : Fin a} transferKernel β R (u t, u (finRotate a t)).

**Claim.** For every a ≥ 1 and every box R (validity not needed; also a = 0, where both sides are 1), Z β a R = cyclic β R a.

**Proof by hand.**

1. *Reindexing.* Site (sides a R) = (k : Fin 4) → Fin (![a, R.x, R.y, R.z] k) ≅ Fin a × Vertex R by x ↦ (x 0, (x 1, x 2, x 3)). Link = Site × Fin 4 ≅ (Fin a × Vertex R) ⊔ (Fin a × Edge R): (x, 0) ↦ temporal link (t, v); (x, j+1) ↦ spatial link (t, (v, j)). Put g_t(v) := U((t,v), 0) and U(t)_(v,j) := U((t,v), j+1). Under this bijection `step x 0` = (t+1, v) with t+1 = `finRotate a t` (the same `finRotate` as in `cyclic`), and `step x (j+1)` = (t, `spatialStep v j`). The bijection is a relabelling of the coordinates of a product of copies of linkHaar, so it carries `haar (sides a R)` to (product over t of gaugeHaar R) ⊗ (product over t of sliceHaar R) (same principle as `measurePreserving_relabel` of Wilson.lean).

2. *The action.* By `action_eq_geometric`, action U = sum over sites and the six planes p.1 < p.2 of Fin 4. The planes (j+1, k+1), j < k, at site (t, v) give the spatial word u(v,j) u(v+e_j,k) u(v+e_k,j)^-1 u(v,k)^-1 of slice U(t), so their sum over v and j<k is `spatialAction (U t)`. The planes (0, j+1) at (t, v) give transport U x 0 (j+1) = U(x,0) U(step x 0, j+1) U(step x (j+1), 0)^-1 U(x, j+1)^-1 = g_t(v) U(t+1)_(v,j) g_t(v+e_j)^-1 U(t)_(v,j)^-1 = (gaugeAction R (U(t+1), g_t))_(v,j) (U(t)_(v,j))^-1. So their sum is `temporalAction (U t, gaugeAction R (U (t+1), g_t))`, term by term, with no use of trace cyclicity or inversion. Hence

   exp(-β action U) = prod_t exp(-β spatialAction(U t)) · prod_t temporal β R (U t, g_t · U(t+1)).

3. *Halves.* exp(-β S_sp(U t)) = halfWeight(U t)², and since t ↦ t+1 permutes Fin a, prod_t halfWeight(U t)² = prod_t halfWeight(U t) halfWeight(U(t+1)). (For a = 1 both sides are halfWeight(U 0)².) No gauge invariance of the spatial action is used, because the Lean kernel puts the half weight on v, not on g·v.

4. *Gauge integration.* Fubini on (gauges) × (slices) (continuous integrand on a compact space). For fixed slices the integrand is a product over t of functions of g_t alone, so the integral over prod_t gaugeHaar is the product over t of ∫ temporal(U t, g · U(t+1)) d gaugeHaar(g) (product formula for `Measure.pi`). With step 3 the t-th factor times halfWeight(U t) halfWeight(U(t+1)) is transferKernel β R (U t, U(t+1)) by the definition of `transferKernel` (`gram` times `average`). Integrating over the slices gives cyclic β R a. ∎

**Argument order.** The Lean action produces temporal(U(t), g_t·U(t+1)), the gauge acting on the later slice, and `transferKernel (u, v)` averages the gauge on its second argument v. So the factor is K_R(u t, u (t+1)) = K_R(u t, u (finRotate a t)) exactly as fixed. With the reverse order the identity would still hold, but only through pointwise symmetry K_R(u,v) = K_R(v,u) (row 667 1.4), which is not proved in Lean; the fixed order avoids it. **No off-by-one** (finRotate in the same direction on both sides; a = 1, 2 also correct as Lean objects, since Lean sums over (site, plane) pairs and never identifies coinciding geometric plaquettes), **no orientation mismatch, no measure mismatch** (all factors normalized Haar; temporal links become the gauge variables, one per vertex per time).

**Lean notes for row 1509 (not defects).** (a) The fibre types Fin (![a, R.x, R.y, R.z] (j.succ)) and Fin (![R.x, R.y, R.z] j) should agree by `Matrix.cons_val_succ`; if not definitionally in the elaborated form, a `Fin.cast` is needed in the site equivalence and must commute with `finRotate` (it does: `finRotate` is defined uniformly in n). (b) The measure step is a composition of `MeasurableEquiv.piCongrLeft`, a sum-to-product split of `Measure.pi` and a curry; I did not look up Mathlib names at the pin.

**Q3 verdict: yes, Z β a R = cyclic β R a by hand, for every a ≥ 1 and every R; the definition fixed for rows 1508-1509 has the right argument order.**

## Q4. cyclic β R a = sum of a-th powers of the positive eigenvalues, a ≥ 3

**Claim.** For β > 0, R valid and a ≥ 3, cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a, which is the right side of the weight clause of `transfer_boxSpectrum`. Row 698 Lemma 1.1 (ii) states the same with Tr T_P^k (k ≥ 2), proved there through row 667 A0(e) (trace of a product of HS integral operators as a kernel integral, via the HS equality ‖S_k‖_HS = ‖k‖_2 polarized) and A2 (iv).

**A proof by hand that uses only what the Lean unit already has, plus four listed pieces.** Write T = transfer β R, K = transferKernel β R (real, continuous, 0 < K ≤ 1), X = Slice R, μ = sliceHaar R. Let (φ_i), i in PositiveSlot T, be the orthonormal eigenvectors chosen as in `boxSpectrum_of_operator` (`nonzero_eigenblock_basis`), T φ_i = λ_i φ_i, λ_i = i.1.val > 0, the index countable and ∑ λ_i² < ∞ (both proved inside that theorem).

1. *Iterated kernels.* K_1 = K, K_{m+1}(u,w) = ∫ K(u,v) K_m(v,w) dμ(v); each K_m is continuous (parametric integral of a continuous function on a compact space, as in `Kernel.average`). For fixed w put c_w = K(·, w) ∈ C(X) ⊂ L². By `operator_apply` and induction, T^m c_w =ᵐ K_{m+1}(·, w). By Fubini on `Measure.pi` over Fin a (bounded continuous integrand), cyclic β R a = ∫ dμ(u) ∫ dμ(v) K(u,v) K_{a-1}(v,u) = ∫ dμ(u) ⟨r_u, T^{a-2} c_u⟩, with r_u = conj K(u,·) = K(u,·), so that ⟨r_u, f⟩ = ∫ K(u,v) f(v) dv.
2. *Coefficients.* ⟨r_u, φ_i⟩ = (T φ_i)(u) = λ_i φ_i(u) for μ-a.e. u (`operator_apply`). For the column, K real gives ⟨φ_i, c_w⟩ = conj ∫ K(v,w) φ_i(v) dv = conj (T* φ_i)(w) a.e. (`operator_adjoint`, `operator_apply`, adjKernel K (w,v) = K(v,w)), and T* = T (`IsPositive`), so ⟨φ_i, c_w⟩ = λ_i conj φ_i(w) a.e. w. The index is countable, so a.e. u works for all i at once. Pointwise symmetry of K is not needed.
3. *Spectral expansion.* For m ≥ 1 and every h: T^m h = ∑'_i λ_i^m ⟨φ_i, h⟩ φ_i (HasSum in L²). Reason: the eigenspaces of the compact self-adjoint T span a dense subspace (Mathlib, as sized by RECEIPT-1b), the 0-eigenspace is ker T, so h = h_0 + ∑ ⟨φ_i,h⟩ φ_i with T h_0 = 0; apply the continuous T^m. **This is where a ≥ 3 is used**: m = a - 2 ≥ 1 kills h_0. For a = 2 one needs instead r_u ⊥ ker T for a.e. u simultaneously, i.e. an uncountable family of a.e. statements; that needs separability of L²(μ) (true here, X compact metric, σ-algebra countably generated) or the HS equality of A0(e).
4. *Assembly.* ⟨r_u, T^{a-2} c_u⟩ = ∑_i λ_i^{a-2} ⟨φ_i, c_u⟩ ⟨r_u, φ_i⟩ = ∑_i λ_i^{a-2} · λ_i conj φ_i(u) · λ_i φ_i(u) = ∑_i λ_i^a |φ_i(u)|² for a.e. u. The terms are nonnegative, so by monotone convergence ∫ dμ(u) of it = ∑_i λ_i^a ‖φ_i‖² = ∑_i λ_i^a, finite since λ_i^a ≤ ‖T‖^{a-2} λ_i². ∎

**What the kernel unit of row 1506 lacks for this proof** (none is a defect of row 1506; all are row 1508 work):

- (K1) a Fubini/reindexing lemma turning ∫ over `Measure.pi` on Fin a into the iterated integral of step 1;
- (K2) a composition lemma: T applied to (a representative of) a continuous function is represented by the continuous parametric integral, iterated m times (A0(e)'s S_k S_l = S_{k∘l}, needed here only for continuous kernels);
- (K3) the spectral expansion T^m h = ∑' over PositiveSlot of λ^m ⟨φ,h⟩ φ for m ≥ 1, from the Mathlib density of eigenspaces for compact self-adjoint operators and the slot basis of `boxSpectrum_of_operator` (that basis is chosen inside a proof with `.choose`, so row 1508 must re-choose it with `nonzero_eigenblock_basis`; the power sum does not depend on the choice);
- (K4) the exchange of ∫ and ∑' for nonnegative terms (`lintegral_tsum` or `integral_tsum`).

Not needed: the HS equality, completeness of a tensor basis of L²(X×X), trace-class theory, pointwise symmetry of K, separability (for a ≥ 3).

**Remark on row 1508's scope.** Row 1508 asks for the reusable unit "for a positive compact L²-kernel operator on a probability space, a at least 2". Two cautions from the proof above. (i) At a = 2 the general unit needs separability or the HS equality (step 3); on a general probability space with non-separable L² the a = 2 case needs an extra argument (the kernel's rows lie in a separable subspace because an L² function on μ⊗μ is measurable for a countably generated sub-σ-algebra). The Wilson consumer needs only a ≥ 3 (`BoxSpectrum.weight` is fixed only for a ≥ 3). (ii) For a merely L² kernel the a-fold cyclic integrand need not be integrable a priori (it is, by an HS argument, but that is more work); the Wilson kernel is bounded and continuous, so stating the unit for bounded continuous (or bounded measurable) kernels, a ≥ 3, is enough and lighter. Recommendation: state the unit for a ≥ 3 and bounded continuous real kernels on a compact second-countable space with a Borel probability, unless a = 2 comes for free.

**Q4 verdict: yes by hand, for a ≥ 3 (also a = 2 with separability, true here). Nothing in row 1506's unit is wrong; (K1)-(K4) are missing and belong to row 1508.**

## Verdict

**FAITHFUL.** No definition or statement of row 1506 to change. Slice, sliceHaar, spatialAction, gaugeAction, temporalAction and transferKernel are the hand kernel A_T of row 667 (1a) on the unequal box of row 698 Lemma 1.1 and the K_R of RECEIPT-1b (Q1). The operator lemmas and `transfer_boxSpectrum` say what RECEIPT-1c claims on the full complex L² space with no hidden hypothesis (Q2). By hand, Z β a R = cyclic β R a for every a ≥ 1 and every R, with the argument order K_R(u t, u (t+1)) forced by the temporal plaquette orientation, no off-by-one, orientation or measure mismatch (Q3); and cyclic β R a = ∑' over PositiveSlot of λ^a for a ≥ 3 by a route that avoids the HS equality, needing (K1)-(K4) only (Q4).

Advice for rows 1508-1509, not changes to row 1506: keep the argument order of `cyclic` as fixed; state the trace unit for a ≥ 3 (a = 2 needs separability); row 1509's site equivalence may need a `Fin.cast` on the spatial fibres.

Not done: no build, no axiom print (the lead replays); Mathlib declaration names for (K1)-(K4) and for the measure reindexing were not looked up at the pin. The Lean proofs were read for the statements they prove, not re-verified; kernel checking is the lead's replay.

Credit: hand construction rows 667 and 698 (Claude Opus 5.5), spectral design row 697 (Claude Fable 5.2), Lean Stage 1b-1c (gpt-6.2-astra, rows 1504, 1506); Wilson and transfer conventions from Ethan Sussman and Levent Alpoge, with Claude and Codex (CA-I Definition 1.1 and outline GL8 at 31a47c543775, as cited by RECEIPT-1c).

Done 2026-11-25T02:41Z (date -u).

Prior check: `grep -i 'cyclic|power sum|trace identity'` in library/open-core.md gives no match; the cyclic identity is FINISH rows 1508-1509 (open) and row 698 Lemma 1.1 (ii) by hand. Nothing here is claimed new.
