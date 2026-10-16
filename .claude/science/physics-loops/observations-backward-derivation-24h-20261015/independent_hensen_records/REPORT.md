# Independent fixed-selection Hensen record reproduction

PASS for the source-bound fixed-selection reproduction. No material discrepancy found. This is exposed-data development work, not a new hypothesis rejection, holdout, apparatus audit or formal scientific audit.

## Identities and source reading

Complete note SHA256: 97424be700a2c6a89ba00b7772ebf0805b4c3898d4b8a757844582b97e108f2c. Complete author runner SHA256: 88d1003f0b53e89dbad5a84d4ecddea29ceaeef5c80c6558a52669f928a1e9fa. Frozen identities are in frozen_sources.json; intake plan and original execution receipt are separately hashed. The original author output and source were verified unchanged after reproduction.

The exact archive SHA256 is c28eb0f075759aef620a0b2e00a70fd675ce712bc8214d11c103f5a3d29492c0; its 152913-byte size and MD5 match the note. All four member hashes were independently calculated and match. The complete README body, all 17 ODS column descriptions and complete deposited analysis-example source were read as untrusted source material. The original example was never imported or executed. Its commented parameter-scan examples were not followed. No raw archive/member was copied into this repository by this checker.

The deposited header describes a broader recorded readout range ending at 14620 ns; the original analysis example applies its narrower fixed 3700-ns window ending at 14320 ns. The reproduction correctly follows the latter, with strict lower and inclusive upper readout endpoints. Herald gates are lower-inclusive/upper-exclusive, channel-dependent, separated by 250000 ps and require distinct channels. The invalid-marker rule is exactly zero or greater than 250 on each side, and both specified early-excitation counts must be zero. These are adopted original selections, not recertified causal timing conditions.

## Independent implementation and results

Before inspecting the new author implementation, I wrote a separate column-based NumPy parser from the deposited header/example and used exact rational binomial recurrence for the three tails. The deposited code was not executed. The independent calculation gives successive counts 4746,361,248,245 and 196 wins. Every setting/outcome table entry matches the note and author output. The selected original-row-index digest independently matches e94aa6c1b0699d656eaf76475a19fcdbd5409a8a980553c2d37ef229211511e8; this checks selection identity and is not record-order exploration.

Computed S=2.4224998704613707 and the original descriptive error=0.20382659825201987 match. That error formula is descriptive and is not used to justify the adaptive-memory null. Unequal setting counts explain why the separately calculated game score is 2.4.

The original example explicitly uses q=.75+3*(tau+tau²), giving 0.03917464355879003. The stronger conditional-independent-input bound uses q=.75+tau-tau² and gives 0.039109972413714174. The ideal uniform case gives 0.03907767138965722. They are distinct null bounds, all rounded to .039 at the deposited reporting precision. No tighter conditional independence assumption was substituted into the deposited result. This calculation does not independently establish the physical validity of either calibration model or give a posterior probability of the broader network hypothesis.

## Exact author reproduction and execution record

After the independent count calculation I read the complete author runner, output, intake plan and receipt. The runner faithfully implements the deposited fixed predicates and labels, refuses a changed archive identity, and distinguishes all three win bounds. Running it with --output directed to this allowed directory gives exactly identical JSON, including runner/member hashes and selected-row digest. execution.json records the actual 120-second-bounded command and runtime. Independent commands and outputs are preserved in independent_execution.json and independent_selection_identity_execution.json, with the final independent_results.json retaining the identity check. No calculation failed or timed out.

Two initial source-display attempts produced truncated tool output because the raw data/RTF metadata were unnecessarily verbose. They were not used as evidence of complete metadata reading: the example/header were reread and the complete README body was rendered to text with a bounded textutil stdin conversion, which succeeded. No original analysis or metadata code was run. Only the checker and the inspected new author reproduction were executed.

## Scope disposition

The intake plan explicitly records prior exposure to the published N, wins, S, tau and significance summary before archive download. This work is therefore a data-to-counts reproduction against already-known results. No thresholds, labels, time segments, stopping rules or record order were searched; no network fit or new theory test was attempted. Timing closure, random-source characterization, herald causal ordering and latent conditional independence remain outside this reproduction. The note preserves those limitations and the distinction from its earlier frozen block08 intake.

No author artifacts, git state, publication or audit status were changed.
