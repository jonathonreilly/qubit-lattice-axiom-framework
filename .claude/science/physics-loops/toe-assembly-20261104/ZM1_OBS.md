# ZM1-OBS. Observable classes for the zoom comparison

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (ZM1_OBS_REFEREE.md); the referee's edits R1-R21 are applied, with the prior-work credits of `prior/ZM1_OBS.md`.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The choice of observable class for ZM1-I1 is the owner's; the five classes, the corrected four-test table and both rankings are proposed, and none is adopted. The edit pass ran on the laptop Codex account (`gpt-6.1-terra`, high, session `01a1b175-a231-75c2-8563-2a5991c6ca11`) after the Mac mini's account reached its limit and an earlier partial pass was discarded. The lead (Claude Opus 5.5, laptop) checked the editor's map of R1-R21 against the text; that is a text check, not a second referee. Both five-mode laws remain live. All classes and readings below are proposed comparison specifications, not adoptions. The owner has not chosen a class. No axiom or working-set entry changes.

**Proved under the displayed hypotheses.** Diagonal gauge projection; evenness and representative-site preservation; reconstruction from the full invariant two-point family; twist invisibility on the invariant algebra; the absolute-budget bound; zero-momentum and moment rigidity; conditional band-speed transfer; the sharp-grading, area and Creutz identities; and the finite-string endpoint selection rule. Numbered results below include their proofs. R-GI and its on-site consequence, invariant evenness, and the finite-register obstruction were already proved in `ZM1.md`, `RCS1.md`, and `GA2_Y2.md`, respectively. Referee closures, unrefereed: Lemma S0, Theorems 8′ and 9′, Lemma ER, Proposition A, Lemma P1, Lemma SP, Lemma C′-free, Lemmas DL and AX, Proposition T (each ZM1_OBS_REFEREE.md).

**GAP.** The draft's Theorem C(4) treats `K_φU₀` as an admissible ZM1-I1 fine update; it is a PS-1 update under NN-a but not of the stated `L5-U` form. Its several-branch lemma needs `p>0`, which every class meets. GAP b-zero is repaired by proposed rule R-b. Its proposed string budget does not yet define stationary translation-covariant axial data to which the speed theorem applies. Its flow-like claim is closed for the specified free trace-class kernels; its relative and quantum-link forms remain open. Its scaling-limit construction needs a common algebra and does not itself supply convergence of dynamics or charged sectors. Details and corrected statements appear below. These gaps do not refute the frozen sources.

**Open by name.**

None of these was attacked in this lane; each is inherited or left open by the closures above.
- **ZM1-I1[a], ZM1-I1[b], ZM1-I1[c], ZM1-I1[d], ZM1-I1[e].** Specifications, not worked, as `TOE_ASSEMBLY.md` line 227 directs. For any chosen class, Lemma ER, Theorem 7 and Theorem 11 make a counterexample the natural first attack.
- **ZM1-I1, the owner's selection**, with §4's table and the R-b, R-c, R-d and R-e repairs.
- **ZM1-OBS-twist.** Whether the five-mode law's update class should contain the matter-phase layer `∏_xe^{iφN_x}` (a PS-1 update under NN-a, Proposition T(5)), and whether `α∘γ_φ` equals the tick of a base law with other constants. The first is a law-specification choice for the owner.
- **ZM1-OBS-d-lim.** Whether the normalized (d2) amplitudes converge in the VC1 vacuum (the hypothesis of Lemma DL). By Lemma AX, convergent limits give branch data only when the charge does not move transversely.
- **The relative and quantum-link forms of (c′).** The quantum-link form needs the c-number reduction of `ZM1.md` Attack 2 (line 382).
- **ZM1-i**, with GAP e-dynamics: the tower, convergence of its updates, and its charged sectors.
- Inherited, unchanged: Z2-spatial, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5 and the rung rule (`ZM1.md` line 16); RCS-P, MT1-S[R-CS^str] and R-CS (`RCS1.md` line 18).

**Provenance.** Distilled from `ZM1_OBS_DRAFT.md`, SHA-256 `fcf9b7f24eebfa20ceaa7ce2e6fc7530198a30734a26d496f7f7037186578499`, pass 1 Claude Opus 5.5. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b135-cfce-7bd2-b8ea-e94d37b92b40` (from the run log, on the Mac mini). The draft's toy calculation and literature reports are not independently rerun or verified. They are not proof. Prior-work search and overlap: `prior/ZM1_OBS.md`. This editing session: Codex gpt-6.1-terra, effort high, codex-cli 0.165.0; session id not visible. The referee closures are unrefereed; this editing session is not an independent referee or an audit.

## Prior work in the repository

- **Finite-clock relative loop ratios.** Add this as a native worked comparison for class (b). It supplies explicit self-energy cancellation and relative errors when individual loop expectations vanish (`ref/main/docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md:544–550`: “cancels the Gaussian self terms exactly”). It would add a separate normalization option; its growing alphabet remains explicit (`same file:4`: “`N=8beta`”).

- **Local Peter–Weyl approximation.** Use its spatial tail, energy-dependent cutoff error, and boundary-sector witness when specifying class (a)’s resources. It would replace an unpriced finite-register approximation with a quantified component: “First choose `r` … then choose `R`” (`ref/main/docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). It does not identify those truncations with either five-mode register.

- **Contact versus separated limits.** Use the Haar contact construction to distinguish what separation-envelope data and overlapping smeared data retain. Its separated-smearing theorem “says nothing about overlapping smearing regions” (`ref/main/docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md:77`), while its contact variance survives (`same file:83`: “for `f=1` it is exactly1 at every `n`”).

- **Failure of absolute summability in a supplied massless comparator.** The massive-determinant/noncompact gauge note gives plaquette covariance “not absolutely summable” in its stated `d≥3` setting (`ref/main/docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:236–238`). This would qualify applications of F and S to massless gauge composites, whose hypotheses require summability (`T/ZM1_OBS_DRAFT.md:217–218`, `231`). The comparator remains `"conditional-support"` (`main note:828`) and `"unaudited"` (`ref/main/docs/audit/data/ledger/ma/massive_wilson_loop_curvature_noncompact_covariance_and_compact_defect_bounds_bounded_theorem_note_2026-09-14.json:27`).

- **YM’s existing observable interfaces.** Class (e) should be compared with H-BLOCK’s joint block/smeared state requirement, which is “not a consequence of curvature cumulant bounds” (`Y/port/p8b-limits.md:57`). This would state precisely what its weak-* compactness construction still needs to match on the YM side.

The evenness lemma is credited to `RCS1.md` Theorem 4.

## 1. Definitions inferred by the distiller

The following make the draft's conventions explicit. They are mathematical definitions, not physical axioms. Use `L5-U[m]` or `L5-O[S_+]` as in `LW1_5.md`, with quasi-local algebra `𝔄`, tick `α`, local compact gauge groups, invariant algebra `𝔄^G`, matter parity `θ`, and gauge average `E`. The tick commutes with the local gauge actions. Use the coarse counterparts with subscript 1. A block map `Φ:𝔄₁→𝔄` is the unital injective graded *-homomorphism of `ZM1.md` Definition Z. In (G1), `Φ(G_X^(1),T)=Σ_{x∈S_X}G_x^T`, where the nonempty finite sets `S_X` are pairwise disjoint. (G2) fixes the image under gauge transformations outside their union. Representative-site maps have `S_X={x_X}`. One coarse tick is `L` fine ticks.

A datum is a finite ordered tuple `d=((B₁,s₁),…,(B_n,s_n))`, with coarse observables and integer times. Define
\[
 F_0(d)=\omega_0\!\left(\prod_j\alpha^{Ls_j}(\Phi(B_j))\right),\quad
 F_1(d)=\omega_1\!\left(\prod_j\alpha_1^{s_j}(B_j)\right),\quad
 \Delta(d)=|F_0(d)-F_1(d)|.
\]
Products keep the displayed order. Extend linearly to finite combinations of tuples of the same shape. For stationary states, a truncated two-point value subtracts the product of its one-point values. A comparison class `O` comprises data, its domain and a nonnegative budget `ε_p`. The proposed `ZM1-I1[O]` asks, for the specified VC1 fine vacuum, for `L≥2`, `p≥1`, a Definition-Z map obeying (Z-a), (Z-b), (G1), (G2) and singleton sets, a coarse law of the specified form, a stationary coarse state, and constants independent of the variable data, such that the stated budget holds. Constants may depend on an explicitly quantified support radius or composite list. Every budget in §5 weakens as `p` decreases, so “there exist ... `p≥1`” is equivalent to `p=1` (referee closure, ZM1_OBS_REFEREE.md, Lemma P1). A fixed `p`, such as ZM1(a)1’s “explicit `p >= 2`” (`TOE_ASSEMBLY.md` line 281), must be stated to carry content. The original ZM1-I1 uses unit one-body profiles supported at `|θ|≤κ≤κ₀` and budget `C(κ^p+tκ^{p+1})`; its exact quantifiers are `ZM1.md` R6. Its coarse local gauge invariance is an additional hypothesis when invoked below.

For a fixed algebra and family of state/update pairs, data *determine* a property when equal data imply equal property; *cannot detect* means two allowed pairs have equal data and different property. A comparison with nonzero errors does not automatically transfer every such property continuously. The four tests ask whether a reading fixes a target, is closed, assumes physics, or adds structure. `P` means pass and `C` conditional, as in pass 1. These judgments are proposed, not owner decisions.

## 2. Gauge-invariant data

**Theorem 1 (Haar and homomorphism tools; draft Lemmas 3.1–3.2).** A continuous finite-dimensional representation of a compact group admits an invariant inner product; Haar averaging is the orthogonal projection onto invariant vectors. A unital *-homomorphism of C*-algebras is contractive and preserves exponentials of self-adjoint elements.

*Proof.* Average any inner product over Haar measure. Haar invariance makes the average of the representation idempotent and self-adjoint, with invariant range. A unital homomorphism contracts spectra; use the spectral radius for self-adjoint elements and the C*-identity for general elements. Apply the norm-convergent exponential series. □

**Theorem 2 (diagonal gauge projection; draft A, A1–A2).** Suppose `ω₀` is locally gauge invariant and the fine tick fixes the local gauge unitaries. Under (G1), for any one coarse gauge transformation `g`, simultaneously replacing every entry of a datum by `gB_jg*` leaves `F₀` unchanged. This requires neither (G2) nor singleton sets. The same holds for `F₁` when `ω₁` is locally gauge invariant. For finite-dimensional invariant entry spaces, Haar projection of their tensor product leaves the value unchanged; if the invariant tensor space is zero, the value vanishes. If both states are invariant, `Δ(d)=Δ(P_Λd)` for any finite set of coarse sites. If only the fine state is invariant, `|F₁(d)-F₁(P_Λd)|≤Δ(d)+Δ(P_Λd)`. For invariant entries, replacing a stationary coarse state by `ω₁∘E₁` preserves all data and stationarity.

*Proof.* By Theorem 1 and (G1), `Φ(g)` is the product of fine local gauge unitaries at `S_X`. Gauss generators at distinct sites commute. The tick fixes each factor, so the entire evolved product is conjugated by that product. Fine invariance removes it. Connectedness and products of exponentials extend the statement to the local group; average its tensor representation to obtain the selection rule. The discrepancy bound is the triangle inequality. The average `E₁` fixes invariant products and commutes with the tick, so the last state is stationary and locally invariant. □

In particular, one entry whose span carries a representation of the local group at `X` with no invariant vector, all other entries being invariant at `X`, gives zero. This extends the singleton charged two-point result R-GI of `ZM1.md` §5 to (G1) sets and both laws. It is a statement about simultaneous projection of the **whole tuple**, not a claim that each entry can be separately projected.

**Theorem 3 (evenness and invariant image; draft B).** On both laws `𝔄^G⊆𝔄_even`. For a representative-site map satisfying (G1)–(G2), `Φ(𝔄₁^G)⊆𝔄^G`. Gauge-commuting automorphisms preserve `𝔄^G`. In the GNS representation of a locally invariant state, `H_phys=closure(π(𝔄^G)Ω)` lies in the even subspace.

*Proof.* The first assertion is already `RCS1.md` Theorem 4. Its argument multiplies local gauge-centre actions on all sites supporting a local element: they negate each matter mode and both ends of each link, hence act as matter parity on the even link algebra. Gauge averaging and norm density extend the result. At a representative site, (G1) and Theorem 1 turn a fine gauge conjugation of `Φ(B)` into the image of the coarse conjugation; (G2) handles all remaining sites. Gauge commutation gives invariance under the update and its inverse. The invariant state implements parity in GNS and fixes `π(A)Ω` for invariant `A`. □

**Theorem 4 (reconstruction; draft D).** For a stationary, translation-invariant state, assume tick and translations preserve `𝔄^G`. The complete data `ω(A* α^t τ_β(B))`, with all `A,B∈𝔄^G` and all integer `t,β`, determine the cyclic representation of `𝔄^G` on `H_phys` and its tick and translation implementers, up to unitary equivalence. The truncated data for all local invariant `A,B` determine the unitary representation on `H_phys⊖CΩ`. Every invariant-entry datum is a matrix element in this restricted structure.

*Proof.* At `t=β=0` the untruncated values are the GNS inner products; left multiplication gives the algebra representation. The action on `π(A)Ω` determines the implementers on a dense set. The centered local vectors `π(A-ω(A))Ω` are dense in the orthogonal complement, and their evolved inner products are exactly the truncated values. Their Gram matrices define an isometry intertwining the actions, which extends to a unitary. Invariant evolved products preserve `H_phys`. □

This does not reconstruct an arbitrary representation on `H_phys^⊥`. Class (a)'s *complete exact data* include the full truncated family: for any local `A,B`, choose `β` of sup-norm 1 and include `τ_{-β}B` in a support ball of radius `R₀+1`. This does not make its uniform-in-`R₀` long-distance error estimate automatic: `C_{R₀}` may grow with `R₀`. Nor do truncated data alone determine the invariant algebra representation or its one-point values.

**Theorem 5 (twist invisibility; draft C).** In the enlarged gauge-invariant update class, append `K_φ=∏_x e^{iφQ_x}` on U, or the product of site parities on O. The corresponding automorphisms are `α_φ=α∘γ_φ` and `α_π=α∘θ`; on U, `γ_φ(c)=e^{iφ}c` and it fixes link operators. They agree with `α` on `𝔄^G`. Thus all invariant-entry data agree for every state. A locally invariant stationary state remains stationary. If `γ_φ(A)=e^{-iqφ}A`, then `α_φ^t(A)=e^{-iqφt}α^t(A)`. In the state GNS space the implementer on a charge-`q` subspace is multiplied by `e^{-iqφ}`; on O the odd subspace is multiplied by `-1`. A band so supported has the same slopes after its eigenphase is shifted by the constant. For `q≠0`, a scalar band value `V(K₀)=λ1` becomes a node exactly when `e^{iqφ}=λ`. R-CS^str finite string states are unchanged, and the covariant representation problem defined solely on `𝔄^G` is unchanged.

*Proof.* The finite product of local central gauge rotations acting on a local element sends every matter annihilator to `e^{iφ}c`; a U-link operator conserves total rishon number, so its phases cancel. This defines the infinite-volume automorphism locally. Gatewise gauge invariance makes it commute with the tick. An invariant local element is fixed by each factor, and density gives the result on `𝔄^G`. Gauge invariance of the state gives the implementing unitary, and the displayed eigenvalue follows directly. A constant local phase shift leaves derivatives of a locally chosen quasienergy branch unchanged. The string-state formula contains the state and strings, not the update; the restricted dynamics agree. □

**GAP C-law.** A layer in LZ1's enlarged class need not be a tick of the original `L5-U` or `L5-O` base form. Thus this is a counterexample to identifying charged phase origins *within the enlarged class*, conditional on a charged band, not a proof of indistinguishability between two admissible base laws. The equality of fine invariant data survives, but equivalence of the original ZM1-I1 existential statements requires closure of the admissible law and vacuum reading under the twist. R-CS^str implementers can carry an extra choice; equality of the restricted dynamics alone does not establish a unique physical phase convention. See `RCS1.md` Definition 5 and Theorem 8(c). The vacuum reading is closed under the twist. `K_φU₀` differs from the base tick composed with any GA1-P-5 member, whose gates are link-only (`GA1_5.md` line 50). Under NN-a, `K_φU` is a PS-1 update whenever `U` is (referee closure, ZM1_OBS_REFEREE.md, Proposition T). So the twist relates two PS-1 updates with the same invariant data; only one has the `L5-U` form that ZM1-I1 states.

## 3. Budgets, rigidity and speeds

**Theorem 6 (absolute-budget vacuity; draft V).** On a subset of data, if `|F_0(d)|≤s(d)` and every candidate has `|F_1(d)|≤s(d)` and `2s(d)≤Cε_p(d)`, every candidate satisfies `Δ(d)≤Cε_p(d)` there.

*Proof.* Triangle inequality. □

Thus an absolute power budget can be vacuous for faster-decaying correlators or loops; it does not follow that every absolute budget is useless. Relative budgets introduce their own domains and exact constraints.

For the next results, let `T^{(i)}_β` be unitary `Z³` translations, commuting with `U_i`, and let `v_{i,a}` be a finite list of vectors. Put `C_i(β,t)_{ab}=⟨v_{i,a},U_i^tT^{(i)}_βv_{i,b}⟩`, `c_i(θ,t)=Σ_β C_i(β,t)e^{-iθ·β}`, and `ξ_i(f)=Σ_{a,β} f_a(β)T^{(i)}_βv_{i,a}`. Here `f̂(θ)=Σ_βf(β)e^{iθ·β}`, so `‖f‖²=(2π)^{-3}∫|f̂|²`, and `c_i(θ,t)` is defined when the sum converges absolutely. In applications use centered local composites, fine time `L t`, and the induced coarse-cell translations. For charged fields omit centering. Let `N(f)=max_i‖ξ_i(f)‖`.

**Theorem 7 (Fourier form and rigidity; draft F0, F, F1–F2).** If `Σ_β‖C_i(β,0)‖<∞`, then `c_i(·,0)` is continuous and positive semidefinite and `ξ_i` extends boundedly to `ℓ²`. If the sums also converge absolutely at fixed `t`,
\[
 \langle\xi_i(f),U_i^t\xi_i(g)\rangle=(2\pi)^{-3}\int\hat f(\theta)^*c_i(\theta,t)\hat g(\theta)d\theta .
\]
If the difference of these forms is bounded by `ε(κ)‖f‖‖g‖` for profiles supported in `|θ|≤κ` and `ε(κ)→0`, then `c₀(0,t)=c₁(0,t)`. If instead at `t=0` the difference of norms is bounded by `Cκ^p N(f)^2` and `Σ_β(1+|β|)^n‖C_i(β,0)‖<∞` with integer `n<p`, the moments `Σ_β β^k C_i(β,0)` agree for every `|k|≤n`. A relative dynamical budget `C(κ^p+tκ^{p+1})N(f)N(g)` implies the first hypothesis for each fixed `t` when `p>0`.

*Proof.* Fourier inversion gives the form for finitely supported profiles. Positivity of Gram forms and Fejér approximate identities give pointwise positivity of the continuous symbol; its supremum bounds `ξ`, extending the formula. Normalized Fourier indicators of shrinking balls about zero test arbitrary matrix entries and yield equality by continuity. For the static relative bound, shrinking balls around nonzero `θ` and then setting `κ↓|θ|` gives `‖c₀-c₁‖=O(|θ|^p)`, since the symbols are bounded. Weighted summability gives `C^n` symbols. Taylor expansion along every ray forces all derivatives through order `n` to vanish; their Fourier series are the stated moments. Boundedness of `ξ_i` gives the last implication. □

For charged fields in locally invariant, coarse-cell-invariant fine and coarse states, R-GI makes every distinct-site coefficient zero. Hence the symbol is the on-site matrix and the original ZM1-I1 bound forces exact equality of on-site return amplitudes at each tick. This is already `ZM1.md` R-GI and its consequence, not a new closure. For centered invariant composites the equality is instead of **sums over all separations**, when absolutely convergent, including short distances. The digest notes a massless comparator with non-absolutely-summable plaquette covariance: `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md` in its stated conditional setting; it is unaudited. Summability must be checked, not presumed.

**Theorem 8 (one-branch speed transfer; draft S).** Suppose `Σ_β|C_i(β,0)|<∞` and, for all `t∈N₀` and all `f,g` with Fourier support in `B_{κ₀}`, the band form is `⟨ξ_i(f),U_i^tξ_i(g)⟩=(2π)^{-3}∫\bar{f̂}ĝ\,w_ie^{-itλ_i}dθ`, with continuous `w_i≥0`, `w₁(0)>0`, continuous real phases `λ_i(0)=0`, and the relative dynamical budget of Theorem 7 for `p>0`. Then `|λ₀(θ)-λ₁(θ)|=O(|θ|^{p+1})`. Directional derivatives at zero agree wherever they exist.

*Proof.* Shrinking Fourier balls and taking `κ↓s=|θ|` yields the pointwise bound `|w₀e^{-itλ₀}-w₁e^{-itλ₁}|≤C(s^p+ts^{p+1})max w_i`. At `t=0`, weights are comparable and bounded below near zero. Subtract the weight difference to obtain `|e^{-itδλ}-1|≤C'(s^p+ts^{p+1})`. For nonzero `δλ`, continuity allows `|δλ|≤π/2`; choose `t=ceil(π/(2|δλ|))`. The left side is at least `√2`. Rearranging yields `|δλ|=O(s^{p+1})`. Divide by `s` along a ray. □

**Theorem 9 (several branches; corrected draft S′).** Suppose `p>0`, `Σ_β‖C_i(β,0)‖<∞`, and, for all `t∈N₀` and all `f,g` with Fourier support in `B_{κ₀}`, the branch form is `⟨ξ_i(f),U_i^tξ_i(g)⟩=(2π)^{-3}∫f̂(θ)^*c_i(θ,t)ĝ(θ)dθ`, where in a punctured neighborhood of zero
\[
 c_i(\theta,t)=\sum_{k=1}^{n_i}W_{i,k}(\theta)e^{-it\lambda_{i,k}(\theta)},\qquad W_{i,k}\ge0,
\]
with finitely many continuous branches, phases extending continuously to zero with `λ_{i,k}(0)=0`, `‖W_{i,k}‖≥w>0`, and within each side phase gaps at least `g|θ|` modulo `2π`. Then `Σ_k‖W_{i,k}(θ)‖≤n_iΣ_β‖C_i(β,0)‖` (referee closure, ZM1_OBS_REFEREE.md, Lemma S0); write `S` for the maximum of these bounds. If the absolute band-limited form error is at most `C(κ^p+tκ^{p+1})‖f‖‖g‖`, then each branch on either side has a branch on the other within `O(|θ|^{p+1})` modulo `2π`. Along rays, existing branch-speed sets coincide. A cone `±v|θ|`, `v>0`, satisfies the gap condition with `g=2v`. The theorem applies to it only if both branches carry weights at least `w`.

*Proof.* Localized profiles give `‖c₀(θ,t)-c₁(θ,t)‖≤C(s^p+ts^{p+1})`. Average each symbol against `e^{itλ}` over `0≤t<T`, where `λ` is one selected branch. The selected contribution is its weight; each other same-side contribution has norm at most `πS/(Tgs)`, by the geometric-sum estimate. If `δ` is the circular distance to the other side's nearest phase, its averaged contribution is at most `πS/(Tδ)`. Choose `T=ceil(ηs^{-p-1})` with sufficiently small fixed `η`. The comparison error and the same-side leakage are eventually less than `w/2`, so `δ≤2πS/(wT)=O(s^{p+1})`. Exchange sides. Since `p>0`, this is smaller than the within-side gap; continuity gives a unique matching branch along a sufficiently short ray. Divide by `s`. □

**Theorem 8′ (positive weights off zero suffice).** (referee closure, ZM1_OBS_REFEREE.md) In Theorem 8, replace "`w₁(0)>0`" by "`w₁(θ)>0` for `0<|θ|<κ₀`". Then there is `s_*>0`, depending on `C`, `p`, `κ₀` and the continuity of `λ₀−λ₁` at `0`, with
\[
 |\lambda_0(\theta)-\lambda_1(\theta)|\le 8\pi C\,|\theta|^{p+1}\qquad(0<|\theta|\le s_*).
\]

*Proof.* Fix `θ₀`. As in Theorem 8's proof (relative budget, normalized profiles concentrated at `θ₀`, then `κ↓s`), for every `t∈N₀`
\[
 |w_0e^{-it\lambda_0}-w_1e^{-it\lambda_1}|\le C(s^p+ts^{p+1})\max_iw_i\qquad\text{at }\theta_0 .
\]
At `t=0` this gives `|w₀−w₁|≤Cs^p max_iw_i`. If `Cs^p≤1/2`, then `max_iw_i≤2w₁(θ₀)`. Write `δλ=λ₀(θ₀)−λ₁(θ₀)`. Since `w₁e^{−itλ₀}−w₁e^{−itλ₁}=(w₁−w₀)e^{−itλ₀}+(w₀e^{−itλ₀}−w₁e^{−itλ₁})`,
\[
 w_1|e^{-it\delta\lambda}-1|\le 2Cs^p\,w_1+2C(s^p+ts^{p+1})\,w_1\le 4C(s^p+ts^{p+1})\,w_1 .
\]
Divide by `w₁(θ₀)>0`: `|e^{−itδλ}−1|≤C₁(s^p+ts^{p+1})` with `C₁=4C`. Choose `s₁` so that `|δλ|≤π/2` for `|θ₀|≤s₁`. The draft's step (draft line 237: `t_*=⌈π/(2|δλ|)⌉`, `|e^{−iδλt_*}−1|≥√2`) gives `|δλ|≤2πC₁s^{p+1}=8πCs^{p+1}` once `C₁s^p≤1/2` and `s^{p+1}≤1/(4C₁)`. The value `w₁(0)` is never used. □

So Theorem 8 applies to composites whose weight vanishes at `θ=0`, such as a conserved density (draft line 353: "a conserved density has `c(0) = 0` and signal `O(κ^2)`").

**Theorem 9′ (relative budget, comparable weights).** (referee closure, ZM1_OBS_REFEREE.md) In Theorem 9, replace the absolute error by the relative error `C(κ^p+tκ^{p+1})N(f)N(g)`, and the weight bounds by
\[
 w\,\rho(\theta)\le\|W_{i,k}(\theta)\|,\qquad \textstyle\sum_k\|W_{i,k}(\theta)\|\le S\rho(\theta)\qquad(0<|\theta|<\kappa_0)
\]
for one function `ρ>0`. Keep `p>0`, summability and the gap condition. Then the conclusions of Theorem 9 hold, with a matching distance at most `(8πCS²/w²)|θ|^{p+1}` for small `|θ|`.

*Proof.* Use normalized profiles concentrated at `θ₀` with unit vectors `u,u′`. The relative budget gives, after `κ↓s`, `|⟨u,(c₀−c₁)(θ₀,t)u′⟩|≤C(s^p+ts^{p+1})max_i‖c_i(θ₀,0)‖`. Since `c_i(θ₀,0)=Σ_kW_{i,k}(θ₀)`, the right side is at most `CSρ(θ₀)(s^p+ts^{p+1})`. Divide every symbol and weight at `θ₀` by `ρ(θ₀)`. The rescaled data obey Theorem 9's pointwise bound with constant `CS`, and its weight bounds `w` and `S`. Theorem 9's proof works at one `θ₀` at a time (the average is over `t`), so it gives `δ≤2πS/(Tw)` with `T=⌈ηs^{−p−1}⌉`, `η=w/(4CS)`, that is `δ≤(8πCS²/w²)s^{p+1}`, with constants independent of `θ₀`. The matching along rays is unchanged. □

With `ρ≡1` the relative budget implies the absolute one used in Theorem 9, so Theorem 9′ contains it.

**GAP S′ in pass 1.** With the draft’s summability hypothesis the weight bound `S` is automatic (referee closure, ZM1_OBS_REFEREE.md, Lemma S0). Near `θ=0` all phases are small, so plain and circular distances agree. The conclusion needs `p>0`, which every class meets. Neither theorem establishes a common speed across different species. `LZ1.md` leaves that comparison open.

## 4. Loops and strings

**Theorem 10 (sharp grading; draft W1).** Let self-adjoint `E` have finite spectrum, `ω((E-n)²)=0`, and `[E,Y]=qY` with `q≠0`. Then `ω(Y)=0`. The same conclusion holds for `E²=1`, `ω((E-s)²)=0`, `s=±1`, and `EY=-YE`.

*Proof.* If `P` projects onto the `n` eigenspace, the spectral gap and the state condition give `ω(1-P)=0`. Cauchy–Schwarz gives `ω(Y)=ω(PYP)`. The commutator moves that eigenspace to a different one, so `PYP=0`. Anticommutation gives the same conclusion for the `s` eigenspace. □

On U, an oriented fundamental loop with nonzero net traversal of some link has nonzero end-number charge there. In the locked states and `ω_AB` the relevant end numbers are sharp, so such loop expectations vanish; see `RCS1.md` Theorems 7–8 for the states. In particular this holds for the simple rectangles of class (b). The draft's phrase “every closed fundamental loop” needs the traversal qualification: an immediately retraced loop has zero net end-number charge, so this proof does not make it vanish. On O, a loop traversing a link an odd number of times vanishes in a state sharp in that link's end parity. No such O witness is asserted here. This gives a counterexample to a universal nonzero area/perimeter-law assertion for simple fundamental rectangles in the U witnesses, not to any frozen result.

**Theorem 11 (loop normalizations; draft W2–W3).** For nonzero rectangular loop expectations let `w_i(R,T)=-log|ω_i(W_{R,T})|`. If `w_i=2μ_i(R+T)+c_i+o(R+T)`, then `|w₀-w₁|/(RT)→0` as `min(R,T)→∞`. If `w_i=σ_iRT+O(R+T)`, the normalized difference tends to `|σ₀-σ₁|`. For `χ=Δ_RΔ_T w`, every `f(R)+g(T)` cancels and `w=σRT+2μ(R+T)+c` gives `χ=σ`.

*Proof.* `(R+T)/(RT)≤2/min(R,T)`. The mixed finite difference kills sums of one-variable functions and sends `RT` to 1. □

`GA2_Y2.md` Theorem N already proves that an invertible operator link covariant under a group whose continuous finite-dimensional image is infinite (`GA2_Y2.md` Corollary 2.2) is impossible on a finite register. For the connected groups `U(5)` and `Spin(10)` this is every nontrivial continuous representation; for a finite image, Theorem 2.3 there gives an invertible link. Theorem 2.5 there gives the rank obstruction for the stated U and O links. Injective unital *-homomorphisms preserve spectra, so their block images remain noninvertible; nilpotent U-link entries remain nilpotent. This is an obstruction to exact Wilson-link identification, not to comparing loop expectation values through a separately specified dictionary.

**Theorem 12 (finite-string endpoint rule; draft E).** In a locally gauge-invariant state and for gauge-commuting dynamics, take the straight R-CS^str strings `B_{r,b}(x)` of `RCS1.md` §5, with far endpoint `y=x+2re`. In any ordered product containing once an evolved adjoint of one string and once an evolved second string, plus arbitrary evolved gauge-invariant elements, the expectation is zero when their far endpoints differ. When the endpoints agree, the matrix in the two free indices is a scalar multiple of `δ_{bb'}`.

*Proof.* A string is invariant at its starting and interior sites and transforms irreducibly in the fundamental or vector representation at its far endpoint. Gauge covariance preserves these transformation laws under time evolution. If endpoints differ, average at one endpoint; a single nontrivial irreducible representation has no invariant vector. At a common endpoint, Schur's lemma makes the invariant two-index tensor proportional to the identity. □

For parallel strings with a common far endpoint, their starting points lie on the same axis line. Thus these particular finite-string amplitudes have no transverse displacement data. This is a data-level companion, not a replacement, for `RCS1.md` Corollary 9, which proves transverse flatness in limit sectors under additional disjointness and tick-equivalence hypotheses. Locked-state string denominators vanish (`RCS1.md` Theorem 7); `ω_AB` has positive open-string denominators and the conditional flatness results of Theorem 8. The endpoint rule alone does not establish a dispersion relation or rule out all other charged observables.

## 5. Proposed classes and checks

The following are five proposed readings. They do not assert existence. `P/C` records the draft's four tests in the order target, closedness, physics by premise, added structure. The qualifications below are part of the check. The fine vacuum in the U statement is a VC1 vacuum; the O analogue is a separate proposed comparison.

### 5.1 (a): local invariant, separation envelope

For every support radius `R₀`, let `A,B` be invariant norm-at-most-one coarse observables supported in the ball of radius `R₀` about the origin. Include their cell-group images and truncated two-point values at all ticks and all cell separations `r=|β|∞≥1`. Define, for each fixed `A,B`,
\[
 M(r,t)=\sup_{|\beta'|_\infty\ge r}\max_i |F_i^T(A^*,\tau_{\beta'}B;t)|,\quad
 |F_0^T-F_1^T|\le C_{R_0}(r^{-p}+tr^{-p-1})M(r,t).
\]
A zero envelope forces both values zero. `ZM1-I1[a]` is the existence statement of §1 with this bound for all these data, with fixed `p≥1` and constants `C_{R₀}`. Theorem 2 permits a gauge-invariant coarse state. No one-point matching is separately imposed.

Exact complete data determine the centered physical-sector tick/translation representation by Theorem 4 and the translation-of-support observation following it. The specified *rate* compares separated tails for fixed local observables; it does not by itself prove speed transfer. It excludes odd field entries and does not reconstruct `H_phys^⊥`. Theorem 5 gives conditional twist invisibility. R-GI does not remove any invariant entry. Theorem N does not forbid these quantum-link observables. Even the general free separated-observable comparison remains Z2-spatial, `ZM1.md` §0. This class could serve as an operator-side correlator interface for GA2 and T0-start, but composition with a continuum comparison requires a common dictionary and propagated errors, not merely matching names. It offers LZ1-i physical-sector correlation data, not a proved speed equality.

**Four tests: P P P P, proposed.** No target value is fixed; all finite radii are quantified; no charged-sector or continuum result is assumed; and the envelope avoids the specific vacuity in Theorem 6. The envelope is an additional chosen normalization and can be dominated by a large distant outlier. Thus test 4 is a judgment, not a theorem that no extra structure was introduced. The bound forces `|m₀(r)−m₁(r)|≤C_{R₀}(r^{-p}+tr^{-p-1})max_im_i(r)` for the tail envelopes `m_i(r)=sup_{|β|_∞≥r}|F_i^T|`, hence exact asymptotic equality of every invariant channel’s correlation length and tail amplitude (referee closure, ZM1_OBS_REFEREE.md, Lemma ER), when the relevant asymptotic forms exist. `GA2_Y2.md`'s SC fixes state, scale, list, Wilson-function dictionary, normalization and tolerance; it is a diagnostic, not GA2. The finite-region Peter–Weyl approximation in `docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md` is conditional and unaudited, retains boundary sectors, and does not identify its registers with either five-mode law.

### 5.2 (b): (a) plus spatial loops

Add static traces of quantum-link products around every coordinate-plane `R×T` rectangle and cell-group images; on U also include `W_C*W_C`. Put `w_i=-log|ω_i(W_C)|` when nonzero. Offer three alternative budgets, for `p≥1`:
\[
 \text{(b-P)}\ |w_0-w_1|\le C|C|^{1-p},\quad
 \text{(b-A)}\ |w_0-w_1|\le CRT\min(R,T)^{-p},\quad
 \text{(b-Cr)}\ |\chi_0-\chi_1|\le C\min(R,T)^{-p}.
\]
`ZM1-I1[b]` adds one chosen loop budget to (a). **Rule R-b** (proposed repair, ZM1_OBS_REFEREE.md; not adopted). In this subsection `Γ` denotes a rectangle and `C` a constant. Let `Γ` range over coordinate-plane rectangles with sides `R,T≥1`, in every position, with their cell-group images. Let `Y` range over `W_Γ` on both laws and, on `L5-U`, also `W_Γ^*W_Γ`. Write `F_0(Y)=ω₀(Φ(Y))` and `F_1(Y)=ω₁(Y)`.
- (z) `F_0(Y)=0` if and only if `F_1(Y)=0`. A violation fails the bound.
- Where both values are nonzero, put `w_i(Y)=−log|F_i(Y)|`. Budgets (b-P) and (b-A) apply to every such `Y`.
- (b-Cr): for `Γ` with `R,T≥2`, let `Γ′,Γ″,Γ‴` share the corner of `Γ` with least coordinates and have sides `(R−1,T−1)`, `(R,T−1)`, `(R−1,T)`. If the four values of the same type (`W` or `W^*W`) are nonzero, put `χ_i(Γ)=w_i(Γ)+w_i(Γ′)−w_i(Γ″)−w_i(Γ‴)` and impose `|χ_0(Γ)−χ_1(Γ)|≤C min(R,T)^{-p}`. If one of the four vanishes, (z) already compares the zero pattern and no `χ` comparison is made.

The per-position definition matters because `ω₁` need not be translation invariant. GAP b-zero is repaired by this proposed rule.

Theorem 11 gives the stated area and perimeter distinctions and cancellation of additive perimeter/corner terms, conditional on the asymptotic expansions and nonzero expectations. It does not prove a law exists. Theorem 10 gives simple-rectangle vanishing in the U witnesses, and Theorem N prevents exact Wilson-link identification. Quantum-link loop magnitudes may exceed one; their logarithms need not be positive. GA2's weak-coupling window and an infrared string tension are different questions. Spatial loops alone supply no charged-sector speed. A conditional, unaudited finite-clock example of relative loop comparison with a growing alphabet appears in `docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md`; its ratio cancels self terms, but it is not a five-mode comparison. Existing Creutz diagnostics are in `docs/CONFINEMENT_STRING_TENSION_NOTE.md` and are bounded qualitative support.

**Four tests, proposed:** (b-P) P C P C; (b-A) P C P P; (b-Cr) P C P P. With rule R-b, test 2 passes for all three. (b-A) and (b-Cr) compare only `σ` (Theorem 11) and assume no value of it; in perimeter-law vacua they add no loop content beyond (a). Closedness is conditional on the family, blind products and zero convention. At `p=1` the area and Creutz forms discard perimeter distinctions; at a fixed `p>1` the area form compares them and gets (b-P)’s test-4 C (referee closure, ZM1_OBS_REFEREE.md, Proposition A); the perimeter form compares a potentially UV-sensitive coefficient. Creutz cancellation is algebraic, not a guarantee of a meaningful continuum observable.

### 5.3 (c): band-limited invariant composites

Fix a finite local invariant list `O_a`, either fixed by the owner now or quantified universally over every finite list with list-dependent constants. Require the coarse state to be invariant under coarse cell translations. Use the centered vectors of §3 and profiles `f,g∈ℓ¹(Z³)^d` with Fourier support `|θ|≤κ≤κ₀`, and all `t∈N₀`; the smearing series converges in norm by Lemma SP. No summability domain is imposed on the states (proposed repair, ZM1_OBS_REFEREE.md; not adopted). Compare with
\[
 |\langle\xi_0(f),U_0^t\xi_0(g)\rangle-\langle\xi_1(f),U_1^t\xi_1(g)\rangle|
 \le C(\kappa^p+t\kappa^{p+1})N(f)N(g).
\]
`ZM1-I1[c]` asks for this comparison with the §1 maps and laws. The list, profiles and constants must be specified before using the reading. The smearing denotes a GNS vector, not automatically a bounded element of the quasi-local algebra. Theorem 7 applies where its summability hypotheses hold.

**Lemma SP (summable profiles).** (referee closure, ZM1_OBS_REFEREE.md) Let `T` be a unitary representation of `Z³` on `H`, let `U` commute with it, and let `v₁,…,v_d∈H`. For `f∈ℓ¹(Z³)^d` put `ξ(f)=Σ_{a,β}f_a(β)T_βv_a`.
1. The series converges in norm, and `‖ξ(f)‖≤‖f‖₁max_a‖v_a‖`.
2. If `f̂` is `C⁴` on `T³`, then `f∈ℓ¹`.
3. If `Σ_β‖C(β,0)‖<∞`, then `ξ` agrees on `ℓ¹` with Theorem 7's bounded extension.
4. Let `ρ` be smooth, supported in the unit ball, with `∫|ρ|²=1`. For unit `u` put `f̂_δ(θ)=(2π)^{3/2}δ^{-3/2}ρ((θ−θ₀)/δ)u`, and define `g_δ` from `u′` in the same way. Then `‖f_δ‖=1`, `f_δ∈ℓ¹`, and for every density `c(θ,t)` that represents the form `⟨ξ(f),U^tξ(g)⟩` and is continuous at `θ₀`, `⟨ξ(f_δ),U^tξ(g_δ)⟩→⟨u,c(θ₀,t)u′⟩` as `δ→0`.

*Proof.* (1) `‖T_βv_a‖=‖v_a‖`. (2) `f(β)=(2π)^{-3}∫f̂(θ)e^{−iθ·β}dθ`; four integrations by parts in the coordinate with the largest `|β_j|` give `|f(β)|≤C(1+|β|)^{-4}`, which is summable on `Z³`. (3) `ℓ¹⊂ℓ²`; both maps are bounded and agree on finitely supported `f`. (4) Parseval gives `‖f_δ‖²=∫|ρ|²=1`; (2) gives `f_δ∈ℓ¹`; the form equals `∫|ρ(y)|²⟨u,c(θ₀+δy,t)u′⟩dy`, which converges by continuity at `θ₀`. □

The proofs of Theorems 7-9, 8′ and 9′ use normalized profiles only through the limits in (4). So they hold verbatim with smooth profiles in `ℓ¹`.

Theorem 7 imposes exact zero-momentum correlation sums wherever the time-`t` sums also converge, and static moment equalities under its stronger hypotheses. Theorems 8–9 transfer speeds only for the stated isolated, weighted bands and corresponding error form. For multiple branches Theorem 9 uses an absolute norm bound; a relative bound implies it under bounded `ξ`. By Theorems 8′ and 9′ this includes species whose composite weight vanishes at zero momentum, provided it is positive off zero, or comparable across branches. This can supply LZ1-i for visible even species, not a fermion or interspecies common speed. GA2 and T0-rate need an independently fixed operator-to-continuum dictionary and rates. Gauge-invariant composite data do not access arbitrary `H_phys^⊥` or fix the charged phase in Theorem 5's enlarged family.

**Proposed (c′), flow-like variant.** Replace local composites by bilocals `Σ_{x,y}K(x,y)ψ_x* T_{x→y}ψ_y`, with specified paths, kernels, convergence and transformation laws. It is an analogy to smoothing, not Wilson flow on group-valued links. **GAP c′:** the draft's inference from ZM1's free band-limited elementary-field estimates to arbitrary such smoothed bilocals requires constituent momentum support, normalization, uniformity and a truncation argument; no such proof is supplied in the draft. For trace-class kernels with Fourier support in `|θ|≤κ` in both variables, the free comparison holds with absolute error `8β(t)‖K‖₁‖K′‖₁`, so `p=2` (referee closure, ZM1_OBS_REFEREE.md, Lemma C′-free). The relative form of the (c) budget is not proved for bilocals. `ZM1.md` proves a narrower free `p=2` comparison and does not transfer it to interacting quantum links. The no-invertible-link theorem does not exclude every possible quantum-link flow. Flowed continuum observables are context, not an established identification.

**Four tests: P C P C, proposed.** With R-c, closedness passes if the list is fixed now or quantified universally; as written before the repair, the list, profiles, summability domain and range needed fixing. Rigidity forces exact short-distance-inclusive sums, and (c′) adds kernels and paths; neither is implied by a long-distance comparison.

### 5.4 (d): (a) plus R-CS^str data

Fix an axis `e` and coarse strings `S_b=B^{(1)}_{n,b}(X)`. Let `Φ₀=Φ`, `Φ₁=id`, `α₀=α^L`, and `N_i(X,n)=Σ_bω_i(Φ_i(S_b)*Φ_i(S_b))`. The coarse state is invariant under coarse cell translation along `e`. For every coarse site `X` and `n≥n₀`, require `N₀(X,n)=0` iff `N₁(X,n)=0`; compare (d1) and (d2) where both are positive (proposed repair, ZM1_OBS_REFEREE.md; not adopted). Add:

- (d1) normalized string-state truncated invariant correlators `Σ_bω_i(Φ_i(S_b)*Φ_i(A)*α_i^t(Φ_i(τ_βB))Φ_i(S_b))/N_i`, with the corresponding one-point products subtracted; use (a)'s envelope uniformly in `n`.
- (d2) normalized same-far-end amplitudes `Σ_bω_i(Φ_i(B_{n,b}(X))*α_i^t(Φ_i(B_{n-j,b}(X+2je))))/[N_i(X,n)N_i(X+2je,n-j)]^{1/2}`.

Require the normalized (d2) amplitudes to converge for each displacement and tick as `n→∞`, yielding `A₀,A₁` of Lemma DL, and impose the axial band-limited relative budget of the form in (c) on those limits (proposed repair, ZM1_OBS_REFEREE.md; not adopted). It uses the proposed odd label `χ_tot` over parity-sharp backgrounds. `ZM1-I1[d]` adds these requirements to (a).

**GAP d-domain and speed.** At finite `n`, allowed `j` is constrained by the string lengths, and the normalized kernel depends on `X,n,j`; a stationary positive-definite `Z`-translation kernel with a common GNS representation, a limit, and the Fourier-domain budget have not been constructed. Therefore Theorems 8–9 cannot yet be applied to (d2). The corrected conditional claim is axial speed transfer *if* a specified limiting translation-covariant kernel satisfies all hypotheses of either theorem. The endpoint rule only says that the displayed common-end family has no transverse amplitudes. It does not prove all transverse physics absent. Locked states have no positive string denominators; in `ω_AB`, RCS1 proves the stated positive open-string and transverse-flatness results. If the normalized (d2) amplitudes converge as the string length grows, for every displacement and tick, the limits form a positive-definite function on `Z²` with a covariant cyclic representation (referee closure, ZM1_OBS_REFEREE.md, Lemma DL). Theorems 8-9 then apply under their remaining hypotheses. Those hypotheses fail when the charge propagates in three dimensions: in the free massless walk the on-axis amplitude, for some residue, has no finite branch form at any small axial momentum (Lemma AX). The corresponding interacting conclusion requires Lemma AX’s stated hypotheses. The string-sector tick phase is not fixed by invariant dynamics alone (Theorem 5). GA2/T0 need additional bridges; this charged prescription supplies neither by itself.

**Four tests: P C C C, proposed.** The axis, domain, limits and odd label need specification. R-CS^str is a working candidate whose adoption awaits RCS-P and MT1-S; the axis selects the data being tested.

### 5.5 (e): tower and scaling limits

Take block maps `Φ_k:𝔄_k→𝔄` of factor `2^k` (Definition Z with (Z-a), (Z-b), (G1)-(G2) and singleton sets), each a composite `Φ_k=ι₁∘⋯∘ι_k` of one-step maps `ι_j:𝔄_j→𝔄_{j−1}`, with coarse laws `α_k` and `α_k`-invariant states `ω_k` (draft line 398) (proposed repair, ZM1_OBS_REFEREE.md; not adopted). Require the (a) bound at every level with one `p` and constants independent of `k`; this is the proposed `ZM1-I1[e]`, a tower requirement rather than only one step. If all `𝔄_k` are identified with one fixed separable unital algebra `𝔄_*`, record weak-* limit points of `ω₀∘Φ_k` restricted to `𝔄_*^G`. Compactness gives subsequential limit points. If band-limited data are additionally supplied at every level with the hypotheses of Theorems 8–9, their speed conclusions apply pairwise at those levels.

*Proof of compactness.* The state space of a separable unital C*-algebra is weak-* compact and metrizable; any sequence has a convergent subsequence. The invariant algebra is separable as a closed subspace. □

**GAP e-dynamics.** Compactness of pulled-back states alone gives neither a compatible tower, convergence of updates, uniqueness of limit, nor a charged sector. Reading charged structure from a limit is proposed and needs a separate construction. A weak-* state on `𝔄_*^G` is not automatically the full scaling algebra of the cited literature. The YM H-BLOCK interface also requires a joint block/smeared state, not just separate curvature bounds (`prior/ZM1_OBS.md`, YM library `port/p8b-limits.md`). T0-start and T0-rate still need their specified topology, uniform estimates and dictionary.

**Four tests: C P P P, proposed.** The tower moves the target beyond a single interacting step; the fixed sequence and uniform constants specify the remaining data. This pass does not prove the tower exists.

## 6. Ranking, dependencies and checks

Pass 1’s criteria, in order, are content in VC1 vacua, well-posedness on finite quantum links, the four tests, fit to ZM1-I1 as one interacting step, and downstream supply. Pass 1's proposed ranking is **(a), (c), (e), (d), (b)**. It favors a one-step invariant comparison, then spectral access, while counting the tower requirement, axis choice and loop zero/normalization issues as costs. The stated criteria do not determine this order (ZM1_OBS_REFEREE.md §4.3). Under the weighting “prefer the least demanding class whose added data a named consumer uses”, the corrected verdicts give (a), (c), (e), (b), (d). The order is a judgment, not an owner selection. (a) is included in (b) and (d); (e) repeats it along a tower; (c) uses a different budget. Combinations are possible.

The four-test outcomes above incorporate the referee’s correction and the proposed repairs; the full comparison follows. In particular, its P for (a)'s fourth test is conditional in substance on accepting the envelope; its P for (e)'s closedness holds for ZM1-I1[e], which quantifies the tower existentially; the common algebra enters only the optional limit-point clause. No proposed reading is promoted to a working-set axiom.

`GA1_5.md` line 50 (GA1-P-5’s gates are link-only), `VC1_5.md` line 29 (readings E and P) and `TOE_ASSEMBLY.md` line 235 (NN-a) bear on the twist (Proposition T).

**Corrected four-test table** (proposed; not adopted). Line references in this imported table refer to the pass-2 text identified in the referee report; section references are to that report:

| Class | Passes 1-2 | Referee, as written | Referee, after the repairs | Reasons for the referee verdicts |
|---|---|---|---|---|
| (a) | P P P P | P P P P | P P P P | (1) No target, no existence, no fixed `p`. (2) Every support radius is quantified, and the constants `C_{R₀}` are existential. (3) Dropping charged data settles nothing: in locally gauge-invariant vacua charged two-point data are on-site (Theorem 2 and the paragraph on line 75), and (a) asserts no MT1-S or GA2 conclusion. (4) The relative form is needed by Theorem 6 and the vanishing rate by ZM1(a)1. Lemma ER shows what the envelope then forces, exact tail matching, which is long-distance content. Test 4 stays a judgment, as line 126 says. |
| (b-P) | P C P C | P C P C | P P P C | (2) Rule R-b assigns every zero case. (4) It demands equality of the perimeter coefficient, a local self-energy quantity that a long-distance comparison does not need; the draft's item 23 is context for this, not a premise. |
| (b-A) | P C C P | P C P P | P P P P at `p=1`; P P P C at a fixed `p>1` | (3) As for (b-Cr): the form compares `σ` and assumes no value of it. Blindness to the perimeter coefficient leaves a question open; it does not settle it. If the owner keeps pass 1's stricter reading of test 3, then (b-A) and (b-Cr) both get C. (2) Rule R-b. At a fixed `p>1` the form compares perimeter coefficients (Proposition A) and gets (b-P)'s test-4 C. By Lemma P1 the existential statement is the `p=1` case. |
| (b-Cr) | P C P P | P C P P | P P P P | (2) Rule R-b. (3) As for (b-A). (4) Theorem 11's cancellation is what the form is for. |
| (c) | P C P C | P C P C | P P P C, if the list is fixed now or quantified universally | (2) As written, the list, the profiles and the summability domain are open, and the domain depends on the candidate (§3.4). R-c fixes the profiles and removes the domain. (4) Theorem 7 forces exact zero-momentum sums, contact terms included, which speed transfer does not need. |
| (d) | P C C C | P C C C | P C C C | (2) The axis, the limits and the odd label beyond parity-sharp backgrounds need fixing, and (d2) either presumes the limits of Lemma DL or lapses (§3.6). (3) It builds the working candidate R-CS^str into ZM1-I1 before RCS-P and MT1-S settle (`TOE_ASSEMBLY.md` line 225). (4) The axis decides which motion the data can show (Theorem 12). R-d adds only what the data need, so it changes no verdict. |
| (e) | C P P P | C P P P | C P P P | (1) It moves ZM1-I1 from one interacting step to ZM1(a)1 along the tower. (2) ZM1-I1[e] quantifies the tower existentially, so it is closed once each `Φ_k` is a Definition-Z map as §1 requires (R-e makes this explicit). The limit-point clause is a use of the class, not part of its statement. |

Prior work: `ZM1.md` already proves the original R-GI on-site consequence and the narrower free `p=2` result; `RCS1.md` already proves invariant evenness, locked denominator vanishing and conditional string-sector flatness; `GA2_Y2.md` already proves Theorem N and the finite-list diagnostic limitations. `prior/ZM1_OBS.md` records the repository search, supporting notes, limitations and paths. The supplied weak-window note `docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md` distinguishes separated and contact observables in a conditional, unaudited comparator; it does not prove either limit here. Literature cited in pass 1, including operator-algebraic scaling limits and gradient flow, remains context and was not independently checked in this pass.

The pass-1 floating-point toy check reported a two-site U(1) model: separated charged correlation zero, invariant correlator change at most `4.6×10⁻¹⁵` under a twist, and on-site phase agreement to `1.2×10⁻¹⁵`. It is reported in `ZM1_OBS_DRAFT.md` §7; it was not rerun and proves no general statement. No new numerical or independent referee check is claimed.


## Appendix: referee closures and proofs

These closures are unrefereed. References to lines of ZM1_OBS.md in the imported proofs refer to the pass-2 text identified in the referee report.

**Lemma S0 (the bound `S` is automatic).** (referee closure, ZM1_OBS_REFEREE.md) Assume the hypotheses of Theorem 9 together with `Σ_β‖C_i(β,0)‖<∞`, as the draft's Lemma S′ does (draft line 239). Then for `0<|θ|<κ₀`,
\[
 \|W_{i,k}(\theta)\|\le\|c_i(\theta,0)\|\le\textstyle\sum_\beta\|C_i(\beta,0)\| ,
\]
so `S:=max_i sup_θΣ_k‖W_{i,k}(θ)‖≤max_i n_iΣ_β‖C_i(β,0)‖<∞`.

*Proof.* At `t=0` the branch form gives `c_i(θ,0)=Σ_kW_{i,k}(θ)`. If the hypothesis is stated as a form identity for profiles with Fourier support in `B_{κ₀}` (the draft's wording), the same pointwise identity follows from Theorem 7's proof: normalized profiles concentrated at `θ` and continuity of both densities at `θ≠0`. Each `W_{i,k}(θ)` is positive semidefinite, so `0≤W_{i,k}(θ)≤c_i(θ,0)`, and the operator norm is monotone on positive semidefinite matrices. The last inequality bounds an absolutely convergent Fourier series. □

**Lemma ER.** (referee closure, ZM1_OBS_REFEREE.md) Fix `A,B∈𝔄₁^G(R₀)` and `t∈N`. Put `m_i(r)=sup_{|β|_∞≥r}|F_i^T(A^*,τ_βB;t)|`, so that `M(r,t)=max_im_i(r)`, and `ε(r)=C_{R₀}(r^{-p}+tr^{-p-1})`. If (a)'s bound (line 120) holds, then for every `r≥1`
\[
 |m_0(r)-m_1(r)|\le\varepsilon(r)\,M(r,t).
\]
So if `ε(r)<1` and `M(r,t)>0`, both `m_i(r)>0` and `m_0(r)/m_1(r)∈[1−ε(r),(1−ε(r))^{-1}]`.

*Proof.* Let `|β|_∞=r′≥r`. Then `r′^{-p}+tr′^{-p-1}≤r^{-p}+tr^{-p-1}` and `M(r′,t)≤M(r,t)`, so the bound at `β` gives `|F_0^T(β)|≤|F_1^T(β)|+ε(r)M(r,t)≤m_1(r)+ε(r)M(r,t)`. Take the supremum over `β`, then exchange the sides. The ratio bounds follow from the two one-sided inequalities. □

*Consequence.* At every fixed tick the tail envelopes of the two sides agree to relative order `r^{-p}`. If `m_i(r)=a_ie^{−r/ξ_i}(1+o(1))` with `a_i>0`, then `ξ₀=ξ₁` and `a₀=a₁`. If `m_i(r)=a_ir^{−η_i}(1+o(1))`, then `η₀=η₁` and `a₀=a₁`. Definition Z compares `Φ(A)` with `A` directly (`ZM1.md` line 56, "the **correlation error**"), so no renormalization factor can absorb a difference of amplitudes. So ZM1-I1[a] asks a coarse law of the `L5-U` form to reproduce, in coarse units, every invariant channel's correlation length and tail amplitude exactly. This is long-distance content, and it is what the vanishing rate of `ZM1(a)1` asks; it does not change (a)'s test 4. It is a strong demand on a law with finitely many constants. The (c) budget, through Theorem 7, and the (b-Cr) budget, through Theorem 11, force exact equalities of the same kind. So for any chosen class, a counterexample is the natural first attack on ZM1-I1[O].

**Proposition A (the area form at fixed `p>1`).** (referee closure, ZM1_OBS_REFEREE.md) Let `w_i(R,T)=2μ_i(R+T)+c_i+o(R+T)` with `μ₀≠μ₁`. For every `p>1` and every constant `C`, (b-A) fails on the squares `R=T=n` for all large `n`.

*Proof.* `|w₀−w₁|=4|μ₀−μ₁|n+O(1)+o(n)`, while `C·RT·min(R,T)^{-p}=Cn^{2−p}=o(n)`. □

At `p=1` the right side is `C·max(R,T)`, while `|w₀−w₁|≤4|μ₀−μ₁|max(R,T)+O(1)+o(R+T)`. So (b-A) holds for a large enough `C`, and the area form is blind to perimeter coefficients at `p=1` only. At a fixed `p>1` it compares them, like (b-P).

**Lemma P1 (the existential exponent is `p=1`).** (referee closure, ZM1_OBS_REFEREE.md) In the ranges `r≥1`, perimeter `|Γ|≥1`, `min(R,T)≥1` and `0<κ≤1`, every budget of `ZM1_OBS.md` §5 is nonincreasing in `p`. So a candidate that meets a budget with some `p≥1` (and some `κ₀` in (c) and (d2)) meets it with `p=1` and `κ₀′=min(κ₀,1)`, with the same constants. Hence every ZM1-I1[O] that reads "there exist ... `p≥1`" is equivalent to its `p=1` case.

*Proof.* In these ranges `r^{-p}≤r^{-1}`, `tr^{-p-1}≤tr^{-2}`, `|Γ|^{1-p}≤1`, `min(R,T)^{-p}≤min(R,T)^{-1}`, `κ^p≤κ` and `tκ^{p+1}≤tκ²`. □

The original ZM1-I1 (`ZM1.md` line 361) has the same form. So the rate exponent carries content only if the owner fixes it. `TOE_ASSEMBLY.md` line 281 asks `ZM1(a)1` for "an explicit `p >= 2`". In the existential reading, Theorem 7's moment clause reduces to `n=0`, which its first clause already gives, and Proposition A does not apply.

**Lemma C′-free.** (referee closure, ZM1_OBS_REFEREE.md) Assume the hypotheses of `ZM1.md` Theorem Z2 (line 240: `F=1` or `5`, `0<ε<π/2`, `μ=0`, `L≥2`), with `Φ=Γ(J̃_L)`, fine sea `P`, coarse sea `P_c` and the free walk as coarse law. Let `0<κ≤√v/2`, `t∈N` and `β(t)=(3.5/v+2.66)κ²+1.5tκ³`. Let `K,K′` be trace-class operators on the coarse one-body space with `K=P_κKP_κ` and `K′=P_κK′P_κ`, where `P_κ` projects onto momentum support `|θ|≤κ`. For a singular value decomposition `K=Σ_nσ_n|w_n⟩⟨u_n|` put `B_K=Σ_nσ_nc₁^†(w_n)c₁(u_n)`, the coarse bilinear `Σ_{X,Y}K_{XY}c₁^†_Xc_{1,Y}`. Then `B_K` converges in norm, and
\[
 \big|\omega_P\big(\Phi(B_K)^*\alpha^{Lt}(\Phi(B_{K'}))\big)-\omega_{P_c}\big(B_K^*\alpha_1^{t}(B_{K'})\big)\big|\le 6\,\beta(t)\,\|K\|_1\|K'\|_1 .
\]
The truncated values differ by at most `8β(t)‖K‖₁‖K′‖₁`.

*Proof.* For `σ_n>0`, `u_n` and `w_n` lie in `ran P_κ`, because `K^*K` and `KK^*` have their ranges there. For unit vectors `‖c^†(w)c(u)‖≤1`, so both series converge in norm, with norms at most `‖K‖₁` and `‖K′‖₁`. Expand both expectations in the two decompositions. By `Φ(c₁(h))=c(J̃h)` and `α^{Ls}(c(h))=c(V^{-Ls}h)` (`ZM1.md` line 279), a fine term is
\[
 \omega_P\big(c^\dagger(\tilde Ju)\,c(\tilde Jw)\,c^\dagger(V^{-Lt}\tilde Jw')\,c(V^{-Lt}\tilde Ju')\big),
\]
and the coarse term drops `J̃` and has `V^{-t}`. The CAR give `c(a)c^†(b)=⟨a,b⟩−c^†(b)c(a)`. So each term is a scalar `⟨J̃w,V^{-Lt}J̃w′⟩` times a normally ordered two-point function, minus a normally ordered four-point function.
1. The scalars differ by at most `2.66κ²+1.5tκ³≤β(t)`. Indeed `J̃^*J̃=1` gives `⟨J̃w,V^{-Lt}J̃w′⟩−⟨w,V^{-t}w′⟩=−⟨J̃w,V^{-Lt}(V^{Lt}J̃−J̃V^t)V^{-t}w′⟩`, and Theorem Z2(3) (line 243) applies to `V^{-t}w′`, which has the same momentum support.
2. The two-point functions differ by at most `β(t)`, and the four-point functions by at most `4β(t)`. These are the cases `n=1` and `n=2` of the normally ordered bound `n^{(n+2)/2}β` (`ZM1.md` line 277), with times in `{0,t}`. Reordering the annihilators changes both sides by the same sign.

Every scalar and every function has modulus at most `1`, so a term differs by at most `β+β+4β=6β(t)`. Sum with weights `σ_nσ′_m`. For the truncation, each one-point value differs by at most `β(0)‖K‖₁` (the case `n=1` at `T=0`) and has modulus at most `‖K‖₁`, so the products differ by at most `2β(0)‖K‖₁‖K′‖₁≤2β(t)‖K‖₁‖K′‖₁`. □

So with c-number links the bilocals of (c′) obey `p=2` for times `t≤1/κ`, in an absolute trace-norm budget. The relative form of line 149 is not proved for them. The quantum-link form needs the c-number reduction that `ZM1.md` Attack 2 (line 382) does not supply.

**Lemma DL (limit amplitudes).** (referee closure, ZM1_OBS_REFEREE.md) Fix `i∈{0,1}`, an axis `e` and a coarse site `X`. Write `Φ₀=Φ`, `Φ₁=id`, `U_{(0)}=Ũ^L` and `U_{(1)}=Ũ₁`. Let `ω_i` be locally gauge invariant, stationary, and invariant under the coarse cell translation along `e` (for `i=0`, its fine lift). Write `B_n(Y)=B^{(1)}_{n,1}(Y)` for the coarse straight string with `2n` links from `Y` along `e`; its far end is `Y+2ne`. Assume `‖π_i(Φ_i(B_n(Y)))Ω_i‖>0` for all `Y∈X+2Ze` and `n≥n₀`. For `k<n−n₀` put
\[
 u^{(n)}_k=\frac{\pi_i(\Phi_i(B_{n-k}(X+2ke)))\Omega_i}{\|\pi_i(\Phi_i(B_{n-k}(X+2ke)))\Omega_i\|},\qquad a_n(k,t)=\langle u^{(n)}_0,\,U_{(i)}^t\,u^{(n)}_k\rangle .
\]
1. `a_n(k,t)` is the normalized (d2) amplitude of line 164 at string length `n` and displacement `k`.
2. `⟨U_{(i)}^su^{(n)}_j,U_{(i)}^tu^{(n)}_{j′}⟩=a_{n−j}(j′−j,t−s)`.
3. If `A(k,t)=lim_{n→∞}a_n(k,t)` exists for every `(k,t)∈Z²`, then `A` is a positive-definite function on `Z²` with `A(0,0)=1`.
4. Then there are a Hilbert space, commuting unitaries `T` and `U` on it, and a cyclic unit vector `v` with `A(k,t)=⟨v,U^tT^kv⟩`. So Setting F holds in one dimension for the limits, and Theorems 7-9, 8′ and 9′ apply to `(A₀,A₁)` under their remaining hypotheses.

*Proof.* (1) Both strings end at `X+2ne`. By Theorem 12 (on the fine side, through Theorem 2 at the far coarse site), `ω_i(Φ_i(B_{n,b}(X))^*α_{(i)}^t(Φ_i(B_{n−k,b′}(X+2ke))))` is `δ_{bb′}` times a value independent of `b`. Likewise `N_i(Y,m)=D‖π_i(Φ_i(B_m(Y)))Ω_i‖²`, with `D` free indices (5 on U, 10 on O). The `D` equal terms divided by `[D‖·‖²·D‖·‖²]^{1/2}` give `a_n(k,t)`. (2) The unitary implementing the translation by `−j` cells maps the two strings to `B_{n−j}(X)` and `B_{n−j′}(X+2(j′−j)e)` and commutes with `U_{(i)}`. On the fine side, (Z-b) intertwines `Φ` with the lift up to a global phase or global parity. Both strings carry the same charge, so the factor is common and cancels in the inner product. (3) For finitely many `(j_a,s_a)` and `c_a∈C`, (2) gives `Σ_{a,b}c̄_ac_bA(j_b−j_a,s_b−s_a)=lim_n‖Σ_bc_bU_{(i)}^{s_b}u^{(n)}_{j_b}‖²≥0`. (4) Complete the finitely supported functions on `Z²` in the form `⟨δ_{(j,s)},δ_{(j′,t)}⟩=A(j′−j,t−s)`, after dividing out null vectors. The two shifts preserve the form, so they act as commuting unitaries; take `v=δ_{(0,0)}`. □

**Lemma AX (axial averaging).** (referee closure, ZM1_OBS_REFEREE.md) Let `T` be a unitary representation of `Z³`, `U` a unitary commuting with it, and `v` a vector with
\[
 \langle\xi(f),U^t\xi(g)\rangle=(2\pi)^{-3}\!\int\overline{\hat f}\,\hat g\;W(\theta)\,e^{-itw(\theta)}\,d\theta\qquad(f,g\in\ell^1(\mathbb Z^3),\ t\in\mathbb N_0),
\]
where `W≥0` is bounded, `w` is real, and both are continuous off `θ=0`. Fix an axis `e`, write `θ=(θ_e,θ_⊥)`, and let `ν_{θ_e}` be the image of the measure `(2π)^{-2}W(θ_e,θ_⊥)dθ_⊥` under `θ_⊥↦w(θ_e,θ_⊥)` mod `2π`. Then the axial amplitudes `⟨v,U^tT_{ke}v⟩` have the axial density `c_e(θ_e,t)=∫e^{−itμ}dν_{θ_e}(μ)`, continuous in `θ_e`. If near some `θ_e⁰` they also have a finite branch form `Σ_kW_k(θ_e)e^{−itλ_k(θ_e)}` with continuous data, then `ν_{θ_e}=Σ_kW_k(θ_e)δ_{λ_k(θ_e)}` there. So if `ν_{θ_e}` is nonzero and has no atoms, no finite branch form exists near `θ_e`.

*Proof.* A profile supported on the axis has `f̂` depending on `θ_e` alone. Fubini turns the three-dimensional form into the axial form with density `c_e`. Dominated convergence makes `c_e` continuous, since the point `θ=0` meets each slice in a null set. Two densities that represent the same form on band-limited axial profiles and are continuous agree pointwise (Lemma SP(4) in one dimension). At fixed `θ_e` both sides are then the Fourier coefficients, for `t≥0`, of finite positive measures on the circle. For `t<0` the coefficients are the complex conjugates. A finite measure on the circle is determined by its Fourier coefficients. □

*Application: the free massless walk.* In the free analogue of (d) the links are c-numbers, so the strings reduce to creators `ψ^†_{X,b}`. The coarse (d2) amplitude is then the on-axis particle propagator `ω_{P_c}(ψ_{X,b}α₁^t(ψ^†_{X+2ke,b}))`. Its three-dimensional density is `W(θ)e^{∓itw(θ)}`, where `W` is a diagonal entry of the positive-band projection `1−P_c(θ)` and `±w(θ)` are the eigenvalues of `h(θ)` (`ZM1.md` line 265). The same line gives `1 − cos w = s^2 (1 − chi)` with `1 − chi = (2/3) sum_j sin^2(theta_j/2)`. So at fixed `θ_e` the function `w(θ_e,·)` is a strictly increasing function of `ζ(θ_⊥)=Σ_{j⊥e}sin²(θ_j/2)`, a nonconstant real-analytic function on `T²` (here `s=sin ε>0`, and `w∈[0,π)`). Its level sets are null, so `ν_{θ_e}` has no atoms. For `θ≠0`, `h(θ)` has the positive eigenvalue `w(θ)≥2v|θ|/π>0` (line 265), so `tr(1−P_c(θ))>0`. Hence for some residue and flavour the diagonal entry has `∫W(0,θ_⊥)dθ_⊥>0`, and by continuity `ν_{θ_e}≠0` for all `θ_e` near `0`. By Lemma AX, for that residue the axial data have no finite branch form at any small `θ_e`. Theorems 8-9, 8′ and 9′ do not apply to them.

So the draft's supply for (d), "the fermion's speeds along `e` (Lemmas S, S′ on (d2)), if its axial data form gapped branches" (draft line 383), fails in the free analogue: a charge that propagates in three dimensions gives an axial phase continuum, not branches. The same holds in the interacting case whenever the limit of Lemma DL is the on-axis amplitude of a three-dimensional covariant structure whose bands have null level sets in `θ_⊥`. Theorem 12 does not change this. It forbids amplitudes between strings with different far ends; it does not forbid transverse motion of the charge between them. The axial data can form branches when the charge does not move transversely, as in the transversely flat setting of `RCS1.md` Corollary 9.

**Proposition T.** (referee closure, ZM1_OBS_REFEREE.md) Let `U` be an update in LZ1's class (`LZ1.md` line 28). Use `K_φ` and `γ_φ` as in Theorem 5; on `L5-O`, `K_π=∏_xP_x` and `γ_π=θ`.
1. `K_φU` is in LZ1's class, and `α_{K_φU}=α_U∘γ_φ` equals `α_U` on `𝔄^G` (Theorem 5).
2. A locally gauge-invariant state is `α_U`-invariant if and only if it is `α_{K_φU}`-invariant. So VC1's conditions (i)-(iii) select the same states for `U` and `K_φU`, and so do readings E and P (`VC1_5.md` line 29).
3. For every class whose entries lie in `𝔄₁^G` and every candidate `(Φ,α₁,ω₁)`, the data and budgets are the same for `(ω₀,U)` and `(ω₀,K_φU)`.
4. On `L5-U` with `φ∉2πZ`, and on `L5-O` with `φ=π`, `α_{K_φU₀}` equals neither `α_{WU₀}` nor `α_{U₀W}` for any member `W` of GA1-P-5.
5. If `U` is an update of PS-1's nearest-neighbour class under NN-a (`TOE_ASSEMBLY.md` line 235), so is `K_φU`. On `L5-U`, `γ_φ` is implemented by the layer `∏_{x:x₁ even}e^{iφ(N_x+N_{x+e₁})}`; on `L5-O`, `γ_π=θ` by `∏_{x:x₁ even}P_xP_{x+e₁}`.

*Proof.* (1) is Theorem 5. (2) For such a state `ω∘γ_φ=ω` on local elements, and `γ_φ` commutes with `α_U`; so `ω∘α_{K_φU}=ω∘γ_φ∘α_U=ω∘α_U`. Condition (ii), condition (iii) and reading P do not involve the update, and E is extremality within the set that (i)-(iii) fix. (3) follows from (1) and Theorem 2's last clause. (4) GA1-P-5's gates are link-only (`GA1_5.md` line 50: "each `g_X` is a link-only gauge-invariant unitary"), so every member fixes every matter operator. With `α(A)=U^*AU` one has `α_{WU₀}=α_{U₀}∘γ_W` and `α_{U₀W}=γ_W∘α_{U₀}`, where `γ_W(A)=W^*AW`. Since `γ_φ` commutes with `α_{U₀}`, either equality gives `γ_φ=γ_W` on `𝔄`. Apply both sides to `c_{x,j}`: `e^{iφ}c_{x,j}=c_{x,j}`, false for `φ∉2πZ`. On `L5-O`, `γ_π(γ_{x,a})=−γ_{x,a}` gives the same contradiction. (5) On `L5-U` each link has `p_{ℓ,x}+p_{ℓ,y}=m` (`VC1_5.md` §2), so `∏_xe^{iφQ_x}` differs from `∏_xe^{iφN_x}` by the link factors `e^{iφm}`, which are scalars; both give the automorphism `γ_φ`. Each gate `e^{iφ(N_x+N_{x+e₁})}`, or `P_xP_{x+e₁}` on `L5-O`, is a unitary supported in `F_x` and `F_{x+e₁}` that commutes with `P_xP_{x+e₁}`. The edge triples `(x,x+e₁,ℓ)` with `x₁` even are pairwise disjoint and cover every site, so the product is one nearest-neighbour layer. Composing with `U` adds one layer, so the depth stays finite and independent of volume. `α_{K_φU}=α_U∘γ_φ` fixes every local gauge generator, because `γ_φ` fixes the number-conserving bilinears `G^T_x` (on `L5-O`, the even bilinears `G^{cd}_x`) and `α_U` fixes them. `γ_φ` commutes with every cell lift, because each lift sends a matter mode to a signed matter mode (`VC1_5.md` Theorem 2.2) and `γ_φ` multiplies every matter annihilator by the same phase. □

So, for classes with invariant entries, ZM1-I1[O] posed for fine updates in LZ1's class does not distinguish `U` from `K_φU`. Under NN-a both are PS-1 updates (5). ZM1-I1 as stated admits "base tick, or with a plaquette class that GA1-P-5 supplies" (`ZM1.md` line 361), and (4) shows that `K_φU₀` is not of that form with the base tick `U₀`. Whether `α_{K_φU₀}` equals the tick of a base law with other constants is not decided here. Whether the five-mode law's update class should contain the matter-phase layer, as a chemical-potential-like free constant, is a law-specification choice for the owner.

*Bearing on LZ1's census.* `K_φU` is in LZ1's class, so `LZ1.md` Theorem 2.2 (line 56) applies to it: "Every band in `H_nt` is identically `1` on any connected `C¹` neighbourhood of a node." So on odd bands the twist removes and creates only flat nodes. Under LZ1-SC the dispersion clause applies only to bands with image in `ker(Ũ−1)^⊥` (`TOE_ASSEMBLY.md` line 229), and a band equal to `1` near a node does not have such an image. So the twist does not affect that clause on odd bands. On charged even bands, such as charge `±2` composites in the trivial pattern, Theorem 2.2 does not apply, and Theorem 5 lets the twist move a propagating node.
