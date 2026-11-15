# CH1-5O-E′: loop data and heat-kernel models

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (CH1_5OEP_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

**Proved under the stated inputs.** The large-register coherent-state lemma and its loop approximation (Theorems 1–2); cancellation of the tick by permitted inverse layers (Theorem 3); exact heat-kernel plaquette moments and their separation (Theorem 4); the conditional finite-data construction and a spatial random-link model witness (Theorem 5); its implication for the proposed 45-channel comparison (Corollary 5.1); and the finite-region Gauss-trace result (Theorem 6). These are author-side checks, not independent review or retained status.

**GAP.** Theorem 5 proves the comparison for the random-link model classes. The draft pins the frozen statement's classes by these models (`CH1_5OEP_DRAFT.md` lines 54 and 238); the record intends T0-start's classes (frozen `CH1_5OE.md` Definition 6). The draft does not show that the model measures lie in T0-start's class: reflection positivity, density in `𝒜_{k0}(g)` at `g ≤ g_*`, and T0-start's class for `SU(5)` and `Spin(10)` (T0-start[G]) are unchecked. So the model witness does not decide CH1-5O-E′ for T0-start's classes; Theorem 5's first part reduces that case to SEP[T0-start]. Theorem 5 gives the corrected model statement. A large-register limit does not establish the same result for `S_+`.

**Open.** CH1-5O-E′ with T0-start's classes; SEP[T0-start]; CH1-5O-E′[VC1]; HEAT; inherited, unchanged: CH1-5O-E, CH1-5O-i, CH1-5U-i, the R-A residual, AM, AM-5, CH1-i, CH1-ii, CG1-i, CG1-ii, CG1K-loc, CG1K-H, LW1-5-BG, LW1-5-X, GA1-P-5, Y2-W[`L5-O`], VC1, the formulation of IR and AM (`CH1.md` Definition 8), and T0-start[G] for `Spin(10)` and the candidate subgroup factors. No law is eliminated. No amendment or reading is adopted here.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af5d-8d1c-7c32-88ac-5aa243c851ea`. Pass 1: Claude Opus 5.5, `CH1_5OEP_DRAFT.md`. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model identity, reasoning effort and session ID are not visible in this session. Date 2026-11-06. HEAD at read `ccdafd71c76de792065d9eefb0c8c5d8dfdb1b75`; working files need not belong to that commit. SHA-256: draft `c33bb719917f377249c968bd0a4418771e85218d4833f661178950fc4b02f188`; frozen `CH1_5OE.md` `70dbb28f246343ddadf91c44998456927840ee4b9b2532b9ef83e758b92bd98a`; `CH1_5O.md` `053f1ecf4da057b46eaf70b0c0cb4ac9c6629898a125f6bc959016bb1ccd95e3`. The draft's floating-point and Monte Carlo checks are reports, not proofs; they were not rerun. Standard heat-kernel existence and Fourier formula, Peter–Weyl, Haar measure, product states, and the unique trace on the matter CAR algebra are inputs. Perelomov, Lieb and Simon are credited for coherent-state context; the present bounds are the draft's. `LIT_HIGGS.md` supplies context, not a physical identification. Referee closures R-HK (the heat-kernel measure), R-T (uniqueness of the matter trace) and R-C (continuity of coherent rays) in CH1_5OEP_REFEREE.md rebuild the cited inputs that Theorems 1, 2, 4 and 5 use. They are unrefereed.

**Editing provenance.** Codex `gpt-6.1-terra`, effort high, codex-cli 0.165.0, session `01a1af88-8910-7500-a9c9-2e2e750a746c`.

## 1. Definitions inferred by the distiller

1. The spatial lattice is `ℤ³`. `𝔄` is the quasi-local matter and link algebra. `G=Spin(10)` acts by local conjugations; `E` denotes the local Haar conditional expectation onto `𝔄^G`. The cell group is `𝒢=2ℤ³⋊O_{c₀}`, with the 24 proper cubic rotations about `c₀=(1,1,1)/2`. The cited `VC1_5.md` expectation commutes with cell lifts. Gauge invariance does not impose a Gauss-singlet sector.
2. On an oriented link `(x,y)`, `U^{ab}=iη^y_aη^x_b=2T_{a,10+b}`, with twenty Hermitian Majoranas and `{η_i,η_j}=2δ_{ij}`. Put `𝐔=Σ E_{ab}⊗U^{ab}`. The end actions rotate rows and columns by the vector map `R:G→SO(10)`. The central `ϖ∈G` maps to `−I`. A cell lift on a reversed link exchanges ends and sends `U^{ab}` to `−U^{ba}`. These action and lift identities, and the gate commutation facts, are inputs from `LW1_5.md` and `VC1_5.md`. `LW1_5.md` B1-5 and `VC1_5.md` Theorem 2.2 state the lifts for `S_+`. For another irreducible register with `τ_E=0` the same proof applies: the end swap `∏_a(η^y_a−η^x_a)/√2` lies in `Spin(20)` and acts on every `Spin(20)` register, and the proof of `VC1_5.md` Theorem 2.1 uses no property of the register (`CH1_5OEP_DRAFT.md` line 90).
3. A path here has distinct links. For a closed path `C` with ordered factors `X_i=𝐔` or `𝐔^T` according to orientation, define `Ŵ_C=(1/10)tr((X_n/k)⋯(X_1/k))`, with one factor `1/k` for each link. It is Hermitian and invariant because distinct link factors commute and adjacent gauge rotations cancel. Its classical value is `cl_u(C)=tr(u_C)/10`. Products may have overlapping paths, but each constituent path uses each link once.
4. A block link is a straight path of `m` fine spatial links; a skeleton loop uses each block link at most once. Fix a finite list `Λ` of such loops. The standard comparison sends each `Ŵ_C` to the normalized vector trace on the corresponding group-valued block loop. For products of at most two entries, including adjoints and both orders, `d_Λ` is the maximum absolute difference of expectations; distance to a class is the infimum. These are distances between finite data vectors, so the triangle inequality applies. The fixed-data clauses are (a′) distance at most `δ` to some `K`-measure and (b′) distance greater than `δ` to every `G`-measure.
5. An `L5-O` update has irreducible `so(20)` link registers and can include finitely many layers of local gauge-invariant gates (`CH1_5O.md` Definition 1). Cell covariance of extra layers is separate. The law's own tick is `U₀=W_E M_o M_e`; set `τ_E=0` for general registers unless the electric layer is specified. Stationarity means invariance under the resulting automorphism. This definition does not itself identify the VC1 state.
6. **Proposed, not adopted:** R-E′ compares pure-gauge T0-start small-field classes with fixed maps, normalization, scale, tolerance and nonempty precisely specified classes. The full admissibility conditions are not pinned here. The random-link classes below are proposed model classes only. Frozen `CH1_5OE.md` (Definition 6, line 22, and its R-E′ row, line 165) records that embedding the pure-gauge version in CH1-5O-E also depends on the `W=0` reading. Neither finite matching nor a stabilizer establishes the light spectrum or a unique effective group.

**Proposed normalization, not adopted (O1).** For a register `R`, let `κ_R` be the largest eigenvalue of `U^{11}` on `R`, and put `Ŵ_C=(1/10)tr((X_n/κ_R)⋯(X_1/κ_R))`. On `R_k^-`, `κ_R = k`: on `S_−^{⊗k}`, `U^{11}` is a sum of `k` commuting involutions, so its eigenvalues on `R_k^-` are at most `k`, and `φ₀^{⊗k} ∈ R_k^-` has eigenvalue `k`. On `S_+`, `κ_R = 1` (referee closure, CH1_5OEP_REFEREE.md).

## 2. Coherent registers

**Theorem 1 (draft Lemma K).** Let `S_−` be the half-spin representation of `Spin(20)` with chirality convention of `LW1_5.md`. The commuting involutions `U^{aa}` have one-dimensional joint eigenspaces on the full spinor space. Their joint `+1` vector `φ₀` lies in `S_−`. For `k≥1` let
\[
R_k^- = \operatorname{span}\{\rho(h)^{\otimes k}\phi_0^{\otimes k}:h\in Spin(20)\}.
\]
It is irreducible. The link operators on it are sums over the `k` copies. For every `O∈SO(10)` there is a continuous ray `ψ_O` with
\[
\langle\psi_O,\mathbf U\psi_O\rangle=kO,\quad
\|(\mathbf U/k-O)(v\otimes\psi_O)\|=\|((\mathbf U/k)^T-O^T)(v\otimes\psi_O)\|=3\|v\|/\sqrt{k},
\]
and `‖𝐔/k‖≤10`. End gauge actions send the ray to `ψ_{R(g)O}` and `ψ_{OR(g)^T}`; the end swap sends it to `ψ_{−O^T}`.

*Proof.* Let `d_a=(η^y_a+iη^x_a)/2`. The ten CAR number operators obey `U^{aa}=2d_a†d_a−1`; their joint eigenspaces are lines. The product of the `U^{aa}` is the negative of the stated chirality product, since its ordering has 45 inversions. Hence `φ₀∈S_−`. Off-diagonal `U^{ab}` anticommutes with `U^{bb}`, so its expectation in `φ₀` vanishes. In the squared norm of `(𝐔−I)(v⊗φ₀)`, cross terms vanish by the same involution and the nine diagonal contributions give `9‖v‖²`. The transpose is identical with the ends exchanged. Moreover `(𝐔†𝐔)_{ab}=10η^x_aη^x_b`; with `Γχ=Σ_a e_a⊗η^x_aχ`, `Γ†Γ=10I`, so `‖𝐔‖=10` on the full half-spin space, and the triangle inequality gives the bound on `R_k^-`.

`η^x_aφ₀=−iη^y_aφ₀`, so `(L_y^{cd}+L_x^{cd})φ₀=0`. The diagonal `Spin(10)` fixes `φ₀`. The top eigenspace of `Σ_a U^{aa}` in the tensor product is the unique line `φ₀^{⊗k}`, with eigenvalue `10k`. In any orthogonal decomposition of the orbit span into invariant summands, the projections of that vector lie in the same top eigenspace; only one can be nonzero. Its summand contains the orbit, proving irreducibility.

Choose a target-end lift of `O` and apply it to `φ₀^{⊗k}`. The two lifts differ by the spin centre, which acts as a scalar, so the ray is well defined; `|ψ_O⟩⟨ψ_O|=p(N_O)`, with `N_O=Σ_{ab}O_{ab}U^{ab}` and `p` the Lagrange polynomial of the top eigenvalue `10k`, so the ray is continuous (referee closure R-C, CH1_5OEP_REFEREE.md). Covariance gives its mean. At `O=I`, the `k` centered fluctuations have zero cross terms by product factorization and zero one-copy means; the one-copy norm is 3. Rotation gives both displayed identities. The diagonal stabilizer gives the source action. The end swap is the spin lift `∏_a(η^y_a−η^x_a)/√2`; its conjugation exchanges the end Majoranas and sends `U^{ab}` to `−U^{ba}`. It maps `φ₀` to the all-minus joint eigenvector, which is `ρ(ϖ_y)φ₀` up to a phase, and it carries the target-end group onto the source-end group. So it maps `ψ_O` to a source rotation of `ρ_k(ϖ_y)φ₀^{⊗k}`. The diagonal stabilizer turns this into a target rotation of `φ₀^{⊗k}`, a coherent ray, and its mean is `−kO^T`. So the image is `ψ_{−O^T}` (referee closure R-S, CH1_5OEP_REFEREE.md). □

## 3. Loop approximation and stationarity

**Theorem 2 (draft Theorem U).** Let `ν` be any probability law on `SO(10)` values on spatial fine links. Put the register `R_k^-` on each link. Let `Φ_u` be the product of the coherent link states, `τ` the matter trace, and
\[
\omega=(\tau\otimes\int\Phi_u\,d\nu(u))\circ E,\qquad
\epsilon=(1+3/\sqrt k)^N-1.
\]
For loops of at most `N` links, the one-loop error against `ν` is at most `ε`, and the two-loop error at most `3ε` if `ε≤1`. For `q≥1`, the error of a product of `q` such loops is at most `q·10^{N(q−1)}ε`. The state is gauge invariant. If `ν` is invariant under geometric cell actions, with transpose on reversed links, it is also cell symmetric.

*Proof.* Continuity of the coherent rays makes each local integrand measurable and bounded. Consistent local product states and integration define a state. Haar averaging makes it gauge invariant and leaves invariant observables fixed.

For a fixed configuration write each normalized link factor as `O_i+Δ_i`. Expand the product. When `Δ_i` acts, the factor on its link is still coherent because the path has distinct links. Theorem 1 bounds that action by `3/√k`; the classical factors have norm one. Thus the loop applied to the product vector differs from its classical value times that vector by at most `ε`. Taking an inner product proves the one-loop bound. For two Hermitian loops write their vectors as `cΦ+e`, `c′Φ+e′`; `|c|,|c′|≤1` and the error is at most `2ε+ε²≤3ε`. For `q` loops telescope the product and use `‖Ŵ_C‖≤10^N`. Integrate.

The lift replaces a reversed link value by `−u^T`, not just `u^T`. Write the linear part of `g` as `Qe_j=ε_je_{π(j)}`. The reversed image links are the links in the directions of `J:={π(j):ε_j=−1}`. Put `σ_x=(−1)^{Σ_{i∈J}x_i}`. The unwanted link sign is `σ_xσ_y`, produced by the local central gauge transformations at sites with `σ_x=−1`. On a local gauge-invariant observable their product acts trivially. The matter trace is automorphism-invariant, and `E` commutes with the lifts. Geometric invariance of `ν` therefore gives cell symmetry. □

**Theorem 3 (draft Lemma I).** For any irreducible register and allowed constants, take `τ_E=0` unless the electric layer is defined. The tick followed by `W_E^{-1}`, `M_o^{-1}`, then `M_e^{-1}` is an allowed update and is the identity. Every state is stationary for it. Each inverse layer has the covariance of its original layer.

*Proof.* Each original cube or electric gate commutes with local gauge unitaries, so its inverse does too. Gates in each layer have the same disjoint supports as the original layer. Their inverse layers are local automorphisms, including at infinite volume. Their composition is `M_e^{-1}M_o^{-1}W_E^{-1}=U₀^{-1}`. Thus the total automorphism is the identity. Cell lifts that permute an original layer also permute its inverse. □

The conclusion concerns the stated broad update class. It does not prove stationarity under the law's own tick or select a vacuum. For `L5-U`, the same cancellation proof applies if its tick and added inverse layers satisfy the same local gate and class hypotheses.

## 4. Heat-kernel comparison

**Definition.** For `G=Spin(10)` or the lift `K≅SU(5)⊂Spin(10)`, use the Lie algebra metric `−tr₁₀(XY)/2`. Let `p_t^G` be the heat-kernel probability law with `∫ρ(g)dp_t=exp(−tC_ρ/2)`. Define `RL(G;σ_*)` as the gauge averages at all block sites of independent link laws `p_σ^G`, `0<σ≤σ_*`. On a finite window these have positive smooth Haar densities. The heat-kernel convolution law makes the holonomy of a four-link plaquette have law `p_{4σ}`. These are precisely defined pure-gauge **models**, not established T0-start classes.

**Theorem 4 (draft Lemma HK).** For `w=tr R(g)/10`,
\[
\begin{aligned}
G=Spin(10):&\quad Ew=e^{-9t/2},\quad Ew^2=F(Ew),& F(x)&={1+45x^{16/9}+54x^{20/9}\over100},\\
K\cong SU(5):&\quad Ew=e^{-12t/5},\quad Ew^2=Q(Ew),& Q(x)&={2+48x^{25/12}+30x^{7/3}+20x^{3/2}\over100}.
\end{aligned}
\]
For `0<s<840/31775`,
\[
Q(e^{-s})-F(e^{-s})\ge {s^2(840-31775s)\over21600}>0.
\]
For `x=e^{-s}`, every `x′∈[0,1]` has `max(|x′−x|,|F(x′)−Q(x)|)≥(Q(x)−F(x))/3`.

*Proof.* The moments are normalized traces of `exp(−tC/2)` on the vector and its tensor square. For `so(10)`, the orthonormal generators `E_{ij}−E_{ji}` give vector Casimir 9. On the tensor square, `C=18−2K₀+2P`, with flip `P` and `K₀=10|Ω⟩⟨Ω|`. Its eigenvalues are 0, 16, 20 with multiplicities 1, 45, 54.

For `su(5)`, the metric is `−tr₅(XY)`. Completeness gives `Σ T_A⊗T_A=−P+1/5` on `V⊗V` and vector Casimir `24/5`. The complexified real vector is `V⊕V̄`. The tensor-square Casimirs are 0, 10, `56/5`, `36/5` with multiplicities 2, 48, 30, 20. Substitution yields the two formulas.

Use `1−a+a²/2−a³/6≤e^{-a}≤1−a+a²/2` for `a≥0`, lower-bounding the positive terms in `Q` and upper-bounding those subtracted in `F`. The constant and linear terms cancel; 100 times the difference is at least `(35/9)s²−(31775/216)s³`. Finally `0≤F′(x)≤2` on `[0,1]`, so the last inequality follows from the triangle inequality. □

At `s=1/60` the lower bound is `18625/4665600000>3.99·10^{-6}`; one third exceeds `1.33·10^{-6}`. The small-time ratio of plaquette variances at matched means tends to `45/24`. This is a property of these heat-kernel laws, not a count inferred from gauge invariance alone.

**Theorem 5 (corrected draft Theorem W).** Fix `Λ,δ` as in Definition 4. Suppose a `K`-class measure `μ` is at distance strictly greater than `δ` from the `G` class. Then an allowed identity update and a stationary invariant state satisfy (a′) and (b′). If a geometrically cell-invariant spatial fine-link configuration law has the same finite data as `μ`, the state is also cell symmetric.

For the spatial models `RL(K;σ_*)`, `RL(G;σ_*)`, take the Case I subgroup `H` with `(a,b)=(2,−3)`, `K≅SU(5)`, any spatial block scale and finite skeleton list containing a plaquette. A cell-symmetric witness exists for
\[
0<\delta<\sup_{0<s\le48\sigma_*/5,\ 31775s<840}
{s^2(840-31775s)\over64800}.
\]
In particular `σ_*≥1/576` permits `δ=10^{-6}`.

*Proof.* Choose `η>0` below both `δ` and the strict separation margin. The block configuration of one time slice, mapped by `R`, can be subdivided by putting each block-link value on one fine link and identity on the others. Theorem 2 approximates its finite data within `η` for large `k`. Theorem 3 makes the state stationary. The triangle inequality proves both clauses. If an invariant fine-link law has the same data, use it instead; Theorem 2 gives cell symmetry.

For the model, `i diag(2,2,2,−3,−3)` is traceless, so the connected Case I group lies in the closed proper `SU(5)` lift. Choose `s` in the displayed range with `s²(840−31775s)/64800>δ`, which exists because `δ` is below the supremum, and put `σ=5s/48`. The subgroup plaquette has first moment `e^{-s}`. Theorem 4 separates its first two moments from those at every full-group heat-kernel time by more than `δ`. Realize its data with independent fine links of law `R_*p^K_{σ/m}`. Heat-kernel convolution gives the desired independent block links; inversion invariance gives cell invariance. The first part applies. For the numerical choice, use `s=1/60`. □

A concrete spatial instance takes `r=a`, a finite plaquette list, `σ_*=1/576`, `δ=10^{-6}`, and `k=10^{18}`. With `η=10^{-7}`, `(1+3/√k)^4−1<1.3·10^{-8}`, so the two-loop error is below `η`. The fine-link law is `R_*p^K_{1/576}` and the update is the tick followed by its inverse layers. The resulting moments are within `η` of `e^{-1/60}` and `Q(e^{-1/60})`; the full-group model cannot match both within `δ`.

**GAP in the draft's conclusion.** The preceding theorem proves separation for the named random-link models, not membership in T0-start's class or satisfaction of every frozen small-field condition. Conditional on that identification it supplies the finite comparison; without it CH1-5O-E′ remains open for T0-start's classes. The lists are spatial skeleton loops read in one time slice. This matches the frozen data, whose list consists of equal-time invariant observables (`CH1_5O.md` line 175).

**Corollary 5.1 (draft Corollary G).** Suppose K45 asserts that, for every allowed update and stationary invariant state, `d_Λ(ω,C(G))≤d_Λ(ω,C(K))`. Then every `μ∈C(K)` lies in the closure of the `G`-class finite data. If K45 is restricted to cell-symmetric states, this conclusion holds for each `μ` realized by a cell-invariant fine configuration law. K45 is false for the spatial random-link models, even with cell symmetry.

*Proof.* Theorems 2–3 give states `ω_η` with `d_Λ(ω_η,μ)≤η`. K45 and the triangle inequality give `d_Λ(μ,C(G))≤2η`; let `η→0`. Theorem 5 supplies a strictly separated model measure and the required cell-symmetric approximants. □

## 5. Proposed readings and open attacks

The four tests in `CH1_5O.md` ask whether an item fixes a listed target, is open-ended, settles a downstream question by premise, or adds unnecessary structure. The draft's assessments, not owner decisions, are:

| Item | Test results and scope |
|---|---|
| Existing update class in an existence claim | Test 1 pass; 2, 3, 4 fail in the draft's assessment: inverse layers make stationarity vacuous. The identity result is Theorem 3; whether the class should be changed is a separate decision. |
| `RL(G;σ_*)` | Tests 1, 2 and 4 pass as a closed model family; test 3 passes as a model but fails as an asserted stand-in for T0-start. Full T0 admissibility is unchecked. The same metric and prescription are used on both groups. |
| `R_k^-`, e.g. `k=10^{18}` | Tests 1–4 pass in the draft's assessment as an instance of free `R`, chosen to meet a bound. It does not establish the dynamics. |

**CH1-5O-E′[VC1] (proposed, open).** For some permitted law data and fixed T0-start comparison data, the state supplied by VC1 for the law's own tick satisfies both (a′) and (b′). VC1, GA1-P-5 and Y2-W[`L5-O`] remain open. Theorem 5 supplies kinematics, not this state or its stationarity.

**C1, correlation-channel count.** The proposed inference from invariant moment tensors to a fixed 45-direction gauge-invariant ratio fails: the cell-symmetric model states of Theorem 5 are exactly invariant while approximating the separated `SU(5)` moments. This is a finite-data counterexample, not a classification of all correlations.

**C2, twisted-box free energy.** The proposed step from a unitary tick and a state to a twisted-box free energy lacks a specified Euclidean weight or partition function. Finite loop-polynomial data instead obey Theorem 2. For a nonempty finite set of links, the product of the central end operators has zero expectation in these coherent mixtures: it maps each affected coherent ray to its orthogonal `ψ_{−O}` ray, distinguished by the eigenvalues `±k` of a rotated diagonal link operator. This observation does not exclude other twist diagnostics.

**C3, Ward identities.** Local invariance gives `ω([𝒢_x^{cd},A])=0`, but the inference to one massless physical channel per generator is unsupported. In the product-link model, gauge-invariant loops on disjoint link sets factor exactly before and after averaging; their connected correlation is zero. The model witness also obeys all the Ward identities. This does not prove a spectral theorem for the law's tick.

**C4, Floquet heating.** The proposed kill stops at **HEAT**, the unproved assertion that every stationary, gauge-invariant, cell-symmetric state of the law's own tick, with its plaquette layer and without inverse cancellation, has the finite-region Gauss-trace form below. HEAT is false for the identity update of Theorem 3, by the nonzero-plaquette state in Theorem 5. It is neither proved nor refuted here for the law's own tick. Heating literature is context, not proof of HEAT.

**Theorem 6 (draft Proposition Z).** On a finite region let `𝔊` be the algebra generated by the local gauge unitaries acting on its matter and internal links. For any finite-dimensional `Spin(20)` register, any `Z∈𝔊`, and any nonempty closed path with distinct links in the region, `tr(ZW_C)=0`. Hence any state whose every finite restriction is `tr(Z_Λ·)` for `Z_Λ∈𝔊_Λ` has zero such loop expectations. The analogous conclusion holds for `L5-U`: conjugation by the central element `e^{iθ}`, `θ∉2πZ`, of a target-end `U(5)` multiplies each link factor by a nontrivial phase (referee closure, CH1_5OEP_REFEREE.md).

*Proof.* The gauge algebra is the linear span of products of site gauge unitaries. Trace one such product times the loop. Matter and link traces factor. On any loop link the factor is `tr(ρ(h)U^{ab})`, where `h` is a product of end-group elements. The target-end `ϖ` commutes with `h` and conjugates `U^{ab}` to `−U^{ab}`. Cyclicity makes the trace its own negative. Thus every summand vanishes. A nontrivial central phase gives the same argument for the stated `L5-U` case. □

If HEAT holds and a comparison class has `inf_μ|E_μ w_p|>δ`, Theorem 6 makes (a′) fail for its VC1 state, as in `CH1_5O.md` R8. This is conditional on HEAT and the class bound. The dark state `ω₀` of `CH1_5O.md` Theorem 12 has the finite-region Gauss-trace form on every finite region: `ω₀=tr(Q_Λ·)/tr(Q_Λ)`, with `Q_Λ∈𝔊_Λ` the projection onto `𝔊_Λu_Λ` (referee closure R-Z, CH1_5OEP_REFEREE.md). So it does not refute HEAT. Its vanishing vector loops are separately established in the cited frozen source; they do not prove HEAT.

**SEP[T0-start] (open).** For fixed T0-start classes and comparison data, find a `K`-class measure at distance greater than `δ` from the `Spin(10)` class, whose finite spatial data have a cell-invariant fine-link realization. Theorem 5 would then supply the stated existence comparison, subject to the class identification. This is a sufficient condition; necessity is not shown.

C1–C3 fail only at the specified inference steps. C4 remains conditional on HEAT. A proposed numerical guide is to compare time-averaged plaquette moments under the base tick on a small finite box with `F` and `Q`; it would not prove the infinite-volume claim. Both `L5-O` and `L5-U` remain live under `TOE_ASSEMBLY.md` §3.5.


## 6. Imported referee closures

These closures are unrefereed. They are imported from `CH1_5OEP_REFEREE.md` section 4.

### R-Z. The dark state is Gauss-tracial on every finite region (repairs G3)

(referee closure, CH1_5OEP_REFEREE.md)

**Statement.** On `L5-O[S_+]`, let `Φ₀` be the dark product state (matter Fock vacuum, rishon vacuum on each link) and `ω₀ = Φ₀∘E` (`CH1_5O.md` Theorems 11-12). Let `Λ` be a finite set of sites, with `ℋ_Λ` and `𝔊_Λ` as in Theorem 6, and let `u_Λ` be the vector of `Φ₀` on `ℋ_Λ`. Let `Q_Λ` be the orthogonal projection onto `𝔊_Λu_Λ`. Then `Q_Λ ∈ 𝔊_Λ`, and `ω₀(A) = tr(Q_ΛA)/tr(Q_Λ)` for every operator `A` on `ℋ_Λ`. So `ω₀` has the form of Theorem 6 on every finite region, with `Z_Λ = Q_Λ/tr(Q_Λ)`.

*Proof.* **Step 1 (`CH1_5O.md` R5 with `S = Λ`, rebuilt).** Fix `x ∈ Λ` and `j ∈ {1,…,5}`. The Gauss generator is `𝒢_x^{2j−1,2j} = M_x^{2j−1,2j} + Σ_{ℓ∋x}L^{2j−1,2j}_{ℓ,x}` (`LW1_5.md` line 83). Each term is `i/2` times the product of the two Majoranas of one mode, so it is that mode's number minus `1/2`: `n_{x,j} − 1/2` for the matter (`LW1_5.md` line 31: "`n_j−1/2=M^{2j−1,2j}`"), and `n^{ℓ,x}_j − 1/2` for the rishon mode `j` at the `x`-end of `ℓ`, by the same Clifford computation. Let `H_{x,j}` be the sum of the terms that act on `ℋ_Λ`, that is, the matter term and the links at `x` with both ends in `Λ`. The other terms act on links with one end in `Λ`, outside `ℋ_Λ`. An operator `T` on `ℋ_Λ` that commutes with every `V_x(g)` commutes with `e^{itH_{x,j}}` for all `t`, hence with `H_{x,j}`. Let `d_x` be the number of links at `x` inside `Λ`. Then `H_{x,j} + (1+d_x)/2` is a sum of commuting number operators. The joint kernel of all of them is the set of vectors of `ℋ_Λ` with every mode empty: each mode of `ℋ_Λ` is a matter mode at a site of `Λ` or a rishon mode at an end of a link inside `Λ`. The empty vector of a link has even rishon parity, so it lies in `S_+`. So the joint kernel is the line of `u_Λ`. `T` keeps this line, so `Tu_Λ = ⟨u_Λ,Tu_Λ⟩u_Λ`.

**Step 2 (the trace form).** Write `V(γ) = ∏_{x∈Λ}V_x(γ_x)` on `ℋ_Λ`, for `γ ∈ Γ := Spin(10)^Λ`. For `A` on `ℋ_Λ`, `E(A) = ∫_Γ V(γ)AV(γ)^*dγ`, since the parts of `V_x(g)` on links with one end in `Λ` commute with `A`. `E(A)` commutes with `𝔊_Λ`. Step 1 gives `E(A)u_Λ = λ(A)u_Λ`, with `λ(A) = Φ₀(E(A)) = ω₀(A)`. For `B ∈ 𝔊_Λ`, `E(A)Bu_Λ = BE(A)u_Λ = λ(A)Bu_Λ`. So `E(A)` acts on `K := 𝔊_Λu_Λ` as the scalar `λ(A)`. `K` is `𝔊_Λ`-invariant and `𝔊_Λ` is `*`-closed, so `Q_Λ` commutes with `𝔊_Λ`, hence with every `V(γ)`. So `E(A)Q_Λ = λ(A)Q_Λ` and `E(A)Q_Λ = E(AQ_Λ)`. Each conjugation by `V(γ)` keeps the trace, so `tr E(AQ_Λ) = tr(AQ_Λ)`. Hence `ω₀(A)·tr(Q_Λ) = tr(Q_ΛA)`, and `tr(Q_Λ) ≥ 1`.

**Step 3 (`Q_Λ ∈ 𝔊_Λ`).** Every `T` that commutes with `𝔊_Λ` maps `K` into `K`: `TBu_Λ = BTu_Λ`, a multiple of `Bu_Λ` by Step 1. The set of such `T` is `*`-closed, so `Q_Λ` commutes with it. So `Q_Λ` lies in the double commutant of `𝔊_Λ`, which is `𝔊_Λ` by the lemma below. ∎

**Lemma (double commutant in finite dimension).** Let `𝔐` be a unital `*`-subalgebra of the operators on a finite-dimensional space `ℋ`. Then `𝔐″ = 𝔐`. *Proof.* Let `X ∈ 𝔐″` and `ξ ∈ ℋ`. The subspace `𝔐ξ` contains `ξ` and is `𝔐`-invariant. `𝔐` is `*`-closed, so the projection `P` onto `𝔐ξ` lies in `𝔐′`. Then `Xξ = XPξ = PXξ ∈ 𝔐ξ`. Apply this to `ℋ^{⊕n}` with `n = dim ℋ`, to the algebra of diagonal copies `M⊕⋯⊕M` (`M ∈ 𝔐`), and to `ξ = (e_1,…,e_n)` for a basis `(e_i)`. The commutant of that algebra consists of the `n×n` matrices with entries in `𝔐′`, and `X⊕⋯⊕X` commutes with all of them. So `(X⊕⋯⊕X)ξ = (M⊕⋯⊕M)ξ` for some `M ∈ 𝔐`. That says `Xe_i = Me_i` for every `i`, so `X = M`. ∎

**Consequence.** With Theorem 6, R-Z gives `ω₀(W_C) = 0` for every closed path with distinct links inside a finite region. This agrees with `CH1_5O.md` Theorem 11. R-Z concerns one state. HEAT stays open.

### R-HK. The heat-kernel measure (rebuilds the input of Theorems 4 and 5)

(referee closure, CH1_5OEP_REFEREE.md)

**Statement.** Let `G` be `Spin(10)` or `SU(5)~`, with the inner product `⟨X,Y⟩ = −tr_10(XY)/2` on its Lie algebra `𝔤` (read through `R`). For each `t > 0` there is exactly one Borel probability measure `p_t` on `G` with `∫ρ dp_t = e^{−tC_ρ/2}` for every smooth finite-dimensional unitary representation `ρ`, where `C_ρ = −Σ_Adρ(T_A)^2` over an orthonormal basis `(T_A)`. Moreover `p_s∗p_t = p_{s+t}`, and `p_t` is invariant under `g ↦ g^{−1}`.

*Proof.* **Uniqueness.** `Spin(10)` acts faithfully and unitarily on the 32-dimensional spinor module of its Clifford algebra, and `SU(5)~ ⊂ Spin(10)` is closed. So `G` is a closed subgroup of a unitary group. The polynomials in the entries of this representation and of its conjugate form an algebra of continuous functions. It contains the constants, separates points and is closed under conjugation. By the Stone-Weierstrass theorem it is dense in `C(G)`. Each such polynomial is a linear combination of matrix coefficients of tensor products of the representation and its conjugate. So two probability measures with the same integrals of every `ρ` agree on a dense subset of `C(G)`. By the Riesz-Markov theorem they are equal.

**Existence.** Let `X = Σ_Aξ_AT_A` with independent standard Gaussians `ξ_A`, and let `μ_s` be the law of `exp(√s X)`. Each `Ad_g` is orthogonal for `⟨,⟩`, so the law of `X` is `Ad`-invariant. Fix an irreducible `ρ`. Then `M(s) := ∫ρ dμ_s = E[exp(√s dρ(X))]` commutes with `ρ(G)`, and so does `C_ρ`. By Schur's lemma, `M(s) = c(s)·1` and `C_ρ = κ·1`. For anti-Hermitian `Y`, `‖e^Y − 1 − Y − Y^2/2‖ ≤ ‖Y‖^3/6`, by the spectral theorem and `|e^{iθ} − 1 − iθ + θ^2/2| ≤ |θ|^3/6`. Also `E dρ(X) = 0` and `E dρ(X)^2 = −C_ρ`. So `c(s) = 1 − sκ/2 + r(s)` with `|r(s)| ≤ s^{3/2}E‖dρ(X)‖^3/6`. `X` and `−X` have the same law, so `c(s)` is real. The convolution power `ν_n := μ_{t/n}^{∗n}` has `∫ρ dν_n = c(t/n)^n·1`, which tends to `e^{−tκ/2}·1`. The probability measures on the compact metric space `G` are weak-* sequentially compact. A limit point `p` of `(ν_n)` has `∫ρ dp = e^{−tC_ρ/2}` for each irreducible `ρ`, since matrix coefficients are continuous. Complete reducibility extends this to every `ρ`. By uniqueness, `p_t := p` is the limit of the whole sequence.

**Semigroup and inversion.** `∫ρ d(p_s∗p_t) = (∫ρ dp_s)(∫ρ dp_t) = e^{−(s+t)C_ρ/2}`. `C_ρ` is Hermitian, so `∫ρ(g^{−1})dp_t(g) = (e^{−tC_ρ/2})^* = e^{−tC_ρ/2}`. Uniqueness gives both claims. ∎

**Scope.** Theorems 4 and 5 use exactly these properties: the Fourier formula for `R` and `R⊗R`, the semigroup law, inversion invariance, and images under the homomorphism `R` (computed as `ρ∘R` on `G`). No proof uses positivity or smoothness of a density.

### R-T. Uniqueness of the matter trace (rebuilds the input of Theorem 2)

(referee closure, CH1_5OEP_REFEREE.md)

The matter algebra is the norm closure of the algebras of finite sets of sites (`VC1_5.md` line 18). Each of these is a full matrix algebra (`LW1_5.md` line 33: "The site algebra is `M_32(C)`"; `n` sites give `M_{32^n}(C)`). On `M_N(C)` with matrix units `E_{ij}`, a tracial state `τ` obeys `τ(E_{ij}) = τ(E_{i1}E_{1j}) = τ(E_{1j}E_{i1}) = δ_{ij}τ(E_{11})` and `Σ_iτ(E_{ii}) = 1`. So `τ = tr/N`. Two tracial states of the matter algebra therefore agree on every finite-site algebra, hence everywhere. For an automorphism `β` of the matter algebra, `τ∘β` is tracial, so `τ∘β = τ`. ∎

### R-C. The coherent ray is well defined and continuous (rebuilds an input of Theorems 1 and 2)

(referee closure, CH1_5OEP_REFEREE.md)

On `R_k^-` put `N := Σ_aU^{aa}` and `N_O := Σ_{ab}O_{ab}U^{ab}` for `O ∈ SO(10)`. Let `h` be a target-end element with `ρ_k(h)^{−1}U^{ab}ρ_k(h) = Σ_cO_{ac}U^{cb}`. Solving gives `ρ_k(h)U^{cb}ρ_k(h)^{−1} = Σ_aO_{ac}U^{ab}`, so `ρ_k(h)Nρ_k(h)^{−1} = N_O`. On `S_−^{⊗k}`, `N` is a sum of `10k` commuting involutions, so its spectrum `σ` on the invariant subspace `R_k^-` is a finite set of integers. Its top eigenvalue there is `10k`, on the line of `φ₀^{⊗k}` (Theorem 1's proof). So `N_O` has spectrum `σ`, and its top eigenspace is the line of `ρ_k(h)φ₀^{⊗k}`. Let `p(t) = ∏_{λ∈σ, λ≠10k}(t−λ)/(10k−λ)`. Then `|ψ_O⟩⟨ψ_O| = p(N_O)`. The right side depends on `O` alone, and it is a polynomial in the entries of `O`. So the ray is well defined and continuous in `O`. Each `Φ_u(A)`, for local `A`, is then a polynomial in finitely many link values, hence measurable and bounded. ∎ `[check]` (1f) tests coherence by this criterion.

### R-S. The end swap (completes item 17)

(referee closure, CH1_5OEP_REFEREE.md)

Let `s̃ = ∏_{a=1}^{10}v_a` with `v_a = (η^y_a − η^x_a)/√2`. Each `v_a` is a unit Clifford vector, and `v_awv_a = −r_a(w)` for every Clifford vector `w`, where `r_a` is the reflection that exchanges `e_a` and `e_{10+a}`. The ten reflections commute and the ten signs cancel. So conjugation by `s̃` exchanges `η^y_a` and `η^x_a` for every `a`. `s̃` is a product of an even number of unit vectors, so `s̃ ∈ Spin(20)`. Hence `s̃U^{ab}s̃^{−1} = iη^x_aη^y_b = −U^{ba}`, and conjugation by `s̃` carries the target-end group onto the source-end group. `s̃^2 = ±1`, so `s̃^{−1}U^{aa}s̃ = −U^{aa}` too, and `s̃φ₀` is the all-minus joint eigenvector. So is `ρ(ϖ_y)φ₀`, since conjugation by `ϖ_y` sends `U^{aa}` to `−U^{aa}`. The joint eigenspace is a line, so `s̃φ₀ = cρ(ϖ_y)φ₀` with `|c| = 1`. Let `ψ_O = ρ_k(h)φ₀^{⊗k}` with `h` in the target-end group, and put `h′ := s̃hs̃^{−1}`, in the source-end group. Then `ρ_k(s̃)ψ_O = c^kρ_k(h′)ρ_k(ϖ_y)φ₀^{⊗k} = c^kρ_k(ϖ_y)ρ_k(h′)φ₀^{⊗k}`, because the two end groups commute. Theorem 1's diagonal stabilizer gives `ρ_k(h′)φ₀^{⊗k} = ρ_k(ȟ)φ₀^{⊗k}`, with `ȟ` the target-end copy of `h′^{−1}`. So `ρ_k(s̃)ψ_O = c^kρ_k(ϖ_yȟ)φ₀^{⊗k}`, a target rotation of `φ₀^{⊗k}`, hence a coherent ray. Its mean has entries `⟨ψ_O, s̃^{−1}U^{ab}s̃ψ_O⟩ = −⟨ψ_O, U^{ba}ψ_O⟩ = −kO_{ba}`. A coherent ray `ψ_{O′}` has mean `kO′`, so the image is `ψ_{−O^T}`; `−O^T ∈ SO(10)` because `10` is even. ∎ `[check]` (1f).

### R-U. The `L5-U` condition of Theorem 6 holds

(referee closure, CH1_5OEP_REFEREE.md)

`LW1_5.md` line 90 gives the `L5-U` Gauss generators "`\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}`" for Hermitian `T`, and `VC1_5.md` line 31 says "its local group is `U(5)`". Take `T = 1` and `θ ∉ 2πZ`. On the register of a link `ℓ` with target `y`, the central element `e^{iθ}` of the target-end `U(5)` acts as `c := e^{iθp_{ℓ,y}}`, with `p_{ℓ,y}` the end number. `c` commutes with the target-end group, since it is central there. It commutes with the source-end group, since it is even and built from other modes. Since `[p_{ℓ,y}, r^y_j] = −r^y_j`, `c` conjugates `U^{jk}_ℓ = r^y_jr^{x†}_k` to `e^{−iθ}U^{jk}_ℓ`, and `U^{jk†}_ℓ` to `e^{iθ}U^{jk†}_ℓ`. So Theorem 6's proof runs with `c` in place of `ϖ`: each loop-link factor `f(h) = tr(ρ(h)X)`, with `X = U^{jk}` or `U^{jk†}`, equals `e^{∓iθ}f(h)`, hence vanishes. ∎
