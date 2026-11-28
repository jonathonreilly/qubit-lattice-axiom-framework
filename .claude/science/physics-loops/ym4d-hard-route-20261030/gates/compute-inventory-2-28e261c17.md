Lead note: this report reads both attempts, so each attempt gets only its own section. Bounded, as it says. I read it in full and did not recheck each row at its source.

Provenance: OpenAI GPT-6 / Codex; effort not exposed; source commit 28e261c1726d3afc037eb4e1255b32968f66806e. Mathematical inventory of research-stage text, not an audit; grants no status. Paths and quoted line numbers are relative to this target. No claims supplied from memory.

## Mapped attempt

No additional **PREMISE** row established in the seven library notes explicitly linked in the current State of attack (`parts/hard-core--mapped.md:10–44`). The first pass's staircase and retired contraction rows are not repeated.

Other classifications, grouped by mathematical assertion rather than run: **EVIDENCE 2; ABANDONED 1; undecided 2.** Evidence means the run is supplementary to a displayed argument, not that this inventory certifies that argument. In particular, the undecided count is not included in EVIDENCE: the written stability and nest-coercivity arguments invoke unresolved analytic estimates; their finite tests do not discharge those estimates. I could not decide from these reads whether the current conditional route relies on those tests for any additional conclusion. The literal old flux-threshold route is explicitly withdrawn.

No additional row established in the three requested formalization-gap categories. This does not clear the explicit gaps in (LIFT-1), (Resp+) with lower layers, REST beyond first order, or END. Those are named open obligations, not automatically one of the three requested categories. The order of choice explicitly permits c_S to depend on L and a_* before x_* is chosen (`parts/hard-core--mapped.md:24`; `library/energy-by-stages.md:152–162`); dependence alone is not a constant-order defect.

## Independent attempt

No additional **PREMISE** rows. **EVIDENCE 0; ABANDONED 0** additional numerical assertions in the three newly read analytic/cluster libraries. These zero counts mean no runs were invoked there, not that the lemmas are certified. The already adjudicated box-gauge shelling is excluded.

Requested formalization gaps (literature inputs, not numerical premises):

| File:line | Statement name | What the gap supplies | Consumer | Hand-proof route |
|---|---|---|---|---|
| `library/lattice_gehring_hls.md:11,39` | Lemma 1 maximal inequality; Lemma 3 Gehring stopping cover | The Vitali covering lemma supplies disjoint balls and fixed dilations covering the level set. The finite selection argument is invoked, not rebuilt; the adapted intrinsic balls also require its metric/dilation hypotheses. | Lemma 2 HLS and Lemma 3, then Lemma 4.5h's Morrey estimate (`parts/hard-core--independent.md:520–528`). | **Unproved here:** order the finite candidate balls by radius, select greedily, prove containment of every rejected ball in a fixed dilation, and state the enlargement/volume bounds for adapted balls. |
| `library/ultralocal_cluster_expansion.md:64–68,78,88–92` | Decay of H^# and labelled majorant | The maximum/Schwarz principle (also asserted for Banach-valued functions) and multivariate Cauchy coefficient bound supply decay and absolute coefficient control. Their applications have displayed estimates, but the analytic theorems themselves are not rebuilt in this library. | Scalar gas expansion and the labelled output e(Y,R;W), explicitly used at `parts/hard-core--independent.md:840,907–908`. | **Unproved here:** give the contour integral coefficient bound on smaller polydiscs, pass to the radius limit, and derive the vanishing-order bound by scalarization or a Banach-valued Cauchy integral. |

The path-expansion note displays its Neumann and alternating-sum arguments (`:19,29`), rather than importing Balaban/Dimock as a substitute for them. I did not certify the loss of rate hidden in “adjusting eps” at `:29`; `:39` itself requires eps smaller than merely 1. This is an unresolved estimate/statement issue, not a run or an established constant-order cycle. The animal count in the cluster setting (`:7`) is also asserted without its counting construction; it is not machine enumeration, and I found no basis to call it a numerical premise.

## Upper chain

**PREMISE (one additional, consumed negative example).**

| File:line | Statement name | What the run supplies | Consumer | Hand-proof route |
|---|---|---|---|---|
| `parts/upper-chain.md:1236,1345` | F20.1 / C4 signed-activity cross-ratio counterexample | The asserted positive two-state example with small interaction mu=10^-3 but log cross-ratio about 1.25 is supplied by the run. Neither the signed weights nor the four partition sums are printed. The independent logical observation that an upper activity bound gives no denominator lower bound does not need this numerical example. | The retained explanation for withdrawing the signed-factorization proof of Proposition 17.5 (`:1110,1234–1242`), and choosing the positive-measure route. This is a premise of the quantitative counterexample, not of Lemma 17.1 or a positive theorem. | **Unproved:** print rational signed weights and four positive partition sums; verify their cross-ratio exceeds a loose rational threshold, using elementary bounds for the exponential/logarithm. Alternatively retain only the missing-denominator objection. |

Other classifications of additional grouped assertions: **EVIDENCE 5; ABANDONED 6; undecided 2.** ABANDONED here includes old numerical values that the current interface does not consume, even when retained as motivation. The fitted lift constants and the claimed sharp Gaussian L^-4 rate do not set the current GS input: Lemma 18.5 instead displays an L^-2 argument (`:1166–1174`), while the interface still asks a producer to supply GS (`:181`). Trials of an open clause are not its discharge. Two toy/sketch comparisons (`:319,1347`) could not be certified as independent written proofs or identified as additional numerical premises; they remain outside EVIDENCE. First-pass rows and counts for Texts 20–21's three lemmas/profile and Text 23.5's nest objection are excluded.

Requested formalization gap:

| File:line | Statement name | What the gap supplies | Consumer | Hand-proof route |
|---|---|---|---|---|
| `parts/upper-chain.md:315–317` | Theorem 4 continuum massive-Green asymptotic | “The standard convergence of the lattice massive Green function” supplies the displayed Bessel-kernel limit; no limiting estimate is given in the proof. The finite-torus Gaussian identities (a)–(c) do not depend on it. | The claimed a^-4 separated-correlator size, the constant-coupling obstruction retained at `:1080`, and the bounded-family discussion at `:319`. | **Unproved:** specify the volume limit/order and separated-point domain, use a heat-kernel or Fourier representation with a uniform integrable remainder, and derive the continuum kernel. The clipped family's pressure estimate at :319 remains separately only a sketch. |

No new constant-order defect established. The failed shell-grid tests explicitly restore the floor condition and choose gamma after l_1 (`:1116`); a failed earlier parameter choice is not a current circular choice.

## Witness

No additional **PREMISE** row established. **EVIDENCE 8; ABANDONED 4; undecided 1** additional grouped numerical assertions (the undecided item is the uniform blocked-map assertion around `:770–795`, discussed below). The two free-value/trend premises and symbolic plane-wave identity of the first pass are excluded, not cleared. The current local correction at `parts/witness.md:1440` now calls the free input a gap; older checkpoint wording at `:34–36` still says discharged. This is a source-status mismatch already covered by the first pass, not a second new row.

The rectangle's choice of D is by the asymptotic nonvanishing argument, not by the printed D=3,5 values (`:395–407`). The 48-choice rank argument displays its block reduction and averaging count (`:546–562`); “also checked by machine” at `:853` is supplementary to that argument, not its exhaustion step. The finite-beta Monte Carlo conclusions do not discharge the current all-scale NT2 clauses. The text's reference to tensor-rank bounds at `:503` is explicitly **source-author memory** (“recalled”); it motivates a failed route and supplies no result in this report.

Requested formalization gap:

| File:line | Statement name | What the gap supplies | Consumer | Hand-proof route |
|---|---|---|---|---|
| `parts/witness.md:776–780` (statement `:770–774`) | Lemma 5.4, uniform blocked rectangle estimate | The transfer “Steps 1 and 2 of Lemma 3.4 use reflections and Lemma 3.3 only” leaves the uniform control of the nonlinear quadratic form A~ of the iterated map undisplayed. Linear blocked-current mass/decay does not itself supply the required second-jet bound. The displayed inverse-sixth-power assertion at :776 has no depth-uniform second-jet estimate underneath it here. | Theorem 5.5's conditional comparison-class route (`:797–804`) and the proposed blocked tree input. The current H-TREE remains explicitly open (`:960–961`); this is not a finding of a numerical proof or a disproof of the rectangle conclusion. | **Unproved:** bound the iterated second jet in a norm compatible with the Ward cancellations and the spatial tail sums, then redo the two remainder sums with constants uniform in depth. `library/witness-blocked-tree-limit.md:188–209` explicitly gives the jet recurrence and leaves its needed control open. |

No additional constant-order defect established. In particular the historical L=150 is qualified as a leading count, while the actual statement chooses L sufficiently large (`:576–578,856`); this inventory cannot turn that into a certified finite threshold. The omitted boundary dimension estimate remains unresolved, but is not a numerical run or one of the selected shorthand/literature rows.

**What was read and not read; scope and recovery.**

Source identity: HEAD was checked at the beginning and end as `28e261c1726d3afc037eb4e1255b32968f66806e`. The requested `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent. No substitute workflow, audit or gate procedure was invoked. Read GOAL's “No computer-assisted steps,” FINISH's “Keeping the two attempts independent” and “Rules,” and the complete first-pass report, including its coverage limitation. Initial broad outputs that truncated were replaced by bounded reads for the arguments adjudicated here; unseen search output is not evidence.

Search: the seven mapped State-of-attack library links, the three independent analytic/cluster libraries, and both consumer part files were searched for computed/numeric/enclosure/exhaust/enumerat/checks/, fit, trend, “to 1e-”, “by machine”, standard, similar and “same argument.” Additional targeted searches followed named consumers and rebuilds. False positives such as “standard white noise,” geometry that must “fit,” definitions computed symbolically on paper, and verification-manifest links are not runs. A statement saying “checked” is not automatically evidence: where the check supplies the proof rather than supplementing a displayed argument, it is PREMISE even if exact.

Mapped bounded reads (all paths under library/ unless stated): `energy-by-stages.md:45–80,150–185,194–196`; `active-energy-junction-cubes.md:1–38,91–221`; `paid-inputs-frozen-mesh.md:1–65` and its search hits; `paid-inputs-frozen-energy.md:156–205`; `excess-localized-competitor-stop.md:1–44,320–361`; `one-step-closure.md:1–20,125–144` (its already adjudicated :145–164 excluded); `quiet-boundary-rarity.md:20–47,295–309`. The current mapped checkpoint was read at `parts/hard-core--mapped.md:1–44`. Followed the scalar-tail dependency through `active-energy-response-tail.md:1–210`, and nest argument through `fibre-propagator.md:142–160`. Searches in analytic-lift and lattice-uhlenbeck were dependency identification only, not new certifications. Metadata/no-run hits and the ordinary word “fit” do not entail reading unrelated proofs in full.

Independent reads: complete `lattice_gehring_hls.md:1–59`, `path_expansion_locality.md:1–39`, `ultralocal_cluster_expansion.md:1–106`; consumer references in `parts/hard-core--independent.md`, especially `:520–528,638,655,709,840,890,907–908`. The previously adjudicated `lattice_sobolev_box_gauge.md` was not re-adjudicated; only targeted rebuild searches touched it. No proof from another attempt is quoted or used in the Independent attempt section.

Upper-chain bounded reads: `parts/upper-chain.md:270–320,347–359,544–557,645–666,706–754,1080–1182,1232–1242,1343–1347,1497–1537`, plus current interface and consumer search hits. Numerical sections previously adjudicated in the first pass were skipped. The counts group algebraic assertions and nonconsumed numerical value families, not every test code or parameter sample. The conditional law/producer gaps in Text 18 are preserved; its exact algebraic tests do not certify the current chart identification.

Witness bounded reads: `parts/witness.md:1–65,315–435,489–610,650–681,685–803,803–860,949–1006`, plus current-consumer and status search hits. First-pass reads of the Ward/plane-wave identities, corner coefficient, withdrawn RANK-U and free near/far enclosures/trend were not re-adjudicated. To check the current second-jet stop, also read `library/witness-blocked-tree-limit.md:1–45,188–218`; the moment-library search was only navigation. No claim that an imported result has no rebuild anywhere in the repository is made: the literature rows identify the missing rebuild in the inspected supplying libraries/proofs.

Not read: any `gates/history-budget-*`; other gate reports (apart from the requested first pass); scripts or numerical logs; external literature; full git history; every proof in every mapped library; or the entirety of the large part files. Gate quotations already embedded in source text were encountered as source text. Search-only references and named analytic hypotheses remain unverified. In particular this is a completed bounded follow-up inventory, not exhaustive proof verification: undecided assertions remain undecided, and absence from a table grants no status. The report adds **one PREMISE row and four formalization-gap rows**, with the computational row restricted to the quantitative negative example. It does not repeat or remove the first pass's findings.

Only this report was written, section by section. No numerics, audit, subagent, commit, push or post; no prompt or instruction file changed. All proposed hand-proof routes are unproved in this report.
