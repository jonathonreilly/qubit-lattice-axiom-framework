# EW1. Electroweak breaking in an FMS-form diagnostic

## 0. Status

**Proved, conditional on the cited finite-register identities.** The parity and adjoint stabilizer results (Theorem 4.1 and Lemma 4.2), the site datum and product-data obstruction (Propositions 4.3–4.4), the copy and symmetry lemmas (5.1–5.2), the varying-register construction (Theorem 5.3), the one-link bounds (5.4, 6.1–6.2), the graded floor and its conditional application (6.3a and 6.3), the sharp-matter and empty-sector results (6.4–6.5), and the tracial-state result (7.2). The proofs below are author-side, conditional checks, not independent review or retained status.

**GAP: reverse transport ordering.** The draft identifies the adjoint of a projected operator product with the same-order projected product on the reversed link. This is false in general. Definition 2.3 below repairs it by defining reverse factors as adjoints. The displayed construction uses this repaired convention. **GAP: fixed law.** Theorem 5.3 chooses `k` after `δ`. It does not prove Q-EW for a fixed `L5-O[R]`. Its construction uses an identity update made with inverse layers. It does not identify the VC1 vacuum, the long-distance spectrum, the weak scale, or EW⁺. **GAP: vector-link scope.** Lemma 5.4 bounds vector transport, not the even-representation transport required by R-FMS. **GAP: thin-transport interpretation.** The bound in Theorem 6.3 has `c_Φ` in its denominator. A uniform lower bound as `δ → 0` needs a uniform bound on `c_Φ`. **GAP: neutral data.** The draft's downstream assertion that all EW on L5-U needs charged data and fluctuating matter does not follow; Proposition 6.5 explicitly permits neutral data at the Lie-algebra level.

**Open.** EW1-U; EW1-O[U₀]; EW1-i and the hierarchy `va`; CG1K-H and CG1-i; VC1; GA1-P-5; Y2-W; HEAT; the spectrum and the scalar channel. The proposed readings and their checks appear below. No reading is adopted; no law is eliminated. The two laws remain live.

**Provenance.** Pass 1: Claude Opus 5.5, `EW1_DRAFT.md`, SHA-256 `4b79723b52842828130b016c085b7525ba6e89363e1b696423e357cbd0046555`. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1afdd-b84d-71b0-ad95-ab4cfc1dadf2` (from the run log). Working-tree HEAD `90fea6a17f412898cde5d51d7a6789d25d9253f8`; the draft reports its own source revision `dfe1706ec`. Working files can differ from HEAD. Context includes `TOE_ASSEMBLY.md` §§3.4–3.5 and EW1, `LW1.md`, `LW1_5.md`, `CH1.md`, `CH1_5OE.md`, `VC1_5.md`, and `MT1.md`; proofs also cite `CH1_5O.md`, `CH1_5OEP.md`, and `GA2_Y2.md` as named inputs. Their frozen labels do not confer retained status here. The draft's two scratch scripts were unavailable and were not rerun. Numerical checks below are pass-1 reports, not independent evidence.

**Literature scope.** Pass 1 reports a search and reads FMS (1981), Maas (2019), Maas–Sondenheimer–Törek (2019), Fradkin–Shenker (1979), Elitzur (1975), Kajantie et al. (1996), Martin (1992), Krauss–Wilczek (1989), Greensite–Matsuyama (2018), and Hermele–Fisher–Balents (2004). It reports Osterwalder–Seiler inaccessible. Its exact locators and limits are in `EW1_DRAFT.md` §1. References L1–L11 below follow the same order, except L5 is Osterwalder–Seiler, L6 Elitzur, L7 Kajantie et al., L8 Martin, L9 Krauss–Wilczek, L10 Greensite–Matsuyama, and L11 Hermele–Fisher–Balents. These are context and attribution, not proof inputs; they were not independently checked in this pass. In particular the diagnostic below is proposed, not a theorem of FMS.

## 1. Definitions inferred by the distiller

The definitions in this section make the draft’s conventions and implicit quantifiers explicit. They are proposed for this item, not adopted as axioms.

### 2.1 Laws, updates and states

The laws are those of frozen `LW1_5.md` §2. `L5-O[R]` has five matter modes per site, Majoranas `γ_{x,1..10}`, and on each link an irreducible unitary representation `R` of `Spin(20)` carrying `U^{ab} = iη^y_aη^x_b`; its local gauge group is `G = Spin(10)`. `L5-U[m]` has the same matter and on each link the rishon register `Λ^m(C^{10})`, `1 ≤ m ≤ 9`, carrying `U^{jk} = r^y_j r^{x†}_k`; its local gauge group is `G = U(5)`. `𝔄` is the quasi-local algebra (`VC1_5.md` Definition 1). `a_{x,g}` is the local gauge automorphism at site `x`, and `κ_g` the global one (`CH1_5O.md` Theorem 1). `𝒢 = 2Z^3 ⋊ O_{c_0}` is the cell group, with lifts `β_s` (`VC1_5.md` Theorem 2.2). `E : 𝔄 → 𝔄^G` is the gauge average (`VC1_5.md` Theorem 2.1).

An **update of the law** is the base tick `U_0 = W_E M_o M_e`, followed or preceded by finitely many layers of local gauge-invariant gates (`CH1_5O.md` Definition 1; `CH1_5OEP.md` Definition 5). `α` denotes its automorphism. The electric layer `W_E` is defined only for `R = S_+` on `L5-O`; for other `L5-O` registers `τ_E = 0`.

**Definition 2.1 (symmetric, stationary).** A state `ω` of `𝔄` is *symmetric* if `ω∘a_{x,g} = ω` for every site `x` and every `g ∈ G` (the conjugation reading, `VC1_5.md` Definition 3), and `ω∘β_s = ω` for every cell lift. It is *stationary for* `α` if `ω∘α = ω`. It is *stationary under the own tick* if this holds for `α` the base tick `U_0` with no added layer.

### 2.2 Composites

**Definition 2.2 (bosonic composite).** Let `(W, σ)` be a finite-dimensional unitary representation of `G` with orthonormal basis `(e_i)`. A *bosonic composite carried at* `x` *in* `σ` is a tuple `Φ = (Φ^i)` of local, fermion-even, linearly independent elements of `𝔄` such that `a_{x,g}(Φ^i) = Σ_j σ(g)_{ji}Φ^j` for `g ∈ G` and `a_{y,g}(Φ^i) = Φ^i` for every `y ≠ x`. If `σ` is real orthogonal, the `Φ^i` are also self-adjoint. For a `W`-valued `Ψ = (Ψ^i)` write `|Ψ|^2 := Σ_iΨ^{i†}Ψ^i`.

This is `CH1_5O.md` Definition 7 for the span of the `Φ^i`, with "even" added. Because `σ` is unitary, `|Φ|^2` is gauge invariant. For a `G`-invariant polynomial `p` on `W` (a polynomial in the coordinates and their conjugates), `p_sym(Φ)` denotes the evaluation that replaces `w_i` by `Φ^i` and `w̄_i` by `Φ^{i†}` and averages each monomial over all orderings of its factors. It is gauge invariant, because each `a_{x,g}` is an automorphism.

### 2.3 Transporters

Let `V` be the defining representation: `R^{10}` for `Spin(10)` (through `SO(10)`), `C^5` for `U(5)`. On a link `ℓ` the end actions move the rows of the operator matrix `𝐔_ℓ` at the target end and its columns at the source end (`LW1_5.md` §4 "Q and G" and "U"; `CH1_5OEP.md` Definition 2). Let an irreducible `σ` occur in `V^{⊗p} ⊗ V̄^{⊗p′}` with projection `P_σ`. Put `σ(𝐔) := P_σ(𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′})P_σ`, where `𝐔̄` has entries `(U^{jk})^†`, and the tensor product of operator matrices multiplies entries in a fixed left-to-right order. For `σ = ⊕_rσ_r`, a fixed decomposition into irreducibles, put `σ(𝐔) := ⊕_rσ_r(𝐔)`, block diagonal. On `L5-O` the entries are Hermitian, so `p′ = 0`. On `L5-U` the centre `e^{iθ}1_5` acts on an irreducible `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` by `e^{iq_rθ}` with central charge `q_r = p − p′`.

**Definition 2.3 (path transporter).** For a lattice path `π = (z_0, ℓ_1, z_1, …, ℓ_N, z_N)` put `𝒯_π := σ(𝐔_{ℓ_1}^{(ε_1)}/c) ⋯ σ(𝐔_{ℓ_N}^{(ε_N)}/c)`. For each irreducible summand, first form the forward factor `σ(𝐔/c)` in the fixed order above. For traversal in the reverse direction use its matrix adjoint, with the operator products reversed. Thus the factor is `σ(𝐔/c)^†`; do not replace it by a fresh same-order evaluation of `σ(𝐔^†/c)`. Here `c > 0` is a fixed normalization per register. A *transporter* from `z` to `z′` is a convex combination `T = Σ_{π∈Π} c_π𝒯_π` over a fixed finite set `Π` of paths from `z` to `z′`. Its reverse is `T^†`, the same combination over the reversed paths.

*Covariance.* Each local gauge automorphism acts on every entry of `𝐔` by the same linear substitution, and it is an automorphism of `𝔄`. So it acts on the entries of `𝐔^{⊗p}` by the tensor power of that substitution, whatever the order of factors. Hence `a_{z_0,g}(𝒯_π) = σ(g)𝒯_π`, `a_{z_N,g}(𝒯_π) = 𝒯_πσ(g)^{−1}`, and `𝒯_π` is fixed at interior sites, where `σ(g)^{−1}σ(g) = 1` cancels. Noncommutativity of the entries plays no rôle.

For an `End(W)`-valued `M`, write `‖M‖^2_HS := Σ_{ij}M_{ij}^†M_{ij}` and `(M^†)_{ij} := (M_{ji})^†`.

### 2.4 The Standard Model image, the electromagnetic image and the parity element

**Definition 2.4.** `H` is the image of a Case I embedding of the Standard Model Lie algebra with even `a` (`CH1_5O.md` Definition 4): colour on the creators of modes 1-3, weak isospin on modes 4-5, hypercharge `i·diag(a,a,a,b,b)`. Its image in `U(5)` is `π(H) = {(g_3e^{iaθ}) ⊕ (g_2e^{ibθ}) : g_3 ∈ SU(3), g_2 ∈ SU(2), θ ∈ R}` (`CH1_5O.md` R3). On `L5-O`, `H ⊂ π^{−1}(U(5)) ⊂ Spin(10)` with `π : Spin(10) → SO(10)`, and `π|_H` is injective because `−1 ∉ H` (`CH1_5O.md` R4). The *standard ratio* is `(a, b) = (−2, 3)`, the hypercharges `(−1/3, −1/3, −1/3, 1/2, 1/2)` on creators of `CH1.md` §4.1. For it, `Q := T_3 + Y = diag(−1/3, −1/3, −1/3, 1, 0)` on `C^5`, with `T_3 = diag(0,0,0,1/2,−1/2)`.

For the standard ratio, `K_em ⊂ H` is the subgroup with `π(K_em) = {diag(B, (det B)^{−1}, 1) : B ∈ U(3)}`; every statement below that uses `K_em` takes the standard ratio. It is the image of `SU(3) × U(1)_em`, and it equals `Stab_H(e_5)` for `e_5` the fifth creator direction: indeed `π(h)e_5 = e_5` forces `g_2 = diag(e^{iφ}, e^{−iφ})` with `φ = bθ`, so `π(h) = (g_3e^{−2iθ}) ⊕ diag(e^{6iθ}, 1)`, and `B := g_3e^{−2iθ}` has `det B = e^{−6iθ}`. `K_em` is connected (it is a copy of `U(3)`).

The *parity element* `c_F` is `ϖ` on `L5-O` (`CH1_5O.md` Definition 3: `ϖ ∈ Spin(10)` projects to `−I`, and `Z = {±1, ±ϖ}` is the centre) and `−1_5` on `L5-U`. Put `Z_F := Z` on `L5-O` and `Z_F := {±1_5}` on `L5-U`.

### 2.5 The reading R-FMS and its instances

**Definition 2.5 (R-FMS(K; D, δ)).** The data `D = (L, (W, σ), v, Φ, Π, c)` are:
- an even block size `L ≥ 2`, blocks `X = Ln + {0, …, L−1}^3` (`n ∈ Z^3`) and block sites `x_X := Ln`;
- a finite-dimensional unitary representation `(W, σ)` and `v ∈ W ∖ {0}`; put `K := Stab_G(v)`;
- for each block `X`, a bosonic composite `Φ_X` carried at `x_X` in `σ`, supported on the sites of `X` and the links with both ends in `X`, with `Φ_{X+t} = β_t(Φ_X)` for block translations `t ∈ LZ^3`;
- for each ordered pair of neighbouring blocks, a transporter `T_{XY}` from `x_X` to `x_Y` (Definition 2.3), translation covariant, with `T_{YX} = T_{XY}^†`;
- a normalization `c`, and a fixed finite generating set `p_1, …, p_s` of the `G`-invariant polynomials on `W` that contains `|w|^2` and the squared norms `|w_r|^2` of the components of `w` in the summands `σ_r` of the fixed decomposition. Such a set exists by Hilbert's finiteness theorem for compact groups, and invariant polynomials separate the orbits of a compact group; both are standard facts, cited, not rebuilt, and used only to make (O) say "on the orbit `Gv`". No proof below uses them: the proofs use only `|w|^2` and the `|w_r|^2`, each invariant because each summand is.

A state `ω` satisfies R-FMS(`K; D, δ`) if for all neighbouring blocks `X, Y`:
- **(O) orbit:** `ω(|p_{j,sym}(Φ_X) − p_j(v)|^2) ≤ δ` for every `j`;
- **(C) classicality:** `Σ_{i,j} ω(|[Φ_X^i, Φ_X^j]|^2 + |[Φ_X^i, Φ_X^{j†}]|^2) ≤ δ`;
- **(A) alignment:** `ω(|Φ_X − T_{XY}Φ_Y|^2) ≤ δ|v|^2`;
- **(T) transport:** `ω(‖T_{XY}^†T_{XY} − 1‖^2_HS) ≤ δ` and `ω(‖T_{XY}T_{XY}^† − 1‖^2_HS) ≤ δ`.

Each operator inside `ω(·)` is gauge invariant: the indices transform by the unitary `σ` at `x_X` or `x_Y` and are summed.

**Definition 2.6 (instances).** Write `𝔨 := Lie(K)`, `𝔥 := Lie(H)`, `𝔨_em := Lie(K_em)`.
- **EW(δ)** (the lane's statement, "SU(2) × U(1) broken to U(1)_em"): `ω` satisfies R-FMS(`K; D, δ`) for some data with `𝔨 ∩ 𝔥 = 𝔨_em`. Since `K_em` is connected, this says `(K ∩ H)_0 = K_em`.
- **EW_grp(δ):** the same with `K ∩ H = K_em`.
- **EW⁺(δ)** (EW1's full pattern, read with the parity element): the same with `K = K_em·Z_F`.
- **Q-EW** (the question): is there a fixed triple `(W, σ, v)` with `Lie(Stab v) ∩ 𝔥 = 𝔨_em` such that for every `δ > 0` some symmetric state, stationary for an update of the law, and some data `D` with this triple satisfy R-FMS(`Stab v; D, δ`)? The orbit point is fixed in advance, as FMS fix their orbit; only `L`, the composites, the transporters and the state may depend on `δ`. Without this, a datum could break a symmetry through components smaller than the tolerance.

---

## 2. Proposed readings of "broken" and their four tests

The tests are those of `TOE_ASSEMBLY.md` §3.2: a reading fails if it "(1) states or fixes something that a part lists as its target, (2) is open-ended, so a part can add to it to get a result, (3) settles a downstream physics question by premise, or (4) adds a structure or a constant that its own reasons do not need." The verdicts below are this pass's assessments, not owner decisions.

**R-VEV (a local order parameter).** "`G` is broken to `K`" if some covariant multiplet `Φ` without a trivial summand has `ω(Φ) ≠ 0` with stabilizer `K`. In every symmetric state this expectation vanishes: frozen `CH1_5O.md` Theorem 2 says "For a covariant multiplet ... its expectation vector obeys v=ρ(g)^T v; it vanishes if ρ has no trivial summand." So R-VEV makes EW1 false by premise in every state. Test 3 fails. Rejected (Elitzur's point, L6).

**R-A and R-L.** Already rejected for EW1 in frozen `CH1_5O.md` (table at lines 166-171): under R-A nothing ever breaks; R-L depends on the lift (Theorem 12). Not revisited.

**R-ST (the local stratum).** "`G` is broken to `K`" if the invariant polynomials of some composite are sharp at the values of an orbit with stabilizer `K`, with no alignment clause. The stratum of a field value is gauge invariant (L2 §3.9). But the minimizing orbit is the same in the Higgs and the confinement regime of one model, and for fundamental Higgs fields the two "are smoothly connected" (L4; L1 p. 30). Read without alignment, R-ST calls the confinement-like regime "broken". It decides by premise that the coset gauge directions are Higgsed whenever a composite sits on the orbit, and that is the content of EW1(a)'s "three massive weak bosons". Test 3 fails. Recorded, not proposed.

**R-SPEC (the spectrum itself).** "Broken" read as "three massive vector channels and one massless one". This is EW1(a)'s own clause. Test 1 fails. It stays EW1's later target; it is not a reading of "broken".

**R-FMS (Definition 2.5), proposed.**
- *Test 1: passes.* It is defined for every closed `K` and asserts nothing. EW, EW_grp and EW⁺ pose EW1's target as questions; no clause of the reading names the Standard Model pattern.
- *Test 2: passes once the data are pinned.* The class of composites (bosonic, carried at the block site, supported in the block) and of transporters (convex combinations over a fixed path set) is fixed in advance. The quantifiers over `δ` and `L` belong to the question Q-EW. A part cannot add a clause.
- *Test 3: passes.* It is a regime statement, which is what L1 (p. 30) and L2 (§3.7) say a gauge-invariant Higgs statement can be. It settles none of EW1(a)'s spectral clauses: the massive `W` and `Z`, the massless photon, the Higgs scalar and the scale `v` remain to be derived.
- *Test 4: passes.* Each ingredient answers its own reason. `W` and `v` state "an orbit with a residual group" (L1 p. 34). "Bosonic": the FMS Higgs field is bosonic, a symmetric state is even (`CH1_5O.md` Theorem 2), and odd block averages do not become commuting: for odd `ψ_x, ψ_y` at different sites `[ψ_x, ψ_y] = 2ψ_xψ_y`, so for odd block averages `[Φ^i, Φ^j] = 2Φ^iΦ^j` up to a term of order `1/|X|`, which averaging does not shrink. (C): orbit values need commuting coordinates. (A): it is the operator form of the frozen relation `φ_x = σ(U_xy)φ_y`, which is FMS's Higgs-regime condition; without it R-ST results. Path transporters: PS-6 says link registers transport frames; and without this restriction (A) is empty, since for a composite built from link operators only, `T := Φ_XΦ_Y^†/|v|^2` is a covariant link-only operator with `TΦ_Y = Φ_X|Φ_Y|^2/|v|^2`, which (O) makes close to `Φ_X`. (T): the frozen relation uses group elements, and (T) is its operator form. `δ` and `L` are needed by any regime statement. The reading fixes no constant.
- *Relation to R-E.* With `δ → 0`, R-FMS asks the block data to approach those of a frozen `G` gauge-Higgs configuration at the orbit `Gv` (frozen `CH1_5OE.md` Definition 3). This file proves no implication either way between R-FMS and the comparison readings of `CH1_5O.md` and `CH1_5OE.md`.

**EW (Definition 2.6), the instance.** Test 1: it is EW1's target posed as a question, which is allowed; the reading does not assert it. Test 2: closed. Test 3: it ignores generators outside `H`, so it does not settle CG1K-H. Test 4: `H` is a parameter; the hypercharge ratio is CG1-i's open input. The explicit results below use the standard ratio, which is the one EW1's target names through the Standard Model charges. Passes.

**EW⁺, the full pattern read with the parity element.** Read EW1's "`SU(3) x U(1)_em`" as `K_em·Z_F`. Test 1: it changes the target's wording only by the element that Theorem 4.1 forces into every R-FMS stabilizer. Test 2: closed. Test 3: it concedes an unbroken gauged fermion parity but does not decide its downstream effects (FL2, CS1). Test 4: it adds exactly `Z_F`, which Theorem 4.1 requires. Passes. Proposed to the owner as the reading of EW1's target group on both five-mode laws.

---

## 4. Structural results on both laws

### 4.1 The parity element is never broken

**Theorem 4.1 (centre).** Take `L5-O[R]` with `R` irreducible, or `L5-U[m]` with any `m`. Let `Φ` be a bosonic composite carried at `x` in `σ`.
1. `a_{x,c}(Φ^i) = Φ^i` for every `c ∈ Z_F` and every `i`. Hence `σ(c) = 1_W`, and `Z_F ⊆ Stab_G(v)` for every `v ∈ W`.
2. `c_F ∉ H`. Hence `K_em·Z_F ≠ K_em`.
3. So in every state of either law, every R-FMS stabilizer `K` with `K ⊇ K_em` contains `K_em·Z_F`. In particular no state satisfies R-FMS with `K = K_em`: the literal full pattern "`G` → `SU(3) x U(1)_em`" is never realized in FMS form.

*Proof.* (1) on `L5-O`. Frozen `CH1_5O.md` Theorem 1 gives `κ_{−1} = id` and `κ_ϖ = Θ`, fermion parity, for irreducible registers (its Definition 3 records these as source identities). For the registers used below the end actions are also scalar: `S_±(20)` restricts to `Spin(10) × Spin(10)` as a sum of products of half-spin factors, on each of which `−1` acts by `−1`, so `−1` at one end acts on `S_±^{⊗k}` by `(−1)^k`. Here `κ_g(A) = ∏_{y∈S(A)} a_{y,g}(A)` over the gauge support. `Φ^i` is carried at `x`, so `a_{y,g}(Φ^i) = Φ^i` for `y ≠ x`. Hence `a_{x,ϖ}(Φ^i) = κ_ϖ(Φ^i) = Θ(Φ^i) = Φ^i`, since `Φ^i` is even. Likewise `a_{x,−1}(Φ^i) = Φ^i`. Then `Σ_jσ(c)_{ji}Φ^j = Φ^i`, and linear independence gives `σ(c) = 1`.

(1) on `L5-U`. The central element `e^{iθ}1_5` of `U(5)_x` acts by `Ad e^{iθQ_x}`, with `Q_x = N_x + Σ_{ℓ∋x}p_{ℓ,x}` the trace Gauss generator (`LW1_5.md` §2, line 90, with `T = 1`; `Q_x` as in its §6). Split `Φ^i = Σ_qΦ^i_q` into `Q_x`-charge components. Each component still commutes with every `Q_y`, `y ≠ x`, because `Q_x` and `Q_y` commute. Frozen `LW1_5.md` Z-U: "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change, and its matter parity is \((-1)^{\sum q_x}\)." So `Φ^i_q` has parity `(−1)^q`. `Φ^i` is even, so only even `q` occur, and `a_{x,−1_5}(Φ^i) = Σ_q(−1)^qΦ^i_q = Φ^i`. Conclude as before.

(2) Frozen `CH1_5O.md` R3: for coprime `(a,b)` with `a` even, "`−I_{10} ∉ π(H)`, so `±ϖ ∉ H`." Its proof shows `−1_5 ∉ π(H)` inside `U(5)`; on `L5-U`, `H = π(H)`, so `−1_5 ∉ H`. Since `K_em ⊆ H`, `c_F ∉ K_em`.

(3) By (1), `Z_F ⊆ K` for every R-FMS datum. If also `K ⊇ K_em`, then `K ⊇ K_em·Z_F`, which is strictly larger than `K_em` by (2). □

**Reading of Theorem 4.1.** `c_F` acts as `−1` on every fermion-odd local operator and as `+1` on every bosonic one; it is a gauged fermion parity. Martin's SO(10) statement (L8) has the same structure: tensor-class order parameters leave "an unbroken R_p", and the target is written "SU(3)_c × U(1)_EM × R_p". On the Standard Model fields with `ν^c`, matter parity `(−1)^{3(B−L)}` equals fermion parity: `3(B − L)` is `1` on quarks, `−3` on leptons and `0` on the Higgs and gauge fields. So EW⁺ is the five-mode analogue of the usual SO(10) electroweak target. This is a reading of EW1's wording, not a failing step of either law. It confirms the remark of frozen `CH1_5O.md` line 90 in FMS form.

### 4.2 Adjoint data never break the electroweak group

**Lemma 4.2 (rank).** Let `W` be a direct sum of copies of the trivial representation and of the adjoint representation (`so(10)` on `L5-O`, `u(5)` on `L5-U`). Let `v ∈ W` with `K_em ⊆ Stab(v)`. Then `Stab(v) ⊇ K_ad`, where `π(K_ad) = U(3) × U(1)_4 × U(1)_5` (block-diagonal on `C^3 ⊕ C e_4 ⊕ C e_5`; on `L5-U` read `π` as the identity of `U(5)`). Moreover `𝔨_ad ∩ 𝔥` has dimension 10, while `𝔨_em` has dimension 9. So no datum of this kind satisfies EW.

*Proof.* Each adjoint component `v_r` of `v` is fixed by `K_em`.

On `L5-O`, `v_r` is a real antisymmetric `10 × 10` matrix commuting with `π(K_em) ≅ U(3)`. As a real representation of this group, `R^{10} = R^6 ⊕ R^2_4 ⊕ R^2_5`: `R^6` is `C^3` with `B` acting, `R^2_4` is `C` with `(det B)^{−1}` acting, and `R^2_5` is two copies of the trivial representation. The first two are irreducible of complex type: `SU(3) ⊂ U(3)` acts irreducibly on `C^3`, which is not self-conjugate, and `(det B)^{−1}` is a character with non-real values. They are not isomorphic to each other (dimensions 6 and 2), and neither contains the trivial representation, which makes up `R^2_5`. By Schur's lemma the commutant is `C·1_6 ⊕ C·1_2 ⊕ M_2(R)`, where `C` acts through the complex structures. Its antisymmetric elements are the span of `J_6`, `J_4`, `J_2`, the complex structures of the three blocks. Each of these commutes with `U(3) × U(1)_4 × U(1)_5`. So `v_r` is fixed by that group, and `Stab(v) ⊇ π^{−1}(U(3) × U(1)_4 × U(1)_5) =: K_ad`.

On `L5-U`, `v_r ∈ u(5)` commutes with `π(K_em)`. As a complex representation, `C^5 = C^3 ⊕ Ce_4 ⊕ Ce_5` is a sum of three pairwise non-isomorphic irreducibles. So `v_r = i·diag(α, α, α, β, γ)`, which is fixed by `U(3) × U(1) × U(1)`.

Finally `K_ad ∩ H ⊇ {h : π(h) = (g_3e^{iaθ}) ⊕ diag(e^{i(φ+bθ)}, e^{i(−φ+bθ)})}`, a group of dimension `8 + 2 = 10`, with Lie algebra `su(3) ⊕ u(1)_{T_3} ⊕ u(1)_Y`. □

[check] (`check_stab.py`): the `K_em`-fixed subspace of `so(10)` has dimension 3.

*Meaning.* An adjoint Higgs field never lowers the rank. Lemma 4.2 says more: any number of adjoint fields that all respect `K_em` leave both `T_3` and `Y` unbroken. So EW needs a datum outside the adjoint. Matter bilinears `M_x^{ab}`, link-end generators `L_{ℓ,x}^{cd}` and rishon bilinears `r^{x†}_ar^x_b` do not suffice, alone or together.

### 4.3 A one-site datum that realizes the electroweak pattern

Write `|∅⟩` for the matter vacuum of a site and `e_{1234} := c^†_1c^†_2c^†_3c^†_4|∅⟩`. For `α, β ∈ C` with `αβ ≠ 0` and `|α|^2 + |β|^2 = 1` put
\[
\psi := \alpha|\varnothing\rangle + \beta\, e_{1234},\qquad \rho_\psi := |\psi\rangle\langle\psi| .
\]
Let `Q_x := (M_x^{ab})_{a<b} ⊕ (Γ_x^{abcd})_{a<b<c<d}`, with `M^{ab} = (i/2)γ_aγ_b` and `Γ^{abcd} = γ_aγ_bγ_cγ_d`. Let `W_Q := Λ^2R^{10} ⊕ Λ^4R^{10}` (real dimension 255) with the action `σ_Q` through `SO(10)`, and `q_ψ := ρ_ψ(Q_x) ∈ W_Q`.

**Proposition 4.3 (the site datum).** On `L5-O`:
1. `Q_x` is a bosonic composite carried at `x` in `σ_Q`, with self-adjoint, linearly independent entries.
2. `Stab_{Spin(10)}(q_ψ) = {g : V_x(g)ψ ∈ Cψ}`, the stabilizer of the ray of `ψ` under the site spin representation `V_x`.
3. For the standard ratio, `Stab(q_ψ) ∩ H = K_em`.
4. `Stab(q_ψ) ⊇ π^{−1}(SU(4) × U(1)_5)`, where `SU(4)` acts on `span(e_1, …, e_4)`. If `|α| ≠ |β|`, the Lie algebra of `Stab(q_ψ)` is exactly `su(4) ⊕ u(1)_5`, of dimension 16.
5. `q_ψ ≠ 0` when `|α| ≠ |β|`.

*Proof.* (1) The entries are even. `M^{ab}` is Hermitian. `Γ^{abcd}` is Hermitian for distinct indices: reversing four anticommuting Hermitian involutions costs `(−1)^{4·3/2} = +1`. Frozen `LW1_5.md` §4 "Q and G": the local transformations "implement \(SO(10)\) on site algebras", with `a_{x,g}(γ_{x,a}) = Σ_bR(g)_{ba}γ_{x,b}`; so `M` and `Γ` transform by `Λ^2R(g)` and `Λ^4R(g)`. Local groups at other sites fix the matter of `x`. Distinct Clifford monomials are linearly independent (`LW1_5.md` F and K: "all such monomials form a basis").

(2) `ρ_ψ` is supported on the even Fock space `H_+`, of dimension 16. Frozen `LW1_5.md` S′ step 3: restriction to `H_+` maps the even algebra onto `End(H_+)`, and "even monomials with at most one member of each pair {S,S^c} stay independent on H_+". The `1 + 45 + 210 = 256` monomials of degree 0, 2 and 4 contain no complementary pair, so they form a basis of `End(H_+)`. Hence a density matrix `ρ` on `H_+` is determined by `q_ρ := ρ(Q_x)`. The map is equivariant: `q_{V(g)ρV(g)^*} = σ_Q(g)q_ρ`, because `(V(g)ρV(g)^*)(A) = ρ(V(g)^*AV(g)) = ρ(a_{x,g^{−1}}(A))` and `σ_Q` is orthogonal. So `σ_Q(g)q_ψ = q_ψ` exactly when `V(g)ρ_ψV(g)^* = ρ_ψ`, that is, when `V(g)ψ ∈ Cψ`.

(3) Let `h ∈ H` and `u := π(h) = (g_3e^{iaθ}) ⊕ (g_2e^{ibθ})`. For `g ∈ π^{−1}(U(5))`, `V(g)c^†_jV(g)^* = Σ_ku_{kj}c^†_k`, since the number-preserving part of the Bogoliubov action is `U(5)` (`LW1_5.md` C). And `V(g)|∅⟩ = χ(g)|∅⟩` with `|χ(g)| = 1`: `|∅⟩` spans the vectors killed by every `c_k`, and `V(g)|∅⟩` is killed by every `V(g)c_jV(g)^* = Σ_kū_{kj}c_k`. Hence
\[
V(g)\psi=\chi(g)\big(\alpha|\varnothing\rangle+\beta\,(ue_1)\wedge(ue_2)\wedge(ue_3)\wedge(ue_4)\big).
\]
The `Λ^0` and `Λ^4` parts are independent and `α ≠ 0`, so `V(g)ψ ∈ Cψ` exactly when `(ue_1)∧⋯∧(ue_4) = e_1∧⋯∧e_4`. A nonzero decomposable 4-vector determines its 4-plane, so this holds exactly when `u` preserves `E := span(e_1, …, e_4)` and `det(u|_E) = 1`. For `u = π(h)`, preserving `E` means that `g_2e^{ibθ}` preserves `Ce_4`, so `g_2 = diag(e^{iφ}, e^{−iφ})`. Then `det(u|_E) = e^{i(3aθ + φ + bθ)}`, and the condition is `φ ≡ −(3a+b)θ`. So `u = (g_3e^{iaθ}) ⊕ diag(e^{−3iaθ}, e^{i(3a+2b)θ})`. For `(a,b) = (−2,3)`, `3a + 2b = 0` and `u = diag(B, (det B)^{−1}, 1)` with `B = g_3e^{−2iθ}`. Conversely each such `u` with `B ∈ U(3)` has this form: choose `θ` with `e^{−6iθ} = det B`, `g_3 = Be^{2iθ}` and `φ = 3θ`. So `π(Stab(q_ψ) ∩ H) = π(K_em)`. Since `π|_H` is injective (`CH1_5O.md` R4), `Stab(q_ψ) ∩ H = K_em`.

(4) If `u = diag(A, λ)` with `A ∈ SU(4)`, then `u` preserves `E` with determinant 1, so `g` fixes the ray. For the Lie algebra, split `so(10) = u(5) ⊕ 𝔭`, where `dV(𝔭)` is spanned by the anti-Hermitian pair operators `Σ_{i<j}(ζ_{ij}c^†_ic^†_j − ζ̄_{ij}c_jc_i)`. `dV(X)` for `X ∈ u(5)` preserves each `Λ^pC^5`; `dV(𝔭)` maps `Λ^0` and `Λ^4` into `Λ^2` (pair creation on `e_{1234}` vanishes, since every pair meets `{1,2,3,4}` or is `{5,5}`). So `X = X_u + X_𝔭` fixes the ray exactly when `dV(X_u)ψ ∈ Cψ` and `dV(X_𝔭)ψ = 0`. The first condition is the infinitesimal form of (3): `X_u` preserves `E` and has zero trace on `E`, which gives `su(4) ⊕ u(1)_5`. For the second: the coefficient of `c^†_ic^†_5|∅⟩` is `αζ_{i5}`, so `ζ_{i5} = 0`. For `{i,j} ⊂ {1,2,3,4}` with complement `{k,l}` in `{1,2,3,4}`, the coefficient of `c^†_ic^†_j|∅⟩` is `αζ_{ij} + s_{ij}βζ̄_{kl}` with a sign `s_{ij} = ±1`. Its vanishing for `{i,j}` and for `{k,l}` gives `|ζ_{ij}| = |β/α||ζ_{kl}|` and `|ζ_{kl}| = |β/α||ζ_{ij}|`. So `|ζ_{ij}|(1 − |β/α|^2) = 0`, and `|α| ≠ |β|` forces `ζ = 0`.

(5) `M^{12} = n_1 − 1/2` (`LW1_5.md` §1), so `ρ_ψ(M^{12}) = |β|^2 − 1/2 ≠ 0`. □

[check] (`check_stab.py`): the ray stabilizer has dimension 16 at `(α, β) = (√(3/4), 1/2)` and at `(0.6, 0.8i)`; 22 at `|α| = |β|`; 25 for `|∅⟩`. `dim(Lie(Stab) ∩ 𝔥) = 9` for `(a,b) = (−2,3)`, and the generators of `𝔨_em` fix the ray. For `(a,b) = (2,3), (2,1), (4,−3)` the intersection also has dimension 9, but by part (3)'s computation its `U(1)` acts on `e_5` by `e^{i(3a+2b)θ}`, so it is not `K_em` there. A non-standard ratio needs its own datum.

### 4.4 Product data keep an extra U(1) on L5-O

Let `U(1)_λ := π^{−1}({diag(1,1,1,1,λ) : |λ| = 1})_0`.

**Proposition 4.4.** Let `T_em` be the maximal torus of `K_em`. Every vector of `End(H_+) ⊕ End(H_−)` (the bosonic site algebra, under conjugation by `V_x`) and every vector of `so(10)` that is fixed by `T_em` is fixed by `U(1)_λ`. `U(1)_λ ∩ H` is finite, and trivial for the standard ratio. Hence if every component of an R-FMS datum `v` lies in these representations and `K_em ⊆ K`, then `K ⊇ K_em·Z·U(1)_λ ≠ K_em·Z`, and EW⁺ fails.

*Proof.* In the site algebra `M_32(C)` the normal-ordered monomials `c^†_Ic_J` (`I, J ⊆ {1, …, 5}`) form a basis of 1024 elements. Under conjugation by `V(g)` with `π(g) = diag(e^{it_1}, …, e^{it_5})`, `c^†_Ic_J` has weight `Σ_{i∈I}t_i − Σ_{j∈J}t_j`; the scalar `χ(g)` cancels. Even operators have `|I| + |J|` even. On `T_em`, `t_4 = −(t_1+t_2+t_3)` and `t_5 = 0`. So the weight vanishes on `T_em` exactly when, for each colour `c ∈ {1,2,3}`, `[c ∈ I] − [c ∈ J] = [4 ∈ I] − [4 ∈ J] =: s`. The `U(1)_λ`-weight is `[5 ∈ I] − [5 ∈ J]`.
- `s = 1`: `{1,2,3,4} ⊆ I ∖ J`, so `J ⊆ {5}`. If `5 ∈ I ∖ J` then `J = ∅` and `|I| + |J| = 5`, odd. If `5 ∈ J ∖ I` then `|I| + |J| = 5`, odd. So `5` is in neither or both, and the `λ`-weight is 0. The case `s = −1` is the same with `I` and `J` exchanged.
- `s = 0`: each of `1, …, 4` lies in both or neither of `I, J`. So `|I| + |J| = 2|I ∩ J ∩ {1,…,4}| + [5∈I] + [5∈J]`. Evenness forces `[5∈I] = [5∈J]`, and the `λ`-weight is 0.

`T_em` and `U(1)_λ` are commuting tori, so the `T_em`-fixed subspace is spanned by joint weight vectors, all of `λ`-weight 0. So `U(1)_λ` fixes it. `so(10)` sits in the even site algebra through `M^{ab}`, so the same holds there (also directly: Lemma 4.2's span of `J_6, J_4, J_2` commutes with `diag(1,1,1,1,λ)`).

`diag(1,1,1,1,λ) = π(h)` for `h ∈ H` forces `g_3 = e^{−iaθ}1_3 ∈ SU(3)`, so `e^{3iaθ} = 1`, and `g_2 = diag(e^{−ibθ}, λe^{−ibθ}) ∈ SU(2)`, so `λ = e^{2ibθ}`. This is a finite set; for `(−2,3)`, `e^{−6iθ} = 1` gives `λ = 1`. Then `K ⊇ K_em·Z` (Theorem 4.1) and `K ⊇ U(1)_λ ⊄ K_em·Z`. □

[check] (`check_stab.py`): the `𝔨_em`-fixed even site operators form a 20-dimensional space, and `max|[dV(λ), O]| = 8.9·10^{−16}` on it.

*Meaning.* Data built from single sites and from adjoint link values (the classical values of coherent registers) realize at best EW and EW_grp, never EW⁺. On `L5-O`, EW⁺ needs data that correlate different sites, for example two-site `Λ^5 ⊗ Λ^5` composites; these have zero expectation in every product of even site states.

---

## 5. L5-O: a construction, and what it does not give

The register is `R_k^-` of frozen `CH1_5OEP.md` Theorem 1, the irreducible top component of `S_-^{⊗k}`. It is an irreducible `so(20)` register, so it lies inside `L5-O`'s free data (`LW1_5.md` §2: "Each link carries a finite nontrivial unitary representation \(R\) of \(\operatorname{Spin}(20)\)"). The electric layer is undefined there, so `τ_E = 0`. The normalization is `c = κ_R = k` (`CH1_5OEP.md` O1). `ψ_I := φ_0^{⊗k}` is the coherent ray at `O = I`.

**Lemma 5.1 (copy expansion).** Let `m = ∏_{j=1}^{d}(U^{a_jb_j}/k)` be a product, in any order, of `d` normalized entries of one link. Then `‖m‖ ≤ 1` and `|⟨ψ_I, mψ_I⟩ − ∏_jδ_{a_jb_j}| ≤ d^2/k`.

*Proof.* On `R_k^-` the link operators are sums over the `k` copies (`CH1_5OEP.md` Theorem 1: "The link operators on it are sums over the k copies"): `U^{ab} = Σ_iU^{ab}_{(i)}`. Each `U^{ab}_{(i)} = iη^y_aη^x_b` is Hermitian with square 1, so `‖U^{ab}/k‖ ≤ 1` and `‖m‖ ≤ 1`. Expand `m = k^{−d}Σ_{i_1,…,i_d}∏_jU^{a_jb_j}_{(i_j)}`. If the copies are distinct, the factors act on different tensor factors of the product vector `ψ_I` and the expectation factorizes. On one copy, `⟨φ_0, U^{ab}φ_0⟩ = δ_{ab}`: `φ_0` is the joint `+1` vector of the `U^{aa}`, and each off-diagonal `U^{ab}` anticommutes with `U^{bb}`, so its expectation vanishes (`CH1_5OEP.md` Theorem 1's proof). There are `k(k−1)⋯(k−d+1) ≥ k^d − C(d,2)k^{d−1}` tuples of distinct copies. Each of the at most `C(d,2)k^{d−1}` other tuples gives a term of modulus at most 1. So the deviation is at most `2C(d,2)/k ≤ d^2/k`. □

Let `Φ_prod := (⊗_xρ_ψ) ⊗ (⊗_ℓ|ψ_I⟩⟨ψ_I|)`, the consistent even product state with the site state `ρ_ψ` of §4.3 at every site and `ψ_I` on every link (`VC1_5.md` Definition 1). Put `ω := Φ_prod∘E`.

**Lemma 5.2 (symmetry and stationarity).** `ω` is symmetric. It is stationary for the update `α_id` of frozen `CH1_5OEP.md` Theorem 3 (the base tick followed by `M_o^{−1}` and `M_e^{−1}`), which is the identity.

*Proof.* Gauge invariance: `φ∘E` is gauge invariant for every state `φ` (`VC1_5.md` Theorem 2.1). Stationarity: `CH1_5OEP.md` Theorem 3 says "The tick followed by \(W_E^{-1}\), \(M_o^{-1}\), then \(M_e^{-1}\) is an allowed update and is the identity", for any irreducible register with `τ_E = 0`; it also says "Each inverse layer has the covariance of its original layer."

Cell lifts. The lifts exist on `R_k^-`: `CH1_5OEP.md` Definition 2 says that for an irreducible register other than `S_+`, with `τ_E = 0`, "the same proof applies: the end swap ∏_a(η^y_a−η^x_a)/√2 lies in Spin(20) and acts on every Spin(20) register". `E` commutes with every lift (`VC1_5.md` Theorem 2.1), so `ω∘β_s = (Φ_prod∘β_s)∘E`. It suffices to show `Φ_prod∘β_s = Φ_prod∘a` for a product `a` of local gauge automorphisms, because `E∘a = E`. The lift acts on matter by `γ_{x,a} ↦ ±γ_{sx,a}`, with the sign implemented by site parity (`LW1_5.md` B1-5: "Site parity implements LW1's sign lift"). `ρ_ψ` is even, so `Ad P` fixes it, and the matter factor of `Φ_prod∘β_s` is again `⊗_xρ_ψ`. The same holds if a lift also multiplies every mode of a site by a power of `i`, as the conjugation by `W_x = i^{x_1+x_2+x_3}` in `LW1_5.md` A2-5 does for the free walk: `|∅⟩` is fixed and `c^†_1c^†_2c^†_3c^†_4` picks up `i^{4s} = 1`. On a link whose orientation the lift keeps, the register operators go to those of the image link, and `ψ_I` goes to `ψ_I`. On a reversed link the lift acts by the end swap, which sends `ψ_O` to `ψ_{−O^T}` (`CH1_5OEP.md` Theorem 1 and R-S), so `ψ_I` goes to `ψ_{−I}`. By `CH1_5OEP.md` Theorem 2's proof, "The unwanted link sign is σ_xσ_y, produced by the local central gauge transformations at sites with σ_x=−1", where `σ_x = (−1)^{Σ_{i∈J}x_i}` and `J` is the set of reversed directions. Let `a := ∏_{σ_x = −1}a_{x,ϖ}`. On links it multiplies the row or column of each end with `σ = −1` by `R(ϖ) = −I`. So it sends `ψ_I` to `ψ_{σ_xσ_yI}` on each link (`CH1_5OEP.md` Theorem 1: "End gauge actions send the ray to ψ_{R(g)O} and ψ_{OR(g)^T}"), which is `ψ_{−I}` exactly on the reversed links. On matter, `a_{x,ϖ}` acts by `Ad(−iP_x)` (`LW1_5.md` §5: "The site factors are respectively \(-1\) and \(-iP_x\)"), which fixes the even `ρ_ψ`. So `Φ_prod∘β_s = Φ_prod∘a` (up to the order of `a` and the lift's permutation of sites and links, which preserves the product form). □

**Theorem 5.3 (the electroweak pattern is realized on L5-O).** Take the standard ratio, `αβ ≠ 0` and `|α| ≠ |β|`, and `K := Stab(q_ψ)`, so `K ∩ H = K_em` (Proposition 4.3). Let `D_L` be these data:
- `W = W_Q`, `σ = σ_Q`, `v = q_ψ`, normalization `c = k`;
- `Φ_X := L^{−3}Σ_{x∈X}𝒯_{π(x_X,x)}Q_x`, where `π(x_X, x)` runs from `x_X` to `x` first along `e_1`, then `e_2`, then `e_3`, inside `X`;
- `T_{XY} := 𝒯_{π(x_X,x_Y)}` along the straight path of `L` links between neighbouring block sites, and `T_{YX} = T_{XY}^†` along the reversed path.

For every `δ > 0` there are an even `L` and a `k` such that `ω` on `L5-O[R_k^-]` satisfies R-FMS(`K; D_L, δ`). So `ω` is a symmetric state, stationary for an update of the law, that satisfies EW_grp(δ), hence EW(δ). The triple `(W_Q, σ_Q, q_ψ)` does not depend on `δ`. The register `R_k^-` can depend on `δ`. This proves the statement across the family of laws, not Q-EW for one fixed register.

*Proof.* *Step 0: the data are admissible.* `Q_x` is carried at `x` (Proposition 4.3(1)). `𝒯_{π(x_X,x)}` is covariant on the left at `x_X`, on the right at `x`, and fixed at interior sites (§2.3). So `𝒯Q_x` is fixed at `x`, because `σ_Q(g)^{−1}σ_Q(g) = 1`, and covariant at `x_X`. Hence `Φ_X` is carried at `x_X`. It is even, because link operators and `Q_x` are even. Its entries are linearly independent, because the term `x = x_X` contributes `L^{−3}Q_{x_X}^i`, whose entries are independent operators on the matter of `x_X`, while every other term acts on the matter of another site. The support condition and translation covariance hold by construction. The reversed path uses the adjoints of the forward link factors in reverse path order, as in the corrected Definition 2.3. Hence its transport is exactly `𝒯^†`.

*Step 1: reduction to a product computation.* Let `F` be one of the finitely many operators in (O), (C), (A), (T) for one pair of neighbouring blocks. `F` is gauge invariant, and `E` fixes `𝔄^G`, so `ω(F) = Φ_prod(F)`. `F` is a finite sum `Σ_tf_tA_t ⊗ B_t`: `A_t` is a product of matter operators at sites of `X ∪ Y`, and `B_t` is a product over finitely many links of monomials in normalized entries. The number of terms, the coefficients and the degree `d_ℓ` on each link depend on `L` and on the fixed `p_j`, not on `k`. Matter and links are commuting tensor factors and `Φ_prod` is a product, so `Φ_prod(F) = Σ_tf_tρ_ψ^⊗(A_t)∏_ℓ⟨ψ_I, m_{t,ℓ}ψ_I⟩`. Let `F^{cl}` be the same sum with each link factor replaced by its classical value `∏δ`. By Lemma 5.1 and telescoping over links (all factors have modulus at most 1),
\[
|\omega(F)-F^{cl}|\le \sum_t|f_t|\,\|A_t\|\sum_\ell d_\ell^2/k =: C_F(L)/k .
\]

*Step 2: classical values.* Replacing every normalized entry `U^{ab}/k` by `δ_{ab}` turns `σ_Q(𝐔/k)` and its transpose into `1`. So `𝒯^{cl} = 1`, `T^{cl} = 1` and `Φ_X^{cl} = L^{−3}Σ_{x∈X}Q_x`. Under `ρ_ψ^⊗` the `Q_x` are independent with mean `q_ψ`. Put `Var := ρ_ψ(|Q_x − q_ψ|^2) ≤ ρ_ψ(|Q_x|^2) = 45·(1/4) + 210·1 = 885/4`, since `(M^{ab})^2 = 1/4` and `(Γ^{abcd})^2 = 1`. All entries have norm at most 1.
- (A): `F^{cl} = ρ_ψ^⊗(|L^{−3}(Σ_{x∈X}Q_x − Σ_{y∈Y}Q_y)|^2) = 2Var/L^3`, because the means cancel and distinct sites are independent with mean zero after centring.
- (T): `F^{cl} = ‖1·1 − 1‖^2_HS = 0`.
- (C): even operators at different sites commute, so `[Φ^i, Φ^j]^{cl} = L^{−6}Σ_{x∈X}C^{ij}_x` with `C^{ij}_x := [Q^i_x, Q^j_x]` and `‖C^{ij}_x‖ ≤ 2`. Independence gives `ρ_ψ^⊗(|Σ_xC_x|^2) ≤ L^3·4 + L^6|ρ_ψ(C)|^2 ≤ 8L^6`. The same holds with `Q^{j†}`. So `F^{cl} ≤ 2·255^2·8/L^6`.
- (O): write `Φ^{cl}_X = q_ψ + Δ` with `Δ := L^{−3}Σ_x(Q_x − q_ψ)`. Then `ρ_ψ^⊗(|Δ^i|^2) ≤ Var/L^3`, `‖Δ^i‖ ≤ 2`, and `‖[Δ^i, Δ^j]‖ = ‖[Φ^{cl,i}, Φ^{cl,j}]‖ ≤ L^{−6}·L^3·2 = 2/L^3`, since only same-site terms survive. The entries are self-adjoint, so `p_{j,sym}(q_ψ + Δ) − p_j(q_ψ)` is a finite sum of ordered products of constants and at least one factor `Δ^i`. Let `Ω` be the GNS vector of `ρ_ψ^⊗`. For one product `P = AΔ^iB`, with `B` a product of `b` factors `Δ`, `PΩ = ABΔ^iΩ + A[Δ^i, B]Ω`, so `‖PΩ‖ ≤ ‖A‖‖B‖(Var/L^3)^{1/2} + ‖A‖·b·2^{b−1}·2/L^3`. Summing over the products gives `F^{cl} ≤ C_{p_j}/L^3` for `L ≥ 1`, with `C_{p_j}` depending only on `p_j`.

*Step 3: choice of L and k.* `ω` is invariant under the translations `2Z^3 ⊇ LZ^3` (Lemma 5.2), so it suffices to check one block `X` and its six neighbours. Choose `L` even with every classical value at most `δ/2` (for (A), at most `δ|q_ψ|^2/2`; `q_ψ ≠ 0` by Proposition 4.3(5)). Then choose `k` with every `C_F(L)/k ≤ δ/2` (for (A), `≤ δ|q_ψ|^2/2`). Finitely many conditions remain, so both choices exist. Lemma 5.2 gives symmetry and stationarity, and Proposition 4.3(3) gives `K ∩ H = K_em`. □

**What Theorem 5.3 does not give.**
- *Dynamics.* Its stationarity is that of the identity update. `CH1_5OEP.md` records the same feature for its own construction ("inverse layers make stationarity vacuous"). Theorem 5.3 shows only that exact gauge invariance, cell symmetry and the registers do not block EW on `L5-O`. The own-tick question is EW1-O[U_0] (§7).
- *The full pattern.* `Lie(K) = su(4) ⊕ u(1)_5` has dimension 16. Besides `𝔨_em` it contains `u(1)_λ` and six real directions of `su(4)` that mix colour with the charged weak direction `e_4`. So the state realizes the electroweak step inside `H`, not EW⁺. By Proposition 4.4 no state built from identical even site states and adjoint link values reaches EW⁺.
- *The register.* Large `k` is not decoration (Lemma 5.4).

**Lemma 5.4 (one S_+ link never transports near orthogonally).** On `L5-O[S_+]`, for every state `ω` of one link and every `c > 0`, the vector-representation transport `T = 𝐔/c` has `ω(‖T^†T − 1‖^2_HS) ≥ 9`.

*Proof.* Frozen `GA2_Y2.md` Theorem 2.5: "\(U^{ab}=i\eta^y_a\eta^x_b\) gives \((\mathbf U^\dagger\mathbf U)^{ab}=N\eta^x_a\eta^x_b\)", with `N = 10`. So `(T^†T)^{aa} = 10/c^2`, and for `a ≠ b`, `(T^†T)^{ab} = (10/c^2)η^x_aη^x_b`, whose square modulus `(η_aη_b)^†(η_aη_b)` is 1. Hence `‖T^†T − 1‖^2_HS` is the scalar `10(s − 1)^2 + 90s^2` with `s = 10/c^2`. Its minimum over `s > 0` is 9, at `s = 1/10`. □

For vector-representation transport on `S_+`, no single link meets (T) for `δ < 9`, in any state. This bound does not apply to every R-FMS representation: in particular the vector representation is excluded by Theorem 4.1. This matches `GA2_Y2.md`'s coherence bound `κ ≤ 1/10` for `S_±` and its option (a1), the large-register free datum. Lemma 5.4 does not bound products of several `S_+` links.

---

## 6. L5-U: one-link bounds, a thin-transport no-go, and the empty sector

On `L5-U[m]` the register is fixed: `Λ^m(C^{10})`, of dimension at most 252. Write `K_m := min(m, 10 − m) + 1`; each end number `N^x_ℓ := p_{ℓ,x}` takes the `K_m` consecutive values `max(0, m−5), …, min(5, m)` (`GA2_Y2.md` Theorem 3.2).

**Lemma 6.1 (one link's fundamental transport).** For every state `ω` of one `L5-U` link, the `5 × 5` matrix `ω(𝐔) := (ω(U^{jk}))` has operator norm at most `1/2`.

*Proof.* For unit vectors `u, w ∈ C^5` put `X := Σ_{jk}ū_jU^{jk}w_k = r^y(u)r^{x†}(w)`, with `r^y(u) := Σ_jū_jr^y_j` and `r^{x†}(w) := Σ_kw_kr^{x†}_k`, a normalized annihilator and creator of two different modes. Then `X^2 = 0`, and `X^†X + XX^† = n^y_u(1 − n^x_w) + n^x_w(1 − n^y_u) ≤ 1`, the projection onto "exactly one of the two modes occupied". For square-zero `X`, `|ω(X)|^2 ≤ ω(X^†X + XX^†)/4` (`GA2_Y2.md` Theorem 3.4's proof). So `|u^†ω(𝐔)w| = |ω(X)| ≤ 1/2`. □ The Slater state of `GA2_Y2.md` Theorem 3.4 has singular values `1/2`, so the bound is attained.

**Lemma 6.2 (one link's adjoint transport).** For one `L5-U` link put `T_adj(X)_{ab} := Σ_{cd}U^{ac}X_{cd}(U^{bd})^†` for `X ∈ M_5(C)`. Let `(T^A)_{A=1}^{24}` be an orthonormal basis of the traceless Hermitian matrices (`tr T^AT^B = δ^{AB}`), and for `u ∈ U(5)` define the fidelity
\[
F_\omega(u):=\frac1{24}\sum_A\operatorname{Re}\,\omega\big(\langle uT^Au^\dagger,\,T_{adj}(T^A)\rangle_{HS}\big),\qquad \langle Y,Z\rangle_{HS}:=\sum_{ab}\bar Y_{ab}Z_{ab}.
\]
A classical link, `T_adj(X) = u_0Xu_0^†`, has `F(u_0) = 1`. On `L5-U[m]`, `F_ω(u) ≤ 3/10` for every state `ω` and every `u`. At `m = 5` the `SU(5)`-singlet vector with end numbers `(N^x, N^y) = (2, 3)` attains `F(1) = 3/10`.

*Proof.* For a matrix `Z` write `Ẑ_z := Σ_{cd}Z_{cd}r^{z†}_cr^z_d`, the one-body operator at end `z`. Since `(U^{bd})^† = r^x_dr^{y†}_b`, `T_adj(X)_{ab} = r^y_aX̂_xr^{y†}_b = X̂_xr^y_ar^{y†}_b`; the even `X̂_x` commutes with the `y`-end modes. For Hermitian traceless `Y`, `Ȳ_{ab} = Y_{ba}`, so
\[
\langle Y, T_{adj}(X)\rangle_{HS}=\hat X_x\sum_{ab}\bar Y_{ab}\big(\delta_{ab}-r^{y\dagger}_br^y_a\big)=-\hat X_x\hat Y_y .
\]
Hence `Σ_A⟨uT^Au^†, T_adj(T^A)⟩ = −Σ_AT̂^A_xŜ^A_y` with `S^A := uT^Au^†`, another orthonormal basis. By Cauchy–Schwarz twice,
\[
\Big|\sum_A\omega(\hat T^A_x\hat S^A_y)\Big|\le\sum_A\omega\big((\hat T^A_x)^2\big)^{1/2}\omega\big((\hat S^A_y)^2\big)^{1/2}\le\big(\omega(C_x)\,\omega(C_y)\big)^{1/2},
\]
where `C_z := Σ_A(T̂^A_z)^2 = Σ_A(Ŝ^A_z)^2` is the `su(5)` Casimir on the `z`-end space `⊕_pΛ^pC^5`. On `Λ^pC^5` it is the scalar `24·I(Λ^p)/C(5,p)`, where the index is `I(Λ^p) = C(3,p−1)`: for traceless diagonal `h`, `Σ_{|S|=p}(Σ_{i∈S}h_i)^2 = [C(4,p−1) − C(3,p−2)]Σ_ih_i^2 = C(3,p−1)Σ_ih_i^2`, using `2Σ_{i<j}h_ih_j = −Σ_ih_i^2`. This gives `0, 24/5, 36/5, 36/5, 24/5, 0` for `p = 0, …, 5`. So `F ≤ (36/5)/24 = 3/10`. For attainment: `Λ^2C^5 ⊗ Λ^3C^5` contains one `SU(5)` singlet `Ψ`. The total generators kill it, so `T̂^A_xΨ = −T̂^A_yΨ`, and `−Σ_Aω(T̂^A_xT̂^A_y) = ω(C_x) = 36/5`. □

[check] (`check_ufid.py`, `m = 5`): the identity `⟨Y, T_adj X⟩ = −X̂_xŶ_y` holds for random `X, Y`; the largest Casimir eigenvalue is `7.2`; 200 random states give fidelity at most `0.0101`; the singlet gives `0.3`.

So no state makes one `L5-U` link transport even an adjoint datum within fidelity `3/10` of a group element. In the construction of Theorem 5.3 each link is within `O(1/k)` of a group element; that mechanism is absent on `L5-U`.

**Lemma 6.3a (graded floor).** Let `E` be self-adjoint with spectrum in `K` consecutive integers, `q ∈ Z ∖ {0}`, and `Y` bounded with `[E, Y] = qY`. Then for every state `ω` and every `z ∈ C`,
\[
\omega\big((Y-z)^\dagger(Y-z)+(Y-z)(Y-z)^\dagger\big)\ge \frac{2|z|^2}{\lceil K/|q|\rceil^2}.
\]

*Proof.* Replace `E` by `−E` if `q < 0`. Let `P_r` project onto the eigenvalues of `E` congruent to `r` mod `q`. `Y` maps the `λ`-eigenspace into the `(λ+q)`-eigenspace, so `Y` and `Y^†` commute with every `P_r`, and so does the operator `A` inside `ω`. Hence `ω(A) = Σ_rω(P_rAP_r)`. On the range of `P_r`, `E_r := (E − λ_r)/q` (with `λ_r` the least eigenvalue in that class) has spectrum in at most `⌈K/q⌉` consecutive integers and `[E_r, P_rYP_r] = P_rYP_r`. Frozen `GA2_Y2.md` Theorem 3.2 states: "Let E be self-adjoint with spectrum in K consecutive integers and [E,Y]=Y. For every state and complex z, ω((Y−z)†(Y−z)+(Y−z)(Y−z)†)≥2|z|²/K²." Apply it to the normalized state `ω(P_r·P_r)/ω(P_r)` when `ω(P_r) > 0`, and sum: the total is at least `Σ_rω(P_r)·2|z|^2/⌈K/q⌉^2 = 2|z|^2/⌈K/q⌉^2`. □

**Theorem 6.3 (thin charged transport fails).** On `L5-U[m]`, let `D` be R-FMS data whose representation `σ` is irreducible with central charge `q ≠ 0`, that is `σ(e^{iθ}1_5) = e^{iqθ}`, and let `X, Y` be neighbouring blocks. Suppose a set `S` of `n` links meets no support of `Φ_X` or `Φ_Y`, and every path of `T_{XY}` crosses `S` exactly once, each link of `S` always in the same direction. Put `K_S := n(K_m − 1) + 1` and `c_Φ := max(‖|Φ_X|^2‖, ‖|Φ_Y|^2‖)^{1/2}`. If `ω` satisfies (O) and (A) for `(X,Y)` and `(Y,X)` with tolerance `δ`, then
\[
\delta\ \ge\ \frac{|v|^4}{(1+c_\Phi|v|)^2\,\lceil K_S/|q|\rceil^2}.
\]

*Proof.* Let `Ω` be the GNS vector of `ω`, so `ω(B^†B) = ‖BΩ‖^2`. Put `Y_{XY} := Σ_iΦ_X^{i†}(T_{XY}Φ_Y)^i`, a gauge-invariant operator.

*Upper bound.* With `ξ := Φ_X − T_{XY}Φ_Y`, `Y_{XY} = |Φ_X|^2 − Σ_iΦ_X^{i†}ξ^i`. The row map `(ψ_i) ↦ Σ_iΦ_X^{i†}ψ_i` is the adjoint of `ψ ↦ (Φ_X^iψ)_i`, whose norm is `‖Σ_iΦ_X^{i†}Φ_X^i‖^{1/2} = ‖|Φ_X|^2‖^{1/2} ≤ c_Φ`. So `‖(Y_{XY} − |v|^2)Ω‖ ≤ ‖(|Φ_X|^2 − |v|^2)Ω‖ + c_Φ(Σ_i‖ξ^iΩ‖^2)^{1/2} ≤ √δ + c_Φ|v|√δ`, using (O) with `p_1 = |·|^2` and (A). Also `Y_{XY}^† = Σ_jΦ_Y^{j†}(T_{XY}^†Φ_X)^j = |Φ_Y|^2 − Σ_jΦ_Y^{j†}ξ′^j` with `ξ′ := Φ_Y − T_{YX}Φ_X`, since `T_{YX} = T_{XY}^†`. The same estimate, with (A) for `(Y,X)`, gives `‖(Y^†_{XY} − |v|^2)Ω‖ ≤ √δ(1 + c_Φ|v|)`. So with `Y′ := Y_{XY}/|v|^2`,
\[
D:=\omega\big((Y'-1)^\dagger(Y'-1)+(Y'-1)(Y'-1)^\dagger\big)\le\frac{2\delta(1+c_\Phi|v|)^2}{|v|^4}.
\]

*Lower bound.* Let `ε_ℓ = +1` if the paths traverse `ℓ ∈ S` from source to target and `−1` otherwise, and put `E_S := Σ_{ℓ∈S}ε_ℓN^x_ℓ`. Each `U^{jk} = r^y_jr^{x†}_k` raises `N^x_ℓ` by one and its adjoint lowers it. An entry of `σ(𝐔)` with `σ ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` has `p` factors `U` and `p′` factors `U^†`, and `p − p′ = q`. So `[E_S, 𝒯_π] = q𝒯_π` for every path that crosses `S` once in the stated directions; links of different registers commute with `N^x_ℓ`. Hence `[E_S, T_{XY}] = qT_{XY}` entrywise. `E_S` commutes with `Φ_X` and `Φ_Y` (disjoint supports), so `[E_S, Y_{XY}] = qY_{XY}`. `E_S` has integer spectrum in `K_S` consecutive values. Lemma 6.3a with `z = 1` gives `D ≥ 2/⌈K_S/|q|⌉^2`. Combine the two bounds. □

*Examples.* The natural charged datum on `L5-U` is the `Λ^4C^5` matter multiplet at one site (products of four creators, `q = 4`). By the computation of Proposition 4.3(3), its vector `e_{1234}` has stabilizer `{diag(A, λ) : A ∈ U(4), det A = 1}`, which meets `H` in `K_em`. At `m = 5` (`K_5 = 6`) a single path (`n = 1`) gives `⌈6/4⌉ = 2` and `δ ≥ |v|^4/(4(1 + c_Φ|v|)^2)`. A cut of `n` links gives a floor of order `q^2/(n^2K_m^2)`, which decays with the block face. Theorem 6.3 gives a positive floor for fixed cut size and a uniform bound on `c_Φ`. If `c_Φ` grows as `δ` changes, the displayed inequality alone does not rule out arbitrarily small `δ`. The floor weakens as the cut grows.

**Lemma 6.4 (sharp matter, and the empty sector).** On `L5-U[m]`:
1. If `τ_E = 0`, every state `ω` with `ω(N_x) = 0` for all `x` is stationary under the base tick `U_0`.
2. For any `τ_E`, the same holds if moreover `ω` is invariant under `Ad e^{iθp_{ℓ,x}}` for every end and every `θ`.
3. Let `ω` be any state in which the matter number of each block, `N_X := Σ_{x∈X}N_x`, is sharp, and let `ω` satisfy (O) and (A) with tolerance `δ`. Let `v_r` be the components of `v` in the summands `σ_r` of nonzero central charge `q_r`, and `s` their number. Then `Σ_{r: q_r≠0}|v_r|^2 ≤ s√δ + δ|v|^2`. Hence if `(W, σ, v)` is fixed and such states exist for every `δ > 0`, then `v_r = 0` whenever `q_r ≠ 0`, and the central `U(1)` of `U(5)` fixes `v`.

*Proof.* (1) Frozen `VC1_5.md` Proposition R2, step (1): "Each hop term has a matter annihilator on its right, so every cube generator kills every vector with empty matter on its cube, and each cube gate acts as the identity there." On a finite region, `ω(N_x) = 0` with `N_x ≥ 0` puts the density matrix `ρ` on the empty-matter subspace `𝒦`. Each cube gate `G` acts as the identity on `𝒦`, so `GρG^† = ρ` and `ω(G^†AG) = ω(A)`. `W_E = 1` at `τ_E = 0`. On every local observable the tick acts through finitely many such gates (the finite-support form that `LW1_5.md` §2 and `CH1_5O.md` R5.1 cite from `LW1.md` E1). (2) `W_E` is a function of the end numbers, and invariance under the `U(1)` they generate makes `ω` block diagonal in each `p_{ℓ,x}`, hence invariant under any unitary function of them.

(3) `σ(𝐔)` is block diagonal over the fixed summands (§2.3), so `T_{XY} = ⊕_rT_r` and `|Φ_X − T_{XY}Φ_Y|^2 = Σ_r|Φ_{X,r} − T_rΦ_{Y,r}|^2`. Take a summand with `q_r ≠ 0`. Frozen `LW1_5.md` Z-U: "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change". Each entry of `Φ_{X,r}` is carried at `x_X` with charge `q_r`, so it changes the total matter number by `q_r`; its support lies in `X`, so `[N_X, Φ^i_{X,r}] = q_rΦ^i_{X,r}` and `[N_Y, Φ^i_{X,r}] = 0`. The same holds for `Φ_{Y,r}`. `T_r` contains link operators only, so it commutes with every `N_x`. Put `A := Φ^{i†}_{X,r}T_r^{ij}Φ^j_{Y,r}`. Then `[N_X, A] = −q_rA`. In a state where `N_X` is sharp, `ω(A) = ω(P_0AP_0) = 0`, with `P_0` the spectral projection at the sharp value, because `P_0AP_0 = 0` for `q_r ≠ 0`. So the cross term vanishes, and `ω(|Φ_{X,r} − T_rΦ_{Y,r}|^2) ≥ ω(|Φ_{X,r}|^2) ≥ |v_r|^2 − √δ`, by (O) for the invariant `|w_r|^2`. Summing over the charged summands and using (A) gives `Σ_{r: q_r≠0}(|v_r|^2 − √δ) ≤ δ|v|^2`. If this holds for every `δ > 0` with `v` fixed, every charged `v_r` vanishes. The centre acts on each summand by `e^{iq_rθ}`, so it then fixes `v`. □

Lemma 6.4(1) is a degenerate feature of the base law. Without a plaquette class (open as GA1-P-5) and at `τ_E = 0`, links move only through matter hops, so in the empty sector every link state is frozen.

**Proposition 6.5 (neutral data on L5-U).** Take the standard ratio.
1. If `K ⊇ K_em` and `K` contains the central `U(1)` of `U(5)`, then `K ∩ H ⊇ K_em·Z_5 ⊋ K_em`, where `Z_5 = {e^{2πin/5}1_5}` is the centre of `SU(5)`. So for a fixed triple realized in states with sharp block matter numbers for every `δ`, EW_grp and EW⁺ fail.
2. EW at the Lie-algebra level is not excluded by neutral data: the vector `w_n := e_{1234} ⊗ (e_5^*)^{⊗4} ∈ Λ^4C^5 ⊗ (C^{5*})^{⊗4}` has central charge 0, and its stabilizer `K_n` satisfies `Lie(K_n) ∩ 𝔥 = 𝔨_em`. It occurs in the product of four rishon-end bilinears `r^{ℓ_i,x†}_ar^{ℓ_i,x}_b` at one site from four different links.

*Proof.* (1) `e^{2πi/5}1_5 = (e^{2πi/5}1_3) ⊕ (e^{2πi/5}1_2)` has determinant `e^{6πi/5}·e^{4πi/5} = 1`. For the standard ratio `π(H) = S(U(3) × U(2))`, so this element lies in `H`. It acts on `e_5` by `e^{2πi/5} ≠ 1`, so it is not in `K_em = Stab_H(e_5)`. Lemma 6.4(3) puts the central `U(1)` in `K` for a fixed triple realized in sharp-matter states for every `δ`.

(2) `u ∈ U(5)` sends `w_n` to `((ue_1)∧⋯∧(ue_4)) ⊗ ((u^{−1})^Te_5^*)^{⊗4}`. This equals `w_n` only if `u` preserves `span(e_1, …, e_4)` (the 4-plane of the first factor, which is also the kernel of `e_5^*`), hence also `Ce_5`. For `u = diag(A, λ)` with `A ∈ U(4)` on that 4-plane, `u·w_n = det(A)λ^{−4}w_n`. So `Stab(w_n) = {diag(A, λ) : det A = λ^4}`, which contains the central `U(1)` (`A = t1_4`, `λ = t`). Its Lie algebra is `{i·diag(X_4, z) : tr X_4 = 4z}`. Every element of `𝔥` in it is block diagonal for `C^3 ⊕ Ce_4 ⊕ Ce_5`, of the form `i·diag(X_3, y, z)` with `tr X_3 + y + z = 0` (`𝔥 ⊂ su(5)`). The condition `tr X_3 + y = 4z` then forces `5z = 0`, so `z = 0` and `y = −tr X_3`; these elements form `𝔨_em`. Each end bilinear `r^{ℓ,x†}_ar^{ℓ,x}_b` is `gl(5)`-valued at `x` and invariant under the group of the far end of `ℓ`; a product of four from different links is carried at `x` in `gl(5)^{⊗4} = (C^5 ⊗ C^{5*})^{⊗4}`, which contains `w_n` after antisymmetrizing the four `C^5` slots. □

So, for a fixed triple, the base-tick-stationary empty sector of `L5-U` (Lemma 6.4(1)) can carry at most EW, never EW_grp or EW⁺. For the stronger group-level target and a fixed triple, sharp block matter numbers are excluded in the every-δ limit. The Lie-level EW target can use neutral data; the bounds do not establish that charged data or fluctuating matter are necessary for EW.

### 6.6 The open lemma on L5-U

**EW1-U (open).** Take the standard ratio. Are there `m ∈ {1, …, 9}` and a fixed triple `(W, σ, v)` with `Lie(Stab v) ∩ 𝔥 = 𝔨_em` such that for every `δ > 0` some symmetric state `ω` of `L5-U[m]` and some R-FMS data `D` with this triple satisfy R-FMS(`Stab v; D, δ`)?

*Why stationarity is dropped.* If a solution has empty matter and link-only composites, it is stationary under the base tick at `τ_E = 0` by Lemma 6.4(1). For other solutions, `CH1_5OEP.md` Theorem 3 notes that "the same cancellation proof applies if its tick and added inverse layers satisfy the same local gate and class hypotheses". So EW1-U is the kinematic core of Q-EW on `L5-U`.

**Attack A1: copy Theorem 5.3.** Take a product state over sites and links with each link near a group element, block-average one-site data, and gauge-average. *Failing step: "one L5-U link can be prepared with transport near a group element".* This is false in every state: Lemma 6.1 bounds the fundamental transport by `1/2` and Lemma 6.2 bounds adjoint fidelity by `3/10`. For fundamental-type transport, independent product links give an expectation norm at most `2^{−N}` over `N` links. Theorem 6.3 gives a floor only under its stated cut and norm hypotheses.

**Attack A2: refute EW1-U by floors.** Theorem 6.3 and Lemma 6.4(3) are such floors. *Failing step: "every R-FMS alignment operator raises a bounded grading through a bounded cut".* It is false. A neutral datum such as `w_n` (Proposition 6.5) is transported by `U(1)`-blind products, which commute with every end number, so Lemma 6.3a has nothing to act on. For charged data the floor decays like `n^{−2}` with the cut size `n`, so it excludes nothing at large block scale. This is the same stopping point as `GA2_Y2.md`'s Attack 1 on Y2-W.

**Attack A3: collective transport in a correlated state.** Look for an entangled link state whose block transporters are collective variables that are nearly orthogonal, as the emergent `U(1)` structure of a `S = 1/2` magnet (L11). *Failing step: "such a state of L5-U is exhibited".* No state is exhibited here. The flux states of `GA2_Y2.md` Theorems 4.3-4.4 make `U(1)`-blind cube products sharp, but they have definite end numbers on every link, so every flux-raising link operator has zero expectation in them, and their sharp eigenvalues are loop data, not near-orthogonal transport. L11 concerns a different model and proves nothing about `L5-U`.

EW1-U stays open. Its negation would not eliminate `L5-U`: it would say that FMS-form electroweak breaking needs a coarse-graining that `L5-U` does not supply at any block scale. That is the question Y2-W asks for the gauge sector (`GA2_Y2.md`).

---

## 7. L5-O under its own tick

**Remark 7.1 (FMS transport is even on every link).** On `L5-O`, Theorem 4.1 gives `σ(ϖ) = 1` for every R-FMS datum. `ϖ` maps to `−I`, which acts on `V^{⊗p}` by `(−1)^p`. So every summand `σ_r ⊆ V^{⊗p_r}` used by a transporter has `p_r` even, and every R-FMS transporter has even degree in the entries of each link. The vanishing argument of frozen `CH1_5OEP.md` Theorem 6 ("The target-end `ϖ` commutes with `h` and conjugates `U^{ab}` to `−U^{ab}`") multiplies a link factor of degree `p` by `(−1)^p`. So it never reaches R-FMS transport on `L5-O`. On `L5-U` the corresponding phase is `e^{−iq_rθ}` (`CH1_5OEP.md` R-U), which reaches charged transport only; this matches Lemma 6.4(3).

**Lemma 7.2 (the tracial state carries no FMS breaking; both laws).** Let `τ` be the tracial state (`VC1_5.md` Theorem 3.2; it is symmetric and stationary for every update). Let `D` be R-FMS data whose transporters use paths with distinct links. Suppose each path contains a link `ℓ` outside the supports of `Φ_X` and `Φ_Y`, such that the part of the path before `ℓ` avoids the support of `Φ_Y` and the part after `ℓ` avoids the support of `Φ_X`. (Straight paths between block sites, cut at the link that crosses the block face, qualify.) Let `v_r` be the components of `v` in the nontrivial summands `σ_r`, and `s` their number. If `τ` satisfies (O) and (A) with tolerance `δ`, then `Σ_r|v_r|^2 ≤ s√δ + δ|v|^2`. So a fixed triple realized in `τ` for every `δ > 0` has `v ∈ W^G` and `Stab(v) = G`.

*Proof.* Write a path transport as `𝒯_π = A_πσ(𝐔_ℓ^{(ε)}/c)B_π`, with `ℓ` the chosen link. `A_π` and `B_π` use the other links of the path, which are distinct from `ℓ`. All factors are even. `τ` is the product of the normalized traces of the sites and links, so for even operators supported on disjoint sets of tensor factors it factorizes. Hence for a nontrivial summand `σ_r`, `τ(Φ^{i†}_{X,r}(𝒯_{π})^{ij}_rΦ^j_{Y,r}) = Σ_{kl}τ(Φ^{i†}_{X,r}A^{ik}_{π,r})·M^{kl}·τ(B^{lj}_{π,r}Φ^j_{Y,r})` with `M := τ(σ_r(𝐔_ℓ^{(ε)}/c))`. `τ` is invariant under the local gauge automorphism at the end `z` of `ℓ` that acts on rows, and that automorphism acts on `σ_r(𝐔_ℓ)` alone by `σ_r(g)` on the left. So `M = σ_r(g)M` for every `g`, and every column of `M` lies in `W_r^G = 0`. So the cross term of (A) vanishes on every nontrivial summand, for every path and hence for the convex combination. As in Lemma 6.4(3), `τ(|Φ_{X,r} − T_rΦ_{Y,r}|^2) ≥ |v_r|^2 − √δ` for each such `r`, and summing against (A) gives the bound. □

**EW1-O[U_0] (open).** Take the standard ratio. Are there an irreducible register `R` and a fixed triple `(W, σ, v)` with `Lie(Stab v) ∩ 𝔥 = 𝔨_em` such that for every `δ > 0` some symmetric state of `L5-O[R]`, stationary under the own tick `U_0` (with `τ_E = 0` unless `R = S_+`), and some data `D` with this triple satisfy R-FMS(`Stab v; D, δ`)?

Theorem 5.3 gives witnesses with inverse layers and a register that may grow with the requested accuracy. EW1-O[U_0] fixes one register and removes those layers. It is the electroweak analogue of `CH1_5OEP.md`'s CH1-5O-E′[VC1], with the VC1 vacuum replaced by "some own-tick stationary state".

**Attack A1: the known own-tick witnesses.** The stationary symmetric states on file are the trace `τ` and the dark witnesses `ω_0, ω_F` (`VC1_5.md` Theorems 4.1-4.2; frozen `CH1_5O.md` R5.1: for every `L5-O[S_+]` update, "Φ₀ and ω₀ are stationary"). *Failing step: "a known own-tick witness carries electroweak FMS data".* For `τ` it is false (Lemma 7.2). For `ω_0` and `ω_F` it is not decided. Their product lift is invariant under the local group `π^{−1}(U(5))` at every site (`CH1_5O.md` R6 for `Φ_0`; for the lift of `ω_F` the full Fock vectors are likewise fixed up to phase by `U(5)`), and that group contains `H`. So in the lift every covariant object at a site has a `U(5)`-fixed expectation vector, and transport through any link passes only `U(5)`-invariant vectors. Neither fact decides (O) or (A), because the gauge-invariant data do not require a lift to be sharp on the orbit. They also live on `S_+`, where vector transport on one link fails (T) (Lemma 5.4). That is not a bound on their admissible even-representation FMS transport. Products of several `S_+` links are not bounded here.

**Attack A2: time-average the witness of Theorem 5.3.** `L5-O[R_k^-]` has the state `ω` of Theorem 5.3. Its Cesàro averages under `U_0` have stationary, gauge-invariant, cell-symmetric weak-* limit points (`LW1_5.md` E2b-5: "Cesàro means of a cell-translation invariant, locally gauge-invariant state have stationary, cell-translation and gauge-invariant weak-* limit points"). *Failing step: "time averaging preserves (O), (A) and (T)".* No bound on the drift is available. The Majorana hop moves `ρ_ψ` at the first tick: on empty matter it creates pairs through `4i d^y_kd^x_j` (`VC1_5.md` Theorem 4.2's proof), and its number-conserving part spreads the four-fermion coherence of `ψ` over neighbouring sites. Whether the limit keeps any FMS order is a question about the law's heating.

**Attack A3: refute EW1-O[U_0] through HEAT.** `CH1_5OEP.md` C4 states HEAT: every stationary, gauge-invariant, cell-symmetric state of the law's own tick has the finite-region Gauss-trace form. With HEAT one might hope to kill alignment as Theorem 6 there kills loops. *Failing steps.* HEAT is open. And even with HEAT, Theorem 6's argument multiplies each link factor by `(−1)^{degree}`, which is `+1` for every R-FMS transporter on `L5-O` (Remark 7.1). Lemma 7.2 covers only the trace itself, `Z_Λ = 1`; a general Gauss-trace form is not a product across a cut link.

EW1-O[U_0] stays open. Its answer bears on VC1 and on HEAT, not on Theorem 5.3, which remains an unrefereed varying-register construction in the update class.

---


## 8. Distiller corrections and reading checks

1. **Reverse-order counterexample and correction.** On an L5-U link take the trivial summand of `V⊗V̄`, projected onto the normalized invariant vector. With the draft’s fixed ordering, its forward factor is `N_x(5−N_y)/5`. Same-order evaluation at `𝐔†` is `N_y(5−N_x)/5`, while the adjoint of the forward factor is itself. In the `m=1` sector with `(N_x,N_y)=(1,0)` these are `1` and `0`. Hence the draft’s assertion that same-order reverse evaluation always equals the adjoint fails. Definition 2.3 uses adjoints for reverse factors. This preserves covariance and makes reversal exact. The construction and all later bounds use this corrected convention.
2. **Fixed-register quantifiers.** The draft's conclusion “Q-EW holds” omits whether the law and register remain fixed. The proof establishes `∀δ ∃L,k,ω,D`; it does not establish `∃k ∀δ ∃L,ω,D`. The latter remains open even with inverse layers. The construction does prove the varying-register claim in Theorem 5.3.
3. **The S₊ conclusion.** Lemma 5.4 proves its displayed vector-representation bound. It does not prove that no one-link transporter in any admissible R-FMS representation meets (T). Theorem 4.1 itself excludes the vector from admissible bosonic data. Thus the S₊ attacks in §7 cannot use that bound as an FMS obstruction.
4. **Thin cut.** Theorem 6.3's estimate is valid with its actual `c_Φ`, but to infer a nonzero floor uniformly across a family as `δ→0`, require a common upper bound on `c_Φ`. The fixed orbit point alone does not bound operator norms.
5. **Neutral data.** Proposition 6.5 concerns a representation vector and its stabilizer; it does not construct an R-FMS state. It does show that the group-theoretic Lie-level target does not itself force charged data. Sharp-matter exclusion applies to the stronger group-level target with fixed triple and arbitrarily small tolerance, not to EW alone.
6. **Proposed-reading checks.** R-VEV: test 3 fails; R-A and R-L: rejected in the cited source; R-ST: test 3 fails according to the draft's interpretation, subject to its unchecked literature context; R-SPEC: test 1 fails. R-FMS: draft assesses tests 1–4 as passing with data pinned. EW and EW_grp are proposed instances; EW⁺ and the fixed orbit point are proposed, with tests assessed as passing. These assessments are judgments, not independent evidence that the diagnostic implies a Higgs spectrum.

The draft's [check] reports are preserved above as historical reports. They were not reproduced. No calculation here establishes a vacuum selection, massive weak bosons, a massless photon, a Higgs scalar, or a weak scale.
