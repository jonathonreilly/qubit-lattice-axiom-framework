# FCON pass 2: source checks

Provenance: Codex, 2026-11-05, checkout `c8dab7974ace28516f8ac295f7baaedaba923ef7`; distillation of Claude's complete 491-line `library/fcon-draft.md`. Research text, not an audit or referee report; grants no status. Exact serving model identifier and effort setting are not exposed. Mathematical checks are written arguments, not runs.

Verdict on the inference in draft Remark 3.4′(3): **WRONG**. ST1 L1450 does not identify the declared precision, so the unconditional actual mean-match claim is not established by this argument; no counterexample to matching is claimed. The exact split is **CORRECT-NO-ADVANCE** as bookkeeping until actual-family identification is supplied. CV gauge equality, zero first variation and the gauge-indicator implication survive with the hypotheses in the manuscript. OT remains Outstanding; no admitted-history counterexample is established.

## Source identities and method

The supplied scope was respected: this checkout and named scratch files under `/tmp`. No home-directory or whole-`/tmp` search was used. The requested `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this pinned checkout. GOAL.md and the requested FINISH.md instructions were read first. No audit, backlog drain, subagent, computation, commit, push or public post was performed. Filesystem hashes and inventories certify source identity only.

All upstream texts are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, at `31a47c543775`. The background and stage methods also credit Tadeusz Bałaban; library flat-propagator imports credit Jonathan Dimock.

| File | Local copy, fetched successfully once | SHA-256 |
|---|---|---|
| [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) | `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex) | `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex) | `/tmp/fcon-pass2/sa_ca_II.tex` | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex) | `/tmp/fcon-pass2/sa_ca_III.tex` | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |
| [YM3-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex) | `/tmp/fcon-pass2/sa_YM3_I.tex` | `248959db554e4678aa88e92c9fe98372cd54b45719bb70bf43c47547d0c9f443` |

The draft's SHA-256 is `c2d0ed5336b780d45de2dd3cbe0f10a4b8637d68f92737d48d4ee250345377b3`. The outline index README, matching rows and neighbours in chunks 05, 07, 09, 10, 12 and 16, and matching entries of obligations.md guided the outline reads. The CA index README and chunk 10 guided the stage-formula and stage-theorem reads. These indexes describe source status; they do not verify a theorem. Some initial batched outputs were truncated; only visible or subsequently re-read excerpts are used below. No upstream file was read whole. CA-II supplies no quoted statement or mathematical premise here.

Bounded source excerpts used below are preserved in `/tmp/fcon-pass2/verified-excerpts.txt`; the recovery checkpoint is `/tmp/fcon-pass2/current-checkpoint.md`.

## Upstream line checks

| Source range checked | Content and disposition |
|---|---|
| SA 6015–6038 | Frame couplings, test radii and waiting depth. Frame and actual action coefficients are distinct. ST1 Tq0 is its explicit adaptation. |
| SA 7165–7195, especially 7178–7183 | Soft gauge uses contour means, a real-part trace, and an indicator. Missing means are excluded by the insertion convention. CV supplies a defined mean on each moved admitted block; it does not establish gauge coverage everywhere. |
| SA 8002–8053 | Quantitative mean contraction, holomorphy, trace-zero preservation and endpoint covariance on a common branch. The source gives a detailed local argument. The Lipschitz estimate is used through the frozen AV/CV input on a smaller ball. |
| SA 9667–9684 | Mean and comb representatives are distinguished. The profile is depth/geometry uniform with constants that may depend on the fixed blocking factor; these lines do not give the quantitative contraction required by OT. |
| SA 11204–11247 | The next-fibre chain rule retains the constraint-curvature multiplier. The gauge gradient vanishes at the physical axial locus. This supports equality of the gauge contributions there, not identification of every later stored marginal. |
| SA 13904–13971; 14091–14120; 14159–14195; 14207–14217 | FG defines the covariance \(D=C+C\Gamma\Gamma^{\mathsf T}C\), its normalized density and auxiliary representation. The regular-step precision and physical Hessian identification are stated with their operator/current hypotheses; the latter argument is sketched. Local compression, independent root decoupling and the physical marginal are different constructions. The source expressly excludes an assertion of a Gaussian law for the full nonlinear disintegration. |
| SA 17315–17404 | The three main tests, collar/rim mean control, and Lemma 2.2's old-test implications. The latter are a sketch using the specified supports and margins. L17396 includes approximate-fluctuation tests, beyond the draft's isolated type-(58) class. |
| SA 17433–17453 | Persistent marks, their disjoint windows, and localization/complete-read requirements. Supports, not merely a stage number, determine which frozen factors are independent. |
| SA 17497–17566 | Stored variables, strip substitution, conditional Gaussian, carried kept form and background differences. L17531 is the displayed stored operation; L17534 puts the Wilson weight in the action it acts upon. L17558 states carriage and the separate positivity problem for a truncated kept form. The small stage-difference estimates at L17564 are sketched, not proved here. |
| SA 17575–17588 | The class uses (t_\flat=t-N_t); stages are (j=t_\flat,\ldots,t-1). This settles the flagged range in draft Lemma 4.3. It is unrelated to the shorter compression count (N_t^0). |
| SA 17612–17630 | The graded curvature thresholds and their margins are part of this source's stage design. The argument is sketched and has an interior-versus-boundary qualification. It is not a proof of old-test redundancy for the changed ST-test. |
| CA-I 54280–54318 | The action split and two Gaussian integrals have explicit different forms and normalizers. The integral formula cites Bałaban (1.60); it is not a new proof of matching the intrinsic SLOT-ST presentation. |
| CA-I 54985–55005 | The boundary theorem explicitly assumes the stage theorem, profile-class hypothesis and integration structure. No omitted stage theorem is imported as a proved conclusion here. |
| CA-I 74300–74324 | Collar and rim integration variables are distinguished. GS/SLOT-ST retains the actual correspondence as a premise. |
| CA-III 111381–111402 | Its inventory marks several stage/domain/continuation proofs incomplete. This is provenance information only; it is not proof that a statement is false or absent elsewhere. |
| YM3-I 3633–3647; 31514–31577 | Bilinear trace pairing, relative logarithmic gauge derivative, pivot elimination and the supplied off-critical precision. These justify the attribution and conventions of descent's relative form; no three-dimensional bound is silently transferred. |
| YM3-I 52091–52134 | Fixed-boundary bump contour, Jacobian, and the requirement that failed Borel coordinates remain fixed. The finite-dimensional method is rebuilt in ST1 FC9 and used conditionally in FCON. |

## Library and draft checks

Relevant changed arguments were read in full. The complete pass-1 draft was read. For frozen inputs, the complete statements and relevant premises/proofs were inspected in bounded ranges: ST1's imports/order, formation (56)–(58), Lemma 12/F1–F7, FM3–FM5 and Theorem FM, CV and FC3–FC9, Theorem FC, Theorem 14/Corollary 14′, and Amendment GS; geoh Definition 5/Lemmas 9–10; descent's definitions, Lemma 2 and actual-formation qualification; CP12's D1–D3 and Theorem 3; DR Theorem 4 and its result; F-meas imports and corresponding source/matching limits; DOM's membership and LOC proposals; IN1's H-M, H-E and constant order; NL1-L Theorem 7 and (18); CI-form H-G/H-S; hm's imports, physical marginal identity and stage limitation; pr-lay (6)–(9); shift-map §14; a3-profile's constants and profile proof; p82's contour definition and gauge covariance; and the relevant ST1-r4 gate findings.

| Draft claim | Check and resulting manuscript location |
|---|---|
| Lemmas 2.2, 3.1, 3.2 | Geometry and exact CV mean checked. The absolute and relative-trace functions agree on the whole common branch; their Hessian is descent's Y3 form. Zero first variation does not require complete gauge coverage. Lemma 1. |
| Lemma 2.3 | Constrained averages and retained independent rows are fixed at fixed datum. This alone says nothing about Borel dependence on analytic components of that datum. D3 and Lemma 6. |
| Lemma 3.3′ | Exact exponent identity checked term by term. The global product-near-one justification was invalid; FMd uses local trace logarithms. Lemma 2 and (5). |
| Theorem 3.4/Remark 3.4′ | Algebraic Gaussian choice is valid. Unconditional actual matching is not proved. Frozen NL1/LF1 does not specify that chosen matrix at every stage; G-ID, normalization, marginal and formation qualifications remain. Theorem 4 and its Outstanding paragraph. |
| Proposition 3.5/Corollary 3.6 | Sign and row-sum estimate checked. Recentring does not localize (S) or identify all pivots with (V^\sharp). The (b/16<b_j/16) comparison is valid. Lemma 3 and Theorem 4. |
| Proposition 3.7 | Cauchy/inverse bound holds for the displayed linear truncation. It does not control the full quadratic or nonlinear saddle, or provide a volume/rim-uniform bound. Lemma 3. |
| Lemmas 4.1–4.2 | Real trace equality and holomorphic continuation checked; path telescoping, branch room and the gauge threshold verified by hand. Lemma 5. |
| Lemma 4.3 | Stage range resolved from SA17575/17585. Use all birth-level test data and locality, not just failed free rows. Analytic-datum dependence is separately qualified. Lemma 6. |
| Lemma 4.4 | Haar/strip/composition arguments hold under their chart, source and target-domain premises. Earlier outputs require earlier FC-test and majorants, so induction must use prior structures. Discussion after Lemma 6. |
| Theorem 4.6/Remark 4.7 | Complete factor coverage was not established; old approximate tests must be accounted for. Outer domination is separate and includes all prefactors. Theorem 9 and its adjoining qualifications. |
| OT and attacks | Telescoping proves sufficiency only. Profile lacks the required (L)-comparison, inherited thresholds and seam estimate. Graded design creates a new failing outcome. Indicator splitting leaves a correction integral. No actual history realizes a counterexample. Lemmas 7–8. |
| Theorem 5.1 and constants | Conditional contour implication retained with all preceding obligations. Distinguish (Z)-tube from its image in the (\beta)-tube. All new structural constants remain early; smallness tests are final coupling ceilings. D4 and Theorem 10. |

## Proposed corrections to frozen texts

FC5 L1221: its premise is proved for the moved level-\(j\) pairs, so its conditional assertion is correct; no error in the frozen theorem. L1218: trace is the correct holomorphic extension of SA's real-part trace on SU(2). L1431–1432: wording should assign the zero linear term to the function, not its Hessian. Assembly-status's FCON → CI edge is valid as an indirect edge through actual formation/contour identities; NL1-L L565 explicitly names these identities. The draft's claim of no contour occurrence was not reliable. No frozen text was edited.

The draft's LOC-flat/K-flat naming remark concerns its former task brief. This checkout's DOM draft calls the unresolved statement LOC♮ and the class \(\mathcal K^\natural\); no claim about a newer checkout is made. The frozen F5 radius comparison is correct. The gate correctly includes the soft gauge indicator within FC-test.

No statement in this record upgrades an imported theorem or assigns retained status. The distilled manuscript remains **not yet refereed**.
