# Independent hostile review of BALABAN_EXTRACT.md

## PRE-STATED — 2026-10-29 03:09:53 UTC

This protocol is written before reading the target's arguments or deriving findings. The target is `BALABAN_EXTRACT.md`, especially §§5–9, tested against the ten supplied arXiv text extractions. This review is independent of the extract's asserted proof statuses. No git commands, numerical approximations, audit ledgers, snapshots, or full read of `PROOF.md` will be used. Only this deliverable will be written; findings will be appended during the review. Read-only operating instructions are the only intended additional files.

### Targets and falsifiers fixed in advance

1. **(a) Thresholds and uniform constants.** Identify the precise field, normalization, region, coupling, scale, and quantifiers in each small-field condition. A coupling-dependent cutoff in an exposition refutes an unqualified fixed-cutoff account of that exposition, but does not by itself refute a separate fixed geometric admissibility radius in nonabelian Yang–Mills. A purported direct-in-scale estimate that actually assumes an inductive stability bound, localization estimate, or running-coupling cutoff refutes the claim that the full-step constraint alone supplies that estimate.
2. **(b) Coupling flow.** Separate an exact rescaling identity, a perturbative coefficient, a conditional induction, and a nonperturbative all-scale flow theorem. A stated/proved flow theorem in the allowed corpus defeats a blanket absence claim at that scope. Absence from these expositions cannot establish absence from inaccessible CMP papers.
3. **(c) Wall map and §7.7.** Rebuild the implications used to classify inherited versus new obligations. A cited theorem with different dimension, field content, normalization, or hypotheses does not establish the target conclusion. A claimed obstruction must be logically necessary, rather than merely an obstruction to one proof strategy.
4. **(d) Eight PROOF.md paraphrases.** Locate the quoted text by string, inspect only relevant ranges, and distinguish a false mathematical assertion from unsupported attribution and from a drifted citation. A refutation needs a counterexample, incompatible source statement, or demonstrable logical failure; unavailable evidence alone is insufficient.
5. **(e) BAL-F2.** Distinguish hard block-average constraints, hard small-field indicators, soft Gaussian block penalties, and physical support restrictions. A uniform estimate for the same relevant object without the alleged necessary hard constraint defeats necessity; an estimate for a different theory/object supplies only a limited comparison.
6. **Systemic defects.** Track symbol identities by file and locating string; check input/output quantifiers and stale minima; ask whether every decisive gate could reject a false case. Verify cited line locations against current text, without using old line numbers as search keys.

### Verdict and evidence discipline

Findings use **CONFIRMED / NOT-VERIFIED / REFUTED** for the expressly scoped proposition; claims use **PROVEN / ARGUED / CONDITIONAL / GAP / OPEN**. Every finding will attach to an exact file and current line or locating string. Third-party material will be paraphrased and identified by arXiv ID plus section/equation; no third-party prose will be copied into the repository. Any corrected number will include an exact derivation. Final closure will state precisely what can be banked and the most dangerous remaining unverified assertion.

## Findings (appended during review)

### F1 — Source silence is not a refutation gate

**Verdict: REFUTED. Claim status: GAP.** Attachment: `BALABAN_EXTRACT.md:32–36`, locating string `What counts as a refutation`, especially the alternative `the read source does not state`; compare the unavailable-body caveat at lines 108–112 and the eight-item count at lines 687–689.

The gate conflates an unsupported attribution with a contradicted assertion. If a readable review states P but is silent about Q, both P∧Q and P∧¬Q remain possible. Thus failure to find Q in that review cannot establish ¬Q or that an inaccessible original never states/proves Q. The adjacent NOT-VERIFIED rule for inaccessible papers is the correct rule; it must also govern claims supported only by omissions in their reviews. The eight REFUTED labels require individual reassessment below. This is a check that cannot decide the proposed negative conclusion, rather than a mathematical refutation of all eight underlying paraphrases.

**Scope receipt.** The two additional read-only files are `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`. Their evidence discipline is applied within the user's narrower file/write restrictions; no git, broader workflow, landing, ledger, or extra authority-file reads are performed. The target's append-only errata in §§11 and 13 are part of the reviewed target: an explicitly corrected sign or narrowed assertion is not counted again as an uncorrected defect.

### F2 — Fixed geometric domains and coupling-dependent integration cuts have been conflated

**Verdict: REFUTED for the general fixed-threshold account; NOT-VERIFIED for the exact CMP 109 statement. Claim status: GAP for the transfer to 4D SU(N).** Attachments: `BALABAN_EXTRACT.md:274–277` (M7), `:448–467` (threshold-based dismissal in §7.6), `:514–539` (B3-4/B3-5/lead-file refutations), `:601–604` (BAL-F2's fixed-threshold premise).

The directly readable accounts distinguish at least the following objects:

| Source and locator | Object and normalization | Actual dependence |
|---|---|---|
| [arXiv:1108.1335](https://arxiv.org/abs/1108.1335), §3.2, (109)–(111) | Scalar integration domain; canonically normalized field and block residual | With `λ_k=L^{-(N-k)}λ`, set `p_k=(-log λ_k)^p`; residual and gradient are bounded by `p_k`, the field by `λ_k^{-1/4}p_k`. The larger complex domain uses further powers of `λ_k`. |
| [arXiv:1512.04373](https://arxiv.org/abs/1512.04373), §6.1, (395)–(396); supplied text lines 2984–3002 | QED3 real minimizer curvature and axial fluctuation | `\|d𝒜_k\|≤(-log e_k)^p` and `\|A_k-H_k^x A_{k+1}\|≤(-log e_k)^{p_0}`, with `p_0<p`. These are two different cuts, both coupling dependent. |
| arXiv:1512.04373, §4.2, (286)–(287) | QED3 complex gauge-potential regularity domain | Potential, derivative, and Hölder derivative have radii `e_k^{-3/4+ε}`, `e_k^{-3/4+2ε}`, `e_k^{-3/4+3ε}`. Here `ε` is a fixed exponent margin, not CMP 109's curvature radius. |
| [arXiv:2204.07201](https://arxiv.org/abs/2204.07201), §3, (14)–(17), and §5 after Theorem 2 / before (74); text lines 730–737 | QED3 small/large-field decomposition | The cutoff is `p(e_k)=(-log e_k)^p`, with `e_k=L^{-(N-k)/2}e`; successive cuts tighten as k increases. |
| [arXiv:2204.08252](https://arxiv.org/abs/2204.08252), §1.5, Theorem 1, (27); §3.4, (98) | Sigma-model deterministic variational regularity class | Fixed small radii `ε_0,ε_1`, tied by `B_3 ε_1≤ε_0`. This is a different domain and a different model. |

The normalization matters. For an abelian unit-scale link `U_b=exp(i e_k A_b)`, its plaquette obeys `|1-U_p|=2|sin(e_k(dA)_p/2)|≤e_k|(dA)_p|`. The QED curvature cut therefore implies a dimensionless link cut `e_k(-log e_k)^p`. This tends to zero as `e_k→0`, although the allowed canonical curvature grows. This derivation explains how a coupling-scaled link threshold and a fixed admissibility radius can coexist: for sufficiently small e, the former lies strictly inside the latter. Neither equality of the two domains nor a contradiction follows.

**What fails:** the expositions do not support excluding coupling-dependent cuts from Balaban's method in general, or using their absence to dismiss the lane's threshold option. **What does not fail on this evidence:** a fixed CMP 109 geometric background class may indeed exist; the corpus does not independently verify its exact (1.2)/(2.9), nor show that it equals the integration domains in later CMP papers. QED3 and scalar φ⁴3 do not prove a 4D nonabelian threshold prescription. B3-5 already acknowledges Dimock's logarithmic cuts; the defect is exporting the narrower CMP 109 assertion into the broad planning conclusion.

### F3 — The extract's own alternative cut invalidates its unconditional summability dismissal

**Verdict: REFUTED as an all-regime inference. Claim status: PROVEN for the conditional algebra below; OPEN for the cut's admissibility in the lane.** Attachments: `BALABAN_EXTRACT.md:275–277`, `:516–521` (especially the claim that the no-uniform-iteration conclusion is unaffected), and `:646–647` (M7 erratum). Matching current transcription: `PROOF.md:1401–1404`, locating string `1/g² + β(K - k) log L`.

Use only the formulas the extract itself assumes. Write `n=K-k`, `t=n log L>0`, `a=g_K^{-2}`, and `h_k=ε_1 g_k/(C t)`. From `a+βt≤g_k^{-2}≤a+β't`, exact algebra gives

`(ε_1/C)(β+a/t) g_k³ ≤ h_k ≤ (ε_1/C)(β'+a/t) g_k³`.

The omitted finite-scale term is **`a/t=g_K^{-2}/((K-k)log L)`**. The cubic comparison with coefficients β/C and β'/C is only an asymptotic statement when `a/t→0`. If n is fixed and `g_K→0`, instead `h_k/g_k=ε_1/(C n log L)` is constant: the cut is exactly linear in `g_k`. At n=0 the displayed alternative is undefined. Thus the erratum's all-regime exclusion of linear scaling is false.

Moreover, for fixed terminal g and β>0,

`h_{K-n} ≤ ε_1/[C sqrt(β) (log L)^{3/2}] · n^{-3/2}` for `n≥1`.

Since `Σ_{n≥1}n^{-3/2}≤1+∫_1^∞x^{-3/2}dx=3`, this alternative has a k-uniformly summable tail. In particular `∏(1+D h_{K-n})≤exp(D Σ h_{K-n})` is bounded if D is uniform. By contrast, the bounds on g give a divergent `Σ g_{K-n}` of order `Σ n^{-1/2}`. These are different answers to the precise iteration test. Fixed cuts still give no such summability, but the extract cannot say its conclusion is unaffected for all cuts it lists. This does **not** establish that the alternative applies to the same field `φ_j`, retains uniform D, controls excluded fields, or repairs the proof; all four are missing bridge obligations.

### F4 — Direct-in-k definitions do not make the local inverse a fixed finite problem

**Verdict: REFUTED for the stated reason; CONFIRMED for the scalar uniform-bound mechanism below. Claim status: PROVEN for the elementary coercivity and series argument; CONDITIONAL for the full derivative estimates and their nonabelian transfer.** Attachments: `BALABAN_EXTRACT.md:231–239` (especially `fixed finite problem after scaling`) and `:250–260` (M1/M3).

In arXiv:1108.1335 §2.4, (79)–(85), the local cube has coarse-unit side 3M and lattice spacing `L^{-k}`. Its scalar dimension scales as **`(3M L^k)^3`**, not a fixed finite dimension. Rescaling it to unit spacing enlarges its side to `3M L^k`; rescaling preserves the number of variables. Fixed geometric size therefore does not establish a uniform inverse bound.

The source supplies the missing analytic input in Appendix D, Lemma 29, (342)–(348), rather than deriving it from finiteness. Rebuilding its essential coercivity argument: on each unit block, split f into its mean and mean-zero part. The positive block penalty controls the mean; a unit-block discrete Poincaré inequality controls the mean-zero part through the gradient with a constant independent of the mesh. For normalized block averages, `Q_k Q_k^T=I`. The soft coefficients satisfy

`a_k = a/(1+L^{-2}+…+L^{-2(k-1)})`, hence `a(1-L^{-2})≤a_k≤a` for `k≥1`.

Thus `||f||²≤C_P||∂f||²+||Q_k f||²` gives `⟨f,(-Δ+μ̄_k+a_kQ_k^TQ_k)f⟩≥min(C_P^{-1},a(1-L^{-2}))||f||²`, for `μ̄_k≥0`. The small physical mass is not the uniform gap. Summing block inequalities only discards positive bonds across block boundaries. Appendix D then adds weighted and pointwise regularity estimates; an L² gap alone is not a proof of all the quoted Hölder/sup bounds.

Once local estimates have a genuinely uniform constant `C_loc`, the commutator with a smooth cutoff in a partition of unity produces `C_loc/M` per step. With bounded walk branching b, a walk series is bounded by `C_0 Σ_{r≥0}(b C_loc/M)^r=C_0/(1-b C_loc/M)` if `b C_loc<M`. This gate can fail and is non-circular only because `C_loc` was controlled before choosing M. It sums **walk length r**, not RG depth k. No product of k operator-norm bounds is needed. This supports the extract's central mechanism while rejecting its shortcut for the crucial input.

The source also contradicts an absolute no-iteration gloss: arXiv:2204.07201 §5, (53)–(55), constructs the k-step minimizers as compositions of single-step operators; arXiv:1712.10029 §3.9, Theorem 1, (327)–(331), proves multiscale regularity by induction on k. Composed definitions, induction, and direct uniform estimates coexist. What is avoided is multiplying a lossy norm estimate at every RG step, not composition or induction itself.

### F5 — The missing gauge-field theorem supplies a weighted supremum, not the lane's unweighted source estimate

**Verdict: CONFIRMED for the stated abelian comparison; NOT-VERIFIED for (G♯_0-field), (SPD)/(W2), and the nonabelian transfer. Claim status: CONDITIONAL.** Attachments: `BALABAN_EXTRACT.md:373–386`, `:428–440`, and `:469–478`.

The supplied full text removes the extract's access truncation at arXiv:1712.10029 §3.2. In §3.7.1, (285)–(290), weights must satisfy `p_{j'}/p_j≤L^{|j-j'|}`. Both `p_j=1` and, for sufficiently small terminal e, `p_j=(-log e_j)^p` are allowed. In §3.9, Theorem 1, (327), local gauge-equivalent potential/derivative/Hölder bounds are controlled by `C_0 M p_j` times

`sup_{1≤j'≤k} L^{-3(k-j')/2} p_{j'}^{-1} ||dA_{j',δΩ_{j'}}||∞`.

Here `C_0` depends on L, M must be sufficiently large, the coarse data satisfy specified axial conditions, and the domains form a multiscale history. The introduction and §3.9 identify this as an abelian version of the CMP regularity results. It is substantially better evidence than a fermion propagator analogy, and supports the extract's weighted-supremum pointer.

Rebuilding why this does not settle the lane's level count: the source indices label disjoint geometric shells `δΩ_j`, and the norm includes explicit scale and weight factors. By contrast, k sources living on overlapping copies of one coarse region can have the same sign and identical responses: any nonzero linear response T then gives `T(Σ_{j=1}^k f)=k T f`, although `sup_j||f||=||f||`. An embedding preserving the relevant norms and spatial organization is indispensable. Neither a supremum in the source theorem nor an abelian result turns this into a uniform estimate for arbitrary all-level chain sources. The excerpt immediately before Theorem 1 also corrects an earlier failure of averaging identities in multiscale domains; unverified transfer of global identities is specifically unsafe here.

### F6 — Background-dependent linear averages still compose into one soft quadratic penalty

**Verdict: REFUTED as stated. Claim status: PROVEN for arbitrary frozen linear maps; OPEN for the nonlinear chain Hessian.** Attachment: `BALABAN_EXTRACT.md:363–367`, locating string `At Z ≠ 1` / `no longer a single composite term`.

Background dependence of the linear maps alone does not cause the claimed failure. Let `Q_0,…,Q_{k-1}` be any fixed linear maps (including maps evaluated at a nontrivial background), let `κ_i>0`, fix x₀ and x_k=B, and minimize `½ Σ_i κ_i||Q_i x_i-x_{i+1}||²` over intermediate x's. Define `P=Q_{k-1}…Q_0`, `P_{i+1,k}=Q_{k-1}…Q_{i+1}` (empty product I), and

`Σ=Σ_{i=0}^{k-1} κ_i^{-1} P_{i+1,k}P_{i+1,k}^T`.

Writing `r_i=Q_i x_i-x_{i+1}`, telescoping gives `B-Px₀=-Σ_i P_{i+1,k}r_i`. Minimizing this weighted quadratic under that linear relation gives `r_i=-κ_i^{-1}P_{i+1,k}^T Σ^{-1}(B-Px₀)` and minimum

`½ (B-Px₀)^T Σ^{-1}(B-Px₀)`.

The last summand in Σ is `κ_{k-1}^{-1}I`, so Σ is positive definite without any commutation or covariance assumption on the Q_i. Gaussian integration gives the same exponent, plus a determinant normalization. What may cease to be scalar is the penalty covariance Σ; it remains one composite term.

A nonlinear Hessian can additionally contain residual/multiplier times second derivatives of the averaging map, and gauge slices may alter its domain. Those are real additional obligations. They cannot be replaced by the assertion that background covariance of frozen Q's destroys Gaussian composition. Nor does this identity by itself bound Σ, its inverse, or the full chain inverse uniformly in k.

### F7 — Exact hard-source absorption is linear-coordinate-specific

**Verdict: CONFIRMED for the linear identity; REFUTED as an automatic nonlinear source-transfer rule; NOT-VERIFIED for its application to (SPD)/(W2). Claim status: PROVEN for the algebra, OPEN for the application.** Attachments: `BALABAN_EXTRACT.md:432–441`, `:607–618`, and the corrected sign at `:708–710`.

For a fixed hard **linear** constraint `QA=B`, adding `⟨s,QA⟩` changes the objective by the constant `⟨s,B⟩`. The set of minimizers is unchanged. For a soft penalty, completing the square gives

`κ||QA-B||²/2+⟨s,QA⟩ = κ||QA-(B-s/κ)||²/2+⟨s,B⟩-||s||²/(2κ)`.

For quadratic fine action with Hessian K and positive definite `K+κQ^TQ` on the space being minimized over, the change in minimizer is `-(K+κQ^TQ)^{-1}Q^Ts` (with the corresponding restricted maps on a fixed slice). Thus the extract's append-only sign repair is correct. The claim that the change is nonzero for every nonzero s additionally needs `Q^T` injective on the relevant data space and compatibility with the gauge slice. Normalized full-row-rank scalar block averages have this property; an arbitrary constrained/sliced map need not.

For a nonlinear composite constraint `F(A)=B`, it is `⟨s,F(A)⟩`, not an arbitrary linear source in `Ran DF(A₀)^T`, that is constant. Explicit counterexample: constrain `(x,y)` by `x+y²=0`, minimize `S=(x²+y²)/2`, and take `A₀=(0,0)`. The original minimum is `(0,0)`. Since `DF(A₀)=(1,0)`, the source `3x/2` lies in the alleged normal range. On the constraint the new objective is `y⁴/2-y²`, whose minima are exactly `(x,y)=(-1,±1)`, with value `-1/2`; its value at the old minimum is 0. The hard nonlinear constraint did not absorb the linear source.

Linearizing the constraint does not remove this issue: in coordinates `x'=x+y²`, the same source becomes `3x'/2-3y²/2`. The residual quadratic term is precisely what an exact change of variables must retain. Goswami, arXiv:2204.08252 §3.3, Lemma 5 and (70)–(74), likewise uses a nonlinear correction to linearize its constraint. The extract itself recognizes multiplier-times-second-derivative terms in §7.6; its §9 localization to exactly two soft-scheme obligations has not traced those terms and their norms through this coordinate change. Hard absorption is bankable as the displayed linear identity only.

### F8 — A conditional stability theorem cannot establish nonexistence of a coupling-flow proof

**Verdict: REFUTED for the negative inference; NOT-VERIFIED for the exact CMP 122 II theorem and historical absence claim. Claim status: OPEN for a verified 4D SU(N) marginal-flow input.** Attachments: `BALABAN_EXTRACT.md:278–282`, `:299–312`, `:505–513`, `:559–564`, and `:615–617`.

The supplied corpus establishes a distinction the extract needs to retain. In arXiv:1108.1335 §3.1, (106), and arXiv:1212.5562 §3.3, Remark 2, (222), `λ_{k+1}=Lλ_k` is the chosen canonical scalar scaling; counterterms and polymer interactions have a separate dynamical problem. In arXiv:1502.02946 §1.1 and §1.3, (20), the model is explicitly superrenormalizable, without coupling-constant renormalization, and `e_{k+1}=L^{1/2}e_k`. The same charge scaling appears in arXiv:2009.01156 §2.1, (7), and §2.2, (28). It is not a four-dimensional asymptotically free beta-function theorem.

There is also positive historical context which should not be erased: arXiv:1108.1335 §1.1 credits Balaban's Yang–Mills ultraviolet analysis in dimensions 3 and 4, while arXiv:1502.02946 §1.1 distinguishes the incomplete full-flow treatment in his early scalar-QED work from improvements in later papers on other models. Neither statement identifies or proves the particular 4D running-coupling theorem sought here. They reinforce the need to distinguish a full RG representation, a stability theorem, and a marginal-coupling trajectory theorem.

However, these papers do prove nontrivial flows of other parameters. ArXiv:2009.01156 §2.2, Proposition 1, (28)–(30), fixes a unique sequence of vacuum-energy, mass, and polymer parameters with specified boundary conditions; §2.3, Theorem 1, then assumes initial values chosen using that result. ArXiv:2204.07201 §5, (72)–(73), explains the corresponding sequence-space fixed point. This is an explicit example of a theorem stated conditionally on small quantities coexisting with a proof that those hypotheses can be arranged.

Logically, `(all g_k≤γ) ⇒ stability` is compatible with a separate theorem `∃ bare g_0 : all g_k≤γ and g_K=g`. A review's omission of the latter supplies no contrary evidence. CMP 119/122's actual treatment remains unverified here; there is no independently read CMP body in this review. The extract can bank **no verified 4D flow imported from the presently checked corpus**, not **no published flow proof exists** or **a hard scheme cannot inherit one**.

Nor do two-sided logarithmic bounds imply the stated one-loop limit. For an exact elementary witness, let inverse-coupling increments alternate between 1 and 2. Their n-step cumulative sum lies between n and 2n, but the increments do not converge. A tensor Ward identity determines an allowed transverse form; it does not determine its scalar coefficient, sign, or a trajectory staying in the required interval. Those remain separate obligations.

### F9 — Analyticity is a conditional route to derivative bounds, not closure of the wall map

**Verdict: CONFIRMED for the conditional Cauchy mechanism; NOT-VERIFIED for (N-bg)/(H-C) and the claim that only two soft-scheme items remain. Claim status: CONDITIONAL / OPEN.** Attachments: `BALABAN_EXTRACT.md:388–402`, `:469–478`, `:614–618`; compare the target's own explicit missing-input list at `:240–243`.

Cauchy estimates need a **uniform input-domain margin and uniform norm bound for the relevant function**. They do not follow from analyticity of the minimizer alone. For example, `f_k(z)=kz³` is entire, and even has `|f_k(z)|≤1` on `|z|≤1/k`, but `f_k'''(0)=6k`. For a fixed input margin r and bound M in the appropriate norm, Cauchy does give a uniform directional third derivative `≤6M/r³`; multilinear/operator norms and sums over coordinates need their own norm conversion. Integrating that derivative gives a Hessian Lipschitz bound on an interior domain.

The extract's M4 lists additional effective-action bounds; **with those and a uniform input radius**, its proposed mechanism is sound. Goswami's §4, (101)–(104), demonstrates analyticity through the implicit critical-point equation, but an output condition on `|ℋ(B)|` is not by itself a uniform B-polydisc or a bound on the lane's effective action. A composite background also must be identified with the lane's per-level branches before it supplies their derivatives. Current `PROOF.md`, locating string `Without one of these, COMP proves`, expressly leaves this composite/tower distinction conditional. Thus §7.7 is a research map, not a theorem import or a proof that remaining hard/soft differences are exhausted by (SPD)/(W2) and a level count.

### F10 — The eight advertised paraphrase refutations do not survive as eight established refutations

**Verdict: REFUTED for banking the eight-item count as established; individual dispositions below. Claim status: GAP for the blanket verdict.** Attachments: `BALABAN_EXTRACT.md:490–539` and `:687–689`. The verdict column evaluates **the extract's claimed refutation**, not the truth of every underlying PROOF.md assertion.

| Extract item and attachment | Current locating string / place | Review verdict on the extract's refutation | What the evidence actually supports |
|---|---|---|---|
| B3-1, target :491–498 | `PROOF.md:1032`, `CMP 102's Theorem 1 is about the hard constraint (0.4)` | **NOT-VERIFIED** | The exact historical averaging map and theorem hypotheses cannot be independently recovered from the allowed CMP-free corpus. Chronology and a later declaration of a new definition identify a transfer obligation, but do not independently prove the old theorem's quantified scope. The extract's §13 concedes that the old map is inferred. Keep the import pending. |
| B3-2, target :499–504 | `PROOF.md:6739–6740`, `covariances, CMP 95/96/102b` | **CONFIRMED, narrowly: add/correct the primary pointer** | ArXiv:1410.2798 §3.8, (108)–(110), explicitly presents an abelian simplification of the multiscale nonabelian analysis in its reference [7], CMP **99:389–434**; its references identify the other titles. This verifies the missing central pointer, not an assertion that CMP 95/96/102 contain no relevant auxiliary results. |
| B3-3, target :505–513 | `PROOF.md:1377,1379`, `β_j → 2 b0 ln L` / `Sources: CMP 109`; correction already at :1405 | **NOT-VERIFIED as a claim about the complete originals** | The supplied transcription explicitly withdraws the coefficient attribution, and two-sided bounds do not prove the limit (F8). No CMP-body absence proof has been checked. The needed exact coefficient/trajectory theorem remains OPEN, not disproved. |
| B3-4, target :514–523 | `PROOF.md:4399–4401`, `Balaban-type per-level thresholds` / `they re-seed at each level` | **REFUTED as the extract's compound dismissal** | Coupling-dependent cuts occur in the expositions (F2), and the extract's alternative has a summable tail (F3). Moreover the original paragraph concerns reseeding large-field action estimates, not constructing minimizers. ArXiv:1304.0705 §3.3, Lemma 13, (166)–(175), obtains a suppression factor from that level's action and characteristic function. A different induction constructing backgrounds does not refute this contextual claim. An exact 4D `φ_j∼g_j` identification is still NOT-VERIFIED. |
| B3-5, target :525–529 | `PROOF.md:901–903`, `dimensionless (\|\|1 - U_p\|\| ≲ p(g_k) g_k` | **NOT-VERIFIED for CMP 109** | The exact historical domain was not independently read. The wider link-cutoff form is supported in the QED analogue after normalization (F2), so cannot be dismissed as intrinsically incompatible with Balaban's method. Fixed background admissibility and a smaller integration cut need separate labels. |
| B3-6, target :530–532 | `PROOF.md:784`, `Balaban takes L sufficiently large` | **REFUTED: no contradiction was shown** | An assertion that L is an odd integer greater than 11 is compatible with choosing L sufficiently large. Its first possible odd value is 13. Fixing that L and then taking M large also creates no contradiction. The extract may replace vague wording by the precise assumed bound, but it has not refuted the original existence-of-a-large-L wording. This logical verdict does not certify CMP 109's bound from its original body. |
| B3-7, target :533–536 | `PROOF.md:685,926`, `is L1e's hypothesis` / `That is L1e's hypothesis` | **CONFIRMED, narrowly: not equality of domains** | Current PROOF.md :943–944 and :1036–1037 itself lists the additional divergence quantity J not controlled by the curvature-only statement. Bounded curvature need not bound its divergence: on spacing h, an abelian Cartan component `A_2(n)=a h(-1)^n/2` has discrete curvature of magnitude a but its discrete divergence has magnitude `2a/h`. For the corresponding commuting links, the sine-curvature and its divergence have magnitudes `sin(ah²)/h²` and `2sin(ah²)/h³`, giving the same separation as h tends to zero. Thus the second condition is independent of a curvature supremum. The original implication from a theorem on a larger domain need not be invalid. |
| B3-L, target :537–539 | Lead-file quotations as reproduced in the target; lead files were not separately read | **NOT-VERIFIED for their precise intended field/domain** | The general rejection of coupling-dependent thresholds is contradicted by F2; the exact lead-file claim and its intended cutoff cannot be settled by the reproduced sentence. No corrected lead-file status is fabricated. |

**Correct count at this review's scope:** of the eight proposed refutations, **2 have narrowly supported corrections, 2 claimed refutations are rejected, and 4 remain NOT-VERIFIED**. This is not a claim that only two underlying PROOF.md assertions can be false; it is the count the checked evidence warrants. The target's opening `6 + 2` versus later `7 + 1` was already explicitly corrected and is not a second scientific finding. B3-8 is a separate NOT-VERIFIED item, not a ninth member of the eight; its claimed contrary evidence fails as an absence test (F8).

**Citation drift — CONFIRMED; claim status PROVEN by string relocation and old-line inspection.** The old lines below were individually inspected after locating their strings. They no longer contain the claimed quotation. These are current local-file locations, not a universal offset to apply elsewhere:

| Item | Extract's old PROOF.md line(s) | Current line(s) |
|---|---:|---:|
| B3-1 | 1000 | 1032 |
| B3-2 | 6707 | 6740 (quotation begins 6739) |
| B3-3 | 1345, 1347 | 1377, 1379 |
| B3-4 | 4367–4368 | 4399–4400 |
| B3-5 | 870 | 902 (sentence begins 901) |
| B3-6 | 752 | 784 |
| B3-7 | 653, 894 | 685, 926 |
| B3-8 (separate item) | 5288 | 5320 |

### F11 — Symbol, quantifier, and decidability audit

**Verdict: CONFIRMED for the distinctions and algebraic tests stated here; NOT-VERIFIED where specified. Claim statuses: PROVEN / CONDITIONAL / OPEN as indicated.** Attachments: `BALABAN_EXTRACT.md:143–171`, `:212–239`, `:258–282`, `:443–467`, and `:579–595`.

| Symbol/object | Exact identity used in this review | Consequence |
|---|---|---|
| `ε_0, ε_1` | Target :143–146/:274–275: purported CMP 109 background and fluctuation radii. Goswami text :254–255: variational-domain and coarse-data radii. Dimock 1512 text :2179–2187: a fixed exponent margin ε in a coupling-dependent complex domain. | They are not interchangeable constants, even when named identically. No inequality between the sigma-model B₃ or radii and Yang–Mills radii has been accepted. |
| `γ, γ_k` | Target :275 versus :279: logarithmic cutoff scale versus allowed coupling bound. Dimock decay γ is a third object. | F3's limit requires specifying `t=(K-k)log L` and terminal `g_K`; it cannot use the coupling bound γ in place of γ_k. |
| `C` | Dimock 1108 §2.4 text :533–547 permits changing C and explicitly adds α-dependence for (81). | The extract's literal `depending on L, but no other parameters` at :219 is **REFUTED when applied to the Hölder estimate**: the supported label is `C(L,α)` for fixed α, still independent of k and volume. No equality of successive printed C's was used. |
| `M, κ, B_3` | Target :587–595 separates geometry, norm constants, polymer decay, and penalty strengths. Goswami (98) uses its own propagator decay and a regularity constant; F6's κ_i are positive penalties. | Large geometric M does not mean a large lane norm constant; increasing a penalty is not increasing a polymer decay rate. B₃ in the sigma model is not a numerical value for CMP 102. |
| `k, j, η` | Dimock k counts coarse-graining; current PROOF :1376–1378 uses resolution j in the opposite direction. Target :580–582 distinguishes fine spacing `η=L^{-k}` from lane displacement η. | All summability calculations here use n=K−k explicitly. A bound on spacing cannot be substituted for a bound on displacement. |
| `p_0` | Dimock's integer exponent in `p_{0,k}=(-log e_k)^{p_0}` differs from a level-zero value `p_0=p(λ_0)` in scalar notation. | The ratio test below uses the exponent, not the initial cutoff value. |

The decisive gates have these actual failure conditions:

1. **Source-omission/conditional-theorem gates:** cannot decide historical nonexistence. Countermodels are given in F1/F8. The same-model lane transcription cannot independently authenticate the inaccessible primary theorem. **GAP.**
2. **Random-walk gate:** needs `b C_loc(L,α)/M<1`; failure of a uniform local bound cannot be repaired merely by calling the cube finite (F4). **PROVEN implication, missing nonabelian input.**
3. **Goswami's self-reproducing B₃:** §3.4, (98), really states an induction carrying B₃ and the condition `B₃ exp(-2κM)≤1/2`; it does not multiply B₃ by itself at every step. The actual test is `2κM-log B₃(M)≥log 2`, together with `B₃(M)ε_1≤ε_0`. Since (98) defines B₃ using M-dependent regions and pre-existing propagator constants, one must bound that expression and choose ε₁ compatibly after M is fixed. No numerical closure, uniform SU(N) constants, or primary CMP theorem has been checked here. **ARGUED architecture; CONDITIONAL closure.**
4. **Nested-domain cutoff gate:** `C p_{0,k}/p_k≤1/2` means `-log e_k≥(2C)^{1/(p-p_0)}` for `p_0<p`. With `e_k≤e_K`, it is enough to impose this at the largest allowed coupling e_K. It could fail for a changed exponent ordering or an uncontrolled terminal coupling. The d=3 sources impose small terminal/bare input coupling; their test is not a tautology. **PROVEN conditional algebra.**
5. **Irrelevant level-sum gate:** setting `q=L^{-α}`, `Σ_{j=0}^{k-1}L^{-α(k-j)}=q(1-q^k)/(1-q)` for α>0. At α=0 it equals k. The extract's larger bound `1/(1-q)` is valid. A common background alone does not create α>0: `Σ_{j<k}F(U)=kF(U)` is a counterexample. Normalization/subtraction and an actual scale gain are indispensable. **PROVEN conditional algebra; original 4D hypotheses unverified.**
6. **Cauchy gate:** fixed norm bounds and domain margins must precede the derivative comparison, and must apply to the correct composite/tower object (F9). **CONDITIONAL.**
7. **Hardness gate:** a hard delta constraint, a small-field indicator, and a finite soft Gaussian penalty have different functions. The scalar soft inverse and the finite-a auxiliary gauge inverse in arXiv:1512.04373 §3.2–§3.3, (188)–(195), disprove any universal claim that a hard delta is necessary for a uniform linear inverse. They do not prove the nonlinear SU(N) soft chain has the corresponding bounds. **CONFIRMED limited comparison; full BAL-F2 OPEN.**

No decisive check script is specified or executed by the extract: its :42–44 explicitly declines a numeric check. References to unrelated lane diagnostics are not silently treated as validation and were not opened outside the read budget. The historical level coefficient `≈25(k−1)` at :443–444 is **NOT-VERIFIED** here. Current PROOF.md's string `The pre-repair coefficient is (121/13)(k−1)` conflicts with it, but that header is not a derivation; the extract itself :697 admits not re-deriving 121/13. Neither number is banked by this review, and no fabricated numerical correction is offered.

### Pre-stated exact-arithmetic validation — 2026-10-29 03:29:47 UTC

Before the following small plain-Python check: (i) the two-step soft elimination with Q₀=3, Q₁=2 and κ₀=κ₁=1 must give coefficients `(18/5,-6/5,1/10)` for `(x²,xB,B²)`; (ii) the nonlinear hard-source counterexample must have value -1/2 at (-1,±1) versus 0 at (0,0); (iii) the scalar soft-coefficient recurrence must agree exactly with its geometric-series formula. Any mismatch blocks the associated algebraic validation. These are checks of reviewer derivations, not evidence for a Yang–Mills theorem.

**Validation result: CONFIRMED at the stated scope.** The initial `python` launcher was unavailable, so no check ran on that attempt. Re-running with `python3` and only `fractions.Fraction` returned the three polynomial coefficients exactly, value `-1/2` at both nonlinear constrained minima, and exact recurrence agreement for `L=3,13`, `k=1,…,8`. The general derivations in F4/F6/F7, rather than this finite recurrence check, supply the quantified algebra. No floating-point arithmetic, numerical library, file-producing script, or long job was used.

## Corpus coverage and limits

The following are the substantive inspected passages, not claims to have read every paper in full. Local text extractions, found by string and read in bounded ranges, supplied the mathematical content. Official arXiv abstract records for 1108.1335, 2204.07201, and 2204.08252 were also checked for model/title/provenance. No original CMP body, lane literature notes, snapshot, audit ledger, or third additional repository file was read.

| arXiv ID | Inspected section/equation anchors | Bearing on this review |
|---|---|---|
| 1108.1335 | §2.4 (79)–(100); §3.1–§3.2 (106), (109)–(113); Appendix D (340)–(348), (367)–(370) | Soft scalar inverse, genuine uniform coercivity, walk convergence, coupling-dependent small fields. |
| 1212.5562 | Introduction's repeated large/small splits; §3.3 Remarks 2–3, (222) | Moving cutoffs; canonical coupling scaling; explicit omission of the additional R-operation needed in Balaban's other models. |
| 1304.0705 | §3.3 Lemma 13, (166)–(175), remarks (182)–(183); Theorem 2 and stability corollary (221)–(226) | Per-level action supplies fresh large-field suppression; partition-function stability and an uncompleted correlation-function extension. |
| 1410.2798 | §3.5–§3.8 (83)–(88), (105)–(110), references [5]–[9] | Hard abelian gauge constraint, coercivity on the specified slice, fluctuation covariance versus auxiliary inverse, direct CMP 99:389 pointer. |
| 1502.02946 | §1.1, §1.3 (18)–(20); §5.3 (218)–(228) | Scalar QED3 with no marginal charge renormalization; coupling-dependent real and complex domains. |
| 1512.04373 | §3.2–§3.3 (186)–(197); §4.2 (286)–(287); §6.1 (395)–(397) | Finite-a gauge auxiliary inverse, hard fluctuation covariance, distinct background and fluctuation cuts. |
| 1712.10029 | Introduction; §3.7.1 (281)–(290); §3.9 Theorem 1 (327)–(332) | Weighted multiscale gauge regularity and induction; no unweighted all-level-source conclusion. |
| 2009.01156 | §2.1 (7)–(9); §2.2 Proposition 1 (28)–(30); §2.3 Theorems 1–2 (37)–(42) | Actual counterterm/polymer flow and its conditional use; QED3 stability, not 4D Yang–Mills AF. |
| 2204.07201 | §1 Theorem 1 and source/volume discussion; §3 (14)–(19); §4 (20)–(24); §5 (53)–(56), (71)–(74) | Coupling-dependent moving cuts, compositions of minimizers, finite-volume scope, and separate dynamical-flow argument. |
| 2204.08252 | §1.5 Theorem 1 (27); §3.1 (36)–(39); §3.3.1 (59)–(74); §3.4 (98)–(100); §4 (101)–(104) | Fixed sigma-model variational radii; nonlinear constraint linearization; self-reproducing induction; analyticity. |

## Summary table for the five requested targets

| Target | Supports | Contradicts / fails | Unsettled | Verdict / claim status |
|---|---|---|---|---|
| **(a) Thresholds and non-compounding** | Soft composite inverse estimates; local coercivity plus walk convergence; weighted norms; induction with a fixed target constant; geometric sums once a positive scaling gain is proved. | Universal fixed-threshold account; fixed-finite-cube shortcut; all-regime cubic cutoff and unchanged nonsummability inference; absolute no-iteration account. | Exact nonabelian CMP domains and bounds, and admissible use of a different cutoff in this lane. | **CONFIRMED** for limited mechanisms; **REFUTED** for identified inferences; 4D transfer **CONDITIONAL/OPEN**. |
| **(b) Coupling flow** | The checked d=3 theories have canonical charge/quartic scaling and separately controlled counterterms. No verified 4D marginal-flow import was obtained. | Inferring historical nonexistence from a conditional stability theorem or a review's silence; inferring a one-loop coefficient from two-sided bounds. | CMP 119/122's exact contents, the deferred theorem, SU(N) scope, coefficient, and actual small trajectory. | Negative inference **REFUTED**; historical claim **NOT-VERIFIED**; needed 4D result **OPEN**. |
| **(c) Wall map / §7.7** | Useful paper pointers and conditional analytic route. | Background dependence alone destroys soft Gaussian composition; a linear hard-source identity automatically settles nonlinear source rows. | Actual slice/norm/domain matches and all uniform constants. | Pointers **CONFIRMED** narrowly; closure **NOT-VERIFIED / OPEN**. |
| **(d) Eight refutations** | Two narrow corrections: CMP 99:389 pointer; curvature-only domain is not the two-clause domain. | Two refutations as argued: B3-4's compound dismissal and B3-6's alleged large-L contradiction. | Four original-paper/lead-domain attributions. | **2 CONFIRMED narrowly / 2 REFUTED as review verdicts / 4 NOT-VERIFIED**; eight bankable refutations is **REFUTED**. |
| **(e) BAL-F2** | Hard linear absorption and soft data shift; uniform soft scalar and finite-a abelian auxiliary inverses. | Necessity of a hard delta for all uniform inverse estimates; automatic nonlinear hard absorption; exhaustion by exactly two soft walls. | Whether this particular nonlinear SU(N) scheme has a uniform inverse and closes its source estimates. | Linear facts **CONFIRMED / PROVEN**; general necessity rejected; actual BAL-F2 **NOT-VERIFIED / OPEN**. |

The six entries in §7.7 should consequently be read as follows:

| Wall | Bankable disposition |
|---|---|
| (GAP-Z) | CMP 99:389 is the relevant nonabelian propagator pointer. No theorem with the lane's composite Hessian, covariant slice, and norms has been verified. |
| (G♯_0-field) | Abelian regularity is directly visible in 1712.10029 Theorem 1. A matching all-level-source estimate still needs the weighted-domain-to-chain bridge. |
| (N-bg)/(H-C) | Conditional Cauchy consequence only after uniform input radius, action norm, and branch identification are supplied. |
| FLOW's unconstrained fine inverse | Distinguish constrained from unconstrained operators; an instability of the latter does not by itself refute the former. For example `K=diag(-1,1)` is positive on `ker Q` for `Q=(1,0)`, and `K+2Q^TQ=I` is positive as well. This elementary comparison supports investigating either constraint strategy, not a claim that the actual 4D Ward/flow route is complete. |
| (SPD)/(W2) | Exact linear top-range absorption is verified. Its nonlinear coordinate/source identification and the norm estimate are unverified. |
| Level-count factor | A positive scale gain sums; same-size contributions need not. The cited old numerical coefficient is not independently verified, and changing to a hard scheme does not automatically remove multiplier terms. |

**Closing receipt — 2026-10-29 03:42:14 UTC.** Eleven findings, all five requested targets, and all eight advertised refutations are addressed. Final table-delimiter validation succeeded. The target's observed size/mtime remained 68,728 bytes / 2026-10-28 23:30:49 UTC; PROOF.md's final observed size/mtime was 738,959 bytes / 2026-10-29 03:21:13 UTC. String locators control if lines drift later. Only `CODEX_REVIEW_BALX.md` was written; no git command was run.

## Exactly what may be banked

1. **PROVEN here:** the finite-a scalar coefficient bounds and coercivity mechanism under their stated Poincaré/normalization hypotheses; the conditional geometric/walk sums; the general frozen-linear Gaussian composition identity; the linear hard-source identity and corrected soft shift; the counterexamples to the extract's broader inferences; the finite-scale correction and conditional summability in F3. The arXiv uniform derivative/regularity statements are source-verified at the stated scalar/abelian scope, not independently reproved in their entirety or imported into 4D SU(N).
2. **CONFIRMED source distinctions:** the accessible Balaban-method expositions do use coupling-dependent integration domains; these coexist with fixed deterministic regularity radii. They employ both compositions/induction and direct uniform bounds. The missing CMP 99:389 reading pointer and the weighted-supremum structure of Dimock's gauge regularity theorem are supported. No quoted source supports identifying their constants or domains with the lane's by name alone.
3. **CONDITIONAL planning facts:** Cauchy estimates and irrelevance gains are valid mechanisms when their independent hypotheses hold. The wall map is a guide to missing matches, not a list of imported proofs. No new PROOF.md claim status, 4D marginal-flow theorem, nonabelian inverse estimate, nonlinear level-count closure, infinite-volume limit, or correlation-function construction is banked.

**Single most dangerous unverified item:** a k- and volume-uniform inverse bound for the **actual nonabelian composite Hessian on the lane's gauge slice in its source norms**, including curvature and residual/multiplier terms. Scalar/abelian uniformity and linear hard-source absorption do not supply it; assuming they do would silently promote several wall-map entries at once.
