lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5O-E′ on `L5-O`, pass 1: exact `Spin(10)` invariance fixes no gluon count, and the lemma holds in heat-kernel model classes

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the open lemma `CH1-5O-E′` (`CH1_5OE_DRAFT.md` section 6.2; frozen `CH1_5OE.md` line 167), under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status. It adopts no law, reading, class or register. It changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation: `/tmp/toe-ch15oep/check2.py`, output `/tmp/toe-ch15oep/out2.txt`, 18.5 s, 690 MB peak, floating point and Monte Carlo, started after `memory_pressure` showed 61 percent free. A first, larger version (`check.py`, output `out.txt`) took 87.5 s and peaked at 835 MB. That run broke the one-minute limit, so its output is not cited. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), at the start of the run | `481fcd124` |
| same checkout, after its HEAD moved during the run (read only for `CH1_5OE.md`) | `1a6005d26` |
| working-tree file `CH1_5OE_REFEREE.md`, read before its commit `1be8b7478` by another Mini lane | none |
| same checkout, after its HEAD moved again (read only for the frozen `CH1_5OE.md` and `CH1.md` line 13) | `58586b850` |

No other branch was read.

Files read, by line. `AGENTS.md` lines 1-27. `docs/ai_methodology/SCIENCE_WORKFLOW.md` lines 1-293 (all). `docs/MINIMAL_AXIOMS_2026-06-29.md` lines 1-80. This folder, at `481fcd124`: `CH1_5OE_DRAFT.md` lines 1-246 (all; Theorem C at 102-107, Lemma B at 117-119, Lemma D at 153-163, the four-test table at 177-181, CH1-5O-E′ at 187-189, B1-B4 at 197-203); `CH1_5O.md` lines 1-188 (all; Definition 1 at 19, Theorem 11 at 104-106, R5 to R5.2 at 140-144, R8 at 157-159, the four tests at 164, CH1-5O-E at 175); `GA2_Y2.md` lines 1-169 (all; Definition 4 at 22, the T0-start request at 169); `LIT_HIGGS.md` lines 1-177 (all); `Y2W_DRAFT.md` lines 1-208 (all; T0-start's class at 54, Definition SC at 56, the four-test row at 76, option (a1) at 171-177); `CH1_5O_DRAFT.md` lines 1-60 (the update class at 53); `LW1_5.md` lines 1-140 and 140-352 in part (the law at 72-97, Q and G at 123-130, R at 132-134, B1-5 at 255-257); `VC1_5.md` lines 7, 20, 23, 35 and 39, found by `grep`; `LIT_QLM.md` lines 1-60 and 163-165. At `1a6005d26`: `CH1_5OE.md` lines 1-127 (all, pass 2). In the working tree: `CH1_5OE_REFEREE.md` lines 1-12 and 105-125, only for the corrected wording of CH1-5O-E′ (its edit E3). At `58586b850`: the frozen `CH1_5OE.md` lines 1-12, 31 and 165-182, and `CH1.md` line 13 (Amendment 4); section 0.2 records them. SHA-256 prefixes of the files read: `CH1_5OE_DRAFT.md` `2c2ff5dfaf0c3868`, `CH1_5OE.md` `5a5c94d11637ac93` (pass 2) and `70dbb28f246343dd` (frozen), `CH1.md` `633e4aa4eed86d1e`, `CH1_5O.md` `053f1ecf4da057b4`, `GA2_Y2.md` `25db8a18aff1d30f`, `Y2W_DRAFT.md` `f9d8db9c15b4b101`, `LW1_5.md` `7afb7ee2a52d91cd`, `VC1_5.md` `7461113c411eeda4`.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law, the update class, Definition SC and CH1-5O-E′ are read plainly. Where the text leaves a choice open, the choice is named and put through the four tests (section 7). Nothing is adopted.

**Working set used, by name.** PS-5, PS-6 and PS-6r, only through the law `L5-O` of `LW1_5.md` section 2 (line 80) and its free datum `R`. PS-1c, only through the cell lifts. LW1's conjugation reading of gauge invariance (`LW1_5.md` line 35: "Gauge invariance means invariance under conjugation, not necessarily a zero Gauss-charge sector"). PS-7r, only through its sentence "the vacuum is the state VC1 builds" (section 8). PS-2, PS-3, PS-4 and PS-8 to PS-11 are not used. Results used, each quoted or re-derived at the point of use: from `LW1_5.md`, the law, "Q and G" and B1-5; from `VC1_5.md`, Theorem 2.1 and the cell group; from `CH1_5O.md`, Definition 1, Theorem 11, R5, R5.2 and R8; from `CH1_5OE_DRAFT.md`, the statement of CH1-5O-E′, Lemma B and Lemma D (context); from `Y2W_DRAFT.md`, Definition SC; from `GA2_Y2.md`, Definition 4 and the T0-start request.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the Fock space of ten fermion modes built from twenty Majoranas; joint eigenspaces of commuting involutions; an irreducibility argument through one top eigenvector (Lemma K(iv)); Cauchy-Schwarz; expansion of a product of sums; the bounds `1 − a + a²/2 − a³/6 ≤ e^{−a} ≤ 1 − a + a²/2` for `a ≥ 0`; completeness relations for orthonormal bases of `so(10)` and `u(5)`; Casimir operators on tensor squares; the mean value theorem; the spin lift `cos(θ/2) + sin(θ/2)η_cη_d` of a plane rotation and the reflection identity `vwv = −r_v(w)` for a unit Clifford vector `v`. Standard mathematics cited, not rebuilt: the heat-kernel probability measure `p_t` on a compact connected Lie group, with `∫ρ(u)dp_t(u) = exp(−tC_ρ/2)` for every finite-dimensional unitary representation `ρ`; the Peter-Weyl theorem (a probability measure on a compact group is determined by these integrals); Haar measure on compact groups and their products; product states and the unique tracial state of a UHF algebra; local sections of a covering map. Literature context, credited from memory or from the search below, never load-bearing: coherent states of compact groups and their classical limits (Perelomov; Lieb, Commun. Math. Phys. 31 (1973) 327-340; Simon's extension to compact-group spins); `SO(N)` quantum links from `so(2N)` rishons (Brower, Chandrasekharan, Riederer and Wiese, mapped in `LIT_QLM.md` section 5); large-representation quantum links (Schlittgen and Wiese; Bär, Brower, Schlittgen and Wiese; `LIT_QLM.md` sections 3-4); lattice heat-kernel Yang-Mills in two dimensions (Migdal; Driver; Sengupta; Lévy); heating of generic periodically driven many-body systems to infinite temperature (D'Alessio and Rigol; Lazarides, Das and Moessner), used only to place attack C4.

**Literature search (this lane, time-boxed).** Three standard web searches on 2026-11-06. (1) Quantum links in large representations, coherent states, classical limit: it found Bär-Brower-Schlittgen-Wiese (hep-lat/0110148, already in `LIT_QLM.md`). It found no quantitative error bound for loop data of coherent product states on `SO(20)` links. (2) Lieb's classical limit: Lieb (1973), the Berezin-Lieb inequalities and Simon's extension. These bound free energies, not loop moments. (3) Heat-kernel Wilson loops: Driver's YM2 expectations, Lévy (arXiv:1601.06283) and arXiv:2305.02306. They supply context for the model classes of section 5. No `SU(5)` against `Spin(10)` moment comparison was found. The closest repo record is `LIT_QLM.md` line 165, rebuild candidate 3: "SO(20) normalization, coherent symbols, and quantitative errors for one specified large highest-weight family". Lemma K and Theorem U below are an instance of it, for loop data.

---

## 0. The question, quoted

`CH1_5OE_DRAFT.md` line 187: "**Lemma CH1-5O-E′ (open; CH1-5O-E in reading R-E′).** There exist an `L5-O` update, a stationary, gauge-invariant, cell-symmetric state `ω`, a Case I embedding with `α` even and group `H`, a closed `G_∞` with `H ⊆ G_∞ ⊊ Spin(10)`, and pinned data in the form of Definition SC — a block scale `r`, a fixed finite list `Λ_r` of gauge-invariant block-loop observables that contains the vector-representation block plaquettes, the standard identification (each loop observable mapped to its trace formula on `G`-valued links of `rZ^4`, for `G = G_∞` and for `G = Spin(10)`), the classes of section 6.1 with coupling bound `g_*`, and `δ` — such that:" Lines 188-189: "(a′) some `μ` in the `G_∞` class satisfies `|ω(O) − E_μ(O)| ≤ δ` for every product `O` of at most two observables of `Λ_r` and their adjoints; (b′) no `μ'` in T0-start's `Spin(10)` class meets the bounds of (a′)."

`CH1_5OE.md` line 112 (pass 2; line 167 of the frozen file) fixes the data first: "For fixed `r`, `Λ_r`, standard maps, nonempty precisely defined pure-gauge small-field classes and `δ`, ask for an `L5-O` update and a stationary, cell-symmetric gauge-invariant state, Case I `H` with even `a`, and candidate `K`, such that ..." The working-tree referee file, edit E3, corrects the end to: "such that (a′) some `K`-class measure meets the bounds of (a), and (b′) no `G`-class measure meets those bounds." Theorem W below treats both orders of quantifiers.

`CH1_5O_DRAFT.md` line 53 defines the updates: "An *`L5-O` update* is the tick of `L5-O[R]` (`LW1_5_DRAFT.md` section 8.1) with `R` an irreducible register of `𝔨 = so(20)` (for example `S_+`), followed or preceded by finitely many layers of gauge-invariant gates. A gauge-invariant gate is a local unitary that commutes with every local gauge unitary below." Frozen `CH1_5O.md` line 19 keeps the class: "An `L5-O` update has irreducible `so(20)` registers and may include finitely many gauge-invariant gate layers."

`CH1_5OE.md` line 23 (pass 2; line 31 of the frozen file) leaves one door open: "The theorem does **not** prove that exactness can never imply a restriction on invariant correlations: a property could hold for every stationary state of `A^G`."

`Y2W_DRAFT.md` line 76, the four-test row of Definition SC, test (3): "pass only with `ω` the state VC1 supplies. 'There is a state' would choose the vacuum by premise and fail".

**The lane's target.** Prove or refute CH1-5O-E′. The lead named two outcomes in advance. A proof that every exactly `Spin(10)`-invariant state matches the 45-gluon class at least as well as any `K`-class would give a named failing step of `L5-O`'s route to a smaller effective group. A state that matches a `K`-class better keeps `L5-O` alive. The attacks must differ from B1-B4 (`CH1_5OE_DRAFT.md` section 6.3) and from A1-A4 (`CH1_5O.md` section 5).

## 0.1 Outcome in one paragraph

**CH1-5O-E′ holds when heat-kernel model classes stand in for T0-start's, and it carries no information about `L5-O`.** Four closures do the work. *Lemma K and Theorem U (kinematic universality).* Let `R_k^−` be the irreducible register spanned by the `Spin(20)`-orbit of `φ_0^{⊗k}`, where `φ_0` is the `+1` joint eigenvector of the ten diagonal link operators `U^{aa}` in `S_−`. This is a value of the free datum `R`. Gauge averages of mixtures of coherent product states on `R_k^−` reproduce the loop data of every probability measure `ν` on `SO(10)`-valued link configurations. For loops of at most `N` links the error is at most `3[(1 + 3/√k)^N − 1]` on products of two loops. Every fixed polynomial in loops converges as `k → ∞`. The state is cell symmetric when `ν` is. So exact `Spin(10)` gauge invariance and the link kinematics constrain no loop data, and in particular no gluon count. An exactly invariant state has the count of the configuration law it is built from. *Lemma I (inverse layers).* The tick of `L5-O[R]`, followed by the inverses of its own layers, is an `L5-O` update in the sense of `CH1_5O_DRAFT.md` line 53, and it is the identity. Every state is stationary for it. *Lemma HK (exact separation).* For heat-kernel laws, the vector plaquette `w` has `E w² = G(E w)` on `SU(5)` and `E w² = F(E w)` on `Spin(10)`, with explicit sums of powers. `G(e^{−s}) − F(e^{−s}) ≥ (s²/21600)(840 − 31775s) > 0` for `0 < s < 840/31775`. *Theorem W.* Take the random-link model classes: gauge-averaged independent heat-kernel links, for `SU(5)` and for `Spin(10)`. Take the standard Case I group `H` with `(α, β) = (2, −3)`, `G_∞ = SU(5)`, any block scale, any finite list of skeleton loops that contains a block plaquette, and `δ = 10^{−6}`, with time bound `σ_* ≥ 1/576`. Then CH1-5O-E′ holds. The update is the tick with its inverse layers on `L5-O[R_k^−]`. The state is the gauge-averaged coherent mixture of independent `SU(5)` heat-kernel link values. It is stationary, gauge invariant and cell symmetric. For any pinned classes, CH1-5O-E′ follows from a separation statement about the two classes alone (SEP), once the separating `K`-measure is realized by a cell-symmetric configuration law. **Counterexample.** The kill "every exactly `Spin(10)`-invariant state matches the 45-gluon class at least as well as any `K`-class" is false in the model classes. For any classes it would put every `K`-class measure in the closure of the `Spin(10)` class's data, a statement with no `L5-O` content (Corollary G). **The form with content** is the VC1 form of `Y2W_DRAFT.md` line 76: the state VC1 supplies, under the law's own tick. Four kill attacks on it differ from A1-A4 and B1-B4. C1 (count correlation channels), C2 (twisted box) and C3 (Ward identities) fail at named kinematic steps, refuted by Theorem U and the state of Theorem W. C4 (Floquet heating) stops at an open hypothesis, HEAT. Proposition Z shows what HEAT would give: every Gauss-sector-tracial state has zero vector loops. **No named failing step for `L5-O`.**

## 0.2 The frozen restatement

While this lane ran, the checkout's HEAD moved to `58586b850`, which freezes `CH1_5OE.md` (CH1 Amendment 4). Frozen line 167: "**CH1-5O-E′ (proposed, open).** For fixed `r`, `Λ_r`, standard maps, nonempty precisely defined pure-gauge small-field classes and `δ`, ask for an `L5-O` update and a stationary, cell-symmetric gauge-invariant state, Case I `H` with even `a`, and candidate `K`, such that (a′) some `K`-class measure meets the bounds of (a), and (b′) no `G`-class measure meets those bounds. This is an existence version. Even a proof would not identify the state supplied by VC1." `CH1.md` line 13 (Amendment 4): "CH1-5O-E and its pure-gauge form CH1-5O-E' stay open." Frozen line 5 keeps the GAP: "the proposed R-E′ has classes that are not pinned; the Gaussian calculation does not establish their separation."

The analysis below was written against the wording of section 0, and it applies to the frozen statement unchanged. Frozen line 167 is the pass-2 statement with the referee's edit E3, as quoted in section 0. Theorem W(ii) pins the "precisely defined pure-gauge small-field classes" by model classes, and Lemma HK proves their separation. With T0-start's classes the lemma reduces to SEP[T0-start] (Theorem W(i)). Frozen line 167 already says that a proof "would not identify the state supplied by VC1"; section 8 states that VC1 form as its own open lemma. Frozen line 165 adds that "whether pure gauge is admissible in frozen CH1-5O-E turns on the `W = 0` reading". Nothing here depends on that reading, since the results concern CH1-5O-E′ as stated.

---

## 1. Setting

### 1.1 Links, loops and gauge maps

On a link `ℓ = (x, y)`, with source `x` and target `y`, write `η^y_a` and `η^x_b` (`a, b = 1, …, 10`) for the two sets of Clifford generators. Then `U^{ab}_ℓ = 2T_{a,10+b} = iη^y_aη^x_b` (`LW1_5.md` line 80). The row index `a` belongs to the target and the column index `b` to the source. `LW1_5.md` line 85 reads: "`L^{cd}_{ℓ,z}=L^{cd}_x` if `z` is the source of `ℓ`, and `L^{cd}_y` if it is the target". Line 123 gives `L_y^{cd} = T_{cd}` and `L_x^{cd} = T_{10+c,10+d}`, with

\[
[L_x^{cd},U^{ab}]=i(δ_{db}U^{ac}−δ_{cb}U^{ad}),\qquad [L_y^{cd},U^{ab}]=i(δ_{da}U^{cb}−δ_{ca}U^{db}).
\]

Put `𝐔_ℓ = Σ_{ab}E_{ab} ⊗ U^{ab}_ℓ`, an operator on `C^{10} ⊗ R_ℓ`. The target group rotates the row index and the source group rotates the column index, through the covering map `R: Spin(10) → SO(10)`. The same brackets act on `γ_{y,a}` and `γ_{x,b}`, and this makes the hop `h_ℓ = (i/2)Σ_{ab}γ_{y,a}U^{ab}γ_{x,b}` invariant. With the sign convention fixed this way, the gauge map of `g` at the target sends `𝐔_ℓ ↦ (R(g) ⊗ 1)𝐔_ℓ`, and at the source it sends `𝐔_ℓ ↦ 𝐔_ℓ(R(g)^T ⊗ 1)`. The opposite convention exchanges `R(g)` and `R(g)^T` throughout and changes nothing below. `LW1_5.md` line 33: "Links commute with matter and are ordinary tensor factors."

**Paths and loops.** A *closed path* `C` is a cyclic sequence of sites `x_0, x_1, …, x_n = x_0` with links `ℓ_1, …, ℓ_n`. The link `ℓ_i` joins `x_{i−1}` and `x_i`, and the `n` links are distinct. The factor `X_i` is `𝐔_{ℓ_i}` if `ℓ_i = (x_{i−1}, x_i)`, and `𝐔_{ℓ_i}^T` otherwise (transpose of the matrix indices only). The *vector loop* is `W_C = (1/10)tr(X_n ⋯ X_1)`. Entries on distinct links commute, so the product is unambiguous. `W_C` is Hermitian: the entries are Hermitian and commute across links, so each product of entries is its own adjoint. `W_C` is gauge invariant: a gauge map at `x_i` multiplies `X_i` on the left by `R(g)` and `X_{i+1}` on the right by `R(g)^T` (indices mod `n`), and these cancel inside the trace. This is the loop of `CH1_5O.md` Theorem 11, with one factor `U^{ab}_ℓ` on each of its links.

**Classical values.** A *configuration* is `u ∈ SO(10)^L`, with `L` the set of fine links. Its holonomy along `C` is `u_C = O_n ⋯ O_1`, with `O_i = u_{ℓ_i}` or `u_{ℓ_i}^T` by the same rule. Put `cl_u(C) = (1/10)tr u_C ∈ [−1, 1]`. A gauge map acts on configurations by the formulas above.

### 1.2 Comparison data

Fix a block scale `r = ma`, with `m = L^{k_0}` in ZM1's notation (`Y2W_DRAFT.md` line 56). A *block link* is the straight fine path of `m` fine links between neighbouring block sites. A *skeleton loop* is the fine path of a closed block path that uses each block link at most once. It is a closed path in the sense of 1.1. A finite list `Λ` of skeleton loops plays the role of Definition SC's list `Λ_r`. On a register with scale `k` (section 2) the listed observable is the normalized loop `Ŵ_C = (1/10)tr((X_n/k) ⋯ (X_1/k))`. The *standard identification* `ι` maps `Ŵ_C` to `w_{C_b}(U) = (1/10)tr R(U_{C_b})` on `G`-valued block links of `rZ^4`, for `G = G_∞ ⊆ Spin(10)` and for `G = Spin(10)`. Here `C_b` is the block path of `C`, read in one time slice. This is the identification of `CH1_5OE_DRAFT.md` line 187, normalisation included.

Let `P_2(Λ)` be the set of products of at most two observables of `Λ`, both orders included. Each `Ŵ_C` is Hermitian, so adjoints add nothing. For a state `ω` and a probability measure `μ` on block configurations, put

\[
d_Λ(ω,μ)=\max_{O∈P_2(Λ)}|ω(O)−E_μ(ιO)|,\qquad d_Λ(ω,\mathcal C)=\inf_{μ∈\mathcal C}d_Λ(ω,μ).
\]

Define `d_Λ(μ, μ')` between two measures in the same way. These are sup-distances between finite data vectors, so the triangle inequality holds. In this notation (a′) says `d_Λ(ω, μ) ≤ δ` for some `μ ∈ 𝒞(G_∞)`, and (b′) says `d_Λ(ω, μ') > δ` for every `μ' ∈ 𝒞(Spin(10))`.

### 1.3 Gauge average and cell lifts

`VC1_5.md` line 35, Theorem 2.1: "Averaging a local observable over the finitely many compact local gauge groups that act on it defines a positive unital contraction `E:A→A^{gauge}`. Local invariant observables are dense in `A^{gauge}`. Restriction gives an affine bijection from gauge-invariant states on `A` to states on `A^{gauge}`, with inverse `φ↦φ∘E`. The map `E` commutes with `α` and the cell lifts." Its proof uses four facts. Each local gauge group is compact. It acts by inner automorphisms of a finite tensor factor. Local groups at different sites commute. Each lift carries each local gauge group onto a local gauge group. These hold for every register `R`. Two consequences are used below. First, `E ∘ α^G_{x,g} = E` by invariance of Haar measure, so `φ ∘ E` is gauge invariant for every state `φ`. Second, `E(A) = A` for `A ∈ 𝔄^G`.

`VC1_5.md` line 20: "The cell group is `G = 2 Z^3 ⋊ O_c0`, with `c0=(1,1,1)/2` and `O` the 24 proper signed coordinate permutations." Call it `𝒢`. `LW1_5.md` line 257 (B1-5) describes the lifts of the `L5-O` law: "A geometric symmetry of the dressed Majorana law acts on a reversed link by exchanging the two sets of ten auxiliary Majoranas. This is an orientation-preserving transformation in 20 dimensions and lifts to Spin(20); it sends `U^{ab}` to `−U^{ba}`, while reversing the two matter Majoranas gives the other minus sign. Site parity implements LW1's sign lift." That argument uses only the Clifford relations and the spin lift of the end swap. With `τ_E = 0` it applies to every register `R`. So the lift `β_g` of `g ∈ 𝒢` acts on the matter by an automorphism of the CAR algebra. It moves the register of `ℓ` to that of `gℓ`, and it applies the end swap on each link whose orientation `g` reverses.

---

## 2. Coherent states on large registers

On one link, `S_±` are the two half-spin representations of `Spin(20)`. `LW1_5.md` line 134 fixes the labels: "On `S_+`, the product of the ten commuting `2T_{2j-1,2j}` is chirality `+1`".

**Lemma K (the registers `R_k^−` and their coherent states).**
(i) The ten `U^{aa}` commute and are involutions. On the full spinor space their joint eigenspaces are lines, and `∏_aU^{aa} = −∏_j 2T_{2j−1,2j}`. Hence the joint eigenvector `φ_0` with all `U^{aa} = +1` lies in `S_−`. In `S_−` it spans the eigenspace of `Σ_aU^{aa}` for the eigenvalue `10`.
(ii) `⟨φ_0, U^{ab}φ_0⟩ = δ_{ab}`. For every `v ∈ C^{10}`, `‖(𝐔 − 1)(v ⊗ φ_0)‖ = ‖(𝐔^T − 1)(v ⊗ φ_0)‖ = 3‖v‖`. On `C^{10} ⊗ S_−`, `‖𝐔‖ = 10`.
(iii) Every diagonal generator `L_y^{cd} + L_x^{cd}` annihilates `φ_0`. So `ρ(g_y)ρ(g_x)φ_0 = φ_0`, where `g_y` and `g_x` are one element of `Spin(10)` placed at the two ends.
(iv) For `k ≥ 1`, `R_k^− := span{ρ^{⊗k}(h)φ_0^{⊗k} : h ∈ Spin(20)} ⊆ S_−^{⊗k}` is irreducible. On it the link operators are `U^{ab} = Σ_{i=1}^kU^{ab}_{(i)}`, and `‖𝐔/k‖ ≤ 10`.
(v) For `O ∈ SO(10)` there is `h` in the target-end group with `ρ_k(h)^{−1}𝐔ρ_k(h) = (O ⊗ 1)𝐔`. The ray of `ψ_O := ρ_k(h)φ_0^{⊗k}` depends on `O` only, and `O ↦ |ψ_O⟩⟨ψ_O|` is continuous. Moreover `⟨ψ_O, 𝐔ψ_O⟩ = kO`, and for every `v ∈ C^{10}`

\[
\|(\mathbf U/k−O⊗1)(v⊗ψ_O)\|=\|((\mathbf U/k)^T−O^T⊗1)(v⊗ψ_O)\|=3\|v\|/\sqrt k .
\]

(vi) A gauge map of `g` at the target end sends the ray of `ψ_O` to that of `ψ_{R(g)O}`. At the source end it sends it to that of `ψ_{OR(g)^T}`. For the central element `ϖ`, at either end, the image is `ψ_{−O}`. The end swap `s̃` sends each `U^{ab}` to `−U^{ba}`, and the ray of `ψ_O` to that of `ψ_{−O^T}`.

*Proof.* (i) Put `d_a = (η^y_a + iη^x_a)/2`. The Clifford relations give `{d_a, d_b^†} = δ_{ab}` and `{d_a, d_b} = 0`, and `d_a^†d_a = (1 + iη^y_aη^x_a)/2`. So `U^{aa} = 2d_a^†d_a − 1`. The spinor space `C^{1024}` is an irreducible module of the twenty generators, hence of the CAR algebra of the ten modes `d_a`. So it is their Fock space, and the joint eigenspaces of the ten number operators are lines. Next, `∏_a iη_aη_{10+a}` and `∏_j iη_{2j−1}η_{2j}` both equal `±i^{10}η_1η_2⋯η_{20}`. Reordering `(1, 11, 2, 12, …, 10, 20)` into increasing order takes `9 + 8 + ⋯ + 1 = 45` transpositions, an odd number. So the first product is minus the second. On `φ_0` the first product is `+1`. So the second is `−1`, and `φ_0 ∈ S_−` by the quoted label. On `S_−`, `Σ_aU^{aa} ≤ 10`, with equality exactly on the line of `φ_0`. [check] (1b), (1d).

(ii) For `a ≠ b`, `U^{ab}` anticommutes with `U^{bb}`: moving `iη^y_bη^x_b` past `η^y_a` gives the sign `(−1)^2`, and past `η^x_b` the sign `−1`. So `⟨φ_0, U^{ab}φ_0⟩ = ⟨φ_0, U^{ab}U^{bb}φ_0⟩ = −⟨U^{bb}φ_0, U^{ab}φ_0⟩ = −⟨φ_0, U^{ab}φ_0⟩ = 0`. Then `(𝐔 − 1)(v ⊗ φ_0) = Σ_ae_a ⊗ Σ_{b≠a}v_bU^{ab}φ_0`. Its squared norm is `Σ_aΣ_{b,b'≠a}v̄_bv_{b'}⟨φ_0, U^{ab}U^{ab'}φ_0⟩`. For `b = b'` the operator is `(U^{ab})^2 = 1`. For `b ≠ b'` it is `U^{ab}U^{ab'} = η^x_bη^x_{b'}`, which anticommutes with `U^{bb}`, so its expectation is `0`. The squared norm is `Σ_aΣ_{b≠a}|v_b|^2 = 9‖v‖^2`. For `𝐔^T` the same steps use `U^{ba}U^{b'a} = η^y_bη^y_{b'}`. Finally, `𝐔^*𝐔` has entries `Σ_cU^{ca}U^{cb} = 10η^x_aη^x_b`, with diagonal entries `10`. So `𝐔^*𝐔 = 10ΓΓ^*` with `Γψ = Σ_ae_a ⊗ η^x_aψ`, and `Γ^*Γ = 10`. The eigenvalues of `𝐔^*𝐔` are `0` and `100`, so `‖𝐔‖ = 10`. [check] (1d).

(iii) From `iη^y_cη^x_cφ_0 = φ_0`, multiplication by `−iη^y_c` gives `η^x_cφ_0 = −iη^y_cφ_0`. For `c ≠ d`, `η^x_cη^x_dφ_0 = −iη^x_cη^y_dφ_0 = iη^y_dη^x_cφ_0 = η^y_dη^y_cφ_0 = −η^y_cη^y_dφ_0`. So `(T_{cd} + T_{10+c,10+d})φ_0 = (i/2)(η^y_cη^y_d + η^x_cη^x_d)φ_0 = 0`. The diagonal copy of `Spin(10)` is generated by the exponentials of these generators, so it fixes `φ_0`. [check] (1e).

(iv) `R_k^−` is a `Spin(20)`-invariant subspace of `S_−^{⊗k}`, so the Lie algebra acts on it by `Σ_i dρ_{(i)}`. This gives the formula for `U^{ab}`. `N := Σ_aU^{aa} = Σ_iN_{(i)}` is a sum of commuting operators. Each is at most `10`, with equality only on `φ_0` in its copy (part (i)). So `N ≤ 10k` on `S_−^{⊗k}`, and the eigenspace for `10k` is the line of `φ_0^{⊗k}`. Suppose `R_k^− = V_1 ⊕ V_2` with orthogonal invariant summands. Their projections commute with `N`. Write `φ_0^{⊗k} = v_1 + v_2` with `v_i ∈ V_i`. Then `Nv_i = 10kv_i`, so each `v_i` lies on the line of `φ_0^{⊗k}`. The two are orthogonal, so one is zero, say `v_2`. Then `φ_0^{⊗k} ∈ V_1`, so `V_1` contains the whole orbit span, and `V_2 = 0`. Finally `‖𝐔/k‖ ≤ (1/k)Σ_i‖𝐔_{(i)}‖ = 10` by (ii).

(v) The target-end group acts on the row index through `R`, which maps onto `SO(10)`. This gives `h`. Two choices of `h` differ by the kernel `{±1}`. The element `−1` of the end group is a rotation by `2π` in a plane, so it is `−1 ∈ Spin(20)`, and it acts on `S_−^{⊗k}` as `(−1)^k`. So the ray depends on `O` only. Local continuous sections of the covering map give continuity. Since `⟨φ_0^{⊗k}, U^{cb}φ_0^{⊗k}⟩ = kδ_{cb}`, we get `⟨ψ_O, U^{ab}ψ_O⟩ = Σ_cO_{ac}kδ_{cb} = kO_{ab}`. For the norm identity take first `O = 1`. Write `(𝐔/k − 1)(v ⊗ φ_0^{⊗k}) = (1/k)Σ_iξ_i`, where `ξ_i = Σ_ae_a ⊗ Σ_bv_b(U^{ab} − δ_{ab})_{(i)}φ_0^{⊗k}` uses copy `i` only. For `i ≠ j` the inner product `⟨ξ_i, ξ_j⟩` factorizes over copies and contains the factor `⟨φ_0, (U^{ab} − δ_{ab})φ_0⟩ = 0`, so it vanishes. Each `‖ξ_i‖ = 3‖v‖` by (ii). So the norm is `(1/k)√k · 3‖v‖ = 3‖v‖/√k`. For general `O`, conjugation gives

\[
(\mathbf U/k−O⊗1)(v⊗ρ_k(h)φ_0^{⊗k})=(O⊗ρ_k(h))(\mathbf U/k−1)(v⊗φ_0^{⊗k}),
\]

and `O ⊗ ρ_k(h)` is unitary. For the transpose, `ρ_k(h)^{−1}𝐔^Tρ_k(h) = 𝐔^T(O^T ⊗ 1)`; this step uses that `O ⊗ 1` has scalar entries. So `((𝐔/k)^T − O^T ⊗ 1)(v ⊗ ψ_O) = (1 ⊗ ρ_k(h))((𝐔/k)^T − 1)(O^Tv ⊗ φ_0^{⊗k})`, of norm `3‖O^Tv‖/√k = 3‖v‖/√k`. [check] (1g), for `k = 2`.

(vi) At the target end, `ρ_k(g)ψ_O = ρ_k(gh)φ_0^{⊗k}` and `ρ_k(gh)^{−1}𝐔ρ_k(gh) = (R(g)O ⊗ 1)𝐔`. At the source end, the source element commutes with `h`. By (iii) it acts on `φ_0^{⊗k}` as the inverse element placed at the target. So the image is again a target rotation of `φ_0^{⊗k}`, that is, a coherent ray. Its classical value is read off from `⟨𝐔⟩`: the source map sends `𝐔` to `𝐔(R(g)^T ⊗ 1)`, so the value is `OR(g)^T`. For `ϖ`, `R(ϖ) = −1`. The end swap is `s̃ = ∏_{a=1}^{10}(η^y_a − η^x_a)/√2`. Each factor is a unit Clifford vector `v_a`, and `v_awv_a = −r_{v_a}(w)`, where `r_{v_a}` is the reflection in the hyperplane orthogonal to `(e_a − e_{10+a})/√2`; it exchanges `e_a` and `e_{10+a}`. The ten signs cancel, so conjugation by `s̃` exchanges `η^y_a` and `η^x_a` for every `a`. `s̃` is a product of an even number of unit vectors, so `s̃ ∈ Spin(20)`. It sends `U^{ab} = iη^y_aη^x_b` to `iη^x_aη^y_b = −U^{ba}`. It maps `S_−` and `R_k^−` to themselves, and `ρ_k(s̃) = s̃^{⊗k}` there. Next, `s̃φ_0` is the joint eigenvector with all `U^{aa} = −1`, and so is `ρ(ϖ_y)φ_0`. The joint eigenspace is a line, so the two agree up to a phase. Hence `ρ_k(s̃)ψ_O = ρ_k(s̃hs̃^{−1})ρ_k(s̃)φ_0^{⊗k}` is a source rotation of a target rotation of `φ_0^{⊗k}`, that is, a coherent ray. Its value is `⟨𝐔⟩ = −kO^T`, by `s̃^{−1}U^{ab}s̃ = −U^{ba}` (`s̃^2 = ±1`). [check] (1f). ∎

The lemma is the part of `LIT_QLM.md`'s rebuild candidate 3 that the loop comparison needs. The coherent states are the standard ones of a compact group (Perelomov; Lieb; credited). The one quantitative input is the exact identity of (v): one link deviates from its classical value by `3/√k` in operator norm on its coherent vector. For `k = 1` this gives nothing: the half-spin registers are far from classical, as `Y2W_DRAFT.md` Theorem W2(iii) records ("`κ ≤ 1/10` for every state").

---

## 3. Kinematic universality

Let `τ` be the tracial state of the matter CAR algebra. It is the unique tracial state of that UHF algebra, so every automorphism preserves it. For a configuration `u`, let `Φ_u` be the product state of the link algebra whose restriction to each finite set of links is the vector state of `⊗_ℓψ_{u_ℓ}`. For a Borel probability measure `ν` on `SO(10)^L`, put `ω_ν(A) = ∫Φ_u(A)dν(u)` for local `A`. The integrand depends continuously on finitely many coordinates (Lemma K(v)), and `|Φ_u(A)| ≤ ‖A‖`. So `ω_ν` extends to a state of the link algebra.

**Theorem U (kinematic universality).** Put the register `R_k^−` on every link, take any constants, and let

\[
ω=(τ⊗ω_ν)∘E .
\]

(i) `ω` is a gauge-invariant state, and `ω(A) = (τ ⊗ ω_ν)(A)` for `A ∈ 𝔄^G`.
(ii) Let `C, C'` be closed paths of at most `N` links each, and `ε := (1 + 3/√k)^N − 1 ≤ 1`. Then `|ω(Ŵ_C) − E_ν[cl(C)]| ≤ ε` and `|ω(Ŵ_CŴ_{C'}) − E_ν[cl(C)cl(C')]| ≤ 3ε`.
(iii) For closed paths `C_1, …, C_q` of at most `N` links each, `|ω(Ŵ_{C_1}⋯Ŵ_{C_q}) − E_ν[∏_jcl(C_j)]| ≤ q·10^{N(q−1)}ε`.
(iv) Suppose `ν` is invariant under the geometric action of `𝒢`: each `g` moves the value of a link to the link `g` maps it to, transposed when `g` reverses the link. Then `ω` is cell symmetric.

*Proof.* (i) `E ∘ α^G_{x,g} = E`, and `E(A) = A` on `𝔄^G` (section 1.3).

(ii) Fix `u`. Work in the finite tensor product of the registers of the links of `C`, where `Φ_u` is the vector state of `Φ := ⊗_ℓψ_{u_ℓ}`. Write `X̂_i := X_i/k = O_i ⊗ 1 + Δ_i`, with `O_i` the classical factor. Let `J_i` be the isometry `C → R_{ℓ_i}`, `1 ↦ ψ_{u_{ℓ_i}}`. Lemma K(v) says that `Δ_i(1 ⊗ J_i)`, a map from `C^{10}`, has norm `3/√k`. Hence `‖Δ_iΨ‖ ≤ (3/√k)‖Ψ‖` for every vector `Ψ` whose factor on `R_{ℓ_i}` is `ψ_{u_{ℓ_i}}`: such a `Ψ` is `(1 ⊗ J_i ⊗ 1)Ψ'` with `‖Ψ'‖ = ‖Ψ‖`. Expand `X̂_n ⋯ X̂_1 = Σ_{S ⊆ {1,…,n}}Π_S`, where `Π_S` takes `Δ_i` for `i ∈ S` and `O_i ⊗ 1` otherwise, in order. Apply `Π_S` to `v ⊗ Φ`, factor `1` first. When factor `i` acts, no earlier factor has touched `R_{ℓ_i}`, because the links are distinct. So each `Δ_i` costs at most `3/√k`, and each `O_i ⊗ 1` costs `1`. Hence `‖Π_S(v ⊗ Φ)‖ ≤ (3/√k)^{|S|}‖v‖`, and `Π_∅(v ⊗ Φ) = (u_Cv) ⊗ Φ`. Summing over `S ≠ ∅`,

\[
\|\hat X_n\cdots\hat X_1(v⊗Φ)−(u_Cv)⊗Φ\|\le\big((1+3/\sqrt k)^n−1\big)\|v\|.
\]

Since `Ŵ_CΦ = (1/10)Σ_a(e_a^* ⊗ 1)X̂_n⋯X̂_1(e_a ⊗ Φ)`, this gives `‖Ŵ_CΦ − cl_u(C)Φ‖ ≤ ε`. Write `Ŵ_CΦ = cΦ + e` and `Ŵ_{C'}Φ = c'Φ + e'`, with `c, c'` real in `[−1, 1]` and `‖e‖, ‖e'‖ ≤ ε`. Then `|Φ_u(Ŵ_C) − c| = |⟨Φ, e⟩| ≤ ε`. Since `Ŵ_C` is Hermitian, `Φ_u(Ŵ_CŴ_{C'}) = ⟨cΦ + e, c'Φ + e'⟩`, which differs from `cc'` by at most `ε + ε + ε^2 ≤ 3ε`. Integrate over `ν` and use (i): `Ŵ_C` and `Ŵ_CŴ_{C'}` lie in `𝔄^G` and act on links only.

(iii) By Lemma K(iv), `‖X̂_i‖ ≤ 10`, so `‖Ŵ_{C_j}‖ ≤ 10^N`. Telescope: `Ŵ_{C_1}⋯Ŵ_{C_q}Φ − c_1⋯c_qΦ = Σ_jŴ_{C_1}⋯Ŵ_{C_{j−1}}(Ŵ_{C_j} − c_j)c_{j+1}⋯c_qΦ`. The `j`-th term has norm at most `10^{N(j−1)}ε`. Take the inner product with `Φ` and integrate.

(iv) Fix `g ∈ 𝒢`, with linear part `Qe_j = ε_je_{π(j)}`. By section 1.3 and Lemma K(vi), `(τ ⊗ Φ_u) ∘ β_g = τ ⊗ Φ_{u'}`. Here `u'` is obtained from `u` by moving each value between the links that `g` relates, and replacing it by `−u_ℓ^T` when `g` reverses the link. The reversed image links are exactly the links in the directions `i ∈ J := {π(j) : ε_j = −1}`. So `u' = s·u''`, where `u''` is the geometric image (transposed, without sign), and `s_ℓ = −1` on the links in the directions of `J` and `+1` on the others. Put `σ_x = (−1)^{Σ_{i∈J}x_i}`. Then `s_ℓ = σ_xσ_y` for `ℓ = (x, y)`. Let `γ` be the product of the local gauge maps of `ϖ` at the sites with `σ_x = −1`. These commute, so `γ` is an automorphism. By Lemma K(vi), `γ` multiplies the value of a link by `−1` at each end that lies at such a site. So `Φ_{u''} ∘ γ = Φ_{s·u''} = Φ_{u'}`. On the matter `γ` acts by an automorphism, which preserves `τ`. For `A ∈ 𝔄^G`, `γ(A) = A`, so `(τ ⊗ Φ_{u'})(A) = (τ ⊗ Φ_{u''})(γ(A)) = (τ ⊗ Φ_{u''})(A)`. Integrating, `(τ ⊗ ω_ν)(β_g(A)) = ∫(τ ⊗ Φ_{u''})(A)dν(u) = (τ ⊗ ω_ν)(A)`. The last step is the invariance of `ν` under `u ↦ u''`. Finally `E` commutes with `β_g` (section 1.3), so `ω ∘ β_g = (τ ⊗ ω_ν) ∘ β_g ∘ E = ω`. ∎

**What Theorem U says.** On the registers `R_k^−`, the data of exactly `Spin(10)`-invariant states on any finite list of loops (each link used at most once) fill out the data of all probability measures on `SO(10)`-valued configurations, up to errors that vanish as `k → ∞`. Every polynomial in finitely many loops is included. Cell symmetry costs only the cell invariance of `ν`. This answers, for loop data, the possibility left open in frozen `CH1_5OE.md` line 31. No property of finite loop data is forced by exactness on these registers beyond what the configuration laws already have. In particular, a configuration law with values in a subgroup `K` gives an exactly invariant state with `K`'s gauge-invariant loop statistics. The gauge average rotates each `K`-configuration over the whole group, as in `CH1_5OE_DRAFT.md` Theorem C, and changes no gauge-invariant quantity.

**Two realizations used below.**
- *Subdivision.* Given a measure `μ` on block configurations, take its configuration in one time slice and map each value by `R`. Place the value of each block link on the first fine link of its path, and `1` on every other fine link. Call the resulting law `ν_μ`. The fine holonomy of a skeleton loop is then the block holonomy, so `E_{ν_μ}[∏_jcl(C_j)] = E_μ[∏_jιŴ_{C_j}]`. `ν_μ` is not cell invariant.
- *Independent links.* If the fine links are independent with a common law `λ` on `SO(10)` invariant under `O ↦ O^T`, then `ν = λ^{⊗L}` is invariant under the geometric action of `𝒢`. The values along a closed path of `n` links are then independent with law `λ`, in either orientation.

---

## 4. The inverse layers

`LW1_5.md` lines 75-78: "`M_e=\prod_{C\in\mathcal T_e}e^{-ia_eH_C},\quad M_o=\prod_{C\in\mathcal T_o}e^{ia_oH_C},\quad U_0=W_EM_oM_e.` Cube gates in a layer have disjoint matter and links." Line 95: "the electric class has independent free `τ_E`, including zero". Line 128: "Every hop and cube gate commutes with every `𝒢_x^{cd}`." Line 130: "The specified electric operator commutes with both end algebras."

**Lemma I (the inverse layers make every state stationary).** Fix an irreducible register `R` and the constants, with `τ_E = 0` unless `R = S_+`. Consider the layers

\[
W_E^{-1}=\prod_\ell e^{i\tau_E\Gamma^x_\ell},\qquad M_o^{-1}=\prod_{C\in\mathcal T_o}e^{-ia_oH_C},\qquad M_e^{-1}=\prod_{C\in\mathcal T_e}e^{ia_eH_C}.
\]

(i) Each is a layer of gauge-invariant gates in the sense of `CH1_5O_DRAFT.md` line 53. Each is preserved by every cell lift that preserves the corresponding layer of `U_0`.
(ii) The tick `U_0` followed by `W_E^{−1}`, then `M_o^{−1}`, then `M_e^{−1}`, is an `L5-O` update, and its automorphism is the identity.
(iii) Every state is stationary for this update.

*Proof.* (i) A gate `e^{±ia H_C}` is a local unitary. `H_C` commutes with every Gauss generator (line 128), and the local gauge unitaries are generated by the exponentials of the Gauss generators. So the gate commutes with every local gauge unitary. The same holds for `e^{iτ_EΓ^x_ℓ}` by line 130. The gates of one layer have the disjoint supports of the corresponding layer of `U_0` (line 78). A lift that maps a layer onto itself conjugates each gate to a gate of the same layer, and it does the same for the inverse gates. (ii) Each layer is a product of commuting gates with disjoint supports, and it defines an automorphism, as in LW1 E1 (line 78: "Infinite products mean local automorphisms as in LW1 E1"). Gate by gate, the automorphism of an inverse layer is the inverse of the automorphism of the corresponding layer of `U_0`. So the three inverse layers, in the order given, compose to the inverse of the tick, `M_e^{−1}M_o^{−1}W_E^{−1} = U_0^{−1}`, and the update is the identity automorphism. The tick of `L5-O[R]` followed by finitely many layers of gauge-invariant gates is an `L5-O` update by line 53. (iii) `ω ∘ id = ω`. ∎

So, in the update class on file, "stationary for some update" is no condition on a state. The class does not restrict the angles of added gates, and the tick's own layers with negated angles undo it.

---

## 5. Heat-kernel model classes and an exact separation

### 5.1 The model

For a compact connected Lie group `G` with an `Ad`-invariant inner product on its Lie algebra, let `p^G_t` (`t > 0`) be the heat-kernel probability measure (cited). It satisfies `∫ρ(u)dp^G_t(u) = exp(−tC_ρ/2)` for every finite-dimensional unitary representation `ρ`, with `C_ρ = −Σ_Adρ(T_A)^2` over an orthonormal basis. Peter-Weyl (cited) gives two properties from this formula alone. `p_t` is invariant under `u ↦ u^{−1}`, because `∫ρ(u^{−1})dp_t = (e^{−tC_ρ/2})^* = e^{−tC_ρ/2}`. And `p_s * p_t = p_{s+t}`, because the integrals multiply. So a product of `n` independent `p_s`-distributed elements, each possibly inverted, has law `p_{ns}`.

Use `⟨X, Y⟩ = −(1/2)tr_{10}(XY)` on `so(10)` (`CH1_5OE_DRAFT.md` line 56) and its restriction to subalgebras. Let `SU(5)~` be the connected subgroup of `Spin(10)` with Lie algebra `su(5) ⊂ u(5) ⊂ so(10)`, for the standard complex structure on `R^{10} = C^5`. `R` maps it onto `SU(5)`, which is simply connected, so `R` is an isomorphism on it.

**The random-link classes `RL(G; σ_*)`.** For `G ∈ {SU(5)~, Spin(10)}` and `σ_* > 0`, `RL(G; σ_*)` is the set of gauge averages, over `G` at every block site, of the product measures `⊗_{ℓ_b}p^G_σ` on `G`-valued links of `rZ^4`, `0 < σ ≤ σ_*`. Each member is a `G`-gauge-invariant probability measure with no Higgs field. On every finite window it has a smooth positive Haar density, the gauge average of a product of smooth positive densities. Its loop data are those of the product measure, since loops are gauge invariant. A block plaquette has holonomy law `p^G_{4σ}`. Block loops with no common block link are independent. The class is a model only; section 7 tests it.

### 5.2 Moments of the vector plaquette

**Lemma HK.** Let `w = (1/10)tr R(u)` and `s > 0`.
(i) *`Spin(10)`.* Under `p_t`, `E w = e^{−9t/2}` and `E w^2 = F(E w)`, with `F(x) = (1 + 45x^{16/9} + 54x^{20/9})/100`.
(ii) *`SU(5)~`.* Under `p_t`, `E w = e^{−12t/5}` and `E w^2 = G(E w)`, with `G(x) = (2 + 48x^{25/12} + 30x^{7/3} + 20x^{3/2})/100`.
(iii) For `0 < s < 840/31775`, `G(e^{−s}) − F(e^{−s}) ≥ (s^2/21600)(840 − 31775s) > 0`. At `s = 1/60` the bound is `18625/4665600000 > 3.99 · 10^{−6}`.
(iv) Let `x = e^{−s}` with `s` as in (iii), and `Θ := (G(x) − F(x))/3`. For every `t' > 0`, `max(|e^{−9t'/2} − x|, |F(e^{−9t'/2}) − G(x)|) ≥ Θ`.

*Proof.* `E w = (1/10)tr e^{−tC_{10}/2}`, and `E w^2 = (1/100)tr e^{−tC_{10⊗10}/2}`, since `(tr R(u))^2` is the character of `R ⊗ R`.

(i) The basis `T_{ij} = E_{ij} − E_{ji}` (`i < j`) is orthonormal. `−Σ_{i<j}T_{ij}^2 = Σ_{i<j}(E_{ii} + E_{jj}) = 9`, so `C_{10} = 9`. Next, `Σ_{i<j}T_{ij} ⊗ T_{ij} = Σ_{i≠j}E_{ij} ⊗ E_{ij} − Σ_{i≠j}E_{ij} ⊗ E_{ji} = K − F`. Here `F` is the flip and `K = Σ_{ij}E_{ij} ⊗ E_{ij} = 10|Ω⟩⟨Ω|`, `Ω = Σ_ie_i ⊗ e_i/√10`; the diagonal terms cancel in the difference. Since `(T ⊗ 1 + 1 ⊗ T)^2 = T^2 ⊗ 1 + 1 ⊗ T^2 + 2T ⊗ T`, `C_{10⊗10} = 9 + 9 − 2(K − F) = 18 − 2K + 2F`. `F` and `K` commute, and `FΩ = Ω`. The joint eigenvalues give: on `Ω`, `C = 0`; on the symmetric tensors orthogonal to `Ω` (dimension 54), `C = 20`; on the antisymmetric tensors (dimension 45), `C = 16`. So `E w^2 = (1 + 45e^{−8t} + 54e^{−10t})/100`. With `x = e^{−9t/2}`, `e^{−8t} = x^{16/9}` and `e^{−10t} = x^{20/9}`.

(ii) For `X ∈ u(5)` acting on `R^{10} = C^5`, `tr_{R^{10}}(X_RY_R) = 2Re tr_5(XY)`. So the restricted inner product on `su(5)` is `−tr_5(XY)`. An orthonormal basis of `u(5)` for `−tr` is `iE_{jj}`, `(E_{jk} − E_{kj})/√2` and `i(E_{jk} + E_{kj})/√2` (`j < k`). Summing over it gives `Σ X ⊗ X = −Σ_{jk}E_{jk} ⊗ E_{kj} = −F`. Removing `(i/√5)1 ⊗ (i/√5)1 = −1/5` gives `Σ_AT_A ⊗ T_A = −F + 1/5` over an orthonormal basis of `su(5)`, on `V ⊗ V` with `V = C^5`. Multiplying the two tensor factors gives `C_V = −(−5 + 1/5) = 24/5`. Likewise `C_{V̄} = 24/5`. Over `C`, `R^{10} ⊗ C = V ⊕ V̄`, so `C_{10} = 24/5` and `E w = e^{−12t/5}`. On `V ⊗ V`, `C = 48/5 − 2(−F + 1/5) = 46/5 + 2F`: `56/5` on the 15 symmetric tensors and `36/5` on the 10 antisymmetric ones. `V̄ ⊗ V̄` is the same. On `V ⊗ V̄` the generators act as `T_A ⊗ 1 + 1 ⊗ T̄_A` with `T̄_A = −T_A^T`. So `Σ T_A ⊗ T̄_A = −(id ⊗ transpose)(−F + 1/5) = K' − 1/5`, with `K' = Σ_{jk}E_{jk} ⊗ E_{jk}` of eigenvalues `5` (once) and `0`. So `C = 10 − 2K'`: `0` once and `10` on 24 dimensions. `V̄ ⊗ V` is the same. In total `C_{10⊗10}` has the eigenvalue `0` twice, `10` on 48 dimensions, `56/5` on 30 and `36/5` on 20. So `E w^2 = (2 + 48e^{−5t} + 30e^{−28t/5} + 20e^{−18t/5})/100`. With `x = e^{−12t/5}`, the exponents become `25/12`, `7/3` and `3/2`. [check] (2a), (2b).

(iii) For `a ≥ 0`, `1 − a + a^2/2 − a^3/6 ≤ e^{−a} ≤ 1 − a + a^2/2`. Proof: `f(a) = e^{−a} − (1 − a + a^2/2)` has `f(0) = 0` and `f'(a) = 1 − a − e^{−a} ≤ 0`, so `f ≤ 0`. Then `g(a) = e^{−a} − (1 − a + a^2/2 − a^3/6)` has `g(0) = 0` and `g' = −f ≥ 0`, so `g ≥ 0`. Apply the lower bound to the three terms of `G` (positive coefficients) and the upper bound to the two terms of `F` (subtracted). The constant terms give `2 + 48 + 30 + 20 − 1 − 45 − 54 = 0`. The linear terms give `−s(48·25/12 + 30·7/3 + 20·3/2 − 45·16/9 − 54·20/9) = −s(200 − 200) = 0`. The quadratic terms give `(s^2/2)(1250/3 − 3680/9) = (35/9)s^2`. The cubic terms of `G` give `−(s^3/6)(15625/36 + 13720/36 + 2430/36) = −(31775/216)s^3`. So

\[
100\,(G−F)(e^{-s})\ \ge\ \tfrac{35}{9}s^2−\tfrac{31775}{216}s^3=\tfrac{s^2}{216}(840−31775s).
\]

At `s = 1/60`, `840 − 31775/60 = 18625/60`, and the bound is `18625/(3600·60·21600) = 18625/4665600000`. [check] (3a): `G − F = 1.05 · 10^{−5}` at `s = 1/60`; the bound holds on its whole range; `G − F > 0` on a grid of `s ∈ [10^{−4}, 3]`.

(iv) `F'(x) = (80x^{7/9} + 120x^{11/9})/100 ∈ [0, 2]` on `[0, 1]`. Put `x' = e^{−9t'/2} ∈ (0, 1)`. If both `|x' − x| < Θ` and `|F(x') − G(x)| < Θ`, then `G(x) − F(x) ≤ |G(x) − F(x')| + |F(x') − F(x)| < Θ + 2Θ = 3Θ`, a contradiction. ∎

At matched first moments the `SU(5)` plaquette fluctuates more than the `Spin(10)` plaquette. Expanding (i) and (ii) to second order in `t` shows that the ratio of the variances tends to `45/24`, the ratio of the dimensions. This is the gluon count of `CH1_5OE_DRAFT.md` Lemma D, here exact and for group-valued measures. [check] (4): Brownian motion on `SU(5)` at `t = 0.2` and on `SO(10)` at `t' = 0.2 · 8/15` (matched `E w = e^{−0.48}`) gives variances `0.00888` and `0.00465`, against the formulas' `0.00892` and `0.00465`.

---

## 6. The witness and the 45-gluon kill

**Theorem W (CH1-5O-E′ holds in the model classes).**
(i) *Any pinned classes.* Fix data as in section 1.2: a block scale `r`, a finite list `Λ` of skeleton loops, the standard identification, classes `𝒞(G_∞)` and `𝒞(Spin(10))` of measures on block configurations, and `δ > 0`. Suppose some `μ ∈ 𝒞(G_∞)` has `d_Λ(μ, 𝒞(Spin(10))) > δ`. Then there are an `L5-O` update and a stationary gauge-invariant state that satisfy (a′) and (b′). If, moreover, the data of `μ` on `P_2(Λ)` equal those of a `𝒢`-invariant configuration law, the state can be chosen cell symmetric, and CH1-5O-E′ holds for these data.
(ii) *The model classes.* Let `H` be the standard Case I group, `(α, β) = (2, −3)`, and `G_∞ = SU(5)~`. Take the classes `RL(SU(5)~; σ_*)` and `RL(Spin(10); σ_*)` for any `σ_* > 0`, any block scale `r = ma`, and any finite list `Λ` of skeleton loops that contains a block plaquette `p`. Let

\[
0<δ<δ_0(σ_*):=\sup\Big\{\tfrac{s^2}{64800}(840−31775s):0<s\le\tfrac{48σ_*}{5},\ 31775s<840\Big\}.
\]

Then CH1-5O-E′ holds for these data. For `σ_* ≥ 1/576` one may take `δ = 10^{−6}`.

*Proof.* (i) Pick `η > 0` with `η ≤ δ` and `d_Λ(μ, 𝒞(Spin(10))) > δ + η`. Pick `k` with `3ε ≤ η`, where `ε = (1 + 3/√k)^N − 1` and `N` is the largest number of fine links of a loop in `Λ`. Take the register `R_k^−` on every link, `τ_E = 0`, and the update of Lemma I. It is an `L5-O` update, and every state is stationary for it. Let `ω` be the state of Theorem U for the configuration law `ν_μ` (subdivision), or for the `𝒢`-invariant law in the second case. By Theorem U(ii), `d_Λ(ω, μ) ≤ 3ε ≤ η ≤ δ`, which is (a′). For every `μ' ∈ 𝒞(Spin(10))`, the triangle inequality gives `d_Λ(ω, μ') ≥ d_Λ(μ, μ') − d_Λ(μ, ω) > (δ + η) − η = δ`, which is (b′). `ω` is gauge invariant by Theorem U(i), and in the second case cell symmetric by Theorem U(iv).

(ii) `ψ(Y) = i·diag(2, 2, 2, −3, −3)` is traceless, so the Lie algebra of `H` lies in `su(5)`. `H` is connected, so `H ⊆ SU(5)~ ⊊ Spin(10)`. `SU(5)~` is closed. Pick `s` in the stated range with `(s^2/64800)(840 − 31775s) > δ`, and put `σ = 5s/48 ≤ σ_*`. Let `μ` be the member of `RL(SU(5)~; σ_*)` at time `σ`. Its plaquette has law `p_{4σ}`, so `E w = e^{−12·4σ/5} = e^{−s}`. By Lemma HK(iii)-(iv), every `μ' ∈ RL(Spin(10); σ_*)`, at any time, differs from `μ` by at least `Θ ≥ (s^2/64800)(840 − 31775s) > δ` on `Ŵ_p` or on `Ŵ_p^2`. So `d_Λ(μ, RL(Spin(10); σ_*)) ≥ Θ > δ`. Now realize `μ` by independent fine links. Let `λ` be the image under `R` of `p^{SU(5)~}_{σ/m}`; it is invariant under `O ↦ O^T`. Under `ν = λ^{⊗L}`, each block link, a product of `m` independent fine values, has law `R_*p_σ`. Distinct block links use disjoint fine links, so they are independent. So the joint law of the skeleton holonomies under `ν` equals that of the block holonomies under `⊗p_σ`, and the data of `ν` on `P_2(Λ)` are the data of `μ`. `ν` is `𝒢`-invariant (section 3). Part (i) applies. For `σ_* ≥ 1/576`, `s = 1/60` is admissible, and `δ_0 ≥ 18625/13996800000 > 1.33 · 10^{−6} > 10^{−6}`. ∎

**The witness, concretely.** Block scale `r = a`. `Λ` is the vector plaquettes of a finite window. `δ = 10^{−6}` and `η = 10^{−7}`. The register is `R_k^−` with `k = 10^{18}`; then `(1 + 3·10^{−9})^4 − 1 < 1.3 · 10^{−8}`, so `3ε < η`. The update is the tick with `τ_E = 0`, followed by `M_o^{−1}` and then `M_e^{−1}`. The state is `ω = (τ ⊗ ∫Φ_udν(u)) ∘ E`, where `ν` makes the fine links independent with law `R_*p^{SU(5)~}_{1/576}`. Every plaquette then has `ω(Ŵ_p) = e^{−1/60}` and `ω(Ŵ_p^2) = G(e^{−1/60})`, within `10^{−7}`. No random-link `Spin(10)` measure, at any time, comes within `10^{−6}` of both values.

**Corollary G (the 45-gluon kill is a statement about the classes).** Fix classes `𝒞` and a list `Λ` of skeleton loops. Let K45 be the statement: for every `L5-O` update, every stationary gauge-invariant state `ω`, and every closed `K` with `H ⊆ K ⊊ Spin(10)`, `d_Λ(ω, 𝒞(Spin(10))) ≤ d_Λ(ω, 𝒞(K))`.
(i) If K45 holds, every `μ ∈ 𝒞(K)` has `d_Λ(μ, 𝒞(Spin(10))) = 0`. If K45 is asked only for cell-symmetric states, the same holds for every `μ ∈ 𝒞(K)` whose data on `P_2(Λ)` are those of a `𝒢`-invariant configuration law.
(ii) In the model classes of Theorem W(ii), K45 is false, also when it is asked only for cell-symmetric states.

*Proof.* (i) Fix `μ` and `η > 0`. Theorem U, with `ν_μ` or with the invariant law, and Lemma I give a stationary gauge-invariant state `ω_η` with `d_Λ(ω_η, μ) ≤ η`. K45 gives `d_Λ(ω_η, 𝒞(Spin(10))) ≤ d_Λ(ω_η, 𝒞(K)) ≤ η`. The triangle inequality gives `d_Λ(μ, 𝒞(Spin(10))) ≤ 2η`. (ii) The state of Theorem W(ii), built with `η < Θ/2`, has `d_Λ(ω, 𝒞(SU(5)~)) ≤ η` and `d_Λ(ω, 𝒞(Spin(10))) ≥ Θ − η > η`. ∎

So any proof of the kill would be a proof about two Yang-Mills classes alone. It would use nothing of `L5-O` beyond what Theorem U and Lemma I already grant. In the model classes the kill is false. For T0-start's classes it would require every `K`-class measure to lie in the closure of the `Spin(10)` class's data. `CH1_5OE_DRAFT.md` Lemma D points the other way at order `g^4` in the Gaussian model.

---

## 7. Four-test checks

Tests (`CH1_5O.md` line 164, quoting `TOE_ASSEMBLY.md` §3.2): "1. It states or fixes something that a part lists as its target. 2. It is open-ended, so a part can add to it to get a result. 3. It settles a downstream physics question by premise. 4. It adds a structure or a constant that its own reasons do not need." These are assessments, not owner decisions. Nothing is adopted.

| Item | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| The update class on file (`CH1_5O_DRAFT.md` line 53, `CH1_5O.md` Definition 1), used inside an existence lemma. Not proposed here; tested because Theorem W uses it | pass | fails: layers can be added until the update is the identity (Lemma I) | fails: "stationary" then holds for every state, so the existence form settles its dynamical part by premise | fails: the inverse layers are structure that neither PS-6r nor the cube tick needs | as written, "stationary for some update" is no condition |
| The random-link classes `RL(G; σ_*)` (section 5.1). Proposed only as a model | pass: the same family for `K` and for `Spin(10)`; no group is fixed | pass: one time parameter per simple factor, closed | pass as a model; fails as a stand-in for T0-start's class, which is what GA2 needs | pass: the heat kernel is the convolution semigroup of the inner product already on file; nothing is tuned | model only, like Lemma D's Gaussian model |
| The register `R_k^−`, `k = 10^{18}`, as a value of the free datum `R` (`LW1_5.md` line 97: "Free data are `ε,μ,τ_E,ω_0`, and `R` or `m`, plus any future plaquette data"). An instance, not a proposal | pass | pass: one integer, fixed by Theorem U's error bound | pass: it decides no downstream question; Theorem W also needs the inverse layers | pass: its only reason is the error bound, which needs it | instance of the free datum; not proposed |

The first row is a finding about a definition on file, not a new reading. The record already holds a pinned alternative. `Y2W_DRAFT.md` line 76 passes Definition SC "only with `ω` the state VC1 supplies". That is the form of section 8.

---

## 8. The form with content: the VC1 state

**Lemma CH1-5O-E′[VC1] (open).** There are values of the free data of `L5-O` (an irreducible register `R`, the constants `ε, μ, τ_E`, and a plaquette class with its constant, GA1-P-5) and pinned data `D` with T0-start's classes, such that the state VC1 supplies for that law satisfies (a′) and (b′).

PS-7r (`LW1_5.md` line 65): "For the gauged law, the vacuum is the state VC1 builds from this sea". VC1's state must be stationary under the law's own tick. `VC1_5.md` line 23: "The target conditions are (i) stationarity under the tick `α`; (ii) local gauge invariance; (iii) invariance under all the stated cell lifts". VC1 is open, so this lemma waits on VC1, GA1-P-5 and Y2-W[`L5-O`]. A kill of it must hold for every state VC1 could supply, that is, for every stationary, gauge-invariant, cell-symmetric state of the law's tick. Four such kills are tried. They differ from A1-A4 (global action, centre, finite registers, dark lift) and from B1-B4 (relational channels, frozen complementarity, Gaussian blindness, a one-site composite).

**Attack C1 (kill: count the plaquette-correlation channels).** Claim: exact `Spin(10)` invariance makes every gauge-covariant moment tensor of a block plaquette matrix `Spin(10)`-invariant. By Schur, all 45 directions then fluctuate with equal weight, and every correlation ratio, such as `Var(w)/(1 − E w)^2`, takes its 45-direction value. Then (a′) fails for every proper `K` once `δ` is below the separation. *Fails at the step "invariance of the moment tensors fixes the gauge-invariant ratios".* The state of Theorem W is gauge invariant, so its moment tensors are `Spin(10)`-invariant. Yet its ratios are those of `SU(5)`: `ω(Ŵ_p^2) = G(ω(Ŵ_p))` within `2·10^{−7}`, not `F(ω(Ŵ_p))` (Lemma HK). The invariance comes from averaging conjugates of `SU(5)`-configurations over the gauge group. The averaging changes no gauge-invariant ratio (Theorem U). So exactness fixes no gauge-invariant count.

**Attack C2 (kill: the free energy of a twisted box).** Claim: in a pure gauge theory at weak coupling, the free energy of a box with a centre twist counts the massless modes, about `dim K` of them. The exact `Spin(10)` law of `L5-O` would make the count 45. *Fails at the step "an `L5-O` state carries a twisted-box free energy".* The tick is a unitary with no Euclidean weight, transfer matrix or partition function. So a state defines no free energy of a box. Two state-level stand-ins exist, and neither counts. (a) A free-energy datum written as a polynomial in finitely many loops takes, in a Theorem U state, the value of the configuration law (Theorem U(iii)). In the state of Theorem W it takes `SU(5)`'s value. (b) The centre-twist operator `T_S = ∏_{ℓ∈S}ρ_ℓ(ϖ at the source end)`, over a finite set `S` of links, is gauge invariant: `ϖ` is central in its end group, and the two end groups commute. In every Theorem U state `ω(T_S) = 0` for `S ≠ ∅`, whatever `ν` is. Indeed `ρ(ϖ_x)ψ_O = ψ_{−O}` up to a phase (Lemma K(vi)), and `ψ_{−O}` is orthogonal to `ψ_O`: in the frame of `O` the two are eigenvectors of `U^{11}` with eigenvalues `k` and `−k`. So `T_S` does not tell `K`-like states from `Spin(10)`-like ones.

**Attack C3 (kill: Ward identities of the exact Gauss law).** Claim: gauge invariance gives the Ward identities `ω([𝒢^{cd}_x, A]) = 0` for all `A`, all 45 generators and every site. A Goldstone-type argument then forces one gapless gauge mode per generator, that is, 45 long-range channels in the plaquette correlations, against every `K`-class with fewer. *Fails at the step "the Ward identities of an exact local symmetry force a massless mode per generator".* The state of Theorem W satisfies every such identity, since it is gauge invariant. It has no long-range correlation at all. Under `ν = λ^{⊗L}`, skeleton loops with no common fine link are independent. By Theorem U(ii) their connected correlation in `ω` is at most `3ε + 2ε + ε^2 < 6ε`, which tends to `0` as `k → ∞`. This is Elitzur's lesson in this setting (credited): local gauge invariance produces no Goldstone modes.

**Attack C4 (kill: Floquet heating).** Claim: the law's tick heats every stationary state to infinite temperature within the conserved Gauss sectors. Then every vector loop has expectation zero, and (a′) fails for every small-field class.

**Proposition Z (Gauss-sector traces kill vector loops).** Let `R` be any finite-dimensional unitary representation of `Spin(20)` used as link register. Let `Λ` be a finite set of sites, and `ℋ_Λ` the space of the matter at `Λ` and of the registers of the links with both ends in `Λ`. Let `𝔊_Λ` be the C*-algebra on `ℋ_Λ` generated by the gauge unitaries `V_x(g)`, `x ∈ Λ`, each acting on the matter at `x` and on the ends at `x` of the links inside `Λ`. Then `tr(ZW_C) = 0` for every `Z ∈ 𝔊_Λ` and every closed path `C` inside `Λ`. So every state that is, on each finite region, of the form `A ↦ tr(Z_ΛA)` with `Z_Λ ∈ 𝔊_Λ` (a mixture of normalized traces over Gauss sectors) has `ω(W_C) = 0`.

*Proof.* `𝔊_Λ` is the closed linear span of the products `∏_{x∈Λ}V_x(g_x)`, since these form a group of unitaries. So it suffices to treat such a product. Matter and links are tensor factors, and `W_C` acts on links only. So `tr(∏_xV_x(g_x)W_C)` is a matter trace, times `tr_{R_ℓ}ρ_ℓ(h_ℓ)` for each link off `C`, times `(1/10)Σ∏_{ℓ∈C}tr_{R_ℓ}(ρ_ℓ(h_ℓ)U^{a_ℓb_ℓ}_ℓ)`. Here `h_ℓ` is the pair of end elements of `ℓ`, and the sum runs over the indices of the trace. Fix one factor `f(h) = tr(ρ(h)U^{ab})`, with `h` in the product `E` of the two end groups. Let `c` be `ϖ` in the target-end group. It commutes with `E`, since it is central in its end group and the end groups commute. Conjugation by `ρ(c)` sends `U^{ab}` to `−U^{ab}`, since `R(ϖ) = −1` on the row index. So `f(h) = tr(ρ(c)ρ(h)U^{ab}ρ(c)^{−1}) = −f(h)`, hence `f(h) = 0`. `C` has at least one link, so every term vanishes. ∎ [check] (1h): `tr(ρ(h)U^{ab}) = 0` on `S_−` for random end rotations `h`.

**HEAT (open hypothesis).** Every stationary, gauge-invariant, cell-symmetric state of the law's own tick (with its plaquette layer, and without inverse layers) is, on each finite region, of the form of Proposition Z. *C4 stops at HEAT.* HEAT is false for the update of Lemma I: the state of Theorem W is stationary for it and has `ω(Ŵ_p) = e^{−1/60} ± 10^{−7}`. For the law's own tick, HEAT is neither proved nor refuted. The stationary states on file do not refute it. The tracial state has this form. So does the dark state `ω_0` of `CH1_5O.md` Theorem 12. `CH1_5O.md` R5 (line 140) proves that every gauge-invariant `T` maps the dark vector `u_S` into its own line. The gauge-invariant operators act on each isotypic component of the gauge representation as the full algebra of its multiplicity space. So the component of `u_S` has multiplicity one, and `ω_0` is the normalized trace over it. Heating of generic periodically driven many-body systems is the expected long-time behaviour (D'Alessio and Rigol; Lazarides, Das and Moessner; context only). If HEAT holds for the law's tick, Proposition Z gives `ω(W_p) = 0` in VC1's state. `CH1_5O.md` R8 (line 157: "CH1-5O-E(a) fails for `ω₀` for every `δ < c_*`") uses only that zero. Applied to VC1's state, it makes (a′) fail for every class with `inf_μ|E_μ(w_p)| > δ`. That would be a named failing step of `L5-O` at Y2-W[`L5-O`] in its VC1 form, for every register. Proposition Z needs only an end-group element that acts as `−1` on the link operators. The central `U(1)` of one end, which multiplies `U^{jk}` by a phase `e^{iθ} ≠ 1`, gives the same proof for `L5-U` loops.

**Status of the VC1 form.** C1, C2 and C3 fail at named steps, each refuted by the state of Theorem W or by Theorem U. C4 stops at HEAT. So CH1-5O-E′[VC1] stays open after three failed attacks, with a fourth stopped at a named open hypothesis.

**What would settle it.** *True:* VC1's state, for some free data, with block data within `δ` of a `K`-class and farther than `δ` from the `Spin(10)` class. Theorem U shows that the registers `R_k^−` carry such data kinematically. The missing piece is stationarity under the law's own tick. *False:* HEAT for the law's tick, which kills the small-field part for every class; or a dynamical theorem about the tick that forces the 45-direction ratios on all its stationary states. *Cheapest guide (not a proof):* the time-averaged plaquette moments of a coherent mixture under the base tick, on a box of two plaquettes with a moderate register, compared with `F` and `G`.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma K: the registers `R_k^−` (the `Spin(20)`-orbit span of `φ_0^{⊗k}` in `S_−^{⊗k}`) are irreducible. Their coherent vectors `ψ_O`, `O ∈ SO(10)`, satisfy `⟨𝐔⟩ = kO` and `‖(𝐔/k − O ⊗ 1)(v ⊗ ψ_O)‖ = 3‖v‖/√k`, and the same for the transpose. They transform as stated under end rotations, `ϖ` and the end swap. `‖𝐔‖ = 10` on `S_−`.
- Theorem U (kinematic universality): for every probability measure `ν` on `SO(10)`-valued configurations, `(τ ⊗ ∫Φ_udν) ∘ E` is a gauge-invariant state. On closed paths of at most `N` links its loop data match `ν`'s within `ε = (1 + 3/√k)^N − 1` (one loop), `3ε` (two loops) and `q·10^{N(q−1)}ε` (`q` loops). It is cell symmetric when `ν` is `𝒢`-invariant.
- Lemma I: the tick followed by its inverse layers is an `L5-O` update in the class on file, and it is the identity. Every state is stationary for it.
- Lemma HK: the exact vector-plaquette moments of heat-kernel laws on `Spin(10)` and on `SU(5)~`, and the separation `G(e^{−s}) − F(e^{−s}) ≥ (s^2/21600)(840 − 31775s)`.
- Theorem W: (i) for any pinned classes, a `K`-class measure at `Λ`-distance more than `δ` from the `Spin(10)` class gives (a′) and (b′), and gives all of CH1-5O-E′ when a `𝒢`-invariant configuration law realizes it; (ii) with the random-link model classes, `H` the standard Case I group, `G_∞ = SU(5)~`, any block scale, any list of skeleton loops containing a plaquette, and `δ < δ_0(σ_*)` (for example `δ = 10^{−6}`), CH1-5O-E′ holds, with an explicit update and an explicit stationary, gauge-invariant, cell-symmetric state.
- Corollary G: the 45-gluon kill implies that every `K`-class measure lies in the closure of the `Spin(10)` class's data (if cell symmetry is asked: every such measure realized by a `𝒢`-invariant law).
- Proposition Z: every Gauss-sector-tracial state has zero vector loops, on every register.
- The four-test checks of section 7.

**Counterexamples.**
- To the 45-gluon kill ("every exactly `Spin(10)`-invariant state matches the 45-gluon class at least as well as any `K`-class"), in the random-link model classes, with stationarity and cell symmetry: Theorem W(ii) with Corollary G(ii).
- To "stationarity under some `L5-O` update constrains a state", in the update class on file: Lemma I.
- To "exactness restricts the finite loop data of stationary gauge-invariant states", for loops that use each link at most once: Theorem U with Lemma I. This settles, for such data, the possibility left open in frozen `CH1_5OE.md` line 31.
- To the key steps of attacks C1, C2 and C3 (section 8).

**Open, by name.**
- **CH1-5O-E′[VC1]** (section 8): the same comparison for the state VC1 supplies. C1 (channel count) fails at "invariance of the moment tensors fixes the gauge-invariant ratios". C2 (twisted box) fails at "an `L5-O` state carries a twisted-box free energy". C3 (Ward identities) fails at "the Ward identities of an exact local symmetry force a massless mode per generator". C4 (Floquet heating) stops at HEAT.
- **HEAT** for the law's own tick (section 8). If it holds, Proposition Z with `CH1_5O.md` R8 gives a named failing step of `L5-O` at Y2-W[`L5-O`] in its VC1 form.
- **SEP[T0-start]**, a request to the Yang-Mills side: some T0-start `K`-measure, with the data of a `𝒢`-invariant configuration law, at `Λ`-distance more than `δ` from T0-start's `Spin(10)` class. With it, CH1-5O-E′ holds with T0-start's classes (Theorem W(i)).
- Inherited, unchanged: CH1-5O-E (the frozen specification), CH1-5O-i, CG1K-H, GA1-P-5, Y2-W[`L5-O`], VC1, and T0-start[G] for `Spin(10)` and for the factors of `G_∞`.

**What changes downstream.**
- *CH1-5O-E′* (`CH1_5OE_DRAFT.md` section 6.2; frozen `CH1_5OE.md` line 167; `CH1.md` Amendment 4): it holds in the model classes. With T0-start's classes it reduces to SEP[T0-start]. In both cases the argument uses only kinematics and the inverse layers. It says nothing about the law's tick and cannot yield a named failing step for `L5-O`. The frozen GAP "the Gaussian calculation does not establish their separation" (`CH1_5OE.md` line 5) is answered in the model classes by Lemma HK, exactly and for group-valued measures.
- *The update class* (`CH1_5O_DRAFT.md` line 53; `CH1_5O.md` Definition 1): in every existence statement over updates, "stationary" is no condition (Lemma I). This applies to CH1-5O-E (`CH1_5O.md` line 175) and to CH1-5O-i (frozen `CH1.md` line 227, quoted in `CH1_5O.md` line 173). The pin is the owner's choice. The VC1 form already on file for SC (`Y2W_DRAFT.md` line 76) is one option. A closed list of gate classes without inverses is another. Nothing is adopted.
- *The gluon count:* exact `Spin(10)` invariance fixes no gauge-invariant count (Theorem U, Corollary G, attack C1). A named failing step of `L5-O`'s route to `G_∞` must use the law's tick (HEAT is one candidate) or a fixed small register such as `S_+`, where Theorem U gives nothing.
- *Y2-W[`L5-O`]:* Theorem U strengthens option (a1) of `Y2W_DRAFT.md` section 5.2, from link coherence to the full loop data of any configuration law, at error `O(N/√k)`. The coupling question and VC1 are untouched. HEAT would settle Y2-W[`L5-O`] negatively in its VC1 form, for every register.
- *`LIT_QLM.md` rebuild candidate 3:* Lemma K and Theorem U supply the coherent symbols and quantitative errors for the family `R_k^−`, for loop data.
- *`L5-U`:* Lemma I holds for its tick, and Proposition Z holds with the central `U(1)` of one end. Theorem U would need a `U(10)` coherent family; it is not done here.

**Named failing steps for `L5-O` or `L5-U`.** None. Neither law fails at a named step here. Both stay live under the owner decision of `TOE_ASSEMBLY.md` §3.5.

**Inputs from outside the working set.** The law `L5-O` of `LW1_5.md` section 2 and the results named in the head, each quoted at its point of use. Standard mathematics rebuilt in the text: the Fock space of ten modes from twenty Majoranas; joint eigenspaces of commuting involutions; irreducibility through one top eigenvector; Cauchy-Schwarz; expansion of products of sums; alternating bounds for `e^{−a}`; completeness relations for `so(10)` and `u(5)`; Casimirs on tensor squares; the mean value theorem; spin lifts of rotations and reflections. Standard mathematics cited, not rebuilt: the heat-kernel measure and its Fourier formula; Peter-Weyl; Haar measure; product states and the tracial state of UHF algebras; local sections of covering maps. Literature context, credited and never load-bearing: Perelomov, Lieb and Simon (coherent states, classical limits); Brower, Chandrasekharan, Riederer and Wiese, Schlittgen and Wiese, and Bär, Brower, Schlittgen and Wiese (quantum links); Migdal, Driver, Sengupta and Lévy (heat-kernel Yang-Mills); Elitzur (no Goldstone modes from local gauge invariance); D'Alessio and Rigol, and Lazarides, Das and Moessner (Floquet heating).
