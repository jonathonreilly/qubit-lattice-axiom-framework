# SMG1: symmetric mass generation, outline and rung 1

**Status.** The Hamming-code atom, the translation-protected quadratic obstruction, the zero-hop product ground state and generator gap, the restricted eight-Majorana minimum, and the absence of an intrinsic Floquet gap are proved below for the stated models. The open-segment hopping result is conditional on the cited Fröhlich–Pizzo theorem; its precise hypotheses have not been independently checked here. Gauging the finite group gives the stated local construction, subject to that same stability dependency. These are author-side results, not a referee or audit verdict.

**GAPs.** W2.4 has incompatible quantifiers; the proposed scaling target needs repair. The identification of the fourteen signed terms with the published FK expression is not independently established here. The draft's general statements about a tick's spectral gap and its example for decomposition dependence overreach. The rung-1 generator is not generally the tick Hamiltonian, and its hopping ground state is not shown stationary. R1.5's asserted form of all mixing terms is too restrictive. Details and corrections appear below.

**Open.** R1-H, FLQ, R0-U5, R1.5-D, R2, R3-H, R3-D and W2; owner questions Q1 and Q2. No reading below is adopted.

**Provenance.** Pass 2 distils `SMG1_OUTLINE.md`, pass 1 by Claude Opus 5.5, max. Distiller: gpt-6.1-terra; effort and session id: see run log. Source identities and pass-1 literature coverage are recorded in the outline. This pass did not run git, reproduce the draft's scratch scripts, or independently inspect all historical sources. `prior/SMG1.md` is a retrieval digest, not proof of a source's current status.

## 1. Definitions inferred by the distiller

These are mathematical readings of the draft, not additions to the axioms.

1. A site has `F_x = Λ C⁵`, Majoranas `γ_{x,1},…,γ_{x,10}` with `{γ_{x,a},γ_{y,b}}=2δ_{xy}δ_{ab}`, and parity `P_x`. Links are finite-dimensional ordinary tensor factors. `𝔄` is the quasi-local graded CAR-and-link algebra. A one-dimensional carrier is `Z`, a finite segment, or a ring; the cell translations are by two sites. For a hopping-layer decomposition on a ring take even length.
2. NN-a means a fixed finite product of layers of even unitaries on disjoint nearest-neighbour edge triples. A site-only or link-only gate may be embedded in a triple. The whole tick preserves local gauge transformations and the specified cell action. Write its certified gates as `exp(−iX_g)`, with `X_g` Hermitian and `‖X_g‖<π`.
3. **Proposed R-GEN.** For the specified decomposition set `H_U=Σ_g X_g` formally, with derivation `iΣ_g[X_g,A]` on local `A`. A ground state satisfies `ω(A*[H_U,A])≥0` for all local `A`. A unique gapped ground state has GNS generator with kernel `CΩ` and spectrum in `{0}∪[Δ,∞)`. This is a property of the supplied decomposition; it does not imply stationarity under the tick. The latter is separately required when claimed.
4. An on-site symmetry is a compact `G` acting by even site unitaries, together with its specified link action, commuting with the tick and compatible with cell lifts. The proposed W2 requires an injection of `G_SM=(SU(3)×SU(2)×U(1))/Z₆` into `G`. A proposed vacuum is pure, tick-stationary, `G`- and cell-invariant, and a ground state in R-GEN.
5. Proposed light fields are odd quasi-local `ψ_{A,s}`, `A=1,…,16`, `s=1,2`, transforming in a unitary `G` representation `D` whose restriction is one Standard Model generation including `ν^c`. When local gauge invariants are all matter-even, a charged-sector prescription is a separate input; the fields cannot simply be elements of the invariant algebra. `RCS1.md`, Theorem 4, proves the evenness for the stated live laws.
6. **Proposed R-LIGHT.** For cell translation `τ_y`, choose a nearest `y=[λx]∈2Z³` and define `ψ^λ(x,t)=λ^{3/2}α^{⌊λt⌋}(τ_[λx]ψ)`. The reference two-point distribution is `S_c(x,t)=∫d³p/(2π)³ (1−p̂·σ)/2 exp(i(p·x−c|p|t))`. Ties in the nearest-cell choice require a fixed convention. Distributional limits require smearing in space and time.
7. The target W2 asks for the above data on `Z³`, with (W2.1) `Sym²(D)^G=0`; (W2.2) a pure symmetric state; (W2.3) the rescaled two-point function `Z δ_AB S_c`, `Z,c>0`; and (W2.4) no further light fields, expressed in the draft by convergence of connected correlations of **every** finite family under **every** choice of rescaling powers to free-field Wick-polynomial correlations. W2[fin] relaxes five modes to arbitrary finite site content. W2[L5-U] and W2[L5-O] specify the respective frozen laws and their gauge groups. Gauging `G`, massless gauge fields, reflection positivity, three families, symmetry breaking, a common cone for other species, and identification with ZM1-INV are separate interfaces.

**GAP W2.4.** The universal powers are inconsistent with W2.3: choose the two fields of W2.3 and increase each scaling power by one. Their nonzero distributional limit is multiplied by `λ²` and cannot converge as a finite distribution. The draft's reading test says powers are existential, contrary to the target's universal wording. A corrected target must specify admissible fields, normalization and which powers are quantified, and prove that its criterion excludes extra light sectors. That repair is open. Nor does an oscillating π contribution automatically fail distributional convergence: rapid oscillations can converge weakly to zero. The draft's exclusion of π modes therefore also needs a separate observable or convergence condition.

(W2.1) indeed excludes `G=G_SM` for this representation: `ν^c` is a singlet and its symmetric square is invariant. The implications from free no-go results remain conditional on their exact hypotheses; they do not prove W2 or exclude all interacting constructions. See `CH1.md` F1–F3 and `CG16S.md` RC-W and condition E.

## 2. Construction and atomic algebra

Let `c_a=γ_{x,a}` for `1≤a≤8` on one site. Put

`g₁=−c₁c₂c₃c₄`, `g₂=−c₅c₆c₇c₈`, `g₃=−c₁c₂c₅c₆`, `g₄=−c₁c₃c₅c₇`,

`S=⟨g₁,g₂,g₃,g₄⟩`, and `W=−Σ_{g∈S, deg g=4}g`. The global `S` action is the product of the site adjoint actions, fixing mode 5 and the links. On a chain use link qubits `X_ℓ,Z_ℓ`, Gauss operators `G_x=P_x∏_{ℓ∋x}X_ℓ`, and the terms

`h_x=τ(W_x+14)+τ₅n_{x,5}`, `e_ℓ=τ_E(1−X_ℓ)/2`, `b_(x,x+1)=(i/2)Σ_{a=1}⁸γ_{x,a}Z_ℓγ_{x+1,a}`.

Take positive `τ,τ₅,τ_E`, `16τ+τ₅<π`, `τ_E<π`, `4|θ|<π`. The tick is `U=L₄L₃L₂L₁`: on-site gates, link electric gates, even-bond hop gates, odd-bond hop gates, respectively. Its R-GEN sum is `H(θ)=Σ_x h_x+Σ_ℓe_ℓ+θΣ_ℓb_ℓ`. Set `H₀=H(0)` and `Δ₀=min(14τ,τ₅,τ_E)`.

**Lemma 2.1 (code).** The four generators commute and generate `S≅(Z₂)⁴`, without `−1`. Their supports form the self-dual binary code `C` generated by `11110000, 00001111, 11001100, 10101010`. Its weight enumerator is `1+14z⁴+z⁸`. Further, `g₁g₂=c₁⋯c₈=P^(4)` and `g c_a g⁻¹=(−1)^{u_a}c_a` for the support `u` of `g`.

*Proof.* For ordered products `c_u`, `c_u²=(−1)^{|u|(|u|−1)/2}` and `c_uc_v=(−1)^{|u||v|−|u∩v|}c_vc_u`. The generators are involutions with pairwise even overlap. Their supports are independent, so no nonempty product has empty support. All sixteen codewords have weights 0, 4, or 8, with the stated counts. Even overlap gives `C⊂C⊥`; both have dimension four. For four modes, `P^(4)=∏_j(−ic_{2j−1}c_{2j})=c₁⋯c₈`. The conjugation formula follows from the same Clifford signs. \(\square\)

**Theorem 2.2 (atom).** On `V=Λ C⁴`, the sixteen `S`-characters each occur once. `W` has spectrum `−14` once, `0` eight times in odd parity, and `2` seven times in even parity. Its unique ground vector `ψ` is `S`-fixed and even; the eight vectors `c_aψ` form an orthonormal basis of the odd sector. No nonzero quadratic in `c₁,…,c₈` is `S`-invariant.

*Proof.* Every nonidentity element of `S` is traceless: conjugate its even, nonempty Majorana monomial by one Majorana in its support. Character projection `P_χ=|S|⁻¹Σ_gχ(g)g` therefore has trace one. On its range, `W=−16[χ=1]+1+χ(P^(4))`, yielding the spectrum and parities. The characters `ρ_a(g)=(−1)^{u_a}` are distinct, since equality for `a≠b` would put the weight-two word `e_a+e_b` in `C⊥=C`. Each `c_aψ` lies in a different odd character line. A quadratic `ic_ac_b` is invariant only if the same weight-two word lies in `C⊥`, which is impossible. \(\square\)

The atomic spectrum was already reported in the repository's #10078 precursor, recorded at `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`, entry #10078; that source is identified by `prior/SMG1.md` but was not present at that path in this working folder. Its reported chain tests are finite-size evidence, not a uniform-gap proof. The 32-mode Spin(10) atom is already reported in `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`, conditional-support and unaudited according to the digest.

**GAP FK identification.** The draft checks three signed terms by hand and reports a scratch check of all fourteen against [Fidkowski–Kitaev](https://arxiv.org/abs/0904.2197), Eq. (8). The scratch files are not available here and the equation was not checked term by term in this pass. Thus Theorem 2.2 proves the explicitly defined `W` and its FK-type spectrum; exact equality to that printed expression remains to be checked. This does not affect the proof of the spectrum.

## 3. Quadratic obstruction and minimality

**Theorem 3.1.** On a ring `Z_L`, `L≥2`, let `Q=(i/4)Σ A_{xα,yβ}γ_{x,α}γ_{y,β}+const`, with real antisymmetric `A`, be invariant under global `S` and one-site translation. Then `A_{xa,yβ}=0` for `a≤8`, `β≠a`; each eigenspace of `Q` has dimension divisible by 16. On `Z`, for finite-range translation-invariant `A`, every one of these eight flavour symbols has zeros at `k=0,π`.

*Proof.* Each quadratic transforms by `ρ_αρ_β`, with `ρ_9=ρ_10=1`. The eight `ρ_a` are distinct and nontrivial, so only equal flavours survive among terms involving them. Translation invariance and antisymmetry make each row sum of the flavour matrix zero. Consequently `Γ^a=Σ_xγ_{x,a}` commutes with `Q` and `{Γ^a,Γ^b}=2Lδ_ab`. The eight normalized operators generate `Cl₈(C)≅M₁₆(C)`, so each invariant eigenspace is a sum of 16-dimensional modules. For the infinite chain, the symbol of `iA` is `−2Σ_{r>0}A_{0a,ra}sin(kr)`, proving both zeros. \(\square\)

The symmetry alone does not forbid same-flavour intersite bilinears. One-site translation is essential: a dimerized alternating nearest-neighbour hop is `S`-invariant and gaps that flavour. Translation of the **generator** is the hypothesis; the two ordered hopping layers need not give a one-site-translation-invariant tick.

**Theorem 3.2 (restricted minimum).** For `ν=2n>0` Majoranas, let `U⊂F₂^ν` consist of even words and act by the corresponding sign flips. If it forbids all nonzero quadratic operators and an invariant Hermitian operator has a unique ground vector, then `ν≥8`. The construction of Theorem 2.2 attains eight.

*Proof.* A unique ground vector is a common eigenvector of all implementers. Anticommuting implementers cannot share such a vector; hence `U⊂U⊥` and `k=dim U≤ν/2`. The coordinate functionals `s_a∈U*` are distinct, otherwise the corresponding quadratic is invariant. Self-orthogonality says `Σ_a s_as_aᵀ=0`. For `ν=2` the distinct functionals fill `F₂`, whose sum has nonzero diagonal. For `ν=4` they fill `F₂²`, whose sum has nonzero off-diagonal. For `ν=6` they are six of `F₂³`; the sum over all eight is zero, while the two omitted distinct vectors `v,w` have `vvᵀ+wwᵀ` with nonzero diagonal `v+w`. All cases contradict self-orthogonality. \(\square\)

This is a statement about even-word sign flips and a unique vector, not the full FK `Z₈` classification.

## 4. Product tick and Floquet spectrum

**Theorem 4.1.** At `θ=0`, on a finite segment or ring, `U=e^(−iH₀)` and `H₀` has unique ground vector `Ψ=⊗_x(ψ_x⊗|0⟩_{5,x})⊗⊗_ℓ|+⟩_ℓ`, with gap at least `Δ₀`. It is gauge- and `S`-invariant. On `Z` the corresponding product state `ω₀` is the unique ground state on the full quasi-local algebra, is pure there and on `𝔄^K`, and its GNS generator has a simple zero and gap at least `Δ₀`. It is stationary under the tick and invariant under translations and the stated cell reflection.

*Proof.* The terms are even, commute, are nonnegative, and have unique local kernels. Their individual gaps are `14τ`, `τ₅`, and `τ_E`. If `p_j` are their kernel projections, `H₀≥Δ₀Σ_j(1−p_j)≥Δ₀(1−∏_jp_j)`. The kernel product is the projection onto `Ψ`. All factors are fixed by their gauge and symmetry actions. The on-site and link gates are even, symmetric, gauge invariant and can be embedded in NN-a layers. The reflection `x↦1−x`, `γ_{x,a}↦(−1)^xγ_{1−x,a}`, preserves the terms; on rings the displayed sign convention requires even `L`.

For the infinite ground-state uniqueness, choose a local lowering matrix unit `A=|κ⟩⟨e|` for any factor with excitation energy `λ>0`. All other terms commute with it, so `ω(A*[H₀,A])=−λ ω(|e⟩⟨e|)≥0`. Thus every factor is in its kernel. Cauchy–Schwarz fixes every local expectation to the product state. The same kernel argument proves purity. Purity on the invariant algebra follows from the gauge-invariant extremality equivalence in `VC1_5.md`, section 1. The product GNS space is spanned by finite excitations, whose energies are sums of the local excitation energies. This gives the gap and simple kernel. Each local gate fixes the product state, so the tick does too. \(\square\)

**Theorem 4.2.** In the invariant-algebra GNS subspace orthogonal to `Ω`, the zero-hop tick unitary has `1` in its spectrum for every `0<τ<π/16`.

*Proof.* Let `e` be a normalized even eigenvector of `W` at `2`. The even local operator `K_x=|e⟩⟨ψ|` is gauge invariant. Products on `n` distinct sites give unit, vacuum-orthogonal vectors with tick eigenvalue `exp(16iτn)`. If `16τ/(2π)` is rational, some eigenvalue equals 1; if irrational, its positive integer multiples approach 1. The spectrum is closed. \(\square\)

**GAP: general Floquet claim.** Theorem 4.2 is a counterexample to an intrinsic gap for this product tick. It does not show that every tick lacks one or that a generator is the only meaningful gap notion. `FLQ` asks for a tick-stationary, pure-on-invariants, cell- and `S`-invariant state for nonzero hopping that locally agrees with the generator ground state to `O(θ)`; it remains open.

## 5. Weak hopping and finite gauging

**Lemma 5.1.** On an open segment, Jordan–Wigner ordering by site maps `H(θ)` plus one independent dummy electric link to a spin chain of local dimension 64 of the form `Δ₀(Σ_x H_x+tΣ_{x<N}V_{x,x+1})`, where `H_x≥0` has a unique zero vector and is at least 1 on its complement, `‖V‖≤1`, and `t=4θ/Δ₀`.

*Proof.* Assign each site and its right link to one spin factor, with a dummy link at the end. The Jordan–Wigner strings in a nearest-neighbour even hop cancel outside the two sites. The on-factor assertion follows from Theorem 4.1. The eight summands in `b_ℓ` have norm `1/2`, so `‖b_ℓ‖≤4`; take `V=b_ℓ/4`. The dummy electric term has gap `τ_E≥Δ₀`. Each endpoint gauge transformation flips both its Majorana and `Z_ℓ`; `S` supplies the same sign at both endpoints. Hence each hop preserves both symmetries. \(\square\)

**Theorem 5.2 (conditional imported stability).** Assume [Fröhlich–Pizzo, Theorem 3.5](https://arxiv.org/abs/1812.02457) applies to the normalized finite-dimensional open chain of Lemma 5.1 with threshold `t₀` and yields a unique ground state with gap at least `1/2`. Then for `|θ|<t₀Δ₀/4`, `H(θ)` has a unique open-segment ground state and gap at least `Δ₀/2`, uniformly in length. The state is gauge- and `S`-invariant.

*Proof.* Apply the assumed theorem to Lemma 5.1 and remove the independent dummy link. Symmetry commutes with the Hamiltonian. A nondegenerate ground vector carries a one-dimensional character; its spectral projection varies continuously along the gapped interval. The finite character values cannot change continuously, and they are trivial at `θ=0`. \(\square\)

The paper's abstract confirms a uniform weak-coupling gap for short-range bounded perturbations of an on-site gapped chain. This pass did not retrieve and check the full theorem, its precise constants, or every hypothesis; the theorem above is conditional. The draft's non-strict `≤` threshold in its outline is not justified by its strict stability hypothesis. R1-H retains the native proof and ring and infinite-chain versions. No stationarity for `U` at nonzero `θ` follows from Theorem 5.2.

**Proposition 5.3 (finite `S` gauging).** Replace parity gauge links by `ℓ²(Ŝ)`, with electric basis `|χ⟩`, endpoint action `χ(g)`, shifts `M_ρ|χ⟩=|χρ⟩`, electric term `τ_E(1−|1⟩⟨1|)`, and hop `b^S_ℓ=(i/2)Σ_aγ_{x,a}M_{ρ_a,ℓ}γ_{x+1,a}`. The zero-hop conclusions of Theorem 4.1 and the reduction of Lemma 5.1 hold with local dimension 512; Theorem 5.2 holds conditional on the corresponding stability theorem at that dimension.

*Proof.* All characters take values `±1`, so each shift is a Hermitian unitary. At either endpoint the local action changes both `γ_a` and `M_{ρ_a}` by `ρ_a(g)`; the hop is invariant. The trivial link character and the `S`-fixed atom form the unique local kernel, and the electric gap is `τ_E`. The same product-state and Jordan–Wigner arguments apply; the triangle inequality again gives `‖b^S‖≤4`. Finite shifts are exact unitaries, consistent with the finite-image scope of `GA2_Y2.md`, Theorem 2.1 and Corollary 2.2. \(\square\)

## 6. Assembly ladder and open obligations

The ladder is a proposed research programme, not an implication that its targets are true. Each rung needs its own carrier, state, dynamics and scaling map.

- **R0 atoms.** R0-FK is Theorem 2.2. R0-16 is the prior 32-mode Spin(10) atom cited above, with its source status. **R0-U5** asks for an `L5-U` mirror atom on a multi-site cell; its quartics and carrier must be realized. `CH1.md` C2-5 excludes treating the ten one-site triple products as ten independent CAR modes.
- **R1 eight chains.** Theorems 3.1, 4.1 and 4.2 establish the specified zero-hop generator results. The open-segment hopping claim has the imported dependency of Theorem 5.2. **R1-H** covers a native stability proof and the ring and infinite chain. **FLQ** is the distinct tick-stationarity problem above. One-mode sites and the weak-interaction regime are untreated.
- **R1.5-D decoupling.** Keep the eight-mode mirror and a half-filled light fifth-mode chain, with local symmetric gauge-invariant mixing. Establish a `c=1` Luttinger scaling limit and exclude all extra light fields. Integrating out a gapped mirror in the presence of a gapless sector and controlling the induced couplings are open. `S` forbids quadratic cross terms between the eight Majoranas and mode 5. **GAP:** this does not imply every allowed interaction is a light bilinear times an invariant mirror operator: pure-light and pure-mirror terms are allowed, and more general higher-order mixing needs classification. No Luttinger limit follows from symmetry alone.
- **R2 chiral 1+1D.** Construct a finite-register NN-a model with exact on-site `U(1)` charges and a scaling theory with 3-4-5-0 or CH1-C1 `(1,7)/(5,5)` current levels, without extra light fields. The 3450 null interaction lattice and a three-site atomic result are already recorded in `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`, entries #10058 and #10060, per the digest; the cited stability is for vector-like content only. Mirror decoupling and a matching finite-register carrier remain open. Rotor constructions and finite-size numerics do not establish this target.
- **R3-H and R3-D.** Extend uniform stability and light/mirror decoupling to two spatial dimensions. The proposed flavour-diagonal free zeros occur at `{0,π}²`; no higher-dimensional stability or decoupling theorem is established here. Do not assume the one-dimensional proof carries over word for word.
- **W2 / R4.** Construct the proposed 3+1D chiral 16 and resolve the scaling-definition GAP. `LW1_5.md` Amendment 3, `CH1_5U.md` and `RCSP16.md` record carrier routes and limitations. The `CH1_5U.md` anomaly ledger uses a cited, unverified bordism input. A representation label, atomic gap, or anomaly cancellation does not prove a moving chiral family or a selective mirror gap.

The seven distinct tasks in the outline are: symmetric atoms (R0), volume-uniform stability (R1-H onward), light/mirror decoupling (R1.5-D onward), chiral tick content (R2/W2), charged-sector fields (R1.5/W2), tick-versus-generator dynamics (FLQ), and finite-register gauging (Proposition 5.3 for finite `S`; continuous groups remain separate). Prior failed selective-gap examples and their source locations are catalogued in `prior/SMG1.md`; they do not establish a general impossibility theorem.

## 7. Proposed readings and checks

The draft's four tests ask whether a reading fixes another target, is open-ended, settles downstream physics by premise, or adds unnecessary structure. P means pass, C conditional pass, F fail. These are the draft's assessments, qualified by the checks here.

- **R-GEN: proposed**, Definition 1.3. Draft tests `C, P, C, P`: scoped to SMG1, fixed by the supplied decomposition, conditional on leaving FLQ open, and using gate generators. **Check:** a principal logarithm is unique for each gate under `‖X_g‖<π`, but the sum depends on the decomposition. The draft's example adding `2πP` violates that bound and does not demonstrate dependence within its premises. The draft's conjugated-tick example gives another proposed illustration, but its generic nonstationarity was not independently checked here. The bound is additional specified data unless already supplied by the chosen law; test 4 remains conditional. Q1 asks whether the owner accepts R-GEN for this part. No adoption is implied.
- **R-LIGHT: proposed**, Definitions 1.5–1.7. Draft tests `C, P, C, P`: align with CH1's light reading; supposedly closed; conditional on intending protected `ν^c`; using existing translations and existential `Z,c`. **Check:** W2.4 fails as stated and conflicts with the claimed existential quantification; test 2 fails pending repair. The charged-sector and zoom maps also need separate definitions. Q2 asks whether W2.1 and a symmetry-protected `ν^c` are intended.
- **R1-LAW: proposed**, the explicit five-mode model of section 2, with parity gauge or finite `S` gauge. Draft tests `P, P, P, P`: a rung model, definite data, no downstream physical conclusion, and terms motivated by the carrier and uniqueness. **Check:** the model is definite once boundary and cell conventions are supplied; its generator gap does not establish a nonzero-hop stationary tick state. This reading does not change either live law.

The next independent check should examine Theorem 5.2 against the complete source and all fourteen FK signs, then referee the final file. No retained status follows from this pass.
