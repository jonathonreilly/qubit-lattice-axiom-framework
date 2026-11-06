# LW1-U_sea: transport at the free sea

**Status — pass 2, not independently refereed or retained.** Under the premises of `LW1.md`, the Born law is unchanged at every half-tick. The sea's transport is uniquely diagonal at the even half-tick throughout `0 < μ < 2ε < π`, and at the odd half-tick off `Σπ = {2ε + μ = π, 0 < μ < π/2}`. On `Σπ` every admissible transport has positive cost; uniqueness remains **open**, as **LW1-U_hop**. Its five-flavour counterpart and **LW1-U_f** for other invariant factor states are open. No counterexample to LW1-U_sea is given. **GAP:** pass 1's claim that its finer conditional-independence test proves that a particular pair of cubes is conditionally dependent is stronger than its proof: the proof excludes the homogeneous cube-local representation (CL′), not conditional independence alone. The corrected statement is Theorem 9 below. Other inherited results remain conditional on their cited premises and have not received the fresh referee's independent check.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aea0-1f22-78e2-9abb-d014edf9e978`. Distiller: gpt-6.1-terra; effort: not visible; Codex session `01a1aea0-1f22-78e2-9abb-d014edf9e978`. Pass 1: Claude Opus 5.5, `LW1U_SEA_DRAFT.md`, SHA-256 `ed0746a646a505736bbb3301608035637153b111c75fbea59c17eeac5c49e7bc`. Current repository HEAD `5ff19240cf33824df71619ddac9ce2f943db6247`; source files in the working folder are the supplied snapshots, not claims about current main. Context: `LW1.md` SHA-256 `fe0c60979b50c1b427327d2f12c1d076402eda446c0b99c4bec1c4cbf1368830`; `LW1U_DRAFT.md` `54132cfc92f269c9dfaf191eeedd0aff9ad66657767610a519c23e8e4b16c366`; `TOE_ASSEMBLY.md` `8027d9d44eb5fcaf02393e06dbd75f1f1adc9d9a6e2e8a5f46c279d5e63afcc0`. Pass 1's scratch checks are floating-point guidance, not proofs; their scripts were not independently rerun here.

## 1. Definitions inferred by the distiller

1. The even cubes are `C_b = 2b + {0,1}³`, the odd cubes `D_b = 2b + (1,1,1) + {0,1}³`, `b ∈ Z³`. `R_e,R_o` are the real symmetric cube hop operators of LW1 A1, with `R_e² = R_o² = I`. Their edges carry `η_i(x)=(-1)^{Σ_{j<i}x_j}/√3`.
2. `a = ε − μ/2`, `b = ε + μ/2`, `V_e = exp(−iaR_e)`, `V_o = exp(ibR_o)`, and `V = V_o V_e`. The even layer acts first. In the window, `0<a<π/2` and `0<b<π`.
3. `P` is the upper-half-plane spectral projection of `V`; the sea `ω_P` is its gauge-invariant quasi-free state. For a covariance `G`, `G_xy = ω_G(c_y† c_x)`. The joint Born premise gives the occupation law `ν_G`. The half-step state evolves by `ω ↦ ω ∘ β`, where `β(A)=Γ(W)* A Γ(W)`; its covariance is `W G W*`.
4. The active-cube support is `S_C = {(A,A′): ⟨A′|Γ(u_C)|A⟩ ≠ 0}`. The admissible set `C_h`, cost `d̄`, and optimizers `O_h = argmax_s argmin_{C_h} d̄` are those of LW1 E4–E6. The diagonal coupling is the law of `(c,c)` for `c ∼ ν_h`. Countable cell-translation invariance converts zero expected changes per cell into equality of the two configurations almost surely.
5. On `Σπ`, write `a = π/2 − μ ∈ (0,π/2)`. The boundary `a=0` is the **product point**. In each odd cube, `E` and `O` denote the four corners of even and odd coordinate-sum parity; `N_E,N_O` count particles on them. The finer shared field is `m_D=(N_E,N_O)` before the hop and `(N_O,N_E)` after it.
6. **(CL)** means the homogeneous cube-local representation in `LW1U_DRAFT.md` §10.3: conditional on the active-cube number field, the configurations are independent with a law `α_m` depending only on the cube's number `m`, and similarly after the step. **(CL′)** makes the analogous requirement for `m_D`: `ν_1=∫⊗_D α_{m_D} dλ(m)` and `ν_2=∫⊗_D α′_{m_D} dλ(m)`, where `α′_v` has the swapped counts. Both demand the same local law at every cube, not merely conditional independence. (CL) implies (CL′), since the finer counts are cube-local functions.
7. The joint occupation law and the PS-3h support/selection are supplied readings, not derived physical axioms. This file proposes no new reading or specification. The earlier **PS-3m** remains proposed in `LW1U_DRAFT.md` §8; that draft reports checks 1, 2 and 4 passed, and check 3 passed with a persistent-label qualification. Its scope excludes components without a finite-index stabilizer. Those checks are reported, not re-established here.

## 2. Born law and half-step identity

**Theorem 1 (standard identities).** For finite `A`, `ν_G(c_x=1 for x∈A)=det G_AA`; these principal minors determine the entire Born law. A one-body unitary `u` has Fock-lift matrix element `⟨A′|Γ(u)|A⟩=det u_{A′A}` when `|A|=|A′|`, and zero otherwise. A layer sends `G` to `WGW*` and preserves gauge-invariant quasi-freeness.

*Proof.* Wick's rule gives the first determinant; expanding `∏_{y∈B}(1−n_y)` gives all finite cylinder probabilities. Expanding `Γ(u)∏_{x∈A}c_x†|0⟩` and using the CAR gives the second determinant. The transformed creation and annihilation operators give `WGW*`; Wick contractions transform likewise. Cube-local layers define the infinite-volume automorphism. □

**Theorem 2 (equal Born laws).** Let `G=f(V)` for real continuous `f` on `σ(V)`, `0≤f≤1`. Successive covariances are `G, \bar G, G,…`, and all their occupation laws agree. This holds for the sea in the stated window and also at `μ=0`, `0<2ε<π`, in infinite volume.

*Proof.* Symmetry of the two real hop matrices gives `V_e^T=V_e`, `V_o^T=V_o`, and `V_e V V_e* = V^T`. Transposition reverses products, preserves adjoints and is isometric. Polynomial approximation in `z,\bar z` therefore gives `f(V^T)=f(V)^T`. Thus `V_e G V_e*=G^T=\bar G`; the odd step returns `VG V*=G`. Principal minors of a Hermitian matrix are real and unchanged by conjugation, so Theorem 1 gives equality of laws.

For `μ>0`, LW1 B10 bounds `Re σ(V)` between `cos 2ε` and `cos μ`, strictly inside `(−1,1)`. The upper spectral projection is therefore a continuous function of `V`. At `μ=0` use the even-cell Bloch fibres: `(V^T)(K)=V(−K)^T`. Away from the null fibre `K=0`, the upper spectral projection transposes under this identity; hence `V_e P V_e*=P^T` almost everywhere. The same conclusion follows. □

Pass 1 reports finite-torus checks of the identity and examples where `P≠P^T`; equality of occupation laws does not assert equality of quantum states. It reports maximum identity residuals `4.5×10⁻¹⁶` and `6.2×10⁻¹⁶` in its stated four examples. These are not independent checks.

**Theorem 3 (equal laws select the diagonal).** If the two Born laws at a cell-invariant half-step are equal and the active angle `θ` has `cos θ≠0`, then `O_h` contains exactly the diagonal coupling. If `cos θ=0`, the diagonal pair of any one-particle cube configuration is unsupported.

*Proof.* For occupied set `A`, the diagonal amplitude is `det(cos θ I_A ± i sin θ R_AA)`. The real symmetric matrix `R_AA` has real eigenvalues, so every factor has nonzero real part when `cos θ≠0`. Hence the diagonal coupling is admissible and has zero cost. Any zero-cost invariant coupling is supported on equal configurations and is this coupling. If `cos θ=0`, the one-particle diagonal amplitude is a multiple of `R_xx=0`. □

**Theorem 4 (LW1-U_sea off the hop segment).** In the window, `O_0` is the diagonal singleton. `O_1` is the diagonal singleton unless `2ε+μ=π`, equivalently `(ε,μ)∈Σπ`. At `μ=0`, both are diagonal singletons. Off `Σπ`, a history built using LW1 E5 is almost surely constant for all half-ticks.

*Proof.* Apply Theorems 2–3. The even angle has nonzero cosine; the odd angle vanishes in cosine exactly on `Σπ`. The half-step states and laws repeat with period two. Each selected transition is diagonal, and a countable intersection gives the history statement. □

**Theorem 5 (torus seas).** For even periodic tori with the LW1 signs and tilings, in `0<μ<2ε<π`, the corresponding sea has the same diagonal singleton at each nonexceptional half-step. Its diagonal coupling converges locally to the infinite-volume one as the torus size tends to infinity.

*Proof.* The finite matrices obey the same transpose and diagonal-amplitude identities. The gapped Bloch projection is continuous in momentum, so torus momentum sums converge to its Fourier integral. Principal minors and cylinder probabilities converge. This covers these torus seas, not arbitrary approximants. □

The entropy stage is idle wherever Theorem 4 applies: least cost already selects one coupling.

## 3. The number-conditioned route

**Theorem 6 ((CL) fails on an open dense subset at the even step).** In the window, (CL) fails at every point outside the zero set of
`F=|P_(1,0,0),(2,0,0)|²−|P_(0,0,0),(3,1,1)|²`. That zero set is closed with empty interior.

*Proof.* Suppose (CL) holds. Rotations about `C_0` preserve its number and act transitively on its corners. Hence each corner has conditional occupation probability `m/8` under `α_m`. Homogeneity and conditional independence then give `E(c_x c_y)=E(N_0 N_k)/64` for all corners of distinct cubes `C_0,C_k`. Wick's two-point formula is `E(c_x c_y)=1/4−|P_xy|²`, so the magnitudes must be equal.

At the boundary `a=0`, `P=(I+R_o)/2`. The first pair in `F` is an odd edge and has squared magnitude `1/12`; the second entry is zero. To extend this witness, use the connected open set `0<2ε<π`, `0<μ<π`, including that boundary. LW1 B10's anticommutator identity places the real parts of the spectrum between `cos μ` and `cos 2ε`, in either order. Both lie strictly between `−1` and `1`; locally a fixed contour isolates the upper spectrum. The Riesz formula makes every `P_xy` real-analytic in the two parameters. Thus `F` is real-analytic and not identically zero. Its zero set has empty interior by the real-analytic identity theorem. □

Thus (CL) is sufficient by the conditional theorem in `LW1U_DRAFT.md` §10.3 but is not necessary for the singleton in Theorem 4. The proof does not decide (CL) at its exceptional zeros or at the nonexceptional odd step.

## 4. The pure-hop segment

**Theorem 7 (support and positive cost).** On `Σπ`, the odd one-body gate is `iR_o`. A pair `(A,A′)` in an odd cube is supported exactly when `|A′_E|=|A_O|`, `|A′_O|=|A_E|`, and both corresponding off-diagonal block determinants of `R_D` are nonzero. The support is symmetric. Every admissible coupling has expected changes per odd cube at least `2ν_P(N_D odd)>0`.

*Proof.* `R_D` has zero E–E and O–O blocks. The determinant in Theorem 1 vanishes unless the two off-diagonal blocks are square; then it is their determinant product up to sign. Symmetry follows from `R_D^T=R_D`. For odd total number, the two class counts differ, so swapping them changes at least two sites.

It remains to show positive odd-number probability. In odd-cell Bloch coordinates, `R_o(K)=R_D` and `V+V*=2 sin(a)χ(K)I`, with `χ(K)=⅓Σ_i cos K_i`. The upper spectral projection obeys
`tr(R_D P(K))=4 cos(a)/sqrt(1−sin²(a)χ(K)²)`.
Indeed `V−V*=2i cos(a)R_o+sin(a)[R_o,R_e]`; the trace of `R_o` times the commutator is zero. The displayed trace equals `4` at `K=0` and `4 cos(a)<4` at `K=(π/2,π/2,π/2)`. Thus `P(K)` is not constant, so `P` connects distinct odd cubes. The same is true of `\bar P`, the covariance at the odd step. Its compression `G_D` to one cube is not a projection: for a site with a nonzero outside matrix element, `(G_D²)_xx<G_xx`. Therefore some eigenvalue of `G_D` lies strictly between zero and one. The determinant identity
`E[(-1)^{N_D}]=det(I−2G_D)`
then has absolute value below one, so `ν_P(N_D odd)>0`. The support bound yields the asserted positive cost. □

**Theorem 8 (segment symmetries).** On `Σπ`, let `Z_x=(-1)^{Σ_i⌊x_i/2⌋}`, `D_x=(-1)^{Σ_i x_i}`, and `Y=DZ`. Then `ZPZ=I−P`, `\bar P=YPY`, and `Y` is constant on each odd cube `D_b`, with value `s_b=−(-1)^{Σ_i b_i}`. The state at the odd step is invariant under the cube-local Bogoliubov involution `R_o^s=Y R_o=⊕_b s_b R_{D_b}`. A time-swap-invariant optimizer exists.

*Proof.* `Z` commutes with `R_e` and anticommutes with `R_o`; at the hop angle `ZVZ=−V`. The upper projection of `−V` is `I−P`. LW1 B10's particle-hole identity is `D\bar P D=I−P`, so `\bar P=YPY`. Direct substitution of `x=2b+1+r` gives the stated cube sign. Stationarity gives `P=R_o\bar P R_o`; consequently `\bar P=R_o^s \bar P R_o^s`. The odd gate factors as `iR_o=(iY)R_o^s`. For the final assertion, equal marginals and symmetric support and cost make time swap preserve `O_1`; averaging an optimizer with its swap remains optimal by LW1 E6. □

**Open: LW1-U_hop.** Does `O_1` have exactly one element for every point of `Σπ`? A swap-invariant optimizer need not be unique. No second optimizer is constructed. Off the segment the unique coupling is diagonal; continuity of the gapped projection shows these couplings converge locally to the diagonal coupling at a segment point, which Theorem 7 excludes. Thus the selection is discontinuous there in this local topology, regardless of uniqueness on the segment.

## 5. Three attacks on LW1-U_hop

**Theorem 9 ((CL′) fails except possibly at isolated segment points).** Let `x=(2,1,2)`, `x′=(1,1,1)`, `y=(3,2,2)`. All are O-corners, with `x,x′∈D_0`, `y∈D_{e_1}`. As `a↓0`,
`\bar P_xy=ia/6+O(a²)`, `\bar P_x′y=O(a²)`.
Consequently (CL′), and hence (CL), fails near `a=0` and at all but isolated points of `(0,π/2)`.

*Proof.* If (CL′) held, the twelve parity-preserving cube rotations would make each corner's conditional occupation probability `m_E/4` or `m_O/4`, respectively. Homogeneity and conditional independence would make `|\bar P_xy|` constant for any fixed pair of corner classes in two distinct cubes.

At `a=0`, `P_0=(I+R_o)/2`, `Q_0=I−P_0`, and `V(a)=iR_o+aR_oR_e+O(a²)`. Expanding its Riesz projection gives
`P(a)=P_0+a(P_0 R_e Q_0−Q_0 R_e P_0)/(2i)+O(a²)`.
Across the common face, the two odd-edge entries relevant to `x,y` are `+1/√3` and `−1/√3`, while the even edge has weight `1/√3`. The coefficient of `P_xy` is therefore `1/(6i)`; the coefficient for `x′,y` is zero because `x′` is off that face and its remaining odd-edge entry vanishes. Conjugation gives the stated expansion. Their squared-magnitude difference is `a²/36+O(a³)`. The gapped Riesz formula makes it real-analytic for `|a|<π/2`; since it is not identically zero, its zeros are isolated. □

**GAP in pass 1, §5.5.** The above contradiction proves failure of the specified homogeneous representation. It does not by itself prove that the two named cubes are dependent conditional on the full field: the homogeneous local-law condition could fail separately. The first-order expansion is for a covariance entry, not a proved first-order conditional dependence. The uniqueness attack fails because its full (CL′) hypothesis fails; the stronger dependence claim remains open.

**Theorem 10 (the proposed Margenau–Hill candidate fails positivity).** Let `γ_+=⊗_D Ad Γ(R_D)` on local observables, and define the proposed signed cylinder form `q(E,E′)=Re ω_1(P_E γ_+(P_E′))`. It is consistent and cell-invariant, has both required marginals and vanishes on forbidden cube pairs. At the product point it assigns `−1/648` to a supported pair, and it remains negative there for all sufficiently small `a>0`. Hence it is not a coupling near that point.

*Proof.* Additivity follows from sums of occupation projectors. The cube signs in Theorem 8 differ from `γ_+` by cube parity conjugations, which act trivially on occupation projectors. Theorem 8 gives the second marginal; Theorem 2 equates the two laws. A forbidden matrix element of `Γ(iR_D)` is also zero for `Γ(R_D)`, proving the support assertion.

At `a=0`, let `A={(1,1,1),(1,1,2),(1,2,2),(2,2,2)}` and `B={(1,1,1),(1,1,2),(2,2,1),(2,2,2)}` in the listed order. The local state fills the `+1` eigenspace of `R_D`. Its real Slater amplitudes obey `ψ_Aψ_B=det(P_0)_{AB}`, and `Γ(R_D)ψ=ψ`. Hence `q(A,B)=det(P_0)_{AB} det(R_D)_{AB}`. With `t=1/√3`,
`√3(R_D)_{AB}=[[0,1,0,0],[1,0,0,0],[0,−1,0,1],[0,0,1,0]]`,
`2(P_0)_{AB}=[[1,t,0,0],[t,1,0,0],[0,−t,0,t],[0,0,t,1]]`.
Their determinants give `det R_AB=1/9` and `det(P_0)_AB=−1/72`. The first is nonzero, so the pair is supported; their product is `−1/648`. Local Wick expectations vary continuously with the gapped covariance, preserving the negative sign nearby. □

Pass 1 reports a scratch calculation of 528 negative entries among the `70²` four-particle one-cube entries, minimum `−1/144`, total negative mass `1.074`, signed cost 8 and one-cube least cost 3. These numerical values are not used in the proof.

**Theorem 11 (product point).** At `a=0`, outside the window, the odd-step optimizer is the product of the unique maximum-entropy least-cost one-cube coupling. It is not diagonal.

*Proof.* `P_0=(I+R_o)/2` is a direct sum of rank-four projections. The two Born laws are the same product `⊗_D p`. Every admissible coupling's cube marginal lies in the finite feasible set, and its cost is at least the one-cube minimum. The product of the LW1 B7 unique entropy maximizer on that face attains the bound. Entropy subadditivity bounds the specific entropy by its one-cube entropy. If a different invariant coupling differs on a finite box, either a cube law has smaller entropy or the box has a strict independence deficit. Tiling large boxes repeats this positive deficit, so its specific entropy is strictly smaller. The all-E four-particle pattern has probability `det(I_4/2)=1/16`, and the support sends it to all-O, so the optimizer is not diagonal. □

**Continuation attack.** Theorem 11 alone does not imply uniqueness for `a>0`. Specific entropy is affine on invariant couplings; odd-number sectors, absent at `a=0`, have positive probability for every `a>0` by Theorem 7; and no uniform entropy deficit or contraction is established. `LW1U_DRAFT.md` Theorem 4.3 reports a non-factor family with singleton optimizer at its product endpoint and a nontrivial optimizer segment for small positive parameter. This cited example is not rebuilt here and does not decide the factor-state sea. It illustrates the missing continuity step, not a no-go theorem.

## 6. Five modes and dressed finite systems

**Theorem 12 (five-mode free seas).** Assume the `L5-O` and `L5-U` free tick and PS-3h5 support of `LW1_5_DRAFT.md`: the one-body half-steps are `(W V_e W*)⊗I_5`, `(W V_o W*)⊗I_5`, with `W_xx=i^{x_1+x_2+x_3}`, and the sea covariance is `(WPW*)⊗I_5`. The joint flavour-occupation law, and hence the site-number and site-parity laws, are unchanged at each half-tick. For either actual configuration, the admissible transport is uniquely diagonal off `Σπ`, so its history is constant. On `Σπ` every admissible odd-step transport moves with positive probability; its uniqueness remains open.

*Proof.* The covariances alternate between `(WPW*)⊗I_5` and `(W\bar P W*)⊗I_5`. Diagonal conjugation by `W` does not alter principal minors, and the flavour-block covariance factorizes the quasi-free state. Thus the joint flavour occupation law is unchanged, as are its number and parity projections. When the active cosine is nonzero, choose any flavour occupation pattern realizing a given number or parity pattern. Its diagonal amplitude is the product over flavours of nonzero principal determinants, as in Theorem 3. The coarse diagonal pair is therefore supported. Zero cost then forces the diagonal coupling.

On the segment the hop swaps E/O counts in every flavour. A cube with odd total number cannot preserve either the full site-number pattern or the site-parity pattern: preservation would force E and O totals equal, respectively equal modulo two. Independent flavours and Theorem 7 give positive probability `(1−E[(-1)^{N_D^{(1)}}]^5)/2` of odd total. The support thus forces a change on that event. □

**Theorem 13 (finite dressed identity, conditional).** On a finite torus, suppose the dressed half-step generators of LW1 are real symmetric in the occupation/link basis and the electric layer is absent (`τ_E=0`). Then the two half-steps `M_e,M_o` are symmetric, `M_e U_0 M_e*=U_0^T` for `U_0=M_o M_e`, and any density matrix that is a real function of `U_0` has the same joint occupation/link-value law at all half-ticks.

*Proof.* Exponentials of real symmetric generators are symmetric. The transpose and functional-calculus argument of Theorem 2 applies in finite dimension; conjugate density matrices have the same diagonal in the chosen basis. With an electric layer the ordering becomes `M_e W_E M_o` versus `M_e M_o W_E`, so the identity is not generally supplied by this argument. No identification of the gauged vacuum with such a density matrix is made. □

## 7. Remaining scope and checks

- **LW1-U_hop:** uniqueness on `Σπ`; the five-flavour number and parity versions are also open. The conditional representation, signed form and continuation attacks stop at the precise points above. Failure of these routes does not prove nonuniqueness or impossibility.
- **LW1-U_f:** uniqueness and the requested torus clause for other invariant factor states remain open. Theorem 5 treats the specified torus seas only. Nothing here decides the owner question in `LW1U_DRAFT.md` about the scope of the Qualification.
- **VC1 and TM1:** off `Σπ`, the conditional PS-3 history of the free sea is constant; LW1 B8a separately states that records do not form. This establishes no result for gauged vacua or other states. The dressed identity above leaves the VC1 vacuum identification open.
- **Proposed readings:** no new proposal is made here. PS-3m and its pass-1 check results remain as stated in §1; no adoption follows.
- **Pass-1 numerical checks:** the draft reports `\bar P_xy/a` near `i/6` on a `6³` torus, odd-cube probabilities positive at four sampled points, and finite-torus checks of the segment identities. These are guidance only. The present distillation checks the displayed algebra and hypotheses, not the unprovided scratch scripts or an independent referee's work.
