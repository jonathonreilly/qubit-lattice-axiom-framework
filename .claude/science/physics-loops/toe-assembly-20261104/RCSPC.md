# RCS-PC: Clifford nodes in straight-string sectors

**FINISH: FROZEN 2026-11-07 after pass 3 (RCSPC_REFEREE.md); the referee's edits E1-E14 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `RCS1.md` as its Amendment 3. The lead (Claude Opus 5.5, laptop) checked that the edits are in the text; that is a text check, not a second referee. **Status.** Open: **RCSPC-CL**, **RCSPC-CL′**, **RCSPC-NF**, **RCS-P, Clifford form**, **MT1-S[R-CS^str]** in the VC1 vacuum, **R-CS**, **R-16^str′** (owner candidate, not adopted), **RCSP16-BT**, **CG16D-NLP** (longitudinal motion, energy, base-gate compilation), the owner question on cancelling base layers, and the `χ_sp`-to-`χ_tot` bridge on D-reg. No Clifford node is constructed. Imported referee closures are unrefereed; formal retained status remains separate. R-CS^str and R-16^str′ remain proposed, not adopted.

Editing session provenance: Codex gpt-6.1-terra, effort high, codex-cli 0.165.0; session id not visible.

Provenance: pass 1, `RCSPC_DRAFT.md`, Claude Opus 5.5; pass 2, gpt-6.1-terra, effort and session id: see run log. Source revisions are those recorded in the draft; they have not been refreshed through Git because this task forbids Git. The prior search and overlap record is `prior/RCSPC.md`. This item changes no law, axiom, reading or working-set entry.

The target is a Clifford cone on a band built from spinor-class straight-string sectors, with `{N_i,N_j}=2v²δ_ij`, `v>0`. `RCSP16.md` already proves longitudinal motion `V=e^{iK₁}` and excludes the cone for its two backgrounds under matter-activated updates. `RCS1.md` already proves the conserved-label obstruction and its transverse-disjointness plus tick-equivalence corollary. `CG16B.md` already constructs the rishon witness and the boundary label. `CG16D.md` already constructs D-reg half-column defects. These frozen results are inputs, not independently audited by this distillation. The digest also records earlier finite-clock static charges and rotor dressing in `ref/main/docs/FINITE_CLOCK_STATIC_CHARGE_TRANSFER_HAMILTONIAN_AND_PATH_COMPARISON_BOUNDED_THEOREM_NOTE_2026-09-15.md` and `ref/main/docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md`; neither supplies this moving Clifford band.

## 1. Prior work used

Each item is ported with credit, not re-derived, unless the text says "rebuilt".

- `RCS1.md` definition 5 (covariant representation, band, node, `N_j`) and §5 (R-CS^str(e), straight strings, covariant choice of limit points). Used as the setting.
- `RCS1.md` Lemma 5.1, the identity "`P(Γ)X=XM_{1_Γ(K,w(K))}` for every Borel `Γ`" and its polynomial, Stone–Weierstrass and regularity proof. Ported in Lemma 1.1 for matrix-valued `W`.
- `RCS1.md` Theorem 5 (a conserved label shifted by translations forces flatness) and Corollary 9 (transverse disjointness plus tick quasi-equivalence exclude a Clifford cone). **Extended** by Theorem 1 and Corollary 2: the tick may move labels; quasi-equivalence to the tick transform is not needed.
- `RCS1.md` Lemma 6 (escaping sharp observables separate representations) and R2(a) (strong convergence to a scalar passes to quasi-equivalent representations, by Zorn's lemma). Used in Proposition 3.
- `RCS1.md` §8, attacks A1, A2, A3 and kill attempt K. A3 ("No appropriate fluctuating-loop D1 state is constructed", line 227) is run here on `Ψ_λ` (§4.4). K's missing step ("No general conservation theorem", line 229) is not needed by Theorem 1, which allows labels to move.
- `RCSP16.md` definitions 1-6 (witness, strings, `ω′`, matter-activated gates, projected update `U`), Theorem 1 (`ω′` is D1), Theorem 2 (`U` is in LZ1's class and meets NN-a; every projected gate fixes the all-`H_-` subspace), Theorem 3 (string limits, labels, transverse disjointness by far-ray target-end numbers), Theorem 9 (transverse flatness for matter-activated updates). **Extended:** Corollary 4 extends the no-Clifford-node clause to every update; not the transverse-flatness clause.
- `RCSP16_REFEREE.md` N1 (a finite-string expectation is constant once the endpoint has passed the observable's support), N6 (plane statement), N7 (scope: far-ray updates lie outside Theorem 9), N8 (ray sectors are disjoint from the background GNS representation), N9 (an update `U′` with no inverse layer that acts as `U` on string sectors and is matter-activated).
- `CG16B.md` Theorem 3.1 (the rishon witness), Lemma NN-W, Theorem 6.1 (finite-region flux identity), Theorem 6.2 (finite strings), Proposition L (centre values kept; `χ_tot=−1`; boundary label `−1`) and Example S (`ω_Φ`).
- `CG16D.md` Lemma N, Step 2 (the number of distinct eigenvalues is lower semicontinuous, so it is locally constant on a dense open set, where eigenvalues and Riesz projections are `C¹`). Ported in Lemma 1.2. `CG16D.md` Theorem 9 (columnar D1 state on D-reg; half-column string defects with `χ_sp=−1`). Used in Corollary 10.
- `LZ1.md` §1 (D1 state, band, node, Clifford cone). Used as definitions.
- `CG16S.md` Lemma RC-W and its scope paragraph (line 140). Used only to say when it applies (§4.8).
- `GA1_5.md` Lemma U (link-only unitaries compile into NN-a gates). Used in a remark on the loop-flip layer of §4.4.
- Main branch, comparison only: the three-axis toric-code note (3D toric-code charges move by single `Z` operators; "The charges are bosons"); the cubic-ice note ("Plaquette flips conserve every vertex degree and therefore cannot move or create the fixed charges"); the rotor dressing note (an exact Gauss dressing exists on integer-rotor registers, which are unbounded; Remark 5.2 explains why Lemma 5's mechanism needs a bounded register).

**Prior work the digest missed.** `RCSP16_REFEREE.md` N9, used for non-vacuity without an inverse layer (Corollary 4). `CG16D.md` Lemma N Step 2 as the source of the constant-multiplicity set (the digest cites Lemma N only for flatness). Neither changes the digest's account.

**Failed attempts on file, and what is new here.** The digest lists A1 (frozen backgrounds), A2 (Dirac clouds), A3 (no fluctuating-loop state), K (no universal conservation), the longitudinal witness as a cone, finite-end relative class, D-reg transfer with the matching state, literal centre gauging and the original endpoint statement. None is repeated. The new steps are: labels may move under the tick (Theorem 1); block permutation from sharp asymptotic labels without factoriality (Proposition 3); the lowest-level mechanism (Lemma 5); an explicit fluctuating-loop D1 state (§4.4).

Additional inputs missed by the digest: `RCS1.md` R4 (unitary link factors on `L5-O[S_+]`) and Theorem 8(b) (far-end numbers on `L5-U[2k]`), and `CG16D.md` Theorem 8(iv) (D-reg has odd gauge-invariant elements). The live-law extensions and stationarity-free Proposition L application are referee closures, marked below.

## 3. Definitions inferred by the distiller

The draft infers these conventions from the cited sources. D7 and D9 are mathematical definitions, not adopted readings. Translation invariance means invariance under all cell translations τβ. A ray limit always takes r → ∞ through lengths with positive denominator. All results below are conditional on their stated hypotheses and the cited source results.

**D1 (law).** The U(16)-rishon witness of `CG16B.md` Theorem 3.1, at total rishon number `m` per link, `1≤m≤31`. Sites carry `H=H_+⊕H_-` (`16+16`), with `P=±1` on `H_±`. The local gauge group `Spin(10)` acts on matter by `S_+⊕1` and on each link end by the second quantization of `S_+`. `E_{x,ai}=|a⟩⟨i|` maps `H_-` to `H_+`. The centre implementer is `z_x=−P_x∏_{ℓ∋x}(−1)^{p_{ℓ,x}}`, with `p_{ℓ,x}` the rishon number at the end of `ℓ` at `x`. `𝔄` is the quasi-local field algebra, `𝔄^G` its local-gauge fixed subalgebra, `τ_β` translation by `2β`, `α(A)=U^*AU` the tick. Every element of `𝔄^G` is matter-even (`CG16B.md` Theorem 4.1(b)); so local elements of `𝔄^G` with disjoint supports commute. Results are stated at `m=16` unless they say otherwise.

**D2 (lines and target numbers).** For `c∈Z²` let `L_c={(s,c):s∈Z}` be the `e_1`-line with transverse coordinate `c`. Let `ℓ_{c,s}` be the link from `(s,c)` to `(s+1,c)`. Let `n_{c,s}` be the rishon number at its target end `(s+1,c)`, and `Π^{(j)}_{c,s}` the spectral projection of `n_{c,s}` onto the value `j`. `Spin(10)` acts on the 16 target modes by `S_+`, which preserves their number. So `n_{c,s}` and each `Π^{(j)}_{c,s}` lie in `𝔄^G`; they are even. `τ_β(n_{c,s})=n_{c+2β_⊥,s+2β_1}`, where `β_⊥=(β_2,β_3)`.

**D3 (strings and ray sectors).** `RCSP16.md` definition 2: `B_{r,b}(x)=Σ_aE_{x,ai_0}(T_1⋯T_{2r})_{ab}`, with `(T_k)_{ab}=r^{ℓ_k,y_{k−1}}_ar^{ℓ_k,y_k†}_b` on the `k`-th link `ℓ_k=(y_{k−1},y_k)`, `y_k=x+ke_1`. For a state `ω` of `𝔄` and lengths with positive denominator, `ω^{(x)}_r(A)=Σ_bω(B^*_{r,b}AB_{r,b})/Σ_bω(B^*_{r,b}B_{r,b})` on `𝔄^G`. A **ray state** `ω_x` is a weak-* limit point as `r→∞` along such lengths. For translation-invariant `ω` it is chosen covariantly: one limit point per residue of `x` modulo `2Z³`, translated (`RCS1.md` §5). Its GNS triple is `(H_x,π_x,Ω_x)`; `π_x` is a **ray sector**, and its **line** is `x_⊥=(x_2,x_3)`. Covariance gives `ω_{x+2β}=ω_x∘τ_β^{-1}`, so `π_{x+2β}` is unitarily equivalent to `π_x∘τ_β^{-1}`.

**D4 (built from ray sectors).** A separable covariant representation `(H,π,T,Ũ)` in the sense of `RCS1.md` definition 5, with `T_βπ(A)T_β^*=π(τ_βA)`, `Ũπ(A)Ũ^*=π(αA)`, `ŨT_β=T_βŨ`, is **built from ray sectors** when `π=⊕_{i∈I}σ_i` and each `σ_i` is quasi-equivalent to some `π_{x_i}`. This is the class of `RCSP16.md` Theorem 9 and of RCS-P.

**D5 (updates).** "Every update" means: every automorphism `α` of `𝔄` that commutes with each local gauge transformation and with each `τ_β`. LZ1's class (`LZ1.md` §1) lies in it. Since `α` commutes with gauge transformations, `α(𝔄^G)=𝔄^G`. Theorem 1 uses nothing else about `α`. Matter activation (`RCSP16.md` definition 4) and NN-a are not assumed.

**D6 (bands).** `LZ1.md` §1: a band `(d,F,V)`, a node `K₀` (`V(K₀)=1`, `V` is `C¹` near `K₀`), `N_j=∂_j(i\log V)(K₀)`, a Clifford cone (`{N_i,N_j}=2v²δ_{ij}`, `v>0`). A **Clifford node** is a node with a Clifford cone.

**D7 (label structure).** For a separable covariant representation, a label structure is an orthogonal decomposition `H=⊕_{κ∈C}H_κ` with projections `Π_κ≠0` such that:
- (L1) `T_βΠ_κT_β^*=Π_{β·κ}` for an action `(β,κ)↦β·κ` of `Z³` on `C` with finitely many orbits;
- (L2) `ŨΠ_κŨ^*=Π_{σ(κ)}` for some map `σ:C→C`.

The stabilizer `Γ_κ={β∈Z³:β·κ=κ}` is the same subgroup `Γ_O` for every `κ` in an orbit `O`, since `Z³` is abelian. `σ` is a bijection: the `ŨΠ_κŨ^*` are pairwise orthogonal nonzero projections with sum `1`, so distinct `κ` have distinct images, and every `Π_{κ'}` is hit because `Σ_κΠ_{σ(κ)}=1`. From `ŨT_β=T_βŨ`, `Π_{σ(β·κ)}=Π_{β·σ(κ)}`, so `σ(β·κ)=β·σ(κ)`.

**D8 (labels of sectors).** Parity-sharp backgrounds, `χ_tot` and the boundary label: `RCS1.md` R2 and `RCSP16.md` definition 3. R-16^str′ (`CG16B.md` §7, owner candidate, not adopted) calls boundary label `−1` spinor class over a parity-sharp background sharp in every `z_x`.

**D9 (lowest level).** For a state `ω` of `𝔄` and a direction-1 link `ℓ_{c,s}`, put `j_0(c,s;ω)=\min\{j:ω(Π^{(j)}_{c,s})>0\}`. It exists, since `n_{c,s}` has finitely many values and its spectral projections sum to `1`. For a translation-invariant `ω` it depends only on `c` and `s` modulo 2.

## 4. Results

### 4.1 Rigid labels forbid Clifford nodes (any law, any update)

`RCS1.md` Theorem 5 needs a label that the tick **preserves**. The far-end escape asks for a tick that **moves** labels. Theorem 1 allows that and still excludes a Clifford node.

**Theorem 1 (rigid labels).** Let `(H,π,T,Ũ)` be a separable covariant representation with a label structure (D7). Suppose every orbit `O` of `Z³` on `C` has a stabilizer `Γ_O` of rank at most 2. Then no band has a Clifford node. More precisely, fix `p≥1` such that `σ^p` maps every orbit to itself, and for each orbit a nonzero `n_O∈Z³` with `n_O·β=0` for all `β∈Γ_O`. There are integers `θ_O` with the following property. Let `(d,F,V)` be a band with a node `K₀`, and let `g=p\,i\log V` on a small ball `B` around `K₀`. Then on a dense open subset `U⊂B`, every eigenvalue branch `λ` of `g` has, at every point, `n_O·∇λ=−θ_O` for at least one orbit `O`.

The proof uses three lemmas.

**Lemma 1.1 (spectral transfer; ported from `RCS1.md` Lemma 5.1).** Let `E` be the joint spectral measure of the commuting unitaries `(T_{e_1},T_{e_2},T_{e_3},Ũ^p)` on `T³×S¹`. Let `F:L²(T³;C^d)→H` be an isometry with `T_βF=FM_β` and `Ũ^pF=FM_W` for a continuous `W:T³→U(d)`. Then `E(Γ)F=FM_{1_Γ(K,W(K))}` for every Borel `Γ`. Here `1_Γ(K,W(K))` is the spectral projection of the matrix `W(K)` onto `\{z:(K,z)∈Γ\}`.

*Proof.* `Ũ^p` maps `\mathrm{ran}F` onto itself, because `FM_W=Ũ^pF` and `M_W` is unitary; so `(Ũ^p)^*F=FM_{W^*}`. Hence `f(T,Ũ^p)F=FM_{f(K,W(K))}` for every polynomial `f` in `e^{±iK_j}`, `z^{±1}`. Stone–Weierstrass extends this to continuous `f` on `T³×S¹`, by uniform approximation on both sides. Both sides are spectral integrals of regular Borel measures, so the identity holds for indicator functions of Borel sets: first for open sets, as monotone limits of continuous functions, then by the monotone class theorem. This is the argument of `RCS1.md` Lemma 5.1 ("first verify this for polynomials, extend to continuous functions by Stone–Weierstrass, then to Borel sets by regularity of the measures"), with the scalar `w` replaced by the matrix `W`. □

**Lemma 1.2 (regular branches; Step 2 of `CG16D.md` Lemma N, with the derivative formula rebuilt).** Let `g` be a `C¹` Hermitian `d×d` function on an open ball `B⊂R³`. The set `U` of points near which the number of distinct eigenvalues of `g` is constant is open and dense in `B`. Near each point of `U`, the distinct eigenvalues `λ_1<⋯<λ_r` have constant multiplicities `m_i`, are `C¹`, have `C¹` Riesz projections `P_i`, and satisfy `∇λ_i=\mathrm{tr}(P_i∇g)/m_i`.

*Proof.* Eigenvalues depend continuously on `g`, so distinct eigenvalues stay distinct nearby: the number `N(K)` of distinct eigenvalues is lower semicontinuous. In any open ball inside `B`, `N` attains its maximum at some `K₁`; lower semicontinuity and maximality make `N` constant near `K₁`. So `U` meets every ball, and `U` is open by definition. Near a point of `U`, separate the distinct eigenvalues by fixed small circles; the Riesz projections `P_i=(2πi)^{-1}∮(z−g)^{-1}dz` are `C¹`, their traces `m_i` are constant, and `λ_i=\mathrm{tr}(P_ig)/m_i` is `C¹` (this is `CG16D.md` Lemma N, Step 2: "they and their Riesz projections `P_i` are `C¹`"). For the derivative, differentiate `P_iP_k=δ_{ik}P_i`. For `k=i`, `P_i(∂P_i)P_i=0`. For `k≠i`, `(∂P_i)P_k+P_i∂P_k=0`; multiply by `P_k` on the left to get `P_k(∂P_i)P_k=0`. So `\mathrm{tr}((∂P_i)P_k)=\mathrm{tr}(P_k(∂P_i)P_k)=0` for every `k`, and `\mathrm{tr}((∂P_i)g)=Σ_kλ_k\mathrm{tr}((∂P_i)P_k)=0`. Differentiating `m_iλ_i=\mathrm{tr}(P_ig)` gives `m_i∂λ_i=\mathrm{tr}(P_i∂g)`. □

**Lemma 1.3 (slopes near a Clifford node).** Let `g` be `C¹` near `K₀`, `g(K₀)=0`, and let `M_j=∂_jg(K₀)` satisfy `\{M_i,M_j\}=2v′^2δ_{ij}`, `v′>0`. For every `η>0` there is `ρ_1>0` with this property. Let `0<|K−K₀|<ρ_1`, `ν=(K−K₀)/|K−K₀|`, and let `K` lie in the set `U` of Lemma 1.2. Then every eigenvalue branch `λ_i` at `K` is nonzero, and with `ε_i` the sign of `λ_i(K)`, `|n·∇λ_i(K)−ε_iv′(ν·n)|≤η|n|` for every `n∈R³`.

*Proof.* Put `ρ=|K−K₀|` and `A=ν·M`. The Clifford relations give `A²=v′^2`, so `Q_±=(1±A/v′)/2` are the spectral projections of `A`. Differentiability at `K₀` gives `g(K)=ρA+r` with `‖r‖≤ε(ρ)ρ`, `ε(ρ)→0`. Let `gu=λu`, `‖u‖=1`. Apply `Q_±` to `(ρA−λ)u=−ru`: `|ρv′−λ|‖Q_+u‖≤ερ` and `|ρv′+λ|‖Q_-u‖≤ερ`. One of `‖Q_±u‖` is at least `2^{-1/2}`, so `λ` lies within `\sqrt2ερ` of `ρv′` or of `−ρv′`; for `\sqrt2ε<v′` it is nonzero. If `λ>0`, then `|ρv′+λ|≥ρv′`, so `‖Q_-u‖≤ε/v′`; if `λ<0`, `‖Q_+u‖≤ε/v′`. Next, `n·M=(ν·n)A+(n−(ν·n)ν)·M`. The Clifford relations give `\{a·M,b·M\}=2v′^2(a·b)`, so the second term anticommutes with `A` and maps `\mathrm{ran}Q_+` into `\mathrm{ran}Q_-`. Hence `Q_+(n·M)Q_+=v′(ν·n)Q_+` and `Q_-(n·M)Q_-=−v′(ν·n)Q_-`. For `λ>0`, expanding `u=Q_+u+Q_-u` gives `|⟨u,(n·M)u⟩−v′(ν·n)|≤2v′|n|ε²/v′^2+2‖n·M‖ε/v′≤C|n|ε`, with `C` fixed by `v′` and `\max_j‖M_j‖`; the case `λ<0` is the same with signs exchanged. Average over an orthonormal basis of `\mathrm{ran}P_i(K)`, all with the same sign of eigenvalue, and use Lemma 1.2 and `‖n·∇g(K)−n·M‖≤|n|ε′(ρ)`, `ε′(ρ)→0` by continuity of `∇g`. Then `|n·∇λ_i(K)−ε_iv′(ν·n)|≤|n|(Cε(ρ)+ε′(ρ))`. Choose `ρ_1` with `Cε+ε′≤η` below it. □

*Proof of Theorem 1.* **Step 0 (choices).** `σ(β·κ)=β·σ(κ)` (D7), so `σ` maps orbits onto orbits. There are finitely many, so some power `σ^p`, `p≥1`, fixes each orbit. `Γ_O` spans a subspace of `R³` of dimension at most 2, so an integer `n_O≠0` orthogonal to it exists. Fix `κ_O∈O` and `γ_O∈Z³` with `σ^p(κ_O)=γ_O·κ_O`. Put `q_O(β·κ_O)=n_O·β`. This is well defined: if `β·κ_O=β′·κ_O`, then `β−β′∈Γ_O`. Then `q_O(β·κ)=q_O(κ)+n_O·β` for `κ∈O`, and `q_O(σ^pκ)=q_O(κ)+θ_O` with `θ_O=n_O·γ_O`, since `σ^p(β·κ_O)=(β+γ_O)·κ_O`.

**Step 1 (boosts).** Let `Π_O=Σ_{κ∈O}Π_κ`; it commutes with every `T_β` and with `Ũ^p`. Put `B_t=Σ_{κ∈O}e^{itq_O(κ)}Π_κ+(1−Π_O)`. From `T_βΠ_κ=Π_{β·κ}T_β` and `Ũ^pΠ_κ=Π_{σ^pκ}Ũ^p`: on `Π_OH`, `B_tT_βB_t^*=e^{itn_O·β}T_β` and `B_tŨ^pB_t^*=e^{itθ_O}Ũ^p`.

**Step 2 (shifted spectra).** On `Π_OH` the joint spectral measure of `(e^{itn_O·β}T_β,e^{itθ_O}Ũ^p)` is the image of `E` under `ψ_t(K,z)=(K+tn_O,e^{itθ_O}z)`; by Step 1 it is also `B_tEB_t^*`. The joint spectral measure is unique. So `B_tE(Γ)Π_OB_t^*=E(ψ_t^{-1}Γ)Π_O` for Borel `Γ`.

**Step 3 (forbidden slopes).** Let `(d,F,V)` be a band with node `K₀`. Take an open ball `B∋K₀` of diameter less than `2π` on which `V` is `C¹` and `h=i\log V` has spectrum in `(−π/2p,π/2p)`. Then `W=V^p=e^{−ig}` with `g=ph` on `B`, `g` has spectrum in `(−π/2,π/2)`, and `Ũ^pF=FM_W`. Let `U` be as in Lemma 1.2 for `g`. Suppose some `K_1∈U` and branch `λ_i` have `n_O·∇λ_i(K_1)≠−θ_O` for every `O`. By continuity there is a ball `B_2∋K_1` in a constant-multiplicity ball where `s_O=n_O·∇λ_i+θ_O` has a fixed sign for every `O`, and `|s_O|≤S`. Choose a closed ball `B_3∋K_1` and `t_*>0` with `B_3+[−t_*,t_*]n_O⊂B_2` for every `O` and `t_*S<π`. Put `Γ=\{(K,e^{−iλ_i(K)}):K∈B_3\}`. For `0≤t<t′≤t_*`, a common point of `ψ_t^{-1}Γ` and `ψ_{t′}^{-1}Γ` (taking `ψ` for one fixed `O`) is `(K′,z)` with `K′+tn_O,K′+t′n_O∈B_3` and `λ_i(K′+tn_O)+tθ_O≡λ_i(K′+t′n_O)+t′θ_O` modulo `2π`. (Equal torus points are equal points of `B`, whose diameter is below `2π`.) The function `u↦λ_i(K′+un_O)+uθ_O` has derivative `s_O≠0` of fixed sign on `[t,t′]`, as the segment lies in the convex `B_2`; its values at `t` and `t′` differ by a nonzero amount less than `π`. So the sets `ψ_t^{-1}Γ`, `0≤t≤t_*`, are pairwise disjoint. If `E(Γ)Π_O≠0`, Step 2 gives uncountably many nonzero projections `E(ψ_t^{-1}Γ)Π_O` with pairwise orthogonal ranges, which a separable space cannot hold. So `E(Γ)Π_O=0` for every orbit, and `E(Γ)=Σ_OE(Γ)Π_O=0`, a finite sum. Distinct eigenvalues of `g` in `(−π/2,π/2)` give distinct eigenvalues of `W`, so `1_Γ(K,W(K))=1_{B_3}(K)P_i(K)`. Lemma 1.1 gives `FM_{1_{B_3}P_i}=E(Γ)F=0`. `F` is an isometry, so `P_i=0` almost everywhere on `B_3`. But `P_i` is continuous with trace `m_i≥1`. This contradiction proves the slope statement.

**Step 4 (no Clifford cone).** Suppose `K₀` is a Clifford node with speed `v`. Then `M_j=∂_jg(K₀)=pN_j` satisfy the Clifford relations with `v′=pv`. The sets `\{ν∈S²:±v′(ν·n_O)=−θ_O\}` are circles or empty, finitely many; pick `ν_0` outside all of them. Put `δ=\min_{O,±}|±v′(ν_0·n_O)+θ_O|>0`. Take an open cap `C∋ν_0` on which each `±v′(ν·n_O)` moves by less than `δ/4`, and `η` with `η|n_O|<δ/4` for every `O`. Take `ρ_1` from Lemma 1.3. The open set `\{K₀+ρν:ν∈C,0<ρ<ρ_1\}∩B` meets the dense set `U`. At such a `K`, every branch has `|n_O·∇λ_i(K)+θ_O|≥δ−δ/4−δ/4>0` for every `O`, against Step 3. □

**Remark 1.4.** If the tick fixes every label (`σ=\mathrm{id}`), then `θ_O=0`, and Step 3 gives a zero slope along at least one `n_O` for each branch. The conserved-label result is already proved in `RCS1.md` Theorem 5; this finite-orbit statement is not its full directional-flatness conclusion. Theorem 1 leaves room for longitudinal motion (`n_O` is orthogonal to longitudinal stabilizer elements) and for bands that drift transversely when the tick moves labels (`θ_O≠0`). Such drifting bands can have nonzero leading generators in three directions, but at each point of `U`, `∇λ` lies on one of finitely many affine planes `n_O·k=−θ_O`. A Clifford cone needs slopes `ε_iv′(ν·n_O)` that avoid all of them for some open set of directions `ν` (Step 4).

### 4.2 Factor ray sectors: what a Clifford node needs

**Corollary 2 (factor ray sectors; any update).** Fix a law with a quasi-local field algebra, local gauge actions and cell translations, as in `RCS1.md` definition 1 or `CG16B.md` §1, and an axis `e`. Let `ω` be translation invariant and choose the ray sectors covariantly (D3). Let the ray sectors `π_x` (D3) be factor representations of `𝔄^G`. Let `(H,π,T,Ũ)` be built from them (D4) for any update (D5). For `x∈Z³` put `Γ_x=\{β∈Z³:π_{x+2β}\text{ is quasi-equivalent to }π_x\}`. If every `Γ_x` has rank at most 2, no band in `H` has a Clifford node. So a Clifford node needs some `x` with `π_x` quasi-equivalent to `π_{x+2β}` for every `β` in a subgroup of finite index in `Z³`. That subgroup contains two elements whose components orthogonal to `e` are linearly independent. If ray sectors on distinct lines parallel to `e` are disjoint, then `Γ_x⊆Ze` and no band has a Clifford node.

*Proof.* (a) *Classes.* Let `C` be the set of quasi-equivalence classes of the ray sectors that occur among the summands `σ_i`, and `H_κ` the closed span of the summands in class `κ`. For factor representations, "non-disjointness implies quasi-equivalence" (`RCS1.md` definition 3). So summands in different classes are disjoint. A direct sum of representations each disjoint from `ρ` is disjoint from `ρ`, because an intertwiner restricts to each summand. Hence the subrepresentations on `H_κ` and `H_{κ′}`, `κ≠κ′`, are disjoint, and `H=⊕_κH_κ`. For `X∈π(𝔄^G)′`, `Π_{κ′}XΠ_κ` intertwines these two subrepresentations, so it is zero. Thus each `Π_κ` commutes with `π(𝔄^G)′` as well as with `π(𝔄^G)`: it lies in the centre `𝒵` of `π(𝔄^G)″`. The subrepresentation on `H_κ` is quasi-equivalent to one factor representation, so `π(𝔄^G)″Π_κ` is a factor and `Π_κ` is a minimal projection of `𝒵`. Every central projection `Z` equals `Σ_κZΠ_κ` with `ZΠ_κ∈\{0,Π_κ\}`. So the `Π_κ` are exactly the minimal central projections.

(b) *Tick and translations.* `Ũπ(𝔄^G)Ũ^*=π(α(𝔄^G))=π(𝔄^G)` (D5), so `\mathrm{Ad}\,Ũ` is an automorphism of `π(𝔄^G)″` and of `𝒵`. It maps minimal central projections onto minimal central projections: `ŨΠ_κŨ^*=Π_{σ(κ)}`. In the same way `T_βΠ_κT_β^*` is a minimal central projection. On `T_βH_κ` the representation is unitarily equivalent, through `T_β`, to `π|_{H_κ}∘τ_β^{-1}`; for `κ=[π_x]` this is quasi-equivalent to `π_x∘τ_β^{-1}`, hence to `π_{x+2β}` (D3). So `T_βΠ_κT_β^*=Π_{β·κ}` with `β·[π_x]=[π_{x+2β}]`. The classes of `π_x` with `x` in one residue class modulo `2Z³` form one orbit, so there are at most 8 orbits. The stabilizer of `[π_x]` is `Γ_x`. This is a label structure; Theorem 1 applies.

(c) *The remaining claims.* A subgroup of `Z³` of rank 3 has finite index. Its intersection with `Ze` has rank at most 1, so its image under projection along `e` has rank 2. If sectors on distinct lines are disjoint, then for `β` with a nonzero component orthogonal to `e`, `π_x` and `π_{x+2β}` are disjoint, hence not quasi-equivalent; so `Γ_x⊆Ze`. □

**Remark 2.1 (the far-end escape).** `RCS1.md` Corollary 9 needs each sector to be "quasi-equivalent to its tick transform". Corollary 2 drops that hypothesis for factor sectors. An update that acts on the far ray may move each class to another line (`σ≠\mathrm{id}`); it still gives no Clifford node while sectors on distinct lines are disjoint. So the far-end escape needs the transverse position to be unobservable as well. `RCS1.md` line 221 states the escape as "two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform". For factor sectors Corollary 2 sharpens this to: non-disjoint (equivalently, quasi-equivalent) sectors at transverse displacements in two independent directions. The second alternative alone is not enough.

**Remark 2.2 (scope).** Factoriality of ray sectors is a hypothesis here. The cited frozen texts do not establish it for the backgrounds used here. §4.3 replaces it, for a named class of backgrounds, by sharp asymptotic labels and clustering along the ray.

### 4.3 Sharp asymptotic labels give a label structure without factoriality

Fix the axis `e_1` and ray sectors `π_x` of a state `ω` (D3). Consider two hypotheses.

- **(S1) Sharp line labels.** For each `c∈Z²` there are uniformly bounded self-adjoint `X_{c,s}∈𝔄^G`, `s∈Z`, with supports escaping every finite set, such that `τ_β(X_{c,s})=X_{c+2β_⊥,s+β_1}` for all `β∈Z³`, and `π_x(X_{c,s})→δ_{c,x_⊥}·1` strongly as `s→∞`, for every `x`.
- **(S2) Clustering along the ray.** For every self-adjoint local `Y∈𝔄^G` and every `x`, the limit `ρ_x(Y)=\lim_{s→∞}ω_x(τ_{se_1}Y)` exists, depends on `x` only through `x_⊥`, and `\lim_{s→∞}\lim_{t→∞}ω_x(τ_{se_1}(Y)\,τ_{te_1}(Y))=ρ_x(Y)^2`.

By norm approximation, (S2) then holds for every self-adjoint quasi-local `Y∈𝔄^G`: replacing `Y` by a local `Y_n` with `‖Y−Y_n‖<ε` changes every expectation above by at most `2ε‖Y‖+ε²`, uniformly in `s,t`.

**Proposition 3.** Assume (S1) and (S2). Let `(H,π,T,Ũ)` be built from the ray sectors (D4), for any update (D5). Let `H_c` be the closed span of the summands quasi-equivalent to ray sectors on the line `c`, and `C=\{c:H_c≠0\}`. Then `\{H_c\}_{c∈C}` is a label structure with `β·c=c+2β_⊥`, at most four orbits, and stabilizer `Γ_O=Ze_1` for every orbit. Hence no band in `H` has a Clifford node (Theorem 1).

*Proof.* (a) *Line blocks.* Let `σ_i` be a summand quasi-equivalent to `π_x`. By `RCS1.md` R2(a)'s argument (Zorn's lemma: `σ_i` is a direct sum of pieces each unitarily equivalent to a subrepresentation of `π_x`, and strong convergence to a scalar passes to each piece and then to the sum), `σ_i(X_{c,s})→δ_{c,x_⊥}` strongly. The bound is uniform, so `π(X_{c,s})→Π_c` strongly, where `Π_c` projects onto `H_c`. The `H_c` are orthogonal and span `H`, since each summand lies in exactly one of them. Then `T_βΠ_cT_β^*=\mathrm{s\text{-}lim}\,π(τ_βX_{c,s})=\mathrm{s\text{-}lim}\,π(X_{c+2β_⊥,s+β_1})=Π_{c+2β_⊥}`. This is (L1); the orbits are the residues of `c` modulo `2Z²`, and the stabilizer is `\{β:β_⊥=0\}=Ze_1`. Each `Π_c` is central in `π(𝔄^G)″`: it is a strong limit of elements of `π(𝔄^G)`, and it commutes with every `π(A)`, `A` local, because `X_{c,s}` commutes with `A` once its support is disjoint from that of `A` (D1).

(b) *The tick maps line blocks to sums of line blocks.* `Q_c=ŨΠ_cŨ^*=\mathrm{s\text{-}lim}\,π(α(X_{c,s}))`. As `α` commutes with translations, `α(X_{c,s})=τ_{se_1}(Y)` with `Y=α(X_{c,0})`, a self-adjoint quasi-local element of `𝔄^G`. `Q_c` is central, since `\mathrm{Ad}\,Ũ` preserves the centre; so it reduces every summand. Fix a summand `σ_i` quasi-equivalent to `π_x`, and let `Φ:π_x(𝔄^G)″→σ_i(𝔄^G)″` be the normal isomorphism with `Φ(π_x(A))=σ_i(A)`. On `σ_i`'s space, `σ_i(τ_{se_1}Y)→Q_c` strongly. Normal maps are σ-weakly continuous, and a bounded strongly convergent sequence converges σ-weakly; so `π_x(τ_{se_1}Y)→R_x:=Φ^{-1}(Q_c|_{σ_i})` weakly. `R_x` is a central projection of `π_x(𝔄^G)″`. With `Ω=Ω_x`, weak convergence gives `⟨Ω,R_xΩ⟩=\lim_sω_x(τ_{se_1}Y)=ρ_x(Y)`. Also `⟨Ω,R_x^2Ω⟩=\lim_s⟨Ω,π_x(τ_{se_1}Y)R_xΩ⟩=\lim_s\lim_t⟨π_x(τ_{se_1}Y)Ω,π_x(τ_{te_1}Y)Ω⟩=\lim_s\lim_tω_x(τ_{se_1}(Y)τ_{te_1}(Y))=ρ_x(Y)^2`. As `R_x^2=R_x`, `ρ_x(Y)∈\{0,1\}`. If it is `1`, then `‖(1−R_x)Ω‖^2=0`, and centrality gives `R_xπ_x(A)Ω=π_x(A)Ω` for all `A`: `R_x=1`. If it is `0`, `R_x=0`. So `Q_c` restricted to `σ_i` is `1` or `0`, according to `ρ_x(α(X_{c,0}))`, which depends only on the line `x_⊥` (S2). Hence `Q_c=Σ_{c′∈S_c}Π_{c′}`, with `S_c=\{c′∈C:ρ_{(c′)}(α(X_{c,0}))=1\}`.

(c) *Exactly one block.* The same argument for `α^{-1}` gives `Ũ^*Π_{c′}Ũ=Σ_{c″∈S′_{c′}}Π_{c″}`. Each `S′_{c′}`, `c′∈C`, is nonempty, because `Π_{c′}≠0`. For distinct `c′` the sets `S′_{c′}` are disjoint, because the projections `Ũ^*Π_{c′}Ũ` are orthogonal. Then `Π_c=Ũ^*Q_cŨ=Σ_{c′∈S_c}Σ_{c″∈S′_{c′}}Π_{c″}` forces `Σ_{c′∈S_c}|S′_{c′}|=1`, so `|S_c|=1`. This is (L2). □

**Remark 3.1.** (S1) is the hypothesis of `RCS1.md` Lemma 6 ("eventually an eigenvector") for the far-ray observables, written as a family. (S2) holds whenever the ray state is a product, across finite blocks far along the ray, of block states that repeat with period one cell along the ray and do not depend on the head (§4.4). Proposition 3 does not use stationarity of `ω`, matter activation or NN-a.

### 4.4 Four backgrounds on the witness, including a fluctuating-loop state (attack A3)

All four live on the witness at `m=16`, with matter `|i_0⟩∈H_-` at every site. Write `ς∈Λ⁸C^{16}⊗Λ⁸C^{16}` for the pairing vector of `RCSP16.md` definition 5, `ς=W^*(1)/‖W^*(1)‖`.

- **`ω′`** (`RCSP16.md` definition 5): direction-1 links full at the source end, empty at the target end; transverse links `(8,8)`, the two incident `j`-ends at each site paired in `ς`, `j=2,3`.
- **`ω_Φ`** (`CG16B.md` Example S): every link full at its source end, empty at its target end.
- **`ω_8`** (new): every link has 8 rishons at each end; at each site the two incident `j`-ends are paired in `ς` for `j=1,2,3`.
- **`Ψ_λ`** (new; fluctuating loops). Let `𝒫` be the set of unit plaquettes in the `(1,2)`-plane with corners `2β+(0,0,u)`, `2β+(1,0,u)`, `2β+(1,1,u)`, `2β+(0,1,u)`, for `β∈Z³` and `u∈\{0,1\}`. These plaquettes are pairwise vertex-disjoint and every site is a corner of exactly one. For `p∈𝒫` traverse `p` once, counterclockwise in the `(1,2)`-plane, and at each corner `y` put `J^{(p)}_y=Σ_ar^{\mathrm{in},y†}_ar^{\mathrm{out},y}_a`, where "in" and "out" are the plaquette links entering and leaving `y`. Put `W_p=∏_yJ^{(p)}_y` (the factors are even and act on distinct modes, so they commute). `W_p` moves one rishon once around `p`; it is the rishon form of the plaquette Wilson loop. Let `φ_p` be the restriction of `ω_8`'s vector to the four corner stars of `p`, and `ψ_p=(1+λ(W_p+W_p^*))φ_p/‖⋯‖`, `λ∈R\setminus\{0\}`. `Ψ_λ` is the product of the `ψ_p` over `𝒫`.

**Lemma 4.1 (properties).** For each of the four backgrounds:

(a) It is locally gauge invariant, invariant under `τ_β` for every `β`, and sharp in every `P_x` (value `−1`) and every `z_x` (value `+1`). It is a D1 state for `RCSP16.md`'s update `U`, for the update `U′` of `RCSP16_REFEREE.md` N9, and for the base tick followed by its own inverse layers; all three are in LZ1's class and meet NN-a.

(b) The `e_1` strings have `Σ_b‖B_{r,b}(x)Ψ‖^2>0` for every `x` and `r` (`Ψ` the background vector). Every ray state `ω_x` is, beyond the head, a product over finite blocks (site stars for the first three; corner-star quadruples of `𝒫` for `Ψ_λ`) whose far states repeat periodically along the ray and do not depend on the head.

(c) (S1) holds with `X_{c,s}=n_{c,2s}` (`ω′`, `ω_Φ`), `X_{c,s}=n_{c,2s}−8` (`ω_8`) and `X_{c,s}=n_{c,2s+1}−8` (`Ψ_λ`). (S2) holds.

(d) Every ray sector has `χ_tot=−1` and boundary label `−1`: it is spinor class under R-16^str′.

(e) In `Ψ_λ` the end numbers of every plaquette link of `𝒫` are not sharp: the state is a superposition of closed rishon loops around the plaquettes.

*Proof.* (a) For `ω′` and `ω_Φ` this is `RCSP16.md` Theorem 1 and `CG16B.md` Example S. For `ω_8`: `ς` is invariant under `g⊗g` for `g∈SU(16)` (it is the dual of the wedge pairing, and `\det g=1`), and `S_+(g)` has determinant 1 (`CG16B.md` Example S), so every star state is a `Spin(10)` singlet; `S_+⊕1` fixes `|i_0⟩`. Each `J^{(p)}_y` is a `U(16)`-invariant contraction of a creator and an annihilator at the same site, so `W_p` is gauge invariant and `Ψ_λ` is gauge invariant. Translation invariance holds because the patterns are invariant under `2Z³` and the star or block states are translates. `P_x=−1` since matter is in `H_-`. `z_x=−P_x∏_{ℓ∋x}(−1)^{p_{ℓ,x}}`: the six ends at `x` hold `16`, `0` and four `8`s (`ω′`), `16,0,16,0,16,0` (`ω_Φ`), or `8` each (`ω_8`), so `z_x=+1`. `W_p` changes two end numbers at each corner by `±1`, so every component of `Ψ_λ` has the same `z_x=+1`. The three updates: `U` and `U′` are matter-activated (`RCSP16.md` Theorem 2; `RCSP16_REFEREE.md` N9: "It is matter-activated"), and a matter-activated gate "fixes every vector whose support sites carry `P=−1`, whatever the links hold" (`RCSP16_REFEREE.md` N7). The base tick followed by its inverse layers is the identity. Class membership and NN-a are `RCSP16.md` Theorem 2 and N9; for the third update, `CG16B.md` Lemma NN-W compiles base and inverse layers.

(b) *Positivity.* Expand `B_{r,b}(x)=(Σ_aE_{x,ai_0}r^{ℓ_1,x}_a)\,J_{y_1}⋯J_{y_{2r−1}}\,r^{ℓ_{2r},y_{2r}†}_b`, where `J_{y_k}=Σ_ar^{ℓ_k,y_k†}_ar^{ℓ_{k+1},y_k}_a` sums the interior index (the order of factors is the order in the product `T_1⋯T_{2r}`). For `ω′` and `ω_Φ` the norm is `RCSP16.md` Theorem 3 and `CG16B.md` Example S. For `ω_8`, `J_{y_k}` acts on the two `e_1`-ends at `y_k`, which are paired in `ς`. Let `σ_q` be the `SU(16)`-invariant vector of `Λ^qC^{16}⊗Λ^{16−q}C^{16}` (unique up to scale, as `Λ^q` is irreducible); `ς=σ_8`. Write `J=Σ_aX_a`, `X_a=r^{A†}_ar^B_a`; the `X_a` are even, commute, and `X_a^2=0`, so `J^{16}=16!∏_aX_a`, which maps `σ_0=|0⟩_A|\mathrm{full}⟩_B` to `±16!|\mathrm{full}⟩_A|0⟩_B≠0`. `J` commutes with diagonal `SU(16)`, so `J^qσ_0` is invariant and proportional to `σ_q`; since `J^{16}σ_0≠0`, every `J^qσ_0≠0`. Hence `Jσ_8∝J^9σ_0≠0`. The head has norm square `⟨ς,N_Bς⟩=8` and the tail `⟨ς,(16−N_A)ς⟩=8`. So `Σ_b‖B_{r,b}Φ_8‖^2=64‖Jς‖^{2(2r−1)}>0`. For `Ψ_λ`: by the product structure below, the norm is a finite product of block norms, one per block that the string meets. In such a block, `ψ_p` is a finite sum of three orthogonal components (`φ_p`, `W_pφ_p`, `W_p^*φ_p`), which have different end numbers. The string's factors shift end numbers in the same way on all three, so the images stay orthogonal, and the block norm is at least `|\text{coefficient of }φ_p|^2` times the norm of the string's factors on `φ_p`. That last norm is positive by the `ω_8` computation, since `φ_p` is `ω_8`'s block vector. (`W_pφ_p≠0`: at each corner `J^{(p)}_y` moves a rishon between ends in different `ς`-pairs; the reduced state of one end of `ς` is maximally mixed on `Λ⁸`, so `⟨r^†_br_a⟩=δ_{ab}/2`, the cross terms vanish, and `‖J^{(p)}_yφ‖^2=Σ_aP(a∈B)P(a∉A)=4`.)
*Product structure.* Each factor of `B_{r,b}` acts within one site star: the head on the matter and an end at `x`, each `J_{y_k}` on two ends at `y_k`, the tail on an end at `y_{2r}`. The four backgrounds are products over site stars (`ω′`, `ω_Φ`, `ω_8`) or over the corner-star quadruples of `𝒫` (`Ψ_λ`), with block states of definite parity. So `B_{r,b}Ψ` is a product over the same blocks. All block states along the ray beyond the head are translates of one modified block state (period `2e_1`); the head and the tail affect only their own blocks. For a gauge-invariant local `A` supported away from the tail, `ω^{(x)}_r(A)` is the product-state value and does not depend on `b` or `r` once the tail has passed `A`'s support (`RCSP16_REFEREE.md` N1). Passing to the limit, `ω_x` is a product across these blocks for even observables, with the stated periodicity.

(c) *(S1).* For `ω′` and `ω_Φ`: "On each link far along the ray from `x`, its target-end number is sharply 1 in `ω_x`; on the same links it is sharply 0 in `ω_{x′}` if the lines differ" (`RCSP16.md` Theorem 3). Sharp values on the cyclic vector, and commutation with each local element once the support is passed, give strong convergence, as in `RCS1.md` Lemma 6. For `ω_8` the values are `9` on the ray and `8` off it. For `Ψ_λ` use the links `ℓ_{c,2s+1}`, from `(2s+1,c)` to `(2s+2,c)`: they join two blocks and lie in no plaquette of `𝒫`, so their end numbers are sharply `8` in the background, `9` on the ray and `8` off it. Covariance `τ_β(X_{c,s})=X_{c+2β_⊥,s+β_1}` holds by D2. *(S2)* follows from (b): for `t−s` large, `τ_{se_1}Y` and `τ_{te_1}Y` lie in disjoint unions of blocks, both are even, and the product state factorizes; the single expectations are eventually constant and depend only on the line.

(d) `CG16B.md` Proposition L applies: the witness satisfies (F), its links are link-pure, it is even-translation covariant; the background is D1 and sharp in every `z_y` and every `P_Λ`; and `B_{r,b}` commutes with every `z_y`, `y≠y_{2r}`, and is matter-odd with its matter at `x` (`CG16B.md` Theorem 6.2). Proposition L(ii)-(iii) give `χ_tot=−1` and boundary label `−1`.

(e) `φ_p`, `W_pφ_p` and `W_p^*φ_p` are nonzero and orthogonal (end numbers `8`, `8±1` on each plaquette link). □

**Corollary 4 (every update, four backgrounds).** Over `ω′`, `ω_Φ`, `ω_8` and `Ψ_λ`, take the `e_1`-ray sectors and any update (D5), matter-activated or not, for which the background is D1. No covariant representation built from these sectors has a band with a Clifford node. The sectors are spinor class under R-16^str′. For `ω_Φ` the same holds for every positive coordinate axis.

*Proof.* Lemma 4.1(c) and Proposition 3. For `ω_Φ`, the cell rotations carry the construction to the other axes. □

**Attack A3, run.** `Ψ_λ` is an explicit, exactly solvable, fluctuating-loop D1 state for three LZ1-class updates that meet NN-a. Its `e_1`-ray sectors exist and are spinor class. A3 fails on it at a named step: **the loops of `Ψ_λ` do not reach the inter-block links `ℓ_{c,2s+1}`; the string raises their target number from a sharp `8` to a sharp `9`, so the transverse position of the ray is observable** (Lemma 4.1(c)). The far-end escape fails on all four backgrounds for every update (Corollary 4); this extends the no-Clifford-node clause of `RCSP16.md` Theorem 9 to all updates; its transverse-flatness clause is not extended. A loop dynamics that fixes `Ψ_λ` also exists: the layer of gates `e^{−iθ|ψ_p⟩⟨ψ_p|}`, `p∈𝒫`, is gauge invariant, commuting and `2Z³`-covariant. It is not rotation covariant, since `𝒫` has one plaquette orientation, so it is not offered as an NN-a update. Loops that reach every ray link are the subject of §4.5.

### 4.5 The lowest level: why the witness's strings stay visible

**Lemma 5 (the lowest level is emptied; witness, any `m`, any state).** Let `ω` be any state of `𝔄` and `ℓ_k` the `k`-th link of the ray from `x` (D3), `1≤k≤2r`. Then `Π^{(j)}_{ℓ_k}B_{r,b}(x)=B_{r,b}(x)Π^{(j−1)}_{ℓ_k}`, with `Π^{(j−1)}=0` when `j−1` is not a value of `n_{ℓ_k}`. With `j_0=j_0(ℓ_k;ω)` (D9), `ω^{(x)}_r(Π^{(j_0)}_{ℓ_k})=0`. Hence every ray state has `ω_x(Π^{(j_0)}_{x_⊥,s})=0` and `π_x(Π^{(j_0)}_{x_⊥,s})Ω_x=0` for every ray link `ℓ_{x_⊥,s}`, `s≥x_1`; and for any choice of levels `j_s=j_0(ℓ_{x_⊥,s};ω)`, `π_x(Π^{(j_s)}_{x_⊥,s})→0` strongly as `s→∞`.

*Proof.* `n_{ℓ_k}` counts the 16 target-end modes of `ℓ_k`. In each term of `B_{r,b}(x)` exactly one factor acts on these modes: the creator `r^{ℓ_k,y_k†}_{a_k}` of `T_k`. The annihilator of `T_k` acts on the source end. So `n_{ℓ_k}B=B(n_{ℓ_k}+1)`, and by functional calculus `Π^{(j)}_{ℓ_k}B=BΠ^{(j−1)}_{ℓ_k}`. Then `B^*Π^{(j_0)}_{ℓ_k}B=B^*BΠ^{(j_0−1)}_{ℓ_k}`. By minimality of `j_0`, `ω(Π^{(j_0−1)})=0`, and Cauchy–Schwarz gives `|ω(XΠ^{(j_0−1)})|^2≤ω(XX^*)ω(Π^{(j_0−1)})=0` for every `X`. Sum over `b` and divide by the positive denominator. In the limit `ω_x(Π^{(j_0)})=0`, so `‖π_x(Π^{(j_0)})Ω_x‖^2=0`. For local `A∈𝔄^G`, `Π^{(j_s)}_{x_⊥,s}` commutes with `A` once `ℓ_{x_⊥,s}` lies outside `A`'s support (D1); so `π_x(Π^{(j_s)}_{x_⊥,s})π_x(A)Ω_x=0` for large `s`. The operators have norm at most 1, so the strong convergence extends from the dense set `π_x(𝔄^G)Ω_x` to `H_x`. □

**Lemma 6 (escaping test for disjointness).** Let `ρ_1,ρ_2` be representations of `𝔄^G` and `Z_s∈𝔄^G` uniformly bounded. If `ρ_1(Z_s)→0` strongly and `ρ_2(Z_s)→q·1` weakly with `q≠0`, then `ρ_1` and `ρ_2` are disjoint.

*Proof.* Let `S` be bounded with `Sρ_2(A)=ρ_1(A)S` for all `A`. For vectors `u,w`, `⟨u,Sρ_2(Z_s)w⟩=⟨u,ρ_1(Z_s)Sw⟩→0`, while `⟨S^*u,ρ_2(Z_s)w⟩→q⟨u,Sw⟩`. So `q⟨u,Sw⟩=0` for all `u,w`, and `S=0`. □

This is the weak-limit companion of `RCS1.md` Lemma 6, which needs sharp eventual eigenvalues in both representations.

**Theorem 7 (block-product backgrounds; witness, any `m`).** Let `Φ` be a product state of `𝔄` over a `2Z³`-invariant partition of all modes (matter modes and link-end modes) into finite blocks of diameter less than `D`, each block containing whole link ends (all 16 modes of an end) and each block state of definite parity. Let `ω` be a cell-translation-invariant state of `𝔄` that agrees with `Φ` on `𝔄^G` (for example the gauge average `Φ∘E`, when that average is cell-translation invariant, as in `RCS1.md` R1(b)). Assume the stated ray limits exist. Let `ω_x`, `ω_{x′}` be ray states along `e_1` with `|x_⊥−x′_⊥|≥D`. Then `π_x` and `π_{x′}` are disjoint. For covariantly chosen ray sectors, every `Γ_x⊆Ze_1`; so if the ray sectors are factor representations, no update gives a Clifford node (Corollary 2).

*Proof.* Put `c=x_⊥`, `c′=x′_⊥`, and `Z_s=Π^{(j_0)}_{c,s}` for even `s`, with `j_0` the lowest level for these links (by `2Z³`-invariance it is the same for all even `s`). Lemma 5 gives `π_x(Z_s)→0` strongly. Let `B′_b=B_{r,b}(x′)`. It acts on the matter at `x′` and on the direction-1 links of line `c′`; it is matter-odd, so `B′^*_bXB′_b` is even for even `X`. For local `A,A′∈𝔄^G` and large even `s`, `Z_s` commutes with `A′` and `B′_b` (disjoint supports, `Z_s` even), so `ω^{(x′)}_r(A^*Z_sA′)=Σ_bΦ(B′^*_bA^*A′B′_bZ_s)/Σ_bΦ(B′^*_bB′_b)`. The sums, rather than necessarily each individual summand, are gauge invariant, so agreement of `ω` and `Φ` applies to them. The block containing the target end of `ℓ_{c,s}` has diameter below `D`, so it meets neither line `c′` nor `x′`, and for large `s` it misses the supports of `A,A′`. The product state of definite-parity blocks factorizes even operators on disjoint unions of blocks, so `Φ(B′^*_bA^*A′B′_bZ_s)=Φ(B′^*_bA^*A′B′_b)Φ(Z_s)`. Hence `ω_{x′}(A^*Z_sA′)=q\,ω_{x′}(A^*A′)` for large even `s`, with `q=Φ(Z_s)=ω(Z_s)>0` by the definition of `j_0` (`Z_s` is gauge invariant). So `π_{x′}(Z_s)→q·1` weakly on the dense set `π_{x′}(𝔄^G)Ω_{x′}`, and by boundedness everywhere. Lemma 6 gives disjointness. If `β_⊥≠0`, then for large `k`, `|2kβ_⊥|≥D`, so `kβ∉Γ_x`; as `Γ_x` is a group, `β∉Γ_x`. □

**GAP and correction to draft Theorem 7.** The draft assumed only a translation-invariant block partition, but its proof asserts that `j₀` and `q` are independent of `s`. The partition alone does not imply this: take a translation-invariant partition into single-link blocks, with link states alternating by longitudinal cell, one with target number 0 and the other with target number 1. The corrected theorem above assumes cell-translation invariance of `ω` on the observable algebra. The proof then has constant `j₀` and `q` on even links. The uncorrected general statement is not established by that proof. It is false: a single-link block product with lowest-level weights `ε_s` summable along `e_1` has non-disjoint ray sectors on lines at distance `D` (`RCSPC_REFEREE.md` N1). (referee closure, RCSPC_REFEREE.md), unrefereed.

**Scope of Theorem 7.** Subject to the stated cell-translation invariance and existence of ray limits, it covers gauge averages of product states over single links and single sites (`D=2`): link states may superpose different end numbers, so these are fluctuating backgrounds, the lattice analogue of Higgs-type states in which every link sits near a fixed coherent configuration. It also covers `ω′`, `ω_Φ`, `ω_8` and `Ψ_λ` (`D=2`; the blocks of `Ψ_λ` have diameter `√2`). It does not need stationarity, an update, or sharp centre labels. For spinor class (Lemma 4.1(d)) the background must in addition be sharp in every `P_x` and `z_x`. For no Clifford node it needs factor ray sectors, which no frozen text supplies; §4.4 removes that need for its four backgrounds.

**Remark 5.2 (why a bounded register matters).** Lemma 5 uses only that `T_k` raises a number with a lowest occupied level. (a) On integer-rotor links the link operator `e^{iθ_ℓ}` is unitary and the electric number has no lowest level; there a flux-free state absorbs a straight string, and the main-branch rotor note builds an exact Gauss dressing ("an explicitly constructed isometry"). (b) On `Z₂` links the string factor is a unitary of square one; closed `Z₂` loops act trivially on the toric-code ground state, and sectors with different string paths are equivalent (Naaijkens, arXiv:1012.3857; the main-branch three-axis note's charges move by single `Z` operators). (c) On the witness `T_k` is a non-invertible rishon transfer (`RCS1.md` R4: the strings are not multiples of unitaries), and Lemma 5 applies to every state. So the A3 escape on the witness cannot come from absorbing the string link by link. It needs the displaced ray to empty the same level on the original line (§4.6).

### 4.6 What a Clifford node would need on the witness: the cone lift

**Lemma 8 (quasi-equivalent factor states agree at infinity; one direction of Powers' criterion, rebuilt).** Let `φ_1,φ_2` be states of `𝔄^G` whose GNS representations are quasi-equivalent factor representations. Let `Z_s∈𝔄^G` be uniformly bounded with supports escaping every finite set. Then `φ_1(Z_s)−φ_2(Z_s)→0`.

*Proof.* Let `π_1,π_2` be the GNS representations, `Ω_2` the cyclic vector of `π_2`, and `Φ:π_1(𝔄^G)″→π_2(𝔄^G)″` the normal isomorphism with `Φ∘π_1=π_2`. Then `φ_2=\tilde φ_2∘π_1` with the normal state `\tilde φ_2=⟨Ω_2,Φ(·)Ω_2⟩`. Suppose `|φ_1(Z_s)−φ_2(Z_s)|≥ε` along a subsequence. The ball of `π_1(𝔄^G)″` is weakly compact, so `π_1(Z_s)` has a weak cluster point `Y` along a subnet of it, and `Y∈π_1(𝔄^G)″`. For local `A∈𝔄^G`, `[Z_s,A]=0` once the supports are disjoint (D1); so `Y` commutes with `π_1(A)`, and by density `Y∈π_1(𝔄^G)′`. The representation is a factor, so `Y=y·1`. Along the subnet, `φ_1(Z_s)→y`, and `φ_2(Z_s)=\tilde φ_2(π_1(Z_s))→\tilde φ_2(Y)=y`, because normal states are weakly continuous on bounded sets. So the difference tends to `0` along the subnet, a contradiction. □

**Proposition 9 (cone lift is necessary; witness, any `m`).** Let `ω` be a translation-invariant state of `𝔄` with covariantly chosen ray sectors `π_x` along `e_1` (D3) that are factor representations. Suppose that, for some update, some covariant representation built from them has a band with a Clifford node. Then there is a site `x` and a subgroup `Γ⊆Z³` of finite index such that, for every `β∈Γ` and with `c=x_⊥` and `j_s=j_0(ℓ_{c,s};ω)`,
\[
\lim_{s→∞}\,ω_{x+2β}\big(Π^{(j_s)}_{c,s}\big)=0 .
\]
`Γ` contains elements `β` whose transverse parts `β_⊥` are nonzero and span `R²`. In words: a ray on the line `c+2β_⊥` empties, far along, the lowest level that the background occupies on the line `c`. Call this the **cone lift**.

*Proof.* Corollary 2 gives `x` with `Γ=Γ_x` of finite index, and transverse parts spanning `R²`. For `β∈Γ`, `π_{x+2β}` is quasi-equivalent to `π_x`, and both are factors. Lemma 8 with `Z_s=Π^{(j_s)}_{c,s}` gives `ω_x(Z_s)−ω_{x+2β}(Z_s)→0`, and Lemma 5 gives `ω_x(Z_s)=0` for `s≥x_1`. □

**Remark 9.1 (why "cone").** By covariance, `ω_{x+2β}=ω_x∘τ_β^{-1}`, so Proposition 9 says that the single ray state `ω_x` has `ω_x(Π^{(j)}_{c−2β_⊥,s})→0` along the line `c−2β_⊥`, for every `β∈Γ`, with `j` the background's lowest level there. The limit is taken along each line separately. As `β` runs through `Γ`, the displacement `2β_⊥` takes arbitrarily large values. So one ray state must suppress the lowest level on lines at every transverse distance in a coset of `2Γ_⊥`, each beyond some longitudinal distance. In Theorem 7's backgrounds the same quantity tends to `q>0` instead. A cone-lifting background must therefore correlate distant parallel lines over infinite length. The weight `Σ_bB^*_bB_b` of one ray must suppress the lowest level of every line of a two-dimensional lattice of lines, far enough along.

**Remark 9.2 (the ray disappears far along).** Under the hypotheses of Proposition 9, Lemma 8 applies to every uniformly bounded escaping family, not only to `Π^{(j)}`. With covariance, `ω_x(f_s)−ω_x(τ_γ^{-1}f_s)→0` for every `γ∈Γ` and every uniformly bounded family `f_s∈𝔄^G` whose supports escape every finite set, as `s→∞`. So far along, `ω_x` is asymptotically invariant under the translations `2γ`, `γ∈Γ`, which move its own line to other lines. The ray's line becomes indistinguishable from the lines of a two-dimensional lattice. That is the precise sense in which a Clifford node needs the transverse position to be unobservable.

### 4.7 The open lemma RCSPC-CL and three attacks on it

**RCSPC-CL (open).** On the U(16)-rishon witness at `m=16`, no D1 state that is sharp in every `P_x` and every `z_x` has covariantly chosen factor `e_1`-ray sectors with the cone lift of Proposition 9.

**RCSPC-CL′ (open; proposed wording, not adopted).** On the witness at `m=16`, no D1 state sharp in every `P_x` and `z_x` has covariantly chosen factor `e_1`-ray sectors with `π_x` quasi-equivalent to `π_{x+2β}` for every `β` in a subgroup of finite index of `Z³`. RCSPC-CL implies RCSPC-CL′ (Proposition 9), and RCSPC-CL′ suffices for no update to give a Clifford node on factor spinor-class `e_1`-ray sectors (Corollary 2). The same three attacks below failed on it. It holds for cell-invariant block products (Theorem 7) and states with an exact line-tying number relation (Lemma RL).

If RCSPC-CL holds, Corollary 2 and Proposition 9 give: no update and no such state yields a Clifford node on factor spinor-class `e_1`-ray sectors. If it fails, Proposition 9 says what the failing state must do; whether such a state then carries a Clifford node is not decided here. Stationarity gives no help to either side: the base tick followed by its inverse layers is the identity, it is in LZ1's class and meets NN-a (Lemma 4.1(a)), and every gauge-invariant, translation-invariant state is D1 for it.

**Attack A (decoupling for all states).** *Aim:* prove, for every such D1 state, that `ω_{x′}(Π^{(j)}_{c,s})` has a positive limit point for a displaced ray, as Theorem 7 does for block products. *The step that fails:* Theorem 7 factorizes `Φ(B′^*_bA^*A′B′_bZ_s)=Φ(B′^*_bA^*A′B′_b)Φ(Z_s)`. For a general state the weight `X=Σ_bB′^*_bB′_b` runs parallel to the line `c` at the fixed distance `|c−c′|` along its whole length. So no clustering statement separates `X` from `Z_s`: factor clustering separates an observable only from observables far away from it, and `X` passes next to every `Z_s`. A positivity bound `ω(XZ)≥γ\,ω(X)ω(Z)` for commuting positive `X,Z` on disjoint supports would suffice, but it is false for entangled states. Example: on two qubits in `(|00⟩+|11⟩)/\sqrt2`, `X=|0⟩⟨0|⊗1`, `Z=1⊗|1⟩⟨1|` give `ω(XZ)=0` and `ω(X)ω(Z)=1/4`. The D1 conditions (gauge and translation invariance, stationarity) do not supply such a bound.

**Attack B (an asymptotic flux observable, after Buchholz).** *Aim:* find observables at infinity that detect the line of the ray, as the asymptotic electric flux distribution does in QED (Buchholz 1982, NOT VERIFIED). The exact relation is `n_{c,s}B=B(n_{c,s}+1)` on the ray (Lemma 5), so for any function `f` of target numbers, `ω_x(f(n))=ν_x(f(n+1_c))`. Here `ν_x` is the background weighted by `Σ_bB^*_bB_b`, and `1_c` adds one on the ray's line. A transverse dipole `Σ_{c″}c″_2n_{c″,s}` over a far cross-section is therefore shifted by exactly `c_2` relative to `ν_x`. *The step that fails:* `ν_x` itself is not controlled. Only its support is (it lies in the background's support, which is the content of Lemma 5). A weighted mean can move by more than the exact shift, in either direction. Remark 9.2 shows that under cone lift the weighting makes all lines of a lattice coset look alike far along. An asymptotically vanishing dipole difference between `ω_x` and `ω_{x+2β}` is not excluded by these relations.

**Attack C (a stacking bound).** *Aim:* use the bounded register. At most 16 rishons can cross a link, so the product of any 17 strings along one line is zero, while 17 strings on 17 distinct lines need not be. If a string on line `c` could be moved to line `c+2β_⊥` by a local operation, stacking 17 moved strings would contradict the bound. *The step that fails:* straight-string limit sectors carry no composition law. `RCS1.md` R4 treats the `L5` laws; on the witness, Lemma 5 shows directly that `B^*B` has a kernel, since `B` kills the top level. The strings are not multiples of unitaries, so `\mathrm{Ad}\,B` is not an automorphism and there is no localized endomorphism to compose. Quasi-equivalence of two single-string limits gives a normal isomorphism of von Neumann algebras, not local intertwiners that act on a second string.

**Rigid-plane counterexample attempt — GAP.** The draft asserts that the string weight vanishes only where its line cannot be raised (`n_s=16`). This is false without further state assumptions. The previous example with `n_s=0`, `n_{s+1}=16` does not refute it, since that next link is at the top level.

**Why the GAP is still real.** The weight depends on which flavours are
occupied, not only on the numbers. Referee counterexample to the
draft's sentence, with fluctuating rigid planes: on every direction-1
link with target number `n`, occupy flavours `{1,…,n}` at the target end
and `{1,…,16−n}` at the source end. At a ray site `y_k` the factor
`J_{y_k}=Σ_ar^{ℓ_k,y_k†}_ar^{ℓ_{k+1},y_k}_a` needs a flavour that is a
hole at the target of `ℓ_k` and occupied at the source of `ℓ_{k+1}`:
`\{n_k+1,…,16\}∩\{1,…,16−n_{k+1}\}≠∅`, that is `n_k+n_{k+1}≤15`. Let each
plane value `n_s` be `8` or `10`, independently over `s` and equal on all
lines of the plane, with fixed even numbers on transverse links and
matter `|i_0⟩`. Take the gauge average of this mixture. Then
`n_k+n_{k+1}≥16` everywhere, so every term of `B_{r,b}` annihilates every
configuration, and the gauge-invariant weight is `0`, although no link
has `n=16`. The state is gauge and translation invariant, sharp in every
`P_x` and `z_x` (all end numbers even), and fixed by the base tick
(matter-activated: `RCSP16.md:28`, `RCSP16_REFEREE.md:118`). So the
draft's positivity sentence fails without state assumptions, as the
distiller says.

(referee closure, RCSPC_REFEREE.md), unrefereed.

**Lemma RL (referee closure, RCSPC_REFEREE.md), unrefereed.**

*Statement.* Let `ω` be any state of `𝔄` on the witness (any `m`). Let
`x`, `x′` lie on distinct lines `c≠c′` and let their ray states exist.
Suppose there are fixed lines `c_1,…,c_q` and fixed integers
`κ_1,…,κ_q` (independent of `s`), with `c=c_1`, `κ_1=1` and
`c′∉\{c_1,…,c_q\}`, such that for all large `s` the state `ω` is sharp
in `L_s=Σ_iκ_in_{c_i,s}`, with value `k_s`. Then `π_x` and `π_{x′}` are
disjoint.

*Proof.* `B_b^*B_b` commutes with every target number: `n_ℓB=B(n_ℓ+1)`
on ray links (Lemma 5) gives `B^*Bn_ℓ=n_ℓB^*B`, and off the ray they
commute. Let `g_s` be the spectral projection of `L_s` off `k_s`; then
`ω(g_s)=0` and `0≤ω(B_b^*B_bg_s)=ω(g_sB_b^*B_bg_s)≤‖B_b‖^2ω(g_s)=0`. By
functional calculus `f(n)B=Bf(n+1_c)`, where `1_c` adds one on the ray
links. For `s` on the ray, `L_s(n+1_c)=L_s(n)+1`, so the spectral
projection of `L_s` off `k_s+1`, evaluated in `ω^{(x)}_r`, equals
`Σ_bω(B_b^*B_bg_s)/Σ_bω(B_b^*B_b)=0`. Hence `L_s−k_s` is sharply `1` in
`ω_x`. The ray of `x′` touches none of the lines `c_i`, so `L_s−k_s` is
sharply `0` in `ω_{x′}`. These are uniformly bounded, self-adjoint,
gauge-invariant local elements with escaping supports, and each cyclic
vector is eventually an eigenvector of them. `RCS1.md` Lemma 6
(line 95) gives disjointness. □

Rigid planes are the case `L_s=n_{c,s}−n_{c″,s}`, with a third line
`c″∉\{c,c′\}` and `k_s=0`. The draft's "complementary variant" is
`L_s=n_{c,s}+n_{c_B,s}`, `k_s=16`. In both cases Lemma RL gives disjoint
sectors on distinct lines. So `Γ_x⊆Ze_1`; no two sectors on distinct
lines are quasi-equivalent; and with factor sectors Corollary 2 excludes
a Clifford node. No translation invariance is needed.

Rigid planes, and every exact linear number relation that ties the ray’s line to untouched lines, give disjoint sectors on distinct lines, hence no Clifford node; whether such a state can meet the bare cone-lift limit is not decided. Disjointness alone does not prove the converse of Proposition 9.

**Status.** RCSPC-CL is a lemma on which three distinct attacks (A: decoupling, B: asymptotic flux, C: stacking) failed at the named steps; the rigid-plane attempt gives no node (Lemma RL) and leaves the bare cone-lift limit undecided. It is open. It is not claimed to be true or false.

**RCSPC-NF (open).** Over a D1 witness background sharp in every `P_x` and `z_x`, whose `e_1`-ray sectors are not factor representations and fail (S1)-(S2): does some update and some covariant representation built from them have a Clifford-node band?

### 4.8 D-reg, RC-W and R-16^str′

**Corollary 10 (D-reg's half-column defects; every update).** On D-reg (`CG16D.md` §5), take Theorem 9's columnar D1 state and its half-column string defects along the column axis, chosen covariantly. `CG16D.md` Theorem 9: "A half-column shift gives a weak-* string-limit state with a single unmatched link and `χ_sp=−1` relative to that state." For every update in LZ1's class, no covariant representation built from these defect sectors has a band with a Clifford node.

*Proof.* Proposition 3's proof uses only (S1), (S2), D4 and D5, and that the update maps even elements to even elements; LZ1's class has even gates. (S1): far along the shifted half-column, the links paired in the shifted pattern carry two arrows, while in the background those links carry none; elsewhere nothing changes. Arrow positions are gauge invariant (`ε_{ℓ,x}` is a function of the end's `|0⟩` or `H` content). So the projector onto "two arrows" on the far link of column `c` at the shifted position has eventual eigenvalue `1` in sectors on column `c` and `0` in the others; it is even, so it commutes with every local element once the supports are disjoint. (S2): `CG16D.md` Theorem 9 says "The D1 state and string states are product states whose local vectors lie in such spaces", "The product is therefore of even pure states on disjoint finite blocks"; far along the column the blocks repeat with the shifted pattern, whatever the head. □

This answers CG16D-NLP's Clifford form over that state. Its longitudinal part (a nonzero `N` along the column) is untouched, and so are the energy question and the NN-a form of D-reg's base matter gates.

**Corollary 11 (no Weyl point either).** In every label structure of Theorem 1, no band has a Weyl point in the sense of `CG16S.md` §4: "assume `dim ker(V(K₀)−1)=2`, a smooth local logarithm `H=i log V`, and a smooth rank-two spectral frame with `H=a1+b·σ`, `a(K₀)=b(K₀)=0`. Put `N_{ij}=∂_j b_i(K₀)`. Require `N` invertible".

*Proof.* Near `K₀`, `b(K)≠0` for `K≠K₀`, since `N` is invertible. On the frame the two branches are `a±|b|`, with `∂_n(a±|b|)=∇a·n±\hat b·∂_nb`. Along a direction `ν`, these tend to `∇a(K₀)·n±(Nν·Nn)/|Nν|`. As `ν` runs over `S²`, `(Nν·Nn)/|Nν|` takes every value between `0` (at `ν` with `Nν⊥Nn`) and `|Nn|` (at `ν` parallel to `n`). The other eigenvalues of the Weyl point’s smooth local logarithm `H` stay away from `0` near `K₀`. Put `g=pH` and `W=V^p=e^{−ig}`; the frame branches of `g` are `p(a±|b|)`. Choose `ν` so that `p(∇a(K₀)·n_O±(Nν·Nn_O)/|Nν|)≠−θ_O` for every orbit and both signs; each excluded set of directions is a level set of the non-constant real-analytic function `ν↦(Nν·Nn_O)/|Nν|` on `S²` (analytic because `|Nν|>0`), hence closed with empty interior, so finitely many of them omit an open set of `ν`. The convergence of the slopes is uniform for `ν` in a compact cap, because `|Nν|` is bounded below. For each selected simple frame branch, use the graph and disjoint shifts of Step 3 of Theorem 1, but replace its spectral-window equality by `1_Γ(K,W(K))≥1_{B_3}(K)P_i(K)`: the eigenprojection of `W` contains `P_i` even if other eigenvalues coincide after exponentiation. The separability argument gives `E(Γ)=0`; Lemma 1.1 and the isometry `F` force `1_Γ=0` almost everywhere on `B_3`, contradicting `P_i≠0`. The graph, disjoint shifts and separability step are unchanged. Then argue as in Step 4 of Theorem 1, using Lemma 1.2 on the dense set `U`. (referee closure, RCSPC_REFEREE.md), unrefereed. □

**RC-W.** No Clifford node and no Weyl point is built in this file; in the classes of Corollaries 2, 4 and 10 and Theorem 7 (with factor sectors) none exists. So the question "does RC-W force a mirror partner?" does not arise for any node found here. For the record, RC-W's Weyl-pairing application needs, in `CG16S.md`'s words at line 140, a node set that "is finite and consists of Weyl points", in a setting that "has no links"; `RCSP16.md` Theorem 10 already found those hypotheses unmet for the longitudinal band.

**R-16^str′.** Every ray sector used in Corollary 4 is spinor class under R-16^str′ (Lemma 4.1(d)), and so is every ray sector of Theorem 7's backgrounds that are sharp in every `P_x` and `z_x` (`CG16B.md` Proposition L). Proposition L(i)-(iii) do not use stationarity (`CG16B.md:143-145`), so they apply to every gauge-invariant background sharp in every `P_x` and `z_x`. (referee closure, RCSPC_REFEREE.md), unrefereed. The no-go results are therefore statements about spinor-class sectors in the sense the lane brief asks for, under that candidate reading. They do not adopt it.

## 5. Checks of readings and hypotheses

The four tests ask whether an item (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. `P` passes, `C` is conditional, `F` fails. These are pass-1 judgments. Nothing below is proposed for adoption.

| Item | Status here | 1 | 2 | 3 | 4 | Check |
|---|---|---|---|---|---|---|
| R-CS^str with `χ_tot` | owner's working candidate, used | P | C | C | C | Recorded verdicts of `RCS1.md` §7; unchanged. The results hold for every covariant choice of limit points, so they do not use the open quantifier. |
| R-16^str′ | owner candidate, used for the word "spinor" | P | C | P | P | Recorded verdicts of `CG16B.md` §7; unchanged. No step uses it; it only names the sectors. |
| "Built from ray sectors" (D4) | RCS-P's own representation class | P | P | P | P | It is the class of `RCSP16.md` Theorem 9 and of RCS-P, not a new restriction. |
| "Every update" (D5) | widening | P | P | P | P | It widens LZ1's class, so it cannot exclude a candidate update. |
| Label structure (D7) | theorem hypothesis | P | P | P | P | A closed pair of conditions on `(T,Ũ)`. It is proved, not assumed, in Corollaries 2, 4 and 10. |
| (S1), (S2) | theorem hypotheses | P | P | P | P | Closed conditions, proved for the four backgrounds and D-reg's columnar state. |
| Factor ray sectors | hypothesis of Corollary 2, Theorem 7's last clause, Proposition 9 | P | P | C | P | Test 3 is conditional: if it were made part of R-CS^str (keep only factor limit points), it would exclude non-factor sectors, where RCSPC-NF stays open. It is a hypothesis of theorems, not a reading. |
| Block-product backgrounds (Theorem 7) | class of a theorem | P | P | P | P | A named class with one constant `D`, which the theorem needs. |
| Cone lift (Proposition 9) | derived condition | P | P | P | P | It is a consequence, not an assumption. |
| `ω_8`, `Ψ_λ` | witnesses | — | — | — | — | Not proposed. As vacuum proposals they would fail test 4 (the `ς`-pairings, the plaquette pattern `𝒫` and `λ` are structure the working set does not supply) and test 3 (they would fix a phase). |
| Base tick followed by its inverse layers | used for non-vacuity only | — | — | — | — | `RCSP16.md` leaves the cancellation question with the owner. Corollary 4 needs no cancellation: `U′` of `RCSP16_REFEREE.md` N9 has no inverse layer and also makes the four backgrounds D1. |

No reading is needed that the frozen files do not already name. The owner's guidance ("we can specify if needed") is met by stating the factor hypothesis openly instead of proposing it.

## 6. Open items and downstream limits

- **RCSPC-CL**, **RCSPC-CL′** and **RCSPC-NF** are stated in §4.7 above. The first asks whether a sharp D1 witness background has cone-lifting factor ray sectors; the second is the weaker finite-index quasi-equivalence statement; the third covers non-factor sectors outside (S1)–(S2). All remain open.
- **RCS-P** remains open in its Clifford form. **MT1-S[R-CS^str]** in the VC1 vacuum, **R-CS**, **R-16^str′**, **RCSP16-BT**, and **CG16D-NLP** for longitudinal motion, energy and base-gate compilation remain open. The owner question on cancelling base layers remains open. D-reg supplies `χ_sp`; identifying it with `χ_tot` needs a separate parity-sharpness bridge, as `prior/RCSPC.md` notes.
- Under the proposed R-16^str′ reading, the stated witness sectors are spinor class; this does not establish an irreducible 16 or physical spatial spin.

**Live-law carry-over (referee closure, RCSPC_REFEREE.md), unrefereed.**

*Law-independent results.* Theorem 1, Lemmas 1.1-1.3, Corollary 2, Proposition 3, Lemmas 6 and 8, and Corollary 11 use only a
separable covariant representation of a quasi-local `𝔄^G` in which even
local elements commute with local elements of disjoint support. Both
`L5` laws are fermionic quasi-local algebras, where even local elements
commute with every local element on disjoint modes; `RCS1.md:32` gives
the representation class.

*`L5-U[m]`: the mechanism is present.* `RCS1.md:86`: "On U, for a
positively oriented link, `(T_i)_{ab}=(U^{ba}_{ℓ_i})*=r^{ℓ_i,y_{i−1}}_a
r^{ℓ_i,y_i*}_b`", and `B_{r,b}=Σ_a(T_1⋯T_{2r})_{ab}c^†_{x,a}`
(`RCS1.md:195`). The far-end number of `ℓ_i` is bounded (five flavours: "`5−k` for the last index", `RCS1.md:115`),
even and gauge invariant, and only `T_i`'s creator acts on that end. So
`nB=B(n+1)` and Lemma 5's proof applies word for word. Theorem 7
(corrected) and Proposition 9 follow on `L5-U[m]`, since their proofs use
only Lemma 5, Lemmas 6 and 8, Corollary 2 and product factorization.

*`L5-U[2k]`, `k=1,2`, over `ω_AB`: every update.* (S1) holds with
`X_{c,s}` the far-end number of `ℓ_{c,s}` minus `k`, since "each ray link
has end numbers `(k−1,k+1)` from near to far, and every other link has
`(k,k)`" (`RCS1.md:107`). (S2) holds: in each index term the interior
index `a_i` occurs only at `y_i` (far end of `ℓ_i`, near end of
`ℓ_{i+1}`), and the head pairs `c^†_{x,a_0}` with the near end of `ℓ_1`
at `x`. So `B_{r,b}` is a product of factors each inside one site star,
`Φ_AB` is a product of Fock vectors, and the ray state is a product over
site stars with period one cell along the ray, independent of the head,
as in Lemma 4.1(c). Proposition 3 gives: for every update in the sense
of D5, no covariant representation built from these `χ_tot=−1` sectors
(`RCS1.md` R2(d)) has a Clifford-node band. This extends the
no-Clifford-cone clause of `RCS1.md` Theorem 8(d) from the base tick to
every update. Its transverse-flatness clause is not extended, because it
uses tick equivalence (`RCS1.md:125`: "the tick equivalence in (c) make each group invariant").

*`L5-O[S_+]`: the mechanism is absent.* `RCS1.md:195`: "each `(T_i)_{ac}`
is `±iη^{\rm far}_cη^{\rm near}_a`, with one sign for all indices; it is a
self-adjoint unitary." Lemma 5 needs a bounded self-adjoint link
observable `n` with `nW=W(n+1)` for the link factor `W`. For unitary `W`
this reads `W^*nW=n+1`, so `\max\mathrm{spec}(n)+1=\max\mathrm{spec}(n)`,
which is impossible. So no bounded observable is raised by a link
factor, and Lemma 5, Theorem 7 and Proposition 9 do not transfer as
proved. The law-independent results still apply there wherever their
hypotheses are verified. No A3 obstruction for `L5-O[S_+]` follows from
this file, as stated here.


- RC-W requires its own finite Weyl-node and setting hypotheses. No node here triggers its mirror-pairing conclusion. A charged tick implementer and charged-sector zoom comparison remain separate obligations.

The four-test verdicts in §5 are pass-1 judgments, not adoption. The frozen results cited above retain their own provenance and verification limits. The literature search in `RCSPC_DRAFT.md` is context only; several listed references were not verified there, and no proof here depends on them.
