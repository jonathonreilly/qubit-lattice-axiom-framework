lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1-I1[INV]: the zoom with the owner's invariant-algebra block map, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-ZM1INV/`. A check guides and never proves.

**Source revisions read.** Branch `claude/toe-assembly` at `b2690b690` (local checkout, sparse). No other branch was needed: the digest `prior/ZM1INV.md` quotes the relevant lines of main and the open PRs, and every result used below lives in this folder.

Files read at that commit, by line: `prior/ZM1INV.md` (all, 94 lines); `TOE_ASSEMBLY.md` lines 221-256 (sections 3.6-3.9) and 296-314 (ZM1); `ZM1.md` lines 1-140 (status, Definitions Z and G, Theorems Z0-Z1) and 340-400 (Theorem Z3', ZM1-I1 in its precise form, Lemma R-GI, Attacks 1-3); `ZM1_OBS.md` lines 1-142 (sections 0-3) and 163-180 (section 5.1) and 272-300 (Lemma S0, Lemma ER, Proposition A, Lemma P1); `ZM1I1A.md` (all, 156 lines); `ZM1I1A_OWNER_CHECK.md` lines 120-192 (options 7-10, Q2); `VC1_5.md` lines 1-57, 84-130 (Theorems 2.1, 2.2, 4.2, 5.2, 5.3, 5.5) and the theorem list; `VC1_5U_ODD.md` lines 1-20 and the theorem list; `GA1_5.md` lines 1-64 and 148-186 (definitions, Theorems 6.1-6.4, Proposition S-odd statement); `LZ1I.md` lines 1-12 and the theorem list.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The owner's text ZM1-INV and the retained class (a) with `p = 2` are read plainly, as quoted in section 0. Where the text leaves a choice open (which VC1 vacuum, which coarse constants), the choice is named and nothing is adopted.

**Working set used, by name.** PS-5, PS-6r and PS-7r only through the two five-mode laws and the VC1 witnesses as frozen in `LW1_5.md` and `VC1_5.md`; the owner decisions GA1-P-NN = NN-a (section 3.7), ZM1-I1[a] (section 3.8) and ZM1-INV (section 3.9). No axiom and no working-set entry changes.

**Inputs from outside the working set.** Standard finite-dimensional algebra, rebuilt where used: Schur's lemma, the isotypic decomposition of a unitary representation of a compact group and its commutant, highest weights of `U(5)`, and the classification of unital `*`-homomorphisms between finite-dimensional C*-algebras by multiplicity matrices. Literature is in section 2 and is never load-bearing.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 252, the owner's map: "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form). Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants. Use this \(\Phi\) in class (a). Impose no map on charged fields or Gauss generators. Retain class (a) and \(p=2\) as the comparison required of any replacement whose observable and state interfaces make that comparison well-defined. Whether the bound is achieved remains unproved."

Line 253, the retained data: "the VC1 fine vacuum, the admissible fine updates, \(L\ge2\), the coarse law \(\alpha_1\) and the \(\alpha_1\)-invariant state \(\omega_1\), one coarse tick as \(L\) fine ticks, and the relative tail-envelope bound with \(p=2\). The open statement is now ZM1-I1[INV]."

Line 243, the bound (class (a)): "For every support radius \(R_0\), take all norm-at-most-one \(A,B\in\mathfrak A_1^G\) supported in that ball. Include their cell-group images. Compare their truncated two-point values at every nonnegative coarse tick and every cell separation \(r=|\beta|_\infty\ge1\). For each fixed \(A,B\), set \(M(r,t)=\sup_{|\beta'|_\infty\ge r}\max_i|F_i^T(A^*,\tau_{\beta'}B;t)|\). Require \(|F_0^T-F_1^T|\le C_{R_0}(r^{-p}+tr^{-p-1})M(r,t)\), with \(p=2\). A zero envelope gives zero values on both sides. No separate one-point matching is imposed."

`ZM1.md` line 361 fixes the vacuum and the coarse law: "Let `ω_0` be a vacuum that VC1 supplies for `L5-U[m]` (base tick, or with a plaquette class that GA1-P-5 supplies)", and "a coarse law `α_1` of the `L5-U` form, and an `α_1`-invariant state `ω_1` of `A_1`". The lane brief adds `L5-O` as an alternative fine law.

The lane brief: "Either construct ... or prove that no such data exist for a named class of vacua or updates, naming the step."

## 0.1 Outcome in one paragraph

**Reduced to an open kinematic lemma, after three named attacks.** The locked P-witnesses that VC1 has on file (`VC1_5.md` Theorem 5.5 for even `m`, Theorem 4.2 for `L5-O`) restrict to *characters* of the invariant algebra: every gauge-invariant observable is sharp in them, and their physical space is `CΩ` (Theorems C1, C1-O, Corollary C3). So every invariant truncated value vanishes, on both sides, for every unital homomorphism `Φ` (Corollary C2). In these vacua the class (a) comparison with `p=2` is empty, and ZM1-I1[INV] with an even coarse `m₁` is equivalent to K-INV with an even `m₁`: the existence of a cell-covariant, exponentially local, unital injective `*`-homomorphism `𝔄₁^G→𝔄^G` with `L≥2` (Theorem R). K-INV is necessary in every vacuum. The old trace obstruction does not transfer, because the invariant algebra has many traces (Lemma T). Three attacks on K-INV fail at named steps: neutral matrix registers (no unital `M_D` sits in a local invariant algebra, Lemma N); decimation with equivariant links (a path of two or more links cannot carry a coarse link, by end-number spectra, Lemma E; one-link paths contradict covariance); and good-sector decimation (exact on the good sector, Lemma S, but coarse end numbers cannot stay at the representatives, Lemma F). Any solution must carry each coarse link constraint on fine factors shared by both end images (Lemma F′). The other first tests (the R2 mixture, the swap bands, the two-band states, the ice states) are not trivial: there the comparison forces exact tail matching. Charged fields and Gauss generators get no map. No reading is adopted; R-V (pose the question in the vacuum VC1 selects) passes the four tests.

## 1. Definitions and the exact statement

These definitions restate frozen texts. Nothing new is proposed in this section.

1. **Laws.** `L5-U[m]`, `1≤m≤9`, and `L5-O[S_+]` as in `VC1_5.md` section 2 (quoted there from `LW1_5.md`): five CAR modes per site; on `L5-U[m]` each link register is `Λ^m C^{10}` with five rishon modes at each end, `p_{ℓ,x}+p_{ℓ,y}=m`; on `L5-O` it is `S_+`. `𝔄` is the quasi-local algebra, `α` the tick, `𝔄^G` the fixed algebra of all local gauge automorphisms, `E` the gauge average (`VC1_5.md` Theorem 2.1).
2. **Regions.** For a finite set `R` of sites and links, `𝔄(R)` is the algebra of the matter at the sites of `R` and of the links of `R`; `H_R` is the finite Hilbert space it acts on (Jordan-Wigner on the matter, so `𝔄(R)=End(H_R)`). `G_R` is the product of the local groups `U(5)_x` (resp. `Spin(10)_x`) over all sites `x` whose group acts nontrivially on `𝔄(R)`, including outer endpoints of links of `R`. Put `𝔄^G(R)=𝔄(R)∩𝔄^G`. It is the commutant of `G_R` in `End(H_R)`.
3. **Coarse system (R-form).** `ZM1I1A.md` section 1 item 3: "The coarse algebra of a law of `L5-U` form is the same construction on that graph, with any `m₁∈{1,…,9}`." Coarse cell `u∈Z³` holds eight coarse sites `X=(u,r)`; its fine block `β_u` holds `(2L)³` fine sites (`ZM1I1A.md` section 1 item 2). One coarse tick is `L` fine ticks.
4. **The data of ZM1-I1[INV].** An integer `L≥2`, a coarse `m₁`, and:
   - (INV-1) a unital injective `*`-homomorphism `Φ:𝔄₁^G→𝔄^G`;
   - (INV-2) cell covariance: each coarse cell translation and each proper cubic rotation about a coarse cell centre has a fine lift `g` with `Φ∘g₁=g∘Φ` (the phase or parity allowed by `ZM1.md` Definition Z acts trivially on `𝔄^G`, which is even by `ZM1_OBS.md` Theorem 3);
   - (INV-3) exponential locality: for each `R₀` there are `C_{R₀},ξ` such that, for `A∈𝔄₁^G` supported in a coarse ball of radius `R₀` about `X`, `Φ(A)` lies within `C_{R₀}e^{-R/ξ}‖A‖` of `𝔄(N_R)`, where `N_R` is the set of fine sites within distance `R` of the blocks of that ball;
   - (INV-4) a coarse law `α₁` of the `L5-U[m₁]` form (resp. `L5-O`) and an `α₁`-invariant state `ω₁` of `𝔄₁`;
   - (INV-5) the class (a) bound with `p=2`, for the fine vacuum `ω₀` and an admissible fine update `α`.
5. **K-INV(m, m₁, L).** The kinematic part: there is `Φ` with (INV-1), (INV-2) and (INV-3). It mentions no state and no update.
6. **Character.** A state `ω` is a *character on `𝔄^G`* if `ω(AB)=ω(A)ω(B)` for all `A,B∈𝔄^G`.
7. **Truncated values.** `F_0^T(A^*,B;t)=ω₀(Φ(A)^*α^{Lt}(Φ(B)))-ω₀(Φ(A)^*)ω₀(Φ(B))`, and `F_1^T` likewise with `ω₁,α₁` and no `Φ` (`ZM1_OBS.md` section 1).

## 2. Literature read

Searches (WebSearch, 2026-11-07): operator-algebraic renormalization of lattice gauge theory; wavelet scaling maps; coarse-graining of quantum and fermionic cellular automata; Balaban, Dimock, Gawędzki-Kupiainen block-spin maps; Lieb-Robinson bounds and clustering; index theory of cellular automata; C*-algebraic lattice QCD with the Gauss law; free-fermion entanglement renormalization. Abstract pages fetched where marked. No result below is a proof step. Each is context for a design choice.

| Work | arXiv | What was checked | Use here |
|---|---|---|---|
| Brothier, Stottmeister, "Operator-algebraic construction of gauge theories and Jones' actions of Thompson's groups", CMP (DOI 10.1007/s00220-019-03603-4) | 1901.04940 | abstract page fetched; abstract opens "Using ideas from Jones, lattice gauge theory and loop quantum gravity," | Their refinement is a unital map of full link algebras in 1+1 dimensions with continuous groups; the frozen `ZM1I1A.md` RC-6 already checks its eq. (2.1). Context for attack 2 (section 5.4). |
| Brothier, Stottmeister, "Canonical quantization of 1+1-dimensional Yang-Mills theory: an operator-algebraic approach" | 1907.05549 | search result only, NOT VERIFIED beyond the listing | Context. |
| Morinelli, Morsella, Stottmeister, Tanimoto, "Scaling limits of lattice quantum fields by wavelets", CMP 387 (2021) | 2010.11121 | abstract page fetched: "We present a rigorous renormalization group scheme for lattice quantum field theories in terms of operator algebras." "The renormalization group is considered as an inductive system of scaling maps between lattice field algebras." | The closest published analogue of a homomorphic block map (scaling maps are injective homomorphisms of field algebras, free scalar fields). No gauge constraint. Context only. |
| Stottmeister, Morinelli, Morsella, Tanimoto, "Operator-algebraic renormalization and wavelets", PRL 127 (2021) 230601 | 2002.01442 | search result only, NOT VERIFIED | Context. |
| Osborne, Stottmeister, "Conformal field theory from lattice fermions", CMP 398 (2023) | 2107.13834 | search result only, NOT VERIFIED beyond the listing | Context: the same framework for lattice fermions in 1+1 dimensions. |
| Trezzini, Pizzamiglio, Bisio, Perinotti, "Renormalisation of Fermionic Cellular Automata" | 2511.23398 | abstract page fetched; opens "We present an exact renormalisation scheme for fermionic cellular automata on hypercubic lattices." | Exact coarse-graining by tiles and subspaces. It is a subspace notion (`ZM1.md` Attack 3), not a unital homomorphism. Context for attack 3. |
| Trezzini, Bisio, Perinotti, "Renormalisation of Quantum Cellular Automata", Quantum (2025) | 2407.12652 | search result only, NOT VERIFIED | Context. |
| Duranthon, Di Molfetta, "Coarse-grained quantum cellular automata" | 2011.04287 | search result only, NOT VERIFIED | Context. |
| Gross, Nesme, Vogts, Werner, "Index theory of one dimensional quantum walks and cellular automata", CMP 310 (2012) 419 | 0910.3675 | search result only, NOT VERIFIED | Context: locality-preserving automorphisms carry an index; Φ here is a homomorphism, not an automorphism, so no index is used. |
| Nachtergaele, Sims, "Lieb-Robinson bounds and the exponential clustering theorem", CMP 265 (2006) 119 | math-ph/0506030 | abstract page fetched: "a non-vanishing spectral gap implies exponential clustering in the ground state of such systems." | Context: decay of truncated correlations is a gap property; the character vacua of section 4 have zero truncated invariant correlations with no gap argument. |
| Grundling, Rudolph, "Dynamics for QCD on an infinite lattice", CMP (DOI 10.1007/s00220-016-2733-5) | 1512.06319 | abstract page fetched: the authors "show that the dynamics automorphism group descends to the algebra of physical observables." | Context: the infinite-lattice gauge-invariant observable algebra with the Gauss law enforced; here the analogue is `𝔄^G` and the frozen `VC1_5.md` Theorem 2.1. |
| Bałaban, "Renormalization group approach to lattice gauge field theories I", CMP 109 (1987) | none | title only (library record), NOT VERIFIED | Context: measure-level block averaging (R-MEAS in `ZM1I1A.md`), outside the owner's operator map. |
| Dimock, "The renormalization group according to Balaban I, II" | 1108.1335, 1212.5562 | search result only, NOT VERIFIED | Context: small-field/large-field split for scalar fields. |
| Dimock, "Quantum electrodynamics on the 3-torus I, II" | math-ph/0210020, math-ph/0407063 | search result only, NOT VERIFIED | Context: block averaging in gauge theory is measure-level. |
| Gawędzki, Kupiainen, block-spin papers (CMP 1980s) | none | search result only, NOT VERIFIED | Context. |
| Haegeman, Swingle, Walter, Cotler, Evenbly, Scholz, "Rigorous free fermion entanglement renormalization from wavelet theory", PRX 8 (2018) 011003 | 1707.06243 | search result only, NOT VERIFIED | Context: isometric (not unital) coarse-graining. |

**What the search found and did not find.** The published homomorphic scaling maps (Morinelli et al.; Brothier-Stottmeister) act on full field or link algebras of free or 1+1-dimensional systems. The rigorous block-spin programs for gauge theory (Bałaban, Dimock) act on measures. The exact cellular-automaton schemes (Trezzini et al.) act on subspaces. The search did not find a unital homomorphism of gauge-invariant algebras for a quantum link model in 3+1 dimensions. This is a report of these searches, not a claim that none exists.

## 3. Prior work used

All paths are in this folder unless stated. Each result is quoted where it is used.

| Result | Path | How it is used |
|---|---|---|
| Gauge average `E`, affine bijection of invariant states, `E` commutes with `α` and lifts | `VC1_5.md` Theorem 2.1 | Section 4: states on `𝔄^G` and their gauge-invariant extensions. |
| P-witnesses for even `m` (empty or full matter, flavours `1..k` at every end) | `VC1_5.md` Theorem 5.5 | Section 4: the character vacua of `L5-U[2k]`. Extended: their restriction to `𝔄^G` is multiplicative (Theorem C1). |
| Dark P-witnesses of `L5-O[S_+]` | `VC1_5.md` Theorem 4.2 | Section 4: the character vacua of `L5-O`. Extended the same way (Theorem C1-O). |
| Invariant algebra is even; representative-site maps keep invariance | `ZM1_OBS.md` Theorem 3 | Section 1 item 4 (the parity in (INV-2) acts trivially). |
| Lemma ER: relative envelopes force equal tail lengths and amplitudes | `ZM1_OBS.md` appendix | Sections 4 and 5: a nonzero fine tail against a zero coarse tail is excluded. |
| Dark pairs make class (a) automatic for finite-range maps | `ZM1I1A.md` Theorem 7 | Section 4: extended to character pairs with no locality hypothesis (Corollary C2). |
| Dark kinematics of empty/full product states | `ZM1I1A.md` Theorem 8 | Section 4: strengthened from darkness to multiplicativity on `𝔄^G`. |
| Trace obstruction for the full-algebra map | `ZM1I1A.md` Theorems 1-6, RC-1, RC-3 | Section 5.1: why it does not transfer (traces on `𝔄^G` are not unique). |
| `1/4` tail of the R2 mixture | `ZM1I1A.md` Theorem 9, RC-5; `VC1_5.md` Proposition R2 | Section 4: a non-character test state. |
| Neutral swap band, every `m` | `GA1_5.md` Theorem 6.3, Proposition S-odd | Section 4: a non-character test state with a moving invariant tail. |
| Two neutral Clifford bands | `LZ1I.md` Theorems 6-8 | Section 4: a non-character test state. |
| Ice states and purity versus tail triviality | `VC1_5U_ODD.md` Theorems 4.2, 4.3 | Section 4: odd-`m` states are not characters. |
| Linear transported fields excluded; Attack 2 on c-number links | `ZM1.md` Theorems Z3, Z3', Attack 2 | Section 5.4: the transport problem reappears for invariant composites. |
| Coherence `κ≤1/2` of an `L5-U` link | `GA2_Y2.md` Theorem 3.4 (quoted in `ZM1.md` line 30) | Section 5.4: links are not c-numbers. |
| Gauge-invariant link-only operators; `(U^{jk})^2=0` | `GA2_Y2.md` Theorem 3.4; `GA1_5.md` section 1 | Section 5.3. |

**Prior work the digest did not list.** None found in the files read. One fact is new here and was not on file: the even-`m` and `L5-O` P-witnesses restrict to characters of `𝔄^G` (section 4). `ZM1I1A.md` Theorem 8 proved the weaker statement that they are dark.

## 4. Exactly solvable cases

### 4.1 The locked vacua are characters of the invariant algebra

`VC1_5.md` Theorem 5.5 (quoted): "Let `m=2k`. On every link occupy flavours `1,...,k` at each end. Take empty matter on every site and gauge average the resulting product state. It satisfies (i)–(iii) and P, has sharp `Q_x=3m`, and filling 0. Full matter gives a second witness with `Q_x=5+3m` and filling 5." Write `ψ` for the product state and `ω=ψ∘E`. For a finite region `R`, `Ψ_R∈H_R` is the product vector of `ψ` on `R`.

**Theorem C1 (locked `L5-U` vacua are characters).** Let `m=2k`. For every finite region `R` and every `A∈𝔄^G(R)`, `AΨ_R∈CΨ_R`. Hence `ω` (empty or full) is a character on `𝔄^G`.

*Proof.* For each site `x` acting on `H_R`, let `h_{x,j}` count the quanta of flavour `j` at `x`: the matter mode `(x,j)` if `x` is a site of `R`, plus the `j`-th rishon mode of each end at `x` of a link of `R`. The diagonal torus of `G_R` acts on each occupation-basis vector by the phases `∏_{x,j}e^{iθ_{x,j}h_{x,j}}`, so occupation-basis vectors are joint weight vectors with weight `(h_{x,j})`. Let `d_x` be the number of ends at `x` in `R`.

*Empty case.* `Ψ_R` has `h_{x,j}=d_x` for `j≤k` and `h_{x,j}=0` for `j>k`. Let `v` be an occupation-basis vector with this weight. No quantum of flavour `j>k` occurs, so each end holds a subset of `{1,…,k}` and has at most `k` rishons. Each link has `p_{ℓ,x}+p_{ℓ,y}=2k`, so each end holds exactly `{1,…,k}`. The ends at `x` then give `h_{x,j}=d_x` for `j≤k`, so the matter at `x` is empty. Thus `v=±Ψ_R`.

*Full case.* At a site `x` of `R`, `h_{x,j}=d_x+1` for `j≤k`. There are `d_x+1` slots (the ends and the matter), each holding flavour `j` at most once, so each holds it. At an outer endpoint `y`, `h_{y,j}=d_y` for `j≤k` forces the same for its ends. So every end contains `{1,…,k}`; by `p_{ℓ,x}+p_{ℓ,y}=2k` it equals `{1,…,k}`. Then `h_{x,j}=1` for `j>k` puts flavour `j` in the matter at `x`. Thus `v=±Ψ_R` again.

So the weight space of `Ψ_R` is `CΨ_R`. An element `A∈𝔄^G(R)` commutes with `G_R`, hence with its torus, hence preserves each weight space: `AΨ_R=aΨ_R`. Now `ω(B)=ψ(B)` for invariant `B` (Theorem 2.1 of `VC1_5.md`: `E` fixes invariant elements), and `ψ|_{𝔄(R)}` is the vector state of `Ψ_R`. For `A,B∈𝔄^G(R)` with `AΨ_R=aΨ_R`, `BΨ_R=bΨ_R`: `ω(AB)=⟨Ψ_R,ABΨ_R⟩=ab=ω(A)ω(B)`. Local invariant elements are dense in `𝔄^G` (`VC1_5.md` Theorem 2.1) and `ω` is continuous, so `ω` is multiplicative on `𝔄^G`. □

**Theorem C1-O (locked `L5-O` vacua are characters).** The witnesses `ω_0=Φ_0∘E` and `ω_F=Φ_F∘E` of `VC1_5.md` Theorem 4.2 are characters on `𝔄^G`.

*Proof.* `VC1_5.md` Theorem 4.2 uses the Cartan charges "`H_{x,j}=(n_{x,j}-1/2)+\sum_{ℓ∋x}(n^{ℓ,x}_j-1/2)`". On `H_R` take the same sum over the factors at `x` that lie in `R`. Each term is at least `-1/2`, with equality exactly when the mode is empty. So the joint weight of the empty product vector is the unique minimum, and its weight space is spanned by that vector (it lies in `S_+`, since an empty link has even parity). The full vector is the unique maximum in the same way (a full link holds ten rishons, even parity). The rest is the proof of Theorem C1. □

**Corollary C2 (character pairs make class (a) empty).** Let `ω₀` be a character on `𝔄^G`, invariant under a fine update `α` that commutes with every local gauge automorphism. Let `ω₁` be a character on `𝔄₁^G`, invariant under a coarse law `α₁` with the same property. Let `Φ:𝔄₁^G→𝔄^G` be any unital `*`-homomorphism. Then `F_0^T(A^*,τ_βB;t)=F_1^T(A^*,τ_βB;t)=0` for all `A,B∈𝔄₁^G`, all `β` and all `t≥0`. The class (a) bound holds for every `p` and every `C_{R₀}≥0`.

*Proof.* A gauge-commuting automorphism maps `𝔄^G` into itself: `γ(α(X))=α(γ(X))=α(X)` for every local gauge automorphism `γ` and invariant `X`. So `α^{Lt}(Φ(τ_βB))∈𝔄^G`. Multiplicativity and invariance give `ω₀(Φ(A)^*α^{Lt}(Φ(τ_βB)))=ω₀(Φ(A^*))ω₀(Φ(τ_βB))`. The coarse side is the same. □

This needs no locality and no covariance of `Φ`. It strengthens `ZM1I1A.md` Theorem 7, which needed finite range and gave the bound only for separated supports.

**Corollary C3 (no physical sector).** In a character vacuum, `H_phys=closure π(𝔄^G)Ω=CΩ`.

*Proof.* `‖π(A)Ω-ω(A)Ω‖²=ω(A^*A)-|ω(A)|²=0` by multiplicativity. □

So the locked vacua carry no gauge-invariant excitation. There is no band, no tail and no Clifford cone in them. The bands of `GA1_5.md` Theorem 6.3 and `LZ1I.md` Theorem 7 live in other states (multiplicity-mixed densities), consistent with this.

### 4.2 Which first tests are trivial for the criterion

| Fine state and update | Character on `𝔄^G`? | Class (a) for this state |
|---|---|---|
| `VC1_5.md` Theorem 5.5 witnesses, even `m`, base tick | yes (C1) | trivial for every unital `Φ` paired with a character coarse state (C2). Only K-INV is left. |
| `VC1_5.md` Theorem 4.2 witnesses, `L5-O`, base tick | yes (C1-O) | trivial in the same way. |
| `VC1_5.md` Theorem 5.2 at `t=±∞` (empty/full matter, tracial links), base tick | no: an end-number projection `P` has `0<ω(P)<1` | dark (`ZM1I1A.md` Theorem 8). Trivial for finite-range `Φ` (`ZM1I1A.md` Theorem 7). For a merely exponentially local `Φ`, Lemma ER forces the fine truncated values to vanish exactly beyond some `r` (they face a zero coarse tail), which is a real condition on `Φ`. |
| R2 mixture (`VC1_5.md` Proposition R2) | no | not trivial: tail `1/4` at every separation (`ZM1I1A.md` Theorem 9, RC-5). If `Φ`'s image contains a channel with that tail, `ω₁` must reproduce amplitude `1/4` exactly (Lemma ER). It is an E-witness, not a P-witness. |
| swap-band states (`GA1_5.md` Theorem 6.3, Proposition S-odd), NN-a | no: `H_phys` contains the band | not trivial: a unit-amplitude travelling correlation (`ZM1I1A.md` RC-4) if the image contains the band composite. |
| two-band states (`LZ1I.md` Theorems 6-8) | no | not trivial: two speeds (`ZM1_OBS.md` Theorem 9′ conditions). |
| odd-`m` ice states (`VC1_5U_ODD.md` Theorems 4.2-4.3, under ICE-T) | no: loop operators act on `L²(ν)` | not trivial; tails not computed (`ZM1I1A.md` open item). |

So the only exactly solvable vacua on file that are P-witnesses (the locked ones) make the comparison empty. The nontrivial test states are the mixture, the band states and the ice states. None of them is shown to be the VC1 vacuum.

## 5. Main results

### 5.1 Reduction to kinematics

**Theorem R (reduction).** Let `m∈{2,4,6,8}`, let `ω₀` be a locked witness of `VC1_5.md` Theorem 5.5 and let `α` be the base tick. Then ZM1-I1[INV] holds for `(ω₀,α)` with some even coarse `m₁` if and only if K-INV`(m,m₁,L)` holds for some `L≥2` and some even `m₁`. The same holds for `L5-O[S_+]` with the witnesses of `VC1_5.md` Theorem 4.2 and a coarse `L5-O` system. For every fine vacuum and update, ZM1-I1[INV] implies K-INV for the `m₁` and `L` it uses.

*Proof.* "Only if" and the last sentence: the data of ZM1-I1[INV] contain a map with (INV-1)-(INV-3), for the `m₁` and `L` they use. (For odd `m₁` the "if" direction would need a coarse `α₁`-invariant state whose invariant truncated values vanish beyond some separation, by Lemma ER; none is on file, so the theorem is stated for even `m₁`.) "If": let `Φ` satisfy (INV-1)-(INV-3). Take `α₁` the base tick of `L5-U[m₁]` on the coarse lattice, with any allowed constants. It is a law of the stated form, and it commutes with every coarse gauge automorphism (`VC1_5.md` Theorem 2.1, "The map `E` commutes with `α`", applied to the coarse law). Take `ω₁` the coarse locked witness. It is `α₁`-invariant (`VC1_5.md` Theorem 5.5, applied to the coarse law) and a character on `𝔄₁^G` (Theorem C1). The fine pair has the same two properties. Corollary C2 gives the class (a) bound with any constant. Constants do not depend on any variable data. For `L5-O` use Theorem C1-O and `VC1_5.md` Theorem 4.2 in the same way. □

So, for the locked vacua, ZM1-I1[INV] is a statement about `Φ` alone. The state, the coarse law and `p` play no role. The rest of section 5 works on K-INV.

**Lemma T (the trace obstruction does not transfer).** For even `m` and every finite region `R` with at least one link, `𝔄^G(R)` has at least two tracial states. In particular a unital homomorphism into `𝔄^G` need not carry the normalized trace to the normalized trace.

*Proof.* The normalized trace `τ` restricts to a tracial state. The locked character `ω` of Theorem C1 is multiplicative, hence tracial: `ω(AB)=ω(A)ω(B)=ω(BA)`. They differ on an end-number projection `P=[p_{ℓ,x}=k]`: `ω(P)=1`, while `τ(P)=C(5,k)²/C(10,2k)<1`. □

`ZM1I1A.md` Theorem 1 rests on "A tracial state on `M_n` vanishes on off-diagonal matrix units and has equal values `1/n` on diagonal units", that is, on uniqueness of the trace on full matrix algebras. `𝔄^G(R)` is a direct sum of several matrix algebras, so that step has no analogue. This confirms the owner-check sentence "Neither full-algebra obstruction applies directly" (`ZM1I1A_OWNER_CHECK.md` option 8) on the step where the old proof starts.

### 5.2 Attack 1: neutral matrix registers

*The construction.* Encode each coarse cell, or each coarse site, in a fine register built from gauge-neutral operators: a unital copy `M_D⊂𝔄^G` near the block, with copies at different blocks commuting. Then send `𝔄₁^G` (an even subalgebra of the coarse algebra) into the product of these registers.

**Lemma N (no neutral matrix register).** Let `m` be even, or take `L5-O`. For every finite region `R` and every `D≥2` there is no unital `*`-homomorphism `M_D→𝔄^G(R)`.

*Proof.* By the proof of Theorem C1 (or C1-O), `A↦a` with `AΨ_R=aΨ_R` is a unital `*`-homomorphism `𝔄^G(R)→C`. Composed with a unital `M_D→𝔄^G(R)` it gives a unital homomorphism `M_D→C`. Its kernel is a two-sided ideal of codimension one. `M_D` has no such ideal for `D≥2`: the ideal generated by any nonzero matrix is all of `M_D`, because `E_{ij}XE_{kl}=X_{jk}E_{il}`. □

**Attack 1 fails at** "the fine invariant algebra near a block contains a unital copy of `M_D`". Lemma N excludes it for every finite region. The attack in its finite-range form is therefore empty. (For a merely exponentially local register, the attack would need a near-inclusion lemma for finite-dimensional algebras; that lemma is not rebuilt here, and the finite-range failure is the one claimed.)

Lemma N also says what any `Φ` must do. The fine local invariant algebras have one-dimensional summands, so every coarse local algebra `𝔄₁^G(R₁)` must reach them through its own one-dimensional summands (characters). The coarse algebra has them (Theorem C1 on the coarse lattice). So Lemma N obstructs registers, not K-INV.

### 5.3 Attack 2: decimation with equivariant links

*The construction.* Choose covariant representatives `x_X` (one fine site per coarse site). Send the coarse matter and the coarse ends at `X` to the fine matter and fine ends at `x_X`, equivariantly for `U(5)_X≅U(5)_{x_X}`. Send each coarse link `ℓ=(X,Y)` into the algebra of a fine path `γ_ℓ` from `x_X` to `x_Y` by a unital `*`-homomorphism, equivariant for the two end groups and invariant under the groups of the inner sites. Restrict the product map to `𝔄₁^G`. (This is the invariant-algebra form of `ZM1.md` Attack 1 and of the Brothier-Stottmeister refinement checked in `ZM1I1A.md` RC-6.)

For `L5-U[m]` write `P_m=\{\max(0,m-5),…,\min(5,m)\}` for the spectrum of one end number. It has at least two elements for `1≤m≤9`.

**Lemma E (a path of two or more links cannot carry a coarse link).** Let `γ` be a fine path from `x` to `y` with `n≥2` links, and let `H_γ` be a finite Hilbert space of fine factors that contains its first and last links. Let `p_x` be the end number at `x` of the first link and `p_y` the end number at `y` of the last link. Let `K=Λ^{m₁}(C⁵⊕C⁵)` be a coarse `L5-U[m₁]` link with end numbers `p_X,p_Y`. There is no unital `*`-homomorphism `ι:End(K)→End(H_γ)` with
\[
\mathrm{Ad}(e^{i\theta p_x})\circ\iota=\iota\circ\mathrm{Ad}(e^{i\theta p_X}),\qquad \mathrm{Ad}(e^{i\varphi p_y})\circ\iota=\iota\circ\mathrm{Ad}(e^{i\varphi p_Y})\qquad(\theta,\varphi\in\mathbb R).
\]
Only the centres of the two end groups enter, so equivariance for `U(5)×U(5)` is more than enough.

*Proof.* (i) *Form of `ι`.* Put `e_{ij}=ι(E_{ij})` for matrix units of `End(K)`, `d=dim K`, and `K'=e_{11}H_γ`. The map `W^*:K⊗K'→H_γ`, `E_i⊗ξ↦e_{i1}ξ`, is unitary: `e_{i1}^*e_{j1}=δ_{ij}e_{11}` and `Σ_ie_{ii}=1`. It gives `ι(a)=W^*(a⊗1)W`.
(ii) *Charges split.* Put `u_θ=e^{iθp_x}` and `v_θ=ι(e^{iθp_X})`. Equivariance gives `u_θι(a)u_θ^*=v_θι(a)v_θ^*`, so `v_θ^*u_θ` commutes with `W^*(End K⊗1)W` and equals `W^*(1⊗c_θ)W` for a unitary `c_θ`. Thus `Wu_θW^*=e^{iθp_X}⊗c_θ`. Both `θ↦u_θ` and `θ↦e^{iθp_X}` are continuous one-parameter groups, so `c_θ` is one too: `c_θ=e^{iθk_x}` with `k_x` self-adjoint. Differentiating at `θ=0`, `Wp_xW^*=p_X⊗1+1⊗k_x`. Likewise `Wp_yW^*=p_Y⊗1+1⊗k_y`. Since `[p_x,p_y]=0` and `[p_X,p_Y]=0`, `1⊗[k_x,k_y]=0`.
(iii) *Joint spectra.* On `K` the pair `(p_X,p_Y)` has joint spectrum `\{(q,m₁-q):q∈P_{m₁}\}`. So on `H_γ` the pair `(p_x,p_y)` has joint spectrum `\{(q+a,m₁-q+b):q∈P_{m₁},(a,b)∈S'\}`, with `S'` the joint spectrum of `(k_x,k_y)`. But `p_x` and `p_y` act on different tensor factors (the first and last links differ because `n≥2`), so their joint spectrum is `P_m×P_m`. Let `s=\min P_m`. Then `(s,s)=(q+a,m₁-q+b)` for some `q∈P_{m₁}` and `(a,b)∈S'`. The interval `P_{m₁}` has at least two elements, so `q+1` or `q-1` lies in it. Then `(s+1,s-1)` or `(s-1,s+1)` lies in the joint spectrum, and one of its entries is below `\min P_m`. Contradiction. □

**Corollary E1.** In Attack 2 every path has one link, so `x_X` and `x_Y` are fine neighbours whenever `X,Y` are coarse neighbours. Cell covariance gives `x_{X+2e_i}=x_X+2Le_i`, a vector of length `2L≥4`, while it is a sum of two unit vectors. So Attack 2 has no instance with `L≥2`.

**Attack 2 fails at** "each coarse link is carried by an equivariant unital homomorphism into the algebra of a fine path". Lemma E excludes paths of two or more links; covariance excludes one-link paths. This is the invariant-algebra shadow of the adjacency step in `ZM1I1A.md` Theorem 2, reached here by end-number spectra instead of traces. Lemma E is for `L5-U`; on `L5-O` the end data are parities, and the corner argument in step (iii) does not apply.

### 5.4 Attack 3: decimation on the good sector of a path

*The construction.* Take `m=m₁=1`. Then a link holds one rishon, at one end. Put `x_X=LX` with `L≥3` odd (so coarse cell centres go to fine cube centres and rotations lift; `LW1.md` A2 as quoted in `ZM1.md` line 26). Join `x_X` to `x_{X+e_i}` by the straight fine path `γ` of `L` links. Send the coarse star at `X` (matter and six ends) identically to the fine star at `x_X` (matter and the six first-link ends; with `m=1` each end is a five-mode space with occupation `0` or `1` on both sides). Send each coarse link to its path by Lemma S below.

Label the path `x=z_0,z_1,…,z_n=y`, links `ℓ_i=(z_{i-1},z_i)` with tail `z_{i-1}` and head `z_i`. Let `h_i=1` if the rishon of `ℓ_i` is at its head. Let `P_γ` be the projection onto `h_1=h_2=…=h_n`. It is a function of end numbers, so `P_γ∈𝔄^G`.

**Lemma S (on the good sector a path is a coarse link).** (a) At each inner site `z_i`, exactly one of the two path ends at `z_i` is occupied if and only if `h_i=h_{i+1}`; so `ran P_γ` is the set where every inner site holds exactly one path rishon. (b) There is a unitary `W_γ:ran P_γ→(C⁵_x⊕C⁵_y)⊗C_{int}`, `C_{int}=⊗_{i=1}^{n-1}C⁵_{z_i}`, intertwining `U(5)_x×U(5)_y` on the first factor and `∏_iU(5)_{z_i}` on the second. The commutant of `∏_iU(5)_{z_i}` in `End(ran P_γ)` is `W_γ^*(End(C⁵_x⊕C⁵_y)⊗1)W_γ`, and `ι_γ(a)=W_γ^*(a⊗1)W_γ` is an equivariant `*`-isomorphism from the coarse `m₁=1` link algebra `End(C⁵_X⊕C⁵_Y)` onto it. (c) The Wilson line `T^{jk}_γ=Σ_{a}U_{ℓ_n}^{ja_{n-1}}⋯U_{ℓ_1}^{a_1k}`, with `U_ℓ^{ab}=r^{head}_ar^{tail\dagger}_b`, satisfies `T_γ^{jk}=P_γT_γ^{jk}P_γ` and `T_γ^{jk}=(-1)^{n+1}ι_γ(U^{jk})` with the coarse `U^{jk}=r^Y_jr^{X\dagger}_k`.

*Proof.* (a) At `z_i` the path ends are the head of `ℓ_i` (occupied iff `h_i=1`) and the tail of `ℓ_{i+1}` (occupied iff `h_{i+1}=0`). Exactly one is occupied iff `h_i+1-h_{i+1}=1`. (b) If all `h_i=0`, the occupied ends are the tail of `ℓ_1` (colour in `C⁵_x`) and the tail of `ℓ_{i+1}` at each `z_i`; if all `h_i=1`, the head of `ℓ_i` at each `z_i` and the head of `ℓ_n` (colour in `C⁵_y`). Identify the occupied end at `z_i` with `C⁵_{z_i}` by its colour label in both cases. Both ends at `z_i` carry the defining representation of `U(5)_{z_i}`, so `W_γ` intertwines. `C_{int}` is irreducible under `∏_iU(5)_{z_i}` (a tensor product of irreducibles of the factors), so by Schur's lemma the commutant is `End(C⁵_x⊕C⁵_y)⊗1`. The coarse link space for `m₁=1` is `Λ¹(C⁵_X⊕C⁵_Y)=C⁵_X⊕C⁵_Y` with the same end actions. (c) Rishons of different links commute (link factors commute with one another, `VC1_5.md` section 1 item 1). On a link holding one rishon at its tail, `U^{ab}` vanishes: `r^{tail\dagger}_b` either kills it or makes two tail rishons, and `r^{head}_a` then meets an empty head. So `T_γ` vanishes unless all `h_i=1`, and its range lies in all `h_i=0`. On the all-heads vector with colours `c_1,…,c_{n-1}` at the inner sites and `j'` at `y`, each factor gives `U^{a_ia_{i-1}}_{ℓ_i}|head,c_i⟩=-δ_{a_ic_i}|tail,a_{i-1}⟩` (one anticommutation inside the link). The sum over `a` gives `(-1)^nδ_{jj'}` times the all-tails vector with colour `k` at `x` and colours `c_i` at the `z_i`. Under `W_γ` this is `(-1)^n|X,k⟩⟨Y,j|⊗1`. On the coarse link, `U^{jk}|Y,j'⟩=-δ_{jj'}|X,k⟩`. □

So on `P=∏_γP_γ` the decimation is an equivariant `*`-homomorphism of the whole coarse algebra, and its restriction to `𝔄₁^G` lands in `P𝔄^GP`. The infinite product `P` is not in `𝔄`. A local version `ι(A)P_{R₁}` (product over the paths of the support region `R₁`) depends on `R₁`, so it is not one map. The construction must therefore be extended to the defect sectors `1-P_γ`.

**Lemma F (end numbers cannot stay at the representatives).** Let `m=m₁`, `1≤m≤9`. There is no unital `*`-homomorphism `Φ:𝔄₁^G→𝔄^G` such that, for one coarse link `ℓ=(X,Y)` and a fine path from `x` to `y` with `n≥2` links, `Φ(f(p^ℓ_X))=f(p_x)` and `Φ(f(p^ℓ_Y))=f(p_y)` for every function `f` on `P_m`.

*Proof.* End numbers are gauge invariant, so `p^ℓ_X,p^ℓ_Y∈𝔄₁^G`. Let `s=\min P_m`. On the coarse link `p^ℓ_X+p^ℓ_Y=m`, and `2s=m` has no solution for `1≤m≤9` (`s=0` needs `m=0`; `s=m-5` needs `m=10`). So `[p^ℓ_X=s][p^ℓ_Y=s]=0`. Its image is `[p_x=s][p_y=s]`, a product of nonzero projections on different link factors, which is nonzero. □

**Lemma F′ (a link constraint needs shared fine support).** Let `Φ` satisfy (INV-1). Let `P,P'∈𝔄₁^G` be projections with `PP'=0`. If `Φ(P)∈𝔄(R_1)` and `Φ(P')∈𝔄(R_2)` with `R_1,R_2` sharing no site or link factor, then `P=0` or `P'=0`.

*Proof.* Invariant elements are even (`ZM1_OBS.md` Theorem 3). In a finite region containing `R_1∪R_2`, order the Jordan-Wigner modes with `R_1` first. An even element of `𝔄(R_2)` then acts as `1⊗Q⊗1`, because its Jordan-Wigner strings through `R_1` occur in pairs and cancel. So `Φ(P)Φ(P')=(Q_1⊗1)(1⊗Q_2)`, which is zero only if `Q_1=0` or `Q_2=0`. Injectivity gives `P=0` or `P'=0`. □

So in any finite-range solution of K-INV, the images of `[p^ℓ_X=q]` and `[p^ℓ_Y=q']` (with `q+q'≠m₁`) share fine support. The coarse link constraint must be carried by fine factors that both images touch.

**Attack 3 fails at** "the good-sector decimation extends to a unital map on `1-P_γ` that keeps each coarse end number at its representative" (Lemma F). Extension by zero on `1-P_γ` is not unital. Other extensions must move the coarse end-number data off the representatives onto shared fine factors (Lemma F′); none is constructed here.

### 5.5 Where K-INV stands

K-INV`(m,m₁,L)` is open. Three distinct attacks failed, each at a named step:
1. neutral matrix registers fail at "a local invariant algebra contains a unital `M_D`" (Lemma N);
2. decimation with equivariant links fails at "a fine path of two or more links carries a coarse link equivariantly" (Lemma E, Corollary E1);
3. good-sector decimation fails at "coarse end numbers stay at the representatives on the defect sectors" (Lemma F).

What a solution must do, from Lemmas N, E, F and F′: it must have no local matrix registers; it must not carry coarse links equivariantly on paths; and the two end-number projections of each coarse link must have images with common fine support. By Theorem R, a solution for even `m` and even `m₁` would prove ZM1-I1[INV] at once, in the locked vacua, and a proof that K-INV fails would refute ZM1-I1[INV] for every vacuum and update.

## 6. What the invariant-only map carries

The owner's text: "Impose no map on charged fields or Gauss generators." Here is what a solution `Φ` of ZM1-I1[INV] would and would not hand on. Each line is a consequence of the definitions and the cited frozen results, not a new claim of existence.

- **Its domain.** `𝔄₁^G` is even (`ZM1_OBS.md` Theorem 3). It contains the central charges `Q_X` (`VC1_5.md` Theorem 5.3 proof: "Each `Q_x` belongs to the centre of `A^gauge`"), so `Φ(Q_X)` is defined. No condition ties `Φ(Q_X)` to any fine Gauss charge. Traceless generators `\mathcal G^T_X` are not invariant and lie outside the domain. So the coarse Gauss law has no fine reading through `Φ`.
- **LZ1-i.** Class (a) compares truncated invariant two-point values. By `ZM1_OBS.md` Theorem 4, complete exact data fix the centered physical-sector tick and translation representation. With errors, it gives Lemma ER (tail lengths and amplitudes) and, under the summability, phase and weight hypotheses of `ZM1_OBS.md` Theorems 8′ and 9′, branch matching for composites in the image of `Φ`. It does not give a common speed across species (`ZM1_OBS.md` section 5.1: the rate "does not by itself prove speed transfer"). In a character vacuum `H_phys=CΩ` (Corollary C3), so LZ1-i has no band to test there.
- **GA2.** Wilson loops of bounded size are local invariant elements and lie in the domain. Class (a) fixes the support radius `R₀` before the constant `C_{R₀}`, so it does not control loops whose size grows with the separation (class (b) of `ZM1_OBS.md`, not adopted). A comparison with continuum Yang-Mills still needs a dictionary and propagated errors (`ZM1_OBS.md` section 5.1). `Φ` gives the operator-side correlator data only.
- **R-CS^str.** A finite charge-anticharge string is an invariant local element, so its image is defined and class (a) compares it at each fixed `R₀`. The straight-string limit needs control uniform in the string length; class (a) allows `C_{R₀}` to grow with `R₀`, so the limit is not carried.
- **MT1-S and CG1's `16`.** Odd elements are not in `𝔄₁^G`. No odd or charged field has an image. These consumers get no zoom from `Φ` and need a separate bridge, as the owner's text says.



## 7. Readings for the owner, four-tested

Theorem R shows that, if the VC1 fine vacuum is a locked witness, the comparison is empty and ZM1-I1[INV] is K-INV. The owner may want the question to have content in the vacuum. Three candidate readings follow. None is adopted. Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its reasons do not need.

- **R-V (pose ZM1-I1[INV] in the vacuum VC1 selects, once VC1 is decided).** This is the owner's own wording, "the specified VC1 fine vacuum", made explicit. (1) P: no target value. (2) P: one vacuum, once named. (3) P: it assumes nothing about that vacuum. (4) P: nothing added. *Effect:* until VC1 names a vacuum, ZM1-I1[INV] is posed only up to that choice; if VC1 names a locked witness, Theorem R applies.
- **R-NC (exclude vacua whose restriction to `𝔄^G` is a character).** (1) C: it states a property of VC1's vacuum. (2) P. (3) **F**: by Corollary C3 it requires `H_phys≠CΩ`, that is, gauge-invariant excitations in the vacuum, which is part of VC1(1)'s target ("massless gauge and graviton modes"). (4) P. *Fails test 3.*
- **R-ALL (require the bound in every P-witness VC1 supplies).** (1) P. (2) **F**: the set of witnesses grows as VC1 work proceeds (`VC1_5U_ODD.md` adds ice witnesses under ICE-T), so a part can add to it. (3) P. (4) C. *Fails test 2.*

Recommendation: no reading is needed to state the results above. R-V is the only candidate that passes all four tests, and it restates the owner's text.



## FINISH

No `[check]` was run; every step above is a written proof in finite-dimensional algebra.

**Proved (pass 1, author-side, unrefereed).**
- Theorem C1: on `L5-U[2k]` the locked P-witnesses of `VC1_5.md` Theorem 5.5 (empty and full matter) restrict to characters of `𝔄^G`. Theorem C1-O: the same for the `L5-O` witnesses of `VC1_5.md` Theorem 4.2. This strengthens `ZM1I1A.md` Theorem 8 (darkness).
- Corollary C2: if both vacua are characters on the invariant algebras and invariant under gauge-commuting updates, class (a) holds for every unital `*`-homomorphism `Φ`, with every `p` and constant; no locality is needed. Corollary C3: in a character vacuum `H_phys=CΩ`.
- Theorem R: for the locked vacua and the base tick, ZM1-I1[INV] holds with an even coarse `m₁` if and only if K-INV`(m,m₁,L)` holds for some `L≥2` and even `m₁` (coarse `L5-O` for `L5-O`). For every vacuum and update, ZM1-I1[INV] implies K-INV.
- Lemma T: `𝔄^G(R)` has at least two tracial states, so the trace-transfer step of `ZM1I1A.md` Theorem 1 has no analogue.
- Lemma N (no unital matrix register in a local invariant algebra; even `m`, `L5-O`); Lemma E and Corollary E1 (no equivariant carriage of a coarse `L5-U` link by a fine path of two or more links; none of one link under covariance with `L≥2`); Lemma S (on its good sector an `m=1` path is exactly an `m₁=1` coarse link, with the Wilson line as `U^{jk}`); Lemma F (coarse end numbers cannot stay at the representatives); Lemma F′ (the two end-number images of a coarse link must share fine support, for finite range).

**Counterexamples.** None to ZM1-I1[INV]. Lemmas N, E and F refute three specific constructions, not the statement.

**Open by name.**
- **K-INV(m, m₁, L)**: a cell-covariant, exponentially local, unital injective `*`-homomorphism `𝔄₁^G→𝔄^G` with `L≥2`. Three distinct attacks failed: neutral matrix registers (at Lemma N), decimation with equivariant links (at Lemma E and Corollary E1), good-sector decimation (at Lemma F). By Theorem R, K-INV for even `m` and even `m₁` is ZM1-I1[INV] in the locked vacua.
- **K-INV-O**: the same on `L5-O`; Lemma E does not apply there (end parities, no corner).
- **ZM1-I1[INV] in non-character vacua**: the R2 mixture, the swap-band states, the two-band states and the ice states (under ICE-T). Each needs K-INV and a coarse law that reproduces every nonzero invariant tail in the image of `Φ` exactly (Lemma ER).
- Inherited and unchanged: VC1 (which vacuum; R-V is offered in section 7), ICE-T, LZ1-i[ZM1a], ZM1-G, Y1, H-BLOCK, R-CS, MT1-S.

**What changes downstream.**
- ZM1 and ZM1(a)1: in the locked vacua the owner's comparison is empty, and the invariant-algebra route is exactly the kinematic question K-INV. Any lane on ZM1-I1[INV] should work K-INV first; the three failed attacks and Lemma F′ say what a solution must avoid.
- VC1: the locked witnesses have one-dimensional physical space (Corollary C3). If VC1(1)'s "massless gauge and graviton modes" must be vectors of the vacuum's own `H_phys`, no locked witness is the VC1 vacuum. This is a conditional observation for VC1 lanes, not a VC1 result.
- LZ1-i and GA2: they get nothing from a locked vacuum. In other vacua they get invariant correlator data with exact tail matching (Lemma ER) and conditional branch matching, not a common speed and not large loops (section 6).
- Charged sectors (R-CS, MT1-S, CG1's `16`) and Gauss generators get no zoom from `Φ`, as the owner's text says; finite strings get images at fixed `R₀` only.
- No axiom, working-set entry, reading or frozen file changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
