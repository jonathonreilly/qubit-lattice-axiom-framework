lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5O-E′ referee report (pass 3): loop data and heat-kernel models

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). The lane ran in a pass-1 slot of the run, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). Its task was pass 3, the referee, of `CH1_5OEP.md`. This session wrote neither pass 1 (`CH1_5OEP_DRAFT.md`) nor pass 2 (`CH1_5OEP.md`). This is one check: one line-by-line read of `CH1_5OEP.md`, with the draft read wherever `CH1_5OEP.md` cites it. No other review was read or reviewed.

**What this file is.** A referee report. It grants no status. It adopts no law, reading, class, register or normalization. It changes no axiom or working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. It edits no other file. A "referee closure" (R-Z, R-HK, R-T, R-C, R-S, R-U in section 4) is a complete short argument written here. It is unrefereed.

**Text read.** `CH1_5OEP.md` as of commit `8311a7d7e` (the last commit that touches it; unchanged at branch head `c2bfcd143` when this file was written). SHA-256 of the file read: `2824e4b8f778c7a6f46147613d077b4f7c5bd3e493fd1b9038a0bcac9171f7a3`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), at the start of the run | `8311a7d7e` |
| same checkout, after other lanes moved its HEAD during the run (no file read here changed) | `c2bfcd143` |

No other branch was read.

**Files read, by line.** `AGENTS.md` lines 1-27. `docs/ai_methodology/SCIENCE_WORKFLOW.md` lines 1-293. This folder: `CH1_5OEP.md` lines 1-136 (all); `CH1_5OEP_DRAFT.md` lines 1-330 (all); `LW1_REFEREE.md` lines 1-80 and its section headings (format only); `Y2W_DRAFT.md` lines 1-40 (head format), 50-60 (T0-start's class, Definition SC) and 74-78 (four-test rows); frozen `CH1_5OE.md` lines 1-182 (all); `CH1_5O.md` lines 17-22 (Definition 1), 104-116 (Theorems 11-12), 140-146 (R5 to R5.3), 157-159 (R8) and 162-176 (the four tests, CH1-5O-i, CH1-5O-E); `GA2_Y2.md` lines 1-40 and 160-169; `LW1_5.md` lines 28-40, 60-100 (the laws, free data), 118-136 (Q and G, R) and 250-260 (B1-5); `VC1_5.md` lines 18-40; `CH1.md` lines 13 and 34, found by grep; `TOE_ASSEMBLY.md` lines 212-214 (§3.5), found by grep. SHA-256 prefixes: `CH1_5OEP_DRAFT.md` `c33bb719917f3772`, `CH1_5OE.md` `70dbb28f246343dd`, `CH1_5O.md` `053f1ecf4da057b4`, `LW1_5.md` `7afb7ee2a52d91cd`, `VC1_5.md` `7461113c411eeda4`, `GA2_Y2.md` `25db8a18aff1d30f`, `Y2W_DRAFT.md` `f9d8db9c15b4b101`, `CH1.md` `633e4aa4eed86d1e`, `TOE_ASSEMBLY.md` `8027d9d44eb5fcaf`. Where `CH1_5OEP.md` line 11 records a hash, it matches.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law, the update class, the frozen CH1-5O-E′ and its classes are read plainly. Where the record leaves a choice open, this report names it. One optional normalization rule is put through the four tests (section 6). Nothing is adopted.

**Working set used, by name.** PS-5, PS-6 and PS-6r, only through the laws of `LW1_5.md`: `L5-O` with its free datum `R`, and `L5-U` for Theorem 6's last clause. PS-1c, only through the cell lifts. LW1's conjugation reading of gauge invariance (`LW1_5.md` line 35: "Gauge invariance means invariance under conjugation, not necessarily a zero Gauss-charge sector"). PS-7r, only through its sentence "the vacuum is the state VC1 builds", for CH1-5O-E′[VC1]. No other entry.

**Inputs from outside the working set.** Results of this part, each quoted at its point of use: `CH1_5O.md` Definition 1, Theorems 11-12, R5 (rebuilt in R-Z) and R8; `LW1_5.md` "Q and G" and B1-5; `VC1_5.md` Theorem 2.1, Theorem 2.2 and the cell group; frozen `CH1_5OE.md` Definitions 1, 5 and 6 and CH1-5O-E′. Standard mathematics rebuilt here: Clifford relations; uniqueness of the tracial state of a full matrix algebra; Lagrange interpolation; the finite-dimensional double commutant theorem; the heat-kernel measure on a compact matrix group, through convolution powers of a Gaussian step. Standard mathematics cited inside those rebuilds: Schur's lemma, Haar measure, the Stone-Weierstrass theorem, the Riesz-Markov theorem, weak-* compactness of the probability measures on a compact metric space, and Gaussian moments. Literature context, credited and never load-bearing: Evertz, Jansen and Kastrup (Phys. Lett. B 194 (1987) 277) and Kovács and Tomboulis (hep-lat/9806030), on reflection positivity of lattice gauge measures; the credits of `CH1_5OEP.md` line 11 and of the draft's line 26.

**Literature search (this lane, time-boxed).** The draft's record (`CH1_5OEP_DRAFT.md` line 28, three searches) was read and reused. Two more standard web searches ran on 2026-11-06: (1) Gauss-law-sector traces, infinite temperature and Wilson loops; (2) heat-kernel lattice measures with independent links and reflection positivity. Neither found a statement of Theorem 6 or of R-Z. Neither found a check of independent-link models against a small-field class. They found the two reflection-positivity papers credited above.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false or unsupported line, quoted, with a fix); INCOMPLETE (a named missing step, with the step). `[check]` marks one scratch computation: `/tmp/toe-ch15oepref/check.py`, output `/tmp/toe-ch15oepref/out.txt`, 25 s, peak resident memory 510 MB, floating point, started after `memory_pressure` showed 65 percent free. `scripts/lab_ops.py` (the preflight and numeric lock of `SCIENCE_WORKFLOW.md` §10) is absent from this sparse checkout, so that preflight did not run. A check guides and never proves.

**Counts.** 56 items: 47 CORRECT, 6 ERROR, 3 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. The distiller marks three GAP claims. One is real (G1, the classes). Two are not gaps (G2, temporal loops; G3, the dark state).

---

## 1. Verdict table

| # | Item (`CH1_5OEP.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Title (1) | CORRECT | |
| 2 | §0 "Proved under the stated inputs" list (5) | CORRECT | Each listed result is proved below. R-HK and R-T rebuild the cited heat-kernel and trace inputs. |
| 3 | §0 GAP, membership of the model classes (7, sentences 1-3) | CORRECT | Gap real (G1). Wording: "the non-simple extension" plays no role for `SU(5)` and `Spin(10)`; the draft cites the positive densities, it does not prove them. Edit E1. |
| 4 | §0 GAP, spatial loops only (7, sentence 4) | ERROR | True as a description, wrong as a gap (G2). The frozen list holds equal-time invariant operators. Edit E1. |
| 5 | §0 corrected statement and the `S_+` remark (7, sentences 5-6) | CORRECT | The draft says the same of `S_+` (line 323). |
| 6 | §0 Open list (9) | CORRECT | Frozen `CH1_5OE.md` line 5's list, plus CH1-5O-E′[VC1], HEAT and SEP[T0-start]. |
| 7 | §0 Provenance (11) | CORRECT | The three recorded hashes and the HEAD commit check out. |
| 8 | Definition 1 (15) | CORRECT | |
| 9 | Definition 2 (16) | INCOMPLETE | B1-5 and `VC1_5.md` Theorem 2.2 state the lifts for `S_+`. The step to `R_k^-` is missing. Edit E5. |
| 10 | Definition 3 (17) | CORRECT | The factor `1/k` is defined on `R_k^-` only. Optional rule O1. |
| 11 | Definition 4 (18) | CORRECT | (b′) is per measure, as in frozen `CH1_5OE.md` line 167. |
| 12 | Definition 5 (19) | CORRECT | |
| 13 | Definition 6 (20) | ERROR | Wrong file. The `W = 0` reading is in `CH1_5OE.md` (Definition 6, line 22; R-E′ row, line 165), not in `CH1_5O.md`. Edit E4. |
| 14 | Theorem 1, statement (24-33) | CORRECT | `[check]` (1a)-(1g), at `k = 1` and `k = 2`. |
| 15 | Theorem 1 proof, first paragraph (35) | CORRECT | |
| 16 | Theorem 1 proof, second paragraph (37) | CORRECT | |
| 17 | Theorem 1 proof, third paragraph (39) | INCOMPLETE | The end-swap step stops before the image is shown to be a coherent ray. R-S supplies the step. Continuity rests on cited local sections; R-C replaces them. Edit E6. |
| 18 | Theorem 2, statement (43-48) | CORRECT | |
| 19 | Theorem 2 proof, first paragraph (50) | CORRECT | Continuity by R-C. |
| 20 | Theorem 2 proof, second paragraph (52) | CORRECT | |
| 21 | Theorem 2 proof, third paragraph (54) | ERROR | `J` is used and never defined. Trace invariance by R-T. Edit E3. |
| 22 | Theorem 3, statement (56) | CORRECT | |
| 23 | Theorem 3, proof (58) | CORRECT | |
| 24 | Scope paragraph after Theorem 3 (60) | CORRECT | |
| 25 | Definition of `p_t` and of `RL(G;σ_*)` (64) | CORRECT | R-HK rebuilds existence and the Fourier formula. The density sentence is cited; no proof uses it. |
| 26 | Theorem 4, statement (66-77) | CORRECT | `[check]` (2a), (2b), (3a), (3b). |
| 27 | Theorem 4 proof, `so(10)` (79) | CORRECT | |
| 28 | Theorem 4 proof, `su(5)` (81) | CORRECT | |
| 29 | Theorem 4 proof, separation (83) | CORRECT | Its last step is the mean value theorem. |
| 30 | Numbers and the variance ratio (85) | CORRECT | `[check]` (4). |
| 31 | Theorem 5, first part (87) | CORRECT | |
| 32 | Theorem 5, model part (89-94) | CORRECT | |
| 33 | Theorem 5 proof, first paragraph (96) | CORRECT | Optional wording O3 (the time slice). |
| 34 | Theorem 5 proof, second paragraph (98) | INCOMPLETE | "Choose `s` in the displayed range" must also require `s²(840−31775s)/64800 > δ`. Edit E7. |
| 35 | Concrete instance (100) | CORRECT | `[check]` (5). |
| 36 | GAP at 102, sentence 1 | CORRECT | Gap real (G1). |
| 37 | GAP at 102, sentence 2 | ERROR | The draft makes no "assertion for an arbitrary four-dimensional list" (G2). Edit E2. |
| 38 | GAP at 102, sentence 3 | CORRECT | Correct once sentence 2 is removed. |
| 39 | Corollary 5.1, statement (104) | CORRECT | |
| 40 | Corollary 5.1, proof (106) | CORRECT | The state of Theorem 5's proof already has `d_Λ(ω,C(K)) ≤ η < δ < d_Λ(ω,C(G))`. |
| 41 | §5 introduction (110) | CORRECT | |
| 42 | Four-test row, the update class (114) | CORRECT | The referee agrees with the marks. |
| 43 | Four-test row, `RL(G;σ_*)` (115) | CORRECT | `σ_*` plays the part of `g_*`, which the frozen data already carry. |
| 44 | Four-test row, `R_k^-` (116) | CORRECT | |
| 45 | CH1-5O-E′[VC1] (118) | CORRECT | A proposed open question. Its four-test status is that of SC in `Y2W_DRAFT.md` line 76. |
| 46 | C1 (120) | CORRECT | |
| 47 | C2 (122) | CORRECT | `[check]` (C2), at `k = 1` and `k = 2`. |
| 48 | C3 (124) | CORRECT | The connected correlation is exactly zero. This is sharper than the draft's `< 6ε` and true. |
| 49 | C4 and HEAT (126) | CORRECT | |
| 50 | Theorem 6, statement (128) | CORRECT | `[check]` (1h). R-U shows the `L5-U` condition holds. |
| 51 | Theorem 6, proof (130) | CORRECT | |
| 52 | Conditional failure as in R8 (132, sentences 1-2) | CORRECT | |
| 53 | GAP at 132, the dark state (132, sentence 3) | ERROR | Not a gap (G3). `CH1_5O.md` R5 holds on every finite region; R-Z gives the Gauss-trace form there. Edit E8. |
| 54 | Vanishing loops do not prove HEAT (132, sentence 4) | CORRECT | |
| 55 | SEP[T0-start] (134) | ERROR | "This reduction is sufficient, not necessary" asserts an unproved non-necessity. "spatial/temporal" points to the non-gap G2. Edit E9. |
| 56 | Closing paragraph (136) | CORRECT | |

## 2. The distiller's GAPs

`CH1_5OEP.md` marks GAP at three places: line 7, line 102 and line 132. Lines 7 and 102 make the same two claims, G1 and G2. Line 132 makes G3.

### G1. The model classes are not shown to be T0-start's classes. Real.

Line 7: "It proves positivity of finite-window densities and small heat-kernel time, but does not check the full T0-start conditions, including reflection positivity and the non-simple extension. Thus its model witness does not close the frozen CH1-5O-E′." Line 102: "The preceding theorem proves separation for the named random-link models, not membership in T0-start's class or satisfaction of every frozen small-field condition."

**What the draft claims.** Draft line 54: "Theorem W(ii) pins the 'precisely defined pure-gauge small-field classes' by model classes, and Lemma HK proves their separation." Draft line 238: "Then CH1-5O-E′ holds for these data." The draft also marks the limit itself. Draft line 48: "CH1-5O-E′ holds when heat-kernel model classes stand in for T0-start's". Draft line 263, test (3) for `RL(G; σ_*)`: "pass as a model; fails as a stand-in for T0-start's class, which is what GA2 needs". So the draft proves the lemma for data it pins itself.

**What the record asks.** Frozen `CH1_5OE.md` line 167 fixes the data first: "For fixed `r`, `Λ_r`, standard maps, nonempty precisely defined pure-gauge small-field classes and `δ`, ask for an `L5-O` update and a stationary, cell-symmetric gauge-invariant state". Line 22, Definition 6, names the intended classes: "R-E′ proposes pure-gauge T0-start small-field classes for both sides ... The intended T0-start class requires a Haar density and further conditions, including reflection positivity. Its non-simple extension, normalization, existence and precise admissibility remain to be pinned." Line 165: "Pinning is not yet done". `Y2W_DRAFT.md` line 54 quotes T0-start's class: "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`".

**Verdict.** The gap is real. Pinning the classes is the owner's step, and the record intends T0-start's classes. The draft does not show that `RL(K;σ_*)` or `RL(G;σ_*)` lies in that class. Unchecked: reflection positivity, and density in `𝒜_{k0}(g)` at `g ≤ g_*`. Moreover, T0-start's class for `SU(5)` and `Spin(10)` is itself a request, T0-start[G]. T0 is stated for Wilson `SU(2)`, and `GA2_Y2.md` line 169 says: "SU(5), SO(10), matter, anisotropy and matching are separate extensions". `𝒜_{k0}(g)` is not defined in any file read here, so this report does not decide membership.

**Wording.** "The non-simple extension" plays no role here. Both groups, `SU(5)~` and `Spin(10)`, are simple and connected. Frozen line 167 needs that extension only for "non-simple groups, disconnected components and abelian factors". The draft cites the positivity of the densities (draft line 26, "the heat-kernel probability measure `p_t` ... cited, not rebuilt"); it does not prove it. No theorem uses that positivity.

**Repaired statement.** Theorem 5 as written (lines 87-94) is the correct model statement. With T0-start's classes, Theorem 5's first part reduces CH1-5O-E′ to SEP[T0-start] (line 134, with edit E9). Replacement texts are edits E1 and E2.

### G2. Spatial loops only. Not a gap.

Line 7: "Its comparison is also constructed for spatial equal-time skeleton loops; it does not construct observables for arbitrary spacetime loops of rℤ⁴." Line 102: "Also, the construction maps only spatial loops to one time slice; the assertion for an arbitrary four-dimensional list has no supplied temporal-link construction."

**The draft makes no such assertion.** Draft line 76: "Here `C_b` is the block path of `C`, read in one time slice." Draft line 232, Theorem W(ii): "any finite list `Λ` of skeleton loops that contains a block plaquette `p`". A skeleton loop is a closed path of fine spatial links (draft line 76: "It is a closed path in the sense of 1.1").

**The record asks for no temporal loop.** The list consists of framework observables. `CH1_5O.md` line 175: "The finite invariant observable list `Λ_r` contains vector block plaquettes". Frozen `CH1_5OE.md` line 18, Definition 2: "`A` is the quasi-local algebra of a fixed `L5-O` update `α`; `A^G` is the subalgebra fixed by all local gauge transformations." Every element of that algebra is an equal-time operator on the spatial lattice. No file read here defines a temporal link operator or a temporal loop observable. A spatial loop maps to the same loop in one time slice of `rℤ⁴`. Each `RL` measure is invariant under all lattice translations of `rℤ⁴`, so the slice does not matter.

**Verdict.** Not a gap. The scope limit that does exist is already a hypothesis of Theorem 5: the list must consist of skeleton loops in the vector representation, each using each block link at most once. Edits E1 and E2 remove the clause.

### G3. The dark state and the Gauss-trace form. Not a gap.

Line 132: "The draft's assertion that the dark state has the required finite-region Gauss-trace form uses a global multiplicity-one argument without establishing its boundary-region restrictions: **GAP** at that inference."

**What the draft argues.** Draft line 288: "`CH1_5O.md` R5 (line 140) proves that every gauge-invariant `T` maps the dark vector `u_S` into its own line. The gauge-invariant operators act on each isotypic component of the gauge representation as the full algebra of its multiplicity space. So the component of `u_S` has multiplicity one, and `ω_0` is the normalized trace over it."

**R5 is local, not global.** `CH1_5O.md` line 140: "Let `S` be a finite set of sites, `𝔄_S` the algebra of the matter at `S` and of the links with both ends in `S`, and `u_S` the vector of `Φ₀` on `𝔄_S` ... Every `T ∈ 𝔄_S` that commutes with every gauge unitary `V_x(g)` satisfies `T u_S = Φ₀(T) u_S`." For `S = Λ`, `𝔄_S` is exactly the region algebra of Theorem 6. So the draft's argument runs on each finite region. It needs no boundary statement.

**What the draft does omit.** Two short steps: the computation of `ω₀` on the region as a normalized trace, and the membership of the projection in `𝔊_Λ`. R-Z (section 4) supplies both, with R5 rebuilt. **Verdict.** Not a gap. Edit E8 replaces the GAP sentence by R-Z's statement.

### The `S_+` remark (line 7, last sentence)

"A large-register limit does not establish the same result for `S_+`." This is correct, and it is not a gap in the draft. Draft line 323 says the same: "a fixed small register such as `S_+`, where Theorem U gives nothing".

## 3. Details of the non-CORRECT items

Items 4, 37 and 53 are G2 and G3 of section 2.

### 3.1 ERRORS

**Item 13 (line 20).** "`CH1_5O.md` explains that embedding the pure-gauge version in CH1-5O-E also depends on the `W=0` reading." A grep of `CH1_5O.md` finds no `W = 0`, no "pure gauge" and no "pure-gauge". The reading is in frozen `CH1_5OE.md`. Line 22: "So R-E′ instantiates the frozen specification if a gauge-Higgs comparison class may have `W = 0`; the frozen text does not say, and the owner may specify." Line 165: "whether pure gauge is admissible in frozen CH1-5O-E turns on the `W = 0` reading". Fix: edit E4.

**Item 21 (line 54).** "For each reversed coordinate direction put `σ_x=(−1)^{Σ_{i∈J}x_i}`." `J` appears nowhere else in `CH1_5OEP.md`. The sentence also reads as one sign per direction, while `σ_x` is one sign built from all of `J`. The draft defines `J` (line 160): "The reversed image links are exactly the links in the directions `i ∈ J := {π(j) : ε_j = −1}`", for linear part `Qe_j = ε_je_{π(j)}`. The sign check holds with that `J`: for `ℓ = (x, x+e_i)`, `Σ_{j∈J}(x_j + (x+e_i)_j) = 2Σ_{j∈J}x_j + [i∈J]`, so `σ_xσ_{x+e_i} = −1` exactly when `i ∈ J`. Fix: edit E3.

**Item 55 (line 134).** "This reduction is sufficient, not necessary." The file proves sufficiency (Theorem 5, first part). It proves no case where CH1-5O-E′ holds and SEP fails. The necessary condition that does follow is weaker than SEP: if `d_Λ(ω,μ) ≤ δ` and `d_Λ(ω,μ′) > δ`, then `d_Λ(μ,μ′) > 0`. The same line's "subject to the spatial/temporal and class identifications" points to G2, which is not a gap. Fix: edit E9.

### 3.2 INCOMPLETE

**Item 9 (line 16).** "A cell lift on a reversed link exchanges ends and sends `U^{ab}` to `−U^{ba}`. These action and lift identities, and the gate commutation facts, are inputs from `LW1_5.md` and `VC1_5.md`." The cited statements cover `S_+` only. `LW1_5.md` line 255: "For `L5-O` with `S_+`, the dressed tick is also cell covariant." `VC1_5.md` line 31: "`L5-O[S_+]` has five matter modes per site". Theorems 2 and 5 use the lifts on `R_k^-`. The missing step is short, and the draft gives it (line 90: "That argument uses only the Clifford relations and the spin lift of the end swap. With `τ_E = 0` it applies to every register `R`."). The end swap `s̃ = ∏_a(η^y_a−η^x_a)/√2` is a product of ten unit Clifford vectors, so `s̃ ∈ Spin(20)`, and it acts on every `Spin(20)` register. B1-5's proof uses nothing else of `S_+` except the electric layer, which is absent at `τ_E = 0`. The proof of `VC1_5.md` Theorem 2.1 (line 37) uses only that "Gates commute with Gauss generators and lifts permute gauge sites". Fix: edit E5.

**Item 17 (line 39).** "It maps `φ₀` to the unique all-minus joint eigenvector, the same ray as `ϖ` at one end. This proves the last transformation." Two steps are missing: conjugation by `s̃` moves the target-end rotation `h` to the source end, and a source rotation of `ρ_k(ϖ_y)φ₀^{⊗k}` must be shown to be a coherent ray with mean `−kO^T`. R-S gives both, as the draft does (line 127). The same paragraph's "local sections give continuity" cites local sections of the covering map; R-C proves continuity without them. Fix: edit E6.

**Item 34 (line 98).** "Choose `s` in the displayed range and `σ=5s/48`. ... Theorem 4 separates its first two moments from those at every full-group heat-kernel time by more than `δ`." Separation by more than `δ` needs `Θ ≥ s²(840−31775s)/64800 > δ`, not only `s` in the range. Such `s` exists because `δ` is below the supremum. The draft says so (line 242: "Pick `s` in the stated range with `(s^2/64800)(840 − 31775s) > δ`"). Fix: edit E7.

### 3.3 Notes on CORRECT items that bear on the freeze

**Item 3.** The membership gap is real; only its wording needs edit E1 (section 2, G1).

**Item 10.** `Ŵ_C` carries "one factor `1/k` for each link". The number `k` exists only on `R_k^-`. The frozen data are fixed before the update, and the update includes the register. Theorem 5 is still a correct statement: its list is a list of paths, normalized on the chosen register. A register-independent rule is optional O1 (section 6, with its four tests).

**Item 25.** "On a finite window these have positive smooth Haar densities." No proof in `CH1_5OEP.md` uses this sentence. It bears only on G1. The load-bearing heat-kernel facts are existence, the Fourier formula, the semigroup law and inversion invariance; R-HK rebuilds them.

**Item 40.** The proof of Corollary 5.1's last claim needs a state with `d_Λ(ω,C(K)) < d_Λ(ω,C(G))`. Theorem 5's proof takes `η < δ` and `η` below the margin `d_Λ(μ,C(G)) − δ`. Then `d_Λ(ω,C(K)) ≤ d_Λ(ω,μ) ≤ η < δ`, and `d_Λ(ω,C(G)) ≥ d_Λ(μ,C(G)) − η > δ`. So no extra condition such as the draft's `η < Θ/2` is needed.

**Item 48.** Line 124: "In the product-link model, gauge-invariant loops on disjoint link sets factor exactly before and after averaging; their connected correlation is zero." Proof. Let `C, C′` use disjoint sets of fine links and let `ν = λ^{⊗L}`. For each `u`, `Φ_u` is a product state over links, so `Φ_u(Ŵ_CŴ_{C′}) = Φ_u(Ŵ_C)Φ_u(Ŵ_{C′})`. The two factors depend on disjoint coordinates of `u`, which are independent under `ν`. So `ω_ν(Ŵ_CŴ_{C′}) = ω_ν(Ŵ_C)ω_ν(Ŵ_{C′})`. `E` fixes gauge-invariant elements, so the same holds for `ω`. ∎ The draft's bound (line 280, "at most `3ε + 2ε + ε^2 < 6ε`") is true and weaker.

**Item 50.** Line 128: "The analogous conclusion holds for `L5-U` if an end-central `U(1)` acts on each link factor by a nontrivial phase." R-U shows the condition holds for `L5-U` as `LW1_5.md` specifies it. The clause may drop its "if" (optional O2).

## 4. Referee closures

Each closure is complete as written. Each is unrefereed.

### R-Z. The dark state is Gauss-tracial on every finite region (repairs G3)

**Statement.** On `L5-O[S_+]`, let `Φ₀` be the dark product state (matter Fock vacuum, rishon vacuum on each link) and `ω₀ = Φ₀∘E` (`CH1_5O.md` Theorems 11-12). Let `Λ` be a finite set of sites, with `ℋ_Λ` and `𝔊_Λ` as in Theorem 6, and let `u_Λ` be the vector of `Φ₀` on `ℋ_Λ`. Let `Q_Λ` be the orthogonal projection onto `𝔊_Λu_Λ`. Then `Q_Λ ∈ 𝔊_Λ`, and `ω₀(A) = tr(Q_ΛA)/tr(Q_Λ)` for every operator `A` on `ℋ_Λ`. So `ω₀` has the form of Theorem 6 on every finite region, with `Z_Λ = Q_Λ/tr(Q_Λ)`.

*Proof.* **Step 1 (`CH1_5O.md` R5 with `S = Λ`, rebuilt).** Fix `x ∈ Λ` and `j ∈ {1,…,5}`. The Gauss generator is `𝒢_x^{2j−1,2j} = M_x^{2j−1,2j} + Σ_{ℓ∋x}L^{2j−1,2j}_{ℓ,x}` (`LW1_5.md` line 83). Each term is `i/2` times the product of the two Majoranas of one mode, so it is that mode's number minus `1/2`: `n_{x,j} − 1/2` for the matter (`LW1_5.md` line 31: "`n_j−1/2=M^{2j−1,2j}`"), and `n^{ℓ,x}_j − 1/2` for the rishon mode `j` at the `x`-end of `ℓ`, by the same Clifford computation. Let `H_{x,j}` be the sum of the terms that act on `ℋ_Λ`, that is, the matter term and the links at `x` with both ends in `Λ`. The other terms act on links with one end in `Λ`, outside `ℋ_Λ`. An operator `T` on `ℋ_Λ` that commutes with every `V_x(g)` commutes with `e^{itH_{x,j}}` for all `t`, hence with `H_{x,j}`. Let `d_x` be the number of links at `x` inside `Λ`. Then `H_{x,j} + (1+d_x)/2` is a sum of commuting number operators. The joint kernel of all of them is the set of vectors of `ℋ_Λ` with every mode empty: each mode of `ℋ_Λ` is a matter mode at a site of `Λ` or a rishon mode at an end of a link inside `Λ`. The empty vector of a link has even rishon parity, so it lies in `S_+`. So the joint kernel is the line of `u_Λ`. `T` keeps this line, so `Tu_Λ = ⟨u_Λ,Tu_Λ⟩u_Λ`.

**Step 2 (the trace form).** Write `V(γ) = ∏_{x∈Λ}V_x(γ_x)` on `ℋ_Λ`, for `γ ∈ Γ := Spin(10)^Λ`. For `A` on `ℋ_Λ`, `E(A) = ∫_Γ V(γ)AV(γ)^*dγ`, since the parts of `V_x(g)` on links with one end in `Λ` commute with `A`. `E(A)` commutes with `𝔊_Λ`. Step 1 gives `E(A)u_Λ = λ(A)u_Λ`, with `λ(A) = Φ₀(E(A)) = ω₀(A)`. For `B ∈ 𝔊_Λ`, `E(A)Bu_Λ = BE(A)u_Λ = λ(A)Bu_Λ`. So `E(A)` acts on `K := 𝔊_Λu_Λ` as the scalar `λ(A)`. `K` is `𝔊_Λ`-invariant and `𝔊_Λ` is `*`-closed, so `Q_Λ` commutes with `𝔊_Λ`, hence with every `V(γ)`. So `E(A)Q_Λ = λ(A)Q_Λ` and `E(A)Q_Λ = E(AQ_Λ)`. Each conjugation by `V(γ)` keeps the trace, so `tr E(AQ_Λ) = tr(AQ_Λ)`. Hence `ω₀(A)·tr(Q_Λ) = tr(Q_ΛA)`, and `tr(Q_Λ) ≥ 1`.

**Step 3 (`Q_Λ ∈ 𝔊_Λ`).** Every `T` that commutes with `𝔊_Λ` maps `K` into `K`: `TBu_Λ = BTu_Λ`, a multiple of `Bu_Λ` by Step 1. The set of such `T` is `*`-closed, so `Q_Λ` commutes with it. So `Q_Λ` lies in the double commutant of `𝔊_Λ`, which is `𝔊_Λ` by the lemma below. ∎

**Lemma (double commutant in finite dimension).** Let `𝔐` be a unital `*`-subalgebra of the operators on a finite-dimensional space `ℋ`. Then `𝔐″ = 𝔐`. *Proof.* Let `X ∈ 𝔐″` and `ξ ∈ ℋ`. The subspace `𝔐ξ` contains `ξ` and is `𝔐`-invariant. `𝔐` is `*`-closed, so the projection `P` onto `𝔐ξ` lies in `𝔐′`. Then `Xξ = XPξ = PXξ ∈ 𝔐ξ`. Apply this to `ℋ^{⊕n}` with `n = dim ℋ`, to the algebra of diagonal copies `M⊕⋯⊕M` (`M ∈ 𝔐`), and to `ξ = (e_1,…,e_n)` for a basis `(e_i)`. The commutant of that algebra consists of the `n×n` matrices with entries in `𝔐′`, and `X⊕⋯⊕X` commutes with all of them. So `(X⊕⋯⊕X)ξ = (M⊕⋯⊕M)ξ` for some `M ∈ 𝔐`. That says `Xe_i = Me_i` for every `i`, so `X = M`. ∎

**Consequence.** With Theorem 6, R-Z gives `ω₀(W_C) = 0` for every closed path with distinct links inside a finite region. This agrees with `CH1_5O.md` Theorem 11. R-Z concerns one state. HEAT stays open.

### R-HK. The heat-kernel measure (rebuilds the input of Theorems 4 and 5)

**Statement.** Let `G` be `Spin(10)` or `SU(5)~`, with the inner product `⟨X,Y⟩ = −tr_10(XY)/2` on its Lie algebra `𝔤` (read through `R`). For each `t > 0` there is exactly one Borel probability measure `p_t` on `G` with `∫ρ dp_t = e^{−tC_ρ/2}` for every smooth finite-dimensional unitary representation `ρ`, where `C_ρ = −Σ_Adρ(T_A)^2` over an orthonormal basis `(T_A)`. Moreover `p_s∗p_t = p_{s+t}`, and `p_t` is invariant under `g ↦ g^{−1}`.

*Proof.* **Uniqueness.** `Spin(10)` acts faithfully and unitarily on the 32-dimensional spinor module of its Clifford algebra, and `SU(5)~ ⊂ Spin(10)` is closed. So `G` is a closed subgroup of a unitary group. The polynomials in the entries of this representation and of its conjugate form an algebra of continuous functions. It contains the constants, separates points and is closed under conjugation. By the Stone-Weierstrass theorem it is dense in `C(G)`. Each such polynomial is a linear combination of matrix coefficients of tensor products of the representation and its conjugate. So two probability measures with the same integrals of every `ρ` agree on a dense subset of `C(G)`. By the Riesz-Markov theorem they are equal.

**Existence.** Let `X = Σ_Aξ_AT_A` with independent standard Gaussians `ξ_A`, and let `μ_s` be the law of `exp(√s X)`. Each `Ad_g` is orthogonal for `⟨,⟩`, so the law of `X` is `Ad`-invariant. Fix an irreducible `ρ`. Then `M(s) := ∫ρ dμ_s = E[exp(√s dρ(X))]` commutes with `ρ(G)`, and so does `C_ρ`. By Schur's lemma, `M(s) = c(s)·1` and `C_ρ = κ·1`. For anti-Hermitian `Y`, `‖e^Y − 1 − Y − Y^2/2‖ ≤ ‖Y‖^3/6`, by the spectral theorem and `|e^{iθ} − 1 − iθ + θ^2/2| ≤ |θ|^3/6`. Also `E dρ(X) = 0` and `E dρ(X)^2 = −C_ρ`. So `c(s) = 1 − sκ/2 + r(s)` with `|r(s)| ≤ s^{3/2}E‖dρ(X)‖^3/6`. `X` and `−X` have the same law, so `c(s)` is real. The convolution power `ν_n := μ_{t/n}^{∗n}` has `∫ρ dν_n = c(t/n)^n·1`, which tends to `e^{−tκ/2}·1`. The probability measures on the compact metric space `G` are weak-* sequentially compact. A limit point `p` of `(ν_n)` has `∫ρ dp = e^{−tC_ρ/2}` for each irreducible `ρ`, since matrix coefficients are continuous. Complete reducibility extends this to every `ρ`. By uniqueness, `p_t := p` is the limit of the whole sequence.

**Semigroup and inversion.** `∫ρ d(p_s∗p_t) = (∫ρ dp_s)(∫ρ dp_t) = e^{−(s+t)C_ρ/2}`. `C_ρ` is Hermitian, so `∫ρ(g^{−1})dp_t(g) = (e^{−tC_ρ/2})^* = e^{−tC_ρ/2}`. Uniqueness gives both claims. ∎

**Scope.** Theorems 4 and 5 use exactly these properties: the Fourier formula for `R` and `R⊗R`, the semigroup law, inversion invariance, and images under the homomorphism `R` (computed as `ρ∘R` on `G`). No proof uses positivity or smoothness of a density.

### R-T. Uniqueness of the matter trace (rebuilds the input of Theorem 2)

The matter algebra is the norm closure of the algebras of finite sets of sites (`VC1_5.md` line 18). Each of these is a full matrix algebra (`LW1_5.md` line 33: "The site algebra is `M_32(C)`"; `n` sites give `M_{32^n}(C)`). On `M_N(C)` with matrix units `E_{ij}`, a tracial state `τ` obeys `τ(E_{ij}) = τ(E_{i1}E_{1j}) = τ(E_{1j}E_{i1}) = δ_{ij}τ(E_{11})` and `Σ_iτ(E_{ii}) = 1`. So `τ = tr/N`. Two tracial states of the matter algebra therefore agree on every finite-site algebra, hence everywhere. For an automorphism `β` of the matter algebra, `τ∘β` is tracial, so `τ∘β = τ`. ∎

### R-C. The coherent ray is well defined and continuous (rebuilds an input of Theorems 1 and 2)

On `R_k^-` put `N := Σ_aU^{aa}` and `N_O := Σ_{ab}O_{ab}U^{ab}` for `O ∈ SO(10)`. Let `h` be a target-end element with `ρ_k(h)^{−1}U^{ab}ρ_k(h) = Σ_cO_{ac}U^{cb}`. Solving gives `ρ_k(h)U^{cb}ρ_k(h)^{−1} = Σ_aO_{ac}U^{ab}`, so `ρ_k(h)Nρ_k(h)^{−1} = N_O`. On `S_−^{⊗k}`, `N` is a sum of `10k` commuting involutions, so its spectrum `σ` on the invariant subspace `R_k^-` is a finite set of integers. Its top eigenvalue there is `10k`, on the line of `φ₀^{⊗k}` (Theorem 1's proof). So `N_O` has spectrum `σ`, and its top eigenspace is the line of `ρ_k(h)φ₀^{⊗k}`. Let `p(t) = ∏_{λ∈σ, λ≠10k}(t−λ)/(10k−λ)`. Then `|ψ_O⟩⟨ψ_O| = p(N_O)`. The right side depends on `O` alone, and it is a polynomial in the entries of `O`. So the ray is well defined and continuous in `O`. Each `Φ_u(A)`, for local `A`, is then a polynomial in finitely many link values, hence measurable and bounded. ∎ `[check]` (1f) tests coherence by this criterion.

### R-S. The end swap (completes item 17)

Let `s̃ = ∏_{a=1}^{10}v_a` with `v_a = (η^y_a − η^x_a)/√2`. Each `v_a` is a unit Clifford vector, and `v_awv_a = −r_a(w)` for every Clifford vector `w`, where `r_a` is the reflection that exchanges `e_a` and `e_{10+a}`. The ten reflections commute and the ten signs cancel. So conjugation by `s̃` exchanges `η^y_a` and `η^x_a` for every `a`. `s̃` is a product of an even number of unit vectors, so `s̃ ∈ Spin(20)`. Hence `s̃U^{ab}s̃^{−1} = iη^x_aη^y_b = −U^{ba}`, and conjugation by `s̃` carries the target-end group onto the source-end group. `s̃^2 = ±1`, so `s̃^{−1}U^{aa}s̃ = −U^{aa}` too, and `s̃φ₀` is the all-minus joint eigenvector. So is `ρ(ϖ_y)φ₀`, since conjugation by `ϖ_y` sends `U^{aa}` to `−U^{aa}`. The joint eigenspace is a line, so `s̃φ₀ = cρ(ϖ_y)φ₀` with `|c| = 1`. Let `ψ_O = ρ_k(h)φ₀^{⊗k}` with `h` in the target-end group, and put `h′ := s̃hs̃^{−1}`, in the source-end group. Then `ρ_k(s̃)ψ_O = c^kρ_k(h′)ρ_k(ϖ_y)φ₀^{⊗k} = c^kρ_k(ϖ_y)ρ_k(h′)φ₀^{⊗k}`, because the two end groups commute. Theorem 1's diagonal stabilizer gives `ρ_k(h′)φ₀^{⊗k} = ρ_k(ȟ)φ₀^{⊗k}`, with `ȟ` the target-end copy of `h′^{−1}`. So `ρ_k(s̃)ψ_O = c^kρ_k(ϖ_yȟ)φ₀^{⊗k}`, a target rotation of `φ₀^{⊗k}`, hence a coherent ray. Its mean has entries `⟨ψ_O, s̃^{−1}U^{ab}s̃ψ_O⟩ = −⟨ψ_O, U^{ba}ψ_O⟩ = −kO_{ba}`. A coherent ray `ψ_{O′}` has mean `kO′`, so the image is `ψ_{−O^T}`; `−O^T ∈ SO(10)` because `10` is even. ∎ `[check]` (1f).

### R-U. The `L5-U` condition of Theorem 6 holds

`LW1_5.md` line 90 gives the `L5-U` Gauss generators "`\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}`" for Hermitian `T`, and `VC1_5.md` line 31 says "its local group is `U(5)`". Take `T = 1` and `θ ∉ 2πZ`. On the register of a link `ℓ` with target `y`, the central element `e^{iθ}` of the target-end `U(5)` acts as `c := e^{iθp_{ℓ,y}}`, with `p_{ℓ,y}` the end number. `c` commutes with the target-end group, since it is central there. It commutes with the source-end group, since it is even and built from other modes. Since `[p_{ℓ,y}, r^y_j] = −r^y_j`, `c` conjugates `U^{jk}_ℓ = r^y_jr^{x†}_k` to `e^{−iθ}U^{jk}_ℓ`, and `U^{jk†}_ℓ` to `e^{iθ}U^{jk†}_ℓ`. So Theorem 6's proof runs with `c` in place of `ϖ`: each loop-link factor `f(h) = tr(ρ(h)X)`, with `X = U^{jk}` or `U^{jk†}`, equals `e^{∓iθ}f(h)`, hence vanishes. ∎

## 5. Checks behind the verdicts, section by section

### 5.A Status and definitions (lines 5-20)

Line 11's hashes: the draft (`c33bb719…`), frozen `CH1_5OE.md` (`70dbb28f…`) and `CH1_5O.md` (`053f1ecf…`) match the files read; `ccdafd71c76de792065d9eefb0c8c5d8dfdb1b75` is the parent of `8311a7d7e`. Line 9's list equals frozen `CH1_5OE.md` line 5's list plus the three new names. Definition 1 matches `VC1_5.md` lines 18-20 and 35; a rotation `x ↦ Q(x−c₀)+c₀` with `Q` a signed permutation maps `Z³` to `Z³`. Definition 2 matches `LW1_5.md` line 80: "`T_{ij}=i\eta_i\eta_j/2`, and `U^{ab}=2T_{a,10+b}`, with `\eta_a=\eta^y_a` and `\eta_{10+b}=\eta^x_b`". Definition 3: each entry `U^{ab}` is Hermitian, and entries on distinct links commute, so every term of the trace is a product of commuting Hermitian operators; a gauge map at `x_i` sends `X_i ↦ R(g)X_i` and `X_{i+1} ↦ X_{i+1}R(g)^T` in both orientations, and `R(g)^TR(g) = 1` cancels inside the trace. Definition 4: frozen (b′) reads "no `G`-class measure meets those bounds", which is `d_Λ(ω,μ′) > δ` for each `μ′`, as line 18 states. Definition 5 matches `CH1_5O.md` line 19 and `LW1_5.md` line 85 ("The displayed `W_E` is defined for `S_+` only").

### 5.B Theorem 1 (lines 24-39)

The sign: in `(1,11,2,12,…,10,20)`, the value `10+a` precedes the values `a+1,…,10`, so the sequence has `Σ_a(10−a) = 45` inversions; hence `∏_aU^{aa} = −∏_j2T_{2j−1,2j}` and `φ₀ ∈ S_−` by `LW1_5.md` line 134 (`[check]` (1a)). The norm: for `b ≠ b′`, `U^{ab}U^{ab′} = η^x_bη^x_{b′}` anticommutes with `U^{bb}`, and `(U^{ab})^2 = 1`, so the squared norm is `Σ_aΣ_{b≠a}|v_b|^2 = 9‖v‖^2`; the transpose uses `U^{ba}U^{b′a} = η^y_bη^y_{b′}` (`[check]` (1c)). `(𝐔^*𝐔)_{ab} = Σ_cU^{ca}U^{cb} = 10η^x_aη^x_b`, so `𝐔^*𝐔 = 10ΓΓ^*` with `Γ^*Γ = 10`; on `C^{10}⊗S_−`, `Γ` has domain `S_+`, and the norm is `10` (`[check]` (1d)). The stabilizer: `η^x_cη^x_dφ₀ = −η^y_cη^y_dφ₀` (`[check]` (1e)). Irreducibility: orthogonal projections onto invariant summands commute with `N = Σ_aU^{aa}`, a sum of represented generators `2T_{a,10+a}`, so they keep its one-dimensional top eigenspace. The `1/√k` identity: cross terms contain `⟨φ₀,(U^{ab}−δ_{ab})φ₀⟩ = 0` (`[check]` (1g) at `k = 2`: `3.000`). The end swap and continuity: R-S and R-C.

### 5.C Theorems 2 and 3 (lines 43-60)

Theorem 2(ii): `Σ_{S≠∅}(3/√k)^{|S|} = (1+3/√k)^n − 1`; `Ŵ_CΦ = (1/10)Σ_a(e_a^*⊗1)X̂_n⋯X̂_1(e_a⊗Φ)` gives `‖Ŵ_CΦ − cl_u(C)Φ‖ ≤ ε`. Two loops: `⟨cΦ+e, c′Φ+e′⟩ − cc′ = c⟨Φ,e′⟩ + c′⟨e,Φ⟩ + ⟨e,e′⟩`, of modulus at most `2ε + ε^2`. Only the Hermiticity of `Ŵ_C` is used, so the two loops may share links. Theorem 2(iii): the telescoping sum has `j`-th term at most `10^{N(j−1)}ε`. Cell symmetry: with `J` as in edit E3, `σ_xσ_y = −1` exactly on links in the directions of `J`; the central gauge maps fix every gauge-invariant observable; R-T gives `τ∘β_g = τ`. Theorem 3: `M_e^{−1}M_o^{−1}W_E^{−1}·W_EM_oM_e = 1`, gate by gate; the gates commute with every Gauss generator (`LW1_5.md` line 128) and have the disjoint supports of line 78.

### 5.D Theorem 4 (lines 64-85)

`so(10)`: `C_{10} = 9`; on the tensor square `C = 18 − 2K₀ + 2P`, with eigenvalues `0, 16, 20` of multiplicities `1, 45, 54` (`[check]` (2a)). `su(5)`: the restricted metric is `−tr_5(XY)`; `Σ_AT_A⊗T_A = −P + 1/5` on `V⊗V`; `C_V = 24/5`; on `V⊗V`, `C = 46/5 + 2P` (`56/5` on 15, `36/5` on 10 dimensions); on `V⊗V̄`, `C = 10 − 2K′` (`0` once, `10` on 24); in total `0, 10, 56/5, 36/5` with multiplicities `2, 48, 30, 20` (`[check]` (2b)). The exponents: `5/(12/5) = 25/12`, `(28/5)/(12/5) = 7/3`, `(18/5)/(12/5) = 3/2`. The bound: constants `2+48+30+20−1−45−54 = 0`; linear terms `200 − 200 = 0`; quadratic `(1/2)(1250/3 − 3680/9) = 35/9`; cubic `(1/6)(15625+13720+2430)/36 = 31775/216`; and `35/9 = 840/216`. At `s = 1/60` the bound is `18625/4665600000 = 149/37324800 = 3.992·10^{−6}`, while `Q − F = 1.052·10^{−5}` (`[check]` (3a)). `F′(x) = (80x^{7/9} + 120x^{11/9})/100 ∈ [0,2]`; the minimum over `x′` of the maximum in line 77 is `3.549·10^{−6} ≥ Θ = 3.506·10^{−6}` (`[check]` (3b)). Variance ratio: `F(e^{−s}) − e^{−2s} = (2/45)s^2 + O(s^3)` and `Q(e^{−s}) − e^{−2s} = (1/12)s^2 + O(s^3)`, so the ratio tends to `45/24` (`[check]` (4)).

### 5.E Theorem 5 and Corollary 5.1 (lines 87-106)

First part: `d_Λ(ω,μ) ≤ 3ε ≤ η ≤ δ` gives (a′); `d_Λ(ω,μ′) ≥ d_Λ(μ,μ′) − η > δ` gives (b′). Model part: `σ = 5s/48` gives a plaquette law `p^K_{4σ}` with `E w = e^{−12·4σ/5} = e^{−s}`; a full-group plaquette has `E w = e^{−18σ′} ∈ (0,1)`, so Theorem 4's last clause applies. The realization: `λ = R_*p^K_{σ/m}` is transpose-invariant (R-HK inversion), a straight block link carries the product of `m` independent values, of law `R_*p^K_σ` (R-HK semigroup), and distinct block links use disjoint fine links. `λ^{⊗L}` is invariant under the coordinate permutations and transposes of the geometric action. `s = 1/60` needs `σ_* ≥ 5/(48·60) = 1/576`, and then `δ_0 ≥ 18625/13996800000 = 1.3307·10^{−6} > 10^{−6}`. Concrete instance: with `x = 3·10^{−9}`, `(1+x)^4 − 1 = 4x + 6x^2 + 4x^3 + x^4 = 1.2000000054…·10^{−8} < 1.3·10^{−8}`, and `3ε < 3.9·10^{−8} < η = 10^{−7}` (`[check]` (5)). Corollary 5.1: `d_Λ(μ,C(G)) ≤ d_Λ(μ,ω_η) + d_Λ(ω_η,C(G)) ≤ η + d_Λ(ω_η,C(K)) ≤ 2η`; see item 40 for its last claim.

### 5.F Section 5 (lines 110-136)

The four-test rows report the draft's lines 262-264 faithfully. C2: `T_S` is gauge invariant because `ϖ` is central in its end group and the two end groups commute. In a Theorem 2 state `ω(T_S) = ∫∏_{ℓ∈S}⟨ψ_{u_ℓ}, ρ(ϖ_x)ψ_{u_ℓ}⟩dν = 0`: with `M := ρ_k(h)U^{11}ρ_k(h)^{−1}`, `Mψ_O = kψ_O` and `Mρ(ϖ_x)ψ_O = −kρ(ϖ_x)ψ_O`, and eigenvectors of a Hermitian operator for `k ≠ −k` are orthogonal (`[check]` (C2): `7·10^{−17}` at `k = 1`, `3·10^{−18}` at `k = 2`). C3: item 48. C4 and line 126: the Theorem 5 state is stationary for the identity update and has `ω(Ŵ_p) ≈ e^{−1/60} ≠ 0`, so by Theorem 6 it is not Gauss-tracial. Theorem 6: the products `∏_xV_x(g_x)` form a group of unitaries, since gauge unitaries at different sites commute (even matter operators; commuting end groups); their span is a `*`-algebra and so equals `𝔊`; the trace factors over matter and links; on a loop link `f(h) = tr(ρ(c)ρ(h)U^{ab}ρ(c)^{−1}) = −f(h)` with `c = ϖ_y` (`[check]` (1h): `0.0`). Line 132's first sentence matches `CH1_5O.md` line 157: "CH1-5O-E(a) fails for `ω₀` for every `δ < c_*`", which uses only `ω₀(W) = 0`.

### 5.G Citations of the draft

Theorem labels (lines 24, 43, 56, 66, 87, 104, 128) match draft Lemma K, Theorem U, Lemma I, Lemma HK, Theorem W, Corollary G and Proposition Z. The renaming `G ↦ Q` in Theorem 4 avoids the clash with the group `G`; the formulas agree. Theorem 5 restricts Theorem W(ii)'s conclusion to the model statement; its constants agree with draft line 235. The four-test table (lines 114-116) agrees with draft lines 262-264. Line 7's "The draft claims its random-link model classes close the frozen small-field comparison" fits draft lines 54 and 238 (section 2, G1). Line 102's "the assertion for an arbitrary four-dimensional list" has no counterpart in the draft (G2). Line 132's "global multiplicity-one argument" misreads draft line 288, which rests on the per-region `CH1_5O.md` R5 (G3). Line 124 sharpens draft line 280 correctly (item 48).

## 6. Required edits

Each edit names the line, the text to change and the new text. None changes the content of a theorem.

- **E1 (line 7; items 3-5).** Replace the GAP paragraph by: "**GAP.** Theorem 5 proves the comparison for the random-link model classes. The draft pins the frozen statement's classes by these models (`CH1_5OEP_DRAFT.md` lines 54 and 238); the record intends T0-start's classes (frozen `CH1_5OE.md` Definition 6). The draft does not show that the model measures lie in T0-start's class: reflection positivity, density in `𝒜_{k0}(g)` at `g ≤ g_*`, and T0-start's class for `SU(5)` and `Spin(10)` (T0-start[G]) are unchecked. So the model witness does not decide CH1-5O-E′ for T0-start's classes; Theorem 5's first part reduces that case to SEP[T0-start]. Theorem 5 gives the corrected model statement. A large-register limit does not establish the same result for `S_+`."
- **E2 (line 102; items 36-38).** Replace the paragraph by: "**GAP in the draft's conclusion.** The preceding theorem proves separation for the named random-link models, not membership in T0-start's class or satisfaction of every frozen small-field condition. Conditional on that identification it supplies the finite comparison; without it CH1-5O-E′ remains open for T0-start's classes. The lists are spatial skeleton loops read in one time slice. This matches the frozen data, whose list consists of equal-time invariant observables (`CH1_5O.md` line 175)."
- **E3 (line 54; item 21).** Replace "For each reversed coordinate direction put `σ_x=(−1)^{Σ_{i∈J}x_i}`." by "Write the linear part of `g` as `Qe_j=ε_je_{π(j)}`. The reversed image links are the links in the directions of `J:={π(j):ε_j=−1}`. Put `σ_x=(−1)^{Σ_{i∈J}x_i}`."
- **E4 (line 20; item 13).** Replace "`CH1_5O.md` explains that" by "Frozen `CH1_5OE.md` (Definition 6, line 22, and its R-E′ row, line 165) records that".
- **E5 (line 16; item 9).** Append: "`LW1_5.md` B1-5 and `VC1_5.md` Theorem 2.2 state the lifts for `S_+`. For another irreducible register with `τ_E=0` the same proof applies: the end swap `∏_a(η^y_a−η^x_a)/√2` lies in `Spin(20)` and acts on every `Spin(20)` register, and the proof of `VC1_5.md` Theorem 2.1 uses no property of the register (`CH1_5OEP_DRAFT.md` line 90)."
- **E6 (line 39; item 17).** Replace "local sections give continuity" by "`|ψ_O⟩⟨ψ_O|=p(N_O)`, with `N_O=Σ_{ab}O_{ab}U^{ab}` and `p` the Lagrange polynomial of the top eigenvalue `10k`, so the ray is continuous (referee closure R-C, CH1_5OEP_REFEREE.md)". Replace "It maps `φ₀` to the unique all-minus joint eigenvector, the same ray as `ϖ` at one end. This proves the last transformation." by "It maps `φ₀` to the all-minus joint eigenvector, which is `ρ(ϖ_y)φ₀` up to a phase, and it carries the target-end group onto the source-end group. So it maps `ψ_O` to a source rotation of `ρ_k(ϖ_y)φ₀^{⊗k}`. The diagonal stabilizer turns this into a target rotation of `φ₀^{⊗k}`, a coherent ray, and its mean is `−kO^T`. So the image is `ψ_{−O^T}` (referee closure R-S, CH1_5OEP_REFEREE.md)."
- **E7 (line 98; item 34).** Replace "Choose `s` in the displayed range and `σ=5s/48`." by "Choose `s` in the displayed range with `s²(840−31775s)/64800>δ`, which exists because `δ` is below the supremum, and put `σ=5s/48`."
- **E8 (line 132; item 53).** Replace "The draft's assertion that the dark state has the required finite-region Gauss-trace form uses a global multiplicity-one argument without establishing its boundary-region restrictions: **GAP** at that inference." by "The dark state `ω₀` of `CH1_5O.md` Theorem 12 has the finite-region Gauss-trace form on every finite region: `ω₀=tr(Q_Λ·)/tr(Q_Λ)`, with `Q_Λ∈𝔊_Λ` the projection onto `𝔊_Λu_Λ` (referee closure R-Z, CH1_5OEP_REFEREE.md). So it does not refute HEAT."
- **E9 (line 134; item 55).** Replace "subject to the spatial/temporal and class identifications. This reduction is sufficient, not necessary." by "subject to the class identification. This is a sufficient condition; necessity is not shown."
- **E10 (line 11; items 2, 19, 21, 25).** Append: "Referee closures R-HK (the heat-kernel measure), R-T (uniqueness of the matter trace) and R-C (continuity of coherent rays) in CH1_5OEP_REFEREE.md rebuild the cited inputs that Theorems 1, 2, 4 and 5 use. They are unrefereed."

**Optional edits.** None is needed for correctness.

- **O1 (line 17; item 10).** A register-independent normalization: "For a register `R`, let `κ_R` be the largest eigenvalue of `U^{11}` on `R`, and put `Ŵ_C=(1/10)tr((X_n/κ_R)⋯(X_1/κ_R))`." On `R_k^-`, `κ_R = k`: on `S_−^{⊗k}`, `U^{11}` is a sum of `k` commuting involutions, so its eigenvalues on `R_k^-` are at most `k`, and `φ₀^{⊗k} ∈ R_k^-` has eigenvalue `k`. On `S_+`, `κ_R = 1`. Four tests (assessments, not owner decisions): (1) pass, it fixes a normalization and decides neither (a′) nor (b′); (2) pass, it is one number determined by the register; (3) pass, on `S_+` it gives the plain loop, so it makes no small register look classical; (4) pass, `κ_R` is a property of `R`, the comparison needs some normalization, and frozen `CH1_5OE.md` Definition 5 lists normalizations as open specifications. It passes as a proposal. Nothing is adopted.
- **O2 (line 128; item 50).** By R-U, the `L5-U` clause can read: "The analogous conclusion holds for `L5-U`: conjugation by the central element `e^{iθ}`, `θ∉2πZ`, of a target-end `U(5)` multiplies each link factor by a nontrivial phase."
- **O3 (line 96; item 33).** "A block law can be subdivided" can read "The block configuration of one time slice, mapped by `R`, can be subdivided", as in draft line 165.

## 7. Open statements to carry by name

- **CH1-5O-E′** with T0-start's classes (frozen `CH1_5OE.md` line 167). Theorem 5's first part reduces it to SEP[T0-start]. It holds in the random-link model classes (Theorem 5, model part).
- **SEP[T0-start]** (line 134, with edit E9).
- **CH1-5O-E′[VC1]** (line 118).
- **HEAT** (line 126). By R-Z the dark state does not refute it.
- Inherited, unchanged (line 9): CH1-5O-E, CH1-5O-i, CH1-5U-i, the R-A residual, AM, AM-5, CH1-i, CH1-ii, CG1-i, CG1-ii, CG1K-loc, CG1K-H, LW1-5-BG, LW1-5-X, GA1-P-5, Y2-W[`L5-O`], VC1, the formulation of IR and AM (`CH1.md` Definition 8), and T0-start[G] for `Spin(10)` and the candidate subgroup factors.

## 8. Freeze recommendation

**Freeze after edits E1-E10.** Every theorem of `CH1_5OEP.md` is correct: Theorems 1-6 and Corollary 5.1, with the steps that R-S, R-C, R-T and R-HK supply. The six ERRORs are a misread gap stated twice (G2), a second misread gap (G3), a wrong file name, an undefined symbol and an unproved non-necessity. The three INCOMPLETE items each need a short insertion. The one real gap, G1, is stated correctly in substance and stays open as CH1-5O-E′ with T0-start's classes. The dated amendment can record: Theorems 1-6 and Corollary 5.1 as proved; CH1-5O-E′ as holding in the random-link model classes and as reduced to SEP[T0-start] for T0-start's classes; CH1-5O-E′[VC1], HEAT and SEP[T0-start] as open; no named failing step for `L5-O` or `L5-U`, both live under `TOE_ASSEMBLY.md` §3.5. The referee closures R-Z, R-HK, R-T, R-C, R-S and R-U enter as imported, unrefereed closures if the lead takes them.

---

## FINISH

**Proved here (pass 3, unrefereed).**
- The verdicts of section 1: 56 items, 47 CORRECT, 6 ERROR, 3 INCOMPLETE. Every theorem of `CH1_5OEP.md` (Theorems 1-6, Corollary 5.1) is correct, with the steps below.
- R-Z: on `L5-O[S_+]`, the dark state `ω₀ = Φ₀∘E` equals `tr(Q_Λ·)/tr(Q_Λ)` on every finite region `Λ`, where `Q_Λ ∈ 𝔊_Λ` is the projection onto `𝔊_Λu_Λ`. The proof rebuilds `CH1_5O.md` R5 and the finite-dimensional double commutant theorem.
- R-HK: the heat-kernel probability measure on `Spin(10)` and on `SU(5)~` exists and is unique with `∫ρ dp_t = e^{−tC_ρ/2}`; it is a convolution semigroup and inversion invariant.
- R-T: the tracial state of the matter algebra is unique, hence invariant under every automorphism.
- R-C: `|ψ_O⟩⟨ψ_O| = p(N_O)`, so the coherent ray is well defined and continuous.
- R-S: the end swap maps `ψ_O` to `ψ_{−O^T}`.
- R-U: the condition of Theorem 6's `L5-U` clause holds for `L5-U` as `LW1_5.md` specifies it.
- Item 48: under independent fine links, loops on disjoint fine-link sets have connected correlation exactly zero in the Theorem 2 state.

**Counterexamples.** None to any theorem of `CH1_5OEP.md`. Two pass-2 GAP claims are refuted: G2 (the draft asserts nothing for temporal loops, and the frozen list holds equal-time invariant operators) and G3 (by R-Z). Line 134's "not necessary" is unproved; this report proves neither it nor its negation.

**Open, by name.** CH1-5O-E′ with T0-start's classes; SEP[T0-start]; CH1-5O-E′[VC1]; HEAT; and the inherited list of section 7.

**What changes downstream.**
- `CH1_5OEP.md` can enter the frozen part by a dated amendment once edits E1-E10 are applied.
- CH1-5O-E′ holds in the random-link model classes. For T0-start's classes it reduces to SEP[T0-start] and stays open. The frozen GAP "the Gaussian calculation does not establish their separation" (`CH1_5OE.md` line 5) is answered for the model classes by Theorem 4, and not for T0-start's classes.
- HEAT stays open for the law's tick. The dark state does not refute it (R-Z).
- Theorem 3 stands: in existence statements over the update class on file, "stationary for some `L5-O` update" is no condition. Pinning the class is the owner's choice; nothing is adopted here.
- No named failing step for `L5-O` or `L5-U`. Both stay live under `TOE_ASSEMBLY.md` §3.5.
