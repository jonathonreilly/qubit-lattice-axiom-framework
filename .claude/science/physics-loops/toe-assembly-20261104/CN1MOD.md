# CN1MOD. Massive-photon speed flow

## 0. Status

**Pass 2; not refereed or frozen.** The target remains open. The results below are mathematics conditional on their displayed hypotheses, not a construction of the RG, a framework law, or a physical prediction. No reading or axiom is adopted.

**Proved here.** The one-loop pair coefficient is strictly attractive on positive speeds (1); the discrete estimate and its window (Theorem 1); an analytic size-to-Lipschitz estimate (Lemma 2); a conditional discrete speed box (Lemma 3a); UB″ implies the proposed discrete consequence under the specified uniform smallness (Theorem 3); Cauchy obstructions to fixed-disc bounds (Proposition 4 and Corollaries 4′–4″); a tangent-domain estimate for an abstract recursion (Proposition 5); and a restricted continuum quartic integral vanishes (Lemma 6). All are author-side checks. The one-loop physical identification is an imported, conditional input.

**GAP.** The draft's gauge-transformation sign is wrong; its finite-torus covariance is an infinite-volume formula (§1). UB″ is unproved; it is sufficient, not equivalent to the target. The proposed discrete target does not establish CN1's interpolated R1″-MOD. A tangent disc is not equivalent to a fixed disc in running couplings and is not proved to support UB″. The asserted failure of every bare-coupling expansion, the exact gauge-invariant block flow for the massive model, and the claimed necessity of quartic positivity in every BBS-type scheme are not proved (§5). The last-scale prefactor in the draft's proof of Theorem 3 needs the correction given below. The draft's quartic diagram identification requires the specified cutoff prescription; it is not established for arbitrary RG slices.

**Open by name.** UB″; R1″-MOD[d]; R1″-MOD; B1; B2; C1 and the lattice quartic sign; the discrete unequal-charge n-species spread theorem; R1-MOD, R1′, R1-OBS, CN1-T, CN1-T(r), R2 with R2-a/H-TICK, R2-b/H-TRANSFER and R2-c, R3, R-P, H-PHOTON, H-THR, H-FIN, GB1-U1, GA1-5-Φ as a cone, VC1 and ZM1-I1[INV]. The named attacks A, B, C and earlier attacks 1–4 are assessed in §5. These open items prevent the framework conclusion.

**Provenance.** Pass 1: `CN1MOD_DRAFT.md`, SHA-256 `67f7e50b173bebba1137876710d244aea2a7a5256ee0932da6d0d64654ef4c9a`; prior digest `prior/CN1MOD.md`, SHA-256 `6df25381998d77ab8d244413d72decaf2e709c25b407523446f51e8212ca85c2`. Context: `TOE_ASSEMBLY.md` §§3.4–3.6, W3; `CN1.md`, `LZ1.md`, `LZ1I.md`, `LW1.md`. Pass 1 records historical source revisions and literature searches; these are not refreshed as current branch status. Pass 2 model requested: `gpt-6.1-terra`; effort and session id: see run log. No independent referee has checked this file.

## 1. Supplied model and proposed readings

M″ is a proposed rung-1 Euclidean model. On a four-dimensional periodic lattice of side T, take n≥2 four-component Grassmann species, charges q_a∈Z\{0}, speeds v_a>0, mass counterterms μ_a, and real link fields A. Let w_a0=1, w_aj=v_a, U_aμ(x)=exp(i e q_a A_μ(x)), and Hermitian Euclidean gamma matrices obey {γ_μ,γ_ν}=2δ_μν. The Wilson fermion action is

\[
S_F=\sum_{a,x}\left\{\mu_a\bar\psi_a\psi_a+\sum_\mu w_{a\mu}\left[\bar\psi_a\psi_a-\tfrac12\bar\psi_a(x)(1-\gamma_\mu)U_{a\mu}(x)\psi_a(x+\hat\mu)-\tfrac12\bar\psi_a(x+\hat\mu)(1+\gamma_\mu)U_{a\mu}(x)^*\psi_a(x)\right]\right\}.
\]

At A=0 the symbol is μ_a+Σ_μw_aμ[(1−cos p_μ)+iγ_μ sin p_μ]. At μ_a=0 the nonzero corners have positive Wilson mass; persistence of massless interacting modes and counterterm selection are assumptions to be proved. The photon is Gaussian with covariance δ_μν/(\hat k²+m²), \(\hat k^2=\sum_\mu(2\sin(k_\mu/2))^2\). On the torus the inverse Fourier transform is a discrete sum T⁻⁴Σ_k; the draft's Brillouin-zone integral is the infinite-volume covariance. Uniformity in T and treatment of possible fermion zero modes are open. Set G₀=e², L≥2, h=log L and N=⌊log_L(1/m)⌋, for 0<m≤L⁻². The photon speed is one in the bare units.

**GAP, gauge sign.** With the action above and ψ(x)↦exp(ieqχ(x))ψ(x), invariance of S_F requires A_μ(x)↦A_μ(x)+χ(x)−χ(x+μ̂), not the sign in the draft. The mass and Feynman gauge fixing mean the Gaussian weight is not invariant under this transformation. Charge conjugation, translations, spatial cubic symmetry and time reflection are assumed in the usual lattice implementation. Species interchange is covariance between exchanged data when equal charges and counterterms are exchanged; it is an actual symmetry at exchange-fixed data. The fermionic action's covariance alone does not give gauge invariance of the full massive weight.

### Definitions inferred by the distiller

These conventions make the draft's statements precise; they add no physical axiom.

1. An exact scale integration is a specified decomposition and exact integration of fluctuation fields followed by rescaling. Its existence, holomorphic coordinates and uniform bounds are hypotheses, not consequences of this definition.
2. X_k lies in a complex Banach space with an isometric involution σ exchanging species 1 and 2. Speed is the spatial/temporal local kinetic coefficient ratio, defined only where the temporal coefficient is nonzero. G and c are chosen photon coordinates fixed by σ. These coordinates are gauge- and scheme-dependent until an observable bridge is supplied.
3. Use a direct-sum norm such that \(\|X-\sigma X\|=2|\Delta|+E\), with Δ=v₁−v₂ and E the norm of all other exchange-odd components. E≥0 and E=0 at an exchange-fixed state. The definition presupposes such a coordinate splitting and norm.
4. \(B'=[v_-,v_+]\subset(0,\infty)\) is a compact interval containing each of v₁,v₂,c; Λ bounds below are over its entire product. Counterterms and the RG scheme must be exchange covariant for the symmetry argument.
5. Bounds on complex neighbourhoods refer to a scalar holomorphic coordinate map on the entire stated open set. For real positive bare coupling, all quantities compared by inequalities are real. A fixed neighbourhood radius is an added, strong hypothesis.
6. An N-independent constant is uniform in all allowed masses, bare speeds in the chosen set, T, and 0<G₀≤G*. The proposition's constant may first be written as a function of G₀ and then bounded using G*.
7. The continuum quartic statement uses a scalar cutoff on each of four identical propagators, or a prescribed difference of the resulting fourth powers. A general shell integration with mixed-scale propagators or lattice seagulls is not identified with this integral.

**Proposed target R1″-MOD[d].** For two equal unit charges, choose L, G*, a compact bare-speed set B and C,γ>0 independently of N. For each allowed m, G₀ and bare speeds, suitable counterterms and exact scale integration give
\[|\Delta_k|\le C(1+G_0k)^{-\gamma}|\Delta_0|\quad(0\le k\le N),\]
and δ_k=|Δ_k|+κE_k obeys δ_{k+1}≤(1−cG_k)δ_k in a window with N-independent end margins, for fixed c>0 and κ≥1. This is a proposed discrete consequence, not a replacement theorem for CN1's interpolation. Strict decrease requires δ_k>0.

**Proposed UB″.** Choose K,β,r,b_±>0, θ∈[0,1), k_m∈N, B′ and G*>0 uniformly. For each model datum an exchange-covariant exact integration R_k on 0≤k<N satisfies, with η_k=G_k²+G_ke^−βk+G_ke^−β(N−k):

- (U0) E₀≤K|Δ₀|; (U1) R_kσ=σR_k.
- (U2) On the open r-neighbourhood of [σX_k,X_k], \(\rho^{(k)}(Y)=[R_k(Y)]_{v_1}-v_1(Y)-hG(Y)F(v_1(Y),c(Y))\) is holomorphic and bounded by Kη_k for k<N−k_m, and by KG_k otherwise.
- (U3) E_{k+1}≤θE_k+KG_k²|Δ_k|.
- (U4) 1/G_k+b₋≤1/G_{k+1}≤1/G_k+b₊, with G_k>0.
- (U5) v₁(k),v₂(k),c(k)∈B′.

The exponential terms are intended to bound lattice and threshold corrections; their identification and the bounds themselves are open for M″. For mL^N≤1, the proposed O((mL^k)²) threshold factor is ≤L^−2(N−k), if that estimate is independently established. Exchange covariance removes a source at a completely exchange-fixed state, not every source independent of Δ when E≠0. U0 and U3 control the other odd data; they do not follow from symmetry alone.

## 2. Pair flow and discrete estimates

The imported one-loop flow of `CN1.md` §§3–5 gives increment hG_kq²F(v,c), with
\[
F(v,c)=\frac{(4s^2+3s+1)(1-s)}{6\pi^2(1+s)^2},\quad s=v/c,\qquad
F_s'(s)=-\frac{4s^2(s+3)}{6\pi^2(1+s)^3}<0. \tag{1}
\]
**Proof.** Substitute s=v/c into CN1's P(v,c)(c−v), expand the numerator as −4s³+s²+2s+1, and differentiate. □

Thus F(v₁,c)−F(v₂,c)=−ΛΔ, where Λ=c⁻¹∫₀¹|F′(s₂+t(s₁−s₂))|dt. On B′, 0<Λ_min≤Λ≤Λ_max; at v₁=v₂=c, Λ=1/(3π²c). The physical input is conditional on the ported one-loop coefficients, not an all-orders RG result.

**Theorem 1 (discrete pair contraction).** Fix λ,K,β,b₋,b₊>0, θ∈[0,1), k_m∈N and N>k_m. Let G_k>0, Δ_k∈R, E_k≥0 for 0≤k≤N, and suppose U4, plus
\[
\begin{aligned}
|\Delta_{k+1}|&\le(1-\lambda G_k+K\eta_k)|\Delta_k|+E_k &&(k<N-k_m),\\
|\Delta_{k+1}|&\le(1+KG_k)|\Delta_k|+E_k &&(N-k_m\le k<N),\\
E_{k+1}&\le\theta E_k+KG_k^2|\Delta_k|. 
\end{aligned}
\]
Set κ=2/(1−θ), K′=K(1+κ), δ_k=|Δ_k|+κE_k. If G₀≤1 and λG₀≤(1−θ)/2, then
\[
\delta_N\le C(G_0)(1+b_+G_0N)^{-\lambda/b_+}\delta_0,
\quad C(G_0)=(1+b_+G_0k_m)^{\lambda/b_+}
\exp\!\left[K'\left(G_0^2+G_0/b_-+\frac{2G_0}{1-e^{-\beta}}+k_mG_0\right)\right].
\]
If also K′G₀≤λ/4 and k_β is the least nonnegative integer with K′e^−βkβ≤λ/4, then δ_{k+1}≤(1−λG_k/4)δ_k for k_β≤k<N−max(k_β,k_m).

**Proof.** U4 gives G_k≤G₀ and κ(1−θ−λG_k)≥1. Thus in the bulk δ_{k+1}≤(1−λG_k+K′η_k)δ_k; in the last k_m steps δ_{k+1}≤(1+K′G_k)δ_k. Also
\[\sum_{k<N}G_k^2\le G_0^2+G_0/b_-,\quad
\sum_{k<N}G_ke^{-\beta k},\ \sum_{k<N}G_ke^{-\beta(N-k)}\le G_0/(1-e^{-\beta}),\]
and Σ_{k<n}G_k≥b₊⁻¹log(1+b₊G₀n). Multiply the step bounds, use 1+x≤eˣ, and replace n=N−k_m using (1+x(N−k_m))(1+xk_m)≥1+xN. In the window K′η_k≤3λG_k/4, proving the last assertion. □

**Lemma 2.** Let σ be a linear involution of a complex Banach space, and ρ holomorphic and bounded by M on the open r-neighbourhood of [σX,X]. Then |ρ(X)−ρ(σX)|≤(M/r)‖X−σX‖.

**Proof.** Cauchy's derivative estimate on every radius r′<r in every unit direction gives ‖Dρ‖≤M/r along the segment. Integrate the derivative along it. □

This gives a Lipschitz estimate from a strong analytic size hypothesis. `CN1_REFEREE.md` item 36 already proves the subsequent exchange-odd Lipschitz-to-pair-bound step; `CN1.md` Theorem 3 gives the continuous-flow analogue. Neither supplies U2 for M″.

**Lemma 3a (discrete box).** For n species and photon, suppose the one-step leading terms are
\[v_a^+=v_a+hGq_a^2P(v_a,c)(c-v_a)+\rho_a,\quad c^+=c+hG\sum_bn_bq_b^2R(v_b,c)(v_b-c)+\rho_0,\]
where P,R≥0 on B′×B′, each |ρ_a|,|ρ₀|≤K(G_k²D_k+φ_k), φ_k≥0 and Σφ_k≤Φ, and U4 holds. Let m₀>0,M₀ be the initial minimum and maximum, D₀=M₀−m₀, B′=[m₀/2,M₀+m₀/2],
\[\bar p=\max_{B'^2}\max\{\max_a q_a^2P,\sum_b n_bq_b^2R\},\quad
\bar D=e^{2K(G_0^2+G_0/b_-)}(D_0+2K\Phi).\]
If hG₀p̄≤1 and K[(G₀²+G₀/b₋)D̄+Φ]≤m₀/2, all speeds stay in B′ through N.

**Proof.** Until the first exit, each leading move is a convex combination of the current speeds. Hence D_{k+1}≤(1+2KG_k²)D_k+2Kφ_k. Discrete Grönwall and Theorem 1's square-sum estimate give D_k≤D̄. The accumulated perturbation of either endpoint is at most K[(G₀²+G₀/b₋)D̄+Φ]≤m₀/2. Induction prevents exit. □

This is the discrete counterpart of the box argument already in `CN1.md` Theorem 3. Its consensus-vanishing remainder premise is not implied by exchange symmetry; U2–U4 alone do not give it, so U5 remains an independent UB″ condition.

**Theorem 3 (conditional reduction).** Assume UB″ and suppose uniformly G*≤1, hG*Λ_max≤1, λG*≤(1−θ)/2, 3KG*≤r, and K₁(1+κ)G*≤λ/4, where λ=hΛ_min, κ=2/(1−θ), K₁=max(K,2K/r). Then the proposed R1″-MOD[d] holds with γ=λ/b₊ and constants independent of N. Specifically one may take
\[|\Delta_k|\le C_* (1+K)\kappa(1+b_+G_0k)^{-\lambda/b_+}|\Delta_0|,\]
where C_* is the uniform version of Theorem 1's C with K₁ and at least 2k_m in place of k_m. The window has the fixed margins from Theorem 1 with K₁.

**Proof.** U1–U2 and (1) give Δ_{k+1}=(1−hG_kΛ_k)Δ_k+ρ(X_k)−ρ(σX_k). Lemma 2 bounds the last term by (M_k/r)(2|Δ_k|+E_k), with M_k=Kη_k in the bulk and KG_k at threshold. Since η_k≤3G_k and 3KG₀≤r, Theorem 1's hypotheses hold with K₁; U3–U4 give the other inequalities. U0 yields δ₀≤(1+κK)|Δ₀|≤(1+K)κ|Δ₀|. At k=N use Theorem 1. For k<N, apply its product proof with the original N-dependent η: the start-side exponential sum is bounded as before and the end-side sum is also bounded by G₀/(1−e^−β). At most k_m threshold steps occur. When k≤k_m, or N≤k_m, use the crude factors directly; the enlarged C_* absorbs these finite steps. This also repairs the draft's unsupported assertion that the unmodified endpoint constant automatically works at every intermediate k. The common smallness of G* gives a fixed window. □

The theorem proves only UB″ ⇒ R1″-MOD[d]. It does not prove the converse or the original interpolated R1″-MOD. The bound is a power of N≈log_L(1/m), not a momentum power. The rate distinction is already proved for the marginal example in `LZ1I.md` Theorem 12; LZ1's R-P needs more.

## 3. Analyticity domains

**Proposition 4 (Cauchy obstruction).** If F is holomorphic on |z|<r, |F|≤B, and |F′(0)|≥αN−β for r,B,α>0 and β≥0, then N≤(B/r+β)/α.

**Proof.** Cauchy's estimate on every smaller disc gives |F′(0)|≤B/r. □

**Corollary 4′ (conditional one-loop obstruction).** Fix unequal bare speeds and suppose each Δ_N(z) is holomorphic near z=0, Δ_N(0)=Δ₀, and
\[\partial_z v_a(N)|_0=\sum_{k<N}hF(v_a,1)(1+\epsilon_k^a),\qquad \sum_k|\epsilon_k^a|\le c_1\]
uniformly in N. Then no fixed r,B>0 bound |Δ_N(z)|≤B|Δ₀| on |z|<r for all N.

**Proof.** By (1), Λ₀=−[F(v₁,1)−F(v₂,1)]/Δ₀>0. The derivative of Δ_N/Δ₀ at zero is −hΛ₀N+O(1). Proposition 4 contradicts an N-uniform disc bound. □

The first-order matching, including summability of lattice and mass corrections, is a hypothesis, not proved for M″ here. Likewise, if a coupling expansion has 1/G_N=1/z+Σ_{k<N}b_k+O(z) with Σb_k≥bN−c, then its second Taylor coefficient grows in magnitude and Cauchy's second-derivative estimate gives the same obstruction.

**Corollary 4″ (decay obstruction).** Suppose G_N is holomorphic and bounded by B on |z|<r, real on real z, G_N(0)=0 and G_N′(0)=1, uniformly in N. Then G_N(x)≥x/2 for 0≤x≤r²/(8B). Thus these fixed-disc hypotheses are incompatible with U4 for all N. Similarly, if F_N=Δ_N/Δ₀ is holomorphic and bounded by B on |z|<r, real on the real axis, and F_N(0)=1, then F_N(x)≥1/2 for 0≤x≤r/(4B). These hypotheses are incompatible with uniform decay |F_N(x)|≤C(1+xN)^−γ at fixed x>0.

**Proof.** Cauchy gives B≥r in the first case and B≥1 in the second. On |z|≤r/2, |G_N″(z)|≤8B/r² and |F_N′(z)|≤2B/r. Taylor's theorem gives the asserted lower bounds, within |z|≤r/2. U4 gives G_N(x)≤x/(1+b₋xN), which becomes <x/2 for N>1/(b₋x); the second decay also tends to zero. □

The obstruction requires a uniformly bounded holomorphic **observable or coordinate** on a fixed disc with the stated normalization. It neither rules out the real-axis flow nor proves that every possible bare-coupling representation has those properties.

**Proposition 5 (abstract tangent domain).** Let b>0, K≥0, C₀=K+2(b+K)² and r₀=min{1,b/(2C₀),1/[4(b+K)]}. Suppose complex G_{k+1}=G_k−bG_k²+R_k with |R_k|≤K|G_k|³ when |G_k|≤r₀. Then:

(i) If Re(1/G₀)≥1/r₀, Re(1/G_k)≥1/r₀+bk/2 and |G_k|≤(1/r₀+bk/2)⁻¹ for all k.

(ii) If all G_k are real and G₀=−t, 0<t≤r₀, some k≤2/(bt)+1 has |G_k|>r₀.

The set in (i) is the closed disc |G−r₀/2|≤r₀/2 with 0 removed.

**Proof.** For 0<|G_k|≤r₀ put w_k=1/G_k and u=bG_k−R_k/G_k. Then |u|≤1/4 and
\[|w_{k+1}-w_k-b|\le [K+2(b+K)^2]|G_k|\le b/2.\]
For (i), induction gives the lower bound on Re w and hence the upper bound on |G|. For (ii), if all iterates through ⌈2/(bt)⌉ stayed in the small region, real w would increase by at least b/2 per step from −1/t to a nonnegative value. It cannot cross from w≤−1/r₀ to w≥1/r₀ in a step of at most 3b/2<2/r₀. Contradiction. □

**GAP TD.** Proposition 5 controls an abstract recursion on a tangent disc; it does not prove the RG recursion or analyticity of all UB″ coordinates there. A fixed disc in a running variable is not equivalent to a tangent disc in the bare variable: the former contains small negative values while the latter does not. The full-disc obstruction does not establish that every proof must use running-coupling expansions. TD remains a proposed domain and its sufficiency is open.

## 4. Continuum quartic calculation

**Lemma 6.** Let v>0, p_v=(p₀,vp₁,vp₂,vp₃), Ã=(A₀,vA₁,vA₂,vA₃), A∈R⁴. Let \(\mathcal N\) be continuous, positive away from zero and positively homogeneous of degree one, and ψ measurable with ∫₀∞|ψ(t)|dt/t<∞. Then
\[\int_{\mathbb R^4}\psi(\mathcal N(p))\frac{\operatorname{tr}[(\not p_v\not{\widetilde A})^4]}{(p_v^2)^4}\,d^4p=0.\]

**Proof.** The Clifford relations give, for X=\not p\not a, X²=2(p·a)X−p²a² and
\[\operatorname{tr}X^4=32(p\cdot a)^4-32(p\cdot a)^2p^2a^2+4p^4a^4.\]
On S³, rotational invariance gives E(ω·e)²=1/4 and E(ω·e)⁴=1/8; these follow by dividing the second and fourth moments of a standard Gaussian coordinate by E|g|²=4 and E|g|⁴=24. Substitute p′=p_v and p′=ρω. Homogeneity makes the radial integral ∫ψ(t)dt/t independent of ω; absolute integrability justifies Fubini. The angular factor averages to |Ã|⁴(32/8−32/4+4)=0. □

For a constant field and four identical continuum propagators with scalar cutoff χ(\(\mathcal N\)), the formal box term is proportional to this integral with ψ=χ⁴ when integrable. A difference of two such terms also vanishes. **GAP:** this does not by itself establish the contribution of a general exact RG shell with mixed propagators, nor the lattice contribution with Peierls seagulls. The draft's numerical trace and Monte Carlo checks are reported in `CN1MOD_DRAFT.md` §4.5; they were not rerun and are not proof.

Cubic symmetry and charge conjugation allow Q(A)=Σ_μA_μ⁴−½(A·A)²; Q(e₁)=1/2 and Q((1,1,1,1)/2)=−1/4. Thus symmetry alone does not impose a positive quartic form. It does not establish that the actual generated lattice coupling has either sign.

## 5. Attacks, prior results and framework bridge

**Attack A: integrate out the massive Gaussian photon, then seek bounds analytic on a fixed bare-coupling disc uniform in N.** Corollary 4″ rules out this strategy if it yields the normalized uniformly bounded running coordinate or pair observable and the claimed real-axis decay. Corollary 4′ gives an alternative conditional obstruction from the one-loop coefficient. **GAP:** integrating out the photon does not logically force every useful expansion to give those fixed-disc bounds; renormalized or nonuniform representations are not excluded. Thus the draft's claimed unconditional defeat of attack 2 is too broad. Its original kernel scale-summability issue for the massless case is recorded in `CN1_OUTLINE.md` and `prior/CN1MOD.md`.

**Attack B: gauge-covariant block RG with background fermions.** Proposed plan: retain the photon, use covariant block averaging and small/large field decomposition, and bound fermion operators. **B1 (open):** prove the needed 3+1-dimensional analytic, exponentially decaying background-field block operators uniformly through N scales on the required complex small-field domain. A local axial-gauge Neumann expansion does not by itself control the transition functions between blocks. **B2 (open):** decouple the fermion integral across large-field regions. **GAP:** the supplied massive, gauge-fixed Gaussian action is not gauge invariant. Exact Ward identities, absence of a photon mass, and absence of all local quartic terms at each scale do not follow from gauge covariance of S_F; an explicit Stueckelberg completion or controlled modified Ward identities and a compatible RG must be supplied. The sign of the real one-loop beta function alone does not prove a constructive infrared flow. Pass 1's comparison to Balaban–O'Carroll–Schor and Dimock is a proposed route, not an imported theorem for this model.

**Attack C: non-covariant finite-range RG and polynomial localisation.** Proposed plan: decompose the photon covariance, track local relevant/marginal terms and an irrelevant polymer remainder. Candidate coordinates include fermion temporal and spatial kinetic and vertex terms, photon quadratic terms and symmetry-allowed quartics. **C1 (open):** control the effective bosonic interaction and regulator with the actual generated quartic terms. If a quartic polynomial is negative along a real field direction, exp(−V) grows quartically there and a purely Gaussian regulator cannot bound it uniformly along that direction. Lemma 6 and the symmetry example do not determine the lattice sign. **GAP:** this observation does not prove that every BBS-type norm requires a nonnegative localized quartic or that placing it in a remainder cannot be controlled by a different norm, localisation, cancellation or finite-field decomposition. Gauge-restoring cancellations for the massive gauge-fixed model also require proof. B1 and C1 are named unpassed steps, not impossibility theorems.

**Earlier attacks.** Attack 1, summing the all-orders renormalized expansion, and attack 4, convergence of the large-N expansion, remain open at the steps recorded in `CN1.md` and `CN1_OUTLINE.md`. Attack 2 is limited as under A. For attack 3, Lemma 2 supplies a Lipschitz estimate *assuming* a uniform complex-neighbourhood size bound; U2 remains open. It does not follow from Ward identities and symmetry alone.

**Already in the repository.** `CN1.md` Theorems 1–3 prove the corresponding conditional continuous star-flow alignment, equal-charge exponent and robust flow; Proposition 4 gives a persistent-source counterexample. `LZ1I.md` Theorems 11–12 give the integrated-drag and marginal-rate distinction. `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` gives one-loop Peierls matching and truncated-flow attraction for its supplied carrier, with higher-loop control open; the digest reports it unaudited. `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` gives the constant-coefficient exchange result under assumed positive drag, without deriving physical coefficients. `docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md` gives node-resolved truncated-flow contrasts, not omitted-order control. `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` gives a one-step high-mass polymer bound, not an invariant RG neighbourhood. `docs/NATIVE_INTERACTING_WEYL_PROTECTED_PATHS_BOUNDED_THEOREM_NOTE_2026-09-13.md` packages an imported finite-range Weyl theorem, not a dynamical-photon construction. These path citations follow the digest's supplied snapshot; they are not current audit claims. The pass-1 literature search and its unfetched sources are recorded in `CN1MOD_DRAFT.md` §2; no external construction is used as a proof here.

**Framework bridge.** M″ is a proposed supplied model for rung 1, not a realization of a live law. Rung 2 needs at least: (1) H-PHOTON and GA1-5-Φ as a photon cone; (2) GB1-U1 and a justified Gaussian limit of the finite link sector; (3) a framework regulator and N-uniform removal, with the target ultimately massless; (4) a reflection-positive Euclidean/transfer identification with the unitary tick, R2-a/H-TICK and ST1; and (5) an invariant observable meaning for the gauge-fixed speed coefficients, R1-OBS or another bridge. `TOE_ASSEMBLY.md` §3.6 keeps R-CS^str as an unadopted working candidate; §3.9's ZM1-INV comparison concerns invariant observables. None of these bridges follows from the mathematics above.

## 6. Proposed readings and four checks

The draft's tests ask: (1) whether a proposal fixes a target by stipulation, (2) whether it is closed rather than open-ended, (3) whether it settles downstream physics by premise, and (4) whether it adds unnecessary structure. P=pass, C=conditional, F=fail. These are proposed author-side assessments, not owner decisions.

| Proposal | Pass-1 checks 1–4 | Distillation check |
|---|---|---|
| M″ as supplied rung-1 model | P, P, P, C | P, C, P, C. The action is explicit, but counterterm choice, finite-volume zero modes and RG scheme remain open. The Wilson term and regulator are model choices. |
| R1″-MOD[d] as precise form of R1″-MOD | P, P, P, P | C, P, P, C. It is a proposed discrete target; it drops the original interpolation and does not prove equivalence. |
| UB″ as a sufficient sub-lemma | P, P, P, P | P, P, P, C. Theorem 3 proves sufficiency under its smallness hypotheses. U0–U5 are separate strong conditions, not one proved size estimate, nor shown necessary or minimal. |
| TD, tangent disc equivalently fixed running disc | P, P, P, P | P, C, P, F as stated. Proposition 5 only controls the abstract recursion; the domains are not equivalent and sufficiency for UB″ is open. |

The proposed CN1 amendment “R1″-MOD reduces to UB″; attacks A, B, C failed at Corollary 4″, B1, C1” is **not adopted**. The supported version is: UB″ plus the displayed smallness conditions implies R1″-MOD[d]; A is obstructed only under Corollary 4″'s fixed-disc hypotheses, and B1 and C1 remain unproved steps. No downstream file is amended here.
