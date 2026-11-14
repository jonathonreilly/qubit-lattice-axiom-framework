lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5O-E referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) of `CH1_5OE.md`, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), headless on the Mac mini; effort as set by the lead (first line). This session wrote neither pass 1 (`CH1_5OE_DRAFT.md`) nor pass 2 (`CH1_5OE.md`). This is one check of the proof: one whole-file, line-by-line read. No other review was read or reviewed. `LW1_REFEREE.md` was read only for its format.

**What this file is.** A referee report. It grants no status, adopts no reading, law or class, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. It is not an amendment. A "referee closure" is a short complete argument written here; it is unrefereed. "[check]" marks a tiny scratch computation; it guides and never proves. "Frozen" qualifies either a file (its status) or a measure (Definition 3 of `CH1_5OE.md`); the noun it modifies tells which.

**Text read.** `CH1_5OE.md` at commit `1a6005d26` (the last commit that touches it, and the branch head when read). SHA-256 of the file read: `5a5c94d11637ac93fbf26ced1c286e277ee6f8a2acd5711de4ede2fce2b7383c`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), HEAD | `1a6005d265` |

No other branch was read.

Files read at that commit, by line. This folder: `CH1_5OE.md` lines 1-127 (all); `CH1_5OE_DRAFT.md` lines 1-246 (all; last changed `481fcd124`; SHA-256 `2c2ff5dfaf0c3868610a55eda2189e177df358259f05a19e77bbab07a090ac3d`, the hash `CH1_5OE.md` line 5 records); `CH1_5O.md` lines 1-188 (all; last changed `1ec3f96a5`; SHA-256 `053f1ecf4da057b46eaf70b0c0cb4ac9c6629898a125f6bc959016bb1ccd95e3`, the hash line 5 records); `VC1_5.md` lines 30-40 (Theorem 2.1 and its proof; last changed `bf95fc909`); `CH1.md` lines 5, 7, 9, 13, 85, 99 and 231 (status, Amendments 1-2, open list, CH1-5O-i), found by `grep` (last changed `1ec3f96a5`); `Y2W_DRAFT.md` lines 1-40 (format of the head) and 50-80 (Definition SC, SC-loop, Lemma 0, four-test table; last changed `92e03055c`); `GA2_Y2.md` line 155 (last changed `bf403a16a`); `TOE_ASSEMBLY.md` line 387 (GA2(a); last changed `7d2b20d29`); `LW1_5.md` lines 35, 80 and 150 (last changed `271c868a4`); `LW1_REFEREE.md` lines 1-80 and its section headings, for format only (last changed `5a2a0affe`). Repository rules, all lines: `CLAUDE.md`, `AGENTS.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md` (`66962bfc2` is the last commit that touches the last two). `CH1_5OE.md` cites neither `CH1_5O_DRAFT.md` nor `LIT_HIGGS.md`; neither was read. The audit ledger was not read.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-O`, the frozen specification CH1-5O-E (`CH1_5O.md` line 175) and the readings of `CH1_5OE.md` are read plainly. Where the frozen text leaves a choice open (whether a gauge-Higgs class may carry no Higgs field), this report names the choice for the owner, runs the four tests on the plain reading, and adopts nothing.

**Working set used, by name.** None directly. The statements checked use PS-5, PS-6 and PS-6r only through the law `L5-O` of `LW1_5.md` section 2 (line 80), PS-1c only through the cell lifts, and LW1's conjugation reading of gauge invariance (`LW1_5.md` line 35: "Gauge invariance means invariance under conjugation, not necessarily a zero Gauss-charge sector"). Results used, by name: `VC1_5.md` Theorem 2.1; `CH1_5O.md` Definitions 1-5 and Theorems 1-7; `Y2W_DRAFT.md` Definition SC (pass 1, not adopted; used only to read R-E′).

**Inputs from outside the working set.** Standard mathematics rebuilt in the text: Lagrange interpolation; Haar averaging; Isserlis' moment formula; Cauchy-Schwarz; the Taylor series of `tr ρ(exp X)`; marginals of densities (Tonelli); the isotypic dichotomy for invariant subspaces; elementary arithmetic of coprime pairs. Standard mathematics cited, not rebuilt: existence and invariance of Haar measure; the Peter-Weyl theorem; the spectral theorem for normal operators in finite dimension; measure zero of `C^1` images of lower-dimensional manifolds. Literature context, credited from memory and never load-bearing: Fröhlich, Morchio and Strocchi, and 't Hooft (gauge-invariant composites); Fradkin and Shenker, and Osterwalder and Seiler (complementarity of Higgs and confinement regions); Isserlis and Wick (Gaussian moments).

**Method.** Every statement and proof step of `CH1_5OE.md` was re-derived by hand. Verdicts: CORRECT; ERROR (a false or garbled line, quoted, with a fix); INCOMPLETE (a named missing step or hypothesis, with a referee closure). One [check]: `/tmp/toe-ch15oeref/check.py`, output `/tmp/toe-ch15oeref/out.txt`; 29 s, 677 MB peak; floating point; run after `memory_pressure` showed 63 percent free. `scripts/lab_ops.py` is absent from this sparse checkout, so its preflight and numeric lock were not run. The check covers Theorem 6 and the covariance of `M`; the pieces, their inequivalence and the generated subalgebras used in Theorem 4; the eigenvalues in GAP C; `c_10` and `c_45`; a Monte Carlo of Theorem 7 with the adjoint representation and variances different from pass 1's; and the cube arithmetic after Corollary 4.1. It reran none of pass 1's scripts.

**Counts.** 56 items: 50 CORRECT, 4 ERROR, 2 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. All three GAPs the distiller marked are real, with two qualifications: the first clause of GAP B is a reading question, not a gap, and GAP C occurs only at `(a, b) = (0, ±1)` (section 3).

---

## 1. Verdict table

| # | Item (`CH1_5OE.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Title and Status paragraph (1, 3) | CORRECT, one clause excepted | The clause "the proposed R-E′ changes the frozen gauge-Higgs specification" is item 10. The proved list omits Theorem 2 and Corollary 4.1 (edit E8). |
| 2 | Provenance (5) | CORRECT | Both recorded hashes equal the hashes of the files read; commit `481fcd124` exists. "effort and session ID: not visible" is the distiller's own view; the lead's run-log sentence before it supplies them. |
| 3 | Inputs and credits (whole file) | INCOMPLETE | No line lists the cited standard inputs (Haar measure, Peter-Weyl, measure zero of lower-dimensional images) or credits the authors whose ideas sections 3-4 use (Fröhlich-Morchio-Strocchi, 't Hooft, Fradkin-Shenker, Osterwalder-Seiler). Edit E6. |
| 4 | Definition 1 (9) | CORRECT | Moreover `b` is odd and `a ≠ ±b` (R3). |
| 5 | Definition 2 (10) | CORRECT | Matches `VC1_5.md` Theorem 2.1 and `CH1_5O.md` Definition 2; the inputs are labelled as inputs. |
| 6 | Definition 3 (11) | CORRECT | Implicit: `(W, σ)` is a finite-dimensional unitary representation; "frozen" holds almost surely. `W = 0` is not excluded (item 10). |
| 7 | Definition 4 (12) | CORRECT | |
| 8 | Definition 5 (13) | CORRECT | Faithful to `CH1_5O.md` line 175, but drops "with coupling at most `g_*`" and "under `ι′`, within `δ`" (edit E9). |
| 9 | Definition 6, R-Esym and R-Easym (14) | CORRECT | This R-Esym contains the frozen extensions by definition; the draft's R-Esym infers it from unbounded Higgs couplings. One name carries two meanings (edit E5). |
| 10 | Definition 6, last sentence; the same claim in lines 3 and 110 | ERROR | "R-E′ removes the gauge-Higgs requirement of the frozen specification; it is a proposed change, not an already valid instantiation." Under Definition 3 a measure with `W = 0` is a gauge-Higgs measure, and the frozen text does not say whether `W = 0` is allowed. Section 2.1. |
| 11 | Definition 7 (15) | CORRECT | `κ` acts by `*`-automorphisms (implicit, as in the draft). |
| 12 | Theorem 1, bijection (19, sentences 1-2) | CORRECT | |
| 13 | Theorem 1, exactness clause (19, sentence 3) | ERROR (citation) | "`CH1_5O.md` Lemma G, Theorem E, Theorem L and Corollaries L.2, L.4 and IR" are draft names; `CH1_5O.md` numbers these results Theorems 1, 2, 5, 6, 7 and 3. The content, a tautology, is right. |
| 14 | Theorem 1, GNS clause (19, sentence 4) | CORRECT | |
| 15 | Proof of Theorem 1 (21) | CORRECT | Two one-line steps are implicit: `E∘a_{x,g} = E`, so `φ∘E` is gauge invariant; and `κ_g O = O` for quasi-local `O ∈ A^G`, by density of local invariant elements (`VC1_5.md` Theorem 2.1) and continuity of `κ_g`. |
| 16 | Remark after Theorem 1 (23) | CORRECT | "the definition of exotic in the draft" is `CH1_5O.md` Definition 4: "A colour-exotic type has `σ₃∉{1,3,3̄}`" (edit E10). |
| 17 | Remark on frozen one-point functions (25) | CORRECT | True for every gauge-invariant measure, frozen or not. |
| 18 | Theorem 2, statement (29) | CORRECT | |
| 19 | Proof of Theorem 2(i) (31) | CORRECT | The chain-condition clause skips one step: equal dimension forces equal identity component, since a closed subgroup of full dimension is open. |
| 20 | Proof of Theorem 2(ii) (33) | CORRECT | The orbit span needs a `G`-invariant inner product (average any inner product). |
| 21 | Theorem 3, statement (35-39) | CORRECT | "independent" means `g` is independent of `u`. |
| 22 | Proof of Theorem 3 (41) | CORRECT | |
| 23 | Corollary 3.1, statement (43) | INCOMPLETE | "orbit extension" is undefined when `μ` carries `K`-Higgs fields; "`ι=ι′∘j` on the support" must use the inclusion through which `ν` is built; each `ι′(O)` must be `G`-gauge invariant and integrable. Referee closure R1. |
| 24 | Proof of Corollary 3.1 (45) | CORRECT under R1's hypotheses | The Higgs-field case needs the explicit `ν` and `J^*J = 1` (R1). |
| 25 | GAP in pass 1 (47) | CORRECT | Gap real. Counterexample R2 for every class of measures with densities; R6 for actions built from `G` plaquettes and Higgs hopping, at quadratic order. Section 3. |
| 26 | Corollary 3.2 and proof (49-51) | CORRECT | The subgroup letter `J` clashes with the isometry of Theorem 2(ii) (edit E11). |
| 27 | Remark (53) | CORRECT | |
| 28 | Theorem 4, statement (55) | CORRECT | |
| 29 | Proof of Theorem 4, pieces and dichotomy (57) | CORRECT | [check]: the commutant of `ad(Lie H)` on `A ⊕ B` has dimension 4 (two inequivalent pieces of complex type) for six admissible `(a, b)`, and 8 for the excluded `(1, 0)`, where `A ≅ B`. |
| 30 | Proof of Theorem 4, both pieces (59) | CORRECT | [check]: `su(3) ⊕ su(2) ⊕ A` generates 24 dimensions; `Lie H + A + B` generates 45; `dim[𝔭, 𝔭] = 25`. |
| 31 | Corollary 4.1 and proof (61-63) | CORRECT | Read the window with `S` its endpoint sites; the marginal on its links depends only on `u` there and `g` at those sites. |
| 32 | Remark (65) | CORRECT | Open cubes qualify from side 16 links ([check]). |
| 33 | Theorem 5, statement (69) | CORRECT | |
| 34 | Proof of Theorem 5 (71) | CORRECT | |
| 35 | Remark (73) | CORRECT | "necessary" holds for the full set of identities, which includes `ΦP_j(Φ) = λ_jP_j(Φ)`: then `q(Φ) = Σ_jq(λ_j)P_j(Φ) = 0`. On a finite register an anti-Hermitian `Φ` always satisfies `q(Φ) = 0` for its minimal polynomial (R5). |
| 36 | Theorem 6, statement (75-79) | CORRECT | [check]: residual 0; multiplicities 32 and 288; `P_{9i/2}(M) = ΓΓ^*/10`; `[M, R⊗V] = 0` for a random `g`. |
| 37 | Proof of Theorem 6 (81) | CORRECT | Two one-line computations are omitted: the entries of `P_{9i/2}(M) = (M + i/2)/(5i)`, and the covariance of `M` (section 2.3). |
| 38 | Remark (83), first sentence | ERROR | "The Clifford multiplication image is the 32-dimensional channel; the other is its kernel." Section 2.1. |
| 39 | Remark (83), rest | CORRECT | |
| 40 | GAP in pass 1 (85) | CORRECT | Real in its first sentence, and only at `(a, b) = (0, ±1)` (R3). Its last two sentences are scope remarks that pass 1 also makes. Section 3. |
| 41 | Gaussian model (89) | CORRECT | Theorem 7 also uses the model with `K = G`; say "a closed `K ⊆ G`" (edit E12). |
| 42 | Theorem 7, statement (91-96) | CORRECT | [check], adjoint representation and new variances: `Var/(Ew − 1)^2` 0.3306 against `2/N_eff` = 0.3310; ratio at `r = 0.6` 0.1189 against 0.1192. |
| 43 | Proof of Theorem 7 (98) | CORRECT | |
| 44 | Remark (100) | CORRECT | For `C = C′` the ratio is `2/N_eff` whatever the propagator (R4). |
| 45 | The four tests (104) | CORRECT | Matches `TOE_ASSEMBLY.md` §3.2 as quoted in `CH1_5O.md` line 164. |
| 46 | Table, R-Esym (108) | CORRECT | |
| 47 | Table, R-Easym (109) | CORRECT | |
| 48 | Table, R-E′ (110) | CORRECT, one clause excepted | "pure gauge changes frozen CH1-5O-E" is item 10. |
| 49 | CH1-5O-E′ (112) | ERROR | "no G-class measure satisfies (b)" is garbled: (b) is an exclusion, which a measure cannot satisfy. Section 2.1. |
| 50 | Attack B1 (116) | CORRECT | |
| 51 | Attack B2 (117) | CORRECT | |
| 52 | Attack B3 (118) | CORRECT | "(b′)" is not defined in this file; edit E3 defines it. |
| 53 | Attack B4 (119) | CORRECT | |
| 54 | Attacks A1-A4 (121) | CORRECT | Matches `CH1_5O.md` lines 179-182. |
| 55 | Section 7, first paragraph (125) | CORRECT | |
| 56 | Section 7, open names (127) | CORRECT | For parity with `CH1_5O.md` line 13, add AM and "the formulation of IR and AM (`CH1.md` Definition 8)" (edit E13). |

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 10 (lines 3, 14, 110).** Line 14 reads: "R-E′ removes the gauge-Higgs requirement of the frozen specification; it is a proposed change, not an already valid instantiation." Line 3 reads "the proposed R-E′ changes the frozen gauge-Higgs specification", and line 110 reads "pure gauge changes frozen CH1-5O-E". The frozen text, `CH1_5O.md` line 175, says only: "`𝒞(G∞)` is a gauge-Higgs comparison class with coupling at most `g_*`". It puts no form on `𝒞(Spin(10))`. Definition 3 of `CH1_5OE.md` reads: "A `G` gauge-Higgs measure on `G^L × W^S` is invariant under `(U,φ)↦(g·U,σ(g)φ)`." With `W = 0` the space is `G^L` and the condition is gauge invariance. So a pure-gauge class is a gauge-Higgs class unless "gauge-Higgs" requires `W ≠ 0`. Neither text says that. The three lines state one reading as a fact.
*Fix.* Line 14, last sentence: "R-E′ takes the zero Higgs representation on both sides. By Definition 3 these measures are gauge-Higgs measures. So R-E′ instantiates the frozen specification if a gauge-Higgs comparison class may have `W = 0`; the frozen text does not say, and the owner may specify." Line 3: delete "changes the frozen gauge-Higgs specification and". Line 110: replace "pure gauge changes frozen CH1-5O-E" by "whether pure gauge is admissible in frozen CH1-5O-E turns on the `W = 0` reading". Section 3 runs the four tests on that reading.

**Item 13 (line 19).** The line reads: "If the hypotheses of `CH1_5O.md` Lemma G, Theorem E, Theorem L and Corollaries L.2, L.4 and IR hold for these states". `CH1_5O.md` has no results under these names. Its titles read "Theorem 1 (global action and implementers; draft Lemma G)", "Theorem 2 (averaging; draft Theorem E)", "Theorem 3 (tail bound; draft Corollary IR)", "Theorem 5 (spectral selection; draft Theorem L)", "Theorem 6 (finite-orbit correlations; draft Corollary L.2)" and "Theorem 7 (uniform correlation bound; draft Corollary L.4)".
*Fix.* "If the hypotheses of `CH1_5O.md` Theorems 1, 2, 3, 5, 6 and 7 (draft Lemma G, Theorem E, Corollary IR, Theorem L, Corollaries L.2 and L.4) hold for these states".

**Item 38 (line 83).** The line reads: "The Clifford multiplication image is the 32-dimensional channel; the other is its kernel." Clifford multiplication is `Γ^*: C^{10} ⊗ C^{32} → C^{32}`, `e_a ⊗ ψ ↦ γ_aψ`. Its image is all of `C^{32}`, since `Γ^*(e_1 ⊗ γ_1ψ) = ψ`; that is not a subspace of `C^{10} ⊗ C^{32}`. If the line means `Γ` instead, its image is the 32-dimensional channel, but its kernel is `0`, since `Γ^*Γ = 10`. Under either reading one clause fails.
*Fix.* "The 32-dimensional channel is the range of `Γ`; the 288-dimensional channel is the kernel of Clifford multiplication `Γ^*: e_a ⊗ ψ ↦ γ_aψ`." *Proof.* `ΓΓ^*Γ = 10Γ`, so `ran(ΓΓ^*/10) = ran Γ`. The orthogonal complement of `ran Γ` is `ker Γ^*`. ∎

**Item 49 (line 112).** The line reads: "such that some `K`-class measure satisfies (a) and no `G`-class measure satisfies (b)". Clause (b) of Definition 5 is an exclusion ("(b) excludes all C(G) measures"). A measure cannot satisfy an exclusion. The draft's clause, line 189, reads: "(b′) no `μ'` in T0-start's `Spin(10)` class meets the bounds of (a′)".
*Fix.* "such that (a′) some `K`-class measure meets the bounds of (a), and (b′) no `G`-class measure meets those bounds." This also defines the label (b′) that line 118 uses.

### 2.2 INCOMPLETE

**Item 3 (inputs and credits).** The file names Peter-Weyl, Lagrange, Wick and Cauchy-Schwarz at their points of use. It does not say which standard facts are cited rather than rebuilt. Corollary 4.1 uses "Its image has Haar measure zero" with no source. The file credits no author for the frozen-orbit idea of section 3 or for complementarity. The draft lists both, in its lines 24 and 246.
*Closure.* Add one paragraph to the head (edit E6): "Standard mathematics cited, not rebuilt: existence and invariance of Haar measure; the Peter-Weyl theorem; the descending chain condition for closed subgroups of a compact Lie group (sketched in Theorem 2); measure zero of `C^1` images of lower-dimensional manifolds. Literature context, credited from memory and never load-bearing: Fröhlich, Morchio and Strocchi, and 't Hooft (gauge-invariant composites; the orbit construction of Theorem 3); Fradkin and Shenker, and Osterwalder and Seiler (complementarity); the `Spin(10)` decomposition `10 ⊗ 16 = 16̄ ⊕ 144`."

**Item 23 (Corollary 3.1, line 43).** Three things are missing. (1) Theorem 3 builds `ν` only for a pure `K`-gauge measure, so "orbit extension" is undefined when `μ` carries `K`-Higgs fields. (2) The compatibility "`ι=ι′∘j` on the support" must use the inclusion through which `ν` is built. The fixed `j` of Definition 5 may be a different map. (3) Theorem 3's identity needs each listed product `ι′(O_1)ι′(O_2)` to be `G`-gauge invariant and `ν`-integrable.
*Closure.* R1 (section 5) states the corollary with these hypotheses and proves it. It also shows that hypothesis (2) holds automatically for loop lists with the standard identification.

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 9.** Line 14's R-Esym contains the frozen extensions by definition. Lines 47 and 108 discuss both that class and the draft's R-Esym, which only leaves Higgs couplings unbounded. Give the two classes two names (edit E5).
- **Item 15.** The two implicit steps: `E∘a_{x,g} = E` by invariance of Haar measure, so `φ∘E` is gauge invariant; and `κ_g O = O` for quasi-local `O ∈ A^G`, since local invariant elements are dense in `A^G` (`VC1_5.md` Theorem 2.1: "Local invariant observables are dense in `A^{gauge}`") and `κ_g` is isometric.
- **Item 13, content.** The distiller's conditional form is the right one. `CH1_5O.md` Theorem 7 assumes invariance under the `γ_j`, which not every state has; the draft's "Every state in its image satisfies the conclusions" (draft line 76) holds because each conclusion is an implication.
- **Item 19.** In a strictly descending chain of closed subgroups the dimension is eventually constant. A closed subgroup of the same dimension is open, so it contains the identity component. From then on the identity components agree, and the finite component groups decrease strictly, which must stop.
- **Item 35.** R5 shows that on a finite register an anti-Hermitian `Φ` always has exact polynomial projectors. What a finite composite fixes is its spectrum. This supports the stopping points of B1 and B4.
- **Item 37.** `P_{9i/2}(t) = (t + i/2)/(5i)`, so `P_{9i/2}(M)` has diagonal entries `(i/2)/(5i) = 1/10` and off-diagonal entries `(i/2)γ_aγ_b/(5i) = γ_aγ_b/10`. Also `(ΓΓ^*)_{ab} = γ_aγ_b`, because `Γ^*(e_b ⊗ φ) = γ_bφ`. Covariance: write `M_{ab} = (i/2)(γ_aγ_b − δ_{ab})`. With `κ_g(γ_a) = Σ_cR(g)_{ca}γ_c` and `Σ_cR_{ca}R_{cb} = δ_{ab}`, `κ_g(M_{ab}) = Σ_{c,e}R_{ca}R_{eb}M_{ce} = (R^TMR)_{ab}`. On `C^{32}` the implementer of `g = exp X` is `V = exp((1/4)Σ_{ab}X_{ab}γ_aγ_b)`, since `[(1/4)Σ_{ab}X_{ab}γ_aγ_b, γ_c] = Σ_aX_{ac}γ_a` ([check]: residual `2·10^{-15}`; `[M, R⊗V]` residual `10^{-15}`).
- **Item 40.** R3 gives the exact eigenvalue statement.
- **Item 44.** R4: the self-correlation ratio separates the two Gaussian models for every pair of propagators.

## 3. The three GAPs marked by the distiller

### GAP A: membership of the frozen measures in R-Esym (lines 3 and 47)

Line 47 reads: "The inference “unbounded Higgs couplings, therefore `ν∈C(G)` at coupling ≤ `g_*`” does not follow without an action, a definition of coupling, and an admissibility/closure proof. Nor does an arbitrarily chosen extension of an observable satisfy a separately fixed `ι′`".

**Verdict: real.** Two steps of the draft's Corollary C.1 do not follow.

*Step 1.* Draft line 111: "R-Esym bounds the gauge coupling and not the Higgs couplings, so `ν ∈ 𝒞(Spin(10))`." R2 (section 5) refutes this inference for every class whose members have densities with respect to Haar measure on the links times any σ-finite reference measure on the Higgs fields. This covers Gibbs measures at every finite value of every Higgs coupling. It applies on every graph with `12|L| > 45|S|`, for instance every periodic 4D box. So frozen measures are not members of such a class. The draft describes the frozen set as "the support of the infinite-hopping limit of a fixed-length Higgs action" and adds "that limit is context, not used" (draft line 60); this report does not prove that limit either. Whether a class contains frozen measures is a property of the pinned class, and R-Esym's wording does not fix it. R6 adds a second obstacle, for classes whose actions are built from `G` plaquette terms and Higgs hopping terms. Restricted to the frozen set in unitary gauge, such an action has one coefficient on all of `𝔨` at quadratic order, so in the Gaussian model of section 5 it gives `N_eff = dim K`. A witness with different couplings on different factors does not have that form. Writing its frozen extension as such an action needs further terms, for example Higgs-dependent plaquette terms, and the pinned class must say whether their coefficients count as gauge couplings.

*Step 2.* Draft line 111: "For `O ∈ Λ_r` let `ι'(O)` be the extension of `ι(O)` given by Theorem C(iii)". In the frozen specification the data are fixed first: `CH1_5O.md` line 175, "Fix in advance the data `D` ... with `ι'` determined by `ι` through a fixed inclusion `j`". So `ι′` is given, not chosen. The property the proof needs is (C2) of R1. It holds automatically for loop lists with the standard identification. For listed Higgs observables it is a condition on the pinned data.

*Repaired statement.* R1. The distiller's last sentence, "An R-Esym class defined to contain these extensions has the corollary's obstruction by premise", is R1 with (C1) true by definition. For loop lists with the standard identification nothing else is needed. For such a class, CH1-5O-E is false for every update and every state. That is the failure of test 3 that line 108 records.

### GAP B: the classes of R-E′ (line 3, with lines 14 and 110)

Line 3 reads: "**GAP:** the proposed R-E′ changes the frozen gauge-Higgs specification and its classes are not pinned; the Gaussian calculation does not establish their separation." It has three clauses.

**(i) "changes the frozen gauge-Higgs specification": not a gap; a reading question** (item 10). The plain reading is: a gauge-Higgs comparison class may have `W = 0`. Four-test check of that reading (proposed, not adopted):
1. It fixes no target. It names no group, breaking pattern, state or member of a class.
2. It is not open-ended. It is one closed clause on the range of `W`.
3. It settles no downstream question by premise. It permits pure-gauge classes and does not require them. CH1-5O-E stays open under it.
4. It adds no structure or constant. It removes a restriction that no stated reason needs.

It passes all four. Only the owner can adopt it.

**(ii) "its classes are not pinned": real.** T0-start's class is a request. `GA2_Y2.md` line 155 reads: "The proposed **T0-start[G]** asks the YM programme to prove its scale-uniform CT1–CT4 bounds and T0 conclusions from every admissible small-coupling start in its inductive class". No pinned product prescription for a non-simple group, its components or its abelian factors is on file. Pass 1 proposes one (draft line 183), and `CH1_5OE.md` line 112 says it "needs its own definition and checks". A repair needs a specification by the owner and by the Yang-Mills programme. This report proposes none.

**(iii) "the Gaussian calculation does not establish their separation": real.** Theorem 7 concerns a stipulated model. The draft's table over-reads it; its line 181 says, for R-E′ test 3, "Lemma D shows the two classes differ in two-point data". *Repaired statement, inside the model:* R4. The self-correlation ratio separates the two models for every pair of propagators. It still says nothing about T0-start classes.

### GAP C: eigenvalues of a classical Case I orbit (line 85)

Line 85 reads: "The assertion that a classical Case I orbit always has four distinct eigenvalues `±ia,±ib` and ranks 3,3,2,2 needs `a,b≠0` and `a≠±b`. For example `(a,b)=(0,1)` is coprime with even `a`".

**Verdict: real in its first sentence, and only at `(a, b) = (0, ±1)`.** The other two exceptions cannot occur. With `a` even and `(a, b)` coprime, `b` is odd, so `b ≠ 0` and `a ≠ ±b`. *Repaired statement:* R3. So draft line 145 ("`q` has the roots `±ia, ±ib` and the `P_j(Φ)` are the FMS projectors ..., of ranks 3, 3, 2, 2") holds for every admissible `(a, b)` except `(0, ±1)`. At `(0, ±1)` the classical projectors have ranks 6, 2 and 2. The draft's Attack B4 (line 203) uses the orbit with plane values `(1, 1, 1, 3, 3)/2`, which has four distinct eigenvalues, so B4 is unaffected. The GAP's second and third sentences are scope remarks, and pass 1 says the same. Draft line 203 reads: "That is a dynamical property of a stationary state. It is part of what CH1-5O-E′ asks, not a consequence of the kinematics." Draft line 207 lists the coset mass and the weak coupling as separate needs. Those two sentences mark no gap in pass 1.

## 4. Check against `CH1_5OE_DRAFT.md` where `CH1_5OE.md` cites it

| `CH1_5OE.md` line | What it says about pass 1 | Draft line | Verdict |
|---|---|---|---|
| 5 | Draft SHA-256 `2c2ff5df…0ac3d` | file | Matches the file read. |
| 14 | R-Esym, R-Easym, R-E′ | 66-68 | R-Easym and R-E′ match. The T0-start clause ("requires a Haar density and further conditions, including reflection positivity") matches the quote at line 68. R-Esym is changed: it now contains the frozen extensions by definition (item 9). |
| 23 | "The definition of exotic in the draft also includes the gluon octet" | 82 | Matches; line 82 cites `CH1_5O_DRAFT.md` line 67, whose frozen form is `CH1_5O.md` Definition 4. |
| 47 | The inference "unbounded Higgs couplings, therefore `ν∈C(G)`" | 111 | Faithful: "R-Esym bounds the gauge coupling and not the Higgs couplings, so `ν ∈ 𝒞(Spin(10))`". |
| 47 | "an arbitrarily chosen extension of an observable" | 111, 48 | Faithful: line 111 chooses `ι′(O)` as "the extension of `ι(O)` given by Theorem C(iii)"; line 48 chooses `j(u) = (u, v̄)`. |
| 47 | "the unconditional assertion that *every* pinned R-Esym instance is false" | 111 | Faithful: "In R-Esym, no update, no state and no pinned data satisfy CH1-5O-E." |
| 83 | Labels `16̄⊕144` credited from memory; scratch check with zero residual and multiplicities 32 and 288 | 143, 145 | Faithful. |
| 85 | Four distinct eigenvalues `±ia, ±ib` and ranks 3, 3, 2, 2 | 145 | Faithful. Line 145 does not say "always", but it states the claim for the Case I orbit with no condition on `a`. |
| 100 | Gram check `c_10 = 2`, `c_45 = 16`; 400,000 samples, 0.1930 against 0.1926 | 165 | Faithful. |
| 106-110 | "Pass-1 check" column | 177-181 | Faithful. |
| 114-119 | Attacks B1-B4 "with corrected stopping points" | 197-203 | Each corrected stopping point is equal to or weaker than the draft's, and each follows from the distilled theorems. |

Results map one to one. Theorem 1 is Proposition V, with clause (ii) made conditional and clause (iii) moved to the remark at line 23. Theorem 2 is Lemmas S and S′. Theorem 3 is Theorem C. Corollaries 3.1 and 3.2 are C.1 (made conditional) and C.2. Theorem 4 is Lemma B. Corollary 4.1 is C.3. Theorems 5 and 6 are Lemma R(i)-(iii) and R(iv). Theorem 7 is Lemma D. Two items of pass 1 were dropped: D1's clause "`c_ρ > 0` if `ρ` is nontrivial", which Theorem 7 replaces by "when the denominator is nonzero"; and C.1's explicit formula for `ν` with Higgs fields, which R1 restores.

## 5. Referee closures

Each closure is a complete argument, written here and unrefereed. None uses a computer.

**R1 (Corollary 3.1 with its hypotheses; closes item 23).** Fix the data `D` of Definition 5 and a candidate `K`. Let `μ` be a probability measure on `K^L × W_1^S`, invariant under `k·(u, η) = (k·u, (σ_1(k_x)η_x)_x)`. Here `(W_1, σ_1)` is a finite-dimensional unitary `K` representation, and `W_1 = 0` is allowed. Take `(W, σ, v)` with `Stab(v) = K` (Theorem 2(i)). Take a `K`-equivariant isometry `J: W_1 → W_2` into a finite-dimensional unitary `G` representation `(W_2, σ_2)` (Theorem 2(ii)). Let `ν` be the law of `(g·u, (σ(g_x)v)_x, (σ_2(g_x)Jη_x)_x)` under `μ ⊗ m^{⊗S}`, and put `j_v(u, η) = (u, v̄, (Jη_x)_x)`. Assume:
- (C1) `ν ∈ 𝒞(G)`;
- (C2) for every `O ∈ Λ_r`, `ι′(O)` is a Borel function on `G^L × W^S × W_2^S`, invariant under the `G` gauge action; every listed product `ι′(O_1)ι′(O_2)` is `ν`-integrable; and `ι′(O)∘j_v = ι(O)` holds `μ`-almost everywhere.

If `μ` meets the bounds of (a), then `ν` meets them under `ι′`, so (b) fails. For lists of loops with the standard identification, (C2) holds for every `v`.

*Proof.* `ν` is gauge invariant: `h·(g·u, σ(g)v̄, σ_2(g)Jη) = ((hg)·u, σ(hg)v̄, σ_2(hg)Jη)`, and `m^{⊗S}` is invariant under `g ↦ hg`. The sampled point equals `g·j_v(u, η)`. Let `F` be a listed product `ι′(O_1)ι′(O_2)`, or a single `ι′(O_1)`. `F` and `|F|` are gauge invariant, so `F(g·j_v(u, η)) = F(j_v(u, η))`. Tonelli on `|F|` and then Fubini give
`E_νF = ∫∫F(g·j_v(u, η)) dm^{⊗S}(g) dμ(u, η) = ∫F(j_v(u, η)) dμ(u, η) = E_μ(ι(O_1)ι(O_2))`,
using (C2) on each factor. Hence `|ω(O) − E_ν(ι′O)| = |ω(O) − E_μ(ιO)| ≤ δ` for every listed product. By (C1), `ν` is a measure of `𝒞(G)` that meets the bounds, so (b) fails. For loops, `ι′(O) = w_{ρ,C}` depends only on the links, and `j_v` keeps the links `u`, so `ι′(O)∘j_v = w_{ρ,C}|_{K^L} = ι(O)`. ∎

**R2 (no frozen extension has a density; refutes the draft's step in GAP A).** Let `λ` be a σ-finite Borel measure on the Higgs space `Y`, for example Lebesgue measure on `W ⊕ W_2`, or an invariant measure on a fixed-length orbit. Let `𝒞_ac(G)` be any class of gauge-Higgs measures on `G^L × Y^S`, each with a density with respect to `m^{⊗L} ⊗ λ^{⊗S}`. Every Gibbs measure `Z^{−1}e^{−A} d(m^{⊗L} ⊗ λ^{⊗S})` with `0 < Z < ∞` is of this kind, at every finite value of every coupling in the action `A`. Let `K` be a candidate, and let the graph satisfy `12|L| > 45|S|`. Then no measure `ν` built as in R1 lies in `𝒞_ac(G)`.

*Proof.* Suppose `ν` has a density `f`. By Tonelli its link marginal has the density `∫f dλ^{⊗S}` with respect to `m^{⊗L}`, so it gives measure zero to every `m^{⊗L}`-null set. The link marginal of `ν` is the law of `g·u`. It is concentrated on the image of `K^L × G^S` under `(u, g) ↦ g·u`. That image is compact, hence Borel, and it is `m^{⊗L}`-null by Corollary 4.1, since `|L| dim K + 45|S| ≤ 33|L| + 45|S| < 45|L|`. So the marginal gives a null set measure one, a contradiction. ∎

`𝒞_ac(G)` is a hypothesis of R2, not a proposed class, so it needs no four-test check.

**R3 (eigenvalues of `ψ(Y)`; repairs GAP C).** Let `(a, b)` be coprime with `a` even. Then `b` is odd, so `b ≠ 0` and `a ≠ ±b`. On `C^{10}` the operator `ψ(Y)` has the eigenvalues `ia` and `−ia` (multiplicity 3 each) and `ib` and `−ib` (multiplicity 2 each). These are four distinct values if and only if `a ≠ 0`. If `a = 0`, then `b = ±1`, and the eigenvalues are `0` (multiplicity 6) and `±i` (multiplicity 2 each).

*Proof.* If `b` were even, 2 would divide `gcd(a, b) = 1`. An even `a` differs from `±b` when `b` is odd. Write `C^{10} = V ⊕ V̄`, the `±i` eigenspaces of the complex structure, with `V = C^3 ⊕ C^2`. On `V`, `ψ(Y) = ia·1_3 ⊕ ib·1_2`. On `V̄` it is the complex conjugate, `−ia·1_3 ⊕ −ib·1_2`. Now `ia = −ia` only if `a = 0`; `ib ≠ −ib` since `b ≠ 0`; and `±ia ≠ ±ib` since `a ≠ ±b`. If `a = 0`, then `|b| = gcd(0, b) = 1`. ∎ [check]: for `(0, 1)` the imaginary parts `−1, 0, 1` occur 2, 6 and 2 times; for `(−2, 3)`, `(2, 3)`, `(2, 1)`, `(4, 1)` and `(2, 5)` there are four values, two of them occurring 3 times and two occurring 2 times.

**R4 (the self-correlation ratio does not depend on the propagator; repairs GAP B(iii) inside the model).** In the model of `CH1_5OE.md` section 5, let `ρ` be nontrivial and `D(C, C) > 0`. Then `Var(w_{ρ,C})/(E w_{ρ,C} − 1)^2 = 2/N_eff`. The ratio does not depend on `D`, on `ρ`, or on a common rescaling of the `σ_A^2`. It equals `2/45 ≈ 0.044` for every `Ad(G)`-invariant model on `G`. It is at least `2/33 ≈ 0.061` for every model on a candidate `K`.

*Proof.* Theorem 7 with `C′ = C` gives `r = 1`. The quotient `S_1^2/S_2` is unchanged by `σ_A^2 ↦ tσ_A^2`. Theorem 7 gives `N_eff = 45` for an `Ad(G)`-invariant covariance, and `N_eff ≤ dim K ≤ 33` for a candidate. ∎

So inside the model, a `G`-model and a candidate model with the same means differ in the variance of each single loop, whatever propagators they use. The "differing propagators" of line 100 matter only for pairs with `r < 1`. Both `E(W^*W)` and `E(W)` are compared data when `W ∈ Λ_r`. The model stays stipulated; R4 says nothing about T0-start classes.

**R5 (exact projectors on finite registers; supports items 35, 50 and 53).** Let `𝒦` be finite dimensional, `𝔅 ⊆ B(𝒦)` a unital `*`-subalgebra, and `Φ ∈ M_d(𝔅)` with `Φ^* = −Φ`. Let `λ_1, …, λ_m` be the distinct eigenvalues of `Φ` as an operator on `C^d ⊗ 𝒦`. They are imaginary; `q(Φ) = 0` for `q(t) = Π_j(t − λ_j)`; and the `P_j(Φ)` of Theorem 5 are the spectral projections of `Φ`.

*Proof.* The map `Φ ↦ Σ_{ab}E_{ab} ⊗ Φ_{ab}` from `M_d(𝔅)` to `B(C^d ⊗ 𝒦)` is an injective `*`-homomorphism. So the image of `Φ` is anti-Hermitian, hence normal with imaginary eigenvalues, and it is unitarily diagonalizable (spectral theorem, cited). `q(Φ)` vanishes on every eigenspace, so it is `0`; by injectivity `q(Φ) = 0` in `M_d(𝔅)`. On the `λ_k`-eigenspace, `P_j(Φ)` acts as `P_j(λ_k) = δ_{jk}`. ∎

So at finite size the hypothesis `q(Φ) = 0` always holds for some `q`. What a finite composite controls is its spectrum. That is the stopping point of B4 as distilled.

**R6 (one plaquette coefficient on all factors, at quadratic order; supports GAP A).** Let `ρ_1, …, ρ_k` be finite-dimensional unitary `G` representations and `β_1, …, β_k` real. Put `s(U) = Σ_iβ_i(1 − Re w_{ρ_i}(U))`. Then `s(exp X) = c⟨X, X⟩ + O(|X|^4)`, with `c = Σ_iβ_ic_{ρ_i}/(2d_{ρ_i})`. For a fixed-length Higgs hopping term, `|σ(exp X)v − v|^2 = |dσ(X)v|^2 + O(|X|^3)`, and `dσ(X)v = 0` for `X ∈ 𝔨 = Lie(Stab v)`.

*Proof.* `tr ρ(exp X) = Σ_{n≥0}tr(dρ(X)^n)/n!`. The `n = 1` term vanishes, since `so(10)` is perfect (line 100). `dρ(X)^3` is anti-Hermitian, so its trace is imaginary and drops out of the real part. `tr dρ(X)^2 = −c_ρ⟨X, X⟩` by Theorem 7. Hence `1 − Re w_ρ(exp X) = c_ρ⟨X, X⟩/(2d_ρ) + O(|X|^4)`. For the hopping term, `σ(exp X)v − v = dσ(X)v + O(|X|^2)`. If `X ∈ 𝔨`, then `σ(exp tX)v = v` for all `t`, so `dσ(X)v = 0`. ∎

Consequence. In unitary gauge the frozen set is `K^L × {v̄}`. There every hopping term vanishes, since `σ(u_ℓ)v = v`, and `s(u_p)` has the quadratic form `c⟨X_p, X_p⟩` on `𝔨`. So the restriction of an action made of such plaquette and hopping terms to the frozen set has one coefficient on every simple or abelian factor of `𝔨`. In the stipulated Gaussian model it gives one variance on `𝔨`, so `N_eff = dim K`. A witness `μ` with different couplings on different factors has a different action on `K^L`. Writing its frozen extension as an action of this kind needs further terms, for example Higgs-dependent plaquette terms. A pinned R-Esym class must say whether their coefficients are gauge couplings bounded by `g_*`. R6 is exact for quadratic forms; it proves nothing about measures outside the model.

## 6. Required edits

Required before the freeze (E1-E7):

- **E1** (item 13, line 19). Replace the draft names: "If the hypotheses of `CH1_5O.md` Theorems 1, 2, 3, 5, 6 and 7 (draft Lemma G, Theorem E, Corollary IR, Theorem L, Corollaries L.2 and L.4) hold for these states".
- **E2** (item 10, lines 3, 14, 110). Line 14, last sentence: "R-E′ takes the zero Higgs representation on both sides. By Definition 3 these measures are gauge-Higgs measures. So R-E′ instantiates the frozen specification if a gauge-Higgs comparison class may have `W = 0`; the frozen text does not say, and the owner may specify." Line 3: delete "changes the frozen gauge-Higgs specification and". Line 110: replace "pure gauge changes frozen CH1-5O-E" by "whether pure gauge is admissible in frozen CH1-5O-E turns on the `W = 0` reading".
- **E3** (item 49, line 112). Replace "such that some `K`-class measure satisfies (a) and no `G`-class measure satisfies (b)" by "such that (a′) some `K`-class measure meets the bounds of (a), and (b′) no `G`-class measure meets those bounds".
- **E4** (item 23, lines 43-45). State Corollary 3.1 with R1's hypotheses (C1) and (C2) and the explicit `ν` with Higgs fields, or replace it by R1 labelled "referee closure, `CH1_5OE_REFEREE.md`". Keep the sentence "This includes R-Esym only when its definition actually guarantees that closure."
- **E5** (item 9, lines 14, 43, 47, 108). Give the two R-Esym classes two names. For example: R-Esym for the draft's class (gauge coupling at most `g_*`, Higgs couplings unbounded, contents otherwise unpinned), and R-Esym-F for the class that contains the frozen extensions by definition.
- **E6** (item 3, head). Add the inputs-and-credits paragraph of section 2.2.
- **E7** (item 38, line 83). Replace the first sentence by "The 32-dimensional channel is the range of `Γ`; the 288-dimensional channel is the kernel of Clifford multiplication `Γ^*: e_a ⊗ ψ ↦ γ_aψ`."

Optional, not blocking (E8-E14):

- **E8** (line 3). Add Theorem 2 and Corollary 4.1 to the list of proved results.
- **E9** (line 13). Restore "with coupling at most `g_*`" and "(b) no `C(G)` measure matches the same list under `ι′` within `δ`".
- **E10** (line 23). Cite `CH1_5O.md` Definition 4 for the definition of a colour-exotic type.
- **E11** (lines 49-53). Rename the subgroup `J` of Corollary 3.2, for example to `K″`.
- **E12** (line 89). "Fix a closed `K ⊆ G` (a candidate, or `G` itself)".
- **E13** (line 127). Add AM and "the formulation of IR and AM (`CH1.md` Definition 8)".
- **E14** (lines 47, 73, 85, 100). Attach R2 and R6 to GAP A, R5 to the remark at line 73, R3 to GAP C and R4 to the remark at line 100, each labelled "referee closure, `CH1_5OE_REFEREE.md`", as `CH1_5O.md` does for its imported closures.

## 7. Open statements to carry by name

- **CH1-5O-E** (OPEN specification; `CH1_5O.md` line 175, `CH1_5OE.md` Definition 5). Unchanged by this report.
- **CH1-5O-E′** (proposed, OPEN, not adopted; `CH1_5OE.md` line 112 as corrected by E3). Its attacks B1-B4 stop at the steps named in `CH1_5OE.md` section 6; A1-A4 carry over from `CH1_5O.md`. Whether it is an instance of CH1-5O-E turns on the `W = 0` reading (section 3, GAP B(i)), which the owner may specify.
- **The R-A residual** (`CH1_5O.md`; OPEN, and it matters only under R-A).
- Inherited, unchanged: **CH1-5O-i**, **CH1-5U-i**, **AM**, **AM-5**, **CH1-i**, **CH1-ii**, **CG1-i**, **CG1-ii**, **CG1K-loc**, **CG1K-H**, **LW1-5-BG**, **LW1-5-X**, **GA1-P-5**, **Y2-W[`L5-O`]**, **VC1**, the formulation of **IR** and **AM** (`CH1.md` Definition 8), and the requests **T0-start[G]** for `Spin(10)` and for the factors of a candidate group.

This report opens no new statement. Hypothesis (C1) of R1 is a property of a class still to be pinned, not a new lemma.

## 8. Freeze recommendation

**Recommendation: `CH1_5OE.md` can enter the frozen part by a dated amendment once E1-E7 are applied.** Every theorem and corollary of the file is correct under its stated hypotheses; Corollary 3.1 is correct once R1's hypotheses are written into it. The four ERRORs are a citation, two garbled sentences and one reading stated as a fact. None changes the content of a theorem. The two INCOMPLETE items are a missing credits line and Corollary 3.1's hypotheses; both have closures here. The three GAPs are real as section 3 states. They can stay in the frozen text as GAPs, with R1, R2 and R3 attached.

The amendment should follow the form of `CH1.md` Amendment 2. It should record that no proved result changes. It should say that CH1-5O-E stays an open specification, and that CH1-5O-E′ is proposed and not adopted. It should not adopt R-E′, the `W = 0` reading, or any comparison class. A possible text, for the lead to check and not adopted here:

> No proved result of this file changes. `CH1_5OE.md` (Claude draft `CH1_5OE_DRAFT.md`, Codex distillation, referee `CH1_5OE_REFEREE.md`, frozen) proves: the exactness results of `CH1_5O.md` restrict no gauge-invariant data, and gauge-invariant operators have only the trivial `H`-type (Theorem 1); every closed subgroup is a stabilizer, and every `K`-gauge measure has a frozen `Spin(10)` gauge-Higgs extension with the same gauge-invariant expectations (Theorems 2-3); a `Spin(10)` comparison class that contains these extensions makes CH1-5O-E false by premise (Corollary 3.1 with the referee's hypotheses), while no class of measures with densities contains them on large windows (referee closure R2); every closed `K` with `H ⊆ K ⊊ Spin(10)` has `dim K ≤ 33` (Theorem 4); the polynomial projectors of a covariant operator matrix are exact once `q(Φ) = 0`, whatever the commutators of its entries (Theorem 5); and in a stipulated Gaussian model, two-loop data separate `Spin(10)` from every such `K` (Theorem 7). Open: CH1-5O-E (an open specification) and the proposed variant CH1-5O-E′; whether a pure-gauge class is admissible in CH1-5O-E is a reading for the owner. No named failing step for either law.

---

## FINISH

**Proved here (referee closures, unrefereed).**
- Verdicts on `CH1_5OE.md` at `1a6005d26`: 56 items, 50 CORRECT, 4 ERROR, 2 INCOMPLETE. Every theorem and corollary holds under its stated hypotheses; Corollary 3.1 holds under R1's.
- R1: Corollary 3.1 with explicit hypotheses (C1) and (C2), with Higgs fields on both sides. (C2) holds automatically for loop lists with the standard identification.
- R2: on any graph with `12|L| > 45|S|`, no frozen extension of a measure of a candidate `K` has a density with respect to Haar measure on the links times any σ-finite reference measure on the Higgs fields.
- R3: for coprime `(a, b)` with `a` even, `ψ(Y)` has four distinct eigenvalues, of multiplicities 3, 3, 2 and 2, if and only if `a ≠ 0`. At `(0, ±1)` it has three, of multiplicities 6, 2 and 2.
- R4: in the Gaussian model, `Var(w_{ρ,C})/(E w_{ρ,C} − 1)^2 = 2/N_eff`, whatever the propagator, the representation and the scale. It is `2/45` for `Spin(10)` and at least `2/33` for every candidate.
- R5: on a finite register, an anti-Hermitian covariant matrix has exact polynomial projectors, namely its spectral projections.
- R6: at quadratic order, `G` plaquette terms and Higgs hopping terms give one coefficient on all of `𝔨`.

**Counterexamples.**
- To the draft's step "R-Esym bounds the gauge coupling and not the Higgs couplings, so `ν ∈ 𝒞(Spin(10))`" (draft line 111): R2, for every class of measures with densities, for instance Gibbs measures at any finite couplings, on every periodic 4D box.
- To draft line 145, the roots `±ia, ±ib` with ranks 3, 3, 2, 2 for every even-`a` Case I orbit: `(a, b) = (0, 1)` (R3).
- To `CH1_5OE.md` line 83, first sentence: the image of Clifford multiplication is all of `C^{32}`, and the kernel of `Γ` is `0` (item 38).

**Open, by name.** CH1-5O-E (open specification); CH1-5O-E′ (proposed, not adopted); the R-A residual; inherited and unchanged: CH1-5O-i, CH1-5U-i, AM, AM-5, CH1-i, CH1-ii, CG1-i, CG1-ii, CG1K-loc, CG1K-H, LW1-5-BG, LW1-5-X, GA1-P-5, Y2-W[`L5-O`], VC1, the formulation of IR and AM, and T0-start[G] for `Spin(10)` and for the factors of a candidate group.

**What changes downstream.**
- *`CH1_5OE.md`:* ready to enter the frozen part by a dated amendment after E1-E7 (section 6).
- *Pinning CH1-5O-E:* a `Spin(10)` class that contains the frozen extensions of the `G∞` witnesses makes CH1-5O-E false by premise (R1). A class of measures with densities contains none of them on large windows (R2), so Theorem 3 alone decides nothing for such a class.
- *R-E′:* whether it instantiates the frozen specification turns on one reading, `W = 0`. That reading passes the four tests and awaits the owner.
- *GA2 and Definition SC:* in the Gaussian model, the variance of one listed loop separates `Spin(10)` from every candidate, whatever the propagators (R4). A certificate still needs `δ` below that variance, which is of order `g^4`.
- *FMS projectors on `L5-O` (B1, B4):* exact projectors always exist on finite registers (R5). The open point is the spectrum of a block composite, as `CH1_5OE.md` says.
- *Named failing steps for `L5-O` or `L5-U`:* none. Both laws stay live under the owner decision of `TOE_ASSEMBLY.md` §3.5.
