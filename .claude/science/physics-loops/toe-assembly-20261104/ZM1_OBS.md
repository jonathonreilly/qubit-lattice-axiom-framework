# ZM1-OBS. Observable classes for the zoom comparison

## 0. Status

**Pass 2, conditional and unrefereed.** Both five-mode laws remain live. All classes and readings below are proposed comparison specifications, not adoptions. The owner has not chosen a class. No axiom or working-set entry changes.

**Proved under the displayed hypotheses.** Diagonal gauge projection; evenness and representative-site preservation; reconstruction from the full invariant two-point family; twist invisibility on the invariant algebra; the absolute-budget bound; zero-momentum and moment rigidity; conditional band-speed transfer; the sharp-grading, area and Creutz identities; and the finite-string endpoint selection rule. Numbered results below include their proofs. R-GI and its on-site consequence, invariant evenness, and the finite-register obstruction were already proved in `ZM1.md`, `RCS1.md`, and `GA2_Y2.md`, respectively.

**GAP.** The draft's unconditional identification of the twist with another admissible *base five-mode law* is not established. Its several-branch proof needs uniform weight bounds, circular phase separation and `p>0`. Its loop zero rule does not define a Creutz ratio when a required expectation vanishes. Its proposed string budget does not yet define stationary translation-covariant axial data to which the speed theorem applies. Its flow-like free-field claim needs a proof for the specified kernels and profiles. Its scaling-limit construction needs a common algebra and does not itself supply convergence of dynamics or charged sectors. Details and corrected statements appear below. These gaps do not refute the frozen sources.

**Open by name.** ZM1-I1[a], ZM1-I1[b], ZM1-I1[c], ZM1-I1[d], ZM1-I1[e] are specifications, not attacks or existence results. ZM1-I1 remains open pending the owner's selection. Also unchanged: Z2-spatial, ZM1-i, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5, and the rule selecting rung `n` or the exact fixed point (`ZM1.md` §0). RCS-P and MT1-S[R-CS^str] remain open; R-CS^str is a named working candidate, not an adopted prescription.

**Provenance.** Distilled from `ZM1_OBS_DRAFT.md`, SHA-256 `fcf9b7f24eebfa20ceaa7ce2e6fc7530198a30734a26d496f7f7037186578499`, pass 1 Claude Opus 5.5. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b135-cfce-7bd2-b8ea-e94d37b92b40` (from the run log, on the Mac mini). The draft's toy calculation and literature reports are not independently rerun or verified. They are not proof. Prior-work search and overlap: `prior/ZM1_OBS.md`. This is not an independent referee or an audit.

## 1. Definitions inferred by the distiller

The following make the draft's conventions explicit. They are mathematical definitions, not physical axioms. Use `L5-U[m]` or `L5-O[S_+]` as in `LW1_5.md`, with quasi-local algebra `𝔄`, tick `α`, local compact gauge groups, invariant algebra `𝔄^G`, matter parity `θ`, and gauge average `E`. The tick commutes with the local gauge actions. Use the coarse counterparts with subscript 1. A block map `Φ:𝔄₁→𝔄` is the unital injective graded *-homomorphism of `ZM1.md` Definition Z. In (G1), `Φ(G_X^(1),T)=Σ_{x∈S_X}G_x^T`, where the nonempty finite sets `S_X` are pairwise disjoint. (G2) fixes the image under gauge transformations outside their union. Representative-site maps have `S_X={x_X}`. One coarse tick is `L` fine ticks.

A datum is a finite ordered tuple `d=((B₁,s₁),…,(B_n,s_n))`, with coarse observables and integer times. Define
\[
 F_0(d)=\omega_0\!\left(\prod_j\alpha^{Ls_j}(\Phi(B_j))\right),\quad
 F_1(d)=\omega_1\!\left(\prod_j\alpha_1^{s_j}(B_j)\right),\quad
 \Delta(d)=|F_0(d)-F_1(d)|.
\]
Products keep the displayed order. Extend linearly to finite combinations of tuples of the same shape. For stationary states, a truncated two-point value subtracts the product of its one-point values. A comparison class `O` comprises data, its domain and a nonnegative budget `ε_p`. The proposed `ZM1-I1[O]` asks, for the specified VC1 fine vacuum, for `L≥2`, `p≥1`, a Definition-Z map obeying (Z-a), (Z-b), (G1), (G2) and singleton sets, a coarse law of the specified form, a stationary coarse state, and constants independent of the variable data, such that the stated budget holds. Constants may depend on an explicitly quantified support radius or composite list. The original ZM1-I1 uses unit one-body profiles supported at `|θ|≤κ≤κ₀` and budget `C(κ^p+tκ^{p+1})`; its exact quantifiers are `ZM1.md` R6. Its coarse local gauge invariance is an additional hypothesis when invoked below.

For a fixed algebra and family of state/update pairs, data *determine* a property when equal data imply equal property; *cannot detect* means two allowed pairs have equal data and different property. A comparison with nonzero errors does not automatically transfer every such property continuously. The four tests ask whether a reading fixes a target, is closed, assumes physics, or adds structure. `P` means pass and `C` conditional, as in pass 1. These judgments are proposed, not owner decisions.

## 2. Gauge-invariant data

**Theorem 1 (Haar and homomorphism tools; draft Lemmas 3.1–3.2).** A continuous finite-dimensional representation of a compact group admits an invariant inner product; Haar averaging is the orthogonal projection onto invariant vectors. A unital *-homomorphism of C*-algebras is contractive and preserves exponentials of self-adjoint elements.

*Proof.* Average any inner product over Haar measure. Haar invariance makes the average of the representation idempotent and self-adjoint, with invariant range. A unital homomorphism contracts spectra; use the spectral radius for self-adjoint elements and the C*-identity for general elements. Apply the norm-convergent exponential series. □

**Theorem 2 (diagonal gauge projection; draft A, A1–A2).** Suppose `ω₀` is locally gauge invariant and the fine tick fixes the local gauge unitaries. Under (G1), for any one coarse gauge transformation `g`, simultaneously replacing every entry of a datum by `gB_jg*` leaves `F₀` unchanged. This requires neither (G2) nor singleton sets. The same holds for `F₁` when `ω₁` is locally gauge invariant. For finite-dimensional invariant entry spaces, Haar projection of their tensor product leaves the value unchanged; if the invariant tensor space is zero, the value vanishes. If both states are invariant, `Δ(d)=Δ(P_Λd)` for any finite set of coarse sites. If only the fine state is invariant, `|F₁(d)-F₁(P_Λd)|≤Δ(d)+Δ(P_Λd)`. For invariant entries, replacing a stationary coarse state by `ω₁∘E₁` preserves all data and stationarity.

*Proof.* By Theorem 1 and (G1), `Φ(g)` is the product of fine local gauge unitaries at `S_X`. Gauss generators at distinct sites commute. The tick fixes each factor, so the entire evolved product is conjugated by that product. Fine invariance removes it. Connectedness and products of exponentials extend the statement to the local group; average its tensor representation to obtain the selection rule. The discrepancy bound is the triangle inequality. The average `E₁` fixes invariant products and commutes with the tick, so the last state is stationary and locally invariant. □

In particular, a single charged entry at `X` and no other entry charged at `X` gives zero. This extends the singleton charged two-point result R-GI of `ZM1.md` §5 to (G1) sets and both laws. It is a statement about simultaneous projection of the **whole tuple**, not a claim that each entry can be separately projected.

**Theorem 3 (evenness and invariant image; draft B).** On both laws `𝔄^G⊆𝔄_even`. For a representative-site map satisfying (G1)–(G2), `Φ(𝔄₁^G)⊆𝔄^G`. Gauge-commuting automorphisms preserve `𝔄^G`. In the GNS representation of a locally invariant state, `H_phys=closure(π(𝔄^G)Ω)` lies in the even subspace.

*Proof.* The first assertion is already `RCS1.md` Theorem 4. Its argument multiplies local gauge-centre actions on all sites supporting a local element: they negate each matter mode and both ends of each link, hence act as matter parity on the even link algebra. Gauge averaging and norm density extend the result. At a representative site, (G1) and Theorem 1 turn a fine gauge conjugation of `Φ(B)` into the image of the coarse conjugation; (G2) handles all remaining sites. Gauge commutation gives invariance under the update and its inverse. The invariant state implements parity in GNS and fixes `π(A)Ω` for invariant `A`. □

**Theorem 4 (reconstruction; draft D).** For a stationary, translation-invariant state, assume tick and translations preserve `𝔄^G`. The complete data `ω(A* α^t τ_β(B))`, with all `A,B∈𝔄^G` and all integer `t,β`, determine the cyclic representation of `𝔄^G` on `H_phys` and its tick and translation implementers, up to unitary equivalence. The truncated data for all local invariant `A,B` determine the unitary representation on `H_phys⊖CΩ`. Every invariant-entry datum is a matrix element in this restricted structure.

*Proof.* At `t=β=0` the untruncated values are the GNS inner products; left multiplication gives the algebra representation. The action on `π(A)Ω` determines the implementers on a dense set. The centered local vectors `π(A-ω(A))Ω` are dense in the orthogonal complement, and their evolved inner products are exactly the truncated values. Their Gram matrices define an isometry intertwining the actions, which extends to a unitary. Invariant evolved products preserve `H_phys`. □

This does not reconstruct an arbitrary representation on `H_phys^⊥`. Class (a)'s *complete exact data* include the full truncated family: for any local `A,B`, choose a sufficiently large `β` and include `τ_{-β}B` in a sufficiently large support ball. This does not make its uniform-in-`R₀` long-distance error estimate automatic: `C_{R₀}` may grow with `R₀`. Nor do truncated data alone determine the invariant algebra representation or its one-point values.

**Theorem 5 (twist invisibility; draft C).** In the enlarged gauge-invariant update class, append `K_φ=∏_x e^{iφQ_x}` on U, or the product of site parities on O. The corresponding automorphisms are `α_φ=α∘γ_φ` and `α_π=α∘θ`; on U, `γ_φ(c)=e^{iφ}c` and it fixes link operators. They agree with `α` on `𝔄^G`. Thus all invariant-entry data agree for every state. A locally invariant stationary state remains stationary. If `γ_φ(A)=e^{-iqφ}A`, then `α_φ^t(A)=e^{-iqφt}α^t(A)`. In the state GNS space the implementer on a charge-`q` subspace is multiplied by `e^{-iqφ}`; on O the odd subspace is multiplied by `-1`. A band so supported has the same slopes after its eigenphase is shifted by the constant. For `q≠0`, a scalar band value `V(K₀)=λ1` becomes a node exactly when `e^{iqφ}=λ`. R-CS^str finite string states are unchanged, and the covariant representation problem defined solely on `𝔄^G` is unchanged.

*Proof.* The finite product of local central gauge rotations acting on a local element sends every matter annihilator to `e^{iφ}c`; a U-link operator conserves total rishon number, so its phases cancel. This defines the infinite-volume automorphism locally. Gatewise gauge invariance makes it commute with the tick. An invariant local element is fixed by each factor, and density gives the result on `𝔄^G`. Gauge invariance of the state gives the implementing unitary, and the displayed eigenvalue follows directly. A constant local phase shift leaves derivatives of a locally chosen quasienergy branch unchanged. The string-state formula contains the state and strings, not the update; the restricted dynamics agree. □

**GAP C-law.** A layer in LZ1's enlarged class need not be a tick of the original `L5-U` or `L5-O` base form. Thus this is a counterexample to identifying charged phase origins *within the enlarged class*, conditional on a charged band, not a proof of indistinguishability between two admissible base laws. The equality of fine invariant data survives, but equivalence of the original ZM1-I1 existential statements requires closure of the admissible law and vacuum reading under the twist. R-CS^str implementers can carry an extra choice; equality of the restricted dynamics alone does not establish a unique physical phase convention. See `RCS1.md` Definition 5 and Theorem 8(c).

## 3. Budgets, rigidity and speeds

**Theorem 6 (absolute-budget vacuity; draft V).** On a subset of data, if `|F_i(d)|≤s(d)` for both sides and `2s(d)≤Cε_p(d)`, every candidate satisfies `Δ(d)≤Cε_p(d)` there.

*Proof.* Triangle inequality. □

Thus an absolute power budget can be vacuous for faster-decaying correlators or loops; it does not follow that every absolute budget is useless. Relative budgets introduce their own domains and exact constraints.

For the next results, let `T^{(i)}_β` be unitary `Z³` translations, commuting with `U_i`, and let `v_{i,a}` be a finite list of vectors. Put `C_i(β,t)_{ab}=⟨v_{i,a},U_i^tT^{(i)}_βv_{i,b}⟩`, `c_i(θ,t)=Σ_β C_i(β,t)e^{-iθ·β}`, and `ξ_i(f)=Σ_{a,β} f_a(β)T^{(i)}_βv_{i,a}`. In applications use centered local composites, fine time `L t`, and the induced coarse-cell translations. For charged fields omit centering. Let `N(f)=max_i‖ξ_i(f)‖`.

**Theorem 7 (Fourier form and rigidity; draft F0, F, F1–F2).** If `Σ_β‖C_i(β,0)‖<∞`, then `c_i(·,0)` is continuous and positive semidefinite and `ξ_i` extends boundedly to `ℓ²`. If the sums also converge absolutely at fixed `t`,
\[
 \langle\xi_i(f),U_i^t\xi_i(g)\rangle=(2\pi)^{-3}\int\hat f(\theta)^*c_i(\theta,t)\hat g(\theta)d\theta .
\]
If the difference of these forms is bounded by `ε(κ)‖f‖‖g‖` for profiles supported in `|θ|≤κ` and `ε(κ)→0`, then `c₀(0,t)=c₁(0,t)`. If instead at `t=0` the difference of norms is bounded by `Cκ^p N(f)^2` and `Σ_β(1+|β|)^n‖C_i(β,0)‖<∞` with integer `n<p`, the moments `Σ_β β^k C_i(β,0)` agree for every `|k|≤n`. A relative dynamical budget `C(κ^p+tκ^{p+1})N(f)N(g)` implies the first hypothesis for each fixed `t` when `p>0`.

*Proof.* Fourier inversion gives the form for finitely supported profiles. Positivity of Gram forms and Fejér approximate identities give pointwise positivity of the continuous symbol; its supremum bounds `ξ`, extending the formula. Normalized Fourier indicators of shrinking balls about zero test arbitrary matrix entries and yield equality by continuity. For the static relative bound, shrinking balls around nonzero `θ` and then setting `κ↓|θ|` gives `‖c₀-c₁‖=O(|θ|^p)`, since the symbols are bounded. Weighted summability gives `C^n` symbols. Taylor expansion along every ray forces all derivatives through order `n` to vanish; their Fourier series are the stated moments. Boundedness of `ξ_i` gives the last implication. □

For charged fields in locally invariant, coarse-cell-invariant fine and coarse states, R-GI makes every distinct-site coefficient zero. Hence the symbol is the on-site matrix and the original ZM1-I1 bound forces exact equality of on-site return amplitudes at each tick. This is already `ZM1.md` R-GI and its consequence, not a new closure. For centered invariant composites the equality is instead of **sums over all separations**, when absolutely convergent, including short distances. The digest notes a massless comparator with non-absolutely-summable plaquette covariance: `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md` in its stated conditional setting; it is unaudited. Summability must be checked, not presumed.

**Theorem 8 (one-branch speed transfer; draft S).** Suppose near zero the scalar symbols have the form `c_i(θ,t)=w_i(θ)e^{-itλ_i(θ)}` for all nonnegative integer `t`, with continuous `w_i≥0`, `w₁(0)>0`, continuous real phases `λ_i(0)=0`, and the relative dynamical budget of Theorem 7 for `p>0`. Then `|λ₀(θ)-λ₁(θ)|=O(|θ|^{p+1})`. Directional derivatives at zero agree wherever they exist.

*Proof.* Shrinking Fourier balls and taking `κ↓s=|θ|` yields the pointwise bound `|w₀e^{-itλ₀}-w₁e^{-itλ₁}|≤C(s^p+ts^{p+1})max w_i`. At `t=0`, weights are comparable and bounded below near zero. Subtract the weight difference to obtain `|e^{-itδλ}-1|≤C'(s^p+ts^{p+1})`. For nonzero `δλ`, continuity allows `|δλ|≤π/2`; choose `t=ceil(π/(2|δλ|))`. The left side is at least `√2`. Rearranging yields `|δλ|=O(s^{p+1})`. Divide by `s` along a ray. □

**Theorem 9 (several branches; corrected draft S′).** Suppose `p>0` and, in a punctured neighborhood of zero,
\[
 c_i(\theta,t)=\sum_{k=1}^{n_i}W_{i,k}(\theta)e^{-it\lambda_{i,k}(\theta)},\qquad W_{i,k}\ge0,
\]
with finitely many continuous branches, phases extending continuously to zero with `λ_{i,k}(0)=0`, `‖W_{i,k}‖≥w>0`, `Σ_k‖W_{i,k}‖≤S<∞`, and within each side phase gaps at least `g|θ|` modulo `2π`. If the absolute band-limited form error is at most `C(κ^p+tκ^{p+1})‖f‖‖g‖`, then each branch on either side has a branch on the other within `O(|θ|^{p+1})` modulo `2π`. Along rays, existing branch-speed sets coincide. A cone `±v|θ|`, `v>0`, satisfies the gap condition, but only if the observables have the stipulated nonvanishing branch weights.

*Proof.* Localized profiles give `‖c₀(θ,t)-c₁(θ,t)‖≤C(s^p+ts^{p+1})`. Average each symbol against `e^{itλ}` over `0≤t<T`, where `λ` is one selected branch. The selected contribution is its weight; each other same-side contribution has norm at most `πS/(Tgs)`, by the geometric-sum estimate. If `δ` is the circular distance to the other side's nearest phase, its averaged contribution is at most `πS/(Tδ)`. Choose `T=ceil(ηs^{-p-1})` with sufficiently small fixed `η`. The comparison error and the same-side leakage are eventually less than `w/2`, so `δ≤2πS/(wT)=O(s^{p+1})`. Exchange sides. Since `p>0`, this is smaller than the within-side gap; continuity gives a unique matching branch along a sufficiently short ray. Divide by `s`. □

**GAP S′ in pass 1.** Continuity on the punctured ball plus a lower bound on `‖W‖` does not supply its proof's finite `sup Σ‖W‖`; it is an added hypothesis above. Eigenphases are periodic, so the geometric-sum bound uses circular distance. The conclusion also needs `p>0`. Neither theorem establishes a common speed across different species. `LZ1.md` leaves that comparison open.

## 4. Loops and strings

**Theorem 10 (sharp grading; draft W1).** Let self-adjoint `E` have finite spectrum, `ω((E-n)²)=0`, and `[E,Y]=qY` with `q≠0`. Then `ω(Y)=0`. The same conclusion holds for `E²=1`, `ω((E-s)²)=0`, `s=±1`, and `EY=-YE`.

*Proof.* If `P` projects onto the `n` eigenspace, the spectral gap and the state condition give `ω(1-P)=0`. Cauchy–Schwarz gives `ω(Y)=ω(PYP)`. The commutator moves that eigenspace to a different one, so `PYP=0`. Anticommutation gives the same conclusion for the `s` eigenspace. □

On U, an oriented fundamental loop with nonzero net traversal of some link has nonzero end-number charge there. In the locked states and `ω_AB` the relevant end numbers are sharp, so such loop expectations vanish; see `RCS1.md` Theorems 7–8 for the states. In particular this holds for the simple rectangles of class (b). The draft's phrase “every closed fundamental loop” needs the traversal qualification: an immediately retraced loop has zero net end-number charge, so this proof does not make it vanish. On O, a loop traversing a link an odd number of times vanishes in a state sharp in that link's end parity. No such O witness is asserted here. This gives a counterexample to a universal nonzero area/perimeter-law assertion for simple fundamental rectangles in the U witnesses, not to any frozen result.

**Theorem 11 (loop normalizations; draft W2–W3).** For nonzero rectangular loop expectations let `w_i(R,T)=-log|ω_i(W_{R,T})|`. If `w_i=2μ_i(R+T)+c_i+o(R+T)`, then `|w₀-w₁|/(RT)→0` as `min(R,T)→∞`. If `w_i=σ_iRT+O(R+T)`, the normalized difference tends to `|σ₀-σ₁|`. For `χ=Δ_RΔ_T w`, every `f(R)+g(T)` cancels and `w=σRT+2μ(R+T)+c` gives `χ=σ`.

*Proof.* `(R+T)/(RT)≤2/min(R,T)`. The mixed finite difference kills sums of one-variable functions and sends `RT` to 1. □

`GA2_Y2.md` Theorem N already proves that an invertible covariant operator link with nontrivial continuous representation is impossible on a finite register. Theorem 2.5 there gives the rank obstruction for the stated U and O links. Injective unital *-homomorphisms preserve spectra, so their block images remain noninvertible; nilpotent U-link entries remain nilpotent. This is an obstruction to exact Wilson-link identification, not to comparing loop expectation values through a separately specified dictionary.

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

**Four tests: P P P P, proposed.** No target value is fixed; all finite radii are quantified; no charged-sector or continuum result is assumed; and the envelope avoids the specific vacuity in Theorem 6. The envelope is an additional chosen normalization and can be dominated by a large distant outlier. Thus test 4 is a judgment, not a theorem that no extra structure was introduced. `GA2_Y2.md`'s SC fixes state, scale, list, Wilson-function dictionary, normalization and tolerance; it is a diagnostic, not GA2. The finite-region Peter–Weyl approximation in `docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md` is conditional and unaudited, retains boundary sectors, and does not identify its registers with either five-mode law.

### 5.2 (b): (a) plus spatial loops

Add static traces of quantum-link products around every coordinate-plane `R×T` rectangle and cell-group images; on U also include `W_C*W_C`. Put `w_i=-log|ω_i(W_C)|` when nonzero. Offer three alternative budgets, for `p≥1`:
\[
 \text{(b-P)}\ |w_0-w_1|\le C|C|^{1-p},\quad
 \text{(b-A)}\ |w_0-w_1|\le CRT\min(R,T)^{-p},\quad
 \text{(b-Cr)}\ |\chi_0-\chi_1|\le C\min(R,T)^{-p}.
\]
`ZM1-I1[b]` adds one chosen loop budget to (a). Pass 1 proposes that two zero expectations pass and exactly one zero fails.

**GAP b-zero.** This rule is enough to say whether an individual log comparison is skipped, but it does not define `χ` when *any* of the four loop expectations entering it vanishes. It also leaves degenerate `R=1` or `T=1` rectangles unspecified. A corrected Creutz domain requires all four expectations on both sides nonzero, with `R,T≥2`, plus an explicit separate rule for all excluded cases. The current reading is conditional until that choice is made. `W_C*W_C` has its own zero cases and normalization; it is not a fundamental loop expectation.

Theorem 11 gives the stated area and perimeter distinctions and cancellation of additive perimeter/corner terms, conditional on the asymptotic expansions and nonzero expectations. It does not prove a law exists. Theorem 10 gives simple-rectangle vanishing in the U witnesses, and Theorem N prevents exact Wilson-link identification. Quantum-link loop magnitudes may exceed one; their logarithms need not be positive. GA2's weak-coupling window and an infrared string tension are different questions. Spatial loops alone supply no charged-sector speed. A conditional, unaudited finite-clock example of relative loop comparison with a growing alphabet appears in `docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md`; its ratio cancels self terms, but it is not a five-mode comparison. Existing Creutz diagnostics are in `docs/CONFINEMENT_STRING_TENSION_NOTE.md` and are bounded qualitative support.

**Four tests, proposed:** (b-P) P C P C; (b-A) P C C P; (b-Cr) P C P P. Closedness is conditional on the family, blind products and zero convention. The area form can discard perimeter distinctions; the perimeter form compares a potentially UV-sensitive coefficient. Creutz cancellation is algebraic, not a guarantee of a meaningful continuum observable.

### 5.3 (c): band-limited invariant composites

Fix a finite local invariant list `O_a` and states for which the `t=0` correlation matrices are absolutely summable. Use the centered vectors and profiles of §3, with Fourier support `|θ|≤κ≤κ₀` and all `t∈N₀`. Compare with
\[
 |\langle\xi_0(f),U_0^t\xi_0(g)\rangle-\langle\xi_1(f),U_1^t\xi_1(g)\rangle|
 \le C(\kappa^p+t\kappa^{p+1})N(f)N(g).
\]
`ZM1-I1[c]` asks for this comparison with the §1 maps and laws. The finite list, summability domain, allowed profiles and constants must be specified before using the reading. The infinite `ℓ²` smearing denotes a GNS limit under Theorem 7, not automatically a bounded element of the quasi-local algebra.

Theorem 7 imposes exact zero-momentum correlation sums wherever the time-`t` sums also converge, and static moment equalities under its stronger hypotheses. Theorems 8–9 transfer speeds only for the stated isolated, weighted bands and corresponding error form. For multiple branches Theorem 9 uses an absolute norm bound; a relative bound implies it under bounded `ξ`. This can supply LZ1-i for visible even species, not a fermion or interspecies common speed. GA2 and T0-rate need an independently fixed operator-to-continuum dictionary and rates. Gauge-invariant composite data do not access arbitrary `H_phys^⊥` or fix the charged phase in Theorem 5's enlarged family.

**Proposed (c′), flow-like variant.** Replace local composites by bilocals `Σ_{x,y}K(x,y)ψ_x* T_{x→y}ψ_y`, with specified paths, kernels, convergence and transformation laws. It is an analogy to smoothing, not Wilson flow on group-valued links. **GAP c′:** the draft's inference from ZM1's free band-limited elementary-field estimates to arbitrary such smoothed bilocals requires constituent momentum support, normalization, uniformity and a truncation argument; no such proof is supplied. `ZM1.md` proves a narrower free `p=2` comparison and does not transfer it to interacting quantum links. The no-invertible-link theorem does not exclude every possible quantum-link flow. Flowed continuum observables are context, not an established identification.

**Four tests: P C P C, proposed.** The list, profiles, summability and range need fixing. Rigidity forces exact short-distance-inclusive sums, and (c′) adds kernels and paths; neither is implied by a long-distance comparison.

### 5.4 (d): (a) plus R-CS^str data

Fix an axis `e` and coarse strings `S_b=B^{(1)}_{r,b}(X)`. Let `Φ₀=Φ`, `Φ₁=id`, `α₀=α^L`, and `N_i(X,r)=Σ_bω_i(Φ_i(S_b)*Φ_i(S_b))`. On the positive-denominator domain add:

- (d1) normalized string-state truncated invariant correlators `Σ_bω_i(Φ_i(S_b)*Φ_i(A)*α_i^t(Φ_i(τ_βB))Φ_i(S_b))/N_i`, with the corresponding one-point products subtracted; use (a)'s envelope uniformly in `r`.
- (d2) normalized same-far-end amplitudes `Σ_bω_i(Φ_i(B_{r,b}(X))*α_i^t(Φ_i(B_{r-j,b}(X+2je))))/[N_i(X,r)N_i(X+2je,r-j)]^{1/2}`.

The draft proposes an axial band-limited relative budget of the form in (c) for (d2), uniformly in `r≥r₀`, and limits as `r→∞`. It uses the proposed odd label `χ_tot` over parity-sharp backgrounds. `ZM1-I1[d]` adds these requirements to (a).

**GAP d-domain and speed.** At finite `r`, allowed `j` is constrained by the string lengths, and the normalized kernel depends on `X,r,j`; a stationary positive-definite `Z`-translation kernel with a common GNS representation, a limit, and the Fourier-domain budget have not been constructed. Therefore Theorems 8–9 cannot yet be applied to (d2). The corrected conditional claim is axial speed transfer *if* a specified limiting translation-covariant kernel satisfies all hypotheses of either theorem. The endpoint rule only says that the displayed common-end family has no transverse amplitudes. It does not prove all transverse physics absent. Locked states have no positive string denominators; in `ω_AB`, RCS1 proves the stated positive open-string and transverse-flatness results. The string-sector tick phase is not fixed by invariant dynamics alone (Theorem 5). GA2/T0 need additional bridges; this charged prescription supplies neither by itself.

**Four tests: P C C C, proposed.** The axis, domain, limits and odd label need specification. R-CS^str is a working candidate whose adoption awaits RCS-P and MT1-S; the axis selects the data being tested.

### 5.5 (e): tower and scaling limits

Take compatible one-step maps `ι_j:𝔄_j→𝔄_{j-1}`, compositions `Φ_k=ι₁⋯ι_k`, coarse laws and states. Require the (a) bound at every level with one `p` and constants independent of `k`; this is the proposed `ZM1-I1[e]`, a tower requirement rather than only one step. If all `𝔄_k` are identified with one fixed separable unital algebra `𝔄_*`, record weak-* limit points of `ω₀∘Φ_k` restricted to `𝔄_*^G`. Compactness gives subsequential limit points. If band-limited data are additionally supplied at every level with the hypotheses of Theorems 8–9, their speed conclusions apply pairwise at those levels.

*Proof of compactness.* The state space of a separable unital C*-algebra is weak-* compact and metrizable; any sequence has a convergent subsequence. The invariant algebra is separable as a closed subspace. □

**GAP e-dynamics.** Compactness of pulled-back states alone gives neither a compatible tower, convergence of updates, uniqueness of limit, nor a charged sector. Reading charged structure from a limit is proposed and needs a separate construction. A weak-* state on `𝔄_*^G` is not automatically the full scaling algebra of the cited literature. The YM H-BLOCK interface also requires a joint block/smeared state, not just separate curvature bounds (`prior/ZM1_OBS.md`, YM library `port/p8b-limits.md`). T0-start and T0-rate still need their specified topology, uniform estimates and dictionary.

**Four tests: C P P P, proposed.** The tower moves the target beyond a single interacting step; the fixed sequence and uniform constants specify the remaining data. This pass does not prove the tower exists.

## 6. Ranking, dependencies and checks

Pass 1's proposed ranking is **(a), (c), (e), (d), (b)**. It favors a one-step invariant comparison, then spectral access, while counting the tower requirement, axis choice and loop zero/normalization issues as costs. The ranking is a judgment, not an owner selection. (a) is included in (b) and (d); (e) repeats it along a tower; (c) uses a different budget. Combinations are possible.

The four-test outcomes above retain pass 1's assessments with the disclosed gaps. In particular, its P for (a)'s fourth test is conditional in substance on accepting the envelope; its P for (e)'s closedness presumes the common algebra and tower have actually been fixed. No proposed reading is promoted to a working-set axiom.

Prior work: `ZM1.md` already proves the original R-GI on-site consequence and the narrower free `p=2` result; `RCS1.md` already proves invariant evenness, locked denominator vanishing and conditional string-sector flatness; `GA2_Y2.md` already proves Theorem N and the finite-list diagnostic limitations. `prior/ZM1_OBS.md` records the repository search, supporting notes, limitations and paths. The supplied weak-window note `docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md` distinguishes separated and contact observables in a conditional, unaudited comparator; it does not prove either limit here. Literature cited in pass 1, including operator-algebraic scaling limits and gradient flow, remains context and was not independently checked in this pass.

The pass-1 floating-point toy check reported a two-site U(1) model: separated charged correlation zero, invariant correlator change at most `4.6×10⁻¹⁵` under a twist, and on-site phase agreement to `1.2×10⁻¹⁵`. It is reported in `ZM1_OBS_DRAFT.md` §7; it was not rerun and proves no general statement. No new numerical or independent referee check is claimed.
