# CH1-5O-E′: loop data and heat-kernel models

## 0. Status

**Proved under the stated inputs.** The large-register coherent-state lemma and its loop approximation (Theorems 1–2); cancellation of the tick by permitted inverse layers (Theorem 3); exact heat-kernel plaquette moments and their separation (Theorem 4); the conditional finite-data construction and a spatial random-link model witness (Theorem 5); its implication for the proposed 45-channel comparison (Corollary 5.1); and the finite-region Gauss-trace result (Theorem 6). These are author-side checks, not independent review or retained status.

**GAP.** The draft claims its random-link model classes close the frozen small-field comparison. It proves positivity of finite-window densities and small heat-kernel time, but does not check the full T0-start conditions, including reflection positivity and the non-simple extension. Thus its model witness does not close the frozen CH1-5O-E′. Its comparison is also constructed for spatial equal-time skeleton loops; it does not construct observables for arbitrary spacetime loops of `rℤ⁴`. Theorem 5 gives the corrected spatial model statement. A large-register limit does not establish the same result for `S_+`.

**Open.** CH1-5O-E′; CH1-5O-E′[VC1]; HEAT; SEP[T0-start]; CH1-5O-E; CH1-5O-i; CH1-5U-i; the R-A residual; AM; AM-5; CH1-i; CH1-ii; CG1-i; CG1-ii; CG1K-loc; CG1K-H; LW1-5-BG; LW1-5-X; GA1-P-5; Y2-W[`L5-O`]; VC1; the formulations of IR and AM (`CH1.md` Definition 8); and T0-start[G] for `Spin(10)` and the candidate subgroup factors. No law is eliminated. No amendment or reading is adopted here.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af5d-8d1c-7c32-88ac-5aa243c851ea`. Pass 1: Claude Opus 5.5, `CH1_5OEP_DRAFT.md`. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model identity, reasoning effort and session ID are not visible in this session. Date 2026-11-06. HEAD at read `ccdafd71c76de792065d9eefb0c8c5d8dfdb1b75`; working files need not belong to that commit. SHA-256: draft `c33bb719917f377249c968bd0a4418771e85218d4833f661178950fc4b02f188`; frozen `CH1_5OE.md` `70dbb28f246343ddadf91c44998456927840ee4b9b2532b9ef83e758b92bd98a`; `CH1_5O.md` `053f1ecf4da057b46eaf70b0c0cb4ac9c6629898a125f6bc959016bb1ccd95e3`. The draft's floating-point and Monte Carlo checks are reports, not proofs; they were not rerun. Standard heat-kernel existence and Fourier formula, Peter–Weyl, Haar measure, product states, and the unique trace on the matter CAR algebra are inputs. Perelomov, Lieb and Simon are credited for coherent-state context; the present bounds are the draft's. `LIT_HIGGS.md` supplies context, not a physical identification.

## 1. Definitions inferred by the distiller

1. The spatial lattice is `ℤ³`. `𝔄` is the quasi-local matter and link algebra. `G=Spin(10)` acts by local conjugations; `E` denotes the local Haar conditional expectation onto `𝔄^G`. The cell group is `𝒢=2ℤ³⋊O_{c₀}`, with the 24 proper cubic rotations about `c₀=(1,1,1)/2`. The cited `VC1_5.md` expectation commutes with cell lifts. Gauge invariance does not impose a Gauss-singlet sector.
2. On an oriented link `(x,y)`, `U^{ab}=iη^y_aη^x_b=2T_{a,10+b}`, with twenty Hermitian Majoranas and `{η_i,η_j}=2δ_{ij}`. Put `𝐔=Σ E_{ab}⊗U^{ab}`. The end actions rotate rows and columns by the vector map `R:G→SO(10)`. The central `ϖ∈G` maps to `−I`. A cell lift on a reversed link exchanges ends and sends `U^{ab}` to `−U^{ba}`. These action and lift identities, and the gate commutation facts, are inputs from `LW1_5.md` and `VC1_5.md`.
3. A path here has distinct links. For a closed path `C` with ordered factors `X_i=𝐔` or `𝐔^T` according to orientation, define `Ŵ_C=(1/10)tr((X_n/k)⋯(X_1/k))`, with one factor `1/k` for each link. It is Hermitian and invariant because distinct link factors commute and adjacent gauge rotations cancel. Its classical value is `cl_u(C)=tr(u_C)/10`. Products may have overlapping paths, but each constituent path uses each link once.
4. A block link is a straight path of `m` fine spatial links; a skeleton loop uses each block link at most once. Fix a finite list `Λ` of such loops. The standard comparison sends each `Ŵ_C` to the normalized vector trace on the corresponding group-valued block loop. For products of at most two entries, including adjoints and both orders, `d_Λ` is the maximum absolute difference of expectations; distance to a class is the infimum. These are distances between finite data vectors, so the triangle inequality applies. The fixed-data clauses are (a′) distance at most `δ` to some `K`-measure and (b′) distance greater than `δ` to every `G`-measure.
5. An `L5-O` update has irreducible `so(20)` link registers and can include finitely many layers of local gauge-invariant gates (`CH1_5O.md` Definition 1). Cell covariance of extra layers is separate. The law's own tick is `U₀=W_E M_o M_e`; set `τ_E=0` for general registers unless the electric layer is specified. Stationarity means invariance under the resulting automorphism. This definition does not itself identify the VC1 state.
6. **Proposed, not adopted:** R-E′ compares pure-gauge T0-start small-field classes with fixed maps, normalization, scale, tolerance and nonempty precisely specified classes. The full admissibility conditions are not pinned here. The random-link classes below are proposed model classes only. `CH1_5O.md` explains that embedding the pure-gauge version in CH1-5O-E also depends on the `W=0` reading. Neither finite matching nor a stabilizer establishes the light spectrum or a unique effective group.

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

Choose a target-end lift of `O` and apply it to `φ₀^{⊗k}`. The two lifts differ by the spin centre, which acts as a scalar, so the ray is well defined; local sections give continuity. Covariance gives its mean. At `O=I`, the `k` centered fluctuations have zero cross terms by product factorization and zero one-copy means; the one-copy norm is 3. Rotation gives both displayed identities. The diagonal stabilizer gives the source action. The end swap is the spin lift `∏_a(η^y_a−η^x_a)/√2`; its conjugation exchanges the end Majoranas and sends `U^{ab}` to `−U^{ba}`. It maps `φ₀` to the unique all-minus joint eigenvector, the same ray as `ϖ` at one end. This proves the last transformation. □

## 3. Loop approximation and stationarity

**Theorem 2 (draft Theorem U).** Let `ν` be any probability law on `SO(10)` values on spatial fine links. Put the register `R_k^-` on each link. Let `Φ_u` be the product of the coherent link states, `τ` the matter trace, and
\[
\omega=(\tau\otimes\int\Phi_u\,d\nu(u))\circ E,\qquad
\epsilon=(1+3/\sqrt k)^N-1.
\]
For loops of at most `N` links, the one-loop error against `ν` is at most `ε`, and the two-loop error at most `3ε` if `ε≤1`. For `q≥1`, the error of a product of `q` such loops is at most `q·10^{N(q−1)}ε`. The state is gauge invariant. If `ν` is invariant under geometric cell actions, with transpose on reversed links, it is also cell symmetric.

*Proof.* Continuity of the coherent rays makes each local integrand measurable and bounded. Consistent local product states and integration define a state. Haar averaging makes it gauge invariant and leaves invariant observables fixed.

For a fixed configuration write each normalized link factor as `O_i+Δ_i`. Expand the product. When `Δ_i` acts, the factor on its link is still coherent because the path has distinct links. Theorem 1 bounds that action by `3/√k`; the classical factors have norm one. Thus the loop applied to the product vector differs from its classical value times that vector by at most `ε`. Taking an inner product proves the one-loop bound. For two Hermitian loops write their vectors as `cΦ+e`, `c′Φ+e′`; `|c|,|c′|≤1` and the error is at most `2ε+ε²≤3ε`. For `q` loops telescope the product and use `‖Ŵ_C‖≤10^N`. Integrate.

The lift replaces a reversed link value by `−u^T`, not just `u^T`. For each reversed coordinate direction put `σ_x=(−1)^{Σ_{i∈J}x_i}`. The unwanted link sign is `σ_xσ_y`, produced by the local central gauge transformations at sites with `σ_x=−1`. On a local gauge-invariant observable their product acts trivially. The matter trace is automorphism-invariant, and `E` commutes with the lifts. Geometric invariance of `ν` therefore gives cell symmetry. □

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

*Proof.* Choose `η>0` below both `δ` and the strict separation margin. A block law can be subdivided by putting each block-link value on one fine link and identity on the others. Theorem 2 approximates its finite data within `η` for large `k`. Theorem 3 makes the state stationary. The triangle inequality proves both clauses. If an invariant fine-link law has the same data, use it instead; Theorem 2 gives cell symmetry.

For the model, `i diag(2,2,2,−3,−3)` is traceless, so the connected Case I group lies in the closed proper `SU(5)` lift. Choose `s` in the displayed range and `σ=5s/48`. The subgroup plaquette has first moment `e^{-s}`. Theorem 4 separates its first two moments from those at every full-group heat-kernel time by more than `δ`. Realize its data with independent fine links of law `R_*p^K_{σ/m}`. Heat-kernel convolution gives the desired independent block links; inversion invariance gives cell invariance. The first part applies. For the numerical choice, use `s=1/60`. □

A concrete spatial instance takes `r=a`, a finite plaquette list, `σ_*=1/576`, `δ=10^{-6}`, and `k=10^{18}`. With `η=10^{-7}`, `(1+3/√k)^4−1<1.3·10^{-8}`, so the two-loop error is below `η`. The fine-link law is `R_*p^K_{1/576}` and the update is the tick followed by its inverse layers. The resulting moments are within `η` of `e^{-1/60}` and `Q(e^{-1/60})`; the full-group model cannot match both within `δ`.

**GAP in the draft's conclusion.** The preceding theorem proves separation for the named random-link models, not membership in T0-start's class or satisfaction of every frozen small-field condition. Also, the construction maps only spatial loops to one time slice; the assertion for an arbitrary four-dimensional list has no supplied temporal-link construction. Conditional on those missing identifications, it supplies the respective finite comparison; without them CH1-5O-E′ remains open.

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

**Theorem 6 (draft Proposition Z).** On a finite region let `𝔊` be the algebra generated by the local gauge unitaries acting on its matter and internal links. For any finite-dimensional `Spin(20)` register, any `Z∈𝔊`, and any nonempty closed path with distinct links in the region, `tr(ZW_C)=0`. Hence any state whose every finite restriction is `tr(Z_Λ·)` for `Z_Λ∈𝔊_Λ` has zero such loop expectations. The analogous conclusion holds for `L5-U` if an end-central `U(1)` acts on each link factor by a nontrivial phase.

*Proof.* The gauge algebra is the linear span of products of site gauge unitaries. Trace one such product times the loop. Matter and link traces factor. On any loop link the factor is `tr(ρ(h)U^{ab})`, where `h` is a product of end-group elements. The target-end `ϖ` commutes with `h` and conjugates `U^{ab}` to `−U^{ab}`. Cyclicity makes the trace its own negative. Thus every summand vanishes. A nontrivial central phase gives the same argument for the stated `L5-U` case. □

If HEAT holds and a comparison class has `inf_μ|E_μ w_p|>δ`, Theorem 6 makes (a′) fail for its VC1 state, as in `CH1_5O.md` R8. This is conditional on HEAT and the class bound. The draft's assertion that the dark state has the required finite-region Gauss-trace form uses a global multiplicity-one argument without establishing its boundary-region restrictions: **GAP** at that inference. Its vanishing vector loops are separately established in the cited frozen source; they do not prove HEAT.

**SEP[T0-start] (open).** For fixed T0-start classes and comparison data, find a `K`-class measure at distance greater than `δ` from the `Spin(10)` class, whose finite spatial data have a cell-invariant fine-link realization. Theorem 5 would then supply the stated existence comparison, subject to the spatial/temporal and class identifications. This reduction is sufficient, not necessary.

C1–C3 fail only at the specified inference steps. C4 remains conditional on HEAT. A proposed numerical guide is to compare time-averaged plaquette moments under the base tick on a small finite box with `F` and `Q`; it would not prove the infinite-volume claim. Both `L5-O` and `L5-U` remain live under `TOE_ASSEMBLY.md` §3.5.
